# V3-C0020 — Algorithm Q potřebuje hranici aktuálního řádku

**Confirmed, medium.** Úloha§5.1.4–39(f), odpověď614/file625,
Algorithm Q2–Q3 a následující tvrzení o kandidátních cestách.
Podpůrný hint71/file82 používá stejný strom. Originální sazba obou
stran zobrazená v images/tableaux-file-625.png a -082.png.

Q prochází buňky po řádcích. Již rozebrané horní řádky znovu obsahují
libovolné původní hodnoty. Při vracení prvku do(i,j) se proto cesta
nesmí dostat nad řádek i. Vytištěné Q3 však stále bez této podmínky
porovnává skutečné P_(r−1,s) s P_(r,s−1); obdobně strom pro výběr
kandidáta není omezen na právě aktivní řádky. Následující vstup je
v přesném doménovém rozsahu úlohy a narazí na tuto vadu.

## Přípustný vstup a dva korektní počáteční kroky

Vezměme tvar(2,2) a

    P = [1 2]       Q = [0 −1]
        [3 4],          [1  0].

P je standardní tableau. Meze Q podle39(c) jsou po buňkách
[-1,1], [-1,0], [0,1], [0,0], takže všechny čtyři položky vyhovují.
Nepředpokládá se vstup mimo přípustný obor ani vlastnost cizího grafu.

1. Pro(i,j)=(1,1) jsou kandidáty(1,1) a(2,2). Jejich kódy jsou
   Q a DRQ: v(2,2) je levý soused3 větší než horní2, a pak jde
   cesta nahoru do(1,1). V pořadí D<Q<R je první DRQ.
   Q2 nastaví Q12=Q11−1=−1. Q3 vrátí K=4 po cestě přes(2,1)
   a(1,1), takže vznikne P=[4 2; 1 3].
2. Pro(1,2) je jediným kandidátem(2,2), protože Q12=−1.
   Horní soused2 je větší než levý1; K=3 se vrátí do(1,2).
   Výsledkem je P=[4 3; 1 2]. Dolní řádek Q zůstává[1 0].

## Konkrétní rozpor v dalším kroku

Nyní(i,j)=(2,1). Q21=1 není nekladné, takže kořen(2,1) není
kandidátem; Q22=0 dává jediného kandidáta(r,s)=(2,2).
Strom z hintu však z(2,2) vede nahoru, protože

    P12=3 > P21=1.

Jeho cesta se tedy nedostane do(2,1). Už tím je vyvráceno výslovné
tvrzení pod Q3, že každý kandidát má v uvedeném stromu cestu
do aktuální buňky; kód požadovaný Q2 zde není definován.

I kdybychom jediného kandidáta prostě zvolili, Q3 provede tentýž
nesprávný krok: uloží P22←3 a nastaví r←1. Každý další krok Q3
už r nebo s pouze zmenšuje. Do cíle s řádkem2 se tedy nikdy nemůže
vrátit a podmínku ukončení nemůže splnit. Rozhodující hodnoty3 a1
leží uvnitř původního tvaru; konvence pro buňky mimo tvar tento
rozpor neřeší.

Pro doplňující kontrolu původu páru stačí ruční dopředný průchod
z [4 3; 2 1], se samostatnou dříve doloženou opravou C0006 v S′:
dolní vložení2 dá Q21=1; svislé vložení3 dá Q12=−1; vložení4
končí v(2,2), a proto dá Q11=0,Q12=−1. Výsledný P je[1 2;3 4].
Protipříklad ale tento původ nepotřebuje:39(f) výslovně připouští
každý standardní P a každé Q v uvedených mezích.

## Lokální oprava a vztah k primárnímu zdroji

V Q3 se horní soused smí uvažovat pouze při r>i. Na řádku i
je nutné jít doleva, dokud není dosaženo(i,j). Stejná hranice
musí platit při vytváření stromu a kandidátních kódů v Q2;
například porovnávat nulu místo P_(r−1,s), je-li r=i.
V uvedeném příkladu pak jediný poslední kandidát jde správně
z(2,2) doleva do(2,1), čímž obnoví[4 3;2 1].

Tato hranice odpovídá primárnímu
[Novelli–Pak–Stoyanovskii1997](https://www.math.ucla.edu/~pak/papers/bij.pdf),
Algorithm P′, Step1, tištěná58/PDF6. Zdroj používá sloupcové
pořadí a pro levého souseda výslovně podmiňuje j′_1>j′_0;
jinak dosazuje0. Při transpozici tvaru jde právě o podmínku r>i
pro horního souseda. Sazba tohoto místa byla zobrazená v
images/tableaux-nps-boundary-file006.png.

Úplná správnost opravené obecné bijekce má vlastní důkazový blok;
krátký protipříklad zde sám nezastupuje jeho invarianty. Nový nález
je odlišný od C0006: ten opravuje návrat v dopředném S′ na70,
zatímco zde selhává inverzní Q na614 při přípustném tableau a Q.

## Errata a rozsah potvrzení

Všech pět vrstev bylo cíleně zkontrolováno podle stran70,71,613,614
i názvů algoritmů, kandidátů a autorů. Podrobnosti jsou v
sources/tableaux-inverse-boundary-errata-review.json. Relevantní
známá změna39 opravuje jen množné číslo v odpovědi(a); změny614
se týkají40–42. Žádná odpovídající oprava Q2/Q3 nebo stromového
invariantu nebyla nalezena. První edice tento nový Algorithm P/Q
nemá a její pozdější dodatky jej nedoplňují.

Rozpor je doložen v našem skenu, ne tvrzením o prvenství či odměně.
Fyzický výtisk nebyl ověřen. Nebyl spuštěn žádný numerický běh.
