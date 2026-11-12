# §1.3.3: počty cyklů, jejich délky a inkluze–exkluze

Kontrola dne 1. 11. 2026. Vlastněný rozsah: pravděpodobnostní text na
s. 179–181, cv. 17–22 a 25–27, odpovědi na s. 524–526. Samostatně jsou
zpracovány cv. 23 a historické odkazy. Algoritmy I/J a cv. 12–16, 24,
28–38 nejsou součástí tohoto zápisu.

Autoritativní podklad je sken třetího vydání, prvního dotisku (květen 1997).
Tiráž a inventář souhlasí; soubor má SHA-256
`e2c5ee120bad91e33f617614b846849c4801115b2e7aa820f56fc5ffb9bbebb9`.
Tištěná s. p je strana p+15 v DjVu. Původní obrazy s. 179–184 a 524–526
byly přečteny; obrázky 179–180 jsou ve vlastní složce `../images/`, ostatní
v `../../../images/`. Fyzický exemplář nebyl ověřen.

## Značení a rozsah parametrů

S_n je množina permutací n různých prvků, s rovnoměrným rozdělením;
S_0 obsahuje jedinou prázdnou permutaci. C_m je počet cyklů délky m,
C je celkový počet cyklů, H_n = sum_{j=1}^n 1/j a
H_n^(2) = sum_{j=1}^n 1/j^2. Cyklus délky m budeme nazývat m-cyklem.
Počty n,k jsou nezáporná celá čísla, m kladné celé číslo; při volbě
náhodného prvku nebo jednotlivého cyklu musí být n≥1.

## Rovnice (21) a přechod od rekordů k cyklům

Pro pravděpodobnostní argument stačí tato vlastnost kanonického zápisu:
nejmenší prvek každého cyklu je první a tyto první prvky klesají.
Po odstranění závorek jsou tedy právě ony minimy zleva doprava, tj. prvky
menšími než všechny předchozí. Naopak vložení závorky před každé takové
minimum vytvoří právě kanonický zápis. To dává bijekci, a proto zachovává
rovnoměrné rozdělení. Samostatnou implementaci kanonického převodu
kontroluje jiný pracovník.

Nezávisle lze rozdělení C odvodit vkládáním prvku n do permutace z S_(n-1).
Existuje n stejně pravděpodobných možností: nový singleton nebo vložení za
kterýkoli z n-1 dosavadních prvků. Jen singleton zvýší C. Jeho generující
funkce, tj. polynom E z^C, je tedy

```
E z^C = product_{j=1}^n (z+j-1)/j.
```

To je generující funkce součtu nezávislých Bernoulliho veličin
s pravděpodobnostmi 1/j. Proto E C = H_n a Var C = H_n-H_n^(2).
Koeficient z^k je nepodepsané Stirlingovo číslo prvního druhu [n k]/n!.
Minimum je 1 a maximum n pro n≥1. Rovnice (21) je správná v kontextu
neprázdných permutací; pro S_0 jsou obě krajní hodnoty 0.

## Počet m-cyklů a cv. 17

Vybereme m prvků, cyklicky je uspořádáme a zbytek libovolně permutujeme.
Počet dvojic (permutace, vyznačený m-cyklus) je

```
binom(n,m) (m-1)! (n-m)! = n!/m,  1≤m≤n.
```

Celkový počet cyklů ve všech permutacích je n!H_n. Výběr jednoho z těchto
cyklů má P(délka=m)=1/(mH_n), a tedy střední délku n/H_n.
Při výběru permutace a konkrétního prvku k má cyklus obsahující k délku m
v právě binom(n-1,m-1)(m-1)!(n-m)!=(n-1)! permutacích. Jeho délka je
proto rovnoměrná na 1,…,n a průměr je (n+1)/2.

Tvrzení na s. 180, že druhý průměr je větší, platí ostře pro n≥2 a
rovností pro n=1: Cauchyho nerovnost pro čísla 1,…,n dává
H_n·n(n+1)/2 ≥ n². Kontextové slovo „somewhat“ zde nepovažuji za
nový nález o triviálním n=1.

Odpověď 17 obsahuje známé úpravy z 24. 12. 2001 (závorky v jmenovateli)
a 26. 2. 2008 (označení p_m); nové věcné chyby nenalezeny.

## Pevné body, rovnice (22)–(28), cv. 19

P_nk označuje počet permutací s k pevnými body. Výběrem jejich množiny
se získá P_nk=binom(n,k)D_(n-k), kde D_j=P_j0. Rozklad S_n podle počtu
pevných bodů dává (23) a po dosazení (22) také (24).

