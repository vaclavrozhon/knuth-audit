# §4.3.2: zbytky, převody a úlohy1–13

Dokončeno2.11.2026. Originály284–294 a630–632 vizuálně přečteny;
sekce má14 úloh a končí až na294. Tento blok uzavírá matematický text
284–291 a úlohy1–13. Historický kontext a násobení pomocí konvoluce14
mají samostatné pokračování. Níže jsou obecné důkazy; konečné kontroly
je doplňují a nejsou jejich náhradou.

## Konvence a věta o zbytcích

Modul m je kladné celé číslo. Zbytek `x mod m` je jediné celé číslo
z[0,m), jehož rozdíl od x je násobkem m; zápis `x≡y (mod m)` znamená,
že m dělí x-y. V reálné variantě úlohy2 se používá Knuthova definice
`x mod m=x-m*floor(x/m)`, tedy rozdíl je **celočíselný** násobek m.
Knuth navíc definuje `x mod 0=x` (§1.2.4,39); kongruence modulo0
proto znamená rovnost, což je podstatné pro krajní případy úlohy6.

V textu jsou moduly m_1,...,m_r po dvojicích nesoudělné, tedy
`gcd(m_i,m_j)=1` pro i!=j. Označme jejich součin M. Rovnost všech
zbytků čísel x,y je ekvivalentní dělitelnosti x-y každým m_j, tedy M.
V libovolném intervalu[a,a+M), kde a je celé číslo, je proto nejvýše
jedno řešení předepsaných zbytků. Na druhé straně je zde M celých čísel
a přesně M možných uspořádaných seznamů zbytků. Injektivní zobrazení
mezi stejně velkými konečnými množinami je surjektivní: řešení existuje.

Před tímto argumentem lze libovolné vstupní u_j nahradit `u_j mod m_j`.
Toto triviální znormalizování je v prvním tištěném důkazu implicitní;
při doslovném čtení jeho poslední rovnosti s nenormalizovanými u_j
by pravá strana mohla ležet mimo množinu zbytků. Samotná věta je
správná pro všechny celočíselné u_j. Nejde zde o nové tvrzení, že
arbitrární zbytek musí již ležet v[0,m_j).

Pro konstruktivní důkaz položme B_j=M/m_j a nechť phi(m_j) je počet
čísel1..m_j nesoudělných s m_j (Eulerova funkce; phi(1)=1).
`E_j=B_j^phi(m_j)` je1 modulo m_j a0 modulo každého jiného m_i.
Pro m_j=1 je požadavek modulo1 prázdný a vzorec zůstává správný.
Pak `a+(sum u_j E_j-a) mod M` splňuje jak kongruence, tak interval.
Alternativně stačí `E_j=B_j*(B_j^(-1) mod m_j)`, kde inverzi dává
rozšířený Eukleidův algoritmus. Vzorec(8) je matematicky platný,
ale pro výpočet není třeba rozkládat m_j a počítat phi(m_j).

Souřadnicové sčítání, odčítání a násobení(2)–(4) jsou platná díky
`(x op y) mod m=((x mod m) op (y mod m)) mod m`. Výsledek představuje
celé číslo v určeném intervalu délky M; bez meze na skutečný výsledek
zde může docházet k přetečení. Čas O(r) počítá jednoslovné operace
pro každý z předem vybraných modulů a nezahrnuje převody. Nejde
o tvrzení, že při pevném slově existuje libovolně mnoho nesoudělných
jednoslovných modulů; jejich maximální možný součin řeší úloha5.
Paralelnost jednotlivých souřadnic nevyvrací potřebu přenosů v dřívějším
klasickém algoritmu. Není to dolní mez pro všechny paralelní sčítačky.

**Úloha1:** inverses7^(-1) mod11=8,7^(-1) mod13=2,
11^(-1) mod13=6 dávají smíšené číslice1,7,6. Hodnota
`6*7*11+7*7+1=512` má předepsané zbytky1,6,5. Protože7*11*13=1001,
je v[0,1000) jediná. I tištěný výraz s mocninami6,10,12 dává512.

