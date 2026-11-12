# MPR 4–5: všechny nerovnosti a příklad spolehlivosti

D095–D096, kontrola 6. listopadu 2026. Původní sazba file24–25 byla
zobrazena jako `images/sequential/file-024.png` a `file-025.png`.
Každý číslovaný i nečíslovaný matematický výrok má níže argument.
Bibliografické výjimky a rozsah převzetí starých důkazů jsou na konci.
V této poznámce EX² znamená E(X²); čtverec střední hodnoty píšeme (EX)².

## D095 — str. 4, (15)–(22)

**(15), (17), Markov.** Pro každé ω platí
f(X(ω))≥s[X(ω)∈S], protože f≥s na S a f≥0 mimo S. Násobení
nezápornou vahou pω a součet dává (17), včetně explicitního nulového
příspěvku mimo S. Dělení kladným s dá (15). Prázdné S, nulová hmotnost
S a nulové Ef(X) jsou dovoleny; v posledním případě P(X∈S)=0.
Ve spočetném prostoru jsou všechny podmnožiny událostmi; existence
Ef(X) znamená dříve vyhlášenou konečnost očekávání. Pokud dovolíme
rozšířenou hodnotu +∞, zůstává nerovnost pravdivá, ale je triviální.
Žádný nekonvergentní rozdíl se nepoužívá.

**(16), (18) a exponenciála.** Pro f(x)=|x|, S={x:|x|≥m}, s=m>0
je (16) přímé dosazení. Pro reálné X s konečným druhým momentem
vezměme f(x)=(x−EX)², S={x:|x−EX|≥r} a s=r², r>0. Pak je Ef(X)
přesně var(X), což dává (18). Omezení r>0 je doména předchozího
kladného prahu, nikoli nové tvrzení pro nulový jmenovatel. Je-li rozptyl
nulový, X=EX skoro jistě: nezáporný součet čtverců s nulovou hodnotou
má každý člen kladné hmotnosti nulový. Odhad je tedy správně0.
Pro reálné a je e^(ax)>0; při existenci momentu lze užít (15), např.
pro a>0 na horní ocas s=e^(at). Pro a<0 jde stejným postupem o dolní
ocas; pro a=0 je funkce konstantní a mez pouze triviální. Slovo „useful“
není další univerzální číselné tvrzení.

Odkaz do §1.2.10 souhlasí s originálem sv.1 str.98: je tam stejný
argument přes nezáporné čtverce a pravděpodobnost ocasu. Tím se
neuzavírá celý tamní rozbor Algorithm M.

**(19), konkávnost a kritérium druhé derivace.** (19) je definice
konvexity; −f konvexní znamená opačnou nerovnost pro f. Pro reálné
dvakrát diferencovatelné f na intervalu I z (19) plyne monotónnost
sečnových směrnic: pro x<t<y je

```
(f(t)−f(x))/(t−x) ≤ (f(y)−f(x))/(y−x)
                ≤ (f(y)−f(t))/(y−t).
```

Limity t k endpointům vnitřního úseku dávají neklesající f′; jeho
existující derivace f″ je proto nezáporná. Obráceně f″≥0 dává podle
věty o střední hodnotě neklesající f′. Pro x<t<y leží podle téže věty
levá sečnová směrnice pod pravou; úpravou dostaneme
f(t)≤((y−t)f(x)+(t−x)f(y))/(y−x), tedy (19).
Případy x=y, p=0 nebo q=0 jsou rovnosti. U uzavřených konců je
potřeba předpokládaná diferencovatelnost/její spojité jednostranné
rozšíření; pouze znalost f″ v otevřeném vnitřku by neomezovala libovolně
přepsanou koncovou hodnotu. Tisk říká, že f má druhou derivaci na I,
nikoli jen na nepojmenované menší množině.

**Všech pět rodin konvexních příkladů.** Pro reálné a máme
(e^(ax))″=a²e^(ax)≥0, včetně a=0. Pro celé n≥1 je
(x^(2n))″=2n(2n−1)x^(2n−2)≥0; n=0 znamená konstantu1 a řeší se
zvlášť, aby se v x=0 nezaváděl umělý zápis 0·x^−2. Pro libovolné
celé n a x>0 je (x^n)″=n(n−1)x^(n−2)≥0, protože celé n je buď
≤0, nebo ≥1; n=0,1 mají druhou derivaci0. Zvláště (1/x)″=2/x³.
Dále (ln(1/x))″=1/x²>0 a (x ln x)″=1/x>0. Také
(ln x)″=−1/x²<0 potvrzuje následnou konkávnost logaritmu.

