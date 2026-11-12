# §4.4 A/B: základní převody, MIX a úlohy 1–5, 7, 8, 10, 19

Kontrola 2. listopadu 2026. Původní sazba textu 319–323, zadání
327–329 a odpovědí 635–638 byla vizuálně přečtena. Oddíl má 19 úloh;
errata nahrazují úlohy 9 a 11, ale nepřidávají další číslo. Tento blok
uzavírá devět uvedených úloh. Zbytek §4.4 zůstává otevřený.

`b,B >= 2` označují vstupní a výstupní základ. `floor(x)` je dolní
celá část a `{x}=x-floor(x)` zlomková část. U programů MIX značí
`w=beta^5` kapacitu pěti bajtů, kde beta je počet hodnot bajtu;
binární příklady používají beta 64 nebo 256. Platná nezáporná
velikost slova je menší než w.

## Čtyři metody, strany 319–320

**1a:** eukleidovské dělení `u=Bq+r`, `0<=r<B`, dává nejnižší
číslici r a další úlohu q. Indukcí po počtu dělení je původní
u součtem již vydaných číslic a `B^k` násobku zbylého podílu.
Pro nulu můžeme vydat jedinou číslici 0, jak činí program (1).

**1b:** Hornerovo pravidlo postupně vytváří hodnotu přečteného
prefixu číslic: `v <- b*v + další číslice`. Aritmetika v základu B
mění reprezentaci, nikoli tuto identitu.

**2a:** pro původní zlomek `0<=u<1` po k krocích platí

```text
u = U_-1/B + ... + U_-k/B^k + r_k/B^k,  0 <= r_k < 1.
```

Další číslice je `floor(B*r_k)` a nový zbytek `{B*r_k}`.
Po M číslicích se tedy volba nejbližší hodnoty redukuje na porovnání
`r_M` s 1/2. Při rovnosti je nutné zvolit konvenci pro půlení;
text ji neurčuje jednotně a úloha 3 ji výslovně diskutuje.
Zaokrouhlení může šířit přenos a může dát 1. Největší vstup s m
číslicemi v základu b je `1-b^-m`; k zaokrouhlení na 1 je potřeba
`b^-m <= B^-M/2`, s rovností závislou na konvenci. To vysvětluje
podmínku `b^m >= 2 B^M` na straně 320.

**2b:** od nejnižší vstupní číslice opakujeme `v <- (v+d)/b`.
Po posledním dělení vznikne přesně původní zlomek. Je-li každé
dělení zaokrouhleno s absolutní chybou nejvýše eta a sčítání je
přesné, konečná chyba je nejvýše
`eta*(1+1/b+...+1/b^(m-1)) < eta*b/(b-1)`.
To dokládá upozornění knihy, že zaokrouhlování mezivýsledků se
musí kontrolovat. Přidání přibližné konstanty `B^-M/2` předem
nemá bez další analýzy zaručený účinek přesného zaokrouhlení.

## Smíšené základy, úlohy 1 a 2

Vektor `(a_0,...,a_m)` má váhy `1,b_0,b_0*b_1,...`; poslední
číslice může být neomezená. V cílových základech `B_0,...,B_(M-1)`
provedeme stejnou Hornerovu rekurenci, tentokrát s násobiteli
`b_(m-1),...,b_0`. Násobení číslicového vektoru konstantou k a
přičtení a realizujeme odspodu: začneme přenosem a a pro každou
číslici d vypočteme podíl a zbytek `k*d+carry` při dělení příslušným
B_j. Horní neomezená číslice absorbuje poslední přenos. Invariant
vážené hodnoty je stejný jako u obyčejného sčítání.

Pro úlohu 2 dělíme postupně čísly `B_0,B_1,...`. Vstupní vektor
zůstává v b_j soustavě. Dlouhé dělení začíná nahoře a další sloupec
dělí hodnotu `r*b_j+a_j`; protože `0<=r<divisor` a `a_j<b_j`,
nová podílová číslice je menší než b_j. To dokazuje správnost
obou smíšených algoritmů bez převádění pracovních hodnot do desítkové
soustavy. Zápis posledního „dělení nekonečnem“ v tabulce jen značí
uložení neomezené nejvyšší číslice.

Všechny řádky obou tabulek byly reprodukovány. Výchozí hodnota je
292357 sekund/uncí; výsledek je `8,3,1,2,5` v pořadí tuny,
hundredweights, stones, pounds, ounces. Celkem prošlo dalších 2000
smíšených příkladů proti nezávislému vyhodnocení vážené hodnoty.
Erratum 8. dubna 2002 opravuje pouze index j na J v odpovědi 1.

