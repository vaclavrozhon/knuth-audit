# Předmluva vi–ix: jednotlivé argumenty pro Tarjanův algoritmus

6. listopadu 2026. Digitální vydání 1, březen 2025. Souborové strany
7–10; na file 10 je zde pokryta pouze horní část s T5–T9.
Původní sazba file 7–10 prohlédnuta; nativní text ztrácí například
`≠`, čárky u proměnných a závorky. Důkazy níže jsou vlastní;
nepřebírají neotevřený odkaz na budoucí §7.4.1.2 ani jeho úlohu 50/60.

## T-P01. Základní tvrzení na p. vi

Graf je konečný orientovaný multigraf; smyčky ani souběžné oblouky
argumenty nemění. Dosažitelnost připouští cestu délky nula. Vzájemná
dosažitelnost je reflexivní a symetrická přímo a tranzitivní zřetězením
cest v obou směrech. Je tedy ekvivalencí.

Kontrakce vrcholů orientovaného cyklu nikdy nesloučí různé její třídy:
vrcholy cyklu jsou vzájemně dosažitelné. Každý netriviální krok sníží
počet vrcholů. Smyčky, které kontrakce vytvoří, je třeba považovat za
vnitřní oblouky supervrcholu, nikoli znovu kontrahovat. Jestliže dvě
různé zbývající supervrcholové třídy jsou vzájemně dosažitelné, cesty
tam a zpět obsahují orientovaný cyklus procházející více supervrcholy.
Proto skončení kontrakcí právě zanechá silné komponenty. Pro tvrzení
„bez cyklů“ jde o kondenzaci s odstraněnými vnitřními smyčkami.

Konečný neprázdný acyklický orientovaný graf má sink: jinak lze z každého
vrcholu pokračovat po výstupním oblouku a po více než n krocích opakovat
vrchol, čímž vznikne cyklus. Kondenzace tedy má sink komponentu S.
Žádná cesta, která ze zbytku grafu vstoupí do S, už z S nevystoupí.
Odstranění S proto nezmění dosažitelnost mezi ostatními vrcholy, a tím
ani jejich silné komponenty. Totéž vysvětluje bezpečnost odstranění
oblouků vedoucích do už vyřešených sinků.

V DFS každý nový vrchol dostane právě jednoho rodiče, který byl objeven
dříve. Rodičovské oblouky tedy nemají cyklus a tvoří orientovaný les.
Aktivní vrcholy jsou přesně zásobník dosud neukončených volání: jediná
cesta od aktuálního kořene do aktuálního vrcholu. Zkoumání každého oblouku
a ukončení každého vrcholu jednou dokazuje skončení konečného DFS.

## T-P02. Lemma S, p. vii

Pracujeme s konceptuálním DFS, které po ukončení vůdce kompletního
sinkového bloku ihned odstraní celý blok. Stav lemmatu se sleduje mezi
těmito událostmi, nikoli uprostřed označení vůdce za neaktivní a jeho
odstranění. Prázdný stav U je dovolen mezi kořeny; samotné lemma
má výslovnou podmínku `|U|≥1`.

Indukční invariant je přesně tištěné lemma: v pořadí PRE jsou komponenty
aktuálně viděných oblouků intervaly S1,…,Sk; první vrchol každého bloku
je aktivní a jediné meziblokové oblouky jsou rodičovské oblouky
z posledního aktivního vrcholu Sj do vůdce Sj+1. Aktivní vrcholy leží
na jediné rodičovské cestě. Aktuální vrchol v je tedy v posledním bloku.

* Při vstupu do nového kořene je U jednoprvkové: invariant platí.
* Nový cíl u oblouku z v se vloží na konec pořadí, jako nový jednoprvkový
  blok; jediný nový meziblokový oblouk je rodičovský `v→u`.
* Oblouk do již odstraněného vrcholu není v indukovaném grafu na U.
  Oblouk z v do jeho vlastního bloku na komponentách nic nezmění.
