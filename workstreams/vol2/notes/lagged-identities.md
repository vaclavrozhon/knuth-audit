# §3.2.2-23,30–33: periody a identity zpožděných generátorů

Kontrola 1. listopadu 2026. Zadání str.39–40, odpovědi
[556](../images/vol2-p556.png), [557](../images/vol2-p557.png),
[558](../images/vol2-p558.png). Všechny relevantní vrstvy errat
prověřeny; u 30 je známé doplnění označení (a) z 28.9.2002,
ne změna matematického tvrzení. Nová chyba v těchto pěti úlohách nenalezena.

Pro řád k a celočíselné koeficienty a_j píšeme
f(x)=x^k-a_1x^(k-1)-...-a_k. Předpokládáme, že f modulo 2 je
primitivní, tedy jeho kořen má řád M=2^k-1 v tělese s 2^k prvky.
Počáteční hodnoty rekurence nejsou všechny sudé. Zápis modulo (f,2^e)
znamená dělení monickým f a redukci všech koeficientů modulo 2^e.
I označuje identitu matice, u polynomů ji zapisujeme jako 1.

## Úloha 30(a): přesná podmínka růstu

Každý nenulový počáteční vektor modulo 2 je cyklický: jeho prvních k
posunů tvoří bázi. Proto modulo všech 2^e má periodu rovnou řádu x
modulo (f,2^e), jak také plyne z [úlohy 11(e)](period-lifting.md).
Perioda může při zvýšení e nejvýše zdvojnásobit. Zvedací věta 11(c)
ukazuje, že má tvar 2^(e-1)M pro všechna e právě tehdy, je-li modulo 8
rovna 4M, tedy x^(2M)!=1 modulo (f,8).

Položme u=x^M. Protože u=1 modulo 2, lze modulo 8 psát u=1+2t.
Pak u²=1+4(t+t²). Zbytky t modulo 2 leží v tělese, a tedy
u²=1 modulo 8 právě když t(t+1)=0 modulo 2, tj. t je 0 nebo 1.
To je ekvivalentní u=1 nebo -1 modulo 4. Pro plný růst proto potřebujeme
vyloučit obě znaménka, nikoli pouze u=1.

Rozdělme f na sudou a lichou část: f(x)=A(x²)+xB(x²), kde A a B
jsou celočíselné polynomy. V tělese modulo (f,2) platí
A(x)²=xB(x)². Odmocňování je tam jednoznačné a x^(2^k)=x,
takže A(x)=x^(2^(k-1))B(x) modulo 2. Umocněním se kongruence
zvedne na A(x)²=x^(2^k)B(x)² modulo (f,4).
B je nenulový modulo 2 a má stupeň <k, tedy je invertibilní i modulo 4.
Jinak by f bylo čtvercem polynomu modulo 2 (pro k=1 je B=1).

Nyní první výjimečná identita v zadání,

```
f(x)²+f(-x)² = 2 f(x²)             modulo 8,
```

je ekvivalentní A(x)²+xB(x)²=f(x) modulo 4. Rozdíl má stupeň <k,
takže ekvivalentně mizí modulo (f,4). Po dosazení předchozí rovnosti
a vydělení jednotkou xB(x)² dostaneme x^M=-1 modulo (f,4).
Obdobně druhá výjimečná identita

```
f(x)²+f(-x)² = 2(-1)^k f(-x²)      modulo 8
```

vede po oddělení sudých a lichých členů k x^M=1 modulo (f,4).
Úloha proto správně vyžaduje, aby neplatila ani jedna identita.
Argument nevychází z náhodných seedů nebo empirické délky cyklu.

Vlastní konečná kontrola prošla všech **630** primitivních modulo-2
rekurencí stupně k<=6 s koeficienty a_j z {0,1,2,3}, včetně všech
jejich zvednutí v tomto rozsahu. Obě identity byly spočítány obyčejnou
konvolucí celočíselných koeficientů a porovnány s polynomickou mocninou
modulo 4 i s přímými cykly modulo 8, celkem **120544 stavů**.

