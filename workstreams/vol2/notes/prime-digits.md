# §4.5.4-38: prvočísla s maximálním počtem stejných číslic

Zadání415 a odpověď665 byly vizuálně přečteny. Všech deset
tištěných hodnot je správných, včetně obou optimalizačních podmínek.
Nejprve se maximalizuje počet výskytů číslice d, poté samotné číslo
mezi padesáticifernými prvočísly s tímto počtem výskytů.

## Hodnoty a konečné důkazy

Položme `r=(10^50-1)/9`, tedy padesáticiferné číslo tvořené
samými jedničkami. Počet konkurentů v posledním sloupci zahrnuje
všechna padesáticiferná čísla s více výskyty d a všechna větší
čísla se stejným počtem výskytů. Všichni konkurenti jsou složení.

| d | Největší prvočíslo P_d | Počet d | Vyloučení konkurenti |
|---|---|---:|---:|
|0|10^49+9|48|3969|
|1|r+3·10^46|49|30|
|2|2r+3·10^47+7|48|8575|
|3|3r+2·10^49|49|5|
|4|4r+2·10^49−3|48|2020|
|5|5r+3·10^49+4|48|1083|
|6|6r+2·10^48+3|48|2346|
|7|7r+2·10^25|49|49|
|8|8r+10^38−7|48|4850|
|9|9r−8000|49|35|

`verify_prime_digits.py` generuje konkurenty dvěma odlišnými způsoby.
První mění vybrané pozice konstantního desetinného slova a skládá
hodnotu pomocí mocnin10. Druhý prochází strom desetinných prefixů,
udržuje počet odlišných číslic a porovnání s P_d. Shoda výsledných
množin kontroluje i vedoucí nulu, přesnou délku a pořadí kritérií.
Protože každý P_d má48 nebo49 výskytů, stačí nejvýše dvě odlišné
pozice. Nevynecháváme sudé konce ani čísla dělitelná3 či5;
i pro ně je uložen explicitní svědek.

Každý z22962 konkurentů má buď vlastní dělitel mezi2 a97,
nebo bázi a, pro kterou selže silný test prvočíselnosti.
Při `n-1=2^s t`, t liché, musí prvočíslo n splnit
`a^t=1 mod n` nebo `a^(2^j t)=-1 mod n` pro některé0<=j<s.
Neplatnost těchto nutných podmínek je přesný důkaz složenosti,
nikoli pravděpodobnostní závěr. Nezávislý validátor přepočítává
mocniny vlastní binární aritmetikou; dělitele kontroluje postupným
čtením desetinných číslic modulo dělitel.

Deset vítězů má certifikáty ECPP, tedy důkazy prvočíselnosti
pomocí eliptických křivek. PARI certifikáty pouze navrhlo.
`verify_ecpp.py` nezávisle ověřil40 článků pomocí celočíselné
aritmetiky křivek, invertibility jmenovatelů a Hasseho meze
na počet bodů. Konce řetězců mají152 uložených Lucasových
certifikátů včetně opakovaných malých uzlů napříč deseti důkazy.
Lucasův certifikát zde znamená úplný rozklad n−1 a svědka
řádu n−1 modulo n. Každý jeho prvočinitel je dokázán rekurzivně.
Žádný výsledek typu „probable prime“ se nepoužívá jako důkaz.

Všech deset checkpointů prošlo za5.643s, session12123, exit0,
limit600s a maximálně60s na jednotlivý návrh certifikátu.
Všechny certifikáty, vylučovací svědci a časy jsou uloženy
v `results/prime-digits*.json`; úspěšné bloky se neopakovaly.

## Errata a závěr

Čtyři historické a aktuální vrstvy errat a `err2.textxt` byly
prohledány pod415/665/38, „useless“ a hodnotami příkladu.
Žádná relevantní změna nebyla nalezena. Výpočty potvrzují celou
odpověď; nevzniká nový nález. Fyzický pozdější dotisk nebyl ověřen.
