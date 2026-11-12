# Dancing Links: symetrie, sekundární položky a pořadí

Rozsah: úlohy 15–21, hlavní text str. 70–72, zadání 125–126 a odpovědi
419. Originální stránky byly zobrazeny; kód není odvozen pouze z OCR.
Žádný nový potvrzený nález. Oprava odpovědi 20 je již v oficiálních erratech
z 5. ledna 2026 a má samostatnou kartu E023.

## Langfordova involuce, úloha 15

Položení čísla i na pozice j a j+i+1 se zrcadlením změní na položení
s první pozicí j′=2n−i−j. Označme h=n−[n sudé]. Pak j+j′ je n pro
liché n a n+1 pro sudé n, tedy vždy liché číslo. Přesně jedna z obou
pozic splňuje j≤n/2. Zrcadlení nemá pevné řešení, protože už poloha
čísla h by musela mít celočíselné j=(2n−h)/2. Vynechání příslušných
možností proto vybírá přesně jedno řešení z každé dvojice.

Pro alternativní pravidlo i=1 platí j+j′=2n−1; právě jedna první pozice
je menší než n. Počet odstraněných možností je n−1, zatímco první
pravidlo odstraní floor(n/2). Platí i pro malé případy bez řešení.
Celkově má (16) součet (2n−i−1), tedy 3n(n−1)/2 možností.

Exact cover pokryje každé číslo právě jednou a každou pozici právě jednou;
to je bijekce s Langfordovými uspořádáními. Všech devět možností (17)
a obě zrcadlové posloupnosti na str. 70 odpovídají této konstrukci.

[check_langford_dlx.py](check_langford_dlx.py) ověřil **30 úplných množin
modelů pro n=1..10**: bez omezení a s každým ze dvou omezení. Nezávislý
oracle pokládá čísla od největšího a nepoužívá exact cover. Každý model
prošel přímou kontrolou vzdáleností. Pro n=11/12 dávají obě varianty
17 792 / 108 144 zástupců. Náklady prvního/druhého pravidla jsou:

| n | Doporučené pravidlo | Omezení čísla 1 | Úspora doporučeného |
|---|---:|---:|---:|
| 11 | 47 954 679 | 54 095 791 | 11,35 % |
| 12 | 310 006 467 | 346 551 975 | 10,55 % |

Úplné n16 porovnání skončilo 1. listopadu v18:14:40UTC. Obě varianty
daly326721800řešení. Doporučené pravidlo potřebovalo1123272951633memů,
omezení čísla1 potřebovalo1219554377149memů: úspora je **7,895 %**.
Spolu s11,35 % a10,55 % pro n11/12 to podporuje neformální „asi10 %“
v odpovědi15. Výkonové tvrzení není interpretováno jako univerzální
přesná procentní mez pro každé n. Úloha15 je nyní v úplném registru reviewed.

`check_langford_dlx_large.py` ověřil terminální metadata, hashe obou
vstupů a logů, shodu s generátorem a celé profily uzlů bez opakování výčtu.
Výsledek je v `results/langford_dlx/large-comparison.json`.
Samostatné účtování hlavního textu na70 zůstává rozlišeno: naměřených
1.123272951633T je o0,5953 % méně než knižních1.13T;3438.01memů na řešení
není přesná reprodukce vytištěných3460. Nejde o potvrzenou chybu, protože
knižní nízkoúrovňová varianta může účtovat přístupy jinak. Tato mezera
zůstává u hlavní strany70, nikoli u již dokončeného obsahu samotné úlohy15.

## Dámy a slack, úlohy 16–17; str. 71

Rovnosti pro řádky a sloupce zajišťují jednu dámu na každém řádku a sloupci.
Podmínky i+j=s a i−j=d jsou přesně obě rodiny diagonál. Součet na diagonále
je nanejvýš jedna právě tehdy, když jej doplní jednoznačně určený bit
slacku na jedna. Každá rodina má 2n−1 diagonál, tedy dohromady n²+4n−2
binárních proměnných. Všechny položky a možnosti v (23)–(24) souhlasí
s těmito vzorci.