**(20), úplný důkaz Jensenovy nerovnosti.** Předpokládáme integrabilní
reálné X s hodnotami v I a existující Ef(X), jak vyžaduje zdejší
konvence pro očekávání. Pro konečné váhy p1,…,pn≥0 se součtem1
se dokazuje

```
f(Σj pj xj) ≤ Σj pj f(xj)
```

indukcí. Pro n=1 je rovnost. Když pn=1, ostatní váhy jsou nula a jsme
v témže případě. Jinak q=1−pn>0, y=Σj<n pj xj/q∈I;
nejprve (19) pro qy+pn xn a pak indukce na y dají požadovaný výsledek.
Nulové váhy lze vynechat. To přesně doplňuje indukční krok krátkého
tištěného řešení MPR42, jehož podmínka na str.16 je stejná jako (20).

Pro spočetný obraz X vynechme hodnoty nulové hmotnosti a označme
Sn=Σj≤n pj>0, μn=Σj≤n pj xj/Sn, νn=Σj≤n pj f(xj)/Sn.
Konečná nerovnost dává f(μn)≤νn. Absolutní konvergence obou
očekávání a Sn→1 zaručují μn→μ=EX, νn→Ef(X). Je třeba zdůvodnit
f(μn)→f(μ), nikoli jen formálně „vzít limitu“.

Střední hodnota μ patří do I: leží mezi krajními mezemi hodnot X;
je-li konečný kraj a vynechaný, pak X−a>0 skoro jistě, takže jeho
očekávání je kladné a μ>a (analogicky na pravém kraji). Je-li μ
ve vnitřku I, konvexita zaručuje spojitost tam. Konkrétně zvolme
c<μ<d v I a menší okolí μ uvnitř (c,d). Výše odvozené nerovnosti
pro sečnové směrnice je omezí dvěma konečnými krajními směrnicemi,
takže |f(t)−f(μ)|≤K|t−μ| pro t v tomto menším okolí. Tím je limita
oprávněná. Pokud μ je zahrnutým levým či pravým krajem I, nezápornost
X−μ či μ−X a nulové očekávání vynutí X=μ skoro jistě; Jensen je
pak rovnost bez požadavku spojitosti f na konci. Singleton I je stejný
případ. Tento argument pokrývá i konvexní funkce s koncovým skokem,
které nemusí být na kraji spojité.

**Tři důsledky a dvoubodový případ.** Pro X>0 skoro jistě a konečné
μ=EX máme μ>0. Použití (20) na 1/x, −ln x a x ln x dává postupně
1/μ≤E(1/X), ln μ≥E ln X a μ ln μ≤E(X ln X), kdykoli jsou uvedená
očekávání definována. Kladnost X sama nezaručuje jejich konečnost;
nevynecháváme obecnou podmínku z (7). Pro rozdělení s hodnotami x,y
a vahami p,q=1−p jsou EX=px+qy a Ef(X)=pf(x)+qf(y), takže (20)
je přesně (19), včetně p=0,1 a x=y. Historická fasciklová oprava
doplnila q=1−p; místní 4B tuto formulaci již obsahuje.

**(21) a doména (22).** Nezáporné celočíselné X splňuje
[X>0]≤X bodově. Součet očekávání dává (21); rovněž tisknuté řady
p1+p2+… a p1+2p2+… jsou přesně obě strany. Rozdíl je nezáporný
součet Σk≥2(k−1)pk. V (22) je potřeba 0<EX²<∞, aby byl podíl
definován. Strana5 výslovně přechází k nezápornému X, které není
jistě nulové. Při EX²=0 je X=0 skoro jistě a pravděpodobnost P(X>0)
je přímo0; nepočítá se podíl0/0. Důkaz a tento oddělený okraj jsou níže.

## D096 — str. 5, (23)–(25)

