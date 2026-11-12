# Princip 0–1, celá p68 a Theorem C s jeho korolárem

Checkpoint X0099, P0932–P0942. Originál p68/file85 a začátku
p69/file86 je v `images/file085.png`, `file086.png`; oba
přečteny. První odstavec p68 je již celý v proof-069/P0931.
Zde se přesně přebírají algebraicky odvozené majority,
asociativita, distributivita a absorpce z proof-063. Žádný
z nich nepoužíval princip 0–1, takže následující důkaz není
kruhový. Celá 75 v proof-068 poskytuje pravidla intervalů N/D.
Žádný program, test všech bitových slov ani enumerace.

## V konečném grafu všechny hrany oddělují vrcholy — P0932

Pro různé vrcholy a,b vyberme první hranu a—u nejkratší
cesty a→b. Projekce na [a..u] má v a hodnotu a a v b
hodnotu u: u je jediný společný bod intervalů trojice b,a,u,
protože je na cestě a→b a další dva intervaly ho obsahují
jako konec. Vektor všech hranových projekcí je tedy injektivní.
Každá složka je booleovský homomorfismus podle P0927.

Pro konečnou neprázdnou algebru se použije přesně Theorem G
z proof-064; singleton má prázdný štítek. Prázdná algebra se
vloží do libovolné booleovské mocniny prázdným zobrazením.
Tím je konečný význam hranových štítků úplně doložen.
Pro nekonečnou algebru nemusí hrany existovat, například
v hustém řetězci. Obecné tvrzení o booleovských souřadnicích
proto níže dokazujeme poloprostory, nikoli předstíráním
konečně mnoha hran. Souřadnic může být nekonečně mnoho.

## Základní uspořádání a monotónnost projekcí — P0933

Pro pevný základ o pišme u≤_o v právě když u∈[o..v],
tedy m(o,u,v)=u. Je to částečné uspořádání: reflexivita je
krajní vztah; tranzitivita je N. Antisymetrie plyne z D:
z [ouv] a [ovu] vyjde [uvu], a tedy u=v.

Nechť p(s)=m(s,r,t) je projekce do libovolného intervalu.
Z u≤_o v a homomorfismu p plyne

    p(u)=m(p(o),p(u),p(v)),

takže p(u)∈[p(o)..p(v)]. Absorpce P0866 dává
m(o,p(o),p(v))=p(o), tedy p(o)∈[o..p(v)]. Vnoření N
nyní dává p(u)∈[o..p(v)]. Projekce je proto monotónní
v uspořádání se **stejným** původním základem o; základ
se ve výsledku neposouvá na p(o).

Proto je m(u,v,z) monotónní v každém argumentu vzhledem
k ≤_o: při změně jediného argumentu jde o právě dokázanou
projekci, zbývající dva jsou pevné. Dvě po sobě jdoucí
změny dovolují současně u≤_o c, v≤_o d a dávají

    m(u,v,z)≤_o m(c,d,z).

## Přidání jednoho bodu ke konvexní množině — P0934

Je-li A neprázdná konvexní množina a x libovolný bod, pak

    hull(A∪{x}) = H = union(c∈A) [x..c].          (H)

H obsahuje A a x. Pro u∈[x..c], v∈[x..d] s c,d∈A
a libovolné z dává P0933

    m(u,v,z)≤_x m(c,d,z).

Bod e=m(c,d,z) je v A díky konvexitě, a proto m(u,v,z)
leží v [x..e]⊆H. H je tedy konvexní. Každá konvexní
množina obsahující A a x musí obsahovat každý [x..c],
takže H je nejmenší taková. To je obecný důkaz (H),
nezávislý na pozdějším Theorem C i na booleovském modelu.

## Konvexní poloprostor odděluje libovolné dva body — P0935

Pro a≠b vyberme inkluzně maximální konvexní A obsahující a
a neobsahující b. V konečném prostoru takové A existuje
z konečnosti. Pro libovolnou množinu M použijeme standardní
Zornovo lemma: rodina je neprázdná díky {a}, sjednocení
každého neprázdného řetězce je konvexní, obsahuje a a stále
neobsahuje b. Pro prázdný řetězec je horní mez {a}.
Zornovo lemma je zde výslovný obecný množinový princip,
nikoli skrytý závěr o konečnosti algebry.

Dokážeme, že také M\A je konvexní. Pro x,y∉A maximalita
a (H) dávají u,v∈A takové, že

    b∈[x..u],   b∈[y..v].

Pišme s∧t=m(b,s,t); asociativita s pevným středem b,
komutativita a majority dávají komutativní idempotentní
operaci s b∧s=b. Máme x∧u=b, y∧v=b. Položme p=u∧v,
které leží v A, protože u,v∈A. Pro libovolné z a
w=m(x,y,z) distributivita projekce dává

    w∧p = m(x∧p,y∧p,z∧p)
         =m(b,b,z∧p)=b,

