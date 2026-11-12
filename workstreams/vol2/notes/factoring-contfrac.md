# §4.5.4: řetězové zlomky, algoritmy E/F a úlohy 11–14, 28

Vizuálně byly přečteny strany 397–401, 412–414, 659–660 a 664.
Matematická část E/F a uvedené úlohy jsou uzavřeny ve zde vymezeném
rozsahu. Dva nové problémy jsou [C0158](C0158-reduced-convergent-norm.md)
a [C0159](C0159-factor-base-coprimality.md). Časová analýza E zůstává
heuristická, přesně jako v knize. Dixonův obecný časový odhad na
401–402 patří do dalšího bloku. Úplné historické benchmarky nebyly
znovu provedeny; rozsah získaných původních pramenů je v §8.

## 1. Kongruence čtverců a faktorizace

Nechť `N>1` a `0<x,y<N`. Jestliže `x²=y² (mod N)`, ale
`x!=y` a `x+y!=N`, jsou `gcd(x-y,N)` i `gcd(x+y,N)` vlastní
netriviální dělitele N. První nemůže být N kvůli `|x-y|<N`.
Kdyby byl 1, invertibilita x-y v kongruenci
`(x-y)(x+y)=0 (mod N)` by vynutila `x+y=N`, spor. Druhý
se dokáže stejně. Tento základní argument nepotřebuje nesoudělnost
x a N; ta bude potřebná pro úplnost eliminace v §3.

Faktorová báze je konečný seznam prvočísel `p_1,...,p_m`.
Relací rozumíme dvojici `(X,e)`, kde `e=(e_0,...,e_m)` je
vektor nezáporných exponentů a

```
X² = (-1)^e_0 * product_j p_j^e_j (mod N).                 (1)
```

Součin relací se sudým součtem v každé souřadnici dává
`x=product X_i mod N` a
`y=(-1)^(sum e_i0/2)*product_j p_j^(sum e_ij/2) mod N`.
Pak `x²=y² (mod N)`. Vektor parit exponentů má m+1 souřadnic
nad tělesem se dvěma prvky; m+2 relací proto vždy obsahuje
neprázdnou lineární závislost. Není tím zaručena netriviální
kongruence ani nalezení faktoru.

## 2. Algoritmus E: přesný invariant, redukce a ukončení

Pišme `D=kN`, `R=floor(sqrt(D))`; D není čtverec. Konvergenty
řetězového zlomku sqrt(D) jsou zkrácené zlomky `p_n/q_n`.
V následující rekurzi používáme C místo knižního U, abychom
nepletli pomocný stav s posunutou proměnnou algoritmu E:

```
C_0=R, V_0=1,
V_(n+1)=(D-C_n²)/V_n,
a_(n+1)=floor((R+C_n)/V_(n+1)),
C_(n+1)=a_(n+1)*V_(n+1)-C_n.                            (2)
```

Přesný důkaz celočíselnosti, podlahy, periodicity a normové
identity je v [euclid-quadratic.md](euclid-quadratic.md), §12(a–c).
Jeho specializace dává

```
p_n²-D*q_n²=(-1)^(n+1)*V_(n+1), gcd(p_n,q_n)=1.          (3)
```

V E2 je posunuté `U=R+C_n`. Identita
`V_(n+1)=a_n(C_(n-1)-C_n)+V_(n-1)` vysvětluje výpočet V
bez dělení. Zbytek po dělení `R+C_n` číslem V dává nové
`U=2R-((R+C_n) mod V)`. Protože jde o redukovaný stav sqrt(D),
`0<V<=U<=2R`. Čitatelé se mohou počítat modulo N, neboť
jejich rekurze používá pouze součet a násobení celým a_n.
E3 má tedy platnou kongruenci `P²=(-1)^S V (mod N)`.

