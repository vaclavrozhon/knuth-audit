# §3.4.1-24: logistické zobrazení při konečné přesnosti

Rozsah: výzkumná úloha na str.140; v odpovědích není řešení24.
Původní stránka je již vizuálně ověřena. Nález C0053 (normalizace hustoty)
zůstává v [základním bloku](distributions-basic.md). Zde dokončujeme
požadované teoretické a empirické zkoumání pro **výslovně určené modely**.
Nejde o klasifikaci všech možných aritmetik ani o důkaz kvality generátoru.

## 1. Přesná aritmetika a její omezení

Položme f(x)=4x(1−x) pro 0<=x<=1. Jestliže x=sin²(theta), potom
f(x)=sin²(2theta). Pro theta=pi*u tak posun u -> 2u mod1 dává f.
Téměř všechny počáteční u jsou v bázi2 normální: četnost každého
k-bitového slova je2^(-k). Dyadické intervaly proto mají správné četnosti;
sevření libovolného intervalu dyadickými dokazuje rovnoměrné rozdělení
trajektorie u. Spojitá transformace pak dává hustotu

```
h(x) = 1/(pi*sqrt(x*(1−x))),
F(x) = (2/pi)*asin(sqrt(x)).                         (1)
```

Množina výjimek má míru0 i v souřadnici x: zobrazení sin²(pi*u) je
Lipschitzovské, a tedy posílá nulové množiny na nulové množiny.
Výsledek je o dlouhodobých četnostech téměř každé trajektorie;
neříká, že každý jednotlivý V_n při rovnoměrném V_0 už má hustotu(1).
Monotónní souřadnice t=F(x) převádí f na **stanové zobrazení**:
T(t)=2t pro t<=1/2, T(t)=2−2t pro t>=1/2.

Ani při přesném výpočtu nejsou po sobě jdoucí hodnoty nezávislé:
dvojice (X,f(X)) leží s pravděpodobností1 na grafu funkce. Dvě nezávislé
veličiny se spojitou hustotou by tam měly pravděpodobnost0.
Dokonce kovariance za stacionární hustoty(1) je0, neboť
E(X)=1/2, E(X²)=3/8, E(X³)=5/16, a E(X*f(X))=1/4.
Nulová kovariance zde neznamená nezávislost. Kniha v této úloze
nezávislost neslibuje.

Pro kvantované iterace x_(n+1)=f(x_n)+eta_n, |eta_n|<=delta, a přesnou
trajektorii v_n ze stejného počátku platí z |f'|<=4 indukcí

```
|x_n−v_n| <= delta*(4^n−1)/3.                       (2)
```

Jde o horní mez, nikoli tvrzení, že chyba opravdu takto roste. Typickou
infinitesimální rychlost oddalování popisuje průměr logaritmu derivace:

```
Integral h(x)*log|f'(x)| dx = log 2.                (3)
```

Dosazení x=sin²(theta) redukuje integrál na průměr log|4cos(2theta)|.
Identita Integral_0^(pi/2) log(sin theta) dtheta=−(pi/2)log2 plyne
z dvojitého úhlu a symetrie sin/cos; dává(3). Řetězové pravidlo navíc
pro nehraniční body dává přesně

```
(f^n)'(x) = 2^n*sin(2^(n+1)*theta)/sin(2theta).
```

To vysvětluje typickou ztrátu přibližně jednoho bitu počáteční přesnosti
za iteraci. Nenahrazuje to(2) ani statistický model zaokrouhlovacích chyb.

## 2. Konečná aritmetika: co platí bez experimentu

Libovolné deterministické zobrazení konečné množiny stavů nakonec vstoupí
do cyklu. Je-li počet stavů M, součet délky počáteční neperiodické části
a délky cyklu nepřekročí M. Dlouhodobé četnosti jediné trajektorie jsou
rovnoměrné na jejím cyklu, a proto nemohou přesně mít spojitou hustotu(1).
Mohou ji však přibližovat v distribuční funkci.

Pro binární aritmetiky jsou přesné pevné body0 a3/4. Navíc1/2 -> 1 -> 0
a1/4 -> 3/4. Tyto příklady samy vyvracejí jakékoli tvrzení, že **každý**
počátek musí vést k očekávaným četnostem. Nepopírají tvrzení „téměř každý“
v ideální spojité aritmetice, ani nejsou novým nálezem v knize.

