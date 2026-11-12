# §1.3.3: prameny a známá errata

Stav k 1. 11. 2026. Tato poznámka přesně odděluje matematické ověření
od přečtení citovaných pramenů. Matematické výsledky jsou v
`basic-proofs.md` a `longest-cycle.md`; jediný nový potvrzený nález je
v `arbitrary-function-expectation.md`. Historický odstavec na s. 182
a bibliografický dovětek odpovědi 23 nejsou označeny jako úplně ověřené.

## Kniha a čtyři vrstvy errat

Autoritativní knižní podklad: `books/taocp-vol1-ed3-print1-1997.djvu`,
třetí vydání, první tisk z května 1997, SHA-256
`e2c5ee120bad91e33f617614b846849c4801115b2e7aa820f56fc5ffb9bbebb9`.
Číslo obrazové strany DjVu je tištěné číslo plus 15. Přečteny obrazy
s. 179–184 a 524–526 v přiděleném rozsahu; předchozí konvence střední
hodnoty byly přečteny v OCR na s. 98–104 a vizuálně na s. 103–104.
Algoritmus kanonického převodu a jeho tabulky mají jiného vlastníka.
Fyzický exemplář nebyl kontrolován.

Podle stran i tematických slov byly prohledány všechny čtyři texty
`errata/text/{all1-prepre,all1-pre,all1,err1}.txt`. Relevantní původní
strany errat byly porovnány vizuálně; obrazy jsou v `../images/`:
all1-prepre strany 15, 16, 38; all1 strany 8, 14; err1 strany 7, 12.
Vrstva all1-pre neobsahuje opravu přiděleného rozsahu. Aktuálnost
stažených vrstev zkontroloval koordinátor 1. 11. 2026.

| Knižní místo | Datum známé opravy | Obsah |
| --- | --- | --- |
| 178, kanonický zápis | 24. 12. 2001 | Mezera před `(1 6 3)(4 5)`. |
| 181, (25) | 23. 12. 2024 | Index n místo m a zápis alternující řady. |
| 182, historie | 17. 3. 1998 | De Moivre → de Moivre. |
| 182, historie | 18. 9. 2002 | Doplnění Todhuntera, Algebra, 2. vydání 1860, §762. |
| 182, historie | 29. 3. 2023 | Chelsea 1957 → 1967. |
| 183, cv. 22 | 9. 9. 1998 | Interpunkce v zápisu P(n; k_1, k_2, …). |
| 183, cv. 22(c) | 29. 3. 2023 | Příklad φ_n=1 jen pro n≥1. |
| 524, odp. 17 | 24. 12. 2001 | Závorky v jmenovateli mH_n. |
| 524, odp. 17 | 26. 2. 2008 | Symbol p_m. |
| 524, odp. 19 | 15. 9. 1999 | Chybějící faktor n! na třech místech. |
| 524, odp. 21 | 10. 4. 2023 | Doplnění odkazu na odpověď 1.2.5-21. |
| 524, odp. 22 | 1. 1. 2006 | j≥0 → j>0 ve čtyřech součinech. |
| 525, odp. 23 | 4. 11. 2003 | `[to appear]` nahrazeno Gourdonovou disertací, 1996. |
| 525, odp. 23 | 10. 11. 2022 | Poslední odkaz: strana 373 → 343. |

Tyto položky nejsou nové nálezy. Úprava integrability v cv. 22(c)
mezi nimi není; podrobné hledání je v poznámce k tomuto nálezu.

## Inkluze–exkluze: s. 182

