# D156–D159 — MPR54–57: trojúhelníky v náhodném grafu

7. listopadu 2026. Původní zadání p16/file36 a odpovědi
p378/file398 přímo zobrazeny; také autorův PS p16/file22
a p35/file41. Všech šest vrstev errat a tři TeX soubory
byly posouzeny podle stran, úloh a obsahu. Žádná relevantní
oprava nebo nový rozpor. První, druhý a podmíněný momentový
princip se přebírají z úplných D147–D152.

V55 jsou přesně vymezeny tři povolené výpočetní výjimky:
dva velké počty a historická velikost BDD nebyly nezávisle
reprodukovány. Jejich označení reviewed níže znamená
posouzený rozsah s touto výslovnou výjimkou podle
completion_criteria ve full-review.json, nikoli důkaz
pravdivosti těchto tří empirických údajů.

## 54(a): první moment a přesná událost

Nechť n≥0 je celé a každý z binom(n,2) možných hranových
indikátorů je nezávislý bit s parametrem p∈[0,1].
Pro každou trojici A vrcholů je W_A součin indikátorů
jejích tří různých hran, tedy indikátor její úplnosti.
Nezávislost hran dává E W_A=p³. Proto pro

    X=∑_|A|=3 W_A,      m=binom(n,3),

platí E X=mp³. Jde o nezápornou celočíselnou proměnnou
a graf obsahuje trojúhelník právě tehdy, když X>0.
První momentový princip tedy dává

    P(X>0)≤mp³.

Mez může být větší než1; i tehdy je platná, pouze slabá.
Lze ji samozřejmě nahradit min(1,mp³), ale to nemění
kontrolovaný tištěný výrok.

## 54(b): každý člen druhého momentu

Rozvoj X² je součet W_AW_B přes uspořádané dvojice
trojic. Nejde o součet přes neuspořádané dvojice.
Rozdělme je podle s=|A∩B|:

| s | společných hran | hran ve sjednocení | počet uspořádaných dvojic |
|---|---|---|---|
| 3 | 3 | 3 | binom(n,3) |
| 2 | 1 | 5 | 12 binom(n,4) |
| 1 | 0 | 6 | 30 binom(n,5) |
| 0 | 0 | 6 | 20 binom(n,6) |

Každý koeficient má úplný výklad:

- Pro s=3 je A=B a vybírá se jedna trojice.
- Pro s=2 zvolíme čtyři vrcholy. Na nich je šest možností
  společné hrany a dva způsoby, jak zbývající dva vrcholy
  přiřadit první a druhé trojici. Dostáváme6·2=12.
  Tištěný příklad W_{uvw}W_{uvw′} představuje společnou
  hranu uv; ostatní volby společné hrany a pořadí dávají
  všechny zbývající členy. Každý součin žádá pět hran,
  nikoli šest, protože společná binární hrana se nesčítá
  ani nezvyšuje na novou nezávislou kopii.
- Pro s=1 zvolíme pět vrcholů, společný vrchol pěti
  způsoby a další dva vrcholy první trojice šesti způsoby.
  Druhá trojice je určena zbytkem. Tedy5·6=30.
- Pro s=0 zvolíme šest vrcholů a první trojici dvaceti
  způsoby; druhá je její doplněk. Tedy20.

Každá dvojice patří právě do jednoho řádku a je v něm
spočtena právě jednou. Nezávislost různých hran proto dává

    E X² = m p³ +12 binom(n,4)p⁵
                 +30 binom(n,5)p⁶+20 binom(n,6)p⁶.       (A)

To je celý tištěný jmenovatel. Pro n≥3 a p>0 je kladný
a druhý momentový princip dává

    P(X>0) ≥ (mp³)²/(E X²).                            (B)

Při n<3 nebo p=0 je X=0 jistě a pravděpodobnost0
se určí přímo; výraz0/0 se nepoužívá. Pro n=3 je
X jediný indikátor a dolní i horní mez jsou přesně p³.
Pro p=1 a n≥3 počítají čtyři řádky dohromady všech m²
uspořádaných dvojic, takže(B) je přesně1. Všechny součty
jsou konečné; nevyžadují další momentové předpoklady.

## 55: obě číselné meze přesně

Pro n=10 máme binom(n,3)=120, binom(n,4)=210,
binom(n,5)=252 a binom(n,6)=210. Tedy

    E X=120p³,
    E X²=120p³+2520p⁵+11760p⁶
         =120p³(1+21p²+98p³).

Pro p>0 je dolní mez

    L(p)=120p³/(1+21p²+98p³).

Oba případy vycházejí přesně:

