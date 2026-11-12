# §1.3.2-16–17: zaokrouhlené harmonické součty

Originály s.160–161 a518–519 zobrazeny1.listopadu2026. Označme
M=10^n a R(M,j)=floor(M/j+1/2), tedy zaokrouhlený člen v celočíselném
měřítku M. Hledaný součet je S_n=(1/M)sum_{j>=1}R(M,j).
Člen je nenulový právě pro1<=j<=2M, včetně rovnosti: přesná polovina
se podle zadání zaokrouhluje nahoru. Proto S_n skutečně konečně skončí.

## Skupiny stejných členů a strojový program

Pro kladné celé r platí přesná ekvivalence

```
R(M,j)=r  iff  2M/(2r+1) < j <= 2M/(2r−1).
```

Pro první index j skupiny je tedy její poslední index
h=floor(2M/(2r−1)). Přičteme(h−j+1)r a pokračujeme v h+1.
Skupiny jsou souvislé, disjunktní a pokryjí1,...,2M. Počáteční
člen pro j=1 je M. Pro n=5,r=1 je rozsah66667,...,200000,
přesně133334 členů; poznámka v zadání je správná.

Program `mixal_rounded_harmonic.py` přesně přepisuje s.518–519.
CONST=2M, S je dosavadní celočíselný součet a M (název paměťového
místa v programu) je právě první nezapočtený index j. Aby se tyto
dvě různé role nepomíchaly, v tomto důkazu paměťové místo
M nepoužíváme jako nový matematický parametr: matematické M je
stále10^n, zatímco index je j.

Vstup do INNER má rA=r>0. TEMP dostane2r−1; DIV spočte h,
INCA1 vytvoří h+1. Rozdíl proti uloženému j je počet členů skupiny.
MUL R a SLAX5 vytvoří příspěvek, ADD S jej přičte. TEMP se načte
do rX a blok1H uloží nový součet i index h+1. Následný blok
vyhodnotí floor((2M+j)/(2j))=R(M,j); při nulovém výsledku součet
skončí. Počáteční skok do1H používá rA=M,rX=2, tedy přesně první
již započtený člen a druhý index.

Pro požadovaná n=2,3,4,5 se všechny mezivýsledky vejdou do slova
pro každý b=64,...,100. Například dyadické rozdělení harmonické
řady dává H_{2M}<=19, tedy součet<=M H_{2M}+M<=20M<=2000000,
zatímco b^5>=64^5>10^9. Jednotlivé příspěvky jsou nezáporné a
nejvýše tento součet; ostatní čísla jsou nejvýše4M+2. Indexové
registry v původním kódu jsou malé: rI1 od3 do−1, rI2 od0 do12.
Nulový r nikdy nevstoupí do dělení2r−1.

CHAR převádí deset desetinných číslic; SLAX o5−n umístí celé číslo
na čtyři pozice a n desetinných cifer do rX. Vysunuté koncové bajty
jsou znaky mezery, nikoli desetinné nuly. SLA1 a INCA40 vloží
tečku. Každý výsledek zabírá dva slova a následuje třetí prázdné.
Tisk se provede až po dokončení všech čtyř hodnot, takže nehrozí
souběh změn se čtením tiskárny.

Výsledky přesně jsou6.16,8.449,10.7509,13.05363; všech120 výstupních
znaků souhlasí. `check_rounded_harmonic.py` prošel43994 kontrolami,
včetně všech37 radixů, hranic skupin pro M<=500 a nezávislých součtů.

## Nová časová oprava V1-C0027

Kniha uvádí65595u plus tisk. Časy jednotlivých instrukcí jsou
explicitně uvedeny na s.138: zejména MUL/CHAR=10u,DIV=12u,
načtení/uložení/ADD/SUB/posuny=2u, příslušné skoky a změny
registrů=1u. Nezávislý ruční rozpis kódu je:

| Blok | Cena jednoho průchodu | Počet |
|---|---:|---:|
| START před OUTER |3u|1|
| OUTER až JMP1F |26u|4|
| INNER až LDX TEMP |43u|907|
|1H až JAP INNER |29u|911|
| LDA S až J1NN OUTER |26u|4|
| OUT |1u|1|
| HLT |1u|1|

