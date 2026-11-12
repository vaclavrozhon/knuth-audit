# Monotónní podíly a chordální grafy: SAT 346–347

Kontrola 31. 10. 2026. F037 je drobný překlep v důkazu 346(a).
Algoritmus 346(b), oba rozepsané příklady a charakterizace 347 fungují.

## F037: obrácené slovo v monotónnosti

Odpověď 346(a), str. 616, má větu „Decreasing p_j doesn't decrease any
trace.“ Poslední `decrease` má být `increase`. Monomy nezáporné řady
se při snížení pravděpodobností nezvětšují. Zadání úlohy na str. 347
uvádí směr monotónnosti správně.

U grafu s jedinou hranou a—b je `K_(a,G)=1/(1−p_b)`.
Pro p_a=1/8 a p_b=1/2 ležíme uvnitř R(G), stejně jako po změně
p_b na 1/4. Podíl přitom klesne z 2 na 4/3. Už samotná stopa b
má váhu klesající z 1/2 na 1/4.

Znění je vizuálně ověřeno v PDF i původním autorově PostScriptu,
Pre-Fascicle 6A, 23. září 2015, str. 252. V kompletních stažených
erratech `all4b`, `all4f6`, ani krátkých verzích nebyla odpovídající
oprava nalezena. Fyzický exemplář dosud ověřen není.

## Nezávislý důkaz monotónnosti bez nekonečné řady

Pišme `K_(a,G)=M_(G\N[a])/M_(G\a)`. Po odstranění a postupně
odstraňme jeho sousedy v₁,…,v_d. Je-li H₀=G\a a H_j=H_(j−1)\v_j,
teleskopicky dostáváme

`K_(a,G)=Π_j (1−p_(v_j) K_(v_j,H_(j−1)))^(−1)`.

Všechny jmenovatele jsou kladné v R(G). Indukce podle počtu vrcholů
dává monotónnost každého menšího podílu. Každý faktor výše proto
roste při zvýšení parametrů, dokud zůstáváme v R(G). Pro izolovaný
vrchol je součin prázdný a K=1. Důkaz pokrývá i nulové p_i.

Algoritmus nejprve ověří R(G\a), spočítá K a vyžaduje p_a K<1.
Zkouška R(G\N[a]) je po úspěchu G\a redundantní, ale neškodná.
Pro libovolné q≤p je `q_a K(q)≤p_a K(p)<1`; z
`M_G(q)=M_(G\a)(q)(1−q_a K(q))` plyne kladnost na celém boxu.
Obrácený směr je přímo nutný. Jde tedy o skutečný test příslušnosti
k R(G), nikoli jen o zkoušku kladnosti M v jediném bodě.

Obě tabulky pro žebřík P₃ □ P₂ byly přepsány po kontrole obrázku;
každá pomocná proměnná byla symbolicky porovnána s podílem dvou
polynomů získaných úplným výčtem nezávislých množin. Platí všechny
primované i dvojitě primované hodnoty a oba výsledné součiny.

## Proč stromové uspořádání charakterizuje chordální grafy

V libovolném cyklu vezměme vrchol největší hloubky v uspořádávajícím
lese. Jeho oba sousedé v cyklu jsou jeho předky, tedy jsou navzájem
porovnatelní. Druhá podmínka (*) je nutí být spojeni hranou.
Cyklus délky alespoň čtyři má proto tětivu. To dokazuje 347(a)
bez potřeby rozebírat orientaci jednotlivých hran cyklu.

Pro 347(b) použijme reprezentaci průniky souvislých podstromů U.
Nejvyšší vrchol U_a každého neprázdného T(a) patří do T(a).
Uspořádejme a před b, je-li U_a vlastním předkem U_b; při rovnosti
rozhodne pořadí indexů. Předci každého vrcholu jsou řetězec, takže
takový částečný pořádek opravdu pochází z lesa. Mají-li T(a),T(b)
společný bod t, oba U_a,U_b leží na cestě od kořene do t, tedy
jsou porovnatelné. Pro a≺b≺c a t∈T(a)∩T(c) leží U_b na cestě
od U_a do t, a proto v T(a)∩T(b). Obě podmínky (*) platí.

Izolovaný vrchol lze reprezentovat samostatným jednovrcholovým
teritoriem připojeným k pomocnému stromu; prázdná teritorie nejsou
pro reprezentaci potřebná.

## Faktorizace a přesný test 347(c,d)

Počítejme od listů ke kořenům

`θ_v=p_v / Π_(u potomkem v, u~v)(1−θ_u)`.

Pro libovolnou množinu vrcholů uzavřenou směrem k potomkům má
indukovaný graf polynom `Π_v(1−θ_v)` se stejnými θ jako původní
graf. Důkaz indukcí odstraní jeden kořen a. Také odstranění N[a]
zanechá množinu uzavřenou směrem k potomkům: není-li vrchol sousedem
a, nemůže být sousedem a žádný jeho potomek, podle (*).
Poměr dvou menších součinů je právě převrácený součin přes sousedy
a mezi potomky. Obvyklá rekurence pro M pak doplní faktor 1−θ_a.

Pokud všechny θ_v<1, stejná rekurence při snížení p monotónně sníží
všechna θ, takže M zůstane kladné na celém boxu. Naopak pro p∈R
jsou všechny indukované podgrafy v R a každý faktor spočítaný v tomto
pořadí je kladný. Dostáváme přesně ekvivalenci v zadání 347(d).
Jednoznačnost θ vyplývá z výpočtu od listů a kladných jmenovatelů.

## Reprodukovatelné kontroly

`check_chordal.py` porovnává chordalitu přímým hledáním indukovaných
cyklů s nezávislou eliminací simpliciálních vrcholů. Z eliminačního
pořadí sestaví les a přímo zkontroluje obě podmínky (*) na všech
dvojicích a trojicích. Pro pravděpodobnostní vektory porovnává
rekurzivní algoritmus a výpočet θ s kladností všech indukovaných
Möbiových polynomů. Zahrnuje nuly, hranici a parametry mimo R.
Číselné rozsahy a výsledky jsou v `results/chordal.json`.
