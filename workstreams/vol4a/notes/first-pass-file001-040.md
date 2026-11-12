# První průchod: souborové strany 1–40

6. listopadu 2026. Rychlý první průchod dle výslovného zpřesnění uživatele:
celé stránky přečteny, podezřelé formule a obrázky porovnány s původní sazbou,
krátké přímé kontroly; nejde o certifikaci každého tvrzení ani úplnosti auditu.
Nové nálezy: **0**. Otevřená konkrétní matematická podezření: **0**.

## Vydání a mapování

Tiráž na souborové straně 5 přímo uvádí „First printing, January 2011“ a
ISBN 978-0-201-03804-0, ve shodě s `inventory/books.json`. Hash se přebírá
z inventáře, nebyl znovu počítán. DjVu má 901 stran (`djvused ... -e n`).
Fyzický výtisk nebyl ověřen.

- Souborová 1 je obálka, 2–16 jsou i–xv, 17 je obrazová xvi (Hommage à Bach).
- Tištěná strana 1 je souborová 18; pro hlavní text platí `file_page = printed_page + 17`.
- `text/vol4a.txt` vynechává obrazové strany 1 a 17. Jeho pořadí segmentů
  proto není pořadí stran souboru. Nová navigační kopie `sources/file001-040-ocr.txt`
  byla pořízena po jednotlivých stranách přímo pomocí `djvutxt --page=N`.
- `sources/file001-021.pdf` a `sources/file022-040.pdf` jsou výřezy původního
  DjVu, nikoli nová sazba. V druhém PDF platí lokální strana = souborová − 21.

## Matematický obsah a konkrétní kontroly

**i–xvi:** vydání, předmluva, notace, hodnocení úloh, tři ukázkové úlohy,
obsah a obrazová strana. Součty počtů neprázdných slov
`sum(n**k, k=1..n)` dávají pro n=5,10,24 přesně 3905, 11111111110 a
1391724288887252999425128493402200. Formulaci „10-letter alphabet“ upřesňují
známá errata; číselný součet při současné změně délkového limitu je správný.
Monus, medián, ν10=2, λ10=3, ρ10=1 a součin cyklů jsou konzistentní.
Poincarého tvrzení v ukázkové úloze 3 bylo přečteno, jeho důkaz nereprodukován.

**1–3:** definice a pět typů kombinatorických otázek; Langfordovy páry.
Paritní argument dává nutnou podmínku n≡0 nebo 3 (mod 4): sudé značky
obsadí stejný počet sudých a lichých pozic, zbývající počet v každé paritě
musí být sudý. V (2) sedí všechny vzdálenosti párů, šířka 7, součet 136 v
každé polovině a nulový moment; v (3) sedí vzdálenosti a vážený součet 5268.
Provedena kontrola svědků, nikoli minimum šířky, globální maximum či počty
optimálních řešení. Největší řetězec (4) je již opraven v erratech z 15. 5. 2020.

**3–8:** ortogonální latinské čtverce a přesné pokrytí. Čtverce (5) jsou
latinské a ortogonální včetně obou hlavních diagonál. Oba čtverce (7) jsou
latinské a jejich 100 uspořádaných dvojic je různých. Převod: pozice každé
značky M tvoří transverzálu L; deset disjunktních transverzál naopak dává M
po normalizaci prvního sloupce. Součet deseti uvedených počtů transverzál je
808; samotná enumerace se nespouštěla. Řádové součiny a poměry odhadů
výpočetní práce odpovídají textu. Konstrukce pro všechna n>6 a historické
zdroje pouze přečteny, neodvozovány znovu.

**9–12:** SGB slovník, krytí abecedy, slovní čtverec a krychle, slovní grafy.
Převzat lokální primární slovník `audit-2026-10-31/sources/sgb-words.txt`;
5757 slov, začátek/končení i příklady pořadí 1000–5000 souhlasí. Vzdálenost
`yucca`–`abuzz` má čtverec 2415; globální maximum se nehledalo. Uvedené
kryty mají 20,24,25 různých písmen. Čtverec (9) je symetrický, nejvyšší pořadí
372; krychle (10) je symetrická ve třech souřadnicích, nejvyšší pořadí 2968.
Byla přečtena pravidla sousednosti a konkrétní cesty (11)–(14); nejkratší
cesty a rozsáhlé enumerace krychlí nebyly znovu hledány. (13) má známou opravu.

