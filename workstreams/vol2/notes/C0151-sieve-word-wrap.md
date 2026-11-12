# V2-C0151: návrat indexu počítá bity místo slov

Stav: **confirmed**. §4.5.4, str.390, komentáře u INC1 M1 a INC1 M2.
Pole podle odstavce nad programem obsahuje L_i=lcm(m_i,30) bitů,
tedy W_i=L_i/30 slov. Registr rI1 indexuje slova S'[i,rI1]
a po každém bloku30 hodnot se zmenšuje o1.

Komentáře však při záporném indexu přičítají L_i.
Správně musí přičíst W_i. Pro m_i=7 jde o210 bitů a7 slov.
Z indexu0 po DEC1 dostaneme -1; vytištěný návrat dává209,
který je mimo sedmislovné pole. Správný další index je6.

Přesný rozvrh bitů, invariant kruhového slovního indexu a
161 577 kontrol celých bloků včetně 9315 návratů jsou
v `notes/factoring-fermat.md` a `results/factoring-fermat.json`.
Základní myšlenka hromadného AND je správná.
Symbolické konstanty M1,M2 mají být počty slov; nález je
přesně v komentářích, které jim přiřazují počet bitů.

Původní strana390 vizuálně přečtena. Ve všech čtyřech vrstvách
errat a současném TeXu nenalezena oprava této jednotky.
Oprava19.5.2005 nahrazuje pouze znak logického AND.
Kontrola3.11.2026; fyzický poslední tisk a prvenství neověřeny.
Draft neodeslán.
