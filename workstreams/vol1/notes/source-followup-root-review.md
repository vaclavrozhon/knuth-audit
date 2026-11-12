# Kořenové převzetí nových pramenných dokladů

1. listopadu 2026. Přečteno všech šest stabilních předání
otter-1948, raney-1960, riordan-1966, height-enumeration-sources,
joyal-1981 a hwang-hu-tucker-access. Hashe čtyř nových PDF souhlasí
s uvedenými SHA256. Přesný snapshot jednotlivých stabilních dokladů
je results/source-followup-root-manifest.json. Celá pracovní složka
source-followup zůstává aktivní, starší zmrazené důkazy se neměnily.

Kořenová matematická revize převodů:

- Otter: A=x psi, takže koeficient odmocniny pro A je alpha^(3/2)
  krát velikost Otterova b. Po dosazení abs(b)=sqrt(2 beta/alpha)
  se hlavní asymptotická konstanta mění na alpha sqrt(beta/(2pi)),
  přesně jako v knize. Otterova logaritmická derivace dává přímo
  obě rekurence s_nk a a_n; není to pouze citace názvu článku.
- Raney: otočení pořadí převádí prefixové zápisy na knižní postfixové.
  V obou případech se musí počítat cyklické pozice, nikoli počet
  různých posunutých slov. Dvojí počítání dává faktor f/N i při
  periodickém slovu, proto souhlasí také lesní rozšíření.
- Riordan: přidáním pevně označeného listu ke kořeni mají všechny
  původní vrcholy neorientovaný stupeň o1 vyšší než počet dětí.
  Ze všech nových označených stromů má přidaný štítek stupeň1 v
  podílu (k0+1)/(n+1). Tento faktor přesně vykrátí rozšířený
  multinomický jmenovatel a dává knižní n!(n−1)!.
- Výška: neuspořádané větve vedou k obyčejnému Eulerovu součinu,
  větve s rozdělenými štítky k exponenciální řadě. Podmínka pevného
  štítku kořene odstraňuje faktor n. Neztotožňujeme výšku či průměr
  stromu se součtem hloubek v úloze o délkách cest.
- Joyal: součin rozděluje štítky, substituce je rozklad na neprázdné
  komponenty, derivace přidává nový zvláštní štítek. Labelleova
  rovnost počtů na n a n−1 štítcích dává faktor1/n v Lagrangeově
  inverzi. Je správně odlišeno označené a neoznačené počítání.

Přímé čtení původních stran provedl podagent v rozsazích přesně
uvedených v jednotlivých poznámkách. Kořen přečetl tyto mapy a
přezkoumal výše uvedené převody; netvrdí druhé úplné čtení všech
stovek stran ani novou certifikaci vedlejších cizích vět.
Úspěšné matematické testy se neopakovaly.

Nové doklady uzavírají poslední pramenné mezery úloh §2.3.4.4-2,
4 a20. Úloha32 stále čeká na Peirce, Dvoretzky–Motzkin a Bergmana;
závěr hlavního textu stále na Gooda a relevantní části Species.
Hwangovy strany124–127 a Hu–Tucker518 zůstávají výslovně partial.
Abstrakt, bibliografická metadata ani neúspěšný HTTP požadavek
se nepovažují za přečtený obsah. Nový nález tímto blokem nevznikl.

## Sedmé předání: Cayley1857

Přečteno celé `cayley-leaves-1857.md`; samostatný snapshot je
v `results/source-followup-cayley-root-manifest.json`. Součinová
rovnice počítá prázdnou multimnožinu, jediný podstrom a alespoň
dva podstromy, tedy přesně `1+C+(C-x)=1+2C-x`. Podmínka alespoň
dvou dětí zaručuje konečnost koeficientů, neboť strom s `n` listy
má nejvýše `n-1` vnitřních vrcholů. Tím je atribuce původního
modelu na245–246 z1857 potvrzena; článek1859 se správně odlišuje.

Toto uzavírá pouze Cayleyovu část úlohy5. Samostatná MacMahonova
pasáž1891 o rovnosti sériově paralelních sítí a přesném citovaném
rozsahu stále chybí. Úloha5 proto zůstává celkově partial.

## Katz a Rubin–Sitgreaves

Kořen přečetl oba stabilní podklady `katz-1955.md` a
`katz-priority-candidate.md`, ověřil jejich převody a přímo
prohlédl knihu590, Katze516, původní titul zprávy19A a její
tištěnou stranu8. Přímé týmové čtení zahrnuje všech512–517
u Katze a titul i1–9 u Rubina–Sitgreavesové; ne celý51stránkový
soubor zprávy. Přesný snapshot je v
`results/source-followup-katz-root-manifest.json`.

