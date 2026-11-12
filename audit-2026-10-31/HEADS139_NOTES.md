# DLX139 — devět dlaždic s hlavami a ocasy

Kontrola 2. listopadu 2026. Zadání je na tištěné straně 140 (PDF160),
odpověď na straně 453 (PDF473). Zobrazen původní svazek 4B i autorův
draft z roku 2019, odpověď na straně 157 (PDF163).

**Matematická část souhlasí v celém rozsahu.** Celou úlohu zatím vedeme
jako `partial`, protože historické údaje o Haubrichově sbírce nemáme
ověřené v původním prameni. Nevznikl nový nález ani kandidát na chybu.

## Přesné vymezení symetrií

Každá dlaždice obsahuje čtyři různé barvy, dvě sousední hlavy a dva
sousední ocasy. Po otočení má jediný zápis `HHtt`, čtený od severu
proti směru hodinových ručiček (N,W,S,E). Existuje právě 24 typů,
odpovídajících permutacím barev. Do hry se vybírá devět různých typů.

Při porovnání **sad** dovoluje odpověď 139 výslovně přejmenování všech
čtyř barev, odraz všech dlaždic a globální výměnu hlav s ocasy. Tyto
operace tvoří grupu velikosti 4! × 2 × 2 = 96. Program kontroluje
všech 9216 složení jejích permutací na 24 typech.

Při počítání **řešení jedné pevné sady** se jednotlivé dlaždice smějí
otáčet, nikoli obracet. Celá čtvercová sestava se počítá jen jednou
ze čtyř otočení. Jednoznačný reprezentant má hlavy prostřední dlaždice
na severu a západě. Tato normalizace je volná: středová dlaždice má
čtyři různé barvy, takže žádné netriviální otočení celou sestavu nezachová.

Barevné permutace, odrazy a výměna polarity dávají bijekce mezi řešeními
ekvivalentních sad. Proto stačí spočítat každý reprezentant sady jednou.
Všechny čtyři lokální orientace jsou v obou řešičích povolené; odraz
samotné dlaždice povolený není. Vnější obvod nemá další omezení.

## Část (a): úplný cenzus sad

Výčet pokryl všech **1 307 504 = C(24,9)** výběrů. Každý patří právě
do jedné z **14 124** orbit. Výsledek nezávisle potvrzuje Burnsideovo
lemma: pro každou permutaci se počet pevných devític získá jako
koeficient x⁹ v součinu faktorů (1+x^d) přes délky jejích cyklů.

| Velikost stabilizátoru | Velikost orbity | Počet tříd |
|---:|---:|---:|
| 1 | 96 | 13 157 |
| 2 | 48 | 882 |
| 3 | 32 | 7 |
| 4 | 24 | 78 |

Vážený součet velikostí je přesně 1 307 504. Pouhé přejmenování barev
dává **54 498 tříd**. Tento počet byl získán dvěma způsoby: rozkladem
každé plné orbity na orbity S4 a samostatným Burnsideovým součtem pro S4.
Ověření čísla není dokladem historického prvenství jeho autora.

## Část (b): všechny počty řešení

Na každé ze 14 124 reprezentativních sad byl spuštěn původní Knuthův
DLX2. Matice má 18 primárních položek (devět polí a devět typů),
12 sekundárních položek pro vnitřní hrany a 297 možností:
8 × 9 × 4 + 9 pro orientaci středu. Změna polarity na jižní a východní
hraně převede doplňování hlavy a ocasu na rovnost barvy v Algorithm C.

Nezávislý C++ program používá přímý řádkový výčet s geometrickými
podmínkami. Pracuje s celočíselnými podepsanými hranami ve směru
hodinových ručiček, bez exact cover a bez Pythonových možností DLX.
Oba výčty dokončily všechny případy. Uložena je **celá stejná množina
11 431 řešení**, rozdělená podle sady; shoda se kontroluje i pro všechny
neřešitelné sady. Každá sestava je navíc přímo zkontrolována po hranách.

