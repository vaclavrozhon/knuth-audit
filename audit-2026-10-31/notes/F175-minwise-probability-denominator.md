# F175: The auxiliary minimum probability omits one element

Status: confirmed locally; low severity. TAOCP4B, first edition,
second printing PDF, p388/file408, answer MPR113(a).
Physical-copy verification and root acceptance are not asserted.

The answer defines A={k,...,n} union B, where B contains t elements
below k. Thus |A|=n−k+1+t, and minwise independence gives
P_B=1/(n−k+1+t). The printed denominator is n−k+t.

Take n=5,k=4 and choose uniformly from all120permutations.
In the displayed inclusion–exclusion example, the printed values yield

```
1−3/2+3/3−1/4 = 1/4.
```

The event requires4π=4, the images of1,2,3 to be1,2,3 in some
order, and5π=5. There are exactly3!=6 such permutations, so
its probability is6/120=1/20. The corrected denominators give

```
1/2−3/3+3/4−1/5 = 1/20.
```

All denominators in this witness are positive; the discrepancy does
not depend on an endpoint convention. In the smallest two-element
case n=2,k=1,t=0, the printed auxiliary probability is1 instead
of1/2. At k=n,t=0 it would even divide by zero.

Insert +1 in the denominator. The inclusion–exclusion signs and all
main conclusions of MPR113(a,b) remain valid, as proved in the full
audit note. No enumeration or numerical experiment is needed.

The same denominator appears in the original PDF and the author's
11September2019 Pre-Fascicle5A p45/file51. All six local official
errata layers and their three TeX sources were assessed; no applicable
correction was found. Only file408 is an error location.
