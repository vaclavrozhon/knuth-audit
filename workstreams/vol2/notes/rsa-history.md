# §4.5.4: historické odkazy RSA na 405–407

Dokončeno 4. listopadu 2026 místního času (3. listopadu UTC). Tento
blok doplňuje [matematický audit RSA](rsa-basic.md), nic z jeho pěti
úspěšných výpočetních kontrol neopakuje. Výsledek: oba zbývající
historické odkazy jsou doloženy; žádný nový nález.

## 1. X.509, Annex C, 1989

Z digitální historické sbírky ITU byl získán [původní svazek](https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.260.43.en.1056.pdf)
*CCITT Blue Book, Volume VIII, Fascicle VIII.8*. Titulní strana
(PDF 2) výslovně uvádí Geneva 1989, plénum Melbourne 14.–25. listopadu
1988 a doporučení X.500–X.521. Datum doporučení 1988 tedy není
rozpor s Knuthovým bibliografickým rokem 1989.

Vizuálně přečteny celé tištěné strany 74–75 a příloha C končící
na straně 76 (PDF 84–86). Strana 74 označuje přílohu za informativní,
nikoli integrální součást doporučení. C.7 na straně 76 uvádí
Fermatovo číslo F4=2^(2^4)+1=65537, jeho binární zápis a 17 násobení.
Citace v Knuthovi na 405 proto souhlasí obsahem, datem i stránkami.

Pro exponent 65537 stačí 16 čtverců a jedno další násobení, zatímco
pro třetí mocninu stačí čtverec a násobení. Poměr 17/2=8.5 z knihy
je poměr těchto počtů aritmetických operací. Skutečný čas závisí
na realizaci čtverců a násobení; audit nedokládá univerzální časový
poměr na libovolném stroji. Tento aritmetický argument již byl
ověřen v původním bloku RSA.

Před získáním originálu byl přečten i [oficiální přetisk X.509](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-X.509-198811-S!!PDF-E&lang=e&type=items),
PDF 2 a 25–27 (tištěné 23–25). Poznámka přetisku uvádí stejné
znění jako v Blue Book, ale možné odlišné rozvržení. Citaci 74–76
proto potvrzuje až nyní získaný originál, ne přetisk s jiným
stránkováním. Ostatní části 236stránkového svazku nebyly auditovány.
Dobová doporučení v C.6 nejsou předmětem aktualizace tohoto bloku.

## 2. Cocks 1973 a zveřejnění v roce 1997

Známý dodatek z 16. listopadu 2010 na Knuthově 407 zmiňuje
Cocksovu transformaci x^(pq) modulo pq z roku 1973 a její
odtajnění v roce 1997. Dva rozdílné doklady pokrývají oba údaje.

[Cocksova zpráva](https://cryptocellar.org/cesg/notense.pdf) nese datum
20. listopadu 1973. Celý jednostránkový přepis byl vizuálně přečten.
Je to pozdější sazba obsahu zprávy, nikoli sken původního rukopisu.
Odstavec 1 skutečně posílá N=PQ a šifruje D=C^N modulo N. P,Q
jsou prvočísla; uvedené podmínky jsou P nedělí Q−1 a Q nedělí P−1.
Zpráva popisuje inverze P' modulo Q−1 a Q' modulo P−1 a obnovu
C ze dvou zbytků. Pro různá P,Q je správnost přímo případem důkazu
v [rsa-basic.md §1](rsa-basic.md#1-modulární-inverze-a-společná-zpráva):
exponent N je nesoudělný s (P−1)(Q−1). Konkrétně modulo Q platí
D^P'=C^(PQP')=C, též když Q dělí C; analogicky modulo P a pak CRT,
tedy jednoznačná rekonstrukce ze zbytků. Historický údaj o transformaci
je tím potvrzen, aniž bychom přebírali všechny odhady obtížnosti
z odstavců 2–4 zprávy.

[Oznámení CESG v archivní kopii](https://cryptome.wikileaks.org/jya/storynse.htm)
(záhlaví archivu 4. února 1998) výslovně datuje oficiální potvrzení
do prosince 1997, při zveřejnění Ellisova historického textu z roku
1987. Dále uvádí Cocksovu interní zprávu 1973 a oznamuje zpřístupnění
čtyř původních technických zpráv, převedených do HTML bez jiných
redakčních změn. To rozlišuje veřejné odhalení roku 1997 od následného
širšího zpřístupnění původních poznámek. Knuthův dodatek toto rozlišení
neporušuje.

Kopie oznámení uvádí jako původní URL `www.cesg.gov.uk/storynse.htm`;
archivní hostitel není CESG. Facsimile Cocksova původního dokumentu
z roku 1973 se získat nepodařilo (zkoušený odkaz 404). Historický
závěr stojí na obsahu přepisu a dochovaném oficiálním oznámení,
nikoli na tvrzení, že byl přečten původní fyzický exemplář.

## 3. Evidence a rozsah

Výše uvedené doplňuje starší kontrolu všech vrstev errat a vizuální
čtení Knuthových 403–407; nový rozpor se sazbou nebyl nalezen.
Oprava „considered“ na „published“ na 406 (7. července 1999) i Cocksův
dodatek z roku 2010 zůstávají známými erraty, nikoli novými nálezy.
Úloha 44 a sedm souvisejících zpráv na 405 byly mezitím uzavřeny
v [rsa-advanced.md](rsa-advanced.md).

[Metadata](../sources/rsa-history.json) rozlišují přesné PDF, přetisk,
archivní HTML, vizuálně čtené stránky a neúspěšný odkaz. Původní
bajty HTML jsou v gzip; čitelné HTML a extrahované texty mají
normalizované konce řádků a odstraněné koncové mezery. Žádné
hlášení nebylo odesláno. Pozdější fyzický dotisk Knutha nebyl ověřen.
