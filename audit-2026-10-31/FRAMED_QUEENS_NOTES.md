# Rámované dámy — úloha 7.2.2–7

Kontrola 1. listopadu 2026. Zadání na str. 55 a odpověď na str. 398
byly zobrazeny v původním PDF. **Nová chyba zatím nenalezena.** Úloha
zůstává částečná: doplňkový počet pro n = 27 se ještě počítá a formulaci
o všech n > 16 neoznačujeme za obecně dokázanou.

## Přesné zadání a malé případy

V nulovém indexování musí permutace q splnit

    q[0] = 1, q[1] = n−1, q[n−2] = 0, q[n−1] = n−2,

a každá dvojice dam musí být v různých sloupcích a na různých diagonálách.
Knižní sedmnáctidámový svědek byl již ověřen v
[základní kontrole](BACKTRACK_BASIC_NOTES.md). Nové úplné výčty dávají:

| n | Počet rámovaných řešení |
|---|---:|
| 4, 5 | po jednom |
| 6 až 16 | nula |
| 17 | 16 |
| 18 | 72 |
| 19 | 1 512 |
| 20 | 5 484 |
| 21 | 57 808 |
| 22 | 238 592 |

Jde o orientované desky se čtyřmi předepsanými damami, nikoli o třídy
vzhledem k symetriím. Dva algoritmy v [framed_queens.cpp](framed_queens.cpp)
projdou stejnou množinu různým způsobem:

- `rows` přidává řádky v pevném pořadí, používá posouvané diagonální
  bitové masky a předem vyloučí útoky všech pevných dam.
- `mrv` vybírá dosud neobsazený řádek s nejmenší doménou, používá absolutní
  součty a rozdíly souřadnic. Nepřebírá předpočítané útočné masky `rows`.

Oba výčty mají přesný 128bitový počet. Navíc se porovnává součet a XOR
64bitových otisků celých desek; otisky jsou doplňkovou kontrolou, nikoli
matematickým důkazem rovnosti množin. Pro n ≤ 22 program u **každého**
nalezeného výsledku přímo porovnává všechny dvojice dam i předepsaná pole.

## Rotační filtr a jeho přesné váhy

Čtyři pevné dámy se při čtvrtotáčce permutují mezi sebou. Zrcadlení tento
rám nezachová, proto se používá pouze grupa C4. Je-li p = q⁻¹, pak sloupce
třetího řádku ve čtyřech otočeních jsou

    q[2], n−1−p[2], n−1−q[n−3], p[n−3].

Pro pevné c = q[2] ponecháme desku, jen pokud c je minimum této čtveřice.
Tento test lze provést již omezením tří řádků/sloupců:

    q[n−3] ≤ n−1−c, p[2] ≤ n−1−c, p[n−3] ≥ c.

Je-li t počet výskytů minima ve čtveřici, má ponechaná deska váhu 4/t.
Tím se správně započtou i desky s vlastní rotační symetrií: má-li deska
stabilizátor velikosti s, její orbita má 4/s různých desek, z nichž filtr
ponechá t/s. Jejich celková váha je (t/s)(4/t) = 4/s.
Pouhé násobení čtyřmi by při shodných minimech správné nebylo.

Z počtů N₁, N₂, N₃, N₄ ponechaných desek podle multiplicity minima tedy
obnovíme celý počet jako

    (12 N₁ + 6 N₂ + 4 N₃ + 3 N₄) / 3.

Částečný součet jediného prefixu nemusí být dělitelný třemi. Runner proto
sčítá přesné čitatele a dělí až po dokončení všech částí.

## Rozsah dokončené kontroly

[check_framed_queens.py](check_framed_queens.py) dokončil kontrolu za
36,71 sekundy; [validation.json](results/framed_queens/validation.json)
obsahuje příkazy, verzi překladače, hashe zdroje a binárky a výsledky:

- Úplné výčty oběma metodami pro n = 4 až 22, shodné počty a otisky.
- Rotační filtr oběma metodami pro n = 8 až 22; přesně vážené součty
  se rovnají neomezeným počtům.