Pro konkrétní j určených pevných bodů je počet permutací (n-j)!.
Inkluze–exkluze proto dává

```
D_n = n! sum_{j=0}^n (-1)^j/j!,
p_nk = (1/k!) sum_{j=0}^{n-k} (-1)^j/j!,   0≤k≤n.
```

Nespoléháme zde na nekonečnou řadu pro faktoriel z dřívější sekce.
V polynomu G_n(z)=sum p_nk z^k se po sloučení j+k=r uplatní binomická
věta a dostaneme G_n(z)=sum_{r=0}^n (z-1)^r/r!. Tedy G'_n=G_(n-1).
Pro n≥2 jsou první dva faktoriální momenty E C_1=E C_1(C_1-1)=1,
odkud Var C_1=1. Derangement existuje pro n≥2 (například jeden n-cyklus),
identita dává maximum n. Přehled 24 permutací pro n=4 má správné skupiny
9,8,6,0,1 a správně vyznačené pevné body.

V (25) nahrazuje erratum z 23. 12. 2024 písmeno m písmenem n a
vyjasňuje znaménka střídavé řady. Nejde o nový nález.

Pro cv. 19 je zbytek střídavé řady v absolutní hodnotě přísně mezi 0
a n!/(n+1)!=1/(n+1)≤1/2 pro n≥1. Proto D_n je nejbližší celé číslo
k n!/e (žádná rovnost na půlintegeru). Tištěná odpověď opomíjí faktor n!
ve třech místech; přesně tuto chybu opravuje erratum z 15. 9. 1999.
Tvrzení cv. 19 má ve skenu správně n≥1; OCR znak chybně rozpoznávalo.

## Cv. 20–21: zápisy a rozdělení cyklového typu

Cyklový typ je posloupnost α=(α_1,α_2,…) nezáporných celých čísel,
kde α_m počítá m-cykly. Položme c=sum α_m. Pro pevnou permutaci lze
c různých cyklů uspořádat c! způsoby a každý m-cyklus rotovat m způsoby.
Počet různých úplných disjunktních cyklových zápisů je tedy
c! product m^(α_m), včetně prázdného součinu pro n=0.

Počet permutací daného typu je

```
n! / product_{m≥1} (m^(α_m) α_m!),  pokud sum m α_m=n,
0 jinak.
```

Důkaz: vyplníme n prázdných pozic n! pořadími. Stejnou permutaci
reprezentují rotace jednotlivých cyklů a permutace α_m bloků stejné
délky. Tato akce je volná, protože všechny prvky jsou různé. Po vydělení
n! dostáváme přesně odpověď21. Dodatečný odkaz na odpověď1.2.5-21
z 10. 4. 2023 nemění tvrzení ani důkaz.

## Cv. 22(a,b): nezávislé Poissonovy počty

Zvolme 0<w<1. Označme N=sum m α_m, případně +∞. Řešením (a) je
nezávislé Poissonovo rozdělení s parametry μ_m=w^m/m:

```
f(w,m,k) = exp(-μ_m) μ_m^k/k!,   k≥0.
```

Existence: konečné součty N_M=sum_{m≤M}mα_m mají střední hodnotu
sum_{m≤M}w^m≤w/(1-w). Monotónní konvergence dává E N=w/(1-w)<∞,
tedy N<∞ skoro jistě. Pravděpodobnost každé konečné konfigurace k je
součinem pravděpodobností jednotlivých souřadnic (limitou konečných
válcových událostí); protože sum μ_m=−log(1-w), tento součin je
(1-w)w^N product 1/(m^k_m k_m!), což je požadovaná podmínka (ii).

Jednoznačnost: událost samých nul má podle (ii) pravděpodobnost 1-w>0.
Porovnání této události s konfigurací obsahující jen k m-cyklů dává
f(w,m,k)/f(w,m,0)=μ_m^k/k!. Normalizace určí f(w,m,0)=exp(-μ_m).
Tento argument odstraňuje případnou otázku dělení nulovým nekonečným
součinem v tištěné odpovědi.

Součtem přes konečně mnoho typů s N=n dostaneme P(N=n)=(1-w)w^n,
neboť pravděpodobnosti v S_n sečtené přes typy dávají1. Podmíněné
rozdělení α při N=n je přesně rozdělení cyklového typu v S_n.
P(N=∞)=0 rovněž plyne z geometrické řady. Tištěné j≥0 v několika
součinech odpovědi22(a,b) opravuje známé erratum z 1.1.2006 na j>0.

## Cv. 22(c): podmínka existence střední hodnoty

