# V4A-F0006 — nesprávná pravděpodobnostní limita náhodných Hornových klauzulí

6. listopadu 2026. **Confirmed, medium.** Zadání §7.1.1–50,
p86/file103; sazba images/proof-file103.png. Odpověď na p543/file560
pouze odkazuje na Istrateho článek. Níže je nezávislý rozpor přímo
s knižním modelem, bez simulace a bez předpokladu správnosti článku.

Pro c=10 vytištěná limita dává alespoň e^(-10). Dokážeme však

    limsup P_n(10) ≤ e^(-18) + e^(-12)/(1-e^(-6)) < e^(-10).

Tím je nepravdivost vytištěné limity doložena, aniž bychom museli
určit správnou limitu nebo dokonce předpokládat její existenci.

## 1. Přesný model a počet klauzulí — P0748

Klauzule je normalizovaná množina literálů bez protikladného páru,
s nejvýše jedním kladným literálem. Čistě záporných klauzulí je
2^n, včetně prázdné; kladnou hlavu lze zvolit n způsoby a množinu
záporných literálů z ostatních n−1 proměnných 2^(n−1) způsoby.
Proto T_n=(n+2)2^(n−1), přesně jako v knize. Jednotlivé výběry
jsou nezávislé a stejnoměrné, s opakováním. Volíme c=10,
takže m=10·2^n je celé číslo pro každé n; zaokrouhlování není problém.

## 2. Nutné podmínky pro nejmenší model — P0749

Každý splnitelný Hornův systém má nejmenší model S⊆[n].
Přesné důkazy nejmenšího modelu a odvozování jsou P0726/P0735
a P0738/P0744; použijeme je v tomto rozsahu:

Nejprve uzavřeme pouze definite klauzule od faktů. Je-li celý
systém splnitelný, tato uzávěra je obsažena v každém modelu,
a proto také splní čistě záporné klauzule (jejich modely jsou
uzavřené směrem dolů). Je tedy nejmenším modelem celého systému.
Každá proměnná i∈S byla poprvé odvozena z klauzule s hlavou i
a předpoklady obsaženými v dříve odvozené části S, tedy v S\{i}.

Pro pevné S s |S|=k musí tudíž platit obě následující podmínky:

* Nevyskytuje se žádná klauzule porušená přiřazením S.
  Takových klauzulí je přesně (n−k+1)2^k: 2^k čistě záporných
  s množinou předpokladů v S, a po 2^k pro každou hlavu mimo S.
* Pro každé i∈S se vyskytuje alespoň jedna klauzule z množiny
  W_i={R⇒i : R⊆S\{i}}, která má 2^(k−1) prvků.

Množiny W_i jsou navzájem disjunktní, protože mají různé hlavy;
všechny jsou disjunktní od množiny porušených klauzulí. Druhá
podmínka sama nevylučuje cyklické podpory, ale potřebujeme pouze
nutnost, takže případné nadpočítání je pro horní mez bezpečné.

## 3. Pomocný nezávislý Poissonův model — P0750

Každému z T_n typů klauzulí přidělme nezávislý počet výskytů
Poisson(λ), kde λ=18/n. Celkový počet M má rozdělení

    Poisson(μ),   μ=λ T_n=9(1+2/n)2^n.

Podmíněně při M=t dostáváme právě t nezávislých stejnoměrných
klauzulí s opakováním: pravděpodobnost počtů a_1,…,a_T se po
podmínění rovná t!/(T^t∏a_i!), tedy multinomickému rozdělení.
Lze proto spojit oba modely stejnou nekonečnou posloupností
nezávislých klauzulí a nezávislým počtem M.

Pro n≥36 platí μ≤9.5·2^n, tedy m−μ≥0.5·2^n. Chebyshevova
nerovnost dává Pr(M>m)≤μ/(m−μ)^2≤38·2^(-n)→0.
Přidáním klauzulí se splnitelnost nemůže zvýšit, a proto

    P_n(10) ≤ Pr(Poissonův systém je splnitelný) + Pr(M>m).

Poissonizace zde tedy poskytuje horní mez pro správný knižní
model s pevným počtem klauzulí, nikoli jeho neodůvodněnou náhradu.

## 4. Horní mez přes všechny možné nejmenší modely — P0751

Z disjunktnosti v části 2 plyne pro pevné S s k prvky nutná
událost s pravděpodobností přesně

    exp(-λ(n-k+1)2^k) · (1-exp(-λ2^(k-1)))^k.

