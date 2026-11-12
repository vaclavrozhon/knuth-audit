# D104 — celá MPR1: netranzitivní kostky

6. listopadu 2026. Celé zadání na12/file32 a odpověď na370/file390
přímo zobrazeny; zadání navíc ve vyšším rozlišení, aby byla jednoznačná
každá tečka. Celá odpověď porovnána také s autorovým Pre-Fascicle5A,
tištěná27/file33. Níže jsou všechny tři části i matematický dovětek.

## Model a celá část(a)

Fyzických šest stěn je stejně pravděpodobných a různé kostky padají
nezávisle. Opakované počty teček dávají nerovnoměrné rozdělení
čísel, odtud „biased“. Očíslování/pořadí stěn nemění rozdělení
jednoho hodu. Pro každou dvojici je36 stejně pravděpodobných párů.

V pořadí vytištěných sítí, nejprve horní řádek zleva a potom dolní,
mají zadání tyto stěny:

```
A = (5,1,5,5,1,5),
B = (4,3,4,4,3,6),
C = (3,2,3,6,2,6).
```

Každá5 na A překoná všech pět stěn B kromě6, každá1 nepřekoná
žádnou. Počty jsou tedy přesně5+0+5+5+0+5=20.
Každá4 na B překoná dvě2 a dvě3 na C, každá3 jen dvě2,
a6 také dvě2 a dvě3, nikoli dvě další6. Tím dostáváme
4+2+4+4+2+4=20. Na C obě3 i obě2 překonají právě dvě1 na A;
každá6 překoná všech šest stěn A. Pořadí je2+2+2+6+2+6=20.
Všech18 tištěných dílčích sčítanců je tedy správných a všechny
tři pravděpodobnosti jsou20/36=5/9. Rovnosti čísel na různých
kostkách nejsou započítány jako výhry; například6 proti6 je remíza.

## Část(b), celá odpověď a její jedinečnost

Všechny stěny vytištěného řešení jsou

```
A = (3,3,3,3,3,6),
B = (2,2,2,5,5,5),
C = (1,4,4,4,4,4).
```

První duel má5·3+1·6=21 výher; druhý3·1+3·6=21; třetí
1·0+5·5=25. Výsledné7/12,7/12,25/36 jsou všechny striktně
větší než5/9, protože příslušné čitatele jsou větší než20.
To dokazuje požadovanou existenci a každý detail obrázku.

Odpověď navíc tvrdí jedinečnost při obvyklých počtech teček1,…,6.
Ta zde není převzata bez kontroly. Každá šestistěnná kostka se
v tomto modelu redukuje na jedno neklesající šestiprvkové slovo
nad1,…,6. Je jich C(11,6)=462: ekvivalentně šest nezáporných
četností se součtem6, tedy klasické rozmístění pěti oddělovačů
mezi šest položek. Je to úplný prostor, nikoli vzorek.

Program `verify_mpr001_dice.py` sestaví pro všech462² uspořádaných
dvojic přesný počet

```
w(A,B) = Σv=1..6 count_A(v) · Σu<v count_B(u).
```

Jeho každý člen počítá právě všechny páry se stejnou hodnotou v
na první kostce a menší hodnotou u na druhé; členy jsou disjunktní.
Hrana A→B existuje právě tehdy, když w(A,B)≥21, což je ekvivalentní
striktní pravděpodobnosti>5/9. Vzniklo55070 hran. Smyčka nemůže
existovat, protože u stejného rozdělení je P(A>B)≤1/2; ani opačné
hrany mezi dvěma kostkami nemohou existovat, neboť jejich počty
výher mají součet≤36<42.

Každé řešení je právě orientovaný trojúhelník A→B→C→A.
Kód projde každý možný nejmenší index a, každý jeho větší cíl b
a bitovým průnikem všech cílů b s předchůdci a najde všechna c>a.
Podmínka nejmenšího a vybírá jeden z přesně tří cyklických zápisů
daného orientovaného trojúhelníku; nic jiného nevyřazuje.
Jediný výsledný trojúhelník je právě vytištěná trojice. Jsou tedy
tři označená řešení, která se liší jen cyklickým přejmenováním A,B,C,
a jedno řešení po této přirozené identifikaci. Permutace fyzických
stěn se již nepočítají jako nové rozdělení.

Úplnost ověření plyne z uvedeného úplného výčtu kostek, přesného
kritéria každé hrany a obousměrné ekvivalence s trojúhelníky.
Všechny smyčky jsou konečné:462² párových výpočtů a nejvýše tolik
průchodů přes hrany; bitový průnik pouze určí dosud nevyjmenované
koncové vrcholy. Neprovádí se hledání nad všemi možnými počty stěn
nebo mimo rozsah1,…,6. Celá konkrétní kontrola trvala0.462024s,
nice15. Výsledky jsou v `results/sequential/mpr-001-dice.json`.
Žádný dřívější test nebo census se neopakoval.

