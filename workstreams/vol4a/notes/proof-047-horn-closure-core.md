# Hornova věta, core a úlohy 7.1.1–44/45

Checkpoint X0076, P0722–P0729. Originál: text p57–58/file74–75,
zadání p85/file102 a odpovědi p543/file560. Obrazy file074.png,
file075.png, proof-file102.png a nově proof-file560.png.
Žádný program ani enumerace. Úplnost prime CNF se přesně přebírá
z proof-035, P0601; znovu se nedokazuje.

## Definice, všechny příklady a implikace — P0722

Hornova klauzule má po normalizaci nejvýše jeden pozitivní literál,
Kromova je disjunkce dvou literálů, které nemusí být různé.
Čtyři Hornovy příklady na p57 mají postupně 0,1,1,1 pozitivních
literálů. Šest Kromových příkladů je

    x∨x, ¬x∨¬x, ¬x∨¬y, x∨¬y, ¬x∨y, x∨y.

První se normalizuje na x, druhý na ¬x; jen poslední má dva
různé pozitivní literály. Tím souhlasí i vytištěné tvrzení,
že z těchto šesti pouze poslední není Hornův.
Na syntaktickém opakování x∨x nezakládáme falešný spor.

De Morganovo pravidlo a definice implikace dávají přesně

    ¬u∨¬v∨¬w∨¬x∨¬y∨z
      =¬(u∧v∧w∧x∧y)∨z
      =(u∧v∧w∧x∧y⇒z).

Obecná kladná hlava je důsledkem konjunkce záporných proměnných;
čistě záporná klauzule má jako hlavu nepravdu.
Prázdný předpoklad dává jednotkovou klauzuli.

## Theorem H: nutnost a všechny řádky vytištěné algebry — P0723

Vezměme dvě pravdivá přiřazení a,b pro klauzuli
x₀∨¬x₁∨⋯∨¬x_k. Při souřadnicovém meetu c=a∧b má klauzule hodnotu

    (a₀∧b₀)∨R=(a₀∨R)∧(b₀∨R),
    R=∨_{i=1}^k(¬aᵢ∨¬bᵢ).

První faktor je nejméně a₀∨∨¬aᵢ=1, druhý nejméně
b₀∨∨¬bᵢ=1. Celý součin je tedy 1. To dokazuje rovnost
i nerovnost v původním řetězci a zároveň případ k=0.
Pokud klauzule nemá pozitivní hlavu, už jediná její pravdivá
hodnota v a znamená některé aᵢ=0, a tedy cᵢ=0;
negativní klauzule proto také zůstává pravdivá.
Pro prázdnou zápornou klauzuli je předpoklad nesplnitelný.

Meet tedy zachovává každou Hornovu klauzuli i jejich konjunkci.
Prázdná konjunkce 1 je uzavřená také. Není tu předpokládána
monotónnost celé funkce, která pro Hornovy funkce obecně neplatí.

## Theorem H a44: obecná postačitelnost — P0724

Předpokládejme meet-uzavřenou pravdivou množinu f.
Z P0601 existuje úplná prime CNF. Stačí dokázat, že každá její
klauzule má nejvýše jeden pozitivní literál.

Předpokládejme naopak prime klauzuli c s pozitivními x_r,x_s.
Primalita je zde podstatný předpoklad z okolní věty H:
stručné „c is a clause“ v odpovědi44 jej nezrušuje.
Nahraďme v c literál x_r jeho negací a označme výsledek c'.
Kdyby i c' byla klauzulí/implikátem f, pak
c∧c' by byla c bez literálu x_r, což odporuje primalitě.
Existuje tedy pravdivý bod a falsifikující c':
a_r=1 a všechny ostatní literály c jsou nepravdivé.
Obdobně pro otočení x_s existuje pravdivý bod b s b_s=1
a všemi ostatními literály c nepravdivými.

V a∧b jsou x_r i x_s nulové. Každý další pozitivní literál
je nulový v obou bodech; každá proměnná negativního literálu
je jedničková v obou. Proto c(a∧b)=0, ve sporu s meet-uzavřeností
a s tím, že c je implikátem f. Tím je dokázána obecná klauzule
libovolné délky, ne pouze čtyřliterálový příklad.

V příkladu odpovědi c=x₁∨x₂∨¬x₃∨¬x₄ mají uvedení svědci
přesně první čtyři souřadnice a=1011,b=0111; meet0011
falsifikuje c, jak je požadováno. Hodnoty dalších proměnných
nejsou určovány ani nepotřebují být stejné.

Pro f=0 je pravdivá množina prázdná a reprezentací je prázdná
klauzule; pro f=1 je reprezentací prázdná konjunkce. Oba případy
jsou Hornovy a splňují podmínku včetně n=0.
Tím jsou ověřeny oba směry věty H i celá odpověď44.

## Definite Horn: přesná charakterizace — P0725

