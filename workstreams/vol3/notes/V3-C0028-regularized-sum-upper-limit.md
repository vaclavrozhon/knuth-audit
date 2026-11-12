# V3-C0028 — chybějící konečná mez pomocného součtu

**Confirmed / low**, 2026-11-07. Originál tištěná636/file647,
§5.2.2, odpověď44, přesná rovnost pro r_{−1}(m) na čtvrtém
řádku odpovědi. Zobrazen také původní129–130 a erratum2021
v`images/bubble-all3-pre-check-11.png`.

Na129 je r_{−1}(m)=Σ_(1≤t<m)e^(−t²/(2m))/t. Na130 se správně
zavádí

    f_{−1}(x)=√(2m)(e^(−x²/(2m))−1)/x, f_{−1}(0)=0,

a hlavní text výslovně pracuje s konečným součtem0<t<m.
Odpověď44 na636 však v přesné rovnosti

    r_{−1}(m)=H_{m−1}+(1/√(2m)) Σ_(t>0) f_{−1}(t)

horní mez vynechává. Tento nekonečný součet neexistuje jako
konečné číslo. Stačí platný m=2: po vynásobení1/√(2m) jsou
jeho členy(e^(−t²/4)−1)/t. Pro každé celé t≥2 jsou≤−1/(2t),
protože e^(−1)<1/2. Částečné součty tedy klesají k−∞,
zatímco levá strana je kladné konečné e^(−1/4). Přičtení
konečného H_1=1 divergenci neodstraní. Obecně má f stejný
záporný harmonický ocas pro každé pevné m>0.

Oprava je přesně **Σ_(0<t<m)**. Potom se konečné harmonické
členy vyruší po jednom a rovnost platí identicky, včetně m=2.
Nelze použít rozšíření Gaussian sumy na všechna t>0:
po odečtení1 je pomocný ocas harmonický. Žádná regularizovaná
konvence nekonečného součtu není v tomto argumentu definována.

Jde o lokální chybu meze v pomocné rovnosti. Hlavní text130
má správnou konečnou mez; asymptotická řada r_{−1} i výsledek
W_n s49/36 jsou platné. Jejich vlastní důkaz se ukládá odděleně
do `notes/exchanging-proof-bubble-w-128-130-43-44.md`.
Tento protipříklad sám žádný z těchto výsledků nevyvrací.

Pět vrstev dokumentuje
`sources/regularized-sum-upper-limit-errata-review.json`.
Known2021 odstranění−δ_{k0} na prvním řádku44, změna meze
Eulerovy formule(36), doplnění f_{−1}(x) a starší úpravy
konstant se této nekonečné sumy nedotýkají. Žádný matematický
program ani test; fyzický výtisk nebyl kontrolován.
