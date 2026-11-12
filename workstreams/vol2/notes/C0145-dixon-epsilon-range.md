# V2-C0145: rozsah epsilon v odhadu počtu výjimek

Stav: **confirmed**, drobná chyba v kvantifikaci, nikoli vyvrácení
koncentračního výsledku pro malé epsilon. Na straně 372, v odstavci
o Dixonovi, je výslovně uvedeno „for all positive epsilon“.
Původní sazba byla vizuálně přečtena v `images/vol2-p372.png`.

Označme T(m,n) počet dělení v knižním Eukleidově algoritmu a
a=12 ln(2)/pi^2. Pro každé epsilon>0 má existovat c(epsilon)>0
takové, že mezi 1<=m<=n<=N je nejvýše

```
B_epsilon(N)=N^2 exp(-c(epsilon)(log N)^(epsilon/2))
```

dvojic nesplňujících |T(m,n)-a ln n|<(ln n)^(1/2+epsilon).
Základ logaritmu v B není pro následující spor podstatný.

Vezměme epsilon=4. Dvojice (m,n)=(1,1) je výjimkou pro
každé N>=1: algoritmus vykoná jedno dělení, takže test je 1<0.
Počet výjimek je tedy alespoň 1. Pro každé pevné c>0 ale

```
N^2 exp(-c(log N)^2) -> 0.
```

Pro dost velká N by proto měl být počet výjimek menší než 1.
Spor trvá i při asymptotickém čtení výroku a při vložení
libovolné pevné multiplikativní konstanty před B.
Stejný argument funguje pro každé epsilon>2.

Je tedy třeba omezit epsilon na malé kladné hodnoty, nebo
změnit odhad počtu výjimek, například přidáním omezeného členu.
Samotný protipříklad neurčuje největší správný rozsah epsilon
a zde se znovu nedokazuje ostrá koncentrační věta.

Původní Dixonův článek z roku 1970 nebyl získán. Jeho vlastní
článek z roku 1971, strana 374, reprodukuje tutéž formulaci;
byla přečtena přímo ze skenu. Jde tedy zřejmě o převzaté
opomenutí rozsahu, nikoli doloženou chybu při citování.
Rozdíl jednoho počátečního kroku mezi konvencemi T a Dixonovým
L pro m<n tento protipříklad neovlivňuje: T(1,1)=L(1,1)=1.

Všechny čtyři řady `all2-prepre`, `all2-pre`, `all2`, `err2`
byly 3. listopadu 2026 prohledány podle strany i jmen a tématu.
Opravy na stranách 372–373 z roku 2000 mění (57) a atribuci
Lochsovi, nikoli tento rozsah. Aktuální `sources/err2.textxt`
rovněž neobsahuje odpovídající opravu. Poslední fyzický dotisk
ani priorita nálezu nejsou ověřeny; návrh hlášení není odeslán.

Metadata pramenů: [euclid-average.json](../sources/euclid-average.json).

