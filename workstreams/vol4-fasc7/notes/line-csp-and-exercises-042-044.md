# Relace(21–22), všechny čtyři výsledky a úlohy42–44

Původní p13/file28, zadání p117/file132 a odpovědi p167–168/file182–183
byly zobrazeny. Všechny tři obrázky(23) byly navíc zobrazeny ve větším
výřezu `images/file-028-equation23.png`. Převzatými uzavřenými vstupy
jsou pouze celý graf a orientace(20), úplná Tabulka1 a prostorový
model104(d); jejich konkrétní důkazy jsou v `hc-network-020.md`,
`cubie-junctions-exercise-041.md` a `histoscape-projection-fig104d.md`.
Níže se tyto důkazy znovu nepočítají, ale ověřují se nové tištěné kroky.

## L22-1 — jedna proměnná na každou čáru a všechny relace

Každá neorientovaná čára má právě jednu proměnnou, pojmenovanou jejími
konci v abecedním pořadí. Hodnoty + a − jsou nezávislé na orientaci;
`>` znamená šipku od prvního jména ke druhému a `<` opačnou. Volba
jedné hodnoty každé proměnné je tedy bijektivní s označeními všech čar.
Podmínka každého junctionu přesně říká, že jeho incidentní označení
patří do Tabulky1. Tím je dokázán obecný převod na CSP v úvodním
odstavci p13, nikoli jen existence některého platného obrázku.

Úplný seznam26 hran byl nezávisle ověřen v N20-2. V(21) je každá
z nich uvedena právě jednou a žádná další. Vstup má19 junctions,
proto19 lokálních podmínek. Při zápisu O pro šipku od junctionu
a I pro šipku k němu jsou celé relace Tabulky1:

```
T: O+I O-I OOI OII
V: I+ IO +O O- OI -I
W: O+I -+- +-+
Y: IO- O-I -IO --- +++
```

U Y se začátek cyklického pořadí může zvolit libovolně; množina řádků
je vůči cyklickému posunu uzavřená. Pro větev j→k přelož O na `>`
a I na `<`, je-li j<k, a oba symboly vyměň, je-li j>k. Znaménka
se nemění. Na každé z těchto pozic tedy musíme obrátit šipku:

| j | pořadí sousedů v(20) | obrácené pozice, od1 |
|---|---|---|
| a | bc | žádná |
| b | eda | 3 |
| c | adm | 1 |
| d | bgc | 1,3 |
| e | bfg | 1 |
| f | qhe | 3 |
| g | deh | 1,2 |
| h | fjg | 1,3 |
| i | jk | žádná |
| j | lih | 2,3 |
| k | iln | 1 |
| l | jsk | 1,3 |
| m | cno | 1 |
| n | kmp | 1,2 |
| o | mpr | 1 |
| p | on | 1,2 |
| q | sf | 2 |
| r | os | 1 |
| s | rlq | 1,2,3 |

`check_line_csp22.py` provede právě tento překlad pro každý jednotlivý
řádek a porovná celé výsledné množiny s nezávislým přepisem originálu.
Všech19 seznamů proměnných a všech80 tištěných tuples souhlasí;
úplné řádky jsou v `results/line-csp22.json` pod `relations`.
Například b dostává `>+>,-+-,+-+`, neboť třetí větev je ba, ale
proměnná ab je orientována opačně. U e dostáváme `>>-,<-<,-<>`,
spolu se `---,+++`, přesně tištěnou množinu, byť v jiném pořadí.
Poznámka vysvětlující zkrácené zápisy dvojic a trojic je prostá
jednoznačná konkatenace těchto čtyř jednopísmenných hodnot.

## L22-2 — oba pomocné kroky pod(22)

Kdybychom zavedli i opačně pojmenovanou proměnnou ba, její doménu
určuje ab jednoznačně involuce `+↦+,−↦−,<↦>,>↦<`.
Relace `(ab,ba)∈{++,--,<>,><}` tedy přesně vynucuje stejnou fyzickou
čáru. Pro všech26 hran lze každé řešení původního modelu právě jedním
způsobem rozšířit na52 proměnných; opačně restrikce dává původní
řešení. Dodatečných26 proměnných a26 vazeb je eliminovatelných.
To odůvodňuje uvedenou úsporu reprezentace; není zde tvrzena
univerzální nerovnost času libovolných dvou heuristických řešičů.
V příkladu seznamu je známá oprava `bc→bd`, viz níže.

