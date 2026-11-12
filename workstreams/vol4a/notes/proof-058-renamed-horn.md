# Úloha 7.1.1–55: přejmenování na Hornovy klauzule

Checkpoint X0087, P0813–P0820. Zadání p87/file104, odpověď
p544–545/file561–562. Originály file104.png, proof-file561.png
 a nově proof-file562.png. Celý důkaz lineárního rozhodování je
nezávislý na pravdivosti formule. Žádný matematický program.
Přesná jednotka vytištěného koeficientu3 zůstává odděleně partial.

## 55(a): všechna párová omezení a obě implikace — P0813

Pracujeme se standardním normalizovaným CNF tohoto bloku:
v klauzuli se neopakuje proměnná a nejsou v ní obě její polarity.
Unit a prázdná klauzule jsou již Hornovy a nepotřebují žádné omezení.
Normalizace opakovaného x∨x na x odpovídá přímo poznámce p57;
netvrdíme nové tvrzení o libovolném nenormalizovaném syntaktickém zápisu.

Pro výskyt kladného x_i označme Y_i=y_i, pro záporný ¬x_i označme
Y_i=¬y_i. Po substituci x_i⊕y_i je tento literál negativní právě
když Y_i=1. Klauzule je tedy Hornova právě tehdy, když mezi jejími
Y_1,…,Y_k je nejvýše jedna nula. To je ekvivalentní konjunkci
všech klauzulí Y_i∨Y_j pro1≤i<j≤k.

Pro vytištěný x1∨¬x2∨x3∨¬x4 dostáváme přesně

    (y1∨¬y2)(y1∨y3)(y1∨¬y4)
    (¬y2∨y3)(¬y2∨¬y4)(y3∨¬y4).

Každý dvojitě pozitivní pár vytvoří právě nesplněné omezení;
naopak bez takového páru je nejvýše jeden pozitivní literál.
Konjunkce podmínek pro všechny vstupní klauzule tedy splňuje
požadovanou bodovou ekvivalenci pro každé přejmenování y.
Pro klauzuli délky k jsou počty přesně C(k,2); k=0,1 dávají0.
Výsledná funkce g používá jen původní přejmenovací bity, jak žádá(a).

## 55(b): obecný řetězec a jeho invariant — P0814

Pro k≥4 zavede kniha k−3 pomocných t2,…,t_{k−2}.
Pro j=2,…,k−1 přidá tři klauzule

    (¬t_{j−1}∨Y_j), (¬t_{j−1}∨t_j), (Y_j∨t_j),

s hranicemi **¬t1=Y1** a **t_{k−1}=Yk**. První hranice má
negaci: není to dosazení t1=Y1. Počet trojic je k−2.
Pro k=3 stejná hranice dává pouze všechny tři páry, bez pomocné
proměnné; k=2 ponecháme jediný pár, k≤1 nepřidáváme nic.

Nutnost: je-li Y_p=0, pak se v příslušné trojici vynutí t_p=1
(u p=1 přímo z t1=¬Y1). Následující prostřední klauzule
¬t_{j−1}∨t_j přenášejí1 doprava; první klauzule pak vyžadují
Y_j=1 pro každý další j<k. Poslední prostřední klauzule vynutí
i t_{k−1}=Yk=1. Dvě nuly mezi Y proto nemohou mít rozšíření.
Stejná argumentace pokrývá i dvojici posledních dvou pozic,
kterou přímo zakazuje poslední Y_{k−1}∨Yk.

Dostatečnost: je-li mezi Y nejvýše jedna nula, zvolme pro každé
vnitřní j≤k−2 hodnotu

    t_j=1 právě tehdy, když se nula objevila mezi Y1,…,Y_j.

Pokud t_{j−1}=1, potom další Y_j musí být1 a t_j=1;
všechny tři klauzule platí. Pokud t_{j−1}=0, první dvě klauzule
platí automaticky a třetí platí, protože Y_j=0 vynutí t_j=1.
Na poslední hranici: dřívější nula vynutí Y_{k−1}=Yk=1;
bez dřívější nuly nesmí být oba poslední bity nulové. Tedy
všechny poslední tři klauzule také platí. Toto dává explicitní
rozšíření, nikoli jen neprokázanou ekvisplnitelnost.

Pomocné proměnné jednotlivých vstupních klauzulí jsou disjunktní.
Proto lze jejich rozšíření spojit právě tehdy, když jedno společné
y úspěšně přejmenuje všechny původní klauzule. Pokud 2SAT vrátí
model, odhodíme t a získáme skutečný přejmenovací vektor y.

