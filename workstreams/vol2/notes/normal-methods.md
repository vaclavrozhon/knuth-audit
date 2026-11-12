# §3.4.1 C: normální generátory P, M, F, R

Stav 2026-11-01. Sazba122–132,139,140,586–588 vizuálně přečtena.
Ověřeny matematické konstrukce P/M/F/R, tabulky128/131 a úlohy10–12,
20–21. Historické atribuce mimo níže uvedený Brentův zdroj, doplněk
Leva1992 a metoda Wallace z úlohy31 se dokončí v kontextovém bloku.
Čísla počítá `verify_normal_methods.py`, výsledky jsou v
`results/normal-methods.json`; úspěšné bloky se při `--resume` neopakují.

## 1. Polární transformace P a obecné odmítání

Po přijetí bodu (V1,V2) v jednotkovém kruhu má jeho úhel Theta
rovnoměrné rozdělení na[0,2pi) a je nezávislý na S=V1²+V2².
Plocha kruhu poloměru sqrt(s) je pi*s, takže S je rovnoměrné na[0,1].
Nový poloměr R=sqrt(−2ln S) má CDF1−exp(−r²/2), r>=0.
Hustota ve dvojici (R,Theta) je r*exp(−r²/2)/(2pi). Jacobián
polárních souřadnic je r, proto kartézská hustota je
exp(−(x²+y²)/2)/(2pi), součin dvou standardních normálních hustot.
Tím je doložena i nezávislost obou výstupů, nikoli jen jejich marginály.

Pravděpodobnost přijetí pi/4 a geometrické momenty jsou ověřeny
v `distributions-basic.md`,§3. Známé opravy na str.122:
22.12.1998 přiřazovací šipky,7.2.2000 zvláštní S=0,30.9.2003
SD0.590. Nulový případ nemění spojitý zákon, ale zabrání dělení nulou
u konečné mřížky; přesná spojitá normalita se pro konečný vstup neslibuje.

Obecné odmítání: pro hustoty f,g a konečné c s f<=c*g navrhneme X z g
a přijmeme s pravděpodobností f(X)/(c*g(X)). Společná hmotnost přijetí
a X v množině B je integral_B f/c; celková pravděpodobnost přijetí1/c.
Podmíněním tedy dostaneme f. Kde g=0, je také f=0 a podíl lze libovolně
dodefinovat. Počet pokusů má střední hodnotu c. Levné dolní/horní meze
akceptačního podílu mohou rozhodnout před jeho přesným výpočtem.

## 2. Směs obdélníků, klínů a ocasu M; úlohy10,11

Zde f(x)=sqrt(2/pi)exp(−x²/2), x>=0, je hustota absolutní hodnoty
standardní normální veličiny; F je její integrál od0. Položme
h=1/5 a s_j=(j−1)/5,1<=j<=16. Obdélník j má hmotnost
p_j=h*f(s_j+h), klín j má hmotnost
p_(j+15)=F(s_j+h)−F(s_j)−p_j, j1..15. Ocas má p31=1−F(3)
a pomocná barva32 má p32=0. Tyto nezáporné hmotnosti dávají součet1.
Každá komponenta je normalizovaná: klín má hustotu

```
g_j(x) = (f(x)−f(s_j+h))/p_(j+15),  s_j<=x<=s_j+h.    (1)
```

Součet obdélníků je0.91830983477..., ocas0.00269979606...;
komentáře92 procent a jednou za370 tedy souhlasí. Graf9 po opravě
7.2.2000 ukazuje správné intervaly a výšky. Vyobrazená plocha je p_j,
nikoli plocha normalizované hustoty g_j, která je1.

Algoritmus L: seřazení dvou nezávislých rovnoměrných čísel dá konstantní
hustotu2 v trojúhelníku0<=u<=v<=1. Předpokládáme h>0,b>0 a
a−b(x−s)/h<=g(x)<=b−b(x−s)/h. Přijetí v<=u+g(s+hu)/b
má pro pevné u délku g(s+hu)/b. Marginalizace a změna x=s+hu tak
vrací hustotu g. Test v<=a/b je bezpečný dolní odhad téže hranice.

