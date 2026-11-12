# §4.3.3C: Fourierova transformace, přesnost a úlohy 8–10

Kontrola 2.11.2026. Vizuálně přečteny původní strany305–311,
zadání316–317 a odpovědi633. Tento blok uzavírá rovnice (34)–(51)
v původním číslování a úlohy8–10. Teoretické výpočetní modely,
historické odkazy a ostatní úlohy jsou vedeny odděleně.

## Přesná transformace a pořadí indexů

Pro K kladné celé a ω=exp(2πi/K) definujme transformaci
`hat(u)_s=sum_(t=0..K−1) ω^(st) u_t`. Základní identita
`sum_s ω^(sj)=K` pro K|j a0 jinak plyne z konečné geometrické řady.
Součin transformací dvou posloupností je proto transformací jejich
cyklické konvoluce: koeficient s indexem r je součet všech u_i v_j
s i+j≡r modulo K. Při nulách od indexu n dále a K>=2n−1 se tato
konvoluce shoduje s obyčejným součinem dvou polynomů stupně<n.
Dvojí transformace dává `K u_((-r) mod K)`, což dokazuje (40).

Nyní K=2^k. V průchodu j uložme j již zpracovaných výstupních bitů
jako celé číslo h, zbývající k−j vstupní bity jako t. Označme A
číslo získané obrácením právě j bitů čísla h. Rovnice (38) je přesně

```
A^[j](h,t) = sum_(T=0..2^j−1) ω^(2^(k−j) A T) u_(2^(k−j)T+t).
```

Rozdělení podle nejnižšího bitu T dává další předepsaný průchod;
případné rozdíly exponentů jsou násobky K. To je indukční důkaz
všech průchodů. Pro j=k dostaneme transformaci s obrácenými k bity
indexu, jak výslovně uvádí (39). Každý průchod má K operací a celkem
je jich k, tedy O(K log K) aritmetických operací.

**Úloha8.** Označme R permutaci obracející bity indexů, F transformaci
s ω a F_minus transformaci s ω^(−1), obě bez normalizace. Samotný
program průchodů vrací RF; jeho varianta pro inverzi vrací R F_minus.
Nelze zrušit dvě R, pokud mezi nimi stojí transformace. Pro k=2 a
vstup u=(0,1,0,0) dostaneme

```
(R F_minus R F u)/4 = (0, (1+i)/2, 1/2, −i/2),
```

což není u. Jde o přesný protipříklad, ne o numerickou chybu.

**Úloha9.** Náhrada ω číslem ω^q dává
`tilde(u)_s=hat(u)_((qs) mod K)` pro každé celé q. Nesoudělnost q,K
není potřebná pro tuto identitu; bez ní se ale výstupy opakují a
transformace obecně není invertovatelná. Volba q=−1 odstraní
závěrečnou permutaci r→−r z (40). Bitové obrácení z (39) se nadále
musí respektovat.

## Škálování a úloha 10

Pro vstupy délky n bitů zvolme K=2^k a L=2^l s 2n<=Kl<4n.
Číslice U_t,V_t v základu L jsou nulové pro t>=K/2. Položme
`u_t=U_t/(KL)`, `v_t=V_t/(KL)`, takže 0<=u_t,v_t<1/K.
Potom konvoluční koeficienty součinu jsou `W_r=K^2 L^2 w_r`.
Mají nejvýše k+2l bitů a jejich složení posuny s přenosy stojí
O(K(k+l)). To dává deklarovanou závěrečnou cenu O(n+nk/l).

Při třetí transformaci je vstupem `hat(u)_t hat(v)_t`. Ve stavu
A^[j](h,t) má dvojice původních indexů p,q koeficient

```
S(p,q) = ω^((p+q)t) sum_(T=0..2^j−1) ω^(2^(k−j)(A+p+q)T).
```

Jeho absolutní hodnota je2^j právě pro `A+p+q≡0 modulo2^j`, jinak
je0. Takových dvojic je v úplném rozsahu0<=p,q<K přesně K^2/2^j.
Každý součin |u_p v_q| je menší než1/K^2, a tudíž |A^[j]|<1.
To je celý důkaz úlohy10, včetně počtu dvojic uváděného v odpovědi.

Pro analýzu zaokrouhlení je užitečná ještě **pevná rezerva**:
nenulové p,q leží pouze v první polovině rozsahu. Pro j<k zbývá
nejvýše K^2/(4*2^j) dvojic, a proto |A^[j]|<1/4. Pro j=k je
nejvýše K/2 dvojic a |A^[k]|<1/2. U prvních dvou transformací
také |A^[j]|<1/2, přímo z trojúhelníkové nerovnosti a škálování.

## Odmocniny jednotky a zaokrouhlování

Pišme ω_r=exp(2πi/2^r)=x_r+i y_r. Rovnice (46)
`x_(r+1)=sqrt((1+x_r)/2)`, `y_(r+1)=y_r/(2x_(r+1))`
platí pro r>=2; počáteční ω_2=i se zadává přesně. Podmínka r>=2
je známé erratum ze14.8.2005, které vylučuje dělení0 při r=1.

