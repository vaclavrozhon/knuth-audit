# F142: příliš široká doména Gompertzova rozdělení

Potvrzeno 3. 11. 2026 v našem PDF 4B, tištěná str. 469 / PDF 489,
historická poznámka za odpovědí 7.2.2.1–189. Stejné znění má autorův
draft Fascicle 5C, tištěná str. 173 / PDF 179. Fyzický výtisk neověřen;
prvenství nálezu netvrdíme. Závažnost: střední, matematická doména.

Kniha uvádí distribuční funkci

`F(x)=1−a^(1−b^x), a,b>0, x≥0`.

Pro povolené `a=4, b=1/2, x=1` však dostaneme přesně
`F(1)=1−4^(1/2)=−1`. Žádná numerická aproximace není potřeba.
Také `a=1/2, b=2, x=1` dává `−1`, takže je nutné omezit oba parametry.

Správně je **a>1, b>1**. Pak `F(0)=0`,
`F'(x)=ln(a) ln(b) b^x a^(1−b^x)>0` a `lim F(x)=1`.
Tyto podmínky jsou pro řádné rozdělení na konečné poloose také nutné:

- při `0<b<1` je limita `1−a`, která pro kladné a není 1;
- při `b=1` nebo `a=1` je funkce identicky nulová;
- při `b>1, a<1` je záporná pro každé `x>0`.

Navazující formule `E X=g/ln b` pro `a=e` je správná s opravenou
podmínkou `b>1`. Integrujeme pravděpodobnost přežití
`exp(1−b^x)` a položíme `t=x ln b`; vznikne právě `g/ln b`.
Volba `b<1` by místo toho dávala zápornou střední hodnotu a divergující
integrál pravděpodobnosti přežití.

Prohledány krátké i úplné vrstvy 4B a Fascicle 5 a oba původní TeXy,
nejen čísla stránek. Oprava této domény nebyla nalezena. Známé erratum
19. 12. 2019 se týká odpovědi 189(a); jeho vlastní chyba zůstává samostatně
evidovaná jako C006. Rozpis a hashe: [errata-check.json](results/gould189_192/errata-check.json).

Gompertzův původní článek z roku 1825 byl získán jako veřejný sken JSTOR
z Internet Archive. Na str. 518 / PDF 7 skutečně používá dvojitou
exponenciálu `L_x=d g^(q^x)`. Jde o historický kontext; náš protipříklad
vyvrací výslovnou doménu v Knuthově formulaci nezávisle na historickém značení.
[Původní sken](sources/gould189_192/gompertz1825.pdf),
[záznam JSTOR](https://www.jstor.org/stable/107756).

Pro ruční ověření stačí přečíst řádek s `a,b>0` na
[straně knihy](images/gould189-192-original-489.png) a dosadit výše
uvedená tři čísla. [Autorův draft](images/gould189-192-draft-179.png)
vylučuje, že jde pouze o chybu převodu jednoho PDF.
