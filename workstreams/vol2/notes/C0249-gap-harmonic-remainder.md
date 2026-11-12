# V2-C0249 — chybějící faktor v harmonickém zbytku

6. listopadu 2026. **Confirmed / low**, §3.5, odpověď 20(b),
tištěná **594**, souborová **606**. Nově zobrazena původní sazba
v `images/vol2-p594.png`, třetí vydání, první dotisk 1997.
Chybný je jeden asymptotický mezikrok; tvrzení úlohy zůstává správné.

Odpověď zavádí

```
p_n = max_{n≤m≤2n−1} m l_m^(1),
S_n = Σ_{k=n}^{2n−1} 1/k
```

a píše `p_n S_n = p_n ln 2 + O(1/n)`. Obecně však z
`S_n = ln 2 + O(1/n)` plyne pouze `p_n S_n = p_n ln 2 + O(p_n/n)`.
Předpoklad omezenosti p_n v zadání ani před tímto krokem není.

## Platný protipříklad a přesná dolní mez zbytku

Vezměme `U_j=1−2^(−j)` pro všechna celá j≥0. Máme U_0=0;
všechny body jsou různé a leží v [0,1). Pro m≥2 jsou mezery

```
1/2, 1/4, …, 2^(−(m−1)), 2^(−(m−1)).
```

Jejich maximum je 1/2, tedy pro n≥2 platí `p_n=(2n−1)/2`.
Přitom bez numerické aproximace

```
S_n−ln 2
 = Σ_{k=n}^{2n−1} ∫₀¹ (1/k−1/(k+t)) dt
 = Σ_{k=n}^{2n−1} ∫₀¹ t/[k(k+t)] dt
 ≥ (1/2) Σ_{k=n}^{2n−1} 1/[k(k+1)]
 = 1/(4n).
```

Proto `p_n S_n−p_n ln 2 ≥ (2n−1)/(8n)`. Zbytek neklesá k nule,
a nemůže tedy být O(1/n), jak vyžaduje vytištěná rovnost.
Protipříklad nepoužívá nulové mezery ani opakované body.

## Oprava zachovávající celou závěrečnou větu

První dvě nerovnosti odpovědi jsou platné:
`1=Σ l_n^(k) ≤ Σ l_(n+k−1)^(1) ≤ p_n S_n`.
Stačí z nich přímo odvodit

```
p_n ≥ 1/S_n = 1/ln 2 + O(1/n).
```

Vybereme m_n∈[n,2n−1] dosahující maximum. Protože m_n≥n,
tyto indexy jdou do nekonečna; protože m_n<2n, zbytek je také
O(1/m_n). Dostáváme přesně závěrečnou dolní mez limsup z úlohy.

Jinou opravou je před sporným krokem oddělit případ nekonečného
limsup, kdy je závěr triviální. Při konečném limsup jsou p_n nakonec
omezené a tištěná velikost zbytku je pak platná. Takové rozdělení
případů ale v odpovědi není uvedeno. Nejde o vyvrácení optimální
konstanty, konstrukce z 20(d) ani minimaxové věty 21(c).

## Kontrola známých oprav

6. listopadu 2026 prohledány všechny relevantní místní vrstvy
`errata/text/all2-prepre.txt`, `all2-pre.txt`, `all2.txt`, `err2.txt`
a `errata/originals/err2.textxt` podle 181, 594, 595, odpovědi 20,
Ramshaw, gap a harmonic; přečteny také sousední stránkové rozsahy.
První vrstva přechází od 593 k 596, druhá od 591 k 608,
současné vrstvy od 586 k 609. Žádná oprava tohoto mezikroku není
uvedena. Oprava 596 je interpunkční změna jiné odpovědi.

Doklad tiráže je `inventory/vol2-frontmatter.txt` ve společném
repozitáři; vydání a posun +12 souhlasí s inventářem.
Pozdější fyzický dotisk a prvenství neověřeny. Žádný výpočet,
census ani email nebyl vytvořen nebo spuštěn.
