# §4.5.2: dávkování38, Penk39 a Brent–Kung40

Původní zadání355–356 a odpovědi645–646 byly vizuálně přečteny.
Čtyři vrstvy errat zahrnuty. Níže jsou obecné důkazy a přesná
realizace náčrtu38; historické rychlostní srovnání není přeměřeno.
C0128 je drobná záměna logaritmu s jeho zaokrouhlením v poznámce40.

## 38: jak dávkovat kroky pomocí krajních slov

Slovo bude obsahovat ell bitů, tedy nezápornou velikost menší než
W=2^ell; znaménko koeficientu evidujeme zvlášť. Po odstranění
společných mocnin2 mají kladné vstupy U,V alespoň jeden lichý
operand. Při simulaci vedeme celočíselnou matici A tak, že

```text
A (U,V)^T = 2^s (u,v)^T,                                (1)
```

kde s je počet simulovaných jednotlivých posunů doprava a
(u,v) aktuální operandy; horní T převádí řádkový vektor na
sloupcový. Začínáme jednotkovou maticí a s=0.
Při půlení u ponecháme první řádek A a zdvojnásobíme druhý;
při půlení v naopak. Zvětšení s o1 potom zachová(1).
To je význam známé opravy2013: půlí se sudý operand.

Jsou-li oba operandy liché, odečteme menší od většího a hned
provedeme jeden posun vzniklého sudého rozdílu. Například při
u>v, s řádky A1,A2, nahradíme řádky výrazem A1-A2,2A2
a zvětšíme s. Řádky mají stále tvar (a,-b),(-c,d), kde
a,d>0 a b,c>=0. Po každém takovém atomickém kroku platí
det(A)=2^s a všechny absolutní koeficienty jsou nejvýše2^s:
odečtení se znaménky nejvýše zdvojnásobí dosavadní mez,
stejně jako vynásobení druhého řádku dvěma.

Potřebná rozhodnutí lze udělat z krajních slov. Nízká slova
U mod W,V mod W určují paritu každého aktuálního operandu,
dokud s<ell: k výpočtu `(A1*(U,V)^T)/2^s mod2` stačí vstupy
modulo2^(s+1). Pro znaménko rozdílu vezmeme společnou škálu
T=2^q a vysoká slova h=floor(U/T),j=floor(V/T), obě<W.
Pokud A1-A2=(r,t), pak

```text
(rU+tV)/T leží mezi
r h+t j+min(r,0)+min(t,0)
a r h+t j+max(r,0)+max(t,0).                             (2)
```

Obě kladné meze bezpečně určují u>v, obě záporné u<v.
Při nejistém znaménku dávku ukončíme a aplikujeme její matici
na celé operandy. Prázdnou dávku nahradíme jedním přesným
krokem. Totéž uděláme, pokud by nový koeficient měl velikost
W nebo větší. Součty a součiny slov vyžadují příslušné místo
pro přenos, například dvouslovný dočasný výsledek.

Po s=ell je společná škála právěW, jak uvádí kniha. Obecně ale
musí být dovolené skončit dříve, obdobně jako v L. Například
W=8,U=463,V=65 vede při třech přímých posunech na(1,65)
a matici `[[1,-7],[0,8]]`. Koeficient8 už do daného slova
nepatří. Ani jiný druhý řádek s oběma velikostmi<8 nemůže
splnit aU+bV=8V: z gcd(463,65)=1 plyne65|a, tedy a=0,b=8.
Naší realizaci proto doplňuje explicitní mez pro zastavení.
Tento detail náčrtu nepovažujeme za nový potvrzený nález:
zadání žádá analogii s L, kde zastavení simulace patří k metodě.
Netvrdíme, že každá dávka má přesně ell kroků nebo že oba
operandy musí při každé dávce ostře klesnout.

Každý neprázdný blok zachovává gcd a snižuje součet kladných
operandů. Totéž platí pro náhradní přesný krok; při rovnosti
skončíme. To dokazuje správnost i ukončení hybridního algoritmu.
Ověřovací kód používá celé operandy pouze jako nezávislý
kontrolní výpočet pro tvrzení o simulaci; její rozhodnutí
závisí jen na hlavách, spodních slovech a malé matici.

U varianty40 se znaménko u-v vůbec netestuje: volba operace
závisí na počítadle c a spodních bitech. Proto lze stejnou
myšlenku použít bez vysokých slov. Pro rozhodnutí modulo4
je nutné zachovat dva dostupné spodní bity aktuálních operandů;
dávku skončíme dříve, než dojdou, a nulu ověříme při aplikaci
matice na celé operandy. Samotné tvrzení knihy, že vysoká
slova nejsou potřebná, je tak doloženo.

