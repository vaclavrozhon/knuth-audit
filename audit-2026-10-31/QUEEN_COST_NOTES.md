# Ceny šestnácti dam: 230, 232–236

Kontrola 1. listopadu 2026. Úplně prošlo **14 772 512** rozmístění
16 neútočících dam, 1 141 190 303 uzlů přímého bitového stromu.
Výpočet [queen_costs.cpp](queen_costs.cpp) trval 58 sekund. Samostatný
oracle prošel všechny permutace pro n=4,…,9 a potvrdil množiny optimálních
rozmístění podle všech deseti kritérií. Ověřeny byly všechny uložené
velké modely, jejich diagonály, ceny a úplné orbity D4.

## Potvrzené výsledky knihy

| Kritérium | Hodnota | Rozmístění | Třídy D4 |
|---|---:|---:|---:|
| minimum součtu vzdáleností | 95,6348751794… | 8 | 1 |
| maximum součtu vzdáleností | 102,8735985163… | 8 | 2 |
| minimum součtu dolních celých částí vzdáleností | 84 | 96 | 12 |
| minimum součtu 4d⁴ | 127 760 | 16 | 4 |
| maximum součtu 4d⁴ | 187 760 | 8 | 1 |
| minimum součtu d²⁰ | 130230066663839627189/64 | 8 | 1 |
| limitní minimum seřazených vzdáleností | čtyřikrát každé w=226,202,194,58 | 16 | 8 |

Zde w=4d²=(2i−17)²+(2j−17)² pro souřadnice i,j=1,…,16.
Minimum i maximum součinu vzdáleností dávají přesně tytéž množiny modelů
jako součet vzdáleností. Součiny w byly počítány přesně ve 192 bitech,
nikoli pomocí logaritmů; Python je nezávisle přepočítal. Všechny tři
obrázky 74, ukázka limitního n=16 na straně 152 a tři obrázky ke 235 byly
extrahovány z poloh znaků v PDF a jsou členy správných optimálních množin.

Obecně je součet d² pro libovolnou permutaci n dam nebo věží
n(n²−1)/6. Pro n=16 tedy 680. To potvrzuje 234. Převod maximalizace
na minimalizaci v 230 je správný při uvedeném pevném počtu d možností:
celková nová cena je dC minus stará cena.

## Nezávislý původní DLX5