## 3. Úplné grafy pevné přesnosti

Model: N=2^b, stav k představuje k/N, 0<=k<=N. Nejprve spočítáme
přesný racionální výsledek, poté zaokrouhlíme **jednou**:

```
T_floor(k) = floor(4*k*(N−k)/N),
T_even(k)  = nearest-even(4*k*(N−k)/N).
```

V druhém pravidle se přesná polovina zaokrouhlí na sudé celé číslo.
Pro(2) můžeme vzít delta=1/N, resp.1/(2N). Obě pravidla mají symetrii
T(k)=T(N−k). Modely se liší od plovoucí řádové čárky s mezivýsledky.

[Program](../verify_logistic.py) projde všech38 modelů b=2,...,20,
celkem **4 194 334 stavů i hran**. Odstraní vrcholy s nulovým vstupním
stupněm, najde zbývající cykly a zpětně přiřadí každému stavu povodí
(cyklus, do kterého dospěje) a vzdálenost od něj.

Nezávislý validátor používá druhý aritmetický vzorec
4k(N−k)/N=N−(2k−N)²/N pro každou hranu. Ověří také pro **každý stav**
shodu označení povodí se následníkem a přísný pokles kladné vzdálenosti.
Cykly jsou disjunktní, mají skutečně uvedené hrany a nulovou vzdálenost;
počty povodí sečtené přes všechny cykly dávají N+1. Tyto invarianty
certifikují úplnost rozkladu bez opakování algoritmu odstraňování.

Tabulka uvádí největší povodí. D je supremum rozdílu distribučních funkcí
cyklu a(1). Desetinné hodnoty D jsou popisné numerické výsledky, nikoli
intervalové certifikáty. Celočíselné periody a počty jsou přesné.

| b | zaokrouhlení | počet cyklů | perioda největšího povodí | počet stavů povodí | D |
|---|---|---:|---:|---:|---:|
| 8 | dolů | 3 | 4 | 252/257 | 0.23451 |
| 8 | k nejbližšímu sudému | 3 | 8 | 212/257 | 0.19380 |
| 12 | dolů | 5 | 9 | 3980/4097 | 0.35853 |
| 12 | k nejbližšímu sudému | 7 | 45 | 2180/4097 | 0.16497 |
| 16 | dolů | 6 | 79 | 43998/65537 | 0.04157 |
| 16 | k nejbližšímu sudému | 6 | 1 (nula) | 63025/65537 | 1 |
| 20 | dolů | 11 | 451 | 672272/1048577 | 0.03440 |
| 20 | k nejbližšímu sudému | 10 | 87 | 476218/1048577 | 0.06492 |

Všechna povodí, celé cykly a další momenty jsou
v [JSON](../results/logistic-fixed.json). Výsledky ukazují, že zvýšení
přesnosti nemusí monotónně prodlužovat periodu ani zlepšovat četnosti.
Směs cyklů s vahami velikostí povodí odpovídá **rovnoměrnému výběru k**;
nejde o rovnoměrný výběr bitových reprezentací plovoucích čísel.

## 4. Plovoucí řádová čárka

[C++ experiment](../experiment_logistic.cpp) má explicitní binary32 a
binary64 mezivýsledky, režim k nejbližšímu se sudou polovinou a zakázané
slučování násobení se sčítáním i přeuspořádání výrazů. Porovnává

```
A: round(round(4*x)*round(1−x)),
B: round(4*round(x−round(x*x))).
```

Deset počátků:0,1/4,1/2,3/4,1,0.1,0.123456789,1/7,
0.3141592653589793,0.625. Jejich **skutečné bity po převodu** jsou uloženy;
zejména zápis0.1 není tvrzením o přesném racionálním počátku1/10.
Celkem40 případů. V každém počítáme prvních65 536 hodnot a hledáme cyklus
Brentovým algoritmem s limitem50 milionů vyhodnocení f.

Vybrané výsledky, mu označuje délku neperiodického začátku:

