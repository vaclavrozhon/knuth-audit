# Hornova implikace 49 a náhodný model 50

Checkpoint X0079, P0746–P0752. Původní zadání p86/file103,
odpovědi p543/file560; images/proof-file103.png a proof-file560.png.
Žádný program, simulace nebo census.

## Úloha 49: implikace obou Hornových funkcí — P0746

Nechť G=∧_j c_j. Potom F≤G právě tehdy, když neexistuje
přiřazení s F=1 a G=0. Podle De Morganovy identity to je
ekvivalentní nesplnitelnosti každého F∧¬c_j zvlášť.
Je-li c_j disjunkce literálů, ¬c_j je konjunkce opačných
jednotkových literálů. Kladná jednotka je definite Hornova
klauzule, záporná jednotka je indefinite Hornova klauzule.
Každý test je tedy instance již dokázané úlohy48/P0744.

Jestliže některý test vrátí model, jde přímo o svědka F=1,G=0.
Jsou-li všechny nesplnitelné, libovolný model F splňuje všechny
c_j, tedy G. To dokazuje obě implikace a algoritmus poskytuje
také konkrétní protipříklad, když implikace neplatí.

Při délkách N_F,N_G, r klauzulích G a n proměnných je jednoduchá
implementace nejvýše O(r(N_F+n)+N_G), tedy polynomiální v délce
explicitního vstupu. Připojení jednotek pro c_j stojí O(|c_j|).
Při r=0 je G=1 a test vrátí true; prázdná klauzule c_j=0
má ¬c_j=1, takže se správně testuje nesplnitelnost F. Protichůdné
jednotky se zpracují obecným Horn SAT algoritmem; n=0 také funguje.
Netvrdíme bez důkazu lineární čas pro celou sérii r testů.

## Přidané tvrzení o přeznačení — P0747 partial

Závorka v odpovědi49 navíc tvrdí existenci efektivního testu,
zda existují y_1,…,y_n tak, že F(x)=G(x XOR y), a odkazuje
na Kleine Büning–Lettmann, Aussagenlogik (1994), §5.6.
Dané y lze polynomiálně ověřit: F≤G(x XOR y) testujeme po
jednotlivých přeznačených klauzulích G, jejichž negace jsou stále
konjunkce jednotek. Opačnou implikaci přepíšeme bijekcí x↦x XOR y
na G≤F(x XOR y) a použijeme stejný postup. Přeznačený celý CNF
nemusí být Hornův; Hornův je vždy testovaný antecedent s jednotkami.
Automatické hledání y tím ale dokázáno není a pouhé vyzkoušení
všech 2^n možností by efektivnost neprokázalo. Tato matematická
povinnost zůstává partial, nikoli bibliografickým skipem vydávaným
za důkaz. Nevzniká z ní karta, protože není znám konkrétní rozpor.

## Úloha 50: rozpis a nalezený rozpor

Samostatná poznámka F0006-random-horn-limit.md obsahuje úplné
argumenty P0748–P0752:

* P0748: přesný správný počet (n+2)2^(n−1) v knižním modelu.
* P0749: disjunktní množiny nutných podpor nejmenšího modelu
  a klauzulí, které ho porušují.
* P0750: přesný Poissonův převod a jednostranná vazba na pevné m.
* P0751: obecná horní mez, uniformní malé i velké velikosti modelu.
* P0752: ostrý rozpor s vytištěnou limitou při c=10.

To je F0006 confirmed/medium, jediná error lokace p86/file103.
Horní mez je nezávislá na citovaném článku; správná přesná limita
zůstává neurčena. Bibliografie Istrateho článku byla ověřena na
primárních zdrojích, jeho preprint má odlišný chybný normalizační
počet a není použit jako matematický vstup.

Žádná stránka se tím celá neuzavírá. Na p86 čekají 51–54,
na p543 je navíc nevyřešený dodatek P0747 a odpověď51. Main-text
frontier p60/file77, čtení p218/file235 zůstávají oddělené.
