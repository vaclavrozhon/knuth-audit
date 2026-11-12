# §1.1-9: simulace výpočetních metod

Kontrola 1. listopadu 2026, V1-X0022, V1-X0023 a V1-C0001.
Výpočetní metoda C=(Q,I,Omega,f) má množinu stavů Q, vstupů I,
koncových stavů Omega a přechodovou funkci f:Q->Q. Koncové stavy
jsou pevné body f. Metoda může na některých vstupech běžet navždy;
její vstupně-výstupní funkce je proto obecně částečná.

## 1. Přesná opravená definice a ukončení

Metoda C2 reprezentuje C1 pomocí funkcí g:I1->I2, h:Q2->Q1
a j:Q2->{1,2,...}. Značka f^[t] znamená t opakování přechodu f.
Po opravách z 1. ledna 2002 a 4. září 2025 jsou podmínky:

```text
(a) h(g(x)) = x                         pro x v I1;
(b) f1(h(q)) = h(q'), q'=f2^[j(q)](q)   pro q v Q2;
(c) h(q') v Omega1 právě když q' v Omega2.
```

V roce 1997 bylo (a) nahrazeno přímým požadavkem shody koncových
výstupů a navíc se požadovalo h(Omega2) podmnožina Omega1.
Oprava 2002 tuto podmínku odstranila, vložila dnešní (a) a požadovala
(c) ve všech stavech q. Oprava 2025 omezuje (c) na cílové stavy q'
vzniklé alespoň jedním blokem simulace. Zdroje: `all1-prepre`, s. 30,
a `all1`, s. 11; obě sazby byly zobrazeny. Aktuální text potvrzuje
také `sources/err1.textxt`. Tyto změny jsou známá errata V1-X0023.

Pro vstup x definujme q_0=g(x) a q_(k+1)=f2^[j(q_k)](q_k).
Indukcí z (a),(b) dostaneme h(q_k)=f1^[k](x). Časy těchto vzorků
striktně rostou, neboť j je kladné. Jestliže C1 skončí v kroku K>=1,
podmínka (c) pro q_K říká, že také C2 dosáhla koncového stavu.
Pokud už x leží v Omega1, použijeme q_1. Obráceně, jestliže C2
skončí v čase t, některý vzorek q_k s k>=1 leží po t a je koncový,
takže (c) dává ukončení C1. Konečné výstupy odpovídají přes h.
Tento důkaz zahrnuje i překryv vstupů s koncovými stavy.

## 2. Skládání simulací

