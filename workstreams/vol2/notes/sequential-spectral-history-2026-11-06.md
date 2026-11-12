# Souvislá revize §3.3.4: kontinuanty, historie a závěr

6. listopadu 2026. Navazuje na čtyři poznámky `sequential-spectral-*`.
Původní sazba 114–115, 117–118 a 584 byla znovu zobrazena; stránka
souboru je tištěná strana + 12. Matematická část F a odpovědi 30/32
se neopakují. Nový nález **V2-C0245 je pouze bibliografický, nízké
závažnosti**. Zbytek tohoto bloku nepřidal potvrzenou matematickou chybu.

## Úloha 31: přesný rozsah

Úloha je označena jako výzkumná. Kontrola formulace, uvedených důsledků
a konečných experimentů není vyřešením požadavku pro všechna dostatečně
velká m. Dnešní stav literatury neodvozujeme z absence výsledku ve
staré knize. Všechny čtyři vrstvy errat a aktuální TeX byly znovu
prohledány; opravy z 2. dubna 2013 byly zobrazeny přímo na stranách
4 a 13 `all2-pre`:

- obtížnost HM47 → HM48, atribuce Borosh → Borosh a Niederreiter;
- doplnění Kontorovichova přehledu, Bull. AMS 50 (2013), 187–228;
- BIT 25 (1980), 193–208 → **BIT 23 (1983), 65–74**.

Tyto zveřejněné změny jsou samostatně V2-X0114. Neřeší hodnoty
exponenciálních bází ani matematickou domněnku.

### Dvě konvence zápisu

Každé kladné slovo dává continuant jako jmenovatel redukovaného zlomku;
nesoudělnost plyne z determinantů ±1 matic jednotlivých kroků.
Kanonický konečný řetězový zlomek má poslední člen alespoň 2.
Záměna konce `(d)` za `(d-1,1)` zachovává hodnotu, ale může zmenšit
největší člen. Například 3/4 = [0;1,3] = [0;1,2,1].

V odpovědi 31 je výslovně formulována existence **libovolného slova**
nad abecedou 1,2,3. V tomto continuantovém smyslu čteme i výpočty
pro abecedu 1,2. Nezaměňujeme tento výrok za přesně totožný seznam
kanonických rozvojů. Obě konvence jsou v uloženém soupisu odděleny.
Přesnou konvenci při pozdějším čtení §4.5.3 zachovat; samotná záměna
konvence není nyní prohlášena za novou chybu knihy.

### Momenty

Pro nezávislé rovnoměrné cifry z 1,…,A a počáteční K₋₁=0, K₀=1
platí Kₙ=dₙKₙ₋₁+Kₙ₋₂. Píšeme μ=(A+1)/2 a
v=(A+1)(2A+1)/6. Potom

`E Kₙ = μ E Kₙ₋₁ + E Kₙ₋₂`.

Pro A=3 je dominantní kořen 1+√2; pro A=2 dostáváme přesně
`E Kₙ = (4/5)2ⁿ + (1/5)(−2)⁻ⁿ`. Vektor druhých momentů
`(E Kₙ², E KₙKₙ₋₁, E Kₙ₋₁²)` vzniká opakovaným násobením

```
[ v   2μ  1 ]
[ μ    1  0 ]
[ 1    0  0 ].
```

Druhá mocnina této matice má všechny prvky kladné. Perronův kořen ρ
tedy skutečně určuje růst prvního momentového komponentu, protože
počáteční vektor je nezáporný a nenulový. Ověřené intervaly pro √ρ
leží nad dominantním kořenem rovnice pro průměr; odečtení `(E Kₙ)²`
nemění dominantní řád rozptylu. Charakteristické polynomy jsou

- A=3: `x³ − (17/3)x² − (13/3)x + 1`, √ρ v (2.51527723,2.51527724);
- A=2: `x³ − (7/2)x² − 3x + 1`, √ρ v (2.04032869,2.04032870).

Program kontroluje znaménka v racionálních koncích a počet kořenů
nad dolní mezí, nikoli pouze plovoucí aproximaci. Úplný momentový
kód i archivovaný výsledek byly přečteny. Nový běh nebyl potřeba.
Tištěné 2.51527 je zkrácené, nejbližší pětimístné zaokrouhlení by bylo
2.51528; u přibližně uvedené růstové báze to bez předepsané konvence
nepovažujeme za potvrzenou chybu. Heuristické „almost surely“ v odpovědi
není důkaz pokrytí všech jmenovatelů: samotné první dva momenty jej nedávají.

### Úplnost starého výpočtu a krátká kontrola certifikátů

Přečten celý `continuant_census.cpp`, celý `verify_continuants.py`
a funkce `bounded_quotients` ve `verify_spectral_details.py`.
Strom prochází všechna kladná slova až do limitu. Jmenovatel při
prodlužování roste (s neškodnou počáteční rovností u prvního 1), takže
ořezání větve při překročení limitu je správné. V použitých mezích
nepřetéká ani výpočet čitatele; jmenovatel se před porovnáním rozšiřuje
na 64 bitů. Dokončení každé kořenové větve není celý soupis; ten
potvrzuje až závěrečný řádek `COMPLETE`, který je přítomen v obou logách.

