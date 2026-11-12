# Obnova §4.2.1 D, 225–227: historie po jednotlivých tvrzeních

Kontrola 7. listopadu 2026. Originální strany 225–227 (soubor 237–239)
znovu vizuálně přečteny. Starší `single-precision-context.md` neuzavírá
všechna historická tvrzení: jeho slovo „uzavřen“ označovalo jen tehdejší
cílenou kontrolu. Zde jsou zdroje a mezery rozděleny jednotlivě.
Nevznikl nový nález ani nový matematický výpočet.

## Starověk a raná novověká notace

Následující tvrzení zůstávají **bibliograficky neověřená**. Nejde o
protipříklady a nevydáváme odkaz v auditované knize za nezávislý důkaz.

| Tvrzení na 225 | Přesná mezera |
| --- | --- |
| Babylonská aritmetika kolem 1800 př. n. l. nebo dříve | Nezískán datovaný původní doklad ani příslušné stránky Neugebauera. |
| Rozsáhlé užití základu 60 | Nebyl proveden soupis tabulek či výpočtů. |
| Chybějící zápis exponentu a jeho určení kontextem | Neověřeno na příslušných původních tabulkách. |
| Dochovaný chybný součet kvůli posunu řádů | Neugebauer 1952, 26–27 nebyl získán; konkrétní výpočet nebyl reprodukován. |
| Vzácnost takových chyb | Vyžadovala by rozsah prozkoumaného korpusu; ten nemáme. |
| Apollonios, 3. století př. n. l., oddělování mocnin 10 | Příslušný text Pappa nebyl získán. |
| Jeho opatrně formulované prvenství | Nedoloženo srovnáním starších pramenů. |
| Pappova sbírka a její datování do 4. století | Příslušné vydání nebylo čteno. |
| Dlouhá mezera v užití pro součin a podíl | Neuzavřen obecný historický negativní výrok. |
| Logaritmy přibližně 1600 | Primární text s datováním zde nebyl čten. |
| Oughtred, logaritmické pravítko, 1630 | Návrh, publikace a prvenství nebyly samostatně doloženy. |
| Zavádění zápisu x^n v té době | Primární typografické doklady nebyly získány. |
| Dřívější zvláštní symboly pro druhou a třetí mocninu | Původní příklady nebyly získány. |

Samotná algebra oddělování řádu je správná:
`(a·10^r)(c·10^s)=(ac)·10^(r+s)` a pro `c≠0`
`(a·10^r)/(c·10^s)=(a/c)·10^(r−s)`. Plyne z pravidel mocnin
pro celočíselné exponenty, včetně záporných, a dokazuje užitečnost
popisované notace. **Nedokazuje její historické autorství ani prvenství.**

## Torres, Zuse, Stibitz a první hardware

Torresův vlastní text je dostupný v reprintu *limbo* 17 (2003),
9–31. Nově znovu přečteny titulní strana 9 a §VI na 24, lokální
soubor `sources/torres-ensayos-1914.pdf`, strany souboru 1 a 16.
Na 24 skutečně navrhuje pevný počet významných desítkových cifer,
oddělený exponent a použití v aritmometru. Příklady se shodují:
`.243527·10^4=2435.27` a `.341862·10^(−5)=.00000341862`.
To uzavírá obsah návrhu a oba příklady. Reprint sám zde nedokládá
Madrid, přesný rok původního zveřejnění 1914 ani nezávislost na jiných
návrzích. Tyto tři historické složky zůstávají omezené.

