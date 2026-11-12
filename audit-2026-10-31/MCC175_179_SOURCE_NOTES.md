# Úplný průchod MCC úlohami 175–179

Kontrola 3. listopadu 2026. Zadání 4B str. 146–147, odpovědi str. 467;
autorův draft Fascicle 5c str. 82–83 a 171. Knižní PDF má posun +20,
draft +6. Původní stránky byly zobrazeny; OCR slouží jen k navigaci.

Úlohy 177–179 jsou zrevidované. 175–176 zůstávají částečné kvůli
otevřené otázce nulových řádků [C037](C037_ZERO_ROWS.md). Dříve přijaté
výsledky v nenulové doméně zůstávají platné. Nová potvrzená chyba nevznikla:
F070 je již evidovaný chybný index v rekurenci 177(b).

## Co se počítalo a co se neopakovalo

`check_mcc175_179_sources.py` dekóduje 82 číslic matic 179 z každé ze dvou
verzí a porovnává je. Kontrola všech 512 + 128 podmnožin dává sedm původních
a tři zredukovaná pokrytí. Šest nových drobných vstupů DLX3 zkoumá jen
hranici nulových řádků. První nástrojový proces včetně těchto šesti běhů
trval 0,364 s; jednotlivé časy nebyly uloženy, jsou výslovně `null`.
Pozdější chyba reportovací aserce vedla pouze k opětovnému načtení hotových
výstupů, nikoli k novému hledání; viz `results/mcc175_179/development-notes.txt`.

Z `results/mcc_arithmetic/arithmetic.json` se přebírají, bez dalšího běhu:
52 případů opakování, 160 matic s nenulovými řádky, 72 koeficientových
kontrol a oba výčty rozkladů 360. Zdrojový program ani přijaté výsledky
se nemění. Všechny nové výpočty a renderování mají `nice 15`.

**Výslovně nereplikováno:** údaj asi 1300 mems na řešení a přibližně
sedminásobné zpomalení proti specializovanému algoritmu 7.2.1.5M v 177(a).
K dispozici jsou správné rozměry převodu a nezávisle přijaté přesné počty,
nikoli nové měření těchto historických rychlostí. Pokyn uživatele dovoluje
vynechat dlouhou reprodukci; v registru je `verified: false`.

## 175: jednoznačné opakování možnosti

Pomocná primární položka # vynutí právě jednu volbu v každém článku
řetězce. Označíme-li zvolenou kopii původní možnosti jedničkou a prázdnou
alternativu nulou, sekundární x zakáže přechod 1→0. Přípustné volby jsou
právě monotónní slova 0…01…1; pro každou násobnost od nuly do předepsané
meze existuje jediné rozšíření. Počet pomocných položek i možností souhlasí.

Neobarvené původní sekundární položky dostanou novou barvu specifickou
pro původní možnost: její kopie se snášejí, výskyt v jiné původní možnosti
zůstává neslučitelný. Již obarvené položky si zachovají původní barvy.
Při horní mezi nula lze původní možnost odstranit.

Pro nulový řádek není původní možnost legálním vstupem MCC. Jeho volby
je potřeba doplnit zvlášť nebo přidat pomocnou primární položku s dolní
mezí nula. Kniha tento krok nevyslovuje; kvůli možnému implicitnímu
předpokladu z definice MCC vedeme pouze kandidáta C037.

## 176: převod hodnot 0, 1, 2

Pro cílový součet T položme h = floor(T/2). Primární A má násobnost T,
B násobnost h a h pomocných položek # násobnost jedna. Přidané možnosti
tvoří monotónní slovo A^u B^(h−u); sekundární položky zakazují sousední BA.
Obsahují-li vybrané původní řádky p jedniček a q dvojek, rovnice jsou

```
p + q + u = T,
q + (h − u) = h.
```

Tedy u = q a p + 2q = T. Rozšíření je jediné a přípustné právě pro
požadovaný součet. To dokazuje všechny čtyři případy T = 2, 3, 4, 11;
souhlasí rozměry 3N, 3N, 4N, 7N primárních a 0, 0, N, 4N sekundárních
položek i všechny vypsané koncové články řetězce. Ukázkový řádek
(2,1,0,2,0,…) správně dává `A1 B1 A2 A4 B4`.

Omezení na nenulové původní řádky a jeho snadná oprava jsou stejné jako
v 175. Nulový řádek znamená nezávislou volbu zahrnout/nezahrnout, kterou
doslovný vstup MCC neuchovává. Viz C037 a šest uložených minipříkladů.

## 177: počty, rekurence a známé F070

Nenulových vektorů bloků je 2^s 3^t − 1. Opakovat se smějí právě
2^t − 1 nenulových vektorů s nulovými jedničkovými souřadnicemi a
s dvojkovými souřadnicemi v {0,1}. Ve vykreslených PDF i PS je znak
`b_i ≠ 2` správný; OCR vynechává lomítko. Nejde o další chybu.

Převod 176 přidá 2t možností a používá s + 3t primárních položek.
Každý opakovatelný řádek dá podle 175 navíc jednu primární, jednu
sekundární a dvě možnosti. Všechny tři rozměry v části (a) a oba
v části (b) jsou správné. Vektory jsou výslovně nenulové, takže
otevřený okrajový případ 175–176 se sem nepřenáší.

