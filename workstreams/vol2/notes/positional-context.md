# Kapitola 4: úvod a historický kontext §4.1

Aktualizace obnovy 6. listopadu 2026: původní souhrnné uzavření níže
nenahrazuje kontrolu každého tvrzení a tištěného mezikroku. Aktuální
stav určuje `results/quality-recovery-2026-11-06.json`; první nový blok
je `recovery-positional-foundations-2026-11-06.md`. Konkrétní staré
důkazy se přebírají až po přečtení a s přesným původním rozsahem.

## Rozsah uzavření

Původní strany 194–209, zadání 210–213 a odpovědi 604–611 byly celé
přečteny vizuálně. Matematické části a všech 34 úloh jsou doloženy
v navazujících poznámkách; poslední obecné komplexní soustavy uzavírá
[complex-extensions.md](complex-extensions.md). Tento dokument doplňuje
historické souvislosti, epigrafy a změny ve všech čtyřech vrstvách errat.

Uzavření znamená přečtení textu, kontrolu jeho matematických tvrzení,
porovnání známých oprav a níže vymezenou kontrolu pramenů. **Není to nový
úplný dějepis číselných soustav ani nezávislé potvrzení každého prvenství,
každého data a každé bibliografické položky.** Nedostupné či neprostudované
prameny jsou výslovně rozlišeny. Nevznikl nový nález; známé opravy se do
počtu nových chyb nezapočítávají.

## 1. Epigrafy na straně 194

| Výrok | Ověřený pramen a výsledek | Meze ověření |
|---|---|---|
| M. P. La Touche, 1878 | *The Letters of a Noble Woman*, ed. Margaret Ferrier Young, London: George Allen & Sons, 1908, 49–50. Originály obou stran přečteny vizuálně. Datum je July 1878; text i vyznačená výpustka v Knuthovi souhlasí. Slovo Number je v originálu v jednotném čísle. | Jde o vydání dopisů z 1908, nikoli prohlídku rukopisu. |
| B. Parlett, 1979 | Coonenova disertace *Contributions to a Proposed Standard for Binary Floating-Point Arithmetic*, Berkeley, 1984, str. 1.1, má doslova stejnou větu s atribucí B. N. Parlett (1979). Titul s podpisy a datem 1. 6. 1984 a strana 1.1 přečteny vizuálně. | Dokládá rané písemné svědectví, nikoli záznam původního ústního projevu. |
| John Nepair, 1616 | *Memoirs of John Napier of Merchiston* (1834), 379 a 381–382, přetisk předmluvy anglického překladu. Strany 381–382 vizuálně, 379 textově. Kontext, obsah a rok anglického vydání souhlasí. | Přetisk pravopis modernizuje a například má calculations místo Knuthova Calculators. Originál 1616 nebyl získán, proto nepřisuzujeme rozdíl chybě Knutha a netvrdíme úplnou pravopisnou shodu. |
| F. H. Wales, 1936 | Existenci diskuse po Phillipsově přednášce a začátek Walesova příspěvku dokládá dostupný indexovaný text původního časopisu, str. 204. | Přesná pasáž epigrafu nebyla samostatně přečtena v původním obrazu; pokusy o PDF vracely 503, vydavatelský odkaz HTML místo PDF. Atribuce a přesné znění zůstávají v tomto omezeném rozsahu. |

