# §1.2.11.1: význam O-notace a všech 13 úloh

Audit 1. listopadu 2026, třetí vydání, první dotisk. Zobrazeny původní
strany 107–111 a odpovědi 502–503. Níže se používá číslování rovnic
originálu, nikoli přečíslovaný a podstatně zkrácený pomocný Markdown.
Faktoriálové rozvoje (16)–(17) a úloha 12 mají samostatný důkaz
v [asymptotic-factorial-powers.md](asymptotic-factorial-powers.md).

## Definice a algebra množin funkcí

Pro funkci f na kladných celých číslech je O(f(n)) množina všech
funkcí h, pro něž existují M>0 a celé n0>=1 tak, že
`|h(n)| <= M|f(n)|` pro všechna n>=n0. Konečný počáteční úsek
h není omezen. Každý výskyt O může představovat jinou funkci.
Sčítání a násobení množin funkcí znamená všechny možné bodové
součty a součiny. Knižní zápis A=B znamená inkluzi A do B;
samostatná funkce na levé straně představuje jednoprvkovou množinu.

Inkluze jsou tranzitivní. Obraz množiny zobrazením zachovává inkluzi,
což dokazuje i pravidlo substituce pro libovolnou funkci g, pokud
jsou všechny výrazy definovány. Opakované nezávislé výskyty O nejsou
pojmenovaná proměnná se závazně stejnou hodnotou. Proto běžné
odečtení dvou zdánlivě stejných O nemusí dát nulu.

Odhad H_n=ln n+gamma+O(1/n), rovnice (1), je již obecně dokázán
v [harmonic-analytic.md](harmonic-analytic.md). Součet čtverců je přesně
n³/3+n²/2+n/6, což okamžitě dává (2)–(4). Pro polynom
`P(n)=sum_{j=0}^m a_j n^j` a n>=N>=1 platí

```text
|P(n)| <= n^m sum_{j=0}^m |a_j| N^(j−m).                 (O1)
```

Volby N=1 a N=2 jsou přesně oba knižní odhady. Je-li polynom
nulový, lze místo nulového součtu vzít libovolné M>0.

Rovnice (5)–(10) mají tyto přímé důkazy:

- (5): pro f samotné vezmeme M=1.
- (6): násobení konstantou c násobí odhad |c|; pro c=0
  je levá strana jen nulová funkce a inkluze stále platí.
- (7): O(f)+O(f)=O(f), protože se sčítají konstanty M
  a vezme se větší n0. Opačná inkluze plyne přičtením nuly.
- (8): O(O(f)) znamená sjednocení O(h) přes h v O(f).
  Odhady se skládají násobením konstant; opačný směr používá h=f.
- (9): součin odhadů pro u v O(f), v v O(g) dává uv v O(fg).
- (10): **po opravě z 20. ledna 2022 musí být f(n) nenulové
  pro každé n**. Potom pro h v O(fg) definujeme v=h/f všude;
  v je v O(g) a h=fv. Bez této podmínky může být h nenulové
  v počátečním bodě, kde f=0, takže doslovná inkluze selže.
  Jde o známé erratum, nikoli o nový nález.

## Komplexní proměnná poblíž nuly

Pro komplexní z znamená h(z)=O(f(z)) odhad
`|h(z)| <= M|f(z)|` v dost malém uzavřeném kruhu |z|<=r,
kde M,r>0. Není tím předpokládána analytická povaha h.
Jestliže mocninná řada `sum a_k z^k` konverguje v z0!=0,
jsou čísla a_k z0^k omezená. Srovnání s geometrickou řadou
tedy dává absolutní konvergenci pro |z|<|z0|. Pro pevné
0<r<|z0| je zbytek po stupni m omezen číslem

```text
|z|^(m+1) sum_{j>=0} |a_(m+1+j)| r^j.                    (O2)
```

To dokazuje (11). Vložením již ověřených generujících funkcí
dostáváme (12) pro exp z, (13) pro log(1+z), (14) pro (1+z)^a
a (15) pro `log(1/(1−z))/(1−z)`, jehož koeficienty jsou H_k.
Exponent a je pevný a větev logaritmu má v nule hodnotu 0.
Pro m=0 se nenapsané členy interpretují jako prázdný součet,
nikoli jako dosazení m=0 do izolovaného posledního členu 1/m.

Příklad exp z=O(1) je lokální: na |z|<=r platí |exp z|<=exp r.
Stejná konstanta nemůže platit pro všechna r, protože na kladné
reálné poloose exponenciála roste neomezeně.

## Dolní odhady, limity a úlohy 1–8,11,13

Zápis g=Omega(f) znamená, že existují L>0,n0 s
`|g(n)|>=L|f(n)|` pro n>=n0. Zápis g=Theta(f) znamená
současně tento dolní odhad a g=O(f). Nejde o tvrzení o
přesném vedoucím koeficientu. Nezáporný čas alespoň L n²
nakonec převýší čas nejvýše M n log n, protože n/log n roste
do nekonečna; samotná notace neurčuje bod, kdy k tomu dojde.

