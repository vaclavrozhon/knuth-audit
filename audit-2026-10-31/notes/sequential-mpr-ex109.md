# MPR109: konečný uspořádaný coupling a každý řezový krok

7. listopadu 2026. Zadání p22/file42, odpověď p386/file406,
autorský PS11.9.2019 p22/file28 a p43/file49 přímo zobrazeny.
Zvětšené výřezy původní sazby `mpr109-answer-detail.png` a
`mpr109-ps-detail.png` potvrzují oba níže uvedené lokální problémy.
Všech šest vrstev errat a tři TeX zdroje bez jejich opravy.
Hlavní tvrzení zadání je pravdivé; žádná numerická kontrola se
nepoužívá jako náhrada důkazu a žádný nový běh nebyl proveden.

## Podmínky a všechny části(a)

P je konečný neprázdný částečně uspořádaný prostor. Značka≼
je reflexivní, antisymetrická a tranzitivní; prvky lze očíslovat
1,…,n bez tvrzení, že číselné pořadí je jeho uspořádáním.
p_i,q_i≥0 a oba součty jsou1. Pro A⊆P definujeme
A↑={x:∃a∈A,a≼x}, pro B⊆P pak B↓={x:∃b∈B,x≼b}.
Zadaná podmínka je p(A↑)≤q(A↑) pro každé A. Každý horní
uzávěr je horní množina; každá horní množina U má U=U↑
reflexivitou a tranzitivitou. Podmínka tedy přesně znamená
p(U)≤q(U) pro všechny horní množiny U.

Coupling je matice c_ij≥0 s řádkovými součty p_i a sloupcovými
q_j. Podle již doloženého diskrétního modelu107 lze její kladné
položky vzít jako atomy. Nerovnost X≼Y ve všech atomech znamená
c_ij=0, kdykoli i není≼j. Takový coupling nutně splňuje zadanou
podmínku: X∈U a X≼Y implikuje Y∈U pro každou horní U.

Pro(a), P={1,2,3},1≺3,2≺3, jsou všechny horní množiny
∅,{3},{1,3},{2,3},P. Jejich podmínky jsou právě

```
0≤0,
p3≤q3,
p1+p3≤q1+q3,
p2+p3≤q2+q3,
1≤1.
```

Tím je doložen celý tištěný seznam, včetně trivialit. Povolené
dvojice jsou(1,1),(1,3),(2,2),(2,3),(3,3); zakázané tedy
c12,c21,c31,c32. Poslední dvě netriviální nerovnosti dávají
p2≥q2 a p1≥q1. Konkrétní splňující coupling je

```
[q1   0    p1−q1]
[0    q2   p2−q2]
[0    0    p3   ].
```

Všechny položky jsou nezáporné, řádky mají součty p a třetí
sloupec má součet1−q1−q2=q3. To také přímo řeší existenci
v tomto speciálním případě, nejen zapisuje podmínky.

V předchozí108, omezené na řetězec1<2<3, jsou horní množiny
jen∅,{3},{2,3},P. Dostáváme dvě netriviální nerovnosti
p3≤q3 a p2+p3≤q2+q3. Přibývá povolená dvojice(1,2), takže
vynucené nuly jsou pouze c21,c31,c32. Přesně to uvádí srovnání
v odpovědi; existence na řetězci je nezávisle pokryta D206.

##(b): každý komplement a směr nerovnosti

Množina L=B↓ je dolní. Její doplněk A=P\L je horní:
pokud x∈A,x≼y a y∈L, pak y≼b pro jisté b∈B a tranzitivita
by dávala x≼b, tedy x∈L, spor. Proto A=A↑ a předpoklad dává
p(A)≤q(A). Odečtením od1 dostáváme

```
p(B↓)=1−p(A)≥1−q(A)=q(B↓).
```

Tím je doložen každý tištěný krok(b). Platí také B∅ a B=P;
nikde se nedělí pravděpodobností, takže nulové váhy nevadí.