| Počet řešení k | Počet tříd |
|---:|---:|
| 0 | 9666 |
| 1 | 1883 |
| 2 | 1051 |
| 3 | 537 |
| 4 | 380 |
| 5 | 213 |
| 6 | 147 |
| 7 | 68 |
| 8 | 60 |
| 9 | 27 |
| 10 | 29 |
| 11 | 9 |
| 12 | 24 |
| 13 | 4 |
| 14 | 8 |
| 15 | 2 |
| 16 | 5 |
| 17 | 4 |
| 18–23 | po jedné třídě |
| 24–26 | žádná |
| 27 | jedna |

Celý histogram je přesně stejný jako v knize. Žádná sada nemá více
než 27 řešení. Raw vstupy, výstupy a terminální logy všech 14 124
DLX případů jsou v jednom archivu `native/cases.tar.gz`; samostatná
metadata mají kontrolní součet každého členu. Nezávislý výčet uchovává
celý stdout, terminál, zdroj a hash binárky. Opakování hledání není třeba.

## Původní obrázky

Z PDF vektorů byly získány a ověřeny všechny **108 podepsané hrany**:
devět dlaždic sady (*) a dvě čtvercové sestavy po devíti dlaždicích.
Barvy A/B/C/D znamenají zelenou/modrou/bílou/červenou. Směr trojúhelníku
rozlišuje hlavu a ocas, takže se nekontrolují pouze barvy.

Sada (*) je skutečně jediná třída s 27 řešeními a má 96 různých
ekvivalentních sad. Oba další obrázky jsou platná jedinečná řešení.
Jsou to přesně ty **dvě** jedinečně řešitelné třídy, jejichž stabilizátor
má čtyři prvky. U obou jsou explicitně ověřeny všechny kombinace
odrazu a výměny polarity s odpovídajícím přejmenováním barev; po otočení
zpět na normovaný střed vracejí přesně původní sestavu.

## Errata a historické mezery

Prohledáno šest vrstev aktuálních a historických errat 4B a Fascicle 5,
včetně TeXu, s mapováním stránek 140/453 ↔ 138/261 ↔ 76/157 v draftu.
Použita předchozí přímá kontrola čtyř oficiálních souborů z dnešních
15:22 UTC; jejich lokální hashe zůstávají stejné. Nové stahování se zde
neprovádělo. V relevantních položkách nebyla nalezena oprava této úlohy.

Jeden textový zásah `exercise 139` v TeXu Fascicle 5 není o této hře:
má lokaci 4f5.161 a opravuje tři diaboly, tedy obsah dnešní úlohy **319**
na straně 163. Záměna čísla v tomto štítku nesmí přiřadit cizí opravu
k HHtt139. Ostatní tři zásahy se týkají úlohy121 na straně138 ve4B.
Kontexty i porovnání jsou uložené.

Autorův draft uvádí stejné matematické počty i historické věty.
[Kadon](https://www.gamepuzzles.com/moredge.htm) a
[katalog PuzzleWorld](https://puzzleworld.org/PuzzleWorld/books/books.htm)
uvádějí Haubrichův doplněk z roku 1996 *About, Beyond and Behind Card
Matching Puzzles*. Jsou to bibliografické stopy, nikoli původní rozbor.
Konkrétní dotaz do katalogu Internet Archive vrátil nula záznamů;
to není důkaz obecné nedostupnosti knihy.

Neověřené zůstává prvenství řešení v roce1996, údaj o435 sebraných
nerovnocenných hrách a17 čistých sadách a Hoek Loos1974 jako první
takový exemplář sbírky. Chybí obsah původního rozboru a datovaný
sbírkový předmět či návod. Nikomu nebyla poslána zpráva.

## Doklady a navázání

- [Přijaté výsledky](results/heads139/accepted.json)
- [Orbity a Burnside](results/heads139/groups-checked.json)
- [Úplná shoda řešení a automorfismy](results/heads139/counts-checked.json)
- [108 hran originálu](results/heads139/figures-checked.json)
- [Errata](results/heads139/errata-check.json) a [historické zdroje](results/heads139/source-status.json)
- [Původní strana453](images/vol4b-p453.png) a [autorův draft157](images/fasc5c-p157-heads139.png)

Další sekvenční úloha je140. Historické mezery139 zůstávají explicitně
otevřené; audit celého svazku zdaleka není dokončen.