**Každý mezikrok (23).** Nechť X≥0, q=P(X>0)>0 a EX²<∞.
Při konečném druhém momentu je EX konečné, protože 2|X|≤1+X².
První řádek (23) je rozdělení prostoru na X>0 a X=0. Na druhé
události je X²=0, pokud má kladnou pravděpodobnost. Pokud je její
pravděpodobnost0, autorova podmíněná střední hodnota může být EX²,
ale součin s0 je stále0. Takže přechod k druhému řádku je platný
i pro q=1. V podmíněném prostoru X>0 platí
E(X²|X>0)≥E(X|X>0)², buď podle Jensen pro x², nebo z nezápornosti
E((X−E(X|X>0))²|X>0). Nakonec EX=q E(X|X>0), a proto

```
EX² ≥ q (EX/q)² = (EX)²/q.
```

Dělení kladným EX² dává (22). To nevyužívá celočíselnost, takže
zobecnění na nezáporné reálné X je dokázáno. Číselná řada p1+4p2+9p3+…
na prvním řádku str.5 je přesně EX² v původním celočíselném případě.
Jestliže q=0, X=0 skoro jistě a případ už byl vyřešen přímo. Označení
„not always zero“ zde čteme pravděpodobnostně; hodnoty na nulových
atomech nerozhodují o žádném momentu.

**Rozšíření na záporná X s EX≥0.** Zaveďme Y=max(0,X). Bodově
Y≥X a Y²≤X², takže EY≥EX≥0 a EY²≤EX². Pokud EY²>0, již
dokázaná mez dává

```
P(X>0)=P(Y>0) ≥ (EY)²/EY² ≥ (EX)²/EX².
```

Poslední srovnání smí umocnit EY≥EX právě díky oběma nezáporným
stranám. Pokud EY²=0, X≤0 skoro jistě a EX≥0 vynutí X=0 skoro
jistě; výsledek se opět řeší přímo. Pro EX=0, EX²>0 je tvrzená dolní
mez prostě0. Toto jsou přesně předpoklady a závěr MPR47; MPR46
obsahuje uvedenou podmíněnou kvadratickou nerovnost. Odkaz MPR118
skutečně míří na Paleyho–Zygmundovu variantu, zadání str.24;
MPR54 skutečně počítá trojúhelníky náhodného grafu, zadání str.16.
Tyto odkazy neuzavírají celé úlohy ani jejich tištěné odpovědi.

**(24), převzatý důkaz s přesně doplněnými nulami.** Převzatý P050,
`GENERAL_PROBABILITY_NOTES.md`, oddíl „50: podmíněná mez a metoda
druhého momentu“, již obsahuje správný argument. Výsledek
`results/ross.json` (6642 nenulových tabulek a6 nulových případů)
je zachován; žádná z těchto enumerací se nespouštěla znovu. Zde
rozepisujeme jeho vztah ke každému tvrzení hlavního textu.

Nechť X=Σj=1..m Xj pro binární Xj, aj=EXj, μ=EX=Σj aj.
Definujme Uj=Xj/X na X>0, jinak0. Bodově Σj Uj=[X>0]; žádné
0/0 ve větvi X=0 nedefinujeme. Pro aj>0 je

```
EUj = aj E(1/X | Xj=1)
    ≥ aj / E(X | Xj=1),
```

protože X≥1 na tomto podmínění a 1/x je konvexní. Označme jeho
podmíněnou střední hodnotu tj. Pak 1≤tj≤m. Jestliže aj=0, je Xj=0
skoro jistě a EUj=0; při μ>0 dává původní nulová konvence tj=μ>0,
takže i vytištěný člen aj/tj je0. Sečtení dává (24) bez nezávislosti
Xj. Pokud μ=0, všechny Xj jsou0 skoro jistě a P(X>0)=0 přímo;
v této deterministické větvi se žádný vytištěný podíl nevyhodnocuje.
To je stejný triviální okraj jako u druhého momentu, nikoli další
kandidát na erratum.

**Proč je Rossova mez alespoň druhý moment.** Pro každý aj>0
je aj tj=E(XXj); pro aj=0 jsou obě strany0. Sečtením
Σj aj tj=E(XΣjXj)=EX². Pro μ>0 použijme Jensen na 1/t s vahami
aj/μ po vynechání nulových vah:

```
Σj aj/tj = μ Σj (aj/μ)/tj
          ≥ μ / Σj (aj/μ)tj = μ²/EX².
```

