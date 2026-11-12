/* Audit reconstruction of the original answer11 prefix plus the 2002
   all2-prepre replacement, printed34-35. Default intentionally reproduces
   the undeclared x. -DAUDIT_REPAIR supplies the missing declaration only.
   This is not the separately published author source rng-double.c. */
#include <stdio.h>
#define KK 100
#define LL 37
#define mod_sum(x,y) (((x)+(y))-(int)((x)+(y)))
double ran_u[KK];
void ranf_array(double aa[],int n) {
  register int i,j;
  for (j=0;j<KK;j++) aa[j]=ran_u[j];
  for (;j<n;j++) aa[j]=mod_sum(aa[j-KK],aa[j-LL]);
  for (i=0;i<LL;i++,j++) ran_u[i]=mod_sum(aa[j-KK],aa[j-LL]);
  for (;i<KK;i++,j++) ran_u[i]=mod_sum(aa[j-KK],ran_u[i-LL]);
}
#define TT 70
#define is_odd(s) ((s)&1)
void ranf_start(long seed) {
  register int t,s,j;
  double u[KK+KK-1],ul[KK+KK-1];
  double ulp=(1.0/(1L<<30))/(1L<<22);
#ifdef AUDIT_REPAIR
  int x[KK+KK-1];
#endif
  /* Replacement begins here. The earlier declaration is retained. */
  double ss=2.0*ulp*((seed&0x3fffffff)+2);
  for (j=0;j<KK;j++) {
    x[j]=0; u[j]=ss;
    ss+=ss; if (ss>=1.0) ss-=1.0-2*ulp;
  }
  x[1]=1; u[1]+=ulp;
  for (s=seed&0x3fffffff,t=TT-1; t; ) {
    for (j=KK-1;j>0;j--)
      x[j+j]=x[j],u[j+j]=u[j],x[j+j-1]=0,u[j+j-1]=0.0;
    for (j=KK+KK-2;j>=KK;j--) {
      x[j-(KK-LL)]=x[j]^x[j-(KK-LL)],
        u[j-(KK-LL)]=mod_sum(u[j-(KK-LL)],u[j]);
      x[j-KK]=x[j]^x[j-KK],u[j-KK]=mod_sum(u[j-KK],u[j]);
    }
    if (is_odd(s)) {
      for (j=KK;j>0;j--) x[j]=x[j-1],u[j]=u[j-1];
      x[0]=x[KK],u[0]=u[KK];
      x[LL]=x[KK]^x[LL],u[LL]=mod_sum(u[LL],u[KK]);
    }
    if (s) s>>=1; else t--;
  }
  for (j=0;j<LL;j++) ran_u[j+KK-LL]=u[j];
  for (;j<KK;j++) ran_u[j-LL]=u[j];
  for (j=0;j<10;j++) ranf_array(u,KK+KK-1);
}
int main(void) {
  register int m; double a[2009];
  ranf_start(310952);
  for (m=0;m<2009;m++) ranf_array(a,1009);
  printf("%.20f\n",ran_u[0]);
  ranf_start(310952);
  for (m=0;m<1009;m++) ranf_array(a,2009);
  printf("%.20f\n",ran_u[0]);
  return 0;
}
