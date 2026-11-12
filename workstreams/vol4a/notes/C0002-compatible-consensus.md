# V4A-C0002 — kompatibilita nezaručuje generalized consensus

Stav **candidate**, nízká priorita. Souvislost se známým erratem odpovědi540
je otevřená; nejde o tvrzení o novosti ani o novou kartu známé chyby odpovědi.

Místo: §7.1.2, tištěná120 / file137, odstavec „Decomposition of partial
functions“, věta začínající „For if u1, ..., ul are mutually compatible“.
Text odkazuje na generalized consensus definovaný v §7.1.1–32, str.83/file100.
Původní sazba obou míst přečtena a uložena ve výřezech s vyšším rozlišením.

## Přímý příklad

Vezměme dvě kompatibilní podkrychle dvoukrychle:

    u = 0* = {00,01}, v = *0 = {00,10}.

Jejich sjednocení je {00,01,10}. Jeho jediné maximální podkrychle jsou u a v;
každá je tedy obsažena v jednom původním členu. Podle definice32(a) zde
generalized consensus neexistuje, protože by nesměl být obsažen ve sjednocení
zbývajících členů po odstranění kteréhokoli členu. Totéž plyne z31(a):
kompatibilní dvojice nemá žádný protilehlý pár 0/1, ale pro existenci konsensu
je potřeba právě jeden. Není použit okrajový případ n=0/1 ani duplicita vstupů.

Pro daný důkaz stačí průnik kompatibilních podkrychlí; zde je to {00}.
Obecně v každé souřadnici zvolíme jedinou předepsanou hodnotu, pokud existuje,
a libovolnou hodnotu jinak. Párová kompatibilita brání konfliktu. Tím vznikne
společné doplnění všech sloupců jedné nezávislé množiny. Samotná ekvivalence
s bipartitností grafu tedy zůstává platná.

## Errata a důvod nejistého stavu

Prohledány relevantní historické a aktuální vrstvy `all4a-pre`, `all4a`,
`err4a`, `all4f0`, `err4f0` podle stran83/120/540, úlohy/odpovědi32 a výrazů
consensus/compatibility (včetně OCR bez c). Na str.120 nalezena pouze oprava
odkazu na §7.4.1.2 z11.11.2021.

**Příbuzné známé erratum existuje:** all4a-pre, str.540 řádky2–3 odpovědi32(a),
19.6.2011, mění „the generalized consensus if and only if this subcube is
contained ...“ na „the only subcube that could possibly be a generalized
consensus“. Původní odpověď také prohlédnuta (file557). Jde o stejný problém
existence objektu. Přímé přenesení této opravy do výše uvedené věty na str.120
v evidovaných erratech není uvedeno. Candidate zachovává právě tuto nejistotu
rozsahu již známé opravy; potvrzenou novou chybu zatím neoznačujeme.

Doklady: `images/file137-detail.png`, `images/file100-detail.png`,
`images/file557.png`; původní PDF/OCR ve stejnojmenných sources.
Žádný výpočetní program nebyl potřeba. Doporučená minimální textová úprava:
nahradit odkaz na generalized consensus neprázdným průnikem a společným
doplněním kompatibilních podkrychlí.

## Zpřesnění po úplném důkazu 32, X0071

Proof-042, P0670/P0671, dokládá přesně, že známá oprava nemění definici
a neřeší doslovný odkaz p120. Zbývající nejistota není rozsah opravy:
čtyřsymbolová souřadnicová operace z odpovědi dává u kompatibilní rodiny
právě neprázdný průnik. Pokud ji p120 neformálně nazývá konsensem
i bez existence objektu definovaného v zadání, zamýšlená konstrukce
je správná. Candidate je proto ponechán jen pro tento rozdíl názvu
a definice; nejde o nový výskyt již opraveného tvrzení iff na p540.
Originál p120 znovu prohlédnut, pět vrstev i obě F1 prohledány; bez
nového programu. Bipartitní tvrzení zůstává platné.