Všechny proměnné jsou omezené m, takže integrabilita, výměny součtů
i nenulové jmenovatele v této větvi jsou odůvodněné. Výrok „often
easier to compute“ je praktické srovnání, ne univerzální nákladová mez.

**Význam spolehlivostního polynomu a BDD odkaz.** Pro nezávislé bity
Yj s P(Yj=1)=pj je pravděpodobnost každého y rovna
∏j:yj=1 pj ∏j:yj=0(1−pj). Součet těchto výrazů přes f(y)=1 je
multilineární polynom F(p1,…,pn), souhlasící s f na nulajedničkových
vrcholech. Proto Ef(Y)=P(f(Y)=1)=F(p). Zápis f(p) v knize znamená
toto multilineární pokračování, nikoli aplikaci logického OR na
neceločíselné pravděpodobnosti. Odkaz do4A §7.1.4 byl porovnán
s originály str.206 a211, `vol4a-ref206.png`, `vol4a-ref211.png`.

Konkrétní algoritmický důvod přesného výpočtu je následující. Na koncích
uspořádaného BDD jsou hodnoty R0=0,R1=1; na uzlu proměnné j platí
R=(1−pj)RLO+pj RHI podle úplné pravděpodobnosti a nezávislosti dosud
nečtených bitů. Zpracování zdola nahoru drží invariant, že každému
zpracovanému uzlu je přiřazena správná pravděpodobnost jeho podfunkce.
Obě hrany míří do vyšších indexů proměnných, tedy graf je acyklický;
po konečném počtu uzlů se dosáhne kořene. Každý uzel potřebuje
konstantně aritmetických operací a jednu uloženou hodnotu: O(N)
operací a O(N) paměti pro N uzlů, nikoli tvrzení o konstantní bitové
ceně racionální aritmetiky. Přeskočené proměnné nepřidávají faktor,
protože jejich dvě pravděpodobnosti se sečtou na1. Pro p=0,1 rekurence
volí příslušnou větev správně. Poznámka o nutnosti aproximací u složitých
f je praktické omezení dostupných prostředků, nikoli matematická
nemožnost konečné úplné enumerace.

**Všechny implicanty a všechny jmenovatele (25).** Tři množiny
požadovaných jedniček jsou A={1,2,3}, B={2,3,4}, C={4,5}.
Žádná neobsahuje jinou, takže každá je minimální splňující množina.
Každá splňující množina obsahuje alespoň jednu z nich; tím jde přesně
o všechny tři prime implicants. Funkce je monotónní, protože přidání
jedniček zachovává splněnou konjunkci. Pro X1=Y1Y2Y3,
X2=Y2Y3Y4, X3=Y4Y5 máme bodově X>0 právě tehdy, když f(Y)=1.
Nezávislost dává čitatele a1=p1p2p3,a2=p2p3p4,a3=p4p5.

Při kladné pravděpodobnosti podmínění jsou podmíněné příspěvky:

| podmínění | EX1 | EX2 | EX3 | součet |
|---|---:|---:|---:|---:|
| X1=1 |1|p4|p4p5|1+p4+p4p5|
| X2=1 |p1|1|p5|p1+1+p5|
| X3=1 |p1p2p3|p2p3|1|p1p2p3+p2p3+1|

Každý zbytek obsahuje právě nefixované nezávislé bity. Dosazením do
(24) vzniká přesně (25). Když má jedna podmiňovací událost nulovou
pravděpodobnost, tabulka už netvrdí její podmíněnou střední hodnotu
podle autorovy konvence; příslušný čitatel je ale0. Všechny zobrazené
jmenovatele v (25) jsou ≥1, takže člen je0 a konečný vzorec zůstává
platný pro všechna pj∈[0,1], včetně úplně nulového systému.

**Skutečná pravděpodobnost a tři čísla.** Inkluze–exkluze dává

```
P(A∪B∪C)=P(A)+P(B)+P(C)−P(AB)−P(AC)−P(BC)+P(ABC).
```

Zde AC=ABC={Y1=…=Y5=1}, takže tyto dva členy se zruší. Zbývá
p1p2p3+p2p3p4+p4p5−p1p2p3p4−p2p3p4p5, přesně tisk.
Pro všechna pj=9/10 platí

