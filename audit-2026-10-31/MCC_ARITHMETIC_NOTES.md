# Převody a heuristiky MCC: úlohy 163–170, 175–178

Kontrola 1. 11. 2026. Používáme původní DLX3 a nezávislé aritmetické
výpočty. Změna názvů mezí v 175 z 27. 3. 2024 nemění konstrukci;
chybějící koncová závorka v 166 je známé erratum z 26. 11. 2024.

## F070: n místo t v rekurenci 177(b)

Na str. 467 má binomický koeficient v součtu být `binom(t,k)`, nikoli
`binom(n,k)`. Proměnná n zde není definována. Správná rekurence je

```
Q(s,0) = Bell(s),
2 Q(s,t+1) = Q(s+2,t) + Q(s+1,t) - sum(k=0..t) binom(t,k) Q(s,k).
```

Důkaz: nové dvě kopie prvku nejprve odlišíme jako x,y a prohodíme je.
Rozklady pevné při prohození mají buď x,y ve stejném bloku
(`Q(s+1,t)`), nebo dva samostatné bloky se stejným zbytkem. Ve druhém
případě zvolíme z t dosavadních zdvojených prvků ty, jejichž kopie
rozdělíme mezi oba bloky; zbylých k typů dává `binom(t,k) Q(s,k)`.
Tyto druhé případy je třeba vyloučit, protože po ztotožnění x,y
vzniknou dva stejné bloky. Burnsideovo počítání proto dává uvedené
minus. Pro libovolné multipartice P jsou naopak povoleny a znaménko
je plus.

Nezávislá kontrola počítá koeficienty součinů `(1+x^v)` pro Q a
`1/(1-x^v)` pro P, přes všechny nenulové přípustné vektory v.
Všech 72 kombinací 0≤s,t≤5 a obou variant souhlasí s rekurencemi.
Oba číselné údaje knihy jsou správné: P(5,5)=91 914 202 a
Q(5,5)=75 114 998. Chybné n je vidět v PDF467 i PS171; nenalezeno
v all4b ani historickém all4f5 (vydaná str.275).

## F071: velká horní mez může změnit heuristiku167

Závěr odpovědi167 na str.463, že libovolné dvě hodnoty v_p≥M_p+2
jsou zcela ekvivalentní, neplatí při výslovně zvolené heuristice166.
Ta rozhoduje shodu priorit pomocí SLACK=v−u. Změna neomezující horní
meze proto může změnit zvolenou položku.

Pět možností je `A X`, `A Y`, `B U`, `B V`, `B W`. A,B jsou primární,
X,Y,U,V,W sekundární. A má meze [1,4] nebo [1,5], B má [2,6].
M_A=2 a M_B=3; obě porovnávané meze A splňují v_A≥M_A+2.

Na kořeni mají obě položky θ=2. Pro v_A=4 má A menší SLACK3 než
B se SLACK4 a větví se A. Pro v_A=5 jsou SLACKy4 shodné; delší
seznam B o třech možnostech má přednost. Tím padá už tvrzení,
že indukce zajistí stejné volby.

| v_A | První položka | Řešení | Uzly | Vyhledávací mems DLX3 |
|---:|---|---:|---:|---:|
| 4 | A | 12 | 37 | 1560 |
| 5 | B | 12 | 35 | 1368 |

Úplné logy jsou v `results/mcc_arithmetic/upper-bound-a*.log`.
Nezávislá rekurence pracuje pouze s počty zbývajících možností a
dolními mezemi; dává stejné profily po úrovních, nikoli jen součet.
Všechny horní meze jsou tak velké, že nikdy nevyloučí žádnou volbu.

Původní argument o rozdílu BOUND a SLACK funguje při pevném výběru
položek. Pro úplnou ekvivalenci je nutné navíc požadovat, aby změna
SLACK neovlivnila M3. Oprava se týká chování a rychlosti, nikoli
správnosti nalezených pokrytí. PDF463 a PS167 potvrzují znění;
v erratech nebyla tato oprava nalezena.

## Ostatní ověřené konstrukce

- 163: při prázdném seznamu je FT[l] záhlaví i, takže podmínka
  `a≤N` nastaví p=i a untweak provede nulový počet iterací.
- 164: null volby jsou právě záhlaví; x≤N je bezpečně odliší od
  datových uzlů. Podrobný návrh tisku stop nebyl implementován.
- 165: profil jedné položky je a_j=binom(j+d,d). Poměry
  a_(j+1)/a_j=(j+d+1)/(j+1) pro d>0 přísně klesají; tím vyplývají
  všechny použité součinové nerovnosti. Dva konkrétní profily mají
  340 a245 uzlů. Větvit položku s větší povinnou násobností je výhodné.
- 166: je-li zbylá dolní mez L>0, lze jako první vzít jen len−L+1
  možností; pro L≤0 je jich len+1 včetně null. Oříznutí nulou dává
  přesně tiskovanou monus-formuli. Závěr o délce seznamu plyne z165.
- 168: barevné pomocné položky vynucují prefix zvolených kopií.
  Pro každou násobnost0..2 a0..3 existuje právě jedno rozšíření.
- 169: nebarvená položka vybraného vrcholu vyloučí každého zvoleného
  souseda; společná barva0 nevybraných sousedů nezpůsobí falešný konflikt.
- 170: nevybraný vrchol volí první vybraný soused. Předchozí sousedé
  mají barvu0, tento barvu1, takže rozšíření je jednoznačné a zajišťuje
  maximalitu. Všechny grafy na1..4 vrcholech a všechny velikosti množin
  byly porovnány s přímým výčtem: 150 graf/varianta případů souhlasí.
- 175: u řetězového kódování označme z_i=1, pokud byla zvolena možnost
  obsahující α, jinak0. Sekundární x_i vynucuje z_(i−1)≤z_i.
  Každé přípustné opakování tedy má právě jeden monotónní řetězec.
  Ověřeno52 dvojic mez/požadavek, včetně nesplnitelných požadavků.
- 176: pomocné možnosti tvoří slovo A^u B^(h−u), protože sekundární
  položky zakazují sousední BA. Pro cílT a h=floor(T/2) tím získáme
  přesně rovnici počet_jedniček+2 počet_dvojek=T a jediné rozšíření.
  Celkem160 matic s nenulovými řádky, cíle2,3,4,11 a1..3 sloupce
  souhlasí s přímým výčtem podmnožin. Nulové řádky je třeba předem
  oddělit a na konci doplnit ve všech variantách; nejsou možnostmi MCC.
- 177: počty položek a možností souhlasí. Opakovat se smějí právě
  nenulové řádky bez jedničkových typů a s dvojkovými souřadnicemi0/1.
  Znak `b_i≠2` je ve výtisku správný; extrakce textu zahazuje lomítko.
- 178: specializovaný gadget pro exponent3 má právě tři možnosti
  doplnění, odpovídající 3=3,2+1,1+1+1. Přímý rekurzivní výčet
  rozkladů360 dává34 s různými faktory a52 s opakováním. MCC dává
  stejné počty, 29/37 možností a9+1/13+5 položek podle knihy.

Nebyly reprodukovány historické údaje o rychlosti výčtu multipartic.
Úlohy171–174 a179 do tohoto záznamu nepatří.
