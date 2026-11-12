# ZDD: hlavní text119–122 a úlohy251–260

3. listopadu 2026. Celé znění hlavního textu, zadání a odpovědí bylo
přečteno v knize i autorově draftu;16 obrazů stran a zvětšených výřezů
má zaznamenané hashy. Historický text123 je samostatný následující blok.

Nové potvrzené nálezy jsou [F151](F151_ZDD_ASYMPTOTIC_FACTOR.md),
[F152](F152_CIRCULAR_ZDD_CACHE.md), [F153](F153_ZDD123_WRONG_EDGE.md).
Nejednoznačnosti [C041,C042](ZDD251_260_CANDIDATES.md) zůstávají
kandidáty; úlohy256 a254 proto nejsou označeny za úplně uzavřené.
Známá oprava E109 mění ROOT(0) na RLINK(0) v zadání252; kniha ji
obsahuje, draft nikoli. Datum publikované opravy je25.7.2022.

Staré F079/F080 a všech48 dvakrát ověřených případů,300 barevných rodin
a obecná algebra258 byly převzaty beze změny a bez opakování. Nových
35 nativních případů s nezávislým množinovým modelem trvalo2,867s
s nice15: jeden domino příklad, pět grafů256,22 kruhových případů260
a sedm malých ménage případů. Žádný nový dlouhý běh. Osm zachovaných
stromů má20 živých procesů, všechny nice15.

## Algoritmus Z a úlohy251,253,254

Každá možnost má primární položku. Po každém sestupu se proto množina
aktivních primárních položek ostře zmenší. Signatura rozpracovaného
předka se nemůže znovu objevit u potomka: hodnota Z[t] dosud nedokončené
cache položky nebude přečtena. Opakované signatury mezi sourozeneckými
větvemi mají poddiagram již dokončený.

Při pivotu i tvoří dokončení disjunktní rodiny podle jediné vybrané
možnosti obsahující i. Po jejím odstranění vznikne přesně reziduální
problém reprezentovaný signaturou. Jeho poddiagram lze proto sdílet.
Z6 připojuje nový rozhodovací uzel s nízkou větví do dosavadního řetězce
a vysokou do poddiagramu právě zkoušené možnosti. Při nulové vysoké
větvi nový uzel nevzniká. To vysvětluje řetězec(124), jeho obrácené
pořadí voleb i jediného rodiče každého pomocného neviditelného uzlu.

Každá zamítnutá možnost v nízkém řetězci obsahuje pivot, který pak
vybraná možnost pokryje. Už se tedy nemůže později znovu testovat.
Také vybraná možnost z budoucího reziduálního problému zmizí.
Výsledkem je free ZDD: na žádné cestě se možnost neopakuje.

Z5 cyklicky projde zbytek řádku a Z6 jej obrátí. Zpětný průchod jednou
překročí spacer před řádkem, v němž TOP=1−číslo možnosti; proto
`o=1−j` poskytne správné číslo i pro jednopoložkový řádek. Z7 obnoví
pivot a dokončí jeho cache položku. Původní cover/hide a opačné operace
zachovávají správné délky; zkrácené barevné operace C se pro Z nesmí
použít beze změny, protože délky sekundárních seznamů jsou relevantní.

Úloha251: první řešení se rozpozná zásahem do předem uložené nulové
signatury s kořenem1. Po pokrytí všech primárních položek nezbývá žádná
aktivní možnost, a tedy ani relevantní sekundární položka. Prázdný
aktivní primární sloupec však úspěchem není; viz kandidát C042.

Úloha253: při cache miss se uloží c_l=COUNT. Rekurze a cache hity
navyšují COUNT právě o počty dokončení v disjunktních větvích. Rozdíl
COUNT−c_l při návratu je počet všech dokončení aktuální signatury.
Na cache hit se tentýž počet přičte jednou za aktuální prefix.
Sdílení poddiagramu nevytváří dvojí započtení stejného řešení.
Tento invariant kontroluje i všech35 nových malých případů.

