# §3.6-7: co lze určit ze zkrácených stavů

Zadání na 193 a odpověď na 599 byly přečteny v původní sazbě.
Lineární kongruenční generátor je zde rekurence

```
X_(n+1) = (a X_n + c) mod M,  M=2^32,
0 <= X_n < M.
```

Pozorujeme horních 16 bitů, tedy H_n=floor(X_n/2^16). Zadání předpokládá
periodu M a požaduje určit a i první diferenci X_1−X_0 ze 150 hodnot H_n.
Odpověď na 599 dokonce tvrdí, že stačí H_n mod 4. Níže rozlišujeme
jednoznačnost parametrů od možnosti předvídat výstup. Protipříklady
nejsou obhajobou tohoto šifrování; vyvracejí konkrétní rekonstrukční
záruky bez dodatečných předpokladů.

## C0076: 150 hodnot nezaručuje jednoznačnost

Vezměme X_0=0, a=1 a buď c=1, nebo c=3. V obou případech je perioda
přesně 2^32: rovnost nc=0 modulo 2^32 platí právě tehdy, když n je
násobkem 2^32, protože c je liché. Pro 0<=n<150 ale máme X_n=n,
respektive X_n=3n. Oba stavy jsou menší než 2^16, takže všech 150
pozorovaných H_n je nula. První diference jsou přitom 1 a 3.

Žádný algoritmus, bez ohledu na dobu výpočtu, nemůže z totožného
vstupu zaručeně určit, která první diference byla použita. Podmínka
plné periody sama nestačí. Obecné vyjádření „v typických případech“
nebo výstup všech kompatibilních parametrů by měnily znění úlohy;
nelze je dodatečně vydávat za již vyslovený předpoklad. Tento příklad
používá záměrně špatný multiplikátor a=1, který zadání nevylučuje.
Nesplňuje doporučení a mod 8=5 z obecného přehledu; to však není
hypotéza úlohy 7, jež výslovně uvádí pouze rekurenci a plnou periodu.

## C0077: dva prostřední bity nikdy neobsahují vysoké bity parametrů

Položme L=2^18. Pozorování H_n mod 4 závisí pouze na X_n mod L.
Redukcí rekurence dostaneme

```
X_(n+1) mod L = ((a mod L)(X_n mod L) + (c mod L)) mod L.
```

Z indukce tedy dvě trojice parametrů, které jsou shodné modulo L,
dávají stejná dvoubitová pozorování pro všechna n. Například všechny

```
a=5+u L,  c=1+v L,  X_0=0,  0<=u,v<2^14
```

jsou přípustné parametry modulo M. Každý generátor má plnou periodu:
c je liché a a=1 modulo 4, tedy platí již ověřená věta 3.2.1.2A.
Dokonce všechny mají a mod 8=5. Přesto všech 2^28 dvojic (a,c) dává
stejný nekonečný proud H_n mod 4. Diference X_1−X_0 je zde přímo c.
Tato nejednoznačnost není jen degenerací krátkého konstantního prefixu.

Konkrétně a=5 a a=262149 při c=1,X_0=0 dávají X_2=6 a X_2=262150:
H_2 je 0 a 4, ale H_2 mod 4 je v obou případech nula. Obdobně změna
c z 1 na 262145 je vidět již v celém H_1, ale nikoli v H_1 mod 4.
Vyšší pozorované bity jsou tedy nezbytné k určení vyšších bitů
parametrů. Samotná uvedená dvojice bitů je může určit nanejvýš modulo
2^18, a ani v tomto zmenšeném problému zde netvrdíme obecnou
jednoznačnost ze 150 vzorků.

## Rozsah kontroly a zdrojů

`verify_truncated_lcg.py` porovnává iterativní rekurenci s nezávislým
uzavřeným výrazem a^n X_0+c(a^n−1)/(a−1) modulo M, se zvláštním
případem a=1. Prošlo 10500 přesných stavových porovnání. Výpočet
ilustruje oba protipříklady; všeobecné závěry výše mají krátký důkaz
a nejsou odvozeny jen z testovaných prefixů.

Známé erratum z 10. května 2009 odstraňuje z odpovědi 7 nevhodnou
citaci Blum–Blum–Shub. Neopravuje dvoubitové tvrzení. Prohledány
`all2-prepre`, `all2-pre`, `all2`, `err2` a uložený aktuální TeX podle
193/599, multiplikátoru, bitů a citované šifry; opravy C0076/C0077
nenalezeny.

Knuthův původní IEEE článek z roku 1985 se nepodařilo získat: vydavatel
vrací ověření prohlížeče. Stanfordský předtisk CS-TR-80-800 nebyl
přístupný a v dostupném zrcadle chybí. Autorův vlastní
[seznam vybraných prací](https://cs.stanford.edu/~knuth/da.html) dokládá
pozdější přetisk jako kapitolu 24. Jeho algoritmus, přesnou složitost
ani změny mezi verzemi zde nepředstíráme jako přečtené nebo ověřené.
Vlastní protipříklady na tomto zdroji nezávisejí. Audit této úlohy
uzavíráme jako potvrzené chyby jejího neomezeného znění; úspěšný
univerzální rekonstrukční algoritmus za těchto hypotéz neexistuje.

Fyzický pozdější tisk a prvenství neověřeny; návrhy nebyly odeslány.
