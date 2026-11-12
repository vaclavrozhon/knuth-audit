# §4.5.1: motivace, historické odkazy a uzavření oddílu

Audit 2. listopadu 2026. Text na str. 330–333 i odpovědi na
str. 638–640 přečteny v původní sazbě. Všechny matematické
odstavce a 16 úloh jsou pokryty poznámkami rational-basic,
rational-slash, rational-linked a rational-experiments.
Tato poznámka doplňuje bibliografické podklady a přesné hranice
historické kontroly. Celý obsah každého citovaného článku není
součástí auditu knihy a není zde prohlašován za prověřený.

## Motivace a doporučené kontroly

Úvod §4.5 správně odlišuje přesnou hodnotu racionálního výrazu
od zaokrouhleného desetinného výstupu. Tvrzení o neexistenci
zaokrouhlovací chyby se vztahuje k přesným vstupním zlomkům
a přesně provedeným operacím; nedodává přesnost fyzikálně měřeným
vstupům. Pozdější text sám vyžaduje kontroly přetečení.

Doporučená kontrola pomocí inverzí Cauchyho matic byla skutečně
provedena v úloze 10 na pěti Hilbertových maticích; viz
[rational-linked.md](rational-linked.md). Příklady číselných těles
s odmocninami jsou obecně odůvodněny v rational-basic.
Odhad přibližně 61 % nesoudělných náhodných jmenovatelů je
odkaz na limitní model věty 4.5.2D; jeho důkaz bude prověřen tam.
Nejde o tvrzení o libovolné nerovnoměrné distribuci vstupů.

## Henrici 1956 a Matula 1972

