"""Literal pointer algorithms, independent of recursive tree oracle.

None is the null link. H is a separate header. Node maps carry L/R, lt/rt, info.
"""
from copy import deepcopy
H = -1

def stack_inorder(root, d):
    stack=[]; p=root
    while True:
        if p is not None:
            stack.append(p);p=d[p]['L'];continue
        if not stack:return
        p=stack.pop();yield p;p=d[p]['R']

def stack_postorder(root,d):
    stack=[];p=root;q=None
    while True:
        if p is not None:
            stack.append(p);p=d[p]['L'];continue
        if not stack:return
        p=stack.pop();r=d[p]['R']
        if r is not None and r!=q:
            stack.append(p);p=r;continue
        yield p;q=p;p=None

def morris(root,d,pre=None):
    p=root;r=None
    while p is not None:
        q=d[p]['L']
        if q is None:
            if pre is not None:pre.append(p)
        else:
            while q!=r and d[q]['R'] is not None:q=d[q]['R']
            if q!=r:
                d[q]['R']=p
                if pre is not None:pre.append(p)
                p=d[p]['L'];continue
            d[q]['R']=None
        yield p
        r=p;p=d[p]['R']

def rotations(root,d):
    p=root;q=-1000000;sentinel=q;out=[]
    while True:
        if p is None:p,q=q,None
        if p==sentinel:return out,q
        out.append(p)
        r=d[p]['L'];d[p]['L']=d[p]['R'];d[p]['R']=q;q=p;p=r

def inorder_successor(p,d,right_only=False):
    q=d[p]['R']
    if d[p]['rt']:return q
    while (d[q]['L'] is not None if right_only else not d[q]['lt']):q=d[q]['L']
    return q

def preorder_successor(p,d,right_only=False):
    if (d[p]['L'] is not None if right_only else not d[p]['lt']):return d[p]['L']
    q=p
    while d[q]['rt']:q=d[q]['R']
    return d[q]['R']

def parent_f(p,d):
    q=r=p
    while not d[q]['lt'] and not d[r]['rt']:q=d[q]['L'];r=d[r]['R']
    if not d[r]['rt']:
        q=d[q]['L']
        if p==d[q]['R']:return q
        while not d[r]['rt']:r=d[r]['R']
        return d[r]['R']
    r=d[r]['R']
    if p==d[r]['L']:return r
    while not d[q]['lt']:q=d[q]['L']
    return d[q]['L']

def post_successor(p,d,head=H,guard_root=True):
    q=parent_f(p,d)
    if guard_root and q==head:return head
    if p!=d[q]['L']:return q
    while not d[q]['rt']:q=inorder_successor(q,d)
    return q

def double_successor(p,phase,d):
    if phase==1:return (d[p]['L'],1) if not d[p]['lt'] else (p,2)
    return (d[p]['R'],1 if not d[p]['rt'] else 2)

def insert_full(p,q,d,side='R'):
    other='L' if side=='R' else 'R'; tag=side.lower()+'t';otag=other.lower()+'t'
    d[q][side],d[q][tag]=d[p][side],d[p][tag]
    d[p][side],d[p][tag]=q,0
    d[q][other],d[q][otag]=p,1
    if not d[q][tag]:
        r=d[q][side]
        while not d[r][otag]:r=d[r][other]
        d[r][other]=q

def insert_right_threaded(p,q,d,side='R'):
    if side=='R':
        d[q]['R'],d[q]['rt']=d[p]['R'],d[p]['rt']
        d[p]['R'],d[p]['rt']=q,0;d[q]['L']=None
    else:
        r=d[p]['L'];d[q]['L']=r
        if r is not None:
            while not d[r]['rt']:r=d[r]['R']
            d[r]['R']=q
        d[p]['L']=q;d[q]['R']=p;d[q]['rt']=1

