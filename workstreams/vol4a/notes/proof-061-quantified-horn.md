# Úlohy 7.1.1–58/59: kvantifikované Hornovy formule

Checkpoint X0090, P0842–P0849. Zadání p87/file104, odpověď
p545/file562 a její pokračování p546/file563 přečteny v původní
sazbě `proof-file104/562/563.png`. Přesně se přebírá důkaz
nejmenšího Hornova modelu z proof-047 a lineární implementace C
z proof-049; žádný matematický program ani nový běh se nepoužil.

## Doména a nová univerzální proměnná — P0842

Každá booleovská proměnná je v prefixu právě jednou; žádné volné
proměnné. Existenciální strategie závisí pouze na dřívějších
univerzálních hodnotách. Duplicitní literály lze odstranit,
tautologickou klauzuli zahodit; prázdnou klauzuli naopak zachovat.

Zaveďme novou proměnnou x₀=⊥. Do každé čistě záporné klauzule
přidáme kladný literál x₀ a prefix rozšíříme zleva o ∀x₀.
Při x₀=0 zůstává původní formule; proto pravdivost rozšířené
formule implikuje původní pravdivost. Obráceně původní vítězná
strategie funguje pro obě x₀, protože x₀=1 tyto klauzule pouze
oslabuje. Rozšíření tedy zachovává pravdivost, včetně prázdné
klauzule, která se změní na jednotkovou (x₀).

Každá nová klauzule je definite Horn, tedy pravidlo A→z s právě
jednou kladnou hlavou. **x₀ se nikde nevyskytuje v těle pravidla.**
Univerzální proměnné jsou x₀,…,x_m, existenční y₁,…,y_n.
Značka u≺v označuje pořadí kvantifikátorů, nikoli indexů.

## Proč lze odstranit pozdější univerzální předpoklad — P0843

Odpověď odstraňuje x_j z těla pravidla A→y_k, jestliže y_k≺x_j.
To obecně nezachovává jednotlivou strategii; potřebujeme zachování
**existence** vítězné strategie. Následuje obecný důkaz tohoto kroku.

Modely Hornovy formule jsou uzavřené na konečný neprázdný průnik:
pokud je celé tělo pravidla pravdivé v průniku, je pravdivé v každém
modelu, a tedy je v každém modelu pravdivá i hlava. Přesný stejný
princip pro Hornovy funkce byl dokázán v proof-047.

Nechť s_y(a_{<y}) je libovolná vítězná strategie. Pro úplné
přiřazení univerzálních proměnných a vezměme průnik všech jejích
výsledných modelů pro b≥a, souřadnici po souřadnici. Jejich
univerzální část má průnik přesně a, protože mezi nimi je b=a.
Existenční souřadnice y má hodnotu

    g_y(a_{<y}) = AND { s_y(c) : c ≥ a_{<y} }.

Každý takový prefix c má úplné rozšíření b≥a, a s_y na budoucích
hodnotách nezávisí. Průnik je tedy opět legální vítězná strategie.
Navíc je g_y monotónní ve všech svých univerzálních vstupech:
větší a zmenší množinu konjunktů, takže výsledek nemůže klesnout.
Tento důkaz existence nic exponenciálně nepočítá.

Kdyby taková monotónní strategie porušovala pravidlo po odstranění
všech univerzálních členů pozdějších než jeho hlava y, nastavme
tyto odstraněné proměnné na 1 a ostatní univerzální hodnoty nechme.
Hodnota y se nezmění, protože všechny změněné proměnné jsou pozdější.
Všechny ostatní členy těla zůstanou 1: univerzální hodnoty neklesly
a existenční strategie jsou monotónní. Původní pravidlo by proto
bylo porušeno také, spor. Jedna strategie tedy splňuje všechna
zesílená pravidla zároveň. Opačný směr je okamžitý, neboť každé
zesílené pravidlo implikuje původní. Redukce v odpovědi je platná.

## Jádra jsou definována bez kruhu — P0844

Pracujme s redukovanou soustavou pravidel H. Nejprve spočteme

    C₀ = core(H ∪ {x₁,…,x_m}).

Žádné y nepředchází x₀, takže vytištěná definice C₀ neodkazuje
na sebe prostřednictvím dalších existenčních jednotek. Potom pro
každé j=1,…,m spočteme

    C_j = core(H ∪ {x_i : i≠j}
                   ∪ {y_k : y_k≺x_j a y_k∈C₀}).