neboť x∧p=(x∧u)∧v=b a y∧p=(y∧v)∧u=b.
Tedy b∈[w..p]. Pokud by w∈A, konvexita A a p∈A by
nutila b∈A, spor. Proto w∉A pro všechna z, přesně
konvexita komplementu. A je hledaný poloprostor.

## Vložení, ekvivalence identit a přesný počet testů — P0936

Pro každý poloprostor A je jeho indikátor h_A homomorfismus
do {0,1}: alespoň dva vstupy leží ve stejné z množin A,
M\A, a konvexita příslušné množiny tam ponechá jejich medián.
Proto h_A(m(x,y,z))=m(h_A(x),h_A(y),h_A(z)).
P0935 oddělí každé dva různé body, takže vektor všech těchto
indikátorů je injektivní. Každá mediánová algebra se tedy
vloží do booleovské mocniny se souřadnicovým mediánem.
Prázdný a jednobodový případ jsou triviální a Zorn nepotřebují.

Jestliže dvě mediánové formule souhlasí na bitech, souhlasí
po dosazení libovolných bodů ve všech souřadnicích vložení,
a injektivitou i v původní algebře. Opačný směr platí,
protože {0,1} je sama mediánová algebra. To dokazuje
celý princip 0–1 pro identity, ne pouze konkrétní tabulku.

Pro formule bez konstant v n≥1 proměnných je každá
interpretace selfduální a vrací 0 na všech nulách, 1 na všech
jedničkách, indukcí podle termu. Ze 2^n vstupů proto stačí
jeden z každé komplementární dvojice, tedy 2^(n−1) vstupů.
Dvojice samé nuly/samé jedničky je automatická pro obě
formule, takže stačí právě uvedených **2^(n−1)−1** kontrol
tohoto postupu. Pro n=1 je to 0 kontrol a všechny termy
jsou projekce. Nulární term bez konstant vůbec nevzniká.
Neprohlašuje se, že jde o optimální algoritmus pro každý
jednotlivý pár formulí nebo o celkový čas bez ceny evaluace.

## Identita (64) a význam vyšších mediánů — P0937

Na bitech má m(x,w,m(y,w,z)) při w=0 hodnotu xyz,
při w=1 hodnotu x∨y∨z. Stejné dvě hodnoty má většina
pěti vstupů x,w,y,w,z: při dvou nulových w musí být
všechny x,y,z jedničky, při dvou jedničkových w stačí
jediná další jednička. Asociativita dává druhý vytištěný
způsob uzávorkování; princip 0–1 dává celou (64) v každé
algebře.

Vyšší lichý medián zde znamená mediánový term představující
booleovskou většinu, nikoli neexistující úplné uspořádání M.
Takový term existuje podle přesně dokázaného Theorem P,
a princip 0–1 zaručí nezávislost na jeho volbě i symetrii
multimnožiny vstupů. Vzorec (49) byl v Boolean případě
úplně dokázán v P0831; tentýž princip jej nyní převádí
i do libovolné mediánové algebry, bez opakování toho důkazu.

## Identita (65), všechny arity a opakované vstupy — P0938

Pro s≥1 má levá strana při y=0 hodnotu AND_i x_i,
při y=1 hodnotu OR_i x_i, indukcí přes jednotlivé ternární
mediány. Na pravé straně je s proměnných x_i a s−1
kopií y, dohromady 2s−1 prvků. Při y=0 je většina
pravdivá právě když všech s vstupů x_i je 1; při y=1
právě když alespoň jeden je 1. Obě strany tedy souhlasí
na bitech a podle P0936 v každé algebře. Pro s=1 jsou
obě strany x_1, bez mediánového kroku; nejde o vynechaný
krajní případ. Výrok o počtu a téměř polovině kopií y
je přesně s−1 z 2s−1 pozic.

## Konvexita, ideály a dvoubodový obal — P0939

V mediánovém grafu jsou grafové intervaly stejné jako
algebraické. Proto C obsahuje interval mezi každými dvěma
svými prvky právě když obsahuje m(u,v,z) pro u,v∈C
a všechna z∈M. Konvexní množina a ideál jsou totožné
podmínky. „Všechny vrcholy nejkratší cesty“ znamená všechny
takové cesty, protože interval je jejich sjednocení.

Průnik libovolné rodiny konvexních množin je konvexní;
M je konvexní. Nejmenší konvexní nadmnožina dané množiny
tedy existuje jako průnik všech takových nadmnožin.
Interval [u..v] je konvexní podle P0872, obsahuje u,v,
a každá konvexní množina obsahující u,v musí obsahovat
celý interval. Proto je přesně hull{u,v}, včetně u=v.

## Celý Theorem C: obraz, nejmenší obal a pevné body — P0940

Pro neprázdný konečný seznam v_1,...,v_m, m≥1, definujme

    F(x)=m(v_1,x,m(v_2,x,...,m(v_(m−1),x,v_m)...)).

