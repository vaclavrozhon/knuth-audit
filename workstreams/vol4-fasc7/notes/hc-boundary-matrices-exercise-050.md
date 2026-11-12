# Úloha50: správné matice, přesné předpoklady a dvě oddělené mezery

Zadání p118/file133 a odpověď p169/file184 byly celé zobrazeny.
Navíc byl přímo prohlédnut velký výřez všech šesti matic
`images/file-184-matrices50.png`; špatně čitelné spodní řádky
V/Λ nebyly odhadnuty z OCR. Úplný nový konečný certifikát je
`check_boundary_matrices50.py` a `results/boundary-matrices50.json`.

## E50-a — seznam konkrétních případů není úplný pro celý vstup

Každá ze šesti uvedených formulí správně popisuje svůj konkrétní
obrázek a orientaci větví. Nicméně tvrzení, že jde o všechny
možnosti realizovatelného HC obvodu, nemá platný důkaz jen
z definice: C0008 dává jednoduchý biconnected obvod s platným
labelingem, u jehož W leží prostřední větev na obvodu. Jeho
přesná realizace a přímý rozpor pořadí jsou v `notes/F7-C0008.md`.
Tento obvod má dokonce všechny junctions různé a nemá žádnéT.
Chybějící případ tedy není důsledkem opakovaných bodů obvodu.

Zvlášť proto nezaměňujeme dvě tvrzení: matice pro uvedených
šest konfigurací jsou správné; jejich deklarovaná úplnost
pro všechny realizovatelné sítě je candidateC0008. Žádná
stránka ani celá50 se automaticky neuzavírá.

## E50-b — odvození všech96 položek

Stavy řádků i sloupců mají pořadí `>,<,−,+`. Řádek je štítek
`j_(k−1)→j_k`, sloupec štítek `j_k→j_(k+1)`. Písmena g,l,m,p
jsou štítky `>,<,−,+` čáry od j_k do třetího souseda. Při
převodu lokálního řádku Tabulky1 se tedy šipka na větvi k
předchozímu junctionu obrací, zatímco na následující a třetí
větvi se neobrací. Znaménka se nemění.

- **L=T(next,prev,inner):** větev next je levý bar O, takže
  sloupec je vždy>. Větev prev je volný stonek, takže vstup
  může být kterýkoli. Pravý bar inner je I, tedy písmeno l.
  To dává l v celém prvním sloupci a nuly jinde.
- **R=T(inner,next,prev):** větev prev je pravý bar I, takže
  vstup je>. Větev next je volná; levý bar inner je O.
  To dává g v celém prvním řádku a nuly jinde.
- **V=V(next,prev):** šest Tabulkových řádků po uvedeném
  obrácení příchozí orientace dává přesně
  `1010 / 0101 / 1000 / 0100`. Nenulové položky jsou1,
  protože žádná třetí větev neexistuje.
- **Λ=V(prev,next):** stejných šest řádků s opačným pořadím
  větví dává `1001 / 0110 / 0100 / 1000`.
- **W=W(next,inner,prev):** O+I dává vnější pár(>,>) a p;
  −+− dává(−,−) a p; +−+ dává(+,+) a m. Všechny další
  položky jsou0.
- **Y=Y(next,inner,prev):** pět řádků dává postupně
  (−,<):g, (>,>):m, (<,−):l, (−,−):m, (+,+):p.
  Žádné další položky nejsou přípustné.

To kontroluje všech28 nenulových i68 nulových položek.
Přípustná dvojice vnějších štítků v každé z těchto konfigurací
určuje třetí štítek jednoznačně; žádná matice proto nepotřebuje
na jedné pozici součet dvou různých písmen.

## E50-c1 — přesný indukční význam nekomutativního součinu

Nejprve pracujme s **výskyty** proměnných podél obvodového
průchodu a předpokládejme, že každý jeho junction patří do
jednoho ze šesti skutečně uvedených případů. Uvažujme otevřený
úsek k po sobě jdoucích junctions. Položka(s,t) součinu jejich
matic je konečný polynom s nezápornými celočíselnými koeficienty:
slovo zaznamenává štítky třetích větví v pořadí výskytu a
koeficient počítá právě přiřazení mezilehlých obvodových
štítků se vstupem s a výstupem t.

Pro k=1 jde o přímo odvozenou matici. Při připojení dalšího
junctionu se sečtou všechny čtyři možnosti společného
obvodového štítku a jeho případné nové písmeno se připojí
zprava. To je přesně násobení matic a konkatenace slov;
každé přiřazení má jediný společný stav, takže je započteno
jednou. Indukce dokazuje celý součin včetně násobností.
Stopa ztotožní počáteční a koncový stav, tedy uzavře průchod.

Je-li obvod jednoduchý a každá skutečná vnitřní čára se
vyskytne právě jednou, jde zároveň o přesnou charakterizaci
přiřazení skutečným proměnným. Tyto předpoklady platí pro
tištěný příklad(20), jak ověřujeme níže.

Při více výskytech jedné fyzické čáry ale musí platit ještě
jejich společná identita a správné obrácení orientace. To
součin sám nezajišťuje: C0007 má stopu25gg a žádné skutečné
přípustné přiřazení sdílené vnitřní chordě. Slova pak popisují
pouze nezávislé výskyty. U opakované obvodové čáry by bylo
obdobně třeba ztotožnit i její obvodové stavové výskyty.
Tento problém je oddělený od chybějícího W případu v C0008.

## E50-c2 — každý prvek celého tištěného příkladu

