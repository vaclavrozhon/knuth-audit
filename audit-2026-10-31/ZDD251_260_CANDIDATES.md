# Dvě interpretační otázky: C041 a C042

3. listopadu 2026. Obě znění přímo prohlédnuta v knize i autorově draftu,
šest relevantních vrstev errat bez odpovídající změny. Jde o kandidáty;
nezvyšují počet potvrzených nálezů.

## C041: přesné nebo schematické sčítání velikostí v256?

Odpověď256, kniha481/draft185, popisuje nejprve časT(2q)+T(2r)
a ZDD velikostiZ(2q)+Z(2r), poté prozkoumání menšího z lichých grafů.
Jako vysvětlení řádu nákladů je to správně. Jako přesný počet všech
uzlů v dokončeném výstupu však má být **Z(2q)+Z(2r)−1**.

Pro q,r≥2 má spojovací vrchol jediný minimální stupeň2 a větví první.
Úspěšná větev zanechá disjunktní K(2q),K(2r). Oba poddiagramy mají
dohromady (Z(2q)−2)+(Z(2r)−2) rozhodovacích uzlů. Přidá se jeden
kořen pro úspěšnou spojovací hranu a jen dva společné terminály.
Neúspěšná větev další uzly ZDD nevytváří. Proto výsledný součet−1.

Při q=r=2 má každý K4 osm uzlů, celý graf15. Vytištěný součet dává16.
Nejde o další projev F079: zde používáme již opravené přesné hodnotyZ.
Pět nových malých grafů souhlasí ve dvou implementacích.

Přesný počet updatů je

    U_Z(2q)+U_Z(2r)+U_Z(k)+(2q+2r+4),
    k=min(2q+1,2r−1).

Poslední člen je cena prvního větvení. Počet skutečných položek cache
je `F_(2q+1)+F_(2r+1)+F_(k+1)` včetně nulové signatury. Knižní vzorec
pro cache může tento počet správně vyjádřit, pokud C pro lichý graf
počítá navštívené stavy a ne přidanou nenavštívenou nulu. Proto z něj
nevytváříme další chybu. Otázka zůstává přesnost versus schematičnost
formulace o velikosti a čase, nikoli obecné chování algoritmu.

## C042: podmínka LEN(i)≠0 v254(b) potřebuje vymezit sekundární položky

Kniha480/draft184 říká „each item i“ a pak podmiňuje příspěvek do
signatury nenulovou LEN. To je správný filtr pro sekundární položky.
Aktivní primární položka však musí mít bit1 i tehdy, když nemá možnosti;
jinak se nesplnitelný stav může zaměnit za úspěšnou prázdnou signaturu.

Nejkratší neprázdný příklad bez prázdného vstupního sloupce:

    primary: a b c
    options: a b
             a c

MRV vybere b. Po možnosti a b zbývá c s LEN(c)=0. Kdyby se filtr
LEN≠0 použil i na c, vznikla by signatura0 a Z2 by oznámil úspěch,
přestože c pokryto není. Správný primární bit to nedovolí.

Hlavní text120 i zadání254 výslovně definují primární bity správně.
Odstavec254(a) se zabývá sekundární položkou; je tedy možné, že autor
v254(b) implicitně pokračuje pouze pro sekundární část. Samotná věta
„If LEN…“ je navíc dostačující podmínka, nikoli výslovná definice opačné
větve. **Proto tuto věc necháváme jako kandidáta na zpřesnění textu,
nikoli potvrzenou chybu Algorithm Z.**

Archivovaný autorův `sources/knuth-programs/dlx6.w` rozlišuje dvě
operace: primární položka přispívá vždy, sekundární má test `len==0`.
Nativní program tedy tento problém nemá. Nepouštíme jeho staré úspěšné
testy znovu. Možná úprava textu: test pouze pro sekundární položky,
nebo výslovné odmítnutí prázdné primární položky před cache lookup.

Doklady: [source-checked.json](results/zdd251_260/source-checked.json),
[odpovědi251–254](images/csharp247-250-original-500.png),
[odpovědi255–260](images/zdd251-260-original-501.png).
