# §7.1.1 p54–55 a úlohy18–21: prvoimplikanty, přesná minima a monotónnost

6. listopadu 2026, X0065. Originály images/file071.png, file072.png,
file098.png, proof-file553.png a proof-file554.png; návaznost na konec
p53/file70. Bez programu, enumerace formulí nebo rerunu starých důkazů.

## P0597: doména literálů a geometrický význam

Používáme normalizované termy: opakované literály odstraníme a rozporné
termy obsahující x i ¬x vynecháme z DNF. Klauzule jsou analogicky
bez duplicit a bez tautologické dvojice x,¬x. Prázdný term je1,
prázdná klauzule0. Konzistentní term je neprázdná podkrychle,
s pevnými souřadnicemi jeho literálů a hvězdičkami jinde.
Je implikantem f právě když celá tato krychle leží v množině f=1.
Smazání literálu znamená uvolnění souřadnice. Prvoimplikant je
proto přesně inkluzně maximální obsažená podkrychle; nejde o
globálně největší dimenzi. Duálně je klauzule implikovaná f právě
když její neprázdná nulová podkrychle leží v f=0; primární klauzule
odpovídá maximální takové krychli.

Tato doména je nutná zejména v úloze18. Odpovídá výslovnému
krychlovému výkladu p54/úlohy30 a větě p55 „splnitelná právě když
má implikant“. Pro syrovou nenormalizovanou syntaxi by závěr18
neplatil: v DNF x∨(y∧¬y) a CNF x nemá rozporný člen y∧¬y
společný literál s klauzulí x. Takový člen není podkrychlovým
implikantem zde používaného významu. Tento rozdíl domény není
nový nález a není skryt v důkazu přiřazením hodnot.

## P0598: celý tříproměnný příklad a (27)

Původní funkce konce p53 má pravdivé body
010,011,101,111. První člen x∧¬y∧z lze rozšířit na x∧z:
nově přidaný111 již pokrývá y∧z. Poslední ¬x∧y∧¬z lze rozšířit
na ¬x∧y: přidaný011 také pokrývá y∧z. Dostáváme přesně (27).

Indukovaný graf krychle na těchto bodech je cesta
010—011—111—101. Jediné maximální podkrychle jsou proto její
tři hrany, tj. ¬x∧y, y∧z, x∧z; čtverec neexistuje.
Každá je prime také přímým testem smazání literálu:
z má zakázaný bod001, x má100, y má110 a ¬x má000.
To pokrývá všechny jednotlivé neúspěšné redukce tří členů,
včetně všech čtyř literálů jmenovaných v textu.

## P0599: úplný seznam (29) a všechny členy (30)

Pravdivé body příkladu (22) jsou již přesně ověřeny v P0535.
Všechna jejich spojení lišící se jedním bitem jsou

    0000—0001, 0000—0100, 0100—1100, 0111—1111,
    1100—1101, 1101—1111, 1111—1110, 1110—1100.

Úplnost lze číst po jednotlivých vrcholech: např.0001 má jediného
souseda0000, 0100 má0000/1100, 0111 jen1111; zbylé čtyři body
tvoří uvedený čtverec, s již uvedenými připojeními.
První čtyři hrany jsou mosty. Jediný čtyřcyklus je tedy11**.
Každá alespoň dvourozměrná podkrychle obsahuje čtverec; vyšší
dimenzí by přibyly další čtverce, které v seznamu nejsou.
Maximální podkrychle jsou právě

    A=000*, B=0*00, C=*100, D=*111, E=11**.

Každý vrchol leží na některé hraně, proto žádný původní minterm
není prime. Překlad pevných bitů do literálů dává všech pět členů
(30): ¬w¬x¬y, ¬w¬y¬z, x¬y¬z, xyz, wx.
Známá oprava „are the terms of“ před(30) je zohledněna.

## P0600: obě tvrzení o redundanci na p55 a jejich přesná minima

V (27) je y∧z pokryto x∧z nebo ¬x∧y podle hodnoty x.
Zbývající dvě hrany jsou nutné: bod101 patří jen prvnímu prime,
bod010 jen druhému. DNF tedy potřebuje alespoň2 členy a4 literály;
obou mezí dosáhne (x∧z)∨(¬x∧y).