Původní již ověřený obvod(20) je `a b e f q s r o m c`.
Při dosazení skutečných pořadí z(20) dává přesně

`V W Y W V W V W Y W`.

Třetí větve v jejich skutečném pořadí jsou
`bd,eg,fh,ls,op,mn,cd`: jde o sedm **různých** vnitřních
čar, jejichž druhé konce leží uvnitř obvodu. Všech deset
obvodových čar je také různých. Proto zde právě platí
předpoklady přenosu z výskytů na skutečné proměnné v E50-c1.

Úplný součin byl odvozen ze všech96 správných položek.
Má jen čtyři nenulové prvky:

`P_(>,>)=3σ, P_(>,−)=2σ, P_(−,>)=2σ, P_(−,−)=σ`,

kde `σ=pmpppmp`; všech dalších12 prvků je0. To souhlasí
s každým tištěným prvkem, nikoli jen se stopou. Stopa je4σ:
tři případy mají vstupní čáru j_(−1)→j_0 označenou>,
jeden−. Všechny vnitřní štítky jsou v uvedeném pořadí
`+,−,+,+,+,−,+`. Tím je přesně ověřen i řetězec znamének
a důvod, proč tento konkrétní obvod je volný.
Starý geometrický či čtyřřešeniový výpočet se znovu nespouštěl.

## E50-c3 — komprese polynomů na nulu, jedno slovo nebo mixed

Pro aritmetiku polynomů s nezápornými koeficienty stačí
rozlišovat0, kladný násobek jediného slovaσ, a alespoň dvě
různá slova(mixed). Koeficient jediného slova není pro tuto
klasifikaci potřebný. Operace jsou přesné:

- při sčítání je0 neutrální, dvě stejná jednotlivá slova
  zůstávají jedním, dvě různá dávají mixed; mixed se přičítáním
  nikdy neztratí, protože koeficienty nejsou záporné;
- při násobení je0 absorbující a dvě jednotlivá slova se
  spojí konkatenací;
- mixed krát libovolný nenulový polynom je mixed, a stejně
  z druhé strany. Stačí z nenulového činitele vybrat jedno
  slovo w: dvě různá slova u,v druhého činitele dávají
  uw≠vw, respektive wu≠wv, z krácení ve volném monoidu.

Tím se přesně reprodukuje třída každé položky a nakonec
třída součtu diagonál. Nulový výsledek znamená žádné takové
přiřazení výskytům; jeden monom má ve všech výskytech stejné
štítky; mixed obsahuje alespoň dvě stejně dlouhá slova,
která se liší na alespoň jedné pozici. Délka je vždy počet
junctions s třetí větví, nezávisle na zvolené cestě stavy.

Za předpokladů E50-c1, které vylučují další ztotožňování
výskytů, je tak mixed přesně výrok, že nějaká skutečná
vnitřní proměnná má více než jednu možnou hodnotu. Při jedné
hodnotě celého vektoru lze libovolné obvodové řešení kombinovat
s libovolným řešením zbývajících vnitřních relací; jde o dvě
inkluze kartézského součinu z FB-2. Nulový případ je prázdný
a žádná proměnná v něm nemá dvě možné hodnoty.

Bez uvedených předpokladů se zde neprohlašuje úplná správnost
obecného finálního testu. C0007 samotný není protipříkladem
jeho booleovského výsledku; C0008 ale již ukazuje skutečný
vstup, kterému šestipřípadový postup neumí přiřadit správnou
matici. Obě omezení zůstávají v inventáři viditelná.

## E50-c4 — ukončení a konkrétní efektivní realizace

Přímá implementace ukládající nejvýše16 skutečných slov
délkyO(q) provede q násobení4×4 matic s konstantním počtem
skalárních operací. Kopírování a porovnávání celých slov dává
O(q²) času a O(q) paměti. To již poskytuje konečný a efektivní
postup pro přesně vymezenou polynomiální úlohu.

Lze dostat i O(q) operací na slovním RAM bez pravděpodobnostního
hashování. Po každém junctionu mají všechny aktuální monomy
stejnou délku. Označme různé aktuální prefixy různými malými
identifikátory. Při kroku V/Λ se nepřipojí písmeno a id se
pouze kopíruje; při jiném kroku vznikne nejvýše konstantně
mnoho dvojic `(id_prefixu,písmeno)`. Dvě nové konkatenace
jsou stejné právě při stejné dvojici. Konstantní seznam těchto
dvojic se může přesně porovnat i kvadraticky, stále za
konstantní práci na junction, a dát nové kanonické id.
Mixed a0 se přenášejí podle právě prokázaných operací.

Celkem tedy O(q) kroků s celočíselnými identifikátory O(log q)
bitů; pro samotné rozhodnutí stačí aktuální konstantně velká
tabulka a při ukládání vysvětlujících prefixů O(q) prostoru.
Žádná náhodná kolize není předpokládána. Ukončení plyne
z přesně q konečných kroků. Tento vlastní rozbor ceny je
pro redukovanou aritmetiku, nikoli tvrzení, že jím byla
vyřešena chybějící kompatibilita skutečných opakovaných čar.

## Errata a stav

Všechny vrstvy errat byly zkontrolovány v C0007/C0008; žádná
oprava50 není uvedena. Matice a příklad jsou checked.
Úplnost50(a), fyzická interpretace opakovaných výskytů a
obecný finální algoritmus zůstávají přesně vymezené partial
s oběma candidate kartami. Žádná nová dlouhá enumerace ani
restart starého ověření se nespustily.