Pro j<=5 je (1) konkávní, pro j>=6 konvexní, protože f''=(x²−1)f.
V konkávním případě horní mez dává tečna v pravém konci, spodní
rovnoběžka prochází levým koncem: a_j=g_j(s_j),
b_j=−h*g_j'(s_j+h). V konvexním případě horní mez je sečna:
b_j=g_j(s_j). Spodní tečna má stejnou směrnici, tedy pro jediný
x_j v(s_j,s_j+h) s g_j'(x_j)=−b_j/h klademe
a_j=g_j(x_j)+(x_j−s_j)b_j/h. Existenci a jednoznačnost uvnitř
tohoto intervalu dává přísná konvexita a věta o střední hodnotě.
Změna formulace30.6.2024 nevyžaduje hledat jiné kořeny mimo tento interval.

Potom D_(j+15)=a_j/b_j. Přímé zjednodušení dává

```
g_j(X)/b_j = E_(j+15)*(exp(((s_j+h)^2−X²)/2)−1),
E_(j+15)=25/j                         pro j<=5,
E_(j+15)=1/(exp((2j−1)/50)−1)         pro j>=6.          (2)
```

Proto M4–M6 implementují právě L. Po odmítnutí se vracíme do stejného
klínu, takže se nezmění směšovací hmotnost. Oprava2.12.1999 mění
komentář M3 na16<=j<=31; kód M2 původně rozhodoval správně.

Aliasová konstrukce používá logické barvy1..32, poté barvu32 přejmenuje
na index0. Oproti doslovným nulovým indexům odpovědi7 je zde nutné
číst P/Y s tímto přejmenováním. Větve s aliasem vždy míří na obdélník.
Je-li dárcem obdélník k, podmíněné f v[P_j,1) se transformuje na
rovnoměrné X v[(k−1)/5,k/5) pomocí
Z_j=1/(5(1−P_j)), Y_j=k/5−Z_j. Vlastní obdélník j používá
Q_j=1/(5P_j), X=s_j+f*Q_j. P9=1 znamená, že Y9/Z9 se nepoužívají;
jejich formální dělení nulou se proto vůbec nemá provádět. Tabulka
po známé opravě28.7.2000 nahrazuje jejich nuly pomlčkou.

Úloha11: hustota návrhu na[3,infinity) je
g(x)=exp(9/2)*x*exp(−x²/2). Její CDF je1−exp(−(x²−9)/2), takže
X=sqrt(9−2ln V) má tento zákon pro0<V<1. Přijetí s podílem3/X
vrací požadovaný normální ocas. M8 proto testuje U*X>=3.
Pravděpodobnost odmítnutí0.08622910... je přibližně jedna dvanáctina.
Při implementaci s možností přesného V=0 je vhodné nový V vylosovat;
spojitý důkaz je tvrzení skoro jistě, kde tato událost má míru0.
M9 použije nezávislý znaménkový bit a dá celé normální rozdělení.

Všech226 tištěných čísel tabulky128 a pomocných hodnot586 bylo
certifikováno90cifernou intervalovou aritmetikou. Integrály F mají
nezávislé uzavření střídavou Taylorovou řadou s přesným racionálním
zbytkem; polohy tečen jsou uzavřeny230 kroky monotónního půlení.
Po zapracování oprav Y4,Y5,Z4,Z5 a pomlček Y9/Z9 není žádný nesoulad.
Přímý součet všech aliasových větví nezávisle kontroluje původní p_j.

## 3. Liché/sudé délky F, Brent a úloha12

Pro pevné h v[0,1] losujme V1,V2,... a zastavme při prvním vzestupu
V_K>V_(K−1), s V0=h. K znamená počet porovnávacích losování.
Pr(K>k)=h^k/k!, protože k bodů musí ležet pod h v jediném z k!
pořadí. Odečtením sousedních ocasů a součtem přes lichá k dostaneme
Pr(K liché)=exp(−h). Dále E(K)=sum_(k>=0)h^k/k!=exp(h).
Tím je odmítací metoda pro hustotu úměrnou exp(−h(x)) dokázána.

Položme S(x)=sqrt(2/pi)*integral_x^infinity exp(−t²/2)dt a definujme
a_j rovností S(a_j)=2^(−j), a0=0; d_j=a_j−a_(j−1).
První nulový bit vybírá interval[a_(j−1),a_j) s hmotností2^(−j).
Zbývající bity jsou nezávislé rovnoměrné číslo v tomto intervalu.
Po výběru j se odmítáním s
h_j(x)=(x²−a_(j−1)²)/2 získá podmíněná normální hustota.

