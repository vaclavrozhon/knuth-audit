# MPR113: úplné pořadové pravděpodobnosti, otevřená prvočíselná poznámka

**Aktualizace 17. listopadu 2026:** C048 je nyní potvrzen jako chybné
znění a připsání historického výsledku. Původní práce z let 1896 a 1899
byly získány a příslušné pasáže zobrazeny. Kvantitativní mez z roku 1899
má v exponentu odmocninu z logaritmu. Nejde o důkaz nepravdivosti silnější
tištěné asymptotiky. Podrobnosti a přesné stránky jsou v
`C048-prime-number-error-exponent.md`; následující text zachovává stav
původní kontroly ze 7. listopadu.

7. listopadu 2026. Celé zadání p23/file43 a odpověď p388/file408
přímo zobrazeny, stejně jako autorský PS11.9.2019 p44–45/files50–51.
Detail exponentu z původního PDF potvrzuje absenci odmocniny.
Šest vrstev errat a tři TeX zdroje bez použitelné opravy113.
F175 je potvrzená lokální chyba jmenovatele; C048 je pouze
kandidát k zamýšlenému znění asymptotické meze. Celá úloha
zůstává partial kvůli této matematické poznámce, nikoli kvůli
nedostupné bibliografii. Žádný nový matematický běh ani restart.

##(a): všechny okraje a kompletní události

Nechť n≥1, 1≤k≤n a množiny L={a_1,...,a_l}, {b},
R={c_1,...,c_r} jsou vzájemně disjunktní, takže l+r+1≤n.
Událost E vyžaduje, aby obrazy prvků L byly<k, bπ=k a obrazy
prvků R byly>k. Je-li l≥k nebo r>n−k, potřebné obrazy se
nevejdou do dostupných k−1, respektive n−k hodnot, takže P(E)=0.
To platí pro libovolnou rodinu permutací. Také k mimo1,...,n
dává nulovou pravděpodobnost; používáme přirozený celočíselný obor.

V kompletním případě l=k−1,r=n−k jde přesně o událost
{x:xπ<bπ}=L. Všechny její předpoklady i inkluze a exkluze
byly úplně dokázány v(1) `sequential-mpr-ex112.md`; dosadíme
t=k−1. Pravděpodobnost je

```
(k−1)!(n−k)!/n! = 1/(n binom(n−1,k−1)).              (1)
```

Není zde předpoklad nezávislosti různých obrazů. Důkaz používá
jen minwise vlastnost pro všechny příslušné podmnožiny.
Rovnoměrně náhodná permutace všech n prvků má tutéž
pravděpodobnost, protože obrazy L lze uspořádat(k−1)! způsoby,
obrazy R (n−k)! způsoby a obraz b je pevný.

V nekompletním případě je q=n−l−r−1 volných prvků. Musíme
vybrat právě k−1−l z nich, které mají být pod k; ostatní musí
být nad k. Tyto kompletní události jsou disjunktní, jejich
sjednocení je přesně E a je jich binom(q,k−1−l). V každé
platí(1), takže

```
P(E)=binom(n−l−r−1,k−1−l) (k−1)!(n−k)!/n!
    =(k−1)_l (n−k)_r (n−l−r−1)!/n!,                (2)
```

kde (x)_j je klesající součin a prázdný součin je1.
Oba vzorce platí v přípustném oboru; mimo něj použijeme výše
odvozenou nulu. Kraj l=r=0 dává1/n, n=1 dává1. Nezavádíme
faktoriály záporných čísel.

V tištěném příkladu b=2,k=7,L={5},R={1,8} jsou pro n≥8
prvky skutečně odlišné. Z(2) dostaneme přesně
6(n−7)(n−8)(n−4)!/n!. Pro n=8 je pravá strana0: nad7
zbývá jen jediný obraz, ale R má dva prvky. Pro n≥9 odpovídá
čitatel šesti možnostem pro5π, dvěma uspořádaným odlišným
horním obrazům a libovolnému dokončení zbývajících n−4 pozic.

## Každý tištěný mezikrok a F175

Přejmenování domény a_i=i,b=k,c_j=k+j v kompletním případě
je dovoleno: bijektivní přejmenování zachovává minwise vlastnost
všech podmnožin. Hodnoty obrazů se nepřejmenovávají. Pro
B⊆{1,...,k−1}, |B|=t, je

```
A={k,...,n}∪B, |A|=n−k+1+t,
P_B=P(min_{a∈A} aπ=kπ)=1/(n−k+1+t).                 (3)
```

