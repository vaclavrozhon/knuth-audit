# D105 — celá MPR2, včetně obecného počtu kostek

6. listopadu 2026. Zadání na12/file32 a celá odpověď na370–371,
file390–391, byly přímo zobrazeny. Autorův Pre-Fascicle5A má tentýž
matematický text na27–28/file33–34; také obě tyto strany byly zobrazeny.
Níže jsou samostatně prověřeny všechny tištěné redukce pro tři kostky
a celý matematický dovětek pro n kostek. Žádný census ani numerické
hledání není potřeba. Bibliografické výjimky jsou uvedeny na konci.

## Tři kostky: model, odstranění rovností a slovo

Každá kostka má konečný kladný počet stejně pravděpodobných stěn;
hody různými kostkami jsou nezávislé. Čísla na stěnách mohou být
libovolná reálná čísla. Označme výhry A=P(A>B), B=P(B>C), C=P(C>A),
přičemž v těchto třech pravděpodobnostech je nerovnost ostrá.

Je-li nějaká hodnota x na více kostkách, nahradíme všechny její výskyty
na A hodnotou x+ε a na C hodnotou x−ε; na B ponecháme x. Zvolíme
kladné ε tak, aby 2ε bylo menší než nejmenší kladná mezera mezi
různými původními hodnotami. Pokud žádné dvě různé hodnoty nejsou,
stačí libovolné ε>0. Všechny původní ostré nerovnosti se zachovají.
Původní rovnosti nebyly výhrami v žádném duelu, takže jejich rozdělení
žádnou pravděpodobnost výhry nezmenší. Žádná hodnota již neleží
na více kostkách. Opakování na téže kostce ničemu nevadí.

Seřazení stěn podle hodnot tedy dává slovo nad A,B,C. Pro řešení1(b)
je přesně CBBBAAAAACCCCCBBBA: hodnoty1,2,3,4,5,6 dávají postupně
bloky C,BBB,AAAAA,CCCCC,BBB,A. Vyměníme-li sousední AB za BA,
zvětší se A o součin kladných hmotností těchto dvou položek;
B a C se nezmění. Obdobně zlepšují BC→CB a CA→AC příslušné
ostatní duely. U stejně pravděpodobných stěn mají hmotnosti známé
racionální hodnoty; argument však platí i pro libovolné kladné váhy.

Při pevných položkách existuje jen konečně mnoho jejich permutací
a každá výměna přísně zvětšuje A+B+C. Posloupnost výměn proto
skončí. Po sloučení stejných sousedních písmen zbývá střídání
C,B,A,C,B,A,…, případně po cyklickém přejmenování tří kostek.
Cyklické přejmenování pouze permutuje A,B,C a zachovává jejich
minimum. Nedokazujeme, že při přejmenování zůstávají stejné názvy
jednotlivých souřadnic.

Slovo tedy má tištěný tvar

```
C^c1 B^b1 A^a1 … C^ck B^bk A^ak,
```

kde všechna c_i jsou kladná, a_i,b_i jsou kladná pro i<k,
a poslední b_k,a_k smějí být nulová. Každá ze tří kostek je stále
neprázdná. Normalizované hmotnosti α_i,β_i,γ_i mají každá součet1.
Přímo rozdělením výher podle bloku první kostky dostáváme všechny
tři vytištěné výrazy:

```
A = Σ_i α_i Σ_{j≤i} β_j,
B = Σ_i β_i Σ_{j≤i} γ_j,
C = Σ_i γ_i Σ_{j<i} α_j.
```

Například A v i-tém bloku překoná právě B v blocích1,…,i;
C v i-tém bloku překoná právě A v blocích1,…,i−1. Členy jsou
disjunktní události a nezávislost dává jejich součiny.

## Všech šest změněných vah a tři případy λ

Nejsme-li již v koncovém tvaru k≤2,α₂=0, jsou α₁,α₂,β₁,β₂,γ₁,γ₂
kladné. Pro k≥3 to plyne z vnitřních bloků; pro k=2 s α₂>0 musí
být β₂>0, jinak by na konci zůstalo zakázané sousední CA.
Nulové bloky jsou odstraněny ještě před touto úvahou.

Pro λ>0 provádí tisk změnu

```
γ₂′=λγ₂, γ₁′=γ₁+(1−λ)γ₂,
β₂′=λβ₂, β₁′=β₁+(1−λ)β₂,
α₁′=α₁/λ, α₂′=α₁+α₂−α₁/λ.
```