## Nejkratší přesný výstup, úloha 3

Označme původní toleranci epsilon>0. Po M číslicích má algoritmus
zbytek r a zvětšenou toleranci `e=B^M*epsilon`. Existuje vyhovující
M-místná hodnota právě když `min(r,1-r)<e`; nejbližší dva body
výstupní mřížky jsou právě dolní prefix a prefix zvětšený o `B^-M`.
Test A2 je přesně tato podmínka. První úspěšné M je tedy minimální.
Konec nastane, jakmile `B^-M/2<epsilon`, případně dříve.

Je-li vybráno zaokrouhlení nahoru a poslední číslice je B-1, byl
by zaokrouhlený výsledek násobkem `B^-(M-1)`. Tatáž hodnota by
tedy vyhovovala už předchozí úrovni, což odporuje tomu, že A2 tam
neukončilo výpočet. Proto nevzniká přenos přes více číslic.
Pro M=0 se případně pouze změní U_0 z 0 na 1.

Pokud původní u leží na mřížce `b^-m` a epsilon=`b^-m/2`, žádné
jiné číslo této mřížky nemůže být stejně blízko výstupu: přísná
nerovnost dává jednoznačnou zpětnou rekonstrukci.
Přesná racionální kontrola zahrnula 18900 případů, 266 přesných
půlení a 8710 výstupů s M=0. Kratší délky byly testovány samostatným
orákulem nejbližšího bodu mřížky. Známá oprava 19. února 2011
odstraňuje tečku z prostředního jména Jon L White.

## Konečné rozvoje, úloha 4

Číslo se jmenovatelem `b^m` má konečný rozvoj v základu B právě
když jeho zkrácený jmenovatel dělí nějaké `B^M`. Pro všechny takové
vstupy je tedy nutné a postačující, aby každý prvočíselný dělitel b
dělil B. Nutnost plyne už z `1/p`, kde p dělí b; pro postačitelnost
zvolíme M dost velké pro všechny konečné exponenty prvočísel.
Binární případ je identita `2^-k=5^k/10^k`. Přesná kontrola 2401
dvojic základů souhlasí s důkazem.

## Jednoslovný převod a úlohy 5, 7, 8

Pro `D=10^n<w` a `0<=u<D` dává (2) `wu=Dq+r`. Proto
`D(q+1)/w=u+(D-r)/w` leží v intervalu `[u,u+1)` a program (4)
vydá správných n číslic. Jeho celočíselná smyčka `a <- (10a) mod w`
s výstupem `floor(10a/w)` je přesnou metodou 2a pro a/w.

Odpověď 5 obsahuje nesprávné **„if and only if“**. Pro konstantu
`0<=c<w` je přesná podmínka `c>=D-gcd(w,D)`, nikoli `c>=D-1`.
Obecný důkaz i konkrétní binární příklad jsou v
[C0108-radix-constant.md](C0108-radix-constant.md).

Úloha 7 je správná i na hranici u=w. Pro u=0 je závěr okamžitý;
pro u>0 platí `a*u <= x*u < a*u+u/w <= a*u+1`.
Když `a=1/d` a `u<a*w`, přidaná chyba je menší než a. Zlomková
část a*u je násobkem a a může být nejvýše `1-a`, takže se
nepřekročí další celé číslo. Kontrola zahrnula 77736 přesných případů.

Program odpovědi 8 ovšem selže již na u=10. Jednak `1//10`
znamená dolní aproximaci, jednak `ADD U` používá stále původní
vstup. Podrobnosti a opravený program viz
[C0109-radix-mix-reciprocal.md](C0109-radix-mix-reciprocal.md).
Obě chyby byly izolovány: samotná oprava konstanty dá pro u=10
číslice `[0,10]`, samotné uložení aktuálního vstupu dá `[10]`;
obě opravy dohromady dají `[0,1]`, vždy od nejnižší číslice.

Opravená varianta používá `K=floor(w/10)+1` pro binární w a
`q=floor(u*K/w)`. Z úlohy 7 je q přesné nebo o 1 větší;
záporné `u-10q` se opraví snížením q. Součin 10q se vejde do
slova: `q<=K-1=floor(w/10)` a w není dělitelné 10.
Po první iteraci je aktuální u menší než w/10, takže další oprava
už podle úlohy 7 není potřeba.

