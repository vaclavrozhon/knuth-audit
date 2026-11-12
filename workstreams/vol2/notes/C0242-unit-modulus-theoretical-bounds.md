# C0242 — jednotkový modul v teoretických mezích

6. listopadu 2026. Nízká závažnost, `confirmed` v dostupném prvním
dotisku. Dva související okraje v §3.3.3 evidujeme společně; nejde
o selhání běžných generátorů nebo Dedekindova algoritmu.

## Věta P, původní strany 80 a 82

Definice na straně 10 připouští celé m > 0 a 0 ≤ a,c,X0 < m.
Proto m=1, a=c=X0=0 splňuje předpoklady a má maximální periodu 1.
Ve větě P není uvedeno m > 1. Její hlavní vzorec je i zde správný:

```text
d = gcd(a−1,m) = gcd(−1,1) = 1,
r = (2(c mod d)−d)/(2m) = −1/2,
Pr(X[n+1] < X[n]) = 0 = 1/2+r.
```

Následující ostrá mez |r| < d/(2m) však tvrdí 1/2 < 1/2.
Ve druhém důkazu na straně 82 se v (11) zahodí delta člen,
protože (x−s(x))/m má údajně vždy být necelé. V jediném stavu
je tento argument 0; levá strana (11) je 0 a pravá 1/2.

Stačí pro tento důkaz a ostrý závěr vyžadovat m > 1, případně
samostatně ošetřit m=1 a v závěru použít neostrou mez. Pro m>1
má plnoperiodický generátor jediný cyklus délky m a žádný pevný
bod; také 1 ≤ c mod d ≤ d−1. Důkazy knihy tedy pro netriviální
obor fungují.

## Odhad počtu kroků, původní strana 87

Věta D výslovně dovoluje 0 < h ≤ k. Při h=k=1,c=0 má její
tabulka m1=m2=1,m3=0 a t=1. Samotný vzorec D správně vrátí
sigma(1,1,0)=0. Navazující tvrzení t ≤ log_phi(k) ale dává 1 ≤ 0.

Pro k≥2 a nesoudělné 0<h≤k je automaticky h<k. Eukleidův
rozklad má poslední podíl alespoň 2, takže zpětná indukce dává
k≥F[t+2]>phi^t pro t≥1. Uvedená logaritmická mez pak platí.
Stačí výjimka k=1; algoritmus ani jeho asymptotická složitost
se nemění.

Čistě pólový rozklad na straně 85 také potřebuje h=k=1 vyřídit
samostatně: racionální funkce je tehdy konstanta 1. To zde
nepočítáme jako další nález reciprocity; její obě strany jsou 0
a samostatná kontrola základního případu důkaz doplní.

## Evidence a meze závěru

Přímo přečteny původní obrazy 10,80,82,87; souborové strany jsou
22,92,94,99. Přesná aritmetika obou protipříkladů je v
`results/sequential-unit-theory-edges.json`. Prohledány všechny
čtyři řady errat a aktuální TeX dne 6.11.2026, včetně slovních
odkazů mimo dotčené stránky. Žádná odpovídající oprava nalezena.
Výřez a hashe: `sources/sequential-2026-11-06/theoretical-tests-errata.json`.

Toto je potvrzení matematického okraje v naší sazbě, nikoli
ověření nejnovějšího fyzického dotisku, prvenství nebo Knuthova
souhlasu. Korespondence nevznikla.
