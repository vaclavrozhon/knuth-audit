@x
@<Set |best_itm| to the best item for branching@>=
tmems=mems,t=max_nodes;
@y
@<Set |best_itm| to the best item for branching@>=
tmems=mems;
o,best_itm=cl[root].next;
o,t=nd[best_itm].len;
if (t>maxdeg) maxdeg=t;
cmems+=mems-tmems;

@ The unused original MRV code is retained in this documentation section.
@<Unused original MRV selection@>=
tmems=mems,t=max_nodes;
@z
