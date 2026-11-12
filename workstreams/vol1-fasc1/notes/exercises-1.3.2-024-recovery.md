# §1.3.2′, úloha 24 — úplný StrCpy a přesná cena

Zadání file55/p47, odpověď file114/p106, třetí digitální vydání
3. května 2023. Originální sazba byla zobrazena v
`images/recovery-strcpy-114.png`. Tato poznámka nahrazuje neuzavřenou
nákladovou část staré `exercises-1.3.2-021-026.md`; starý důkaz se nemaže.
Žádný program, starý verifikátor ani pipeline simulace se nespouštěly.

## 1. Přípustné stavy a přesný kontrakt

Zdroj začíná na s, cíl na d; n≥0 nenulových bajtů je následováno nulou.
Oba logické intervaly délky n+1 jsou disjunktní. Všechny dotčené zarovnané
octabytes jsou přístupné a adresová aritmetika nenaráží na zakázaný přechod
adresního prostoru. Jde o obyčejnou paměť bez souběžných změn či I/O efektů.
Volající poskytuje platný návratový rámec. Registry $0 až $9 a rM jsou
pracovní; globální ones a flip mají vytištěné hodnoty.

SUB při výpočtu rozdílu adres může u extrémních adres vyvolat V; pro obecný
modulární adresový kontrakt předpokládáme tento trip zakázaný nebo handler,
který zachová vypočtený výsledek. Důkaz nezahrnuje libovolný handler.
Konkrétní níže uvedený hraniční případ žádnou takovou výjimku nepotřebuje.
Paměťové dostupnosti a návratový rámec jsou vstupní podmínky, nikoli nová
tvrzení o všech OS. Normální stránka má délku dělitelnou osmi, takže
zarovnaný octabyte obsahující přístupný bajt nepřekračuje hranici stránky.

Po návratu musí bajty d,...,d+n odpovídat původním s,...,s+n a všechny
ostatní bajty musí zůstat stejné. Není slíbena nulová hodnota rM ani
zachování pracovních registrů. POP 0 nevrací žádný lokální výsledek.

## 2. Masky a inicializace pro všechna zarovnání

Položme a=s mod8, b=d mod8, U_k=octabyte obsahující s+8k a V_j původní
cílový octabyte obsahující d+8j. MMIX čte big endian a LDOU/STOU zaokrouhlí
adresu dolů na násobek osmi. Posuny o 64 dávají nulu.

Maska m=(-1)>>8a vybírá platný konec U_0. BDIF(ones,u) obsahuje bajt 1
právě tam, kde je bajt u nulový: max(1−x,0)=1 iff x=0 pro 0≤x≤255.
Úvodní AND s m tak vyloučí všechny nuly před začátkem řetězce.

Je-li b≥a, nastaví se r=8(b−a), l=64−r. Inicializační MUX vytvoří

    in = (U_0 & m) | ((V_0 << r) & ~m).

Následné spojení `in>>r` s V_0 při masce (-1)>>r zachová přesně prvních
b cílových bajtů a připojí správný zdrojový prefix. `$1=d−s`; při
`$0=s+8k` tedy adresa zápisu po zarovnání označuje V_k. Pro a=b je r=0,
l=64, žádné předchozí slovo se nepřimíchá. To pokrývá i oba začátky na
hranici octabyte.

Je-li b<a, první záporná větev nastaví r=8(8+b−a), l=8(a−b) a
`$1=d−s−8`. Inicializační MUX je nyní

    in = (U_0 & m) | ((V_0 >> l) & ~m).

Posun `in<<l` zachová prvních b bajtů V_0 a připojí konec U_0; jeho
posledních l bitů čeká na U_1>>r. Po načtení U_1 je `$0=s+8`, takže
upravený rozdíl adres stále vede do V_0. Pokud U_0 již obsahuje terminátor,
PBZ je nevykonaný skok a JMP 5F posune $0 o osm bez načtení dalšího U.
Tentýž adresový vztah proto platí i v této krátké větvi.

## 3. Invariant hlavní části a obou konců

Při každém spojení je `out=previous<<l` a `tt=current>>r`; rM má spodních
64−r bitů nastavených. MUX tedy spojí disjunktní bitová pole ve správném
pořadí. Inicializační výše popsaná výplň nahrazuje neexistující předchozí
slovo původním cílovým prefixem.