## Přesné počty a lineární algoritmus — P0815

Nechť L je celkový počet vstupních literálů a r počet klauzulí.
Počet přidaných proměnných a binárních klauzulí je přesně

    A=Σ_{k≥4}(k−3),
    C=r_2+Σ_{k≥3}3(k−2),

kde sumy běží přes vstupní klauzule a r_2 je počet dvouliterálových.
Tedy A≤L a C≤3L, přičemž C<3L pro L>0. Celkový počet
výstupních literálů je **2C≤6L**. Vstupní prázdné klauzule
nemění přejmenovatelnost: jsou Hornovy při každém y, i když
samotná formule s nimi není splnitelná.

Při jednom průchodu vznikne konstantní počet klauzulí na vstupní
literál. Použité proměnné jsou indexované jako v předchozím 2SAT
algoritmu; počet skutečně použitých je nejvýše L. Na výstupní
formuli použijeme P0811: graf a SCC mají O(L) vrcholů/hran,
rozhodnutí i svědek přejmenování mají O(L+r) čas a paměť.
To je požadované O(m) pro standardní vstupní délku, která počítá
literály i hranice klauzulí. Pokud rozhraní požaduje navíc explicitní
výstup pro všech n včetně nepoužitých proměnných, cena je O(n+L+r);
nepoužité bity lze jinak implicitně zvolit0. Vázání na běžný
indexovaný vstup není tvrzením o konstantní ceně libovolně dlouhých
řetězcových názvů proměnných.

Tento algoritmus rozhoduje přejmenovatelnost **daných klauzulí**.
Je odlišný od hledání y, pro které jsou dvě Hornovy funkce F(x)
a G(x⊕y) ekvivalentní v dodatku49. P0747 zůstává otevřena.

## Vytištěné „length <3m“ — P0816, partial pro jednotku délky

Předchozí výpočet prokazuje koeficient3 pro počet **binárních
klauzulí** vzhledem k počtu vstupních literálů. Výstup obsahuje
jejich dvojnásobný počet literálů. Samotný vytištěný pětiliterálový
příklad má9 klauzulí a18 literálů, takže při m=5 není jeho
literálová délka <15. Při měření binárními spojkami má tentýž
vstup4 a výstup17 spojek, nikoli méně než12.

Na p544 se slovo length nepřiřazuje jednoznačně jedné z těchto
veličin; na p59 se výslovně pracovalo s celkovou délkou klauzulí.
Proto zde koeficient3 nevydáváme za ověřenou společnou délkovou
mez a necháváme přesnou konvenci otevřenou. Nejde o nový confirmed
ani candidate záznam: obecné O(m), ekvivalence i skutečné počty
jsou správné a doložené; nejde o chybu rozhodovacího algoritmu.
Stačí-li zamýšlený počet výstupních klauzulí, vytištěný koeficient
je správný. Žádné zvláštní podezření z nulového m se nevytváří.

## Celý pětiproměnný příklad — P0817

Pro samé kladné vstupní literály je Y_i=y_i. Tři trojice jsou

    (y1∨y2), (y1∨t2), (y2∨t2);
    (¬t2∨y3), (¬t2∨t3), (y3∨t3);
    (¬t3∨y4), (¬t3∨y5), (y4∨y5).

To je přesně všech devět klauzulí v originálu; žádná negace
pomocné proměnné nebyla čtena jen z OCR. Obecný důkaz P0814
platí s t2=[některé z y1,y2 je0], t3=[některé z y1,y2,y3 je0].
Případ libovolné záporné vstupní polarity mění pouze odpovídající
Y_i, nikoli řetězový argument.

## Dodatek: každá splnitelná 2CNF má Hornovo přejmenování — P0818

Nechť a je splňující přiřazení původní 2CNF F. Zvolme y=a.
Pak F(x⊕y) je splněna při x=0. Každá její klauzule tedy
obsahuje alespoň jeden negativní literál, a protože má nejvýše
dva různé literály, obsahuje nejvýše jeden pozitivní. Je Hornova.
Unit a tautologie při obvyklé normalizaci také nepůsobí potíž.
To je přímý obecný důkaz uvedeného důsledku; netvrdí se opačná
implikace (nesplnitelná x∧¬x je sama Hornova).