Původní nezávislý validátor ověřil Eukleidovým algoritmem každý kladný
svědek; u abecedy 3 navíc pro každý chybějící jmenovatel prošel všechny
nesoudělné čitatele. Nejde tedy jen o dva běhy téhož stromového programu.
U abecedy 2 je nezávislá úplná kontrola záporných případů omezena na
m≤500; úplnost vyšších bloků stojí na stromovém algoritmu. Obě dřívější
neúspěšná očekávání validátoru jsou stále v logu: kanonická výjimka 3618
a absence kanonického řešení pro 2³³. Opravené bloky skončily úspěšně;
chybové běhy nejsou vydávány za úspěšné.

Archivovaný soupis pro A=3 navštívil **1 072 189 037 slov** do m=2 000 000.
Neopakoval se. Pro libovolná slova má 27 výjimek, pro kanonickou konvenci
38. Pouze 54 a 150 potřebují v první konvenci člen 5; čtyři největší
výjimky vyžadující 4 jsou 2052,2370,5052,6234, jak uvádí kniha.
V kanonické konvenci přibývá mimo jiné 3618 a m=6 potřebuje 5.
Tvrzení knihy o dolní oblasti není tvrzením, že existuje jen těchto
šest výjimek; uvádí čtyři **největší** s požadavkem 4.

Pro A=2 starý soupis do 2²⁰ obsahuje 608 473 přípustných jmenovatelů
včetně 1, nebo 541 810 kanonických. V 64 blocích po 2¹⁴ jsou poměry
pro libovolná slova 0.490234375 až 0.65283203125. Knižní „appears“
a přibližné .50–.65 nečteme jako ostrou dokázanou mez každého bloku.

Rozklad mocnin 2 používá první prefix se jmenovatelem P>√m a předchůdcem
Q≤√m. Pro neprázdný zbytek platí `m=PR+QS`, gcd(P,Q)=1,
1≤S<R. Tedy

`ceil((m+Q)/(P+Q)) ≤ R ≤ floor((m−Q)/P)` a `PR ≡ m (mod Q)`.

To jsou právě meze a kongruence v obou programech. Prázdný zbytek a
zbytek tvořený jedinou 1 jsou výslovně obslouženy; druhý případ musí
být v nekanonické variantě, neboť má R=S=1. Předchozí úplné porovnání
pro m≤500 i závěrečný log byly přečteny. Všech 11 mocnin 2²⁵,…,2³⁵
má uloženého svědka. Pro 2³³ je přípustný čitatel 6038880255 a rozvoj
končí 2,2,1; kanonický konec 2,3 podmínku A≤2 poruší.

Nový `check_sequential_continuant_certificates.py` provedl jen kontrolu
čtyř uložených polí: dekomprimované SHA-256, počty, seznamy výjimek,
64 blokových četností, 65 svědků výjimek a 11 mocninných svědků.
Zlomky svědků skládá odzadu přesnou racionální aritmetikou. Běh při
nice 15: **1.943071631 s, exit 0**, session 92448. Neopakoval strom,
zkoušení všech čitatelů ani validaci všech kladných zlomků. Výsledky
minimálnosti a úplnosti jsou přijaty v rozsahu původního přezkoumaného
programu a dokončeného archivu, nikoli vydávány za nový nezávislý běh.

### Prameny a dnešní stav tvrzení