[Primární reprint](https://dialnet.unirioja.es/descarga/articulo/2976250.pdf)
není faksimile původního vydání 1913/1914. Jeho úvodní matematické
meze pro exponenty ani jiná tvrzení o obecné automatice se nepřebírají
jako důkaz zde auditovaného oddílu.

Zuseho archivní metadata dříve doložila patentový záznam 1936;
nedostupný původní PDF (429) nebyl přečten. Proto jednotlivě zůstává
otevřen Berlín a rok příslušného návrhu, binární plovoucí reprezentace,
termín „semi-logarithmic“, pravidla pro nekonečno, pravidla pro
neurčenou hodnotu i nezávislost návrhu. Stejně neuzavřen je Stibitzův
návrh, New Jersey a rok 1939. Matematický důkaz implicitního bitu
v úloze 3 není důkaz Zuseho historické priority.

Pro Bell Model V a Harvard Mark II chybí primární dokumenty potřebné
k nezávislému uzavření jednotlivých údajů: plovoucí hardware, reléová
realizace, návrh roku 1944 a prvenství v USA. Obě zařízení mají vlastní
záznam v mapě; prvenství je další samostatný záznam. Randell 1973,
100, 155, 163–164, 259–260; sborník Harvard 1947, 41–68 a 69–79;
*Datamation* duben/květen 1967 a ZAMP 1 (1950), 345–346 nebyly
v tomto auditu obsahově získány. Nejsou označeny jako přečtené.

## Zpráva Burkse, Goldstina a von Neumanna

Nově znovu přečteny strany reprintu 92, 96–97 a 115–117
(soubor 1, 5, 6, 24–26). Titulní poznámka připisuje text autorům,
zprávě z roku 1946 a *Collected Works* 5, 34–79 (1963).
Čísla stran reprintu nesmějí být zaměněna za čísla citovaná knihou.
[Primární reprint](https://www.cs.princeton.edu/courses/archive/fall10/cos375/Burks.pdf).

V §5.3 na 97 se skutečně posuzuje plovoucí čárka. Autoři označují
přípravu měřítek za malou část přípravy programu, exponenty za náklad
paměti a víceslovnou přesnost za obtížnější. §6.6.7 na 116 výslovně
uvažuje softwarovou alternativu a zavádí levý/pravý posun pro její
zrychlení. Tabulka na 117 obsahuje obě instrukce (násobení/dělení 2).
Tím jsou doloženy tyto konkrétní postoje, nikoli jejich nadčasová
platnost pro libovolný stroj.

Naproti tomu tento čtený rozsah sám nedokládá celou chronologii
Moore School 1944–1946, srovnání elektronek s relé, tvrzení, že
škálování vedlo programátory k lepšímu povědomí o přesnosti, ani
absolutní nemožnost vybavit tehdejší návrh oběma druhy hardwaru.
Označení prvního stroje s uloženým programem a druhého elektronického
stroje vyžaduje navíc přesné historické vymezení; zůstává otevřené.
GE a údajné první spojení obou aritmetik nebyly nezávisle doloženy:
citovaný sborník 1951, 65–69 nebyl získán. Rozpor se netvrdí.

## Rané podprogramy a každá bibliografická položka

První vydání Wilkes–Wheeler–Gill 1951, 35–37 a 105–117 nebylo
získáno. Vyhledávání v tomto bloku našlo pouze odlišné druhé vydání
1957, katalogové údaje a sekundární bibliografie. Nepoužíváme jejich
stránkování jako náhradu. Jednotlivě zůstává neověřeno autorství
a obsah A1–A11, publikační prvenství, použití desetinného exponentu
na binárním stroji, téměř stejná cena škálování a posunu i konkrétní
zjednodušení převodů vstupu/výstupu.

Podmíněný matematický mezikrok však platí: má-li hodnota tvar
`10^e f`, změna exponentu o jednotku při zachování hodnoty vyžaduje
změnu f o faktor 10 nebo 1/10. Binární radix ukládání f tuto rovnost
nemění. Cena na EDSAC ani úplné I/O rutiny z rovnosti neplynou.
Tvrzení o převažujícím vydávání v technických memorandech nemá zde
bibliometrický doklad; není uzavřeno jako kvantifikovaný přehled.

Všechny následující položky mají v mapě vlastní omezený záznam:

| Položka na 226 | Rozsah skutečné kontroly |
| --- | --- |
| Stark–MacMillan, Math. Comp. 5 (1951), 86–92 | Původní článek nebyl získán; ani tvrzení o propojovacím panelu neuzavírá bibliografický záznam. AMS index byl nástrojem nedostupný. |
| McCracken 1957, 121–131 | Obsah těchto stran nečten. |
| Carr, CACM 2,5 (1959), 10–15 | Obsah nečten. |
| Wadey, JACM 7 (1960), 129–139 | Obsah nečten. |
| Knuth, JACM 8 (1961), 119–128 | Obsah nečten. |
| Kesner, CACM 5 (1962), 269–271 | Obsah nečten. |
| Brooks–Iverson 1963, 184–199 | Obsah těchto stran nečten. |
| Campbell v Buchholz 1962, 92–121 | Obsah nečten; hledisko konstruktéra není nezávisle ověřeno. |
| Padegs, IBM Systems J. 7 (1968), 22–29 | Obsah nečten; hledisko konstruktéra není nezávisle ověřeno. |

Samotný bibliografický výčet zde netvrdí správnost všech algoritmů
v těchto pracích. Ta nebyla auditem provenience ani čtením titulu
prokázána. Odkaz na další literaturu v §4.2.2 se posoudí v daném
oddílu, nevydává se za předem uzavřený seznam.

## IEEE a závěrečná věta o MMIX

Coonenova vlastní disertace, §1.1, znovu přečtena na 1.2–1.4
(původní soubor 10–12; lokální výřez 1–3). Svědectví účastníka
dokládá ustavení pracovní skupiny na podzim 1977, návrhy 1978,
další vývoj v letech 1980–1981 a návrh 10.0 u IEEE Standards Board
v době psaní. Tento zdroj není sčítáním výrobců na konci osmdesátých
let. Kahan–Palmer 1979 již má samostatně vymezené čtení v X0200.
[Coonenův primární text](https://www.arithmazium.org/library/lib/jerome_coonen_phd_thesis.pdf).

U Goldberga byl znovu otevřen pouze autorizovaný **upravený reprint**
u Oracle, úvod a údaj o původu. Úvod přímo popisuje rychlé přijímání
standardu komerčními výrobci. Neurčuje přesný podíl výrobců, přesný
začátek pozdních osmdesátých let ani samostatně nedokazuje hodnotící
slovo „revolutionary“. [Goldbergův reprint](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).
Neúspěšný starý odhad PDF zůstává neúspěšným odkazem; tento HTML
reprint jej nepřeměňuje na získané původní PDF.

Jednotlivé citace IEEE Micro 4 (1984), 86–100; Cody 1983,
133–139; Kahan, West-83 Paper 16/1; a Cody–Coonen TOMS 19 (1993),
443–451 nebyly obsahově získány a jsou vynechány. U Goldberga nebyla
z původního vydání ověřena zvláštní strana 413. Ověření reprintu se
na tuto stranu nerozšiřuje.

Věta na 227 je dobové ohlášení budoucí náhrady MIX počítačem MMIX
a jeho zamýšlené shody se standardem. Jako tvrzení o tehdejším záměru
je přímo doložena vlastní knihou. Není to současný termín vydání ani
důkaz úplné shody jakékoli konkrétní implementace MMIX; ty se zde
neověřují.

## Errata a návaznost

Převzata přesně vymezená úplná kontrola všech čtyř vrstev errat a
aktuálního TeXu pro 214–228/611–613, doložená souborem
`sources/single-precision-errata-excerpts.txt`. V tomto úseku je
relevantní známá oprava 15. listopadu 2023: místo vydání WWG na
226 mění Reading na Cambridge. Zůstává **known erratum**, nikoli
nový nález. TeXové úpravy mezer či rejstříku se nevydávají za
matematickou chybu.

Celý hlavní text 214–228 i všech 19 úloh §4.2.1 nyní mají individuální
posouzení. Výzkumná 17, význam zaokrouhlení/divize v 7, průměrná
cena 19, přesná relace FCMP a zde označené historické mezery zůstávají
otevřené. Další práce: §4.2.2 od 229/241, nejprve všechny rovnosti,
nerovnosti a konkrétní mezikroky; dopředný kurzor 418 zůstává držen.
