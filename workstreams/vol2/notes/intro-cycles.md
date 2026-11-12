# §3.1: konečné posloupnosti, detekce cyklů a prostřední čtverce

Kontrola 1. listopadu 2026. Tato poznámka dokládá úlohy §3.1-2 až 10,
16 až 18 a 22, s níže uvedenými omezeními u rozsáhlé odpovědi 7.
Neuzavírá celou sekci. Strany zadání 6–9 a odpovědí 539–543 byly zobrazeny;
například [str. 7](../images/vol2-p007.png),
[539](../images/vol2-p539.png), [540](../images/vol2-p540.png).
Historické opravy viz poslední oddíl.

## Jednoduché výpočty a algoritmus K

Pro úlohu 2 předpokládáme milion nezávislých rovnoměrných desetinných cifer.
Počet řetězců s přesně 100 000 výskyty každé cifry je multinomický koeficient,
tedy pravděpodobnost je

```text
P = 1000000! / ((100000!)^10 * 10^1000000).
```

Dosazení Stirlingova vzorce pro faktoriál dává aproximační výraz v knize.
Výpočet s 60 desetinnými místy dává
`P = 2.559687864515764516864781059186242447292e-26`.
Uvedená aproximace `2.56e-26` je správná; relativní odchylka samotného
Stirlingova výrazu je přibližně `-8.25e-6`.

Metoda prostředních čtverců pro `2n` cifer v základu `b>=2` je zobrazení
`S(x)=floor(x^2/b^n) mod b^(2n)` na stavech `0<=x<b^(2n)`.
Pro úlohu 3 přímý celočíselný výpočet dává `S(1010101010)=3040504030`.
Ověřen je také příklad na str. 3: `5772156649^2=33317792380594909201`
a následující stav `7923805949`.

V algoritmu K každý krok zachovává interval `0<=X<10^10`.
U K6 je větev s přičtením menší než `9914055677`, druhá větev je kladná.
V K10 je výsledek kladný: pro `X<100000` je to `X^2+99999`, jinak
`X-99999>=1`; obě větve také dávají výsledek menší než `10^10`.
Přímý skok K2 do K11 znamená druhou cifru 8, tedy `X>=800000000>0`.
Proto K11 nenásobí nulu donekonečna. Při každém násobení je vstup menší
než `10^9`, a tak výsledek zůstává menší než `10^10`. Tím je doložena
odpověď 4(a), včetně ukončení vnitřní normalizace.

Všech 45 řádků [tabulky 1 na str. 6](../images/vol2-p006.png) bylo
ručně přepsáno ze sazby a porovnáno s přesným přepisem K. Souhlasí.
Stejně tak souhlasí řetězec z odpovědi 4(b):

```text
3830951656 -> 5870802097 -> 1226919902 -> 3172562687
           -> 3319967479 -> 6065038420 -> 6065038420.
```

Úloha 5: deterministické zobrazení na `10^10` stavech musí mezi prvními
`10^10+1` členy opakovat stav. Od prvního opakování se shoduje celý další
průběh. To je důkaz eventualní periodicity, nikoli tvrzení o dobré náhodnosti.

## Úloha 6: Floydova detekce

Nechť `f` je zobrazení konečné množiny `m>=1` stavů do sebe a
`X_{t+1}=f(X_t)`. Označme `mu` počet členů před vstupem do cyklu a
`lambda` délku cyklu. První opakovaný člen má index `mu+lambda`, tedy
`0<=mu<m`, `1<=lambda<=m` a `mu+lambda<=m`. Krajní možnosti v odpovědi
6(a) realizují celý cyklus, respektive cesta končící pevným bodem.

Pro `r>n` platí `X_r=X_n` právě tehdy, když `n>=mu` a `lambda` dělí
`r-n`. Nejmenší **kladné** `n` s `X_n=X_{2n}` je proto

```text
n = lambda * (ceil(mu/lambda) + [mu=0]),
```

kde `[mu=0]` je 1 při `mu=0`, jinak 0. Leží mezi `mu` a `mu+lambda`
včetně. Všechny takové indexy jsou násobky `lambda`, takže hodnoty `X_n`
jsou stejné. Pologrupa je množina s asociativním násobením; idempotent je
prvek `e` splňující `e*e=e`. Poznámka o jednoznačném idempotentu mezi
mocninami jednoho prvku odpovídá stejnému argumentu: vezmeme `X_1=a`
a `f(x)=a*x`, takže `X_n=X_(2n)` právě znamená idempotenci `a^n`.

Po nalezení `n` se dvojice `X_i,X_{n+i}` poprvé shodne při `i=mu`.
Je-li `lambda<mu`, první návrat `X_{n+i}=X_n` pro `0<i<mu` je při
`i=lambda`. Pokud se takový návrat nenajde, platí `mu<=lambda`, a tedy
`n=lambda`. To dokazuje i poněkud úsporně zapsanou odpověď 6(c).
Obě fáze potřebují `O(mu+lambda)` aplikací `f` a konstantně mnoho stavů.
Zde `O(t)` znamená horní mez konstantním násobkem `t`.