Součet prvních dvou vah každého druhu se zachovává. Proto se nemění
žádný příspěvek z pozdějších bloků. Raný příspěvek k A lze psát
(α₁+α₂)(β₁+β₂)−α₁β₂; součin α₁′β₂′ je α₁β₂, tedy A′=A.
Raný příspěvek k C je γ₂α₁, rovněž nezměněný. Raný příspěvek k B
je (β₁+β₂)γ₁+β₂γ₂. Po dosazení má jeho přírůstek přesně tvar

```
[(1−λ)(β₁+β₂)+(λ²−1)β₂]γ₂
  = (1−λ)(β₁−λβ₂)γ₂.
```

Tím jsou ověřeny všechny tištěné rovnosti, nikoli jen konečný závěr.

1. Jestliže β₁≥β₂, zvolíme λ=α₁/(α₁+α₂), tedy 0<λ<1.
   Pak α₂′=0 a α₁′=α₁+α₂. Obě další první váhy se zvětší,
   druhé zůstanou kladné. Přírůstek B je nezáporný, protože
   β₁−λβ₂≥β₁−β₂≥0.
2. Jestliže β₁<β₂ a γ₁/γ₂≤β₁/β₂, zvolíme λ=1+γ₁/γ₂>1.
   Pak γ₁′=0 a β₁′=β₁−(γ₁/γ₂)β₂≥0. Dále α₁′<α₁,
   takže α₂′>α₂≥0. Oba činitelé1−λ a β₁−λβ₂ jsou záporní,
   tudíž B′−B>0. Rovnost v podmínce může vynulovat i β₁′;
   to pouze odstraní další blok.
3. Jestliže β₁<β₂ a γ₁/γ₂>β₁/β₂, zvolíme λ=1+β₁/β₂>1.
   Pak β₁′=0, γ₁′=γ₁−(β₁/β₂)γ₂>0 a opět α₂′>α₂≥0.
   Nyní β₁−λβ₂=−β₂, takže B′−B=β₁γ₂>0.

Všechny hmotnosti jsou nezáporné a jejich součty zůstávají1;
proto automaticky nepřekračují1. Každý případ vynuluje alespoň
jeden dříve kladný blok. Nulové bloky odstraníme, stejné sousední
sloučíme a případné nové zakázané sousedství opět uspořádáme
konečnými zlepšujícími výměnami. Tyto výměny lze dělat s celými
váženými bloky; jejich konečný počet permutací a přísný růst
A+B+C znovu zaručují konec. Rozdělování bloků není potřeba.

Počet kladných bloků se při každé λ-redukci přísně sníží a nikdy
se nezvětší následným uspořádáním nebo přejmenováním. To je přesný
invariant ukončení pro tištěné „shorter array“; samotné k by nebylo
vždy dostatečným měřítkem, například po odstranění počátečního C.
Celkem je nejvýše tolik λ-redukcí, kolik bylo původních bloků.
Tento existenční důkaz nevyslovuje polynomiální čas pro všechny
pomocné výměny a žádný takový náklad nepotřebuje.

## Koncový případ a ostrá mez

Pro k≤2,α₂=0 máme α₁=1. Pokud k=1, doplníme β₂=γ₂=0.
Ze tří součtů dostáváme

```
A=β₁, B=1−β₁γ₂, C=γ₂.
```

Položme r=1/φ=(sqrt5−1)/2, takže r²+r=1. Pokud jsou A i C
větší než r, pak B<1−r²=r. V každém případě tedy min(A,B,C)≤r.
Všechny předchozí operace toto minimum nezmenšovaly, a stejná
horní mez platí i pro původní kostky.

Pro konečné počty stejně pravděpodobných stěn jsou původní tři
pravděpodobnosti racionální; jejich minimum nemůže být iracionální r.
Proto platí požadované min(A,B,C)<r. Přísnost se netvrdí pro
libovolné reálné váhy: dvě dvoubodové a jedna konstantní veličina
vhodnými iracionálními vahami rovnosti skutečně dosáhnou.
Asymptotickou dosažitelnost s konečnými kostkami už obecně dokazuje
D104; žádný jeho výpočet se neopakuje.

## Dovětek pro n: polynomy, váhy, konstrukce a všechny rovnosti

Nejprve ověříme samotnou konstrukci, potom zvlášť její optimalitu.
Pro n≥2 definujme

