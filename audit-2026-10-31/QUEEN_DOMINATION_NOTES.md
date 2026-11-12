# Dominující dámy: text na str. 94 a úlohy 159–161

Kontrola 1. 11. 2026. Všech 7 624 512 pětiprvkových podmnožin šachovnice
8×8 bylo prohlédnuto nezávislým bitovým programem. Přesně 4 860 z nich
pokrývá všechna pole. Každý uložený výsledek pak prošel geometrickou
kontrolou řádků, sloupců a diagonál v samostatném Python programu.

## F067: dvě velikosti komponent v odpovědi 160

Správný histogram komponent grafu přesouvání jediné dámy je:

| Vrcholů v komponentě | Počet komponent |
|---:|---:|
| 1 | 388 |
| 2 | 100 |
| 3 | 40 |
| 4 | 34 |
| 5 | 20 |
| 18 | 4 |
| 20 | 2 |
| 3804 | 1 |

Počet komponent 589, izolovaných vrcholů 388 a velikost obra 3 804
v knize souhlasí. Zbývajících 200 komponent ale má velikosti **2 až 20**,
nikoli 2 až 12. Poslední příklad (65) na str. 94 patří do komponenty
velikosti **20**, nikoli 8. První tři příklady patří do obra správně.

Poslední příklad má dámy v buňkách (číslováno od nuly shora zleva)
(0,2), (2,7), (3,3), (5,0), (7,5). `check_queen_component.py` začne pouze
s touto polohou, bez seznamu všech 4 860 řešení. Vyzkouší každý přesun
každé dámy na každé volné pole a přímo geometricky ověří pokrytí desky.
Opakováním do uzávěru získá přesně 20 poloh a 26 hran. Tím je nezávisle
dokázána souvislost i uzavřenost této komponenty. Všech 20 poloh je
v `results/queen_domination/components-direct.json`.

„Přesun“ zde znamená libovolné přemístění jedné dámy. Tento výklad
reprodukuje všechny tři správné počty knihy. Pro kontrolu byly spočítány
i dvě přísnější varianty: pouze přesun po dámské linii dává 849 komponent,
legální šachový tah se zákazem přeskakování jiných dam dává 861. Nejsou
to grafy zamýšlené v odpovědi 160 a jejich čísla nemícháme do F067.

Oba chybné údaje jsou čitelné v PDF str. 461 a autorově PS str. 165.
Ve veřejných all4b a all4f5 nebyla oprava nalezena; historický vydaný
Fascicle 5 má odpověď na str. 269. Jde o jeden nález ke stejné odpovědi.

## Ostatní počty jsou správné

Všech deset omezení v hlavním textu na str. 94 dává po řadě
284, 880, 88, 200, 90, 2, 18, 48, 3 248 a 96 řešení.
Všech deset kvadrantových případů 159 má uvedené počty
134, 884, 33, 23, 34, 1, 16, 0, 22, 0 a vážený součet 4 860.

Varianty 161 mají 728 nezávislých dominujících pětiprvkových množin,
352 totálně dominujících a 20 klikově dominujících. Samostatný výčet
neútočících dam po řádcích potvrzuje také počty maximálních nezávislých
množin velikostí 6,7,8: 6 912, 2 456 a 92. Kódování 161 je správné:
sekundární položka hrany vyloučí společný výběr sousedů; vynechání
samotného vrcholu z pokrývací možnosti vyžaduje cizího souseda; barvy
1 u zvoleného vrcholu a 0 u nesousedů vyloučí každou nehranu kliky.

Při osmi symetriích čtverce má úplných 4 860 poloh 638 tříd:
577 tříd velikosti 8 a 61 tříd velikosti 4. Historické počty paměťových
operací a uvedené zrychlení Algorithm M nebyly reprodukovány.