U sekundárních položek se pouze nevyžaduje dosažení součtu jedna. Jejich
pokrytí stále odstraní každou možnost, která se s vybranou možností
překrývá. Větvení na primární položce zajistí, že se žádná přípustná
volba neztratí. Jakmile jsou primární položky pokryty, nemůže zbýt další
zvolená možnost obsahující primární položku. To dokazuje zobecnění
algoritmu X a jeho podmínku z posledních odstavců str. 71.

Nezávislé permutace, množinový exact cover a doslovný spacerový X dávají
právě umístění **2413 a 3142**. S doplňkovými možnostmi jsou v obou
případech slacky a2,a5,a8,b−3,b0,b3. Souhlasí všechny vytištěné možnosti
v obou odpovědích.

Úloha 16 neurčuje pořadí primárních položek. Při pořadí začínajícím
a2,a8,b−3,b3 jsou tyto položky skutečně prvními čtyřmi větveními **na všech
větvích** a mají nanejvýš dvě možnosti. Při pořadí r1..r4,c1..c4,a2..a8,
b−3..b3 je první cesta a2,a3,a4,a8. Tato závislost je v hlavním textu
na str. 72 výslovně popsána; rozdíl není nový nález.

Pro předepsané pořadí úlohy 17 byla porovnána celá seřazená stopa X3,
včetně dvou neúspěšných větví, proti nezávislé množinové rekurzi. Souhlasí
všechny vytištěné vynucené možnosti. Na poslední úspěšné větvi se poslední
možnost r4c2 vybírá přes položku c2, která předchází r4; odpověď zde tvrdí
jen pořadí vybraných možností, nikoli že se větví na r4.

## Sekundární možnosti a druhá smrt, úlohy 18–19

S a,b,c,d primárními má příklad (6) přesně řešení {ce,adf,bg} a {bcf,adg}.
S pouze a,b primárními a požadavkem zasáhnout každou čistě sekundární
možnost zbývá jen {adg,bcf}, jak uvádí zadání.

Po pokrytí všech primárních položek je každá dosud slučitelná možnost
čistě sekundární: možnost obsahující primární položku už byla buď vybrána,
nebo odstraněna spolu s pokrytím této položky. Neprázdná čistě sekundární
možnost zůstává slučitelná právě tehdy, když se nachází alespoň v jednom
neprázdném seznamu aktivní sekundární položky. Jejich délky jsou tudíž
všechny nulové právě tehdy, když je každá taková možnost zasažena již
vybranými možnostmi. To je přesně test v odpovědi 19.

Spacerový algoritmus byl rozšířen pouze rozdělením původních hlaviček
na dva kruhy a dodatečným testem v X2. Operace cover/uncover zůstávají
beze změny. [check_dlx_secondary.py](check_dlx_secondary.py) ověřil
**4 929 vstupů** proti přímému výčtu podmnožin: všechny multimnožiny
nejvýše tří neprázdných možností na nejvýše čtyřech položkách při každém
počtu primárních položek a 300 dalších přeuspořádaných vstupů. Zahrnuty
jsou nulové počty primárních položek, prázdná rodina možností i duplicity.
Prošlo 4 671 testů přijetí a 11 675 úplných obnov paměti.

Pokud by někdo připustil i **prázdnou možnost**, musí se vstup okamžitě
zamítnout: prázdnou množinu nelze zasáhnout. Samotný test LEN ji nevidí.
Kniha však prázdné možnosti v používaném vstupním modelu vylučuje;
výslovná formulace „options can’t be empty“ je v odpovědi 39(a) na str. 423
a odpovídá spacerové reprezentaci. Tento okraj jsme zaznamenali, nikoli
označili za chybu v rámci uvedené konvence.

## Párové pořadí, úloha 20 a známé E023

V jednoduchém (25) se α_j a β_k překrývají právě když k<j. Zbývá
binom(m+1,2) dvojic; délky všech α dávají sum(j+1)=binom(m+1,2),
délky všech β dávají 2m. Všechny čtyři řádky (25) a (26) souhlasí.

Pro účinnější kódování označme g(r)=r & −r. Položka y_r patří do A_j
právě pro r≤j<min(m,r+g(r)) a do B_k právě pro r−g(r)≤k<r.
Společná položka tedy vždy implikuje j>k.

