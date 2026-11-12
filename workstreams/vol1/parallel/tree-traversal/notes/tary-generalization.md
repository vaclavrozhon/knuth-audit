# Vlastní řešení otevřené úlohy §2.3.1-35

Pro pevné celé t≥2 je t-ární strom buď prázdný, nebo kořen s uspořádanou t-ticí disjunktních t-árních podstromů C1,...,Ct. Prázdné pozice jsou rozlišeny: jediný potomek v pozici 1 není stejný tvar jako v pozici 2. Následující volby dávají konkrétní smysluplné zobecnění hlavních témat, nikoli tvrzení, že všechny možné reprezentace a algoritmy byly klasifikovány.

## Průchody, zásobník a kódy

Pro každé j=0,...,t definujeme j-pořadí: nejprve projdeme C1,...,Cj, navštívíme kořen, poté C(j+1),...,Ct. j=0 je preorder a j=t postorder; pro t>2 neexistuje jediné privilegované „inorder“ bez další volby j. Obecný iterátor může mít na zásobníku rámec (P,k), kde k značí příští dítě nebo fázi návštěvy. Úplný postup:

```text
push(root,0), pokud root není null
while zásobník neprázdný:
    (P,k) = pop()
    pokud k=j: navštiv P
    pokud k=t: pokračuj další iterací
    push(P,k+1)
    pokud C[k+1](P) není null: push(C[k+1](P),0)
```

Invariant rámce: všechny děti s indexem ≤k již byly dokončeny, větší ještě nezačaly. Každý rámec postoupí nejvýše t-krát; prázdný vstup nedělá nic. Čas je O(tn), paměť nejvýše hloubka stromu plus konstantní pracovní prostor. Poslední dítě lze zpracovat bez ponechání rodiče na zásobníku, pokud již nezbývá jeho návštěva; jde o stejný princip jako v T.

Pro preorder variantu bez zadržování rodiče během posledního dítěte je maximální zásobník `h(T)=max(1+h(C1),...,1+h(C(t-1)),h(Ct))`, s h(null)=0. Při rovnoměrných t-árních tvarech dává omezená generující funkce `g_0=1` a `g_k=1/(1-z*g_(k-1)^(t-1))`. Celková funkce splňuje `G=1+z*G^t`, takže počet tvarů je `binom(tn,n)/((t-1)n+1)` (koeficientová inverze rovnice G−1=z*(1+(G−1))^t). Toto je přesné zobecnění, nikoli nekritické přenesení binární asymptotické konstanty.

Adresy jsou slova nad 1,...,t. Preorder je lexikografické s koncem slova před všemi číslicemi; postorder s koncem za nimi; j-pořadí s 1<...<j<konec<j+1<...<t. Listy mají ve všech těchto pořadích stejnou relativní posloupnost. Preorder spolu s maskou t nenulových dětských pozic a INFO jednoznačně určuje strom. Důkaz otevřených slotů používá f=počet dětí−1 stejně jako Lemma P; maska navíc určuje, které z t pozic jsou použity. Pouhý stupeň by nestačil.

Rekurzivní lexikografické porovnání `(INFO,C1,...,Ct)` s prázdným stromem na začátku dává lineární pořadí tříd ekvivalence, ale nikoli dobré pořadí: binární klesající posloupnost z úlohy 36 lze vložit do prvních dvou slotů. Pro porovnávání lze použít t návštěv kořene, vždy před příslušným dítětem, a zapisovat (INFO, příslušný bit masky); stejné indukční dekódování dává analogii odpovědi 26.

## Konkrétní threading a kopie bez pomocného zásobníku

Zobecníme alternativní reprezentaci z úlohy 33. Pole C1 obsahuje vždy preorder následníka P; tag rozlišuje, zda je to skutečné první dítě. Pole C2,...,Ct zůstávají obyčejnými dětskými odkazy nebo null. Je-li první dítě prázdné, C1 je nit: vede buď do prvního neprázdného pozdějšího dítěte, nebo za celý podstrom P. Hlavička má v první pozici kořen, případně nit sama na sebe. Následník je tak vždy jedno čtení C1.

