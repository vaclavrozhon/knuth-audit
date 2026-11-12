# MPR 121: všechny části, podpory, nulové události a nekonečné entropie

D219 a známá oprava E135, 7. listopadu 2026. Staré nálezy F006/F008
se přebírají pod původními ID; žádný nový nález ani kandidát. Původní
PDF p24/file44 a p390/file410 i autorův PS p24/46,file30/52 byly
zobrazeny. Starých 6560 numerických kontrol se neopakuje a nenahrazuje
jimi obecný důkaz. Nový jediný cílený běh ověřuje dvě tištěná zaokrouhlení
přesnými racionálními intervaly; trval 0.000794268969912082 s pod nice15.

## Definice, součty a převzaté F006/F008

Zadání popisuje diskrétní zákony x,y na společné konečné nebo spočetné
množině. Sjednocení jejich kladných podpor je spočetné: hodnot s hmotností
alespoň 1/j může být nejvýše j. Logaritmus lg má základ 2. Člen s y(t)=0
je nulový podle tištěné konvence, i když x(t)=0. Je-li y(t)>0=x(t),
člen divergence je +∞. Poměr 0/0 lze na společném nulovém bodě zvolit
libovolně, neboť ho X ani Y nenavštíví.

Součet D=Σ y(t)lg(y(t)/x(t)) je vždy dobře definovaný v rozšířeném
smyslu. Záporné členy odpovídají 0<r=y/x<1 a mají velikost
x·(−r ln r)/ln2≤x/(e ln2); jejich součet je konečný.
Poslední dvě tištěné formy D=E lgρ(Y)=Σy lgρ platí obecně.
První forma E[ρ(X)lgρ(X)] sečte jen body x>0 a potřebuje y≪x.

Přesný starý důkaz F008 v results/information.json a archivním
knuth-report-f006-f008-draft.txt skutečně pokrývá tuto chybu:
x=(1,0), y=(1/2,1/2) dává ρ(X)=1/2 jistě. První očekávání je −1/2,
další dvě jsou +∞; také Eρ(X)=1/2 místo 1 v odpovědi (b). Žádný
sporný součin 0·∞ ani dosazení v nulové události není k rozporu
potřeba. Oprava: definovat D součtem a první očekávání použít
jen při y≪x; případ nesouhlasných podpor v (b) vyřešit nejprve.

Staré F006: pro Y=2 jistě je tištěné E lg(1/Y)=−1, ale
správné E lg(1/y(Y))=lg1=0. To je rozpor i s odkazovanou
definicí svazku 3. V této poznámce se všude používá opravené

    H_Y=Σ_t y(t)lg(1/y(t))=E lg(1/y(Y))∈[0,+∞].

Původní Eq.6.2.2–(18) na p442 a nulová konvence na p443 byly
zobrazeny v DjVu svazku 3,file453–454. Ověřený rozsah je pouze
definice, konvence a interpretace průměrné informace; graf,
algoritmy a další tvrzení těch stran zde nejsou uzavřeny.

E135 zaznamenává známou autorskou změnu názvu z 31.5.2021:
„divergence of Y from X“ se změnilo na „divergence of X from Y“.
Je vidět v all4f5,file3 a TeX281–285; vydání 4B ji již obsahuje.
Je to autorova konvence, nikoli náš nález nebo důvod měnit D(y||x).

Intuitivní věta o ztrátě informace má přesný obsah: překvapení
při výsledku t je −lg x(t), zatímco pro pravý zákon je −lg y(t).
Rozdíl je lgρ(t), a jeho střední hodnota pod Y je D(y||x).
Při singularitě je nekonečná. Netvrdí se, že jednotlivé
neceločíselné hodnoty jsou délkami konkrétního prefixového kódu.

## (a) Každý člen a obě desetinné hodnoty