Pro k=0 je druhý faktor 1 a první exp(-λ(n+1)). Sjednocovací
mez tedy dává pro pravděpodobnost splnitelnosti horní mez součtem
těchto výrazů vynásobených binom(n,k), pro k=0,…,n.

Člen k=0 je nejvýše e^(-18). Pro 1≤k≤n/2 využijeme
binom(n,k)≤n^k/k!, 1-e^(-z)≤z a λ(n-k+1)≥9:

    člen k ≤ ((9·2^k)^k/k!) exp(-9·2^k).

Pro každé k≥1 máme k≤2^(k−1) a k^2≤(9/8)2^k.
První nerovnost plyne indukcí; druhá se přímo ověří pro k=1,2,3
a pokračuje, protože (k+1)^2≤2k^2 pro k≥3. Dále ln9<3 a ln2<1.
Proto

    ln((9·2^k)^k/k!) ≤ k ln9 + k^2 ln2
                      < 3k+k^2
                      ≤ (21/8)2^k < 3·2^k.

Každý takový člen je tedy nejvýše exp(-6·2^k).
Zbývající k>n/2 můžeme omezit hrubě: faktor podpory je ≤1,
n−k+1≥1 a 2^k>2^(n/2), takže jejich celý součet je nejvýše

    2^n exp(-(18/n)2^(n/2)) → 0.

Tento odhad pokrývá i k=n. Nezaměňujeme tedy limitu se součtem
pouze nad pevnými k a nenecháváme nezkontrolovaný velký ocas.

Spojením s částí 3 dostáváme

    limsup P_n(10) ≤ e^(-18)+Σ_{k≥1}e^(-6·2^k)
                  ≤ e^(-18)+e^(-12)/(1-e^(-6))
                  < 3e^(-12) < e^(-10).

Poslední dvě ostré nerovnosti používají pouze e^(-6)<1/2,
e^(-18)<e^(-12) a e^2>3. Žádné desetinné přiblížení se nepoužívá.

## 5. Přímý rozpor a meze závěru — P0752

Vytištěný nekonečný součin má všechny faktory v (0,1). Jeho
hodnota je nejvýše první faktor 1−e^(-10). Tištěná pravá strana
je proto alespoň e^(-10), v ostrém rozporu s právě dokázanou
horní mezí limsup. Nejde o chybu pouze pomocného důkazu:
samotná požadovaná asymptotická pravděpodobnost je nesprávná.

Přesnou správnou limitu zde **netvrdíme**. Ze samotného rozporu
neplyne, že stačí všude nahradit c za 2c; takový návrh by potřeboval
nový obecný limitní důkaz. Algoritmus C a konečný počet T_n jsou
správné a tímto nálezem nejsou zpochybněny.

## 6. Primární citace, originál a errata

Bibliografický odkaz na odpovědi 50 byl ověřen proti stránce
[vydavatele](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.10028):
Gabriel Istrate, Random Structures & Algorithms 20(4), 2002,
483–506. Abstrakt obsahuje stejnou limitu. Autorův
[preprint](https://arxiv.org/abs/cs/9912001) je uložen jako
sources/istrate-random-horn-1999.pdf s metadaty; jeho strana 5
je v images/istrate-random-horn-p5.png.

V sazbě preprintu je uveden počet N(n)=(n+2)2^n−1, který
neodpovídá normalizovaným neprázdným Hornovým klauzulím:
těch je (n+2)2^(n−1)−1. Tentýž nesprávný jmenovatel je
vidět v images/istrate-random-horn-18.png a -19.png. Proto
citaci nelze mechanicky převzít bez kontroly normalizace.
Neprohlašujeme tím prověření celého článku ani jeho konečné
časopisecké sazby; vlastní rozpor části 1–5 na článku nezávisí.

Původní knižní sazba p86/file103 a odpověď p543/file560 byly
zobrazeny. Relevantní vrstvy errata/text/all4a-pre.txt, all4a.txt,
err4a.txt, all4f0.txt a err4f0.txt byly prohledány podle stran
86/543, úlohy/odpovědi 50, jména Istrate, Horn, satisfiability
a obsahu formule. Žádná odpovídající oprava není uvedena.
F0 je předchůdcem této části; F1 obsahuje jiné sekce. Kontrola
provedena 6. listopadu 2026. Fyzický exemplář nebyl porovnán;
nález neobsahuje tvrzení o prvenství.

Jediná error lokace pro UI: file103 / printed86, tvrzení v zadání50.
Citace v odpovědi543 sama není druhou matematickou chybou.
