# Lucas, Fine a Ramus: převzetí původních citací

2. listopadu 2026, X0701. Zmrazený balík
`parallel/binomial-primary-followup/MANIFEST.json` má SHA-256
`0db2353fafffc41c208109e19af77f43dd5a64c411bd244b0dcec740c00f0a58`.
Root před změnou vlastních poznámek ověřil všech 112 souborů,
151 789 563 bytů a 16 vnějších vstupů. Zmrazené podklady se nemění.
Jejich stažení není považováno za přečtení celých ročníků.

Root přečetl předání, všech pět pramenných poznámek, čtecí rozsah,
jednotlivé stavy a výsledky prohledání všech čtyř vrstev errat.
Přímo v obrazech pak ověřil tento rozsah:

- TAOCP: zadání 10 na 69 a 38 na 71, jejich odpovědi 484 a 487;
  bibliografické doplňky na straně 32 souboru all1-prepre.
- Lucas BSMF: titul 49, binomická pasáž 51–52, zápis společnosti 79.
- Lucas AJM: titul ročníku, titul a autor na 184, binomická část
  §XXI na 229–230 do formule (137) a jejího slovního vysvětlení.
- Fine: celý článek 589–592, bez sousedních článků na sdílených stranách.
- Ramus: titul ročníku a celý článek 353–355.

## Lucas a Fine

Pro nezáporná celá m,n značí C(m,n) počet n-prvkových podmnožin
m-prvkové množiny; mimo 0<=n<=m je nula. Pro prvočíslo p položme
q=floor(m/p), r=floor(n/p), a=m mod p, b=n mod p. Lucasův původní
zápis C_m^n znamená zdejší C(m,n). BSMF 51–52 i AJM formule
(137) dávají přesně

```text
C(m,n) = C(q,r) C(a,b) (mod p).
```

Opakování přes konečné rozvoje v základu p dává součin příslušných
číslicových binomických koeficientů. To jsou části 10(e),(f).
Zápis zasedání společnosti přímo uvádí 7. listopad 1877 a stejný
titul Lucasova sdělení, zatímco titul ročníku má 1878. Rok 1877
v zadání a rok 1878 u publikovaného článku se tedy nevylučují.
Zápis zasedání není vydáván za zápis samotné kongruence.

Fineova věta 1 používá totožný součin. Její důkaz na 590 rozloží
(1+x)^M podle číslic M v základu p, použije
(1+x)^(p^j)=1+x^(p^j) modulo p a porovná koeficienty. Jedinečnost
číslicového rozvoje vylučuje další příspěvek k dané mocnině.
Věta 2 počítá nenulové koeficienty jako součin (M_j+1); věta 4
charakterizuje řádky, jejichž žádný koeficient p nedělí. To souhlasí
i s již dokázanou úlohou 12. Ostatní dvě věty a důkazy byly přečteny
jako kontext; obecný audit všech hraničních konvencí Fineova článku
není novým závazkem TAOCP.

Oba původní prameny pracují s nezápornými kombinatorickými indexy.
Rozšíření na záporné celé horní indexy v nynějším zadání není
neoprávněně připsáno Lucasovi ani Fineovi: dokazuje je (L1)–(L2)
v `binomial-congruences.md`. Staré úspěšné testy se neopakovaly.

Dicksonův článek doplněný erraty 9. ledna 2003 zůstává nečtený.
Nový balík přesně identifikuje ročník 33 (1902), článek 378–384
a dvě digitální kopie; obsah 383–384 se nepodařilo získat. Katalog,
bibliografie ani omezené vyhledávání není náhradou původní pasáže.
Úloha 10 proto zůstává partial právě pro tento pramen.

## Ramus

Ramus označuje počet prvků x, modul p a zbytkovou třídu r.
Jeho p zde nemusí být prvočíslo. Knižní značení je x=n, p=m,
r=k. Ramus počítá jen neprázdné kombinace, proto pro n>0 platí
S(n,m,k)=y_n^(k)+[k=0], kde S je součet C(n,t) přes t mod m=k
a hranatá závorka má hodnotu 1 při splnění podmínky, jinak 0.

