# §4.2.2–28: vlastní obecný důkaz Diamondovy věty

Nechť b>=2 je celočíselný základ a p>=1 počet cifer. Množinu
plovoucích hodnot bez omezení exponentu označme S: obsahuje nulu
a čísla ±m b^e, kde b^(p−1)<=m<b^p a e je celé. R značí
zaokrouhlení na nejbližší prvek S; přesné poloviny lze rozhodovat
libovolným pevným pravidlem. V knize se navíc předpokládá, že
všechny mezivýsledky leží v dovoleném rozsahu exponentů.

Funkce f je na intervalu I přísně rostoucí a přísně konvexní nebo
konkávní; g je její inverze na f(I). Konvexita zde znamená, že
směrnice sečen na sebe navazujících intervalech přísně rostou;
u konkávní funkce přísně klesají. Položme F=R∘f, G=R∘g a h=G∘F,
vždy pouze tam, kde jsou uvedená vyhodnocení definována.
Dokážeme h³=h² pro b^p>=3.

Hlavní myšlenka: pokračující drift u konvexní funkce nutí bod,
k němuž jsme právě zaokrouhlili, být zápornou mocninou základu
(tj. číslem −b^e, nikoli obecně mocninou se záporným exponentem).
Dva další kroky by vyžadovaly dvě taková čísla příliš blízko sebe.
Přesnou podmínku dává lemma níže. Důkaz je vlastní; nedostupný
šestistránkový článek Diamond1978 tím není prohlášen za přečtený.

## 1. Geometrie mřížky

Pro nenulové z∈S označme z⁻ a z⁺ jeho bezprostředního předchůdce
a následníka a l(z)=z−z⁻, r(z)=z⁺−z. Pro nulu definujeme
l(0)=r(0)=0; nula nemá bezprostřední sousedy a R(t)=0 jen pro t=0.
Je-li R(t)=z, pak

    z−l(z)/2 <= t <= z+r(z)/2.                         (1)

Jediné body, v nichž l(z)>r(z), jsou z=−b^e. Tam platí
l(z)=b^(e−p+1) a r(z)=b^(e−p). V ostatních bodech l(z)<=r(z).
To plyne přímo z konstantní mezery uvnitř exponentového pásma;
při zvětšení absolutní hodnoty přes mocninu b se mezera násobí b.

Jsou-li a<c prvky S, pak

    2(c−a)−l(c) >= r(a).                              (2)

Je-li a=0, je pravá strana nula a levá kladná. Je-li c=0,
stačí c−a>=r(a), protože a⁺<0. Pro nenulové a,c: pokud c=a⁺,
obě strany jsou r(a). Jinak jsou disjunktní úseky
[a,a⁺] a [c⁻,c] uvnitř [a,c], a tedy c−a>=r(a)+l(c), což dává
ještě silnější nerovnost. Argument funguje i přes nulu; nevyžaduje
konečný počet plovoucích čísel mezi a a c.

## 2. Lemma pro tři střídající se zaokrouhlení

Předpokládejme nyní přísnou konvexitu f. Nechť plovoucí
hodnoty a<c a u<v splňují

    a=G(u), v=F(a), c=G(v).

Nutně a!=0: jinak g(u)=0, tedy f(0)=u∈S a v=u.
Také v!=0: jinak f(a)=0, tedy g(0)=a∈S a c=a.
Pišme L=l(a), M=l(c), T=l(v), D=c−a, E=v−u. Potom

    2D−M < L,   a tedy a=−b^e pro nějaké celé e.        (3)

Důkaz: Z u<v a v=R(f(a)) plyne f(a)>=v−T/2>u, protože
u<=v⁻=v−T. Z a<c a c=R(g(v)) podobně plyne g(v)>a.
Označme α=g(u), β=g(v); tedy α<a<β a všechny tři body leží v I.
Podle (1) máme a−α<=L/2 a β−a>=D−M/2>0. Při c=0 je
β=0 a M=0, takže tato mez platí i v nulovém kraji. Dále E>=T>0.
Přísná konvexita a zaokrouhlovací meze dávají

    (2E−T)/L
      <= (f(a)−u)/(a−α)
       < (v−f(a))/(β−a)
      <= T/(2D−M).                                   (4)

Protože 2E−T>=T>0, dostáváme 2D−M<L. Nerovnost (2) pak
vynutí r(a)<l(a), tedy a=−b^e. Použili jsme skutečné body
α,a,β v definičním oboru; nevyhodnocujeme f na středech
zaokrouhlovacích buněk, které by mohly ležet mimo I.

## 3. Dvě záporné mocniny nemohou vyhovět (3)

Pro a=−b^e<c=−b^d, e>d, je

    2(c−a) = 2(b^e−b^d),
    l(a)+l(c) = b^(1−p)(b^e+b^d).

Opačná nerovnost k (3), totiž 2(c−a)>=l(a)+l(c), je ekvivalentní

    2 b^(p−1) (b^(e−d)−1) >= b^(e−d)+1.               (5)

