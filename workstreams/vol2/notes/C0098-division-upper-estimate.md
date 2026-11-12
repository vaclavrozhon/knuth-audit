# V2-C0098: implicitní horní odhad v §4.3.1-20/21

**Candidate, interpretační otázka.** Doslovný protipříklad je přesný;
nejisté je, zda má být předpoklad převzat z předchozího kontextu D.
Originály271,282,625 a erratum pro282 z3.2.2005 vizuálně přečteny.

Úloha19 zavádí qhat jako „an approximation to q“ a20 odkazuje na její
značení a předpoklady. Podmínka2005 qhat<b nevylučuje odhad zdola.
Pro b10,n2,u100,v50,qhat1 dostaneme pravý podíl q2 a zbytek0.
Pomocný rhat=(1*10+0)-1*5=5. Druhý test je `1*0<=10*5+0`, tedy platí.
Závěr20 q=qhat nebo qhat-1 je nepravdivý. Splněny jsou i podmínky21:
vedoucí číslice v je5>=floor(b/2), qhat!=q, ale0 není alespoň40.

Obecný důkaz20 z daného testu poskytuje pouze q>=qhat-1. K závěru je
potřeba q<=qhat. Také důkaz21 používá qhat>=q+1. Obě tvrzení jsou tedy
správná pro **horní odhady**, které algoritmus D skutečně používá;
žádná chyba výsledků D z tohoto pozorování neplyne.

Kontextová rovnice(2) na271 a větaA zaručují horní odhad, což je důvod
nepotvrzovat nyní novou chybu. Naopak formulace úlohy19 „let ... be an
approximation“ a přidání qhat<b v2005 podporují širší doslovné čtení:
pro samotnou definici(2) už je tato přidaná podmínka automatická.
Vhodné redakční zpřesnění je q<=qhat<b v20 a převzetí do21.

Všechny čtyři vrstvy errat prohledány2.11.2026; žádné další doplnění
horního odhadu nalezeno nebylo. Přesný svědek je v
[classical-division-exercises.json](../results/classical-division-exercises.json),
obecné důkazy v [poznámce](classical-division-exercises.md).
Poslední fyzický dotisk ani autorský záměr nejsou ověřeny; neodesláno.
