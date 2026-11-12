# §1.3–1.3.1: inventář, errata a zbylé otázky

Kontrola1.11.2026, první dotisk třetího vydání. Zobrazeny originály
s.124–144 a507–510 (strany souboru o15 vyšší). Je přesně26 úloh,
s hodnoceními:

```
1:00  2:02  3:02  4:00  5:10  6:10  7:M15  8:15
9:15 10:15 11:15 12:10 13:10 14:20 15:10 16:20
17:26 18:22 19:14 20:20 21:24 22:28 23:27 24:21 25:30 26:32
```

Nová cvičení v dostupných erratech nejsou. Doplněná odpověď23
zroku2018 je opravou stávající úlohy, nikoli novou úlohou.

| Rozsah | Doložený výsledek |
|---|---|
| Definice a všechny skupiny instrukcí | [mix-semantics.md](mix-semantics.md), algebraické vysvětlení a kontrola tabulek |
| Úlohy1–15 | Přesné odpovědi a zdůvodnění v témže souboru |
| Úlohy16–25 | [mix-programs.md](mix-programs.md), obecné invarianty a přesné časy |
| Úloha26 | [mix-loader.md](mix-loader.md), důkaz synchronizace, formátu, znamének a přenositelnosti |
| Reprodukce | `mix_machine.py`, `check_mix_description.py`, `results/mix-description.json`:4323 úspěšných kontrol |

Z 26 úloh je nyní 21 `checked`; 16,17,22,23,24 jsou `partial` pro
neuzavřené globální dolní meze optimality. Revize X0669 uzavřela
všechny konkrétní odkazy úlohy 25; X0670 uzavřela prostorové
minimum 24(a). Správnost uvedených programů v těchto položkách
otevřená není; u 24 zbývá časové minimum části (b).
Hlavní popis zůstává `partial` pro níže uvedenou časovou nejasnost
a vymezenou historickou kontrolu. Úvod §1.3 má ověřený autorský
záměr a specifikaci MMIX; předpověď budoucích vydání se nehodnotí
jako tvrzení, že konverze už byla dokončena.

## Errata

Prohledány všechny čtyři textové řady `all1-prepre`, `all1-pre`,
`all1`, `err1` i zdrojový `err1.textxt`, podle stran i názvů operací.
Výpis40 záznamů v `sources/mix-description-errata-extract.json`
obsahuje duplicity mezi řadami a konec předchozí sekce na s.507;
nejde tedy o40 různých oprav MIXu. Zobrazeny PDF obrazy:
`all1-prepre`12,13,36,37; `all1-pre`11,16; `all1`7.

Podstatné opravy:

- Fig.13, s.126: správné rozdělení zařízení až do U20,15.7.1998.
- S.131: desetibajtový dělenec rAX v obou vzorcích,28.9.1997.
- MOVE: výchozí F=1 doplněno24.1.2003; již bylo správně v tabulce1.
- S.138: čas plovoucích operací odkazuje do §4.2.1,11.10.1998.
- Odpověď14: tři způsoby no-op pro STJ/STZ,25.3.2003.
- Odpověď22: čas54u nezahrnuje HLT,28.9.1997; krajní hodnoty
  tabulky ±5^13 jen pro b>65,17.11.2007.
- Odpověď23: dodatek George Wahida s explicitním A>=0,28.2.2018.
- Odpověď26: dva chybné znaky na štítcích,30.12.1997 a21.11.1998;
  GO maže overflow,29.11.2011; cílová adresa >=0100,3.11.2022.
- Vyjasnění „42 instrukcí“ z18.8.2010 dále zpřesněno20.12.2023
  na instrukce pro X a indexy. Opravdu 7registrů krát6 podmínek.
- Úloha18 v2023 výslovně zahrnuje i další aspekty stavu počítače.

Dále zkontrolovány drobné typografické, interpunkční a slovní opravy
na s.125,130,131,133,134,135,138,139,142–144,507–509. Nemění
výše uvedené invarianty. OCR záměna i/I u kódu INCi byla ověřena
proti sazbě errat, není novým aritmetickým problémem.