Primární archiv JACM potvrzuje Henriciho článek v ročníku 3,
čísle 1, na str. 6–9 z ledna 1956. Dobové zprávy NBS z roku
1955 jej uvádějí nejprve jako rukopis a potom jako přijatý článek.
To potvrzuje identitu citace a čas přípravy, nikoli absolutní
prvenství před všemi možnými technickými zprávami. Úplný původní
článek nebyl přečten; historické prvenství zůstává neověřeno.
[JACM 1956](https://projects.csail.mit.edu/jacm/jacm56.html),
[zpráva NBS, červenec–září 1955](https://www.govinfo.gov/content/pkg/GOVPUB-C13-11a70bdce32ea205577c2ecab5be35bc/pdf/GOVPUB-C13-11a70bdce32ea205577c2ecab5be35bc.pdf).

Vydavatelský záznam Matulovy kapitoly z roku 1972 potvrzuje
rozsah 479–489 a popis konečně přesné racionální aritmetiky
s nenásilným pokračováním při překročení přesného rozsahu.
Knuthův odkaz na 486–489 je dílčí rozsah uvnitř této kapitoly,
nikoli nesprávně uvedené počáteční stránky. Konkrétní strany
486–489 nebyly z originálu získány; neprohlašujeme jejich přesný
obsah ani prvenství pojmů za ověřené.
[Vydavatelský záznam a souhrn](https://www.sciencedirect.com/science/article/pii/B9780127759500500236).

## Následné práce Matuly a Kornerupa

Autorský seznam publikací potvrzuje údaje všech následných citací
na str. 332: dvě práce z roku 1978, článek z LNCS 72 (1979),
Computing Supplement 2 (1980) a IEEE články z let 1983, 1985
a 1990. U roku 1978 jde skutečně o dvě práce na str. 29–38
a 39–47; to odpovídá známému erratu z 6. července 2006.
Konferenční archiv potvrzuje oba samostatné názvy a autorství.
Přímé stažení jeho PDF vrátilo HTTP 403. Webový nástroj sice
identifikoval PDF, ale neposkytl zde viditelné snímky, takže
obsah těchto dvou originálů **není označen za přečtený**.
[Autorský seznam](https://s2.smu.edu/~matula/publications.html),
[ARITH 4](https://www.acsel-lab.com/arithmetic/arith4/arith4.html).

Z vydavatelského repozitáře Aarhuské univerzity byl získán
primární preprint *Finite Precision Rational Arithmetic:
Slash Number Systems*, DAIMI PB-166, říjen 1983, předcházející
časopisecké práci z roku 1985. PDF má 28 dvoustranových listů.
V originálu přečteny titulní a abstraktové strany, tištěné
strany 1–5 a 48–50, tedy listy 1–4 a 27–28 souboru.
Definice konečných zlomkových formátů, jejich mediánové
zaokrouhlování přes řetězové zlomky a motivace knihy souhlasí.
Závěr výslovně rozebírá velké mezery u jednoduchých zlomků
a návrh jejich zaplňování dalšími kódy. To podporuje nutnost
rozlišovat neškálovaný základní formát knihy a jeho další varianty.
Tabulku 6 na str. 48 jsme vizuálně přečetli, její numerické
konstanty však samostatně nereprodukovali.
[Primární preprint](https://tidsskrift.dk/daimipb/article/view/7440).

Primární dvoustranová poznámka autorů z Aarhusu, datovaná
22. července 1988, byla přečtena celá. Popisuje výhody pro
úlohy s jednoduchými racionálními výsledky a současně rozlišuje
problém rozsahu a problém přesnosti. Třetí list uloženého PDF
obsahuje příklad determinantu z práce z roku 1979. Jeho vstupní
matice a hodnota 5/13 byly přečteny v sazbě a přesně ověřeny
v intervalovém experimentu. Plný článek z roku 1979 a všechny
řádky jeho tabulky nepovažujeme za auditované. Poznámka se tedy
používá jako primární doklad stanoviska autorů a zdroj konkrétního
příkladu, nikoli jako důkaz univerzální převahy slash aritmetiky.
[Poznámka autorů a přiložený příklad](https://www.arithmazium.org/classroom/lib/Matula_Kornerup_Rationally_Biased_Rounding_Can_Be_Beneficial_B.pdf).

U článků z let 1980, 1983 a 1990 je ověřena bibliografie a
relevance z uvedených primárních/autorských podkladů. Jejich
úplné konstrukce aritmetických jednotek a časové analýzy nebyly
znovu dokazovány; kniha je zde pouze uvádí jako další literaturu.
Rozdíl mezi preprintem z roku 1983 a časopiseckým rokem 1985
není chybou citace.

## Vrstvy errat a konečný stav

Ve všech čtyřech vrstvách all2-prepre/all2-pre/all2/err2 byly
zahrnuty tyto související změny:

- 11. června 2005: doplnění Hofstadterova výroku za úvod §4.5.
- 9. října 2024: oprava roku knihy *Metamagical Themas* na 1985.
  Jde o známé erratum; primární původ výroku v Hofstadterově
  textu nebyl nově auditován.
- 6. července 2006: rozdělení společného rozsahu 29–47 na dvě
  samostatné bibliografické položky 29–38 a 39–47.
- 15. ledna 2002: doplnění odkazu na §4.5.3-39 k porovnávání
  zlomků v odpovědi 1; základní křížové porovnání je správné.
- 1. ledna 2020: obnovení prvních dvou řádků úlohy §4.5.3-43
  vynechaných pouze v dotiscích 2019. Definice zaokrouhlení
  v §4.5.1 se touto změnou nemění; související úloha bude
  prověřena ve svém oddílu.

Oddíl je dokončen ve vymezeném rozsahu: původní text, všech
16 úloh, odpovědi a relevantní změny errat. Nové potvrzené nálezy
jsou C0113, C0115 a C0116; C0114 zůstává interpretační kandidát.
Údaje o posledním fyzickém dotisku a prioritě nálezů zůstávají
neověřené. Nic nebylo odesláno. Metadata zdrojů a přesný rozsah
čtení jsou v `sources/rational-context-manifest.json`.