U A–E mají soukromé body A:0001, D:0111, E:1101.
Tyto tři prvoimplikanty jsou nutné; ještě zbývá0100, které
pokrývá B nebo C. Oba tyto členy současně potřeba nejsou.
Minimum je4 členy a11 literálů: A,D,E a jeden z B,C.

Dolní meze nejsou omezené na již prime DNF. Každý konzistentní
implikant lze rozšířit do maximální podkrychle, aniž přibyde člen
nebo literál. Pokud nějaký term pokrývá soukromý bod, jeho
maximální rozšíření musí být příslušný jediný prime. U prvního
příkladu jsou proto nutné dva různé členy velikosti≥2, u druhého
alespoň členy velikosti≥3,3,2,3. To ospravedlňuje obě minima.

## P0601: obecná úplnost obou prime forem

Každý pravdivý bod je mintermová krychle a konečným uvolňováním
souřadnic ji lze rozšířit do maximální krychle uvnitř f=1.
Disjunkce všech prvoimplikantů proto pokrývá přesně f.
Duálně každý nulový bod leží v maximální nulové krychli,
takže konjunkce všech primárních klauzulí je přesně f.
Pro konstantu0 je rodina implikantů prázdná a prime CNF jediná
prázdná klauzule; pro konstantu1 jsou role obrácené.
Výklad tedy pokrývá i prázdné rodiny a nulární funkce.

## P0602–P0603: celá úloha18 a čtyři ekvivalentní podmínky

**P0602:** pro konzistentní term T a netautologickou klauzuli C
platí T⇒C právě když mají stejný literál. Společný literál
implikaci dokazuje okamžitě. Není-li společný, lze všechny
literály T nastavit na1 a všechny literály C na0: konflikt uvnitř
jedné rodiny vylučuje normalizace a konflikt mezi nimi by byl
právě společný literál. Ostatní souřadnice jsou libovolné.
Vznikl by T=1,C=0. Pokud T patří DNF pro f a C CNF pro f,
vyšlo by současně f=1 a f=0, spor. To je požadovaný závěr.

**P0603:** každá normalizovaná DNF pro f je OR svých termů,
takže f⇒C právě když každý její term implikuje C, tedy má s C
literál společný. Totéž platí pro prime DNF z P0601.
Pokud f⇒C, tuto vlastnost má každý implikant f. Obráceně
stačí všechny mintermy skutečných modelů, které jsou mezi
implikanty. Tím jsou dokázány všechny čtyři ekvivalence dodatku:
C je implikována f; má společný literál s každým implikantem;
s každým prime implikantem; s každým členem libovolné zvolené
DNF pro f. Doména z P0597 platí v každém kroku.

## P0604–P0605: úloha19, všechny prime klauzule i optimum

**P0604:** nulové body (22) jsou
a=0010, b=0011, c=0110, d=1000, e=1001, f=1010, g=1011,
h=0101. Úplný seznam jejich hran je

    ab, ac, af, bg, de, df, eg, fg.

h je izolovaný a ac je koncová hrana. Zbytek jsou dva čtverce
abgf a degf sdílející fg. Další čtyřcyklus není: cesta z f do g
mimo fg vede buď přes a,b, nebo přes d,e; spojení obou má délku6.
Vyšší podkrychle chybí. Maximální nulové krychle jsou proto právě

    0*10, 0101, *01*, 10**.

**P0605:** negací jejich pevných literálů dostáváme přesně odpověď

    (w∨¬y∨z) ∧ (w∨¬x∨y∨¬z) ∧ (x∨¬y) ∧ (¬w∨x).

Každá klauzule má soukromý nulový svědek:
0110,0101,0011,1000 v uvedeném pořadí. Žádná se nedá vypustit.
Navíc jakoukoli netautologickou klauzuli lze zesílit na prime
rozšířením její nulové krychle. Klauzule pokrývající některý
soukromý svědek musí rozšířením dojít právě k danému prime;
jeden člen nemůže pokrýt dva různé soukromé svědky.
Proto každé CNF potřebuje alespoň4 klauzule a nejméně
3+4+2+2=11 literálů. Vytištěná forma obou mezí dosahuje.
Její „shortest“ tedy není vyvozeno pouze z neodstranitelnosti.

