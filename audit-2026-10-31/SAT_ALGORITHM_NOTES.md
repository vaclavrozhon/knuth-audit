> **Revize 12. 11. 2026: F025 vyřazena.** Originál už definuje hranu l' -> l; stará kontrola přečetla čárku opačně. Mez vstupního stupně i binární test jsou správné. F026 o nekonzistentní silné komponentě zůstává platná. Podrobnosti: [oprava posouzení](../integration/2026-11-12-novelty-review/notes/vol4b-f025-dismissal.md). Staré pasáže o F025 níže jsou historické a neplatí.

# SAT: blokované klauzule, autarkie a Algorithm R

Kontrola 31. 10. 2026, 7.2.2.2–162–164. Záporné číslo v programech
znamená negovaný literál. Klauzule nemají opakovanou proměnnou ani
tautologii. Prázdná klauzule je dovolena jako okamžitý důkaz nesplnitelnosti.
Autarkie podle str. 228 musí být **konzistentní** množina literálů.

## Algorithm R: co skutečně počítáme

`check_recursive_sat.py` věrně provádí R1–R3 ze str. 330. Zachovává
pořadí klauzulí i literálů; při remíze bere první nejkratší klauzuli.
Neprovádí žádné další předzpracování, ukládání vyřešených podúloh ani
hledání silně souvislých komponent. Autarkie testuje přímo podle definice.
Počítá návštěvy každého ze tří kroků zvlášť.

Správnost rozhodnutí plyne indukcí: jednotková klauzule vynucuje literál;
autarkie dovoluje nastavit své literály a odstranit všechny dotčené
klauzule beze změny splnitelnosti; zbývající případ zkouší obě hodnoty
proměnné. Po neúspěšné první hodnotě zůstává zvolená klauzule zkrácená,
takže návrat do R2 pracuje se skutečnou klauzulí aktuálního F. Každá
větev odstraní alespoň jednu proměnnou. Při s=1 se už nevětví, proto
se s nemůže dostat do nepřípustné nuly v R2.

Číselné T_n,U_n,V_n v odpovědi 163 přirozeně omezují návštěvy R2.
R1 je proveden přesně o jednou více než R2; každé R2 totiž vyvolá
právě jeden vstup do R1, případně v rekurzivním volání. R3 je nejvýše
tolikrát jako R2. Proto stačí mez R2 pro všechny požadované O-odhady.
T_0=0 se tak neplete s jednou závěrečnou návštěvou R1.

## 163 a obecné k≥3 v 164

Když jednoprvkový autarkický test selže, existuje klauzule s opačným
literálem. Při pravé větvi R3 se zkrátí a nezmizí, takže rekurzivní
volání má klauzuli kratší než k. To ospravedlňuje U_(n−1).
Selhání dvouprvkového testu v předchozím R3 zase zanechá svědka, který
se zkrátí při následujícím jednoprvkovém kroku R2. Proto i jednotkový
případ po návratu z R3 pokračuje do U, nikoli jen do obecného T.
Při dvouprvkové autarkii stačí T_(n−2).

Obecné stavy V_(n,s) proto splňují uvedenou rekurenci. Její explicitní
řešení pro k≥3 je od příslušných počátečních indexů

```
V_(n,s) = s + U_(n−1) + ... + U_(n−s),
U_n = V_(n,k−1),
T_n = U_n + U_(n−k) + 1 = 2U_(n−1)+1.
```

Tyto vztahy lze ověřit společnou indukcí v max-rekurencích; členy
s největším s dominují. Pro k=3 dostáváme přesně Fibonacciho vzorce
z odpovědi 163. Pro obecné k posun
`W_n=U_n+(k−1)/(k−2)` převádí rekurenci na součet předchozích k−1
hodnot. Pro kladný kořen λ rovnice `λ^(k−1)=Σ_(j=0)^(k−2) λ^j`
volba horní a dolní konstanty podle počátečních hodnot a indukce
dává W_n=Θ(λ^n). U k=4 jde o uvedený tribonacciovský kořen.