| formát | výraz | počátek zapsaný desetinně | mu | perioda |
|---|---|---|---:|---:|
| binary32 | A | 0.1 | 1744 | 4344 |
| binary32 | A | 0.123456789 | 1056 | 1 (nula) |
| binary32 | A | 1/7 | 383 | 1 (nula) |
| binary32 | A | 0.3141592653589793 | 468 | 836 |
| binary32 | B | 0.1 | 3143 | 203 |
| binary64 | A | 0.3141592653589793 | 5509878 | 1 (nula) |
| binary64 | B | 0.1 | 15118151 | 9458152 |

V dalších osmi nebanálních binary64 případech byl dosažen limit detektoru.
Netvrdíme jejich periodu, neperiodičnost ani dolní mez periody50 milionů.
Krátký vzorek může mít přesto malou odchylku: binary64/A s počátkem
0.3141592653589793 má v prvních65 536 hodnotách D≈0.00295, ale později
se trvale ustálí na nule. Samotná jednorozměrná histogramová shoda tedy
nestačí ani k dlouhodobému tvrzení o těchto konkrétních trajektoriích.

[Nezávislá validace](../validate_logistic_float.py) počítá zaokrouhlení
pomocí přesných zlomků a dělení celých čísel. Ověřila9185 uložených hran
obou formátů a **celé všech20 binary32 trajektorie**, celkem27 491 stavů,
slovníkem navštívených stavů, nezávisle na Brentově detektoru. Všechny
nalezené binary64 cykly byly přepočteny v Pythonu:30 086 200 kroků,
uzavření, minimálnost periody a začátku i kontrolní hash souhlasí.
Minimálnost periody lambda plyne z neuzavření v lambda/p pro každého
prvočíselného dělitele p. Minimálnost mu>0 plyne z toho, že předchozí
stav není předchůdcem vstupu na cyklu. Pythonové dlouhé binary64 běhy
nejsou tvrzeny jako zlomková kontrola každého kroku; tu mají uložené sondy.

Výsledky: [experiment](../results/logistic-float.jsonl),
[validace](../results/logistic-float-validation.json). Všechny běhy skončily0.

## 5. Primární zdroje, errata a závěr auditu

Von Neumann, *Various Techniques Used in Connection With Random Digits*,
Collected Works5,768–770, je uložen z
[LANL](https://mcnp-green.lanl.gov/pdf_files/InBook_Computing_1961_Neumann_JohnVonNeumannCollectedWorks_VariousTechniquesUsedinConnectionwithRandomDigits.pdf).
Všechny tři stránky vizuálně přečteny. Hlavička uvádí původní NBS Applied
Math. Series3,36–38(1951), shrnutí sepsal George Forsythe. Str.769 potvrzuje
Ulamovu atribuci, zdvojování úhlu i varování před zaokrouhlováním.
Sám historický zdroj má hustotu s chybným faktorem1/(2pi); není to tentýž
faktor jako v C0053. Str.770 podporuje atribuci úlohy23 a parity v metoděF.
Zdroj neslibuje nezávislost logistické posloupnosti.

Galias, *Periodic Orbits of the Logistic Map in Single and Double Precision
Implementations*, IEEE TCS-II68(2021),3471–3475, je uložen z
[autorova webu](https://www.zet.agh.edu.pl/~galias/ps/tcasii2021lpublished.pdf).
Přečten celý text a vizuálně tabulkyII/III na3473–3474. Autor uvádí úplné
soupisy pro přesně stanovený výraz A:10 binary32 a20 binary64 cyklů při
parametru4. Naše periody4344/836 s tabulkou souhlasí. Úplnost jeho obřího
výpočtu samostatně nepotvrzujeme; vlastní úplné soupisy jsou jen §3 výše.
Autorovy poměry povodí počítají všechny reprezentovatelné stavy, což je
jiné rozdělení počátků než rovnoměrná reálná mřížka. Expirace certifikátu
při stažení veřejného autorského PDF je zapsána v metadatech zdroje.

Vrstvy all2-prepre, all2-pre, all2, err2 a aktuální TeX err2 prohledány
pro str.140/588, úlohu24, Ulam/von Neumann/logistic. Žádná oprava24 nebyla
nalezena; změna úlohy25 z17.8.2024 s ní nesouvisí. C0053 je již doložen.
Tento blok nepřidává nález. Výzkumná část24 je uzavřena jako obecná analýza
konečných modelů, úplné malé grafy a reprodukovatelné pokusy vyšší přesnosti.
