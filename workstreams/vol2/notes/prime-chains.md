# §4.5.4-39: prvočíselné řetězce

**Rozsah.** Zadání 415 a odpověď 665–666 byly přečteny v původní sazbě.
Číselné příklady jsou správné. Nový nález **V2-C0181** je bibliografický:
Kellerův článek patří do Math. Comp. **41**, nikoli 40. Úloha požaduje
co nejdelší nalezený řetězec; neformuluje konečné maximum, jehož dosažení
by bylo možné certifikovat. Níže je vlastní konečná konstrukce a přesně
vymezená kontrola historických tvrzení. Tištěný exemplář nebyl prověřen.

## 1. Následník a certifikát prvočíselnosti

Následníkem prvočísla p rozumíme prvočíslo q = 2^k*p+1 pro celé k >= 0.
Pro p = 2 je tedy povolen přechod 2→3 s k = 0. Pro liché p musí být k >= 1,
protože p+1 je sudé a větší než 2. Řetězec je konečná posloupnost takových
přechodů. Nejmenší následník má nejmenší přípustný exponent k.

Známe úplný prvočíselný rozklad q−1: při lichém p jsou to 2 a p.
Použijeme tento **Lucasův certifikát**: číslo a splňující

```
a^(q−1) = 1 mod q,
gcd(a^((q−1)/ell)−1, q) = 1 pro každý prvočíselný dělitel ell čísla q−1.
```

Proč stačí? Pro libovolný prvočíselný dělitel d čísla q má a modulo d
nějaký multiplikativní řád h, tedy nejmenší kladné h s a^h = 1 mod d.
První rovnost dává h | q−1. Druhé podmínky vynucují v h plnou mocninu
každého prvočísla z rozkladu q−1; jinak by h dělilo (q−1)/ell.
Proto h = q−1. Protože h | d−1, platí d >= q a nutně d = q.
Tím je q prvočíslo. Rozklady a certifikáty menších prvočísel kontrolujeme
rekurzivně až k 2, které je počátečním případem.

Je-li q prvočíslo, vhodnou hodnotou a je každý generátor nenulových
zbytků modulo q. Pro liché p tvoří generátory podíl
(1/2)*(1−1/p) >= 1/3. Jejich náhodné hledání tedy vyžaduje v průměru
nejvýše tři pokusy. Ověření jednoho certifikátu potřebuje konstantní
počet modulárních umocnění s O(log q) násobeními. To vysvětluje poznámku
v odpovědi, proč je primalita následníků snadná, když už známe primalitu p.

## 2. Vytištěná čísla a vlastní prodloužení

Vynechané číslo a jeho nejmenší následník jsou

```
P = 9582170887127842377060195852353537,
Q = 2066678528579921308409812579227882652882296135112078218441270655539079806279302783351291332069672615937.
```

P má 34 číslic, začíná 95 a končí 37, takže prostředních 30 vynechaných číslic
souhlasí. P = 2^31*4462046030502692971872257+1 a Q = 2^227*P+1.
Q má přesně 103 číslic. Úplný řetězec od 2 přes všechna vytištěná čísla,
Q a dvě další vlastní hodnoty má 15 vrcholů. Postupné exponenty jsou

```
0, 1, 2, 1, 5, 1, 1, 29, 3, 37, 31, 227, 835, 115.
```

Tento seznam spolu s počátečním p = 2 určuje celý řetězec jednoznačně,
bez opisování posledního 389místného čísla. Hodnoty v plné délce jsou
v `results/prime-chains.json`. Každý ze 14 přechodů má certifikát primality
a pro každé menší k buď vlastní dělitel, nebo bázi, která neprojde silným
testem složenosti. Ověřených vyloučení je 1288. Tím je dokázána minimalita
**všech** zvolených následníků, nejen posledního výslovně uvedeného v knize.

Silný test se zde používá pouze k certifikaci složenosti: pro liché n
rozložíme n−1 = 2^s*d, d liché. Prvočíslo by muselo pro každou bázi a
nesoudělnou s n splňovat a^d = 1, nebo a^(2^j*d) = −1 pro některé
0 <= j < s. Pokud neplatí žádná z možností, je n složené. Případ báze
soudělné s n rovněž nemůže dát takto odmítnuté prvočíslo. Přijatý
pravděpodobně prvočíselný kandidát se za důkaz nepovažuje.