Celá podmínka n je
`(kn,mn,np)∈{<+<,<-<,<<<,<><}`. Prostřední souřadnice probíhá
celou doménu, zatímco krajní jsou vždy `<`. Je proto ekvivalentní
právě `(kn,np)∈{<<}`, při libovolné hodnotě mn. Není to pouhá
projekce ztrácející vazbu: plná relace je kartézský součin jediné
dvojice s celou prostřední doménou. Ušetří se čtyři ternární řádky
proti jedinému binárnímu, tedy12 uložených symbolů proti2. Tento
argument platí pro každé T, nezávisle na zbytku sítě.

## L22-3 — úplnost právě čtyř řešení ruční propagací

Každý následující závěr je vynucen konkrétními již zkontrolovanými
relacemi, ne odhadnut z obrázku. Z n máme kn=np=`<`. Z k pak ik=`<`,
kl=+. Relace i dovoluje při ik=`<` jen ij=`>` nebo−, zatímco j
dovoluje na prostřední pozici ij jen+ nebo−. Proto ij=− a j vynutí
jl=hj=+. Následně h vynutí fh=gh=+. Z g vychází dg=+,eg=−;
z d vychází bd=cd=+. Z l dostáváme ls=+.

Z p při np=`<` může být op pouze `>` nebo+; z o smí být prostřední
op jen+ nebo−. Proto op=+, a o dává mo=or∈{`<`,−}.
Z b plyne ab=be∈{`>`,−}; z e při eg=− plyne be=ef∈{`>`,−};
f při fh=+ dává ef=fq. Z c plyne ac=cm∈{`<`,−}.
V m mají cm a mo obě doménu{`<`,−}, takže zbývají pouze `<-<`
a `---`; proto mn=− a cm=mo. Z s při ls=+ zbývají jen `<+>`
a `-+-`, tj. `(rs,qs)=(<,>)` nebo `(−,−)`.

Všech26 proměnných se tím dělí na následující pevné hodnoty a tři
zbylé skupiny:

```
bd cd dg fh gh hj jl kl ls op = +
eg ij mn = -
ik kn np = <
u = ab = be = ef = fq,          u ∈ {>, -}
v = ac = cm = mo = or,          v ∈ {<, -}
(rs,qs) ∈ {(<,>),(-,-)}.
```

Zbývající a zakazuje právě dvojici(u,v)=(−,−). Z q plyne, že
qs=− vyžaduje u=`>`; z r plyne, že rs=− vyžaduje v=`<`.
Naopak po splnění těchto tří omezení vyhovuje každá uvedená
proměnná všem19 relacím: to lze dosadit do výše uvedených
zbytkových řádků. Jsou proto přesně čtyři případy:

| u | v | rs | qs | výklad |
|---|---|---|---|---|
| − | < | < | > | zadní stěna |
| > | − | < | > | levá stěna |
| > | < | − | − | podlaha |
| > | < | < | > | volný objekt104(d) |

Doplňkový strojový certifikát používá pouze podporové škrtání tuples
a rozvětvení na ab, potom případně ac, potom případně qs. Jeho celý
strom má7 uzlů a4 listy; žádná prohledávací část nebyla přeskočena.
Invariant škrtání: hodnota, kterou žádný slučitelný řádek lokální
relace nepodporuje, nemůže být v řešení. Žádné řešení se neodstraní.
Domény se jen zmenšují, takže konečně skončí; každé větvení partitionuje
zbývající řešení podle jediné hodnoty proměnné. Každý list se ověří
dosazením do všech relací. To je rovněž úplný nezávisle čitelný
certifikát v `propagation_tree`, ne výčet4^26 přiřazení. Běh nice15
trval pod sekundu a staré úspěšné geometrické kontroly neopakoval.

## L22-4 — všechny tři původní obrázky(23) a jejich výklad

Již uzavřený model104(d) se přes N20-4 přiřadí všem19 pojmenovaným
junctions. Pro každou z26 čar se přesně určí její fyzická hrana
a směr parametrizace. Překlad všech již ověřených značek104(d)
dává právě poslední řádek tabulky L22-3.

