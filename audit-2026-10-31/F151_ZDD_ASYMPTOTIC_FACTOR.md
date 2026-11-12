# F151: v asymptotickém počtu uzlů chybí odmocnina

3. listopadu 2026; §7.2.2.1, hlavní text str.121, autorský draft str.57.
Oba obrazy uvádějí přibližně `(N/5) F_(N+1)`. Správně je

    (N/sqrt(5)) F_(N+1),       N sudé, N→∞.

Odpověď255 má správný uzavřený tvar

    V_N=((N−5)F_(N+1)+2(N+1)F_N)/5.

Po dříve doložené opravě F079 je počet uzlů `Z_N=V_N+3`.
Protože `F_N/F_(N+1)→1/phi` a `1+2/phi=sqrt(5)`, platí

    Z_N/(N F_(N+1)) → (1+2/phi)/5 = 1/sqrt(5).

Poměr skutečného počtu k vytištěné aproximaci tedy směřuje k `sqrt(5)`,
nikoli k1. Oprava `+2` na `+3` z F079 to neřeší; jde o jinou chybu.
Řád `Theta(N² F_N)` pro čas zůstává správný.

Starší [ZDD_COUNT_NOTES.md](ZDD_COUNT_NOTES.md) říkají, že „asymptotika
zůstávají“. To platí pro řád růstu a pro důsledek opravy F079, ale tato
věta nesmí být čtena jako ověření vytištěného koeficientu N/5. Tento
datovaný doplněk upřesňuje starý záznam; starý důkaz ani program neměníme.

Přesná aritmetika pro N100 a N1000 je v
[source-checked.json](results/zdd251_260/source-checked.json). Nevznikl
žádný nový výčet párování. Číselné příklady knihy 10 228 uzlů pro K16
a zaokrouhlených48 milionů pro K32 jsou správně; druhý přesný počet je
47 786 403.

Zdrojové obrazy: [kniha](images/zdd251-260-original-141.png),
[autorův draft](images/zdd251-260-draft-63.png).
V šesti relevantních vrstvách errat odpovídající oprava nenalezena;
podrobnosti v [errata-search.json](results/zdd251_260/errata-search.json).
Fyzický výtisk neověřen. Potvrzení neznamená doložené prvenství.
