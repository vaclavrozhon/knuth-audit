# §1.2.6-(59)–(60), úloha 65: konvergence a asymptotika

Audit 1. listopadu 2026. Zobrazen originál s. 69,74,491.
Základní notace a polynomiální pokračování Stirlingových čísel
jsou definovány v `stirling-identities.md`, zejména (S1)–(S3).
Zde c(r,r−k), S(r,r−k) znamenají právě tyto polynomy v r,
kde k je nezáporné celé číslo. Pro komplexní a definujeme
`z_[a]=Gamma(z+1)/Gamma(z−a+1)` tam, kde má podíl smysl,
a jinde jeho meromorfním pokračováním. Pro Re(z)>0 v (59)
je čitatel konečný a reciproká Gamma ve jmenovateli celistvá.
Mocnina z^a používá větev logaritmu s −pi/2<arg(z)<pi/2.

## Co se ověřuje

Knižní rovnice mají různé levé strany:

```text
z^r = sum_{k>=0} S(r,r−k) z_[r−k],       Re(z)>0;           (A1)
z_[r] = sum_{k=0}^m (−1)^k c(r,r−k) z^(r−k)
        + O(|z|^(Re(r)−m−1)),            z→+infinity.       (A2)
```

V (A2) je vlevo padající mocnina, jejíž podtržení OCR snadno
ztratí. Odhad platí pro pevná r a celé m>=0; níže také
v každém uzavřeném sektoru |arg(z)|<=pi/2−delta, delta>0.
Symbol O znamená omezení absolutní hodnoty chyby konstantou
krát uvedenou mocninu |z| pro dost velké |z| v daném sektoru.

Primární pramen je D. E. Knuth, *Two Notes on Notation*,
AMM 99 (1992), 403–422, autorský preprint
<https://arxiv.org/abs/math/9205211>. Pasáž (2.25)–(2.29)
na stranách preprintu 17–18 obsahuje Loganův důkaz (A1)
a odkaz na asymptotiku podílů Gamma. Následuje vlastní
doplnění odhadů, které ospravedlňují záměny nekonečných řad
a integrálů; numerická shoda by je nenahradila.

## Koeficienty logaritmické generující funkce

Položme p=−r a pro |u|<1 definujme

```text
A(u) = −log(1−u)/u,   A(0)=1,
g_p(u) = A(u)^(p−1)/(1−u) = sum_{k>=0} a_k(p)u^k.          (A3)
```

Integrální vyjádření A(u)=integral_0^1 (1−tu)^−1 dt
ukazuje Re(A(u))>1/2. Funkce A tedy nemá v jednotkovém
kruhu nuly a její logaritmus s log A(0)=0 je jednoznačný.
V (A3) používáme tuto větev. Koeficient a_k(p) je polynom
v p stupně nejvýše k, protože log A(u) má nulový konstantní
člen a v koeficientu u^k exponenciály mohou přispět jen
první k mocniny log A.

Pro kladné celé p platí exponenciální generující funkce
cyklových Stirlingových čísel

```text
(−log(1−u))^p / p! = sum_{j>=p} c(j,p)u^j/j!.
```

Lze ji dokázat z rekurence (S2) porovnáním derivací nebo
výběrem p nepojmenovaných cyklů. Derivace této rovnosti dává
`a_k(p)=c(p+k,p)Gamma(p)/Gamma(p+k)`.
Dualita (58) a polynomiální pokračování tedy dávají

```text
(p)^[k] a_k(p) = S(−p,−p−k).                              (A4)
```

Obě strany jsou polynomy v p a shodují se pro všechna kladná
celá p, proto i pro všechna komplexní p. Tím se vyhneme
nepovolenému dělení v p=0,−1,... . Stejnou skutečnost lze
vidět z nul S(n,n−k) pro 0<=n<k: pravá strana je dělitelná
rostoucím součinem (p)^[k].

## Odhad koeficientů a důkaz absolutní konvergence (A1)

