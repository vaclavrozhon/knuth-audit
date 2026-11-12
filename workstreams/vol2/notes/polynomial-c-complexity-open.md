# §4.6.1–21: čas při větších poklesech stupně

Stav 4. listopadu 2026: uzavřeno, **V2-C0202 confirmed v přesně uvedeném
klasickém modelu**. Původní název souboru zůstal kvůli starším odkazům.
Úloha438 a odpověď677 uvádějí O(n^4(log(Nn))^2) bez předpokladu
na poklesy stupňů. Pro doslovný algoritmus R s hustým školským násobením
níže dáváme rodinu s N=2 a cenou Omega(n^5). Není to dolní mez pro
všechny implementace C ani pro samotný problém polynomiálního gcd.

Intuitivně: C3 odstraní velký společný faktor až **po** pseudodělení.
Při velkém poklesu stupně se proto v R opakovaně násobí mnohem delší
celá čísla, než jsou koeficienty normalizovaných členů posloupnosti.
Definice modelu je v §1, konkrétní rodina v §2 a přesný počet v §3.

## 1. Model a rozsah tvrzení

Délka nenulového celého čísla z znamená počet bitů jeho absolutní
hodnoty. Husté školské násobení dvou čísel délky a,b provádí a*b
průchodů vnitřní smyčkou. Je to algoritmus 4.3.1M, strana268, s vynechaným
**volitelným** testem nulové číslice M2. Pevná jiná báze než 2 mění
asymptotické odhady jen konstantou. Znaménka mají konstantní cenu.

Toto vymezení je podstatné: M2 lze také ponechat. Číslo -7*4^(D-1)
z našeho příkladu má v binární soustavě mnoho nul a násobení s tímto
číslem lze provést rychleji posunem a násobením sedmi. Níže netvrdíme
stejnou dolní mez pro tuto úpravu, pro rychlé celočíselné násobení,
pro ukládání koeficientů ve faktorizovaném tvaru ani pro sdružování
nulových kroků pseudodělení. Jde o standardní hustý klasický model,
v němž už neplatí neomezená redukce odpovědi677 na poklesy <=1.

Algoritmus R bereme přesně se smyčkou k=m-n,...,0 na426; ověřujeme
**obě** varianty: doslovnou i optimalizaci nízkých indexů v závorce R2.
Pseudoremainder prem(f,g) je jednoznačný zbytek r v identitě
lc(g)^(deg(f)-deg(g)+1) f = qg+r, deg(r)<deg(g), kde lc značí vedoucí
koeficient. Algoritmus C normalizuje tento zbytek dělením g*h^delta;
zde g,h označují jeho pomocná celá čísla a delta rozdíl stupňů.

## 2. Vstupy s konstantními koeficienty

Nechť D>=2, y=x^D a W=1+x+...+x^(D-1). Položme

```
A(y) = y^4+y^3+y^2+1,
B(y) = y^3-y^2-y+1,
u = W A(y), v = W B(y),
U = u+v, V = u.
```

Oba vstupy U,V jsou monické, tedy primitivní, stupně n=5D-1.
Každý jejich koeficient má absolutní hodnotu nejvýše N=2.
Po prvním kroku C s delta=0 je zbytek v; pomocné hodnoty g,h zůstávají 1.
Další normalizované nenulové zbytky jsou přesně

```
C = W (4y^2+y-1),
E = 4^(D-1) W (-7y+11),
H = 32 (-7)^(D-1) W.
```

Potom následuje nulový zbytek. Tato tvrzení plynou ze tří identit

```
A = (y+2) B + (4y^2+y-1),
16 B = (4y-5)(4y^2+y-1) + (-7y+11),
49 (4y^2+y-1) = (-28y-51)(-7y+11) + 512.
```

Dosazení x^D nemění racionální dělení, pouze rozdíly stupňů.
Společný monický faktor W násobí zbytky a nemění vedoucí koeficienty.
Proto prem(v,C)=4^(D-1)W(-7y+11). Po tomto kroku C má g=4,h=4^D.
V následujícím dělení C polynomem E jsou stupně 3D-1 a 2D-1, delta=D,
a vedoucí koeficient dělitele je

```
a = -7*4^(D-1).
```