* Oblouk z v do staršího bloku Sj uzavře cyklus bloků Sj,…,Sk:
  dopředné spojení poskytují právě invariantní rodičovské oblouky,
  zpětné spojení nový oblouk. Celý tento suffix se sloučí, ale žádný
  dřívější blok ne, protože nemá cestu zpět z tohoto suffixu.
  Intervalovost, aktivní vůdce i jediný zbývající vstupní stromový
  oblouk se zachovají. Tím jsou vyčerpány možné cíle dalšího oblouku.
* Při ukončení v, které není vůdcem Sk, zůstane vůdce Sk aktivní.
  Graf se nemění a předchozí poslední aktivní vrchol v už není potřeba
  jako spojnice do dalšího bloku, protože žádný další blok není.
* Je-li v vůdcem Sk, je jediným dosud aktivním vrcholem Sk: vůdce je
  první a v je poslední na aktivní cestě. Po ukončení v byly prohlédnuty
  všechny výstupní oblouky celého Sk. Žádný nevede do neviděného
  vrcholu (ten by DFS již objevilo), žádný nevede do jiného bloku U
  (Sk je poslední sink). Sk je tedy skutečný sink mezi neodstraněnými
  vrcholy celého grafu. Odstraní se i jeho vstupní stromový oblouk;
  pro zbývající prefix invariant platí znovu.

To současně dokazuje, že odstraňujeme celé skutečné silné komponenty,
a nikoli jen odhady vytvořené z prozatím viděných hran. Žádná budoucí
hrana jim nemůže umožnit cestu ven, neboť všechny jejich výstupy už známe.

## T-P03. Corollary S a les po odstranění hran, p. vii

Nechť v je nejdříve objevený vrchol silné komponenty C. Všechny ostatní
vrcholy C jsou v okamžiku jeho objevení neviděné. Z v k nim vedou cesty
uvnitř C, takže je DFS objeví před ukončením v a leží v `desc(v)`.
Rodičovská cesta z v k libovolnému x∈C leží také v C: každý její vrchol
y splňuje `v→*y→*x→*v`. Zvlášť proto C zůstává spojité po vymazání
rodičovských hran do vůdců ostatních komponent.

Pokud x∈desc(v) patří jiné komponentě D s vůdcem w, nemůže w být
pravým předkem v: cesta `w→*v→*x→*w` by je sloučila. Jelikož w je
předkem x podle předchozího odstavce, musí ležet uvnitř podstromu v.
Platí tedy `POST(w)<POST(v)`. Právě takové celé podstromy byly odebrány
dříve v pořadí vůdců podle POST. To dokazuje obě inkluze v tištěném
vzorci

`Cj = desc(vj) \ (desc(v1) ∪ … ∪ desc(vj−1))`.

`desc` zde obsahuje vrchol samotný, což je nutné i u izolovaného vrcholu.
Odstraněním hran do všech vůdců proto vzniknou přesně stromy těchto
množin. „Connected components“ znamená obyčejné slabě spojené komponenty
orientovaného lesa, nikoli silné komponenty (ty by v lese byly jednotlivé
vrcholy). Směr hran se při této větě ignoruje.

## T-P04. Definice LOW a Theorem T, p. viii

Čas dozrání nestromového oblouku je jeho prohlédnutí; čas dozrání
stromového oblouku `a→b` je ukončení b. V downpath klesají časy dozrání
podél po sobě jdoucích oblouků. Podmínka „matured before“ mluví
o již proběhlých událostech; nerozšiřuje LOW spícího předka pomocí
budoucího dozrání. Cesta délky nula zajišťuje `LOW(v)≤PRE(v)`.
Jediný zatím nedozrálý stromový oblouk bez pokračování vede k později
objevenému vrcholu a nemůže toto minimum zmenšit.