1. Každá funkce v O(n^(−1/3)) má limitu 0 přímým odhadem.
   Výrok není stejnoměrný přes všechny možné konstanty M.
2. Rozdíl dvou nezávislých členů O(f) je O(f), nikoli nutně 0.
   Například f−0=f; důkaz odhadu je trojúhelníková nerovnost.
3. Rozepsáním součinu získáme
   `n ln n+gamma n+O(sqrt(n) ln n)`. Zbylé členy jsou
   O(sqrt(n)), O(1) a O(n^(−1/2)), které tento odhad zahrnuje.
4. Pro pevné a>0 použijeme exp((ln a)/n) do stupně 3:
   `n(a^(1/n)−1)=ln a+(ln a)²/(2n)+(ln a)³/(6n²)+O(n^(−3))`.
   Platí i pro a=1, kdy všechny napsané členy vymizí.
5. Tvrzení je nepravdivé. Pro f=n²,g=1 je funkce n v O(f+g),
   ale n−n² není O(1), tedy n není v f+O(g).
6. Pro každé pevné k platí kn=O(n), ale konstanta závisí na k.
   Součet je přesně n²(n+1)/2=Theta(n³). Aby odhad
   `sum_{k=1}^n O(n)=O(n²)` měl použitý smysl, musí mít
   sčítané odhady společnou konstantu i práh pro všechny k<=n
   (nebo jediný výskyt O znamená stále stejnou funkci n).
   Rodina kn takovou jednotnost nemá. Toto je obsah knižního
   vysvětlení; nejde o důkaz pro libovolnou nejednotnou rodinu.
7. Pro celé m>=0 a x>0 dává řada exp x odhad
   `exp(x)/x^m >= x/(m+1)!`, který roste neomezeně.
   Pro m<0 a x>=1 stačí x^m<=1 a exp x→infinity.
   Stručná knižní odpověď výslovně rozepisuje první případ.
8. Položíme n=exp x. Pro m>=0 použijeme předchozí důkaz
   s exponentem m+1, který dává x^m/exp x→0; pro m<0
   je odhad ještě bezprostřednější. Knižní oprava „method of
   the previous exercise“ přesně vystihuje potřebný limitní krok.
11. ln n/n→0, takže z=ln n/n nakonec leží v kruhu platnosti
   (12). S m=1 dostaneme (18) a po násobení n rovnici (19).
   Logaritmus libovolného pevného základu b>0,b!=1 se od ln
   liší konstantním faktorem; uvnitř O((log n/n)²) je to jedno.
   Výrok o klesání n^(1/n) je asymptotický: derivace ln x/x
   je (1−ln x)/x²<0 pro x>e, tedy posloupnost klesá pro n>=3.
13. g=Omega(f) právě když f=O(g): stačí vyměnit konstanty
   M=1/L. Nedělíme žádnou funkcí, takže jsou zahrnuty i jejich nuly.

## Úlohy 9–10: exponenciála a logaritmus s chybovým členem

Pro libovolné komplexní w platí přímo z absolutně konvergentní řady

```text
|exp(w)−1| <= sum_{j>=1} |w|^j/j! <= |w| exp(|w|).        (O3)
```

Jestliže |h(z)|<=M|z|^m na |z|<=r, m>=0, pak pravá strana
(O3) pro w=h(z) je nejvýše `M exp(M r^m)|z|^m`.
To dokazuje úlohu 9 **včetně m=0**; tento případ pomocný Markdown
nesprávně vynechává. Pro m=0 se |z|^0 interpretuje jako 1.

Knižní odpověď po opravě z února 2008 odhaduje |exp(h(z))|
číslem 1+C|z|^m. **Tento samotný odhad nedává odhad vzdálenosti
od 1**: například funkce konstantně −1 má modul 1, ale rozdíl
od 1 má modul 2. Pro zamýšlený exponenciální výraz je potřebný
krok právě (O3), získaný stejnou řadou po vynechání konstanty.
Zaznamenáváme doplnění důkazu, ne nový nepravdivý vzorec:
upravené otištěné nerovnosti jsou pravdivé a celá věta platí.

Pro úlohu 10 vezmeme celé m>0. Zmenšíme r tak, aby
M r^m<=rho<1. Větev log(1+w), která je v w=0 nulová,
má pro |w|<=rho odhad

```text
|log(1+w)| <= sum_{j>=1} |w|^j/j <= |w|/(1−rho).
```

Tedy log(1+O(z^m))=O(z^m). Pro m=0 to obecně neplatí:
h(z)=−1+z je O(1), ale log(1+h(z))=log z není u nuly
omezený a není tam ani definovaný. Volba logaritmické větve
je podstatná; nevybíráme svévolně hodnoty posunuté o 2pi i.

## Rozsah a výsledek

Všechny matematické části hlavního textu a všech 13 úloh jsou
doloženy zde a v poznámce o faktoriálových rozvojích. Důkazy
jsou obecné; nebyl přidán program, který by jen opakoval tyto
elementární odhady na konečných vzorcích. Nový nález se nepotvrdil.
Historický pramen a známé opravy jsou zvlášť v
[asymptotic-notation-scope.md](asymptotic-notation-scope.md).
