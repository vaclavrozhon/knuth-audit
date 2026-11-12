# Historické odkazy k mocnění a sčítacím řetězcům

Blok V2-X0075; strany 461–462, 466, 477–478. Navazuje na matematické
důkazy v předchozích blocích. Dva nové bibliografické nálezy jsou C0232
a C0233. Jejich pravdivost nezávisí na níže přiznaných mezerách ve
čtení ostatních historických pramenů.

## 1. Datta–Singh: první díl, nikoli druhý (C0232)

Na straně 461 je ve skutečném obrazu knihy vytištěn tučný svazek **2**,
rok 1935 a strana 76. Pravidlo připisované Pingalovi je však v dílu **I**,
strana 76; pokračuje na straně 77. V kombinovaném vydání z roku 1962
jde v nově získaném knihovním PDF o souborové strany 97–98.
Strana 76 dílu II, souborová strana 367, pojednává o rovnicích vyšších
stupňů. Všechny tři stránky byly přečteny vizuálně.

Tiráž na souborové straně 3 výslovně uvádí první vydání dílu I roku
1935, dílu II roku 1938 a společné vydání roku 1962. Oprava tedy je
**2 → 1**; rok 1935 se nemění. Nejde o jiný nalezený svazek se shodnou
stranou, ale o shodu konkrétního algoritmu a příkladů 2^6 a 2^7.

Pravidlo rozkládá exponent opakovaným půlením sudého čísla a odečtením
jedničky od lichého čísla. Obráceným průchodem se provádějí čtverce
a zdvojení. Datta–Singh odkazují na sutry VIII.28–31 vydání z roku
1840; toto sanskrtské vydání jsme přímo nečetli.

Srovnání s Plofkerovou, *Mathematics in India* (2009), strany 55–56,
potvrzuje interpretaci algoritmu. Datování je tam podáno opatrně.
Knuthovo známé erratum z 21. září 2004 mění datování na dobu před
rokem 400 n. l., název spisu a následující časový odstup; číslo dílu
neopravuje. Starší erratum z 13. dubna 1990 opravuje Bombay na Lahore.
Datování původního sanskrtského textu zde samostatně nerozhodujeme.

Nový knihovní sken je jiný než archivní sken dříve použitý při auditu
největšího společného dělitele. Mají různý počet úvodních stran;
jejich souborová čísla stránek se nesmějí zaměnit.

## 2. Saidan: vydání 1978, nikoli 1975 (C0233)

