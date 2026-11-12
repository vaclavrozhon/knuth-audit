# §1.2.9-19: Gaussův vzorec pro racionální harmonická čísla

Audit 1. listopadu 2026. Originály s. 95, 497–498 zobrazeny.
Pro reálné x>-1 definujeme zobecněné harmonické číslo

```text
H_x=sum_{n>=1}(1/n-1/(n+x)).                           (H1)
```

Řada je absolutně konvergentní, protože její členy jsou
x/(n(n+x))=O(n^-2). Pro celá x>=0 teleskopuje na obvyklý
součet 1+1/2+...+1/x. Zadání používá tuto definici z již
prověřené úlohy 1.2.7-24. V prvním dotisku je v definici
poškozená závorka; oprava z 17. července 1997 ji napravuje.

Pro celá 0<p<q dokážeme

```text
H_(p/q)=q/p-(pi/2)cot(pi p/q)-log(2q)
       +2 sum_{0<k<q/2} cos(2pi pk/q) log sin(pi k/q).  (H2)
```

Nesoudělnost p,q není potřeba. Všechny reálné logaritmy
na pravé straně mají kladný argument.

## Filtr pomocí kořenů jednotky

Položme omega=exp(2pi i/q). Pro reálné 0<x<1 zaveďme

```text
A(x)=sum_{n>=1}(1/n-1/(n+p/q)) x^(p+nq),
f(x)=sum_{k=1}^{q-1} omega^(-kp) log(1-omega^k x),
g(x)=(1-x^p)log(1-x)+(q/p)x^p
                         -x^p log((1-x^q)/(1-x)).     (H3)
```

Komplexní logaritmus je analytická větev s log(1)=0,
získaná řadou uvnitř |omega^k x|<1. Filtr kořenů jednotky
z `generating-basic.md` dává

```text
sum_{k=0}^{q-1}omega^(-kp)log(1-omega^k x)
       =-q sum_{j>=0}x^(p+jq)/(p+jq).                  (H4)
```

Dosazením (H4) a `sum_{n>=1}x^(nq)/n=-log(1-x^q)`
dostaneme přesnou identitu A(x)=f(x)+g(x).

Koeficienty A jsou O(n^-2), takže dominovaná konvergence
dává lim_(x->1-) A(x)=H_(p/q); postačuje dokonce přímo
stejnoměrná absolutní konvergence na [0,1]. Není nutné
použít silnější obecnou Abelovu limitní větu. Dále
`(1-x^p)log(1-x)->0` a `(1-x^q)/(1-x)->q`, tudíž

```text
lim_(x->1-) g(x)=q/p-log q.                            (H5)
```

## Vyhodnocení konečné logaritmické sumy

Pro 0<theta<2pi je

```text
1-exp(i theta)=2 sin(theta/2) exp(i(theta-pi)/2),
log(1-exp(i theta))=log 2+log sin(theta/2)
                                       +i(theta-pi)/2. (H6)
```

Argument (theta-pi)/2 leží mezi -pi/2 a pi/2, takže
odpovídá spojitému přiblížení z x<1; žádná větev se nemění.
Po dosazení theta=2pi k/q se f(1) rozpadá na část s log sin
a zbývající část. Položíme v=omega^(-p), kde v^q=1,v!=1.
Konečná geometrická řada a její derivace dávají
`sum_{k=1}^{q-1}v^k=-1` a `sum_{k=1}^{q-1}k v^k=q/(v-1)`.
Zbývající část je tedy

```text
-log 2+i pi/2+i pi/(v-1)
                 =-log 2-(pi/2)cot(pi p/q).            (H7)
```

Páry k a q-k v druhé části dávají
`2 cos(2pi pk/q)log sin(pi k/q)`. Je-li q sudé, prostřední
index k=q/2 přispívá nulou, protože log sin(pi/2)=0.
Sečtení s (H5) dokazuje (H2).

V původním posledním řádku odpovědi 19 jsou špatná
znaménka před kotangentou a v mezivýrazech. To je již
publikovaná oprava z 1. ledna 2006 (`all1-prepre`, strana 34).
Tentýž den byla opravena také záměna f(x) za f(1) v limitním
řádku. Oba opravené kroky odpovídají (H5)–(H7).

## Tři úvodní příklady

Seskupení po sousedních dvojicích v konvergentních
alternujících řadách a (H1) dávají

```text
sum_{n>=0}(-1)^n/(n+1) =1-H_(1/2)/2,
sum_{n>=0}(-1)^n/(2n+1)=2/3-H_(1/4)/4+H_(3/4)/4,
sum_{n>=0}(-1)^n/(3n+1)=3/4-H_(1/6)/6+H_(2/3)/6.       (H8)
```

Jednotlivé párové členy jsou rozdíly dvou reciprokých
aritmetických posloupností. Například pro obecné a>0
`sum_{j>=0}(1/(j+a)-1/(j+b))=H_(b-1)-H_(a-1)`;
posun H_x=H_(x-1)+1/x převádí záporné argumenty na (H8).
Dosazení (H2), případně přímé integrály
`integral_0^1 1/(1+t)dt`, `integral_0^1 1/(1+t^2)dt`,
`integral_0^1 1/(1+t^3)dt`, dává postupně

```text
log 2,    pi/4,    log 2/3 + pi sqrt(3)/9.              (H9)
```

Pro poslední integrál použijeme přesný rozklad
`1/(1+t^3)=(1/3)/(1+t)+(2-t)/(3(1-t+t^2))`.
Doplnění čtverce v druhém jmenovateli dává (H9).
Integrace geometrických částečných součtů je oprávněná:
zbytek má absolutní integrál nejvýše 1/(a(N+1)+1)
pro řadu s t^(an), takže jde k nule. Alternující řady
se tu nesčítají jako dvě divergentní řady odděleně.

Matematický výsledek je uzavřen. Primární Gaussova §33,
rovnice [75], a Abelův článek z roku 1826 dosud nebyly
ověřeny; historické tvrzení o nedostatečnosti Gaussova
důkazu proto zůstává samostatně `partial`.