Při ukončení v už byly všechny oblouky z jeho podstromu prohlédnuty.
Pokud v není vůdce posledního bloku, existuje v aktuálním bloku cesta
z v do jeho staršího vůdce. Zvolme první její oblouk `x→y`, který
opustí DFS podstrom v. Pak `PRE(y)<PRE(v)` a x je potomek v.
Stromová cesta `v→*x` následovaná `x→y` je downpath: nestromový poslední
oblouk byl prohlédnut před ukončením x, nejhlubší stromové oblouky
dozrávají první a každý rodičovský oblouk až po nich. Koncový y je
neodstraněný, neboť celá původní cesta byla v aktuálním bloku.
Tedy `LOW(v)<PRE(v)`.

Naopak pokud `LOW(v)<PRE(v)`, downpath svědčí o cestě z v ke staršímu
vrcholu U. Podle Lemma S nemůže poslední blok mít cestu do dřívějšího
bloku; dosažený starší vrchol je proto ve stejném bloku jako v. V tedy
není jeho první vrchol. To dokazuje tištěnou ekvivalenci. Izolovaný
vrchol a jednoprvková komponenta se smyčkami mají LOW=PRE a správně
se odstraní ihned při ukončení.

## T-P05. Proč stačí relaxace a kódování REP/LINK

Když dozraje oblouk `v→u`, každý dosavadní minimální downpath z u
lze prodloužit zleva tímto obloukem: všechny jeho relevantní časy
jsou dřívější. Nové minimum je proto `min(LOW(v),LOW(u))`, pokud u
zůstává neodstraněný. Naopak každý nově dostupný netriviální downpath
musí začínat právě nově dozrálým obloukem; jinak jsou jeho oblouky
i jejich pořadí již dříve stejné. U stromového oblouku se tato relaxace
provádí až při návratu z dítěte. U nestromového hned při prohlédnutí.
Začínáme hodnotou PRE(v), tedy cestou délky nula. Tím jsou pokryta
všechna minima v definici.

Odstranění jiného bloku platné minimum nezvýší. Je-li jeho svědkem
w s `PRE(w)≤PRE(v)`, existuje cesta v→w a podle řetězce z Lemma S
i cesta w→v; oba patří stejnému bloku a odstraňují se spolu. Ostatní
koncové vrcholy s vyšším PRE minimum neovlivňují. LOW neaktivního v
se novými pozdějšími oblouky také nemění: už dozrálý první oblouk
jeho downpath nemůže předcházet později prohlédnutému oblouku v sestupném
časovém pořadí. Proto hodnoty uložené na zásobníku zůstávají platné.

Ve T3 se REP(v) nastaví na PRE(v), LINK(v) na SENT. Každé skutečné
snížení REP označí LINK(v)=Λ; REP se nikdy nezvětšuje, dokud v není
odstraněno. Tedy pro aktivní v přesně platí (**) i (***). Jde o dvě
různá užití LINK: po ukončení ne-vůdce se pole změní v odkaz zásobníku.
PRE se explicitně ukládat nemusí, protože jediný potřebný test rovnosti
si LINK pamatuje od první ostré změny.

Kód `SENT+v` musí být jedinečný pro každého vůdce a větší než všechny
ranky 1,…,n; používá se abstraktní adresní/integer kód knihy, nikoli
tvrzení o přípustnosti sčítání dvou ukazatelů v jazyce C. Odstraněný
cíl má tak vysoké REP, že ve T6 nemůže snížit REP aktivního v.
Sentinel má REP=0 a bezpečně ukončuje zásobníkové smyčky.

## T-P06. T1–T9 včetně zásobníku a zkrácení ve T6

T1 označí všechny vrcholy PARENT=Λ; DFS kořen má rodiče SENT a dítě
rodiče rovného skutečnému vrcholu. Test viděnosti v T2 a T6 tedy funguje
i po odstranění, protože PARENT se už nemění. T2 prochází pole pozpátku;
na vstupu už byly dokončeny celé dřívější DFS stromy, a proto jsou
všechny vrcholy dosažitelné z již zvolených kořenů odstraněny. T3–T6
procházejí seznam oblouků; ARC rodiče uloží pokračování za stromovým
obloukem. T9 ho obnoví přesně jednou po návratu. Smyčka a paralelní
oblouky pouze provedou opakovaný neškodný test minima.