## 39: správnost Penkova rozšíření

Vstupy jsou kladné, jak upřesňuje erratum2014. Po Y1 píšeme
U=2^k u,V=2^k v, kde alespoň jedno z u,v je liché. Každá
trojice z=(z1,z2,z3) znamená lineární vztah

```text
z1*u+z2*v=z3.                                           (3)
```

Trojice x,y představují aktuální kladné operandy, t pomocný
rozdíl. Y2 vztah(3) splňuje pro (1,0,u),(v,1-u,v) a obě
možné inicializace t. Při Y3 se sudé koeficienty půlí.
Nejsou-li oba sudé, přičteme (v,-u,0) a půlíme. Přičtený
vektor má hodnotu0 v(3). Integrálnost plyne z parity(3):
pokud jsou u,v liché, mají t1,t2 stejnou paritu; pokud je
právě jeden sudý, koeficient druhého je sudý a přičtení
(v,-u) odstraní jedinou lichou paritu.

Y5 při kladném t3 pouze kopíruje t; při záporném používá
(v-t1,-u-t2,-t3), což je záporné t plus nulový vektor.
Y6 je rozdíl x-y, případně opět opravený nulovým vektorem.
Třetí souřadnice tak přesně sledují původní B. Při ukončení
vracíme (x1,x2,2^k x3), takže x1*U+x2*V=gcd(U,V).

Zbývají meze koeficientů, které potřebují errata1998:

```text
0<=x1,y1,t1<=v,  -u<=x2,y2,t2<=0,
0<x3<=u,        0<y3<=v.                               (4)
```

Inicializace je splňuje. Půlení a opravené půlení zobrazují
oba intervaly v(4) do sebe; záporné Y5 je jejich zrcadlení.
Kladné třetí souřadnice se po odečtení a půlení nezvětšují.

V Y6 musí být podmínka t1<=0, nikoli původní t1<0. Protože
x3,y3>0 a druhé koeficienty jsou nekladné, jsou x1,y1>0.
Po případné opravě tedy 1<=t1<=v. Máme současně
1-v<=t3=x3-y3<=u-1. Rovnice(3) potom dává

```text
-u-1 < (t3-t1*u)/v < 0.
```

Výraz je celé t2, tedy -u<=t2<=-1, jak potřebujeme.
Původní ostrá podmínka selhává už na u=3,v=1: Y6 vytvoří
(0,2,2), což porušuje deklarovanou mez t2<=0.
Jde o známou opravu, nikoli nový nález; lineární vztah sám
zůstává i v původním kroku platný.

Je-li v po Y1 liché a t3 sudé, rovnice(3) modulo2 ukazuje,
že oba koeficienty jsou sudé právě tehdy, když t1 je sudé.
Proto lze t2 a analogické druhé koeficienty při výpočtu
vynechat; případný výsledný druhý koeficient dopočteme z(3).
Pro liché u platí symetrické kritérium s t2. Odkaz na Y1,
nikoli Y2, je známá oprava2006.

## 40: invariant a počet kroků bez testování velikosti

Nechť M=max(|u0|,|v0|)>=1 pro počáteční vstupy, m=lg M,
kde lg je logaritmus o základu2.
První vstup je lichý, druhý může být i0 nebo záporný.
s je počet půlení v v K3; c je pomocné počítadlo algoritmu.
Průběžně platí

```text
|u| <= 2^(m-(s-c)/2),    |v| <= 2^(m-(s+c)/2).           (5)
```

Na začátku s=c=0. Půlení v zvětší s,c o1, tedy nezmění
první mez a rozpůlí druhou. Prohození operandů a změna
c na-c prohodí i obě meze. Před K5 už c<=0, takže první
mez není větší než druhá; náhrada v výrazem (u+v)/2 nebo
(u-v)/2 proto druhou mez nepřekročí. Znaménka operandů
nevadí, protože používáme absolutní hodnoty a trojúhelníkovou
nerovnost. Ze dvou možností je právě jedna sudá, neboť u,v
jsou v tomto místě liché. Zachování gcd plyne z lichosti
prvního operandu stejně jako v B.