**13–17:** definice grafů, podgrafů, stupňů, automorfismů, vzdáleností,
barvení a Theorem B. Zobrazené příklady v obr. 2, (16), (17), (22), (23)
prohlédnuty. Přímé argumenty: 3-krychle má 2³·3!=48 symetrií; okolí do
vzdálenosti 2 v grafu obvodu 5 dává alespoň 1+k+k(k−1)=k²+1 vrcholů;
důkaz trojúhelníkové nerovnosti odstraní opakovanou část spojených cest.
Bipartitnost ⇔ absence lichého cyklu souhlasí s barvením podle parity
lesních cest. Klasifikace případů rovnosti Moorovy meze ani velké slovní
komponenty se nereprodukovaly. Údaj 1198 na s.16 a podmínku „two steps“ již
opravují errata. Mapové hranice a literární/historické atribuce nebyly
ověřovány proti externím pramenům.

**18–23:** digrafy a multigrafy, obrázek 3, matice sousednosti, SGB reprezentace,
vzorec (33), algoritmus B a začátek katalogu grafů. Obrázek 3 a uvedené
komponenty/cesta prohlédnuty; dvě vlastní jména jsou opravena ve známých erratech.
Smyčka multigrafu přispívá 2 do stupně i na diagonálu převodu na digraf.
Mocniny A²,A³ v (29) souhlasí; šest přeznačení v (30) je šest možných matic.
Počítací mez grafů >2^(n(n−1)/2)/n! je správná: každá třída má nejvýše n!
označení a alespoň prázdný graf jich má méně. U (33) dává zbytek adresy
0 po dělení 8 posun +20 a zbytek 4 posun −20; 10¹²·3,6 ns=1 hodina.

Algoritmus B: pouze dosud neobarvený vrchol se vloží na zásobník, barva se
pak nemění; každá hrana je prohlédnuta z obou konců. Shodné barvy na hraně
vytvářejí spolu s lesními cestami lichý uzavřený sled. Po vyprázdnění
zásobníku je obarvena celá dosažitelná komponenta. Vnější průchod zahrne i
izolované vrcholy; každý vrchol se odebere ze zásobníku jednou a každý
oblouk se prohlédne jednou, tedy O(m+n). Původní sazba má správné `COLOR(w)≥0`
v B3 a `COLOR=-1` v B1, které OCR deformuje. Počty katalogových grafů na
spodní části s.23 pouze přečteny; generátory nebyly spouštěny.

## Výjimky a errata

Bibliografie a přeskočené historické údaje jsou rozepsány po stránkách v
`ui-page-coverage.json`. Neověřeny přesné citace a původ dat autorových
osobních vzpomínek, většiny historických dat, epigrafů a prózy. Nejde o
otevřená podezření na chybu. Žádné dohledávání externích pramenů se neprovádělo.

Výslovně nereprodukovány: tabulka L_n, velké benchmarky, globální optima
Langfordových párů, unikátnost ortogonálního partnera, 808 transverzál,
maximální vzdálenost slov, horní mez 24 různých písmen pěti SGB slov,
počty slovních krychlí/komponent, globální minimálnost Steinerova stromu,
klasifikace Moorových grafů, automatická kontrola mapových hranic a počty
katalogových grafů. Jejich text byl přečten a nic z toho se nevydává za
nezávisle přepočítané. Odkazované úlohy a odpovědi mimo tento rozsah ještě
nejsou součástí pokrytí.

Pro úvod náleží historické vrstvy `all4f0`, `err4f0`, `all4a-pre`, `all4a`,
`err4a` (text i původní/PDF varianty dostupné v `errata/`). F0 výslovně uvádí,
že pozdější změny po jeho přechodu do první edice patří do errat 4A. F1–F4
se týkají jiných bloků knihy; v tomto bloku nevzniklo podezření vyžadující
jejich prohledání. Relevantní začátky všech pěti textových vrstev byly
přečteny 6. 11. 2026; archív byl stažen 31. 10. 2026. Nový nález neoznačen.

Zohledněné opravy/amendmenty: all4a-pre s.v, viii, ix, xii, 1, 2, 3, 6,
9, 10, 11, 12, 13, 15, 16, 17, 19, 22, 23; all4a s.v, ix, x, xiv;
err4a potvrzuje krátkou aktuální řadu. Změny týkající se pouze šestého
 dotisku na s.3,14,18 se na naši první sazbu nevztahují. Žádná z těchto
položek není vlastní nález a nevytváří kartu ani červenou stránku.

## Reprodukce a další kurzor

`nice -n 15 python3 workstreams/vol4a/scripts/first_pass_sanity.py`
vypíše `results/first-pass-sanity.json`; je to jediná krátká sada přímých
kontrol, bez hledání řešení. Původní sazba byla vykreslena pomocí
`ddjvu -format=pdf -page=...` a `pdftoppm -q -r 110 -png -singlefile`.

Další souvislý kurzor: **souborová 41 / tištěná 24**, pokračování příkladů SGB.
