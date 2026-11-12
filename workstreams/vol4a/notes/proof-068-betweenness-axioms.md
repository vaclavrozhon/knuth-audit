# Úloha 75: od abstraktního „mezi“ k mediánové algebře

Checkpoint X0097, P0916–P0922. Zadání p89–90/file106–107
a odpověď p547–548/file564–565 byly přečteny v původní sazbě.
Zde se **nepoužívá** předchozí distributivita z proof-063:
ta vycházela z jiných axiomů, jejichž platnost teprve dokazujeme.
Tvrzení platí i pro nekonečné M; žádný argument nepředpokládá
konečný počet jeho prvků nebo různost zavedených bodů.

Pišme [abc] pro „b leží mezi a,c“. Máme pouze:

1. [aba] ⇒ a=b.
2. [uxv] a [xyu] ⇒ [vyu].
3. Pro každou trojici x,y,z existuje právě jedno w=m(x,y,z)
   splňující [xwy], [xwz], [ywz].

## (a) Majority — P0916

Nechť w=m(x,x,y). Axiom 3 dává [xwx]; axiom 1 dává w=x.
Proto m(x,x,y)=x. Zbývající podmínky v axiomu 3 současně
dávají [xxy] pro každé x,y. Dosud není použita žádná symetrie.

## (b) Symetrie krajních bodů a komutativita — P0917

Z [uxv] a vždy pravdivého [xxu] dá axiom 2 při y=x vztah
[vxu]. Výměnou u,v dostaneme i opačný směr. Tedy

    [uxv] ⇔ [vxu].

Toto je přesně znění po známé opravě „Setting y=x“ na p547
line −5. Podmínky definující m(x,y,z) jsou nyní symetrické
v celé trojici x,y,z: jde o tři neuspořádané dvojice krajů.
Jednoznačnost z axiomu 3 tedy dává všech šest permutací
komutativního zákona. Navíc jsou vždy pravdivé oba krajní
vztahy [aab] i [abb], včetně opakovaných symbolů.

## (c) Pevné body a přepsané pravidlo N — P0918

Podle axiomu 3 je x=m(u,x,v) právě tehdy, když [uxx],
[uxv], [xxv]. První a třetí jsou vždy pravdivé, takže

    [uxv] ⇔ x=m(u,x,v).

Použitím symetrie krajů se axiom 2 přepíše na pravidlo N:

    [uyv], [uxy] ⇒ [uxv].                       (N)

Skutečně v původním axiomu nahraďme jeho x symbolem y
a jeho y symbolem x. Druhou premisu [yxu] máme ze [uxy],
výsledek [vxu] je po symetrii [uxv]. N je vnoření intervalů;
není to ještě další pravidlo D, které teď samostatně odvodíme.

## (d) Vnitřní tranzitivita — P0919

Předpokládejme [uxy], [uyv] a zaveďme z=m(x,y,v).
Máme [xzy], [xzv], [yzv]. Z [yxu] a [yzx] použijme N
s krajním bodem y; dostaneme [yzu], tedy [uzy]. Z [uyv]
a [uzy] dostaneme dalším N vztah [uzv]. Proto z splňuje
všechny tři vztahy pro medián trojice u,y,v. Tentýž medián
je y podle (c), neboť [uyv] je předpoklad. Jednoznačnost
dává z=y a z [xzv] nyní plyne [xyv]. Dokázali jsme

    [uyv], [uxy] ⇒ [xyv].                       (D)

To vysvětluje oba stručné nevypsané kroky v odpovědi (d).
Nepředpokládáme lineární uspořádání ani metrické vzdálenosti.

## (e) Konvexita opačných paprsků — P0920

Předpoklady jsou [uxv], [uyz], [vyz]. Přesně podle nápovědy
zaveďme

    w=m(y,u,v),  p=m(w,u,x),  q=m(w,v,x),
    r=m(p,x,z),  s=m(q,x,z),  t=m(r,s,z).

