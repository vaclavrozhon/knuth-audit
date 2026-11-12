# MPR92–94 — Doobova urna a každé použití nezávislosti

D190–D192, 7. listopadu 2026. Celá zadání p20/file40 a odpovědi
p384/file404 přímo zobrazeny; autorův PS p20/file26 a p40/file46
má stejné relevantní znění. Přebírané důkazy D098/D100/D101/D174
mají níže přesně vyznačený rozsah. Žádný matematický běh.

## 92: každý čas včetně přechodu přes m

V modelu(27) je X0=1 deterministická počáteční červená koule;
Xi pro i≥1 označuje barvu i-tého přidání. Po n přidáních jsou
R_n=1+Σi=1..n Xi, B_n=1+n−ΣXi a Z_n=R_n/(n+2).
Tyto identity a obě přechodové větve již doložil D098.

Fixujme celé m>0 a H_n=σ(X0,…,Xn). Proměnná Q=Xm je omezená,
tedy její Doobovy podmíněné průměry existují a jsou integrabilní.
D174 dokázal konečnou záměnnost všech kladných pozic: pravděpodobnost
slova délky l s a jedničkami a b nulami je a!b!/(l+1)!.
Při n<m můžeme v prvních m pozicích vyměnit pozice m a n+1;
prefix do n zůstane pevný. Sečtením přes ostatní koncové pozice
dostaneme rovnost společných pravděpodobností prefixu a Xm=1,
respektive prefixu a Xn+1=1. Každý prefix má kladnou pravděpodobnost,
a proto po dělení pravděpodobností prefixu

```
E(Xm|H_n)=E(Xn+1|H_n)=R_n/(n+2)=Z_n,   0≤n<m.
```

Druhá rovnost je přímo pravděpodobnost červeného tahu z daného
složení urny. Konstantní X0 nepatří mezi permutované tahy.
Pro n≥m je Xm již H_n-měřitelná, tedy E(Xm|H_n)=Xm. Celý výsledek:

```
Q_n = (1+X1+⋯+Xn)/(n+2)  pro 0≤n<m;
Q_n = Xm                  pro n≥m.
```

Zejména Q0=1/2. Q1=(1+X1)/3 pro m>1, ale Q1=X1 pro m=1.
Q2=(1+X1+X2)/4 pro m>2, zatímco Q2=Xm pro m=1 nebo2.
Tyto malé případy odlišují podmíněný průměr od nesprávného
pokračování Z_n i po odhalení cílového tahu.

Pro úplnost je martingalový přechod přesně ověřen ve třech režimech:
n<m−1 přebírá obě větve urnového martingalu D098;
n=m−1 dává E(Q_m|H_{m−1})=E(Xm|H_{m−1})=Z_{m−1}=Q_{m−1};
n≥m podmiňuje již známou Xm a nemění ji. K vlastní historii Q
se přejde věžovou identitou D098. Všechny hodnoty jsou v[0,1].
Tím je celý tištěný výpočet i okraj m=1 doložen.

## 93: neidentické nezávislé adresy a celý nový vzorec

Pro n=1,…,t předpokládáme p_nk≥0, Σk=1..m p_nk=1,
m≥1, a vzájemně nezávislé adresy X_n. Pravděpodobnost úplného
vektoru je Πn p_n,x_n. Q je počet prázdných přihrádek, tedy
Q=Σk Ik, kde Ik=Πn[X_n≠k]. Nezávislost souřadnic dává

```
E Ik = Πn=1..t(1−p_nk),
μ=E Q=Σk=1..m Πn=1..t(1−p_nk).
```

Nezávislost různých Ik se nepředpokládá ani nepoužívá. Při některém
p_nk=1 je příslušná pravděpodobnost prázdnosti0; pokud všechna
p_nk=0, je1. Pro t=0 je prázdný součin1 a Q=μ=m deterministické.
Pro m=1,t≥1 je Q=μ=0. Všechny součty jsou konečné.

D101 již dokázal, že změna jediné adresy mění Q nejvýše o1:
vyprázdnění původní přihrádky a zaplnění nové dávají rozdíl dvou
indikátorů. Zde explicitně doplníme všechny nové váhy.
Na kladně pravděpodobném prefixu u délky n−1 definujme

```
w(v)=Πj=n+1..t p_j,v_j,
g_u(x)=Σv w(v) Q(u,x,v),
Y_n(u,x)=g_u(x)−Σz=1..m p_nz g_u(z).
```

Součet w(v) je1, a pro n=t je v jediný prázdný vektor s vahou1.
Nezávislost zaručuje, že w(v) je správné podmíněné rozdělení
budoucnosti pro každý u i x. Proto je g_u(x)=E(Q|u,X_n=x)
na podporovaných x a Y_n je právě rozdíl Doobových průměrů.
Pro x mimo podporu můžeme stejný konečný vzorec použít jako
pomocnou funkci; při průměrování má taková souřadnice váhu0.
Na nulových prefixech se podmíněná verze může zvolit libovolně;
nic na nich nedělíme a výsledky platí skoro jistě.

Váhy zajišťují Σx p_nx Y_n(u,x)=0. Pro každé x,x′ také

```
|Y_n(u,x)−Y_n(u,x′)|
 = |Σv w(v)(Q(u,x,v)−Q(u,x′,v))|
 ≤ Σv w(v) =1.
```

