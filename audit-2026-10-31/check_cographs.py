"""Independent induced-subgraph and cotree checks for SAT 343 and 345."""
from itertools import combinations,product
from fractions import Fraction as Q
from pathlib import Path
import json


def cograph(adj):
    return not any(sorted((adj[v]&sum(1<<u for u in S)).bit_count() for v in S)==[1,1,2,2]
                   for S in combinations(range(len(adj)),4))


def components(adj,vertices,complement=False):
    todo=set(vertices);out=[]
    while todo:
        start=todo.pop();part={start};queue=[start]
        for v in queue:
            neighbors={u for u in todo if bool(adj[v]>>u&1)!=complement}
            todo-=neighbors;part|=neighbors;queue+=sorted(neighbors)
        out.append(part)
    return out


def cotree_nodes(adj,vertices=None):
    if vertices is None:vertices=set(range(len(adj)))
    if len(vertices)==1:return [sum(1<<v for v in vertices)]
    parts=components(adj,vertices)
    if len(parts)==1:parts=components(adj,vertices,True)
    assert len(parts)>1
    return [sum(1<<v for v in vertices)]+[s for part in parts for s in cotree_nodes(adj,part)]


def scaled_mobius(adj,pnums,den=4):
    """Value for EVERY induced subgraph, scaled by den^number_of_vertices."""
    values=[1]*(1<<len(adj))
    for mask in range(1,len(values)):
        bit=mask&-mask;v=bit.bit_length()-1;others=mask^bit
        neighbors=others&adj[v];remainder=others^neighbors
        values[mask]=den*values[others]-pnums[v]*den**neighbors.bit_count()*values[remainder]
    return values


def independent_sum(adj,p):
    value=Q(0)
    for mask in range(1<<len(adj)):
        if any(mask>>v&1 and mask&adj[v] for v in range(len(adj))):continue
        term=Q(1)
        for v in range(len(adj)):
            if mask>>v&1:term*=-p[v]
        value+=term
    return value


def main():
    counts={};vectors=0;counter_counts={};first_counter=None
    for n in range(1,6):
        edges=list(combinations(range(n),2));count=counter=0
        for edge_mask in range(1<<len(edges)):
            adj=[0]*n
            for k,(i,j) in enumerate(edges):
                if edge_mask>>k&1:adj[i]|=1<<j;adj[j]|=1<<i
            if not cograph(adj):continue
            nodes=cotree_nodes(adj);count+=1
            for pnums in product((1,2,3),repeat=n):
                values=scaled_mobius(adj,pnums)
                actual=all(v>0 for v in values)
                corrected=all(values[node]>0 for node in nodes)
                assert actual==corrected
                if values[-1]>0 and not actual:
                    counter+=1
                    if first_counter is None:first_counter=(n,[(i,j) for i,j in edges if adj[i]>>j&1],pnums,str(Q(values[-1],4**n)))
                vectors+=1
        counts[n]=count;counter_counts[n]=counter
    adj=[2,1,8,4];p=[Q(3,4)]*4
    assert independent_sum(adj,p)==Q(1,4)
    assert independent_sum(adj,[Q(3,4),Q(3,4),0,0])==Q(-1,2)
    # Actual event system: U,V independent uniform on {0,1,2,3}.
    # A1=(U!=0), A2=(U!=1), A3=(V!=0), A4=(V!=1).
    event_masks=[]
    for u,v in product(range(4),repeat=2):
        event_masks.append(sum(int(b)<<i for i,b in enumerate((u!=0,u!=1,v!=0,v!=1))))
    assert all(event_masks)
    conditional_checks=0
    for i in range(4):
        remote=[j for j in range(4) if j!=i and not (adj[i]>>j&1)]
        for subset in range(1<<len(remote)):
            forbidden=sum(1<<j for k,j in enumerate(remote) if subset>>k&1)
            sample=[mask for mask in event_masks if not mask&forbidden]
            if sample:
                assert Q(sum(mask>>i&1 for mask in sample),len(sample))==Q(3,4)
                conditional_checks+=1
    connected=[row|16 for row in adj]+[15]
    assert independent_sum(connected,p+[Q(1,10)])==Q(3,20)
    assert cograph(connected)
    boundary=[Q(1,2)]*4
    assert independent_sum(adj,boundary)==0
    decreased=[Q(1,4),Q(1,2),Q(1,2),Q(1,2)]
    assert independent_sum(adj,decreased)==0
    report={'cographs_by_order':counts,'probability_vectors_checked':vectors,
            'positive_root_but_outside_R_cases_by_order':counter_counts,
            'first_counterexample':first_counter,
            'cotree_criterion_matches_all_induced_subgraphs':True,
            'F033_two_disjoint_edges_M_at_three_quarters':'1/4',
            'F033_M_after_zeroing_other_edge':'-1/2',
            'F033_actual_probability_space_points':16,
            'F033_actual_event_marginals':['3/4']*4,
            'F033_lopsidependency_conditional_checks':conditional_checks,
            'F033_actual_avoidance_probability':0,
            'F033_connected_five_vertex_cograph_M':'3/20',
            'F035_boundary_M':0,'F035_boundary_after_strict_single_decrease_M':0,
            'scope':'All labelled cographs through five vertices and all probability vectors in {1/4,1/2,3/4}^n. General corrected cotree proof is in COGRAPH_NOTES.md.'}
    (Path(__file__).parent/'results/cographs.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
