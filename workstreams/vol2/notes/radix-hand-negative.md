# §4.4 C a úlohy 6, 11, 12: ruční převody a záporný základ

Kontrola 2. listopadu 2026. Původní sazba 323–325, 327–328 a 637
byla vizuálně přečtena, stejně jako relevantní náhrady v erratech.
`b` označuje vstupní základ, `B` výstupní základ a `v` hodnotu již
přečteného prefixu číslic. V první části jsou oba základy kladné.
Čtyři základní metody jsou definovány v [radix-basic.md](radix-basic.md).

## Ruční celočíselné převody

Připsání další vstupní číslice d k dosavadnímu prefixu, čtenému
v cílovém základu B, vytvoří hodnotu Bv+d. Přičtením `(b-B)*v`
dostaneme právě bv+d, tedy hodnotu delšího vstupního prefixu.
To je invariant ručního postupu i Hornerova pravidla 1b.
Pro převod 8→10 odečítáme dvojnásobek prefixu, pro 10→8 jej
přičítáme; pro 9→10 odečítáme prefix jednou a obráceně přičítáme.

Je nutné pracovat s celým prefixem vlevo od postupujícího bodu.
Jeho délka v nové soustavě nemusí být číslem kroku. To je obsah
známé náhrady z roku 2018, včetně nových příkladů a úlohy 11.
Devět tabulek v `verify_radix_hand_negative.py` kontroluje každý
mezilehlý prefix, nejen výslednou hodnotu. Například:

```text
1234567 v základu 8 → 1, 10, 83, 668, 5349, 42798, 342391
342391 v základu 10 → 3, 42, 526, 6537, 102677, 1234567 (základ 8)
21446  v základu 8 → 2, 17, 140, 1124, 8998
8998   v základu 10 → 8, 131, 1603, 21446 (základ 8)
```

Počáteční 8 v posledním řádku je záměrná nenormalizovaná vstupní
číslice; po prvním kroku již máme běžný zápis v základu 8.
Původní příklady 5325121↔1419857 a 57721→24529 rovněž souhlasí.

V úloze 12 seskupení ternárních číslic po dvojicích dává
`1|21|20|11|21|02|10`, tedy `1764723` v základu 9. Převod do
desítkové soustavy postupuje přes prefixy
`1,16,150,1354,12193,109739,987654`. Zpětné prefixy v základu 9
jsou `9,118,1316,14483,160428,1764723`; počáteční 9 je opět
dočasně nenormalizovaná. Všechny rovnosti jsou přesné.

## Zlomky a kontrola devítkou

Ruční zlomkový převod je metoda 2a: násobení 8 lze v desítkové
aritmetice provést jako desetkrát minus dvakrát; násobení 10
v osmičkové aritmetice jako osmkrát plus dvakrát.
Pro `.14159` vyjdou osmičkové číslice `110374` a postupné
desítkové zbytky s pevným jmenovatelem 100000 jsou
`13272,06176,49408,95264,62112,96896`.
Číslo **95264** je známá oprava 25. října 1999; první tisk má
95246, ale jeho další dvojnásobek již odpovídá správnému zbytku.
Při opačném převodu `.110374` vyjde desítkový prefix `141586`;
zbytky v základu 8 jsou `324730,121160,454140,671700,502600,233400`.
Program kontroluje i všechny mezilehlé dvojnásobky obou tabulek.

Protože `10 ≡ 1` a `8 ≡ -1` modulo 9, je desítkový součet
číslic shodný s osmičkovým střídavým součtem, kde nejnižší číslice
má znaménko plus. Důkaz platí pro každý prefix. Prošlo i 10000
nezávislých porovnání zápisů a konkrétní příklad doplněný 2024:
`6+6+8 ≡ 4-3+2-1 (mod 9)`.

Údaj o zachycení asi 89 % chyb odpovídá rovnoměrnému rozdělení
nenulových chybných výsledků mezi devět zbytkových tříd; není
bezpodmínečnou vlastností libovolného modelu lidských chyb.
Kontrola může minout chybu dělitelnou 9. Také vyhledávání chybného
kroku půlením předpokládá, že zkoušené chybné prefixy test odhalí.
Text kontrolu výslovně označuje za nedokonalou, proto zde není
nový nález. Srovnání obtížnosti ruční práce není formální časová mez.
Historické prameny Soden/Rozier patří do samostatné kontroly kontextu.

## Základ −2: celé číslo a metody 1a/1b

Číslice jsou 0 a 1; váha j-té číslice zprava je `(-2)^j`.
Takový konečný zápis může vyjadřovat kladná i záporná celá čísla.
Pro celé u určíme zbytek r z množiny {0,1} jeho paritou a položíme

```text
r = u mod 2,        q = (u-r)/(-2) = -floor(u/2).
```

