# V4A-F0002: chybějící „induced“ u průměru podgrafů kografu

Potvrzeno v doloženém prvním dotisku 6. listopadu 2026. Závažnost nízká:
nepravdivé obecné tvrzení v závorce; klasifikace v úloze 90 zůstává správná.

## Přesné místo a sazba

Svazek 4A, §7–90, odpověď na tištěné str. 526 / file543, třetí řádek
odpovědi: tvrzení, že všechny souvislé podgrafy kografu mají průměr ≤2.
Původní sazba images/proof-file543.png výslovně nemá slovo „induced“.
Definice na str. 13 / file030 rozlišuje subgraph od induced subgraph:
obecný podgraf může mít libovolnou podmnožinu hran.

Zadání na str. 42 / file059 správně definuje kografy pomocí jednovrcholových
grafů, disjunktního sjednocení a komplementace; vlastní zadání není chybné.

## Protipříklad

G=K4 je kograf: G je komplement disjunktního sjednocení čtyř K1.
Vezměme na stejných vrcholech {1,2,3,4} podgraf H s hranami
{1,2}, {2,3}, {3,4}. Podle definice knihy je H souvislý (dokonce spanning)
podgraf G. Vzdálenost mezi 1 a 4 je přesně 3, takže diam(H)=3>2.
Nejde o malý degenerační případ ani o odlišnou definici průměru.

Stačí doplnit „induced“: indukované podgrafy kografů jsou kografy
(indukce podle konstrukce, restrikce komutuje s komplementem i sumou).
Každý souvislý kograf s alespoň dvěma vrcholy je netriviální join:
komplementy lze pomocí De Morganových vztahů přesunout k listům
konstrukčního stromu a souvislý kořen nemůže být disjunktní sjednocení.
Dva vrcholy v různých částech jsou sousední; dva ve stejné části mají
společného souseda v jiné části. Proto má průměr nejvýše 2.
To postačuje i k platnému závěru, že P4 není kograf.

## Vyloučení známých errat

Prohledány všechny relevantní lokálně uložené historické/aktuální vrstvy:
errata/text/all4a-pre.txt, all4a.txt, err4a.txt, all4f0.txt, err4f0.txt.
Hledání podle 526, answer 90, cograph/ograph, subgraph, induced/indu ed,
diameter i odpovědního offsetu F0 146 (=526−380).

all4a-pre má na této odpovědi známou opravu odkazu (47)→(39), 23. 5. 2011,
a změnu označení kol W5/W6→W4/W5, 23. 12. 2015. Ani jedna nedoplňuje
„induced“. Obě opravy jsou aplikovány a protipříklad stále platí.
F0 má jiné opravy „subgraph→induced subgraph“ u úloh 79/80 na str. 90
a odpovědi 81 na str. 168; týkají se jiného oddílu, nikoli §7–90.
Žádná odpovídající oprava této věty nebyla nalezena.

Pouze str. 526 / file543 je nová chybová lokace. Definice na str. 13
a zadání na str. 42 slouží jako správné podklady. Tištěný exemplář
nebyl nezávisle porovnán; prvenství nálezu se netvrdí.
