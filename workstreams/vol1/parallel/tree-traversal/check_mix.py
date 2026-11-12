"""Actual printed MIX programs and complete exercise-20 variants.

No shared simulator modifications. VISIT's call is timed; the external visit and
return are an abstract zero-time hook, preserving registers as required.
"""
from pathlib import Path
import sys, json, hashlib
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from mix_machine import Machine, number, Word
from mixal import Assembly, put
from tree_shapes import shapes, build, orders, stack_height

BASE = Path(__file__).resolve().parent
HEAD, STACK, AVAIL, VISIT, OVERFLOW = 900, 2000, 2100, 800, 801

def program(kind, b=64, capacity=20):
    rows = [(k,'EQU',str(v)) for k,v in [('HEAD',HEAD),('A',STACK),('MAX',capacity),('AVAIL',AVAIL),('VISIT',VISIT),('OVERFLOW',OVERFLOW)]]
    rows += [('LLINK','EQU','1:2'),('RLINK','EQU','1:2'),('LLINKT','EQU','0:2'),('RLINKT','EQU','0:2'),('LINK','EQU','0:2'),('INFO','EQU','3:5'),('','ORIG','100')]
    if kind.startswith('T'):
        linked = 'linked' in kind
        optimized = 'opt' in kind
        rows += [('T1','LD5','HEAD(LLINK)'),('T2A','J5Z','DONE'),('','ENT6','0')]
        if optimized:
            rows += [('T3','LD3','0,5(LLINK)'),('','J3Z','T5')]
        push = [('','ENT4','0,6'),('','LD6','AVAIL'),('','J6Z','OVERFLOW'),('','LDX','0,6(LINK)'),('','STX','AVAIL'),('','ST5','0,6(INFO)'),('','ST4','0,6(LINK)')] if linked else [('', 'DEC6','MAX'),('','J6NN','OVERFLOW'),('','INC6','MAX+1'),('','ST5','A,6')]
        if not optimized:
            push[0] = ('T3',push[0][1],push[0][2])
        rows += push
        rows += [('', 'ENT5' if optimized else 'LD5','0,3' if optimized else '0,5(LLINK)'),('T2B','J5NZ','T3')]
        rows += [('T4','LD4','0,6(LINK)'),('','LD5','0,6(INFO)'),('','LDX','AVAIL'),('','STX','0,6(LINK)'),('','ST6','AVAIL'),('','ENT6','0,4')] if linked else [('T4','LD5','A,6'),('','DEC6','1')]
        rows += [('T5','JMP','VISIT'),('','LD5','1,5(RLINK)'),('T2C','J5NZ','T3'),('','J6NZ','T4')]
    elif kind == 'S':
        rows += [('S0','ENT5','HEAD'),('','JMP','2F'),('S3','JMP','VISIT'),('S1','LD5N','1,5(RLINKT)'),('','J5NN','1F'),('','ENN6','0,5'),('S2','ENT5','0,6'),('2H','LD6','0,5(LLINKT)'),('','J6P','S2'),('1H','ENT6','-HEAD,5'),('','J6NZ','S3')]
    elif kind in ('U','U-fixed','U-fixed-i4'):
        rows += [('U1','LD5','HEAD(LLINK)'),('U2A','J5Z','DONE'),('U3','LD6','0,5(LLINK)'),('','J6Z','U6'),('U4','CMP5','1,6(RLINK)'),('','JE','5F'),('','ENT4','0,6'),('','LD6','1,6(RLINK)'),('','J6NZ','U4'),('U5','ST5','1,4(RLINK)'),('U9','LD5','0,5(LLINK)'),('','JMP','U3'),('5H','STZ','1,6(RLINK)'),('U6','JMP','VISIT'),('U7','LD5','1,5(RLINK)'),('U2','J5NZ','U3')]
    else:
        raise ValueError(kind)
    if kind == 'U-fixed':
        j=next(i for i,row in enumerate(rows) if row[0]=='U4')
        rows[j:j+1]=[('', 'ENTA','0,5'),('','SLA','3'),('U4','CMPA','1,6(RLINK)')]
    if kind == 'U-fixed-i4':
        j=next(i for i,row in enumerate(rows) if row[0]=='U4')
        rows[j:j+2]=[('U4','ST5','TEST(1:2)'),('','LD4','1,6(RLINK)'),('TEST','DEC4','0'),('','J4Z','5F')]
    rows += [('DONE','HLT','0'),('','END','100')]
    return Assembly(rows,b)

