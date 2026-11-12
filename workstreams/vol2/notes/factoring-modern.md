# §4.5.4: moderní faktorizace, strany 402–403

Audit třetího vydání, prvního dotisku (1997), dne 3. listopadu 2026.
Původní strany [402](../images/vol2-p402.png) a
[403](../images/vol2-p403.png) byly vizuálně přečteny. Pollardův
odstavec na 402 už pokrývá `factoring-pminusplus.md`; zde následují
kvadratické síto, metoda eliptických křivek a číselné síto.

**Výsledek:** matematické rozklady a počty číslic na 403 jsou správně.
Vlastní certifikáty dokazují prvočíselnost všech 21 faktorů použitých
níže. Primární články potvrzují citované heuristické časy a hlavní
historická data. Nový nález nevznikl. Přesný původ Guyova citátu a
dobový praktický přechod u `10^112` zůstávají částečně ověřené.

## 1. Význam a rozsah časových odhadů

Označme `N` faktorizované číslo a `p` jeho hledaný prvočíselný
dělitel. **Hladké číslo** má všechny prvočíselné dělitele pod zvolenou
mezí. Kvadratické síto hledá mnoho hladkých hodnot kvadratického
polynomu, aby jejich vhodným součinem získalo kongruenci dvou čtverců;
její využití bylo obecně dokázáno v `factoring-contfrac.md`.

Pomeranceův původní článek z roku 1985, strana 174
([obraz](../images/pomerance-quadratic-sieve-1985-p6.png)), výslovně
datuje svůj návrh do roku **1981**. Bibliografické údaje LNCS 209,
169–182 odpovídají titulní straně. Z textu byly čteny strany 169–171,
pasáž o vzniku síta na 174 a bibliografie; není tím tvrzen audit všech implementačních variant
zbytku článku.

**ECM**, metoda eliptických křivek, nahrazuje grupu nenulových zbytků
modulo `p` grupou bodů eliptické křivky. Změna křivky mění počet
bodů, a tím dává novou šanci, že tento počet bude hladký.
Lenstra1987, strany 649–650 a 671–672, byly vizuálně přečteny.
Článek odlišuje předpoklad o hustotě hladkých čísel od dokázaných
kroků algoritmu; nejde o bezpodmínečnou časovou větu. Jeho hlavní
člen `K(p)` má

```
ln K(p) = sqrt((2 + o(1)) ln(p) ln ln(p)).
```

Knižní slovo „heuristically“ a koeficient 2 proto odpovídají
originálu. Následující převod je vlastní algebraická kontrola.
Pišme `L = sqrt(ln(N) ln ln(N))`. Pro `p` řádu `sqrt(N)` platí

```
ln p = (1/2 + o(1)) ln N,
ln ln p = ln ln N - ln 2 + o(1),
ln K(p) = (1 + o(1)) L.
```

Dřívější knižní odhad pro konkrétní algoritmus E má logaritmus
`(2+o(1))L`. Jejich poměr tedy směřuje k `1/2`: tvrzení o druhé
odmocnině času je správné na úrovni hlavního exponentu, tedy
`T_ECM = T_E^(1/2+o(1))`. Není to ekvivalence skutečných časů
včetně všech nižších členů. Pro menší `p` hlavní exponent klesá.
Hasseova věta o počtu bodů křivky zůstává standardním externím
matematickým vstupem; celý Lenstrův článek zde nebyl znovu dokazován.

**NFS**, číselné síto, používá související rozklady v celých číslech
a v číselném tělese, tedy konečném rozšíření racionálních čísel.
Pro audit není potřebná podrobná konstrukce této metody, protože
ji ani kniha neuvádí. Buhler–Lenstra–Pomerance1993, první dvě strany
([první](../images/buhler-lenstra-pomerance-nfs-1993-p1.png)),
potvrzují pro obecná `N` heuristický hlavní koeficient
`c=(64/9)^(1/3)` v exponentu