Poměr (t+1)/(t−1) pro t>1 klesá, takže stačí e−d=1.
Pro b>=3,p>=1 máme 2b^(p−1)(b−1)>=2(b−1)>=b+1.
Pro b=2,p>=2 máme 2b^(p−1)>=4>3. To pokrývá právě b^p>=3.
Hraniční případ b=3,p=1 dává rovnost; přísnost (3) ho vylučuje.

## 4. Iterace, konkávní funkce a směr driftu

Zaokrouhlení na nejbližší prvek uspořádané mřížky je monotónní,
a to i při libovolném pevném výběru přesných polovin. Proto jsou
F,G,h monotónní. Pokud x_i=h^i(x_0), posloupnost x_i je od prvního
kroku neklesající nebo nerostoucí. Rovnost sousedních členů znamená
stabilitu všech následujících členů.

Kdyby x_3!=x_2, všechny čtyři x_0,x_1,x_2,x_3 by tedy byly přísně
monotónní. Pišme y_i=F(x_i), i=0,1,2; i y_0,y_1,y_2 jsou přísně
monotónní, protože x_(i+1)=G(y_i). Žádný y_i nemůže být nula:
R(t)=0 nastává v tomto modelu pouze pro t=0, a pak by g(0)=x_i
vrátilo přesně x_i. Také x_1 a x_2 jsou nenulové; např. x_1=0
by znamenalo g(y_0)=0, tedy f(0)=y_0∈S, a x_2=x_1.

Uvažujme nejprve rostoucí posloupnosti. Je-li f konvexní, lemma
aplikované na

    (a,c,u,v)=(x_1,x_2,y_0,y_1)
    (a,c,u,v)=(x_2,x_3,y_1,y_2)

vynutí, že x_1 i x_2 jsou záporné mocniny b. První aplikace
současně dává (3), což odporuje (5). Druhá aplikace připouští
x_3=0 díky definici l(0)=0 a nulovému kraji ověřenému v lemmatu.

Je-li f konkávní, je g konvexní. Použijeme totéž lemma s prohozenými
f a g na čtveřice (y_0,y_1,x_0,x_1) a (y_1,y_2,x_1,x_2).
Pak y_0,y_1 musí být záporné mocniny b a první nerovnost opět
odporuje (5). Počáteční x_0 může být nula: v lemmatu se
vyskytuje jako u, na jehož nenulovost nebyl kladen žádný požadavek.

Klesající posloupnosti převedeme na rostoucí záměnou z za −z
na obou osách, tedy funkcí f*(t)=−f(−t), inverzí g*(t)=−g(−t)
a zaokrouhlením R*(t)=−R(−t). R* je opět zaokrouhlení na nejbližší
číslo. Konvexita se zamění s konkávností; žádná další podmínka
na rozhodování polovin není potřeba.

Tím je důkaz hotov. Přísná konvexita/konkávnost zaručuje ostrou
nerovnost (4); samotné výběry přesných polovin ji nemohou změnit
na rovnost. Nemusíme předpokládat existenci druhé derivace, pouze
přísnou konvexitu. Obvyklá formulace knihy pomocí neměnného
nenulového znaménka f'' je postačující.

## 5. Zdroje a kontrolní případy

Původní zadání str.245 a odpověď str.617 byly vizuálně přečteny;
oprava2025 mění slovo „precision“ na „fraction size“, nikoli větu.
Článek H.G.Diamond, *Math. Comp.*32(141),227–232(1978),
DOI10.1090/S0025-5718-1978-0461879-7, je bibliograficky potvrzen.
AMS vracelo403, JSTOR420; OpenAlex a SemanticScholar odkázaly
pouze na tentýž nedostupný soubor. Nezískal jsem jinou verzi důkazu.

Kontrola v `verify_accuracy_diamond.py` používá racionální rostoucí
funkce f(x)=A−K/(x−C), K>0, zvlášť na každé straně pólu C,
a přesnou racionální inverzi g(y)=C+K/(A−y). Jejich druhá derivace
má znaménko opačné k x−C. Program kontroluje nejen h³=h²,
ale i nerovnosti (3)–(4) u pokračujících přechodů a znaménkové
transformace. Jde o doplněk obecného důkazu, nikoli jeho náhradu.

Pro f(x)=115−35/(x−97), x>97, při desetinných dvouciferných
číslech dostáváme 110→100→99→99. Takže h²=h obecně neplatí.
Tento příklad byl nalezen přes sekundární odkaz na Diamondův
článek a zde je ověřen samostatně; jeho autorství původní sazbou
článku neověřeno. Ostrou nutnost vyloučit b2,p1 dokládá úloha29,
již přesně prověřená v `accuracy-iterations.md`.

Výsledek běhu:40 formátových bloků a jeden samostatný příklad,
52688 platných trojích iterací,814 aplikací pomocného lemmatu,
730 případů se změnou i ve druhém kroku, žádné porušení tvrzení.
Včetně358 nulových počátků a4078 nulových konců. Dalších33232
kombinací opouštělo zvolený definiční obor a bylo výslovně vyřazeno.
Formáty zahrnují i b2,p1; v této konečné rodině se protipříklad
nenašel, což nijak neoslabuje přesný protipříklad z úlohy29.