| p | E X | E X² | L(p) |
|---|---|---|---|
| 1/2 | 15 | 555/2 | 30/37 |
| 1/10 | 3/25 | 981/6250 | 10/109 |

Nezávislá krátká racionální kontrola v
verify_mpr054_057_bounds.py trvala0.000338s, nice15.
Počítá jen tyto dva zlomkové případy a porovnání čísel;
neobsahuje výčet grafů ani konstrukci BDD. Výsledek je
results/sequential/mpr-054-057-bounds-arithmetic.json.

Také všechny tištěné desetinné aproximace mají správné
zaokrouhlení na tři desetinná místa. Přesné intervaly jsou

    1621/2000 < 30/37 < 1623/2000,             tedy .811,
     183/2000 < 10/109 < 185/2000,             tedy .092.

Dva velké tištěné zlomky označme

    q₁ = 35165158461687 / 2⁴⁵,
    q₂ = 4180246784470862526910349589019919032987399
                                      / (4·10⁴³).

Jako čísla splňují

    1997/2000 < q₁ < 1999/2000,               tedy .999,
     209/2000 < q₂ <  211/2000,               tedy .105,
    30/37 < q₁ < 15,       10/109 < q₂ < 3/25.

Výsledek ukládá kladné celočíselné rozdíly po křížovém
násobení pro každé zaokrouhlení. Toto je kontrola
aritmetiky tištěných zlomků. Sama **nepotvrzuje**,
že q₁ a q₂ skutečně jsou pravděpodobnostmi grafové události.

### Převod generujícího polynomu a metoda BDD

Počet booleovských proměnných je přesně binom(10,2)=45.
Je-li g_j počet označených grafů s j hranami obsahujících
trojúhelník, pak

    G(z)=∑_{j=0}^{45}g_j z^j,
    P(X>0)=∑_{j=0}^{45}g_j p^j(1−p)^{45−j}
          =(1−p)⁴⁵ G(p/(1−p))                     (p<1).   (C)

Každý konkrétní graf s j hranami má díky nezávislosti
pravděpodobnost p^j(1−p)^{45−j}; grafy jsou disjunktní
výsledky, což dokazuje obě rovnosti. Pro p=1 se používá
první konečný součet, nikoli nedefinované dosazení do
druhého zápisu. V daném příkladu jsou krajní hodnoty
P₀=0 a P₁=1.

Původní reference §7.1.4–25 ve4A byla zobrazena na
p260/file277 a odpověď p624/file641. Obsahuje právě
požadovanou úpravu BDD. Její potřebný argument:

Proměnné mají pevné pořadí1,…,M (zde M=45), terminály
úroveň M+1. Pro terminály nastavme P_false=0,P_true=1.
Má-li uzel v úroveň i a potomky a,b na úrovních j,k>i,
položme

    P_v=(1+z)^{j−i−1}P_a
                     +z(1+z)^{k−i−1}P_b.                (D)

Invariant: P_v počítá přijímaná přiřazení proměnných
od úrovně i včetně, s vahou z za každou jedničku.
Nulová a jedničková větev jsou disjunktní; druhá přidá
faktor z. Přeskočené proměnné jsou volné a každá má
součet vah1+z. To dokazuje(D) i rozdílné délky přeskočení.
Před kořenem na úrovni i₀ se přidá faktor(1+z)^{i₀−1}.
Pro terminální kořen to dává správně0 nebo(1+z)^M.

Zpracování od vyšších úrovní k nižším končí, protože BDD
je konečný a každý potomek má přísně vyšší úroveň.
Každý uzel se vyhodnotí jednou. Při naivních operacích
s polynomy stupně≤M je cena O(M²s) aritmetických operací
a prostor O(Ms) koeficientů pro s uzlů. To dokazuje
možnost přesného výpočtu z daného správného BDD;
**nedokazuje** konkrétní velikost nebo výsledek
nepředloženého BDD.

### Výslovně povolené neprovedené reprodukce

V lokální starší evidenci se nenašel důkaz těchto tří
konkrétních údajů. Původní PDF i autorův PS je uvádějí
shodně. Nový výčet prostoru2⁴⁵ grafů ani budování
milionového BDD nebyly spuštěny. Podle výslovného
uživatelského povolení vynechat dlouhý brute force
zůstávají jako **verified:false**:

1. Skutečná hodnota q₁ pro p=1/2.
2. Skutečná hodnota q₂ pro p=1/10.
3. Historický údaj přibližně1.4milionu uzlů odpovídajícího BDD.