Invariant před zpracováním dalšího slova: celý již zapsaný logický prefix
se rovná zdroji, neobsahuje terminátor a nic mimo něj nebylo změněno;
out a in obsahují přesně potřebné dva sousední fragmenty. Zápis v 3H
nastane jen při t=0, tedy celý právě používaný vstupní fragment je nenulový.
Předchozí zadržený fragment také neobsahoval terminátor, jinak by rutina
už odešla. Následující čtení a posuny zachovají invariant.

Při t≠0 se nejprve spočte mm=t>>r. Je-li mm≠0, nejméně jedna nula
je v nyní vydávaném slově. BNZ přejde přímo k poslednímu částečnému zápisu.
Je-li mm=0, vydávané slovo ještě neobsahuje žádnou nulu a smí se zapsat
celé; větev 5H posune adresu a použije out=in<<l, mm=t<<l. První nula
je nyní v tomto zadrženém fragmentu. Není potřeba načíst slovo za ním.
Pro r=0 tato odložená větev nemůže nastat, protože t>>0=t≠0.

V konečné větvi je mm nenulová a v každém nulovém bajtu obsahuje bit 1.
MOR s flip=#0102040810204080 obrací pořadí osmi bajtů. Výraz
`mm & ~(mm−1)` izoluje nejnižší nastavený bit; po obrácení bajtů zpět jde
o bit v nejnižší pozici prvního nulového bajtu v pořadí řetězce. Odečtení
jedničky vytvoří samé jedničky právě v bajtech ZA terminátorem. Závěrečný
MUX proto převezme nový prefix včetně terminátoru a zachová původní cílový
suffix. Inicializace již zachovala prefix před d.

Libovolné nulové bajty před s či za s+n nemohou změnit první platný marker.
Ani nulové bajty původního cíle nejsou součástí testované zdrojové masky.
Logická disjunkce intervalů postačí i při překryvu jejich zaokrouhlených
octabytes: každý zápis zachovává všechny bajty mimo cílový interval,
tedy zejména dosud nepřečtené zdrojové bajty. Konečnost n a posun čtení
po osmi zaručí ukončení. Důkaz zahrnuje n=0 a všech 64 dvojic (a,b).

## 4. Přesné mems a oops, včetně všech větví

Definujme

    q = floor((a+n)/8), t = floor((b+n)/8), I = [b<a].

q je index zdrojového octabyte s terminátorem, t odpovídající index cíle.
Každý U_0,...,U_q se čte právě jednou a každý cílový V_0,...,V_t se právě
jednou zapisuje. Navíc se cíl načte při inicializaci a při posledním MUX,
i kdyby to bylo totéž slovo. Počet mems je tedy přesně

    M = 4+q+t.

Všechny zde použité instrukce mají základní cenu 1υ; nesprávná predikce
podmíněného skoku přidá 2υ. POP stojí zvlášť 3υ. Přímé sčítání bloků:

| Blok | mems | oops |
|---|---:|---:|
| b≥a: vstup až po JMP 4F | 2 | 21 |
| b<a, q≥1: vstup až po vykonaný PBZ 2F | 2 | 25 |
| následující 2H: SLU,LDOU,INCL,BDIF | 1 | 4 |
| úplný cyklus od 4H přes 3H a 2H | 2 | 8 |
| 4H s první nulou v nynějším cíli, včetně posledních 9 instrukcí | 2 | 18 |
| 4H s nulou až v odloženém fragmentu, včetně 5H a posledních 9 | 3 | 20 |
| b<a,q=0: celý vstup, nevykonaný PBZ,JMP 5F,5H a posledních 9 | 4 | 40 |

Posledních devět je LDOU,MOR,SUBU,ANDN,MOR,SUBU,PUT,MUX,STOU.
První koncový řádek zahrnuje PBZ nevykonaný (3υ), BNZ vykonaný (3υ);
druhý PBZ nevykonaný (3υ), BNZ nevykonaný (1υ), STOU a 5H.

Pro b≥a je q úplných cyklů a δ=t−q∈{0,1} označí odložený konec.
O=21+8q+18+2δ=39+6q+2t. Pro b<a,q≥1 je q−1 úplných cyklů,
δ=t−q+1∈{0,1}, takže O=25+4+8(q−1)+18+2δ=41+6q+2t.
Pro b<a,q=0 je také t=0 a platí zvláštní řádek 40. Celkem, BEZ POP,

    T = (4+q+t)μ + (39+6q+2t + I(2−[q=0]))υ.              (1)