Simulace přepsaných instrukcí používá dosavadní interpreter
`mix_float_machine.py`, včetně znamének nul, posunů a přetečení.
Proti celočíselným orákulům prošlo:

- 2510 běhů programu (1), přesná cena `18M+4`;
- 6936 běhů (4) s původními i zobecněnými konstantami, cena `16n+19`;
- 42 očekávaných odmítnutí přetečení v (4);
- 1520 běhů Hornerova programu (6);
- 2510 běhů opravené odpovědi 8, včetně 85 oprav podílu.

Opravený program 8 uchovává původní U a přidává pomocné CURRENT.
Jeho cena je `35M+3+21C`, kde C je počet oprav, nejvýše jedna.
Původní údaj asi 33 cyklů na číslici se vztahuje k neúplné smyčce.
Podmínka pro časovou výhodu (4) proti (1) při n=M je n>=8.
Věta o vedoucích nulách se čte v rozsahu jednoho slova MIX;
u libovolně velkých hypotetických slov sama tato okolnost nestačí.

Program (6) provádí pro m+1 číslic právě m iterací. Následující
věta knihy uvádí m-1: drobný samostatný nález
[C0110-horner-operation-count.md](C0110-horner-operation-count.md).

## Binárně kódované desítkové číslice, tabulka 1 a úlohy 10, 19

BCD zde znamená, že každá desítková číslice d je v jednom čtyřbitovém
poli, tedy celé slovo je polynom číslic se základem 16.
Pro zdvojení přičtení 3 k jednotlivým polím nepřenáší mimo pole,
protože d+3<=12. Nejvyšší bit d+3 je 1 právě pro d>=5.
Zachycené bity h tedy určují opravu `h-(h>>2)`, tj. hodnotu 6
v každém takovém poli. Součet `2*U+h-(h>>2)` má v daném poli
`2d` nebo `2d+6`; s přenosem z nižšího pole právě vytváří
desítkovou číslici i správný přenos. Je nutné ponechat místo pro
případnou novou nejvyšší číslici.

Pro půlení nejprve položíme T=`U>>1`. Lichá číslice vyššího pole
vloží do sousedního nižšího pole hodnotu 8, kde má být 5. Proto
z T extrahujeme nejvyšší bit každého pole, h, a odečteme
`(h>>2)+(h>>3)`, tedy 3 za každý takový přenos. V příslušném
poli už byla alespoň hodnota 8, takže nevzniká nežádoucí výpůjčka.
Nejnižší zahazovaný bit je přesně zbytek po dělení 2.

Všech šest řádků tabulky pro 369 souhlasí. Prošlo 12000 případů
zdvojení a půlení, včetně čísel s až 24 číslicemi.

V úloze 19 nechť d postupně nabývá hodnot 1,2,4. V každém páru
d-místných bloků je hodnota `16^d*A+B`; požadujeme `10^d*A+B`.
Maska vybere `16^d*A`, a proto odečteme jeho násobek
`c=1-10^d/16^d`. Uvedené masky `F0F0F0F0`, `FF00FF00`,
`FFFF0000` vybírají právě tyto bloky. Dělení vybraného slova
`16^d` je přesné. Sloučený blok je nejvýše `10^(2d)-1`, tedy
se vejde do svého 2d-místného pole a nezasáhne jiné bloky.
Po třetí operaci zbývá celý desítkový vstup jako obyčejné binární
celé číslo. Kontrola proti parsování desítkového řetězce prošla
pro 15006 osmimístných vstupů. Oprava 2005 pouze mění znak
bitového AND a doplněk 2013 úlohu doporučuje.

## Evidence a zbývající práce

`verify_radix_basic.py` má pět dokončených checkpointů; relace 87610
skončila exit 0. Výsledky jsou v `results/radix-basic.json`, log a
přepis instrukcí jsou uloženy vedle. Testy doplňují výše uvedené
obecné důkazy a bez nového důvodu se neopakují.

Všechny čtyři vrstvy errat byly prohledány podle stran, čísla
úlohy i instrukcí. C0108–C0110 v nich nebyly nalezeny. Nejnovější
fyzický dotisk, priorita ani odměna ověřeny nejsou; nic nebylo
odesláno. Další bloky: záporný základ 6, aktualizovaná 9, ruční
převody 11/12, tisk 13, rychlé metody 14–16 a floating point 17/18.
