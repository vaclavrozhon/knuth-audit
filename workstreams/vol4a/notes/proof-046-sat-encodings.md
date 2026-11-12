# Úlohy 7.1.1–40 až 43: SAT kódování a smíšené klauzule

Checkpoint X0075, P0711–P0721. Originál: p85/file102 a p542/file559,
images/proof-file102.png a images/proof-file559.png. Pro význam
Horn/Krom byla přečtena definice na p57/file74, images/file074.png.
Úplné algoritmy a jejich lineární meze tím ještě prověřeny nejsou.
Žádný matematický program.

## 40: A a B jsou přesně lineární uspořádání — P0711

Uvažujme nejprve konečný neprázdný neorientovaný graf s r vrcholy.
Proměnné p_uv existují právě pro u≠v. A vyžaduje pro každou
dvojici právě jednu z hodnot p_uv,p_vu rovnu 1. Definujme
u<v právě když p_uv=1, s u<u nepravdivým.

Každá klauzule B je p_uv∧p_vw⇒p_uw pro tři různé vrcholy.
Při u=w by oba předpoklady odporovaly A, takže tato omezená
doména stačí pro celou tranzitivitu. Relace je tudíž ostré
úplné uspořádání. Konečná taková relace má jednoznačnou posloupnost
všech vrcholů: existuje nejmenší prvek, protože jinak by postupné
volby předchůdců vytvořily cyklus, v rozporu s tranzitivitou;
pak pokračujeme indukcí po jeho odstranění.

Obráceně každé pořadí dává model A∧B. Dvě různá pořadí mění
relaci některé dvojice, takže existuje přesně r! modelů A∧B,
jak uvádí odpověď. Nejde o počet Hamiltonových cest ani o dělení
dvěma kvůli obrácenému pořadí.

## 40: přesná doména a význam pomocných proměnných — P0712

q_uvw existuje jen při třech různých vrcholech a nehraně u–w.
Není požadována hrana u–v ani v–w; tuto důležitou doménu
potvrzuje původní sazba zadání.

Tři klauzule C jsou

    q⇒p_uv,  q⇒p_vw,  (p_uv∧p_vw)⇒q.

Proto q_uvw je právě indikátor u<v<w. Pro každé pořadí je
rozšíření o všechny q jednoznačné; žádný další stupeň volnosti
neumožní obejít nehranu.

## 40: D a Hamiltonova cesta — P0713

Pro každou nehranu mezi různými u,w klauzule D vyžaduje
nějaký v odlišný od obou s q_uvw∨q_wvu=1. Podle P0712 tedy
existuje vrchol přísně mezi u a w v jednom ze dvou směrů pořadí.

Konečná dvojice není sousední v pořadí právě tehdy, když mezi
ní leží třetí vrchol. D tedy říká, že žádná nehrana není
sousední dvojicí pořadí, ekvivalentně všechny sousední dvojice
jsou hranami G. Pořadí je proto Hamiltonova cesta.

Obráceně z Hamiltonovy cesty nastavíme p podle jejího pořadí
a q podle prostřednosti. A/B/C pak platí a každá nehrana má
alespoň jeden mezilehlý vrchol, takže platí i D.
To jsou oba směry, nejen nutná podmínka.

Pro r=1 jsou všechny rodiny klauzulí prázdné a jediný vrchol
je triviální Hamiltonova cesta. Pro r=2 je při nehraně D prázdnou
disjunkcí, tedy nepravdivé; při hraně jsou dvě orientace přípustné.
Pro prázdný graf je formule pravdivá a koresponduje s prázdným
pořadím. Zda se toto nazývá „Hamiltonova cesta“, závisí na
konvenci prázdné cesty; zde se tato konvence samostatně neuzavírá
a nevzniká kvůli ní karta. Dokázaná ekvivalence je bezpodmínečná
pro neprázdné grafy. Tato přesná doménová mez brání tvrzení,
že jsme bez výhrady uzavřeli všechny formulace celé p542.

## 40: náklady konstrukce — P0714

Pro r≥2 a h neuspořádaných nehran je proměnných p právě r(r−1),
proměnných q právě 2h(r−2). Při počítání vytištěných výskytů,
včetně opakovaných klauzulí pro opačně uspořádanou dvojici:

- A má 2r(r−1) dvouliterálových klauzulí.
- B má r(r−1)(r−2) tříliterálových klauzulí.
- C má 6h(r−2) klauzulí, celkem 14h(r−2) literálů.
- D má 2h klauzulí po 2(r−2) literálech, včetně prázdných při r=2.