**Úloha2:** pro reálná u_j je nutnou podmínkou stejná zlomková část,
protože všechny moduly jsou celočíselné. Je také postačující:
odečteme společnou zlomkovou část f, vyřešíme celočíselný problém
v intervalu[ceil(a-f),ceil(a-f)+M), pak f přičteme. Dostaneme právě
jedno řešení v[a,a+M). Bez podmínky například moduly2,3 a požadavky
u≡0 (mod2), u≡1/2 (mod3) nemají ani reálné řešení.

## Zobecněná věta: úloha3

Nyní moduly nemusejí být nesoudělné. Píšeme
`M_j=lcm(m_1,...,m_j)`, `M_0=1`, kde lcm je nejmenší kladný společný
násobek. Nutná podmínka existence je

```
u_i ≡ u_j (mod gcd(m_i,m_j))  pro všechna i,j.             (G)
```

Předpokládejme, že s již řeší prvních j-1 kongruencí a0<=s<M_(j-1).
Hledáme `s+t*M_(j-1)` se zbytkem u_j. Položme
`d=gcd(M_(j-1),m_j)`, `h=m_j/d`. Podmínka(G) zaručuje d|(u_j-s):
Každý gcd(m_i,m_j) dělí tento rozdíl a jejich nejmenší společný násobek je d.
Tato identita plyne pro každý prvočíselný exponent z distributivity
minima přes maximum. Po dělení d je `M_(j-1)/d` nesoudělné s h, takže

```
t = ((u_j-s)/d)*(M_(j-1)/d)^(-1) mod h.
```

Existuje a je jednoznačné v[0,h). Nové s leží v[0,M_j) a zachovává
předchozí kongruence. To je obecný indukční důkaz i algoritmus;
pro h1 se volí t0. Pořadí všech modulů včetně opakovaných jedniček
nepůsobí problém. Přičtením násobku M_r se vybere obecný interval.

V tištěné formulaci se c_j volí tak, že
`c_j*M_(j-1)≡d (mod m_j)`. Po vydělení d je to přesně naše inverze,
takže tištěné `t=(c_j*(u_j-s))/d mod h` souhlasí.

Také početní důkaz na630 je úplný při indukci podle r: po zvolení
prvních r-1 zbytků musí poslední splnit kongruence modulo
`g_i=gcd(m_i,m_r)`. Jejich vzájemná kompatibilita plyne z(G), protože
gcd(g_i,g_j) dělí gcd(m_i,m_j). Indukční hypotéza dává
`m_r/lcm(g_1,...,g_(r-1)) = M_r/M_(r-1)` možností. Všech kompatibilních
seznamů je tedy M_r. Rozdíl dvou řešení je násobkem M_r, což současně
dokazuje jejich jednoznačnost. Selhání(G) nutně vylučuje řešení.

## Výběr modulů: úlohy4/5

Pro nesoudělné moduly je každé prvočíslo p zastoupeno v nejvýše jednom
modulu. Jestliže jsou moduly menší než100 a liché, exponent p v jejich
součinu nemůže překročit největší k, pro které p^k<100. Horní mez je
součin všech takových největších mocnin pro lichá prvočísla p<100.
Je dosažitelná volbou každé mocniny jako samostatného modulu.

Hladový výběr sestupně dává přesně tištěný seznam

```
99,97,95,91,89,83,79,73,71,67,61,59,53,47,43,41,37,31,29,23,17.
```

Po prvních čtyřech modulech jsou použita prvočísla3,5,7,11,13. Součin
dvou zbývajících prvočísel je již nejméně17^2>100, proto dále následují
jen prvočísla. Výběr je konečný, jedničky nepřidávají rozsah. Oproti
optimu chybějí činitelé3^2,5,7: optimální součin je **315krát větší**.
To dokazuje zápornou odpověď bez hledání všech rozkladů do modulů.

Dodatek2000 omezuje **zbytek**, nikoli hodnotu modulu, na8bitů.
Je proto přípustný i modul256, jehož zbytky jsou0..255. Maximem je
`lcm(1,...,256)`, dosažené mocninami2^8,3^5,5^3,...,251.
Přesný součin je v `results/modular-basic.json`; racionální porovnání
s mezemi1.665*10^109 a1.675*10^109 potvrzuje zaokrouhlení1.67*10^109.
Požadavek pevného počtu modulů je jiný optimalizační problém, který
zdejší úloha neukládá. Známá oprava1999 napravuje sazbu „p prime“.