Jsou-li oba operandy nenulové, obě pravé strany(5) jsou
alespoň1. Z toho s+|c|<=2m. Při v=0 je c<=0, případně
jsme skončili hned na počátku; opět z |u|>=1 plyne s<=2m.
Kromě první a poslední návštěvy K2 nastane alespoň jedno
půlení v K3, protože K5 vždy vytvoří sudé v. Při t návštěvách
K2 proto t<=s+2<=2+2m. Tento argument také vylučuje nekonečný
běh: s by jinak neomezeně rostlo.

Původní [Brent–Kung1983](https://maths-people.anu.edu.au/~brent/pub/pub082.html),
§6 na152–154, byl přečten v sazbě. Jeho PM používá při rovnosti
počítadla prohození (>=0), zatímco Knuth používá >0; invariant
platí pro obě volby. Není tedy správné mechanicky přebírat
jednotlivé stopy nebo empirické počty mezi oběma variantami.

Pro u=1,v=3*2^k-1,k>=2 má knižní varianta skutečně s=2k,t=k+4.
První K5 dá3*2^(k-1). Po k-1 posunech a prohození je
(u,v,c)=(3,1,-(k-1)); K5 dává v=2. Následuje k-1 návratů
přes půlení2 na1 až k c=0, přičemž K5 obnovuje2. Další
posun vyvolá prohození na(1,3,-1), K5 opět vytvoří2, poslední
posun a K5 dají v=0. Sečtení dává uvedené počty. Zde je
pouze C0128: m není k+2, nýbrž k+lg(3-2^-k).

## Rekurzivní rodina v poznámce40

Definujme a0=3,a1=1,
`a_(j+1)=min(|3a_j-16a_(j-1)|,|5a_j-16a_(j-1)|)`.
Všechny členy jsou kladné liché. Dokážeme s=2j+2,t=2j+3
pro vstup(a_j,2a_(j-1)), j>=1. Případ(1,6) má s=4,t=5.

Píšeme a=a_j,p=a_(j-1),b=a_(j+1). Nový vstup(b,2a)
po prvním posunu a prohození dává (u,v,c)=(a,b,-1).
Je-li b=|3a-16p|, K5 dává v=2(a-4p); je-li b=|5a-16p|,
dává v=-2(a-4p). To platí nezávisle na znaménku výrazů
uvnitř absolutních hodnot. Protože a-4p je liché, další
K3 provede přesně jeden posun a c=0. Následující K5 v obou
případech dává2p. Tím jsme dosáhli přesně původního stavu
(a,2p,0), se dvěma dodatečnými posuny i návštěvami K2.
Indukce hotova; výběr minima je potřebný pro malé vstupy,
nikoli pro samotné počty.

Knižní tvrzení m~phi*j je výslovně empirické; phi=(1+sqrt5)/2.
Kontrola rekurze do j20000 dává m/j přibližně1.61832112
oproti phi~1.61803399, s kolísáním v kratších prefixech.
To je slučitelné s pozorováním, nikoli důkaz limity. Otázka,
zda může být t asymptoticky větší než2m/phi, tím vyřešena není.
Audit ji zachovává jako výzkumnou otázku.

## Prameny a reprodukovatelnost

[Bojanczyk–Brent1987](https://maths-people.anu.edu.au/~brent/pub/pub096.html),
233–235, byl přečten v sazbě: EPM udržuje celočíselnou matici
Bézoutových koeficientů a při liché paritě ji opravuje nulovým
vektorem před půlením. To potvrzuje věcnou souvislost odkazu39
i bibliografickou opravu2015. Zbytek článku ani celý návrh
hardwarových buněk nebyly nově auditovány.

Odkazy38 na Sorensona a Shallita–Sorensona jsou ověřeny
v primárních autorských/univerzitních záznamech; rozsah je
v `sources/gcd-variants-bibliography.json`. Výrok o čtyřnásobné
rychlosti na jednom počítači je historická experimentální
zpráva bez podkladů pro nové přeměření, nikoli obecná záruka.

`verify_gcd_variants.py` kontroluje po každém kroku přesné
lineární vztahy, intervaly i gcd. Relace48478, PID1153559,
limit600sekund, exit0. Penk65786 vstupů (všechny1..256 plus
250 větších); Brent–Kung8506 znaménkových vstupů,299 členů
první rodiny,103 plných běhů druhé a20000 jejích indukčních
prefixů; Gosper65856 vstupů s šířkami2,3,4,8bitů.
Všechny tři checkpointy prošly. Žádný z těchto běhů není
časovým benchmarkem implementací v historických článcích.