**Přesná rovnost (3) ovšem platí pro p_n, nikoli obecně pro
P=p_n mod N.** Vlastní knižní řádek `P=159316,V=720,S=0`
by vynucoval `Q²=128704`, což není čtverec. Správný nezkrácený
čitatel a jmenovatel jsou `750943,1691`. Nález C0158 také
zahrnuje opětovné použití téže rovnosti na str. 400 a potřebu
nezkráceného čitatele v důkazu úlohy 14.

Stav (2) je v konečné množině redukovaných stavů a má jednoznačný
předchůdce. Proto se vrátí do počátku. Je-li V=1, podmínka
`0<sqrt(D)-C<1` vynutí C=R; jde tedy právě o tento návrat.
Znaménko se může obrátit podle parity periody. Při opakování
pomocných stavů se nemusí opakovat P modulo N; E pouze ukončuje
pokus po jedné periodě, neslibuje úplnou faktorizaci každého N.

Oprava E1 z 2. července 2001 začíná stavem n=1 a vypouští
první původní průchod. Byla přečtena v PDF `all2-prepre`,
str. 22–23. Původní tabulka má 13 řádků, opravená nahrazuje
první dva jediným řádkem `(U,V,A,P,S)=(876,73,12,5329,1)`.
Prvních 100 původních průchodů dává **24** výstupů; opravených
**25**, jak tvrdí doprovodný text. Tento rozdíl je již opraven
změnou E1, není dalším novým nálezem.

## 3. Úloha 12: správnost a úplnost F při nesoudělnosti

Nejprve předpokládejme `gcd(N,product_j p_j)=1`. Všechny X
z (1) i všechny odvozené odmocniny y jsou potom invertibilní
modulo N. F ukládá postupně řádky s odlišnými nejpravějšími
lichými souřadnicemi. Odstranění liché souřadnice v F4 je
současně násobením relací a sčítáním jejich celočíselných
exponentů. Všechny již odstraněné souřadnice zůstávají sudé.
Uložit lze nejvýše m+1 řádků; v F5 jsou všechny exponenty sudé
a platí kongruence čtverců. Je-li netriviální, §1 dokazuje
správnost vráceného gcd.

Pro úplnost označme K prostor všech binárních závislostí mezi
vektory parit vstupních relací. Každému `c in K` přiřaďme
kořen jednotky `z(c)=x/y mod N`, přičemž z a -z považujeme
za stejný výsledek. Kořen jednotky zde znamená `z²=1 mod N`.
Toto přiřazení je homomorfismus z aditivní grupy K do
multiplikativní grupy těchto kořenů modulo znaménko:
násobení relací odpovídá sčítání, a použití téhož vstupu
dvakrát přispívá poměrem `X_i²/((-1)^e_i0 product p_j^e_ij)=1`.

Každý závislý vstup F vytváří jednu závislost s jedničkou
u právě přidaného vstupu. Tyto závislosti tvoří bázi K:
libovolnou závislost lze zbavit poslední jedničky příslušnou
vytvořenou závislostí a pokračovat indukcí. Pokud jsou všechny
výsledky F5 triviální, je homomorfismus triviální na celé bázi,
a tedy na K. Žádná kombinace vstupů pak nedává (18). Tím je
úplnost dokázána; zahrnuje i kombinace s vyššími mocnostmi,
protože zdvojení relace nic nemění.

**Bez nesoudělnosti tato úplnost neplatí.** Pro N=155, k=29,
bázi 2,3,5 a prvních šest výstupů opraveného E algoritmus F
všechny dosažené páry zahodí. Čtvrtý a šestý původní výstup
ale přímo dávají `x=116,y=101`, tedy faktor 5. Podrobná stopa
je v C0159. E4 výslovně dovoluje v tomto bodě skončit, takže
pozdější úspěch F z dalších výstupů protipříklad neodstraňuje.
Přirozenou opravou je předem odstranit prvočinitele N obsažené
v bázi; v praktickém použití se to obvykle už udělalo.

## 4. Úloha 13: přesná podmíněná pravděpodobnost