Počty nenulových skupin po j=1 jsou18,61,198,630, součet907.
Lze je spočítat nezávisle bez běhu programu jako počet neprázdných
intervalů pro r=1,...,M, minus první skupina. Blok1H proběhne
navíc jednou za každé n. Celkem tedy

```
3 +4·26 +907·43 +911·29 +4·26 =65631u před OUT,
65633u včetně OUT a HLT.
```

Tvrzení65595u je tudíž příliš malé i při vyloučení OUT i HLT;
nejde jen o jejich obvyklou rozdílnou konvenci. Rozdíl36u vůči
prvnímu číslu se rovná4·(10−1), takže by vznikl chybným započtením
čtyř CHAR jako1u. To je vysvětlení možné příčiny, nikoli doložená
historie vzniku chyby. Všech37 strojových profilů souhlasí s ručním
rozpisem. V žádné ze čtyř vrstev errat nebyla oprava času nalezena.

Poznámku o rychlejším přímém sečtení malých indexů lze uskutečnit:
`hybrid_program()` je naše explicitní varianta, která pro každé n
nejprve přímo sčítá j<sqrt(2M), pak přejde do původního skupinového
jádra. Meze jsou15,45,142,448; rI3=j,rI4=2j. Přímá smyčka má
stejný invariant součtu, jedno DIV a nepočítá konec skupiny.
Pro b=64,65,100 má stejný úplný výstup a čas41513u, úsporu24120u.
Index2j je nejvýše896 a bezpečně se vejde pro všechny radixy.
Nejde o tištěný kód ani o důkaz globální optimality.

## Úloha17: obecný asymptotický důkaz

H_t=sum_{j=1}^t1/j je harmonické číslo a gamma je Eulerova konstanta,
limita H_t−ln t. Používáme již ověřený odhad H_t=ln t+gamma+O(1/t).
Zvolme celé1<=m<M, které zde znamená mez pro velikost zaokrouhleného
členu, a N=floor(2M/(2m+1)). Právě indexy j<=N mají R(M,j)>m.
Jejich součet po vydělení M se od H_N liší nejvýše N/(2M).
Zbylá část se rozpadá na hladiny k=1,...,m:

```
S_n = H_N + O(N/M)
    + (1/M) sum_{k=1}^m k (floor(2M/(2k−1))−floor(2M/(2k+1))).
```

Součet po částech dává přesně

```
sum_{k=1}^m floor(2M/(2k−1)) − mN.
```

Nahrazení jednotlivých dolních celých částí jejich argumenty
má chybu O(m); důležité je provést teleskopování před odhadem,
aby se nevytvořila zbytečná chyba O(m²). Dále

```
2 sum_{k=1}^m 1/(2k−1) = 2H_{2m}−H_m,
mN/M = 1 + O(1/m) + O(m/M).
```

Proto
S_n=H_N+2H_{2m}−H_m−1+O(1/m)+O(m/M).
Při m=floor(sqrt(M)) je N asymptoticky M/m a
ln N+ln m=ln M+O(M^(−1/2)). Dostáváme

```
S_n = n ln10 + 2gamma −1 +2ln2 + O(10^(−n/2)).
```

Odečtení dvou po sobě jdoucích vztahů dokazuje požadovanou limitu
S_{n+1}−S_n→ln10. Původní tisk má na druhém řádku H_n místo H_N
a H_{2m} místo2H_{2m}; obě chyby už opravuje erratum20.května1999,
`all1-prepre`, s.38. Nejde o naše nové nálezy.

## Nezávislá numerická kontrola velkých n

Pro celočíselný součet T(M)=M S_n lze zaměnit pořadí sčítání:
R(M,j) je počet kladných k s j<=2M/(2k−1), tedy

```
T(M) = sum_{k=1}^M floor(2M/(2k−1)).
```

Jde o počítání týchž bodů mřížky po hladinách místo po indexech.
`layer_sum` navíc sdružuje shodné podíly q=floor(2M/(2k−1));
jejich poslední index je floor((floor(2M/q)+1)/2). Tento nezávislý
výpočet souhlasí se skupinovým součtem i přímým součtem malých n.
Všech pět dodatečně uvedených hodnot S_6,...,S_10 souhlasí přesně,
například S_10=24.5665766353. Asymptotický hlavní člen je
24.56657662086342; zaokrouhlení24.566576621 v knize je správné.

Úspěšné kontroly43994+9 se nemají opakovat bez změny nebo pochybnosti.