Racionální zbytek je (512/49)W, takže syrový pseudoremainder je

```
a^(D+1)*(512/49)W = 512*(-7)^(D-1)*4^(D^2-1)W.
```

C3 jej dělí číslem g*h^D=4^(D^2+1), čímž přesně získá H.
Syrový zbytek má D nenulových koeficientů délky Theta(D^2), přestože
normalizované C,E,H mají pouze O(D) bitů v každém koeficientu.
Samotná velikost zbytku ještě není časovým protipříkladem; ten následuje.

## 3. Přesná dolní mez pro obě vytištěné varianty R

Pracovní koeficienty algoritmu R označme r_j, počátečně koeficienty C.
V prvním kroku k=D se najednou zruší celý nejvyšší blok W*4x^(2D).
Zbude stupeň nejvýše 2D-1. Proto jsou všechny následující koeficienty
r_(2D-1+k) pro D>k>=1 nulové: v těchto krocích R jen násobí číslem a.

Pro doslovnou variantu a 0<=j<D je před krokem k>=1 přesně
r_j=-a^(D-k). Pro optimalizaci v R2 se nejprve nastaví
r_j=-a^(D-j) a operace s j<k se vynechají. Jakmile k<=j<D,
je před krokem k opět r_j=-a^(D-k), což plyne indukcí od k=j.

Vyberme jen následující podmnožinu součinů a*r_j:

```
1 <= k <= floor(D/4),
ceil(D/2) <= j < D.
```

Pro D>=4 je j>=k, takže se tyto součiny provádějí v obou variantách.
Je jich floor(D/4)*floor(D/2)=Theta(D^2). První operand má přesně
2D+1 bitů; druhý má

```
floor((D-k)*log2(abs(a)))+1 = Theta(D^2)
```

bitů, rovnoměrně ve zvolené množině k. Každý součin proto vyžaduje
Theta(D^3) průchodů vnitřní smyčkou hustého M. Celkem dostáváme
**Omega(D^5)=Omega(n^5)**. Cena ostatních součinů, sčítání, inicializace,
výpočtu mocnin a následného přesného dělení je nezáporná a není potřeba.
Pro N=2 požaduje úloha O(D^4 log^2 D); poměr D/log^2 D roste bez omezení.
Tím je tvrzení v modelu §1 vyvráceno, včetně optimalizace uvedené v R2.

## 4. Co naopak platí: obecná horní mez a normální případ

Nechť původní stupeň je n>=1, N>=1 a L=max(1,log2(N(n+1))).
Vlastní determinantový důkaz v `subresultants.md` §§2–3 a §7 dává
pro normalizované členy a pomocné hodnoty g,h délku b=O(nL).
Při jednom pseudodělení s rozdílem delta mají pracovní koeficienty
O((delta+2)b) bitů: každý ze <=delta+1 kroků násobí vstupním
koeficientem délky <=b a sčítá dva výsledky. Rekurze
M_(t+1)<=2M M_t pro maximální absolutní hodnoty to dokazuje přímo.

V každém kroku je O(n) celočíselných součinů, z nichž jeden operand
má <=b bitů a druhý O((delta+2)b). Celé pseudodělení tedy stojí
O(n(delta+1)^2 b^2). Mocniny lze tvořit postupným násobením za
O((delta+1)^2 b^2). Podílový polynom C nepotřebuje; i kdyby se počítal,
stejné postupné mocniny a O(delta+1) součinů se vejdou do této meze.

Přesné dělení v C3 má dělitel délky O((delta+1)b) a výsledek délky
O(b). Školské dělení stojí O((delta+1)b^2) na koeficient, tedy
O(n(delta+1)b^2). Výpočet dalšího h postupnými mocninami a přesným
dělením má O((delta+1)^2 b^2), neboť výsledné h má O(b) bitů.
Počáteční obsahy a závěrečné odstranění obsahu mají O(nb^2) operací
klasickým celočíselným Eukleidovým algoritmem.