```
θ=π/(n+2), q=1/(4cos²θ), p=1−q,
f₀(z)=1, f₁(z)=1−z, f_{j+1}(z)=f_j(z)−z f_{j−1}(z),
f_{−1}(z)=1.
```

Poslední pomocný počátek je konzistentní s rekurencí pro f₁.
Definice Chebyshevových polynomů U₀(t)=1,U₁(t)=2t,
U_{j+1}(t)=2tU_j(t)−U_{j−1}(t) dává, kontrolou obou počátků
a téže rekurence,

```
f_j(x²)=x^{j+1} U_{j+1}(1/(2x))  (x≠0).
```

V x=0 jde o polynomiální identitu s odstranitelným zápisem pravé
strany, nikoli o dosazení do samotného1/(2x). Ze sčítacího vzorce
pro sinus a obou počátků rovněž indukcí plyne
U_j(cosθ)=sin((j+1)θ)/sinθ. S x=1/(2cosθ)>0 tedy

```
f_j(q)=x^{j+1} sin((j+2)θ)/sinθ,
f_n(q)=0,
f_j(q)>0 pro −1≤j≤n−1.
```

Rekurence také přímo dává
f_j(z)=Σ_{h=0}^{floor((j+1)/2)} (−1)^h binom(j+1−h,h) z^h:
Pascalova identita ověřuje každý koeficient i oba počátky.
Jeho stupeň je tedy floor((j+1)/2). Sinusový vzorec určí právě
tolik různých kladných kořenů
1/(4cos²(kπ/(j+2))), k=1,…,floor((j+1)/2).
Nejmenší je k=1. Tím je prověřena i volba kořene, kterou by
samotná rovnost f_n(1−p_n)=0 neurčovala.

Vytvořme D₁ konstantní a D_j,2≤j≤n, se dvěma hodnotami,
nízkou s pravděpodobností α₁^(j)=1−u_j a vysokou s
pravděpodobností α₂^(j)=u_j, kde

```
u₂=q,
u_{j+1}=q/(1−u_j),
u_j=q f_{j−3}(q)/f_{j−2}(q),
1−u_j=f_{j−1}(q)/f_{j−2}(q).
```

Poslední dvě identity plynou indukcí z rekurence; jejich kladné
čitatele a jmenovatele zajišťují0<u_j<1. Z f_n(q)=0 dále plyne

```
f_{n−1}=q f_{n−2},
q f_{n−3}=f_{n−2}−f_{n−1}=(1−q)f_{n−2},
u_n=1−q=p.
```

Zvolme skutečné hodnoty v přesném pořadí

```
low(D_n)<…<low(D₂)<D₁<high(D_n)<…<high(D₂).
```

Při nezávislých hodech pak

```
P(D₁>D₂)=α₁^(2)=1−u₂=p,
P(D_j>D_{j+1})=1−α₁^(j)α₂^(j+1)=1−(1−u_j)u_{j+1}=p,
P(D_n>D₁)=α₂^(n)=u_n=p.
```

Ve vnitřním duelu je jedinou prohrou nízká hodnota D_j proti
vysoké hodnotě D_{j+1}; všechny ostatní tři páry vyhrávají.
To je přesně celý tištěný řetězec rovností včetně obou konců.

Pro M stejně pravděpodobných stěn zaokrouhlíme každé M u_j na
celé číslo s chybou nejvýše1 a konstantní kostku zopakujeme Mkrát.
Každá změna pravděpodobnosti jednoho duelu je nejvýše2/M:
součin dvou čísel z[0,1] se při změnách δ,ε změní nejvýše
|δ|+|ε|. Proto minimum konečných kostek je alespoň p−2/M.
To dokazuje asymptotickou dolní mez pro stejný počet stěn na
všech kostkách, včetně případu nulových zaokrouhlených četností.

## Obecná horní mez: úplná redukce na dvě hodnoty

Následující vlastní důkaz doplňuje skutečnou optimalitu; výše
ověřená konstrukce sama horní mez nedokazuje. Pracujeme s n≥3
a konečnými rozděleními s libovolnými kladnými reálnými váhami.
Nejdříve lze všechny původní hodnoty na různých kostkách nepatrně
a navzájem různě posunout. Konečná kladná minimální mezera
zajišťuje zachování všech původních ostrých porovnání, zatímco
rozlišení rovností může výhry pouze přidat. Můžeme tedy předpokládat,
že žádné dvě kostky nesdílejí hodnotu.