Čtyři nezměněné strany mají y=x=1/6, takže přispívají 0.
Na dvou změněných stranách jsou y=1/5 a 2/15. Poměry y/x
jsou 6/5 a 4/5, poměry x/y jsou 5/6 a 5/4. Proto přesně

    D(y||x)=(1/5)lg(6/5)+(2/15)lg(4/5),
    D(x||y)=(1/6)lg(5/6)+(1/6)lg(5/4)=(1/6)lg(25/24).

scripts/verify_mpr121_log_rounding.py používá jen identitu
ln r=2Σ_(k≥0)s^(2k+1)/(2k+1), s=(r−1)/(r+1). Vznikne
integrací geometrické řady 2/(1−s²), konvergentní pro |s|<1.
Po N=12 členech má ocas velikost nejvýše
2|s|^(2N+1)/[(2N+1)(1−s²)], protože jmenovatele dalších
členů jsou nejméně 2N+1. Tato mez je použita oboustranně
i pro záporné s, nikoli jako empirický odhad.

Všechny součty, ocasy a dělení jsou přesné Fraction operace.
Kladný interval pro ln2 umožňuje bezpečné dělení intervalů
kladných čitatelů. Certifikované meze dávají přibližně
[.009683135181777106,.009683135181780074] a
[.009815614842261405,.009815614842264413]. Přesné racionální
meze jsou v výsledném JSON; leží striktně uvnitř intervalů
pro zaokrouhlení na .0097 a .0098. Smyčky mají pevně 12 členů,
končí a neprocházejí žádné zákony ani vzorky.

## (b) Nezápornost a přesně kdy nastává rovnost

Pokud některé y(t)>0=x(t), je D=+∞ a tvrzení je vyřešeno.
Jinak Eρ(X)=Σ_(x>0)y=1. Funkce f(r)=r lg r, s f(0)=0,
je striktně konvexní na [0,∞): pro r>0 má
f''(r)=1/(r ln2)>0; přísnost mezi 0 a b>0 plyne také
f(λb)=λf(b)+λb lgλ<λf(b) pro 0<λ<1.

Každý potřebný Jensenův a rovnostní krok dokládá tečna v 1:

    f(r)≥(r−1)/ln2, rovnost právě pro r=1.

Opravdu k(r)=r ln r−r+1 má derivaci ln r, minimum 0 v 1
a k(0)=1. Sečtením nezáporných x(t)k(ρ(t)) dostáváme

    D·ln2=Σ_(x>0)x(t)k(ρ(t))≥0,

protože Σx=Σy=1; argument platí i pro nekonečný kladný součet.
Je to tištěný Jensenův krok, včetně možnosti ρ=0. Součet
je nula právě tehdy, když k(ρ(t))=0 všude, kde x(t)>0,
tedy y=x na podpoře x. Absolutní spojitost zajišťuje
totéž mimo ni. Obrácení je bezprostřední. Tištěné „positive
random variable“ nepotřebuje dodatečnou přísnou kladnost:
nulové hodnoty jsou takto pokryty.

## (c) Normalizace i nulové případy

Pro p,q>0 jsou x̂=x/p a ŷ=y/q na T pravděpodobnostní zákony.
Jejich poměr je ρ·p/q, takže po sečtení každého členu

    D(ŷ||x̂)=Σ_(t∈T)y(t)/q·lgρ(t)+lg(p/q)
             =E(lgρ(Y)|Y∈T)+lg(p/q)≥0.

Singularita uvnitř T dává na relevantních stranách +∞;
přičítá se pouze konečná konstanta, žádné ∞−∞.

Je-li p=0<q, na každém Y-bodu v T je ρ=∞; obě strany
požadované nerovnosti jsou +∞. Pro q=0<p podmíněná událost
nemá hmotnost. Dřívější konvence knihy E(V|A)=EV při P(A)=0
dává vlevo nepodmíněné D≥0, zatímco lg(q/p)=−∞; mez je
triviální. Je-li veličina integrabilní, jde přímo o tu
konvenci; rozšíření na +∞ je rovněž jednoznačné.
Pro p=q=0 samotný lg(q/p) nemá hodnotu: toto nulové T
se vypustí, protože neposkytuje informaci. Nejde o dvojici
různých definovaných výsledků; hodnotu 0/0 nedoplňujeme
a za přirozenou doménu zápisu nevytváříme kandidáta.

