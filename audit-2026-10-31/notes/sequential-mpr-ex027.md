# D129 — celá MPR27, nehomogenní kumulativní součet

6. listopadu 2026. Celá původní p15/file35 byla zobrazena a čtenářsky
rozdělena na úlohy27–40. Tento záznam uzavírá pouze27 a její odpověď
na p374/file394. Zobrazen také Pre-Fascicle5A p15/file21 a p31/file37.
Čtení ostatních zadání samo neznamená jejich matematické uzavření.

Přebíráme plně dokázaný model D127: nezávislé bity X_j s parametry
p_j∈[0,1], q_j=1−p_j, a P_s(k)=P(X₁+⋯+X_s=k). Index s označuje
právě prvních s bitů. P₀(0)=1 a P_s(k)=0 mimo0≤k≤s.

## Celý rozklad podle určené nuly

Pro celé0≤m<n položme r=n−m≥1. Počet nul je T=n−∑X_j,
jejich pozice J₁<⋯<J_T. Událost ∑X_j≤m je přesně T≥r.
Na ní je r-tá nula jednoznačně na některé pozici s=r,…,n.
Stejně jako v úplném důkazu D125 máme ekvivalenci

    {T≥r,J_r=s} = {X₁+⋯+X_{s−1}=s−r, X_s=0}.

Suffix je neomezený. Nezávislost prefixu a X_s dává
pravděpodobnost P_{s−1}(s−r)q_s, bez dělení pravděpodobnostmi.
Po úplném disjunktním sečtení a substituci k=s−r získáme

    ∑_{k=0}^m P_n(k)
       =∑_{k=0}^m P_{n−m−1+k}(k)(1−p_{n−m+k}).

To je přesně tištěná formule se zobecněným binomickým koeficientem.
Pro každý její člen jsou prefixový index n−m−1+k≥0 a index
samostatného bitu1≤n−m+k≤n. Všechny součiny existují i při
p_j=0 či1, a rozklad zahrnuje všechny přípustné vzory právě jednou.
RHS sice používá dané pořadí parametrů, ale argument funguje pro
jakékoli pevné pořadí; výsledek je stejná symetrická pravděpodobnost
celkového počtu jedniček.

## Okrajové případy a přesný rozsah tištěné sumy

Při m=0 zbývá P_{n−1}(0)q_n=∏_{j=1}^nq_j, přesně pravděpodobnost
samých nul. Při m=n−1 je r=1 a formule se změní na

    ∑_{k=0}^{n−1}(∏_{j=1}^k p_j)(1−p_{k+1})
      =1−∏_{j=1}^n p_j,

což je samostatná teleskopická kontrola pravděpodobnosti, že nenastanou
samé jedničky. Pro n=1,m=0 vychází q₁.

Pro m≥n je kumulativní pravděpodobnost přímo1, pro m<0 přímo0.
Při n=0 je tedy rovna1 pro m≥0. To jsou samostatné triviální větve.
Zapsaná prefixová formule řeší netriviální rozsah0≤m<n; nelze do
ní mechanicky dosadit m=n a předstírat definované P_{−1}(0) nebo p₀.
Takové nové parametry nezavádíme. V zadání27 není tištěné univerzální
tvrzení s výslovně zahrnutým m=n; odpověď dává vlastní netriviální
výraz a koncová větev plyne ihned z definice rozdělení. Tento
kontextový rozsah se nepovyšuje na nový nález.

Při společném parametru p_j=p má prefixový koeficient tvar
binom(r+k−1,k)p^k(1−p)^{r−1}. Násobení dalším1−p tedy dává
přesně alternativní vzorec23, s exponentem r=n−m. To ověřuje
i požadovanou analogii, včetně všech horních a dolních indexů.

## Errata a další hranice auditu

Šest vrstev errat a tři TeX zdroje zkontrolovány podle původních
i fasciklových stran a čísla27. Změna Fascicle5 p229 odpověď27
patří oddílu Dancing Links, nikoli MPR; sousední MPR24 už má E123.
Žádná relevantní oprava či nový rozpor. Doklad je
`results/sequential/mpr-027-cumulative-errata.json`.
Bibliografické výjimky pro tuto úlohu nejsou.

Původní file35 zůstává partial, pouze27 je matematicky uzavřena.
Na file394 jsou úplné zdejší odpovědi24–27;28 zatím otevřena.
Již doložená F016 a staré výsledky P028 zůstávají zachovány.
P028 je do doplnění každého mezikroku28–29 veden jako partial,
aniž by se opakovaly jeho úspěšné konečné testy.