U jedné kostky s m≥3 kladnými atomy a vahami w_j jsou její dva
sousední duely lineárními funkcemi těchto vah. Existuje nenulový
směr d_j splňující dvě homogenní rovnice

```
Σ_j d_j=0,
Σ_j d_j P(D_{i−1}>value_j)=0.
```

Je to jádro matice se dvěma řádky a alespoň třemi sloupci.
Zvolíme jeho znaménko tak, aby
Σ_j d_j P(value_j>D_{i+1})≥0. Změnou w→w+t d pro t≥0
se zachovává normalizace a předchozí duel; následující se nezhorší.
Ostatní duely na této distribuci nezávisejí. Nenulový směr se
součtem0 má kladnou i zápornou složku, takže při
t=min_{d_j<0}w_j/(−d_j)>0 vynulujeme alespoň jeden atom a
všechny ostatní váhy zůstanou nezáporné.

Opakováním zbývají nejvýše dva atomy této kostky. Projdeme tak
všech n kostek; pozdější změna vah žádné již odstraněné hodnoty
nevrací. Počet redukcí je nejvýšeΣ_i max(0,m_i−2).
Každý krok zachovává nezávislý produktový model a žádnou
z n cyklických pravděpodobností nezmenšuje. To je úplnost,
invariant i konečné ukončení redukce; nejde o numerickou heuristiku.

Pokud má některá kostka jediný atom, přejdeme rovnou ke kvantilové
mezi níže. Jinak pišme dvě hodnoty l_i<h_i a
u_i=P(D_i=h_i)∈(0,1). Pro dvě sousední kostky jsou, vzhledem
k různým hodnotám, právě tyto druhy uspořádání:

- Disjunktní intervaly. Pokud celý D_i leží níže než D_{i+1},
  je příslušná výhra0 a horní mez je triviální. Pokud leží výše,
  nahradíme D_i konstantou l_i. Jeho výhra nad D_{i+1} zůstane1
  a výhra D_{i−1} nad D_i se může jen zvětšit.
- Interval D_i obsahuje interval D_{i+1}. Výhra D_i nad
  D_{i+1} je u_i a nezávisí na jeho vahách. Nahradíme D_{i+1}
  konstantou h_{i+1}, což jeho následující výhru nezmenší.
- Interval D_{i+1} obsahuje interval D_i. Výhra je1−u_{i+1}
  a nezávisí na vahách D_i. Nahradíme D_i konstantou l_i,
  což nezmenší jeho předchozí duel.
- Všechny sousední intervaly se skutečně proplétají. Pak je
  příslušná výhra buď

```
H_i=1−(1−u_i)u_{i+1}, pokud l_i>l_{i+1},
L_i=u_i(1−u_{i+1}),   pokud l_i<l_{i+1}.
```

Případy vyplývají prostým výčtem čtyř možných párů hodnot.
Navíc

```
H_i−L_i=(1−u_i)(1−u_{i+1})+u_i u_{i+1}>0.
```

V cyklu různých l_i existuje alespoň jedna hrana druhu L.
Cyklicky přejmenujeme kostky, aby jednou z nich byla n→1,
a beze změny vah nově zvolíme hodnoty v pořadí

```
l_n<l_{n−1}<…<l₁<h_n<h_{n−1}<…<h₁.
```

Hrany1→2,…,n−1→n nyní mají výhru H_i; poslední má L_n.
Každá původní H zůstala H, některé L se zlepšily na H a zvolená
poslední L se zachovala. Všechny původní pravděpodobnosti tedy
stále nezmenšujeme. Je to konkrétní realizovatelné pořadí všech
2n hodnot, nikoli nezávislé přepínání neslučitelných duelů.

## Kanonický minimax má konstantní kostku

Položme r_i=1−u_i. Pro poslední kanonickou rodinu jsou
pravděpodobnosti proher

```
Q_i=r_i(1−r_{i+1})  (i<n),
Q_n=1−(1−r_n)r₁.
```

Minimum q=min_{r∈[0,1]^n} max_i Q_i existuje, protože maximum
konečně mnoha polynomů je spojité a krychle je kompaktní.
Platí q>0: rovnost Q_n=0 by vynutila r₁=1,r_n=0,
zatímco Q₁=…=Q_{n−1}=0 potom postupně vynutí r₂=…=r_n=1,
což je spor. Pro r₁=1/2,r₂=…=r_n=0 vyjde maximum1/2,
tedy0<q≤1/2. Tato pomocná horní mez nevyužívá hledaný výsledek.

