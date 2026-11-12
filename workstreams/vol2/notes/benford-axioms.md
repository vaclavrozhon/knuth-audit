# §4.2.4-18: důkaz přímo ze slabých axiomů

Kontrola 2. 11. 2026. Originály str.264 a622 přečteny vizuálně.
`P` je nezáporná, částečně definovaná funkce množin kladných celých čísel;
její obor je uzavřen na disjunktní konečná sjednocení, posun o1 a násobení2.
Platí aditivita na disjunktních množinách, `P(S+1)=P(S)`,
`P(2S)=P(S)/2` a `P(N)=1`. Dále je definována na všech
`L_a={n: a10^m<=n<(a+1)10^m pro některé celé m}`.
Záporné m jsou součástí zadání. Značme `p(a)=P(L_a)` a
`p(a,b)=sum_{a<=k<b}p(k)` pro celá `1<=a<b`.
Poslední zápis je číselný součet; pro velké b/a jej nezaměňujeme
za pravděpodobnost sjednocení překrývajících se množin.

Cílem je `p(a)=log10(1+1/a)`. Důkaz níže nepřidává uzavřenost oboru
P na rozdíly, komplementy nebo konečné množiny.

## 1. Proč je nutné ošetřit konečné výjimky

Desítkové rozdělení je přesné a disjunktní:

```
L_a = union_{i=0}^9 L_(10a+i),
p(a) = p(10a,10a+10).                                      (1)
```
Označme `T_a=2L_a union (2L_a+1)`. Sudá a lichá část jsou disjunktní,
P je na obou definována a `P(T_a)=p(a)`. Nelze však vždy ztotožnit
T_a s `L_(2a) union L_(2a+1)`. Například

```
L_10 union L_11 = T_5 union {1}.
```
Není dovoleno bez důkazu odečíst pravděpodobnost `{1}`: axiomy
její definovanost nepostulují. Tento problém se týká zdůvodnění mezikroku;
rovnost `p(a)=p(2a,2a+2)` je přesto správná, jak ukážeme.

## 2. Dvojice množin, která odstraní jediný bod

Definujme `d(a)=p(a)-p(2a)-p(2a+1)`. Pokud `5` nedělí `a`,
je `T_a=L_(2a) union L_(2a+1)` přesně, tedy `d(a)=0`.
Důvod: pro m>=0 lze interval rozdělit na sudé a liché body;
žádná ze tří příslušných množin nemá body pocházející z m<0.
Interval `[a/10^h,(a+1)/10^h)` totiž obsahuje celé číslo právě tehdy,
když `10^h` dělí a, a pak obsahuje jediný bod `a/10^h`.

Množiny L_1,...,L_9 rozdělují N, takže `p(1,10)=1`.
Podle (1) je `p(10,20)=p(1)` a tudíž `p(2,20)=1`.
Sečtením d(1),...,d(9) dostaneme0. Jediný dosud neznámý člen je
`d(5)`, a tedy i `d(5)=0`.

Položme nyní

```
A = L_10 union L_11,
B = T_5 = union_{m>=1} ([10^m,(6/5)10^m) intersect N).
```
Obě množiny leží v oboru P, `A=B union {1}` a `P(A)=P(B)`.
Neříkáme tím, že je P definována na samotném bodě.

## 3. Všechna a končící číslicí5

Pišme `a=5c`, kde c je kladné liché číslo. Případ c=1 je hotov.
Pro c>=3 položme

```
S = T_(5c) = union_{j>=0} ([10c10^j,(10c+2)10^j) intersect N),
R = L_(10c) union L_(10c+1) = S union {c}.
```
Poslední rovnost používá lichost c: 10c má právě jednu koncovou nulu,
takže jediný příspěvek záporného m je bod c.

Máme dvě pomocné dvojice se stejnou pravděpodobností:

```
A0=A+c-1,       B0=B+c-1,       A0=B0 union {c},
A1=2A+c-2,      B1=2B+c-2,      A1=B1 union {c}.
```
Posuny jsou nezáporné, všechny čtyři množiny jsou v oboru P,
`P(A0)=P(B0)` a `P(A1)=P(B1)`.

**Alespoň jedna z B0,B1 je disjunktní se S.** Následující odhad
platí dokonce pro všechna celá c>=3. Pokud se interval B0 s indexem m>=1
protne s intervalem S s indexem j>=0, porovnání obou krajů dává

```
15/2 < 10^(m-j)/c < 32/3.                                (2)
```
Skutečně horní kraj B0 je `(6/5)10^m+c-1` a dolní kraj S
je `10c10^j`; jejich ostrá nerovnost dává dolní mez větší než
`(10-1)/(6/5)=15/2`. Druhá nerovnost dává horní mez nejvýše
`10+2/c<=32/3`.
Pro průnik B1 a S analogicky dostaneme