Existence všech šesti bodů plyne postupně z axiomu 3.
První tabulka níže obsahuje úplný obecný důkaz. Řádky
1–20 jsou předpoklady a definující mediánové vztahy; žádná
další mediánová identita se do nich nevkládá. Řádky 21–44
používají pouze N a již dokázané D a dávají zejména

    [utv] (44), [utz] (36), [vtz] (38),
    [uwv] (6),  [uwz] (23), [vwz] (29).

Podle jednoznačnosti mediánu trojice u,v,z je tedy t=w.
Z [rtz] a [stz] můžeme dosadit [rwz], [swz] (45–46).
Přesné původní vztahy i všech šest podmínek jednoznačnosti
jsou v těchto dvou krocích uvedeny mezi premisami.
Následující N dává [xwz]; zároveň už máme [wyz] (24).
Poslední N proto dává **[xyz]** (52), jak bylo požadováno.

Tabulka také doloží oba dodatky odpovědi: [prp] (50) dává
r=p a [qsq] (51) dává s=q podle axiomu 1. Tyto rovnosti
nebyly předpokládány ani použity pro důkaz hlavního výsledku.
Získané pravidlo označme

    [uxv], [uyz], [vyz] ⇒ [xyz].                 (E)

## (f) Krátká distributivita — P0921

Pro libovolné x,y,z,u,v definujme přesně body z odpovědi:

    r=m(y,u,v), s=m(z,u,v), t=m(x,y,z),
    p=m(x,r,s), q=m(t,u,v).

Druhá tabulka vychází jen z jejich definujících vztahů,
reflexivity krajů, N, D a **již dokázaného E**. V každém
kroku jsou uvedeny konkrétní premisy a substituce. Výsledkem
je [pqp] (36), a tedy p=q podle axiomu 1. Po dosazení:

    m(m(x,y,z),u,v)=m(x,m(y,u,v),m(z,u,v)).

To je přesně krátká distributivita (53). Není zde kruhové
použití výsledku z mediánové algebry ani ověření pouze pro bity.

## Skutečně získané tři axiomy a doména — P0922

Majority a komutativita už byly dokázány. Z právě získaného
krátkého distributivního zákona zvolme vstupy (x,w,y;w,z):

    m(m(x,w,y),w,z)
      =m(x,m(w,w,z),m(y,w,z))
      =m(x,w,m(y,w,z)).

To je asociativní zákon (52), poslední nutný axiom definice
mediánové algebry. Operace je na celém M jednoznačně definována
axiomem 3. Ani prázdné M nepůsobí problém pro toto čistě
algebraické tvrzení: prázdná operace je jednoznačná a všechny
univerzální podmínky jsou prázdné. Grafová konvence P0886
se tím neřeší a není zde potřebná.

## Původ a kontrola konečného certifikátu

`checks/betweenness75-derivation.py` provádí pouze forward
odvozování nad 11, respektive 10 **pojmenovanými termy**.
Neprochází grafy, modely, přiřazení pravdivosti ani jiné
hodnoty M. Každý krok je univerzální instance N/D/E, takže
výsledek není omezen na prostor s 11 nebo 10 prvky. Symboly
se smějí v konkrétním prostoru rovnat.

Endpoint symetrie je pouze kanonizace prvního/třetího symbolu;
střed se nikdy nepřehazuje. Soubor výsledků
`results/betweenness75-derivation.json` obsahuje všechny
závislosti právě potřebné pro šest vztahů, hlavní závěr,
rovnosti r=p/s=q a distributivitu. Všechny vypsané substituce
byly ručně porovnány s N/D/E a s definicemi bodů. Tabulky
níže jsou čitelným přepisem téhož certifikátu, nikoli druhým
testem nebo novým důkazním vstupem.

Běh `nice -n 15 python3 .../checks/betweenness75-derivation.py`
trval asi 0,12 s. Druhý krátký běh po opravě metadat přidal
k substitučnímu kroku původní mediánovou premisu, aby certifikát
nevyžadoval její domyšlení. Nehledal žádné modely.
Uzávěr má 215/265 vztahů v (e) před/po dosazení a 153 v (f);
výsledné důkazy mají 52 a 36 řádků. Žádný starý výpočet se
neopakoval. Kniha zde neudává obecnou časovou mez, kterou
by tento malý důkaz měl nahrazovat.

