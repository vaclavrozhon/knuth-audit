# Souvislá revize §3.3.3: úlohy 18–28 a konec textu

6. listopadu 2026, X0103–X0104. Přečteny původní strany 90–93,
574–577, dřívější úplné poznámky a tři nálezové důkazy C0033–C0035.
Znovu přečten celý `verify_theoretical_tests.py`, jeho pět výsledných
bloků a log; také celý `verify_discrepancy_frontier.py`, výsledky a log.
Žádný z těchto běhů se neopakoval.

C0033–C0035 zůstávají potvrzené v našem prvním dotisku. Nový nález
v tomto bloku nepřibyl. Ostrá obecná mez v komentáři úlohy 19 zůstává
`partial`; žádný konečný soupis ji nepřepisuje na obecný důkaz.
Celá §3.3.3 je nyní souvisle prošlá, nikoli úplně uzavřená.

## Částečné součty a obdélníky, 18/19

Váha floor(j/k)−floor((j−z)/k) počítá počet zástupců zbytku j
v intervalu 0,…,z−1. To dokazuje první rovnost odpovědi 18 i pro
z≥k. Rozvinutí pilovité funkce dává dva delta příspěvky na krajích;
součet ostatních prvků podle replikačního zákona je d·psi(c/d).
Výsledný vzorec v knize tedy platí pro libovolné reálné c a kladná
celá h,k,z, včetně soudělných h,k. Přijato 6525 přesných kontrol
proti přímému součtu; obecný argument na tomto počtu nezávisí.

V 19 je indikátor intervalu přesně rozdílem dvou podlah. Rozvinutí
součinu dává čtyři uvedené Dedekindovy součty. Dva smíšené delta
členy mají každý absolutní součet nejvýše 1, součin delt nejvýše
1/2. Proto platí tištěné |epsilon|≤2.5/m. Přijaté výsledky zahrnují
27124 obdélníků a přesná maxima pro 95 plnoperiodických násobitelů;
větší explorace 7805 nesoudělných dvojic končí m=160.

Přezkoumán také obecný převod na středové součty. Označme

```text
r_j = (j+1/2)/m−1/2,
tau(a,m,c) = 12 sum_j r_j r_((aj+c) mod m),
F_a(n) = sum_(0≤j<n) ((aj mod m)−(m−1)/2)/m,
R(a,m) = max F_a − min F_a.
```

Přímým rozvinutím platí pro inverzi a' modulo m

```text
tau = sigma + 6psi(a'c/m)−6psi(c/m)+3[c=0 mod m]−3/m.
```

Středové indikátory nemají delta zbytek. Vzorec pro obdélník tedy
platí přesně se čtyřmi tau místo sigma. Rozdíl sousedních tau je
−12r_j pro j=−a'(c+1) mod m; z toho plyne osc(tau)=12R(a',m).
Symetrie j↦m−1−j dává tau(c)=tau(a−1−c). Jsou-li H,L argumenty
maxima/minima, vezmeme šířku w=a'(a−1−H−L) mod m a svislý
cyklický interval začínající v −H s délkou H−L mod m. Jeho čtyři
rohy jsou H,L,a−1−H,a−1−L, takže obě maxima a minima jsou dosažena
současně. Přechod přes okraj řeší doplněk intervalu.

Pro maximální absolutní obdélníkovou odchylku D proto přesně platí

```text
mD = osc(tau)/6 = 2R(a',m) = 2R(a,m).
```

Poslední rovnost plyne z prohození souřadnic. D se zde vztahuje
jen k celočíselným hranicím před dělením m, jak požaduje zadání;
nejde o supremum přes libovolné reálné hranice. Uložených 3043
modelů ověřuje i konkrétní maximalizující obdélník, 1101 z nich
navíc proti nezávislému úplnému hledání. To doplňuje obecný důkaz.

Zbývá dokázat R(a,m)≤A/8, kde A je součet Eukleidových podílů.
76115 dvojic do m=500 prošlo, ale to tuto mezeru neuzavírá.
Jednokroková i dvoukroková jednoduchá indukce byly již vyvráceny;
jejich konkrétní protipříklady v původní poznámce zůstávají platné.
Přesná rekurence pro jednotlivý částečný součet také sama neomezuje
rozpětí všech součtů. Tyto neúspěšné směry se znovu nepočítaly.

Dolní komentář lze vymezit přesněji. Knuthův primární článek 1977,
rovnice (4.28) na 317, dává osc(sigma)≥3(A−E)/2−8, kde v sudé
kanonické reprezentaci E=sum_j (q_j mod 2)/q_j. Jde o lichou
hodnotu podílu, nikoli lichou pozici. Jelikož |tau−sigma|≤6,

```text
mD ≥ (A−E)/4−10/3.
```

Podmínka A−2E≥80/3 tedy zaručuje D≥A/(8m). To je rigorózní
dostatečný význam poznámky o velkých podílech. Neprohlašujeme
stejnou dolní mez za platnou pro každou konečnou dvojici.
Kvalitativní O(1/sqrt(m)) při a řádu sqrt(m) plyne již ze slabší
horní meze A/(4m)+O(1/m), protože A≤floor(m/a)+a.