## Část(c), všechny četnosti a Fibonacciho identita

Pro m≥2 položme a=F_{m−2}, b=F_{m−1}, N=F_m=a+b.
Obě a,b jsou nezáporná celá čísla a N>0. Konstrukce odpovědi je

```
A = a stěn s1 a b stěn s4,
B = N stěn s3,
C = b stěn s2 a a stěn s5.
```

Každá kostka má přesně N stěn; nulová četnost jednoduše vynechá
příslušnou hodnotu. A>B právě na b vysokých stěnách A a B>C právě
na b nízkých stěnách C, takže obě pravděpodobnosti jsou b/N.
Kostka C vyhraje buď svou hodnotou5 proti všem N stěnám A,
nebo hodnotou2 proti a nízkým stěnám A. Počet párů je

```
aN+ab = a(a+2b) = F_{m−2}F_{m+1}.
```

Rozdíl od bN je D_m=a²+ab−b². Přechod m→m+1 mění(a,b)
na(b,a+b) a tím

```
D_{m+1} = b²+b(a+b)−(a+b)² = −D_m.
```

Pro m=2 jsou a=0,b=1 a D_2=−1; indukce proto dává
D_m=−(−1)^m. Tím je vytištěná Fibonacciho identita dokázána
pro každý index použité konstrukce a výsledkem je přesně

```
P(C>A) = F_{m−1}/F_m − (−1)^m/F_m².
```

Znaménko je tedy určeno paritou m: plus pro liché, minus pro sudé.
Pro m=2 je konstrukce A=4,B=3,C=2, výsledky1,1,0, takže zahrnuje
i tento degenerovaný okraj. Pro m=1, pokud jej čteme jako jednou
stěnou každé kostky, může být A=1,B=3,C=5: výsledky0,0,1 přesně
odpovídají plus variantě s F0=0,F1=1. Autorova formule s F_{m−2}
se pro tento okraj nepoužívá bez obvyklého zpětného prodloužení
F_{−1}=1. Pro m=0 by nebyla žádná stěna, a nejde tedy o kostku.

## Matematický dovětek: libovolné n a asymptotika

Položme φ=(1+sqrt5)/2 a r=1/φ. Pak r²+r=1,0<r<1.
Pro libovolné celé n≥1 vezměme b=ceil(nr), a=floor(nr²).
Protože nr²=n−nr, platí a+b=n přesně; obě četnosti jsou
nezáporné a b≤n. Tatáž konstrukce dává

```
P(A>B)=P(B>C)=p=b/n,
P(C>A)=1−p².
```

Pišme b=nr+δ,0<δ<1 (nr je iracionální). První dvě
pravděpodobnosti jsou r+δ/n; třetí je

```
1−(r+δ/n)² = r−2rδ/n−δ²/n².
```

Všechny se tedy liší od r nejvýše(2r+1)/n. Jejich minimum
je třetí hodnota a konverguje k r zdola. Tištěný zápis
„1/φ−O(1/n)“ je tím doložen jako asymptotický odhad; znaménko
O samo nevynucuje kladný zbytek, a zde jsou první dvě skutečně
nad r, třetí pod ním. Nevydáváme všechny tři odchylky za záporné.

Také Fibonacciho poměr jde k r: ψ=(1−sqrt5)/2=−1/φ a
G_m=(φ^m−ψ^m)/sqrt5 splňuje tutéž rekurenci a počátky F0=0,F1=1,
takže G_m=F_m indukcí. Odtud

```
F_{m−1}/F_m = φ^(−1) (1−(ψ/φ)^(m−1))/(1−(ψ/φ)^m) → r,
```

protože |ψ/φ|=φ^(−2)<1. Člen1/F_m² jde rovněž k0.
To vysvětluje přímou návaznost úlohy2; její obecnou horní mez
neprohlašujeme za dokázanou touto samotnou konstrukcí.

## Errata, výjimky a uzavřený rozsah

- D104 uzavírá celé zadání1(a,b,c), všechny vytištěné mezikroky,
  obě sady18 stěn a matematický dovětek odpovědi1.
- Všech šest místních vrstev errat a dostupný původní TeX byly
  porovnány. E117 je známé bibliografické doplnění M. Purcell,
  AMM130(2023),421–436 z28.6.2023. Bylo přímo zobrazeno v all4b9;
  nejde o nový nález. Starší známá změna odpovědi Front2 na téže
  straně již patří E113 a není zde počítána podruhé.
- Savage1994, Buhler–Graham–Hales2018 a doplněný Purcell2023
  jsou výslovně bibliograficky vynechány. Potřebné konstrukce,
  počty a asymptotické argumenty mají vlastní důkazy výše.
- File32 zůstává partial, protože úlohy2–4 jsou další rozsah.
  File390 je partial: pouze MPR1 a dřívější přesný frontmatter
  rozsah jsou převzaty, Front3 a následující MPR2 se neuzavírají.