Úloha12: Millsův integrál
M(x)=exp(x²/2)*integral_x^infinity exp(−t²/2)dt
se rovná integral_0^infinity exp(−xt−t²/2)dt, a proto přísně klesá
pro x>=0. Pro y²=a_(j−1)²+2ln2 je S(y)<S(a_(j−1))/2=2^(−j).
Tedy a_j<y a a_j²−a_(j−1)²<2ln2. V celém j-tém intervalu tak
0<=h_j<ln2<1. Známá oprava19.10.1999 obrací znaménko v nápovědě;
tištěný důkaz586 a tento přímý integrální důkaz jsou v souladu.

Původní F4 při odmítnutí znovu používal podmíněný porovnávací vstup.
Oprava30.9.2003 před návratem do F3 losuje nové nezávislé U; tento
krok je potřebný. Znaménko a j zůstávají zachovány. Konečný bitový
algoritmus má v posledních intervalech omezenou přesnost a atom na
a_t, celkové hmotnosti2^(−t); úvod algoritmu výslovně říká přibližnou
přesnost. Nekonečný ideální model má přesný normální zákon.

Označme A_j pravděpodobnost přijetí jednoho návrhu v intervalu a
B_j očekávaný počet porovnávacích losování v jednom pokusu:

```
A_j=(1/d_j) integral_[a_(j−1),a_j] exp(−h_j(x)) dx,
B_j=(1/d_j) integral_[a_(j−1),a_j] exp( h_j(x)) dx.
```

V algoritmu F stojí první výběr celé veličiny jedno U, další návrh
po každém neúspěchu další U. Obnovovací rovnice dává celkový průměr
sum_j 2^(−j)*(B_j+1)/A_j=2.53946624..., souhlas s2.53947.

Brent při posledním vzestupu recykluje W=(V_K−V_(K−1))/(1−V_(K−1)).
Podmíněně na celou historii před posledním losováním je W rovnoměrné
a nezávislé na přijatém X i K. Lze je proto použít pro další návrh,
i po úspěchu pro znaménko a interval dalšího výsledku. Asymptotický
počet nových U na výsledek je

```
C = sum_(j>=1) 2^(−j) B_j/A_j.                     (3)
```

**C0055:** str.130 uvádí1.37446; správné zaokrouhlení je1.37746.
Náš intervalový certifikát dává

```
1.377460505889 < C < 1.377460505893.
```

Prvních40 kvantilů je uzavřeno dyadickými intervaly a znaménky
nezávisle vyčíslené Taylorovy CDF. Integrály B_j používají pozitivní
mocninnou řadu exp(a*d*t+d²*t²/2) a přesné integrály jejích polynomů;
30 členů má zbytek nejvýše2/31!. Protože A_j>1/2 a B_j<2, celý
ocas (3) za40 je menší než4*2^(−40). Nezávislé vyhodnocení přes erfi
souhlasí s intervalem částečného součtu. To není závěr ze simulace.

