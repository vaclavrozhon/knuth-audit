/****************************************************************
Copyright (C) Lucent Technologies 1997
All Rights Reserved

Permission to use, copy, modify, and distribute this software and
its documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appear in all
copies and that both that the copyright notice and this
permission notice and warranty disclaimer appear in supporting
documentation, and that the name Lucent Technologies or any of
its entities not be used in advertising or publicity pertaining
to distribution of the software without specific, written prior
permission.

LUCENT DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL LUCENT OR ANY OF ITS ENTITIES BE LIABLE FOR ANY
SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.
****************************************************************/
/* word-square generator
   squares [-d] [-x layout] n [start]

   prints all word squares that can be constructed from the
   vocabulary of n-letter words given in standard input, one
   word per line, in alphabetic order, lower-case only

   -d omit squares with duplicate words; not effective with -x

   squares are produced in lexicographic order. if "start"
   string is present, that will be the first across string
   considered.  with a start given, progress reports will
   be printed each time a new first across string is considered;
   this can be used for restarting.

   if -x option is present, then a crossword pattern is
   given in the layout file.  n is the dimension of the
   square layout.  vocabulary input is one word per
   line arranged in blocks.  all words in a block have
   the same length and are in alphabetic order.  blocks
   are separated by empty lines.  blocks are in increasing
   order of word length.

   a layout file looks like
	oooxx
	oooox
	ooooo
	xoooo
	xxooo
   each of the n lines has n o's and x's, with o for white
   squares and x for black.
*/
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SPACE 80000
#define N 16

/* strings are stored in tries, one trie per string size.  all the
   branches for one trie node are kept contiguously in alphabetical
   order, with character c = 0 at end */

typedef struct trie {
	char c;
	struct trie *t;
} trie;

void
fatal(char *s)
{
	void abort(void);
	fprintf(stderr,"%s\n",s);
	abort();
}

int n;		/* lengths of strings */
char *xfile;	/* name of xword layout file */
char line[N];

/* fill line[] with next string.  return number of first byte
   in which this line disagrees with preceding line
*/

int
readline(char line[N])
{
	int i, c;
	int p = -1;
	for(i=0; ; i++) {
		if(i >= N)
			fatal("line overflow");
		switch(c = getchar()) {
		case EOF:
			return -1;
		case '\n':
			if(i == 0)	/*slime: don't touch "line"*/
				return -1;
			line[i] = 0;
			if(p == -1)
				fatal("equal words");
			return p;
		default:
			if(!islower(c))
				fatal("non-lower-case char");
			if(p<0 && c!=line[i])
				if(c < line[i])
					fatal("disordered word");
				else
					p = i;
			line[i] = c;
		}
	}
}

trie space[SPACE];	/* where tries are grown */
trie *spend = space;	/* end of used space */
trie null;

struct trie *
input(int i)
{
	static change;
	static len;
	int k = 0;
	trie t['z'-'a'+2], *s;
	if(i == 0)
		change = readline(line);
	if(change == -1)
		return 0;
	len = strlen(line);
	for(;;) {
		t[k].c = line[i];
		if(i < len-1)
			t[k].t = input(i+1);
		else {
			t[k].t = 0;
			change = readline(line);
			if(strlen(line) != len)
				fatal("mixed sizes in input");
		}
		if(++k >= sizeof(t)/sizeof(*t))
			fatal("node overflow");
		if(change < i)
			break;
	}
	t[k++] = null;
	s = spend;
	spend += k;
	if(spend > space+SPACE)
		fatal("out of space");
	memcpy((char*)s, (char*)t, k*sizeof(*t));
	return s;
}


void
output(trie *t, int lev)
{
	int i;
	if(t == 0)
		return;
	for( ; t->c; t++) {
		for(i=0; i<lev; i++)
			putchar(' ');
		putchar(t->c);
		putchar('\n');
		output(t->t, lev+1);
	}
}

typedef struct square {
	trie *atrie;
	trie *dtrie;
	char asize;	/* length of across word beginning here, or 0 */
	char dsize;
	char cover;	/* zero for black squares, nonzero for white */
} square;

square squares[N*N];
square *last;
int dflag;
int pflag;
int sflag;
trie oneletter[] = {
	{'a'},{'b'},{'c'},{'d'},{'e'},{'f'},{'g'},
	{'h'},{'i'},{'j'},{'k'},{'l'},{'m'},{'n'},
	{'o'},{'p'},{'q'},{'r'},{'s'},{'t'},{'u'},
	{'v'},{'w'},{'x'},{'y'},{'z'},0 };
trie *root[N+1] = { 0, oneletter };