```
EX = 567/250,
EX² = EX + 2(E(X1X2)+E(X1X3)+E(X2X3)) = 303669/50000,
(EX)²/EX² = 15876/18745 = 0.8469458522…,
Rossova mez = 1634490981/1926593200 = 0.8483840704…,
P(f=1) = 4779/5000 = 0.9558.
```

Všechny tři zaokrouhlené hodnoty knihy souhlasí. Nezávislý přesný součet
32 pěti-bitových výsledků je v `results/sequential/mpr-005-reliability.json`;
jde o jediný nový drobný výpočet tohoto bloku, spuštěný nice15, nikoli
opakování starého Rossova testu nebo census.

**FKG a konkrétní slibovaná korelace.** Převzatá část P059 v
`GENERAL_PROBABILITY_NOTES.md`, „59 a61: four functions theorem aFKG“,
dokazuje potřebnou konečnou FKG nerovnost včetně nulových vah.
Její algebraický vstup je úplný: ze čtyř nerovností aibj≤cmax(i,j)dmin(i,j)
pro i,j∈{0,1} plyne smíšená nerovnost, protože

```
c1d0(c0d1+c1d0−a0b1−a1b0)
 =(c1d0−a0b1)(c1d0−a1b0)+(c0c1d0d1−a0a1b0b1) ≥ 0.
```

Pokud c1d0=0, a0b1=a1b0=0 přímo. Zbývající dva členy dávají
(a0+a1)(b0+b1)≤(c0+c1)(d0+d1). Indukce podle počtu bitů seskupí
každou z funkcí podle posledního bitu. Čtyři indukční nerovnosti pro
součty skupin jsou právě tyto čtyři dvoubodové předpoklady; tím platí
four-functions pro každou konečnou Booleovu mřížku.

Pro nezáporné rostoucí f,g a log-supermodulární váhy μ zvolíme
α=fμ,β=gμ,γ=fgμ,δ=μ. Monotónnost i váhová podmínka dávají
α(S)β(T)≤γ(S∪T)δ(S∩T), tedy E(fg)≥Ef·Eg. Obecné konečné reálné
f,g se posunou o svá minima; kovariance se posunem nemění.
Součinové Bernoulliho váhy mají váhovou podmínku s rovností:
pro každý prvek se na obou stranách vyskytuje stejný počet faktorů
pj a1−pj, i když některý je0. Žádné dělení nulovou vahou se neprovádí.

MPR62 na str.18 volí f=[graf souvislý] a g=[graf4-obarvitelný].
Přidání hran zachovává souvislost, takže f roste; odebrání hran zachovává
dané4-obarvení, takže g klesá a1−g roste. FKG pro f,1−g tudíž dává
covar(f,g)≤0, přesně slibovaný příklad korelace. Rovnost je dovolena,
např. pokud je g konstantní. Převzetí starého důkazu nepotřebuje
opakování jeho307252 konečných kovariančních kontrol. Tímto blokem
se neuzavírají všechny podčásti úlohy61 ani celá vzdálená stránka18.

## Známé opravy, bibliografie a rozsah

E115 eviduje zveřejněnou opravu Markovova stránkového rozsahu
707–716→707–714 (13.3.2026) a starší fasciklové doplnění q=1−p
(26.7.2021), které již v místním4B je. Původní `all4b-03.png` a TeX
ověřují existenci první opravy; samotný Markovův článek se zde
neověřoval. Obě položky jsou známé změny, žádný nový nález ani karta.
Šest vrstev: `results/sequential/mpr-004-005-errata.json`.

Přesná historická tvrzení a bibliografie Markov1907, Bienaymé/Chebyshev,
Jensen1906 a Ross1994,185–190 se výslovně vynechávají. Matematické
věty jsou dokázány výše, takže tato výjimka nevynechává jejich důkaz.
Odkaz na Jensenovu nápovědu6.2.2–36 byl vizuálně potvrzen na původní
str.458 sv.3 (`vol3-ref458.png`), bez převzetí celé úlohy o entropii.
Odkazy MPR42,46,47,50,54,61,62,118 byly porovnány se zadáním;
jejich úplné odpovědi a další podčásti budou mít vlastní sekvenční rozbor.
Na str.4–5 nejsou další obrázky či tabulky. Přehled podmíněných příspěvků
výše je naše pomocná tabulka, nikoli nezkontrolovaný převzatý obrázek.

File24–25 jsou reviewed v tomto přesně vymezeném rozsahu.