Po T7 je ne-vůdce vložen na SINK a případná nižší hodnota REP je
předána jeho rodiči, právě při dozrání rodičovského oblouku. Vůdce
přejde do T8. Pro vůdce v je REP(v)=PRE(v). Všechny jeho neodstraněné
potomky tvoří právě poslední komponentu; žádný další její aktivní
vrchol už není. Jejich LOW jsou ≥PRE(v), protože cesta k dřívějšímu
vrcholu by sloučila bloky. Každý neaktivní vrchol staršího bloku má
LOW≤PRE<PRE(v). Potomci v byli navíc dokončeni po objevení v, kdežto
již neaktivní vrcholy starších bloků před ním. Poslední komponenta
je tedy souvislým horním úsekem zásobníku, přesně rozpoznaným
podmínkou `REP(SINK)≥REP(v)`. T8 všechny a pouze tyto vrcholy označí
stejným kódem a odstraní; nakonec označí samotného vůdce v.

Zvláštní větev T6 má další předpoklady `u=ROOT` a `p=n`. Právě viděný
oblouk z aktuálního vrcholu zpět ke kořeni sloučí podle Lemma S všechny
zbývající bloky U: vedou k němu dopředné stromové spojnice a zpět
nový oblouk. Žádný neviděný vrchol už neexistuje. Veškeré dosud
neprohlédnuté oblouky proto míří jen uvnitř U nebo do dříve odstraněných
sinků a nemohou tuto silnou komponentu změnit. Je bezpečné neprohlížet
zbytek. Smyčka vloží na SINK aktivní rodičovský řetězec kromě ROOT,
potom v=ROOT. Všichni mají REP≥PRE(ROOT), takže T8 odstraní celý
zásobník a kořen; `u=SENT` vede zpět do T2. Tato optimalizace nemusí
dokončit původní DFS les ani postorder; správnost výstupních komponent
je pro ni právě dokázána samostatně.

T2 skončí po nejvýše n posunech w. Každý vrchol je objeven nejvýše
jednou, vložen do SINK nejvýše jednou a odstraněn nejvýše jednou;
každý prohlédnutý oblouk posune a na následníka. To dává ukončení
a čas O(n+m), paměť O(n) pomocných polí vedle vstupních seznamů.
Zkrácení ve T6 prochází každý zbývající aktivní vrchol pouze jednou.
Pro n=0 se po T1 ihned ukončí T2; m=0 dává n jednoprvkových tříd.
Na konci mají dva vrcholy shodný REP právě tehdy, když byly odstraněny
v témže bloku; podle T-P02 jde právě o vzájemnou dosažitelnost.

## T-P07. Errata, rozsah a zbývající bibliografie

Relevantní položky jsou v `results/errata-front-025.json` a znovu
porovnány s `errata/originals/err4f7.textxt` (řádky 231–249).
Změna odkazu 12a.ps.gz→12a.pdf a úlohy 50→60 není nový nález.
Odstranění pomocné ROOT a nahrazení w je správné: w se od zahájení
DFS stromu do návratu T2 nemění, takže ROOT=w po celý strom.
Nová slabší/přívětivější formulace v poznámce k p. viii nemění argument.
Ověření těchto známých úprav nenahrazuje argumenty výše.

Historická priorita Tarjana a datace optimalizace 2021 nejsou z vlastního
matematického důkazu odvozeny; primární historické prameny v tomto bloku
neověřeny. Bibliografická výjimka je výslovná. Žádný nový nález se zde
nepotvrzuje. Dolní část file 10 (Hopcroft–Karp) patří následujícímu bloku.

Doplňková kontrola `check_tarjan_targeted.py` (nice 15) porovnala osm
pevných malých vstupů s nezávislou maticí vzájemné dosažitelnosti.
Obsahují prázdný graf, izoláty, smyčky, paralelní oblouky, již vyřešený
sink, slučování a T6 se zbývajícími neprohlédnutými oblouky. Výstup
`results/tarjan-targeted.json` souhlasí. Nejde o úplný výčet a obecný
důkaz tím není nahrazen.