## Úloha 7: Brentův a Gosperův detektor

Definujme `ell(n)` jako největší mocninu dvojky nejvýše `n`. Brent porovnává
`X_n` s `X_{ell(n)-1}`. V bloku s `ell(n)=p`, kde `p` je mocnina dvojky,
je rozdíl indexů od 1 do `p`; rovnost proto nastane právě tehdy, když
`p-1>=mu` a rozdíl je násobkem `lambda`. První úspěšný blok má
`p=2^ceil(log2(max(mu+1,lambda)))` a první shoda je při
`n=p-1+lambda`. Aktualizace proměnných v odpovědi 7(b) skutečně udržují
referenční index `p-1` a odpočítávají délku bloku. Případ `mu=0,lambda=1`
je zahrnut; nedochází k nulové délce cyklu.

V Gosperově detektoru je `e(n)` největší `e>=0`, pro které `2^e` dělí `n+1`.
Tabulka ukládá poslední stav s každou hodnotou `e`. Stav uložený při indexu
`i` je porovnáván ještě s indexem `i+2^(e(i)+1)` včetně, protože porovnání
předchází přepsání. Nechť `L=ceil(log2(lambda))`.
První opakování zachycené tabulkou je proto při

```text
n = mu + lambda + j,
j = nejmenší nezáporné celé číslo s e(mu+j) >= L-1.
```

Pro `lambda=1` je `j=0`. Jinak jsou vhodné indexy od sebe vzdáleny
`2^(L-1)` a `0<=j<2^(L-1)<lambda`. Než se detektor zastaví, žádný stav
se tedy nevyskytne více než dvakrát a nejvýše
`max(1,2^(L-1))` různých stavů se vyskytne podruhé. Rozdíl indexů při
shodě je přesně `lambda`, ne její větší násobek. To ověřuje i doplňující
Gosperův odstavec odpovědi 7.

Přepis algoritmů a vzorce byly porovnány na všech 16 384 dvojicích
`0<=mu<=127`, `1<=lambda<=128`. Důkazy výše pokrývají obecné hodnoty.
### Doplňující citované výsledky odpovědi 7