Uloženy jsou jen relevantní výňatky a metadata:
[La Touche](../sources/la-touche-1908-excerpt.pdf),
[Coonen](../sources/coonen-thesis-excerpt.pdf),
[Napier](../sources/napier-memoirs-1834-excerpt.pdf).
Zdroje pocházejí z [digitalizace La Touche](https://upload.wikimedia.org/wikipedia/commons/a/a2/The_letters_of_a_noble_woman_%28Mrs._La_Touche_of_Harristown%29_%28IA_lettersofnoblewo00latorich%29.pdf),
[archivu Coonenovy disertace](https://www.arithmazium.org/library/lib/jerome_coonen_phd_thesis.pdf)
a [e-rara](https://www.e-rara.ch/download/pdf/18939754.pdf).

Úvodní dva odstavce kapitoly správně vymezují předmět aritmetických
algoritmů. Hodnotící věty o zajímavosti či významu aritmetiky nejsou
matematickými univerzálními tvrzeními, která by vyžadovala protipříklad.

## 2. Bernoulliho 118 bitů: původní sazba a přesná kontrola

Získán byl sken C. I. Gerhardt, *Leibnizens mathematische Schriften*,
svazek 3, část 1 (1855), z digitalizace BnF/Gallica uložené na
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Leibniz_-_Mathematische_Schriften,_Gerhardt_vol_3a.djvu).
V této kopii je souborová strana 98 tištěná 97; mapa byla ověřena přímo
na obrazu. Uložený [výňatek 96–97](../sources/gerhardt-1855-excerpt.djvu)
zachovává původní DjVu stránky, nikoli rekonstruovanou sazbu.
Obě byly přečteny vizuálně, včetně tabulky a odstavce o hledání period.

V originálu je na poslední pozici dvojice 1/0. Pro dolní možnost je
přesný přepis tří řádků

```
111100100000010011111101100110001101101101100110000100
111100100101100101011011011010100011011100101010000000
1111010000
```

Má délky `54+54+10=118` a hodnotu
`314159265358979323846264338327929808`. Skutečná dolní 35místná
aproximace, tj. `floor(10^35 π)`, je
`314159265358979323846264338327950288`. Rozdíl je `20480=2^14+2^12`;
právě na bitových pozicích 12 a 14 (počítáno od exponentu nula zprava)
je nula místo jedničky. Horní možnosti, s posledním bitem 1 a s horním
celým přiblížením π, mají přesně tytéž dvě chyby.

Nezávislou kontrolou přepisu je i **posloupnost délek běhů**, tedy počtů
po sobě jdoucích stejných bitů, kterou Bernoulli sám tiskne za číslem.
Pro dolní možnost dává přesně

```
421612612223212121222412421211221111212121111321321111174114
```

a souhlasí s původním obrazem. Knuthův údaj o dvou nesprávných bitech
je tedy doložen přímo, bez kruhového odvolání na novější text citující
Knutha. Známé erratum 10. 8. 2022 správně mění 35-digit na 35-place:
jedna číslice před čárkou a 35 za ní dávají celkem 36 desetinných cifer.
Jméno editora opravuje již erratum 2011 na C. I. Gerhardt.

[verify_positional_context.py](../verify_positional_context.py) porovnává
přepis s celočíselným převodem a běhy. Interval pro π je odvozen ze stejné
přesné Machinovy identity jako v základním bloku; dřívější testy se
neopakují. Nový 35místný výsledek je sevřen racionálními mezemi, nikoli
určen plovoucím zaokrouhlením.

## 3. Další cíleně ověřené údaje

**Mádhava, doplnění 2023 ke straně 198.** Pro vytištěný údaj
`9·10^11 π ≈ 2827433388233` je rozdíl pravé strany a přesné levé strany
mezi 2.186 a 2.187. Chyba následné aproximace π je tedy přibližně
`2.43·10^(−12)`. Je to historická aproximace, ne tvrzení o správném
zaokrouhlení celého čísla. Z toho nevzniká protipříklad. Uvedený původ
v Nílakanthově komentáři ke Gaṇita §10 nebyl samostatně z kolacionovaného
sanskrtu ověřen. Předchozí údaj al-Kášího na téže straně je přesně
prověřen v [základní poznámce](positional-basic.md), §1.

**Phillipsova přednáška 1936, strany 201–202.** Primární
[vydavatelská stránka](https://www.cambridge.org/core/journals/journal-of-the-institute-of-actuaries/article/abs/binary-calculation/4E077B9A472C2F72D64CCA8B13708EF8)
ověřuje autora E. William Phillips, název *Binary Calculation*, JIA 67,
187–221 a úvodní větu o přechodu k osmičkové soustavě. Přístupný indexovaný
text původního PDF dovolil číst první strany článku a pasáž strany 215
s námitkou k pěti procentům. Matematicky
`(3.(1463))_8=16/5`, takže dělení 64 dává přesně `1/20=5 %`.
Závorky označují opakování bloku. Úplné PDF ani původní obraz těchto
pasáží nebyly získány; [metadata neúspěchu](../sources/phillips-1936-binary.json)
a [vydavatelského pokusu](../sources/phillips-1936-cambridge.json) to zachovávají.
Tvrzení o prvním slovníkovém výskytu octal v roce 1961 nebylo ověřeno
úplnou rešerší historických slovníků; původ u patic elektronek je v knize
sám označen za domněnku.

**Pelikán, doplnění 2024 ke straně 200.** Autorův původní výzkumný text
D. Zlatopolski na [webu muzea výpočetní techniky](https://www.computer-museum.ru/books/Zlatopolski_perfect_arithmetics.pdf)
obsahuje fotografie titulní strany a obou algoritmů. Titul potvrzuje
*Arithmeticus Perfectus*, Wenceslao Josepho Pelicano, Praha 1712.
Přečteny jsou strany souboru 1–3, 9–10 a 14, obrázky na 3, 9 a 10
vizuálně; jen tyto strany jsou [uloženy](../sources/zlatopolski-pelikan-excerpt.pdf).
Jejich výsledky odpovídají `57²=3249` a `79³=493039` a jsou takto zapsány
binárně. Popisek druhého obrázku v moderním článku nesprávně říká
čtvercová odmocnina, ale zobrazený původní výpočet je kubická odmocnina;
Knuth uvádí správně oba typy. Nejde o nový nález v TAOCP.
[Vydavatel](https://www.sciencedirect.com/science/article/abs/pii/S0315086022000659)
potvrzuje bibliografii anglické verze, *Historia Mathematica* 62 (2023),
40–50, DOI 10.1016/j.hm.2022.09.002. Článek uvádí rozsah 86 stran,
Knuth xii+84; bez úplné původní knihy nevyvozujeme z různých součtů
novou chybu. Úplná historická priorita a formulace o zapomenutí po více
než 300 let nebyly nezávisle prokázány.

Všechny nové číselné kontroly prošly; [JSON](../results/positional-context.json)
a [log](../results/positional-context.log) jsou úplné. Shell po verifieru
vypsal log, takže samotný shellový návratový kód není vydáván za další
nezávislou kontrolu.

## 4. Přehled známých historických oprav a hranic pramenné kontroly

Byly porovnány `all2-prepre`, `all2-pre`, `all2`, `err2` i uložený
současný TeX. [Relevantní výňatek](../sources/positional-errata-excerpts.txt)
obsahuje konkrétní záznamy a data. Mimo již výše probrané změny jsou pro
čtení prvního dotisku podstatné zejména tyto skupiny:

| Strany | Změna zachycená erraty |
|---|---|
| 196 | Thompson 1942/37–62 opraven na 1941/37–67; Justesonova tehdy chystaná práce nahrazena bibliografií 2001, následně opraven italský název. |
| 197–198 | Čína používala šedesátkovou soustavu jen zřídka; původní nikdy bylo opraveno. Rok úmrtí Zu Chongzhi na 500 nebo 501. Van Ceulenův interval začíná 1586. Doplněn Bianchini před 1450 a bibliografie Rosińské. |
| 199 | Opravy jména Caramuel, názvu nakladatelství a překladu Pascalovy věty. |
| 200 | Napierova lokální aritmetika je třetí část *Rabdologiæ*, nikoli příloha. Doplněno Leibnizovo použití základu 16 a překlad Strickland–Lewis 2022. |
| 201–202 | Doplněna Hillova přednáška 1845 ve vydání 1860; odstraněno zastaralé hodnocení Glaserovy knihy. Návrh latinského názvu změněn na sexdecimal. |
| 205 | Opravy jména Marczyński a rozsahu stránek IEEE; doplněna oprava Blachmanova článku v CACM. |
| 208–209 | Doplněn Fowler a jeho vyvážená trojková konstrukce. Tvrzení o faktoriální soustavě ve středověké Indii později odstraněno a nahrazeno odkazem na Laisanta 1888; doplněn Rényi 1957 a řetězové zlomky. |
| 213 | Henselův odkaz 1904 nahrazen odkazem 1897. Matematika 2-adických čísel byla ověřena samostatně. |

Tato tabulka **dokládá zapracování autorových známých oprav**, nikoli
samostatné přečtení všech uvedených starých publikací. Totéž platí pro
širší vyprávění o Babylonii, Mayích, přenosu indických číslic, Harriotovi,
Pascalovi, Caramuelovi, Karlu XII., Nystromovi, Taylorovi, prvních
počítačích a jednotlivých znovuobjevech záporných soustav. Jejich
matematický obsah byl ověřen v příslušných blocích; úplná historická
priorita zůstává mimo doložený rozsah této kontroly. U žádné z těchto
atribucí se nezaměňuje absence protipříkladu za důkaz prvenství.

Toto byl původní kontextový souhrn, nikoli aktuální uzavření celé §4.1.
Obnova jednotlivých argumentů probíhá podle mapy uvedené nahoře.
Nálezy C0079 a C0080 a redakční kandidát C0081 se tím automaticky
nemění; na straně 198 je navíc později doložený C0233 z powers-history.