Nechť m označuje počet zlomkových bitů a δ=sqrt(2)*2^(−m).
Každou souřadnici přesného ω_r lze useknout směrem k nule; výsledná
aproximace leží uvnitř jednotkového kruhu a má chybu menší než δ.
Kořeny se smějí počítat s vyšší vnitřní přesností, jak připouští text.
Není bezpečné bez dalšího zacházet se zaokrouhleným jmenovatelem
v (46) jako s přesným. Náš program používá intervaly s přesnými
racionálními konci a celočíselnou odmocninou; každé konečné useknutí
je zvlášť certifikováno shodou obou mezí.

Binární rozklad exponentu (47) vytvoří ω^j z nejvýše k kořenů a
k−1 dalších useknutí. Všechny aproximované mocniny mají normu<=1
a chybu nejvýše (2k−1)δ. Celá tabulka potřebuje O(K) komplexních
násobení: pro každé j odebereme jeden nastavený bit a použijeme již
spočtenou mocninu. Výpočet kořenů má jen polynomiální cenu v k,m,
která je pro zde používané velké K podružná.

Pro operaci `a'=truncate(b'+ω' c')`, kde se usekne až celý součet,
platí při normách<=1

```
|a'−a| < δ+|b'−b|+|ω'−ω|+|c'−c|.
```

Proto chyby prvních transformací splňují E_j<=2E_(j−1)+2kδ,
E_0=0, tedy E_k<2k(K−1)δ. Po bodovém násobení je chyba menší
než `(4kK−2k)δ`. Třetí transformace ji zvětší nejvýše na

```
K(4kK−2k)δ+(K−1)2kδ < 4kK^2δ.
```

Po přesném vydělení K tedy |w'_r−w_r|<4kKδ. Aby následné násobení
K^2L^2 a zaokrouhlení dalo přesné celé W_r, stačí

```
m >= 3k+2l+lg(k)+7/2.
```

Jednodušší podmínka k>=7,m>=4k+2l ji implikuje. Normy aproximací
nepředpokládáme kruhem: při prvních transformacích jejich normy
zůstávají pod1/2 díky trojúhelníkové nerovnosti, useknutí a normám
mocnin<=1. Při třetí transformaci použijeme současnou indukci
pro chybu a normu. Přesná hodnota má normu<1/2 a celková průběžná
chyba je menší než `4kK^2δ<1/2` za uvedené podmínky. Každý další
krok proto opravdu smí použít předpoklad normy<=1.

Přesné dělení K na konci lze spojit s konečným škálováním, takže
nepřidává neanalyzované useknutí. Mezivýsledek může mít m+k
zlomkových bitů, což je stále O(m) místa. Ve všech k průchodech
se dělá K operací s cenou O(M), kde M je cena m-bitového komplexního
násobení. Tím dostáváme O(n)+O(Mnk/l), jak uvádí text.

Parametry příkladů také splňují přesnější podmínku: (k,l,m)=(11,8,60),
(15,15,90) a (27,27,144). Poslední hodnota opravuje známé `m=44`
ze27.4.1999. Zjednodušená mez4k+2l by ve třetím příkladu dávala162,
ale není nutná; přesnější mez je menší než144.

## Tabulky, errata a kontroly

Tabulka1 na str.308 je ověřena přesně v okruhu
`Z[z]/(z^4+1)`, kde z představuje exp(2πi/8). Každá její buňka,
včetně druhé transformace a výsledných koeficientů10,69,64,125,36,
souhlasí. Obě první hlavičky jsou2^7 krát příslušná transformace.
Opravy textových odkazů z let2001 a2015 používají stejný faktor2^7.
OCR errata2015 přesunulo číslo řádku−16 nad vzorec; **nejde o2^16**.
Rozhodující je původní obrázek `accuracy-errata-all2-pre-7.png`.

Další erratum ze8.11.1997 doplňuje číslování chybové meze na str.310
a posouvá následující čísla rovnic. V tomto zápisu jsou odkazy
výslovně podle původního dotisku. Kontrolovány all2-prepre,all2-pre,
all2,err2 a původní stránky relevantních oprav.

`verify_fast_fft.py` používá dva odlišné přesné modely. Průchody a
jejich vzorce se kontrolují v cyklotomickém okruhu, kde se všechny
operace redukují na celočíselné polynomy. Reálná implementace
s pevnou řádovou čárkou používá dvojice celých čísel, certifikované
intervaly pro (46) a skutečné usekávání při každé operaci. Výsledek
porovnává s přímou konvolucí i nezávislým celočíselným součinem.
Konečné testy doplňují obecné důkazy výše.

Běh71268,exit0: všechny tři checkpointy prošly.62 přesných algebraických
případů,3128 stavových buněk (38),372 variant omega^q,40 buněk tabulky1
a62 úplných násobení s pevnou řádovou čárkou do24576 bitů. Ve všech
kořenech stačilo16 pomocných bitů pro certifikované useknutí. Záměrně
nedostatečné m=7 dává u příkladu1234*2341 výsledek2310944 místo2888794;
m=24 vrací správný výsledek. Tento kontrolní neúspěch není chyba knihy.