Předpokládejme pro spor, že minimum nastává ve vnitřním bodě
0<r_i<1. Pak musí být všechna Q_i=q. Jinak v cyklickém seznamu
existuje přechod Q_i=q,Q_{i+1}<q. Mírně zvětšíme r_{i+1}
(pro i=n jde o r₁). Tím Q_i přísně klesne, protože jeho derivace
je −r_i<0, respektive −(1−r_n)<0. Druhá měněná hodnota Q_{i+1}
zůstane při dostatečně malé změně pod q. Ostatní se nezmění.
Zmenšíme tedy počet hodnot rovných q a žádnou takovou nepřidáme.
Po nejvýše n těchto konečných malých změnách by všechny Q_i byly
menší než q. Všechny body lze udržet uvnitř krychle. To odporuje
definici minima, a dokazuje uvedenou nutnou rovnost.

Definujme nyní T(x)=q/(1−x) a T_j=T složené jkrát, T₀(x)=x.
Z Q_i=q pro i<n dostáváme r_i=T_{n−i}(r_n). V okolí
x₀=r_n jsou všechny tyto iterace kladné a menší než1, protože
totéž platí v x₀ a jmenovatele jsou tam nenulové. Změnou x
a současným dosazením r_i=T_{n−i}(x) tedy zachováme
Q₁=…=Q_{n−1}=q. Poslední prohra je

```
Q_n(x)=1−g(x),  g(x)=(1−x)T_{n−1}(x).
```

Kdyby existovala libovolně blízká hodnota x s g(x)>g(x₀),
měli bychom vnitřní bod s Q_n<q a ostatními Q_i=q.
Předchozí argument by pak snížil všechny pod q. Proto by g
musela mít v x₀ lokální maximum.

To však není možné. Přímá derivace a řetězové pravidlo dávají

```
T′(x)=T(x)²/q,
T_j′(x)=q^(−j) ∏_{h=1}^j T_h(x)²,
g′(x)/T_{n−1}(x)
 = (1−x)T_{n−1}(x)∏_{h=1}^{n−2}T_h(x)²/q^{n−1} −1
 = T₁(x)T_{n−1}(x)∏_{h=2}^{n−2}T_h(x)²/q^{n−2} −1.
```

Poslední krok výslovně používá(1−x)T₁(x)=q; pro n=3 je
prostřední součin prázdný a má hodnotu1. Každý T_h je kladný
a přísně rostoucí v daném okolí. Výraz před posledním minus1
je proto přísně rostoucí. Znaménko g′ buď zůstává stejné,
nebo se může změnit pouze ze záporného na kladné; g tam nemůže
mít lokální maximum. Rozpor dokazuje, že minimum na krychli
leží na jejím okraji.

V okrajovém bodě je některé r_i rovno0 nebo1, tedy jedna
z kostek je konstantní. Kanonická rodina tak dosahuje svého
největšího minima výher v systému s konstantní kostkou.
Dosavadní redukce proto opravňují ověřit obecnou horní mez
jen pro systémy obsahující konstantní kostku. Tato podmínka
nebyla převzata bez důkazu z externího zdroje.

## Kvantilová horní mez a uzavření obecného n

Vraťme se k q*=1/(4cos²(π/(n+2))) z polynomiální konstrukce;
hvězdička jej nyní odlišuje od pomocného minima předchozí části.
Položme t₀=0 a t_k=q*/(1−t_{k−1}) pro k=1,…,n.
Stejná rekurence dává

```
t_k=q* f_{k−2}(q*)/f_{k−1}(q*),
1−t_k=f_k(q*)/f_{k−1}(q*).
```

Z již dokázané kladnosti f₀,…,f_{n−1} a f_n(q*)=0
plyne0<t_k<1 pro1≤k<n, t_n=1 a pro všechna k
t_k(1−t_{k−1})=q*.

Kostky cyklicky a případně obráceným pořadím označíme
Y₀=Y_n,Y₁,…,Y_{n−1}, aby konstantní kostka byla Y₀=Y_n=c
a sledované výhry měly tvar P(Y_{k−1}<Y_k). U každé
vnitřní Y_k zvolíme t_k-kvantil y_k:

