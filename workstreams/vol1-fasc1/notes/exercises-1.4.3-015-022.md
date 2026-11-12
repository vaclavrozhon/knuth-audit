# MMIX — §1.4.3′, úlohy 15–22

## 15 — Fputs přes hranice chunků

MemFind vrátí pointer na první dosud nevypsaný znak. Každý node
má nulový padding za DATA, takže host Fputs bezpečně skončí nejpozději
na konci chunku. Vrácené t je počet skutečně napsaných znaků nebo −1.
Chyba se ihned předá; t=0 ukončí smyčku i u NUL na samé hranici.
Jinak xx+=t sčítá počet výstupních znaků a z+=t ukazuje na nalezenou
nulu. Pokud tato adresa není násobek Chunk, je nula skutečně uvnitř
virtuálního stringu. Pokud je na hranici, další MemFind rozliší
pokračování od skutečného počátečního NUL dalšího chunku. Nevypíše se
ani padding, ani skutečný terminátor. Na normálním konci je xx
přesně délka řetězce.

GO uloží link do $0; DoInst vloží původní TRAP inst a nastaví rW
na link. Proto X/Y/Z původního I/O (zejména handle Z) zůstávají v
instrukčním slově i při použití pracovních xx,yy,zz pro jiné účely.
SimFinish použije TrapDone jako link, SimInst se vrací volajícímu;
Fclose potřebuje jen handle a Fseek/Ftell stejný přímý mechanismus.

## 16 — Fopen a pracovní kopie filename

GetArgs načte dva octabyty argumentů přes dvě nezávislá MemFind,
takže jejich případné rozdělení přes hranici chunku není problém.
Výstupní pointer IOArgs se přeloží na interní adresu, druhý argument
(mode) se ponechá jako hodnota. Chybný výpočet zbývající délky je
C0008: maskovat se musí virtuální z, nikoli fyzické x. Tento výpočet
Fopen nevyužívá, protože kopíruje filename po bytech.

Temporary filename začíná až na old alloc+nodesize, tedy za jedním
rezervním novým uzlem. Každý nenulový byte názvu musí už ležet v
některém přiděleném uzlu. První dosud nepřidělený chunk je nulový,
takže právě tam název hned skončí. Během kopie se tudíž může
alokovat nejvýše jeden nový node; nemůže přepsat temporary filename.
Překládání jiných existujících chunků pouze mění LINK, ne jejich adresy.

LDBU/STBU postupují současně o jeden ve virtuální i temporary
adrese, včetně terminátoru. Host Fopen dostane přesnou souvislou kopii.
Po návratu STCO nuluje octabyty pozpátku; protože začátek je zarovnán,
smyčka vymaže celou kopii a nanejvýš ještě přilehlý předchozí padding.
Ten má být nulový a neobsahuje žádná živá data. t s návratovou hodnotou
Fopen se při čištění nemění.

## 17 — Fread/Fwrite po částech

Použít opravený GetArgs z C0008. Invariant: IOArgs míří na první
nezpracovaný byte, y je celkový počet zbývajících bytů a xx počet
bytů do virtuální hranice chunku. Pro y≤xx stačí jediná závěrečná
host operace. Jinak se nejprve provede blok xx, y se sníží o xx,
z posune o xx a následující chunk má zbytek kapacity Chunk.
Každá úspěšná iterace odebere kladný počet bytů, tedy skončí.

Je-li ve vnitřním bloku přeneseno n<xx bytů, host vrátí n−xx.
Po odečtení zbývajícího y je výsledek n−xx−y, právě celkový deficit
původního požadavku. Závěrečný blok už má celý zbývající rozsah,
takže jeho deficit se přebírá přímo. Totéž platí pro Fwrite.

**Rozsah:** kniha výslovně předpokládá, že po prvním úspěšném Fread
nenastane serious reading error. První serious error má hodnotu
−1−xx a po odečtení y dává správné −1−size. Pozdější serious error
by vyžadoval původní size a není tvrzen správně bez uvedeného předpokladu.
Počet/oblast paměti musí být platné pro neprivilegovaný program;
velikosti s horním znaménkovým bitem nejsou tímto signed CMP důkazem
pokryty. Rutiny Fgets/Fgetws/Fputws jsou pouze odkázané v externím
sim.mms, nikoli řešením této úlohy; jejich obecná správnost zde
není prohlášena za ověřenou.

## 18 — menší local ring

Důkazy V0150–V0153 a úlohy 10 se nepotřebují opřít o konkrétní
256, nýbrž o běžné L<ρ a modulo mocniny dvou. Má-li program vždy
L≤ρ−1, uloží se všechny jeho current locals injektivně; full ring
při růstu vždy dovolí store pushed položky. Přechodový marker pro
global PUSH/SAVE může dát L=ρ, ale ihned se celý blok pushne, jako
v úloze 3. POP zachová nejvýše skutečné nové L≤ρ−1 a zahodí právě
případné přepisované vrchní položky. Takový program tedy funguje i
s ρ=32. Podmínka se vztahuje na všechny fáze simulovaného programu,
včetně obnoveného platného kontextu, nikoli jen na jeho první instrukci.

