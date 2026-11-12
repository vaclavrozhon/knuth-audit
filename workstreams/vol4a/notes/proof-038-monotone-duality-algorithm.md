# §7.1.1–26/27: svědci, algoritmus X a jeho náklady

6. listopadu 2026, X0068. Originály zadání p81–82/file98–99 a odpovědí
p537–538/file554–555. Známé erratum přidává v26 požadavek
„Efficiently exhibit“; následující konstrukce jej zahrnují. Žádný běh
algoritmu, žádná enumerace. Přebíráme P0602/P0611/P0620 pouze pro
jejich přesný obecný obsah o kladných prime formách a antichainech.

## P0633: vstupní doména a prázdné rodiny

Označme F rodinu klauzulí monotónní CNF f a G rodinu termů monotónní
DNF g; členy jsou množiny indexů. Obě rodiny jsou množiny bez duplicit
a antichainy, protože jde o prime formy. Proto pro různé členy I,I'
není I⊆I', analogicky pro J,J' v G.

Konstanty mají přesný význam:

    F=∅: f=1;        F={∅}: f=0;
    G=∅: g=0;        G={∅}: g=1.

Rodina s prázdným členem nemá jiné členy. Proměnné mimo sjednocení
obou rodin nejsou relevantní a ve výsledném svědku mohou dostat
libovolné hodnoty. Při rekurzi je lze pro účely výpočtu vynechat,
ale při návratu se doplní, vedle výslovně větvené souřadnice.

## P0634: 26(a), disjunktní členy

Je-li I∩J=∅ pro I∈F,J∈G, zvolíme x jako charakteristický vektor J.
Term J je pravdivý, ale klauzule I nepravdivá; tedy g(x)=1, f(x)=0.
To platí i s prázdným I nebo J. Průchod množinami příslušný vektor
vytvoří přímo. Pokud test(a) neuspěje, každý term G protíná každou
klauzuli F, takže podle P0602 máme bodově g≤f.

## P0635: 26(b), obě nerovnosti sjednocení

Předpokládejme, že (a) neuspělo. Je-li k∈J∈G mimo ∪F, položme
x=1_(J\{k}). Každá klauzule I protíná J, a to mimo k; tedy f(x)=1.
Term J není pravdivý a žádný jiný J' nemůže být podmnožinou
J\{k}, protože by odporoval antichainu. Proto g(x)=0.

Je-li naopak k∈I∈F mimo ∪G, dejme nuly přesně na I\{k} a jinde
jedničky. Každý term J protíná I mimo k, takže g(x)=0. Klauzule I
obsahuje jedničku k a každý jiný I' má prvek mimo I, také s hodnotou1.
Tedy f(x)=1. Obě konstrukce jsou přímé a polynomiální v zapsaném
vstupu; nejsou založeny na hledání ve všech přiřazeních.

## P0636: 26(c), obě velikostní podmínky

Opět předpokládejme, že (a) neuspělo. Pro |J|>|F| vyberme z každého
I∩J jeden prvek, například nejmenší. Jejich sjednocení S má nejvýše
|F| prvků, tedy S⊊J. Vektor x=1_S splňuje všechny klauzule a žádný
term: J není celý obsažen a ostatní J' mají prvek mimo J. Dostáváme
f(x)=1,g(x)=0.

Duálně, pro |I|>|G| vyberme z každého I∩J jeden prvek a jejich
sjednocení označme S⊊I. Položme x=0 na S a x=1 jinde. Každý J
obsahuje nulu, I má alespoň jednu jedničku a ostatní I' mají prvek
mimo I. Opět f(x)=1,g(x)=0. Konstrukce zahrnuje i případ prázdné
opačné rodiny, kdy S=∅. Volby a zápis vektoru jsou polynomiální.

## P0637: 26(d), existence i efektivní konstrukce

Po neúspěchu(b) máme společnou množinu proměnných U=∪F=∪G, |U|=n.
Každé I určuje 2^(n−|I|) přiřazení, kde jeho klauzule selže;
každé J určuje 2^(n−|J|) přiřazení, kde jeho term uspěje.
Označme součet těchto počtů s. Jsou-li s<2^n, unie všech uvedených
„špatných“ událostí nemůže pokrýt krychli, takže existuje f=1,g=0.
Události nemusejí být disjunktní; s počítá jejich incidence.

Pro konstrukci udržujme pevný prefix α a r volných souřadnic.
Invariant je S(α)<2^r, kde S(α) je součet počtů kompatibilních
dokončení všech špatných událostí. Při volbě dalšího bitu

    S(α0)+S(α1)=S(α).

