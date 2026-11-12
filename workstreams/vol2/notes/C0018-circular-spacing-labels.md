# V2-C0018: označení kruhových mezer v §3.3.2-26 a 27

**Stav:** potvrzená matematická chyba v prvním tisku třetího vydání,
str. 78, úloha 26(a) a první tvrzení úlohy 27; také začátky příslušných
odpovědí na str. 566–567. Příčina: poslední mezera obsahuje pevný
počátek kružnice, a proto není rozdělení označených mezer symetrické.
Všechna errata prohledána, novější fyzický tisk ani prvenství neověřeny.
Samotná tato poznámka se týká prvního tvrzení. Navazující audit
celých úloh26/27 je nyní uzavřen v [spacings.md](spacings.md).

## Definice z originální sazby

Na [str. 78](../images/vol2-p078.png), straně souboru 90, jsou U_1,...,U_n
nezávislé rovnoměrné body v [0,1). Jejich uspořádání je
U_(1)<=...<=U_(n). Kniha definuje

```
S_i = U_(i+1)-U_(i)  (1<=i<n),
S_n = U_(1)+1-U_(n).
```

Pro zadané prahy s_i pak tvrdí, že pravděpodobnost všech nerovností
S_i>=s_i je `(1-s_1-...-s_n)_+^(n-1)`, kde `x_+^k=x^k[x>=0]`.
[Odpověď na str. 566](../images/vol2-p566.png) začíná tvrzením,
že vektor (S_1,...,S_n) je rovnoměrný na simplexu: množině nezáporných
vektorů se součtem 1. Oba originály přečteny obrazově.

## Protipříklad se dvěma body

Pro n=2 máme S_1=|U_1-U_2| a S_2=1-|U_1-U_2|. Zvolme s_1=1/2,
s_2=0. Událost |U_1-U_2|>=1/2 tvoří dva pravoúhlé trojúhelníky
v jednotkovém čtverci, každý o odvěsnách 1/2. Její pravděpodobnost je

```
2 * (1/2)*(1/2)^2 = 1/4.
```

Vytištěný vzorec dává 1-1/2=1/2. Protipříklad tedy nepoužívá záporné
prahy, degenerované rozdělení ani numerickou aproximaci.

Ekvivalentně má S_1 hustotu 2(1-s) na (0,1), kdežto S_2 hustotu 2s.
Delší mezera má větší šanci obsahovat předem zvolený počátek 0.

## Obecné správné rozdělení při knižním označení

Uspořádaná n-tice bodů má hustotu n! na oblasti
0<u_1<...<u_n<1. Při změně proměnných na u_1,S_1,...,S_(n-1)
je Jacobian 1. Pro pevné mezery lze u_1 volit v intervalu délky S_n.
Integrací přes u_1 dostaneme hustotu

```
n! * S_n
```

v souřadnicích S_1,...,S_(n-1), kde S_n=1-sum_(i<n) S_i.
Rovnoměrný simplex by měl konstantní hustotu (n-1)!.

Pro nezáporné prahy se součtem T<=1 nyní přeložíme simplex pomocí
S_i=s_i+(1-T)V_i. Integrál souřadnice V_n přes jednotkový simplex
je jeho objem dělený n. Dostáváme

```
Pr(S_i>=s_i pro všechna i)
  = (1-T)^(n-1) * (1-T+n*s_n).
```

Pro n>=2 a T>1 je pravděpodobnost 0. Je-li některý práh záporný,
je třeba ho nejprve nahradit nulou. Knižní formulace „any real numbers“
potřebuje toto upřesnění i po opravě označení mezer: například n=2,
s_1=s_2=-1 by jinak dávalo pravděpodobnost 3.

## Dopad na úlohu 27 a minimální oprava

První tvrzení úlohy 27 říká, že po seřazení mezer a transformaci

```
S'_1=n*S_(1),  S'_j=(n-j+1)*(S_(j)-S_(j-1))  (j>=2)
```

vznikne stejná společná distribuce jako u původního označeného vektoru.
U n=2 má však S'_1=2*min(S_1,S_2) rovnoměrné rozdělení: pro 0<=x<=1,
Pr(S'_1>x)=Pr(x/2<S_1<1-x/2)=1-x. Původní S_1 rovnoměrný nebyl.
Například střední hodnoty jsou 1/2 a 1/3. Tvrzení o stejné společné
distribuci tedy selhává již u n=2.

Jednoduchá oprava pro obě úlohy: kruhové mezery označovat od jednoho
**předem zvoleného pozorování**, například U_1, ve směru kolem kružnice.
Ekvivalentně nejprve náhodně cyklicky posunout vektor mezer. Průměr
hustot je `(1/n)*n!*(S_1+...+S_n)=(n-1)!`, tedy rovnoměrný simplex.
V 26(a) je navíc vhodné výslovně omezit prahy na s_i>=0.

Tato změna zachovává neuspořádanou množinu mezer, tedy i jejich
uspořádané hodnoty. Sama tato chyba proto nevyvrací vzorce pro nejmenší
a největší mezeru nebo birthday test založený na jejich třídění.
Tyto navazující vzorce budou auditovány samostatně; neopravujeme je
automaticky jen proto, že původní odůvodnění používá chybnou symetrii.

## Errata a zdrojová omezení

Dne 1. listopadu 2026 prohledány `errata/text/all2-prepre.txt`,
`all2-pre.txt`, `all2.txt`, `err2.txt` a aktuální `sources/err2.textxt`:
str. 78, 566–567, úlohy 26/27 a výrazy spacings / joint probability.
Oprava definice nebo společného rozdělení nenalezena. Známé opravy
na těchto stránkách se týkají úlohy 24 a historické citace Whitwortha
v odpovědi 26. Vydavatelský náhled 2026 končí před tímto místem,
proto z něj přetrvávání chyby netvrdíme. Návrh hlášení neodeslán.