Identita `u=-2q+r` dokazuje metodu 1a pro cílový základ −2.
Podíl obecně není `floor(u/(-2))`. Pro `|u|>=2` je
`|q| <= (|u|+1)/2 < |u|`; zbývající případy jsou `1→0` a
`-1→1→0`. Algoritmus tedy končí. Jednoznačnost plyne indukcí:
parita určí poslední číslici, poté je jednoznačný zbylý podíl.
Vedoucí nuly se samozřejmě mohou přidávat.

Metoda 1b je stejná identita `v <- b*v+d`, také pro b=−2.
Pracovní hodnoty mohou být záporné. Chceme-li současně počítat
v cílovém základu −2, normalizujeme v každém sloupci celé t
pomocí číslice `t mod 2` a přenosu `(t-(t mod 2))/(-2)`.
Tato normalizace platí i pro záporné přenosy. Pro kladný cílový
základ se záporná celková hodnota vypíše odděleným znaménkem
a převodem absolutní hodnoty; doslovné opakované kladné dělení
záporného u by jinak mohlo uváznout na −1.

## Základ −2: zlomky a metody 2a/2b

Zlomek bez celočíselné části má tvar `sum(d_j*(-2)^(-j),j>=1)`.
Volba jedniček na lichých místech dává minimum −2/3, na sudých
maximum 1/3. Celý přípustný interval tedy je `I=[-2/3,1/3]`.
Metodu 2a lze realizovat takto, se zbytkem r v I:

```text
d = 1 pro r < -1/6, jinak d = 0;
r' = -2*r-d.
```

Obě větve vracejí r' do I. V bodě −1/6 lze vybrat i druhou
číslici; zde volíme 0. Po M krocích platí

```text
u = a + sum(d_j*(-2)^(-j), j=1..M) + r_M*(-2)^(-M),
```

kde a je celočíselná část. Odtud plyne chyba po uříznutí nejvýše
`(2/3)*2^-M`. Obyčejná volba `floor(-2*r)` obecně nedá číslici
0 nebo 1, například pro r=1/4. Proto se původní kladný postup
nedá použít beze změny.

Pro libovolné reálné u můžeme vybrat `a=ceil(u-1/3)`; potom
`u-a` leží v `(-2/3,1/3]`, a lze použít právě popsaný postup.
Celé a se vypíše před bodem metodou 1a. Uzavřený interval I
v pracovním algoritmu je nutný: jeho krajní body odpovídají
periodickým rozvojům `1010...` a `0101...` a jeden se při kroku
může zobrazit na druhý.

Konečné zlomkové rozvoje jsou přesně dyadická racionální čísla
v I, tj. čísla se jmenovatelem dělícím nějakou mocninu 2.
Nutnost plyne ze součtu vah. Pro postačitelnost má zbytek
po každém kroku o jednu nižší mocninu 2 ve jmenovateli.
Po m krocích ze jmenovatele `2^m` zbývá celé číslo v I, tedy 0.

Metoda 2b zpracovává číslice od nejnižší opakováním
`v <- (v+d)/b`. Algebraický důkaz funguje také pro b=−2;
je třeba připustit záporné mezivýsledky. Při chybě každého kroku
nejvýše eta je absolutní konečná chyba menší než 2 eta, protože
přenesené chyby mají velikosti nejvýše `eta,eta/2,eta/4,...`.

Zaokrouhlení na M míst lze bezpečně popsat mřížkou: vybereme
nejbližší celé k k `2^M*u` s pevnou konvencí pro půlení, zapíšeme
celé `(-1)^M*k` v základu −2 a vložíme bod M míst zprava
(případné nuly doplníme). Hodnota je `k/2^M` a chyba nejvýše
`2^(-M-1)`. Kvůli střídavým znaménkům vah se kladný test
„zbytek větší než 1/2“ nepřenáší doslova.

## Doklady a rozsah

Relace 65798 skončila exit 0; oba checkpointy jsou uloženy v
`results/radix-hand-negative.json` a `.log`. Vedle devíti ručních
tabulek a 10000 kontrol modulo 9 prošlo:

- 20001 kladných, nulových a záporných celých vstupů;
- 2100 Hornerových převodů z různých vstupních základů;
- všech 8191 binárních slov délky 0 až 12 jako zlomků v základu −2;
- oba konce intervalu I a hraniční bod −1/6;
- 3007 obecných racionálních vstupů a 15035 nejbližších zaokrouhlení.

Tyto konečné testy doplňují obecné důkazy. Úloha 6 je otevřené
zadání k diskusi bez tištěné odpovědi; zde jsou pokryty všechny
čtyři metody, znaménka, konvergence i zaokrouhlení.
Úloha 11 je uzavřena po známé náhradě, úloha 12 bez nové chyby.
Všechny čtyři řady errat byly prohledány. Doklady náhrad jsou
`images/radix-all2-pre-{8,9,15}.png`, `radix-all2-prepre-18.png`
a `radix-all2-7.png`. Nejnovější fyzický tisk není ověřen.
