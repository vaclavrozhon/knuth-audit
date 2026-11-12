# V2-C0089: horní mez intervalového součtu v erratu2020

**Confirmed.** Erratum28.6.2020 pro str.241, řádky2–3,
na straně6 souboru `all2-pre`. Definice intervalového sčítání
na240, pokračování na241 i originál errata znovu vizuálně přečteny.

Aktualizované intervaly jsou

```text
N=[(24,.60221407)..(24,.60221408)],
h=[(−33,.66260701)..(−33,.66260702)].
```

Definovaná operace sčítá dolní meze se zaokrouhlením dolů
 a horní se zaokrouhlením nahoru. Horní mezN je reprezentovatelná
hodnotaN_hi=.60221408·10^24. Jelikož h_hi>0, musí platit

```text
N_hi < N_hi+h_hi < N_hi+10^16.
```

Následující osmiciferné číslo je právěN_hi+10^16,
tedy(24,.60221409). Horní směrované zaokrouhlení je proto toto
číslo. Erratum ponechává horní mez(24,.60221408), která je menší
než přesný součet dvou dovolených koncových vstupů.

Správná intervalová identita je

```text
N⊕h=[(24,.60221407)..(24,.60221409)].
```

Dolní mez a vytištěný interval součinu jsou správně. Původní
příklad1997 i oprava1999 horní konec při sčítání správně zvětšovaly
o jednu poslední cifru; chyba vzniká v nové náhradě2020.

**Rozsah nálezu:** užší vytištěný interval může obsahovat součet
přesných skutečných konstantSI, pokud se využije dodatečná informace
mimo intervaly. Nález se týká hodnoty definované intervalové operace
nad uvedenými intervaly, ne nesprávnosti fyzikální konstanty.

Všechny čtyři vrstvy errat a aktuálníTeX prohledány2.11.2026 podle
240/241, obou číselných konců a intervalového sčítání; pozdější oprava
nenalezena. Fyzický tisk a prvenství neověřeny; neodesláno.
Přesný výpočet uložen v `results/intervals.json`, reprodukce
`verify_intervals.py`. Důkaz sazby:
`images/accuracy-errata-all2-pre-6.png` a `images/vol2-p240.png`.
