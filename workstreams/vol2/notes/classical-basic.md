# §4.3.1: A/S/M a úlohy 2–16

Dokončený matematický a instrukční blok, 2. listopadu 2026. Kniha: třetí
vydání, první dotisk 1997; originály str.265–270,281–282,623–625 vizuálně
přečteny. Historická úloha1, bibliografický dovětek15 a zbytek sekce patří
následujícím blokům. Algoritmus D již má samostatný [důkaz](division.md).

Zde `b>=2` znamená celočíselný základ, číslice mají hodnoty `0,...,b-1`.
Píšeme `U=sum_i u_i b^i`, podobně V a W; index0 patří nejnižšímu řádu.
Počty číslic m,n jsou kladné. Přenos k je část hodnoty přecházející do
následujícího řádu; u odčítání je k záporná výpůjčka. V pododdílu MIX je
b velikost celého slova, nikoli základ jednoho bajtu.

## Sčítání, odčítání, porovnání: A/S a 2,4,9,11,12

Před krokem A2 v pozici j platí

```
sum_{i<j}(u_i+v_i)b^i = sum_{i<j}w_i b^i + k b^j,
0 <= k <= 1.
```

Rovnost je na začátku prázdná. Dělení `u_j+v_j+k` se zbytkem dá
`w_j` a nový k a zachová rovnost s j+1. Součet nepřesáhne `2b-1`, tedy
přenos zůstane0/1. Po n iteracích se k uloží do w_n. To doplňuje všechny
implikace induktivních tvrzení odpovědi4 i důkaz ukončení.

Pro m sčítanců v úloze2 nahradíme `u_i+v_i` jejich součtem. Induktivně
`0<=k<=m-1`, protože `m(b-1)+(m-1)=mb-1`. Při `m<=b` se konečný přenos
vejde do jediné číslice; přesně tuto podmínku potřebuje původní A3.
Pro úlohu9 nechť `b_j>=2` je základ řádu j a `B_j=product_{i<j}b_i`
je jeho váha. Stejný důkaz s vahami B_j a dělením b_j funguje beze změny;
konečný přenos je opět0/1.

Pro S nahradíme plus mínusem. `-b<=u_j-v_j+k<b` dává k v {-1,0} a
stejnou rovnost pro rozdíl. Na konci `U-V=W+k b^n`, takže `k=-1` právě
když U<V. Tehdy W=b^n-(V-U), je nenulové, a druhé odčítání `0-W` modulo
b^n dává V-U; jeho další výpůjčka se zahodí (úloha12). V úloze11 rozhodne
nejvyšší rozdílná číslice: příspěvek všech nižších řádů má absolutní
hodnotu nejvýše b^j-1, tedy nemůže změnit znaménko rozdílu v řádu j.

## Zleva doprava: úlohy5–8

Algoritmus B v odpovědi5 nejdříve uloží `(u_j+v_j) mod b`. Je-li součet
alespoň b, přičte1 k dosud uloženému levému prefixu obvyklým postupem.
Induktivní tvrzení: dokončený prefix w_n,...,w_j je součtem příslušných
prefixů vstupů. Přenos nepřekročí w_n, protože součet dvou n-místných
čísel je menší než 2b^n. Vnitřní i roste a vnější j klesá; oba cykly skončí.

Algoritmus C v odpovědi6 drží dosud nezapsanou číslici r v řádu i,
`0<=r<=b-2`, a za ní souvislou posloupnost nevyřešených hodnot b-1.
Nový součet t>=b rozhodne o zápisu r+1 a následujících nul; t<b-1 rozhodne
pro r a následující b-1. Při t=b-1 se pouze prodlouží nevyřešená posloupnost.
Nové r je v obou rozhodnutých případech nejvýše b-2. Pozdější přenos tedy
nemůže změnit již zapsané číslice. Závěrečný zápis předpokládá nulový další
přenos. Všechny pozice včetně případné počáteční nuly se zapíší právě jednou,
od nejvyšší po nejnižší.

Pro úlohu7 jsou všechny vstupní číslice nezávislé a rovnoměrné. Označme
`p=(b-1)/(2b)` pravděpodobnost `u_j+v_j>=b`. Pravděpodobnost součtu b-1 je
1/b. Řetěz k změněných číslic při přenosu proto má pravděpodobnost
`p b^{-(k-1)}(1-1/b)`, pokud jeho poslední pozice není počáteční sentinel
w_n=0; pokud je, odpadne poslední faktor. Pro pevné k existuje n-k pozic
prvního typu a jedna druhého. Dostáváme tištěný vzorec

```
m_k = (b-1)/(2b^k) * ((n+1-k)(1-1/b)+1/b),  1<=k<=n.
```

Zde m_k je očekávaný počet přenosů měnících právě k číslic. V řetězu b-1
žádná z příslušných dřívějších dvojic nevyvolala přenos, takže použitá
nezávislost není narušena dřívějšími úpravami prefixu.