Je-li j>k, nechť d je nejvyšší bit, v němž se čísla liší. V čísle j je
jednička a v k nula, takže d=floor(lg(j & ~k)). Položme r=j & −2^d.
Vyšší bity j,k jsou shodné a g(r)=2^d. Dostaneme
r≤j<r+2^d a r−2^d≤k<r; dále 1≤r≤j<m. Položka y_r je tedy společná.
To dokazuje ekvivalenci bez omezení m na mocniny dvou.

Smyčka t←t&(t−1) vymazává nejnižší jedničku. Pro kladné t=j vybírá
přesně počátky příslušných intervalů A. Pro t=−1−j, v dvojkovém doplňku,
postupně vybírá konce intervalů B; podmínka t>−m vyřadí indexy r≥m.
V šířce w=ceil(lg m) připadá každý bit j právě buď A, nebo B, takže
|A_j|+|B_j|≤w. Při m=2^w nastává rovnost. Každé y_r se v každé rodině
objeví nejvýše g(r)krát.

Tiskovaný svědek používá floor(lg(j−k)), což obecně nestačí. Například
m=7,j=6,k=3 má A6={6,4}, B3={4}. Tisk dává y6, správný společný prvek
je y4. Oficiální erratum z **5. 1. 2026**, poslední řádek odpovědi 20 na
str. 419, mění právě tento exponent. E023 je známá oprava, ne nový nález.

Program [check_dlx_ordering.py](check_dlx_ordering.py) porovnal intervalovou
a bitovou definici v 8 256 případech a všechny dvojice pro m=1..128:
**707 264 párových testů**. Opravený svědek funguje všude; původní má
v tomto rozsahu 44 358 selhání (stejné j,k pro více m se počítají zvlášť).

## K-násobné pořadí, úloha 21

Každá α_j^i obsahuje primární a_i, položky B_j z rozhraní i−1 (pokud i>1)
a položky A_j z rozhraní i (pokud i<k). Každé rozhraní má vlastní názvy.
Přesně jedna možnost z každé vrstvy a absence sekundárního překryvu je
proto ekvivalentní j1≤j2≤…≤jk. Počet řešení je binom(m+k−1,k).

Předchozí bitový důkaz omezuje součet obou sousedních sad na ceil(lg m),
nikoli na dvojnásobek. Vnitřní možnosti pro mocninu dvou mají přesně lg m
sekundárních položek. Všechny čtyři ukázkové možnosti pro m=4 souhlasí.

Doslovný spacerový X i neupravený veřejný DLX1 se shodují s kartézským
oraclem v **48 úplných množinách modelů** pro m=1..8,k=1..6. V k=1 se
m identických jednopoložkových možností rozlišuje pořadovým číslem, jak
vyžaduje indexovaná rodina možností. Souhlasí i celé profily obou X.

Pro m=20,k=8 veřejný DLX1 skutečně dokončil **2 220 075** řešení.
Při primárním pořadí a1..a8 spotřeboval **860 664 032 memů**, přibližně
387,67 na řešení, proti knižnímu 1,1G / přibližně500. Změny primárního
pořadí dávají 531 822 934 až 972 000 322 memů; obrácení pořadí sekundárních
položek uvnitř možností původní náklad nezměnilo. Počet řešení je ve všech
případech stejný. Úloha pořadí položek nefixuje a veřejný program nemusí
být totožný s historickým měřením. Tento rozdíl není důkaz nového errata.
Matematika a počty jsou uzavřeny; přesná reprodukce knižních přibližných
memů zůstává jako samostatná mezera, a proto je celý záznam 21 částečný.

## Rozsah úplného průchodu

Uzavřeny úlohy **16–20** (20 s již publikovanou opravou) a celá strana 71.
Úlohy 15 a 21 zůstávají částečné z uvedených výkonových důvodů.
Str. 70 čeká na n16; str. 72 na náklady a rozšíření n-dam. Str. 125 stále
obsahuje částečnou úlohu 14 a str. 126/419 další dosud neuzavřené úlohy.
Zobrazení těchto stránek nepředstírá kontrolu jejich zbývajícího obsahu.
