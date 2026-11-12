# Souvislá revize §2.2.6 — 5. listopadu 2026

X0968 uzavírá matematický průchod polí a ortogonálních seznamů. Znovu byly
přečteny originály 298–307 a odpovědi 556–560, všechny tři důkazní poznámky
`arrays-addressing.md`, `arrays-sparse.md`, `arrays-mix.md` a záznamy o
primárních pramenech včetně pozdějšího X0925. Strana 308 už patří stromům;
na 560 zůstává začátek jejich odpovědi 1 pro následující blok.

Všech 24 matematických úloh a hlavní výklad jsou uzavřeny v níže uvedeném
rozsahu. Dosavadní čtyři `partial` (17, 21–23) měly už doloženou matematiku;
nepřečtené přesné bibliografické verze jsou nyní výslovně přeskočené podle
uživatelova zadání. Nejsou vydávány za přečtené. Nevznikl nový nález ani
nový běh výpočtů. Starší zápisy o otevřených citacích zůstávají historií.

## Adresování a bijekce

Lexikografická hodnost obdélníku počítá pro každý první odlišný index
`(I_r-l_r) product_{s>r}(u_s-l_s+1)`. Násobení délkou prvku c dává
adresu bez mezer. Záporný fiktivní základ není záporná čtená adresa.
Koeficienty příkladu jsou 165,33,3,1; časové pole má 2 419 200 prvků.
Jeho interpretace jako smíšené číselné soustavy vyžaduje c=1, jak správně
upřesňují errata. Odpověď 1 používá správný řádkový krok 2n; úvodní
„indices ... to n“ je zkratka nerozlišující m a n, nikoli vadný vzorec.

Pro trojúhelníky byly ověřeny prefixové součty, změna indexace od 1 a
rozklad obdélníku na `column<=row` a `column>row`. Důkaz nemožnosti
těsného lineárního uložení jednoho trojúhelníku platí pro n>=2; n=0,1
jsou triviální malé výjimky, ne chyba obecného konstrukčního problému.
Nepřímé adresování úlohy 5 i levostranné vyhodnocování MIXAL výrazu
`j+1*j/2` souhlasí s dříve prověřenými pravidly.

Tetraedrické hodnosti jsou součty binomických čísel podle předchozích
vrstev. Obecné balení m! polí používá poziční inverzní tabulku
`B_r=#{s<r:a_s>a_r}`. Inverze vybere nejpravější minimum, přiřadí mu
největší zbývající symbol permutace a odečte 1 od souřadnic napravo.
Tím se znovu dostane tentýž problém menší dimenze, včetně přípustných
mezí a shod souřadnic. Jde o obecný důkaz, ne jen převzetí testů.

U rostoucí krychle opravená rekurence řadí celou slupku M za již uloženou
krychli velikosti M−1. Chybějící posun `(M_r-1)^r` v prvním dotisku
opravdu vadí: pro k=2 původní vzorec přiřadí (1,1) i (1,2) stejný základ.
Polynomiální hodnost úlohy 22 je combinadická hodnost přísně rostoucích
indexů `u_r=i_1+...+i_r+r-1`. Vektory se součtem S tvoří přesný interval
`C(S+k-1,k)..C(S+k,k)-1`, což dokazuje i požadovanou monotonicitu.

Rozšiřitelný obdélník ukládá buňku v bloku vytvořeném pozdější z událostí
„vznik jejího řádku“ a „vznik jejího sloupce“. To dokazuje jak větvený
vzorec, tak maximum obou adres. Obecnou dimenzi navíc pokrývá X0925:
nejpozději zavedená souřadnice určuje neměnný záznam počátku bloku a jeho
tehdejších kroků. Nejde o tvrzení, že chybný doslovný pseudokód disertace
nebo nedostupná časopisecká verze byly bezchybné.

## Seznamy a matice

Obrázek 13 prvního dotisku neodpovídá atributům osob. Zejména BLUE má
tečku u PERSON[3] a chybí správné propojení PERSON[2] a PERSON[1]; opravený
obrázek řadí BLUE přes 2,1 a HAZEL přes 3. Všechny čtyři skupiny atributů
opraveného obrázku jsou konzistentní. Algoritmus G spojuje sestupné
seznamy; v G4 se test „until“ stejně jako v G2/G3 chápe před podmíněným
posunem. Null se nedereferencuje. Každý ukazatel pouze klesá. Kombinovaný
index atributů je platnou odpovědí 10 s obvyklou cenou za údržbu.

Obrázek 14 má všech šest nenulových prvků matice (12), správné pořadí
obou typů odkazů, prázdný řádek 3 a sloupec 2 jako samosmyčky. Pivot
v (2,1) s hodnotou 10 dává přesně (14), včetně vložení (1,3) a smazání
(4,3). Horní odhad paměti úlohy 11 je 800*3+400=2800 slov, bez programu.