Proto má alespoň jedna větev hodnotu <2^(r−1). Pokud ji má větev0,
zvolíme0, jinak1, přesně jako odpověď. Po n krocích je S<1,
tedy S=0, a dostali jsme žádané přiřazení. Pro n=0 je prázdný
vektor přímo svědkem, pokud je součet0<1.

Každá událost je pouze seznam požadovaných nul nebo jedniček.
Její příspěvek po prefixu je0, pokud vznikl konflikt, jinak mocnina2
podle počtu zbývajících volných bitů. Udržování kompatibility a počtu
zbývajících požadavků dovoluje při každém kroku projít N=|F|+|G|
událostí. Celé počty potřebují O(n+log N) bitů, takže například
O(N n(n+log N)) bitových operací po přípravě incidence stačí.
To je explicitní polynomiální svědek, nikoli existenční union bound.

## P0638: kofaktory a zachování vstupního invariantu X3

Při x_k=1 jsou klauzule obsahující k automaticky splněny, takže

    F_1={I∈F : k∉I}.

Při x_k=0 se z ostatních klauzulí smaže k, tedy

    F_0=F_1∪{I : k∉I, I∪{k}∈F}.

U DNF je to duální: G_0 ponechá termy bez k, G_1 navíc přidá
termy původně obsahující k po jeho smazání. To jsou přesně čtyři
vytištěné rodiny. Odstranění členu, který obsahuje jiný, je platná
absorpce jak pro klauzule, tak pro termy. Po deduplikaci a absorpci
zůstávají kladné antichainy, tedy úplné prime formy příslušných
kofaktorů podle P0611/P0620. F_1 a G_0 byly antichainy už předem.
Vznik prázdného členu je ošetřen P0633 a absorbuje všechny ostatní.

Každý původní člen vytvoří nejvýše jeden člen daného kofaktoru;
proto |F_i|≤|F| a |G_i|≤|G|. Nezvětšuje se počet členů ani počet
proměnných. Kofaktorové vztahy a prime invariant tak platí na všech
úrovních rekurze, nikoli pouze při prvním volání.

## P0639: X1 a všechny terminální případy X2

X1 vrací platný svědek podle P0634–P0637. Předpokládejme nyní, že
žádný test neuspěl a |F||G|≤1.

Je-li součin0, má jedna rodina žádné členy. Rovnost sjednocení
pak nutí všechny členy druhé rodiny být prázdné. Antichain tedy
dovolí jen ∅ nebo {∅}. Dvě prázdné rodiny by vyvolaly(d), protože
s=0<1. Zbývají (F,G)=(∅,{∅}) nebo ({∅},∅), tedy stejné konstanty.

Je-li součin1, F={I},G={J}. Test(b) vynutí I=J, test(a) jejich
neprázdnost a test(c) velikost≤1. Jde tedy o tentýž singleton
a f=g=x_k. Dvojice ({∅},{∅}) by už byla zachycena(a).

Proto X2 správně vrací Λ právě v těchto dosud nerozlišených případech.
Ani konstanty ani nula členů nejsou přeskočeným předpokladem.

## P0640: X3, platnost návratu a ukončení

V neterminálním uzlu jsou obě rodiny neprázdné a po(a) nemají
prázdný člen. Po(b) mají stejnou neprázdnou podporu. Zvolené k lze
vzít z této podpory. Pak alespoň jedna klauzule i term obsahují k,
takže |F_1|<|F| a |G_0|<|G|. Proto oba potomci mají součin
v_i=|F_i||G_i| přísně menší než v=|F||G|, i po absorpci.

Indukcí podle v oba rekurzivní výsledky platí. Svědek kofaktorů0
rozšířený o x_k=0 je svědkem původní dvojice; obdobně pro1.
Vrátí-li oba potomci Λ, oba páry kofaktorů jsou stejné, takže f=g
pro obě hodnoty k, a návrat Λ je správný. Předčasný návrat prvního
svědka neovlivňuje korektnost. Doplňované irelevantní bity podle
P0633 nemění hodnoty kofaktorů. Klesající nezáporný celočíselný v
dokazuje ukončení; argument nepotřebuje výsledek testování příkladů.

## P0641: krátký člen a větvicí poměr

V X3 označme m nejmenší velikost členu v F∪G, N=|F|+|G|.
Neúspěch(d) dává po vydělení 2^n

    1 ≤ Σ_(I∈F)2^(−|I|)+Σ_(J∈G)2^(−|J|) ≤ N·2^(−m),

tedy 1≤m≤lg N. Je-li nejkratší I∈F, každý J∈G jej protíná.
Součet četností výskytu prvků I v G je alespoň |G|, takže některé
k∈I je v nejméně |G|/m termech. Pro toto k platí

    |G_0|/|G| ≤ 1−1/m ≤ 1−1/lg N.

