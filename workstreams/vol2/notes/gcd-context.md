# §4.5.2: historický a bibliografický kontext

Kontrola 2026-11-02 až 2026-11-03. Tato poznámka doplňuje matematické
bloky `gcd-basic.md`, `gcd-probability.md`, `gcd-extensions.md`,
`gcd-model.md`, `gcd-research.md`, `gcd-extremal.md`,
`gcd-variants.md`, `gcd-arithmetic.md` a `gcd-text.md`.
Původní stránky knihy 333–353 a příslušné opravy byly zobrazeny.
U historických odkazů níže odlišujeme přečtený obsah, pouhá metadata
a neověřené prvenství. Uzavření tohoto kontextového bloku neznamená
přezkoumání celých citovaných monografií ani vyřešení úlohy 32.

## Eukleidés a starší tradice

[Joyceova edice VII.1](https://mathcs.clarku.edu/~djoyce/elements/bookVII/propVII1.html)
řeší případ, kdy postupné odčítání skončí jednotkou: společný dělitel
původních čísel by musel dělit i jednotku. [VII.2](https://mathcs.clarku.edu/~djoyce/elements/bookVII/propVII2.html)
pracuje s dvojicí, která má společného dělitele většího než 1, nalezne gcd
a dokáže jeho maximalitu. Každý jiný společný dělitel navíc dělí
všechny zbytky, a tedy i nalezený gcd. Obě přeložené
propozice byly přečteny celé; jejich spojení odpovídá Knuthově
parafrázi. Moderní redakční komentář není vydáván za antický text.
Původní řecký rukopis jsme nezkoumali. Známá oprava z roku 1999
na straně 335 správně mění volbu F na předpoklad, že F dělí E.

[Aristotelovy Topiky VIII.3 v překladu MIT](https://classics.mit.edu/Aristotle/topics.8.viii.html)
obsahují argument o rovnoběžce, poměrech a vzájemném odčítání.
Přečten byl tento odstavec, nikoli celé dílo. Překlad neobsahuje
výslovný úplný algoritmus pro gcd. [Materiály MIT k řecké matematice](https://ocw.mit.edu/courses/es-113-ancient-greek-philosophy-and-mathematics-spring-2016/pages/readings/)
odkazují na totéž místo 158b v souvislosti s anthyfairésí, tedy
opakovaným vzájemným odčítáním. To odpovídá opatrnému Knuthovu
slovu „hinted“, nikoli tvrzení o doloženém autorství algoritmu.

U citace von Fritze byl ověřen původní [obsah časopiseckého čísla](https://www.jstor.org/stable/i307223):
*The Discovery of Incommensurability by Hippasus of Metapontum*,
Annals of Mathematics 46 (1945), 242–264. Celý článek nebyl přečten.
Knorrovu *The Evolution of the Euclidean Elements* (1975) dokládá
[dobová nakladatelská inzerce](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9DB1C5CF7BFFFFCA126ED1A5AA901950/S0007087400014849a.pdf/bjh-volume-9-issue-3-cover-and-back-matter.pdf),
nikoli nový audit jeho historického argumentu. Knuth sám podává
předřecké a pythagorejské atribuce jako nejisté; prvenství zde
nezvyšujeme na prokázaný fakt.

Knuthův vlastní [stanfordský přehled z roku 1976](https://bitsavers.retropc.se/pdf/stanford/cs_techReports/STAN-CS-76-562_EarlyDevelPgmgLang_Aug76.pdf)
v bibliografii potvrzuje *Ancient Babylonian Algorithms*, CACM 15
(1972), 671–677, a opravy CACM 19 (1976), 108. Byl ověřen odkaz,
nikoli celý původní článek nebo klínopisné tabulky. Rétorické
označení Eukleidova postupu za předka algoritmů čteme spolu
s bezprostřední zmínkou o starších babylonských postupech.

## Čínský postup, Harris a Lebesgue

Mikamiho *The Development of Mathematics in China and Japan*
(1913), tištěná strana 11, byla vizuálně přečtena v původním skenu.
Obsahuje půlení, odečítání, opakování do rovnosti i příklad
49/91 = 7/13. Knuthův překlad na 340–341 odpovídá tomuto prameni.
Kam přesně se má instrukce opakování vracet, Knuth výslovně
označuje za nejasné; nejde tedy o bezvýhradné historické připsání
moderního binárního algoritmu. Starověký čínský originál ani
Vogelův překlad z roku 1968 nebyly samostatně přečteny.
Doklady: `sources/mikami-1913.json`, `sources/mikami-1913-p11.pdf`.

Harrisův článek z roku 1970 je obsahově prověřen v `gcd-extremal.md`.
Lebesgueův původní článek z roku 1847 byl nyní vizuálně přečten
na stranách 497, 504, 505 a 517. Popis na 504–505 opravdu používá
liché podíly, sudé zbytky s oběma znaménky a odstranění mocniny
dvou ze zbytku. Historický odkaz na tuto variantu je tedy správný.
Bibliografický rozsah však má být **497–517**, nikoli 497–520.
Na 518 začíná jiný článek Serreta; jeho první stránka byla také
zobrazena. Jde o nový potvrzený nález [C0129](C0129-lebesgue-pages.md).
Zbytek těchto dvou článků není tímto blokem matematicky auditován.

## Indický rozšířený algoritmus

Datta a Singh, *History of Hindu Mathematics*, díl II (1938),
jsou dostupní v kombinovaném přetisku z roku 1962. Tiráž přetisku
byla vizuálně přečtena a výslovně odlišuje obě vydání. Z citovaného
rozsahu 89–116 byly vizuálně přečteny strany **90, 93, 94, 99, 100**.
Na 90 je vysvětlení označení kuttaka jako drcení; na 93–94
Árjabhátovo pravidlo a komentář s postupným dělením a zpětným
skládáním koeficientů. Na 99–100 navazuje Bháskara I.
To podporuje citovanou tradici rozšířeného Eukleidova postupu,
nikoli tvrzení, že starý zápis je doslovný program X.

Staré datování Bháskary I v této knize nepřebíráme. Plofkerová,
*Mathematics in India* (2009), na vizuálně přečtené straně 136
uvádí komentář z roku **629**. Tím je podpořena známá oprava
Knuthova šestého století na sedmé z roku 2002. Vizuálně přečtené
strany 317–318 také odlišují údaj, že Árjabhátovi bylo 23 let
v roce 499, od jistého data sepsání celého díla; odpovídá tomu
pozdější Knuthovo přibližné datování kolem roku 500.
Údaje o původu a působení nejsou zaměňovány s jednoznačně
doloženým rodištěm. Neprověřovali jsme sanskrtské rukopisy.
Metadata, přesné stránky, kontrolní součty a uložené obrazové
doklady: `sources/datta-singh-1962-gcd.json` a
`sources/plofker-india-gcd.json`.

## Obecnější celočíselné okruhy a vysoká přesnost

Gaussova celá čísla jsou čísla a+bi s celými a,b a i²=-1.
Jejich norma je a²+b². Pro nenulové v zaokrouhlíme obě souřadnice
u/v na nejbližší celá čísla a dostaneme q. Pak r=u-qv splňuje
norm(r)<=norm(v)/2. Společní dělitelé se zachovávají a kladná
celočíselná norma zbytků klesá: Eukleidův postup tedy skončí.
Výsledný gcd je určen až na násobení jednotkami 1,-1,i,-i;
nejde o největší komplexní číslo podle uspořádání. To přímo
dokládá základní tvrzení o existenci této varianty na straně 345.

Rozsah bibliografické kontroly dalších odkazů:

| Odkaz | Skutečně ověřený rozsah |
|---|---|
| [Hurwitz, Acta Math. 11 (1887), 187–200](https://link.springer.com/article/10.1007/BF02612324) | Nakladatelský záznam, název, autor, rok a stránky; celý článek nepřečten. |
| [Kaltofen–Rolletschek, Math. Comp. 53 (1989), 697–720](https://users.cs.duke.edu/~elk27/bibliography/89/KaRo89.pdf) | Původní první strana 697 vizuálně přečtena, abstrakt a úvod potvrzují uvedený obor; další algoritmy nejsou nově auditovány. |
| [Knopfmacher–Knopfmacher, BIT 31 (1991), 286–292](https://doi.org/10.1007/BF01931288) | Nakladatelská metadata a abstrakt pro komplexní kvadratická tělesa; plný důkaz nepřečten. |
| [Cohen, A Course in Computational Algebraic Number Theory (1993)](https://link.springer.com/book/10.1007/978-3-662-02945-9) | Nakladatelský obsah potvrzuje kapitolu 2 o lineární algebře a mřížkách, strany 45–107; nikoli audit celé kapitoly. |

Lehmerův postup a rozšíření soustav mají vlastní obecný důkaz
v `gcd-extensions.md`; dostupnost původního článku z roku 1938
není zaměňována s jeho úplným přečtením. Číslo 99.856 procenta
na straně 345 odpovídá 100*(1-log2(1+1/1000)). Je to předběžný
odkaz na limitní rozdělení typických podílů v Eukleidově algoritmu,
nikoli rozdělení prvního podílu libovolně zvolených vstupů.
Vlastní důkaz tohoto rozdělení patří do navazující §4.5.3.

## Brocardův dodatek k úloze 36

Byla vizuálně přečtena titulní strana svazku 6 (1880) a strany
145–147 Brocardovy *Propriété d'une série de triangles*.
Na 146 je posloupnost 1,3,5,11,21,43,85,171,341 a její rekurze
u_(n+1)=u_n+2u_(n-1), u_0=1,u_1=3. Když
a_j=(2^j-(-1)^j)/3, jde přesně o u_n=a_(n+2).
Catalanova poznámka s koeficienty 4/3 a -1/3 potvrzuje uzavřený
tvar. Bibliografický dodatek Knuthových errat z roku 2020 je
tedy doložen. Zbytek geometrického článku na 148–151 nebyl
přečten a není prohlašován za prověřený.
Doklady: `sources/brocard-1880.json` a přiložený výřez PDF.

Všechny čtyři vrstvy errat jsou zmapovány v `gcd-inventory.md`;
nový nález C0129 má samostatný záznam obsahového hledání.
Výsledkem tohoto kontextového bloku není nové tvrzení o historickém
prvenství. Nejnovější fyzický dotisk a priorita nálezů nejsou ověřeny,
žádný návrh hlášení nebyl odeslán.