Algoritmus C a jeho úplnost pro konečné Hornovy klauzule
jsou přesně hotový argument proof-049, bez nového auditu.
Existence mediánových svědků není sama výroková Hornova
klauzule: zajistí ji axiom 3 předem; jednoznačnost je v
certifikátu explicitní zvláštní krok. Tím je přesně vymezen
smysl použití Hornových pravidel ve stručné odpovědi.

## Errata a bibliografické výjimky

Z pěti relevantních vrstev (`all4a-pre`, `all4a`, `err4a`,
`all4f0`, `all4f1`) je zde relevantní oprava p547 line −5
z 2. 1. 2012, „Setting y=x“. Její původní sazba je v
`images/proof-y-errata22.png`; odpověď (b) ji zohledňuje.
Úloha 76 a její historické poznámky mají přesné předchozí
pokrytí v proof-063 a nejsou zde znovu matematicky odvozovány.

Primární [archiv obsahu čísla PAMS 5(5), 1954](https://www.jstor.org/stable/i335871)
potvrzuje Sholanderův článek Medians and Betweenness, p801–807.
Primární AMS PDF bylo při této kontrole nedostupné. Jeho
celý text a citace Huntington–Kline 1917 nebyly nezávisle
ověřeny; vlastní odvození je úplné bez těchto externích vstupů.

Následující tabulky používají [abc]=[cba]. U N/D je seznam
substituce (u,x,y,v); u E je (u,x,v,y,z). Mediánový seznam
je (w,a,b,c), tedy w=m(a,b,c). „U“ znamená jednoznačnost
t=w z šesti explicitních vztahů a dosazení do poslední premisy.

## Úplný certifikát 75(e)

| krok | vztah | pravidlo | premisy | substituce |
|---|---|---|---|---|
| 1 | [uxv] | předpoklad |  |  |
| 2 | [uyz] | předpoklad |  |  |
| 3 | [vyz] | předpoklad |  |  |
| 4 | [uwy] | medián |  | (w,y,u,v) |
| 5 | [vwy] | medián |  | (w,y,u,v) |
| 6 | [uwv] | medián |  | (w,y,u,v) |
| 7 | [upw] | medián |  | (p,w,u,x) |
| 8 | [wpx] | medián |  | (p,w,u,x) |
| 9 | [upx] | medián |  | (p,w,u,x) |
| 10 | [vqw] | medián |  | (q,w,v,x) |
| 11 | [wqx] | medián |  | (q,w,v,x) |
| 12 | [vqx] | medián |  | (q,w,v,x) |
| 13 | [prx] | medián |  | (r,p,x,z) |
| 14 | [prz] | medián |  | (r,p,x,z) |
| 15 | [xrz] | medián |  | (r,p,x,z) |
| 16 | [qsx] | medián |  | (s,q,x,z) |
| 17 | [qsz] | medián |  | (s,q,x,z) |
| 18 | [rts] | medián |  | (t,r,s,z) |
| 19 | [rtz] | medián |  | (t,r,s,z) |
| 20 | [stz] | medián |  | (t,r,s,z) |
| 21 | [pxv] | D | 1,9 | (u,p,x,v) |
| 22 | [upy] | N | 4,7 | (u,p,w,y) |
| 23 | [uwz] | N | 2,4 | (u,w,y,z) |
| 24 | [wyz] | D | 2,4 | (u,w,y,z) |
| 25 | [upz] | N | 2,22 | (u,p,y,z) |
| 26 | [uqv] | N | 1,12 | (v,q,x,u) |
| 27 | [qxu] | D | 1,12 | (v,q,x,u) |
| 28 | [vqy] | N | 5,10 | (v,q,w,y) |
| 29 | [vwz] | N | 3,5 | (v,w,y,z) |
| 30 | [vqz] | N | 3,28 | (v,q,y,z) |
| 31 | [pxq] | D | 21,12 | (v,q,x,p) |
| 32 | [urx] | N | 9,13 | (x,r,p,u) |
| 33 | [rpw] | D | 8,13 | (x,r,p,w) |
| 34 | [sqw] | D | 11,16 | (x,s,q,w) |
| 35 | [urz] | N | 25,14 | (z,r,p,u) |
| 36 | [utz] | N | 35,19 | (z,t,r,u) |
| 37 | [vsz] | N | 30,17 | (z,s,q,v) |
| 38 | [vtz] | N | 37,20 | (z,t,s,v) |
| 39 | [qxr] | D | 31,13 | (p,r,x,q) |
| 40 | [qsr] | N | 39,16 | (q,s,x,r) |
| 41 | [qtr] | N | 40,18 | (r,t,s,q) |
| 42 | [qru] | N | 27,32 | (u,r,x,q) |
| 43 | [qtu] | N | 42,41 | (q,t,r,u) |
| 44 | [utv] | N | 26,43 | (u,t,q,v) |
| 45 | [rwz] | U | 44,36,38,6,23,29,19 |  |
| 46 | [swz] | U | 44,36,38,6,23,29,20 |  |
| 47 | [xwz] | N | 15,45 | (z,w,r,x) |
| 48 | [prw] | D | 14,45 | (z,w,r,p) |
| 49 | [qsw] | D | 17,46 | (z,w,s,q) |
| 50 | [prp] | D | 48,33 | (w,p,r,p) |
| 51 | [qsq] | D | 49,34 | (w,q,s,q) |
| 52 | [xyz] | N | 47,24 | (z,y,w,x) |

## Úplný certifikát 75(f)

| krok | vztah | pravidlo | premisy | substituce |
|---|---|---|---|---|
| 1 | [qqr] | kraj |  |  |
| 2 | [qqs] | kraj |  |  |
| 3 | [ury] | medián |  | (r,y,u,v) |
| 4 | [vry] | medián |  | (r,y,u,v) |
| 5 | [urv] | medián |  | (r,y,u,v) |
| 6 | [usz] | medián |  | (s,z,u,v) |
| 7 | [vsz] | medián |  | (s,z,u,v) |
| 8 | [usv] | medián |  | (s,z,u,v) |
| 9 | [xty] | medián |  | (t,x,y,z) |
| 10 | [xtz] | medián |  | (t,x,y,z) |
| 11 | [ytz] | medián |  | (t,x,y,z) |
| 12 | [rpx] | medián |  | (p,x,r,s) |
| 13 | [spx] | medián |  | (p,x,r,s) |
| 14 | [rps] | medián |  | (p,x,r,s) |
| 15 | [tqu] | medián |  | (q,t,u,v) |
| 16 | [tqv] | medián |  | (q,t,u,v) |
| 17 | [uqv] | medián |  | (q,t,u,v) |
| 18 | [sry] | E | 8,3,4 | (u,s,v,r,y) |
| 19 | [qry] | E | 17,3,4 | (u,q,v,r,y) |
| 20 | [rsz] | E | 5,6,7 | (u,r,v,s,z) |
| 21 | [qsz] | E | 17,6,7 | (u,q,v,s,z) |
| 22 | [rqt] | E | 5,15,16 | (u,r,v,q,t) |
| 23 | [sqt] | E | 8,15,16 | (u,s,v,q,t) |
| 24 | [rpz] | N | 20,14 | (r,p,s,z) |
| 25 | [spy] | N | 18,14 | (s,p,r,y) |
| 26 | [rpt] | E | 10,12,24 | (x,t,z,p,r) |
| 27 | [spt] | E | 9,13,25 | (x,t,y,p,s) |
| 28 | [pqt] | E | 14,22,23 | (r,p,s,q,t) |
| 29 | [qpr] | D | 26,28 | (t,q,p,r) |
| 30 | [qps] | D | 27,28 | (t,q,p,s) |
| 31 | [qpy] | N | 19,29 | (q,p,r,y) |
| 32 | [qpz] | N | 21,30 | (q,p,s,z) |
| 33 | [qpt] | E | 11,31,32 | (y,t,z,p,q) |
| 34 | [pqr] | E | 33,22,1 | (t,p,q,q,r) |
| 35 | [pqs] | E | 33,23,2 | (t,p,q,q,s) |
| 36 | [pqp] | E | 14,34,35 | (r,p,s,q,p) |