Podmínění podle N dává požadovanou rovnici, pokud φ je nezáporná
(povolíme +∞) nebo E|φ|<∞. Bez této podmínky je formulace „any function“
nesprávná; úplný protipříklad a posouzení dřívějších konvencí jsou
v `arbitrary-function-expectation.md`. To je jediný nový věcný nález
v tomto matematickém bloku.

Příklad φ=α_1 má φ_n=1 pro n≥1, φ_0=0. Původní „for all n“ je známé
erratum z 29.3.2023. Není totožné s problémem integrability.

## Cv. 18 a 22(d,e)

Lineární funkcionalita v (d) je nezáporná a má konečnou střední hodnotu,
takže není dotčena problémem v (c). Počet cyklů sudé délky má v S_n
průměr sum_{2j≤n}1/(2j)=H_floor(n/2)/2. V Poissonově modelu je průměr
sum_{j≥1}w^(2j)/(2j), jehož koeficienty po dělení 1-w dávají totéž.

Pro (e) položme q=floor(n/m). Kombinatorické faktoriální momenty jsou
E (C_m)_j=1/m^j pro mj≤n a 0 jinak, kde (x)_j=x(x-1)…(x-j+1).
Opravdu: počet uspořádaných j vyznačených m-cyklů a permutace zbytku je
n!/m^j. Binomický rozvoj z^(C_m)=(1+(z-1))^(C_m) dává

```
G_nm(z) = sum_{j=0}^q (z-1)^j/(m^j j!),
p_nkm = [1/(m^k k!)] sum_{j=0}^{q-k} (-1/m)^j/j!  (0≤k≤q).
```

Mimo uvedený rozsah je pravděpodobnost0. Toto odvození platí jako
polynomiální identita pro všechna komplexní z. Poissonova transformace
v odpovědi22(e) je přímo oprávněna alespoň pro |z|≤1; následná rovnost
polynomů ji rozšíří na libovolné z. Není nutné neoprávněně předpokládat
konvergenci dvourozměrné řady pro každou dvojici (w,z).

Všechny hraniční případy:

* n<m: C_m=0 deterministicky;
* m≤n<2m: E C_m=1/m, Var C_m=1/m−1/m²;
* n≥2m: E C_m=1/m, Var C_m=1/m.

Minimum0 je dosažitelné při n≥2m: pro m≥2 stačí identita, pro m=1
derangement. Maximum je q. Proto jsou všechna čtyři čísla ve vytištěné
odpovědi správná pro výslovně uvedené n≥2m. n=1,m=1 má min=max=ave=1,
dev=0, což není rozpor s omezenou statistikou odpovědi.

## Rovnice (29), cv. 25–27

Nechť Ω je konečná množina N objektů, S_1,…,S_M její podmnožiny.
Pro objekt patřící do s z těchto množin je jeho příspěvek do alternujícího
součtu všech průniků sum_{k=0}^s(-1)^k binom(s,k)=(1-1)^s,
tedy1 pro s=0 a0 jinak. Součet přes Ω dokazuje (29) i první důkaz
odpovědi25. Druhý důkaz indukcí na M je přesně aplikace stejného
principu uvnitř S_M na M−1 množin S_j∩S_M. Platí i M=0 a N=0.

Pro cv.26 označme N_k součet velikostí všech k-násobných průniků,
N_0=N. Počet objektů ležících právě v r množinách je

```
sum_{k=r}^M (-1)^(k-r) binom(k,r) N_k.
```

Objekt s násobností s<r přispívá0; pro s≥r je jeho příspěvek
binom(s,r) sum_{h=0}^{s-r}(-1)^h binom(s-r,h), tedy1 právě pro s=r.
Tím je ověřena i identita v odpovědi26 bez problematické interpretace
záporného horního indexu při s<r.

V cv.27 je N=a m_1…m_t a interval přesně 0≤n<N. Množina S_j obsahuje
násobky m_j. Pro neprázdnou množinu indexů J je počet násobků
product_{j∈J}m_j přesně N/product_{j∈J}m_j, protože moduly jsou po
dvojicích nesoudělné. Zahrnutí nuly je zde nezbytné pro tento přesný počet.
Inkluze–exkluze dává N product_j(1−1/m_j). Funguje i m_j=1 (výsledek0),
při opakovaném modulu1 i pro prázdný seznam (výsledek a). Odkaz na
Eulerovu funkci v cv.1.2.4-30 je správný volbou prvočíselných dělitelů N.

## Stav

Rovnice21–29 a cv.17–21,22(a,b,d,e),25–27: `checked`, s odděleně
evidovanými známými erraty. Cv.22(c): viz samostatný nový nález.
Nepřidávám nové automatické konečné testy: obecné důkazy pokrývají
všechny přípustné parametry a skeny byly porovnány přímo.