Úplný algoritmus kopie je v `tary.py:copy_tree`. Jeho invariant je zobecnění C: cílový uzel Q má dosud prázdné dětské sloty, C1 je pokračovací nit K za kopírovaný podstrom. Pro zdrojový P vytvoříme potřebné rezervy v pořadí t,t−1,...,1. Každá nová rezerva R má všechna skutečná dítě prázdná a C1(R) nastavené na dosavadní C1(Q). Je-li vytvářen j>1, zapíšeme Cj(Q)=R; je-li j=1, označíme první slot Q jako skutečné dítě. V obou případech nastavíme C1(Q)=R. Tím se rezervy propojí v rostoucím preorder pořadí, ačkoli je vytváříme zprava doleva. Následuje kopie INFO a postup P=C1(P), Q=C1(Q). Hlavičkový počáteční krok vytvoří pouze první slot a nekopíruje INFO hlavičky.

Indukce po podstromech: levější rezerva se zpracuje dříve než pravější, její pokračovací nit je právě příští rezerva; uvnitř dosud nerozpracovaných rezerv se žádný odkaz nezmění. Nakonec jsou všechny cílové masky a INFO totožné se zdrojem a pokračovací nit K zůstane správná. Po dosažení zdrojové hlavičky je hotovo. Pro pevné t jde o O(n) čas a konstantní počet pomocných ukazatelů, bez zásobníku.

Vložení nového uzlu do pozice 1 je místní jako u binárního alternativního threading. Vložení do pozice j>1 navíc potřebuje poslední preorder uzel předchozích podstromů, jehož pokračovací nit se mění. Jeho nalezení může stát lineární čas; samotný počet změněných odkazů je konstantní pro pevné t. Tím se obecně nepřenáší slib konstantní ceny libovolného vložení.

## Rotace bez zásobníku a bez tagů

W se zobecní přímo na cyklickou rotaci t dětských polí a jednoho vnějšího ukazatele Q. Nechť S je sentinel různý od všech uzlů a od null:

```text
P=root; Q=S
opakuj:
    pokud P=null: P,Q = Q,null
    pokud P=S: skonči (Q=root)
    navštiv P
    R=C1(P)
    C1(P),...,C(t-1)(P),Ct(P) = C2(P),...,Ct(P),Q
    Q=P; P=R
```

Silný invariant je přesně binární: podstrom s vnějším pokračováním X se obnoví a vrátí P=X, Q=původní kořen. Jedna rotace otevře první dítě a přesune X do posledního pole, indukce se vrátí; další rotace otevře další dítě. Po t+1 rotacích kořene se všechna jeho pole vrátí do původní polohy. Tím dostaneme Eulerovo pořadí s t+1 návštěvami každého uzlu a obnovu celé paměti. Algoritmus sám neoznačuje, která fáze návštěvy právě probíhá; nelze bez dalšího tvrdit, že umí filtrovat zvolené j-pořadí. Každá z t+1 zbytkových podposloupností návštěv obsahuje každý uzel právě jednou a vzdálenost dvou po sobě vybraných uzlů je nejvýše t+1 hran.

`tary.py` implementuje tento úplný program i předchozí kopii a ověřuje je proti samostatnému rekurzivnímu oraclu pro všechny ternární tvary do 5 uzlů a čtyřární do 4 uzlů. Výsledek je v `results/tary.json`; testy doplňují indukce, nejsou jejich náhradou.

## Počty a kompaktní uložení

Mezi tn dětskými sloty neprázdného stromu je n−1 nenulových, tedy `(t−1)n+1` prázdných. Přidáním listu do každého prázdného slotu dostaneme plný uspořádaný strom stupňů 0 nebo t s tn+1 uzly; smazání všech listů je inverze. Pro původně prázdný strom vznikne jediný list. Obecná identita počtu listů `n_0=1+sum_(k>=1)(k−1)n_k` platí beze změny.

Analogicky k úloze 37 může neprázdný uzel rezervovat blok t sousedních slov pro své děti a list žádný blok. S m nelistovými uzly je celkem `1+t*m` slov, včetně sentinelových prázdných slotů. U pevného t je to nejvýše `tn−t+1`, ale podle stupňů může být výhodnější použít bitovou masku a souvislý blok jen skutečných dětí. Druhá možnost vyžaduje navíc masku a může zdražit vložení přesouváním položek; bez kapacitní podmínky na slovo nelze tvrdit, že se vejde do původního jednoho odkazu a INFO.