## Úloha 30(b) a tabulka: proč trojčleny stupně >2 vyhovují

Důkaz funguje pro monický trojčlen s libovolnými lichými koeficienty
u x^l a 1. Označme c_j koeficient x^j a c_k=1. První výjimečná
identita vyžaduje pro každý m

```
sum_(i<j, i+j=2m) c_i c_j = c_m(c_m-1)/2       modulo 2.
```

Je-li l sudé, zvolme 2m=l. Levá strana je c_0 c_l lichá, ale
c_m=0, spor. Proto l je liché. Je-li k liché, 2m=k+l obdobně
vynutí nenulový koeficient mezi l a k, spor. Proto k je sudé.
Nakonec 2m=k vynutí m=l, tedy k=2l. Pak modulo 2 je
f=x^(2l)+x^l+1, a tedy f dělí x^(3l)-1. Pro k=2l>2 však
3l<2^(2l)-1, což vylučuje primitivitu. Stejný argument platí
pro monický násobek f(-x), takže druhá výjimečná identita také neplatí.

Tím je pokryta nejen kladná verze v zadání, ale i obě znaménka
skutečných generátorů. Přímé cykly modulo 8 potvrdily všech **72**
podepsaných primitivních trojčlenů stupňů 3–12. Pro skutečný řád 55
byly obě varianty s koeficientem +1 či -1 u zpoždění 24 ověřeny
polynomickým umocněním: řád modulo 8 je přesně 4(2^55-1).
Primitivita všech dvanácti řádků tabulky je v
[poznámce o polynomech](primitive-polynomials.md).

Primární článek R. P. Brenta, *On the periods of generalized Fibonacci
recurrences*, Math. Comp.63 (1994),389–401, byl přečten v autorské
[verzi PDF](../sources/brent-1994-fibonacci.pdf), zejména lemmata 1–4
a věty 1–3. Vizuálně zkontrolované strany PDF
[4](../images/brent-fibonacci-p04.png), [5](../images/brent-fibonacci-p05.png),
[6](../images/brent-fibonacci-p06.png), [7](../images/brent-fibonacci-p07.png)
obsahují předpoklady i rozhodující důkazy. Vlastní odvození výše
vysvětluje, proč jsou v knize nutné právě dvě nerovnosti.
Článek také výslovně uvádí konstantní periodu 6 pro 1-x+x²;
[C0009](C0009-period-search-termination.md) tedy neprezentuje tento
samotný jev jako nový, ale dokládá chybnou aplikaci bez podmínky růstu.

## Úloha 23: odečítání

Rekurence X_n=X_(n-55)-X_(n-24) modulo 2^e má charakteristický
polynom x^55+x^31-1. Modulo 2 je reciproký k ověřenému
x^55+x^24+1, a tedy primitivní. Právě dokázaná trojčlenná věta dává
periodu 2^(e-1)(2^55-1), pokud nejsou všechny počáteční členy sudé.

Důvod možné implementační výhody je přesný: pro dyadické zlomky
v [0,1) s nejvýše t binárními místy má rozdíl velikost <1 a zůstává
přesně reprezentovatelný v binární aritmetice s t bity mantisy.
Je-li záporný, přičte se 1. Součet dvou takových zlomků může před
redukcí přesáhnout 1 a potřebovat o bit více. Odkaz na konkrétní
implementaci §3.6-11 zůstává v auditu této pozdější sekce;
nejde o tvrzení, že odečítání je rychlejší na každém stroji.

## Úloha 31: násobení lichých zbytků

Pro e>=3 má každý lichý zbytek modulo 2^e jednoznačný tvar
(-1)^Y 3^Z, kde Y je 0 nebo 1 a Z je zbytek modulo 2^(e-2).
Jde o rozklad grupy jednotek z §3.2.1.2C. Násobení odpovídá sčítání
Y modulo 2 a Z modulo 2^(e-2). Obě složky proto splňují tutéž
zpožděnou Fibonacciho rekurenci se zpožděními 24 a 55.