Toto je identita, nikoli asymptotika. Přibližný knižní vzorec má správný
hlavní člen (n/4)μ+nυ a omezenou chybu závislou na zarovnání. V dlouhé
části se provede jedno čtení a jeden zápis na osm bajtů, což dosahuje
datové propustnosti běžných osmibajtových paměťových instrukcí. Netvrdí se
globální minimum počtu instrukcí nebo všech konstant pro každé n.

## 5. Přesné srovnání a hraniční kandidát

Triviální vytištěný fragment má n+1 čtení, n+1 zápisů, n+1 průchodů
čtyřmi instrukcemi, úvodní SUBU a poslední chybnou predikci. Jeho přesná
cena bez návratu je (2n+2)μ+(4n+7)υ, jak uvádí zadání.

Nejvstřícnější srovnání účtuje stejný POP oběma realizacím, tedy jej
vynechá na obou stranách. Pro n≥8 je q≥1 a kladná úspora mems je
2n−2−q−t. Při μ=υ je úspora celkem

    Δ = 6n−34−7q−3t−2I.                                  (2)

Pro n=8 jsou q=t=1 a Δ=4−2I≥2. Pro n=9: a=b=7 dává q=t=2 a Δ=0;
a=7,b≤6 dává Δ=1; a≤6,b=7 dává Δ=7; oba≤6 dávají Δ=10−2I≥8.
Pro n≥10 použijeme q,t≤(n+7)/8 a I≤1, tedy
Δ≥(19n−179)/4>0. Proto při kladných μ≥υ je program pro n≥8 nejvýše
stejně drahý, avšak rovnost nastává při n=9,a=b=7,μ=υ. V ostatních
případech uvedené oblasti je striktně levnější.

Konkrétně vezměme s=Data_Segment+7, d=Data_Segment+263 a devět bajtů
ASCII `a` následovaných nulou. Libovolná přístupná okolní paměť může být
nulová. Intervaly jsou disjunktní a q=t=2. StrCpy má vstup 2μ+21υ,
dva úplné cykly 4μ+16υ a přímý konec 2μ+18υ, tedy **8μ+55υ**.
Triviální fragment má **20μ+43υ**. Při μ=υ jsou oba za 63υ před POP,
resp. oba za 66υ při společném POP. Pokud by se POP účtoval pouze StrCpy,
pak je nový program dokonce o 3υ dražší; pro kandidáta tuto nevstřícnou
konvenci nepotřebujeme.

Věta na p106 říká, že běh je méně nákladný pro n≥8 a μ≥υ, ale uvádí
jej jako „approximately“. Proto **MMIX-C0019 zůstává candidate, low**:
pro univerzální striktní čtení je (2) protipříklad, pro pouze orientační
srovnání přibližných cen tato jednotková hrana nemusí být zamýšleným
tvrzením. Možná přesná formulace: „no greater ...“, nebo výslovná výjimka
n=9, obě zarovnání7, μ=υ. Funkční chyba programu zjištěna nebyla.

## 6. Sazba, errata a rozsah uzavření

`results/errata-C0019.json` zachycuje 13 relevantních vrstev včetně
zdrojového err1f1, krátkých/dlouhých fasciklových errat, MMIXware obou
stránek, upstream bugs/rounding/warnings a obou historických vrstev Vol1
i druhého vydání. Všechny zachycené kontexty byly přečteny. Žádný se
netýká StrCpy nebo zdejšího prahu; upstream copy_block je jiná cache chyba.
Vyhledání StrCpy/n/4 a MMIX/106/copy v primárních doménách další opravu
neodhalilo. PDF verze a sazba se shodují s ostatními nálezy v této edici.

E024 má nyní úplný funkční a nákladový argument v rozsahu zadání, ale
přesná interpretace jedné navazující věty zůstává evidovaná v C0019.
Žádná stránka se neoznačuje za úplně uzavřenou jen z tohoto příkladu:
file55 obsahuje další úlohy a file114 začíná úlohu25.

Použití vzorů QUALITY_EXAMPLES: stavový vzor vede k odděleným vstupním
větvím a k přípustnému paměťovému stavu; nákladový vzor k rozpisu každého
skoku včetně chybných predikcí; binomický vzor k přesnému rozlišení
asymptotického hlavního členu a konečného univerzálního tvrzení.
