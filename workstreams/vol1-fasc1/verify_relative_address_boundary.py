#!/usr/bin/env python3
"""Thirteen tiny source assemblies per two originals and audit correction.

No MMIX instruction execution. Decode only the documented MMO loader
records emitted by these three-line cases, to check accepted instructions.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

BASE=Path(__file__).resolve().parent
SOURCES,RESULTS=BASE/'sources',BASE/'results'
MOD=2**64
HALF=2**63
CASES=[
    ('known-bnz-cross-plus-one','BNZ',HALF-4,HALF,False),
    ('future-bnz-cross-plus-one','BNZ',HALF-4,HALF,True),
    ('known-jmp-cross-minus-one','JMP',HALF,HALF-4,False),
    ('future-jmp-cross-minus-one','JMP',HALF,HALF-4,True),
    ('known-bnz-forward-limit','BNZ',HALF-4,HALF-4+4*(2**16-1),False),
    ('known-bnz-too-far','BNZ',HALF-4,HALF-4+4*2**16,False),
    ('known-jmp-backward-limit','JMP',HALF,HALF-4*2**24,False),
    ('known-jmp-too-far','JMP',HALF,HALF-4*(2**24+1),False),
    ('known-bnz-top-wrap','BNZ',MOD-4,0,False),
    ('known-bnz-ordinary-backward-limit','BNZ',4*2**16,0,False),
    ('known-geta-cross-plus-one','GETA',HALF-4,HALF,False),
    ('known-pushj-cross-plus-one','PUSHJ',HALF-4,HALF,False),
    ('known-pbnz-cross-plus-one','PBNZ',HALF-4,HALF,False),
]
OPCODES={'BNZ':0x4a,'JMP':0xf0,'GETA':0xf4,'PUSHJ':0xf2,'PBNZ':0x5a}

def decode(data):
    assert len(data)%4==0
    words=[int.from_bytes(data[i:i+4],'big') for i in range(0,len(data),4)]
    i,loc=0,0; memory={}; records=[]
    def put(address,value):
        memory[address%MOD]=memory.get(address%MOD,0)^value
    while i<len(words):
        word=words[i];i+=1
        if word>>24!=0x98:
            put(loc,word);loc=(loc+4)%MOD;continue
        op,y,z=(word>>16)&255,(word>>8)&255,word&255
        yz=(y<<8)|z
        if op==0:
            assert yz==1;put(loc,words[i]);i+=1;loc=(loc+4)%MOD
        elif op==1:
            assert z in (1,2);v=0
            for _ in range(z):v=(v<<32)|words[i];i+=1
            loc=(v+(y<<56))%MOD
        elif op==2:loc=(loc+yz)%MOD
        elif op==4:
            put(loc-4*yz,yz);records.append(dict(kind='fixr',delta=yz))
        elif op==5:
            assert y==0 and z in (16,24)
            raw=words[i];i+=1
            delta=(raw&0xffffff)-(2**z if raw>>24 else 0)
            put(loc-4*delta,raw);records.append(dict(kind='fixrx',delta=delta,width=z))
        elif op==6:i+=z
        elif op==7:pass
        elif op==9:i+=z
        elif op==10:break
        else:raise AssertionError(('unexpected MMO record',op,y,z))
    return memory,records

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n 15.'
    env=dict(os.environ);env['CWEBINPUTS']=str(SOURCES)+':'
    rows,logs=[],[]
    result=dict(scope='Exact known/future relative-address boundary and range controls, no MMIX execution.',cases=rows)
    def checkpoint():
        (RESULTS/'relative-address-boundary.json').write_text(json.dumps(result,indent=2)+'\n')
        (RESULTS/'relative-address-boundary-build.json').write_text(json.dumps(logs,indent=2)+'\n')
    with tempfile.TemporaryDirectory(prefix='relative-audit-build-',dir=RESULTS) as tmp:
        build=Path(tmp)
        for version,date,change in [('original-2013','20131017','-'),('original-2025','20250620','-'),
                                    ('audit-displacement-first','20250620',str(SOURCES/'audit-relative-address-boundary.ch'))]:
            for cmd in [['ctangle',str(SOURCES/f'mmixal-{date}.w'),change,'mmixal.c'],
                        ['ctangle',str(SOURCES/f'mmix-arith-{date}.w'),'-','mmix-arith.c'],
                        ['gcc','-O0','-std=c11','mmixal.c','mmix-arith.c','-o','mmixal']]:
                p=subprocess.run(cmd,cwd=build,env=env,text=True,capture_output=True)
                logs.append(dict(version=version,command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));checkpoint();p.check_returncode()
            for name,op,source,target,future in CASES:
                definition=f'Target IS #{target:016x}\n'
                program=f' LOC #{source:016x}\nMain {op} '+('' if op=='JMP' else '$1,')+'Target\n'
                program=program+definition if future else definition+program
                (build/'case.mms').write_text(program)
                p=subprocess.run([str(build/'mmixal'),'-o','case.mmo','-l','case.lst','case.mms'],cwd=build,text=True,capture_output=True)
                displacement=(target-source)%MOD
                if displacement>=HALF:displacement-=MOD
                assert displacement%4==0
                k=displacement//4; width=24 if op=='JMP' else 16
                legal=-2**width<=k<2**width
                expected=((OPCODES[op]+(k<0))<<24)|(0 if op=='JMP' else 1<<16)|(k%2**width) if legal else None
                actual=None;records=[];data=(build/'case.mmo').read_bytes()
                if p.returncode==0:
                    memory,records=decode(data);actual=memory[source]
                row=dict(case=name,version=version,source=program,source_address=f'{source:016x}',
                         target_address=f'{target:016x}',displacement_tetras=k,width=width,future=future,
                         expected_accepted=legal,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,
                         expected_instruction=f'{expected:08x}' if expected is not None else None,
                         actual_instruction=f'{actual:08x}' if actual is not None else None,
                         fixup_records=records,listing=(build/'case.lst').read_text(),
                         mmo_hex=data.hex(),mmo_sha256=hashlib.sha256(data).hexdigest(),
                         agrees=(p.returncode==0)==legal and (not legal or actual==expected))
                rows.append(row);checkpoint()
    for version in ['original-2013','original-2025']:
        assert sum(not r['agrees'] for r in rows if r['version']==version)==7
    assert all(r['agrees'] for r in rows if r['version'].startswith('audit'))
    print(json.dumps(dict(assemblies=len(rows),mismatches_per_original=7,audit_all_agree=True)))

if __name__=='__main__':main()