## (d) Entropie na m bodech a rovnostní případ

Pro neprázdné S,|S|=m a uniformní x je y≪x a

    D(y||x)=Σ_(t∈S)y(t)[lg m+lg y(t)]=lg m−H_Y.

Konečnost S zaručuje konečnou entropii; nulové y-členy jsou 0.
Z (b) plyne H_Y≤lg m, rovnost právě pro y=x, tedy uniformní
zákon na celém S. H_Y≥0 plyne z 0≤y≤1. Případ m=1 dává
obě hodnoty 0. m=0 nemůže nést pravděpodobnostní zákon.
Interpretace H jako střední informace je přesně odkazovaná
definice, po opravě F006.

## Nezáporné řetězové pravidlo a úplná konkávnost

Tento oddíl nejprve dokládá základ, aby níže nebyl kruhový
argument o konečnosti entropií. Pro společný zákon z(u,v)
pišme x_v(u)=z(u,v)/y(v), jen když y(v)>0. Definujme
H(X|Y)=Σ_(v:y(v)>0)y(v)H(x_v). Členy jsou nezáporné.
Nulová vlákna se vynechají; libovolná volba zákona na nich
nemá vliv. Na z>0 má bodová identita

    lg(1/z(u,v))=lg(1/y(v))+lg(1/x_v(u))

dva nezáporné sčítance. Sečtením dostáváme bez odečítání
H_(X,Y)=H_Y+H(X|Y), i při +∞.

Funkce h(a)=−a lg a, h(0)=0, je konkávní a nezáporná
na [0,1]: h''(a)=−1/(a ln2)<0 uvnitř a okraje jsou spojité.
Pro konečnou směs a=Σ_j α_j a_j Jensen dává
h(a)≥Σ_j α_j h(a_j). Pro spočetnou směs seskupme členy
za N do jedné skupiny se souhrnnou vahou a jejich váženým
průměrem. Konečná nerovnost a nezápornost posledního členu
dávají h(a)≥Σ_(j≤N)α_jh(a_j). Limitou rostoucích pravých
stran získáme celý součet. Při nulové zbytkové váze poslední
skupinu vynecháme.

Pro každé u použijeme nerovnost na x(u)=Σ_v y(v)x_v(u)
a sečteme nezáporné členy. Vyjde
H_X≥Σ_v y(v)H(x_v)=H(X|Y), včetně nekonečných možností.
Následně H_(X,Y)≤H_X+H_Y, opět bez odčítání.

## (e) Produktový zákon a každá tištěná marginalizace

Marginály z splňují Σ_v z(u,v)=x(u), Σ_u z(u,v)=y(v).
Nezávislý zákon w(u,v)=x(u)y(v) má součet 1 a tytéž
marginály. Nezáporné součty dovolují měnit pořadí a dávají

    H_W=Σ_(u,v)x(u)y(v)[lg(1/x(u))+lg(1/y(v))]
       =H_X+H_Y.

Tato rovnost platí i s +∞. Pokud z(u,v)>0, obě marginály
jsou kladné, tedy z≪w a I=D(z||w) je definováno v [0,∞].
Pro konečné H_X+H_Y už řetězové pravidlo a konkávnost
dokázaly H_Z<∞. Každý tištěný krok je pak oprávněný:

    I=Σz lg z−Σz(lg x+lg y)
     =−H_Z+Σ_u x(u)lg(1/x(u))+Σ_v y(v)lg(1/y(v))
     =H_X+H_Y−H_Z=H_W−H_Z.

