"""Read edges directly from the PDF vector drawing; enumerate connected sets."""
from pathlib import Path
import pikepdf,re,json,subprocess,time
R=Path(__file__).parent;OUT=R/'results/usa_partitions';OUT.mkdir(exist_ok=True)
BOOK=R.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'
subprocess.run(['pdftotext','-f','134','-l','134','-bbox',str(BOOK),str(OUT/'p114-bbox.html')],check=True)
w=re.findall(r'<word xMin="([^"]+)" yMin="([^"]+)" xMax="([^"]+)" yMax="([^"]+)">([A-Z]{2})</word>',(OUT/'p114-bbox.html').read_text())
coords={name:((float(a)+float(c))/2,792-(float(b)+float(d))/2) for a,b,c,d,name in w if 300<float(b)<410};assert len(coords)==48
pdf=pikepdf.open(BOOK);stack=[];ctm=(1,0,0,1,0,0);path=[];curves=False;edges=[];dist=[]
def transform(x,y):
 a,b,c,d,e,f=ctm;return a*x+c*y+e,b*x+d*y+f
for ins in pikepdf.parse_content_stream(pdf.pages[133]):
    op=str(ins.operator);v=list(map(float,ins.operands)) if op in ['cm','m','l'] else []
    if op=='q':stack.append(ctm)
    elif op=='Q':ctm=stack.pop()
    elif op=='cm':
        a,b,c,d,e,f=ctm;A,B,C,D,E,F=v
        ctm=(a*A+c*B,b*A+d*B,a*C+c*D,b*C+d*D,a*E+c*F+e,b*E+d*F+f)
    elif op=='m':path=[transform(*v)];curves=False
    elif op=='l':path.append(transform(*v))
    elif op=='c':curves=True
    elif op=='S':
        if not curves and len(path)>=2:
            names=[]
            for x,y in path:
                name=min(coords,key=lambda s:(coords[s][0]-x)**2+(coords[s][1]-y)**2)
                delta=((coords[name][0]-x)**2+(coords[name][1]-y)**2)**.5
                if delta>2:break
                names.append(name);dist.append(delta)
            else:
                edges.extend(tuple(sorted((a,b))) for a,b in zip(names,names[1:]) if a!=b)
        path=[]
    elif op in ['f','f*','n']:path=[]
edges=sorted(set(edges));assert len(edges)==105,len(edges)
(OUT/'graph.json').write_text(json.dumps(dict(states=sorted(coords),coordinates=coords,edges=edges,max_endpoint_distance=max(dist)),indent=2)+'\n')
print('Extracted105 edges from printed vector paths.',flush=True)

def prepare(size,dc=False):
    names=sorted(coords)+(['DC'] if dc else []);index={s:i for i,s in enumerate(names)};E=edges+([('DC','MD'),('DC','VA')] if dc else []);N=len(names);allmask=(1<<N)-1;adj=[0]*N
    for a,b in E:i,j=index[a],index[b];adj[i]|=1<<j;adj[j]|=1<<i
    def boundary(s):
        t=s;r=0
        while t:
            b=t&-t;t-=b;r|=adj[b.bit_length()-1]
        return r&~s
    sets={1<<i for i in range(N)}
    for k in range(2,size+1):
        nxt=set()
        for s in sets:
            b=boundary(s)
            while b:
                x=b&-b;b-=x;nxt.add(s|x)
        sets=nxt
    def components(s):
        out=[]
        while s:
            reached=front=s&-s
            while front:
                front=boundary(front)&s&~reached;reached|=front
            out.append(reached);s^=reached
        return out
    good=[s for s in sorted(sets) if all(c.bit_count()%size==0 for c in components(allmask^s))]
    name=f'n{N}-k{size}';rows=[]
    for s in good:
        labels=[names[i] for i in range(N) if s>>i&1];cost=sum(bool(s>>index[a]&1)!=bool(s>>index[b]&1) for a,b in E);rows.append(dict(mask=s,states=labels,cost=cost))
    report=dict(n=N,k=size,states=names,adjacency=adj,all_connected=len(sets),reduced=len(good),rows=rows)
    if size==6 and not dc:
        chain=sum(1<<index[a] for a in ['ND','SD','NE','KS','OK','TX']);report['chain_residual_components']=[c.bit_count() for c in components(allmask^chain)];report['maine_options']=sum(bool(s>>index['ME']&1) for s in sets)
        report['mt_tx']=[[names[i] for i in range(N) if s>>i&1] for s in good if (s>>index['MT']&1) and (s>>index['TX']&1)]
        (OUT/'n48-k6-full.xcc').write_text(' '.join(names)+'\n'+'\n'.join(' '.join(names[i] for i in range(N) if s>>i&1) for s in sorted(sets))+'\n')
    (OUT/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n');(OUT/(name+'.xcc')).write_text(' '.join(names)+'\n'+'\n'.join(' '.join(r['states']) for r in rows)+'\n');(OUT/(name+'-cost.xcc')).write_text(' '.join(names)+'\n'+'\n'.join(' '.join(r['states'])+' |'+str(r['cost']) for r in rows)+'\n')
    print(name,'connected',len(sets),'reduced',len(good),flush=True)

if __name__=='__main__':
    for size,dc in [(6,False),(8,False),(7,True)]:prepare(size,dc)