Výpočet byl předem omezen 20 vrcholy, 4096 bity a exponenty menšími 4096.
Za posledním vrcholem se další kandidát v povoleném rozsahu nenašel;
z toho **netvrdíme neexistenci následníka**, ani globální nejdelší řetězec.
Pro tuto neúspěšnou část hledání neukládáme úplnou řadu nezávislých
vyloučení. Závěr je pouze patnáctičlenná certifikovaná konstrukce.

## 3. Fermatova prvočísla a rozsah otázky o existenci

Následník 2 má tvar 2^(k+1)+1. Jestliže k+1 = u*v s lichým u > 1,
pak 2^v+1 je vlastní dělitel (2^v)^u+1. Prvočíselnost proto vyžaduje
k+1 = 2^m. Tato čísla 2^(2^m)+1 se nazývají **Fermatova čísla**;
ta, která jsou prvočísla, jsou přesně následníky 2.

Věta knihy o tom, co se pravděpodobně nikdy nepodaří rozhodovat,
je výhled, nikoli dokázaná nerozhodnutelnost. Samotná existence šestého
Fermatova prvočísla není totéž co existence libovolného následníka 2:
několik jich už známe. Tento rozdíl není nový matematický protipříklad
k některému tvrzenému algoritmu v knize.

Při přechodu k Sierpińského problému odpověď rozšiřuje koeficient p
na libovolné kladné liché celé číslo a. Budeme výslovně zkoumat
složenost všech a*2^k+1. Číslo 78557 = 17*4621 samo není prvočíslo,
takže bez tohoto přirozeného rozšíření by doslovně nemohlo být vrcholem
prvočíselného řetězce. Obsah odpovědi je silnější, netriviální tvrzení
o složenosti všech členů této exponenciální posloupnosti.

## 4. Důkaz, že 78557 a 271129 nemají prvočíselný člen

**Pokrytí exponentů** je konečná rodina podmínek k = r mod d taková,
že každé nezáporné k splní aspoň jednu. Ke každé podmínce přiřadíme
malé prvočíslo ell s 2^d = 1 mod ell a a*2^r+1 = 0 mod ell.
Pak ell dělí a*2^k+1 v celé dané třídě.

Pro a = 78557 fungují následující řádky:

| ell | d | r |
| --- | --- | --- |
| 3 | 2 | 0 |
| 5 | 4 | 1 |
| 7 | 3 | 1 |
| 13 | 12 | 11 |
| 19 | 18 | 15 |
| 37 | 36 | 27 |
| 73 | 9 | 3 |

Sudá k pokryje 3, třídu 1 modulo 4 pokryje 5. Z ostatních k modulo 36
zbývají 3,7,11,15,19,23,27,31,35. Číslo 7 pokryje 7,19,31;
13 pokryje 11,23,35; 19 pokryje 15; 37 pokryje 27; 73 pokryje 3.
To je úplný důkaz pokrytí, nejen konečná zkouška velkého počtu exponentů.

Pro a = 271129:

| ell | d | r |
| --- | --- | --- |
| 3 | 2 | 1 |
| 5 | 4 | 0 |
| 7 | 3 | 2 |
| 13 | 12 | 6 |
| 17 | 8 | 6 |
| 241 | 24 | 10 |

Lichá k pokryje 3, násobky 4 pokryje 5. Zbývají 2,6,10,14,18,22
modulo 24. Číslo 7 pokryje 2,14; 13 pokryje 6,18; 17 pokryje 22
(i 6); a 241 pokryje 10. V obou tabulkách je ell menší než a,
tedy menší než každý a*2^k+1. Jde vždy o **vlastního** dělitele,
což je pro závěr o složenosti podstatné. Primalita 271129 má navíc
rekurzivní Lucasův certifikát.

Důkaz zároveň dává nekonečně mnoho lichých koeficientů bez prvočíselného
členu: nahraďme 78557 číslem 78557 + 140100870*t, t >= 0.
Přírůstek je dvojnásobkem součinu všech sedmi dělitelů. Zachová lichost
i všechny zbytky v první tabulce; vlastní dělitelé zůstanou menší než členy.

## 5. Cunninghamův příklad

Pro A = 554688278430 položme p_k = A*2^k−1. Potom p_(k+1) = 2*p_k+1.
Všech 12 hodnot pro 0 <= k < 12 má přesný certifikát. Další člen
2272003188449279 je dělitelný 19. Původní sazba 666 má skutečně **k < 12**,
nikoli k <= 12; není zde chyba v krajní hodnotě.