Přesné řešení rekurencí je ověřeno pro k=3,...,8 a n≤60, celkem
1481 porovnání vzorců. Nezávislý úplný výčet pravdivostních ohodnocení
kontroluje výsledek algoritmu na všech 8 formulích jedné proměnné,
všech 512 formulích dvou proměnných a všech 20 854 formulích tří
proměnných s nejvýše čtyřmi různými klauzulemi. Navíc 2000 náhodných
instancí 3SAT až 6SAT na nejvýše devíti proměnných. Při skutečném
běhu jsou kontrolovány příslušné meze v 45 200 stavech R1 a 484
návratech do R2 z R3. Bez rozporu pro k≥3.

## F024: Algorithm R nemá lineární mez pro 2SAT

První věta odpovědi 164 na str. 579 uvádí pro k<3 mez T_n=n.
Pro samotný Algorithm R je to nesprávně i asymptoticky.

Vezměme m disjunktních trojic proměnných (a_i,b_i,c_i) a klauzule

`(¬a_i∨b_i), (¬b_i∨c_i), (¬c_i∨a_i)`

v tomto pořadí. Za nimi přidejme na dalších proměnných x,y nesplnitelné
jádro `(x∨y),(x∨¬y),(¬x∨y),(¬x∨¬y)`. Všechny klauzule jsou binární,
žádný literál není čistý. Celkem n=3m+2 proměnných a 3m+4 klauzulí.
V R1 vždy zvolme první nejkratší klauzuli v zachovaném pořadí, v ní
literály v napsaném pořadí; to jsou dovolené volby algoritmu.

Na první trojici ani {b_i}, ani {¬b_i,¬a_i} není autarkie. Algoritmus
se větví na b_i. V pravé větvi jednotkové klauzule postupně nastaví
c_i a a_i, pak se řeší zbytek F_(m−1). Ten je nesplnitelný.
Po návratu do levé větve se obdobně nastaví ¬a_i a ¬c_i a znovu
se řeší úplně stejný zbytek. Pět místních návštěv R2 je jedna pro
větvení a dvě jednotkové návštěvy v každé větvi. Tedy

`C_0=3`, `C_m=5+2C_(m−1)`, a proto **`C_m=8·2^m−5`**.

Další počty jsou `R1=8·2^m−4`, `R3=2^(m+1)−1`. Například n=5
má 11 návštěv R2, n=20 má 507 a n=32 má 8187. Přímý běh ověřil
m=0,...,10. Nesplnitelnost všech členů je zřejmá už z pevného jádra;
u malých členů ji navíc ověřil nezávislý pravdivostní výčet.

Jde o dolní mez Ω(2^(n/3)), která vyvrací libovolnou lineární mez,
nikoli jen přesný koeficient n. Tento příklad nepopírá existenci
jiných efektivních algoritmů pro 2SAT a neporušuje Fibonacciho horní
mez pro 3SAT. Vyvrací jen větu o **konkrétním postupu R**.
Jednoduchá oprava může vyjmout k=2 z uvedené lineární věty nebo výslovně
přidat samostatný 2SAT postup; pouhá změna konstanty nestačí.

## Blokovací graf v odpovědi 162

Značme l↪a, jestliže každá klauzule obsahující ¬l obsahuje také a.
Testy vylučují dvojice stejné proměnné, takže nenabízejí triviální
hranu l↪¬l. Následující protipříklady nemají čisté literály a platí
i při tomto vstřícném výkladu definice grafu.

### F025: orientace grafu nesouhlasí s dvěma dalšími tvrzeními

Vyberme libovolnou klauzuli obsahující ¬l. Všechny výstupní sousedy l
musí obsahovat i tato klauzule, a je jich proto nejvýše k−1.
To omezuje **výstupní** stupeň, zatímco odpověď uvádí vstupní.

Příklad s k=2:
`(¬x∨a),(x∨a),(¬a∨b),(¬b∨a)`.
Hrany x↪a, ¬x↪a a b↪a dávají vstupní stupeň a rovný třem, nikoli
menší než dva. Přidáváním dalších x lze tento vstupní stupeň zvětšovat.