def copy_c(source,dest,u,source_head=H,right_only=False):
    p=source_head;q=u
    def alloc():
        r=max([0,*dest])+1;dest[r]={'L':None,'R':None,'lt':1,'rt':1,'info':-999};return r
    def put(p,q,side):
        (insert_right_threaded if right_only else insert_full)(p,q,dest,side)
    # C1 goes directly to C4.
    first=True
    while True:
        if not first:
            if not source[p]['rt']:put(q,alloc(),'R')
            dest[q]['info']=source[p]['info']
        first=False
        if (source[p]['L'] is not None if right_only else not source[p]['lt']):put(q,alloc(),'L')
        p=preorder_successor(p,source,right_only);q=preorder_successor(q,dest,right_only)
        if p==source_head:return

def compare_r(d,e,hd=H,he=H):
    p=hd;q=he;step=3
    while True:
        if step==2:
            a,b=d[p]['info'],e[q]['info']
            if a!=b:return (a>b)-(a<b)
            step=3
        if step==3:
            a,b=d[p]['L'],e[q]['L']
            if (a is None)!=(b is None):return -1 if a is None else 1
            if a is not None:p,q=a,b;step=2;continue
            step=4
        if step==4:
            if p==hd:return 0
            step=5
        if step==5:
            a,b=d[p]['rt'],e[q]['rt']
            if a!=b:return -1 if a else 1
            p,q=d[p]['R'],e[q]['R'];step=4 if a else 2

def thread_l(root,d,head=H,use_morris=False):
    d[head]={'L':root,'R':head,'lt':0,'rt':0,'info':-999}
    q=head
    traversal=morris(root,d) if use_morris else stack_inorder(root,d)
    import itertools
    for p in itertools.chain(traversal,[head]):
        if d[q]['R'] is None:d[q]['R']=p;d[q]['rt']=1
        else:d[q]['rt']=0
        if d[p]['L'] is None:d[p]['L']=q;d[p]['lt']=1
        else:d[p]['lt']=0
        q=p
    return d

def erase_x(d,head=H):
    p=head;freed=[]
    while True:
        q=inorder_successor(p,d,True)
        if p!=head:
            freed.append(p);del d[p]  # make any later access fail immediately
        if q==head:break
        p=q
    d[head]['L']=None
    return freed

def insert_explicit(p,q,d,initialize_left=True):
    if initialize_left:d[q]['L']=None
    d[q]['R']=d[p]['R'];d[q]['suc']=d[p]['suc']
    d[p]['suc']=q;d[p]['R']=q;d[q]['pred']=p;d[d[q]['suc']]['pred']=q

def insert_alt_left(p,q,d):
    d[q]['L'],d[q]['lt']=d[p]['L'],d[p]['lt']
    d[p]['L'],d[p]['lt']=q,0;d[q]['R']=None

def insert_alt_right(p,q,d):
    # Last node of left subtree, or P when no left subtree.
    pred=p
    if not d[p]['lt']:
        pred=d[p]['L']
        while True:
            if d[pred]['R'] is not None:pred=d[pred]['R']
            elif not d[pred]['lt']:pred=d[pred]['L']
            else:break
    d[q]['L']=d[pred]['L'];d[q]['lt']=1;d[q]['R']=d[p]['R']
    d[pred]['L']=q;d[p]['R']=q

def copy_alt(source,dest,u,head=H):
    p=head;q=u;first=True
    def alloc():
        r=max([0,*dest])+1;dest[r]={'L':None,'R':None,'lt':1,'info':-999};return r
    while True:
        if not first:
            if source[p]['R'] is not None:
                r=alloc();dest[r]['L']=dest[q]['L'];dest[q]['R']=dest[q]['L']=r
            dest[q]['info']=source[p]['info']
        first=False
        if not source[p]['lt']:
            r=alloc();dest[r]['L']=dest[q]['L'];dest[q]['L']=r;dest[q]['lt']=0
        p=source[p]['L'];q=dest[q]['L']
        if p==head:return

def detach_a(p,d,new_head):
    q=p
    while not d[q]['rt']:q=d[q]['R']
    r=d[q]['R']
    if d[r]['L']==p:d[r]['L']=None
    else:
        r=d[r]['L']
        while d[r]['R']!=p:r=d[r]['R']
        d[r]['R'],d[r]['rt']=d[q]['R'],d[q]['rt']
    d[q]['R']=new_head;d[new_head]['L']=p
