# Pallo, Tamari a zbývající Wardův pramen

Root přijal celý zmrazený `parallel/other-trees-originals`:
`MANIFEST.json`, SHA-256
4b50787bcd2e53e42b8106f2e5e6a2d67717e46418c200a59068ed33f8241002,
88 souborů a 32 externích vstupů. Všechny délky a hashe souhlasí.
Dřívější Burksův podmanifest je součástí celku, zůstal nezměněn
a jeho uzavření X0816 se zde nepočítá jako další výsledek.

Root přečetl celé předání, čtecí protokol, stavy úloh, pramenný
inventář a všechny tři nové obsahové poznámky. Přímo obrazově
četl Palla 1993 na 341–343 a 348, Tamariho 1964 na 91–93 a 107,
reprodukci původní Fig. 1, Stasheffův preprint na PDF 1, 4 a 41
a knižní 362 a 577. Přečetl také celý krátký text Rostovy stránky
o původu reprodukce. Rozsah agentovy další četby je samostatně
v `READ_LOG.json`; nejde automaticky o další root četbu.

## Pallo: přesný převod souřadnic

Pallo 1993 definuje na s. 342 rozšířený binární strom: každý
vnitřní uzel má dvě děti a vnější list nemá žádné. Vnější listy
čísluje zleva. Pro i=1,...,n je w_T(i) počet vnějších listů
největšího podstromu končícího i-tým vnějším listem; poslední,
(n+1)-ní list do posloupnosti nezahrnuje.

Kniha na 577 počítá c_i jako počet vnitřních uzlů levého podstromu
i-tého vnitřního uzlu v symetrickém pořadí. Tento levý podstrom
je právě Pallowým největším podstromem končícím i-tým listem.
Protože v rozšířeném binárním stromu je vnějších listů o jeden
více než vnitřních uzlů, převod je w_T(i)=c_i+1. Root porovnal
definice v originálech; oba číselné zápisy bez posunu nesplývají.

Rotace na s. 343 mění a(bc) na (ab)c. Věta 2.1 charakterizuje
dosažitelnost porovnáním w po složkách; důsledek 2.2 dává svaz
a minimum po složkách jako průsek. Oba přímo odkazují na Palla
1986, přesně identifikovaného referencí [11] na s. 348.
To poskytuje přímou autorskou oporu reprezentace a souvislosti
se svazem. Vlastní nový algoritmus Möbiovy funkce na 344–347
ani původní algoritmy číslování z roku 1986 nebyly nově auditovány.

Původní Pallo 1986, Computer Journal 29, 171–175, stále chybí.
Správné dubnové číslo IA je nyní přesně určeno, jeho PDF je však
označeno private. Nová veřejná OUP cesta vrátila 403. Tato metadata
nejsou obsahem článku; přijaté důkazy úlohy se kvůli tomu neotevírají.

## Tamari: zavedení uspořádání a pozdější důkaz

Tamari 1964 na s. 92 výslovně definuje uzávorkování n+1 písmen
a orientovaný přesun a(bc)->(ab)c, včetně použití uvnitř většího
uzávorkování. Na s. 93 říká, že svazová věta i základní značení
byly v jeho pařížské disertaci z roku 1951 bez důkazu. Hlavní
kroky pozdějšího důkazu připisuje Haye Freedmanové, 1958.
Knižní slovo introduced se s tím nevylučuje: zavedení relace
a dokončení důkazu svazové vlastnosti nejsou totožná událost.

Jeho vlastní reference [2] na 107 výslovně rozlišuje disertaci,
její rozmnoženou část a publikovaný výtah BSMF 82 (1954), 53–96.
Poslední podle autora nemá přímé odkazy k nynějšímu tématu.
Proto jej nepovažujeme za náhradu celé disertace. Rootův závěr
stojí na tomto přímém sdělení; nezakládá se na absenci slova v OCR.

Původní Fig. 1 je čitelná v reprodukci Stasheffovy s. 46 (2012):
vložený původní list má číslo 12, orientovanou asociativní úpravu
a diagramy včetně pětiúhelníku. Rostova stránka ji rozlišuje od
svých nových kreseb. Stejný originál s výslovnou atribucí disertaci
je na s. 4 Stasheffova arXiv:1809.02526v2 a reference [169] na 41
uvádí Paris 1951. Skutečná získaná verze je říjen 2018; název
lokálního souboru obsahující 2019 není údaj o verzi.

Historická opora knižní věty je tedy nově přímá a podstatná.
Souvislý původní text disertace 1951 nadále nemáme, reprodukce
jednoho diagramu není četbou celého spisu. Absolutní prvenství
se neprohlašuje za vyčerpávajícím průzkumem uzavřené.

## Ward a celkový stav

Ward–Zedan §5 stále chybí. Nový doplněk nepřinesl žádnou původní
stranu článku; X0692 už měl jen přesný indexovaný text části 5.6.
DNS chyba nové univerzitní adresy, 429 archivního replay a 403
u veřejné ACM varianty nejsou důkazem neexistence dostupné kopie.
Zachované konkrétní dotazy se bez nové opory nemají opakovat.

Čtyři vrstvy errat byly agentem zkontrolovány a root přečetl
jejich přesný výpis; známé P-c, doplnění odpovědí 14/15 a oprava
jména Hussein zůstávají rozlišeny. X0296, X0297 a celé úlohy
14, 15, 19 nadále zůstávají partial pro vymezené pramenné zbytky.
Nový X0818 uchovává tuto revizi a podstatně přesnější doklady.
Žádný nový nález TAOCP ani opakovaný matematický test nevznikl.
