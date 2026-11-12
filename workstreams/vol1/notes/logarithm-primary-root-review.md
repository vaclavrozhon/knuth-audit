# §1.2.2–28: Meggitt, Chen a METAFONT

V1-X0734, 2. listopadu 2026. Čtyři konkrétní odkazy v odpovědi
na s. 471 jsou checked v níže uvedeném rozsahu. Celá úloha 28
zatím zůstává partial pro další historické prameny. Matematické
důkazy a testy X0030 se neopakovaly. Nový nález není.

## Meggitt 1962: přímý trigonometrický algoritmus

Získán je celý původní článek *Pseudo Division and Pseudo
Multiplication Processes*, IBM Journal of Research and Development
6 (April 1962), 210–226, z veřejného archivu
<https://archived.hpcalc.org/laporte/Meggitt_62.pdf>.
Titul, ročník, stránkování a datum byly přímo ověřeny v obrazech.
Datum přijetí 29. srpna 1961 není rok vydání.

Rozhodující jsou s. 216–217 a 223–224. Označme i imaginární
jednotku, x,y reálné souřadnice a q_j nezáporné počty provedených
kroků. Násobení x+iy faktorem 1−i·10^(−j) dává současné změny

```text
x_new = x + 10^(-j)y,
y_new = y - 10^(-j)x.
```

Použijí se staré hodnoty na pravých stranách. Každý krok odečte
úhel arctan(10^(−j)). Volbou q_j podle zbytku se souřadnice y
blíží nule a původní úhel je součtem tabulkových úhlů. Přepsání
pomocí z=10^j y vede na posuny a sčítání/odečítání; článek
výslovně připouští jiný základ než deset. To je konkrétní
trigonometrická obdoba požadovaná Knuthovou poznámkou.

Na s. 223–224 je opačný postup: rozklad zadaného úhlu p na
tabulkové úhly a násobení faktory 1+i·10^(−j), s opačným
pořadím zpracování číslic. Poměr výsledných souřadnic dává
tan p pro 0<=p<pi/2. Tím není tvrzen nezávislý audit všech
tabulek, chybových mezí či krajních případů původního článku.
Root přímo obrazově četl 210, 216–217, 223–224, 226; další
orientační četba textu není vydávána za kontrolu celé sazby.

## Meggitt 1963: související polynomiální metoda

Celý původní článek *Digit-by-Digit Methods for Polynomials*,
IBM 7 (July 1963), 237–245, byl získán z veřejného zrcadla
Bitsavers na mirrorservice.org; přesná URL je v retrievals-03.json.
Root přímo četl obrazy 237–238 a 245 a text dalších částí.

Pro polynom f stupně n definuje autor koeficienty A_r(x_0)
vztahem f(x)=sum_(r=0)^n A_r(x_0)(x−x_0)^r. Posun počátku
o a mění koeficienty podle rovnice (5) na s. 238:

```text
A_s(x_0+a) = sum_(r=s)^n C(r,s) a^(r-s) A_r(x_0),
```

kde C je binomický koeficient. Volba a jako mocniny základu
dává síť sčítání a posunů. Článek se zabývá polynomy,
jejich kořeny a interpolací; nepřipisujeme mu samostatný
konkrétní algoritmus pro sinus. Závěr na s. 245 však výslovně
rozšiřuje použití na hladké funkce aproximované polynomy
v jednotlivých oblastech. Jde o související rozšíření metody
z roku 1962. Samotný odlišný název tedy neodůvodňuje hlášení
chybné citace; přímý trigonometrický příklad dodává první článek.
Datum přijetí 2. listopadu 1962 je od vydání 1963 odlišeno.

## Chen 1972: invarianty pro logaritmus a exponenciálu

Celý původní článek *Automatic Computation of Exponentials,
Logarithms, Ratios and Square Roots*, IBM 16 (July 1972),
380–388, pochází ze stejného veřejného zrcadla. Root přímo
četl obrazy 380, 382–383 a 388, text úvodu 380–381 a další
vybrané pasáže. Konkrétní vztah k úloze dokládají již 382–383.

Invariant je veličina, která se při iteraci nemění. Pro
exponenciálu je jím y·exp(x), s krokem x_new=x−ln a,
y_new=ya. Pro logaritmus je jím y+ln x, s krokem x_new=ax,
y_new=y−ln a. Volí se a=1+2^(−m), takže násobení tímto
faktorem je posun a součet. Index m se volí podle nejvyššího
nenulového bitu zbytku. Tyto vztahy přímo objasňují příbuznost
s knižními algoritmy L a E; nejde o totožný program.

Chen dokončuje výpočet lineární Taylorovou aproximací při
malém zbytku. Ta může obsahovat ještě násobení se zkrácenou
přesností. Celému programu proto nepřipisujeme výhradně posuny
a sčítání. Statistické počty iterací a úplná analýza zaokrouhlení
nebyly samostatně revidovány. Datum přijetí 17. listopadu 1971
se nezaměňuje s rokem 1972.

## METAFONT: autorův průběžně opravovaný zdroj

Autorova stránka <https://www-cs.stanford.edu/~knuth/abcde.html>
přímo potvrzuje titul, rok 1986 a skutečnost, že svazek D
obsahuje zdrojový program. Současně odkazuje na úplné zdroje
`systems/knuth/dist/mf/mf.web` jako na aktuální znění se všemi
opravami. Uložený soubor z CTAN je verze 2.71828182, leden 2021.
Jeho hlavička výslovně váže verzi 1 z 4. ledna 1986 ke svazku D.
Nejde o získaný sken prvního tisku z roku 1986 a úplná kolace
tohoto tisku nebyla provedena.

Root přečetl příslušný zdroj a pomocí WEAVE ověřil přesné
číslování oddílů 120–147. Oddíly 129–136 obsahují logaritmus
a exponenciálu s tabulkou hodnot blízkých
2^27 ln(1/(1−2^(−k))); §132 výslovně odkazuje na TAOCP
1.2.2–25. Oddíly 137–147 používají tabulku úhlů
arctan(2^(−k)), redukci do oktantů, otočení vektoru a opačný
postup pro sinus a kosinus. Jsou tedy přímým obsahovým dokladem
citované rodiny algoritmů v autorově opraveném znění téhož díla.
Pomocná normalizace využívá další aritmetické rutiny; ani zde
netvrdíme, že celý kód používá pouze posuny a součty.

WEAVE zde jen zpracoval literární zdroj a jeho číslování.
Nejde o spuštění numerických algoritmů ani o důkaz jejich
všech chybových mezí. Obecná obsahová citace je ověřena;
shoda každého bitu s vydáním 1986 se tím netvrdí.

## Kniha a errata

Knižní obrazy 26, 470–471 byly přečteny. Všechny čtyři
vrstvy errat byly znovu prohledány podle stran i jmen;
výpis je uložen v results/logarithm-primary-errata.json.
Na s. 471 je známá typografická oprava názvu METAFONT
z 13. srpna 1997. Opravy algoritmů na s. 470 z let 2001,
2002 a 2011 patří do již přijatého matematického auditu.
Žádná nalezená oprava nemění posuzované pramenné souvislosti.
Feynman, Linsky a širší dějiny logaritmů mají oddělenou evidenci.