`check_line_fig23.py` zpracuje všechny původní cesty18–78,79–139,
140–200 z `sources/file-028.svg`. U každého ze tří pohledů se ověří
každý černý tah i každý bílý zakrývající polygon proti uzavřenému
pohledu; všechny intervaly všech30 fyzických hran se přesně rovnají.
Každý původní koncový bod je přiřazen jednoznačně; toleruje se pouze
zaokrouhlení sazby<0.02 bodu, nikoli změna kombinatoriky. Reference
afinní rovinné mapy jsou rozprostřeny po celém obrázku, aby se
nezesilovalo zaokrouhlení tenkého horního rovnoběžníku.

V každém pohledu se samostatně přečte všech45 značek: krátký červený
příčný tah je+, bílá mezera podél černé čáry je− a trojbodový
červený hrot určí orientaci šipky. Každý tah má právě jednu incidentní
hranu; prověří se i překrytí pozdějšími bílými polygony. Všech45
značek každého pohledu přežívá a všechny viditelné hrany jsou
označeny. Obě značky na téže hraně vždy souhlasí. Celé výsledky
jsou v `results/line-fig23.json`.

Zleva se mění proti104(d) právě:

1. qs,rs na−;
2. ac,cm,mo,or na−;
3. ab,be,ef,fq na−.

Jsou to přesně zbylé tři řádky L22-3 v opačném pořadí. Tím je
zkontrolován celý tištěný obrázek(23), nejen počet řešení.

Pro geometrický výklad položme původní histoscape na
`[0,2]×[0,2]×[0,4]` s výškami `[[4,3],[1,2]]` a s kamerou q,
jejíž všechny tři souřadnice jsou kladné, jak již dokládá HP-1.
Připojení poloprostoru z≤0, y≤0 nebo x≤0 modeluje postupně podlahu,
levou a zadní stěnu. Paprsek od původního viditelného povrchu ke
kameře všechny souřadnice zvětšuje, takže nové poloprostory jej
nemohou dodatečně zastínit. Odstraněné původní kontaktní plochy
byly odvrácené od kamery. Na obvodu kontaktu se však průřez materiálu
změní z jednoho kvadrantu na tři: bývalá obrysová polohrana se stane
konkávní hranou mezi dvěma viditelnými plochami. Jiné viditelné
hrany ani jejich znaménka se nemění. Kontaktní obvody jsou právě
uvedené tři skupiny, jak přímo ukazují souřadnice jejich konců
v N20-4. To dokazuje i každý ze tří slovních výkladů v textu.
Poloprostor je zde neomezené pozadí; lze jej nahradit dostatečně
velkou deskou s dodatečnými okraji mimo zobrazený výřez.

## E42 — oba obecné počty

V konečné síti je součet stupňů3t+2v+3w+3y. Každá čára má dva
různé konce a započte se dvakrát, proto proměnných je
`E=(3t+2v+3w+3y)/2`. Junctions je `J=t+v+w+y`, tedy J lokálních
podmínek. Není třeba předpokládat souvislost; prázdná síť dává0,0.
Pro(20) jsou t=1,v=5,w=8,y=5 a dostáváme26,19. Jde o podmínky
v přirozeném modelu před případným slučováním redundantních relací.

## E43(a–c) — duální model, všechny vypsané dvojice

Proměnná junctionu j vybere index jednoho z úplných řádků Tabulky1.
Na každé čáře musí oba konce určit stejnou globálně orientovanou
hodnotu. Tato podmínka je zároveň nutná a postačující: při jejím
splnění má každá čára dobře definované označení a každá lokální
podmínka je automaticky splněna. Opačně každé označení určuje
právě jeden řádek u každého junctionu, neboť řádky jsou různé.
Tedy jde o bijekci řešení, včetně čtyř různých možností T.

Pro ab dávají řádky a v pořadí1…6 hodnoty `<,<,+,>,>,-`.
Řádky b dávají na ab `>,-,+`. Rovnost dává přesně dvojice
41,51,33,62, bez dalších možností.

Pro np mají všechny čtyři řádky n hodnotu `<`. Šest řádků p
dává na np `+,<,<,-,>,>`; proto dostáváme přesně
12,13,22,23,32,33,42,43. Na op dávají řádky o `+,+,-`,
řádky p `>,>,+,<,<,-`, a shodují se právě13,23,36.
Z obou vazeb plyne p∈{2,3}∩{3,6}={3}. V původním modelu
je stejný závěr dvojice np=`<`,op=+, jak již ukázal L22-3.

