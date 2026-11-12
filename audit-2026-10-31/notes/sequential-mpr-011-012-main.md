# MPR 11 a hlavní text12: bin packing, a.s. a q.s.

D102–D103, 6. listopadu 2026. Celé původní file31–32 zobrazeny.
Tento blok uzavírá matematický hlavní text, nikoli úlohy1–4 začínající
na12. Celá strana12 proto zůstává partial. Každý následující odkaz
má buď zdejší důkaz, nebo přesně vymezené převzetí; není to soupis.

## D102 — bin packing a celý hlavní text str.11

**Model a existence optima.** Pro t objektů celočíselných velikostí
1≤xi≤m je přípustné každému objektu přidělit vlastní nádobu. Q je
minimum počtu nádob kapacity m mezi konečně mnoha rozděleními
objektů, takže existuje, 1≤Q≤t pro t>0; Q=0 pro t=0. Případně
lze pro konečnost použít všech t^t přiřazení objektů do očíslovaných
nádob a vynechat prázdné nádoby. Tím není tvrzena praktická účinnost
takového výpočtu. Q je na každém pevném konečném vstupním prostoru
omezená, tedy integrabilní.

**Omezený rozdíl jedné souřadnice.** Vezměme optimální balení
pro (x1,…,xt) a odstraňme objekt n. Zbývající objekty zůstanou
v nejvýše Q nádobách. Nový objekt x′n≤m lze vložit do jedné nové
nádoby, tedy Q(x1,…,x′n,…,xt)≤Q(x1,…,xn,…,xt)+1.
Výměna rolí x′n a xn dává opačný rozdíl≤1. Tím je(45) s cn=1
dokázáno pro každé optimum a pro každé zvětšení i zmenšení objektu.
Není třeba znát konkrétní optimální balení nebo algoritmus pro jeho
nalezení. D101 proto přímo dává(43) pro nezávislé, nikoli nutně
stejně rozdělené velikosti. Q i jeho očekávání jsou stejné náhodné
veličiny jako v definici Doobova procesu; nenahrazují se výstupem
heuristického balicího algoritmu.

**Přesný obsah složitostního výroku.** „NP-complete“ se zde čte
v obvyklém kontextu přidruženého rozhodovacího problému: zda lze
dané objekty zabalit do nejvýše k nádob. Výpočet optimálního Q
je pak nejméně stejně obtížný, protože odpoví testem Q≤k.
Není třeba považovat samotnou celočíselnou funkci Q za jazyk z NP.
Parametr m je zde součástí obecného vstupu v binárním zápisu;
nepřisuzujeme NP-úplnost všem případům s jednou pevnou konstantou m.

Následuje úplný redukční argument pro zde potřebné tvrzení, aby
matematická obtížnost nebyla jen neověřenou bibliografickou citací.

1. **Polynomiální verifikátor → 3-CNF.** Nechť jazyk má certifikát
   délky nejvýše T a deterministický verifikátor běžící nejvýše T
   kroků, kde T je polynom délky vstupu a je alespoň jeho délkou.
   Kratší certifikát lze doplnit na pevnou délku a připojit jeho
   původní délku; verifikátor čte pouze takto určený prefix. Tento
   převod mění délku i čas pouze polynomiálně.
   Standardní jednopáskový model lze použít přímo jako definici NP.
   V T krocích navštíví pouze O(T) buněk. Buňku reprezentujeme
   konečným počtem bitů pro symbol a případnou hlavu s řídicím stavem.
   V legální konfiguraci další obsah jedné buňky závisí jen na ní
   a dvou sousedech. Přechod je pevná konečná pravdivostní tabulka,
   tudíž pevný Booleův obvod; pro nelegální okolí zvolíme libovolný
   výstup. Počáteční konfigurace je legální a deterministický přechod
   legalitu zachovává, takže tyto libovolné výstupy nejsou dosažitelné.
   Pevné vstupní bity, proměnné certifikátu a T vrstev po O(T)
   takových obvodech dávají obvod velikosti O(T²). Dostatečně široký
   pás s rezervou T buněk po obou stranách zajistí, že se nikdy
   nedosáhne chybného okraje. Přijímací stav necháme absorbující;
   výstup testuje přijetí po T krocích. Obvod lze zkonstruovat
   v polynomiálním čase a je splnitelný právě pro přijatelný certifikát.
   Každou bránu vyjádříme pomocí AND a NOT. Pro g=u∧v přidáme
   (¬g∨u),(¬g∨v),(g∨¬u∨¬v); pro g=¬u přidáme(g∨u),(¬g∨¬u).
   Pevné bity a přijetí mají jednotkové klauzule. Každé přiřazení
   splňující tyto klauzule musí dodržovat hodnotu každé brány,
   a obráceně správný výpočet všechny klauzule splňuje. Počet
   proměnných/klauzulí je stále O(T²), délka každé klauzule≤3.
   Satisfiabilita takových formulí je v NP kontrolou přiřazení;
   tím je zde potřebná NP-úplnost 3-CNF doložena, ne předpokládána
   jako další neověřená citace.

