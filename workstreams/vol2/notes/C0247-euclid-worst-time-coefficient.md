# V2-C0247 — koeficient nejhoršího času programu A

6. listopadu 2026. **Confirmed / low:** číselný koeficient ve srovnání
časů na tištěné straně 340 (file352). Program A ani jeho přesná cena
19T + 6 na straně 337 nejsou chybné. Sazba obou stran byla přečtena;
nejde o OCR. Vedle nejhoršího času binárního programu se pro A uvádí
26.8N + 19, kde 1 <= u,v < 2^N.

## Přesný důkaz

Pišme F_0 = 0, F_1 = 1 a F_(j+2) = F_(j+1) + F_j. Pro k >= 2 má
vstup (u,v) = (F_k,F_(k+1)) právě k dělení: nejprve nulový podíl,
pak k−2 jedniček a nakonec dvojku. Obecný důkaz minimálních vstupů
je věta F, nezávisle doložená v euclid-text.md. Proto pro celé N >= 1
platí přesně

    max T(u,v) = max { k >= 1 : F_(k+1) < 2^N },
    max čas A = 19 max T + 6.

Případ N = 1 ověří přímo jediný vstup (1,1). Pro větší N dosažení
zajišťují uvedené Fibonacciho vstupy; obrácené pořadí nemůže být horší.
Z F_k = (phi^k − (−phi)^(-k))/sqrt(5), phi = (1+sqrt(5))/2, plyne

    max čas A = (19 ln 2 / ln phi) N + O(1),
    19 ln 2 / ln phi = 27.3679817… .

Zaokrouhlený vedoucí koeficient je tedy 27.4, nikoli 26.8.
Číslo 26.8 nelze získat správným zaokrouhlením této konstanty.
Neprohlašujeme 27.4N + 19 za nový přesný vzorec maxima; přesný vzorec
je celočíselný Fibonacciho zápis výše.

Konečný doklad v běžném rozsahu MIX: N = 28, u = 165580141,
v = 267914296 < 268435456. Počet dělení je 41 a cena je 785 cyklů;
vytištěný výraz dává 769.4. Menší příklad N = 10, (610,987) potřebuje
15 dělení a 291 cyklů, proti vytištěným 287. Pro N = 30 se náhodou
obě hodnoty rovnají 823; tato shoda neplatnost obecného koeficientu
neodstraňuje. Asymptotický argument se týká standardního abstraktního
modelu jednoho slova, ne tvrzení o neomezeném fyzickém slově MIX.

Pět cílených celočíselných stop je v results/sequential-euclid-followups.json.
Byly spočteny s nice15; žádný census ani starý verifikátor se nespouštěl.
Desetinný výpis konstanty je ilustrace; důkaz je přesný vzorec s phi.

## Errata a hranice závěru

Prohledány all2-prepre, all2-pre, all2, err2 a aktuální err2.textxt
podle 337–341, čísel 26.8/27.4 a tématu. V prvních historických
erratech přecházejí věcné opravy z 335 na 343; další vrstva na 339
mění jen komentář k množství kódu. Oprava tohoto koeficientu nenalezena.
Vyhledání na webu neposkytlo další relevantní primární opravu.

Jde o malou číselnou vadu výkonnostního srovnání, nikoli o nesprávný gcd,
neplatnost Fibonacciho věty nebo důvod přehodnocovat hlavní algoritmus.
Poslední fyzický dotisk ani prvenství nejsou ověřeny. Zpráva se neodesílá.
