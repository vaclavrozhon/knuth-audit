# §4.6.2: historické a praktické poznámky

Pracovní stav 4. listopadu 2026. Matematické bloky a všech 41 úloh mají
vlastní důkazy v dřívějších poznámkách. Zde se kontrolují historické
atribuce a význam citované literatury. Textově přečtený článek není
označen jako vizuálně prověřený originál. Nedostupný plný text není
důkazem chyby ani potvrzením jeho obsahu.

## 1. Petr, Butler a Schwarz; strana 442

[Petr 1937](https://dml.cz/handle/10338.dmlcz/121487),
*Über die Reduzibilität eines Polynoms mit ganzzahligen Koeffizienten
nach einem Primzahlmodul*, má skutečně rozsah 85–94 v ročníku 66.
Text stran 85–90 byl přečten v PDF DML-CZ. Na 86 předpokládá různé
kořeny, na 87 zavádí matici mocnin x^(kp), na 88–89 ji převádí na
vážené cyklické bloky. Pro stupně ireducibilních faktorů d_i dostává
charakteristický polynom `prod_i (T^d_i-1)`.

Vlastní vysvětlení důsledku: po přechodu do rozkladového tělesa lze
polynom reprezentovat hodnotami v jeho různých kořenech. Zobrazení
`h(x) -> h(x^p) mod f(x)` permutuje tyto hodnoty v cyklech délky d_i.
V každém cyklu je pevný vektor určen jedinou souřadnicí. Proto má
jádro Q−I dimenzi r, počet cyklů, a hodnost Q−I je n−r.
Rozšíření tělesa hodnost nemění, protože nenulovost minorů se nemění.
To platí také pro p dělící d_i. **Samotná násobnost kořene 1 v
charakteristickém polynomu by v tomto případě nestačila**; rozhoduje
blokový tvar. Knuthovo „implicit in a more general result“ odpovídá
obsahu Petrova argumentu.

Například nad F_2 mají f=x²+x+1 a f=x(x+1) stejný charakteristický
polynom Q, totiž (T−1)², ale dimenze pevných podprostorů jsou 1 a 2.

Vydavatelské záznamy potvrzují
[Butler 1954, 102–107](https://academic.oup.com/qjmath/article-pdf/5/1/102/7288058/5-1-102.pdf)
a [Schwarz 1956, 110–124](https://academic.oup.com/qjmath/article-abstract/7/1/110/1585420).
Butlerovo PDF přesměrovalo na placený bibliografický záznam; jeho
plný důkaz ani celý Schwarzův článek zde zatím nebyly přečteny.
Oprava českého názvu časopisu z 6. března 1998 je známé erratum.

## 2. Frobenius; odpověď 37 na 689–690

Citovaný text *Über Beziehungen zwischen den Primidealen eines
algebraischen Körpers und den Substitutionen seiner Gruppe* má
rozsah 689–703. ETH poskytuje 15stránkový separát, ale jeho PDF zde
vrací pouze text nové knihovní obálky. Čtena proto byla
[textová reprodukce Springerova přetisku](https://studylibde.com/doc/8343396/21347257027a94ae2134838b5ac3dab9),
identifikovaná [vydavatelským DOI](https://link.springer.com/book/10.1007/978-3-662-41014-1).
Rozsah čtení: úvod 689–690, definice hustoty a formulace na 696–697 a závěr
702–703; ne celý analytický důkaz a ne vizuální kontrola separátu.

Na 689 Frobenius výslovně uvádí sepsání v listopadu **1880** a sdělení
výsledků Stickelbergerovi a Dedekindovi. Vydání 1896 tedy není důvod
opravovat Knuthovo datum objevu. Věta I na 696 dává podíl prvků
Galoisovy grupy s předepsanými délkami cyklů; shoduje se s knihou.
Na 702–703 je výsledek pro jednotlivé konjugační třídy ještě podmíněný.
Je nutno rozlišovat prokázaný cyklový typ od pozdější Čebotarevovy věty.

Původní hustota je zde definována koeficientem log(1/w) v součtu
`sum p^(-1-w)` pro w jdoucí k nule zprava (Dirichletova hustota).
Kniha užívá neformální náhodné velké prvočíslo. Moderní tvrzení pro
rovnoměrnou volbu p<=X vyžaduje přirozenou hustotu; tu v našich
matematických poznámkách používáme jako výslovný externí vstup.
Čtení historické formulace není nový důkaz této silnější verze.

## 3. Legendre a nulový kořen; strana 449

Původní sazba znovu vizuálně přečtena. Historický odstavec slibuje
všechny lineární faktory beznásobného f, ale začíná
`g=gcd(x^(p-1)-1,f)`. Tento g obsahuje právě faktory s **nenulovým**
kořenem v F_p, tělese zbytků modulo p. Faktor x se ztratí.

Pro p=3 a f=x je f beznásobný, ale `gcd(x²-1,x)=1`; všechny další
gcd s g jsou 1. Také f=x(x−1) dává pouze g=x−1. Stačí doplnit
„nonzero“ nebo předem oddělit faktor x. Jde o malou chybějící
podmínku v historickém popisu, nikoli o chybu algoritmu D, který
správně používá x^p−x. **C0222 confirmed.** Původní Legendreův
článek nebyl získán; chyba se nepřipisuje jemu.

## 4. Bernoulli, Schubert a roky; strany 449–450

Známá změna z 17. června 2002 doplňuje Bernoulliho 1708 a odkaz na
[Mignotte–Ştefănescu 2001](https://www.numdam.org/article/RHM_2001__7_1_67_0.pdf).
Čteny byly úvod 67–69 a bibliografie 88–89. Studie rozlišuje Schubertův
přednes 19. června 1794 a vydání 1798; citace časopisu má ročníkové
označení 1793. První dotisk i erratum přitom píší „in 1793“.

To je **C0223 candidate**, nikoli potvrzená chyba: ročníkové datum
1793 je doložené, ale přesný okamžik objevu z přednesu 1794 neplyne.
Původní Schubertův článek a akademické protokoly dosud nebyly čteny.
Navržené znění by mělo rozlišit datum ročníku, přednesení a vydání.
Matematická konečnost interpolační metody na této dataci nezávisí.

## 5. Další dostupné bibliografické doklady

Rabinův [vydavatelský abstrakt](https://epubs.siam.org/doi/10.1137/0209024)
potvrzuje úlohy rozkladu, hledání kořenů a tvorby ireducibilních
polynomů, probabilistický postup i citaci SICOMP 9 (1980), 273–280.
Plný článek nebyl přečten. U
[Moses–Yun 1973](https://doi.org/10.1145/800192.805698)
abstrakt potvrzuje multivariate gcd přes Henselovo zvedání a strany
159–166. Žádný z těchto abstraktů není dobový benchmark.

[Flajoletova autorská bibliografie](https://algo.inria.fr/flajolet/Publications/publist.html)
potvrzuje ICALP 1996, LNCS 1099, 232–243 a vztah k rozšířené verzi
v Journal of Algorithms 40 (2001), 37–81. Odkaz označený jako verze
1996 ve skutečnosti vede na jiný článek *An Analytic Approach to
Smooth Polynomials* z roku 1998. Tuto záměnu odkazu nepřebíráme.
U správného [autorského preprintu 2001](https://algo.inria.fr/flajolet/Publications/FlGoPa01.pdf)
byly čteny abstrakt a úvod na 1–2, poznámka na 8 o rozšíření konferenční
verze a citace 18 na 43. Potvrzují téma průměrné analýzy celého řetězce
squarefree / distinct-degree / equal-degree. Všech 44 stran ani
konstanty hlavních vět nebyly v tomto bibliografickém kroku auditovány.

## 6. Zdrojové mezery, které tento blok dosud neuzavírá

- Legendre 1785, Gaussova poznámka 237, Galois 1830/1846, Serret §7;
  Lagrange 1771, původní Swinnertonův příklad a Weinbergerův odkaz.
- Plné články Butler/Schwarz, Berlekamp 1970, Moenck/Rabin/
  Cantor–Zassenhaus/Camion; praktická srovnání Musser/Brown/Moses–Yun.
- Atkin 1998, Shanksův příspěvek a Cipolla 1903. Jejich algoritmy již
  mají vlastní důkazy; neoznačujeme tím prvenství za potvrzené.
- Van der Waerden a Čebotarev: doplnit původní formulace; hluboké
  analytické věty zůstávají explicitními externími vstupy.
- Knopfmacher–Warlimont 1995: autorův záznam obsahuje správný abstrakt,
  ale odkaz na plné PDF vrací 404. De Bruijnova osobní atribuce a
  Greene–Knuth §4.1.6 nejsou potvrzené samotným vlastním důkazem.

Nedostupná PDF se neopakovaně nezkoušejí stejnou cestou. Rozsah
dostupných alternativ je v manifestu. Žádné již úspěšné matematické
testy se při tomto bibliografickém doplnění neopakovaly.