Tisk však uvádí1/(n−k+t), tedy vynechává1. Není to jiná
konvence pro t: text výslovně říká, že B má t prvků.
Opravit jmenovatel v(3); následující inkluzní rozklad má správná
znaménka a správné podmnožiny. Pro k=4 jsou přesně:

```
P_empty−P_{1}−P_{2}−P_{3}+P_{1,2}+P_{1,3}+P_{2,3}−P_{1,2,3}.
```

Každý z osmi členů s opravenou(3) má podle minwise definice
stejnou hodnotu jako u všech permutací, a proto i celý součet.
Pro n=5,k=4 jsou všechny vytištěné jmenovatele kladné, přesto
chybná formule dává

```
1−3/2+3/3−1/4 = 1/4,
```

zatímco opravená formule dává

```
1/2−3/3+3/4−1/5 = 1/20 = 3!1!/5!.
```

To je přesný konečný rozpor v samotném příkladu: ze120
rovnoměrných permutací jsou žádoucí právě šest uspořádání
prvků1,2,3 pod4 při4π=4 a5π=5. Není potřeba je enumerovat.
Ještě menší n=2,k=1,t=0 dává v jediném členu tištěnou1
místo správné1/2. Při k=n,t=0 je chybný jmenovatel dokonce0.

F175 low, lokální chyba mezikroku pouze na p388/file408.
Hlavní(a,b) zůstávají platné. Původní PDF i autorský PS51
obsahují stejnou chybějící1; žádná ze šesti vrstev a tří TeX
zdrojů ji neopravuje. Fyzický výtisk ani kořenové přijetí
nebyly ověřeny.

##(b), maxwise a všechny pořadové kraje

Nechť A má k prvků a a_j∈A. Pro každé absolutní K=a_jπ
a každou úplnou množinu T prvků s obrazem<K je příslušná
událost kompletním případem(a). Požadované r-té největší
pořadí nastává právě tehdy, když

```
|T∩(A\\{a_j})|=k−r.
```

Takové události jsou navzájem disjunktní, protože každá
permutace určuje jedno K a jedno T. Jejich sjednocení je
přesně požadovaná událost. Každá má podle(a) stejnou
pravděpodobnost jako u rovnoměrné permutace celého[n].

U té je každé relativní pořadí k označených prvků stejně časté:
vybereme jejich k obrazů binom(n,k) způsoby a zbytek doplníme
(n−k)! způsoby, nezávisle na zvoleném relativním pořadí.
V každém pevném pořadovém místě leží a_j v(k−1)! z k!
pořadí. Proto má r-té největší pořadí pravděpodobnost1/k
pro všechna1≤j,r≤k. Zvlášť r=1 dává maxwise a r=k
minwise; k=1 dává1. Shody obrazů nikdy nenastanou.

Primární článek Broder–Mitzenmacher, RSA18(2001),18–30,
byl získán z autorského webu. Původní p24–25 byly zobrazeny:
Lemma5 a Theorem2 odpovídají přesně zdejším úplným událostem
a rank uniformitě. Jejich použitý lemma-předpoklad máme navíc
vlastním inkluzním důkazem výše. Nepřebíráme ostatní výsledky
článku o robustnosti nebo úplnosti vzorkovacích metod.

## Definice ψ, úplný důkaz Θ(n) a přesný číselný údaj

Pro každé prvočíslo p má L(n)=lcm(1,...,n) exponent roven
největšímu j≥0 s p^j≤n, protože právě tolik je nejvyšší mocnost
p v některém z čísel1,...,n. Logaritmováním proto

```
ψ(n)=ln L(n)=Σ_{p prvočíslo} Σ_{j≥1,p^j≤n} ln p.
```

Všechny součty jsou konečné. Pro n=1 je L=1 a ψ=0.
Dolní mez ψ(n)≥(n−1)ln2 je úplně dokázána v MPR111;
přebíráme přesně její elementární prvočíselný rozklad, bez
nového výpočtu či asymptotického předpokladu.

Pro horní mez si všimněme, že každé p^j∈(m,2m] přidá1
k exponentu p v binom(2m,m): v příslušném členu faktoriálového
rozkladu je floor(2m/p^j)−2floor(m/p^j)=1 a všechny další
členy jsou0 nebo1. Proto

```
ψ(2m)−ψ(m) ≤ ln binom(2m,m) ≤ 2m ln2.
```