Pro nejkratší J∈G dostaneme stejný závěr pro |F_1|/|F|.
Volba minimalizující

    ρ_k=min(|F_1|/|F|, |G_0|/|G|)

proto splňuje nápovědu. Dělitele jsou nenulové právě díky X2.
Index mimo společnou podporu by měl ρ_k=1 a nemůže zvítězit nad
nalezeným indexem s ρ_k<1. Četnosti lze získat přímo z incidencí.

## P0642: přesná majorizující rekurence počtu volání

Nechť N_0 je velikost původní dvojice; netriviální případ má N_0≥3.
Použijeme pro celý běh pevnou mez

    ρ=1−1/lg N_0,  tedy 0<ρ<1.

Protože N se v rekurzi nezvyšuje, P0641 zaručuje ρ_k≤ρ v každém
neterminálním uzlu. Jeden potomek má součin nejvýše ρv:

    v_0≤|F||G_0|,    v_1≤|F_1||G|.

Oba mají podle P0640 součin nejvýše v−1. Pro monotónní celočíselnou
majorantu tedy stačí

    A(0)=A(1)=1,
    A(v)=1+A(v−1)+A(floor(ρv)), v>1.

Indukce přímo dává horní mez A(|F||G|) počtu provedení X1.
Monotónnost A plyne ze samotné rekurence. Úspěšný dřívější návrat
může počet jen snížit. Pevná ρ brání záměně lokálně různých poměrů
za jednu neodůvodněnou rekurenci.

## P0643: řešení rekurence včetně malých zbytků

Položme B(v)=A(v)+1. Pro v>1 je

    B(v)=B(v−1)+B(floor(ρv)),     B(0)=B(1)=2.

Je-li q=floor(ρv)≥1, monotónnost při rozvinutí do q dává

    B(v) ≤ (v−q+1)B(q) ≤ ((1−ρ)v+2)B(q).

Pro q=0 mají všechny nižší netriviální argumenty rovněž nulový
menší větevní člen, takže B(v)=2v pro v≥1. Stejná nerovnost platí,
protože ρv<1. Tím je pokryt i okraj, kdy běžně napsané rozvinutí
s k=v−q dosáhne základního argumentu0.

Iterujeme v_(j+1)=floor(ρv_j) do v_t≤1. Stačí

    t=ceil(ln(v_0)/ln(1/ρ)).

Každý faktor výše je nejvýše M=(1−ρ)v_0+2, a proto B(v_0)≤2M^t.
Protože −lnρ≥1−ρ=1/lg N_0 a v_0≤N_0²/4, máme

    t=O((log N_0)²),   log M=O(log N_0),
    A(v_0) ≤ N_0^(O((log N_0)²)).

To je přesná vytištěná mez počtu volání. Případy N_0≤2 končí v X1/X2
a nevkládají se do logaritmu či do definice ρ. Nejde o odhad odvozený
z několika experimentálních časů.

## P0644: náklady jednoho uzlu a význam vstupní velikosti

Test(a) prohlédne dvojice členů, (b) jejich sjednocení, (c) velikosti
a vybrané průniky, (d) součty mocnin a případnou konstrukci P0637.
S explicitními bitovými množinami má každý z těchto kroků polynomiální
čas; absorpci lze provést porovnáním všech dvojic v rodině, také
polynomiálně. Četnosti pro volbu k a vytvoření kofaktorů jsou prosté
průchody incidencemi. To je algoritmický odhad, žádný takový průchod
nebyl za účelem tohoto auditu spuštěn.

Po neúspěchu(b)/(c) má každý I nejvýše |G| prvků a každý J nejvýše
|F|. Společná podpora proto má n≤|F||G| a celková incidence
je nejvýše 2|F||G|. Po přejmenování aktivních indexů je reprezentace
polynomiální v N. První přečtení libovolně dlouhého zápisu se účtuje
v jeho skutečné délce L; při časném selhání testu to nepředstírá čas
závislý jen na počtu členů. Celkově máme polynomiální počáteční
režii v L a výše doložený kvazipolynomiální počet uzlů s polynomiální
režií v N_0. Zadání samo požaduje počet provedení X1, který P0643
dokládá bez další modelové zkratky.

## P0645: dualita a celý dodatek o postupném „růstu“

Dualizace h*(x)=¬h(¬x) mění prime klauzule na prime termy. Proto
rovnost CNF f s DNF g znamená právě dualitu DNF s rodinami F a G;
nejde o rovnost dvou DNF se stejnými nekorigovanými značkami.

