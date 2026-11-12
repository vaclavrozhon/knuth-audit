#!/usr/bin/env python3
"""Compile unchanged existing numerical functions with slash arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import ast
import contextlib
import hashlib
import io
import json
import math
import random
import sys
import time
import mpmath as mp

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'sources'))
from slash_compiler import Slash,SlashRuntime
OUT=ROOT/'results/rational-compiler.json'


def source_function(path,name):
    text=path.read_text()
    node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    return ast.get_source_segment(text,node)+'\n'


def interfaces():
    rng=random.Random(45115);count=0
    rt=SlashRuntime(8)
    for _ in range(400):
        x=rt.make(F(rng.randrange(-20,21),rng.randrange(1,30)))
        y=rt.make(F(rng.randrange(-20,21),rng.randrange(1,30)))
        X,Y=F(*x.pair),F(*y.pair)
        for op,want in [(lambda:x+y,X+Y),(lambda:x-y,X-Y),(lambda:x*y,X*Y)]:
            assert op().pair==rt.format.round(want);count+=1
        if Y:assert (x/y).pair==rt.format.round(X/Y);count+=1
        assert (2-x).pair==rt.format.round(2-X)
        assert (x<y)==(X<Y) and (x==y)==(X==Y)
    rt=SlashRuntime(58)
    src='''import math
from numpy import log
def probe():
    x=1
    x/=10
    print(x)
    print(x,fractional=True)
    return math.sqrt(2.0)+log(2.0)
'''
    env=rt.compile(src);stream=io.StringIO()
    with contextlib.redirect_stdout(stream):z=env['probe']()
    assert isinstance(z,Slash) and rt.special_calls==2
    assert stream.getvalue()=='0.1\n1/10\n'
    powerenv=rt.compile('a=2**-1\nb=2**3\nc=4\nc**=-1\n')
    assert isinstance(powerenv['a'],Slash) and powerenv['a'].pair==(1,2)
    assert type(powerenv['b']) is int and powerenv['b']==8
    assert powerenv['c'].pair==(1,4)
    assert (rt.make(0)/0).pair==(0,0)
    assert (rt.make(1)/0).pair==(1,0)
    assert (rt.make(-1)/0).pair==(-1,0)
    assert (rt.make('inf')*0).pair==(0,0)
    assert (rt.make('inf')-rt.make('inf')).pair==(0,0)
    assert not (rt.make('nan')==rt.make('nan'))
    rejected=0
    for bad in ['import scipy','z=1j','x=isinstance(1,float)','from math import *',
                'def f(float): return float(1)','def print(x): return x']:
        try:rt.compile(bad)
        except NotImplementedError:rejected+=1
        else:raise AssertionError(bad)
    return {'operation_cases':count,'special_calls':2,'stdout':stream.getvalue(),
            'unsupported_programs_rejected':rejected,'special_result':list(z.pair)}


def numerical_programs():
    mp.mp.dps=100
    programs=[('r8_hypot',ROOT/'sources/burkardt-r8_hypot.py',
               [(3.0,4.0),(1.0,2.0**-15),(1.0,2.0**-25),(1e20,1e20)]),
              ('r8_log_2',ROOT/'sources/burkardt-r8_log_2.py',
               [(2.0,),(0.5,),(1.0+2.0**-40,),(1e10,)])]
    rows=[];sources=[]
    for name,path,cases in programs:
        src=source_function(path,name);sources.append({'path':str(path.relative_to(ROOT)),
            'function':name,'source_sha256':hashlib.sha256(src.encode()).hexdigest()})
        normal={};exec(compile(src,str(path),'exec'),normal)
        for args in cases:
            exactargs=[mp.mpf(F(x).numerator)/F(x).denominator for x in args]
            exact=mp.sqrt(sum(x*x for x in exactargs)) if name=='r8_hypot' else mp.log(abs(exactargs[0]),2)
            results=[]
            baseline=float(normal[name](*args))
            results.append({'mode':'original_binary64','value':repr(baseline),
                'absolute_error':mp.nstr(abs(mp.mpf(baseline)-exact),30)})
            for q in [27,58]:
                rt=SlashRuntime(q);env=rt.compile(src,str(path));start=time.monotonic()
                z=env[name](*[rt.input(a) for a in args]);elapsed=time.monotonic()-start
                assert isinstance(z,Slash)
                u,a=z.pair;value=mp.mpf(u)/a if a else mp.sign(u)*mp.inf if u else mp.nan
                results.append({'mode':f'slash_q{q}','pair':list(z.pair),
                    'absolute_error':mp.nstr(abs(value-exact),30),
                    'operations':rt.operations,'special_calls':rt.special_calls,'seconds':elapsed})
            rows.append({'program':name,'arguments':[repr(a) for a in args],
                         'reference_100_digits':mp.nstr(exact,100),'results':results})
    # A 64-bit slash container can lose a small increment near a simple rational.
    row=next(r for r in rows if r['program']=='r8_log_2' and r['arguments']==[repr(1.0+2.0**-40)])
    assert row['results'][2]['pair']==[0,1]
    assert mp.mpf(row['results'][0]['absolute_error'])<mp.mpf(row['results'][2]['absolute_error'])
    return {'sources':sources,'program_cases':len(rows),'rows':rows,
            'comparison_scope':'Original binary64, 32-bit slash q27, 64-bit slash q58; same scalar library functions'}


def collision_program():
    name='algorithm_s_float';path=ROOT/'verify_collision_test.py';src=source_function(path,name)
    normal={};exec(compile(src,str(path),'exec'),normal);rows=[]
    for m,n in [(10,2),(17,12),(64,25)]:
        result=normal[name](m,n)
        modes=[{'mode':'original_binary64','status':result['status'],
                'sum':repr(result['sum']),'mass_error':str(abs(F(result['sum'])-1))}]
        for q in [27,58]:
            rt=SlashRuntime(q);env=rt.compile(src,str(path));r=env[name](m,n)
            total=r['sum'];assert isinstance(total,Slash)
            modes.append({'mode':f'slash_q{q}','status':r['status'],'sum_pair':list(total.pair),
                          'mass_error':str(abs(F(*total.pair)-1)),
                          'operations':rt.operations,'cutoff_pair':list(rt.make(1e-20).pair)})
        rows.append({'m':m,'n':n,'results':modes})
    assert rows[0]['results'][0]['status']=='sentinel_overrun'
    assert all(r['sum_pair']==[1,1] and r['status']=='completed' for r in rows[0]['results'][1:])
    return {'source_path':'verify_collision_test.py','function':name,
            'source_sha256':hashlib.sha256(src.encode()).hexdigest(),'rows':rows}


def cdf_quality():
    # A unit total does not certify the individual probabilities. This oracle
    # counts surjections by inclusion-exclusion, independently of recurrence S.
    from math import comb
    src=source_function(ROOT/'verify_collision_test.py','algorithm_s_float')
    normal={};exec(compile(src,'collision-cdf-original','exec'),normal)
    rows=[]
    for m,n in [(17,12),(64,25)]:
        probabilities=[F(comb(m,j)*sum((-1)**k*comb(j,k)*(j-k)**n for k in range(j+1)),m**n)
                       for j in range(min(m,n)+1)]
        assert sum(probabilities)==1 and all(p>=0 for p in probabilities)
        for mode in ['binary64',27,58]:
            if mode=='binary64':out=normal['algorithm_s_float'](m,n)
            else:
                rt=SlashRuntime(mode);out=rt.compile(src)['algorithm_s_float'](m,n)
            errors=[]
            for record in out['output']:
                c=record['collisions'];want=sum(probabilities[max(0,n-c):])
                z=record['cdf'];actual=F(*z.pair) if isinstance(z,Slash) else F(z)
                errors.append({'collisions':c,'exact':str(want),'reported':str(actual),
                               'absolute_error':str(abs(actual-want))})
            maximum=max((F(e['absolute_error']) for e in errors),default=F(0))
            rows.append({'m':m,'n':n,'mode':str(mode),'maximum_cdf_error':str(maximum),
                         'maximum_cdf_error_decimal':float(maximum),'outputs':errors})
    return {'oracle':'Exact surjection counts by inclusion-exclusion','rows':rows}


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('interfaces',interfaces),('numerical_programs',numerical_programs),('collision_program',collision_program),('cdf_quality',cdf_quality)]:
        if name in data:continue
        start=time.monotonic();v=fn();data[name]={'status':'passed','seconds':time.monotonic()-start,'result':v}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,json.dumps(data[name]),flush=True)