Celková velikost je O(r³) proměnných i literálových výskytů
a pro r≥3 už samotné B má Θ(r³) výskytů.
S explicitním grafem lze formuli v této době vytvořit; binární
zápis indexů přidává faktor O(log r). Není tím tvrzen
polynomiální algoritmus pro rozhodnutí její splnitelnosti.

## 41: konstanta a první kódování — P0715

Každý holub potřebuje alespoň jednu vlastní díru. Výběr jedné
takové díry každému holubu je injekce do n děr, takže nutně m≤n.
Při m≤n lze přiřadit holubu j díru j. Proto konstantní formule
[m≤n] v odpovědi0 má přesně požadovanou splnitelnost.

První skutečné kódování má proměnné x_jk a klauzule

    ∨_{k=1}^n x_jk  pro každého holuba j;
    ¬x_ik∨¬x_jk    pro i<j a každou díru k.

První rodina dává každému holubu díru a druhá zaručuje, že ji
žádný jiný neobsadí. Při splnění mohou někteří holubi získat více
děr; to nevadí formulaci úlohy ani výběru injekce. Obráceně
každá injekce dává model. Není zapotřebí doplňovat „právě jednu“.

Pro m=0 je konjunkce prázdná a pravdivá. Pro n=0,m>0 obsahuje
prázdnou klauzuli a je nepravdivá. Pro m,n≥1 má mn proměnných,
m+n binom(m,2) klauzulí a přesně mn+2n binom(m,2)=m²n
literálových výskytů. To ověřuje vytištěnou velikost Θ(m²n)
v obvyklém nenulovém rozsahu; prázdné klauzule se evidují zvlášť.

## 41: binární kódování a všechny čtyři klauzule XOR — P0716

Nechť n=2^t. Holub j dostane t-bitový kód díry. Podmínka
různých děr pro i<j je ∨_{k=1}^t(x_ik XOR x_jk).
Pro každou dvojici a bit zaveďme y=y_ijk a pišme a=x_ik,b=x_jk.
Čtyři vytištěné klauzule jsou

    (¬y∨a∨b), (y∨¬a∨b), (y∨a∨¬b), (¬y∨¬a∨¬b).

Pro a=b=0 první vynutí y=0; pro a=b=1 poslední vynutí y=0;
pro (a,b)=(1,0) druhá vynutí y=1; pro (0,1) třetí vynutí y=1.
Ostatní klauzule jsou v příslušném případě automatické.
Jde tedy přesně o y=a XOR b. Přidáním ∨_k y_ijk pro každou
dvojici získáme právě navzájem různé kódy, a tedy injekci.

Pro t=0 má každá dvojice prázdnou klauzuli: jedna díra pojme
nejvýše jednoho holuba. Pro m≤1 nejsou žádné párové klauzule.
Pro m≥2,t≥1 jsou mt původní a t binom(m,2) pomocné proměnné,
(4t+1)binom(m,2) klauzule a 13t binom(m,2) literálů.
Velikost je tudíž Θ(m² log n) v uvedeném netriviálním rozsahu.

## 41: známé vypuštění dvou XOR klauzulí — P0717

all4a-pre, p542 řádek9 odpovědi41, 11.4.2014, přidává poznámku,
že postačí první a poslední ze čtyř klauzulí. Tyto dvě klauzule
vyjadřují pouze y⇒(a XOR b), nikoli ekvivalenci.

Párová klauzule ∨_k y_ijk přesto nutí alespoň jednu skutečně
odlišnou souřadnici, a tedy nerovnost kódů. Obráceně při různých
kódech stačí zvolit y=1 pro jednu odlišnou souřadnici a y=0
pro ostatní; obě implikační klauzule pak platí. Je tedy zachována
požadovaná existenční ekvivalence, ale ne obecně jednoznačnost y.

Po této známé optimalizaci je na dvojici 2t+1 klauzulí
a 7t literálových výskytů. Asymptotická mez se nemění.
Oprava je ověřena v obou směrech, nikoli jen převzata podle textu.

## 41: nepřípustné binární kódy a cena jejich vyloučení — P0718

Pro libovolné n≥1 vezměme t=ceil(lg n) a očíslujme díry 0,…,n−1.
Označme t-bitový zápis M=n−1 b₁…b_t. Pro každou nulovou pozici
b_k=0 zakažme prefix x₁…x_{k−1}=b₁…b_{k−1}, x_k=1 klauzulí

    (∨_{i<k}(x_i XOR b_i)) ∨ ¬x_k,

