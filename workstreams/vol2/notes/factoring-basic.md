# §4.5.4: základní dělení, síto a šest úloh

Kontrola 3. listopadu 2026. Uzavírá text algoritmu A na 380–381
a úlohy 1, 2, 3, 6, 8 a 29; celý oddíl zůstává otevřen.
Všechny uvedené knižní strany i příslušné historické opravy byly
přečteny v původní sazbě. Rozpis ostatních oprav a 47 zadání
je v [inventáři](factoring-inventory.md).

## Dělení A a úlohy 1–3

Vstup N je kladné celé číslo. Posloupnost zkušebních dělitelů
d_0=2<d_1<... obsahuje každé prvočíslo nejvýše sqrt(N)
a alespoň jeden člen nejméně sqrt(N). Proměnná n je dosud
nerozložený podíl a k index právě zkoušeného dělitele d_k.
Invariant před dělením: součin vypsaných faktorů krát n je N
a n nemá prvočíselného dělitele menšího než d_k.

Pokud d_k dělí n, musí být prvočíslem: jinak by jeho menší
prvočíselný faktor dělil n, což invariant zakazuje.
To dokazuje úlohu 1 a zachování invariantu po vydělení.
Při nenulovém zbytku pišme n=q*d_k+r, 0<r<d_k.
Pokud q<=d_k, je n prvočíslem. Jinak by jeho nejmenší
prvočíselný faktor p byl větší než d_k, a tedy

```
n >= p^2 >= (d_k+1)^2 > d_k^2+d_k-1 >= q*d_k+r.
```

Pokud q>d_k, lze přejít k dalšímu zkušebnímu děliteli:
d_k<sqrt(n)<=sqrt(N), takže potřebné další prvočíslo
v tabulce existuje. Nalezený dělitel n zmenší; index roste
jen do konečného místa s d_k>=sqrt(N). Tím je dokázáno
ukončení, správnost i to, že se složené členy seznamu nevypisují.

Je-li t počet prvočíselných faktorů s opakováním a k konečný
index, počet dělení A3 je přesně t+k. Při konci přes A2 je
t úspěšných dělení a k neúspěšných; při konci přes A7 je
t-1 úspěšných a k+1 neúspěšných. Knižní vyjádření času
pomocí max(p_(t-1),sqrt(p_t)) je orientační popis délky
prohledávaného seznamu, nikoli uniformní asymptotická rovnost.
Například N=2^t potřebuje t dělení, ačkoli uvedené maximum
je pro t>=2 konstantní. Kniha zde říká „roughly“, přesnou
větu o celkové složitosti z toho nevyvozujeme.

V úloze 2 je N>=3. Bez A2 vznikne falešný poslední faktor 1
právě tehdy, když se největší prvočíselný faktor opakuje.
Poslední dvě shodné hodnoty se obě úspěšně vydělí; po n=1
další nenulový zbytek vyvolá A7. Pokud poslední faktor p
není opakován, dosáhne se A7 už s n=p: po případném odstranění
posledního menšího faktoru q<p se znovu zkouší q; buď tehdy
q^2>=p a končíme, nebo později překročíme sqrt(p), stále
před p. Pro prvočíselné N>=3 platí totéž od d_0=2.
Nejmenší protipříklad je N=4.

Počítání zbytkových tříd vysvětluje zrychlení seznamů:
po 2 a 3 zbývají dvě třídy modulo 6, tj. třetina celých čísel.
Vynechání násobků 5 odstraní dvě z deseti dosavadních tříd
modulo 30, tj. 20 procent. Další prvočíslo 7 odstraní
sedminu, přibližně 14 procent. Jde o asymptotické hustoty,
nikoli přesné počty na libovolném krátkém intervalu.

Tabulka 168 prvočísel do 997 se zarážkou 1000 stačí pro
N<10^6 (a také N=10^6). Příklady:
25852=2*2*23*281 potřebuje 12 dělení;
prvočíslo 25849 potřebuje 38 dělení.

Pro úlohu 3 nechť P je součin těchto 168 prvočísel.
Složené n v intervalu 1000<=n<=10^6 má prvočíselný faktor
nejvýše 1000, a proto gcd(n,P)>1. Prvočíslo v tomto intervalu
není faktorem P, a proto má gcd rovno 1.
P má přesně 416 číslic, začíná 19590 a končí 5910.

Poznámku o rychlosti lze realizovat v konkrétním slovním modelu:
při základu 2^30 se n vejde do jednoho slova a P do 47 slov.
První zbytek P mod n tedy vyžaduje nejvýše 47 dělení
dvouslovného čísla jednoslovným; následný Euclid nejvýše
29 dalších dělení podle již ověřené Fibonacciho meze.
To je méně než 168 zkušebních dělení. Není to časový benchmark
ani tvrzení o každém procesoru.