To zahrnuje celou změnu z rovnoměrných průměrů v(40) na
neidentické distribuce. Každá podmíněná šířka je nejvýše pevná1;
tištěná(41) i navazující argument(42) tedy fungují beze změny.
Deterministická verze D100, nikoli chybná náhodná verze F160,
dává pro t≥1,x>0 oba ocasy

```
P(Q≥μ+x)≤exp(−2x²/t),   P(Q≤μ−x)≤exp(−2x²/t).
```

Pro f(t)≥1 dosadíme x=√(t ln f(t)). Při f(t)>1 je x>0,
při f(t)=1 stačí triviální mez1. Přesná náhrada(44) zní

```
P(Q≥Σk Πn(1−p_nk)+√(t ln f(t))) ≤1/f(t)²,
P(Q≤Σk Πn(1−p_nk)−√(t ln f(t))) ≤1/f(t)².
```

Pro rovnoměrné p_nk=1/m je μ=m(1−1/m)^t, čímž se vrací
původní(44). Pro t=0 je Q konstantní a kladné odchylkové ocasy
prázdné; výraz s dělením t se nepoužívá. Není třeba žádná
asymptotická podmínka na f pro konečné nerovnosti.

## 94: přesné koeficienty při závislosti

Doobova konstrukce D100/D101 vyžaduje pouze integrabilitu Q,
nikoli nezávislost. Q je zde omezená i při libovolném společném
rozdělení adres. Věžová identita a martingal proto zůstávají.
Nezávislost se použila ve dvou dalších místech: v součinovém
průměru E Ik a v možnosti porovnat dvě x se stejným rozdělením
suffixu. Druhé použití je hlavní obsah tištěné odpovědi94.

Fixujme kladný prefix u a na něm podmíněný společný zákon
p(x,v) adresy x=X_n a celého suffixu v. Prefix v dalších
pravděpodobnostech potlačíme; jde o lokální podmíněný model,
stejně jako při psaní Δ v(40). Pišme p_x=Σv p(x,v),
q_v=Σx p(x,v), a uvažujme p_x q_v>0. Přímé rozvinutí
Doobova rozdílu dává

```
Y_n(x)=Σv q_v [a(x,v) Q(u,x,v)−Σz b_z(v)Q(u,z,v)],
a(x,v)=p(x,v)/(p_x q_v),   b_z(v)=p(z,v)/q_v.
```

Součet b_z(v) je1. Aby závorka byla pro libovolnou funkci Q
váženým součtem rozdílů Q(u,x,v)−Q(u,z,v) se stejnými vahami
b_z(v) nezávislými na zvolené skutečné hodnotě x, musí její
koeficient u Q(u,x,v) souhlasit se součtem těchto vah.
I když se člen z=x odečítá sám, porovnání dává
a(x,v)−b_x(v)=Σz≠x b_z(v), tedy a(x,v)=Σz b_z(v)=1.
Právě to vyjadřuje tištěný podíl
P(X_n=x,X_future=v)/(P(X_n=x)P(X_future=v)) a součet vah.
Je to podmíněná nezávislost nynější adresy a budoucnosti při
daném prefixu. V součinovém modelu platí na každém prefixu.
Pokud p_x q_v=0, příslušný atom se vynechá; žádná rovnost
podílů na nulových jmenovatelích se netvrdí.

Při závislosti se při změně x může změnit i rozdělení všech
budoucích adres. Samotná bodová(41) proto nedává rozsah
Doobova přírůstku≤1. Pro některé konkrétní závislé modely
může zvláštní odhad přesto existovat; odpověď popisuje
selhání obecného důkazu, netvrdí nemožnost všech odhadů.

## Úplný konečný svědek významu nezávislosti

Následující příklad jen dokládá otázku94, není chybou v knize.
Vezměme t=m=4, U rovnoměrné na{0,1,2,3} a nezávislý férový
bit B. Všech osm dvojic(U,B) má pravděpodobnost1/8.
Pro B=0 nastavme všechny čtyři adresy na U. Pro B=1 nastavme
adresy na U,U+1,U+2,U+3 modulo4. Každá jednotlivá adresa je
rovnoměrná, ale adresy nejsou nezávislé.

Při B=0 jsou tři přihrádky prázdné, při B=1 žádná. Tedy
Q∈{3,0} s vahami1/2, EQ=3/2. Součinový vzorec93 by chybně
dal4(3/4)^4=81/64, zatímco3/2=96/64. Po první adrese je B
stále férový a Doobův průměr je3/2. Druhá adresa B přesně
odhalí, takže druhý přírůstek je±3/2 a má šířku3.

Kdyby se bez nezávislosti použil exponent s t=4, při x=3/2
by vznikla nepravdivá mez

```
1/2=P(Q−EQ≥3/2)≤exp(−9/8)<1/2.
```

Poslední ostrá nerovnost je přesná: e^(9/8)>1+9/8=17/8>2.
Všech osm stavů a všechny marginály byly vyčísleny přímo,
bez numerického testu či simulace.

## Rozsah uzavření

Celé92–94, každý tištěný mezikrok a všechny okraje jsou doloženy.
Manifest `mpr-092-094-doob-errata.json` pokrývá všech šest
lokálních vrstev i tři TeX zdroje; shody posouzeny v kontextu.
Žádná nová bibliografická citace v těchto odpovědích není.
Bez nálezu, kandidáta, bibliografické výjimky, běhu či restartu.
File40 zůstává partial pro95–97, file404 pro95–99.