### F026: silně souvislá komponenta nemusí být konzistentní

Pro `F=(a∨¬b∨c) ∧ (¬a∨b∨¬c)` obsahuje blokovací graf cyklus

`a↪b↪c↪¬a↪¬b↪¬c↪a`.

Jeho jediná komponenta obsahuje všech šest literálů. Nemůže být
autarkií, protože obsahuje proměnnou současně s její negací.
Kniha však v odpovědi 162(b) tvrdí, že každá netriviální silně
souvislá komponenta je autarkií. Chybí podmínka konzistence.

Po jejím doplnění důkaz funguje: každý literál a v netriviální
komponentě má následníka b ve stejné komponentě. Každá klauzule s ¬a
pak obsahuje b, takže je komponentou splněna. Správná charakterizace
dvouprvkových autarkií jako vzájemných hran zůstává platná pro literály
na různých proměnných.

### Druhý důsledek F025: test blokované binární klauzule

Pro přidávanou klauzuli `(l∨l')` tisk v 162(a) uvádí podmínku
`¬l↪l' nebo ¬l'↪l`. Správně je **`l↪¬l' nebo l'↪¬l`**.
Při rezoluci na l vznikne tautologie právě tehdy, když každá
klauzule s ¬l obsahuje ¬l'; pro druhý pivot symetricky.

Nesprávný test může změnit splnitelnost. Vezměme

```
(x∨y∨z)
(¬x∨z)   (¬x∨¬z)
(¬y∨z)   (¬y∨¬z)
```

Formula má jediné řešení x=y=0,z=1: obě dvojice binárních klauzulí
vynucují ¬x a ¬y, první pak z. Pozitivní x a y jsou jen v první
klauzuli, proto existují hrany ¬x↪y i ¬y↪x. Tisk tedy dovoluje
přidat `(x∨y)`, ale tím se formule stane **nesplnitelnou**.
Příklad nemá jednotkové klauzule, čisté literály ani tautologie.

Oba projevy F025 mají společnou jednoduchou opravu: **obrátit šipku
v první definici blokovacího grafu**. Tím zůstanou tvrzení o vstupním
stupni i vytištěný test binární klauzule správně. Druhou možností je
ponechat definici a opravit obě použití, jak je uvedeno výše. Vzájemné
hrany i silně souvislé komponenty se při obrácení všech hran nezmění;
F026 je tedy další, samostatná chybějící podmínka. Stupeň a binární
test počítáme dohromady jako jeden nález F025.

## Rozsah nezávislé kontroly grafu

`check_blocking_graph.py` prošel všech 21 118 formulí s nejvýše
čtyřmi různými klauzulemi na nejvýše třech proměnných. Správné
kritérium porovnal s explicitní tvorbou rezolvent v **251 272**
případech; stejně tolik přímých testů provedl pro dvouprvkové autarkie.
Zkontroloval 101 640 výstupních stupňů nečistých literálů a 9884
konzistentních netriviálních komponent. Všechny opravené výroky souhlasí.
Počty rozporů tisku v JSON nejsou další samostatné nálezy.

## Provenance a omezení

F024–F026 jsou viditelné v hlavním PDF na str. 579 a v Knuthově
autorském [Pre-Fascicle 6A z 23. 9. 2015](https://www-cs-faculty.stanford.edu/~knuth/fasc6a.ps.gz),
str. 215. Draft byl dodatečně stažen, hash a čas jsou v
`sources/fasc6a-manifest.json`; původní PS je zachován a je převeden i do PDF.
Úplná errata 4B a historického Fascicle 6 neobsahují odpovídající opravy.
Fyzický výtisk dosud neověřen. Nic nebylo odesláno.

Doklady: `results/recursive_sat.json`, `results/blocking_graph.json`,
`images/vol4b-p330.png`, `images/vol4b-p579.png`, `images/fasc6a-p215.png`.