Strany **198 i 461** uvádějí u knihy *The Arithmetic of al-Uqlidisi*
rok 1975. Obě místa byla zkontrolována v obrazu TAOCP.
[Vydavatel](https://link.springer.com/book/10.1007/978-94-009-9772-1)
uvádí první pevnou vazbu z 31. března 1978. Volně dostupná tiráž
vydavatele má copyright 1978 a výslovně označuje původní první vydání
rokem 1978. Její obraz byl přečten; změna pozdějšího digitálního data
vydání s tímto závěrem nemá nic společného. Oprava je **1975 → 1978**
na obou místech.

Samotné strany 341–342 byly přečteny pouze v otevřeném webovém
přepisu na Scribdu. Lokálně stažené HTML neposkytuje použitelný text
těchto stran; uchován je proto výřez z webového čtení s přesným URL.
Nevydáváme jej za obrazovou kontrolu těchto dvou stran.

Příklad skutečně pracuje s 51 políčky: z 51 postupuje přes 26, 13, 7
ke 4. Hodnota v poli j je 2^(j−1), takže posloupnost výpočtu je
8, 64, 4096, 16777216, 33554432, 1125899906842624; závěrečné zdvojení
a odečtení jedničky dává součet 2^51−1. Knuthova stručná zmínka
o ilustraci pro n=51 je tím podpořena, i když samotné 51. políčko
obsahuje 2^50. Z tohoto rozdílu indexování netvoříme další nález.

## 3. al-Biruni a al-Káší

Sachauův překlad *The Chronology of Ancient Nations* (1879),
strany 132, 134–136, byl přečten textově i vizuálně. Strana 133 je
kalendářová tabulka, nikoli součást algoritmu. Strany 134–135
skutečně počítají šachovnicový součet pomocí opakovaných čtverců:
2, 4, 16, 256, 65536, 4294967296, 18446744073709551616.
Odečtení jedničky dává 2^64−1. Citované stránky a rok odpovídají.
Obecné tvrzení o velkém historickém vlivu nebylo samostatně doloženo
studiem recepce díla.

Ruský překlad *Klíče k aritmetice* v *Istoriko-matematicheskie
issledovaniia* 7 (1954), strany 256–257, byl přečten vizuálně.
Pravidlo 16 rozkládá exponent na mocniny dvojky, vytváří příslušné
opakované čtverce a násobí je. Příklady jsou 5^8=390625 a
3^14=3^8·3^4·3^2=4782969. To podporuje Knuthovo připsání binárního
postupu al-Kášímu; moderní pseudokód A je jeho ekvivalentní organizace,
nikoli doslovný přepis historické tabulky.

Předmluva překladatele, strana 11, datuje dokončení spisu do března
1427. Byla přečtena textově i vizuálně; jde o souborovou stranu 9.
U stran 256–257 je souborové číslo o jeden menší, nikoli o dva.
Arabské rukopisy jsme nečetli. Ruský DjVu nemá použitelnou OCR vrstvu.

## 4. Dellac, de Jonquières a Goulard

V původním ročníku *L'Intermédiaire des mathématiciens* 1 (1894)
byly vizuálně přečteny strany 20, 162–164 a 234. Dellacova otázka 49
na straně 20 se ptá na nejmenší počet násobení pro mocninu. Redakční
poznámka správně rozlišuje možnost dělení mocnin od příbuzné
geometrické úlohy. De Jonquièresova odpověď na stranách 162–164
obsahuje tabulku všech prvočísel menších než 200.

Porovnání této historické tabulky s již dokončenými přesnými minimy
do 199 je samostatná nová kontrola dat, nikoli opakování prohledávání
řetězců. Chybné položky jsou 107, 149, 163, 179 a 199; každá je
nadhodnocena o jedničku. Knuthův první tisk opomíná 199, ale to již
opravuje erratum z 2. prosince 2005. Nový nález zde není.

De Jonquières na straně 163 nepřípustně omezuje obecný řetězec na
hvězdový: každý nový člen má používat bezprostředně předchozí člen.
Knuth na chyby tohoto staršího řešení upozorňuje. Goulardova otázka
393 na straně 234 skutečně navrhuje, že přidání faktoru 2 vždy
zvýší minimální délku o jeden. Odpověď de Jonquièresa v ročníku 2
(1895), strany 125–126, dosud nebyla získána; tato konkrétní
bibliografická návaznost zůstává otevřená.

## 5. Scholz a Thurberův případ n=32

Scholzova původní otázka 253, *Jahresbericht der Deutschen
Mathematiker-Vereinigung* 47, Abteilung II (1937), strany 41–42,
byla přečtena v obou obrazech GDZ. Je podepsána Arnoldem Scholzem
v Kielu, přijata 29. června 1937 a používá název Additionskette.
Původní tisk má v bodě (3) zřejmě chybu: l(2^(m+1)−1) ≤ m+l(m).
Již m=4 by vyžadovalo l(31)≤6, ačkoli l(31)=7. Brauerův původní
článek z roku 1939 na straně 736 při citaci Scholze uvádí zamýšlenou
opravu m+l(m+1). Knuthovo připsání standardní domněnky Scholzovi
je tedy v pořádku. Tiskovou chybu starého pramene nepočítáme jako
chybu TAOCP.

Thurberův článek v *Discrete Mathematics* 16 (1976), 279–289, byl
přečten ve všech šesti skenech (jedenáct tištěných stran). Následuje
úplná rekonstrukce krátké argumentace pro 32 ze strany 285.
Značíme l(a) nejmenší délku sčítacího řetězce pro a, λ(a)=floor(log2 a)
a ν(a) počet jedniček v binárním zápisu. Malý krok je krok řetězce,
v němž se λ nezvětší. Řetězec délky r končící v a má r−λ(a) malých
kroků. Používáme Thurberův výsledek z roku 1973: ν(a)≥9 vyžaduje
alespoň čtyři malé kroky. Jeho úplná klasifikace zůstává externím
vstupem, jak je podrobně uvedeno v bloku o třech malých krocích.

Položme R=2^32−1 a uvažujme poslední součet R=a+b. Nemůže v něm
nastat binární přenos: nejnižší vzniklý přenos by na své pozici
zanechal nulu, ačkoli R má samé jedničky. Proto ν(a)+ν(b)=32,
a alespoň jeden sčítanec má nejméně 16 jedniček. Prefix k němu má
alespoň čtyři malé kroky. Zároveň max(a,b)≥2^31, takže poslední
krok do R již λ nezvýší a přidá pátý malý krok. Dostáváme
l(R)≥31+5=36. Horní mez 36 dává věta G použitá na pětikrokový
řetězec 1,2,4,8,16,32; důkaz G je v předchozím uzavřeném bloku.
Tedy l(2^32−1)=36, jak kniha uvádí.

Thurberova věta 2 na straně 288 uvádí rovnost pro prvních 18 kladných
exponentů a dále 20,24,32. Jeho případ n=15 obsahuje delší rozbor
s odkazy na článek z roku 1973; ten zde nepovažujeme za novou
nezávislou klasifikaci. Aktuální Scholzův kontext a velký Cliftův
protipříklad k rovnosti jsou již uzavřeny v X0073.

## 6. Meze tohoto checkpointu

Chace (1927), strany 1,3–4, byl přečten v textovém výstupu webového
PDF. Opakované zdvojování i výběr sčítaných řádků jsou doloženy,
například součinem 19·6=114. Datování Rhindovy předlohy je tam
1849–1801 př. n. l.; samo nestačí k doložení hranice 2000 př. n. l.
Struveho (1930) bibliografické údaje a dostupnost devítistránkové
předmluvy jsou ověřeny na webu Ústavu orientálních rukopisů.
Její obsah dosud nebyl přečten: lokální stažení vrací HTTP403
a screenshoty webového nástroje nevrátily obraz. Tutéž technickou
mezeru má vizuální čtení Chace. Dohledávání těchto pramenů
a původu názvu ruského násobení ještě pokračuje. Žádnou chybu nevyvozujeme pouze z nedostupnosti pramene.
Zbývá především původní odpověď z roku 1895 a konkrétní dobové
svědectví o rozšíření metody v Rusku. Celý blok X0075 proto zatím
zůstává partial; uzavřené nálezy C0232/C0233 jsou doloženy samostatně.

Nové porovnání 46 položek prošlo jednou: PID 1588642, exit 0,
0.001186156 s výpočtu, 0.058469599 s včetně obalu, limit 120 s.
Úspěšné dřívější hledání minim nebylo opakováno.

Ve všech šesti vrstvách autorových errat nebyla nalezena oprava
čísla dílu Datta–Singh ani roku Saidanova překladu. Nový fyzický
dotisk a prvenství oznámení nebyly ověřeny. Oba reporty jsou lokální
návrhy a nebyly odeslány.