Autorův [DLX5](https://www-cs-faculty.stanford.edu/~knuth/programs/dlx5.w)
byl archivován a přeložen beze změn. Sedm běhů nezávisle potvrdilo všechny
optimální modely pro vzdálenosti, součiny, celé části a čtvrté mocniny.
Brali jsme vždy o jedno řešení více než je počet optimálních, takže známe
i mezeru k následující ceně.

Pro vzdálenost používáme přesné celočíselné ceny
floor(2³²d)=isqrt(w·2⁶²). Mezery jsou 17 905 986 a 85 831 444 jednotek,
mnohem více než celková možná chyba 16 zaokrouhlení. Tím jsou doložena
i skutečná minima/maxima reálné ceny. Pro součin používáme
floor(2³² ln(sqrt(w/2))); posun o ln(sqrt(2)) zajišťuje nezáporné ceny
a díky pevnému počtu 16 dam nemění pořadí řešení. Mezery jsou 50 204 199
a 46 293 100. Finální celé součiny i modely souhlasí s přímým výčtem.

Souřadnice každého výstupu DLX5 byly nezávisle zkontrolovány, nejen poslední
řádek se statistikou. Původní DLX3 navíc našel přesně všech 16 limitních
rozmístění při předepsaných čtyřech násobnostech radiálních vzdáleností.

## F075: dvě ceny ve 236 mají jinou jednotku vzdálenosti

Strana 478, autorův PS strana 182: hodnoty pro N=20 mají být přibližně
**2,03×10¹⁸ a 2,05×10¹⁸**, nikoli 2,08×10²¹ a 2,09×10²¹.
Pro explicitně uvedenou permutaci je přesná první hodnota
130230066663839627189/64. Pro limitní obrázek je druhá hodnota
130915446232517223025/64.

Po vynásobení obou hodnot 1024 dostaneme právě čísla zaokrouhlená v knize.
To nasvědčuje použití sqrt(2)d místo definovaného d; jde o vysvětlení
z čísel, nikoli tvrzení o neveřejném autorově kódu. Definice d na straně 112
byla vizuálně ověřena v PDF i PS. Optima a jejich pořadí se škálováním nemění.
Související praktická poznámka: v 233 jsou samotné ln d pro čtyři středová
pole záporné; skutečný vstup nezáporného DLX5 potřebuje konstantní posun.
Tuto související normalizaci nepočítáme jako další samostatný nález.

## F076: v „právě když N≥21“ chybí N=2

Pro kladné **celé** exponenty je správné tvrzení **N=2 nebo N≥21**.
Při N=2 mají všechna rozmístění cenu 680, tedy také limitní rozmístění.
Nejde o požadavek jedinečnosti: i pro N≥21 má úloha 16 optimálních
rozmístění v osmi třídách D4.

Zbytek hranice jsme ověřili přesně, nikoli jen plovoucí aritmetikou:

1. Pro N=1 a N=3,…,20 máme explicitní lepší rozmístění, potvrzená
   celočíselnými intervaly. Pro N=3,…,20 stačí jediný optimální svědek z N=20.
2. Pro každý N=21,…,159 jsme porovnali všech 1 846 955 tříd D4.
   Osm tříd má shodný limitní multiset vzdáleností. U ostatních se nejprve
   zruší společné vzdálenosti a v označuje největší zbývající w. Počítáme
   přesné dolní konce intervalů
   floor(2⁵⁶(w/v)^(N/2)) = isqrt(floor(2¹¹²wᴺ/vᴺ)).
   Rozdíl zaokrouhlených cen má chybu menší než 16; nejmenší nalezený
   rozdíl je 762 845 048 349 141, tedy bezpečně kladný.
3. Pro všechna N≥160 stačí obecná mez. Jestliže v>226, pak v≥234 a všechny
   záporné zbývající členy mají w≤226. Jestliže v≤226, mají záporné členy
   w≤v−8, protože všechny naše normy jsou 2 modulo 8. V obou případech
   jejich poměr k v je nejvýše 113/117. Existuje alespoň jeden kladný
   člen hodnoty v a nejvýše 16 záporných. Přesná celočíselná nerovnost
   **16·113⁸⁰ < 117⁸⁰** proto zaručuje kladný rozdíl pro N≥160.

Tím je opravené tvrzení dokázáno pro všechny kladné celé exponenty.
Pro reálné exponenty netvrdíme, že přechod leží přesně v 21.

## Reprodukce a rozsah

Hlavní data: [n16.json](results/queen_costs/n16.json),
[ověřené symetrie a přesné ceny](results/queen_costs/verified-summary.json),
[nezávislý DLX5](results/queen_costs/dlx5-verified.json),
[obrázky](results/queen_costs/figures-verified.json).
Certifikát hranice: [queen_power_threshold.cpp](queen_power_threshold.cpp),
[přesná příprava tabulek](prepare_queen_power_threshold.py),
[výsledek](results/queen_costs/power-threshold.json),
[krajní exponenty](results/queen_costs/power-threshold-endpoints.json).
Kontroly uložených modelů: [verify_queen_certificates.py](verify_queen_certificates.py).

Historické opravy 232 a 235 z 18. října 2020 jsou v hlavním PDF již
zapracovány. Odpovídající nové opravy F075–F076 nejsou v prověřených all4b
ani all4f5. Optimální obrázky pro n=17,18,19,32,64,128 ani odhad symetrií
pro obecné n zde neověřujeme. Historická rychlost memů není předmětem shody.
