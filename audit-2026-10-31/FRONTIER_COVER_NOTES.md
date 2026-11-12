# Počítání přesných pokrytí — 7.2.2.1–40 až 42

Kontrola 1. listopadu 2026. Zadání na tištěných stranách 127–128, odpovědi
na 424. Obrazy `images/vol4b-p128.png`, `images/vol4b-p424.png` a
`images/fasc5c-dlx39-p128.png` byly prohlédnuty; poslední je odpovídající
autorský PS. Fyzický exemplář není ověřen.

## Algoritmus 40: invariant a mazání

Po zpracování prvních k možností eviduje každá položka databáze počet
podmnožin jejich **indexů**, které nemají konflikt. Už ukončené primární
položky musí být pokryté; ukončené sekundární položky už neovlivní žádné
budoucí rozhodnutí a jejich bity můžeme zapomenout. Nepoužité primární
položky, které nikdy nebyly v žádné možnosti, nakonec vyloučí závěrečný test.

N3 rozdělí podmnožiny na ty, které nepoužijí řádek k, a ty, které jej použijí.
Přidat k lze právě při nulovém průniku příslušných masek. Počty se sčítají,
protože tyto dvě třídy jsou disjunktní. To platí i pro opakované vstupní
možnosti: různé indexy představují různé výběry.

Pro `u=r_k & ~f_k` se v N4 odstraní stavy s nepokrytým bitem `u & p`.
U zbývajících lze vynulovat bity `u & ~p`. Dva takto shodné stavy mají
stejné možnosti pokračování, takže se jejich počty opět sečtou. Ukončené
primární bity zůstávají rovny 1. Na konci nemůže existovat více než jeden
klíč: všechny někdy se vyskytující primární bity jsou 1 a ostatní bity 0.
Proto platí závěrečné N≤1, včetně prázdného vstupu.

Pole se zpracovává sestupně, přes původní délku před každým průchodem.
Při N3 nemůže nová položka spustit další připojení téhož řádku: má s ním
nenulový průnik. Při sestupném N4 je položka přesunutá z konce už vyřízená.
Případná nová normalizovaná položka také nepotřebuje opakovat stejnou
normalizaci. Sloučení mění počet, ale ne podmínky pro další zpracování.

`check_frontier_cover.py` realizuje přesně toto pole, včetně výměny poslední
položky při mazání. Pomocný slovník pouze zrychluje vyhledání shodného klíče.
Po každém prefixu porovnává celou databázi a celé množiny indexových řešení
s nezávislým výčtem všech podmnožin zpracovaných řádků.

`results/frontier_cover/small.json` potvrzuje 9 420 vstupních běhů,
33 770 úplných porovnání prefixů, 67 540 kontrol mezí mezi kroky a
33 770 kontrol dvojnásobné meze během vkládání. Obsahuje různé i opakované
možnosti, různá pořadí, primární i sekundární položky a prázdný vstup.

## C020 — v jakém okamžiku platí mez 2^ν

Označme P sjednocení minulých řádků, R současný řádek a F sjednocení
budoucích. Knižní maska hranice je bitová většina

```text
B = (P & R) | (P & F) | (R & F),    ν = popcount(B).
```

Před N3 jsou proměnlivé pouze bity v `P & (R | F)`, po kompresi N4 pouze
bity v `(P | R) & F`. Obě množiny jsou podmnožinami B. Všechny ostatní bity
mají v přežívajících stavech pevnou hodnotu. V těchto okamžicích je proto
počet klíčů nejvýše 2^ν.

**Během N3 obecně platí jen 2^(ν+1).** Každý původní klíč vytvoří nanejvýš
jeden další klíč; komprese N4 délku nezvětší. Přesný příklad obsahuje jedinou
primární položku a jedinou možnost `{a}`. Máme P=F=0, R=1 a ν=0.

| Okamžik | Databáze (maska, počet) | N |
|---|---|---:|
| N1, před N3 | (0,1) | 1 |
| po N3, před kompresí | (0,1), (1,1) | 2 |
| po kompresi N4 | (1,1) | 1 |

Vytištěné neomezené „never exceeds“ tedy doslovně neplatí uvnitř iterace.
Stačí vymezit kontrolní okamžiky nebo přidat faktor 2. V malých úplných
testech nastalo 2 351 takových dočasných překročení; správné počty řešení
ani asymptotický exponenciální faktor tím nejsou dotčeny.

**Klasifikace: kandidát, nízká závažnost.** Je možné, že autor implicitně
měří pouze po dokončené kompresi. Číselný protipříklad je prokázaný, ale
interpretaci rozsahu tvrzení vedeme otevřeně. Nezvyšuje počet potvrzených
chyb. PDF i PS mají stejné znění; relevantní errata nemají odpovídající
upřesnění.

## Proč má hranice dam nejvýše 3n položek

Předpokládáme pořadí polí po řádcích, uvnitř řádku vzestupně podle sloupce;
bez této podmínky tvrzení pro libovolné pořadí neplatí. Rozdělení položek je
`r_i`, `c_j`, `a_(i+j)`, `b_(i-j)`, jak stanoví (23).

Pro vnitřní řádek `2≤i≤n−1` a aktuální sloupec j:

- hranice obsahuje jedinou položku aktuálního řádku a všech n sloupců;
- součtových úhlopříček je `n−2+[j=1 nebo j=n]`;
- rozdílových úhlopříček je n.