## P0606: úloha20, průnik dvou prime krychlí

Nechť C je maximální krychle uvnitř f=1 a g=1 současně.
Rozšiř ji nezávisle do maximální F⊆{f=1} a G⊆{g=1}.
Protože obě obsahují neprázdnou C, nemají konfliktní pevné bity;
jejich průnik je podkrychle a obsahuje C. Leží zároveň v f∧g.
Z maximality C je F∩G=C, tedy odpovídající term je součinem
prime implikantu f a prime implikantu g (duplicity literálů se odstraní).
Pro nulovou funkci nejsou prime implikanty a tvrzení je prázdné;
konstantní jednička má plnou krychli. Opačný směr, že každý
takový průnik je prime, se netvrdí.

## P0607–P0608: monotónnost a celá úloha21

**P0607:** pokud funkce nikdy neklesne při změně jedné souřadnice
0→1, pak pro x≤y změň rozdílné souřadnice jednu po druhé.
Každý krok neklesá, tedy f(x)≤f(y). Obráceně je jednotlivý
krok zvláštním případem souřadnicového uspořádání. Tím je
ekvivalence definic na p55 úplná.

**P0608:** cofactory g=f(·,0),h=f(·,1) monotónní f jsou
monotónní a g≤h. Obráceně tyto tři podmínky implikují
monotónnost f, uvnitř obou vrstev i mezi nimi.
Booleův rozklad se proto zjednoduší na
f=(g∧¬xₙ)∨(h∧xₙ)=g∨(h∧xₙ).
Indukcí od nulárních konstant vznikne výraz jen z ∧,∨ a
konstant. Konstanty lze postupně odstranit identitami
u∧0=0,u∧1=u,u∨0=u,u∨1=1. U nekonstantní výsledné funkce
nemůže zůstat konstantní kořen, takže se obejdeme úplně bez nich.
Naopak proměnné, AND a OR zachovávají souřadnicové uspořádání,
tedy i každý takový složený výraz je monotónní.
To dokazuje oba směry zadání a všechny matematické kroky odpovědi.

## P0609–P0611: Theorem Q a Corollary Q

**P0609:** obsahuje-li prime implikant monotónní f literál ¬x_j,
smaž jej. Pro každý nový bod s x_j=1 změň tento bit na0;
vznikne starý bod termu, kde f=1, a monotónnost vrátí f=1
i na novém bodu. Smazání tedy stále dává implikant, spor.
Každý prime je proto kladný.

**P0610:** ztotožni kladný term s množinou svých proměnných S.
Při vstupu1_S je pravdivý. Jiný prime s proměnnými R by tam
mohl být pravdivý jen při R⊆S; přísná inkluze by odporovala
primalitě S a rovnost by nebyla jiným prime. Každý prime má
proto svůj soukromý pravdivý bod. Každou DNF lze rozšířit
do prime DNF bez zvýšení počtu členů nebo literálů; soukromé
body vynucují všechny primes. Disjunktivní prime forma je tedy
minimální. Při minimalizaci celkové délky/literálů lze neprime
člen skutečně zkrátit, jak uvádí kniha. Samotné minimum počtu
členů nemusí dát jedinečný syntaktický výraz, ale stejná prime
forma toto minimum také dosahuje. Konstantní případy řeší P0601.

**P0611:** nutnost kladnosti a neobsaženosti různých prime termů
plyne z předchozího. Pro opačný směr vezmi kladnou DNF tvořící
antichain množin proměnných. Je monotónní. Kdyby některý term S
šel zkrátit na S', vstup1_S' by splnil nějaký term R⊆S'⊊S,
spor s antichainem. Každý původní term je tedy prime.
Každý další prime R při1_R musí obsahovat některý původní term
S⊆R, takže primalita vynutí S=R. Seznam je úplný, nikoli jen
množina několika primes. Prázdná rodina/term pokrývají0/1.

## P0612: celý unate dodatek odpovědi21