## 19 — vyčlenění přidání lokální položky

Tři větve lze sjednotit pomocnou rutinou, která přijímá hodnotu
nové položky v arg:

```text
GrowLocal  ADDU t,oo,ll
           AND t,t,lring_mask
           STOU arg,l,t
           INCL ll,8
           (pokračovat původním tělem StackRoom)
```

Běžný XDest předá 0; global PUSH a SAVE předají původní L=ll/8.
Po návratu musí global PUSH přeskočit své původní opakované uložení
markeru (local PUSH si je ponechá). STORE se provede do dosud
volného slotu β před jeho zvýšením, přesně jako dosavadní XDest/SAVE;
pravidlo StackRoom se nemění. Return-link ochrana zůstává v jeho
existujícím GET/PUT. Tím vznikne konkrétní společná sekvence a
odstraní se tři kopie indexace, uložení a růstu. Známou opravu XOR→AND
z roku 2005 přebíráme; v nynější sazbě už je &.

## 20 — binární loader

Invariant vnitřní smyčky: loc=λ+8k a prvních k nenulových octabytů
skupiny je uloženo. Fread čte přesně osm bytů do Global[255]; x≠0
se uloží přes MemFind a loc zvýší o osm. x=0 skupinu ukončí bez
uložení terminátoru. Vnější smyčka načte nové λ. EOF mezi skupinami
ukončí loader; EOF uvnitř neukončené skupiny vyvolá Error.

Po poslední skupině je loc=λ+8l a řádek 575 dá přesně
λ+8(l−1), jak zadání požaduje. Při l=0 je to formální λ−8;
pokud má poslední skupina být skutečný saved context pro bootstrap,
musí obsahovat jeho nenulový koncový word. Libovolný syntakticky
platný soubor nemusí sám představovat platný spustitelný program.
Fread partial header se mimo platný formát nerozlišuje od EOF;
validaci poškozených souborů řešení netvrdí.

Tento invariant spolu s úlohou 12 a ověřeným ropcode0 bootstrapem
uzavírá V0179 pro platný vstupní program: loc ukazuje na saved
packed word, loc−104 na $255=Main, umělé UNSAVE obnoví kontext,
AllDone vynuluje resuming a další Fetch začne Main nebo #f0.

## 21 — konečný stavový prostor; partial kvantitativního tvrzení

Deterministický stroj s konečně mnoha stavy má po prvním opakování
stavu periodickou budoucnost. Má-li nekonečně mnoho Fopen/Fclose
událostí, mezery mezi nimi jsou proto nakonec omezené periodou;
nemohou navždy exponenciálně růst. To dokazuje uvedenou kvalitativní
překážku skutečné nekonečné rekurze, nikoli okamžik nedostatku paměti.

Vypsaná horní rekurze je ekvivalentní
`n[k+1]=n[k]+5+ceil((3*n[k]+2)/512)`.
Pro n[k]=6k a k≤28 je 3n[k]+2≤506, takže další přírůstek je6.
Pro k=29 je čitatel524 a další přírůstek7. Odtud n[k]=6k pro k<30.
Dále je násobitel 1+3/512>1 a přičítaný člen omezený mezi
5+1/256 a 6+1/256, tedy rekurzivní horní odhad roste exponenciálně.

**C0010 zůstává candidate.** Počet chunků se porovnává s 2^61
bajty místo kapacity 559670633304293 uzlů z úlohy4. Z tohoto
kroku dolní mez 100^6065 neplyne. Odhad je ale horní a nebyla
sestrojena přesná stopa skutečného selhání před touto mezí;
proto samotnou chybnou dimenzi nepovyšujeme na důkaz nepravdivosti
číselné dolní meze. Přechod 6066, velikosti .mmb a uvedené dlouhé
časové profily se znovu nepočítaly. Předpoklad faktoru alespoň100
je v textu podmíněný, neprokázaný pro všechny instrukce.

## 22 — jump trace, partial úplné implementace

C0006 opravuje postup y1,y1+1,… na y1,y1+4,… . Po této opravě
se z dvojic rekonstruují celé maximální sekvenční úseky a četnost
každé instrukce je počet úseků, které danou zarovnanou adresu
obsahují (s odděleným započtením řídicích bodů). Jde o přímý
argument rekonstruovatelnosti, ne implementaci traceru.

Návrh v odpovědi nahrazuje nejbližší řídicí instrukci TRIPem a
zachytává arithmetic trips přes přepsané vstupy #0,#10,…,#80.
Oprávnění zapisovat text uděluje OS výslovně; předchozí read-only
předpoklad se zde tedy nepoužije. Chybí kompletní kód obnovy
původních instrukcí, ochrany stavu, souběhu s trip handlers a všech
RESUME případů. Tato úloha40 zůstává partial, nebyla vydávána
za hotový program ani za neřešitelný výzkumný problém.