Při vstupu 1^n jsou všechny negativní literály nepravdivé.
Hornova klauzule tam platí právě když má pozitivní literál,
a po normalizaci tedy právě jeden. Konjunkce Hornových klauzulí
je proto definite, tj. f(1^n)=1, právě když má tento tvar každý
její člen. To zahrnuje jednotkové klauzule i prázdnou konjunkci.
Prázdná klauzule definite není.

Každá definite funkce má aspoň pravdivý bod 1^n, takže je
splnitelná. Nezaměňuje se definice funkce s libovolnou syrovou
formulí obsahující nesjednocené opakované literály.

## Nejmenší model, core a faktorizace — P0726

Pravdivá množina S definite Hornovy funkce je konečná a neprázdná.
Opakované použití binární meet-uzavřenosti dává
c=AND_{x∈S}x∈S. Tento c je souřadnicově ≤ každému pravdivému
vektoru, a je tedy jediným nejmenším pravdivým vektorem.

Bit c_j=1 právě když je x_j=1 v každém modelu. Core K je proto
přesně množina vynucených proměnných. Po dosazení x_j=1 pro j∈K
dostaneme funkci h zbývajících proměnných a přesnou faktorizaci

    f(x)=(∧_{j∈K}x_j) ∧ h(x mimo K).

Pokud některý core bit není 1, levá strana je 0; pokud všechny
jsou 1, rovnost je definicí h. Restrikce zachová Hornovu vlastnost
i definitnost; projekce nejmenšího modelu je nulový vektor,
takže h už nemá žádný core bit. Konstantní definite případ
a n=0 dávají prázdný core a prázdné součiny správně.

Tento důkaz platí i pro jakoukoli neprázdnou meet-uzavřenou
množinu; falešné funkci nepřipisujeme neexistující nejmenší model.

## 45(a): skutečná bijekce obou polovin — P0727

Označme top=1^n. Přidání top k meet-uzavřené množině S
zachová uzavřenost, protože top∧x=x.
Také odebrání top zachová uzavřenost: meet dvou vektorů
odlišných od top nemůže být top.

Proto přidání top je bijekce mezi indefinite a definite Hornovými
pravdivými množinami; inverzí je odebrání top. Na funkcích jde
o vytištěné g=f∨(x₁∧⋯∧x_n) a jeho jednoznačnou inverzi,
která změní jen hodnotu v top. Tím je dokázána i surjektivita,
nejen to, že vzniká nějaká definite funkce. Obě konečné třídy
mají stejnou velikost, tedy definite tvoří přesně polovinu
všech Hornových funkcí. Pro n=0 bijekce zamění konstanty0 a1.

## 45(b): přísná nerovnost počtů — P0728

Je-li f monotónní, pravdivá množina ¬f je dolní množina:
z f(x)=0 a y≤x plyne f(y)=0. Dolní množina je meet-uzavřená.
Pro f≠0 máme f(top)=1, takže ¬f je indefinite Hornova;
pro f=0 je ¬f identicky1. Komplementace je prostá.

Označme M počet monotónních funkcí, I počet indefinite Hornových
a H počet všech Hornových. Dostáváme M≤I+1 a z P0727 H=2I.
Pro n≥1 jsou alespoň tři různé monotónní funkce0,1,x₁, tedy M≥3.
Proto

    H≥2(M−1)>M.

To dodává chybějící explicitní krok k přísnosti; není třeba
počítat konkrétní katalog funkcí ani tvrdit množinové zahrnutí.
Při n=0 jsou M=H=2, přesně uvedená výjimka.

## Co na p57 dosud není důkazově uzavřeno — P0729

Příslib lineárních algoritmů pro splnitelnost čistě Hornových
a čistě Kromových CNF v délce vstupu N je samostatné tvrzení.
Z právě dokázané meetové charakterizace lineární implementace
neplyne. Zůstává **partial** do samostatné kontroly algoritmů C,
jeho obecného Hornova rozšíření48, a K v příslušném modelu.
Žádné staré pouhé přečtení algoritmu tento důkaz nenahrazuje.

P57 má nyní jednotlivě dokázány všechny definice, příklady,
implikační převod i celou větu H; proto další zpracovávaný text
začíná gramatikou na p58, se zachovanou mezerou P0729.
První odstavec p58 je hotový, zbytek gramatiky, pravidel a jejich
počtů je další blok. Stránky57/58 ani543 se zatím celé nepovyšují.

Relevantní all4a-pre, all4a, err4a, all4f0 a err4f0 byly prohledány;
pro tento výrok H/44/45 nebyla nalezena změna. Pozdější přepis
algoritmu C se bude řešit u algoritmu, nikoli přenášet sem.
Alfred Horn 1951, Lemma7, a historické vysvětlení volby Hornových
klauzulí v Prologu zůstávají bibliografickou výjimkou; důkaz
věty je zde vlastní a nepotřebuje tyto prameny.
Není nový nález ani kandidát.
