# Obnova celé §4.2.1–13: nejtěsnější směrované meze

7. listopadu 2026, X0203. Celé zadání228/file240 a odpověď612/file624.
Odpověď obsahuje pouze bibliografický odkaz a vazbu na4.2.2–24;
níže je vlastní úplný algoritmický důkaz, nikoli převzatý nečtený
Yoheho důkaz. Nový numerický běh není potřebný.

## Přesný požadavek a normální pásmo

Nechť S je množina uložitelných normálních čísel třetího vydání,
včetně0. Pro reálný přesný výsledek x definujme
D(x)=max{y∈S:y≤x}, U(x)=min{y∈S:y≥x}, pokud tyto meze existují.
Pak D(x)≤x≤U(x); žádná lepší uložitelná dolní či horní mez není
možná přímo z definice. Knižní „nechceme round“ zde znamená
nechceme volbu nejbližšího bodu; směrované operace jsou stále
zaokrouhlováním v obecném smyslu, nikoli chyba terminologie.

Pro b≥2,p≥1, x≠0 proveďme přesnou normalizaci
x=f b^(e−q), 1/b≤|f|<1. Základní modifikace N5 je

- dolní mez: F=⌊b^p f⌋;
- horní mez: F=⌈b^p f⌉.

Výsledkem je F b^(e−q−p). Podlaha a strop jsou **znaménkové**:
pro záporné x dolní mez zvětšuje velikost, horní ji zmenšuje.
Je-li F=±b^p, přepiš přesně na exponent e+1 a F=±b^(p−1).
Další zaokrouhlování při tomto přepisu není potřebné. Je-li x=0,
obě meze jsou0 s kanonickým exponentem.

V kladném pásmu jsou všechny uložené hodnoty po kroku
Δ=b^(e−q−p). Podlaha i strop (včetně přesného horního přepisu)
jsou sousední hodnoty kolem x. Při x na dolní hranici se obě
rovnají x, takže jemnější soused z nižšího pásma nic nezlepšuje.
Při x nad hranicí leží podlaha již uvnitř tohoto pásma. Záporné
případy plynou z D(−x)=−U(x), U(−x)=−D(x). Tím je dokázána
**globální těsnost přes všechna exponentová pásma**, ne pouze
uvnitř pomocné pevné mřížky.

Je-li přesný výsledek reprezentovatelný, podlaha i strop splývají.
Přesná půlka ani lichost základu zde nevyvolává zvláštní pravidlo;
obě směrované meze jednoznačně určují nerovnosti.

## Každá potřebná změna A a N

A1–A3 nadále prohodí operandy podle exponentů a zarovnají je;
na hodnotě ani znaménku se nic nemění. Nulový operand lze ihned
vrátit přesně. A5/A6 musí dodat přesnou hodnotu nebo dostatečný
zbytek pro rozlišení rovnosti s koncovým bodem. N1 a přesné
normalizační posuny N2–N4 se zachovají; N5 nahradí výše uvedená
podlaha/strop. Teprve konečné meze se posuzují proti rozsahu.

Původní A4 se však **nesmí** ponechat jako prosté vrácení u,
pokud v≠0. Pro d=e_u−e_v≥p+2 již uzavřený důkaz X0193
ukazuje |v| menší než polovinu vzdálenosti u od kteréhokoli
souseda. Proto přesný součet leží striktně mezi u a jeho sousedem
ve směru znaménka v. Úplná náhrada zkratky je:

| Malý operand | Dolní mez součtu | Horní mez součtu |
|---|---|---|
| v>0 | u | succ(u) |
| v<0 | pred(u) | u |
| v=0 | u | u |

To platí i při opačných znaménkách a na hranici exponentového
pásma. Nulové u se zpracuje před touto zkratkou, takže se zde
nevyžaduje nejmenší kladný soused0 v modelu s neomezeným exponentem.

Pro kladné u=(e,F), b^(p−1)≤F≤b^p−1, je succ buď(e,F+1),
nebo při maximálním F dvojice(e+1,b^(p−1)). Pred je buď(e,F−1),
nebo při minimálním F dvojice(e−1,b^p−1). Záporní sousedé se
získají negací a výměnou pred/succ. Konečné krajní exponenty
upravují tyto předpisy podle následujícího oddílu.

Příklad b10,p8,q50: u=(50,.10000000), v=(40,.10000000).
Součet je .10000000001; dolní mez u, horní .10000001. Při −v
je přesný součet .09999999999; dolní soused je .099999999
s exponentem49, horní je u. Prosté odečtení kroku horního pásma
by dalo .09999999, což je sice dolní mez, ale není nejtěsnější.
Všechny vstupy jsou normalizované a d=10=p+2.

Když d≤p+1, zarovnaný konečný součet lze uchovat přesně v
nejvýše2p+1 zlomkových cifrách, s odděleným přenosem před čárkou.
Případné katastrofické zrušení a levé posuny proto nezahodí nic.
Spolu s náhradou A4 je to konkrétní konečný algoritmus pro všechny
d, nikoli požadavek na nekonečný registr. Odčítání používá stejné
kroky s negovaným druhým operandem.

## Násobení, dělení a potřebná informace o zbytku

M1 a přesné exponentové vzorce M2 zůstávají; při nenulovém
jmenovateli určí tentýž matematický podíl, při nulovém součiniteli
přesnou nulu. Součin dvou p-ciferných zlomků má nejvýše2p cifer.
Uchováme jej přesně, normalizujeme jako v M a použijeme směrované
N5. To zahrnuje případný levý posun i přepis výsledného ±1.