Pro Q odlišíme dvě nové kopie jako x a y a poté je prohodíme.
Pevné rozklady mají buď x,y ve stejném bloku, což dává Q(s+1,t),
nebo ve dvou blocích se shodnými zbytky. Druhých je
R = sum(k=0..t) binom(t,k) Q(s,k). Burnside dává
(Q(s+2,t) + Q(s+1,t) + R)/2 orbit. Právě R z nich po ztotožnění x,y
obsahuje zakázané stejné bloky, takže se odečtou a získáme

```
2 Q(s,t+1) = Q(s+2,t) + Q(s+1,t) − sum(k=0..t) binom(t,k) Q(s,k).
```

F070 opravuje n v horním indexu na t. Nejkratší číselná ilustrace
z již přijaté tabulky: s=0, t=1 dává 10 = 9+3−1−1; libovolná volba
n=2 by dala pravou stranu 9. Pro P je znaménko plus. P(5,5)=91 914 202
a Q(5,5)=75 114 998 jsou již nezávisle ověřené, bez opakování výpočtu.

Křížový odkaz 4A, odpověď 7.2.1.5–73, tištěná str. 779, byl zobrazen
ve skutečné straně DjVu 796. Tam je původní označení m,n konzistentní.
V 4B se mění na s,t, ale horní index binomu zůstal n. Toto je doklad
odkazu, nikoli uzavření úlohy v samostatném auditu 4A.

## 178: 360 a původní Wallis

360 = 2³3²5 má 23 netriviálních dělitelů. Šest výplňových možností
dává 29 možností, 9 primárních a jednu sekundární položku. Gadget pro
exponent tři má tři přípustné dvojice výplní: AA, AC a BC; dvojice BA
je zakázána společným x. Původní exponenty tím musí být postupně
3, 2+1 a 1+1+1. Násobnosti (3,1,1,1,1) i konstrukce jsou správné.

Faktory 3 a 6 se mohou opakovat dvakrát, faktor 2 třikrát. Přidání
2+2+4 možností, 1+1+2 primárních a 1+1+2 sekundárních položek dává
37 možností a 13+5 položek. Přijaté nezávislé počty jsou 34 různých
faktorizací a 52 s opakováním.

Byl zobrazen křížový odkaz 4A 7.2.1.7–28, str. 513 a 816 (skutečné
DjVu str. 530 a 833). Primární digitalizát ETH/e-rara obsahuje
Wallisův *A discourse of combinations, alternations, and aliquot parts*,
London 1685. Titul je na PDF str. 2; tištěné str. 125–127 (PDF 20–22)
obsahují dělitele a rozklady 360, výslovný počet 52 a symbolické a³b²c.
Str. 128 (PDF 23) přechází na 110880. Relevantní připsání v knize
je doloženo originálem; absolutní historické prvenství tím nedokazujeme.

- [Katalog ETH/e-rara](https://www.e-rara.ch/zut/content/titleinfo/2507537)
- [Samostatná část v PDF](https://www.e-rara.ch/download/pdf/2573825.pdf)
- DOI: 10.3931/e-rara-8842

Soubor, čas získání a SHA256 jsou v `sources/mcc175_179/wallis-download.json`.
OCR historického písma se nepoužilo jako matematický důkaz. Kontrola
všech tiskových chyb Wallisovy tabulky ani samostatných úloh 4A není
součástí tohoto bloku.

## 179: redukce opakovaných řádků a sloupců

Shodné sloupce jsou redundantní rovnice. Shodné nenulové řádky nelze
v jednom přesném pokrytí použít současně; z každé vybrané třídy stačí
nezávisle zvolit jeden původní řádek. Zachované sloupce jsou 1,2,3,5
a třídy původních řádků {1},{2,4},{3},{5,6},{7},{8},{9} (indexy od 1).

Tři redukovaná pokrytí používají řádky {1,2,4}, {4,7}, {5,6}.
Jejich počty rozšíření jsou 4,2,1; součet sedm. Všechna se přesně
shodují s odpovědí v obou zdrojích. Úplné malé výčty jsou uložené
v `results/mcc175_179/source-checked.json`.

## Errata a stav vydání

Prohledáno šest vrstev: all4b, err4b, all4f5, err4f5 a oba zdrojové
TeXy. Hashované výsledky a kontexty jsou v `results/mcc175_179/errata-check.json`
a `sources/mcc175_179/errata-search-context.txt`. Stejnodenní kontrola
aktuálního 4B archivu je převzata z `results/snakes172/errata-check.json`.

| Záznam | Publikovaná změna | Naše knižní PDF | Autorův draft |
|---|---|---|---|
| E087 | 27. 3. 2024: a→r v 175 a rating M21→M22 | nezapracováno | nezapracováno |
| E088 | 11. 7. 2022: mezera mezi #j a Bj v 176 | zapracováno | nezapracováno |
| E089 | 17. 11. 2021: rozdělení zadání 177 na (a),(b) | zapracováno | nezapracováno |

E088 je vidět i z poloh vektorových znaků: vzdálenost začátků # a B
v příslušné možnosti je 14,538 pt v PDF a 11,667 pt v draftu, rozdíl
2,871 pt. Kontrolní vzdálenost #–A je v obou asi 14,61 pt. Publikované
TeXové erratum výslovně odděluje dvě matematické skupiny mezerou.

Pro F070 ani pro C037 nebyla nalezena odpovídající publikovaná oprava.
Poznámka `2's -> 2s` na konci err4b.textxt je interní redakční seznam,
nikoli publikované erratum. Tištěný exemplář 4B stále neověřen.
