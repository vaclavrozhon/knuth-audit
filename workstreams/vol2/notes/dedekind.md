# §3.3.3: věta P, Dedekindovy součty a celočíselný algoritmus

Audit1.11.2026. Tento blok uzavírá matematiku hlavního textu
str.80–89 a původní úlohy1–17 včetně nové úlohy3 z2001.
Konec textu str.90 a úlohy18–28 se dokončí v navazujícím bloku.
Původní stránky80–92,572–574 a relevantní historická errata
byly vizuálně přečteny. **Nový nález je pouze C0032**, chybný
index v pomocné nerovnosti odpovědi12. Věty P, B, D, K,
algoritmus D a čtyři hlavní příklady souhlasí v rozsahu níže.

## 1. Značení a evidence

`floor(x)` je největší celé číslo nejvýše x, `ceil(x)` nejmenší
celé číslo nejméně x. `delta(x)` je1 pro celé x, jinak0;
hranaté závorky `[tvrzení]` mají stejný význam pravdivostního
indikátoru. Pilovitá funkce je

```text
psi(x)=x−floor(x)−1/2+delta(x)/2.
```

Je periodická s periodou1, lichá a v celých bodech nulová.
V knize se píše `((x))`. Dedekindův součet znamená

```text
sigma(h,k,c)=12 sum_(j=0)^(k−1) psi(j/k) psi((hj+c)/k),   k>0.
```

Používáme přesné racionální počty. [Program](../verify_dedekind.py)
a [výsledky](../results/dedekind.json) oddělují přímou definici,
Eukleidův algoritmus a skutečné periody generátoru. Sedm bloků
prošlo; šest původních se po přidání sedmého neopakovalo.

| Kontrola | Rozsah |
|---|---:|
| Součtová identita pro podlahy | 3480 případů |
| Replikační zákon a Fineova identita | 11088 případů každé |
| Celočíselná reciprocita a Cauchyův odhad | 26021 trojic |
| Posunutí c; Bézoutova identita | 3618;1617 případů |
| Reálné c; škálování | 1845;1230 případů |
| Definice versus věta D a algoritmus D | 105389 trojic |
| Mocninná teleskopická identita | 421556 případů |
| Skutečné generátory s plnou periodou | 3925 orbit, m<=80 |
| Rademacherova identita a prostorové počítání | 1144 trojic |
| Věta K, maximum a vážené podlahy | 1965 dvojic,105388 hodnot |
| Komplexní vzorec odpovědi13 | 312 případů,90 desetinných míst |

Poslední řádek je numerická kontrola, **nikoli intervalový
certifikát**. Obecný důkaz níže na numerice nezávisí.

Relevantní errata:8.11.1997 doplňuje číslo(6),13.6.2001 mění
odkaz pod(10), odstraňuje starou2, přečísluje Fourierovu3 na2
a přidává Fineovu3;25.7.2005 mění rok1978 na1977;
25.2.1999 opravuje index součtu na str.90;28.9.2002 mění
`math.` na `Math.` v odpovědi9. Opravy22/23 se uplatní
v dalším bloku. Všechny čtyři vrstvy a aktuální TeX
prohledány; PDF `all2-prepre` str.5,6,32 přečteno vizuálně.
Oprava na str.577 z2003 již patří §3.3.4-3.

## 2. Podlahy, pilovitá funkce a věta P

Pro celé h, kladné celé k, reálné c a `g=gcd(h,k)` platí

```text
sum_(j=0)^(k−1) floor((hj+c)/k)
 = ((h−1)(k−1)+g−1)/2 + g floor(c/g).                 (A)
```

Po rozdělení indexů modulo k/g jsou zbytky násobků h/g
permutací všech zbytků modulo k/g; jejich součet je známý.
To dokazuje(A), včetně záporného h a necelého c.
Stejným rozdělením dostáváme replikační zákon

```text
sum_(j=0)^(n−1) psi(x+j/n)=psi(nx),   n>=1.           (B)
```

Delta členy ošetřují přesně situaci, kdy nx je celé.
Úloha1 plyne přímo z definice: pro y!=0 je
`x mod y=y psi(x/y)+y/2−y delta(x/y)/2`, s podlahovou
definicí zbytku i pro záporné y. Původní úloha2 je(B).

U generátoru plné periody m>1 položme `s(x)=(ax+c) mod m`,
`b=a−1`, `d=gcd(b,m)`. Všechny stavy x se objeví jednou,
žádný není pevný a `c mod d` leží mezi1 a d−1.
Rozdíl `x−s(x)` je mezi−m a m, takže