## Mersennovy moduly a úloha6

Zde e>=1, B=2^e a m=B-1. Dovolíme oba zápisy nuly0 a m, tedy vstupy
x,y v[0,B). Při součtu s=x+y nejvyšší bit nese B≡1 (mod m), takže
`(s mod B)+[s>=B]` má správný zbytek. Výsledek nepřekročí B-1:
při přenosu s<=2B-2 dává spodní část nejvýše B-2. Analogicky
`((x-y) mod B)-[x<y]` leží v[0,B) a představuje x-y. Vzorec(12)
je také použitelný, jestliže dovolujeme nekanonický zápis nuly m.
U součinu se horní část `floor(xy/B)` přičte k dolní části touto
operací. To dokazuje(16)–(18), včetně nejmenšího případu e1.

Pro nezáporná e,f a f>0 pišme e=qf+r,0<=r<f. Protože2^f≡1 modulo
2^f-1, je `2^e-1≡2^r-1` a pravá strana je v kanonickém rozsahu.
To dokazuje(20). Pro f0 je obojí2^e-1 díky konvenci mod0. Eukleidův
algoritmus aplikovaný opakovaně na exponenty dává

```
gcd(2^e-1,2^f-1)=2^gcd(e,f)-1.                          (19)
```

Platí i pro e=f=0 při gcd(0,0)=0. Čísla jsou tedy nesoudělná právě
tehdy, když gcd(e,f)=1. Volba32,31,29,27,25 je po dvojicích nesoudělná
a přesné násobení ověřuje tištěnou dolní mez2^143 pro součin modulů.

V6(a), pro g>=2, zredukujeme exponenty do0..g-1. Odpovídající mocniny
jsou různé a jejich rozdíly mají absolutní hodnotu menší než2^g-1,
proto je jejich kongruence rovností. Obrácený směr plyne z2^g≡1.
Pro g1 jsou obě kongruence vždy pravdivé; pro g0 jsou obě ekvivalentní
e=f. Nulový modul tedy není protipříkladem k úloze.

V6(b) bereme kladného reprezentanta c inverze e modulo f. Je-li
f>=2 a `ce mod f=1`, pak d=e mod f>0. Geometrická identita dává

```
(1+2^d+...+2^((c-1)d))*(2^e-1)
 ≡ (1+2^d+...+2^((c-1)d))*(2^d-1)
 = 2^(cd)-1 ≡ 2^1-1 = 1 (mod 2^f-1).
```

Pro f1 je antecedent s operátorem mod roven1 nemožný. Pro f0 znamená
ce=1; s nezáporným e a kladným celočíselným c je e=c=1 a vzorec je1.
Konečný součet s c členy předpokládá c>=1; pro výpočet inverze lze
vždy zvolit tento reprezentant. Nezáporné exponenty v6(a) samy
nepřikazují počítat konečnou sumu se záporným počtem členů.

Pro převod celočíselného x do zbytků funguje Hornerovo schéma pro jeho
poziční zápis. Speciálně po blocích e bitů je B≡1, takže se bloky
sečtou operací(16). Rovnice(21)/(22) a analogie se zkouškou devítkou
jsou přímými důsledky tohoto kongruenčního vztahu.

## Garnerův převod a úlohy7–10

Znovu předpokládáme nesoudělné moduly. Označme
`P_j=m_1*...*m_j`, `P_0=1`. Smíšené číslice v_j jsou voleny
z[0,m_j), a představují číslo `S_r=sum_(j=1)^r v_j P_(j-1)`.
Konstanta c_ij je inverze m_i modulo m_j pro i<j.

Při j-tém kroku je nutné splnit
`P_(j-1)*v_j ≡ u_j-S_(j-1) (mod m_j)`.
Opakované odečítání již známých v_i a násobení c_ij ve(24) odstraňuje
postupně m_1,...,m_(j-1); po vynásobení P_(j-1) se vše teleskopicky
zkrátí na právě tuto rovnici. Nové číslo S_j zachová všechny předchozí
zbytky, protože přičtený člen je násobkem jejich modulů. Navíc
`0<=S_j<P_j`, indukcí z rozsahů číslic. To dokazuje(25)/(26) a8.
Současná aktualizace budoucích souřadnic po každém i používá nezměněný
pivot v_i a je jen jiné pořadí týchž výpočtů.