Lichost Z je ekvivalentní X modulo 8 rovno 3 nebo 5. Předpoklad
úlohy, že počáteční X nejsou všechny ±1 modulo 8, proto zajišťuje
nenulový seed Z modulo 2. Složka Z má periodu 2^(e-3)(2^55-1).
Složka Y má periodu 1 nebo 2^55-1. Jednoznačnost rozkladu dává
celkovou periodu rovnou jejich nejmenšímu společnému násobku,
tedy právě 2^(e-3)(2^55-1). Lichost X je převzata z definice (7').

Přímé násobení zbytků bylo nezávisle porovnáno s exponentovým
modelem v **14000 přechodech**, pro e=3,4,5,8,16,32,64.
Jde o kontrolu identit; obecnou délku periody dokazuje argument výše.

## Úloha 32: každá druhá a třetí hodnota

Nad celými čísly má generující funkce G(z)=sum_n X_n z^n jmenovatel
F(z)=1-z^24-z^55 a čitatel stupně <55. Sudé koeficienty získáme
jako (G(z)+G(-z))/2; součin jmenovatelů je

```
F(z)F(-z) = 1-2z^24+z^48-z^110.
```

Po přejmenování z² na w dostáváme pro Y_n=X_(2n)
Y_n=2Y_(n-12)-Y_(n-24)+Y_(n-55), n>=55.
Pro třetí členy použijeme třetí odmocninu jednotky omega a součin
F(z)F(omega z)F(omega² z)=(1-z^24)^3-z^165.
Proto Z_n=X_(3n) splňuje
Z_n=3Z_(n-8)-3Z_(n-16)+Z_(n-24)+Z_(n-55), n>=55.
Identita se nejprve odvodí nad celými/komplexními čísly a pak redukuje
modulo m; dělení 2 či 3 tedy nevyžaduje invertibilitu těchto čísel
modulo m. Ověřeno **892 identit lineárních forem** v 55 nezávislých
počátečních hodnotách, nikoli jen několik číselných seedů.

## Úloha 33: polynomická reprezentace a člen 500

Polynom g_n má koeficienty X_(n+30),...,X_n na stupních 0,...,30
v opačném pořadí a X_(n+54),...,X_(n+31) na stupních 31,...,54.
Při násobení z modulo 1+z^31-z^55 se poslední koeficient přičte
ke stupňům 0 a 31. Jediný potřebný vztah je
X_(n+55)=X_(n+31)+X_n. Tedy g_(n+1)=z g_n a indukcí
g_(n+t)=z^t g_n v tomto okruhu, také po redukci modulo m.
Ověřeno **300 identit** pro všechny počáteční hodnoty současně.

Je-li z^500 mod (1+z^31-z^55)=sum_j c_j z^j, pak vybráním
koeficientu stupně 30 z g_500=sum_j c_j g_j dostáváme
X_500=sum_j c_j X_j. Všech 20 nenulových koeficientů vytištěných
na str.558 souhlasí s přímou symbolickou rekurencí i nezávislým
polynomickým umocněním. Stejně byl ověřen šestiprvkový vzorec X_165.
Přesná čísla jsou v [lagged-identities.json](../results/lagged-identities.json).
Poznámka, že prořezání po blocích odstraní tuto konkrétní řídkou
závislost lépe než každý třetí člen, není sama úplným statistickým
důkazem kvality Lüscherovy metody; té se věnuje zbytek textu sekce.

Reprodukce: [verify_lagged_identities.py](../verify_lagged_identities.py),
[výsledky](../results/lagged-identities.json), [log](../results/lagged-identities.log).
Všechny uvedené kontroly skončily úspěšně, exit 0.