```
(c + o(1)) (ln N)^(1/3) (ln ln N)^(2/3).
```

To odpovídá knižní rovnici (25), kde je libovolné kladné epsilon
uvnitř třetí odmocniny. Nezaměňujeme tuto obecnou variantu se
speciálním číselným sítem pro čísla jako `F9`.
Lenstrova dobová anotovaná bibliografie, první strana, dokládá
Pollardův rukopis ze srpna **1988** a dopis z 31. srpna.
Přesná hodnota praktického přechodu mezi oběma síty u `10^112`
není důsledkem těchto asymptotik. Je to dobový odhad připsaný
A. K. Lenstrovi; podklad tohoto konkrétního měření nebyl získán.
Článek z roku 1993 na straně 51 uvádí přechod přibližně u 125 číslic
a výslovně upozorňuje na jeho citlivost vůči implementaci. To není
spor s pozdějším, opatrně formulovaným odhadem v knize z roku 1997.

## 2. Vlastní certifikáty Fermatových čísel

Fermatovo číslo zde značí `F_m = 2^(2^m)+1`.
Zápis `p_d` v knize znamená prvočíslo s `d` desetinnými číslicemi.
Neznámé zbytky `F12` a `F13` označujeme `C_d`, kde jsme samostatně
dokázali, že jde o složená čísla s `d` číslicemi.

| Číslo | Počet číslic | Číslice jeho ověřených prvočíselných faktorů | Zbylý kofaktor |
|---|---:|---|---|
| `F9` | 155 | 7, 49, 99 | žádný |
| `F10` | 309 | 8, 10, 40, 252 | žádný |
| `F11` | 617 | 6, 6, 21, 22, 564 | žádný |
| `F12` | 1234 | 6, 8, 8, 12, 16 | `C1187` |
| `F13` | 2467 | 13, 19, 19, 27 | `C2391` |

Všechna plná desetinná čísla jsou uložena v
[ověřeném výsledku](../results/fermat-factors-validation.json).
Přesná celočíselná násobení a dělení potvrzují všechny tři rozklady
vytištěné na 403. Knižní hranice `10^22`, `10^16` a `10^27` pro
malé faktory `F11`, `F12`, `F13` byly kontrolovány přímo. Vyjádření
o dvojnásobném počtu číslic u dalšího Fermatova čísla je přibližné:
zde skutečně 155 a 309; nejde o novou matematickou chybu.

[Generátor](../certify_fermat_factors.py) použil PARI/GP `primecert`
pouze k návrhu certifikátů. Jejich platnost poté kontroloval
[samostatný Python program](../verify_fermat_factors.py), používající
`verify_ecpp.py`. **ECPP certifikát** je řetězec eliptických křivek,
který prvočíselnost každého čísla odvozuje z menšího již dokázaného
prvočísla. Zde bylo ověřeno **124 článků řetězců**, zakončených
celkem **106** malými prvočísly s rekurzivními Lucasovými certifikáty.
Faktorizace `n-1` navržená SymPy není sama přijímána jako důkaz;
každý její faktor i Lucasova kongruence jsou zvlášť ověřeny.

Pro úplnost uvádíme matematickou kontrolu rozhodujícího kritéria.
Nechť `n` je lichý kandidát a `q` již dokázané prvočíslo.
Certifikát určuje nesingulární křivku modulo každého prvočíselného
dělitele `l` čísla `n` a bod `S`, který má afinní souřadnice
modulo všech těchto dělitelů. To znamená, že `S` není neutrálním
bodem v žádné z těchto grup. Ověříme `qS=O`, kde `O` je neutrální
bod, a

```
q > (ceil(n^(1/4)) + 1)^2.
```