Při dělení není třeba vytvářet nekonečný rozvoj. Po určení
normalizovaného exponentu rozložme přesný kladný škálovaný
zlomek na b^p|f|=Q+R/D, kde Q celé, D>0 a0≤R<D. Q a R
získá konečné celočíselné dělení odpovídajících koeficientů.
Je-li R=0, oba směry vracejí znaménkový Q. Je-li R>0:

| Znaménko | Dolní koeficient | Horní koeficient |
|---|---|---|
| kladné | Q | Q+1 |
| záporné | −Q−1 | −Q |

Pro volbu směru tedy stačí **nenulovost** přesného zbytku;
porovnání s polovinou není potřebné. U p2 desítkového1/3 je
Q33,R/D=1/3, tedy meze .33 a .34. Podíl nulou nemá definovaný
přesný reálný výsledek, a není tedy případ této úlohy o dvou mezích.

Počet zahozených cifer není sám důkazem, že výsledek je nepřesný:
jsou-li všechny0, obě meze musí splývat. Naopak zahození poslední
nenulové cifry bez informace o zbytku může vydávat vnitřní bod
za vnější mez. To platí pro zarovnání, posun po přenosu i dělení.
Při použití již odvozené softwarové FDIV větve je Q normalizovaný,
a proto stačí test X≠0 podle X0197; interpretovat X jako přesné
desetinné cifry by bylo nesprávné.

Toto je modifikace abstraktních A/N/M. Pro skutečný Program A
nestačí vyměnit několik skoků N5: musí také zachovat zbytek při
dlouhém SRAX a opravit N4 z C0251. Již doložená oprava
X←1+b·[old X≠0] před SRC1 zachová potřebnou nenulovost při
přenosu. Zkrácení registru nesmí vymazat ani poslední nenulový
konec. Zde nepředstíráme, že původní strojový kód už implementuje
směrovanou aritmetiku, ani nezavádíme další nález stejné chyby.

## Konečný rozsah, nula a postupné podtečení

Nechť e_min≤e≤e_max a povoleny jsou jen normální hodnoty plus0.
Nejmenší kladná je ν=b^(e_min−q−1), největší
M=(1−b^−p)b^(e_max−q). Pro0<x<ν je nejtěsnější dvojice(0,ν),
pro−ν<x<0 dvojice(−ν,0). Obě hranice ±ν samy jsou přesné.
Nahradit nenulový podtečený výsledek nulou v obou směrech by
jednu z požadovaných nerovností porušilo.

Je-li x>M, existuje dolní mez M, ale neexistuje konečná horní
mez v této reprezentaci. Pro x<−M je tomu naopak: horní−M
existuje, dolní konečná chybí. Je třeba výslovně ohlásit chybějící
mez; teprve rozšíření reprezentace o ±∞ ji může doplnit.
Samotné saturování obou směrů na M či−M není intervalovým řešením.
Při x=±M jsou obě meze právě x. Zabalení exponentu modulo b
rovněž není platnou náhradou za chybějící vnější mez.

Povolíme-li i postupné podtečení s mřížkou
h_min=b^(e_min−q−p), použijeme v malé oblasti podlahu/strop
x/h_min. Tím se automaticky zahrne0 i nejmenší nenulové hodnoty;
přechod na normální pásmo má stejný krok a je souvislý.
Toto je výslovně jiná množina S, nikoli nevyřčená vlastnost
původního normálního formátu.

## Volitelné skutečné intervalové operandy

Pro intervaly [a,b],[c,d] jsou nejmenší uložitelná uzavření:
součet [D(a+c),U(b+d)] a rozdíl [D(a−d),U(b−c)]. Monotonicita
součtu a rozdílu dává jejich přesné reálné krajní body.
U součinu vezmeme minimum čtyř přesných součinů koncových bodů
pro D a maximum pro U; bilinearita umisťuje extrema do rohů.
U podílu, je-li0∉[c,d], totéž platí pro čtyři přesné podíly:
pro pevný jmenovatel je závislost na čitateli lineární a pro
pevný čitatel je na každé znaménkové větvi jmenovatele monotónní.
Nejprve zaokrouhlený reciproký interval a potom násobení může
zvětšit obal, takže se zde nepoužívá jako důkaz nejtěsnosti.
Jmenovatel obsahující0 vyžaduje další politiku nedefinovanosti
či nesouvislého/neomezeného výsledku; konečné meze obecně nejsou.
To přesahuje samotné dvě směrované bodové operace zadání.

## Bibliografie a přesný stav odkazu

Nově nalezený [archiv sympozia](https://www.acsel-lab.com/arithmetic/arith2/arith2.html)
potvrzuje titul J. M. Yohe, *Roundings in Floating-Point Arithmetic*
a číslo IEEE Transactions on Computers z června1973. Odkazuje
na [desetistránkový sken](https://www.acsel-lab.com/arithmetic/arith2/papers/ARITH2_Yohe.pdf),
který webová služba identifikovala jako PDF. Přímé stažení však
vrátilo403 (www) a406 (alternativní host/http); screenshot služba
předala pouze textový zástupný popis, nikoli čitelný obraz.
**Samotný článek nebyl získán do pracovního prostoru ani přečten.**
Dřívější technická zpráva DTIC AD0713699 zůstává nedostupná.

Údaje577–586 odpovídají tištěnému odkazu a již přečtené bibliografii
Kahan–Palmer1979. Yoheho vlastní algoritmy, jejich optimálnost a
každý externí důkaz výslovně vynecháváme. Výše uvedený důkaz
je samostatný a pokrývá celé matematické zadání13. Vazba na4.2.2–24
zůstává samostatně k budoucímu průchodu; není automaticky uzavřena.
Všechny čtyři vrstvy errat a TeX nemají opravu této úlohy.
Další jsou celé15–18 a historie225–227; dopředný418 je držen.