- Rozklad podle třetího a čtvrtého řádku pro n = 17, 18, 19; každá z
  74, 92 a 112 částí se shoduje oběma metodami a jejich součet odpovídá
  nerozdělenému výčtu.
- Další samostatný Python výčet s množinami místo bitových masek nalezl
  všechny desky pro n = 17 a 18. Explicitně sestrojené čtyři rotace
  potvrzují vzorec pro minimum i přesné racionální váhy 4/t.

Pro n = 27 běží [run_framed_queens.py](run_framed_queens.py), který dělí
výpočet na 344 přípustných dvojic sloupců třetího a čtvrtého řádku.
Každou část zpracuje oběma metodami a přijme pouze shodné dokončené
výsledky včetně rozdělení podle multiplicity minima. Stav je v
[large-n27-wrapper.json](results/framed_queens/large-n27-wrapper.json).
Limit je osm hodin na jednu metodu jedné části. Timeout znamená
nedokončenou část; nikdy nulu ani potvrzený knižní počet.
Po restartu se hotové části i samostatně hotové metody znovu nepřepočítávají.

Knižní údaj **34 651 355 392** není v této chvíli nezávisle potvrzen.
U velkého běhu se již nedělá kvadratická kontrola každé výsledné desky;
platnost zajišťují invarianty dvou prohledávání. Přímá kontrola všech dvojic
byla provedena pro výše uvedený menší rozsah.

## Historická citace a status obecného tvrzení

Stažen byl [Spragueův původní článek](sources/framed_queens/sprague-1890-nonlinear-arrangements.pdf),
*On the different possible non-linear arrangements of eight men on a
chess-board*, Proc. Edinburgh Math. Soc. 8, str. 30–43,
[DOI 10.1017/S0013091500030522](https://doi.org/10.1017/S0013091500030522).
Na [str. 43](sources/framed_queens/sprague-1890-page-14.png) autor skutečně
vyslovuje domněnku nemožnosti rámovaného rozmístění a výslovně přiznává,
že ji nedokázal. Knižní svědek n = 17 ji vyvrací.

Obrázky nejsou v samostatném článkovém PDF. Jsou v oddělené
[obrazové příloze svazku](sources/framed_queens/pems-v8-backmatter.pdf),
jejíž PDF strana 20 obsahuje [obr. 50–53](sources/framed_queens/sprague-1890-figures-50-53.png).
Obrázek 52 byl zobrazen a má přesně předepsané čtyři krajní dámy.
Tím je ověřen obsah i lokalizace knižní historické citace.
Nápis na první straně článku datuje schůzi 14. března 1890; titulní list
svazku uvádí ročník 1889–90. Odlišné katalogové označení „February 1889“
na webu proto není důvodem označit knižní rok 1890 za chybu.

Pro obecný status je relevantní práce Glocka, Munhy Correii a Sudakova,
[The n-queens completion problem (2022)](https://doi.org/10.1007/s40687-022-00335-1).
Jejich věta 1.2 zaručuje doplnitelnost libovolných nejvýše n/60 vzájemně
se nenapadajících dam **pro všechna dostatečně velká n**. Z toho plyne
existence rámovaných řešení pro všechna dostatečně velká n. Samotné
n ≥ 240 nestačí k použití věty: stále je nutný její nespecifikovaný
asymptotický práh. Tato věta ani zdejší výčty neprokazují přesný práh 17.

Při rešerši 1. listopadu 2026 nebyl nalezen pramen dokazující přesně
existenci pro každé n > 16. Hledány byly fráze „framed queens“, Sprague,
číselné podposloupnosti a přesný údaj pro n = 27. Neúspěch tohoto hledání
není dokladem, že takový důkaz neexistuje. Knižní „almost surely“ zde
chápeme jako opatrné vyjádření očekávaného obecného výsledku, nikoli
jako doložený teorém s prahem 17.

Repozitář [Preußerova projektu q27](https://github.com/preusser/q27)
dokládá celkový výčet 27 dam, ale dohledaná stránka sama neuvádí rámovaný
mezisoučet. Odkazované podrobné webové protokoly se při přístupu nezdařilo
načíst. Proto je zde připraven vlastní přepočet a údaj se zatím vede jako
otevřená kontrola, nikoli jako chyba.