Pro růst označme požadovanou duální funkci h=g* a dosavadní DNF a.
Invariant a≤h platí od a=0. Pokud a≠h, rozlišující vektor musí mít
a(x)=0 a h(x)=1, ekvivalentně a(x)=g(¬x)=0. Z něj lze mazat jedničky,
dokud h zůstává pravdivá. Každý nižší bod má stále a=0 díky
monotónnosti a. Jediný průchod bity stačí k inkluzní minimalitě:
bit, jehož smazání jednou dalo h=0, nemůže po dalších smazáních
začít dávat h=1. Je potřeba nejvýše n vyhodnocení g.

Výsledná minimální pravdivá množina je prime term h. Je nový,
protože a na tomto bodě byla0. Přidáme jej do a; term implikuje h,
takže invariant zůstává. Konečně mnoho různých primes zaručuje
ukončení právě při a=h. Počet iterací je počet vypsaných primes,
nikoli předpokládané polynomiální číslo ve vstupu; velký výstup
není skryt. Tím je celý matematický dodatek o generování doložen.

## P0646: přesný externí vstup pro zlepšenou mez

Primární článek Fredman–Khachiyan, Journal of Algorithms 21 (1996),
618–628, byl dohledán jako [původní PDF](https://www.cs.tau.ac.il/~fiat/dmsem03/On%20the%20complexity%20of%20Dualization%20of%20monotone%20Disjunctive%20Normal%20Forms%20-%201996.pdf)
a uložen s metadaty v sources/fredman-khachiyan-1996.pdf.
Jeho Theorem1 na p620 uvádí čas N^(4χ(N)+O(1)), kde χ^χ=N.
Logaritmováním χ logχ=log N dostaneme χ∼log N/loglog N,
tedy přesnou citovanou asymptotickou mez. Aplikace používá stejnou
prime/antichain doménu; podmínky redukující počet proměnných na
polynom v počtu členů jsou v článku výslovné na p619 a byly přečteny.

Toto je položka external_input: úplný důkaz rafinovaného algoritmu
v pozdějších sekcích článku se zde neopakuje. Vlastní důkaz X1–X3
a jeho slabší vytištěné meze na tomto externím vstupu nezávisí.
Bibliografické údaje článku jsou tak ověřeny přímo; jeho další
aplikace nejsou tímto automaticky auditované.

## P0647: otevřený stav a co z kvazipolynomiální meze neplyne

Aktuální [primární preprint Kobayashi–Kurita–Wasa, verze2 z 9.10.2026](https://arxiv.org/abs/2610.11473v2)
nadále výslovně označuje polynomiální výstupovou dualizaci za otevřenou
a uvádí kvazipolynomiální obecný horní odhad. Použit je pouze tento
stav z abstraktu, nikoli nezávislá rekonstrukce jejich nové podmíněné
dolní meze. Kontrola a přesný limit jsou v
sources/dualization-status-2026-11-06.json.

Kdyby problém byl NP-úplný při běžných polynomiálních redukcích,
kvazipolynomiální algoritmus by dal stejný typ subexponenciálního
algoritmu pro SAT. To je důvod pro knižní kvalifikaci „unlikely“;
není to nepodmíněný důkaz, že NP-úplnost nemůže nastat. Stejně tak
poznámka o rychlejším praktickém chování není nový formální odhad:
nebyly reprodukovány empirické benchmarky a tato kvalitativní
poznámka není použita v žádném důkazu.

## Rozsah, errata a úplné stránky

Relevantní vrstvy all4a-pre/all4a/err4a/all4f0/all4f1 neobsahují
další změnu26/27. Známé doplnění efektivnosti v26 je zahrnuto.
Všechny části26 a celý algoritmus27 i matematické dodatky odpovědí
mají nyní argument; rafinovaná citovaná věta je přesný externí vstup.
Žádný nový nález ani kandidát.

P81/file98 obsahuje15–27:15–17 jsou v proof-034,18–21 v proof-035,
22–25 v proof-036 a26–27 zde. Veškerá matematika stránky včetně
přesahu algoritmu na82 a odpovědí je doložena. P537/file554 obsahuje
konec21, celé22–26 a začátek27: příslušné důkazy jsou proof-035/036
a tento soubor. Obě stránky tak mohou mít úplné argumentové pokrytí.
Historické isotone/unate názvy, Knuth–Moore/Gurvich–Khachiyan odkazy
a Lucas/Perrin priority zůstávají výslovné bibliografické výjimky.

P82 ani p538 ještě celé uzavřené nejsou: pokračují úlohami28–31
a odpověďmi28–30, které tento blok neprověřoval. Další sekvenční
úloha28; hlavní textový frontier p57/file74 a čtení p218 se nemění.

Doplnění seznamu zdrojů: prohlédnuty také krátké historické vrstvy
errata/text/err4f0.txt a err4f1.txt; nepřidávají relevantní změnu
tohoto matematického bloku.
