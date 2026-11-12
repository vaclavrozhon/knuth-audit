# Rozdělení grafu USA, strany 114–115 a úlohy 240–245(a)

Graf 48 států a 105 hran byl načten přímo z vektorových čar obrázku (113)
v PDF. Písmena států byla přiřazena podle souřadnic textu. Nepoužili jsme
současnou externí geografickou databázi, která by mohla mít jiné konvence
pro vodní hranice či bodové dotyky. Pro úlohu 245 je přidán DC s hranami
k MD a VA podle zadání.

| Případ | Souvislé možnosti | Po odříznutí nemožných zbytků | Počet rozdělení | Nejmenší cena | Optimální rozdělení |
|---|---:|---:|---:|---:|---:|
| 48 států, skupiny po 6 | 11 505 | 6544 | 4 536 539 | 72 | 2 |
| 48 států, skupiny po 8 | 135 847 | 40 520 | 4 177 616 | 54 | 2 |
| 49 vrcholů včetně DC, po 7 | 42 498 | 17 268 | 4 517 463 | 58 | 1 |

Všechny zveřejněné počty a minima v tomto rozsahu souhlasí. Cenu dělíme
na polovinu, chceme-li počet odstraněných hran.

Nezávislý dynamický program nad bitovými množinami spočítal všechny tři
případy včetně násobností optim. Rozpojené zbytky řeší zvlášť a jejich počty
násobí. Původní DLX5 potvrdil všechna minima i násobnosti; každý jeho
průběžný model byl geometricky a cenově validován. Původní DLX2 navíc
potvrdil celkové počty pro skupiny po 6 a po 7. Běh pro skupiny po 8
byl ukončen po 1200 sekundách; tento jednotlivý běh není důkazem počtu.
Počet pro něj je doložen kompletním nezávislým dynamickým programem.

Úloha 240 má přesně šest uvedených možností obsahujících MT a TX. Řetězec
(114) oddělí komponenty velikostí 11 a 31. ME je ve 25 souvislých šestiskupinách,
ale po redukci zůstane jediná skupina Nové Anglie. DLX-PRE na plném vstupu
odstranil 3983 možností a 5 položek, přesně jako odpověď 241.

Test 242 má obecný důkaz: d lze rozložit na q celých čísel z [L,U), právě
když qL≤d≤q(U−1). Nejmenší možné q je ceil(d/(U−1)); existence tedy
odpovídá d≥L ceil(d/(U−1)). Vedle důkazu prošlo 36 000 malých případů
nezávislým dynamickým rozkladem celého čísla.

Populační příklady na stranách 115–116, úloha 245(b) a optimalizace 246
zatím nejsou v tomto bloku prověřené.

Soubory: [příprava z PDF](prepare_usa_partitions.py),
[nezávislý DP](usa_partition_dp.cpp), [spuštění](run_usa_dp.py),
[validace](verify_usa_partitions.py), [výsledky](results/usa_partitions/verified.json).