Součet je tedy `3n−1+[j je krajní]≤3n`. První řádek má
`3j−[j=n]≤3n−1` položek v hranici pro n≥2; poslední plyne otočením desky
o 180° a obrácením pořadí. Případ n=1 má prázdnou hranici, n=2 ověříme
přímo (maximum 5). Rovnosti pro vnitřek lze získat průnikem intervalů:
minulé součty jsou 2 až i+n−1, budoucí i+2 až 2n a aktuální součet doplní
jeden kraj právě pro j=1 nebo n; u rozdílů aktuální diagonála doplní
případný chybějící kraj, takže je jich právě n.

Testy všech řádků pro n=1 až 11 dávají maxima
`0,5,9,12,15,18,21,24,27,30,33`. S předchozím faktorem 2 mají operace stále
horní odhad `8^n` krát polynom v n. Zpracování n² možností, délka masek,
velikost přesných čítačů i vyhledávání v uspořádané databázi přidají pouze
polynomiální faktory. Naproti tomu úplný výpis všech řešení vyžaduje alespoň
Q(n) kroků; již ověřený odkaz na Simkinovu asymptotiku v úloze 7.2.2–15
odůvodňuje asymptotické rozlišení v odpovědi 41.
Samostatný `check_frontier_variants.py` navíc ověřil explicitní vzorce pro
všech 73 810 polí desek n=1 až 60, bez enumerace jejich řešení.

## Původní článek a Lampingovo jméno

Archivovaný [Rivinův a Zabihův článek](https://www.cs.cornell.edu/~rdz/Papers/RZ-IPL92.pdf)
vyšel v *Information Processing Letters* 41 (1992), 253–256.
Poděkování na straně 256 připisuje kompresní postup oddílu 3.2
**Johnu Lampingovi**. Kniha správně připisuje algoritmus všem třem;
není chyba, že Lamping není uveden jako spoluautor článku.
Primární zdroj a jeho hash jsou v `sources/rivin-zabih-1992-queens.*`.

## Úloha 41: počty a rozlišení výkonových údajů

`check_frontier_queens.py` spočítá obyčejné dámy i queen bees pro n=1 až 11.
Nezávislý souřadnicový backtracking potvrdí každý počet. Při n=11 navíc
porovnává výsledek s archivovaným neupraveným DLX1. Všechny počty souhlasí,
zejména Q(11)=2 680 a H(11)=596 483.

Pro řádky v přirozeném pořadí a sekundární úhlopříčky dostáváme:

| Model n=11 | Maximum včetně N3 | Maximum po N4 |
|---|---:|---:|
| obyčejné dámy | 75 010 | 71 868 |
| bees, rozdílové úhlopříčky | 96 927 | 96 716 |
| bees, součtové úhlopříčky | 71 095 | 62 274 |

Poslední dvě instance mají stejná řešení až na zrcadlení, ale zrcadlení mění
pořadí možností vzhledem k úhlopříčkám. Tím je přímo doložena citlivost
maxima na zpracovávaný vstup. Knižních 75 009 / 364 864 a náklady
25 Mμ / 30 Mμ původní náhodné binární databáze zatím nereprodukujeme.
Rozdíl jedné položky u dam sám o sobě nedokazuje chybu historické implementace;
chybí přesný vstup, kód a konvence měření maxima.

Souřadnicové počty, všechny průběžné délky a výstupy DLX1 jsou uloženy
v `results/frontier_cover/`. Dodatečná porovnání veřejné organ-pipe priority
primárních položek a odstranění jednočlenných úhlopříček zachycuje
`check_dlx_order_costs.py`. Pythonový slovník nenahrazuje historické memové
účtování trojitě vázaného stromu. Úloha 41 proto zůstává **partial**.

Samostatná druhá DP implementace v `check_frontier_variants.py` pracuje
s novými neměnnými mapami pro každou fázi a uchovává pouze bity budoucích
položek. Neprovádí výměny v poli a zapomíná i pevné ukončené primární bity.
Přesto souhlasí všechny tři úplné n=11 počty a všech 363 trojic délek databáze
(před N3, po N3, po N4). Tím je rozdíl maxima ověřen bez závislosti na
první implementaci mazání. Výsledek je v `results/frontier_cover/independent.json`.

Ve veřejné organ-pipe prioritě DLX1 při n=11 naměříme pro dámy
11 456 417 memů (11 306 609 po odstranění triviálních úhlopříček), pro bees
264 339 036 (258 247 994). Přirozená priorita všech řádků před sloupci dává
19 297 741 a 315 324 934. Tyto různé výsledky jsou přesně zaznamenané
benchmarky našich vstupů; nereprodukují přesně historických 12.5 Mμ / 440 Mμ.

## Úloha 42: reprezentace celých řešení

Místo počtu uložíme množinu slov nad abecedou indexů možností; každé slovo
má přísně rostoucí indexy. Počáteční reprezentace je `{ε}`. Přidání řádku k
je konkatenace symbolem k, sloučení stejných stavů je sjednocení. Filtrace
primárních a zapomenutí sekundárních položek zachovávají tutéž reprezentaci
u přežívajících stavů a při jejich sloučení spojí disjunktní množiny slov.

Indukce z invariantu 40 dokazuje, že poslední přijatý stav reprezentuje právě
všechna řešení a žádné slovo dvakrát. Pro jediného svědka stačí uchovávat
libovolné jedno slovo z neprázdné množiny: stejný klíč zaručuje shodnou
budoucí kompatibilitu. To je přesně zamýšlené rozšíření odpovědi 42.
Na všech 33 770 kontrolovaných prefixech byl porovnán celý jazyk, uložený
pro malé vstupy jako množina bitových masek indexů, s nezávislým výčtem.
Opakované možnosti zůstávají rozlišené svým indexem.

Úloha 42 je **reviewed**. U 40 je algoritmus, komprese a obecná opravená
mez ověřena; neomezené znění původní meze zůstává kandidátem C020, a celá
úloha je proto zatím **partial**.