[Brentův původní článek, BIT 20 (1980), rovnice (4.6)–(4.9)](https://maths-people.anu.edu.au/~brent/pd/rpb051i.pdf)
analyzuje spojitou aproximaci rovnoměrné náhodné funkce a náhodně
posunuté fáze geometrických kontrolních bodů. Pro růstový parametr `p>1`
je hlavní konstanta počtu vyhodnocení, normalizovaného druhou odmocninou
počtu stavů,

```text
A(p)=sqrt(pi/8)*((p^2-p+1)/(p*log(p))+1).
```

Zde `log` je přirozený logaritmus. Derivace mění znaménko v jediném
kořeni `(p^2-1)*log(p)=p^2-p+1` pro `p>1`. Jednoznačnost plyne z
přísné konvexity rozdílu obou stran, jeho záporné hodnoty a derivace
v 1 a růstu do nekonečna. Kořen je `2.477136593148...`, náklady
`1.925995836486...` proti `A(2)=1.982769636594...`: úspora 2.86336 %.
Knižní zaokrouhlené hodnoty souhlasí. Nejde o přesné optimum pro každý
konečný deterministický generátor; číslo pochází z uvedeného modelu.
[Výpočet](../results/brent-optimum.json) použil `mpmath` s 50 ciframi,
`findroot` na poslední rovnici s počáteční dvojicí `(2,3)`.

U dodatku Sedgewick–Szymanski–Yao byla naopak potvrzena chyba:
[V2-C0002](C0002-cycle-table-boundaries.md). Chybí `g<m` a počáteční
ošetření rozestupu a meze. Proto je celá odpověď 7 vedena jako
`confirmed`, nikoli jako bezchybná.

Zbylé asymptotické tvrzení jsme porovnali s původním článkem,
[SICOMP 11 (1982), věta 1, korolária 3 a 4, str. 382–386](https://sedgewick.io/wp-content/themes/sedgewick/papers/1982Cycles.pdf).
V jeho modelu `tau` stojí vyhodnocení funkce a `sigma` hledání v tabulce
s `m` položkami. Pro dlouhé trajektorie délky `N=mu+lambda` vyvažuje
volba `g` řádu `sqrt(sigma*m/tau)` příspěvky `N*tau*g/m` a
`N*sigma/g`. Výsledný přírůstek času má řád `N*sqrt(sigma*tau/m)`.
Odpovídající dolní mez má stejný řád za předpokladu `sigma/tau=O(m)`
v uvedeném modelu operací. Jde o kontrolu citace a předpokladů hlubšího
výsledku; vlastní důkaz dolní meze zde nereprodukujeme.

Velmi volná knižní mez na dodatečné nalezení `mu,lambda` po zjištění
kolize je bezpečná: z bodu na cyklu najdeme `lambda` jedním oběhem,
z `X_0` vytvoříme `X_lambda` a obě hodnoty posouváme do první shody.
To stojí celkem `2*lambda+2*mu=2*N` vyhodnocení, méně než uváděná
mez `(g+1)*2^(ceil(log2(N))+1)`. Pro ostrý časový odhad slouží
úspornější obnova v citovaném článku.

Při online výstupu pro dlouhé trajektorie lze vedle předbíhajícího
detektoru vést druhý ukazatel, který vydává pouze zaručeně dosud různé
členy. Pro `g` řádu `sqrt(m)` potřebuje detektor `1+O(m^(-1/2))`
vyhodnocení na vydaný člen a druhý ukazatel jedno další. Tím vzniká
citované `2+O(m^(-1/2))`; počátek běhu však vyžaduje opravu z C0002.

## Úlohy 8–10: prostřední čtverce

Úloha 8: úplný rozklad všech 100 dvouciferných stavů dává:

| Konečný cyklus | Počet počátečních stavů |
|---|---:|
| 00 | 62 |
| 10 | 19 |
| 24, 57 | 3 |
| 50 | 1 |
| 60 | 15 |

Nejdelší úsek bez opakování má 15 stavů a začíná pouze v 42 nebo 69.
To přesně souhlasí s odpovědí. Při rozkladu grafu se nejprve odstraňovaly
vrcholy bez vstupních hran; samostatně se pak kontrolovaly všechny hrany,
hloubky cest a disjunktnost cyklů. Stejná metoda na všech `2^20=1048576`
stavech ověřila údaj z textu na str. 4: 13 cyklů, nejdelší délky 142.
Jejich délky jsou `1,1,1,1,1,1,1,2,2,5,10,44,142`.

Úloha 9: pokud `0<X<b^n`, pak `S(X)=floor(X^2/b^n)<X`; konečná sestupná
posloupnost nezáporných celých čísel proto skončí v nule.

Úloha 10: pro `X=a*b^n`, `0<=a<b^n`, dostáváme
`S(X)=(a^2 mod b^n)*b^n`. Opakováním se koeficient mění na
`a^(2^t) mod b^n`. Je nulový pro dost velké `t` právě tehdy, když každý
prvočíselný dělitel `b` dělí `a`: mocniny postupně dodají všechny potřebné
exponenty; chybějící prvočíslo se žádným umocněním neobjeví.
Pokud je posledních `n+1` cifer nula, pak `b` dělí `a`, a podmínka tedy
platí. Identita z poznámky `3792^2=14379264` a rozklad `3792=3*79*2^4`
také souhlasí.

## Úlohy 16–18 a 22

Při závislosti na `k>=1` předchozích hodnotách je stavem celé k-tuple.
Takových stavů je `m^k`, což je horní mez periody. Je dosažitelná:
v orientovaném grafu slov délky `k-1` vedou hrany odpovídající slovům
délky `k` z prefixu do suffixu. Každý vrchol má `m` vstupních i výstupních
hran a graf je souvislý v obou směrech; Eulerův okruh (okruh používající
každou hranu právě jednou) proto dává cyklické slovo, jehož k-tuple jsou
všechny různé. Určením následujícího symbolu pro každé k-tuple získáme
požadované `f`. Pro `k=1` jde o jeden vrchol s `m` smyčkami. Floydův nebo
Brentův detektor lze použít na celé k-tuple, což řeší úlohu 18.

Úloha 22: u opravdu rovnoměrně vybraného zobrazení jsou hodnoty
`f(0),...,f(m-1)` nezávislé a rovnoměrné. To platí do vyčerpání domény;
nejde o nekonečný zdroj nových nezávislých hodnot. Praktickou otázku, jak
takovou funkci vytvořit, odpověď výslovně ponechává otevřenou.

## Errata, reprodukce a omezení

Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` a `err2.textxt`,
stav zdrojů 1. 11. 2026. Relevantní změny: 11. 6. 1998 zjednodušení
vzorce Floydova indexu; 25. 12. 2002 označení `e(n)` jako `rho(n+1)`;
23. 12. 2024 oprava bibliografie Frobeniova výsledku. Žádná další oprava
ověřených algoritmických vzorců v těchto vrstvách nebyla nalezena.

```sh
python3 workstreams/vol2/verify_intro.py
python3 workstreams/vol2/verify_intro_extra.py
```

Výsledky: [intro.json](../results/intro.json),
[intro-extra.json](../results/intro-extra.json). Druhý skript potřebuje
již vytvořené certifikáty inverze K, viz [poznámka o K](intro-k-inversion.md).
Neověřovali jsme znovu konkrétní historický experiment s neuvedeným seedem
ani statistické testy historické 38bitové posloupnosti; z těchto osobních
sdělení autora nevyvozujeme vlastní výpočetní certifikát.