## V1-C0020: údaj o čase HLT v tabulce1 — candidate

S.138 říká, že HLT zabere1u plus dobu zastavení. V tabulce1 na
s.141 má celá buňka pro C=05 jediný čas10 a vypisuje NUM,CHAR,HLT.
NUM a CHAR opravdu potřebují10u, ale HLT má podle souvislého
popisu čas1u plus čekání. Zobrazeny obě původní stránky; oprava
pro tabulku ani HLT v prověřených vrstvách nenalezena.

Možná oprava: u HLT výslovně uvést1+T, kde T znamená dobu čekání,
nebo poznámku, že10 platí jen pro NUM/CHAR. Zatím jde o drobnou
**nejasnost souhrnné tabulky**, nikoli nový potvrzený nález: také
plovoucí varianty sdílejí tabulkovou hlavičku s jinou běžnou cenou,
takže t může být zamýšleno jako zkratka pro hlavní varianty.
Před případným hlášením vyjasnit tuto konvenci. Náš model používá
výslovné pravidlo s.138; všechny srovnávané časy beztak vynechávají HLT.

## Historické pasáže a odkazy

- Knuthova vlastní stránka [MMIX](https://www-cs-faculty.stanford.edu/~knuth/mmix.html)
  byla získána přímo a přečten úvod, srovnání s MixMasterem a popis
  64bitové architektury. Potvrzuje účel i číslování2009. Autorův
  tehdejší plán budoucí konverze se nezaměňuje s jejím dnešním stavem.
  Uloženy HTML, text a metadata skutečného rozsahu čtení.
- Wordsworthův citát na s.139 souhlasí se dvěma řádky básně v
  [přepisu sbírky1807](https://www.gutenberg.org/cache/epub/8774/pg8774-images.html).
  Knightova edice1896,svazek3, uvádí nad básní „Composed1804,
  Published1807“ a přetiskuje autorovu vzpomínku. Příslušná báseň,
  úvod a poznámky byly přečteny. Jde o doložení běžného datování,
  ne nezávislé ověření rukopisu. Archiv Wordsworth Trust současně
  eviduje rané texty DCMS38.17 a DCMS44.77; přesná chronologie
  verzí nebyla rekonstruována a z rozdílného datování se zde
  nevyvozuje nová chyba. Přepis básně není vydáván za zobrazený sken.
- Odkazy odpovědi 25 do §2.2.2, §1.4.4 a svazků 2–4 jsou nyní
  jednotlivě přímo ověřeny v X0669. Přesné cíle 2.2.2-3–5,
  1.4.4-18, 2.5-28, 5.2.2-12, 6.3-9, 4.5.2B, 6.4-(24) a 7.1
  i mapy stran jsou v `mix-crossrefs-and-space.md`.
- Není hotový nezávislý historický průzkum všech16 modelových názvů
  na s.124 ani standardizace slova „byte“ kolem1975. Výpočet průměru
  je ověřen; autorův přehled není vydáván za přečtení16 manuálů.

## Pomocný Markdown

`md/vol1/18-1.3.1-description-of-mix.md` se na rozdíl od předchozí
asymptotické sekce drží původních otázek, ale ztratil téměř všechny
graficky sázené registry, tabulky a celý program úlohy18. Není
použitelný pro nezávislou rekonstrukci instrukcí. Hodnocení7 je
**M15**, nikoli OCR `MJ5`. Nerovnosti v adresách, indexech, úloze17
a formátu druhého slova karty mají být neostré tam, kde OCR píše `<`
nebo `>`. Písmena O, číslice0 a I/1 jsou opakovaně zaměněna.
Sdílené soubory nebyly měněny; doklady a oprava inventáře jsou vlastní.

Celý svazek zůstává aktivní. Po uložení tohoto bloku pokračuje
§1.3.2: MIXAL, prvočísla, podprogram maximum a další programy.