Core je nejmenší množina obsahující jednotkové předpoklady a
uzavřená na pravidla H. Každý model těchto pravidel a jednotek
obsahuje core; samotná charakteristická funkce core je model.
To se přebírá z proof-047/049, nikoli pouze z názvu algoritmu.
Test v odpovědi je x_j∉C_j pro každé j=0,…,m.

## Nutnost všech testů — P0845

Předpokládejme vítěznou strategii pro H. Pro j=0 zvolme x₀=0
a všechny ostatní univerzální proměnné 1. Výsledný model obsahuje
všechny počáteční jednotky C₀. Proto x₀∈C₀ není možné.

Pro j>0 se nejprve podívejme na hru, ve které jsou **všechny**
univerzální proměnné 1, včetně x₀. Výsledný model obsahuje jednotky
C₀, a tedy také každé y_k∈C₀. Nyní změňme pouze x_j na 0.
Každé y_k≺x_j má stejný předchozí univerzální prefix, takže jeho
hodnota zůstává 1, pokud y_k∈C₀. Výsledný model proto obsahuje
všechny počáteční jednotky C_j, ale neobsahuje x_j. Nemůže tedy
platit x_j∈C_j. Přítomnost jednotky x₀ v C_j pro j>0 není problém:
právě pro tento argument jsme použili hru s x₀=1.

## Dostatečnost, legální strategie a všechny typy klauzulí — P0846

Předpokládejme x_j∉C_j pro všechna j. Definujme

    y_k = 0,                         jestliže y_k∉C₀;
    y_k = AND { x_j : y_k∉C_j },      jestliže y_k∈C₀.

Prázdná konjunkce má hodnotu 1. Pokud y_k≺x_j a y_k∈C₀,
je y_k jednou z počátečních jednotek C_j. V jeho konjunkci se
tedy mohou objevit pouze univerzální proměnné předcházející y_k.
Jde o legální strategii. x₀ v žádné takové konjunkci není,
protože v této větvi y_k∈C₀.

Zvolme libovolné úplné univerzální přiřazení. Ověření klauzule
A→z rozdělíme podle její hlavy; při z=1 je pravidlo automaticky
splněno, takže zbývá vždy jen z=0.

* **z=x_j.** Kdyby A⊆C_j, uzavřenost core by dala x_j∈C_j.
  V A je tedy proměnná mimo C_j. Všechny jiné univerzální x_i
  jsou v C_j jako jednotky; samotné x_j v těle po odstranění
  tautologií není. Musí tedy existovat y_l∈A\C_j. Pokud y_l∉C₀,
  strategie je 0; jinak jeho konjunkce obsahuje x_j=0. V obou
  případech je celé tělo nepravdivé.
* **z=y_k∉C₀.** Všechny univerzální proměnné, které se mohou
  v těle objevit, jsou v C₀: jsou to x₁,…,x_m, zatímco x₀
  nikde v těle není. Protože y_k∉C₀, obsahuje A existenční
  y_l∉C₀. Jeho strategie má hodnotu 0.
* **z=y_k∈C₀, ale y_k=0.** Nějaký faktor x_j=0 jeho konjunkce
  má y_k∉C_j. Uzavřenost C_j opět dává člen A mimo C_j.
  Je-li to univerzální proměnná, je to právě x_j=0. Je-li to
  y_l, je buď mimo C₀ a rovno 0, nebo má x_j jako faktor a je
  také 0. Tělo je proto nepravdivé.

Všechny klauzule platí pro všechna univerzální přiřazení. To
dokazuje tvrzenou ekvivalenci i explicitní konstrukci strategie;
nejde jen o rozhodnutí pomocí neověřeného vnějšího algoritmu.

## Invarianty implementace a náklady — P0847

Označme L počet výskytů literálů po doplnění x₀, r počet klauzulí
a V=m+n+1 počet proměnných prefixu. Odstranění tautologií/duplicit
lze udělat časovými značkami proměnných v O(L+r+V); pořadí prefixu
a odstranění pozdějších univerzálních členů stojí totéž.

Spočteme C₀ a pak m dalších jader. Každý běh má nejvýše V
jednotkových předpokladů. Použije přesně lineární core algoritmus C
z `notes/proof-049-horn-core-algorithm.md`: pro jeho výskytové
seznamy, počitadla, monotónní stav zjištěných proměnných, ukončení
i amortizovaný průchod každým výskytem již existuje obecný důkaz.
Začlenění jednotek nemění tyto invarianty. Jeden běh stojí
O(L+r+V), celkem tedy

    O((m+1)(L+r+V)) času.

