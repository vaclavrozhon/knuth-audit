# Souvislá revize Wallaceovy úlohy §3.4.1–31

6. listopadu 2026, X0124. Znovu přímo přečteny původní 119, 132,
141 a 589–590. Celé starší `wallace-normal.md`, všech 179 řádků
verifieru, všechny čtyři PASS bloky a celý JSON přezkoumány.
C0058 zůstává **confirmed, high**. Nový nález nepřibyl a žádný
starý experiment nebyl spuštěn znovu.

## Co důkazy skutečně říkají

Část (a) je správná: charakteristická funkce lineární kombinace
nezávislých standardních normálních veličin je exp(−t²/2), když
součet čtverců koeficientů je jedna. Ortogonální transformace
zachovává celou společnou hustotu jednoho zásobníku. Nevytváří
nezávislost nového zásobníku na starém. Krajní sin θ=0 při redukci
počtu sčítanců se řeší přímo, není potřeba dělit nulou.

V (b) pro kladné A,B se součtem větším než jedna má rovnice
A r⁻²⁴+B r⁻⁵⁵=1 jediný kladný kořen r>1. Rovnost v trojúhelníkové
nerovnosti a gcd(24,55)=1 dokazují, že žádný jiný charakteristický
kořen nemá modul r. Kořen je jednoduchý. Koeficient dominantního
členu je nenulová lineární forma počátečních 55 hodnot, takže při
nezávislé normální inicializaci je nenulový skoro jistě.
Výjimečné deterministické počátky nejsou tvrzením vyloučeny.
Archivované přesné racionální intervaly šířky 10⁻³⁰ pro oba kořeny
jsou doloženy znaménky celočíselných polynomů; obecný růst na jejich
desetinném vyčíslení nezávisí. Následující návrh proměnlivých úhlů
je v knize výslovně nejistý, nikoli důkaz statistické kvality.

V (c) jsou liché afinní násobitele modulo 1024 skutečně permutace.
Dvě permutace a rotace dvojic tvoří ortogonální transformaci;
součet čtverců S zůstává zachován. Cena dvou násobení a jednoho
sčítání na novou hodnotu nezahrnuje indexování, výběr parametrů,
předvýpočet ani vynechané výstupy. Tištěný čitatel škálování
T=(W+√(2d−1))²/2 má střed d a rozptyl 2d−1/2. Jeho třetí
kumulant je 6d−2 oproti 8d u χ²_d. Kniha jej správně označuje
za aproximaci; tento rozdíl není novou chybou.

## C0058 a kontrola jeho předpokladů

Odkaz na úlohu 23 volí U,V kladné v jednotkovém čtvrtkruhu.
Proto s=2UV/(U²+V²) nemůže být záporný. Jeden společný úhel
na obnovu zásobníku je přímým výkladem uvedených vzorců na 590;
nejde o Brentovu jinou implementaci s úhlem měněným uvnitř průchodu.
Po doporučeném odmítání malých |c| a |s| má úhel rovnoměrný zákon
na [π/6,π/3] ∪ [2π/3,5π/6]. Přesný integrál dává

```
E(c)=0,   β=E(s)=3(√3−1)/π.
```

Uniformní posun každé afinní permutace dává střední matici J
se všemi prvky 1/N. To plyne z jediné návštěvy každého indexu
při proběhnutí všech posunů, nikoli jen z testu součtu indexů.
Pro nezávislé obnovy má tedy střední dvoukroková transformace
hodnotu −β² diag(J,J). Pokud se po každé obnově vrací prvních
m=682 hodnot X, normalizovaný součet L má rozptyl jedna, ale

```
Cov(L_t,L_(t+2)) = −(m/N)β² = −0.325469000481936…,
N=1024, d=2048.
```

Pořadí vracených hodnot je explicitní součást protipříkladu.
Odpovídá přirozenému odběru asi třetiny zásobníku a doporučení
vracet škálované X_j. Nepředstíráme výsledek pro libovolný
nezapsaný plán výběru nebo proměnlivé úhly uvnitř průchodu.
Při pevném poměru m/N se tato korelace nezmenšuje zvětšením zásobníku.

Škálování je přesně a=|W+√(2d−1)|/√(2S), W=Y_(N−1), Z=aL.
Kladná odmocnina zahrnuje i vzácné záporné W+√(2d−1). Vektor L
je kolmý k souřadnici W. Z nezávislosti gaussovského směru a délky
plyne E(L²/S)=1/d a E(W²L²/S)=1/(d+2). Zrcadlení ve směru L
ponechá W,S beze změny, proto E(Z)=0. Dále přesně

```
Var(Z)=1−1/[d(d+2)]<1,
E((Z−L)²)≤1/(d+2)+(8d+1)/(d(2d−1))<1/400.
```

