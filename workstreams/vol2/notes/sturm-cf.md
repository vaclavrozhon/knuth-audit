# §4.6.1: Sturmova věta a aproximace, úlohy 22/23/26

Kontrola 4. listopadu 2026. Původní sazba 434, 438, 677 a 678 byla
zobrazena. V úloze 26 je druhá nerovnost neostrá, `<=`; OCR ji ztrácí.
Na 434 je interval `(a,b]`, nikoli otevřený interval z OCR.
Nový nález nevznikl. Překlep `y_j` v odpovědi 22 je již opraven
erratem ze 17. srpna 2024 na `u_j`.

## 1. Počet změn znamének

Nechť u je nekonstantní reálný polynom bez násobných komplexních
kořenů. Položme u_0=u, u_1=u', kde čárka znamená derivaci. Záporné
zbytky Eukleidova algoritmu, případně násobené kladnými konstantami,
splňují pro i=1,...,k

```
c_i u_(i-1) = q_i u_i - d_i u_(i+1),  c_i,d_i>0;
deg(u_(k+1))=0.
```

Poslední člen je nenulová konstanta: společný kořen u a u' by byl
násobným kořenem u a naopak. To plyne přímo z derivace rozkladu
u=(x-alpha)^s w, kde w(alpha)!=0. Největší společný dělitel je
tedy konstanta a Eukleidův algoritmus jí skončí.

Označme V(x) počet změn znamének v seznamu u_0(x),...,u_(k+1)(x)
po odstranění nul. Například `0,+,-,-,0,+,+,-` má tři změny.
Dva sousední členy nemohou současně vymizet: rekurence by jejich
nulu přenesla až na poslední nenulovou konstantu. Když u_i(x)=0
pro 0<i<k+1, jeho dva sousedé proto mají opačná nenulová znaménka.

Při průchodu takovým vnitřním kořenem má trojice sousedních členů
stále právě jednu změnu, ať je prostřední znaménko kladné, nulové,
nebo záporné. Při několika současných nulách jsou dotčené dvojice
hran seznamu disjunktní; mohou sdílet nenulový vrchol, což součet
změn neovlivňuje. Toto je i přesné zdůvodnění souběžných nul
zmíněných v odpovědi.

V jednoduchém kořeni alpha prvního členu je u_1(alpha)!=0.
Z identity u(x)=(x-alpha)w(x), w(alpha)=u'(alpha), vidíme, že vlevo
od alpha mají u a u' opačná znaménka a vpravo stejná. V samotném
alpha vynechání první nuly dává již pravou hodnotu V. Počet změn
tedy klesne o jednu při dosažení alpha a dále se nezmění.

Každý člen má konečně mnoho kořenů. Sečtením uvedených změn proto
V(a)-V(b) přesně počítá kořeny `a<x<=b`, včetně a=b. Argument
zahrnuje i lineární u, kdy posloupnost má pouze dva členy. Pro
nenulový konstantní u je počet kořenů zvlášť nula; konstrukce
u_1=u' se pro něj nepoužívá.

## 2. Úloha 23: prokládání reálných kořenů

Kořeny dvou polynomů se **prokládají**, když mezi každými dvěma
sousedními kořeny prvního leží právě jeden kořen druhého. Má-li u
n různých reálných kořenů, Rolleova věta dává n-1 takových kořenů u'.
Jejich počet vyčerpává stupeň u', proto jsou také jednoduché.

Obecně nechť u stupně N a v stupně N-1 mají jednoduché prokládané
reálné kořeny beta_1<...<beta_(N-1) polynomu v. Hodnoty u(beta_i)
střídají znaménka. Záporný zbytek w v rovnici c u=qv-dw, c,d>0,
splňuje w(beta_i)=-(c/d)u(beta_i), a tedy také střídá znaménka.
Mezi každou dvojicí beta_i,beta_(i+1) má kořen. Má zároveň stupeň
nejvýše N-2, takže jeho N-2 kořenů je jednoduchých a vyčerpává
jeho stupeň. Pro N=2 je zbytek nenulová konstanta, protože
u(beta_1)!=0. Indukce dává stupně n,n-1,...,1,0 bez vynechání.

## 3. Úloha 26: přesná nejlepší aproximace

Nyní pracujeme nad libovolným tělesem F. Pro nenulové polynomy
u,v s m=deg(u)>deg(v) vytvořme řetězový zlomek v/u. Jeho částečné
jmenovatele a_1,...,a_N jsou podíly Eukleidova algoritmu u,v.
Všechny mají kladný stupeň. Čitatele P_i a jmenovatele Q_i
postupných aproximací (konvergentů) definují rekurence

```
P_-1=1, Q_-1=0;  P_0=0, Q_0=1;
P_i=a_i P_(i-1)+P_(i-2), Q_i=a_i Q_(i-1)+Q_(i-2).
```