kde XOR s konstantou je jediný literál. Počet klauzulí je
nejvýše t a každá má nejvýše t literálů. Každý kód větší než M
má první rozdíl právě tohoto typu a jednu klauzuli poruší;
každý kód ≤M všechny splní. To je nutná i postačující hranice.

Za všechny holuby jde o O(m log n) klauzulí šířky O(log n),
přesně jak uvádí odpověď. Celková cena tohoto přímého způsobu
je O(m²t+mt²) literálů, nikoli bez dalšího Θ(m²t) pro všechny
společné růsty m,n. Pro mocninu dvou není třeba žádná klauzule,
protože M má samé jedničky. n=0 se řeší přímým případem P0715.

## 42: skutečně nesplnitelná Hornova i Kromova formule — P0719

Vytištěná formule je

    (¬x∨y) ∧ (¬z∨x) ∧ (¬y∨¬z) ∧ (z∨z).

Poslední klauzule dává z=1, druhá x=1, první y=1 a třetí spor.
Každá klauzule je Kromova; po idempotentním zjednodušení
z∨z=z je také Hornova. Toto zjednodušování opakovaného literálu
je výslovně dovoleno už v definici na p57.

Formule je navíc minimálně nesplnitelná: po vynechání první,
druhé, třetí či čtvrté klauzule dostáváme postupně svědky
(x,y,z)=(1,0,1), (0,0,1), (1,1,1), (0,0,0).
Její netriviálnost tedy není jen subjektivní popis odpovědi.

## 43: vytištěná náhrada jedné klauzule — P0720

Klauzule x₁∨x₂∨¬x₃ je nahrazena

    (x₁∨¬y∨¬x₃) ∧ (¬y∨¬x₂) ∧ (y∨x₂).

Poslední dvě klauzule přesně vynucují y=¬x₂: zakazují (1,1)
a (0,0). První je pak původní klauzule. Vynucené y je jediné,
takže platí dokonce bodová existenční ekvivalence pro každé x.
První klauzule je Hornova, zbývající dvě Kromovy; poslední má
dva pozitivní literály a není Hornova.

## 43: úplná redukce všech 3CNF — P0721

Vytištěný příklad má dva pozitivní literály, ale obecná věta
musí zahrnout i ostatní znaménka. Klauzule s nejvýše jedním
pozitivním literálem už je Hornova. Při dvou nebo třech
pozitivních literálech ponecháme jeden a každý další x
nahradíme ¬y s novou proměnnou y; připojíme Kromovy
klauzule (¬y∨¬x) a (y∨x), které vynucují y=¬x.

Hlavní klauzule je nyní Hornova, všechny přidané jsou Kromovy.
Na původní klauzuli přibudou nejvýše dvě proměnné a čtyři
klauzule; celá transformace má lineární velikost a každé původní
přiřazení má právě odpovídající rozšíření. Kratší klauzule,
opakované literály i společné původní proměnné mezi klauzulemi
tuto ekvivalenci nemění.

Se známou přesnou 3SAT úplností P0632 to dokazuje NP-těžkost
smíšené třídy. Ověření celého přiřazení je lineární v délce,
takže smíšená splnitelnost je NP-úplná. „Probably not“ je proto
správné pod běžnou neprokázanou hypotézou P≠NP; výsledek
netvrdí nepodmíněnou neexistenci polynomiálního algoritmu.
Samostatné lineární algoritmy pro čistě Hornovy/Kromovy formule
neřeší tento smíšený případ a zůstávají předmětem dalšího bloku.

## Errata, stránkové meze a pokračování

Prohledány all4a-pre, all4a, err4a, all4f0 a err4f0 podle
stran i čísel odpovědí/pojmů. Jediná související změna je známý
dodatek k41; F0 odpověď43 na p141 opravuje jiný grafový údaj.
Citace Cook–Reckhow 1979 a Haken 1985, jejich konkrétní výsledky
a historická priorita nejsou zde nezávisle ověřeny ani potřebné
pro konstrukce; jde o výslovnou bibliografickou výjimku.

P542 má nyní argumenty pro pokračování37,38, již hotovou39
a všechny40–43. P0713 však výslovně neuzavírá konvenci prázdné
Hamiltonovy cesty; stránku proto bezvýhradně nepovyšujeme.
P85 má ještě úlohy44–47. P57 byla použita jen definice Horn/Krom,
její věta H a lineární meze čekají na samostatné doložení.
Není nový nález ani kandidát. Další blok: text p57 a úloha44,
potom algoritmy a zbývající Hornovy úlohy.