První člen druhé meze pochází ze sférického čtvrtého momentu;
druhý používá E(S)=d, Var(S)=2d a jmenovatel alespoň 2d−1
po racionalizaci rozdílu odmocnin. Cauchyho nerovnost omezí
změnu dvoukrokové kovariance na méně než 1/10. Proto i po
tištěném škálování platí **Cov(Z_t,Z_(t+2))<−11/50**.
Důkaz nepředpokládá S=d a nepotřebuje simulaci.

Náhodné nezávislé znaménko sinu vynuluje E(Q) a odstraní právě
tento mechanismus. Nedokazuje nezávislost celého proudu ani
nepřítomnost závislostí vyšších momentů. Závažnost high odpovídá
silnému dopadu na součty a odhady průměrů, nikoli tvrzení,
že každý Wallaceův generátor je chybný.

## Přijaté výsledky a primární literatura

Archiv obsahuje 682 afinních permutací a 18 724 kontrolovaných obrazů,
65 664 přesných uspořádaných dvojic malých matic a 32 768 nových
normálních zásobníků v popisném experimentu. Malé matice používají
c=±3/5, s=4/5, takže jsou nezávislou kontrolou maticového odvození,
nikoli numerickou náhradou spojitého úhlového integrálu. Experiment
generuje úhly odmítáním skutečných bodů čtverce a porovnává varianty
se společnými počátečními zásobníky; tyto dvě varianty tedy nejsou
navzájem nezávislé. Uvedené standardní chyby platí pro jednotlivé
empirické průměry, nejsou kalibrací testu celé kvality generátoru.
Všechny čtyři bloky dříve skončily PASS; nyní byla kontrolována
jejich konstrukce, výstupy a rozsah, bez opakování.

Celý devítistránkový [Brentův preprint 1997](https://maths-people.anu.edu.au/~brent/pd/rpb170tr.pdf)
přečten v textu, strana 7 také znovu v obrazu. V něm se matice mění
uvnitř průchodu a povolené úhly zahrnují záporné hodnoty. Nejde
o přesný recept z 590. Oddíl 8 skutečně popisuje měření rychlosti,
testy transformovaných párů a momentů, včetně problémů čtvrtého
momentu při odběru všech hodnot. To dokládá dobovou zprávu o
rychlosti a úspěšných testech Wallaceových variant na 132.
Není to nezávislá reprodukce těchto měření ani potvrzení statistické
kvality přesného knižního receptu. Velké testy se podle pokynu
uživatele neopakují.

V [pozdějším Brentově preprintu](https://maths-people.anu.edu.au/~brent/pd/rpb213.pdf)
přečten oddíl 5 a strany 2–4 vizuálně. §5.2 již výslovně doporučuje
náhodná znaménka, §5.6–5.7 popisují jiné zbytkové závislosti.
Obecná myšlenka tedy není nová. Hlavička tohoto lokálního preprintu
má rok 2003; [autorův publikační záznam](https://maths-people.anu.edu.au/~brent/pub/pub213.html)
ověřený dnes potvrzuje vydání Computer Journal 51 (2008), 579–584.
Rok v místním názvu souboru označuje publikaci, nikoli datum rukopisu.

[Autorův záznam článku 1998](https://maths-people.anu.edu.au/~brent/pub/pub185.html)
potvrzuje LNCS 1470, 1–20, tedy známou opravu citace z 8. července 1999.
Jeho celý dvacetistránkový text zde auditován není. Původní Wallace 1996
má dřívější institucionální metadata; tehdejší pokus o vydavatelský PDF
vrátil 403. Dnešní rychlý pokus otevřít institucionální seznam selhal.
Plný Wallaceův článek se proto stále neprohlašuje za přečtený.
Brent uvádí také předchozí technickou zprávu z února 1994; rok 1996
v knize lze číst jako rok časopiseckého uvedení, bez nového nálezu
z pouhé existence staršího preprintu.

Všechny čtyři vrstvy errat a aktuální TeX znovu prohledány podle
119/132/590, Wallace, sinusu, náhodných znamének a citace. Známá změna
na 590 upravuje pouze bibliografii; oprava C0058 nenalezena.
Fyzický nejnovější dotisk a prvenství zůstávají neověřené.
Nová korespondence nevznikla.

## Zbývající rozsah §3.4.1

Všechny části A–G a všech 33 úloh nyní mají souvislou revizi;
úloha 21 zůstává partial kvůli globálnímu maximu E. Kandidát C0246
k popisku obrázku 13 zůstává otevřený. Neověřená fakta jsou globální
historické tvrzení na 119, časový poměr na 134 a dobové doporučení
α=7/8 na 137. Wallaceova úloha nevylučuje existenci jiného praktického
přímého generátoru a sama neuzavírá záporné historické tvrzení na 119.
Naopak zpráva o dobových testech na 132 má nyní konkrétní primární
doklad, s přesnou výjimkou pro jejich opakování.

Strany 141 a 589 jsou celé prošlé. Strana 590 je stále partial kvůli
následujícím odpovědím §3.4.2; jejich přítomnost nelze přehlédnout.
Další kurzor je původní 142/file 154, §3.4.2.