```text
[s(x)<x] = ceil((x−s(x))/m)
         = floor((ax+c)/m)−floor((bx+c)/m).
```

Použití(A) a `gcd(a,m)=1` dává počet poklesů
`(m+2(c mod d)−d)/2`. Jejich pravděpodobnost se tedy liší
od1/2 o méně než d/(2m), jak tvrdí věta P. Druhý důkaz
v knize používá(B): součet `x−s(x)` je0 a součet
`psi((bx+c)/m)` je `d psi(c/d)`. Obě cesty souhlasí.

Pro úlohu4 je `10^10=2^10·5^10`. Valuace, tedy exponenty
prvočísel v b, splňují `v2(b)>=2,v5(b)>=1`. Potence je
`max(ceil(10/v2(b)),ceil(10/v5(b)))`; hodnota10 vynucuje
`v5(b)=1`. Největší d je proto `2^10·5=5120`, dosažitelné
vhodným b. Vytištěná mez chyby `1/(2·5^9)` je správná.

Fourierova řada (původní3, nyní2) je
`psi(x)=−sum_(n>=1) sin(2pi nx)/(pi n)`. Koeficienty
vycházejí integrací x−1/2 na(0,1); Dirichletova věta
dává u skoků střed jednostranných limit, tedy0. Není zde
třeba stejnoměrná konvergence. Nová Fineova úloha3 plyne
z(B) pro n2: `psi(x+1/2)=psi(2x)−psi(x)`. Součet
teleskopuje na `psi(2^n x)−psi(x)`, jehož absolutní
hodnota je ostře menší než1, protože `−1/2<psi<1/2`.
Fine1949 bibliograficky ověřen; konkrétní str.401 článku
není zde označena za přečtenou. Důkaz je samostatný.

## 3. Korelace a Cauchyova nerovnost