Počet K všech jednotkových přenosů je pro B a A stejný **pro každý vstup**:
každý přenos sníží součet všech číslic o b-1, takže
`K=(sum_i u_i+sum_i v_i-sum_i w_i)/(b-1)`. U A nastane přenos po j
zpracovaných pozicích s pravděpodobností `(1-b^-j)/2`, neboť jde o součet
dvou rovnoměrných čísel v rozsahu0 až b^j-1. Tedy

```
E K = sum_{k=1}^n k m_k = (n-(1-b^-n)/(b-1))/2.
```

Počet L pozic, kde `u_j+v_j>=b`, má průměr np. Tím je doložena analýza
v odpovědi8; její instrukční konstanta má samostatnou opravu C0095 níže.

## Násobení: M,13,14

Před M4 platí následující rovnost pro již rozpracovaný součin:

```
sum_{l<j+m} w_l b^l + k b^(i+j)
  = U * sum_{l<j} v_l b^l + (sum_{l<i}u_l b^l) v_j b^j.
```

Všechny použité w_l jsou platné číslice. Na začátku je levá strana nulová.
Nahrazení `t=u_i v_j+w_{i+j}+k` dvojicí zbytek/podíl pouze převede hodnotu
z aktuálního řádu do dalšího a přidá právě další člen pravé strany.
`0<=t< b^2` plyne z `(b-1)^2+2(b-1)=b^2-1`, tedy `0<=k<b`.
Po m iteracích se přenos uloží do nové pozice j+m a vznikne invariant
pro j+1,i=0. Nulový násobitel v M2 pouze vytvoří novou nulovou nejvyšší
pozici, takže stejný invariant platí i při přeskočení vnitřního cyklu.
Tím je dokázána odpověď14, ukončení i všechny rozsahy registrů.

Pokud místo nulování v M1 necháme počáteční m-místné W0, přidá se W0
na pravou stranu všech invariantů. `UV+W0<b^(m+n)`; násobení se sčítáním
popsané na str.268 tedy funguje. Tabulka1 (914 krát84) má správných všech
osm stavů před M5/M6 i výsledek76776; záznam stavů je v JSON.

Úloha13 je jeden průchod tohoto postupu s jedinou číslicí násobitele.
MIX ukládá k, počítá dvojité slovo u_i v a přičítá k k dolní polovině;
přetečení zvýší horní polovinu o1. Mez t<b^2 vylučuje její přetečení.

## Úloha10: pořadí instrukcí S

Vstup do aritmetické trojice má A=c=1+k v {0,1}. Tištěné pořadí počítá
`c+u-v+(b-1)`, a přetečení udává, zda nevznikla výpůjčka. Jediná možná
dřívější kladná overflow situace `c+u=b` dává po odečtení a přičtení b-1
správný zbytek; záporné hodnoty mají magnitudu menší než b. Sticky overflow
příznak zůstává zapnutý až k příslušnému JOV/JNOV.

Po prohození05/06 je první hodnota c-v v [-(b-1),1], tedy bez přetečení.
Pak `c-v+u` leží v [-(b-1),b]; jediná mimořádná hodnota b se správně
přenese už v tomto kroku. Závěrečné b-1 dává stejnou platnou číslici a
stejnou informaci o výpůjčce. Záporná nula je přípustná.

Po prohození06/07 to neplatí. Pro n=2,U=b,V=1 se nízká pozice počítá
jako `1+0+(b-1)-1`: přetečení před SUB zanechá A=-1. Výstupní slova jsou
(-1,1) od nízkého řádu, zatímco správné číslice jsou (b-1,0). Formální
vážený součet záporného slova může náhodou souhlasit; požadovanou
nezápornou reprezentaci program neposkytuje.

## Přesné časování MIX: 3,8,13 a A/S/M

Základ bajtu označíme beta; celé slovo má b=beta^5 hodnot magnitudy.
Přepis [classical-basic.mix](../sources/classical-basic.mix) byl porovnán
s originály. Program S zahrnuje opravu STA W+N,1 z10.8.2000. Model používá
samostatná znaménka registrů včetně záporné nuly a skutečné počty návštěv
instrukcí. Celoslovné LD/ST, ADD/SUB a posuny stojí2, MUL10, DIV12,
ostatní zde prováděné instrukce1 cyklus. Vstupní overflow je vypnutý,
jak předpokládají běžná volání; OFLO je jen testovací záchytný bod.

| Program | Přesný čas v cyklech |
|---|---|
| A | 10N+6 |
| S, U>=V | 12N+3 |
| M | 27M(N-Z)+4M+10N+3-3Z+K+K' |
| odpověď3 | **5MN+7N+K+5** |
| odpověď8 | **9N+L+7K+4** |
| odpověď13 | 23N+K+5 |