Nechť N je liché a nesoudělné s faktorovou bází; nechť d je
počet jeho různých prvočinitelů. Pro pevnou nenulovou jednotku
s modulo N má kongruence `x²=s (mod N)`, pokud je řešitelná,
přesně `2^d` řešení. Modulo každou lichou prvočíselnou mocninu
má jednotkový čtverec dva kořeny: z `(x-y)(x+y)=0 mod p^a`
a `gcd(2y,p)=1` plyne `x=±y mod p^a`. Čínská věta o zbytcích
umožňuje nezávislé volby znamének.

Podmiňme se celou předchozí historií F a novým vektorem exponentů.
Čerstvé rovnoměrné x je rovnoměrné mezi těmito kořeny. Součin
s předchozími uloženými X je pevná invertibilní hodnota, takže
tato rovnoměrnost zůstane zachována. Dva výsledky jsou ±y;
pravděpodobnost neúspěchu je přesně `2/2^d=2^(1-d)`.
Pro d>=2 je nejvýše 1/2. Pro Dixonův postup na str. 401 jsou
potřebné předpoklady výslovně splněny; toto použití je správné.
Samotný deterministický výstup E není tímto argumentem prohlášen
za náhodný ani nezávislý.

V neomezeném zadání chybí předpoklady. Pro N=15 a exponenty
`(0,0,2)` při bázi 2,3 jsou kořeny 9 jen 3 a 12; oba F5
zahodí, neúspěch je 1, nikoli 1/2. Taková relace skutečně
vznikne pro k=9. Pro N=8 a nulové exponenty jsou kořeny 1
hodnoty 1,3,5,7; neúspěch je 1/2, nikoli předpovězená 1.
Obě doplnění podmínek eviduje společný nález C0159.

## 5. Úlohy 11 a 14

Pro N=197209 a k=5 je perioda podílů
`1,495,2,495,1,1984` po celé části 992. Celá tabulka 659
souhlasí s přesnou rekurzí; výstupy jsou

```
993²   = 2² (mod N),
2²     = 2² (mod N),
99101² = 1  (mod N).
```

První i poslední dávají například gcd 991; druhý faktor je 199.
Opravená inicializace vypustí pouze první neúspěšný průchod,
takže tyto tři výstupy se nezmění. Základní tabulka na 398
má první dvě relace `(159316;0,4,2,1)` a `(133218;0,0,4,1)`.
Jejich součin dává `x=126308,y=540,gcd(x-y,N)=199`.
Výstup s `P=197197=-12 mod N` po dalších 14 průchodech
je triviální, jak uvádí text.

Pro úlohu 14 použijme **nezkrácené** p_n,q_n z (3).
Je-li liché prvočíslo p dělitelem V, pak
`p_n²=D*q_n² (mod p)`. Nemůže současně dělit q_n, protože
by dělilo také p_n, ve sporu s jejich nesoudělností.
Proto D je čtverec modulo p, včetně možnosti nuly; tedy
`D^((p-1)/2) mod p` je 0 nebo 1. Tím je dokázáno vyloučení
ostatních prvočísel z báze. Stručná odpověď 660 výslovně
počítá nenulový p_n; nulový případ dává D=0 modulo p.

## 6. Úloha 28: průměrné násobnosti

Násobnost `v_p(M)` znamená největší exponent e, pro který
`p^e|M`, při M!=0. Přesný lokální význam „náhodných nesoudělných
celých A,B“ je rovnoměrná dvojice zbytků modulo p^e podmíněná
tím, že nejsou oba násobky p, pro každý e. Tyto distribuce jsou
slučitelné při přechodu k menším e. Dostaneme je také jako
limit konečných zbytkových událostí pro nesoudělné dvojice ve
zvětšujících se čtvercích. Nulová hodnota A²-dB² má v tomto
lokálním modelu pravděpodobnost nula. Průměr definujeme součtem
pravděpodobností `Pr(v_p>=e)`; nejde o nekonečnou rovnoměrnou
volbu celého čísla ani o průměr zahrnující nekonečné hodnoty
v konečném seznamu.