Pak `S` má modulo každého `l` přesně řád `q`. Hasseova mez dává
`q <= (sqrt(l)+1)^2`. Kdyby bylo `n` složené, mělo by prvočíselného
dělitele `l<=sqrt(n)`, což odporuje předchozí ostré nerovnosti.
Při sčítání bodů validátor ověřuje invertibilitu každého použitého
jmenovatele modulo `n`; nesingulárnost zajišťuje kontrola diskriminantu.
Všech **124** kandidátů v eliptických článcích je lichých. Tato
předpokladová kontrola byla doplněna při čtení kódu a provedena
samostatně bez opakování již úspěšných operací na křivkách.

Pro oba zbylé kofaktory `C1187` a `C2391` je konkrétním důkazem
složenosti selhání Fermatovy kongruence se základem **3**:
`gcd(3,C)=1`, ale `3^(C-1) mod C != 1`. Celé zbytky jsou v JSON.
Kontrola používá Python `pow` a nezávislé levostranné binární
umocňování. Počty číslic byly ověřeny nerovnostmi
`10^(d-1) <= C < 10^d`, bez plovoucího logaritmu.

Generování mělo limit 1800 s na cíl a 10800 s celkem; žádný cíl
nevyčerpal limit. Největší návrh trval 22.454 s. Nezávislé ověření
všech 21 prvočísel a pěti součinů trvalo **88.324041437 s**, limit
180 s, návratový kód 0. Příkazy, PID a logy jsou v `RUN_STATE.json`.
První pokus o spuštění selhal kvůli naší chybě cesty ještě před
jakýmkoli výpočtem; log je zachován odděleně. Nejde o nález v knize.

## 3. Historická tvrzení a errata

Lenstra–Lenstra–Manasse–Pollard1993, strana 319, potvrzuje pro `F9`
čtyři měsíce a přibližně 700 stanic. Příslušné části stran 328–329
a 340–345 byly čteny v textovém přepisu. Vizuálně byla čtena 319.
Dodatek z roku 1995 se týká historického Gaussova příkladu, nikoli
změny rozkladu. Jeho text byl čten v přepisu.

Brent1999, strany 429–431, 443–445 a 447, potvrzuje rozklady
`F10`, `F11`, datum **20. října 1995** a rok **1988**. Vizuálně
čteny 430, 444 a 445; další uvedené části v textovém přepisu.
Brent–Crandall–Dilcher–Van Halewyn2000, autorská verze §5,
vizuálně strany 4–5, dokládá čtvrtý faktor `F13` ze 16. června 1995
i velikost složeného zbytku. Kellerova tabulka na Purdue obsahuje
pět malých faktorů `F12` a čtyři `F13`; jde o historickou tabulku
s poslední novinkou z března 2001, nikoli o aktuální stav roku 2026.
Označení „at present“ v knize čteme vzhledem k dotisku 1997.

Všechny čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
byly prohledány podle stran i názvů. Známé změny v `all2-prepre`:

- 402, 8. října 2010: doplnění druhé řady Annals.
- 402, 14. května 1998: doporučení knihy Silverman–Tate, kapitoly 4.
- 403, 7. července 1999: Brentova konečná citace **68 (1999), 429–451**.
- 403, 20. června 2000: konečná citace **69 (2000), 1297–1304**.

Citace zbytku `F13` na Crandall–Fagin1994, stranu 321, nebyla v tomto
bloku ověřena v originálu; údaje o faktorech potvrzuje výše uvedený
primární navazující článek. Podobně Guy1976: vydavatel potvrzuje
ročník 16 v roce 1976, ale původní strany 49–89 nebyly získány.
Sekundární opakování citátu nenahrazuje kontrolu jeho přesného znění.
Tyto omezené bibliografické položky spolu s odhadem `10^112`
zůstávají v odděleném částečném bloku. Podrobnosti a hashe jsou v
[metadatech](../sources/factoring-modern.json).

Nejsou tím ověřeny nejnovější fyzické dotisky ani prvenství nálezů.
Žádné hlášení nebylo odesláno.
