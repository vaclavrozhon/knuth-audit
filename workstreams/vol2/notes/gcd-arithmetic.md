# §4.5.2: poslední dvě úlohy41/42

Zadání356 a odpověď646–647 byly zkontrolovány v sazbě.
Všechny čtyři vrstvy errat prohledány podle stran, úloh a obsahu;
odpovídající nová oprava ani chyba nenalezena.

## 41: společný dělitel čísel a^m-1

Pro kladný celočíselný základ a a nezáporné exponenty m,n platí

```text
gcd(a^m-1,a^n-1)=a^gcd(m,n)-1.                          (1)
```

Používáme gcd(0,0)=0. Při a=1 jsou všechny členy0, takže(1)
platí přímo. Při n=0 je pravá i levá strana a^m-1; obdobně
při m=0. Ve zbývajícím případě a>=2,n>0 napišme m=qn+r,
0<=r<n. Geometrický součet dává

```text
a^m-1 = (a^n-1) a^r (1+a^n+...+a^((q-1)n)) + (a^r-1).
```

Při q=0 je součet prázdný. Poslední člen leží v intervalu
[0,a^n-1), tedy je přesným zbytkem. Eukleidovy kroky na
exponentech proto odpovídají krokům na původních číslech
a končí výrazem(1). Pro a=10 dostáváme požadovanou odpověď.
Nulový dělitel se nepoužívá v operaci mod; je to samostatný
koncový případ, nikoli výjimka z výsledné identity.

## 42: determinant a obecná funkce gcd

Nechť n>=1 a f je libovolná číselná funkce na kladných celých
číslech. Definujeme Möbiovu funkci mu: mu(1)=1, mu(k)=0,
pokud je k dělitelné druhou mocninou prvočísla, jinak mu(k)=(-1)^r,
kde r je počet jeho různých prvočíselných dělitelů. Položme

```text
g(k)=sum_{d|k} mu(k/d) f(d).
```

Identita sum_{d|k} mu(d)=[k=1], plynoucí z rozvoje součinu
(1-1) přes různá prvočísla, dává f(k)=sum_{d|k} g(d).
Hranatá závorka má hodnotu1 při pravdivé podmínce, jinak0.
Definujeme n krát n matici E s E_(i,d)=[d|i] a diagonální
matici D s D_(d,d)=g(d). Matice E je dolní trojúhelníková
s jedničkami na diagonále. Potom

```text
(E D E^T)_(i,j) = sum_{d|i,d|j} g(d) = f(gcd(i,j)).
```

Transpozice E^T prohodí řádky a sloupce. Protože det(E)=1,
obecný Smithův determinant je

```text
det[f(gcd(i,j))] = product_{k=1}^n g(k).                 (2)
```

Žádná nenulovost hodnot f nebo g není potřebná: rozklad
nepoužívá dělení. Platí i pro záporné nebo komplexní hodnoty.

Při f(k)=k dostáváme g(k)=phi(k), kde phi(k) je počet čísel
1<=r<=k nesoudělných s k, s phi(1)=1. Identita
sum_{d|k} phi(d)=k plyne z rozdělení čísel1..k podle jejich
gcd s k: skupina s gcd=k/d má phi(d) prvků. Inverze pak
ukazuje g=phi a determinant je phi(1)...phi(n).

Tištěné sloupcové operace mají stejný význam. Při rostoucím
k odečítáme již upravený sloupec k od sloupců2k,3k,... .
Výsledný sloupec j je původní sloupec j minus součet
výsledných sloupců jeho vlastních dělitelů. Indukcí má
na řádku i hodnotu g(j)[j|i]. Výsledek je přesně E D,
dolní trojúhelníková matice s diagonálou g(j); determinant
se při těchto operacích nezměnil. Pořadí operací je tedy
podstatné a odpověď je udává správně.

## Kontrola a zdrojový rozsah

Čtvrtý checkpoint `verify_gcd_variants.py --resume` ověřil
7623 dvojic exponentů pro základy1,2,3,5,10,16,256 včetně nul,
a64 matic do rozměru16 pro identitu, konstantní, nulové a
náhodné celočíselné funkce. Přímý Bareissův determinant je
porovnán s(2),5984 prvků je navíc zkontrolováno po přesných
tištěných sloupcových operacích. Výsledek exit0, relace3788;
předchozí tři úspěšné checkpointy nebyly znovu spuštěny.

Historický odkaz na Dicksona122–123 byl ověřen vizuálním čtením
[původního svazku](https://archive.org/details/historyoftheoryo01dick),
viz metadata `sources/dickson-1919-gcd.json`. Text zde uvádí
základní determinant i libovolnou funkci f; poznámka39 odkazuje
na Smitha, Proc. London Math. Soc.7(1875–6),208–212 a Collected
Papers2,161. Samotný Smithův článek nebyl přečten. Ostatní
historické věty na těchto dvou stranách nejsou předmětem auditu.
