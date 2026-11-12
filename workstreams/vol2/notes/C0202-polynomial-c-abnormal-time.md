# V2-C0202: čas algoritmu C při větších poklesech stupně

**Confirmed, s explicitním modelem hustého klasického násobení.**
§4.6.1–21,438 a odpověď677. Vstupy stejného stupně n=5D-1 s N=2
vyžadují v doslovném R Omega(n^5) průchodů násobicí smyčkou M při
vynechání volitelného testu M2; vytištěná horní mez je O(n^4 log^2 n).
Platí také pro optimalizaci nízkých indexů v závorce R2.

Definice vstupů, obecný algebraický důkaz a přesný počet jsou v
[úplné poznámce](polynomial-c-complexity-open.md), §§1–3. §4 dokazuje
O(n^5(log(Nn))^2) obecně a požadovanou čtvrtou mocninu při omezených
poklesech. §5 rozlišuje původní Collinsův omezený výsledek a Brownův
kvalitativní model; §6 dokumentuje70 přesných běhů rekurence.

Omezení není formální drobnost: ponechaný test M2, násobení posunem,
rychlé násobení či odložené společné faktory mohou tuto rodinu zrychlit.
Nejde o dolní mez pro libovolnou implementaci C ani pro problém gcd.
Právě pro běžný hustý model nelze bez dalšího důkazu v odpovědi677
předpokládat jen rozdíly stupňů nejvýše1.

Sazba268/425–426/428–429/438/677 přečtena; šest vrstev errat bez
odpovídající opravy. Aktuální fyzický dotisk a prvenství neověřeny.
Hlášení neodesláno.
