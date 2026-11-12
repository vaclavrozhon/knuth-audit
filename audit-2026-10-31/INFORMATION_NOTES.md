# MPR 121–127: další kontrola

## 122: divergence binomického a Poissonova rozdělení

Značme `q=1−p`, `K~Bin(n,p)` a `L=n−K`. Přímým zkrácením faktoriálů
v logaritmu poměru pravděpodobností dostaneme nezávisle na řešení v knize

```
ln(2) D(Bin(n,p) || Pois(np))
 = ln(n!) − E ln(L!) − np ln n + nq ln q + np.
```

Pro pevné `0<p<1` použijeme Stirlingův rozvoj u `nq` a centrální momenty
binomického rozdělení:
`μ₂=npq`, `μ₃=npq(p−q)`, `μ₄=3(npq)²+npq(1−6pq)`.
Je-li `s(x)=(x+1/2) ln x−x+(ln(2π))/2+1/(12x)`, pak

```
E ln(L!) = s(nq) + p/2
           + [−p/4 − p(p−q)/6 + p²/4]/(nq) + O(n⁻²).
```

K odůvodnění zbytku lze rozvinout na centrální oblasti do šestého řádu.
Pátý a šestý centrální moment přispívají `O(n⁻²)`, absolutní zbytek sedmého
řádu je menší; mimo oblast `|L−nq|≤nq/2` je příspěvek exponenciálně malý.
Tím vychází

```
D = [−ln q−p]/[2 ln 2] + p²/[12q ln(2) n] + O(n⁻²).
```

Hlavní člen a požadovaná chyba `O(1/n)` v odpovědi **souhlasí**. Opačná
divergence je nekonečná, protože Poissonovo rozdělení má kladnou hmotnost
v `n+1`, kde binomické rozdělení nemá žádnou.

Program `check_information_asymptotics.py` provedl 40 přímých konečných
součtů s přesností 60 desetinných míst: p=0,1; 0,25; 0,5; 0,75; 0,9,
n od 20 do 10 000. Škálovaná chyba konverguje k nezávisle odvozenému
koeficientu. To je kontrola výpočtu, nikoli náhrada asymptotického důkazu.

## C004: doplnění již známé opravy úlohy 124

Erratum z 15. 7. 2025 opravuje zadání na str. 25: mez platí pro očekávanou
absolutní chybu. Odpověď na str. 390 však stále obsahuje dvě neplatné rovnosti
a jedno bodové tvrzení, které platí jen v očekávání. Stejné znění je
v autorově Pre-Fascicle 5A na str. 47, obrázek `images/fasc5a-p47.png`.

První rovnost má být trojúhelníková nerovnost se třemi absolutními hodnotami.
Příklad: `x=(15/16,1/16)`, `y=(1/2,1/2)`, `f=(0,−1)`, `n=4`.
Zde `2^D=8/√15`, takže `c>1` a `8/15 < m=√(32/√15) < 8`.
Tedy `g=0`. Na vzorku sestávajícím ze čtyř nul je `E_n(f)=0`;
vytištěná rovnost pak tvrdí `1/2=−1/2`. Tento vzorek má kladnou
pravděpodobnost `(15/16)^4`.

Druhá rovnost potřebuje očekávání před čtvercem chyby. Pro
`x=y=(1/2,1/2)`, `f=(0,1)`, `n=2` je `g=f` a
`Var(E_n(g))=1/8`. Samotný čtverec chyby je ale buď 0, nebo 1/4.

Správný důkaz: po trojúhelníkové nerovnosti vezmeme očekávání. První
a poslední člen jsou každý nejvýše `E_Y(|f(Y)|[ρ(Y)>m])≤‖f‖√Δ_c`.
Pro prostřední člen Cauchyho–Schwarzova nerovnost a výpočet rozptylu dají
`E|E_n(g)−E(g)|≤√Var(E_n(g))≤‖f‖/c`. Tím dostaneme opravené zadání.
Dolní mez pro `c<1` funguje pomocí sjednocení událostí a Markovovy nerovnosti.

Přesná enumerace binárních vzorků ověřila 2650 horních mezí pro kladné,
záporné i nulové funkce a 60 nastavení dolní meze, každé při třech prahových
hodnotách. Dalších 1665 konfigurací byly hraniční nebo pro danou mez
nepoužitelné případy; **nepočítají se jako úspěšné testy**.