2. **3-CNF → subset sum bez přenosů.** Vymažeme tautologické
   klauzule a opakované literály. Prázdnou klauzuli lze hned převést
   na pevný nesplnitelný balicí vstup; formuli bez klauzulí na pevný
   splnitelný. Zůstane n proměnných a r neprázdných klauzulí délky≤3.
   Použijeme n+r desítkových pozic. Pro každou proměnnou vytvoříme
   dvě kladná čísla T_i,F_i: oba mají1 v její vlastní pozici a0
   v ostatních proměnných; v pozici klauzule má T_i1, pokud ji daný
   kladný literál splňuje, obdobně F_i pro záporný. Pro každou
   klauzuli přidáme dvě pomocná čísla s jedinými číslicemi1 a2
   v její pozici. Cíl D má1 v každé proměnné a4 v každé klauzuli.
   Ani součet všech čísel nezpůsobí přenos: proměnná má nejvýše2;
   klauzule nejvýše3 výskyty literálů a pomocné1+2, tedy nejvýše6.
   Rovnost součtu s D proto nutí vybrat právě jedno T_i/F_i pro
   každou proměnnou. Počet splněných literálů klauzule je c∈{0,1,2,3}.
   Pomocná čísla mohou doplnit0,1,2 nebo3; číslici4 tedy dosáhnou
   právě když c≥1. To dokazuje oba směry ekvivalence.
   Počet čísel je2n+2r a každé má n+r desítkových pozic, tedy
   O(n+r) bitů. Konstrukce a její výstup mají polynomiální délku.

3. **Subset sum → dvě nádoby.** Označme původní kladná čísla a_i,
   jejich součet S a cíl0<D≤S. V předchozí konstrukci D>0;
   S≥D platí po pozicích, protože každá neprázdná klauzule má
   s pomocnými čísly alespoň4 a proměnná má2. Přidejme dva objekty
   velikostí S a2D a nastavme kapacitu m=S+D. Celkový objem je2m,
   každý objekt je kladný a nejvýše m. Dvě nádoby proto musí mít
   obě přesný objem m. Nádoba nemůže obsahovat oba nové objekty,
   neboť S+2D>m; nemůže obsahovat ani žádný z nich, neboť všechny
   původní objekty mají dohromady jen S<m. Je-li v ní S, potřebuje
   z původních čísel přesně D; je-li v ní2D, potřebuje S−D, jehož
   doplněk má D. To dává obě implikace mezi řešením subset sum
   a balením do dvou nádob. Sčítání a nové bitové délky jsou
   polynomiální. Pevné ano/ne vstupy pro vyřešené krajní formule
   mohou být například jeden objekt1 při m=1 (ano pro k=2),
   respektive tři objekty1 při m=1 (ne pro k=2).

4. **Členství v NP a důsledek pro Q.** Certifikát přiřadí každému
   objektu číslo nádoby nejvýše k≤t (větší k je triviálně ano).
   Součty objemů a jejich porovnání s m vyžadují polynomiálně mnoho
   bitových operací. Rozhodovací problém je tedy NP-úplný, dokonce
   uvedená redukce používá k=2. Přesný Q odpoví na něj porovnáním
   s2, takže obecná optimalizace je NP-těžká. Přesný E Q pro
   libovolné nezávislé vstupní distribuce je nejméně stejně obtížný:
   vezmeme degenerované distribuce s pravděpodobností1 na daném
   vstupním vektoru a E Q=Q. To je matematické podložení poznámky
   o obtížnosti průměru, nikoli tvrzení o prokázaném P≠NP.

