# §4.3.1 — argumenty a samostatné úlohy

6. listopadu 2026, V2-X0138. Nové upřesnění požaduje argument pro
každé matematické tvrzení a každou úlohu, s převzetím už uzavřených
důkazů bez opakování. Celé původní strany265–284 a odpovědi623–630
jsou přečteny a spárovány s těmito důkazy. Přehled jednotlivých43 úloh
a zdrojů je v `results/sequential-classical-evidence.json`; nejde o
nový běh starých ověřovačů ani o přepsání jejich výsledků.

## Převzaté argumenty hlavního textu

| Obsah | Uzavřený argument |
|---|---|
| Radix, rozsahy, A/S, přenosy a správnost programů | `classical-basic.md`, invarianty a přesné ceny |
| M, horní mez b²−1, tabulka a možnosti vynechat nulový násobitel | `classical-basic.md`, násobení a časování |
| Odhady A/B, normalizace, D3/D6 a celé D | `division.md`, `classical-division-exercises.md` |
| Úplný MIX D1–D8, znaménka, přenosy a cena všech větví | `classical-division-mix.md` |
| Komplementy, generující funkce(3)–(5), momenty(6)–(7) | `classical-carries.md` |
| Reciproční iterace a geometrická řada na279 | `classical-context.md`, přesná chyba e^r a zbytek řady |
| Historické implementace a rekordy | `classical-history.md`, `classical-context.md`, pouze jejich doložený rozsah |

Platí známé opravy dělení včetně roku2026. Rozdělení zbytků a přibližné
časy nejsou tvrzením o každém vstupu; přesné vzorce cen v archivu jsou
odlišeny od heuristických průměrů. Žádný nový nález ani výpočet.

Potvrzené vady: C0095 **low** (jeden cyklus v odpovědích3/8), C0096
**low** (triviální n1/2 v15), C0097 **medium** (chybný překryv M může
smazat vstup), C0099 **medium** (chybí dělení b v iteraci), C0100
**low** (dva koeficienty v pomocném BBP mezikroku; výsledná řada platí).
Závažnost nezaměňuje chybu pomocného výrazu za neplatnost hlavního výsledku.

## Co zůstává otevřené

C0098 zůstává **candidate/low**: argumenty20/21 platí při horním odhadu
q̂≥q, který D zachovává. Text může tuto podmínku přebírat kontextem;
pro libovolnou aproximaci neplatí. Obě úlohy proto nově evidujeme
`partial`, aby uzavřený podmíněný důkaz nezakrýval sporný rozsah zadání.
To není nová chyba algoritmuD a původní důkazy jsou zachovány.

Úloha40 nadále **partial**. Archivní hybrid zaručuje správný podíl a
asymptotickou75% úsporu, ale pro pevný malý základ dokazuje zbytek
O(n log n), nikoli tištěné O(n). Pro velký základ a výslovně omezený
rozsah n stačí pevný počet rezervních míst. Není to důkaz nemožnosti
silnějšího algoritmu; nedostupnou časopiseckou verzi nenahrazuje domněnka.

C0101 zůstává **candidate/low**, sporná Eulerova atribuce v dodatku2024,
nikoli nový rozpor BBP matematiky. Archivní příspěvek Ojangurena má
omezený rozsah; E706 nebyl dostupný.

Bibliografické výjimky, historické rychlosti a rekordy se přebírají
s přesnými limity z `classical-context.md`. Nepřečtené knihovny,
absolutní priority ani velké historické výpočty nejsou nově ověřeny.
Dopředné vazby na rychlé násobení/reciproční iteraci a hardwarové
dolní meze patří do§4.3.3.

Celá sekce se neprohlašuje za dokončenou:20/21/40 a atribuceC0101
zůstávají otevřené. Strany282/284/625/628/629 jsou proto partial;
630 také kvůli následující§4.3.2. Nový kurzor284/file296,§4.3.2.
