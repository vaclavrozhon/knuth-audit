# V2-C0153: záměna proměnné v dodatku AKS

**Confirmed, pouze záměna proměnné.** Dodatek z 28. 4. 2005 k §4.5.4,
str. 396, Theorem A, uvádí kongruenci polynomů v neurčité `z`, ale
následný rozsah `0 <= z <= sqrt(r) lg n` omezuje znovu `z`.
Má omezovat celočíselný parametr `a`. Jinak `a` zůstává nekvantifikované
a polynomiální kongruence se zaměňuje s vyhodnocováním polynomu.

V [původní sazbě errata, PDF22](../images/all2-prepre-primality-p22.png)
je opravdu `z`, nejde o chybu OCR.
[Granville 2005, str. 4](../images/granville-2005-primality-p2.png)
explicitně kvantifikuje `a` a rozlišuje kongruenci polynomů od
kongruence jejich hodnot. Totéž činí krok 5
[AKS 2004, str. 784](../images/agrawal-kayal-saxena-2004-p4.png).
Přidání `a=0` v Knuthově formulaci nevadí: tato kongruence je identita.

Samotné `a=0` ovšem nemůže charakterizovat prvočísla. Například
`n=9`, `r=29` splňuje `gcd(n,r)=1` a `ord_r(n)=14>(lg 9)^2`:
`9^7=-1 mod29`, `9^2=23 mod29`, `9^14=1 mod29`, zatímco
`9^3<2^10` dává `(lg9)^2<100/9<14`. Pro `a=0` je kongruence
triviální. Toto ilustruje význam chybějící kvantifikace; není to
protipříklad k větě po nahrazení `z` za `a`.

**Rozsah nálezu:** Granville navíc předpokládá `r<n`, vylučuje
netriviální mocniny a vyžaduje nepřítomnost prvočinitele `<=r`.
Knuth tyto podmínky neuvádí. Z pouhého rozdílu formulací neplyne,
že jsou nezbytné pro pravdivost jeho silnějšího tvrzení. Tato otázka
je nadále otevřenou částí auditu; není zahrnuta do potvrzení C0153.
Následně byl dokončen vlastní standardní důkaz i časové meze v
[primality-aks.md](primality-aks.md); otevřené hypotézy eviduje C0155.
Celý originál AKS 781–793 byl vizuálně přečten.

Všechny čtyři vrstvy errat a aktuální `err2.textxt` prohledány
3. 11. 2026 podle strany, Theorem A, AKS, Granville a kongruence.
Pozdější výskyty Theorem A patří jiným oddílům; oprava této proměnné
nenalezena. Fyzický nejnovější dotisk a priorita nálezu nejsou
ověřeny. Návrh hlášení zůstává neodeslán.