[Borosh–Niederreiter](https://link.springer.com/article/10.1007/BF01937326)
potvrzuje v metadatech BIT 23 (1983),65–74 a v abstraktu tabulky pro
mocniny 2 do exponentu 35. Plný článek není získán; jednotlivé řádky
jeho tabulek nepovažujeme za přečtené. Vlastní uložené svědky se tím
nenahrazují. [Cusickův záznam vydavatele](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0025579300009050)
potvrzuje Mathematika 24 (1977),166–172; plný důkaz nebyl nově kontrolován.
[Bourgain–Kontorovich](https://annals.math.princeton.edu/2014/180-1/p03)
v publikovaném abstraktu tvrdí hustotu jedna pro nějakou absolutní mez.
To není automaticky požadavek úlohy s mezí 2 nebo 3.

Dne 6. listopadu 2026 znovu ověřeny oficiální verze
[Zhang 2605.02518](https://arxiv.org/abs/2605.02518) a
[Shkredov 2603.14116](https://arxiv.org/abs/2603.14116): nadále v2
z 8. května, resp. 24. června 2026. Z lokálních PDF/textů byly znovu
přečteny úvody, přesná věta 1.2 a poznámka 1.3 prvního článku,
definice množiny Z, věta 8 a poznámka 9 druhého. Zde Z není označení
všech celých čísel: je to vymezená třída jmenovatelů zahrnující mj.
dostatečně velká prvočísla. Zhang tvrdí univerzální absolutní mez;
výslovně ji neztotožňuje s 5. Tyto preprinty proto **nejsou dokladem
vyřešení konkrétních mezí 2/3 z úlohy 31**. Jejich úplné důkazy ani
recenzní stav zde nezávisle neověřujeme; netvrdíme ani celosvětovou
otevřenost všech podob těchto problémů.

## Historické G a závěrečný odstavec

Znovu přečten celý krátký text Marsaglia1968 a vymezené pasáže
Coveyou1969: úvod, §10 a začátek §11, konkrétní matice v §11.3.
Gramovy matice mají prvky skalárních součinů bázových vektorů;
kvadratická forma dává normu celočíselné kombinace. To odpovídá
popisu na114 a neověřuje samostatně tvrzení o nezávislém objevu
Janssense a Dietera. Marsagliův text dokládá mřížovou/geometrickou
interpretaci. Naše C0038/C0039 o posunu a uzavřenosti Minkowského
tělesa přitom zůstávají; zdroj nepoužíváme k jejich odvolání.

Stonehamův jednorozměrný matematický důsledek lze zkontrolovat bez
nedostupného plného článku. Pro nenulový seed a primitivní a modulo p
dávají již odvozené Gaussovy meze pro neúplnou periodu absolutní
intervalovou chybu `O(√p log²p)`. Celá perioda má pro hranice na mřížce
1/p intervalovou chybu nejvýše 1; pro libovolné reálné hranice stále O(1).
Rozklad N na celé periody a zbytek tedy dává

`D_N^(1) = O(1/p + √p log²p/N)`.

Při pevném ε>0 a N≥p^(1/2+ε) jde k nule. Není to tvrzení o libovolné
vysoké dimenzi ani o nulovém seedu. Původní publikační záznam
[Stoneham1973](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/22/4/98674/on-the-uniform-distribution-of-residues-within-the-periods-of-rational-fractions-with-applications-to-normal-numbers)
potvrzuje Acta Arith.22,371–389; čtení celého článku se netvrdí.
Niederreiter1979,159–162 bylo znovu čteno v předchozím bloku;
starší bibliografické položky zůstávají ověřeny pouze v uvedeném rozsahu.

Na118 je vyjádřen záměr doplnit další sekci, nikoli tvrzení, že v tomto
vydání už existuje. Metadata [LLL1982](https://link.springer.com/article/10.1007/BF01457454)
a abstrakt/metadatový záznam [Schnorr–Hörner1995](https://link.springer.com/chapter/10.1007/3-540-49264-X_1)
odpovídají autorům, rokům a rozsahům. Pozdější datum online publikace
Schnorr–Hörner není změnou roku konference 1995.

### V2-C0245: Seysenova poslední strana

Původní118/file130 uvádí **Combinatorica13 (1993),363–375**.
[Primární záznam vydavatele](https://link.springer.com/article/10.1007/BF01202355)
uvádí **363–376**, stejně jako jeho strojová pole `citation_firstpage`
a `citation_lastpage` a metadatový záznam DOI v Crossrefu. Oba záznamy
jsou staženy a zahashovány. Prohledány všechny vrstvy errat podle
strany, jména, rozsahu a tématu; odpovídající oprava nebyla nalezena.
Jde o chybný konec bibliografického rozsahu, nikoli matematickou závadu.
Celý Seysenův důkaz nebyl kontrolován. Poslední fyzický dotisk ani
prvenství nálezu neověřeny; žádná zpráva se nepřipravuje ani neodesílá.

### Výslovné bibliografické výjimky

Nedostupné či nepřiměřeně náročné pro tento průchod: Korobov1959
a celý související výklad Kuipers–Niederreiter; úplný původní článek
Coveyou–MacPherson1967 a osobní/nepublikované priority; plný Dieter1975
(AMS znovu nedostupný); Wood1968 konkrétní427; celý Beyer–Roof–Williamson1971
a kapitoly sborníku Zaremba1972; plný Stoneham1973 a starší články
Niederreitera mimo dříve uvedený rozsah; celé důkazy Cusick1977,
Borosh–Niederreiter1983 a Kontorovichův přehled. Zdroje k následným
algoritmům na118 kontrolovány bibliograficky/abstraktem, bez auditu
každého jejich algoritmu. Nejde o ověření těchto nepřečtených pasáží.

## Stav a návaznost

Výzkumná31 zůstává `checked` ve výslovném rozsahu auditu formulace,
momentů a archivovaných experimentů, nikoli jako vyřešená domněnka.
Celá §3.3.4 má po souvislém průchodu stále `partial`: C0042/C0243/C0244
a přesně uvedené empirické/faktické mezery se neztratily. Úloha30
zůstává partial s návratem při4.5.3-42. Původní114 a115 jsou nyní
prošlé i s G;118 má nízký bibliografický nález. Strana584 navíc obsahuje
odpovědi další sekce a zůstává částečná.

Navazuje původní119, §3.4/§3.4.1: transformace náhodných rozdělení,
text, algoritmy i odpovědi. Žádný starý výpočet se nerestartuje.