Úplnost redukce nepřisuzuje autorství ani historickou prioritu;
Garey–Johnson1975 a McDiarmid1989 jsou bibliografické výjimky.
Věty o tom, že nikdo nezná dobrou obecnou metodu nebo že simulace
nedají rozumné meze, čteme jako kvalitativní výpočetní komentář
v tomto kontextu, ne jako nepravdivé tvrzení o neexistenci konečného
vyčerpávajícího algoritmu. Aktuální přehled všech známých efektivních
metod a experimentální vhodnost simulace zde nejsou ověřovány.

**Subaditivita β_t a celá limita.** Nyní je m pevné a objekty jsou
nezávislé se stejným rozdělením. Spojení optimálního balení prvních
s a dalších t objektů je přípustné balení všech s+t. Bodově tedy
Q_{s+t}≤Q_s+Q_t pro dva bloky; očekávání druhého bloku je stejné
β_t jako u prvního t-prvkového pokusu. Odtud β_{s+t}≤β_s+β_t.
β_0=0 a0≤β_r≤r, takže žádné použité očekávání není nekonečné.

Položme b=inf_{k≥1}β_k/k. Pro pevné k napišme n=qk+r,0≤r<k.
Konečná opakovaná subaditivita dává β_n≤qβ_k+β_r≤qβ_k+k.
Po dělení n a limitě n→∞ získáme limsup β_n/n≤β_k/k pro každé k.
Proto limsup≤b, zatímco z definice infima je každé β_n/n≥b.
Tedy lim β_n/n=b existuje. Argument pokrývá i zbytky r=0 a
nevyměňuje infimum s očekáváním. Odkaz na odpověď2.5–39 ve svazku1
na616/file631 je správný: její citovaná subaditivní část používá
právě rozklad do konečně mnoha zbytkových tříd. Zbytek této úlohy
o dynamické paměti se naším čtením neuzavírá.

**Přesná definice a.s. a všechny událostní kroky.** Zdejší a.s.
výslovně znamená lim_n P(A_n)=1, ekvivalentně lim_n P(A_n^c)=0,
protože P(A_n^c)=1−P(A_n). Není to záměna za tvrzení o jedné
události pravděpodobnosti1 na společném nekonečném prostoru;
kniha pracuje s uvedenou asymptotickou konvencí. Známá změna
E116 přidala výslovné slovo „asymptotically“ a v4B je zapracována.

Pro C_n=A_n∩B_n je C_n^c=A_n^c∪B_n^c. Bodově
[A_n^c∪B_n^c]≤[A_n^c]+[B_n^c], takže po očekávání dostaneme
přesně tištěnou nerovnost. Obě pravé strany jdou k0. Nezávislost
A_n,B_n nebyla použita. Konečnou indukcí jde o libovolný pevný
počet takových událostí; počet se v tomto tvrzení nemění s n.
Pro(46) je komplement přesně sjednocením dolního ocasu S_n≤.49n
a horního S_n≥.51n. To ověřuje i všechny ostré/neostré konce
vět přecházejících ze11 na12.

## D103 — hlavní text str.12, před začátkem úloh

**Mince, symetrie a číselný exponent.** Nezávislé férové bity
mají P každého n-bitového slova2^{-n}. Záměna všech bitů za jejich
doplňky je bijekce zachovávající pravděpodobnost a mění S_n na n−S_n.
Proto P(S_n≤.49n)=P(S_n≥.51n), včetně necelých prahů.
Původní zadání1.2.10–21 na106/file121 a jeho odpověď na502/file517
byly přímo zobrazeny. Dolní ocas v odpovědi má exponent
−ε²n/(2p); při p=1/2,ε=.01 je to přesně −.0001n.

Potřebná nerovnost má navíc nezávislý zdejší důkaz: pro
Y_i=X_i−1/2 je férovost důsledkem nezávislosti a každý interval
[−1/2,1/2] má šířku1. D100 s x=.01n dává dokonce
P(S_n≤.49n)≤exp(−.0002n)≤exp(−.0001n). Nejde tedy jen
o nalezení stejného čísla v jiném svazku. Celá obecná úloha
svazku1 se tím nepřebírá; potřebný speciální případ je dokázán.

**(47), všechny kvantifikátory a (48).** Pro každý pevný reálný K
zvolme celé j>max(K,0). Z kladné exponenciální řady plyne
exp(cn)≥(cn)^j/j!, tedy

```
exp(−cn)≤j! c^(−j)n^(−j)=O(n^(−K)),  c=.0001>0.
```