Na kružnici |u|=rho, 1/2<=rho<1, máme

```text
1/2 < |A(u)| <= C log(2/(1−rho)),    |arg A(u)|<pi/2.
```

Proto na každé kompaktní množině parametrů p existují
konstanty C,M>=0, pro něž
`|A(u)^(p−1)| <= C log(2/(1−rho))^M`.
Cauchyho integrální formule pro koeficienty, použitá s
integrálním odhadem místo maxima, dává

```text
|a_k(p)| <= C rho^(−k) log(2/(1−rho))^M
                 integral_{−pi}^pi |1−rho exp(i theta)|^−1 dtheta
         <= C' rho^(−k) log(2/(1−rho))^(M+1).
```

Poslední integrál je O(log(2/(1−rho))), neboť
`|1−rho exp(i theta)|²=(1−rho)²+2rho(1−cos theta)`
a 1−cos theta je na [−pi,pi] zdola omezeno kladnou
konstantou krát theta². Volba rho=1−1/(k+1), k>=1,
tedy ukazuje

```text
|a_k(p)| <= C'' log(k+2)^(M+1),                             (A5)
```

lokálně stejnoměrně v p. Konečné malé k zahrneme do konstanty.

Pro Re(p)>0 a Re(z)>0 použijeme Laplaceův integrál Gamma
a substituci u=1−exp(−t):

```text
z^(−p)
 = 1/Gamma(p) integral_0^infinity exp(−zt)t^(p−1)dt
 = 1/Gamma(p) integral_0^1 u^(p−1)(1−u)^z g_p(u)du.
```

Beta integrál `B(a,b)=integral_0^1 u^(a−1)(1−u)^(b−1)du`
pro Re(a),Re(b)>0 splňuje
`B(a,b)=Gamma(a)Gamma(b)/Gamma(a+b)`; odvození dvojitým
Gamma integrálem a substitucí (s,t)=(v u,v(1−u)) je
oprávněné absolutní konvergencí. Pro pevné a,b s Re(b)>0
je `B(k+Re(a),Re(b))=O(k^(−Re(b)))`. Přímo to plyne
z `(1−v)^(k+Re(a)−1)<=exp(−kv/2)` pro dost velké k,
po substituci v=1−u.

Odhad (A5) a tento beta odhad dovolují integrovat (A3)
po členech absolutně. Výsledný k-tý člen je

```text
a_k(p) Gamma(p+k)/Gamma(p) * Gamma(z+1)/Gamma(z+p+k+1)
 = S(−p,−p−k) z_[−p−k].
```

Tím je (A1) dokázána pro Re(p)>0.

Pro rozšíření na všechna p zvolíme na dané kompaktní množině
celé J tak velké, aby Re(p+J)>0. Pro k>=J lze faktor
násobící a_k(p) přepsat na

```text
(p)^[k] Gamma(z+1)/Gamma(z+p+k+1)
 = (p)^[J]/Gamma(p+J) * B(p+k,z+1).                        (A6)
```

Beta integrál vpravo je O(k^(−Re(z)−1)), stejnoměrně na
kompaktních množinách p,z s Re(z)>0. Spolu s (A5) dostáváme
absolutní a lokálně stejnoměrnou konvergenci celé řady (A1).
Její členy jsou celistvé funkce p; výsledný součet tedy také.
Věta o jednoznačnosti holomorfních funkcí rozšiřuje rovnost
z poloroviny Re(p)>0 na všechna komplexní p. Podmínka
Re(z)>0 tak opravdu stačí i pro necelé a komplexní r.

## Důkaz asymptotického rozvoje (A2)

Nejprve Re(p)>0. Beta integrál se stejnou substitucí dává

```text
z_[−p] = 1/Gamma(p) integral_0^infinity
                  exp(−zt)t^(p−1) H_p(t)dt,
H_p(t) = exp(−t) ((1−exp(−t))/t)^(p−1).                   (A7)
```