Pravděpodobnost jediného cyklu podmíněná počtem `j` cyklických
bodů je `1/j`; jejím vynásobením zákonem počtu cyklických
bodů a sečtením dostaneme přímo vzorec knihy. Katzovo sčítání
vrstev dává týž výsledek, včetně cyklu délky `N` bez stromů.
Obsahový odkaz je tedy uzavřen X0589.

Zpráva datovaná22. ledna1954 výsledek výslovně obsahuje,
a Katz tuto shodu přiznává. Přesto datum přijetí Katzova
článku není datem jeho soukromého objevu. Přesné znění „first
obtained“ proto vedeme jako C0071 candidate a nepřisuzujeme
automaticky absolutní prvenství nikomu jinému. Celková úloha17
zůstává partial pouze pro historickou prioritu; již dříve
potvrzená samostatná chyba C0059 se tím nemění.

## MacMahon1891 a Schröder1870/1871

Kořen přečetl celé oba nové stabilní podklady a přezkoumal jejich
obecné převody. Snapshot dokladů je
`results/source-followup-macmahon-schroder-root-manifest.json`.
Přímé úplné čtení primárních článků provedl podagent, přesné rozsahy
jsou330–346,361–376 a oprava179–180. Kořen netvrdí nové druhé
čtení všech těchto stran ani úplný audit ostatních vět článků.

MacMahon používá asociativní a komutativní ekvivalenci zvlášť pro
sérii a paralelu. Její jednoznačný normální tvar je neuspořádaný
strom s alternujícími značkami S/P a alespoň dvěma dětmi každého
vnitřního uzlu. Zapomenutím značek dostaneme knižní c_n; pro n>1
má strom právě dvě označení, pro n=1 jediné. Explicitní multisetové
faktory původního článku vylučují záměnu za obyčejnou izomorfii
grafů nebo za rovnost výsledného číselného odporu. Citovaných330–339
je skutečně relevantní část delšího článku, nikoli chybný rozsah.
Spolu s CayleyemX0558 je tím celá úloha5 checked (X0591).

Schröderova rovnice F=z+F^2/(1−F) jednoznačně určuje řadu s F(0)=0.
Kořeny rovinného stromu mají alespoň dvě děti, které rozdělují
pevné pořadí listů na intervaly. To je přesně závorkování v původním
článku; duální strom disekce polygonu dává inverzní geometrický
převod. Případ n=1 je algebraický základ, nikoli běžný dvouúhelník.
Autor sám polygonální formulaci nepoužil; bijektivní ekvivalence
stačí k matematické atribuci, nikoli k tvrzení o jeho původním slovníku.
Oprava je vydána1871, přestože je podepsána v prosinci1870.
Kniha má opravenou hodnotu45. Schröderova část je checked (X0592),
úloha31 zůstává partial pouze kvůli dosud nepřečtenému Acerbimu2003.

## Wedderburn1922

Kořen přečetl celé stabilní předání a ověřil přesný posun velikosti:
doplnění chybějících dětí mění každý původní vrchol na vnitřní uzel
plného neuspořádaného binárního stromu. Při n vnitřních uzlech je
n+1 listů. Současné odstranění všech listů je inverzní operace;
včetně prázdného stromu dostaneme g_n=N_(n+1). Neuspořádaná dvojice
se počítá jako polovina počtu uspořádaných dvojic plus polovina
počtu pevných bodů jejich záměny. Tím se odvodí korekční člen
pro shodné podstromy bez předpokladu, že jsou všechny různé.

Dosazení W(z)=1−zG(z) do W(z²)=2z+W(z)² dává přesně druhou
rovnici knihy. Podagent přímo přečetl121–140, samotný obsahový
odkaz je doložen již121–122. Root necertifikuje veškerou vedlejší
externí komplexní analytiku. Úloha6 je tím checked (X0595).
Snapshot je `results/source-followup-wedderburn-root-manifest.json`.

## Acerbi2003

Kořen přečetl celé stabilní předání a nezávisle přepočetl rozklad
označení na první větvi. Označení u kořene přispívá S; označení
v prvním podstromu přispívá H krát alespoň jeden další podstrom,
tedy HS/(1−S). Odtud H=S(1−S)/(1−2S)=S²/z a
h_n=(s_n+s_(n+1))/2. Pro n=10 vychází310954, což se nesmí
ztotožnit s jistým čtením či vysvětlením dochované antické hodnoty.