Úloha254(a): sekundární položka má d+2 stavů: irelevantní, nepuriﬁkovaná
a d možných barev. Potřebuje ceil(log2(d+2)) bitů. Při d4 je to šest
kódů ve třech bitech, jak tisk uvádí. Oddělená pole WD a SIG umožňují
skládat nepřekrývající se bitová pole do oktabajtů. Hash je pouze filtr;
cache hit vyžaduje úplnou rovnost signatury, nikoli jen hashů.

Úlohy254(c,d): fyzicky ponechané uzly na purifikovaném seznamu mohou
být již neaktivní. LEN se musí snižovat i při ponechání odkazů a při
odmítnutí špatných barev. Nulová délka pak znamená, že na barvě už
nezáleží a položku lze vypustit ze signatury. Pomocný stav−1 při
deaktivaci brání dvojímu vyjmutí a určuje správné místo obnovy.
Příslušné části originálního DLX6 byly přečteny. Starých300 přesných
barevných rodin zůstává konečným testem; nepředstíráme strojově
formalizovaný důkaz každého bitového či ukazatelového kroku.
Textová nejednoznačnost254(b) je oddělena jako C042.

## Oba domino diagramy a252

Možnosti(121), všech11 instrukcí(122) a graf(120) souhlasí.
Čtyři množiny čísel možností jsou

    {1,5,6,10}, {1,5,7,9}, {2,3,8,10}, {2,4,5,10}.

Sdílení označené hvězdičkou je správně: {2,4} i {1,6} ponechají
{02,12,20,21}. Při levém pivotu vznikne přesně vytištěná posloupnost
instrukcí. S MRV vznikne diagram odpovědi252, porovnaný celý včetně
nízkých a vysokých větví, až na libovolná jména uzlů. Oba reprezentují
právě čtyři výše uvedená pokrytí. MRV diagram má12 rozhodovacích uzlů,
první11; oba mají dva terminály. Opačné pořadí možností02 12 a20 21
na různých větvích skutečně dokládá neexistenci jednotného pořadí.

## Párování,255 a obrázek123

Na úrovni l jsou pokryté položky1,…,l a libovolná l-prvková podmnožina
zbývajících N−l položek. Všechny takové stavy jsou dosažitelné párováním
každé z1,…,l s jednou z vybrané podmnožiny. Počet je binom(N−l,l)
a součet F_(N+1). Lichý případ má navíc předem uloženou nenavštívenou
nulovou signaturu; tuto konvenci jsme už vysvětlili u F079.

Zbývá-li m=N−2l vrcholů, každá z d=m−1 větví odpovídá jedné hraně.
Lokální počet updatů je1+d+d². Jejich součet dává správné W_N
z odpovědi255; pro sudé N se odečte phantomový příspěvek1 terminálu.
Součet rozhodovacích uzlů má na úplné úrovni phantomový člen−1,
proto je nutná již známá oprava V_N+3. Uzavřené tvary V,W se nemění.
Samostatně je chybný asymptotický koeficient N/5, viz F151.

Obrázek123 má34 popsaných stavů a97 větví. Při čtení všech zdrojových
segmentů se ukázala jedna špatná hrana v obou verzích: F153.
Číselná rovnice1·7+7·5+15·3+10·1+2=99 a příklad větví35,36,38
u signatury00101101 na str.122 jsou správně. Rovněž počty párování
K16 a K32 souhlasí s přesným dvojitým faktoriálem.

Úloha256 má vysvětlený obecný rozklad na dva sudé grafy a menší lichý
neúspěch. Přesné účetnictví kořene a terminálů je v C041; vzhledem
k možné schematičnosti odpovědi ponecháváme celé256 jako partial.

## Extrémní problém257–258 a omezené permutace259