Zbytková chyba je R_i=P_i u-Q_i v. Pišme d_i=deg(R_i),
e_i=deg(Q_i), s konvencí deg(0)=-infinity. Tedy d_-1=m,
d_0=deg(v), R_N=0. Rekurence a rozšířený Eukleidův algoritmus
dávají

```
P_(i-1)Q_i-P_i Q_(i-1)=(-1)^i,
d_(i-1)+e_i=m,  1<=i<=N.
```

Stupně e_i přísně rostou a nenulové chyby mají přísně klesající
stupně. První identita plyne indukcí z převrácení znaménka
determinantu; druhá z e_i=e_(i-1)+deg(a_i) a
deg(a_i)=d_(i-2)-d_(i-1). Tyto identity zahrnují i poslední
konvergent s nulovou chybou, aniž bychom používali neexistující e_(N+1).

Dokážeme silnější verzi z odpovědi. Pro 1<=n<=N předpokládejme

```
deg(q)<e_n,  deg(pu-qv)<d_(n-2).
```

Determinant dvou sousedních konvergentů je nenulová konstanta,
tedy jednotka F[x]. Existují proto polynomy c,d takové, že

```
(p,q)=c(P_(n-1),Q_(n-1))+d(P_n,Q_n).
```

Kdyby d!=0, muselo by být c!=0 a nejvyšší členy jmenovatelů by
se rušily: deg(c)+e_(n-1)=deg(d)+e_n. Zejména deg(c)>deg(d).
V chybě cR_(n-1)+dR_n má první člen přísně vyšší stupeň než
druhý, ať je R_n nenulový, nebo nulový. Proto

```
deg(pu-qv)=deg(c)+d_(n-1)
          <d_(n-2)=d_(n-1)+e_n-e_(n-1).
```

Odtud deg(c)<e_n-e_(n-1), což v rovnosti stupňů jmenovatelů
dává deg(d)<0, spor. Musí tedy být d=0 a (p,q)=c(P_(n-1),Q_(n-1)).

V zadání je navíc deg(pu-qv)<=d_(n-1). Jelikož R_(n-1)!=0,
tato podmínka nutí c být konstantou nebo nulou. To je právě
tvrzení úlohy. Slabší předpoklad v odpovědi dovoluje i nekonstantní
c(x); tyto dvě formulace nezaměňujeme.

## 4. Kroneckerův dovětek

Nechť navíc gcd(u,v)=1 a zvolený konečný stupeň chyby d splňuje
0<=d<=deg(v). Existuje jediné n takové, že
d_(n-2)>d>=d_(n-1), protože poslední nenulový zbytek má stupeň nula.
Položme t=d-d_(n-1). Dvojice x^t(P_(n-1),Q_(n-1)) má chybu
přesného stupně d a jmenovatel stupně e_(n-1)+t<e_n.

Nejmenší možný stupeň jmenovatele je proto také menší než e_n.
Pro jakékoli takové minimální řešení platí předpoklady §3, takže
p/q=P_(n-1)/Q_(n-1). Jmenovatel nemůže být nulový: nenulové pu
má stupeň alespoň m a nulové pu nemá konečný stupeň d. Nulovou
chybu, která není v tomto dovětku předepsána, dává zvlášť P_N/Q_N=v/u.

## 5. Polynomiální čas izolace kořenů

Toto je vlastní důkaz existenčního časového tvrzení z dovětku
odpovědi 22; není to reprodukce všech Heindelových algoritmů.
Nechť u má stupeň n a celočíselné koeficienty absolutní hodnoty
nejvýše N>=1. Jeho kořeny leží v |z|<R=1+N: pro |z|>=R
vedoucí člen převáží součet ostatních, pomocí geometrické řady.