```
P(Y_k≤y_k)≥t_k,
P(Y_k≥y_k)≥1−t_k.
```

Existence pro konečné rozdělení plyne volbou nejmenší hodnoty,
u níž kumulativní součet dosáhne t_k. Součet před ní je menší
než t_k, a proto platí i druhá nerovnost. Pro oba konce zvolíme
y₀=y_n=c; příslušné jednostranné podmínky s t₀=0,t_n=1
platí automaticky.

Protože y₀=y_n, nemůže být všech n kroků přísně rostoucích.
Pro některé k tedy y_{k−1}≥y_k. Nezávislost sousedních
veličin a uvedené kvantilové nerovnosti dávají

```
P(Y_{k−1}≥Y_k)
 ≥ P(Y_{k−1}≥y_{k−1}, Y_k≤y_k)
 = P(Y_{k−1}≥y_{k−1})P(Y_k≤y_k)
 ≥ (1−t_{k−1})t_k=q*.
```

Příslušná ostrá výhra je proto nejvýše1−q*. To platí pro
libovolný systém s konstantní kostkou, tedy po předchozím
minimaxovém a redukčním důkazu i pro všechny původní konečné
kostky. Spolu s dosažitelností a zaokrouhlením je přesně

```
p_n=1−1/(4cos²(π/(n+2))).
```

Pro n=2 se horní mez1/2 dokazuje odděleně součtem dvou
opačných ostrých pravděpodobností≤1; konstantní1 proti férové
dvouhodnotové0,2 ji dosáhne. Pro n=1 je vlastní ostré porovnání
vždy nepravdivé a vzorec dává0; žádné nezávislé dvě kopie téže
kostky se pod tímto triviálním cyklem nepodsouvají. Pro n=3
vzorec souhlasí s r=(sqrt5−1)/2 a s důkazem hlavní úlohy.

## Zdroje, errata a přesný uzavřený rozsah

Kromě originálu a autorova PS byly pro obecnou horní mez otevřeny
dva primární zdroje, uložené s adresami a SHA256 v
`sources/mpr002-primary-source-manifest.json`:

- I. I. Bogdanov, „Нетранзитивные рулетки“, Matematicheskoe
  prosveshchenie, ser.3,14(2010),240–255; volné PDF vydavatele
  MCCME. Byla přečtena relevantní strukturální argumentace,
  nikoli provedena kontrola všech dalších tvrzení článku.
- A. Komisarski, autorova přednáška „Nieprzechodniość
  w porządkach zmiennych losowych“,2018; přečten relevantní
  konstrukční a kvantilový argument. Dřívější redukci na
  konstantní veličinu přednáška pouze cituje, proto ji výše
  dokazujeme samostatně, včetně všech mezikroků a okrajů.

Samotný článek Komisarski, AMM128(2021),423–434, nebyl získán
v plném textu: stránka vydavatele vracela403. Usiskin1964
a Trybuła1965 také nebyly v plném textu prověřeny. Tyto
bibliografické kontroly a historické prvenství jsou výslovně
vynechané; žádný neviděný důkaz z nich není označen za přijatý.
Výše uvedené konečné lineární redukce, kanonické uspořádání,
minimax, kvantily a konstrukce tvoří samostatný úplný důkaz
v rozsahu tvrzení knihy o kostkách.

Šest místních vrstev errat a všechny tři dostupné původní TeXy
byly porovnány. Jediná nově příslušná změna je E118:
známé doplnění Komisarski2021 do poslední řádky odpovědi2
ve Fascicle5, str.183, z26.8.2021. Originální sazba all4f5,
file9, i TeX byly přímo přečteny; doplnění už je v4B na371.
Nejde o nový nález ani matematickou opravu. Sousedsko-stránkové
změny E113/E117 již patří předchozím rozsahům a znovu je nepočítáme.
Renderer errat hlásil Type3 varování; cílový bibliografický řádek
je přesto jednoznačně čitelný a souhlasí s původním TeXem.

D105 uzavírá celou MPR2 a celý matematický dovětek odpovědi2.
File32 zůstává partial kvůli úlohám3–4. File390 zůstává partial
kvůli dříve otevřené Front3; tato poznámka ji nepřebírá.
File391 zůstává partial kvůli odpovědím3 a následujícím.
Žádný nový nález, dlouhý výpočet ani restart starého běhu.
