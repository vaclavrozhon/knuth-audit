# §4.5.1 — zlomky a jednotlivé argumenty

6. listopadu 2026, V2-X0142. Text 330–333 a odpovědi 638–640
jsou přečteny. `results/sequential-fractions-evidence.json` mapuje
každé tvrzení a všech 16 úloh na již uzavřený argument.

Kanonický zápis, čtyři operace, velikost mezivýsledků, rozšířené
hodnoty, oddělení různých zlomků binárními místy a obě uvedená
číselná tělesa mají obecné důkazy v `rational-basic.md`. Údaj 61 %
má přesný limitní model nezávislých rovnoměrných jmenovatelů;
důkaz věty D již existuje v `gcd-probability.md` a přebíráme jej.
Nejde o rovnoměrnou relativní aproximaci libovolného obdélníku.

Mediant rounding, sousedé, oba velké počty i kódování formátů jsou
v `rational-slash.md`. Příklady nejsou důkazem univerzální převahy
nad floating point. Vlastní propojená racionální aritmetika má
důkazy hodnotových a paměťových invariantů v `rational-linked.md`.
Úlohy 15 a 16 jsou provedené experimenty s výslovným rozsahem,
nikoli výzkumné otázky o neznámém optimu. Překladač podporuje
uvedený skalární podjazyk; intervalová varianta má obecnou záruku
obsažení a přiznanou ztrátu závislostí. Viz `rational-experiments.md`.
Žádný program, census ani číselná reference se znovu nespouštěly.

Závažnost čtyř starších položek nyní odpovídá skutečnému dopadu:

- C0113 **confirmed/low**: maximum mezivýsledku má výjimku N=2;
  pro N≥3 je tištěná formule obecně dokázána.
- C0114 **candidate/low**: doslovně nezměněná rutina stále odmítne
  nulového dělitele. Zamýšlené rozšířené operace jsou konzistentní;
  sporný je rozsah formulace o nezměněném algoritmu.
- C0115 **confirmed/low**: nejmenší slash formáty potřebují
  kvalifikaci nulové oblasti. Praktické formáty nejsou dotčeny.
- C0116 **confirmed/low**: Möbiova suma potřebuje kladné souřadnice.
  Pro obdélník obsahující nulu může dát nesprávný počet; použití
  při počítání kladných čitatelů v úloze 13 je správné.

Původní sazba a relevantní errata jsou doloženy v předchozích
blocích. Historické prameny, prvenství a přesný rozsah přečtených
článků zůstávají omezené podle `rational-context.md`; běžné
bibliografické výjimky nejsou nové matematické mezery.

Všech 16 úloh má argument nebo splněný vymezený experiment.
Strana 639 zůstává partial kvůli výkladu C0114, 333 a 640 kvůli
začátku následující sekce. Strana 638 je nyní spárována přes obě
sekce. Další kurzor: 333/file345, §4.5.2, největší společný dělitel.