Argumenty pro meze, jejich přesné číselné hodnoty,
generující převod(C) a BDD invariant(D) jsou úplné.
Žádný z těchto důkazů se nevydává za reprodukci tří
výše uvedených empirických údajů.

## 56: asymptotické meze

Nechť λ≥0 je pevné konečné číslo a p=λ/n; pro všechna
dostatečně velká n je p∈[0,1]. Položme μ=λ³/6.
První moment je

    E X = μ(1−1/n)(1−2/n) → μ.

V(A) mají další tři členy postupně limity

    12 binom(n,4)(λ/n)⁵ = O(1/n) →0,
    30 binom(n,5)(λ/n)⁶ = O(1/n) →0,
    20 binom(n,6)(λ/n)⁶ →λ⁶/36=μ².

To plyne přímo z binom(n,r)=n(n−1)…(n−r+1)/r!;
nejde o předpoklad nezávislosti trojúhelníkových indikátorů.
Proto E X²→μ+μ². Pro λ>0 dostáváme limity horní a dolní
meze μ a μ²/(μ+μ²)=μ/(1+μ), přesně jak je vytištěno.
Pro λ=0 je vždy X=0 a obě meze0; tento kraj se neřeší0/0.

## 56: celý dodatek o skutečné limitě

Dokažme přímo v modelu nezávislých hran, že

    P(X>0) → 1−e^{−μ}.                                (E)

Pro pevné r≥1 označme S_{r,n}=E binom(X,r), součet
pravděpodobností průniků přes všechny r-prvkové množiny
různých trojúhelníků. Pro λ=0 je(E) již vyřešeno.
Předpokládejme λ>0.

### Disjunktní vrcholy

Počet kolekcí r vrcholově disjunktních trojúhelníků je

    (n)_{3r}/(6^r r!),

kde (n)_{3r}=n(n−1)…(n−3r+1). Dělíme6 za každé pořadí
tří vrcholů uvnitř trojúhelníku a r! za pořadí
trojúhelníků. Žádné další identifikace nejsou.
Společně vyžadují přesně3r různých hran, takže jejich
příspěvek konverguje k

    (n)_{3r}/(6^r r!)·(λ/n)^{3r} → μ^r/r!.

### Všechny překrývající se kolekce

Pro každou pevnou kolekci vezměme graf sjednocených hran
a jeho počty v vrcholů, e hran. Propojené komponenty
trojúhelníků tvoříme podle sdílení vrcholu. Každá
komponenta s jediným trojúhelníkem má e=v=3.

V komponentě s alespoň dvěma různými trojúhelníky je
lze seřadit tak, že každý další sdílí vrchol s předchozím
sjednocením (například postupem po spojitém grafu jejich
průniků). První má e−v=0. Pokud další sdílí s dosavadním
sjednocením s vrcholů, přibudou3−s vrcholy:

- s=1: přibudou3 hrany a2 vrcholy, tedy e−v vzroste o1.
- s=2: přibudou alespoň2 hrany a1 vrchol, tedy e−v vzroste
  alespoň o1.
- s=3: nepřibude vrchol a počet hran se nesníží.

Druhý různý trojúhelník nemůže mít s=3 vzhledem k prvnímu:
na stejné trojici vrcholů je jediný trojúhelník. Proto
už po druhém máme e−v≥1 a později se nesníží.
Každá nedisjunktní kolekce tedy má celkově e≥v+1.

Pro pevné r existuje jen konečně mnoho průnikových vzorů
na nejvýše3r vrcholech. Vzor s v vrcholy má O_r(n^v)
označených realizací, každá s pravděpodobností(λ/n)^e.
Protože e≥v+1, jeho příspěvek je O_{r,λ}(1/n).
Konečný součet všech takových vzorů jde k0. Máme tedy
pro každé pevné r přesně

    S_{r,n} → μ^r/r!.                                  (F)

Nezaměňujeme tento bodový limit v r za uniformní
konvergenci nekonečného součtu.

### Přesné oboustranné sevření

Pro celé x≥1 a m≥1 platí Pascalovým vztahem
a teleskopickým součtem

    ∑_{r=0}^m(−1)^r binom(x,r)=(−1)^m binom(x−1,m),

s nulovými binomickými členy mimo přirozený rozsah.
Pro x=0 je každý člen r≥1 nulový. Proto pro každé j≥1
platí bodově, a tedy i po zprůměrování,

    ∑_{r=1}^{2j}(−1)^{r+1}S_{r,n}
       ≤ P(X>0)
       ≤ ∑_{r=1}^{2j−1}(−1)^{r+1}S_{r,n}.              (G)

