# §4.5.2: úlohy31/34 a rozsah výsledků o modelu

Úlohy31 a34 mění erratum2016. Původní zadání355, odpovědi643/645,
text352 a příslušné původní listy errat byly zobrazeny. Níže je
audit převodu publikovaných vět a vlastní odvození jejich důsledků;
není to tvrzení o novém ověření všech71 stran Morrisovy práce.
Úloha32 zatím uzavřena není; navazující audit33 je v `gcd-extremal.md`.

## Použité prameny a čtený rozsah

- Ian D. Morris, *A rigorous version of R. P. Brent's model for the
  binary Euclidean algorithm*, Advances in Mathematics290(2016),73–143,
  DOI10.1016/j.aim.2015.12.008. Uložen je
  [preprint2014](https://arxiv.org/abs/1409.0729), nikoli vydavatelskýPDF.
  Vizuálně čteny str.7–9 a38; definice nákladů na6, úvod a relevantní
  pomocné odhady také v extrahovaném textu. Věty2/3 a důkaz pokračování
  jsou podklady tohoto bloku. Původní spektrální a Tauberovy důkazy
  nepřepisujeme jako vlastní nově dokončený audit.
- Primární publikovaný záznam Surrey a indexovaný text jeho str.80
  potvrzují normalizaci a kladnost hustoty. Veřejný download a
  ScienceDirect vrátily403; nebyly obcházeny.
- Brent1999, [autorský záznam](https://maths-people.anu.edu.au/~brent/pub/pub183.html):
  rozšířený report PRG TR-7-99,18 stran, též arXiv1303.2772.
  Numerická část12–13 přečtena; vydaná kratší verze2000 má41–53.
- Brent2021, *Some instructive mathematical errors*, autorský preprintv3,
  str.12–14 vizuálně přečteny. Jeho vlastní historický popis potvrzuje
  nalezení chybějícího periodického členu v roce1997 a pozdější Morrisův
  důkaz. Tento článek neřeší novou koeficientovou domněnku31.
- Maze: uložený [preprintv2,2005](https://arxiv.org/abs/math/0504426),
  nikoli vydavatelská verze2007. Vizuálně přečteny11–12; přesný
  limit této kontroly jednoznačnosti je uveden níže.

Důležitá oprava vlastní evidence: starší metadata Morrisova preprintu
chybně popisovala plus v rovnici(8). Nové vykreslení a zvětšený
výřez, při shodném SHA-256 PDF, potvrzují **minus**, stejně jako
extrahovaný text. Nesprávná poznámka o chybě preprintu byla odstraněna.
Nález C0122 se týká jiného znaménka, xi=-G', v Knuthově erratu,
a tato oprava evidence jej nijak nemění.

## Normalizace, původní31 a konstanty

Morrisova xi je hustota pravděpodobnosti: xi>0 na(0,1] a
integral_0^1 xi=1. Ocasová funkce knihy je

```text
G(x)=integral_x^1 xi(t)dt,  G'(x)=-xi(x), lambda=xi(1).
```

Operátor na hustotách je

```text
(Lh)(x)=sum_{k>=1} [
 h(1/(1+2^k x))/(1+2^k x)² + h(x/(x+2^k))/(x+2^k)² ].
```

Zde symbol L označuje operátor, nikoli logaritmus; ln2 níže
píšeme vždy výslovně. Morrisova věta2 říká Lxi=xi a dává
stejný asymptotický koeficient počtu odečtení dvěma způsoby:

```text
2/(ln4-integral_0^1 ln(1-x)xi(x)dx) = 4/(pi²xi(1)).          (1)
```

Kniha definuje b=2+(1/ln2)integral_0^1 G(x)/(1-x)dx.
Integrace po částech dává

```text
b ln2 = ln4-integral_0^1 ln(1-x)xi(x)dx.
```

Hraniční součin G(x)ln(1-x) mizí v obou koncích: u1 je
G(x)=lambda(1-x)+O((1-x)²), u0 stačí omezenostG a ln(1-x)->0.
Z (1) okamžitě plyne `lambda/b=2ln2/pi²`, tj. původní zadání31
a známá změna textu(61) jsou doloženy. Není zde záměna přirozeného
logaritmu a logaritmu o základu2.

Morris počítá vlastní odečtení do dosažení rovnosti operandů.
Knuthův počet C zahrnuje ještě závěrečný průchod: C=S+1.
U lichých vstupů počet jednotlivých posunů D odpovídá jehoT.
U obecných vstupů Morris definuje cenu pomocí lichých částí;
Knuth navíc započítá |v2(u)-v2(v)| počátečních posunů.
Jejich průměr je O(1), přesněji má pro rozsah1..2^N-1 limit4/3,
jak bylo dokázáno u C0123. Tyto rozdíly nemění vedoucí člen.

Věta2 platí pro čtyři modely: liché/obecné vstupy, v obou
případech s podmínkou gcd=1 i bez ní, uspořádané u<v<=n.
Symetrie převádí trojúhelník na čtverec; diagonála má zanedbatelný
příspěvek. Po položení n=2^N-1 tedy pro knižní(63) dostáváme

```text
E[C] ~ (4ln2/(pi²lambda))N = 2N/b,
E[D] ~ (8ln2/(pi²lambda))N = 4N/b.
```

To je přesný obsah rigorózního potvrzení Brentova modelu, který
potřebuje text352 a původní úloha34. Neplyne z něj, že nezávislost
jednotlivých posunů je přesná pro každý konečný celočíselný vstup,
ani že empirické konstantní členy v(62)/(65) jsou dokázané.

## Nová34: analytické pokračování G

Pravá polorovina znamená množinu komplexních z s Re(z)>0.
Holomorfní funkce je komplexně diferencovatelná v každém jejím
bodě. Morrisova věta3 konstruuje xi v Hardyho prostoru H²(D),
kde D={z:|z-1|<1}. Pro naše účely H² znamená, že Taylorovy
koeficienty xi(z)=sum a_n(z-1)^n splňují sum|a_n|²<infinity.
Píšeme ||xi||_2=sqrt(sum|a_n|²). Cauchyho–Schwarzova nerovnost dává

```text
|xi(w)| <= ||xi||_2 / sqrt(1-|w-1|²),  w in D.              (2)
```

Následující vlastní argument převádí tuto vlastnost na celou
pravou polorovinu. Pro Re(z)>0 a q=2^k jsou
a=1/(1+qz) i c=z/(z+q)=1/(1+q/z) vD. Při m<=|z|<=M máme

```text
1-|a-1|²=(1+2q Re(z))/|1+qz|² >= 1/(1+qM)²,
1-|c-1|² >= 1/(1+q/m)².
```

Z (2) plyne |xi(a)|+|xi(c)|=O(q), stejnoměrně na takové oblasti.
Současně |1+qz|>=qm a |z+q|>=q. Členy

```text
xi(1/(1+2^k z))/(1+2^k z)² + xi(z/(z+2^k))/(z+2^k)²
```

jsou proto O(2^-k). Jejich součet konverguje lokálně stejnoměrně
na celé pravé polorovině a definuje holomorfní pokračování xi;
naD souhlasí s xi díky rovniciLxi=xi. Nepotřebujeme přitom
neplatný odhad preprintové Proposition7.3, který všechny argumenty
klade do jediného menšího kruhu nezávislého na k. Tyto argumenty
se ve skutečnosti blíží hraniciD; odhad(2) tuto potíž řeší.
Jde o opravu pomocné zkratky v preprintu, nikoli o vyvrácení
Knuthova zadání nebo hlavní Morrisovy věty.

Pravá polorovina je jednoduše souvislá. Lze v ní tedy položit
`G(z)=-integral_1^z xi(w)dw`, nezávisle na cestě. Tato funkce
je holomorfní a na kladné ose souhlasí s ocasovou funkcí výše.
Rovnici(36) ověříme derivováním: derivace její pravé strany je
-Lxi=-xi=G'; obě strany jsou v1 nulové. Lokální stejnoměrnost
potřebná k derivování plyne ze stejných odhadů. Normalizace
integral xi=1 dává G(0)=1 jako jednostranný limit.

Tím je požadované pokračování G doloženo. Rovněž
G(z)+G(1/z)=0 na pravé polorovině, protože obě strany jsou
holomorfní a identita už platí na kladné reálné ose. Složení
H(y)=G(exp(-y)) je liché a analytické v pásu |Im(y)|<pi/2.
To potvrzuje reálnou analyticitu použitou v odpovědi25; širší
komplexní pokračování potřebné pro novou domněnku31 tím netvrdíme.

## Nová31: koeficientová domněnka a stav rešerše

Nové zadání se vztahuje k rozvoji H(y)=sum lambda_(2j+1)y^(2j+1)
z odpovědi25 a ptá se na limitu
`-lambda_(2k+1)/lambda_(2k-1) -> 1/pi²`. To je jiné tvrzení
než původní(61); Morrisovo řešení původní31 je samo nedokazuje.

Z již uložených čtyř koeficientů vycházejí pouze tři poměry
0.05279829735,0.06544539076,0.06984452301, proti cíli
1/pi²=0.10132118364. Tyto hodnoty jsou kompatibilní s původním
pozorováním, neposkytují důkaz limity ani nenulovosti všech
dalších koeficientů.

Rešerše2026-11-02 zahrnula přesné výrazy pro wild conjecture,
koeficienty, Taylorův rozvoj a číslo úlohy v kombinaci s Knuth,
Brent a binary Euclidean algorithm; dále primární záznamy Brent
a Morris. Nalezené práce řeší původní invariantní hustotu a
konstanty, nikoli tuto koeficientovou limitu. V auditovaných
řadách errat není novější řešení. **Řešení nové domněnky nebylo
nalezeno**; není to univerzální tvrzení o neexistenci publikace.
Úlohu31 uzavíráme jako audit výzkumné formulace a doloženého
stavu, ne jako nově vyřešený otevřený problém.

## Úloha32: zatím otevřená otázka rozsahu

Morrisova věta3(f) říká, že pro každé h zL¹, tj. s konečným
integrálem absolutní hodnoty, L^n h konverguje vL¹ k xi*integral h.
Proto Gn konvergují stejnoměrně keG: maximální rozdíl jejich
ocasových integrálů nepřesáhne ||L^n1-xi||_1. Stejný výsledek
také dokazuje jednoznačnost **absolutně spojitého** řešení
(36)/(37), jehož derivace leží vL¹.

Doslovné zadání32 se ale ptá na libovolnou spojitouG. Spojitost
sama nezaručuje absolutní spojitost nebo integrabilní derivaci.
Mazeova věta4.3 v přečteném preprintu popisuje jediný limit
konkrétní posloupnostiGn; její znění neřeší automaticky všechny
spojité pevné body. Její první důkazový řádek navíc používá,
že hromadný bod už je pevný bod, bez vysvětlení tohoto přechodu.
Nelze z toho bez další práce prohlásit, že Knuthovo tvrzení
jednoznačnosti je nepravdivé. Zatím není protipříklad ani důkaz
rozšíření na celou třídu spojitých funkcí. Úloha32 zůstává partial,
s dalším krokem prověřit publikovanou verzi a případnou regularizaci
spojitého pevného bodu. Nový potvrzený nález z toho nevyvozujeme.