[Brentův původní článek](https://maths-people.anu.edu.au/brent/pd/rpb023.pdf)
má na str.705 stejný překlep u rovnice(4), ale přímo v komentáři
Fortranu na téže straně správně1.37746. Přečtena metoda a analýza704–705,
str.705 vizuálně; celý Fortran nebyl samostatně auditován. Doklad a
metadata jsou v `sources/brent-1974-normal.*`. Knižní odkaz704–705
obsahuje potřebnou analýzu, přestože celý článek dobíhá na706;
kratší odkaz proto neoznačujeme za další chybu.

## 4. Poměr rovnoměrných veličin R; úlohy20,21

Pro nezápornou integrabilní g s nenulovým integrálem uvažujme oblast
u>0,u²<=g(v/u). Substituce v=xu má Jacobián u. Plocha nad x v dx
je integral_0^sqrt(g(x)) u du dx=g(x)dx/2. Rovnoměrný bod oblasti
proto má poměr v/u s hustotou g(x)/integral g.
Pro g(x)=exp(−x²/2) dostaneme normální zákon a hranici
|v|<=2u*sqrt(−ln u),0<u<=1. Maximum horní hranice je sqrt(2/e),
dosažené při u=exp(−1/2), takže obdélník R1 je správný.

Z nerovností ln z<=z−1 a ln z>=1−1/z při z=c*u dostaneme obě
meze(28). Proto je R2 bezpečné okamžité přijetí a R3 bezpečné
okamžité odmítnutí; R4 rozhoduje přesně. Míry hranic jsou nulové.
Tvrzení v popisku obr.13 nelze chápat jako doslovnou normalitu
eukleidovských délek paprsků: rozhodující je poměr rovnoměrného bodu
a plošný Jacobián u, jak je správně odvozeno v textu.

Písmeno A označuje plochu přijetí, R obdélníku, I plochu rychlého
přijetí R2 a E plochu rychlého odmítnutí R3. Pokus se přijme s podílem
A/R, proto je očekávaný počet provedení R1 roven R/A. Každá množina
plochy B navštívená v pokusu přispěje B/A návštěvami na výsledek.
Tím přímo dostaneme všechny čtyři varianty tabulky131 a odpověď20.

Máme R=sqrt(8/e), A=sqrt(pi/2). Pro R2 s libovolným c>exp(−1)
položme a=4(1+ln c), b=4c. Plocha je
I=2 integral_0^(a/b) u*sqrt(a−bu)du=(8/15)a^(5/2)/b².
Pro c<=exp(−1) je I=0. Logaritmická derivace pro z=ln c je
5/(2(1+z))−2, takže jediné globální maximum nastane při z=1/4.
Jeho hodnota je(5/6)sqrt(5/e)=1.13020...; geometrická oblast leží
uvnitř obdélníku díky již dokázané dolní mezi. Obě primitivní funkce
pro sqrt(bu±au²) na588 byly také ověřeny. Opravy3.2.2005 přidávají
chybějící a v první primitivní funkci587 a faktory2 v plochách I/E.

Pro skutečný R3, c=exp(1.35), vychází E=0.29410413894... . Všech16
čísel tabulky131 a4 hodnoty ploch byly certifikovány intervaly;
nezávislá numerická kvadratura E souhlasí. Globální optimálnost R3
text prezentuje jako výsledek výpočetních experimentů; zde ji z malé
mřížky parametrů neprohlašujeme za nově dokázanou. Požadované globální
maximum R2 je dokázáno výše.

## 5. C0054: obecné E po opravě2005 stále někdy vynechává oblast

Odpověď21 parametrizuje obecný test jako
X²>=4exp(x−1)/U−4x a uvádí

```
E=2 integral_0^r (H−sqrt(bu−au²)) du,
H=sqrt(2/e), a=4x, b=4exp(x−1),
r=(exp(x)−sqrt(exp(2x)−2e*x))/(2e*x).                (4)
```

Faktor2 už zahrnuje opravu2005. Při x=1 však hranice splňuje
v²=4u(1−u), takže je symetrická i podél u=1/2. Průsečíky s v=H
jsou r=(1−sqrt(1−2/e))/2 a1−r, oba uvnitř(0,1). Odmítací oblast
má stejně velkou pravou a levou část. (4) počítá jen levou část,
a to v horní i dolní polorovině. Přesně tedy

```
E_podle_(4) = 0.121847890228149...,
E_skutečné  = 0.243695780456298... = 2*E_podle_(4).
```

Obecný správný vzorec je
E=2 integral_0^1 max(0,H−sqrt(bu−au²))du.
Alternativou je omezit(4) například na x<=0, kde druhá část nevzniká.
Knižní praktická volba x=−0.35 splňuje tuto podmínku, proto algoritmus
R a jeho vytištěná číselná tabulka zůstávají správné. Tento nález
se týká obecnosti pomocného vzorce, nikoli již opravené svislé symetrie.

## 6. Kontrola zdrojů a další rozsah

C0054: str.588, souborová600; C0055: str.130, souborová142.
Třetí vydání/první dotisk9/1997. Přečteny související listy7,8,32,33
`all2-prepre` a10 `all2` (snímky `normal-errata-*`). Prohledány všechny
čtyři řady `all2-prepre`, `all2-pre`, `all2`, `err2` i aktuální err2
TeX, podle stran i hesel Brent,1.37446,1.37746,exterior,29410.
Žádná odpovídající oprava C0054/C0055 nebyla nalezena. Nejnovější
fyzický dotisk ani prvenství nejsou ověřeny; hlášení zůstávají neodeslaná.