Překlopení pevně zvolené množiny souřadnic je bijekce krychle.
Převádí konzistentní termy i jejich inkluze, počet literálů,
prime krychle a soukromé svědky oběma směry. Je-li po takovém
překlopení f monotónní, přenese se argument P0609–P0610 zpět;
disjunktivní prime forma je nejkratší také pro unate funkci.
Vytištěný příklad ¬x∨y se překlopením x změní na x∨y.
Terminologické a historické poznámky o „isotone“ nejsou důkazem
nějaké další matematické vlastnosti.

## P0613–P0616: satisfiabilita a přesné meze složitostních vstupů

**P0613:** nenulová booleovská funkce má pravdivý bod, tedy jeho
minterm a po rozšíření prime implikant. Každý konzistentní
implikant má nějaký bod, na kterém je f=1. Proto je „nenulová“
ekvivalentní „má implikant“ v použité doméně. To rovněž vysvětluje,
proč nelze v úloze18 přidávat rozporné termy jako implikanty.

**P0614, external_input:** SAT pro formule je NP-úplný. Přesný
použitý externí vstup je uveden v primárním Cookově
[oficiálním popisu problému pro Clay, p5](https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf),
uloženém v sources/cook-clay-pvsnp.pdf s metadaty.
Definice redukcí na p4 a formulové SAT na p5 byly přečteny.
Celý Cookův/Levinův simulační důkaz se zde nezrekonstruovává.

**P0615:** otázka z p55 se týká jednoho algoritmu a pevného
polynomiálního exponentu v délce vstupní formule N, nikoli
exponentu měnícího se s instancí. SAT je v NP, neboť přiřazení
lze ověřit vyhodnocením formule. S P0614 odpovídá polynomiální
řešení otázce P=NP. Aktuální [oficiální stránka Clay](https://www.claymath.org/millennium/p-vs-np/)
ji při kontrole6.11.2026 stále uvádí jako nevyřešenou;
metadata v sources/clay-pvsnp-status.json. Nejde o tvrzení,
že byla prokázána neexistence polynomiálního algoritmu.

**P0616, partial:** pro vstup zadaný libovolnou formulí by
polynomiální algoritmus vracející nejkratší ekvivalentní DNF
rozhodoval SAT: hotovou DNF stačí projít a zjistit, zda obsahuje
nějaký konzistentní term. Tento test je polynomiální ve výstupu;
polynomiální algoritmus musí mít také polynomiální délku výstupu.
Spolu s P0614 tak máme explicitní polynomiální Turingovu redukci.
Knižní věta o NP-hardness ale na této stránce nefixuje reprezentaci
vstupu. Obtížnost při vstupu úplnou pravdivostní tabulkou nebo už
DNF není touto redukcí dokázána; tato širší otázka zůstává partial.
Nezaměňuji ji s doloženým elementárním Theorem Q.

## P0617: odkaz na algoritmus úlohy30 zůstává samostatný

Na p54 je výslovný odkaz na algoritmus úplného hledání primes
v úloze30. Zadání na p82 obsahuje uvedené krychle/buddies/tagy.
Jeho přesné invarianty, úplnost a opravené náklady v odpovědi
nebyly v tomto bloku auditovány a patří do samostatné fronty.
P0617 je partial; existence uvedených konkrétních prime seznamů
nenahrazuje důkaz tohoto obecného algoritmu.

## Stránkové pokrytí, bibliografie a pokračování

P53/file70 nyní může mít argumentové pokrytí: P0536–P0539
dokládají všechny CNF/DNF vzorce a počáteční implikant, tento
soubor dokončuje jeho pokračování a související18–21; úlohy16–17
jsou v proof-034. Historická prevalence/cena PLA a Peirce/Bernays
jsou oddělené bibliografické výjimky.
P54 zůstává partial kvůli P0617, p55 kvůli přesné reprezentaci
v tvrzení P0616. Jejich zbývající matematický obsah má argumenty.
P536 má všechny odpovědi12(b)–21, ale P0580 nulární mez stále
zůstává explicitní partial. P537 má zatím pouze konec21.
Historické Quine/McCluskey/Fiser/Hlavicka/Samson–Mills odkazy
a terminologie zůstávají výslovně neověřené; známá oprava před
(30) je zohledněna a není nálezem.

Další jednotlivé úlohy22–25. Hlavní text pokračuje p56/file73;
čtecí náskokp218 se nepřepisuje. Žádný nový nález ani kandidát,
žádný matematický program.