```
15/4 < 10^(m-j)/c < 16/3.                                (3)
```
Zde používáme obal intervalů B1 s kraji `2*10^m+c-2`
a `(12/5)10^m+c-2`; mez zůstává platná i přes vynechané liché
či sudé body. Kdyby oba typy průniků existovaly, podíl příslušných
mocnin10 by ležel ostře mezi `45/32` a `128/45`, tedy mezi1 a10.
Taková celočíselná mocnina10 neexistuje. Tím je tvrzení dokázáno.

Vyberme i s `B_i intersect S=empty`. Ani B_i ani S neobsahuje c.
Pak existují dvě disjunktní rozdělení téže množiny:

```
R union B_i = S union A_i.
```
Axiom aditivity dává `P(R)+P(B_i)=P(S)+P(A_i)`, tedy `P(R)=P(S)`.
Odtud `d(5c)=0` pro všechna lichá c.

## 4. Obecné zdvojení

Použitím desítkového rozdělení (1) dostaneme

```
d(a)=sum_{i=0}^9 d(10a+i)=d(10a)+d(10a+5)=d(10a).
```
Prostřední rovnost používá nulovost d na číslech nedělitelných5;
poslední rovnost právě dokázaný případ koncové číslice5.
Odstraněním všech koncových nul z a proto dostaneme `d(a)=0`
pro každé kladné a. Tedy

```
p(a,b)=p(2a,2b)=p(10a,10b)
      =p(2^m 10^n a,2^m 10^n b),    m,n>=0.                (4)
```
Tím je sporný mezikrok tištěného důkazu uzavřen přesně za uvedených axiomů.

## 5. Závislost pouze na poměru

Pokud `1<b/a<b'/a'`, hustota grupy `{2^u10^v:u,v integer}`
v kladných reálných číslech dovolí vložit vhodně škálovaný interval
[a,b) do vhodně škálovaného [a',b'). Hustota plyne z iracionality
`log(2)/log(10)`: rovnost racionálnímu p/q by dala `2^q=10^p`,
což odporuje jednoznačnosti prvočíselného rozkladu. Hustota násobků
iracionálního čísla modulo1 byla dokázána v §3.5-22. Přidáním dostatečných
společných exponentů lze všechny čtyři škálovací exponenty zvolit
nezáporné. Použití (4) a nezápornosti jednotlivých p(k) dává

```
p(a,b)<=p(a',b').                                         (5)
```
Z toho plyne, že p(k) neroste s k. Pro celá A<B s B-A>=2 tedy

```
p(A,B) <= (B-A)/(B-A-1) * p(A,B-1).                        (6)
```
Nedělíme pravděpodobností, takže nepotřebujeme předem dokazovat její
kladnost. Při `b/a=b'/a'` aplikujeme (6) na `A=10^n a,B=10^n b`.
Poměr `(B-1)/A` je menší než b'/a', a (4)–(6) tak dávají
`p(a,b)<=(1+O(10^-n))p(a',b')`. Limitou a záměnou dvojic dostaneme
rovnost p pro stejné poměry.

## 6. Určení hodnoty

Interval `[a^n,b^n)` se rozdělí na n sousedních intervalů
s konci `a^n,ba^(n-1),...,b^n`; každý má poměr krajů b/a.
Proto `p(a^n,b^n)=n p(a,b)`.
Položme `m=floor(log10(a^n))`, `m'=floor(log10(b^n))`.
Z (1) a `p(1,10)=1` máme `p(10^u,10^v)=v-u` pro celá0<=u<v.
Vnořením intervalů (a při záporné dolní mezi pouhou nezáporností)
plyne

```
m'-m-1 <= n p(a,b) <= m'-m+1.                             (7)
```
Po vydělení n a limitě je `p(a,b)=log10(b/a)`, zejména požadované
`p(a)=log10(1+1/a)`.

Na str.622 je v poslední horní mezi vytištěno `m'+m+1` místo
`m'-m+1`. Tištěná slabší nerovnost je sama pravdivá, ale neposkytuje
uvedené limitní sevření. Správná mez (7) vyplývá přímo z předchozího
řádku. Tento typografický bod se eviduje odděleně od platnosti věty.

## Rozsah kontroly

Tento obecný důkaz uzavírá úlohu18; konečné testy množin nejsou jeho
náhradou. Pomocný skript ověřuje definici L_a včetně záporných m,
přesné výjimky a dostatečné disjunktní obaly na konečných případech.
Primární Jechův text pracuje s mírou na všech podmnožinách N, a proto
by sám neodstranil zdejší otázku částečného oboru P.