**7:** inverze P_(j-1) modulo m_j je součin c_1j...c_(j-1)j.
S_(j-1) se vyhodnotí Hornerovým schématem modulo m_j, pak se odečte
od u_j a vynásobí jedinou předpočtenou inverzí C_j. Pro j-tou číslici,
j>=2, má tato verze j-2 násobení v Hornerově schématu a závěrečné
násobení, tedy stejný počet j-1 jako ve(24). První číslice je přímo
v_1=u_1 mod m_1. U jednoslovných modulů je výhodné vzestupné uspořádání:
starší m_i a v_i se rovnou vejdou do m_j. Jinak by předpočtená tabulka
`m_i mod m_j` mohla zrušit úsporu paměti. Jedničkové moduly lze před
časovým porovnáním odstranit jako redundantní. Speciální moduly4.3.3B
mohou mít další výhody; jejich podrobná analýza je v té pozdější sekci.

**9:** pro zpětný převod platí
`u_j=(v_1+m_1*(v_2+...+m_(j-1)*v_j)) mod m_j`.
Vyšší členy již obsahují faktor m_j. Postup j=r,...,1 dovoluje
přepsat v_j výsledným u_j, protože dosud potřebné nižší číslice
zůstávají zachovány. Opačné pořadí obecně není bezpečné.

**10:** pro liché moduly definujme h_j=(m_j-1)/2 a vyvážený zbytek
`bal(x,m_j)=(x+h_j) mod m_j-h_j`, ležící v[-h_j,h_j]. Nahrazení
mod tímto operátorem ve(24) zachová kongruence. Výsledek splňuje

```
|S_r| <= sum h_j P_(j-1)
       = (1/2)*sum(P_j-P_(j-1)) = (M-1)/2.
```

Jde tedy o správného reprezentanta v symetrickém intervalu.
Pro s=x+y nebo x-y, kde x,y jsou vyvážené zbytky modulo liché m,
stačí `s-m*[s>(m-1)/2]+m*[s<-(m-1)/2]`. Součin se zredukuje
běžným vyváženým operátorem. Při porovnání rozhoduje první různá
číslice od nejvyšší: její váha P_(j-1) je větší než maximální možný
rozdíl nižší části P_(j-1)-1. To platí pro obyčejný i vyvážený zápis.
Záměnu názvů u/v v poslední větě na290 opravují errata2019.

## Věta S a limity porovnávání

Označme a=m_1 a M součin všech modulů. Předpoklad a<sqrt(M) znamená
M/a>a. Neprostá funkce g na zbytcích0..a-1 ztotožní dva různé zbytky.
Z CRT existuje dvojice celých čísel0<=u<v<M se stejnou hodnotou g
a stejnými ostatními zbytky. Vybereme takovou dvojici s nejmenším u.
Kdyby u>=a, mohli bychom od obou čísel odečíst a; příslušné hodnoty g
ani shodu ostatních zbytků to nezmění. Proto u<a<=L.

Pokud v>=L, je důkaz hotov. Jinak v<L, ale v-u je kladný násobek M/a,
tedy v>=M/a>a. Dvojice

```
U=v-a,  V=u+M-a
```

má0<=U<L<=V<M, stejné dvě hodnoty g (ve vyměněném pořadí) a opět
stejné ostatní zbytky, protože V-U=M-(v-u) je násobkem M/a.
To dokazuje i všechny rovnosti na hranicích L=a a L=M-a. Posunutý
interval dostaneme překladem a vhodně posunutou funkcí g na zbytcích.

Tato věta je **informační překážkou**: žádné předběžné ztotožnění
některých hodnot jedné souřadnice neumožní správně rozhodovat daný práh
pro všechny vstupy. Sama nedává kvadratickou časovou dolní mez pro
všechny algoritmy porovnávání ani nevylučuje rychlejší převod.

## Půlení, přetečení a automorfní čísla11–13

