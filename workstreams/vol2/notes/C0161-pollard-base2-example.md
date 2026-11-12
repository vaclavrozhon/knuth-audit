# C0161: pevná báze 2 selhává na slibovaném příkladu metody p−1

**Stav:** confirmed v dostupném skenu, §4.5.4, úloha 19
na str. 413 a odpověď na 661; třetí vydání, první dotisk 1997.

Úloha říká, že metoda odhalí druhý největší prvočinitel
p=23528569104401 čísla N=2^214+1 z (15). Správně uvádí
p−1=2^4*5^2*67*107*199*41231. Odpověď však předepisuje
pevnou bázi a1=2. Její první fáze vypočte
A=2^E mod N, E=lcm(1,...,1000).

Protože 428|E a 2^428=1 modulo N, vyjde A=1. Všechna
gcd(A^q−1,N) jsou N, stejně jako gcd všech dávek. Žádný
vlastní faktor nevznikne.

Tentýž problém platí po odstranění známých faktorů pro
n6=8174912477117*23528569104401 z 393. Modulo obou jeho
prvočinitelů má báze 2 stejný přesný řád 428, takže pro
libovolný exponent d je gcd(2^d−1,n6) jen 1 nebo n6.
Rozdělení dávek ani kontrola mezikroků tento příklad nespraví.

Báze 3 naopak při stejných hranicích dává

    gcd(3^E−1,n6)=1,
    gcd(3^(E*41231)−1,n6)=23528569104401.

Místní oprava je použít pro tento příklad bázi 3 a v obecném
postupu připustit změnu báze při neúspěchu. Nejde o chybu
Fermatovy věty ani vyvrácení metody p−1.

Sazba 392, 393, 413 a 661 byla zobrazena. Všechny čtyři vrstvy
errat i aktuální TeX bez relevantní opravy. Důkaz, nezávislé
kontroly a meze pravděpodobnosti jsou v
[factoring-pminusplus.md](factoring-pminusplus.md);
výsledky v results/factoring-pminusplus.json, metadata
v sources/factoring-pminusplus.json. Novější fyzický tisk
a prvenství neověřeny. Nic neodesláno.