## Kvadratické zbytky, úloha 6

Nechť p je liché prvočíslo a N nenulový zbytek modulo p.
Kvadratický zbytek znamená hodnotu y^2 pro nějaké y modulo p.
Rovnici x^2-y^2=N přepíšeme na (x-y)(x+y)=N.
Pro každé nenulové v=x+y je jednoznačně u=x-y=N/v.
Protože 2 je invertibilní, x=(u+v)/2 a y=(v-u)/2 jsou
jednoznačné. Počet dvojic (x,y) je tedy p-1.

Pro každé x s nenulovým y existují právě dvě možnosti y a -y.
Výjimku tvoří y=0: takových x jsou dvě, pokud je N kvadratický
zbytek, jinak žádné. Počet různých přípustných x je proto
(p+1)/2, respektive (p-1)/2. To je celý knižní výsledek.

## Síto S, úloha 8

Pro obecný celočíselný horní práh N vezměme M=floor(N/2).
Index k v rozsahu 1<=k<M představuje liché číslo 2k+1<N.
Předem ukončíme výpočet pro N<=3. Tato podmínka v knize
chybí i po známých opravách 2001: nový [C0147](C0147-sieve-empty-range.md).
Původní opravy mění horní index pole a ostré meze;
jejich význam nepřičítáme novému nálezu.

Proměnné j,p,q splňují p=2j+1 a q=(p^2-1)/2=2j+2j^2.
Značení indexů q,q+p,q+2p,... tedy škrtá p^2,p(p+2),p(p+4),...
Aktualizace j'=j+1,p'=p+2,q'=q+2p'-2 zachová invariant.
Každé složené liché a<N má nejmenší prvočíselný faktor
p<=sqrt(a), který byl navštíven dříve, a je jeho lichým
násobkem nejméně p^2. Proto bylo označeno. Prvočíslo se
neoznačí nikdy; výpis přesně odpovídá požadavku.

Jakmile q>=M, další liché kandidáty už nelze použít k vyškrtnutí
žádného nového čísla v poli: jejich čtverce jsou příliš velké.
Lze tedy jen vypsat zbývající neoznačené hodnoty bez další
údržby p,q. To dokazuje navrženou rychlou variantu.

Historická atribuce I.13 odpovídá přímému překladu Nikomacha
z roku 1926, str.204–205. Výklad, zda původní postup vynechává
složené základy, je však nejistý i podle poznámky vydavatelů.
Rozdíl mezi Theta(N ln N) a Theta(N ln ln N) je rozebrán
v [C0149](C0149-nicomachus-sieve-cost.md), pouze candidate.
Řecké rukopisy nebyly kontrolovány.

## Mertensův součet a konstanta

Pišme ln pro přirozený logaritmus, zeta(s)=sum_(n>=1)n^(-s)
pro s>1, gamma pro Eulerovu konstantu a mu pro Möbiovu funkci:
mu(n)=0, má-li n čtvercový prvočíselný faktor, jinak (-1)^k
pro součin k různých prvočísel. Knižní konstanta B je

```
B = gamma + sum_(k>=2) mu(k) ln(zeta(k))/k.
```

Krátké vlastní odvození existence konstanty:
označme theta(x)=sum_(p<=x)ln p přes prvočísla.
Součin prvočísel m<p<=2m dělí binom(2m,m)<=4^m;
sečtením po dyadických intervalech plyne theta(x)=O(x).
Legendreův součet pro faktoriál pak dává

```
ln(n!) = sum_(p,k>=1) floor(n/p^k) ln p
       = n sum_(p<=n) ln(p)/p + O(n).
```

Chyba první mocniny je nejvýše theta(n); vyšší mocniny jsou
nejvýše n sum_p ln(p)/(p(p-1))=O(n).
Z ln(n!)=n ln n+O(n) plyne A(x):=sum_(p<=x)ln(p)/p=ln x+O(1).
Částečným sčítáním je potom sum_(p<=x)1/p=ln ln x+B+O(1/ln x):
konstantní člen vzniká konvergentním integrálem
(A(t)-ln t)/(t ln^2 t), jehož ocas má velikost O(1/ln x).

Eulerův součin a Möbiova inverze pro s>1 dávají
P(s):=sum_p p^(-s)=sum_(k>=1)mu(k)ln(zeta(ks))/k.
Pro s=1+epsilon, epsilon->0+, je proto