Známá oprava čísla v odkazu na Kleine Büning/Lettmann je5.24→5.2.4.
Přesné znění externí věty se nepřebírá: vlastní důkaz dostačuje.

## Dodatek: stejná funkce, jiná přejmenovatelnost zápisu — P0819

Původní příklad na p545 je

    F=(x∨y∨z)(¬x∨¬y∨¬z)(¬x∨z)(¬y∨z).

Poslední dvě klauzule znamenají x≤z,y≤z. Při z=0 vynutí
x=y=0 a první klauzule selže. Při z=1 jsou první, třetí a čtvrtá
klauzule automatické a druhá je ¬x∨¬y. Proto přesně

    F=z(¬x∨¬y),

což je Hornova CNF. Kdyby však původní zápis měl úspěšné
přejmenování a,b,c, jeho první klauzule by vyžadovala alespoň
dvě jedničky mezi a,b,c. Jeho druhá klauzule by vyžadovala
nejvýše jednu jedničku. Obě podmínky jsou neslučitelné.
K nemožnosti přejmenování daného zápisu stačí jeho první dvě
klauzule; zbývající dvě zajišťují právě Hornovu sémantiku F.

## Známý dodatek: méně pomocných proměnných — P0820

Známé erratum z22.11.2015 odkazuje na §7.2.2.2–12. Přesný již
uzavřený počet přebíráme z audit-2026-10-31/SHADOW_PATHS_NOTES.md,
oddíl „SAT kódování a počty“: pro k≥3 je

    q=floor((k−3)/2), r=k−2q∈{3,4}, C=6q+C(r,2)=3k−6.

Neopakuje se žádný tamní census cest, solver ani benchmark.
Doplňme pro přesnou vazbu zde užitý elementární důvod rekurze.
Pro AMO(z1,…,zk), kde z_i=¬Y_i označuje pozitivní literál,
a k≥5 platí ekvivalence s existencí nového t v

    AMO(z1,z2,z3,t) ∧ AMO(¬t,z4,…,zk).

Pokud některé z prvních tří z je1, první AMO vynutí t=0
 a druhé pak všechny zbývající z=0. Pokud některé z pozdějších
z je1, druhé AMO vynutí t=1 a první pak první tři nuly.
Dvě jedničky na téže straně zakáže její vlastní AMO. Naopak
při nejvýše jedné jedničce zvolíme t=0, je-li v první trojici,
a t=1 jinak; obě AMO pak platí. Nulový případ dovoluje obě volby.

První AMO má4 argumenty a6 párových klauzulí, druhá k−2
argumentů. Rekurze proto spotřebuje jednu pomocnou proměnnou
na zmenšení o2, dokud nezbývají3 nebo4 argumenty. Tím sedí
převzatý počet q a stejné množství3k−6 klauzulí, přičemž
pomocných proměnných je méně než k−3 pro k≥4. Pro k≤3
se nic nezlepšuje. To je přesný, nikoli asymptoticky neurčitý
obsah známého dodatku o snížení počtu t.

## Rozsah, errata a bibliografické meze

Všechna(a), rozhodovací úloha(b), všechny uvedené příklady,
důsledky a známý dodatek mají nyní argumenty. Jedinou neuzavřenou
matematickou formulací odpovědi je měřítko doslovné meze<3m
(P0816); správná lineární mez i přesné počty jsou hotové.

Prohledány všechny relevantní vrstvy all4a-pre/all4a/err4a/all4f0/
err4f0 podle55, str.87,544/545, renaming/Horn a citovaných jmen.
F0 odpověď55 na p191 patří jiné sekci; není opravou tohoto místa.
Zohledněny známé přidání odkazu na §7.2.2.2–12 a číslo5.2.4,
obojí bez vlastní karty. Originální erratum p22 je v obrazu
proof-errata-pre-p22.png.

Primární ScienceDirect záznam potvrzuje Aspvallův článek, Journal
of Algorithms1(1980),97–103, DOI10.1016/0196-6774(80)90007-3
(https://www.sciencedirect.com/science/article/abs/pii/0196677480900073).
Celý článek nebyl znovu auditován. Lewis1978 a přesné znění
Kleine Büning/Lettmann5.2.4 zůstávají bibliografickou výjimkou;
vlastní matematika je odvozena výše.

P87/file104 a p544–545/file561–562 zůstávají partial kvůli dalším
obsahovým částem a uvedeným přesným mezerám. Žádná nová celostránková
propagace. Dále56, hlavní text p63/file80; čtení218/file235 beze změny.