void
readxox(void)
{
	int i, j;
	FILE *f;
	if(xfile == 0) {
		for(j=0; j<n*n; j++)
			squares[j].cover = 2;
		return;
	}
	f = fopen(xfile,"r");
	if(f == 0)
		fatal("cannot open layout file");
	for(i=0; i<n; i++) {
		for(j=0; j<n; j++) {
			switch(getc(f)) {
			case 'o':
				squares[n*i+j].cover = 2;
				continue;
			case 'x':
				continue;
			case EOF:
				fatal("missing layout info");
			default:
				fatal("garbage in layout");
			}
		}
		if(getc(f) != '\n')
			fatal("misaligned layout");
	}
	if(getc(f) != EOF)
		fatal("wrong size layout");
}

void
wordheads(void)
{
	int i,j,k;
	for(i=0; i<n; i++) {
		for(j=0; j<n; j++) {
			if((i==0 || !squares[n*(i-1)+j].cover) &&
				   squares[n*i+j].cover) {
				for(k=i+1; k<n; k++)
					if(!squares[n*k+j].cover)
						break;
				if(root[k-i] == 0)
					fatal("need another length");
				squares[n*i+j].dtrie = root[k-i];
				squares[n*i+j].dsize = k - i;
			}
			if((j==0 || !squares[n*i+j-1].cover) &&
				   squares[n*i+j].cover) {
				for(k=j+1; k<n; k++)
					if(!squares[n*i+k].cover)
						break;
				if(root[k-j] == 0)
					fatal("need another length");
				squares[n*i+j].atrie = root[k-j];
				squares[n*i+j].asize = k - j;
			}
		}
	}
}

/* When a word is identified, check it against all
   across words that have been placed. */

int
adup(square *s, trie *a)
{
	square *t;
	for(t=squares+n-1; t<s; t+=n)
		if(t->atrie == a)
			return 1;
	return 0;
}

int
ddup(square *s, trie *d)
{
	square *t;
	for(t=squares+n*(n-1); t<s; t++)
		if(t->dtrie == d)
			return 1;
	return adup(s, d);
}

void
print(void)
{
	int i, j;
	for(i=0; i<n; i++) {
		for(j=0; j<n; j++)
			if(squares[n*i+j].cover)
				putchar(squares[n*i + j].atrie->c);
			else
				putchar(' ');
		putchar('\n');
	}
	putchar('\n');
	fflush(stdout);
}

void
debug(square *s)
{
	printf("%d %d\n",(s-squares)/n,(s-squares)%n);
	output(s->atrie, 0);
	printf("------\n");
	output(s->dtrie, 0);
}

/* record the exhaustion of all possibilities with a particular
   first word; assumes there is a word in first row */

void
progress(void)
{
	square *s;
	for(s=squares; !s->cover; s++) ;
	for( ; s<squares+n && s->cover; s++)
		fprintf(stderr, "%c", s->atrie->c);
	fprintf(stderr, "*\n");
	fflush(stderr);
}

void
gen(square *s, char *start)
{
	trie *a, *d;
	square *succ, *above;
	for( ; ; s->atrie++, start="") {
		a = s->atrie;
		d = s->dtrie;
		if(a&&!d || d&&!a)
			fatal("one trie missing");
		if(a) {
			if(*start) {
				while(a->c && a->c<*start)
					a++;
				start++;
			}
			for(;;) {
				if(a->c==0 || d->c==0)
					return;
				if(a->c == d->c)
					break;
				if(a->c < d->c)
					a++;
				if(d->c < a->c)
					d++;
			}
			if(pflag && s==squares+n-1)
				progress();
			s->atrie = a;
			s->dtrie = d;
			if(dflag) 
				if(d->t==0 && ddup(s,d) ||
				   a->t==0 && adup(s,a))
					continue;
		}
		succ = s + 1;
		if(succ >= last) {
			if(!dflag || !ddup(s,a) && a!=d)
				print();
		} else {
			if(succ->asize)
				succ->atrie = root[succ->asize];
			else if(succ->cover)
				succ->atrie = s->atrie->t;
			if(succ->dsize)
				succ->dtrie = root[succ->dsize];
			else if(succ->cover)
				succ->dtrie = (succ-n)->dtrie->t;
			gen(succ, start);
		}
		if(!a)
			return;
	}
}

main(int argc, char **argv)
{
	trie *s;
	for( ; argc>1 && argv[1][0]=='-'; argc--,argv++) {
		if(strcmp(argv[1],"-s") == 0)
			sflag++;
		if(strcmp(argv[1],"-d") == 0)
			dflag++;
		else if(strcmp(argv[1],"-x") == 0) {
			xfile = argv[2];
			argv ++;
			argc --;
		}
	}
	if(argc < 2)
		fatal("arg count");
	n = atoi(argv[1]);
	if(n<=0 || n>=N)
		fatal("bad string size");
	last = squares + n*n;
	while(s = input(0)) {
		root[strlen(line)] = s;
		line[0] = 0;
	}
	readxox();
	wordheads();
	pflag = argc >= 3;
	gen(squares, argv[2]?argv[2]:"");
	return 0;
}
