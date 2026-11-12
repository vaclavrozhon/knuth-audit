# SAT 212: částečné latinské čtverce a předepsané součty

Kontrola 31. 10. 2026. Dva samostatné nálezy F055 a F056.
Známá úprava odpovědi(a) z31. 5. 2017 je v našem PDF už provedena
a netýká se žádného z nich.

## F055: povolené symboly nejsou totéž co požadované symboly

Definice na str. 335 říká, že neprázdná buňka musí mít symbol k
s r_ik=c_jk=1 a řádky/sloupce nesmějí opakovat symbol. Neříká,
že se každý takto povolený symbol musí skutečně použít.
Indikátorový tensor proto splňuje jen x_i*k≤r_ik a x_*jk≤c_jk,
vedle rovnosti x_ij*=p_ij. Část(a) požaduje všechny tři rovnosti.

Nejmenší protipříklad je n=1, r=c=[1], p=[0]. Prázdná tabulka
splňuje úvodní definici, ale její jediný tensorový prvek musí
být současně0 i1. Zároveň nesplňuje rovnosti označené v(b)
za nutnou podmínku. Nejde tedy jen o odlišný počet řešení.

Neprázdný příklad: n=2, r=c jsou samé jedničky a p je jednotková
matice. Na obě diagonální buňky lze nezávisle dát symbol1 nebo2,
takže úvodní úloha má čtyři řešení. Předepsané tensorové součty
nemá žádné, protože každý řádek má jen jednu obsazenou buňku,
ale musel by obsahovat oba symboly.

Oprava definice může výslovně požadovat, aby množina symbolů
v řádku i byla přesně {k:r_ik=1} a ve sloupci j přesně {k:c_jk=1}.
Pak je(a) okamžitá bijekce a(b) skutečná nutná podmínka.
Alternativou je předem přidat rovnosti počtů řádkových a
sloupcových symbolů s počty obsazených buněk; pouhé zákazy
pak všechna požadovaná použití vynutí.

Původní článek Irving–Jerrum má právě takové rovnosti počtů
výslovně v zadání PLSC na str.176, oddíl4.2. Ověřeno vizuálně
v [primárním článku](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Jerrum.pdf).
Náš archivovaný exemplář je sken; pdftotext nevrací čitelný text.
Knižní znění bylo ověřeno v PDF str.335 i autorově PS str.151.

## F056: v redukci musí být k=K′, nikoli k=(I,J,K′)

Odpověď212(d), str.589, zavádí nové indexy (I,J,K), ale
neúmyslně je používá také jako barvy. Základní řádky a sloupce
mají podle případu(i) povolené jen barvy1,…,N; pomocné indexy
mají podle případu(ii) jen trojice. Buňky spojující oba druhy
indexů proto nemají žádnou přípustnou barvu.

Vezměme N=1, L(1,1)={1}. Vstup je zjevně řešitelný. Indexy
výstupu jsou 1 a h=(1,1,1). Tisk dává

    r = c = [1 0; 0 1],    p = [0 1; 1 0].

Buňky (1,h) a (h,1) musejí být neprázdné, ale průnik jejich
řádkových a sloupcových množin je prázdný. Výstup nemá řešení.
Tento příklad splňuje všechny vyrovnávací rovnosti z(b),
takže F056 je nezávislá na opravě F055.

Stačí nahradit podmínku `k=(I,J,K′)` podmínkou `k=K′`.
Stejný vstup pak dává r=c=[1 0;1 0], p beze změny;
obě obsazené buňky dostanou symbol1 a vše souhlasí.
Všechny nové barvy nad N mají nulové součty, což je dovoleno.
Konstrukce v původním článku na str.177 a183 používá stále
původní množinu barev, v souladu s touto opravou.

Znění chyby potvrzuje PDF str.589 i autorův PS str.225.
Ve stažených all4b a all4f6 odpovídající oprava nenalezena.
Historické erratum na PS str.225 mění jen formulaci exact cover
v(a), nikoli definici r,c v(d).

## Přímý důkaz opravené konstrukce

Pro jednu vstupní buňku(I,J) napišme seznam jako
K1<K2<…<Ks. Hlavička je h=(I,J,K1), pomocný index pro t≥2
je v_t=(I,J,Kt). Obsazené jsou buňky (I,h),(h,J) a pro každé
t≥2 také (h,v_t),(v_t,h),(v_t,v_t).

Hlavičkový řádek a sloupec musejí použít přesně všechny barvy
ze seznamu. Řádek a sloupec v_t musejí použít přesně dvojici
{K_(t−1),Kt}. Jejich společná diagonální buňka proto vynutí
shodnou opačnou barvu v(h,v_t) a(v_t,h). Obě hlavičky mají
stejnou množinu vnitřních barev, a tudíž stejnou zbývající
barvu v(I,h) a(h,J). To je zvolená barva původní buňky.

Naopak zvolíme-li původní barvu K_a, existuje jediné doplnění:
na obě křížové buňky příslušné t dáme K_(t−1), je-li t≤a,
a Kt, je-li t>a. Diagonála dostane druhou barvu dvojice.
Křížové buňky tedy použijí všechny barvy kromě K_a právě
jednou. Základní řádky/sloupce vynutí přesně původní latinské
podmínky. Konstrukce tak zachovává i počet řešení.

Počty požadovaných symbolů a obsazených buněk souhlasí:
základní řádky mají N, hlavičky s a ostatní pomocné řádky2.
Stejně sloupce; r=c zajišťuje rovnost součtů pro každou barvu.
Prázdný vstupní seznam lze před konstrukcí přímo odmítnout;
jinak je hlavička definována. Velikost indexové množiny je
N+Σ|L(I,J)|, tedy přesně deklarovaná a polynomiální.

Část(c), v kontextu palety1,…,N z předchozí úlohy, plyne
z párování: v latinském obdélníku M×N chybí každé barvě
i každému sloupci právě N−M možností. Bipartitní graf
sloupců a nepoužitých barev je pravidelný, takže má perfektní
párování. To vyplní další řádek; opakováním vznikne čtverec.

## Rozsah testů

`check_latin_reduction.py` nezávisle enumeruje malé částečné
latinské tabulky a také všechny binární tensory. Jejich přesné
marginály souhlasí s řešením pomocí exact cover. Pro n=1,2
prošlo všech 4 104 trojic binárních matic; 912 z nich ukázalo
rozdíl mezi povolenými a přesnými množinami. Všech40 vstupů
splňujících vyrovnávací rovnosti dalo shodný výsledek.
Nezávislý výčet zahrnoval258 binárních tensorů.

Knižní čtyřřádkový protipříklad v(b) je správný: součty
souhlasí, ale buňka(1,3) má prázdný průnik povolených barev.

Redukce(d) byla otestována na614 vstupních soustavách seznamů:
N=1; všech81 neprázdných soustav proN=2;500 náhodných proN=3;
30 náhodných proN=4; a plné seznamy proN=3,4. Opravený
exact cover měl vždy stejný počet řešení jako přímý výčet
latinských čtverců, dohromady659 řešení. Vytištěná konstrukce
odmítla všech69 řešitelných vstupů. Výsledky a nejmenší
protipříklady jsou v `results/latin_reduction.json`.

Tato položka kontroluje212; nedeklaruje úplný audit předchozí
redukce3SAT→grid list coloring v211 ani occurrence gadgets208.
