# §2.2.6: adresování polí a obecné bijekce

Originály s. 298–307 a 556–560 byly zobrazeny. `LOC` znamená adresu
prvního slova prvku; `c` je počet slov na prvek. Binomické číslo
`C(a,b)` zde počítá b-prvkové podmnožiny a je nula pro `0<=a<b`.
Indexy jsou celá čísla v uvedených mezích. Tabulky jsou dostatečně velké;
matematický adresovací vzorec sám netvrdí, že libovolné rozměry vejdou do MIX.

## Obdélníky a trojúhelníky, hlavní text a úlohy 1–5

Lexikografické pořadí porovnává první odlišnou souřadnici. Prvek
s indexy I má před sebou přesně
`sum_r (I_r-l_r) product_{s>r}(u_s-l_s+1)` prvků: pro každé r
spočítáme prvky, které se poprvé liší právě na pozici r. Násobení c
a přičtení adresy prvního prvku dává (5), (6) i odpověď 2. Prázdný
součin je 1. Po sobě jdoucí prvky mají adresy vzdálené c, takže není
překryv ani mezera. Záporný fiktivní počátek `LOC(A[0,...,0])` je
algebraická konstanta, nikoli požadavek číst zápornou adresu.

- Úloha 1: `LOC(A[J,K])=LOC(A[1,1])+2n(J-1)+2(K-1)` pro m řádků
  a n sloupců. Slovo „indices ... to n“ v odpovědi je nepřesná zkratka
  pro obecně odlišné horní meze m,n; vzorec je správně.
- Příklad (4): rozměry 3×5×11×3 dávají koeficienty 165,33,3,1.
  Časový příklad má 4×7×24×60×60=2419200 prvků. Interpretace jako
  smíšená číselná soustava předpokládá c=1, jak doplňuje erratum 2023.
- Dolní trojúhelník: před řádkem J je `1+...+J=J(J+1)/2` prvků,
  uvnitř řádku je offset K. Úloha 3 je přímá bijekce indexů
  `(J,K,n) -> (J-1,K-1,n-1)`.
- Horní trojúhelník: před řádkem J je
  `sum_{h=0}^{J-1}(n-h+1)=J(n+1)-J(J-1)/2`; v řádku zbývá offset
  K-J. Dostáváme přesně odpověď 4.
- Dva dolní trojúhelníky: obraz A je `column<=row`, obraz B je
  `column>row` v obdélníku `(n+1)×(n+2)`. Inverze druhého obrazu
  je `B[column-1,row]`; všechny buňky jsou pokryty právě jednou.

Věta o nemožnosti lineárního těsného uložení jednoho trojúhelníku má
samozřejmé malé výjimky n=0,1. Pro n>=2 lze dodat důkaz: pišme
adresu `a0+aJ+bK`. Krajní hodnoty jsou ve vrcholech (0,0),(n,0),(n,n),
tedy rozsah adres má délku `nD`, kde `D=max(|a|,|b|,|a+b|)`.
Těsné uložení by vyžadovalo `nD=(n+1)(n+2)/2-1`, tj. `D=(n+3)/2`.
Sudé n odpadá celočíselností. Pro liché n>=3 je D<=n, a nenulový
vektor `(b,-a)` je rozdílem dvou bodů trojúhelníku (jeho rozdílový
šestiúhelník je dán `max(|x|,|y|,|x-y|)<=n`). Oba body mají tutéž
adresu, spor. Degenerované malé případy nejsou nový nález.

Úloha 5 používá rozšířené nepřímé adresování z §2.2.2-3: modifikátor 7
načte adresové slovo a pokračuje jeho modifikátory. Varianta (i)
`LDA TA2,1:7` nejprve přičte J, potom načte základ
`A0+J(J+1)/2` s následným indexem 2, který přičte K. Varianta (ii)
`LDA C1,7:2` načte `TA,1:7`, přičte J, načte základ řádku a teprve
nakonec přičte K. Použije tedy dva nepřímé přístupy místo jednoho,
ale tabulka není vázána na indexový registr K. MIXAL počítá `j+1*j/2`
zleva doprava, takže jde o `(j+1)j/2`, nikoli běžnou prioritu operací.

## Tetraedrická pole, úlohy 6–8

Pro `0<=K<=J<=I<=n` počítáme předchozí vrstvy, řádky a prvky:
`rank_A(I,J,K)=C(I+2,3)+C(J+1,2)+K`. Pro opačné uspořádání
`0<=I<=J<=K<=n` je počet

```
rank_B(I,J,K) = C(n+3,3)-C(n+3-I,3)
              + C(n+2-I,2)-C(n+2-J,2)+K-J.
```

První rozdíl počítá dokončené vrstvy s první souřadnicí menší než I,
druhý dokončené řádky v aktuální vrstvě. Každý člen závisí nejvýše
na jedné proměnné; obě požadované separovatelné adresace tedy existují.
Stejný rozklad a součet `sum_{h=0}^{t-1} C(h+d-1,d-1)=C(t+d-1,d)`
dává obecně odpověď 7:
`rank(I_1,...,I_k)=sum_{r=1}^k C(I_r+k-r,k+1-r)`.
Indukce podle k současně dokazuje pořadí, jednoznačnost a interval
`0,...,C(n+k,k)-1`; nejde jen o algebraickou shodu vzorců.

