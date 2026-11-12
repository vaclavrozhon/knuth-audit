# DLX151–152 — přímá kontrola původních obrázků, 3. listopadu 2026

Nová kontrola našla správné dílky a jedinou smyčku ve všech čtyřech
vytištěných sestavách. **Žádný nový nález.** E076 a E077 jsou už zveřejněné
opravy, které naše PDF obsahuje. Úloha152 je zrevidovaná s výslovně
vynechaným historickým benchmarkem. Úloha151 zůstává částečná kvůli
přesné historii z roku1999.

## Co bylo hotové a co tento průchod doplnil

Starší [PATH_DOMINO_NOTES.md](PATH_DOMINO_NOTES.md) už obsahoval katalog,
vlastní řešení151(a,b), důkaz maxima32, obecný důkaz nemožnosti nekřížící
se sady a úplný počet **6420** faktorizovaných sestav. Tento počet je
doložen rozdělením625 geometrií do169 orbit a169 nezávisle zkontrolovanými
DRAT certifikáty. **Žádný z těchto řešičů ani ověřovačů se znovu nespouštěl.**

Nově jsou přečteny přímo původní vektorové obrázky v PDF i autorově draftu:
36 dílků v zadání151, po36 v obou odpovědích a48 v odpovědi152. Každá
z156 obdélníkových pozic má správný tvar a přesně předepsaný typ, bez
opakování či chybějících kusů. Kontrolují se konce všech285 podcest;
křížení uvnitř dílku se nepovažuje za rozcestí. Výsledné grafy mají jednu
komponentu, všechny vrcholy stupně2 a žádné výstupy ven z desky.
V původním PDF a draftu jsou stejné všechny dílky a spoje.

| Obrázek | Vodorovné / svislé dílky | Podcesty | Výsledek |
|---|---:|---:|---|
| Zadání151 | 2 / 34 | 63 | všech36 typů, jedna smyčka |
| Odpověď151(a) | 18 / 18 | 63 | všech36 typů, jedna smyčka |
| Odpověď151(b) | 32 / 4 | 63 | všech36 typů, jedna smyčka |
| Odpověď152 | 28 / 20 | 96 | všech48 typů, jedna smyčka |

Všechny12 dodatečných vzorů v zadání152 také přesně odpovídají katalogu:
jeden prázdný a11 se třemi podcestami. **Tím je uzavřena dřívější mezera
existence sestavy48 dílků**, kterou stará časově omezená hledání nevyřešila.
Staré timeouty zůstávají timeouty; nový důkaz je přímo vytištěný svědek.

`accept_paths151.py` ověřil hashe rozbalených169 CNF a DRAT souborů proti
archivovaným metadatům, záznamy úspěšné verifikace,169 orbit a vážený
součet6420. Nově přečtené maximum151(b) patří do uložené množiny6420
modelů. Neproběhla další enumerace. První nový soubor `claims-checked.json`
navrhoval vynechat také6420; finální `accepted.json` to výslovně opravuje
a přebírá starší hotový důkaz. Původní důkazní soubory se nemění.

## Obecné důkazy a model

Pro k=0,1,2,3 podcest jsou počty označených párování1,15,45,15 a počty
pevných bodů půlotáčky1,3,9,7. Burnside dává1,9,27,11 typů. Nekřížící se
párování dávají1,9,18,4, tedy32 typů. Nový malý katalog slouží také
k přímému přiřazení typů v kresbě; nejde o výčet rozmístění.

Po zapomenutí párování jsou pro jednu podcestu9 masek s násobností1;
pro dvě podcesty9 masek s násobností3. Ve152 přibývá prázdná maska1
a plná maska11. Primární položky buněk vynucují úplné pokrytí, typové
položky správný inventář a H/V počet orientací. Sekundární barevné položky
hran vynucují shodu přítomnosti/nepřítomnosti cesty, nikoli její souvislost.
Vnější konce musí být zakázány už při generování možností.

Na desce8×9 je7×9+8×8=127 vnitřních hran. Obě vytištěné ukázkové možnosti
jsou správně: mají stejnou aktivní masku(1,2,3,4) ve dvou otočeních;
u vodorovné možnosti chybí jen vnější nulová hrana, která není sekundární
položkou. Všechny čtyři vytištěné sestavy splňují i předepsané násobnosti.

Ve druhé fázi volíme právě jeden konkrétní dílek na každé místo a každý
typ právě jednou. Párování připojení určuje graf podcest; předčasný cyklus
lze odmítnout evidencí konců rozpracovaných cest. To vysvětluje návaznost
na AlgorithmX a na úlohu413, jejíž zadání skutečně žádá obecné vynucení
jediné smyčky. Tento průchod neoznačuje celý obsah413 za zrevidovaný.

Každý řádek desky8×9 má lichý počet polí a musí obsahovat lichý počet
polí svislých domin. Jsou potřeba alespoň8 takových polí, tedy4 svislé
kusy. Maximum vodorovných je32 a původní obrázek jej dosahuje. Při rovnosti
má každý řádek právě jedno svislé pole, takže svislé kusy párují řádky
(0,1),(2,3),(4,5),(6,7). Vynechání lichých počátečních řádků je tedy
logicky správné; přesnou úsporu času netvrdíme.

## Nekřížící se sada32 — kratší formulace starého důkazu

Obarvíme políčka šachovnicově. Každé domino pokrývá jedno černé a jedno
bílé pole. Má sudý počet aktivních konců, takže parity počtu konců na jeho
obou polích jsou stejné a nezávisí na natočení. Počet typů s lichou
paritou je po skupinách0,6,6,4, celkem16: celkový počet černých konců
je tudíž sudý.

Počet podcest je9+2·18+3·4=57. V uzavřené sestavě spojuje každé rozhraní
právě jeden černý a jeden bílý konec. Počet černých konců proto musí být
roven polovině všech konců, tedy57, což je liché. Spor. Platí i pro více
smyček a pro jakýkoli tvar desky. Starší formulace používá9 nenulových
příspěvků±2, které také nemohou dát nulu; oba důkazy vyjadřují stejnou
šachovnicovou překážku.

## Errata, historie a přesná omezení

- **E076**, 5.11.2022: do odpovědi151 doplnit odkaz na úlohu413.
- **E077**, 22.7.2022: do odpovědi152 přidat prázdný vzor násobnosti1.

Obě opravy jsou přítomné v místním PDF, chybějí v draftu2019. Šest vrstev
errat má stejné hashe jako dnešní ověřené stažení. Žádný nový rozpor.

Vyhledávač našel původní [stránku Eda Pegga](https://www.mathpuzzle.com/dominopat.html),
jejíž indexovaný text připisuje řešení Rogeru Phillipsovi. Přímé otevření
vrátilo ověřovací bránu; nebyla obcházena. Přesné datování1999 a prvenství
nejsou doloženy plným původním dokumentem, takže151 zůstává partial.

Podle uživatelova pokynu jsou výslovně nereplikované: tvrzení o milionech
faktorizovaných řešení151(a), historické časové odhady a náklad35.1Tmems
v152. **Počet6420 v151(b) do vynechání nepatří**, má již hotový důkaz.
Nebyl spuštěn žádný nový placement search. Zdrojové programy starých běhů
zůstaly nezměněné. Následuje153; celý svazek není hotový.