```
P(1+epsilon) = ln(1/epsilon)
            + sum_(k>=2) mu(k)ln(zeta(k))/k + o(1).
```

Na druhou stranu částečné sčítání již dokázaného
prvočíselného harmonického součtu, po substituci u=epsilon ln t,
dává P(1+epsilon)=ln(1/epsilon)-gamma+B+o(1);
zde integral_0^infinity exp(-u)ln(u)du=-gamma.
Porovnání obou konstant dokazuje uvedenou řadu.

Silnější chyba O((ln x)^(-10000)) na659 vyplývá z
prvočíselné věty (3) na382 s chybou
R(x)=O(x exp(-A sqrt(ln x))), A>0.
Částečné sčítání mění její ocas na
R(x)/x-integral_x^infinity R(t)/t^2 dt,
tedy O((sqrt(ln x)+1)exp(-A sqrt(ln x))).
Ten je menší než libovolná pevná záporná mocnina ln x.
Nahrazení p<=x ostrým p<x přidá nejvýše 1/x.
To je vlastní dedukce z (3); samotná hluboká prvočíselná
věta je externí a širší kontext382 zůstává na řadě.

Numerická certifikace používá intervalovou aritmetiku Arb
s 90 desetinnými místy a 220 členy. Pro k>=2 platí
zeta(k)-1<=2^(-k)(1+2/(k-1)) a ln zeta(k)<=zeta(k)-1,
takže absolutní ocas po K je nejvýše
(1+2/K)2^(-K)/(K+1). Výsledný interval leží celý v buňce
zaokrouhlení pro všech 40 vytištěných míst:

```
0.2614972128476427837554268386086958590516
```

Původní Mertensův článek 46–54 odvozuje součet, konstantu
a tuto Möbiovu řadu. Bibliografický údaj v knize je chybný:
Crelle78, nikoli76; viz [C0148](C0148-mertens-volume.md).

## Hladká čísla, úloha 29

Nechť p_1<...<p_m jsou prvočísla a r=floor(ln n/ln p_m).
Číslo je zde hladké, jestliže všechny jeho prvočíselné faktory
leží v této zvolené sadě. Každá nezáporná celočíselná m-tice
(e_1,...,e_m) se součtem nejvýše r dává díky jednoznačnosti
rozkladu jiné číslo p_1^e_1...p_m^e_m<=p_m^r<=n.
Doplnění pomocné souřadnice do součtu r dává počet
binom(m+r,r)=product_(j=1)^r (m+j)/j >= m^r/r!.
Pro r=0 se započítává číslo1. Známé erratum2001 správně
mění „equation“ na „inequality“.

Parentetické odkazy se týkají ostřejších výsledků:
de Bruijnův originál začíná239, kniha uvádí240–247.
Hlavní věty1 a2 jsou právě na240; proto tento rozdíl
nepovažujeme sám o sobě za prokázanou bibliografickou chybu.
Přečteny první dvě strany239–240 a poslední247, ne celý
důkaz. Halberstam1970,102–107 potvrzen metadaty vydavatele,
plný článek dostupný jen předplatitelům; nebyl přečten.
Žádný z těchto ostřejších odhadů nepotřebujeme pro vlastní
úplný důkaz jednoduché úlohy29.

## Reprodukovatelné kontroly

`verify_factoring_basic.py` a `results/factoring-basic.json`:
nezávislé orákulum rozkladu vzniká sítem nejmenších
prvočíselných faktorů, nikoli algoritmem A.

- A: 50 000 vstupů pro každý ze čtyř seznamů dělitelů,
  celkem 200 000 kontrol, invarianty a přesná rovnost t+k.
- Vynechané A2: 49 998 vstupů N>=3, přesně popsaná podmínka selhání.
- P: 999 001 gcd kontrol a 5992 vstupů u horní meze tabulky.
- S: 4095 prahů oběma opravenými variantami; 4093 s pouhými
  známými erraty a přesný nový protipříklad N=2.
- Úloha6: 1134 nenulových zbytkových tříd pro prvočísla do101.
- Úloha29: 24 576 celočíselných mezí, bez logaritmického zaokrouhlování.
- Mertens: rigorózní sevření všech 40 zaokrouhlených číslic.

První běh selhal až na naší mylné konvenci poslední číslice:
vytištěná konstanta je zaokrouhlena, ne useknuta.
Prvních pět úspěšných checkpointů bylo uloženo a znovu
nespouštěno; opravený šestý prošel v obnoveném běhu
PID1255386, session79047, exit0. Není to chyba knihy.
Metadata zdrojů a přesný rozsah četby: `sources/factoring-basic.json`.
