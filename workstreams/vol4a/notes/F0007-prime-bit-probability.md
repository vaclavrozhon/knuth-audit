# V4A-F0007 — pravděpodobnost prvočísla v nbitovém řetězci

6. listopadu 2026. **Confirmed, low.** Komentář k odpovědi
§7.1.1–52, p544/file561, věta začínající „in game (d)“.
Původní sazba images/proof-file561.png; zadání hry(d) na
p86/file103 definuje f(x)=[(x_1…x_n)_2 je prvočíslo].

Kniha u rovnoměrného náhodného výběru všech n bitů uvádí
Θ(1/log n). Správný řád je **Θ(1/n)**. Jde o doprovodnou
pravděpodobnost; žádný výsledek strategické herní tabulky
se z tohoto nálezu nevyvozuje.

## Přesná pravděpodobnost a horní mez — P0767

Bitová slova délky n, včetně počátečních nul, jsou v bijekci
s celými čísly 0,…,2^n−1. Proto je pravděpodobnost přesně

    p_n = π(2^n−1)/2^n.

Pro n≥2 je 2^n složené, takže π(2^n−1)=π(2^n).
K vyvrácení vytištěné dolní meze Θ(1/log n) stačí následující
elementární horní mez; prvočíselná věta není potřeba.

Označme θ(x)=Σ_{p≤x} ln p. Pro každé celé m≥1 součin
prvočísel v intervalu (m,2m] dělí binom(2m,m): každé takové
prvočíslo se v (2m)! objeví jednou a v obou m! ani jednou.
Z binom(2m,m)≤2^(2m) proto plyne

    θ(2m)−θ(m) ≤ 2m ln 2.

Sečtením pro m=1,2,4,…,2^(n−1)
dostaneme θ(2^n)≤(2^(n+1)−2)ln2.
Prvočísel nejvýše 2^(n/2) je nejvýše 2^(n/2); každé větší
prvočíslo přispívá do θ alespoň (n/2)ln2. Tedy

    π(2^n) ≤ 2^(n/2) + 2θ(2^n)/(n ln2)
            ≤ 2^(n/2) + 4·2^n/n,

a tudíž p_n=O(1/n). Proto p_n log n→0 pro každou pevnou
bázi logaritmu větší než 1. To přímo vylučuje Θ(1/log n).

## Opravený řád a přesné převzetí dolní meze

Dolní elementární Chebyshevova mez už má uzavřený argument
ve workstreams/vol2/notes/discrete-log.md, oddíl 4:
centrální binomický koeficient dělí lcm(1,…,2m), takže
ψ(2m)≥2m ln2−ln(2m+1); rozdíl ψ(x)−θ(x)≤sqrt(x)ln x
dává θ(x)≥a x pro pevné a>0 a dostatečně velké x.
Odtud π(x)≥θ(x)/ln x≥a x/ln x.

Přebíráme právě tento analytický argument, nikoli jakýkoli
výpočet diskrétního logaritmu. Při x=2^n dává p_n=Ω(1/n).
Spolu s horní mezí tedy správná náhrada je Θ(1/n).
Žádná nová tabulka prvočísel, program nebo census nebyly potřeba.

## Sazba, rozsah a errata

Význam n se v obou sousedních větách nemění: jde o počet bitů,
jak potvrzuje také uvedená pravděpodobnost F_(n+2)/2^n pro hru(c).
Řád 1/log N by byl přiměřený číselné horní hranici N=2^n,
ale kniha uvádí n, nikoli N.

Relevantní all4a-pre, all4a, err4a, all4f0 a err4f0 byly
prohledány podle answer52, p544, logaritmu a obsahu komentáře.
Známé změny na p544 se týkají odpovědí54 a55; oprava tohoto
komentáře není uvedena. Starší F0 „answer52, p190“ je jiná
sekce o velikosti obvodů a není touto opravou.
Původní zadání i odpověď byly zobrazeny. Fyzický exemplář
nebyl porovnán a není tvrzena priorita nálezu.

Jediná error lokace: file561 / printed544, komentář k52(d).
Zadání, herní tabulka ani Fibonacciho odhad nejsou tímto
argumentem označeny jako chybné.