Úloha 8: šest zobrazení do X uvedených v odpovědi má inverzi podle
nejpravější minimální souřadnice. Je-li minimum v poslední souřadnici,
patří bod do A nebo B podle pořadí prvních dvou souřadnic; je-li ve
prostřední, do C nebo D; je-li v první, do E nebo F. Posuny o 1 a 2
převádějí ostré nerovnosti na neostré, včetně všech shodných indexů.
Následující obecný důkaz zároveň kontroluje celou zobecňující poznámku.

Nechť a je permutace 1,...,m a
`B_r=#{s<r : a_s>a_r}`. Tato inverzní tabulka **podle pozic** je
přesně tabulka opraveného odkazu §5.1.1-7, nikoli původní jiná tabulka.
Zobrazení je `x_r=I_{a_r}+B_r` a `0<=x_r<=n+r-1`, protože
`0<=B_r<=r-1`. Chceme obnovit a i klesající vektor I pouze z x.
Najdeme nejpravější minimum x, na pozici t. Pak `a_t=m`, `I_m=x_t`:
pro dřívější pozice platí x>=I_m a pro pozdější x>=I_m+1, protože
jejich B zahrnuje právě prvek m. Odstraníme souřadnici t a od všech
souřadnic napravo odečteme 1. Získáme tutéž úlohu o rozměru m-1,
s mezemi `0<=x'_r<=n+r-1`; žádná hodnota neklesne pod I_m.
Indukce dává jedinou permutaci a jediný vektor
`n>=I_1>=...>=I_m>=0`. Jde tedy o bijekci na celý obdélník a všech
`m! C(n+m,m)=(n+1)...(n+m)` buněk je využito.

## Pásová, rostoucí a neomezená pole, úlohy 20–23

20. Při `a1=1,a2=2` mají diagonální buňky offset `3I-3`, buňky
nad diagonálou `3I-1` a pod ní `3I-5`, vše vzhledem k A[1,1].
Jsou to tři zbytkové třídy modulo 3, dohromady přesně 0,...,3n-3.
Volba `a1=2,a2=1` je transpozice. Platí i n=1.

21. Položme `M=max(I,J)`. Buňky vrstvy M mají adresový offset
`M(M-1)+I-J`; část I=M dává interval `M(M-1),...,M²-1`, část
J=M, I<M dává `(M-1)²,...,M(M-1)-1`. Všechny vrstvy 1,...,n
tedy pokryjí 0,...,n²-1 a starší adresy se při růstu nemění.

Opravená k-rozměrná rekurence Rosenberga a Stronga má
`L1=A0+I1-1`, `M_r=max(I1,...,Ir)` a

```
L_r = L_{r-1} + (M_r-1)^r
      + (M_r-I_r)*(M_r^(r-1)-(M_r-1)^(r-1)).
```

Člen `(M_r-1)^r` byl doplněn v roce 2006. Důkaz: pro vrstvu M a
`I_r=M` projde předchozí adresa celý interval 0,...,M^(r-1)-1.
Pro `I_r=t<M` musí být maximum předchozích indexů rovno M, takže
předchozí adresa projde právě jeho vnější vrstvu o délce
`D=M^(r-1)-(M-1)^(r-1)`. Přičtení `(M-t)D` naváže tyto bloky
za první blok bez mezery. Vnější posun `(M-1)^r` řadí vrstvy za sebe.
Indukce dokazuje těsné uložení n^k buněk pro každé n a k.

22. Pro nezáporný vektor i položme `u_r=i1+...+ir+r-1`. Dostáváme
bijekci na přísně rostoucí nezáporné indexy u. Combinadická hodnost
`p(i)=sum_{r=1}^k C(u_r,r)` je polynom s racionálními koeficienty,
na těchto vstupech celočíselný. Jeho jednoznačnost lze dokázat hladově:
pro celé N>=0 vybereme největší u_k s `C(u_k,k)<=N`, odečteme tento
člen a pokračujeme; zbytek je menší než `C(u_k,k-1)`, takže další
index je menší než u_k. Pro součet S=i1+...+ik je poslední index
`u_k=S+k-1`, proto příslušné hodnosti tvoří interval
`C(S+k-1,k),...,C(S+k,k)-1`. Vyšší součet tudíž dává vyšší hodnost.

23. Při přidání sloupce J uložíme m nových buněk za dosavadní pole
a poznamenáme `c[J]=A0+mJ`. Při přidání řádku I obdobně uložíme n
buněk a `r[I]=A0+nI`. Počáteční r[0]=c[0]=A0. Buňku (I,J)
vytvořila ta z obou událostí, která nastala později. Je-li pozdější
sloupec, `c[J]>=r[I]` a její adresa je c[J]+I; jinak r[I]+J.
Z toho přímo plyne těsné uložení a neměnnost starších adres.

Navíc v prvním případě při vzniku řádku platilo n0<=J a při vzniku
sloupce m>=I+1, tedy `c[J]-r[I]-J=(m-1)J-I*n0>=0`.
V druhém případě při vzniku sloupce bylo m0<=I a při vzniku řádku
n>=J+1, tedy `r[I]-c[J]-I=I(n-1)-m0*J>=0`. To dokazuje i formulaci
pomocí `max(c[J]+I,r[I]+J)`. Případ shody je pouze původní buňka.
Pokud se mezi novými bloky ponechávají mezery, stejné závěry platí
z monotónního růstu adres: pozdější blok leží až za celým starším
řádkem či sloupcem. Potřebujeme jen příslušný posun prvních buněk.