Poslední nerovnost plyne z binom(2m,m)≤Σ_j binom(2m,j)=2^(2m).
Pro 2^(s−1)<n≤2^s monotónnost a teleskopování dávají
ψ(n)≤ψ(2^s)≤(2^(s+1)−2)ln2<4n ln2. Spolu s dolní
mezí pro n≥2 je tím Θ(n) úplně dokázáno, nezávisle na
historickém Chebyshevově článku.

Pro19≤n≤22 jsou nejvyšší prvočíselné mocnosti
16,9,5,7,11,13,17,19. Žádné z20=4·5,21=3·7,22=2·11
nepřidá vyšší mocnost. Součin lze přímo ověřit:

```
16·9·5·7=5040,
5040·11=55440,
55440·13=720720,
720720·17=12252240,
12252240·19=232792560.
```

Seznam prvočísel do22 je úplný dělením pouze2 a3 pro čísla
do22: každé složené číslo≤22 má prvočíselný dělitel≤sqrt22<5.
Každá uvedená nejvyšší mocnost se mezi1,...,n vyskytuje, takže
jejich součin není jen společný násobek, ale právě nejmenší.
Číselný údaj knihy i interval19≤n≤22 jsou správné.

## C048: tištěná asymptotická mez není tímto auditem doložena

Původní PDF i PS mají skutečně

```
ψ(n)=n+O(n exp(−C log n)), C>0 konstantní.            (4)
```

Odmocnina nad logaritmem chybí v obou sazbách; nejde o OCR.
Při libovolném pevném základu logaritmu je to
ψ(n)=n+O(n^(1−δ)) pro nějakou pevnou δ>0. Změna základu
jen mění konstantu, nemůže z log n udělat sqrt(log n).

Jako přesně vymezené srovnání byl přečten primární článek
Trudgian, arXiv:1401.2689v2 (17.10.2014), Theorem1 na p3,
včetně původního zobrazení. Uvádí pro x≥23

```
|ψ(x)−x| ≤ x sqrt(8/(17π)) X^(1/2) exp(−X),
X=sqrt((ln x)/6.455).
```

Tento tvar dává O(x exp(−c sqrt(ln x))) pro každé pevné
0<c<1/sqrt(6.455), protože čtvrtá odmocnina ln x je pohlcena
libovolným malým exponenciálním oslabením. Nedává(4): poměr
sqrt-založené exponenciály k exp(−δ ln x) roste do nekonečna.
Samotná slabší horní mez však není protipříkladem k silnější.
Žádný důkaz nepravdivosti(4) zde nemáme a netvrdíme jej.

Možný zamýšlený text je −C sqrt(log n). To je interpretace
k dalšímu ověření, nikoli potvrzená oprava. Chybějící přímý
důkaz silnější meze nelze nahradit konečným testováním hodnot
ψ: big-O má neurčenou konstantu i počátek platnosti.

Primární historický článek z1896 nebyl v plném rozsahu posouzen.
Jeho přesnou atribuci a historické datum formulace odhadu proto
ponecháváme jako bibliografickou výjimku. Samotná matematická
platnost tištěné(4) je navíc samostatná otevřená mezera, a proto
MPR113 i odpovídající část file408 zůstávají partial.
Není to tvrzení, že prvočíselná věta nebo klasická slabší mez
jsou nepravdivé. Jejich úplný analytický důkaz včetně externích
odhadů nul zeta-funkce tento audit nereprodukoval; primární
zdroj zde slouží k přesnému porovnání formulací.

Také formulaci „roughly as e^n“ chápeme jako logaritmickou
asymptotiku L(n)=exp(n+o(n)), která plyne z ψ(n)=n+o(n).
Není to tvrzení L(n)/e^n→1. Tuto implikaci ověřujeme algebraicky;
chybějící silnější odhad(4) tím neuzavíráme. Exponenciální
velikost explicitního seznamu je doložena už vlastní Θ(n)
mezí výše a nevyžaduje(4).

Numdam potvrzuje Chebyshevovu citaci JMPA17(1852),366–390;
přesnou historickou prioritu a celý původní text neprohlašujeme
za zkontrolované. Jsou to dvě výslovné historické bibliografické
výjimky (Chebyshev a de la Vallée Poussin), oddělené od C048.

Výsledek: celé(a,b), každý jejich mezikrok po F175, ψ-identita,
Θ(n), přesný LCM a praktická exponenciální dolní mez jsou doloženy.
Asymptotický exponent a jeho zamýšlená oprava zůstávají C048;
celkový stav113 je partial. Další sekvenční práce pokračuje114.