Krátká další rešerše přinesla dostupnou vydavatelskou verzi
[Borda 2023, Lemma 9](https://academic.oup.com/imrn/article/2023/22/19340/7193654).
Její přesná Ostrowského formule souhlasí s již uloženým preprintem.
Členy závisejí i na nižších číslicích; samotná formule zde není
důkazem požadované ostré meze. Pozdější limitní věty neauditovány.
Vyhledaný úryvek Niederreitera a Dieterova bibliografie nedodaly
nový přečtený důkaz přesné konstanty. Pokusy jsou ve zdrojovém JSON.

## Poklesy a spojité modely, 20–25

V odpovědi 20 zkontrolováno všech devět součinů a jejich znaménka,
změny indexu pomocí inverze a, i redukce S9 přes třídu c mod d.
Příspěvek součinu delta členů je −1/4 pro m>2; při m=2 se první
a třetí nulový stav shodují a příspěvek je −1/2. To je přesně C0034:
chybí −[m=2]/(4m). Přijatých 2133 přesných modelů obsahuje jedinou
odchylku původního výsledku, a=1,c=1,m=2, tištěných 1/8 proti 0.

V 21 přímá integrace na afinních větvích potvrzuje pomocné s_n,
opravu krajního intervalu a C=(1−6theta+6theta²)/a pro kladné a,
včetně a=1. V 22 se pro a>1 délky sestupných intervalů sečtou na
1/2. Při a=1 je délka theta: to znovu potvrzuje C0035, nikoli
chybu integrálu 21. Oprava rovnoměrnosti x z roku 2005 toto neřeší.

V 23 přímé dělení na afinní větve dává všechny dva součty i člen
max. S n=floor(a theta) se získá přesně tištěný vzorec a stejnoměrná
asymptotika. Na intervalech je funkce po částech lineární: směrnice
je záporná před aktivací max a kladná po ní. Minima leží v j/(a+1).
Jejich nejmenší odchylka od 1/6 je

```text
(a−2)/(24a(a+1)) pro sudé a,
(a−3)/(24a²) pro liché a.
```

Tedy pro a≥4 je pravděpodobnost vždy >1/6. Výjimky a=2 s theta=1/3
nebo 2/3 a a=3 s theta=1/2 jsou již zaznamenané; nevyvracejí výrok
o velkých a. Přijato 174 přesných integrálních/intervalových modelů.

V 24 délka větve po t−1 poklesech je j1/(a^(t−1)(a−1)); součet
j1 přes slabě uspořádané kladné cifry je binom(a+t−2,t).
Ocasový součet dává (a/(a−1))^a−a/(a−1), s uvedeným rozvojem
e−1+(e/2−1)/a+O(1/a²). Převod x↦1−x mimo nulovou množinu
potvrzuje růstové běhy. a=1 je nutno vyloučit podle C0035.
59 přímých intervalových modelů přijato bez opakování.

V 25 průniky předobrazů s [alpha,beta) dávají tištěné ceil indexy
a oba krajní členy. Chybu lze také přímo omezit integrálem
periodické centrované indikátorové funkce: její primitivní funkce
má rozpětí h(1−h)/a, kde h=beta'−alpha'. To je ostře menší než
tištěných 2h/a pro 0<h≤1. Přijato 12348 přesných obdélníků.

## Geometrie běhů a obrázky, 26–28

Obrázek A-1 je rozdělen přímkami x=y a x+y=1 na čtyři stejné
trojúhelníky; dvě pořadí jsou nemožná. V A-2 se pracuje s hustotou
2 v x>y. Dokud běh roste, nedochází k přetečení; plocha trojúhelníku
pro délku alespoň k≥2 je 1/(2 F[k−1]F[k+1]). Rozdíl sousedních ploch
dává správný obecný vzorec. C0033 je pouze tabulková záměna ocasu
a přesné délky. Opravený řádek pro k=1,…,5 je
1/2, 1/6, 7/30, 7/120, 41/1560. Náhodný řádek a obrázek jsou správné.
Přijata nezávislá polygonová rekurence pro 15 délek; při vytváření
oblastí nepoužívá Fibonacciho vzorec.

V 28 přímá integrace dvou oblastí x<y<z pro z={alpha+2y−x} dává
(1−alpha)²/4+alpha²/4. Plochu zachovávající involuce (x,y)↦(z,y)
obrací první a třetí pořadí. Dále Pr(x<y)=Pr(x>y)=1/2, takže všechny
čtyři ostatní pravděpodobnosti jsou 1/8+alpha/4−alpha²/4. Všech šest
je 1/6 právě pro alpha=1/2±sqrt(3)/6 modulo 1. Zkontrolovány přímky,
průsečíky a popisky A-3; přijato 47 nezávislých polygonových modelů.
Franklinův původní Theorem 13 nebyl přečten, proto jeho atribuci
uvádíme jako bibliografickou výjimku, nikoli jako podklad důkazu.

Původní log ponechává dvě dřívější selhání: odhalení C0034 a vlastní
chybu modelu, který do polygonů vpustil desetinná čísla. Konečný
program má všechny vrcholy i přímky typu Fraction a dokončené bloky
prošly. Dřívější chybu validátoru netajíme ani nepovažujeme za chybu knihy.

## Pokrytí a návaznosti

Čtyři vrstvy errat a aktuální TeX znovu prohledány. Opravy uniformity
v 22 a označení obtížnosti M28 u 23 jsou známy; C0033–C0035 neřeší.
Fyzický novější tisk, prvenství a autorovo uznání nálezů neověřeny.

Na straně 74 je návaznost na 23/24 správně formulovaná jako důvod
k podezření na delší běhy. Tyto spojité výsledky nejsou úplným
důkazem pro všechny konečné LCG. Odkaz je nyní prověřen; stránka
zůstává částečná kvůli §3.5–26. Zbytek strany 75 se tím neuzavírá.

Celé 92,575,576 mají novou stránkovou revizi. 91 zůstává částečná
kvůli měřením v 14, 90 a 574 kvůli ostré mezi 19 a dopředné
závislosti průměru, 93/577 kvůli začínající §3.3.4. Historie praxe
na 88 je otevřená. Přesné důvody zůstávají v UI a v coverage.json.
Další souvislý kurzor je §3.3.4 od 93, odpovědi 577. Nic neodesláno.