Nechť navíc C3 reprezentuje C2 pomocí g',h',j'. Pro stav q v Q3
položme q_0=q a q_(k+1)=f3^[j'(q_k)](q_k). Pak h'(q_k)
je k-tý stav C2 počínaje h'(q). Použijeme-li

```text
g'' = g' o g,   h'' = h o h',
j''(q) = sum_(0<=k<j(h'(q))) j'(q_k),
```

dostaneme po j''(q) krocích C3 přesně stav, který se přes h' zobrazí
na j(h'(q)) kroků C2. Podmínka (b) pro C2->C1 pak dává (b) pro
složení. Podmínka (a) se skládá přímo. Poslední vzorek je cílem
alespoň jednoho bloku C3->C2; obě podmínky (c) proto lze použít
postupně, což dokazuje (c) složení i ve verzi 2025.

Reprezentace je tedy tranzitivní. Je reflexivní pomocí identit a j=1.
Je-li j<=J a j'<=J', pak j''<=JJ', takže tranzitivní je také přímá
reprezentace, definovaná v knize omezeností j. Symetrie se nepožaduje.
Ekvivalence generovaná relací je nejmenší reflexivní, symetrická
a tranzitivní relace, která ji obsahuje. Nezaměňujeme tuto operaci
s tvrzením, že původní relace sama už je ekvivalencí.

## 3. Příklad uchovávající původní vstup

Knižní metoda C2 uchovává původní m,n ve všech stavech a k nim
přidává pracovní hodnoty a,b, případně zbytek r a číslo fáze.
Její koncový stav (m,n,d) se zobrazuje přes h na koncový stav (d)
Euclidovy metody C1. Vstupní dvojice a jejich g,h jsou totožné.

Ve fázi 1 se pracovní stav mapuje na (a,b,0,1), ve fázi 2 na
(a,b,r,2) a ve fázi 3 na (a,b,r,3). Fáze 3 a 4 mají j=2,
ostatní j=1. Fáze 4 se přes h mapuje na (a,r,r,1), fáze 5 na
(a,b,b,1). Přímé dosazení do přechodů dává (b) v každé fázi:
zejména dva kroky z fáze 3 provedou přesun (a,b)->(b,r), zatímco
dva kroky z fáze 4 již provedou další dělení a mod r. Koncové
stavy a jejich obrazy jsou přesně odpovídající jednosložkové výstupy,
takže platí i silnější verze (c) z roku 2002.

Obory pomocných hodnot bereme tak, aby všechny uvedené přechody
byly definované: m,n,a,b>0, r>=0 ve fázi 2 a r>0 ve fázích 3,4.
Kniha tyto obory v příkladu implicitně přebírá z výpočtu gcd.
Kontrola `check_algorithms.py` ověřila 59 552 různých dosažených
stavů pro 1<=m,n<=64 a dalších 1728 fázových rovnic mimo tyto stopy.
Obecný důkaz je dosazení popsané výše, nikoli konečný výčet.

Jedna stavová funkce v opačném směru Q1->Q2 nevystihuje tuto
simulaci: dvě různé původní dvojice mohou v C1 dospět k témuž
stavu, zatímco C2 je stále rozlišuje původním m,n. Knižní motivace
pro dekódování h je proto správná.

## 4. Protipříklad k závěrečné poznámce o izomorfismu

Izomorfismem vstupně-výstupních funkcí zde rozumíme přejmenování
vstupů a výstupů pomocí bijekcí, které zachová funkční hodnoty
i množinu vstupů, na nichž výpočet skončí. To je obvyklý význam
izomorfismu funkcí; kniha zvláštní slabší význam nedefinuje.

Stačí dvě konečné metody:

```text
C1: I1={x},       Omega1={y},       Q1=I1 union Omega1,
    f1(x)=y, f1(y)=y.
C2: I2={x0,x1},   Omega2={y0,y1},   Q2=I2 union Omega2,
    f2(xi)=yi, f2(yi)=yi, i=0,1.

g(x)=x0;
h(x0)=h(x1)=x, h(y0)=h(y1)=y;
j(q)=1 pro všechny q.
```

Podmínka (a) je h(x0)=x. Pro vstup q=xi mají obě strany (b)
hodnotu y a pro koncový q=yi také y. Koncové stavy se mapují
přesně na koncové stavy, takže platí obě podoby (c), 2002 i 2025.
Také původní podmínka výstupu z roku 1997 je splněna. Obě metody
mají disjunktní vstupy a výstupy a vždy skončí po jediném kroku.

C2 tedy dokonce přímo reprezentuje C1. Každá ekvivalence generovaná
kteroukoli z těchto relací je spojí. Jejich vypočtené funkce však
nejsou izomorfní: mezi jedním a dvěma vstupy neexistuje bijekce.
Závěrečná spekulace na s. 467 o charakterizaci izomorfních funkcí
je při obvyklém významu slova nesprávná. Slovo „apparently“ v knize
značí předběžné tvrzení; neprezentujeme je jako formální větu.

**V1-C0001 je potvrzeno v dostupných zdrojích, ale není to nový objev.**
Stejnou konečnou konstrukci zveřejnil Reepca 16. října 2019 v
[diskusi k tomuto cvičení](https://cs.stackexchange.com/questions/115874/is-represents-a-symmetric-relation-in-the-provided-answer-to-taocp-exercise-1).
Jeho vlastní odpověď správně opravuje původní záměnu symetrie;
následný komentář upozorňuje na zhroucení generované ekvivalence.
Tento zdroj používáme pro původ konstrukce, ne místo vlastního důkazu.
Metadata jsou v `sources/simulation-prior-discussion.json`.

V prohledaných třech časových řadách errat a aktuálním `err1`
jsme nenašli změnu této závěrečné poznámky. Opravy 2002 a 2025
protipříklad neodstraňují. Nemáme ověřen tištěný exemplář ani
stanovisko autora. Návrh `reports/V1-C0001.txt` se nikam neodesílá.
Záznam neprohlašuje za chybnou definici simulace ani její tranzitivitu.
