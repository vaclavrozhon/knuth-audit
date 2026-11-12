# Binet, Cauchy a integrální rozšíření: §1.2.3–30 a 46

V1-X0753, 2. listopadu 2026. Obě celé úlohy jsou checked spolu
s přijatou matematikou v sums-and-products.md a matrices.md.
Nové testy se neopakovaly; nový nález nevznikl.

Root ověřil 53 souborů a čtyři vstupní záznamy zmrazeného
MANIFEST-binet-cauchy30-46.json, SHA-256
`50667864728bfed001235043401dca4ad620df11d09dcd7694bf17be51e728ec`.
Jeden vstupní PDF je zároveň mezi 53 soubory. Přečetl celé předání
a obě agentovy poznámky. Přímo obrazově četl následující místa:

- Binet: s. 280, 284–287 a původní obsah XVI. sešitu; také metadata PDF.
- Cauchy: titul X/XVII/leden 1815, s. 29, 103–107 a 111–112.
- Bouniakowsky: titul článku, jeho rub a přesně citovanou s. 4.
- Schwarz: titul přetisku 1890, záhlaví článku s. 223 a celou s. 251.
- TAOCP: s. 36, 38–39, 472 a 475; errata all1 PDF 11
  a all1-prepre PDF 31, přečtená též v návazné kontrole X0752.

Agentův širší rozsah, uvedený v INPUTS a poznámkách, zahrnuje
Binetovy s. 280–293, 298, 354, Cauchyho s. 78–82 a 103–112
a Bouniakowského s. 1–3. Ani jeden rozsah neznamená audit celých
externích svazků.

## Konečná identita a historická data

[Binetova původní sazba](https://people.math.harvard.edu/~knill/graphgeometry/binet/binet1.pdf)
v §4, s. 286–287, sčítá součiny dvou determinantů řádu 2 přes
n(n−1)/2 dvojic různých indexů. Jeho závorková značka je na s. 285
přímo definována jako yz'−zy'; akcenty označují indexy. Po přejmenování
je výsledkem

```text
sum_(j<k) (a_j*b_k-a_k*b_j)(x_j*y_k-x_k*y_j)
 = (sum_j a_j*x_j)(sum_j b_j*y_j)
   - (sum_j b_j*x_j)(sum_j a_j*y_j).
```

To je přesně úloha 30. Dvojice se berou jednou, bez dalšího faktoru 2.
Pro komplexní zvláštní případ knihy se použijí její uvedené konjugace;
historickému prameni se nepřipisuje doslovná moderní komplexní formulace.

Záhlaví s. 280 přímo uvádí přednes 30. listopadu 1812. Dochovaný
obsah identifikuje časopis, XVI. sešit, autora, název i rozsah 280–354;
metadata PDF mají původ BnF a rok 1813. Samostatný titul ročníku IX
zde přímo přečten nebyl. Tato konkrétní mez je zachována, ale nebrání
jednoznačné identifikaci získaného původního článku; rozpor v roce
nebyl zjištěn. Rok přednesu se nezaměňuje s rokem publikace.

[Cauchyho původní svazek](https://archive.org/download/journal-de-lecole-polytechnique-vol-10/Journal%20de%20l%27%C3%89cole%20Polytechnique%20vol%2010.pdf)
má na titulu leden 1815 a na začátku článku s. 29 stejné datum
přednesu 30. listopadu 1812. Tím je přímo doložena věta knihy
o společném dni. Závěr na s. 111–112 popisuje také jejich setkání;
netvrdí se jejich úplná osobní izolace při výzkumu.

Pro m×n matici A a n×m matici B označme A_J podmatici sloupců
s indexy v m-prvkové množině J a B_J podmatici odpovídajících řádků.
Indexy jsou v obou případech rostoucí. Obecná identita úlohy 46 je

```text
det(AB) = sum_(J subset {1,...,n}, |J|=m) det(A_J)*det(B_J).
```

Cauchyho §11 na s. 103–107 pracuje s minory, tedy determinanty
čtvercových podmatic, řádu p. Rovnice (62) na s. 107 je součet
součinů odpovídajících minorů přes P=binomial(n,p) kombinací.
V (60)–(61) rozvíjí součin, na s. 105–106 využívá alternování,
a koeficient jednoho monomu určuje konstantu až na znaménko.
S. 107 volí souhlasná znaménka a dostává konstantu 1.

Převod na knihu je přesný: pro m<=n položme p=m a doplňme A
i B^T nulovými řádky na čtvercové matice řádu n. Vyberme první
m řádků obou soustav. Levá strana je det(AB), zatímco druhý minor
vpravo je det((B_J)^T)=det(B_J). Součet probíhá přes kombinace,
takže nevzniká faktor m!. Případ m>n, prázdný součet a nulový
determinant, pokrývá již přijatý obecný důkaz; nepřipisuje se
Cauchymu formulace odvozené soustavy řádu p>n. Odkaz 30 na případ
m=2 úlohy 46 je správný.

## Dodatek o integrálech

[Bouniakowského originál](https://archive.org/download/mmoiresdelacadm711859impe/mmoiresdelacadm711859impe.pdf)
má titul VII. řady, I, č. 9, 1859, přednes 29. dubna a tisk na
rubové straně červenec 1859. S. 4 po konečné nerovnosti výslovně
přechází ke dvěma spojitým reálným funkcím na témž intervalu:
součin integrálů jejich čtverců je alespoň čtverec integrálu součinu.
Sazba používá ostrou nerovnost a bezprostředně doplňuje rovnost
pro proporcionální funkce. Přechod přes stejně dlouhé podintervaly
má v obou členech stejný kvadrát délky, bez dodatečné konstanty.

[Schwarzův primární přetisk](https://archive.org/download/gesammeltemathem01schwuoft/gesammeltemathem01schwuoft.pdf)
z roku 1890 na s. 223 identifikuje původní Acta Societatis
Scientiarum Fennicae XV, 315–362, s datací 31. října 1885.
Samostatný finský ročník nebyl kolacionován. Na s. 251 autor
definuje A, B, C jako dvojné integrály phi², phi*chi, chi²
nad společnou oblastí. Integrál čtverce alpha*phi+beta*chi
dává kvadratickou formu A*alpha²+2B*alpha*beta+C*beta² a (21),
AC−B²>0, za autorova předpokladu nekonstantního podílu funkcí.
Moderní slabá nerovnost AC−B²>=0 plyne již z nezápornosti integrálu.
Pro obecné funkce s integrovatelnými čtverci se nezávislost potřebná
k ostré nerovnosti chápe až na množinu nulové míry. Toto je naše
upřesnění, nikoli výslovná dodatečná podmínka vytištěná na s. 251.
Historická atribuce integrálního rozšíření v TAOCP je doložena.

Známý dodatek z 1. července 2022 uvádí právě oba tyto prameny.
Známá oprava z 15. prosince 2001 mění v důkazu 46 horní mez
vnitřních indexů z m na n. Čtyři vrstvy errat jsou zachyceny
v agentově extraktu a hashovaných závislostech. Žádný z těchto
již veřejných zásahů se nevydává za nový nález.