To je přesně potřebná obecná vlastnost inkluze a exkluze.
Původní odkaz4A §7.2.1.4–(48), p401/file418, byl
zobrazen; jeho okolní asymptotika rozkladů se nepřebírá.

Pro pevné j lze do obou konečných součtů(G) dosadit(F).
Obě výsledné posloupnosti konečných exponenciálních
součtů jdou při j→∞ k1−e^{−μ}, protože
∑_{r≥0}μ^r/r! konverguje. Pro každé ε>0 tedy nejprve
zvolíme dostatečné j a potom n, což sevře liminf
i limsup P(X>0) v ε-okolí stejného čísla. Tím je(E)
úplně dokázáno bez výměny dvou nezdůvodněných limit.

### Bibliografický odkaz

[Původní článek Erdőse a Rényiho](https://static.renyi.hu/~p_erdos/1960-10.pdf)
byl uložen a přímo prohlédnut na p17,34–36,61;
§3 skutečně obsahuje větu3a o limitním počtu cyklů.
Pracuje s pevným počtem N∼cn hran, takže pro trojúhelníky
má parametr(2c)³/6. Výše uvedený důkaz nezávislých hran
řeší aplikaci v naší úloze samostatně; obecné tvrzení
o zaměnitelnosti modelů se nepředpokládá.
Ročník5 a rozsah17–61 souhlasí s originálem, rok1960
s [bibliografickým záznamem Zentralblatt](https://ftp.gwdg.de/pub/EMIS/classics/Erdos/cit/10316301.htm).
Obsah přehledu jiných vět z článku ani celý původní
důkaz Poissonova zákona se zde neuzavírá. Pro potřebný
knižní odkaz nezůstává bibliografická výjimka.

## 57: každá podmíněná pravděpodobnost a rovnost obou mezí

Pro n≥3 a p>0 podmiňme na úplnost pevné trojice A.
Tři hrany uvnitř A jsou jisté; všechny ostatní hranové
bity zůstávají nezávislé s parametrem p. Pro trojici B
s t=|A∩B| je binom(t,2) jejích hran už jistých, a tedy

    P(W_B=1 | W_A=1)=p^{3−t(t−1)/2}.

Možných B je přesně binom(3,t)binom(n−3,3−t):
vybereme její průnik s A a zbytek z doplňku, jednoznačně.
Všechna t dávají následující úplný součet:

| t | počet | podmíněná pravděpodobnost |
|---|---|---|
| 0 | binom(n−3,3) | p³ |
| 1 | 3 binom(n−3,2) | p³ |
| 2 | 3(n−3) | p² |
| 3 | 1 | 1 |

Označme jeho hodnotu D. Je stejná pro každé A, je≥1
a je právě tištěným jmenovatelem. Nerovnost(24) dává

    P(X>0)≥m p³/D,                                    (H)
    D=binom(n−3,3)p³+3 binom(n−3,2)p³+3(n−3)p²+1.

Nulové binomické koeficienty pro malé n≥3 se jednoduše
vynechají. Pro p=0 dá(H) přímo0/1=0; není tím tvrzena
identita D=E(X|W_A=1) na nemožném podmínění. Pro n<3
je opět událost nemožná a výsledek0 se určí přímo.
Pro n=3 je D=1 a mez přesná p³. Pro p=1 součet
počítá všech m trojic, tedy D=m a mez je1.

Poslední tištěný dodatek o shodě obou metod není jen
číselná shoda. Dvojím počítáním nebo úpravou faktoriálů:

    m·3(n−3)=12 binom(n,4),
    m·3 binom(n−3,2)=30 binom(n,5),
    m·binom(n−3,3)=20 binom(n,6).

Proto mp³D je přesně(A). Je-li mp³>0, platí

    mp³/D = (mp³)²/(E X²).

Nulový případ jsme vyřešili přímo u obou metod.
Podmíněná metoda je zde tedy **stejná mez**, přestože
obecně z D152 poskytuje alespoň tak silný odhad.

## Přesný uzavřený rozsah

54,56 a57 jsou celé důkazově ověřeny, včetně každého
tištěného mezikroku a dodatku.55 má úplné argumenty,
číselné meze a aritmetiku; tři empirická tvrzení mají
výslovně povolené vynechání reprodukce a verified:false.
Není zde nový nález ani kandidát. Jediný nový numerický
běh byl výše popsaný0.000338s výpočet dvou zlomkových
případů; žádný census, restart nebo opakování staré kontroly.

File36 má nyní všechny41–57 posouzené s dřívějšími
bibliografickými výjimkami a s výpočetní výjimkou55.
File398 zůstává partial pro58–59.

