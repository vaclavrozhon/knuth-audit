# Errata pro §2.3.4 a §2.3.4.1

Kontrola 1. 11. 2026: všechny čtyři textové vrstvy
`errata/text/{all1-prepre,all1-pre,all1,err1}.txt` byly prohledány podle stran
362–371, 578–580 i podle věcí a jmen: free tree, subtree, path/walk, Kirchhoff,
spanning tree, Prim, Jarník, Dijkstra, Nahapetian, Stevenson, GraphBase a tabulky
a(i), b(i). Aktuálnost stažených vrstev ověřil kořen této relace; nové stažení
se shodovalo s uloženými soubory. Tato poznámka nezaměňuje obsah poslední krátké
vrstvy za úplná errata prvního dotisku.

Relevantní původní obrazy PDF byly zobrazeny a jsou uloženy v `../images/`:

| Vrstva | Strany souboru PDF |
|---|---|
| all1-prepre | 24, 25, 43 |
| all1-pre | 12, 17 |
| all1 | 9, 15 |
| err1 | 8, 13 |

Následující přehled obsahuje všechny nalezené opravy uvnitř přiděleného rozsahu.
Jde o známá errata, nikoli nové nálezy.

| Místo v knize | Datum opravy | Vrstva | Obsah a posouzení |
|---|---|---|---|
| 363, definice v úvodu §2.3.4.1 | 25 Jul 2008 | all1-prepre 24 | Rozlišení walk/path/cycle; všechny vrcholy cesty různé. Terminologie, správné. |
| 368, ř. −21, −7, −2 | 25 Jul 2008 | all1-prepre 24 | path → walk. Nutné pro sledy s opakováním. |
| 369, ř. 9, −14, −12 | 25 Jul 2008 | all1-prepre 24 | path → walk. Totéž. |
| 364, ř. 6 | 02 Sep 1997 | all1-prepre 24 | Vyznačení hrany mezi V_(k−1) a V_k spojovací čarou. |
| 364, ř. 14 | 02 Sep 1997 | all1-prepre 24 | Libovolný počáteční vrchol nahrazen existencí vhodného; odstraňuje možnost izolovaného vrcholu v důkazu listu. |
| 364, ř. 18, 20 | 01 Jun 2006 | all1-prepre 24 | tree → free tree. |
| 366, ř. 1 pod popiskem obr. 32 | 01 Jun 2006 | all1-prepre 24 | subtree → free subtree. |
| 367, ř. −2 | 14 May 1999 | all1-prepre 24 | e_j → E_j při popisu koeficientů rovnic. |
| 370, ř. −16, redukovaný obrázek úlohy 8 | 22 Jun 2004 | all1-prepre 24 | Nový obrázek má s:Start→U, t:U→Start, b:U→C, c:C→U, smyčky a,d v U. Souhlasí s obecným důkazem redukce. |
| 371, úloha 10 ř. 4 | 02 Dec 1998 | all1-prepre 25 | to that → so that. |
| 578, ř. 4, 5 (odpověď 2) | 25 Jul 2008 | all1-prepre 25, souhrnné erratum od s. 374 | path → walk při výběru nejkratšího sledu. |
| 579, odpověď 8 ř. −2 | 21 Aug 2001 | all1-prepre 43 | Přidána Nahapetianova práce Acta Informatica 3 (1973), 37–41. |
| 579, odpověď 11 ř. 4 | 14 Feb 1999 | all1-prepre 43 | Přesun čárky do uvozovek u common. |
| 580, odpověď 13 ř. 3, 6 | 23 Oct 2006 | all1-prepre 43 | tree → free tree. |
| 364, horní část důkazu | 20 Jan 2020 | all1-pre 12 | Explicitně rozdílné délky s,t dvou cest, společné krajní vrcholy a přesně napsaná obchozí cesta. Důkaz je po změně správný. |
| 578, poslední řádek odpovědi 6 | 11 Nov 2021 | all1-pre 17 | Křížový odkaz 7.4.1 → 7.4.1.2. |
| 579, odpověď 8 ř. −8 | 18 Jul 2021 | all1-pre 17 | Jednotkový tok v e0 není třeba měřit. Vysvětluje rozdíl dimenze prostoru a počtu měření při pevném e0=1. |
| 371, úloha 11 ř. 1 | 17 Nov 2023 | all1 9; err1 8 | Smazán původní úvodní odkaz pouze na Prima. Nahrazen odkazy v odpovědi. |
| 371, úloha 11 ř. −4 | 07 Jul 2023 | all1 9 | minimal cost tree → minimum cost tree. |
| 579, nový odstavec na konci odpovědi 11 | 17 Nov 2023 | all1 15; err1 13 | Odkazy Jarník, Acta Societatis Scientiarum Naturalium Moravicae 6 (1930), 57–61; Prim, Bell System Technical Journal 36 (1957), 1389–1401. Oba primární texty získány; stav čtení v `sources.md`. |

Pro §2.3.4 samotný na s. 362–363 nebyla nalezena zvláštní oprava. Indexové
změny po přidání Jarníka/změně Primova odkazu pouze sledují výše uvedené
přesuny; vlastní audit celého rejstříku do tohoto bloku nepatří.

Žádná vrstva neopravuje opětovné nastavení konečné hodnoty a(j) již vybraného
vrcholu v prvním algoritmu odpovědi 12. Oprava odpovědi 13 na téže s. 580 ani
změny citací úlohy 11 tento problém neřeší. Přesný samostatný podklad je
`prim-answer12.md`; při jeho předání byly příslušné obrazy errat zmrazeny.