Konstanta smí záviset na pevném K, ne na n. To je přesně(47).
Q.s. znamená tuto vlastnost pro pravděpodobnost *komplementu*;
v původní sazbě je nad A_n skutečně čárka. Dva ocasy dávají
P(neplatí(48))≤2exp(−.0001n), které má tutéž vlastnost. Q.s.
také implikuje a.s. například volbou K=1. Nevyžaduje se společný
nekonečný prostor ani přenos do silnějšího pravděpodobnostního pojmu.

**Polynomiální počet událostí: výslovná uniformní interpretace.**
Je-li |I_n|≤C n^d a pro každý pevný L existují C_L,N_L tak, že
pro všechna n≥N_L a všechna i∈I_n platí
P(A_{n,i}^c)≤C_L n^{-L}, pak pro požadované pevné K zvolíme
L=K+d (případně větší kladné celé číslo). Unijní mez dává

```
P(∩_{i∈I_n} A_{n,i} neplatí)
 ≤ Σ_{i∈I_n}P(A_{n,i}^c) ≤ C C_L n^(d−L)=O(n^(−K)).
```

Toto je přesný běžný uniformní smysl výroku o polynomiálním
počtu q.s. událostí. Při rostoucím souboru indexů je uniformita
důležitá a zde je vypsána, ne schována za samotnou zkratku q.s.
Pouhá q.s. pro každé *pevné* i bez společných konstant by nestačila:
P(A_{n,i}^c)=[n=i] dává pro každý pevný i nakonec nulovou chybu,
ale průnik i≤n neplatí nikdy. Tato slabší interpretace není použita
k doložení textu ani ke vzniku nové karty; jde o transparentní
kontextové vymezení potřebné asymptotické domény.

**Všech n^4 lidí.** Každý má stejnou individuální mez
2exp(−.0001n); ta je již uniformní v indexu člověka. Proto
P(někdo selže)≤2n^4 exp(−.0001n). Předchozí důkaz s libovolným
L nebo přímo exponenciální řada ukazuje q.s. všech najednou.
Vzájemná nezávislost různých lidí se zde nepotřebuje; nezávislé
hody jsou použity jen uvnitř každého individuálního rozdělení.

**Poznámka o700000.** Její slovo „negligible“ nemá číselně
definovanou hranici, ale konkrétní velikost tištěné horní meze
lze ověřit. Tři cílené výpočty s přesnými racionálními mezemi
exponenciály dávají

| n | 2 n^4 exp(−.0001n), přibližně |
|---:|---:|
|500000|24.10937309955|
|600000|0.002269687590|
|700000|0.0000001909010963|

První číslo je jen nepoužitelná horní mez, nikoli pravděpodobnost
větší než1. Pro n=700000 je doloženo přesně <2·10^{-7}.
Logaritmická derivace4/n−.0001 je záporná pro n>40000, takže
od tohoto bodu mez dále klesá. Pro každý z exponentů50,60,70
bylo vzato181 kladných členů řady; poměr dalších členů je nejvýše
x/182<1, což dává geometrickou horní mez zbytku. Obě strany
pro požadovaný výraz pak vzniknou obrácením těchto kladných mezí.
Doklad je `results/sequential/mpr-012-numerical-bound.json`.

## Známá oprava, výjimky a přesný konec bloku

- E116: all4f5/err4f5,21.6.2022, str.11 řádek−6, doplnění
  „It's asymptotically almost sure.“ Ověřeno v původním TeX
  a přímo zobrazené stránce3 all4f5. V našem4B file31 je již
  správný doplněk. Je to známá změna, nikoli nový nález.
- Šest vrstev errat posouzeno pro hlavní text11–12. Renderování
  starého all4f5 hlásilo Type3 bounding-box warnings; cílový řádek
  byl následně přímo vizuálně ověřen a je jednoznačně čitelný.
- Bibliograficky vynechány články Garey–Johnson a McDiarmid,
  historie dostupných účinných metod a původ/datum literárního
  citátu P. D. Jamesové. Matematická složitost, koncentrace a limita
  mají vlastní konkrétní důkazy výše.
- D102 uzavírá matematický obsah file31 s těmito výjimkami.
  D103 uzavírá pouze hlavní text file32 nad nadpisem EXERCISES.
  Úlohy1–4 této strany ještě nejsou zkontrolované; stránka partial.
- Žádná zdejší pomocná redukce ani numerický údaj nevyžadují
  spuštění censusů; jediný nový výpočet byl tříbodový racionální
  odhad nice15. Staré procesy a neúplné výsledky zůstaly zachovány.