Pro m=1 znamená F(x)=v_1. Asociativita s pevným středem
x dovoluje jakékoli vytištěné uzávorkování (66).
Na každé booleovské souřadnici se F chová přesně takto:

| hodnoty v_i v dané souřadnici | F(x) |
|---|---|
| všechny 0 | 0 |
| všechny 1 | 1 |
| obsahují 0 i 1 | x |

To plyne z AND/OR rozkladu v P0938. Tabulka dává
F(v_j)=v_j pro každé j a F(F(x))=F(x). Její platnost
se principem 0–1 přenáší do M. Proto x je v obrazu F
právě když F(x)=x, což dokazuje vytištěnou druhou část věty.

Obraz je obsažen v obalu: zprava postupně tvořené mediány
mají dva vstupy již v obalu a třetí x libovolný. Pro m=1
je to přímo v_1, pro m≥2 je to přesně indukční argument
s x' v původním důkazu. Následující identita (67) ukazuje
konvexitu obrazu. Ten obsahuje všechna v_j, takže opačná
inkluze obalu do obrazu plyne z minimality. Tím je (66)
celé doloženo i s oběma inkluzemi, nikoli jen jako souřadnicový
popis širší booleovské krychle.

## Identita (67) a jednoznačně nejbližší bod — P0941

Rovnice (67) je přesně

    m(x,F(y),F(z))=F(m(x,y,z)).

Ve třech řádcích předchozí souřadnicové tabulky jsou obě
strany po řadě 0, 1 a m(x,y,z). Princip 0–1 tedy dává
identitu v celé M. Pro dva body F(y),F(z) obrazu a
libovolné x je výsledek opět v obrazu; to je požadovaná
konvexita použitá v P0940.

Nyní podle známé opravy dosaďme **y=x**:

    m(x,F(x),F(z))=F(m(x,x,z))=F(x).

Každý c∈C má tvar F(z), takže F(x)∈[x..c] pro všechna
c∈C. V grafové metrice to dává

    d(x,c)=d(x,F(x))+d(F(x),c)≥d(x,F(x)).

Rovnost nastane právě pro c=F(x). Je tedy doložena nejen
existence nejbližšího bodu, ale jeho jednoznačnost a tvrzení,
že leží na nejkratší cestě z x ke každému bodu C. Obraz
je neprázdný, protože m≥1 a obsahuje všechna v_j. Pro x∈C
je nejbližším bodem samozřejmě samo x.

## Celý Corollary C a příklad na začátku p69 — P0942

V souřadnicích předchozí tabulky rovnice F(x)=x říká:
souhlasí-li všechny v_i v souřadnici na c_j, musí i x_j=c_j;
jinak je x_j volná. P0940 proto dává přesně text koroláru.
Podmínka **x∈M** zůstává nutná: neprohlašujeme, že všechny
formálně odpovídající binární vektory jsou vrcholy grafu.

V původním stromu (63) jsou štítky c=1000000,
g=1011010, h=1010001. Společné pozice jsou 1=1,2=0,5=0,
ostatní se liší. Vzor je tedy 10**0**. Z úplné tabulky
P0928 jej splňují právě c,d,e,g,h. a nesplní první pozici,
b druhou a f pátou. Je to přesně vytištěný pětibodový obal.

## Úplná stránka a errata

| obsah p68 | argument |
|---|---|
| přidaná hrana, duplikace a šestibitové štítky | P0931, proof-069 |
| konečné i obecné booleovské reprezentace | P0932–P0936 |
| princip 0–1 a 2^(n−1)−1 testů | P0936 |
| celý (64), převod(49), celý(65) | P0937/P0938 |
| konvexní množina, ideál, existence obalu a interval | P0939 |
| Theorem C, oba směry a pevný bod | P0940 |
| všechny kroky(67), konvexita, gate a nejbližší bod | P0941 |

P68 má tedy úplný argumentový rozsah. Na p69 jsou zatím
hotové pouze korolár a jeho první příklad; čtyřcyklové
ekvivalence, obecná úplnost těchto ekvivalencí a Algorithm H
jsou další samostatný blok. Nic z nich se neuzavírá tímto
důkazem booleovské reprezentace.

Pět relevantních vrstev `all4a-pre`, `all4a`, `err4a`,
`all4f0`, `all4f1` prohledáno pro p68–69/zero-one/convex
hull/Theorem C. Známé p68 line −2 (18. 6. 2011) mění
Setting x=y na Setting y=x a je zohledněno výše; oprava
osmibitových štítků z 6. 10. 2018 je v P0931. Původní
sazba obou je v `images/proof-y-errata08.png`. Žádný nový
nález. Text zde nemá bibliografický odkaz vyžadující výjimku;
Zornovo lemma je výslovný standardní množinový vstup pouze
pro oddělení v libovolné nekonečné algebře.