## 6. Prameny a errata

- Sierpiński, Elemente der Mathematik 15(1960),73–74: celý dvoustránkový
  článek vizuálně přečten. Původní konstrukce využívá čínskou větu
  o zbytcích a dělitele prvních šesti Fermatových čísel. Na 73 výslovně
  volí koeficient větší než všechny dělitele. Nekonečně mnoho lichých
  řešení lze vybrat z příslušné aritmetické posloupnosti s lichým krokem.
- Jeho corrigendum 17(1962),85 bylo rovněž přečteno v obrazu z GDZ,
  strana souboru 89. Doplňuje podmínku k > P v druhém důkazu na 74,
  kde P je společný lichý násobek krycích prvočísel; tím zajistí vlastní
  dělitele. Náš přímý důkaz výše tuto mezeru nemá. Oprava se týká
  původního článku, ne chybného výsledku o infinitudě v TAOCP.
- Selfridge, AMM 70(1963),101: původní řešení I vizuálně přečteno.
  Soubor uchovaný na stránce R. W. Newcomba obsahuje sousední úlohu 4994
  a str 100–101, nikoli 102; toto omezení zachováváme. Na 101 výslovně
  uvádí 271129 a jeho šest dělitelů. Rok 1962 pro 78557 potvrzuje
  retrospektiva v úvodu Jones–White, INTEGERS 12A(2012),A10 (primární
  výzkumný článek, čten zde přes webový text; lokální PDF nedostupné).
  Nepřisuzujeme původnímu článku Sierpińského výslovné vypsání 271129,
  které na přečtených 73–74 není.
- Keller 1983: vizuálně 661,668–670,673. Na 670 výslovně uvádí 69
  zbývajících koeficientů pod 78557; na 669 popisuje odstranění 30
  dřívějších kandidátů Jaeschkem a dalších 21 svou tabulkou 7.
  Údaj 69 v knize tedy má přímou oporu v původním článku. Neopakovali
  jsme celý tehdejší výpočet pro všechny koeficienty a tisíce exponentů.
  Hlavička 661 i metadata vydavatele v Crossrefu potvrzují svazek 41.
- Jaeschke 1983 a corrigendum 1985: bibliografické údaje ověřeny
  v metadatech vydavatele; plné originály nebyly získány. Údaj 69 je
  ověřen přímo u Kellera a nezávisí na domněnce o obsahu corrigenda.
- Löh 1989,751–759: původní text dostupný přes indexovaný PDF přepis;
  hlavička 751 a tabulky 1–3 na 754–755 obsahují počátek 554688278429
  a délku 12. Lokální PDF/obraz nebyl získán. Číselný příklad byl
  nezávisle prokázán výše; celý historický rekordový průzkum neopakujeme.
- Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální
  `sources/err2.textxt` podle stran 415/665/666, jmen a charakteristických
  čísel. Nenalezena oprava úlohy 39 ani svazku Kellerovy citace.
  Sousední opravy odpovědí 35 a 40 se netýkají 39; úvodní fiktivní
  demonstrace errat na „straně 666“ nejsou opravami této stránky knihy.
  Starší `err2-2e`, str 616, nová odpověď 41 z 10. 9. 1995 již obsahuje
  tutéž chybnou bibliografii; tato starší vrstva byla čtena textově.

## 7. Reprodukce a meze

`verify_prime_chains.py` a `results/prime-chains.json` uchovávají přesné
hodnoty, rozklady, báze a všechna 1288 vyloučení. Návrhy dává SymPy;
validátor nepřebírá jeho verdikt o primalitě. Sám ověřuje úplnost
rozkladů a 41 Lucasových certifikátů explicitním binárním umocňováním,
nezávisle na vestavěném `pow` použitém při hledání. U dělitelů používá
nezávislý průchod desetinnými číslicemi. Pokrytí se kontrolují také
přímo přes společné periody 36 a 24. Čtyřčlenný příklad 5→11→23→47 ověřen.

Běh: limit 240 s, wrapper PID 1313351, child PID 1313352, session 21318,
2026-11-03T22:12:45 až 22:15:21 UTC, exit 0; vlastní program 156.155 s.
Úspěšný běh nebyl opakován. Výzkumné maximum ani nekonečná existence
následníků nebyly dokázány a nejsou součástí tvrzeného pokrytí.