Funkce H_p je analytická poblíž t=0, s větví určenou
hodnotou 1 uvnitř mocniny. Označme
`Q_p(t)=((1−exp(−t))/t)^p`. Přímá derivace dává
`H_p=Q_p+(t/p)Q'_p`. Exponenciální generující funkce
S(n,p), pro kladné celé p, dává

```text
[t^k]Q_p(t) = (−1)^k S(p+k,p) Gamma(p+1)/Gamma(p+k+1).
```

Po vynásobení konečným rostoucím součinem jde opět
o polynomiální identitu v p, proto pokračuje na obecné p.
Píšeme-li H_p(t)=sum h_k(p)t^k, dostáváme

```text
(p)^[k] h_k(p) = (−1)^k S(p+k,p)
               = (−1)^k c(−p,−p−k).                      (A8)
```

Taylorův rozvoj H_p do stupně m má na malém [0,epsilon]
zbytek O(t^(m+1)). V (A7) tedy jeho integrál činí
O(|z|^(−Re(p)−m−1)) v uvedených sektorech. Na
[epsilon,infinity) je H_p(t)t^(p−1) omezeno exponenciálně
klesající funkcí pro dost velké t; faktor exp(−zt) poskytne
exponenciálně malý zbytek, protože Re(z)>=|z|sin(delta).
Integrál každého Taylorova členu lze prodloužit do nekonečna
za stejnou cenu. Jeho hodnota je
`h_k(p)Gamma(p+k)/Gamma(p) z^(−p−k)`.
Rovnost (A8) nyní dává (A2) pro Re(r)<0.

Pro libovolné pevné r začneme u r−N s Re(r−N)<0
a N-krát použijeme `z_[r+1]=(z−r)z_[r]`.
Koeficienty `D_k(r)=(−1)^k c(r,r−k)` splňují podle (S3)
`D_k(r+1)=D_k(r)−rD_(k−1)(r)`, přesně jako součin
rozvoje činitelem z−r. Zbytek se násobením z−r zvětší
o nejvýše jednu mocninu |z|; požadovaný řád tedy zůstává
správný. To dokončuje důkaz pro všechny komplexní r.

## Konvergence (A2) není pro všechna r stejná

Knižní stručné označení rozvoje jako nekonvergentního
nelze chápat jako univerzální kvantifikaci přes všechny r.
Pro nezáporné celé r je rozvoj konečný. Pro r=−p, kde
p je kladné celé číslo, je levá strana racionální funkce
`1/((z+1)...(z+p))`; její Laurentův rozvoj v nekonečnu
konverguje pro |z|>p. Například r=−1 dává geometrickou řadu
`1/(z+1)=sum_{k>=0}(−1)^k z^(−k−1)` pro |z|>1.
Knuthův primární článek tyto celočíselné případy výslovně
uvádí u (2.18), před diskusí necelých exponentů.

Pro necelé p v polorovině Re(p)>0 má H_p(t) u t=2pi i
neodstranitelnou algebraickou větvovou singularitu: činitel
1−exp(−t) má jednoduchou nulu a exponent p−1 není celý.
Taylorovy koeficienty H_p tedy nemohou po násobení
Gamma(p+k) tvořit řadu s kladným poloměrem konvergence
v 1/z. Kdyby mohly, samotné koeficienty H_p by díky
faktoriálnímu růstu Gamma dávaly celistvou funkci t, což
je spor. Obecně necelé r se na tuto polorovinu přenesou
pomocí konečné Gamma rekurence a násobení či dělení
lineárními činiteli. Nekonečný rozvoj (A2) má tedy pro
necelé r skutečně nulový poloměr konvergence v 1/z.

Jde o potřebné upřesnění rozsahu, ne o nově potvrzený nález:
rovnice (60) tvrdí konečný asymptotický odhad, který je správný,
a celočíselné případy navazují na předchozí konečné identity.
