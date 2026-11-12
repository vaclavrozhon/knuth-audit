# Exact cover: stromy a nejhorší případ

Pracovní poznámky 31. 10. 2026. Všechny počty uzlů zahrnují kořen,
úspěšné listy i neúspěšné listy. To odpovídá výslovné definici na str. 98–99.

## Úlohy 29–30: libovolný strom

Započteno publikované erratum z 22. 3. 2023: strom tvořený jediným
úspěšným kořenem reprezentuje matice 0×0. Neúspěšný list má jeden sloupec
a žádný řádek. Oprava nahrazuje původní zvláštní zacházení s úspěšnými dětmi.

Pro vnitřní vrchol s d dětmi vezmeme disjunktní dětské matice se sloupci
C_j a přidáme tři sloupce a,b,c. Zachováme dětské řádky. Přidáme d řádků
`{a,b,c} ∪ (C\C_j)` a dva ochranné řádky `{a}∪C`, `{b}∪C`, kde C je
sjednocení dětských sloupců. Sloupec c má délku d, a a b délku d+1.
Každý starý sloupec má alespoň d+1 výskytů: d−1 větví do jiných dětí a
dva ochranné řádky. MRV proto jednoznačně zvolí c. Volba j odstraní
nové sloupce, ostatní dětské bloky i ochranné řádky a zachová právě j-tou
matici. To dokazuje konstrukci indukcí, včetně úspěšných dětí s C_j=∅.
Více takových dětí může dát duplicitní řádky, které úloha 30 dovoluje.

`check_search_trees.py` ověřil všech 626 uspořádaných tvarů stromu do osmi
vrcholů a všechna označení listů, celkem **10 880 stromů**. Nezávislý
množinový algoritmus porovnává celý uspořádaný strom a jeho listy; DLX
porovnává profil a počet řešení. U každého navštíveného neúspěšného či
vnitřního vrcholu je minimum MRV jediné. Po opravě žádný nový nález.

## F017: D(1)=1 není horní mez počtu uzlů

Str. 99, (76), uvádí D(0)=D(1)=1. Jediná možnost `{a}` na jediném
prvku a však dává kořen a úspěšný list: **dva uzly**. Matice [1] je
strict, nemá stejné řádky ani sloupce. Nejde o jinou konvenci počítání:
str. 99 výslovně počítá 0×0 řešení jako uzel stromu.

Důsledky se neomezují na základ rekurence:

| Možnosti | Počet možností | Skutečné uzly | D(n) v knize |
|---|---:|---:|---:|
| a | 1 | 2 | 1 |
| a, b | 2 | 3 | 2 |
| a, b, c, ab, bc | 5 | 7 | 6 |

Ve třetím příkladu MRV zvolí a (nebo symetricky c). Větev a zbývá
řešit b,c,bc a má čtyři uzly; větev ab zbývá řešit c a má dva uzly.
S kořenem je to 1+4+2=7. Profil po úrovních je 1,2,3,1 a jsou tři řešení.

Znění je ověřeno ve vykresleném PDF str. 99–100 a v autorově původním
PostScriptu Pre-Fascicle 5C, str. 35. V úplných načtených erratech 4B a
historického Fascicle 5 není odpovídající oprava. Fyzický výtisk neověřen.
Doklady: `images/vol4b-p99.png`, `images/vol4b-p100.png`,
`images/fasc5c-p35.png`, `results/doomsday.json`.

## Úloha 180 po opravě z 15. 2. 2026

Označme MRV délku t, větvící řádky o_1,...,o_t seřazené podle počtu
průniků s_p a délku minimálního prefixu u=t'. Následující indukce
ověřuje opravený strukturální výrok; zahrnuje zákaz stejných sloupců.

Je-li s_1=t, každý prvek v o_1 se musí objevit ve všech t větvících
řádcích a nikde jinde. Dva takové prvky by měly stejné sloupce,
proto o_1={i_1}. Předpokládejme už prefix o_j={i_1,...,i_j}, j<p,
a vnější řádky T_2,...,T_(p−1). Jejich sjednocené okolí má t+p−2
řádků. Řádek o_p obsahuje předchozí prefix a alespoň jeden nový prvek,
jinak by opakoval o_(p−1). Nový prvek se nevyskytuje v prvních p−1
řádcích, takže ve starém okolí má nejvýše t−1 možných výskytů. MRV
vyžaduje alespoň t výskytů: musí přibýt vnější řádek T_p a s_p≥t+p−1.

Při rovnosti je nový řádek jediný; každý nový prvek musí obsadit všech
t dostupných pozic. Více nových prvků by mělo stejné sloupce. Je tedy
právě jeden, i_p, a o_p je přesně prefix délky p. Sloupec i_p se objeví
v o_p,...,o_t a T_2,...,T_p. Indukce dává vnější řádky se suffixy
`i_r,...,i_u`, r=2,...,u, a t−u zbývajících větvících řádků obsahujících
celý prefix. To je přesně opravené schodiště v erratu. Pokud rovnost
poprvé nenastane v pozici u+1, platí s_(u+1)≥t+u+1.