Přímé čtení všech39 stran autorovy univerzitní verze provedl
podagent. Stránkování1–39 není časopisecké465–502. Obsah citace
a jeho explicitní historická opatrnost jsou doloženy; samostatná
kolace všech řeckých rukopisů se netvrdí ani ji knižní odkaz nevyžaduje.
Tím se uzavírá poslední vymezená pramenná mez úlohy31 (X0597).
Snapshot je `results/source-followup-acerbi-root-manifest.json`.

## Hwang1979, Hu–Tucker1971, Hu–Kleitman–Tamaki1979 a Glassey–Karp1976

Kořen přečetl všechna čtyři stabilní předání. Podagent přímo přečetl
Hwang124–127, Hu–Tucker514–518, HKT246–256 a Glassey–Karp368–378.
Kořen navíc přímo zkontroloval původní strany Hwang126–127,
Hu–Tucker518, HKT247/254 a Glassey–Karp371/376–377. Zbytek
Hu–Tucker519–532 není tímto čtením ani auditem abecedního algoritmu.
Veřejná archivní kopie vydavatelských PDF byla získána přesnými
HTTP rozsahy z ISO; původ a kontrola rozsahů jsou výslovně doloženy.
Snapshot je `results/source-followup-four-siam-root-manifest.json`.

Hwangův nejmenší zbývající stupeň je správný pro nezáporné váhy
v úloze10. Přesun přebytečných listů nejhlubšího uzlu k mělčímu
uzlu nezvětší cenu právě díky nezápornosti. Toto omezení nelze
odstranit: pro stupně2,3 a čtyři listy váhy−1 by předepsané greedy
pořadí dalo−6, opačné−7. Kniha v úloze10 nezápornost výslovně má.
Naproti tomu porovnání prefixových součtů v úloze16 platí i pro
reálné váhy: seřazené hloubky l_i mají nezáporné rozdíly
l_i−l_(i+1) a sumace po částech převádí cenu na jejich nezápornou
lineární kombinaci prefixů vah. Obě konkrétní pramenné mezery
uzavírá X0598, starý přístupový záznam X0557 je tím nahrazen.

Hu–Tuckerovo lemma3.1 na518 dokazuje minimální cenu mezilesa
po každém k sloučeních. Výměna dvou nejmenších vah do nejhlubších
sourozeneckých pozic a jejich kontrakce odečte pevné a+b; opačné
rozštěpení je vždy možné. Záměna používá (a−c)(D−d)<=0, nikoli
kladnost a. Vlastní širší důkaz pro reálné váhy je správný, ačkoli
originál zavádí kladné váhy. Poslední mez úlohy14 uzavírá X0599.

HKT věta1' má přesně slučování x(a+b) pro cenu sum w_i*x^l_i,
x>1. Stejná záměna používá (a−c)(x^D−x^d)<=0 a kontrakce cenu
zachovává. Příklad2 na254 souhlasí. Doplňková věta1 pro x<1 se
týká minimaxové ceny, proto se jí nesmí uzavřít Parkerovo připsání
součtové varianty. X0600 uzavírá jen HKT; úloha15 zůstává partial.

Glassey–Karp minimalizují prefixy seřazených vnitřních vah pro
nezáporné listy. Převod na každou neklesající konkávní cenu lze
přesně dokázat identitou sum min(s_j,a)=min_q(S_q+(m−q)a)
a lomenou interpolací na konečné množině argumentů. Pro listy
váhy1 zachovává Huffmanův krok seznam v intervalu [2^r,2^(r+1)]
s nejvýše jednou vahou, která není mocninou2. Z dvojice tvořící
uzel velikosti n lze vybrat mocninu2 v [n/3,2n/3); je jednoznačná
a rovná 2^ceil(lg(n/3)). Horní konec musí být otevřený a při
poměru1:2 se bere menší váha. Tím je ověřena i hraniční konvence
knižní rekurence. X0601 uzavírá konkrétní zdroj, ale nenahrazuje
odlišný článek HLP1929; úloha17 proto zůstává pramenně partial.

Nový nález zde není. Původní vlastní důkazy ani úspěšné konečné
testy nebyly opakovány; přibyly konkrétní pramenné doklady.

## Hardy–Littlewood–Pólya1929

Kořen přečetl celé stabilní předání, přímo větu8 na150 a titulní list
ročníku58. Všech osm původních stran145–152 četl podagent. Titulní
rok1929 potvrzuje již známou opravu; nezvyklá citace1930 uvnitř není
dostatečným důvodem změnit bibliografický rok bez dokladu distribuce.