Pro samotné rozhodnutí stačí držet C₀, aktuální C_j a znovu
použitelná pracovní pole, dohromady O(L+r+V) paměti. Není třeba
zachovávat všechna jádra. Chceme-li navíc vypsat všechny strategie,
pro každý pár (j,k) zjistíme členství y_k∈C_j; celý výstup má
nejvýše mn literálů plus n konstant a lze jej uchovat s touto
dodatečnou pamětí. Tento výstupní čas je již pokryt uvedenou mezí.
Kniha v 58 slibuje účinný algoritmus, nikoli lineární čas z 57.

## Okraje — P0848

* Bez původních univerzálních proměnných je m=0 a jediný test
  x₀∉C₀ je přesně dříve dokázaný Horn SAT test z úlohy 48.
* Prázdná konjunkce má žádná pravidla; každé x_j chybí v C_j,
  všechny nepoužité existenční proměnné mohou být 0. Test přijme.
* Prázdná klauzule vytvoří jednotku x₀, takže test C₀ zamítne.
  Jednotka univerzálního x_j obdobně způsobí x_j∈C_j.
* Bez existenčních proměnných má každé netautologické pravidlo
  univerzální hlavu a ostatní univerzální proměnné v těle. Pro
  její C_j jsou tyto členy jednotky, takže test správně zamítne.
* Nepoužité proměnné prefixu se počítají do V. Žádný náklad
  se neschovává za tvrzení, že každá proměnná musí být v klauzuli.

## Úloha 59: přesný počet pravdivých prefixů — P0849

Pořadí x₁,…,x_n je pevné. Nejde o počítání přeházených prefixů,
ale o 2ⁿ voleb Q_i∈{∃,∀}. Nechť T(f) je počet voleb, pro které
Q₁x₁…Q_nx_nf platí. Dokážeme T(f)=počet jedniček tabulky f.

Pro n=0 existuje jediný prázdný prefix i jediný vstup, a obě
počítané hodnoty jsou f. Pro každý pevný suffix Q₂,…,Q_n označme
y jeho pravdivostní hodnotu na f(0,x₂,…,x_n) a z hodnotu na
f(1,x₂,…,x_n). Doplnění **vnějšího** Q₁=∃ dává y∨z, doplnění
Q₁=∀ dává y∧z. Kvantifikátory se při tom nepřesouvají.

    (y∨z)+(y∧z)=y+z.

Sečtením přes všechny suffixy dostaneme T(f)=T(f₀)+T(f₁).
Indukční předpoklad dává počty jedniček obou disjunktních polovin
pravdivostní tabulky, jejich součet je právě k. Zahrnuty jsou k=0,
k=2ⁿ, nepodstatné proměnné i nulární případ. To je celý argument
vytištěné odpovědi, bez procházení pravdivostních tabulek programem.

## Errata, primární odkazy a přesný limit pokrytí

Dne 2026-11-07 prohledány relevantní vrstvy `all4a-pre`, `all4a`,
`err4a`, `all4f0`, `all4f1`, podle stran, čísel úloh i témat
Horn/quantified/Dahlheimer/Pehoushek/Fraer. Žádná relevantní oprava
58/59 nalezena. Oprava p545 v all4a-pre se týká citace v 55;
p546 mění 67(a). F0 answer59/p192 jsou hradlové řetězce, F1
answer58/p159–160 přepínací sítě: odlišné sekce, nikoli tato úloha.

Primární vydavatelské stránky potvrzují bibliografii 58:
[Karpinski–Kleine Büning–Schmitt, LNCS 329 (1988), 129–137](https://link.springer.com/chapter/10.1007/3-540-50241-6_34)
a [Kleine Büning–Subramani–Zhao, LNCS 2919 (2004), 93–104](https://link.springer.com/chapter/10.1007/978-3-540-24605-3_8).
Plná placená znění se nečetla; původní přisouzení konkrétního
řešení T. Dahlheimerovi ani historie Pehoushek–Fraer 1997 a
QBF-02, pp.1–16 z 59 se nezávisle neověřily. Jde o výslovné
bibliografické výjimky, nikoli o matematické vstupy do důkazů.
Metadata jsou v `sources/quantified-horn-bibliography.json`.

Obě úlohy 58/59 jsou v celém matematickém rozsahu doloženy.
P87/545/546 nejsou tímto uzavřeny jako celé stránky: obsahují
jiné dosud otevřené položky, včetně slovního rozsahu P0840.