Pro plnou periodu definujme `x'=−a^(-1)c mod m`, tedy
jediný nenulový stav se s(x')=0. Rozepišme
`x/m=psi(x/m)+(1−[x=0])/2` a obdobně s(x).
Součty obou pilovitých vektorů jsou0. Násobení dává

```text
sum_x x s(x)/m² = sigma(a,m,c)/12 + m/4−(c+x')/(2m).
```

Dosazení do definice sériové korelace C a použití součtů
x a x² pak dává přesně(17):

```text
C=(m sigma(a,m,c)−3+6(m−x'−c))/(m²−1).              (C)
```

Pro nesoudělná h,k a celé c jsou oba pilovité vektory
permutacemi téhož vektoru. Cauchyova nerovnost proto dává

```text
|sigma(h,k,c)| <= sigma(1,k,0)=(k−1)(k−2)/k.         (D)
```

Úloha12 a její použití jsou správné. Pouze pomocný vzorec
v odpovědi má h místo1: [C0032](C0032-dedekind-cauchy-index.md).
Z(C),(D), `1<=c,x'<=m−1` plyne
`|C−sigma(a,m,c)/m|<6/m`; mez platí i v malých případech.

## 4. Symetrie a posunutá reciprocita

Záměnou j za k−j a lichostí psi dostáváme
`sigma(h,k,c)=sigma(h,k,−c)=−sigma(k−h,k,c)` (úloha10).
Rozdělení indexu do tvaru ik+j a(B) dává
`sigma(dh,dk,dc)=sigma(h,k,c)` pro d kladné celé
a libovolné reálné c (úloha11a).

Označme h' inverzi h modulo k. Pro celé c a `0<theta<1`
je směrnice součtu vůči theta nulová; jediný skok
pochází z indexu `hj+c=0 mod k`. Tedy

```text
sigma(h,k,c+theta)=sigma(h,k,c)+6 psi(h'c/k).         (E)
sigma(h,k,c)=sigma(h,k,0)
 +12 sum_(0<j<c) psi(h'j/k)+6 psi(h'c/k),  c>=0.    (F)
```

(F) lze také dostat indukcí z diskrétního rozdílu psi,
který má dva poloviční příspěvky delta (odpověď6a).
Jsou-li `hh'+kk'=1`, pak pro `0<j<k`

```text
psi(h'j/k)+psi(k'j/h)=j/(hk)−delta(j/h)/2.           (G)
```

Argumenty na levé straně mají součet v(0,1); jejich
podlahy mají součet−1, vyjma celočíselného krajního
případu, který přesně ošetří delta. Součet(G) v(F)
dokazuje posunutou reciprocitu(21), a z klasické
reciprocity pro c0 pak plyne lemma B:

```text
sigma(h,k,c)+sigma(k,h,c)
 = h/k+k/h+1/(hk)+6c²/(hk)−6 floor(c/h)−3e(h,c),
e(h,c)=[c=0]+[c mod h != 0],  0<=c<k.              (H)
```

Pro reálné c se v(H) pouze c² nahradí
`floor(c) ceil(c)`; plyne to z(E) a(G). To je úloha15.

## 5. Klasická reciprocita: dva důkazy

V kořenovém důkazu je `omega=exp(2pi i/k)` a
`zeta=exp(2pi i/h)`. Sken str.85 potvrzuje h v druhém
jmenovateli; OCR zde bylo chybné. Konečný Fourierův
rozklad(23) má správný faktor1/k. Diferenciací
`1+x+...+x^(k−1)` a filtrováním kořenů dostáváme

```text
psi(r/k)=1/k sum_(j=1)^(k−1) omega^(−jr)/(omega^j−1)
         −1/(2k)+delta(r/k)/2.
```

Násobení dvou rozkladů a součet přes r dává(25),(26).
Racionální funkce `(x−1)^2/((x^h−1)(x^k−1))` má pro
nesoudělná h,k jednoduché póly v nenulových kořenech
jednotky různých řádů. Rezidua dávají rozklad(29).
Polovina druhé derivace u x1 má podle Taylorova rozvoje
příslušný koeficient; celá druhá derivace je

```text
h/(6k)+k/(6h)+1/(6hk)+1/2−1/(2h)−1/(2k).
```

Porovnáním s(26) vyjde
`sigma(h,k,0)+sigma(k,h,0)=h/k+k/h+1/(hk)−3`.
Případ h=k=1 je triviální samostatně; v něm je racionální
funkce konstantní a čistý pólový rozklad není použitelný.
To není protipříklad lemmatu B.

Úloha7 nabízí nezávislé počítání mřížových bodů. Položme
`f_j=floor(hj/k)`. Součet `f_j(f_j+1)` je
`2 sum_i i·#{j:ki/h<j<k}`. Proto

```text
sum_(j=1)^(k−1) f_j(f_j+1)
 +2 sum_(i=1)^(h−1) i(floor(ki/h)+1)=kh(h−1).
```

Každé i přispěje přesně2ki. Nahradíme-li podlahy
pilovitou funkcí, dostaneme vytištěný rozvoj na str.573;
jeho konstantní člen je **+1/4**, jak potvrzuje zvětšený
sken. Po dosazení sigma(1,k,0) vychází tatáž reciprocita.

V úloze13 se ve Fourierově součinu ponechá posun c.
Delta členy na obou koncích a jejich společný výskyt
dávají `6(c mod k)/k−6 psi(h'c/k)`, zatímco kořenový
součet nese faktor `omega^(−cj)`. To potvrzuje celý
vytištěný vzorec;312 numerických kontrol jej doplňuje.

## 6. Rademacherova identita (8/9)

Definujme `rho(p,q,r)=12 sum_(j=0)^(r−1)
psi(pj/r)psi(qj/r)` pro kladná p,q,r po dvou nesoudělná.
Tvrzení je `sum_cyc rho=p/(qr)+q/(rp)+r/(pq)−3`.

Komplexní důkaz: integrujme
`cot(pi pz)cot(pi qz)cot(pi rz)` po obdélníku šířky1
s hranicemi mimo póly a s výškou rostoucí do nekonečna.
Svislé strany se zruší; vodorovné dávají−2i.
Reziduum v celočíselném pólu je
`−(p²+q²+r²)/(3pi pqr)`. Ostatní póly mají součet
reziduí `sum_cyc rho/(3pi)`, pomocí konečného Fourierova
rozkladu z předchozího oddílu. Reziduová věta dává výsledek.

Elementární důkaz úlohy9: v kvádru
`1<=i<p,1<=j<q,1<=l<r` má právě jedna z hodnot
i/p,j/q,l/r největší hodnotu. Shody vylučuje nesoudělnost.
Rozdělení podle maxima dává vytištěnou identitu

```text
sum_cyc sum_(j=0)^(r−1) floor(pj/r)floor(qj/r)
 = (p−1)(q−1)(r−1).
```

Pro úplnost definujme `M2(v)=(v−1)(2v−1)/(6v)` a
`W(u,v)=sum_(j=1)^(v−1) j floor(uj/v)`.
Rozvinutí dvou pilovitých funkcí dává

```text
sigma(u,v,0)/12=u M2(v)−W(u,v)/v−(v−1)/4,
rho(p,q,r)/12=pq M2(r)−p W(q,r)/r−q W(p,r)/r
             +sum_j floor(pj/r)floor(qj/r)−(r−1)/4.
```

Sečteme druhý řádek cyklicky a páry W odstraníme prvním
řádkem a klasickou reciprocitou. Zbývá požadovaná identita;
symbolická kontrola přesně zjednodušila rozdíl na0.
Carlitz1954 má správný název a stránky391–397 podle DOI
metadat; samotný článek zde není označen za přečtený.
Vlastní důkazy nestojí na nepřečtené citaci.

## 7. Eukleidův rozklad a algoritmus D (16/17)

Začněme `m1=k,m2=h,c1=c` a definujme
`a_j=floor(m_j/m_(j+1))`, `m_(j+2)=m_j mod m_(j+1)`,
`b_j=floor(c_j/m_(j+1))`, `c_(j+1)=c_j mod m_(j+1)`.
Poslední řádek má `m_(t+1)=1,m_(t+2)=0`; s je první
index s c_s=0. Jsou-li p_j jmenovatele konvergentů,
tedy `p_(-1)=0,p0=1,p_j=a_j p_(j−1)+p_(j−2)`, indukce dává

```text
m1=p_r m_(r+1)+p_(r−1) m_(r+2),
sum_(j=1)^r (−1)^(j+1)/(m_j m_(j+1))
 =(−1)^(r+1) p_(r−1)/(m1 m_(r+1)).                 (I)
```

Teleskopování(H) mění sumu obou poměrů na
`h/k+sum_j(−1)^(j+1)a_j`. Součet reciprokých součinů
je podle(I) `h'/k−[t sudé]`. Pro indikátory e platí

```text
sum_j (−1)^(j+1)e(m_(j+1),c_j)
 =(1−(−1)^t)/2−[s>1](−1)^s.
```

Tím vznikne přesně věta D včetně konstant
`3((−1)^s+[s=1])−2+(−1)^t`. Případ c0 je zahrnut.

Pro úlohu16 aplikujme součtovou integraci per partes
na(I) s vahami c_j^e a `c_(t+1)=0`. Dostáváme

```text
sum_j (−1)^(j+1)c_j^e/(m_j m_(j+1))
 = (1/m1) sum_j (−1)^(j+1) b_j p_(j−1)
                         (c_j^e−c_(j+1)^e)/(c_j−c_(j+1)).
```

Při shodných c je člen nulový, protože b_j=0; podíl lze
chápat spojitě, pro celočíselné e jako součet monomů.
Není správné vyhodnocovat pomocný zápis doslovně jako0/0.
Pro e2 je podíl c_j+c_(j+1), a dostáváme tištěné zadání.

Algoritmus D drží `p=p_(j−1),p'=p_(j−2),s=(−1)^(j+1)`.
A kumuluje celočíselné členy(H), B čitatele podle(I)
a poslední identity. Po ukončení je p=p_t=k původního
vstupu a výstup A+B/p tedy přesný. Inverzní hodnota
z p' má znaménko podle parity t, přesně jak uvádí str.574.
Změna reprezentace B na zbytek modulo původní k musí
přenést celočíselný podíl do A; nezmění výsledek.
Program používá neomezené celé číslo podle zadání,
nepředpokládá nepřetečení pevného strojového slova.

## 8. Příklady a přesnost aproximace(39)

Výpočty věty D a(C) dávají:

| Příklad | Přesný výsledek |
|---|---|
| 1: a=2^34+1,m=2^35,c=1 | sigma=2^33−3+2^(-32), C=(2^68+5)/(2^70−1) |
| 2: a=10001,m=10^10,c=2113248653 | sigma=−31.6926653544 |
| Úloha14: a=2^18+1,m=2^35,c=1 | C=(2^38−3·2^20+5)/(2^70−1), přibližně2^(-32) |

Tabulky Eukleidova postupu jsou ve výsledném JSON.
Potence příkladu2 je3: b=10000 a nejmenší mocnina
dělitelná10^10 je b³. Pro úlohu14 nejsou určeny tři
historické počáteční stavy ani přesná volba párování
v krátkých pokusech. Rozmezí0.2–0.3 proto **není
označeno za reprodukované historické měření**.

Následuje samostatný důkaz chyby(39), aby nezůstala
skryta za symbolem přibližné rovnosti. Položme

```text
T=(1−6c/m+6(c/m)²)/a,
q=c mod a, e=[q!=0],
E=−sigma(m,a,c)+6q/a−3e.
```

Z(H),(C) dostaneme

```text
C−T=(mE+a+1/a+T−3+6(m−x'−c))/(m²−1).             (J)
```

Vezměme `A_j=j/a−1/2`, včetně A0=−1/2, a
`B_j=psi((mj+q)/a)`. Pak `E=−12 sum_j A_j B_j`.
Součet B je0, proto můžeme A centrovat přičtením1/(2a).
Součty čtverců centrovaného A a B jsou
`(a²−1)/(12a)` a `(a−1)(a−2)/(12a)`.
Cauchy dává pro a>=2 `|E|<=a−1`; pro a1 je E0.
Dále `|T|<=1/a` a `|−3+6(m−x'−c)|<=6m−9`.
Pro `1<=a<m,m>=2` proto z(J)

```text
|C−T| <= (m(a+5)+a+2/a−9)/(m²−1) < (a+6)/m.
```

Poslední nerovnost plyne přímo z a<=m−1.
To dokazuje uvedenou přesnost i pro krajní malé moduly.
Nulové kořeny čitatele T jsou `1/2±sqrt(3)/6`;
malá hodnota T sama o sobě neříká nic o krátkých úsecích.

## 9. Věta K a rozsah primárního zdroje

[Knuth1977](https://matwbn.icm.edu.pl/ksiazki/aa/aa33/aa3341.pdf)
byl vizuálně přečten na str.297 a304–317, včetně důkazů
vět1–3. Maximum pro nenulové c určuje odčítací Eukleidův
postup. Důkaz nejprve pomocí konvexity přesune zbytky do
dolní poloviny intervalu, pak zmenší nenulové podíly na1;
ukončení později nemůže maximum zhoršit. Následující
teleskopické rozklady dávají horní odhad. Dolní odhad
plyne z obrácení řetězového zlomku a inverze h modulo k.
Odhad rozdílu od extrému obsahuje konstantu a součet
reciprokých vybraných podílů, což upřesňuje tvrzení
o těsnosti při velkých podílech. Kontrolovány byly i
výjimka posledního podílu1 a samostatný případ c0.
Celý článek nad rámec uvedených stran zde auditován není.

Pro použití výsledku v knize je třeba převod konvence.
Kniha indexuje podíly od1; článek od0 a jejich počet
vynucuje sudý. Označme O součet podílů na lichých
pozicích knihy a E součet na sudých pozicích. Je-li
počet sudý, zdrojové meze jsou
`−O/2−E+1/2 <= sigma <= O+E/2−1/2`.
Dolní mez knihy je o1/2 slabší. Je-li počet lichý,
rozložení posledního podílu A na A−1,1 mění součty
na O−1,E+1. Zdroj pak dává dolní mez knihy přesně
a horní o1/2 silnější. V obou případech tedy platí
vytištěná věta K. Pro h=k=1 je sigma0 a tvrzení
se ověří přímo bez článkové hypotézy h<k.

Přímé součty pro k<=80 potvrdily obě meze a zároveň
maximalizující c z odčítacího algoritmu. Tato nezávislá
kontrola zahrnuje105388 hodnot, nenahrazuje obecný důkaz.
Příklad4 má uvedených22 podílů a správné meze−55 a67.5.

Průměr součtu podílů na str.90 odkazuje na dosud
neauditovanou §4.5.3-35. Důkaz tohoto analytického výsledku
zůstává výslovnou dopřednou závislostí. Po jeho přijetí
je pravděpodobnostní krok Markovovou nerovností správný:
očekávání O(log² m) znamená, že práh(log m)^(2+epsilon)
je překročen s pravděpodobností O((log m)^(-epsilon)).
Výběr je z invertibilních násobitelů modulo m, přesně
jak říká text; nejde bez dalšího o průměr přes jinak
podmíněnou rodinu generátorů.

Historické atribuce Coveyou/Greenberger/Dieter a závěrečný
odstavec o serial testu se uzavřou s navazujícími úlohami.
Nejsou zde vydávány za úplný audit historických pramenů.
