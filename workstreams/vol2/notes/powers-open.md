# §4.6.3-42/43: Cliftovy příklady a Scholzova otázka

Stav 2026-11-04: obě úlohy auditovány včetně náhrady z roku 2005 a
změn z roku 2024. Obecná Scholzova nerovnost zde není vyřešena.
Konkrétní řetězce, jejich nemožná podtržení a dvě velké konstrukce
jsou nezávisle ověřeny. Úplnost Cliftova soupisu optimálních řetězců
a jeho velké tabulky minim jsou výslovné externí výpočetní vstupy,
nikoli výpočty zopakované tímto auditem. Nový nález žádný.

## 1. Tři různé otázky

Sčítací řetězec je rostoucí posloupnost od 1, v níž každý další člen
vzniká součtem dvou předchozích. Délka je počet sčítání a l(n) její
minimum pro cílové číslo n. V **označeném řetězci** podtrhneme některé
členy tak, aby každé sčítání používalo poslední již podtržený člen.
Nejmenší délku takového řetězce označujeme l^0(n). Hvězdový řetězec
používá vždy bezprostředně předchozí člen a jeho minimum je l*(n).
Tedy l(n)<=l^0(n)<=l*(n). Definice v knize a úplný důkaz transformace
G jsou rozebrány v [powers-scholz.md, §1–2](powers-scholz.md#1-označené-řetězce-a-cíl-transformace).

Původní úloha 42 na straně 485 kladla tři otázky:

```text
l(2^n-1) <= n-1+l(n)?              Scholzova nerovnost,
l(2^n-1)  = n-1+l(n)?              její univerzální rovnost,
l(n) = l^0(n)?                    existence optimálního označení.
```

Třetí otázka má od roku 2005 zápornou odpověď. První zůstává obecně
otevřená; druhá dostala v roce 2024 zápornou odpověď. Žádný z těchto
záporných výsledků nevyvrací první nerovnost. Aktualizace 2005 proto
mění úlohu 42 na konkrétní řetězec a přesouvá zbývající otázky do nové
43. Aktualizace 2024 z úlohy 43 vypouští otázku na rovnost.

## 2. Úloha 42: překážka podtržení a řetězec délky 28

Vezměme přesně řetězec délky 27 z nového zadání; celý je uložen jako
`printed` v `results/powers-open.json`. Jeho rozhodující začátek je

```text
1,2,4,8,16,32,64,65,97,128,256,353,...
```

Člen 65 lze vytvořit jen jako 64+1. Předchozí zdvojování už vynutila
podtržený člen větší než 1; proto musí být při tvorbě 65 posledním
podtrženým členem 64. Následující 97 lze vytvořit jen jako 65+32.
Jelikož 64 už je podtrženo, nemůže být posledním podtrženým členem 32;
musíme podtrhnout 65. Jenže 128 vzniká výhradně jako 64+64. To je
s podtrženým 65 neslučitelné. Přesně zde podmínka selže.

Duál znamená obrácení všech hran redukovaného grafu výpočtu; redukce
sloučí mezivýpočty použité pouze jednou. Přesná konstrukce, cena
grafu a její vztah k řetězcům jsou v
[powers-graphs.md](powers-graphs.md). Pro tento řetězec má každý člen
jediný pár operandů, takže volba grafu není nejednoznačná. Obrácený
graf se rozvine například do řetězce se začátkem

```text
1,2,4,...,16384,16385,16401,32768,65536,81937,98322,...
```

Při 16385=16384+1 musí být podtrženo 16384. Při
16401=16385+16 musí následovat podtržení 16385. Ale 32768 vzniká
jen jako 16384+16384 a podmínka nyní selže. Odpověď v erratech má
správně 128 a 32768. Úplný duální řetězec i oba grafy jsou ve výsledku.

Horní mez l^0(5784689)<=28 lze doložit velmi jednoduše: do vytištěného
řetězce vložme 33=32+1 a podtrhněme všechny členy kromě 33,65,97.
Nyní lze 97 počítat jako 64+33, a 65 tudíž nemusí být podtrženo.
Výpočet 128=64+64 už není blokován. Všechny pozdější kroky používají
svého bezprostředního předchůdce; potřebná starší 65 a 97 zůstávají
k dispozici. Tím je označený řetězec délky 28 dokázán přímo.

## 3. Co přesně říká soupis optimálních řetězců

[Cliftův vlastní přehled](https://additionchains.com/ScholzBrauer.html)
uvádí všech 16 optimálních řetězců pro 5784689. Každý z uvedených
řetězců má 27 kroků. Nezávisle jsme ověřili všechna sčítání a všechny
možné páry operandů; v těchto konkrétních řetězcích je vždy jen jedna
volba. Redukcí dostaneme právě dva různé grafy, které jsou navzájem
duální. Každý graf je reprezentován osmi z uvedených řetězců.

Polovina řetězců má výše uvedenou překážku u 128, druhá polovina
u 32768. Nemožnost označení je navíc strojově doložena dvěma odlišnými
modely. První uchovává množinu všech možných posledních podtržených
členů po každém kroku. Druhý zavádí pro každý člen pravdivostní
proměnnou „podtržen“ a přímo vyžaduje, aby poslední takový předchozí
člen byl jedním ze sčítanců. Řešič Z3 rozhoduje splnitelnost těchto
konečných logických podmínek. Oba modely souhlasí pro všech 16
záporných příkladů i pro výše uvedený kladný řetězec délky 28.

Závěr l(5784689)=27 a l^0(5784689)=28 používá jako externí vstup,
že Cliftův soupis je úplný a že neexistuje obecný řetězec kratší než
27. Vlastní validace 16 řetězců by sama úplnost nedokazovala.
Cliftův článek *Calculating optimal addition chains*, Computing 91
(2011), §13 na straně 282, výslovně popisuje výpočet dokazující
l^0(n)=l(n) pro všechna menší n.

Navíc jsme stáhli začátky obou autorských binárních tabulek
`add30.bits.gz` a `addl030.bits.gz` a porovnali všech 5 784 689 položek
od n=1. První a jediný rozdíl v tomto intervalu je právě 27 proti 28
u posledního čísla. Data používají dva bity na rozdíl

```text
l(n)-floor(lg n)-ceil(lg nu(n)),
```

respektive stejný rozdíl pro l^0; nu(n) je počet jedniček binárního
zápisu. Čtyři položky jsou v jednom bajtu, nejnižší dvojice bitů patří
nejmenšímu n. Shoda s dříve ověřeným začátkem obecné tabulky zajišťuje
konzistentní dekódování. Toto porovnání je kontrola publikovaných dat,
nikoli druhý nezávislý výpočet minim.

Archiv obsahuje pouze první 1 MiB každého komprimovaného souboru,
ne celé gzip soubory. Z nich se podařilo rozbalit dostatečně dlouhé
začátky; ukládá se přesně 1 446 173 rozbalených bajtů. Starší obecný
komprimovaný začátek byl znovu použit a serveru byl vyžádán jen zbytek.
Rozsahy HTTP, kontrolní součty a neúplnost gzip jsou v manifestu.

## 4. Přesný protipříklad k rovnosti při n=1541527

Označme R(t)=2^t-1. [Aktuální Cliftova konstrukce](https://additionchains.com/ExactScholz2.html)
dává řetězec pro R(1541527) délky 1541551. Jeho publikovaná tabulka
minim dává l(1541527)=26; zkontrolovali jsme odpovídající položku
v samostatně stažených datech. Proto

```text
l(R(1541527)) <= 1541551 < 1541527-1+26 = 1541552.           (O1)
```

Délka na levé straně není prohlášena za přesné minimum. Pro vyvrácení
univerzální rovnosti stačí tato horní mez. Naopak hodnota 26 pro
malý exponent je zde externí výpočetní výsledek; nereprodukujeme
úplné vyloučení všech řetězců délky 25 pro 1541527.

### 4.1 Krátký popis konstrukce a jejího počtu

Výchozí řetězec pro R(47) má 54 kroků. V následujícím zápisu znamená
`a,...,b` všechna postupná zdvojení od a do b včetně obou krajů:

```text
1,2,3,6,...,24,30,...,480,483,963,...,7704,8187,8189,
8*R(11),...,2^13*R(11),16777213,R(24),
4*R(23),...,2^24*R(23),R(47).
```

Každé první číslo nového úseku je součtem dřívějších hodnot; celkem
je 55 členů, tedy 54 sčítání. Zůstávají dostupné zejména 8*R(11),
4*R(23), R(24) a R(47). Následuje vlastní rozpis autorovy konstrukce,
který zároveň dokládá konečný počet bez milionového seznamu.

Z identity R(2t)=2^t R(t)+R(t) získáme R(2t) z R(t) pomocí t
zdvojení a jednoho součtu. Sedm takových etap vede z 47 do
u=47*128=6016; po dosažení R(u) máme

```text
54+(u-47)+7 = u+14 = 6030 kroků.
```

Nyní vytvořme 2^14 R(u) a přidejme již dostupné 8 R(11). Platí

```text
2^14 R(u)+8 R(11) = 8 R(u+11).
```

Tento výsledek zdvojme u-3krát a přidejme R(u). Dostaneme R(2u+11).
Celá tato etapa stojí 14+1+(u-3)+1=u+13 kroků; celková délka je
(2u+11)+16. Šest běžných etap R(t)->R(2t) vede do
v=(2u+11)*64=770752 a délky v+22.

Nakonec použijeme druhý uchovaný stavební člen:

```text
2^25 R(v)+4 R(23) = 4 R(v+23).
```

Po v-2 zdvojeních a přičtení R(v) dostaneme R(2v+23)=R(1541527).
Poslední etapa stojí 25+1+(v-2)+1=v+25 kroků. Celková délka je
2v+47=(2v+23)+24=1541551, jak požaduje (O1).

### 4.2 Proč je výchozí řetězec zajímavý

V něm dostupné délky bloků jedniček zahrnují 11,24,47, ačkoli žádný
sčítací řetězec délky 8 nemůže obsahovat všechna tři čísla. Tento
malý pomocný problém jsme úplně prohledali: 2061 stavů, žádný řetězec
s osmi kroky. Kratší řetězec by šel na osm kroků doplnit vložením
nejmenšího chybějícího čísla jako (k-1)+1, a také je tedy vyloučen.
Devět kroků stačí, například

```text
1,2,4,8,10,11,12,23,24,47.
```

To vysvětluje výhodu přenosů ve velkém řetězci. Samotná tato malá
překážka ještě není důkazem (O1); ten používá konstrukci §4.1 a externí
minimum 26. Autorův původní protipříklad měl exponent 30978119,
následoval 9307543 a teprve potom 1541527. Poslední číslo není zde
prohlášeno za nejmenší možný protipříklad: autor říká, že je to
nejmenší, které zatím našel.

## 5. Scholzova nerovnost pro první neoznačené optimum

První číslo bez optimálního označení samo není protipříkladem ke
Scholzově nerovnosti. [Cliftův přehled oprav](https://additionchains.com/Repair.html)
obsahuje řetězec pro R(5784689) délky 5784715, tedy přesně
5784689-1+27. Jeho první tabulka byla ověřena celá a nezávisle.

Nový prvek oproti transformaci označených řetězců je vidět už na
začátku. Z obvyklých zdvojování a spojování bloků vytvoříme R(128)
a uchováme 2^64 R(64). Následují dvě jednotlivá sčítání:

```text
U = R(128)+2^64 R(64),
U+1 = 2^64 R(65).
```

Dále

```text
2^64 R(65)+2^32 R(32) = 2^32 R(97).
```

Po zdvojení na 2^128 R(97) můžeme vytvořit R(225), potom R(353)
a pokračovat podle tabulky. Dvě pozdější vložení obdobně využívají
uchované posunuté R(65) a R(97). Všech 29 úseků tabulky má ověřený
první součet, počet zdvojení, koncový člen i průběžný součet délek;
nejde jen o kontrolu poslední algebraické identity.

Zde je přesný princip takového komprimovaného certifikátu. Pro úsek
s,2s,...,2^d s stačí doložit, že s je součtem dvou dříve dostupných
členů a že konec je přesně 2^d s. Všechny vnitřní kroky jsou pak
indukcí platná zdvojení a úsek přidá d+1 členů. Pro první úsek
začínající 1 se odečte počáteční člen od počtu operací. V obou
kontrolovaných konstrukcích používají pozdější první součty pouze
uložené krajní hodnoty předchozích úseků; ověřujeme to přímo hledáním
páru v jejich množině. Dále kontrolujeme přísný růst mezi úseky.
Celý rozvinutý řetězec je tedy platný a má přesně uvedenou délku.

Implementace pracuje s přesnými celými čísly, nikoli s plovoucími
logaritmy nebo náhodnými zbytky. Pro protipříklad §4 stačilo 53
uložených různých krajních hodnot, pro tuto konstrukci 54. Poslední
číslo má v druhém případě 5 784 689 bitů. Nemusíme ukládat miliony
jeho předchůdců ani znovu testovat každé jednotlivé zdvojení.

## 6. Současná formulace a publikované výpočetní rozsahy

Původní kniha na straně 478 uvádí rovnost pro n<=24 a n=32.
Cliftův článek z roku 2011, §13, přímo potvrzuje rozšíření do n<=64.
Jeho vlastní poznámka z roku 2024 na straně 2 uvádí další rozšíření
na všechny exponenty s l(n)<=9. To zahrnuje n<=126; neznamená to,
že množina těchto exponentů končí právě 126. Aktuální errata na
straně 478 správně uvádějí podmínku l(n)<=9 a zároveň (O1).

Tyto rozsahy jsou publikované výpočetní výsledky. Tento blok
neopakoval všechny úplné výpočty pro čísla R(n) a neauditoval celý
pruningový algoritmus článku 2011 nebo všech 15 stran článku
Thurber–Clift 2021. Pro současné tvrzení o rovnosti máme primární
vyjádření samotného autora výpočtu z roku 2024; metadata citace
2021 souhlasí s vydavatelem, plný text tohoto článku zde není doložen.

Pro n, u něhož l(n)=l^0(n), již vlastní důkaz věty G dává Scholzovu
nerovnost. Publikovaný první rozdíl 5784689 tedy zajišťuje celý menší
interval. Konstrukce §5 řeší i toto hraniční číslo, další konkrétní
případy jsou v autorově přehledu. Ani existence prvního rozdílu mezi
l a l^0, ani selhání univerzální rovnosti nedává obecný důkaz či
protipříklad k samotné Scholzově nerovnosti. Úloha 43 je auditována
jako výzkumná otázka, nikoli označena za vyřešenou.

## 7. Kontroly, opravy vlastního validátoru a prameny

Čtyři dokončené bloky v `results/powers-open.json`:

| Blok | Přesný rozsah | Čas |
|---|---|---:|
| chains | 16 řetězců, 16 voleb operací, dva grafy, DP a Z3, konstrukce délky 28 | 0.215017490 s |
| tables | všech 5 784 689 dvojic publikovaných minim, samostatná hodnota l(1541527) | 0.233708132 s |
| constructions | 31+29 komprimovaných úseků, cíle s 1 541 527 a 5 784 689 bity | 0.209757357 s |
| seed | úplné vyloučení osmi kroků obsahujících 11,24,47; 2061 stavů | 0.003770067 s |

Úspěšný obalový běh trval 2.453989150 s, session 99067,
PID 1583220/1583224/1583228/1583230, limit 300 s na blok, vše exit 0.
Úspěšné bloky nebyly opakovány. Před nimi došlo ke dvěma vlastním
chybám, jejichž logy a samostatná metadata zůstávají uloženy:

- Parser HTML odstranil zalomení oddělující řetězce; žádná matematická
  kontrola ještě neproběhla. Opraveno zachováním textových uzlů.
- Při porovnání grafu s jeho duálem validátor neoprávněně požadoval
  stejné pořadí nezávislých vrcholů. Po obrácení hran je třeba vrcholy
  znovu uspořádat podle různých číselných popisků. Oprava se týká
  reprezentace grafu, nikoli Knuthova matematického tvrzení.

Primární zdroje a jejich skutečný rozsah čtení:

- Clift, [Computing 91 (2011), 265–284](https://doi.org/10.1007/s00607-010-0118-8):
  PDF a text uloženy, strany 265 a 282–283 přečteny vizuálně i textově;
  celý algoritmus v ostatních stranách není tímto prohlášen za auditovaný.
- Clift, [A Short Note on Exact Equality for the Scholz-Brauer Conjecture](https://additionchains.com/ExactScholzBrauer.pdf):
  všech pět stran textově; strany 1,2,4,5 také vizuálně. PDF ještě
  používá exponent 9307543. Pozdější autorská HTML tabulka používá
  menší 1541527, shodné s erraty 2024.
- Autorské stránky `ScholzBrauer.html`, `ExactScholz.html`,
  `ExactScholz1.html`, `ExactScholz2.html`: relevantní texty a tabulky
  přečteny; nezávislá velká aritmetická validace se týká ExactScholz2.
- `Repair.html`: úvod a tabulka pro první číslo, které není Hansenovo,
  přečteny a ověřeny. Zářijový dodatek 2026 a ostatní tabulky jsou
  archivovány, ale nejsou všechny nezávisle auditovány. Nové obecné
  výsledky z pouhého textu tohoto dodatku nepřebíráme.
- `Calculating.html`: staženo jako navigace k původnímu algoritmu;
  odkazovaný zdrojový kód nebyl v tomto bloku spouštěn.

Zkontrolovány všechny šestery vrstvy errat a původní sazba nových
úloh na PDF stranách 28 a 44 souboru all2-prepre a straně 9 souboru
all2. Relevantní změny: 2005-09-17 nový příklad a rozdělení úloh,
2009/2011 rozšíření konečných rozsahů, 2024-09-24 protipříklad rovnosti,
oprava historického „remains in doubt“ a odkaz na autorův web.
Vše se eviduje jako známé aktualizace, nikoli nové nálezy.