**de Moivre 1718.** Přečteny celé citované s. 61–63, text i původní
obrazy (PDF strany 84–86). Výklad rozlišuje požadované a vyloučené
pevné pozice, odčítá příslušné průniky a rozpoznává alternující
binomické koeficienty. Odkaz vede ke správnému odvození. Zdroj:
[ETH / e-rara, první vydání](https://www.e-rara.ch/zut/doi/10.3931/e-rara-10420),
místně `../sources/de-moivre-1718.pdf`.

**de Moivre 1756.** Přečteny celé citované s. 110–112, text i původní
obrazy (PDF strany 132–134). Obsah odpovídá prvnímu vydání a podporuje
stejné tvrzení. Zdroj:
[sken třetího vydání](https://archive.org/download/doctrineofchance00moiv/doctrineofchance00moiv.pdf),
místně `../sources/de-moivre-1756.pdf`. Samotný Chelsea dotisk 1967
nebyl získán; rok je zde doložen známým oficiálním erratem, ne novou
kontrolou jeho titulního či copyrightového listu.

**Whitworth.** První vydání z roku 1867 bylo získáno jako
`../sources/whitworth-1867.pdf` a archivní OCR. Přečten titul,
předmluva, obsah a cíleně prohledány výskyty související s vylučováním,
pevnými pozicemi a derangements. Není tím prokázána absence obecného
principu v celé knize. Přímé algebraické odvození bylo skutečně
přečteno v **druhém vydání 1870**, dodatek III, s. 187–195; obrazy
s. 187–188 a titul, předmluva a obsah byly porovnány vizuálně.
Předmluva druhého vydání výslovně říká, že dodatky II a III jsou nově
přidány. Pramen tedy potvrzuje Whitworthův výklad a další rozvoj,
ale ne datování tohoto konkrétního odvození do prvního vydání.
Rok 1867 je správný rok prvního vydání knihy. Z tohoto rozdílu samotného
nevytvářím nový nález, protože citace knihy rokem jejího prvního vydání
může být záměrná. Zdroj přečteného odvození:
[Darwin Online, Choice and Chance, 1870](https://darwin-online.org.uk/converted/pdf/1870_Whitworth_Choice_and_chance_A6354.pdf).

**Todhunter 1860, §762.** Přesné druhé vydání má Google Books id
`3jADAAAAQAAJ`. Ve veřejném hledání se §762 nachází na tištěných
s. 485–486; s. 486 výslovně uvádí úlohu sjednocení událostí, které se
mohou překrývat. Odpověď API je uložena jako
`../sources/todhunter-1860-section762-search.json`. Celé odvození ani
obrazy přesného vydání nebyly zpřístupněny: veřejný PDF odkaz vrátil
429 a obrazový odkaz jen obrázek „image not available“. Tyto zástupné
obrázky nejsou vydávány za obrazy knihy. Starší či novější vydání není
použito jako náhrada přesného citovaného svědka. Zůstává `partial`.

Absolutní prvenství a tvrzení o dobovém rozšíření principu nejsou
matematické věty. Zde ověřené stránky dokládají příslušný obsah,
ne vyčerpávající rešerši všech možných předchůdců či recepce díla.

## Odpověď 23: cyklové délky a konstanta λ

**Shepp–Lloyd 1966.** Článek *Ordered cycle lengths in a random
permutation*, Trans. AMS 121, 340–357, byl získán z
[autorské univerzitní stránky](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Ordered-cycle-lengths-in-a-random-permutation.pdf).
Přečteny s. 340–342, 344, 346–347, 349–356 a bibliografie na 357;
vybrané formule jsou navíc zobrazeny v `../images/`.

Na s. 340–342 je přesně Poissonův model z cv. 22. Rovnice (14)
na s. 347 dává integrál pro λ. Na s. 355 je skutečně uveden druhý
člen λ/2, s výslovným vynecháním podrobností důkazu; vlastní úplný
důkaz v `longest-cycle.md` je proto nezávisle doplňuje. Nejkratší
cyklus je pojednán na s. 349–356: rovnice (22) na s. 352 a následný
důkaz dávají E S_n / log n → exp(−γ). To přesně stačí pro přibližný
průměr uvedený knihou. Silnější O(1) zbytek v (20) je v článku pouze
formálně odvozený a autoři výslovně tvrdí důkaz jen vedoucího členu;
takový O(1) zbytek zde tedy nepřebírám jako dokázaný.

**Gourdon 1996.** Disertace *Combinatoire, algorithmique et géométrie
des polynômes* je získána z
[MIT, kopie primární disertace](https://www.mit.edu/~sfinch/Xavier_Gourdon_-_Combinatoire,_algorithmique_et_geometrie_des_polynomes_-_Ecole_Polytechnique_thesis.pdf).
Přečtena relevantní část kapitoly VII: s. 199–214 a 220–226;
formule na s. 199, 222, 225–226 vizuálně porovnány. Existence rozvoje
s periodickými koeficienty a jeho uniformní zbytek byly zahrnuty do
kontroly, nikoli jen první několik formálních členů. Věta 6 na s. 222
dává pro uvedené zkrácení O(n^−4). Převod singulárních členů na
koeficienty je rozepsán v `longest-cycle.md` a souhlasí s knihou.
Nejde o audit celé disertace ani všech výsledků její kapitoly V,
na které kapitola VII navazuje.

**Mitchell 1968.** Metadata příslušného článku *An evaluation of
Golomb's constant*, Math. Comp. 22, 411–415, byla ověřena přes
[Crossref DOI](https://doi.org/10.1090/S0025-5718-68-99877-3)
a uložena jako `../sources/mitchell-1968-crossref.json`. Primární
text nebyl získán: obě AMS cesty vrátily 403, JSTOR 420 a další
veřejné zrcadlo bylo síťově nedostupné. Vlastní kvadratura s 85
desetinnými místy souhlasí se všemi 40 vytištěnými desetinnými místy
(výstup `../results/lambda-numerical.json`), ale není intervalovým
certifikátem. Nenahrazuje ani přečtení Mitchellova odhadu chyby,
ani ověření autorského připsání. Tento bibliografický bod je `partial`.

**Dickman a Knuth–Trabb Pardo.** Přímý Dickmanův článek v Arkiv 22A,
č. 10 (1930), 1–14 se nepodařilo získat po hledání podle přesného
názvu, autora, časopisu, v Archive a v ADS. Novější bibliografický
záznam není originál. Byl však přečten primární výzkumný report
Knutha a Trabb Parda z roku 1976, s. 39–43, zejména §10 na s. 42:
[Stanford CS-TR-76-538](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/1976/CS-TR-76-538.pdf).
Výslovně identifikuje Dickmanovu a Golombovu konstantu a odvozuje
rovnost integrálů. To je přímý pramen pro pozdější identifikaci,
ale není tím přečten Dickmanův původní numerický výpočet. Časopisecké
vydání je Theor. Comput. Sci. 3 (1976), 321–348,
[DOI](https://doi.org/10.1016/0304-3975(76)90050-5); oprava stránkového
odkazu 373 → 343 je už oficiální erratum. Použitý report má jiné
stránkování a není vydáván za fyzickou kontrolu časopisecké s. 343.

Výrok o neznámém vztahu λ ke klasickým konstantám nebyl vyvrácen.
Je to tvrzení o stavu poznání, nikoli zde dokazovaná absolutní
neexistence takového vztahu.

## Co zbývá pro plně uzavřený zdrojový audit

Přesné původní stránky Todhuntera 1860 §762, Mitchellův článek včetně
odhadu numerické chyby, Dickmanův původní článek, Chelsea titulní či
copyrightový list 1967 a časopisecká s. 343 Knuth–Trabb Pardo nejsou
primárně přečtené. U Whitwortha je výslovně rozlišeno první vydání
1867 a přečtené odvození z roku 1870. To jsou konkrétní meze auditu,
nikoli nové potvrzené chyby knihy.

URL, data stažení a SHA-256 získaných souborů jsou v
`../sources/manifest.json`; neúspěšné přístupy v
`../sources/access-limits.json`. Žádný z těchto pramenů nebyl
publikován ani odeslán třetí osobě.