##(c): přesná síť a plný konečný max-flow argument

Použijeme2n+2 různých vrcholů s,x_1,…,x_n,y_1,…,y_n,t.
Hrana s→x_i má kapacitu p_i, hrana y_j→t kapacitu q_j.
Pro každou povolenou dvojici i≼j ponecháme hranu x_i→y_j
s kapacitou2; ostatní prostřední hrany odstraníme. Kapacita2
je zvolena jen jako konečné číslo větší než celý požadovaný
tok1. Tok hodnoty1 automaticky nasytí všechny krajní hrany,
protože jejich kapacity se na každé straně sčítají na1.
Zákon zachování pak dává požadované řádkové a sloupcové součty
prostředních toků c_ij. Obráceně každý povolený coupling definuje
tok hodnoty1. To dokazuje celou korespondenci zmíněnou v zadání.

Úloha výslovně dovoluje použít max-flow min-cut větu. Aby nebyl
odkaz na §7.5.3 neověřenou matematickou závislostí, zde je důkaz
právě potřebné konečné verze pro libovolné reálné kapacity.
Množina přípustných toků je neprázdná(nulový tok), uzavřená
a omezená v konečně rozměrném prostoru; lineární hodnota toku
tedy dosahuje maxima v. Pokud by v<1, vezměme reziduální síť
maximálního toku: dopředná hrana má reziduum kapacita−tok,
zpětná hrana tok, ponechávají se pouze kladná rezidua.

Nemůže existovat reziduální cesta s→t, protože minimum jejích
konečně mnoha kladných reziduí je kladné a zvýšení o toto minimum
zvětší hodnotu toku. Nechť S jsou reziduálně dosažitelné vrcholy
ze s. Pak s∈S,t∉S; každá původní hrana z S ven je nasycená
a každá hrana zvenku do S má nulový tok. Sečtení zákonů zachování
ve všech vnitřních vrcholech S dává v rovné součtu kapacit hran
z S ven. To je požadovaná rovnost maxima a kapacity tohoto řezu.
Netvrdíme ukončení libovolného postupného augmentačního algoritmu
pro iracionální kapacity; existence maxima byla dokázána kompaktností.

Protože v<1, tento řez nemůže procházet prostřední hranou kapacity2.
Položme I={i:x_i∉S},J={j:y_j∈S}. Každá povolená prostřední
hrana tedy splňuje i∈I nebo j∈J; jinak by vedla z S ven.
Řez má kapacitu přesně Σ_(i∈I)p_i+Σ_(j∈J)q_j<1.
V naší třívrstvé síti jsou všechny s–t cesty tvaru
s→x_i→y_j→t. Podmínka, že každá je blokována krajní hranou
z I nebo J, je tudíž právě

```
i≼j ⇒ i∈I nebo j∈J.
```

Obráceně jakákoli taková dvojice s kapacitou<1 znemožňuje
coupling: každá jeho kladná položka je pokryta vybraným řádkem
nebo sloupcem, takže jeho celková hmotnost je nejvýše
Σ_(i∈I)p_i+Σ_(j∈J)q_j<1. Tím je prokázána přesná ekvivalence
max-flow podmínky, kterou zadání používá, včetně nulových kapacit.

## Opravený řezový důkaz a F172

Pro libovolnou blokující dvojici(I,J) definujme správně

```
A=(P\J)↓={x:∃a∉J,x≼a}, B=P\A.
```

Pokud x∈A, existuje a∉J s x≼a; blokovací podmínka nutí x∈I.
Proto A⊆I. Reflexivita dává P\J⊆A a tedy B⊆J. Dále
A=A↓ a B=B↑. První z těchto rovností dovoluje použít(b):
p(A)≥q(A). Každý krok celého řetězce je proto platný:

```
Σ_(i∈I)p_i+Σ_(j∈J)q_j
 ≥ Σ_(i∈A)p_i+Σ_(j∈B)q_j
 ≥ Σ_(i∈A)q_i+Σ_(j∈B)q_j =1.
```