Obecný důkaz S zachovává původní c v pivotním sloupci až do konce řádku,
zatímco pivotní řádek již obsahuje b/a. PTR vždy stojí pod zpracovávaným
řádkem; při mazání zůstává na předchůdci, při ponechání výsledku se posune
na něj. To vylučuje pozdější použití uvolněného uzlu. Nové uzly vznikají
jen v právě zpracovávané pozici, takže neporuší konečnost průchodu.
Kruhové hlavičky, lineární varianta i pomocné LINK husté varianty mají
správné mezní podmínky. Uložení −PTR do záporného indexu hlavičky
předpokládá kladné adresy ukazatelů; MIX program zachovává znaménko
hlavičky samostatně a PTR ukládá do bajtů 1:3.

Doslovné MIX instrukce 557–559 byly porovnány s přiřazením registrů
v `arrays-mix.md`: návrat, pořadí uložení původních hodnot, porovnání
posunutých indexů, obě příchozí spojení nového uzlu a odpojení před jeho
vrácením do AVAIL. Omezení plovoucí aritmetiky v zadání 15 je podstatné.
Přijaté strojové testy používají pouze přesně reprezentovatelné výsledky;
nedokládají obecnou numerickou stabilitu, podtečení ani zaokrouhlování.
Varianta s FCMP na 559 zachovává součin v rA a při neshodě počítá d−cb/a.

Kopie, násobení a přestavba permutovaných seznamů mají vlastní obecné
invarianty. U inverze platí po všech pivotech pracovní matice
`B=P A^-1 P`; přejmenování řádků a sloupců dává `P^T B P^T=A^-1`.
Není-li další pivot, příslušný řádek transformované původní matice je
nulový. Pouhé přejmenování indexů by pořadí seznamů neobnovilo, proto
řešení 19 výslovně provádí tři lineární přestavovací průchody.

Líná inicializace 24 testuje rozsah V[k] před čtením L[V[k]]. Platný
prefix L obsahuje jen skutečně navštívené indexy, takže ani libovolný
původní obsah V nemůže vyrobit falešně platný prvek. Obnova A a V ukládá
původní hodnoty jednou na navštívený index; L se podle zadání neobnovuje.

## Prameny a přesné výjimky

Přebíráme dříve doložené čtení Doolittla 115–120, AHU úlohy 2.12 a
konkrétních křížových odkazů svazků 2/3/4A z X0267. Nově přečtené záznamy
X0925 doplňují původní Otooovu disertaci 1983, §5.1, a autorské odkazy na
Computing31(1983),1–9. Chowlin abstrakt v Notices AMS577-6 je pouze
oznámení výsledku, nikoli plný norský článek ani důkaz uvedeného vzorce.

Přeskočené přesné plné texty: Deuel1966, CACM9(5),344–347;
Gustavson1978, TOMS4(3),250–269; Schoor1982, IPL15(2),87–89;
Rosenberg–Strong1972, IBM TDB14,3026–3028 a navazující Current Trends4
(1978),263–311; Chowla1961, Norske...34,8–9; Otoo–Merrett1983,
Computing31,1–9. Soukromá připsání Wegnerovi a Nashovi nejsou nezávisle
doložena. Krátké nové hledání neposkytlo žádný další úplný originál;
přesná navigace a důvod ukončení jsou v `arrays-source-check.json`.

Na s.556 zůstává samostatně neověřené historické tvrzení, že záporný
fiktivní základ způsobil mnoho chyb překladačů a zaváděcích programů.
Matematicky je možné takovou chybu vysvětlit, ale tím se nedokazuje její
historická četnost. Stránka proto zůstává partial. Na 298 rovněž trvá
předchozí fyzický úkol o výtahu. Tyto mezery se neschovávají pod citace.

## Errata a mapa

Čtyři vrstvy čerstvě stažené 5. listopadu znovu prohledány po celých
stránkových blocích; výtah v `arrays-errata-extract.json`. Z jedenácti změn
jsou obsahové vady pro červenou mapu na 300,301,305,557,560. Kvalifikace
obdélníku na299, sazba A0 na556, oddělovače registrů, doplněný Doolittle
a konkrétnější odkaz na Algorithm7B samy nezakládají matematický nález.

Celé stránky 299–307 a 557–559 jsou matematicky/fakticky uzavřeny s
uvedenými bibliografickými výjimkami a známými chybami. 556 zůstává
partial z historického důvodu, 560 do dokončení začínající odpovědi
stromů. Přijaté výsledky `array-addressing.json` (638191 kontrol) a
`array-sparse.json` se neopakovaly; rozsah jejich aritmetiky se nerozšiřuje.
