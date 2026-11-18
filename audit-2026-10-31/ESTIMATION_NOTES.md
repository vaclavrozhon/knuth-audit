# Odhady vyhledávacích stromů — 7.2.2, strany 46–51, úlohy 49–61

Pracovní stav k 1. listopadu 2026. Dosud se kontrolují i velké královské
cesty a historické prameny; tato poznámka neuzavírá celý blok 49–61.

## F088: chybějící cena ve druhém momentu, odpověď 53, strana 406

Obecná rekurence nad odstavcem je správná. Je-li c cena současného uzlu,
d počet potomků, C_i cena i-tého podstromu a Q_i jeho druhý moment, pak

    Q = c² + d Σ Q_i + 2c Σ C_i.

Přepis s poli však místo posledního členu používá pouze `2 × COST[l]`.
Má být `2 × c(x1...x_(l−1)) × COST[l]`.

Nejkratší protipříklad má kořen a jediného potomka, oba s cenou 2.
Každý běh vrátí S = 4, takže rozptyl je 0. Tištěný algoritmus vypočte
Q = 4+4+4 = 12 a vrátí 12−16 = −4. Oprava dává Q = 16.
Není to spor s příklady dam: tam jsou všechny ceny rovny jedné.

V `check_estimation.py` byly přesně, pomocí racionálních čísel, porovnány
rekurence s úplným rozdělením všech cest na 1 000 různých stromech
s kladnými racionálními cenami. Opravený přepis všude souhlasí.
Na listech je třeba zvlášť položit m = M = C = c a Q = c²; tím se také
vyhneme implicitní konvenci 0·∞ při inicializaci MIN. Tu nepočítám jako
samostatný nález.

## F089: o jeden delší podmiňující prefix, odpověď 54, strana 407

V posledním faktoru pravděpodobnosti Π(x1...x_l) je vytištěno
`p_(x1...x_l)(x_l)`. Správně má být `p_(x1...x_(l−1))(x_l)`.
Pravděpodobnost volby poslední hrany je podmíněna jejím výchozím uzlem.
V listu navíc tištěná pravděpodobnost nemusí být vůbec definována.
Samotný převod vah `D ← D/p(I)` je správný; přesné testy zahrnovaly
jak rovnoměrné, tak nestejné kladné pravděpodobnosti.

## F090: spotřeba bitů při pěti možnostech, odpověď 49, strana 406

Údaj 3⅓ bitu pro samostatnou rovnoměrnou volbu z pěti možností je příliš
malý. Správné optimum je 3⅗ = 18/5 bitu. Srovnávací údaj 4⅘ pro prosté
zahazování trojic bitů je správný.

Krátký důkaz neplatnosti: žádný výsledek se nesmí rozhodnout dříve než po
3 bitech, protože pravděpodobnost každého má být 1/5 < 1/4. Po třech
bitech se smí rozhodnout nejvýše pět z osmi prefixů: dva prefixy pro
stejný výsledek by již měly hmotnost 1/4 > 1/5. Proto

    E T ≥ 3 + Pr(T > 3) ≥ 3+3/8 = 27/8 > 10/3.

Přesné optimum má silnější důkaz. Po k bitech může mít každý výsledek
nejvýše floor(2^k/5) dokončených prefixů délky k. Tedy

    E T ≥ Σ_(k≥0) (2^k mod 5)/2^k = 18/5.

Rovnosti dosahuje recyklování odmítnutého intervalu: po třech bitech
přijmout hodnoty 0–4; ostatní tři přenést do intervalu 0–2 a přidat bit.
Z nových šesti hodnot přijmout 0–4, jedinou zbylou zahodit a začít znovu.
Platí E T = 3 + 3/8 + (1/16) E T, tedy E T = 18/5.
Výčet všech dosažitelných stavů do 16 bitů pro q = 2–40 potvrdil
rovnoměrnost i optimální pravděpodobnosti pokračování.