Počty jsou nyní obrácené: J proměnných a E vazeb. Důkaz
nespoléhá na realizovatelnost síťového obrázku a platí i pro
nesouvislou nebo prázdnou síť.

## E43(d) — každý číselný mezikrok a meze porovnání

Před uplatněním vazeb má nový model přesně `4^t 6^v 3^w 5^y`
stavů, původní `4^E`. Dosazením E z E42 a rozdělením součinu
vzniká přesně `(1/2)^t (3/2)^v (3/8)^w (5/8)^y`.
V(20) je to `4982259375/35184372088832`
=0.00014160432826315628…, takže tištěné≈0.00014 je správně.
Prázdná síť má poměr1. Poměr nemusí být obecně menší než1:
například samotný cyklus V má poměr(3/2)^v. Text říká „tend“,
nikoli univerzální nerovnost nebo rychlejší algoritmus.

Surový počet stavů nezahrnuje sílu propagace ani pořadí větvení;
proto z něj nelze odvodit univerzální časové srovnání řešičů.
Příklad p=3 a jeho rovnocenný přímý důkaz v(22) je uzavřen výše.
Odkazy na(24),(25) se kontrolují při následujícím hlavním bloku,
nepřebírají se z pouhého odkazu. Bibliografický údaj van Beek,
AAAI10(1992),447–452,Example3 nebyl samostatně ověřen; k důkazům
zde není potřeba. Vnitřní odkaz56 má známou opravu na272–274.

## E44 — celý převod na XCC, nikoli jen první a poslední možnost

Pro každý junction zaveď jeden primární item, pro každou čáru jeden
sekundární item. Ke každému povolenému řádku lokální relace vytvoř
možnost obsahující jeho junction a všechny incidentní čáry
s barvou rovnou globální hodnotě řádku. Primární pravidlo vynutí
právě jednu možnost pro každý junction. Pravidlo barev sekundárního
itemu vynutí stejnou hodnotu čáry na jejích obou koncích. Proto
každé XCC řešení dává jediné CSP řešení a každé CSP řešení vybírá
jedinou množinu možností; jiné primární nebo barevné podmínky
nejsou potřeba. To je celý důkaz převodu, nezávislý na odkazované
úloze7.2.2.1–100.

V(20) je tedy19 primárních a26 sekundárních items. První dvě
možnosti jsou přesně `a ab:< ac:+`, `a ab:< ac:>`; poslední
řádek s dává `s rs:+ ls:- qs:+`. Ostatní možnosti jsou všechny
jednotlivě zkontrolované řádky v L22-1. Použijeme-li plnou Tabulku1,
jsou u n čtyři možnosti `n kn:< mn:c np:<`, kde c probíhá celou
doménu, a celkem `4t+6v+3w+5y=83` možností. To je správný obecný
počet v opravené odpovědi44.

Konkrétní zkrácená relace n v(22) dovoluje také jedinou možnost
`n kn:< np:<`, tedy80 možností pro tento příklad. Čára mn je pak
zmíněna jen v možnosti pro m a její barva je určena tam; n ji
skutečně nijak neomezuje. I zde je převod bijektivní. Tento detail
se nesmí zaměnit za vyvrácení známého errata: obecně může čára
spojovat dva prostřední stonky T. Vynechání jejího itemu na obou
koncích by nerozlišovalo její čtyři možné hodnoty. Plný převod
se4 možnostmi pro každé T se tomuto problému zcela vyhne a jeho
obecná bijekce platí bez dalšího předpokladu.

## Použitá errata a přesný rozsah

Primární `sources/err4f7-2026-11-06.textxt`, krátká i kumulativní
PDF/textová vrstva byly pro tento blok porovnány:

- p13, pátý řádek po(22),4.9.2026: seznam obsahuje bd místo bc;
- p168, konec odpovědi43,22.10.2026: odkaz272–274 místo56;
- p168, konec odpovědi44,6.9.2026: počet začíná4t+6v místo t+6v.

Jsou to již známé opravy, nikoli nové nálezy. Všechny matematické
části42–44, relace21–22, počet čtyř řešení, všechny značky(23)
a konkrétní fyzické výklady jsou uzavřeny v právě uvedeném rozsahu.
Výkon libovolného řešiče a neprověřená bibliografie se neprohlašují
za ověřené. Poslední odstavec p13 o boundary cycle a standardním
označení se kontroluje zvlášť; tento soubor sám neuzavírá celou p13.