Úplný výčet **32 192 strict matic** na nejvýše čtyřech prvcích ověřil
strukturu ve **50 674** MRV volbách, včetně prázdných sloupců. Nezávislý
bitový algoritmus maximalizuje velikost stromu přes všechny MRV remízy
v každém uzlu, nikoli pouze přes jedno pořadí sloupců. Opravená číselná
mez níže platí ve všech těchto případech. Samotný výčet není obecný důkaz.

## Opravená číselná rekurence

Ponecháme (77), (78), (80), změníme pouze D(1) na 2. Hodnoty n=0,...,21:

```
1,2,3,4,6,8,10,14,19,25,33,43,58,77,101,133,175,233,309,405,533,701
```

Pak je maximum jednoznačně při (t,u)=(4,0) pro všechna n≥17.
Pro k≥3 a r=0,...,4 dostáváme

`D(5k+r) = 4^k c_r − 1/3`,

kde `96(c_0,...,c_4)=(200,263,350,464,608)`.
Toto je tvrzení o **opravené** rekurenci; staré konstanty úlohy 181
správně řeší původní chybný základ. Nejde o další samostatný překlep.

### Konečný certifikát platný pro všechna n

Definujme F prvními 17 opravenými hodnotami a periodickou rekurencí
F(n+5)=4F(n)+1 pro n≥12. Přímá konečná kontrola ověří původní maximum
až po n=45, přísný růst, a F(n+5)≥4F(n)+1 i pro n=0,...,11.
Periodičnost tyto poslední dvě vlastnosti přenáší na všechna n.

Velká t≥15 není třeba kontrolovat jednotlivě. Platí
`4^floor(t/5)≥2t`: stačí t=15,...,19 a pak krok t→t+5.
Pro u≥1 položme a=n−t−u+1. Z periodického růstu plyne
F(n)≥2t F(a), zatímco d(n,t,u)≤u+tF(a)≤t+tF(a).
Protože F(a)≥1 a periodický růst má ještě kladný aditivní člen,
je nerovnost ostrá. Pro u=0 obdobně použijeme a=n−t−1 a
d=1+tF(a). Neplatné záporné argumenty jsou v maximu vynechány;
nulový koeficient posledního členu znamená, že se tento člen nepoužije.

Zbývá t≤14. Pro n≥41 jsou všechny použité argumenty alespoň 12.
Označme mezeru G(n)=F(n)−d(n,t,u). Pak

```
G(n+5) = 4G(n) + 4−t             pro u=0,
G(n+5) = 4G(n) + 1−t+3u         pro u>0.
```

Program pro n=41,...,45 přesně ověří G>0 a 3G+c≥0 pro všechny
kandidáty kromě (4,0), kde G=c=0. To zachovává kladnost při kroku +5.
Jde o 595 celočíselných certifikátů a explicitní redukci nekonečného
rozsahu, nikoli extrapolaci z hodnot do 200. Jednoznačnost pro 17≤n≤45
ověřuje přímé maximum. Tím je vzorec pro opravenou rekurenci dokázán.

### Proč opravená rekurence skutečně omezuje stromy

Je potřeba ošetřit i MRV remízy, které vysvětlení u obrázku (81)
nerozebírá. Použijeme F(m+1)≥F(m)+1 a F(m)≥m+1.

Po větvi o_p, p<u, zůstává N=n−t−p+1 řádků. Sloupec i_(p+1)
má jedinou možnost T_(p+1), která protíná všech k=u−p zbývajících
speciálních řádků. Dokud tuto možnost nevezmeme nebo nezrušíme,
MRV má délku nejvýše jedna. Nemůže tedy mezitím skutečně větvit.
Pokud algoritmus nejprve vezme h jiných možností a pak T_(p+1), tyto
jiné možnosti musejí být mimo speciální k-tici, jinak by T_(p+1)
zrušily a vznikl by okamžitě prázdný sloupec. Po T_(p+1) proto zbývá
nejvýše N−k−h řádků a počet uzlů je nejvýše

`h+1+F(N−k−h) ≤ 1+F(N−k)`.

Při dřívějším selhání má řetězec nejvýše N−k+2 uzlů (nejvýše N−k
nespeciálních možností a případně jedna speciální, která zruší
T_(p+1)); to je rovněž nejvýše 1+F(N−k). V obou případech tedy
platí požadovaná mez 1+F(n−t−u+1), i když algoritmus napřed zvolí
jiný nucený sloupec.

Větev o_u má nejvýše F(n−t−u+1) uzlů a další větve nejvýše
F(n−t−u−1). Přičtení kořene dává přesně (80). Případ u=0 dává
(78). Případy n=0,1 jsou nejvýše 1,2. Pro n≥2 nemůže t=n:
všechny sloupce by byly shodné a strict podmínka by ponechala jediný
sloupec a nejvýše jeden neprázdný řádek. Indukce tedy pokrývá všechny
strict problémy s neprázdnými možnostmi a všechny MRV remízy.

Asymptotický závěr Theorem E, O(4^(n/5)), touto opravou zůstává platný.
Nález se týká přesné konečné meze a jejích počátečních hodnot.

Původ analýzy: [Eppsteinův autorský text z roku 2008](https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html).
Výše uvedené protipříklady, výpočet opravených konstant a konečný
certifikát byly odvozeny v tomto auditu.