Jde o jeden výběr bez přenášení náhodného stavu mezi různými voláními,
stejně jako u porovnávané metody v textu. Při hromadné výrobě mnoha
výsledků lze amortizovanou spotřebu snížit až k log₂ 5; to je jiný model.
Primární moderní rozbor tohoto rozlišení a přesné řady je v oddílech 1–2
[Lumbroso, arXiv:1304.1916](https://arxiv.org/abs/1304.1916), archivovaný
v `sources/estimation/`. Citovaný původní článek Knuth–Yao 1976 zatím
nemáme celý; bibliografické dočtení je v registru stále otevřené.

## F091: hladina 20 versus 21, hlavní text na straně 49

Počet vybraných prvků H má rozdělení počtu hlav z úlohy 52. Při ukončení
Algorithm E je však `l = H+1`, jak správně uvádí i sousední průměr H_n+1.
Proto pro n = 100 platí

    Pr(l ≥ 20) = Pr(H ≥ 19) = 1.9519870726687698 × 10^−8,
    Pr(l ≥ 21) = Pr(H ≥ 20) = 2.71522349094416 × 10^−9.

Tištěná hodnota 0.0000000027 odpovídá druhému řádku. Nejmenší oprava je
změnit `l ≥ 20` na `l ≥ 21` (případně `l > 20`).
Přesná konvoluce Bernoulliho veličin souhlasí se Stirlingovými čísly
z vytvářející funkce z(z+1)...(z+n−1)/n!. Pro n ≤ 12 souhlasí také
pravděpodobnost každé jednotlivé cesty se samostatným výčtem podmnožin.
Chyba trvá i v oficiální vydavatelské ukázce z dubna 2026, strana 49.

## F092: poloha návratové značky v odpovědi 58, strana 407

Značka (*) leží před `Set u ← T, T ← S ← Λ`. Návrat po
`u ← LINK(u)` proto znovu přepíše právě vybraný u a vynuluje rozpracované
seznamy. Značka musí být až před `For each w — u`, za inicializací.
Oprava z 14. února 2025 doplňuje zvýšení d a připojení S, ale značku
nepřemisťuje a návrat na ni výslovně ponechává.

Čtyřvrcholový protipříklad: hrany 0–1, 1–2, 1–3, cíl 0, odebíráme 1.
První vrstva označí 2 a 3 jako tarnished a vytvoří T = 3→2.
Na další vrstvě se zpracuje 3, potom `u ← LINK(3) = 2`.
Návrat na tištěné (*) přepíše u prázdným T = Λ. Následné procházení
sousedů nebo čtení LINK(u) tedy požaduje neplatný vrchol.

Doslovný test zachytil právě tento stav. Po posunutí značky a zapracování
známých oprav souhlasí všechny porovnávané vzdálenosti s novým BFS:
**162 366 kontrol**, všechny jednoduché grafy do šesti vrcholů s pevným
cílem 0 a každým dosažitelným odebíraným vrcholem, plus 300 náhodných
grafů do 64 vrcholů s postupným odstraňováním a opakovaným použitím
LINK a STAMP. Symetrie označení pokrývá i jiné cíle.
Autorův původní `WALK-RANDOM` má vnořené smyčky správně.

Důkaz opravené aktualizace: první fáze postupuje po původních vzdálenostech.
Vrchol w ve vrstvě d+1 se označí právě tehdy, když již nemá souseda
ve vrstvě d; indukcí tedy právě ztratil všechny původní nejkratší cesty.
Neoznačení sousedé jsou zdroje se správnými nezměněnými vzdálenostmi.
Fronta R a odložený seznam S zachovávají pořadí podle vzdáleností.
Druhá fáze je BFS zahájené z těchto zdrojů; každá dosud dosažitelná
poškozená komponenta má některý zdroj na hranici, takže žádná nechybí.

## Errata a otevřená návaznost C015

F088–F092 byly zobrazeny v hlavním PDF druhého dotisku i v autorově
Fascicle 5B PostScriptu (strany 44,45,21). Prověřeny jsou
err4b.textxt, err4f5.textxt a historické all4b.txt/all4f5.txt, včetně
posunů stran a změn obsahu. Odpovídající opravy nebyly nalezeny.
Fyzické výtisky dosud ověřené nejsou; návrhy se neodesílají.

Známé erratum E014 zahrnuje:

- 28. 1. 2024: v E5 přesunout D ← Dd před ukončení při d = 0 a rozšířit
  výklad počítání řešení. Nyní konečné D správně odhaduje počet řešení
  i při slepých větvích.
- 11. 11. 2023: na straně 50 „they defend“ → „they defined“.
- 14. 2. 2025: „every shortest path“, doplnit d ← d+1 a připojení S;
  na straně 408 zdůraznit dvojí použití S.

**C015:** změna E5 z roku 2024 narušuje doslovné znění úlohy 57, která
stále používá konečné D ve všech listech. Pro kořen bez přípustných
potomků je M = 1 a nové konečné D = 0; požadovaná nerovnost by byla
0 ≥ 1. Původní důkaz a tvrzení jsou správné pro součin nenulových stupňů
na cestě, tedy D před závěrečným nulováním. Nejnovější úplné zadání 57
nemáme, proto návaznost na již známou opravu zatím vedu jako kandidáta,
odděleně od F088–F092. Ukázka 2026 změnu E5 skutečně obsahuje.

## Správné výsledky a obecné důkazy 49–57

Čtyři příklady Fig. 69 byly znovu vygenerovány přímo z binárních rozvojů
π,e,φ,γ. Souhlasí všechny volby, odmítnuté skupiny bitů, délky 10/20/13/13
i odhady 2129/2689/1489/2609. U e jsou skutečně odmítnuty 101,111,110.
Jednotlivé pozice a stupně obsahuje `exact-verified.json`.

Věta E: dosažení uzlu s pravděpodobností p násobí jeho cenu vahou 1/p,
takže očekávaný příspěvek je právě tato cena. Součet přes konečný strom
dokazuje očekávanou celkovou cenu. Totéž s cenou indikující hloubku
prokazuje 50. Martingal 51 plyne z podmíněné rovnosti
c(v)+Σ p_i C(v_i)/p_i = C(v); po ukončení se drží konstantní.

Úloha 52: součin (1−1/k+z/k) dává Stirlingovo rozdělení. Pravděpodobnost
konkrétní množiny hlav se teleskopicky rovná součinu převrácených
aktuálních mezí Elmových voleb. Chernoffova mez s průměrem H_n dává
pro k = floor((ln n)(ln ln n)) ocas menší než libovolná mocnina 1/n.
V části (d) není nutné (a nebylo by správné) omezit jednotlivý odhad
počtem uzlů prvních k úrovní. Stačí **Markovova nerovnost pro zkrácený
odhad**, jehož očekávání je Σ_(j≤k) binom(n,j) ≤ 2(en/k)^k. Po vydělení
exp((ln n)² ln ln n) je pravděpodobnost opět menší než libovolná mocnina
1/n. Přidáme pravděpodobnost delší cesty z (c). Tím je krátký důkaz
z odpovědi (d) plně doplněn; nejde o další chybu.

Úloha 54 po F089: váha uzlu je převrácený součin skutečných podmíněných
pravděpodobností, proto stejný důkaz funguje. V rekurencích 53 se d nahradí
1/p_i; smíšený člen 2cΣC_i se nemění.
Úloha 55: při p_i=C_i/ΣC_j indukčně vrátí každý podstrom přesnou cenu;
nový odhad je c+C_i/p_i=c+ΣC_j. Kladnost cen zajistí p_i>0.

Úloha 56: nové rozhodování po zamítnutí kandidáta tvoří skryté binární
vrstvy, protože stav obsahuje i již zamítnutá slova. Zahrnout jejich práci
do ceny původního uzlu nestačí bez odpovídajícího modelu větvení.
Při prázdném poison listu se po zamítnutí minimální třída zmenší z r
na r−1 a zůstane minimální, což opravňuje navrženou r- nebo (r+1)-cestnou
variantu. Bias vůči dražšímu podstromu odpovídá ideálním pravděpodobnostem55.

Původní úloha 57: pro listy p_i>0 a Σp_i=1 dává AM–GM
Πp_i ≤ M^(−M), tedy (ΠD_i)^(1/M)≥M. Rovnost nastane při rovnoměrných
pravděpodobnostech listů. Důkaz přes KL divergenci v knize je rovněž správný.

## Přesné momenty stromů dam

| n | Minimum | Maximum | Střední hodnota | Rozptyl |
|---:|---:|---:|---:|---:|
| 4 | 13 | 21 | 17 | 8 |
| 8 | 489 | 7 409 | 2 057 | 1 146 640 |
| 16 | 2 597 105 | 131 048 318 769 | 1 141 190 303 | 1 522 351 842 871 679 100 |

Všechna čísla (32),(33) souhlasí. U 16 dam je směrodatná odchylka
1 233 836 230.16658. C++ prošel celý strom a počítal přesné celočíselné
momenty. Nezávislý Python vygeneroval všechny jednotlivé cesty pro
4 a 8 dam a přesně sečetl jejich racionální pravděpodobnosti; shoda úplná.
Běh a příkaz jsou v `queen-moments-run.json`, malá nezávislá kontrola
v `queen-independent.json`. Výsledky neopakujeme bez důvodu.

## Královské cesty: přesná čísla 59 a experiment 60

Původní SIMPATH a SIMPATH-REDUCE, sestavené z archivovaných CWEB zdrojů,
vytvořily ZDD se **3 174 197 uzly včetně obou sinků**. Samostatný
C++ hodnotitel s přesnými 128bitovými celými čísly potvrdil všech osm
Vennových počtů na straně 408, počet cest, součet jejich délek i počet
Hamiltonovských cest na straně 51. U 2×2 a 3×3 byly navíc všechny
reprezentované množiny hran porovnány s úplným nezávislým DFS (5 a 235 cest).
Graphillion používá nezávisle sestavený graf. Běh skončil 1. listopadu
2026 v 09:42:38 UTC s návratovým kódem 0 po 4576 sekundách.
Graphillion spočítal všech 57 délkových koeficientů 8×8. Jejich součet,
součet délek, Hamiltonovské cesty i všech osm Vennových počtů souhlasí
s původní konstrukcí; jednotlivé vnitřní koeficienty z původního ZDD
se nepočítaly. Zároveň jsou ověřené
menší grafy 2×2, 3×3 a 4×4. Kompletní výstup je
`results/estimation/king-8-graphillion.json`, příkaz a stav v
`graphillion-run.json`. Tím je nezávislá kontrola úlohy 59 uzavřená.

Obecná kontrola rekurence: bez použití hrany e přecházíme do dolního
potomka beze změny množiny navštívených míst, s použitím hrany do
horního potomka a masku návštěv nahradíme j OR t. To dává právě vzorec
v odpovědi pro t=0,1,2,4. Pro délku platí g_x(z)=g_l(z)+z*g_h(z),
tedy L_x=L_l+L_h+N_h. Tento druhý výpočet nevyžaduje uchovávat polynom.

Příklad s bity π na straně 50 má přesně uvedených 36 kroků, spotřebuje
95 bitů a vrací **866 843 099 136 000 000 000**. Počty stupňů 1 až 7
jsou 2,4,4,10,9,6,1. Obnoveno čerstvým BFS po každém kroku,
bez použití WALK-RANDOM nebo jeho inkrementální tabulky vzdáleností.
Zdroj a výsledek: `check_estimation_examples.py`, `examples-verified.json`.

Úloha 60: vlastní reprodukovatelný experiment obsahuje 20 dávek po 10 000
cestách pro každou strategii. Pro rovnoměrný výběr vyšel průměr
5.10413×10^25 a relativní RMSE průměrů jednotlivých dávek 9.47 %;
pro váhy 1+DIST² průměr 5.02668×10^25 a RMSE 5.40 %. Medián χ se
snížil z 0.0592 na 0.0226. Přesná hodnota je 5.081954277…×10^25.
Vlastní pevné seedy tedy podporují odpověď „ano“. Nejde o tvrzení,
že jsme obnovili neznámá náhodná data původního obrázku, ani o záruku,
že každá jednotlivá vychýlená dávka vyjde lépe. Prvních 10 000 vzorků
obou strategií je uloženo v CSV; všech 40 souhrnů v JSONL.

Technická odchylka při sestavení reduceru: GNU89 vracelo poslední výsledek
fprintf místo nuly; sestavení GNU99 obnovilo standardní návrat z main
bez zásahu do algoritmu. Původní zdroje zůstaly nezměněné; changefile
jen odděluje pracovní cestu souboru se jmény.

## Cayleyovy posloupnosti 61

Všechny části (a)–(c) a citovaná asymptotika jsou prověřené.
`check_cayley.py` spočítal P_n metodou diferencí do n=200. Nezávislá
rekurence binárních rozkladů b(j)=b(j−1)+[j sudé]b(j/2) potvrdila
hodnoty do n=20. Dalších 160 případů různých n,m bylo ověřeno běžným
počítáním rozkladů dynamickým programováním. Všechny uvedené počáteční
hodnoty a koeficienty a_nk souhlasí.

(a) Počty uzlů po úrovních splňují 1≤x_(k+1)≤2x_k. Obráceně lze každý
takový profil realizovat: mezi x_k rodičů rozdělíme x_(k+1) potomků,
nejvýše dva na rodiče. Strom výšky n má v knižní konvenci n úrovní.

Výslovná bijekce s rozklady 2^n−1: položíme a_i=2x_i−x_(i+1) pro
i<n a a_n=2x_n−1. Potom Σa_i*2^(n−i)=2^n−1. Z rozkladu zpětně
obnovíme x_n=(a_n+1)/2 a x_i=(a_i+x_(i+1))/2. Celočíselnost plyne
postupně z parity celkové hodnoty a nezápornost a_i dává žádané meze.
Totéž pro x_1=m dává rozklady 2^n*m−1 s díly nejvýše 2^(n−1).
Pro n≤6 byly navíc výslovně zkontrolovány obrazy všech posloupností.

(b) P_(n+1)(m)=Q_n(2m), Q_n(m)=Σ_(j=1)^m P_n(j). Součet polynomu
stupně n−1 má Newtonovy koeficienty právě z diferencí P_n(1),…,P_n(n).
Tabulku jeho hodnot při 2,4,…,2n+2 lze vytvářet samotným sčítáním
diferencí. V každém stupni stačí O(n²) sčítání čísel s O(n²) bity;
celková mez O(n^5) bitových operací v knize je tedy dosažitelná bez
skrytého předpokladu konstantní ceny velkých násobení.

(c) X_(k+1)=ceil(2U_k X_k)≥2U_k X_k. Produkt stupňů proto dominuje
2^binom(n,2)*m^(n−1)*Π_(i=1)^(n−2) U_i^(n−1−i).
Nezávislost a E(U^r)=1/(r+1) dávají uvedenou dolní mez.

Historické prameny jsou archivovány i s URL a SHA256:
[Cayley 1857, str.245–248](https://www.math.ucla.edu/~pak/papers/Cayley-comp.pdf),
[Cook–Kleber 2000, 16 stran](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r44/pdf/),
[Mahler 1940, str.115–123](https://carmamaths.org/resources/mahler/docs/068.pdf).
Cayleyho formulace používá dvě rozlišené jednotky a hodnotu 2^(n−1)−1;
je ekvivalentní běžným binárním rozkladům 2^n−1. Cook–Kleber skutečně
studují podobné, nikoli totožné posloupnosti a používají Knuthův odhad.

Mahlerova věta na str.121–123 dává pro z=2^(n−1)−1 a celé k zvolené
podle 2^(k−1)k≤z<2^k(k+1):

    lg P_n = −k(k−1)/2 + k lg z − lg k! + O(1).

Z podmínky plyne k=n−lg n+O(1). Při h=n−k a t=lg n dostáváme

    lg P_n = binom(n,2) − lg(n−1)! − h(h−1)/2 + (h−1)t + O(1)
           = binom(n,2) − lg(n−1)! + t(t−1)/2 + O(1),

protože h−t=O(1) a chyba aproximace logaritmu součinu posledních h−1
faktorů faktoriálu je O(h²/n). To je přesně formule v knize. Číselná
rezidua do n=200 jsou pouze doplňková kontrola, nikoli její důkaz.

## Doplňkové odhady na stranách 48 a 51

Vlastních 20×1000 pokusů s 64 dámami dalo průměr 3.8855×10^65.
Průměry jednotlivých tisícových dávek leží mezi 2.4743×10^65 a
6.7832×10^65. Knižní hrubý odhad „asi 3×10^65“ z tisíce vzorků proto
není v rozporu s experimentem; nejde o přesně určenou velikost stromu.
U jezdcových cest dalo 20×10000 pokusů průměr 9.42169×10^19,
což leží v uvedeném intervalu (8.6±1.2)×10^19. Generátor, seedy a časy
jsou zaznamenány; `check_estimation_extra.cpp` používá vlastní bitboard
a při každém kroku cesty čerstvě počítá dosažitelnost cíle.

## Zbývá v tomto okolí

Historickou kapitolu Knuth–Yao 1976 a obecné
historické poznámky na stranách 53–54 zatím neoznačuji za dočtené.


## Doplnění 17. listopadu 2026: C015 bez degenerovaného případu

Knižní čtyřdámový strom(4) má šest listů s původními konečnými vahami
8,8,4,4,8,8. Po změněE5 z28.1.2024 jsou váhy0,0,4,4,0,0,
protože čtyři listy jsou slepé a dva řeší úlohu. Jejich geometrický
průměr je0, ale původní úloha57 požaduje alespoň6. Tím je doložena
neslučitelnost publikované změny s původním zadáním; nejde jen
o kořen bez potomků. Aktuální úplné znění57 stále nemáme. C015
zůstává kandidátem s tímto omezením. Náhled má74 souborových stran
a toto zadání neobsahuje. Podrobnosti tohoto druhého průchodu:
`../integration/2026-11-17-focused-4b/notes/second-pass-05.md`.