U extrémního problému první volba obsahuje nejmenší aktivní položku
a libovolnou podmnožinu ostatních. Signatury jsou počáteční plná
množina a všechny množiny bez první položky:2^(n−1)+1.
Každý neprázdný stav s nu položkami má2^(nu−1) větví.
Obrázek257(b) byl z obou zdrojů přečten vektorově:9 stavů a21 hran,
všechny správné. Několik hran je vykresleno společným tahem přes
mezilehlé uzly; segmenty se proto správně rozdělily v těchto uzlech.

Vzorec258 je binomická transformace lokální ceny v_n, odvozená
v dřívějších poznámkách z(1+a)^(n−1) a její derivace. Nově prohlédnuté
oba obrazy souhlasí s přijatou algebrou. Člen1800n2^n je součin
1800·n·2^n, nikoli1800n². V16=40 454 337 297 a v16=10 480 142 147
zůstávají přijaté; n16 se neenumerovalo.

Úloha259: původní přesné důkazy počtů uzlů, updatů a F080 platí.
Oba celé zdroje včetně slovního popisu signatur znovu přečteny;
upozornění na doplněk množiny Y patří ke stejné staré F080.
Žádná z dvaceti nativních permutačních enumerací se neopakovala.

## Kruhové problémy260

Obecný důkaz lineárního počtu stavů a updatů je v F152. Počet řešení
L_n+2 je dříve obecně dokázán v MATCHING199_201_SOURCE_NOTES.md;
F002 o pevných bodech se tím nemění. Nově jsme prověřili celý ZDD
výpočet n3,…,24 a všechny stavy porovnali s obecnými rodinami.

Pro ménage po pevném usazení žen jsou zakázané dvě pozice každého
muže. Zakázaná políčka tvoří cyklus2n. Inkluze–exkluze používá
`r_k=(2n/(2n−k))*binom(2n−k,k)` a počet
`sum_k (−1)^k r_k (n−k)!`. Sedm nových n3,…,9 souhlasí s nezávislým
modelem i nativním DLX6; model porovnal MRV a levý pivot.
Pro pevné k platí r_k(n−k)!/n!→2^k/k!. Bonferroniho sudé a liché
částečné součty pak sevřou podíl počtu řešení a n! mezi aproximace
exp(−2). Proto vytištěné n!/e² asymptoticky platí.

Odhady základů3.1 a2.56 a možné Theta(n exp(n)) jsou v odpovědi
výslovně empirické a nejisté; neoznačujeme je za dokázané věty.
Sedm malých případů nestačí ani k potvrzení historického obratu
heuristiky při n13. Delší extrapolaci jsme výslovně vynechali.

## Přesně vynechané náročné reprodukce

Všechny následující položky mají v registru **verified:false**:

- Str.121: historické náklady a paměť K16 (X360Mμ/6KB, Z2Mμ/2.5MB)
  a K32 (X34 tisícPμ/25KB, Z16Gμ/85MB). Matematické počty párování
  a uzlů byly ověřeny samostatně; nevznikla nová velká enumerace.
- Str.122: Langford n14 náklady X15Gμ/Z11Gμ; n16 X1153Gμ/Z450Gμ,
  paměť20GB a500 milionů uzlů. Počet326 721 800 je normalizovaný
  zrcadlením; nejde o rozpor s653 443 600 orientovanými řešeními.
  Samotný n16 cenzus a500milionový ZDD se nově nevytvářely.
- Odpověď260: dlouhé empirické fitování a srovnání MRV od n13,
  včetně základů3.1/2.56 a domnělého Theta(n exp(n)). Uloženy jsou
  pouze malé případy a jejich přesný model, bez takového závěru.

Vynechání vyplývá z pokynu uživatele nevyžadovat dlouhý brute force.
Nenahrazuje otevřené interpretační otázky C041/C042 a neuzavírá je.
Následuje historie123, konec souhrnu a úlohy261 dál.