N,M jsou počty slov, Z počet nulových slov násobitele; K,K' jsou počty
návštěv dvou INCX v M. V ostatních řádcích mají K,L význam příslušného
programu. Pro M odhad `K=K'=M(N-Z)/2` dává tištěných
`28MN+4M+10N+3-Z(28M+3)`. Vypuštění obou instrukcí M2 (LDX/JXZ) při
zachování ENTX0 odstraní3N cyklů a nulové větve; hranice
`Z/N>3/(28M+3)` v textu odpovídá tomuto odhadu.

Odpovědi3 a8 však v tištěném čase vynechávají jeden cyklus: úvodní tři
instrukce odpovědi3 stojí3 a závěrečné STX2, tedy konstanta5. Úvodní
ENT1,JOV,STZ odpovědi8 stojí1+1+2=4. [C0095](C0095-classical-timing.md)
obsahuje minimální běhy i návrh opravy; algoritmy samotné jsou správné.

## Úloha15: chyba vynechání malých součinů

Zde číslice zlomků číslujeme **od1 za čárkou**, takže součin u_i v_j má
váhu b^(-i-j). Nechť E je přesný součin minus součet zachovaných členů
s i+j<=n+2, ještě před případným zaokrouhlením výstupu. Všechny členy
jsou nezáporné, a maximum vznikne, když všechny vstupní číslice jsou b-1.
Sečtením konečné aritmeticko-geometrické řady dostaneme pro n>=2
(a po přímém ověření také pro n=1)

```
E_max = (b-1)^2 sum_{s=n+3}^{2n}(2n-s+1)b^-s
      = (n-2)b^(-n-1) - (n-1)b^(-n-2) + b^(-2n).
```

První suma je prázdná pro n<=2. Pro n>=3 je maximum kladné a ostře
menší než `(n-2)b^(-n-1)`, jak uvádí kniha. Pro n=1 má však tištěná
pravá strana záporné znaménko, pro n=2 je nulová a ostrá nerovnost
`0<0` neplatí. [C0096](C0096-truncated-product-small-n.md) doplňuje tyto
případy. Analogická věta pro vynechání i+j>n+3 má nulovou chybu pro
n<=3; zápornou mez pro n<3 nelze použít. Nejde o chybu hlavního
asymptotického závěru. Závěrečné zaokrouhlení může přidat další chybu,
a proto není zahrnuto do E. Bibliografická poznámka o metodě správného
zaokrouhlení Krandicka a Johnsona ještě patří kontextovému auditu.

## Úloha16: krátké dělení

Je-li před novou číslicí `0<=r<v`, pak `0<=rb+u_j<bv`; nový podíl
`floor((rb+u_j)/v)` je číslice a nový zbytek je opět menší než v.
Po každém kroku platí: již přečtený prefix vstupu = v krát prefix
podílu + r. Důkaz začíná nulovými prefixy, končí po n krocích přesným
dělením se zbytkem. Přeznačení kroků S1/S2/S3 na Q1/Q2/Q3 je známé
erratum z30.1.2010, nikoli matematická změna.

## Reprodukce, rozsah a errata

[verify_classical_basic.py](../verify_classical_basic.py) a
[classical-basic.json](../results/classical-basic.json) obsahují čtyři
úspěšné checkpointy:

- 38465 úplných dvojic malých čísel pro A/S/B/C, porovnání a krátké
  dělení;12 přesných rozdělení přenosů;2000 smíšených základů.
- 21529 úplných součinů,3000 dalších násobení se sčítáním a8 stavů tabulky1.
- 3960 běhů MIX:480 pro každý z A,S,C3,C8,C13 a platné prohození S,
  plus1080 pro M; navíc3 konkrétní svědci. Nejde o vyčerpání celého MIX.
- 870 racionálních kontrol uzavřené formule E_max a1069 úplných dvojic
  proti přímému součinu minus zachované členy.

Nezávislým orákulem instrukčního modelu jsou celá čísla Pythonu;
ruční četnosti instrukcí nejsou odvozeny z hodnot čítače modelu.
Při prvním běhu vznikla kolize jména vstupu M a konstanty délky M
v našem assembleru. Opravena přejmenováním vstupu na PM; nejde o
chybu knihy. Oba již úspěšné matematické checkpointy zůstaly zachovány.
Obnovený běh dokončil zbývající bloky s návratovým kódem0.

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` byly
prohledány podle stran i výrazů k přenosům, časování a vynechaným
součinům. Vizuální doklady: all2-prepre str.15–17,37; all2 str.10.
Relevantní opravy: komentář A267(2000), adresování S268(2000), drobné
opravy M268–269(2002/2006), označení Q625(2010), odkaz v odpovědi7
z(6) na(7)(14.5.2026). Žádná nalezená položka neopravuje C0095/C0096.
Poslední fyzický dotisk ani priorita těchto nálezů nejsou ověřeny.
