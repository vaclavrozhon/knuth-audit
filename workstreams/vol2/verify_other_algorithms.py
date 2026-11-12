"""TAOCP 3.2.2: array generators, shuffling, binary feedback, and sums."""
from itertools import product
from math import gcd, lcm
from pathlib import Path
import json
import random

ROOT = Path(__file__).resolve().parent


def period(a):
    return next(d for d in range(1,len(a)+1) if len(a)%d == 0
                and all(a[i] == a[i%d] for i in range(len(a))))


def trajectory(state, step):
    seen, out = {}, []
    while state not in seen:
        seen[state] = len(out)
        state, z = step(state)
        out.append(z)
    mu = seen[state]
    return mu, out[:mu], out[mu:]


def check_additive():
    rng = random.Random(3202)
    cases = steps = 0
    for e in (1,2,5,10,30,35):
        m=2**e
        seeds = [[int(i==j) for i in range(55)] for j in range(55)]
        seeds += [[0]*55,[m-1]*55,[rng.randrange(m) for _ in range(55)]]
        for initial in seeds:
            direct=initial[:]
            for n in range(55,605):
                direct.append((direct[n-24]+direct[n-55])%m)
            memory=[0]+initial[::-1]
            j,k=24,55
            for expected in direct[55:]:
                # The nine printed MIX instructions, with a word of e bits.
                accumulator=(memory[k]+memory[j])%m
                memory[k]=accumulator
                j-=1;k-=1
                assert not (j==0 and k==0)
                if j<=0:j=55
                if k<=0:k=55
                assert accumulator==expected
                steps+=1
            memory=[0]+initial[::-1]
            batched=[]
            for _ in range(10):
                for k in range(24,0,-1):
                    memory[k+31]=(memory[k+31]+memory[k])%m
                for k in range(31,0,-1):
                    memory[k]=(memory[k]+memory[k+24])%m
                batched.extend(memory[:0:-1])
            assert batched==direct[55:]
            cases+=1
    return dict(initial_states=cases, single_steps=steps,
                single_call_time='14 + 2/55', batched_call_time='12 + 6/55')