def execute(kind, shape, b=64, capacity=None, right_only=False):
    root,nodes=build(shape); n=len(nodes)
    capacity = n+1 if capacity is None else capacity
    assembly=program(kind,b,capacity); m=Machine(b); assembly.load(m)
    for k in range(8):m.reg[k]=number(-17-k,b)
    m.j=71; m.comparison=-1; m.overflow=True
    addr=lambda p:0 if p is None else 1000+2*p
    inorder=orders(root,nodes)[1]
    all_nodes={HEAD:(root,HEAD,False,False)}
    for p,d in nodes.items():
        l,r=d['L'],d['R']; lt=rt=False
        if kind=='S':
            j=inorder.index(p)
            if l is None and not right_only:l=inorder[j-1] if j else HEAD;lt=True
            if r is None:r=inorder[j+1] if j+1<n else HEAD;rt=True
        all_nodes[addr(p)]=(l,r,lt,rt)
    if kind=='S' and root is None and not right_only:all_nodes[HEAD]=(HEAD,HEAD,True,False)
    for p,(l,r,lt,rt) in all_nodes.items():
        for off,q,tag in [(0,l,lt),(1,r,rt)]:
            link=HEAD if q==HEAD else addr(q)
            word=put(number(731+off,b),number(link,b),10)
            m.mem[p+off]=Word(-1 if tag else 1,word.digits)
    for i in range(capacity):
        p=2200+i
        m.mem[p]=put(number(999,b),number(p+1 if i+1<capacity else 0,b),2)
    m.mem[AVAIL]=number(2200 if capacity else 0,b)
    original={p+off:m.mem[p+off] for p in all_nodes for off in [0,1]}
    seen=[];counts={};done=assembly.symbols['DONE'].value(b)
    for _ in range(50000):
        if m.pc==done or m.pc==OVERFLOW:break
        if m.pc==VISIT:
            seen.append((m.reg[5].value(b)-1000)//2)
            m.pc=m.j
            continue
        counts[m.pc]=counts.get(m.pc,0)+1
        m.step()
    else:raise AssertionError(('step limit',kind,shape,b))
    overflow=m.pc==OVERFLOW
    if not overflow:
        if kind in ('U','U-fixed','U-fixed-i4'):
            for k in ([1,2,3,7] if kind=='U-fixed' else [0,1,2,3,7]):
                assert m.reg[k]==number(-17-k,b),('preserved register',kind,k)
        if kind != 'U':assert seen==inorder,(kind,shape,b,seen,inorder)
        else:
            spine=[];p=root
            while p is not None:spine.append(p);p=nodes[p]['R']
            assert seen==spine,('original U right-spine characterization',shape,b,seen,spine)
        assert all(m.mem[p]==w for p,w in original.items()),('changed node',kind,shape,b)
        if 'linked' in kind:
            p=m.mem[AVAIL].value(b);free=[]
            while p:
                assert p not in free
                free.append(p)
                from mix_machine import field
                p=field(m.mem[p],2).value(b)
            assert sorted(free)==list(range(2200,2200+capacity))
    a=sum(d['R'] is None for d in nodes.values());spine=0;p=root
    while p is not None:spine+=1;p=nodes[p]['R']
    formulas={'T':15*n+a+4,'T-linked':30*n+a+4,'T-opt':12*a+6*n-7,'T-linked-opt':27*a+6*n-22,'S':11*n-a+7,'U':21*n+6*a-3-14*spine,'U-fixed':21*n+12*a-9-14*spine,'U-fixed-i4':27*n+6*a-3-20*spine}
    actual_formulas=dict(formulas, **{'T-opt':7*n+11*a-6,'T-linked-opt':7*n+26*a-21})
    expected=actual_formulas[kind] if n else (7 if kind=='S' else 3)
    if not overflow and kind!='U':assert m.time==expected,(kind,shape,b,m.time,expected)
    return {'time':m.time,'overflow':overflow,'n':n,'a':a,'right_spine':spine,'printed_formula':formulas[kind],'visited':seen,'expected':inorder}

def main():
    out={'prior_completed_before_first_failure':{'T':1454,'T-linked':1454,'T-opt':1454,'T-linked-opt':1454,'S':2908},'domain':'all binary shapes n<=7 at radix64; all shapes n<=4 at each radix65..100; exact capacity/overflow cases','programs':{},'empty':{}}
    kinds=['U','U-fixed']
    for kind in kinds:
        count=0
        for b in range(64,101):
            for n in range(8 if b==64 else 5):
                for shape in shapes(n):
                    execute(kind,shape,b);count+=1
                    if kind=='S':execute(kind,shape,b,right_only=True);count+=1
        out['programs'][kind]=count
        out['empty'][kind]=execute(kind,None)
        (BASE/'results/mix-checkpoint.json').write_text(json.dumps(out,indent=2)+'\n')
    capacity_cases=0
    for shape in shapes(7):
        h=stack_height(shape)
        for kind in ['T','T-linked']:
            assert not execute(kind,shape,capacity=h)['overflow']
            assert execute(kind,shape,capacity=h-1)['overflow']
            capacity_cases+=2
    out['capacity_cases']=capacity_cases
    out['sha256']={x:hashlib.sha256((BASE/x).read_bytes()).hexdigest() for x in ['check_mix.py','tree_shapes.py']}
    (BASE/'results/mix.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
