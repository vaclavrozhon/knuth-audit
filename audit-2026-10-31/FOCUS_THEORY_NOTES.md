# Součty vyhledávacích stromů a lokální výměny

Kontrola 1. listopadu 2026. Rozsah: obecné výsledky 203–206 a 210–214;
nikoli konkrétní obrázek 202, aktivita 207 ani velký výčet Y-pentomin 208.

## 203–206: obecné důkazy

Stupeň uzlu řešení je nekonečno; stupeň ostatních je počet dětí.
Součet vybírá nejmenší stupeň, při shodě levý strom. Pro tři stromy tedy
oba způsoby uzávorkování vždy vyberou nejlevější z globálně minimálních
stupňů. Indukce přes počet zbývajících uzlů dokazuje asociativitu.
Komutativita neplatí: vezměme unární kořen s dítětem řešení a unární kořen
s mrtvým dítětem. V jednom pořadí dostaneme dva unární kroky, v druhém jen jeden.

V součtu má dvojice uzlů a,b stupeň min(d(a),d(b)). Pro každého vlastního
předka a_k uzlu a existuje na cestě okamžik, kdy se právě postupovalo z a_k;
stupeň tehdejší dvojice byl přesně d(a_k). Je-li výsledná dvojice dominantní,
musí být tento stupeň menší než min(d(a),d(b)), takže a je dominantní.
Totéž platí pro b. Obrácená implikace neplatí již u dvou unárních kořenů:
po prvním levém kroku může být levá složka řešením a pravá stále kořenem,
obě dominantní, ale dvojice má stejný stupeň 1 jako její rodič.

Lemma D lze dokázat přímo. Kdyby a i b byly nedominantní, označme A a B
maximální stupně na jejich cestách včetně samotných konců. Oba maxima se
vyskytují už na vlastních předcích. Při opuštění levého předka stupně A
musel být pravý stupeň alespoň A, tedy B≥A. Při opuštění pravého předka
stupně B musel být levý stupeň **větší** než B, což odporuje A≤B.
Nekonečné stupně tento případ neovlivní, protože řešení jsou dominantní.

Je-li T minimálně dominantní a jeho kořen má stupeň nejvýše stupně kořene
T', každý jeho vnitřní uzel má stupeň nejvýše původního levého kořene.
Součet proto zpracuje T až k řešení a teprve tam začne T'. To je přesně
nahrazení každého listu řešení kopií T', jak uvádí 206.

[check_focus_theory.py](check_focus_theory.py) prošel všech 122 označených
uspořádaných stromů do pěti uzlů: 14 884 dvojic, 129 300 dvojic uzlů,
6 491 případů nahrazování listů. Dále 10 000 trojic pro asociativitu.
Testy podporují výše uvedené obecné důkazy; žádný nový nález.

## 210–211: vyšší výměny a neexistence bipárů

Omezení násobnosti nové položky #A na 0,…,2 zakáže právě současnou volbu
tří vyznačených možností. Je potřeba neostrý režim preference Algorithm M,
jak odpověď správně uvádí.

Langford: na čtyřech polohách w<x<y<z jsou tři párování. Součet délek
sousedního párování je menší než u zbylých dvou; u vnořeného párování je
největší délka větší než u křížícího. Dvě různá párování proto nemohou mít
stejnou dvojici předepsaných vzdáleností. Při stejném číselném štítku by se
možnosti navíc překrývaly v primární položce. Bipár tedy není možný.

Dámy: jediná případná změna dvou polí se zachováním řádků a sloupců je
výměna protilehlých rohů obdélníku. Ta nezachová množiny diagonál; nejmenší
nebo největší součet souřadnic se změní. Pomocné slack možnosti tento
závěr nemění, protože by u dvojice nechaly nejvýše jednu dámu.

Sudoku: při výměně dvou různých číslic mezi dvěma poli musejí být jejich
řádky stejné, aby se zachovaly řádkové položky; obdobně musejí být stejné
sloupce. Pak by ale šlo o totéž pole. Pro stejné číslice jsou možnosti
určeny samotnými poli. Bipár opět není možný.

Existenci vyšších výměn ukazují konkrétní svědci: Langford n=3,
231213 ↔ 312132, mění tři možnosti; Langford n=4,
41312432 ↔ 23421314, mění čtyři. Dámy n=4, 2413 ↔ 3142,
zachovávají všechny čtyři množiny řádků, sloupců a diagonál. U sudoku
stačí čtyři rohy 2×2 uvnitř jednoho boxu s číslicemi ab/ba ↔ ba/ab.

## 212–214: kanonické výměny a pořadí rozkladů

Nejmenší položka celé výměny se vyskytuje právě v a,a'. Možnosti b,b'
proto mají větší nejmenší položku. Seřazení podle nejmenší položky a pak
lexikograficky tedy dává a<b, a<a', a'<b', přesně předpoklad Theorem S.

Pro pořadí rozkladů v 213 je nutné chápat vlastní prefix jako **větší**
řetězec. Obyčejná slovníková konvence opravdu selhává, například pro
a={0}, b={1,2}, a'={0,1}, b'={2}: RGS 011 je větší než 001.
Při opravené konvenci nejlevější změněné místo RGS obsahuje v původním
rozkladu menší číslo bloku. Ostatní bloky nemohou vytvořit dřívější rozdíl:
změna jejich pořadí nastává až za prvním změněným minimem dvou nahrazovaných
bloků. Úplný výčet rozkladů do sedmi položek potvrzuje 17 199 uspořádaných
výměn, včetně 5 357 případů, kde obyčejné slovníkové pořadí směr obrací.

Každá kanonická redukce zvyšuje binární vektor vybraných možností v pevném
lexikografickém pořadí. Konečný orientovaný graf řešení je tedy acyklický
a každý vrchol dosáhne nějakého silného řešení. Obrácené procházení hran
ze všech silných řešení dosáhne všech řešení; duplicity se musí sjednotit.
To potvrzuje obecný postup 214. Konkrétní grafický příklad nebyl samostatně
strojově přepsán.

Strojová data: [verified.json](results/focus_theory/verified.json).