Pro bezčtvercový u s n>=2 je diskriminant nenulové celé číslo:
je to, až na znaménko, resultant(u,u')/lc(u), kde lc je vedoucí
koeficient. Integritu lze vidět i ze Sylvestrova determinantu:
při lc(u)=0 je první sloupec nulový, takže determinantový polynom
obsahuje faktor lc(u). Pro komplexní kořeny alpha_i tedy

```
1 <= |lc(u)|^(2n-2) product_(i<j)|alpha_i-alpha_j|^2.
```

Je-li delta nejmenší vzdálenost dvou kořenů a h=n(n-1)/2, plyne
delta >= N^(-(n-1)) (2R)^(-(h-1)). Počet potřebných půlení
intervalu (-R,R] je tudíž O(n^2 log(N+1)). Na každé hloubce
zpracováváme pouze intervaly s kladným počtem kořenů, nejvýše n
intervalů. Prázdné potomky zahodíme. Po dosažení délky <delta
má každý neprázdný interval právě jeden kořen. Případ kořene
přesně v bodě půlení je správně rozdělen konvencí (a,b].

Všechny dělicí body jsou dyadické zlomky s polynomiální bitovou
délkou. Posloupnost lze spočítat přesně pomocí subresultantů
z `subresultants.md` a u každého členu zaznamenat znaménko
škálování vůči zápornému Eukleidovu zbytku. Normalizované koeficienty
mají O(n log(n(N+1))) bitů podle determinantové meze; syrové
pseudodělení může přidat další faktor O(n), ale délka zůstává
polynomiální. Algoritmus používá polynomiálně mnoho celočíselných
operací. Hornerovo vyhodnocení po vynásobení kladnou mocninou
jmenovatele bodu půlení dává znaménka přesnou celočíselnou aritmetikou.

Pokud u má násobné kořeny, nejprve odstraníme gcd(u,u'). Jeho
primitivní část má koeficienty s polynomiální bitovou délkou podle
stejné determinantové meze. Přesné dělení má nejvýše n kroků;
rekurence koeficientů podílu může v bitové délce přidat nejvýše
další polynomiální faktor. Bezčtvercová část proto splňuje stejné
existenční tvrzení o polynomiálním čase. Netvrdíme zde ostrý
exponent časové složitosti ani nevyužíváme neuzavřenou úlohu 21.

## 6. Nezávislé přesné kontroly

`verify_sturm_cf.py` má dva úspěšné bloky v
`results/sturm-cf.json`. Příkaz měl limit 180 sekund, PID 1324637,
tool session 40273, exit 0. Součet naměřených časů je 1.460929 s.

- 100 polynomů z různých celočíselných lineárních faktorů a faktorů
  x^2+c, c>0; 70300 intervalů včetně kořenů na krajích. Orákulem
  jsou předem známé faktory, nikoli další Sturmův výpočet.
  28 posloupností má pouze reálné kořeny; stupně klesají po jedné.
  Kontrola skutečně zahrnula současné nesousední nuly.
- 700 monických dvojic nad F_2 (m<=4) a F_3 (m<=3), včetně
  konstantního v. Úplné vyčíslení jmenovatelů předepsaných stupňů
  používá p jako podíl qv/u; jiná volba p nemůže splnit danou
  malou chybu. Ověřeno 3610 svědků silného tvrzení, 5994 svědků
  slabšího, z toho 2384 s nekonstantním násobkem, a 2160 minimálních
  jmenovatelů Kroneckerova dovětku. Determinantové a stupňové
  identity se kontrolují nezávisle od tohoto vyčíslení.

Úspěšné běhy nebyly opakovány. Konečné testy podpírají obecné
důkazy v §1–4, nenahrazují je.

## 7. Primární prameny a errata

[Sturmův původní sken](https://pnp.mathematik.uni-stuttgart.de/igt/eiserm/enseignement/Sturm-memoire-numerise.pdf)
má titulní list 271, prázdnou 272 a vlastní text od 273.
Vizuálně čteny PDF 1–12, zejména celé §§1–6 na 275–282:
záporné zbytky, zákaz sousedních nul a oba typy změn znamének
jsou v originálu. Citace 271–318 tedy není chyba vzniklá záměnou
273 za 271. Lüneburgův přepis z roku 1999 byl použit pro navigaci;
není vydáván za původní sazbu. Zbytek článku nebyl celý revidován.

[Kroneckerův článek v sebraných spisech](https://www.e-rara.ch/download/pdf/5761162.pdf)
byl vizuálně čten na úvodní straně 115 a na 121–124, článek I.
Obsahuje determinant sousedních konvergentů, zbytkovou identitu
a argument stupni v rovnici (C). Tam uvedená podmínka je
součet stupně chyby a jmenovatele menší než stupeň vstupu.
Jde o doložený předchůdce používané metody; netvrdíme, že moderní
silnější formulace §3 je v těchto čtyřech stranách doslova.
Datum čtení 16. června 1881 je vytištěno na začátku článku.
Celých 81 stran souboru nebylo auditováno.

[Heindelův vydavatelský abstrakt konferenční verze](https://doi.org/10.1145/800204.806312)
výslovně uvádí přesnou celočíselnou izolaci pomocí Sturma a časové
meze. Vydavatelská metadata časopisecké verze, DOI
10.1145/321662.321667, potvrzují JACM 18(4), říjen 1971, 533–548;
jsou uložena. Její plný text vrací 403, proto její konkrétní
algoritmy nepovažujeme za přečtené. Matematické existenční tvrzení
je nezávisle pokryto §5.

Prohledány all2-prepre, all2-pre, all2, err2, původní err2.textxt
i errata druhého vydání s odpovídajícími stranami. Konkrétní log
je `sources/sturm-cf-errata.txt`. Kromě již zmíněného `y_j -> u_j`
je relevantní interpunkční oprava citace Sturma z 22. srpna 2002.
Historie determinantů na 435 patří do dalšího bloku. Všechny
zdroje a hashe eviduje `sources/sturm-cf.json`.