Nezápornost I dává požadovanou nerovnost pro společnou
entropii. Rovnost v konečném případě nastává podle (b)
právě z=w, tj. při nezávislosti.

U spočetných zákonů může být H_W−H_Z tvar ∞−∞.
Takový rozdíl se nevyhodnocuje. Rozsah tištěné rozdílové
identity jsou definované rozdíly, zejména konečné entropie;
nezáporná forma I+H_Z=H_X+H_Y platí rozšířeně.
Je-li H_Z<∞, obě marginály jsou konečné řetězovým pravidlem
a předchozí výpočet platí. Je-li H_Z=∞, podmíněná nerovnost
dává H_X+H_Y=∞ a sčítací forma je pravdivá, ale nelze
odčítat. I je stále jednoznačné z definice D.
To je explicitní omezení algebraického zápisu; není tu
protipříklad mezi dvěma definovanými hodnotami.

Také I+H(X|Y)=H_X platí rozšířeně. Na společném zákoně

    lg(1/x(X))=lg[z(X,Y)/(x(X)y(Y))]+lg[1/x_Y(X)].

Druhý člen je nezáporný, záporná část prvního integrovatelná
stejnou mezí jako u D. Očekávání součtu je tedy oprávněné
i rozšířeně. Je-li H_X konečné, lze odečíst I a získat
první tištěnou definici ve (f). Je-li H_Y konečné, lze
z řetězového pravidla získat H(X|Y)=H_(X,Y)−H_Y, včetně
nekonečného H_(X,Y). V ostatních případech se používá
nezáporný průměr, uvedený v zadání jako třetí forma.

## (f) Každý tištěný krok a obecné conditioning reduces entropy

Pro konečné entropie podmíníme identitu z (e) na každé
kladné Y-vlákno a sečteme. Vznikne přesně

    0≤I_(X,Z)|Y=H(X|Y)+H(Z|Y)−H((X,Z)|Y).

Řetězové pravidlo dává H(Z|Y)=H_(Y,Z)−H_Y a
H((X,Z)|Y)=H_(X,Y,Z)−H_Y. Obě H_Y se zruší a
pravá strana je H(X|Y)−[H_(X,Y,Z)−H_(Y,Z)]
=H(X|Y)−H(X|(Y,Z)). Tím jsou doloženy všechny tištěné
mezikroky v jejich konečné algebraické doméně.

Pro libovolné spočetné zákony na každém kladném Y-vlákně
vyjádříme podmíněný zákon X jako směs zákonů X podmíněných
navíc hodnotou Z. Dokázaná konkávnost dává
H(X|Y=v)≥Σ_w Pr(Z=w|Y=v)H(X|Y=v,Z=w).
Vynásobením y(v) a sečtením nezáporných členů dostaneme

    H(X|(Y,Z))≤H(X|Y)

bez ∞−∞. Nulové dvojice(v,w) se vynechávají. Jsou-li
obě strany nekonečné, jde o platné ∞≤∞; je-li pravá
konečná, levá je automaticky konečná. Tím jsou řešeny
všechny dříve otevřené možnosti P121 v rozsahu úlohy121.

## Přesný konečný rozsah

Celá121, všechny části(a)–(f), každý tištěný mezikrok,
interpretace, nulový a nekonečný okraj jsou posouzeny.
F006/F008 zůstávají jedinými nálezy; potvrzuje je také
nová kontrola všech šesti vrstev errat a tří TeX zdrojů.
E135 je známá změna bez karty/mapy. Žádná bibliografická
výjimka: potřebný vnitřní odkaz byl zobrazen; historická
bibliografie následující123 se zde neuzavírá.

Algoritmus kromě čtyř pevných logaritmických řad není
součástí121. File44 zůstává partial pro122; file410 partial
pro122–124. Starý společný P121 se zachovává jako partial
pro neukončený úplný rozbor122, nikoli jako uzavření121
na základě někdejších numerických kontrol.