Rozdíly stupňů se sčítají teleskopicky: sum(delta)<=n a počet
pseudodělení je <=n+1. Proto sum(delta+1)^2=O(n^2), a máme platnou
obecnou horní mez **O(n^5 L^2)**. Je-li každý delta<=1 (nebo omezen
pevnou konstantou), součet je O(n) a dostáváme **O(n^4 L^2)**.
Jedna jednoduchá oprava úlohy tedy doplní předpoklad o rozdílech stupňů;
jiná oslabí obecnou horní mez. Existence vhodně upraveného rychlejšího
algoritmu není tímto důkazem vyloučena ani zde dokazována.

## 5. Primární literatura a přesný rozsah čtení

Collins, *Computing time analyses for some arithmetic and algebraic
algorithms*, sborník IBM1969,195–231: původní titulní195 je PDF181,
první textová197 je PDF182; nejde o chybu citace195. Vizuálně čteny
PDF181,182,184,185,193–199, tedy titul/úvod, aritmetický model199–200
a rozbor208–214. Na199–200 předpokládá klasické násobení. Věty3.13/3.14
a důsledek3.17 používají předpoklad slabě normální posloupnosti, tj.
následné stupně klesají po jedné. Na214 výslovně ponechává odstranění
podmínky pro primitivní variantu bez důkazu. Jeho redukovaná posloupnost
se mimo tento případ nemusí rovnat C; proto samotná citace není naším
protipříkladem. Ten je nezávisle dokázán v §§2–3.

[Primární záznam NASA](https://ntrs.nasa.gov/citations/19710009721)
a [celý sborník](https://ntrs.nasa.gov/api/citations/19710009710/downloads/19710009710.pdf).
Stažený sborník má302 strany; ostatní příspěvky nepovažujeme za prověřené.
Dřívější TR36 z1968 byl také získán, ale nebyl čten a není podkladem důkazu.

Brown, *The Subresultant PRS Algorithm*, ACM TOMS4(3),1978,237–249:
vizuálně čteny237,244–247,249, PDF1,8–11,13. Model na245 používá součin
velikostí operandů. Na247 rozlišuje normální případ; na249 uvádí
v hustém modelu čtvrtou versus pátou mocninu stupně. Sám označuje rozbor
za kvalitativní a v modelu ignoruje část růstu při sčítání; nepřebíráme
jej proto jako rigorózní důkaz obecné meze. Strana244 také ukazuje možnost
oddělit nadbytečné mocniny při nulových krocích. [Původní článek](https://people.eecs.berkeley.edu/~fateman/282/readings/brown.pdf).

## 6. Nezávislé přesné kontroly a evidence

`verify_polynomial_c_complexity.py` provedl35 hodnot D=1,...,32,48,64,96
v obou variantách R, celkem70 běhů rekurence C. Kontroluje každý vztah
lc(v)^(delta+1)u=vq+r, přesnost normalizace a celou uvedenou posloupnost.
Nezávislé racionální dělení dodává syrový zbytek bez pseudodělicí smyčky.
Každý součin z důkazové podmnožiny kontroluje konkrétní mocninovou identitu.
D=1 je navíc algebraická kontrola rekurence: program pokračuje přes
konstantní zbytek, zatímco skutečné C2 tam končí. Pro D>=2 se tato
odlišnost nevyskytuje; asymptotický důkaz používá D>=4.

Pro D=96 jsou vstupní stupně479, syrové koeficienty mají18706 bitů,
a vybraných1152 součinů dává3,579,591,072 průchodů školskou smyčkou
v každé variantě. Jde o **přesné účtování ceny modelu**, nikoli provedení
miliard násobení ani měření běhu M: Python počítá velká čísla vlastní
rychlou aritmetikou. Úspěšný běh1.433865s, PID1328304/session19900,
limit180s, exit0. První běh selhal na vlastním volání bit_length na
Fraction; po kontrole jmenovatele1 používáme numerator. Úspěšný běh
nebyl opakován.

Původní sazba knihy268,425–426,428–429,438,677 vizuálně přečtena.
Všech šest vrstev errat prohledáno podle stránek, sekce, autorů,
subresultantů a časových mezí; související změny20/22 a staršího vydání
nemění tvrzení21. V našem korpusu nenalezena odpovídající oprava.
C0202 znamená doložený problém **v modelu §1**, nikoli tvrzení o prvenství,
nejnovějším tištěném exempláři nebo všech realizacích algoritmu.
Návrh hlášení je uložen a neodeslán.