Formule (2) na 354 je obecný filtr pomocí m-tých kořenů jedničky:
vážený součet hodnot polynomu v těchto kořenech vybere právě
koeficienty jedné zbytkové třídy. Dosazení (1+y)^n-1 a y=1 dává
Ramusovy počty; bez odečtení 1 jde přesně o knižní odpověď.
Spárováním komplexně sdružených kořenů dostává kosinovou formuli.
Knižní důkaz i vlastní (E1) v `binomial-exercises.md` tento převod
správně provádějí. Vlastní důkaz pokrývá také n=0 s polynomiální
konvencí nulové mocniny; Ramusův zkrácený párový zápis vypouští
kořen -1 při kladném n.

V samotném Ramusově tisku má formule (A) na 354 chybějící faktor
2 před kosinem uvnitř n-té mocniny. Formule (B), další řádky
jeho důkazu a TAOCP tento faktor mají. Například p=3,x=1,r=0
má skutečný počet 0, ale doslova vytištěná (A) dává -1/6.
Jde o kvalifikaci externího pramene, nikoli nový nález v TAOCP.

Titul ročníku uvádí Berlín 1834. Závěrečné datum rukopisu
20. září 1833 není rok vydání. Citované strany 353–355 z doplňku
11. října 2001 odpovídají celému článku. Citace jeho předchůdců
nebyly automaticky rozšířeny na nový audit těchto publikací.

## Dva závěrečné odkazy do Concrete Mathematics

Odpověď 38 dále odkazuje na CMath 5.75 a 6.57. Tyto cíle nebyly
součástí zmrazeného agentova balíku, proto je ověřil root zvlášť.
Starší již uložená sazba má správné úlohy na 238 a 301, odpovědi
na 521 a 533; všechny čtyři pasáže byly přímo přečteny v obrazech.
Tato sazba však sama nedokládá druhé vydání citované TAOCP.

Po neúspěšném veřejném odkazu NTU (404) byla získána veřejně
zrcadlená původní sazba druhého vydání. Přímá četba titulu a tiráže
potvrdila tři autory, druhé vydání, Addison-Wesley, copyright 1994,
ISBN 0-201-55802-5 a číselnou řadu začínající 1 a končící rokem 94.
Soubor má 670 PDF stran a SHA-256
`9137617220ddb1d4f2a8fb619132817f5ecf4549e609f6e3ae5d1c26f9ac257f`.
Nejde o ověření fyzického výtisku. Původ a přesná URL jsou v
`sources/binomial-primary-root/retrieval-mirror.json`.

Ve druhé sazbě byly přímo přečteny úloha 5.75 na 250 a odpověď
536, úloha 6.57 na 315 a odpověď 556. Obrazová mapa uvádí skutečná
čísla stran. Obsah obou citovaných úloh souhlasí se starší sazbou.

Pro modul 3 definujme S_k(n)=sum C(n,3t+k), součet přes celá t.
Pascalovo pravidlo dává S_k(n+1)=S_k(n)+S_(k-1 mod 3)(n).
Z počátečního řádku (1,0,0) indukcí plyne, že dvě hodnoty jsou
stejné a zbývající, na indexu -n mod 3, se liší o (-1)^n.
Součet je 2^n, takže hodnoty jsou floor(2^n/3) nebo ceil(2^n/3).
To je právě vlastnost případu m=3 slíbená odkazem.

Pro modul 5 se stejným sčítáním sousedů cyklicky opakuje vzor
(C,B,A,B,C) v sudém řádku a (C,B,A,A,B) v lichém, s A>=B>=C.
Počáteční vzory řádků 0 a 1 jsou rotacemi tohoto tvaru. Sčítání
zachovává pořadí i vzory a dává šest vytištěných rekurencí na 556.
Položme D=A-B a E=B-C. Přechod ze sudého řádku na lichý mění
(D,E) na (D+E,E); opačný přechod na (D,D+E). Od řádku 1 začíná
dvojice (1,0). Jsou to střídavě dvě sousední Fibonacciho čísla,
kde F_0=0, F_1=1 a F_(j+2)=F_(j+1)+F_j. Rozdíl největšího
a nejmenšího součtu je proto D+E=F_(n+1); i n=0 dává 1.
To vysvětluje přesnou vlastnost m=5 uvedenou v druhém cíli.

Tím je celá úloha 1.2.6-38 uzavřena včetně obou dalších odkazů.
Pramenné jednotky Lucas, Fine a Ramus jsou checked; úloha 10
a širší X0084 zůstávají partial. Nevznikl nový nález TAOCP.
Nová práce nevyžadovala opakování úspěšných matematických testů.
