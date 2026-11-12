@x
level=0;
@y
level=LL=0;
@z

@x
@<Set |best_itm| to the best item for branching@>;
cover(best_itm);
@y
if (level==LL) o,best_itm=cl[root].next;
else { @<Set |best_itm| to the best item for branching@>; }
cover(best_itm);
@z

@x
level--;
oo,cur_node=choice[level],best_itm=nd[cur_node].itm;
@y
level--;
if (level<LL) LL=level;
oo,cur_node=choice[level],best_itm=nd[cur_node].itm;
@z

@x
int level; /* number of choices in current partial solution */
@y
int level; /* number of choices in current partial solution */
int LL; /* all levels up to this frontier use canonical first-item order */
@z

@x
@ @<Record solution and |goto recover|@>=
{
  count++;
@y
@ @<Record solution and |goto recover|@>=
{
  if (level>LL) {
    LL++;
    while (level>=LL) {
      oo,cur_node=choice[level],best_itm=nd[cur_node].itm;
      @<Uncover all other items of |cur_node|@>;
      uncover(best_itm);
      level--;
    }
    level++;
    goto forward;
  }
  count++;
@z
