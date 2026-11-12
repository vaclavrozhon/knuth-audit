# V3-C0012 — převrácená konstanta počtu porovnání

Confirmed, medium. Odpověď §5.2.2-29, s. 633 / file 644, tvrdí
asymptotiku α^−1 n ln n, ale současně definuje
α=−1/∫_0^1 (f(x)+f(1−x)) x ln x dx. Jedno převrácení je navíc.

Pro běžný quicksort na náhodné permutaci má relativní poloha pivota
rovnoměrné limitní rozdělení, tedy f(x)=1. Integrál je
2∫_0^1 x ln x dx=−1/2, α=2, a tištěné tvrzení dává (1/2)n ln n.
Přitom pro n>M platí rekurence C_n=n+1+(2/n)Σ_(j<n) C_j, která dává
C_n=2n ln n+O(n): odečtením sousedních rovnic dostaneme přírůstek
C_n/(n+1) − C_(n−1)/n = 2/(n+1), pro n≥M+2.
Stejnou hlavní konstantu má přesný vzorec (24) na s. 120 pro pevné M.
Věta se výslovně týká také quicksortu, takže příklad splňuje její kontext.

Oprava: při zachování definice α má být α n ln n; alternativně zachovat
α^−1 n ln n a definovat α jako záporný integrál bez převrácení.

Sazba file 644 prohlédnuta. Všech pět vrstev errat v
sources/exchanging-errata-review.json bez odpovídající opravy.
Historická oprava s. 609 (1. 3. 1979) mění jiné řádky odpovědí 24/29,
řešení diferenciální rovnice; tuto závěrečnou konstantu nemění.
Bibliografická atribuce van Emdenovi se zde neposuzuje. Prvenství ani
fyzický výtisk neověřeny.