def check_shuffle():
    xs=[((5**n-1)*3//4)%8 for n in range(8)]
    ys=[((5**n-1)//4)%8 for n in range(8)]
    def M(state):
        table,ix,iy=state
        table=list(table);j=ys[iy]//2;z=table[j];table[j]=xs[ix]
        return (tuple(table),(ix+1)%8,(iy+1)%8),z
    def B(state):
        table,ix,y=state
        table=list(table);j=y//2;y=table[j];table[j]=xs[ix]
        return (tuple(table),(ix+1)%8,y),y
    muM,preM,cycM=trajectory((tuple(xs[:4]),4,0),M)
    muB,preB,cycB=trajectory((tuple(xs[:4]),5,xs[4]),B)
    assert (muM,preM,cycM)==(7,[0,4,5,6,2,0,3],[2,7,4,1,6,3,0,5])
    state_muB=muB
    # The stored previous output delays state repetition by one step here.
    # Remove any redundant prefix from the observable output sequence.
    while preB and preB[-1]==cycB[-1]:
        cycB=[preB.pop()]+cycB[:-1]
        muB-=1
    assert state_muB==47 and muB==46 and len(cycB)==period(cycB)==40
    assert ''.join(map(str,preB))=='2365700531472632401103756476025125417362503746'
    assert ''.join(map(str,cycB))=='3017524061523174620374531604251675302647'

    rng=random.Random(3214);mix_steps=0
    for byte in (2,4,8,64):
        m=byte**5;a=(m//7)|1;x=m-1
        table=[rng.randrange(m) for _ in range(byte)];y=m-1
        for _ in range(2000):
            original=table[:]
            j=y//byte**4
            register_x=(((x+1)%m)*a)%m
            accumulator=table[j]
            table[j]=register_x
            expected_j=byte*y//m
            assert j==expected_j and accumulator==original[expected_j]
            assert register_x==a*(x+1)%m
            x=register_x;y=accumulator;mix_steps+=1
    return dict(M=dict(preperiod=muM, prefix=preM, cycle=cycM),
                B=dict(preperiod=muB, state_preperiod=state_muB,
                       prefix=preB, cycle=cycB),MIX_steps=mix_steps)


def feedback(x,A,k,modified=False):
    if modified and x==0:return A
    raw=x*2;z=raw%(2**k)
    if raw>=2**k and not (modified and z==0):z^=A
    return z


def modified_instructions(x,A,k):
    accumulator=x
    if accumulator==0:accumulator=A
    raw=accumulator+x;accumulator=raw%(2**k)
    overflow=raw>=2**k
    if overflow and accumulator!=0:accumulator^=A
    return accumulator


def check_feedback():
    recurrences=cycles=instruction_checks=0
    for k in range(1,9):
        m=2**k
        for A in range(1,m,2):
            coefficients=[(A>>(k-j))&1 for j in range(1,k+1)]
            for x in range(m):
                assert modified_instructions(x,A,k)==feedback(x,A,k,True)
                instruction_checks+=1
                orbit=[x]
                for _ in range(2*k):orbit.append(feedback(orbit[-1],A,k))
                for bit in (0,k-1):
                    bs=[(v>>bit)&1 for v in orbit]
                    for n in range(k,len(bs)):
                        assert bs[n]==sum(coefficients[j-1]*bs[n-j] for j in range(1,k+1))%2
                        recurrences+=1
            mu,_,word=trajectory(1,lambda x:(feedback(x,A,k),x))
            assert mu==0
            if len(word)==m-1:
                for modified in (False,True):
                    mu,_,word=trajectory(1,lambda x:(feedback(x,A,k,modified),x))
                    assert mu==0 and len(word)==m-1+modified
                    bits=[x&1 for x in word]
                    windows={tuple(bits[(n+j)%len(bits)] for j in range(k))
                             for n in range(len(bits))}
                    assert len(windows)==len(bits)
                    assert ((0,)*k in windows)==modified
                    cycles+=1
    fig=[11,5,10,7,14,15,13,9,1,2,4,8,3,6,12,11]
    assert all(feedback(a,3,4)==b for a,b in zip(fig,fig[1:]))
    return dict(recurrence_equalities=recurrences, complete_word_cycles=cycles,
                modified_instruction_states=instruction_checks,figure_1=fig)


def sync_pattern(k):
    out=[0]*(k+2)
    for j in range(1,k):out += [j]+[0]*(k+2-j)
    assert len(out)==(k*k+7*k-2)//2
    return out


def check_synchronization():
    label_states=full_states=0
    for k in range(1,6):
        word=sync_pattern(k)
        for initial in product(range(k),repeat=k+1):
            table=list(initial[:-1]);y=initial[-1]
            for x in word:
                j=y;y,table[j]=table[j],x
            assert y==0 and table==[0]*k
            label_states+=1
    for k in range(1,4):
        # Two distinct actual values for every bucket.
        m=2*k
        labels=sync_pattern(k)
        word=[2*j+(i%2) for i,j in enumerate(labels)]
        lam=period(word)
        for initial in product(range(m),repeat=k+1):
            table=list(initial[:-1]);y=initial[-1];out=[]
            for n in range(4*len(word)):
                j=k*y//m;y,table[j]=table[j],word[n%len(word)];out.append(y)
            tail=out[2*len(word):]
            assert period(tail)==lam
            full_states+=1
    return dict(label_states=label_states, full_value_states=full_states)


def check_sum_periods():
    cases=0
    for m in (2,3,4):
        words=[w for n in range(1,5) for w in product(range(m),repeat=n)
               if period(w)==n]
        for x in words:
            for y in words:
                a,b=len(x),len(y);upper=lcm(a,b)
                z=[(x[i%a]+y[i%b])%m for i in range(upper)]
                actual=period(z)
                lower=1
                for p in (2,3):
                    aa,bb=a,b;ea=eb=0
                    while aa%p==0:aa//=p;ea+=1
                    while bb%p==0:bb//=p;eb+=1
                    if ea!=eb:lower*=p**max(ea,eb)
                assert upper%actual==0 and actual%lower==0
                if gcd(a,b)==1:assert actual==a*b
                cases+=1
    return dict(pairs=cases)


def main():
    result=dict(status='passed')
    for name,fn in [('additive',check_additive),('shuffle',check_shuffle),
                    ('feedback',check_feedback),('synchronization',check_synchronization),
                    ('sum_periods',check_sum_periods)]:
        result[name]=fn();print(name,'passed',flush=True)
        (ROOT/'results/other-algorithms-partial.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'results/other-algorithms.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