**11:** pro liché M je `(M+1)/2` inverzí2 modulo M. Jeho j-tý zbytek
je `(m_j+1)/2`, protože M-m_j je dělitelný2m_j. Je-li u sudé a
0<=u<M, pak u/2 leží ve stejném rozsahu a souřadnicové násobení touto
inverzí ho proto rekonstruuje přesně. Obecně lze takto dělit v,
pokud gcd(v,M)=1, je známa přesná dělitelnost a zamýšlený podíl leží
v reprezentačním intervalu. Pro záporný podíl se musí vybrat odpovídající
interval; kongruence sama neurčuje znaménko.

**12:** pro0<=u,v<M je součet buď u+v, nebo u+v-M. První hodnota je
nejméně u, druhá je menší než u (protože v<M). To dokazuje test.
Při lichém M a jednom přetečení se změní parita. Všechny váhy P_j
smíšeného zápisu jsou liché, takže parita reprezentovaného součtu je
parita součtu jeho číslic. Dodatečné bity u mod2,v mod2 proto dávají
právě test v hranaté závorce odpovědi. Vyžaduje smíšené číslice,
nikoli pouze jejich původní modulární zbytky.

**13:** n-místný zápis zde dovoluje úvodní nuly (např.0625). Pro
0<=x<10^n platí x^2≡x právě tehdy, když pro každé p=2,5 je x≡0
nebo1 modulo p^n. Čísla x a x-1 jsou nesoudělná, takže p^n musí
celé dělit právě jeden z těchto činitelů. CRT dává čtyři kombinace;
stejné volby0/0 a1/1 jsou triviální0 a1, zbývající dvě jsou x>1.
Jejich součet je10^n+1. Symboly E_1,E_2 z konstruktivního důkazu se
zde berou jako zbytky modulo10^n, nikoli jako libovolné velké mocniny.

Položme `T(x)=3x^2-2x^3`. Je-li x dělitelný p^n, je T dělitelný
p^(2n); je-li x-1 dělitelný p^n, pak
`T(x)-1=-(x-1)^2*(2x+1)` je dělitelný p^(2n). Navíc T≡x modulo10^n.
Zbytek T modulo10^(2n) je tedy správné netriviální prodloužení,
což dokazuje13(b). Pro13(c) použijeme totéž na a=cx:
`c'=3c^2-2c^3*x` splňuje `c'x^2=T(cx)≡1 (mod y^2)`.

Kompatibilní zbytky modulo10,10^2,... tvoří10-adické celé číslo.
Aplikace CRT na každé úrovni a kompatibilita s redukcí dávají bijekci
s párem kompatibilních2-adických a5-adických zbytků, zachovávající
sčítání i násobení. Dvě netriviální nekonečné automorfní posloupnosti
jsou proto právě dvojice(0,1),(1,0); jsou vzájemně1-x. Poznámka knihy
neříká, že by neexistovaly další triviální idempotenty0 a1.

## Kontroly a rozsah

`verify_modular_basic.py`, běh76675, exit0; všech pět bloků dokončeno:

- 247 trojic nesoudělných modulů,22471 úplných celočíselných vstupů,
 3667 vyvážených převodů;21952 seznamů obecných zbytků porovnáno
 s úplnou tabulkou skutečných čísel a1344 racionálních případů.
- 349520 jednoslovných operací s oběma nulami,80275 identit exponentů
 včetně nuly a1458 geometrických inverzí.
- Oba optimální součiny a přesný poměr315, bez heuristické optimalizace.
- 1698 možných ztotožněných párů zbytků a411312 prahů věty S,
 včetně201570 případů vyžadujících transformovanou dvojici.
- 110476 párů pro přetečení/vyvážené porovnání,220 půlení,
 automorfní čísla do32 míst, úplné malé obory do10^5 a13125
 zdvihů inverze čtverce. Orákula používají přímo celočíselné hodnoty,
 nikoli druhý běh téhož převodu.

Všechny čtyři vrstvy errat prohledány; původní strany17/38 v all2-prepre
 a7/14 v all2-pre přečteny. Nové úlohy nepřibyly;5 má dodatek o8bitech,
13 bibliografickou opravu a14 matematickou opravu, která se kontroluje
samostatně. Tento blok nepřidává potvrzený nález. Zbývá14 a kontext,
nikoli znovu provádět právě úspěšné kontroly1–13.