První nerovnost používá obě inkluze a nezáporné váhy, druhá
část(b), rovnost disjunktní rozklad P=A∪B. Žádný blokující
pár tedy nemá kapacitu<1 a předchozí síťový důkaz dává coupling
podporovaný pouze na i≼j. Celá hlavní věta je tím dokázána.

F172: původní sazba místo dolního uzávěru používá
A=(P\J)↑, tj. x≽a, a uvádí B=B↓. Poslední rovnost je pro
takto chybnou volbu A sama pravdivá, ale nerovnost p(A)≥q(A)
má opačný směr než předpoklad o horních množinách. Přesný svědek:
P={1<2},p=(3/4,1/4),q=(1/4,3/4),I=P,J={1}. Všechny horní
nerovnosti platí (jediná netriviální je1/4≤3/4), blokování
platí díky I=P. Tisk dává A={2},B={1}, tedy řetězec

```
5/4 ≥ 1/2 ≥ 1,
```

jehož druhá nerovnost je nepravdivá. Také obecná tištěná inkluze
A⊆I může selhat: pro stejné P, I={1},J={2} je dvojice blokující,
ale (P\J)↑=P není podmnožinou I. Oprava směru uzávěru vyžaduje
upravit i navazující vysvětlení na A=A↓ nebo B=B↑. Jde o jeden
lokální problém volby množiny v důkazu; existence couplingu platí.

## F171: odlišná chyba označení prostřední hrany

Předchozí oprava předpokládá, že síť má jen povolené prostřední
hrany. Tisk však přikazuje odstranit x_i→x_j, když i není≼j.
Takové hrany v síti ze zadání vůbec nejsou; musí jít o x_i→y_j.
Pro P={1<2},p=q=(1/2,1/2) splňují všechny horní množiny podmínku
s rovností. Po odstranění neexistujících xx hran zůstává povolen
tok c12=c21=1/2,c11=c22=0. Má správné marginály a hodnotu1,
ale X2,Y1 nastává s pravděpodobností1/2, tedy není uspořádaný.
Přepsání cílového x_j na y_j zajistí zamýšlenou síť; hlavní
existence zůstává pravdivá (například diagonální coupling).
Tento index je odlišný od špatného směru uzávěru F172.

## Přesný bibliografický rozsah

[Vydavatelský záznam Nawrotzkiho článku](https://onlinelibrary.wiley.com/doi/10.1002/mana.19620240306)
potvrzuje autora, Mathematische Nachrichten24(1962),193–200.
Původní první strana byla stažena a přímo zobrazena; název a úvod
se skutečně týkají monotónního spojení náhodných bodových posloupností.
[Archivní obsah časopisu IMS pro Strassena](https://www.jstor.org/stable/i312822)
potvrzuje V. Strassen, The Existence of Probability Measures with
Given Marginals, Annals of Mathematical Statistics36(1965),423–439.

Výslovně vynechané bibliografické části, bez matematické závislosti:

- Celý historický rozsah Nawrotzkiho důkazu na193–200; rychle
  dostupná byla původní první strana a vydavatelská metadata.
- Celý historický rozsah Strassenova článku423–439; Project Euclid
  vracel servisní kontrolu a přímý požadavek nevrátil PDF. Žádný
  neplatný PDF soubor nebyl uložen a přístup se dále neobcházel.
- Samotné umístění/rozsah odkazu na §7.5.3 nebylo nezávisle
  prohlédnuto; přesná konečná věta, kterou zde zadání explicitně
  formuluje, má úplný vlastní důkaz výše.

Celá109(a–c), každý mezikrok i hlavní existence jsou checked
s lokálními F171/F172 low. Bibliografické výjimky jsou oddělené;
nepokrývají neprokázanou matematiku. Nezávislá revize koordinátora,
prvenství nebo fyzický výtisk se netvrdí. Nové výpočty0, restarty0.