Pravděpodobnost p|A je `1/(p+1)`. Pro d=pd_0, p nedělící d_0,
je násobnost přesně 1 při p|A a jinak 0, tedy
`f(p,pd_0)=1/(p+1)`. Pro d=p²d_0 v téže větvi položme A=pC;
B je jednotka a násobnost je `2+v_p(C²-d_0B²)`. V primitivní
dvojici C,B má větev B jednotka pravděpodobnost `p/(p+1)`;
zbývající větev má násobnost nula. Odtud

```
f(p,p²d_0)=2/(p+1)+f(p,d_0)/p.                         (4)
```

Pro liché p nedělící d má kvadratický nezbytek průměr 0.
Kvadratický zbytek má dva kořeny modulo každé p^e: každý
kořen se zvedne jednoznačně, protože derivace 2x je jednotka.
B musí být jednotka, takže

```
Pr(p^e | A²-dB²)=2/(p^(e-1)*(p+1)),
f(p,d)=sum_e Pr(v_p>=e)=2p/(p²-1).                     (5)
```

Pro p=2 a liché d je dělitelný případ právě A,B lichá,
s pravděpodobností 1/3. Pro d=3 modulo 4 je násobnost 1;
pro d=5 modulo 8 je 2. Pro d=1 modulo 8 jsou první tři
pravděpodobnosti 1/3, potom 1/6,1/12,..., protože každý
lichý čtverec má čtyři kořeny modulo 2^e pro e>=3.
Indukce při zvedání kořenů zachovává čtyři řešení: dvojice
x a x+2^(e-1) se liší v následujícím bitu čtverce.
Výsledky jsou `1/3,2/3,4/3`, přesně jako v odpovědi 664.
Rovnice (4) spolu s těmito základními případy řeší všechna d.

Na str. 400 tak pro p=5 vyjdou pravděpodobnosti
`4/24,8/24,0,0,8/24` podle D modulo 5 a pro 25 hodnoty
`0,40/600,0,0,40/600`, pokud 25 nedělí D. V tomto modelu
je očekávané odstraněné logaritmické množství
`sum f(p_j,kN)*log p_j`. Odečtení přibližného růstu V
jako sqrt(kN) dává kritérium (23), tedy odečtení `(log k)/2`.
Aplikace lokálního modelu na skutečné konvergenty je heuristika.

## 7. Heuristický čas a zlepšení na 399–401

Označme `L=ln N`, `X=2sqrt(N)`, `H=ln X` a `h=ln m`.
Za knižních předpokladů rovnoměrnosti V, přibližně m nutných
relací a `p_m=O(m log m)` dává úloha 29 dolní mez počtu
hladkých čísel (čísel složených jen z báze) `m^r/r!`.
Výsledná časová horní mez je (22), tedy `X*m²*log N*r!/m^r`.

Aby se nepřehlédla podlaha v r, lze zvolit celé
`r=sqrt(L/ln L)+O(1)` a pak
`h=H/r-ln(H/r)-ln(2C)+O(1/m)`, kde `p_m<=C m ln m`.
Pro velké N je `p_m^r<=X`. Pokud r není maximální dovolené,
stačí stále platná slabší dolní mez z úlohy 29 pro toto r.
Stirlingův vzorec pak dává

```
ln(time) <= H+2h-r*h+ln(r!)+O(ln L)
         = r*ln H+2H/r+O(r+ln L)
         = 2sqrt(L ln L)+O(sqrt(L/ln L)*ln ln L).       (6)
```

Tato volba má `ln m ~ sqrt(L ln L)/2`, jak požaduje kniha.
Bez vhodného doladění m by pouhé ignorování podlahy nemuselo
zachovat zobrazený zbytkový člen. Jde o odvození uvnitř
heuristického modelu, nikoli nepodmíněnou záruku algoritmu E.
Čísla `a=4.74540498`, `8.41790771` a exponent `0.40607248`
pro knižní desetinné velikosti souhlasí s uvedenými aproximacemi.