Původní [článek Chatterjeeho a Diaconise](https://arxiv.org/pdf/1511.01437),
věta 1.1 a její důkaz v oddíle 4, používá očekávání i trojúhelníkovou
nerovnost správně a předpokládá absolutní spojitost cílové míry.

Klasifikace: matematická nesrovnalost v odpovědi je ověřena, ale evidujeme ji
jako **doplnění již známé opravy**, nikoli další nezávislý nový nález.

## F009: zaokrouhlení v odpovědi 127(b), str. 391

Vytištěno je

```
lg binom(n, floor(θn)) = n H(θ) − (1/2)lg(2πθ(1−θ)n) + O(1/n).
```

Pro pevné `0<θ<1/2` ale podlaha vytváří další omezený člen,
který obecně nekonverguje k nule. Je-li `r={θn}`, správný rozvoj je

```
lg binom(n, floor(θn))
 = n H(θ) − (1/2)lg(2πθ(1−θ)n) − r lg((1−θ)/θ) + O(1/n).
```

Stačí tedy změnit chybu na `O(1)`, což je pro požadovanou dolní mez dostačující.
Přesnější oprava přidá vypsaný člen se zlomkovou částí. Odvození: použijeme
Stirlingův rozvoj s `θ_n=floor(θn)/n=θ−r/n` a Taylorův rozvoj entropie;
`H′(θ)=lg((1−θ)/θ)` a změna logaritmického prefaktoru je `O(1/n)`.

Krátký protipříklad bez odhadu Taylorova zbytku: zvolme `θ=1/3`. Pro
`n=3k` je odchylka od vytištěného hlavního výrazu `O(1/k)`. Přitom přesně

```
binom(3k+1,k) / binom(3k,k) = (3k+1)/(2k+1) → 3/2.
```

Rozdíl hlavních výrazů pro `3k+1` a `3k` konverguje k `H(1/3)`.
Odchylka pro `3k+1` tedy konverguje k
`lg(3/2)−H(1/3)=−1/3`, nikoli k nule. Pro `3k+2` je limita `−2/3`.
Numerická kontrola s 60 ciframi a n až 30 002 je v `results/sparse_xor.json`.

Znění bylo vizuálně ověřeno v `images/vol4b-p391.png` i autorově původním
Pre-Fascicle 5A, str. 48, `images/fasc5a-p48.png`. V kompletních erratech
4B a historického Fascicle 5 odpovídající oprava nalezena nebyla.
**Dolní mez úlohy 127(b) a exponenciální závěr 127(c) zůstávají správné.**
Fyzický výtisk dosud neověřen; číslo F009 neznamená zaručené prvenství.

## 126 a 127(c): bez dalšího nálezu

Pravděpodobnost, že `Bin(n,m/n)` je rovna m, má minimum při `floor(n/2)`;
poměr sousedních hodnot uvedený v řešení a Stirlingův odhad dávají
jednotnou dolní mez řádu `n^(−1/2)`. Přesných 5150 zlomků pro `1≤n≤100`
potvrdilo místo minima a symetrii v m.

V řešení 127(c) je `ε=θ(1−2θ)/3`. Obě dolní meze na pravděpodobnost
jedničky jsou alespoň `θ+ε`. Pro nulový bit pevného vektoru je rezerva
`2θ²(1−2θ)/3`. Pro jedničkový bit je rezerva
`(2θ−1)(2θ³+5θ²+12θ−9)/9`; po substituci `θ=(1−u)/2`
má v Bernsteinově bázi na `[0,1]` nezáporné koeficienty
`0, 1/24, 55/216, 7/12, 1`.

Chernoffův faktor α je menší než 1 přísnou váženou AM–GM nerovností.
Podmínění dvou nezávislých Bernoulliho vektorů na jejich počty jedniček
stojí nejvýše faktor `O(n)` díky úloze 126. Po sečtení přes možné počty
jedniček zbývá `O(n α^n)`; pravděpodobnost počtu jedniček pod `(θ−ε)n`
je exponenciálně malá z poměru velikostí Hammingových koulí. Tím je
pro libovolný pevný vektor x dokázán závěr „q.s. není řídký“.

Nezávislý výčet bitových masek ověřil 472 počtů párů s předepsanými
vahami, pro `n≤7`, všechny přípustné celočíselné poloměry pod `n/2`
a všechny váhy pevného vektoru. Nejprve šlo o ověření kombinatorického
modelu, nikoli o odvozování exponenciálního závěru z malých příkladů.

## C005: pravý posun logaritmicky konkávní posloupnosti, 125(b)

Zadání pracuje s nezápornými posloupnostmi bez vnitřních nul. Odpověď tvrdí,
že po přidání c na začátek zůstane posloupnost logaritmicky konkávní právě
když `c a₁≤a₀²`. To přesně zajišťuje sousední nerovnosti, ale samo to
nezajišťuje nepřítomnost vnitřních nul.

Příklad: původní posloupnost `(0,0,1,0,0,...)` a `c=1` splňují uvedenou
podmínku. Nová posloupnost `(1,0,0,1,0,0,...)` má vnitřní nuly. Pokud se
pojem logaritmické konkávnosti používá jen pro sousední nerovnosti, jde
o správné tvrzení; pokud zahrnuje také podmínku z úvodu úlohy, je neúplné.
Proto je to **kandidát závislý na výkladu**, nikoli jednoznačná nová oprava.

`check_log_concavity.py` prověřil 644 pravých posunů 161 krátkých
posloupností; 129 případů ukazuje právě tuto otázku podpory. Obyčejná i
binomická konvoluce zachovaly logaritmickou konkávnost bez vnitřních nul
pro všech 25 921 dvojic těchto posloupností. Části o logaritmické
konvexnosti zatím nejsou pokryty tímto výpočtem.