Knižní slabé prefixové porovnání nevyžaduje rovnost celkových součtů,
kterou má původní věta. Přidáním rozdílu součtů k největší složce
menšího vektoru vznikne seřazený vektor se správnou rovností a stejnými
kratšími prefixy. Konvexní větu aplikujeme na−f; monotónnost f pak
vrátí změněnou složku. Opačný směr plyne z min(x,t) a přesné identity
P_k(a)=max_t(sum_i min(a_i,t)−(n−k)t). Kořen oba směry přezkoumal.
Matice se součty řádků/sloupců1 není pro tento vlastní důkaz potřeba;
její úplný důkaz článek výslovně odkládá. Tyto meze se nepředstírají.

X0648 spolu s X0601 uzavírá poslední zdrojovou mezeru úlohy17;
vlastní stromové lemma pro reálné váhy zůstává samostatnou evidencí.
Snapshot je `results/source-followup-hlp-root-manifest.json`.

## Parker1980 a erratum1998

X0652 eviduje nové stabilní předání. Podagent přímo přečetl všech
470–489 a jednostránkové erratum317. Kořen přečetl celou poznámku
a původní obrazy474,483,486 a erratum317. Vyjmuté PDF mají hashe
uvedené v `results/source-followup-parker-root-manifest.json`;
jiné články původních ročníků zde neauditujeme.

Definujme F_r(u,v)=r(u+v). Rozdíl dvou stran Parkerovy QL3 je
r(r−1)(a−b). Pro0<r<1 a a<b je kladný, takže nelze tuto část
článku použít dosazením k doložení knižní varianty minimalizace.
Erratum zpřísňuje QL2 a doplňuje ji do dalších vět; tuto překážku
neodstraňuje. Zmínka na486 se týká jiného průměrového kritéria,
nikoli samostatně minima daného součtu. Atribuci konkrétní
Parkerovy poznámky proto ponecháváme source-partial, přestože
přístup k tomuto článku a erratu už není překážkou.

Doplňkový protipříklad k větě8, G(z)=−sum z_i, a=(1,1), b=(2,2),
má nulový derivovaný Schurův výraz, ale obrácené porovnání hodnot
při slabém porovnání prefixů. Chybí neklesání nebo rovnost součtů.
Knižní úloha17 neklesání požaduje a má samostatný důkaz; tento
problém cizího článku není novým nálezem TAOCP.

## Schwartzova zpráva 1963: doplnění 2. listopadu 2026

Převzata stabilní poznámka `parallel/source-followup/notes/schwartz-1963-report.md`.
Root přímo přečetl titul a předmluvu (PDF 3 a 5), původní strany
48, 50, 54–55, 173 a diagram 4 na 215; porovnal původní knižní
404 a 595. Širší podagentův přesný čtecí rozsah je v předání.
Originál ASD-TDR-62-265, Part II, má výslovné datum 1 June 1963;
číslo zprávy neznamená rok jejího vydání. Předmluva připisuje
Kallickovi základní vývojové diagramy kódovací rutiny.

Pravidlo na 48 vloží nově spojenou váhu za dříve přítomné stejné váhy.
Závěr na 50 výslovně uvádí současné minimum součtu délek a největší
délky mezi optimálními kódy. To dokládá formulaci a historickou
souvislost; vlastní již převzatý obecný důkaz se neopakoval a krátký
argument originálu o deficitech hladin není zde certifikován ve všech
implicitních krocích. Doménou zprávy jsou frekvence či pravděpodobnosti;
záporné váhy a Markowského obecnější kritérium tím nejsou doloženy.

Kanonický prefixový kód je soubor binárních slov, kde žádné není
začátkem jiného; slova stejné délky se berou po sobě v binárním pořadí.
Označíme-li jejich počet b_l a první disponibilní hodnotu délky l
jako s_l, diagram dává s_1 = 0 a s_(l+1) = 2*(s_l+b_l).
Na diagramu 215 je po posledním slovu skupiny nejprve přičtena
jednička a teprve pak proveden posun. Zkratku „add binary 10“ na 55
proto nelze číst jako samotné přičtení čísla 2. Prázdná skupina
pouze posouvá, pomocná vedoucí jednička je značkou délky.

Převod slova hodnoty a a délky l na dyadický interval
[a/2^l,(a+1)/2^l) přímo vysvětluje prefixovou podmínku a úplnost
při Kraftově součtu 1. Krátká slova přiřadíme velkým vahám; zrcadlení
všech větví pak dává rostoucí váhy zleva doprava, jak požaduje úloha 4.
Případ jediného listu řeší vlastní knižní důkaz samostatně.

Obě přesné časopisecké sazby 1964 zůstávají nepřečtené. X0505 a
X0509 proto zůstávají partial, ale už nikoli kvůli úplné absenci
dobového autorského dokladu. Nový X0661 eviduje tento vymezený posun.
Manifest `results/source-followup-schwartz-root-manifest.json` váže
stabilní poznámku, primární PDF, text, obrazy a metadata stažení.
