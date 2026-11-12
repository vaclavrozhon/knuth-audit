# V2-C0084: výjimka pro jednocifernou ternární aritmetiku

**Confirmed v dostupném textu a povoleném modelu zaokrouhlení.**
§4.2.2-15, odpověď614, včetně opravy14.9.2019. Nejde o selhání běžné
binární nebo desítkové aritmetiky. Novější fyzický tisk/prvenství
neověřeny; návrh hlášení neodeslán.

b označuje základ, p počet cifer, R nejbližší normalizovanou plovoucí
hodnotu. Použijeme b=3,p=1 a zaokrouhlení polovin na sudou poslední
cifru. To je dovoleno AlgoritmemN, který pro liché základy výběr na
polovině neomezuje. Stejný důkaz funguje pro poloviny směrem od nuly.
Předpokládáme obvyklou podmínku, že všechny operace jsou definovány.

Odpověď tvrdí, že při b>2 existují v s R(R(2v)/2)≠v, takže vypočtený
střed nemusí ležet mezi konci intervalu. Pro uvedený formát však platí
**R(R(2v)/2)=v pro všechna plovoucí v**:

- Pro v=0 je to triviální.
- Pro v=1 je R(2)=2 a R(2/2)=1.
- Pro v=2 je R(4)=3, neboť sousedé jsou3 a6; dále R(3/2)=2,
  neboť sousedé1 a2 jsou stejně blízko a2 má sudou cifru.

Každé další nenulové číslo je ±3^e nebo ±2*3^e. Zaokrouhlení komutuje
se změnou znaménka a násobením mocninou3, takže dva případy pokrývají
celý formát. Monotonie R potom pro libovolné u<=v dává

```text
u = R(R(2u)/2) <= R(R(u+v)/2) <= R(R(2v)/2) = v.
```

Tedy protipříklad středu v tomto formátu vůbec neexistuje. Oprava:
z tvrzení pro b>2 vyjmout b=3,p=1 (případně explicitně určit v této
výjimce jiné zaokrouhlování). Při polovinách na liché skutečně
R(3/2)=1 a u=v=2 poskytuje protipříklad. Právě proto je potřeba
výslovně uvést použitou konvenci.

Pro b>=4 nebo b3,p>=2 obecné selhání opravdu nastává; důkaz pomocí
b^p−1 a b^p−2 je v notes/accuracy-basic.md, oddíl5. Související
výjimka b3,p1 v odpovědi6(b) také závisí na polovinách; nepřidáváme
ji jako samostatný nález.

Originály215,217,237,244 a614 vizuálně přečteny. Všechny čtyři řady
errat prohledány2.11.2026 podle614,15,midpoint a souvisejících míst.
Oprava14.9.2019 nahrazuje argument neprostotou zdvojení podmínkou
R(R(2v)/2)≠v, ale nevylučuje b3,p1. Její sazba je v
images/accuracy-errata-all2-pre-13.png. Další relevantní změna nebyla
nalezena. Konečný doplněk důkazu ověřuje2738 dvojic pro obě uvedené
konvence; results/accuracy-basic.json, blok ternary_midpoint_boundary.