Dřívější zastavení dělení v E3 při `T mod p_j!=0` a
`floor(T/p_j)<=p_j` je správné: složený zbývající T by měl
dva dovolené prvočinitele větší než p_j, a tedy by překročil
`p_j²+p_j-1`. Stejná mez s p_m omezuje nalezený velký
prvočinitel. Relace obsahující právě jeden větší prvočinitel
se mohou párovat jen s relacemi obsahujícími tentýž prvočinitel.
Jediný výskyt totiž nemůže mít v součtu sudý exponent.

Další doporučení (a–c) mohou zahodit i použitelnou relaci;
jsou to deklarované úsporné heuristiky, nikoli test nemožnosti.
Jeden zbytek modulo součin malých prvočíselných mocnin skutečně
určuje všechny jednotlivé zbytky a odhalí násobnost, pokud
nepřekročí příslušný uložený exponent. Vyšší násobnost je nutné
dovyšetřit; kniha ji výslovně považuje za málo pravděpodobnou.

## 8. Historické podklady a rozsah kontrol

Původní článek Morrison–Brillhart 1975 je dostupný v textovém
přepisu na [StudyLib](https://studylib.net/doc/7962181/a-method-of-factoring-and-the-factorization-of-f7).
Čteny byly úvod, §6, relevantní §7 a §8.1/8.5, nikoli celý
článek v sazbě. Potvrzují kombinaci Legendreových a Kraitchikových
myšlenek, datum faktorizace 13. září 1970 a uvedený rozklad F7.
Odhad 50 minut je v §7 výslovně odhadem novější verze programu;
první historický výpočet trval déle. Tabulka 7 má pro 25 číslic
37,5 sekundy na IBM 360/91, což bereme jako srovnatelný historický
údaj, nikoli přesnou reprodukci knižního „asi 30 sekund“.
Primární PDF AMS pro tento článek i Lehmer–Powers 1931 vrátila
403. Vizuální kontrolu těchto článků netvrdíme.

Článek Williams 1981 má odpovídající název a rozsah 593–601;
autorem zpřístupněný abstrakt a úvod byly čteny, numerické tabulky
nebyly reprodukovány. Dodatečně získaný [oficiální náhled
Wunderlichova článku](https://page-one.springer.com/pdf/preview/10.1007/BFb0062718)
obsahuje strany 328–329, obě vizuálně přečtené. Úvod výslovně
uvádí 1324 faktorizací čísel s 15 až 42 číslicemi a empirický
exponent 0.152, což podporuje knižní přibližný exponent 0.15.
Samotné tabulky a doporučení m přibližně 150 na str. 400
zůstávají neověřeny; plný článek nebyl získán.

`verify_factoring_contfrac.py` má oddělené checkpointy:
3940 parametrických dvojic, 65 956 stavů proti nezkráceným
konvergentům, 46 589 kontrol dovolených prvočinitelů; obě celé
tabulky; 2912 prefixů proti úplnému výčtu podmnožin; 71 702
jednotkových čtverců s 212 446 kořeny; oba nové protipříklady;
2 693 344 lokálních primitivních párů, 640 přesných pravděpodobností
a 1536 racionálních průměrů. Oba prvočinitele F7 mají samostatné
rekurzivní n-1 certifikáty: 27 uzlů a 97 nezávisle ověřených mocnin.

První porovnávací program posouval pomocné U v nezávislém
modelu o jeden index; opraveno před prvním úspěšným checkpointem.
Další zastavení testu odhalilo rozdíl 24/25 výstupů mezi starou
a opravenou inicializací. Již úspěšné checkpointy se neopakovaly.
Celý obnovený běh i doplňující bloky skončily exit 0.
