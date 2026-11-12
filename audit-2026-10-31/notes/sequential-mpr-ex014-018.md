# D117–D121 — celé MPR14–18

6. listopadu 2026. Celá zadání p14/file34 a odpovědi
p372/file392 přímo zobrazeny, také autorův Pre-Fascicle
5A, p14/file20 a p29/file35. Všechny matematické
části níže mají úplný argument. Žádný numerický
běh, nový nález ani restart.

## D117: celé řetězové pravidlo14, včetně nulových prefixů

Pro n≥1 položme G₀=Ω a G_k=A₁∩⋯∩A_k.
První faktor lze chápat jako P(A₁|Ω)=P(A₁).
Pro každý k platí

    P(G_k)=P(G_(k−1)) P(A_k|G_(k−1)).

Je-li P(G_(k−1))>0, jde přesně o podílovou definici
podmínění. Je-li P(G_(k−1))=0, pak G_k⊆G_(k−1)
a P(G_k)=0. Podle výslovné konvence p2 je druhý
faktor P(A_k), tedy je definován v [0,1]; pravá
strana je opět0. Nedělíme nulou.

Základ n=1 je totožnost. Při indukčním přechodu
dosadíme už prokázaný součin pro P(G_(n−1)) do
poslední rovnosti. Po konečných n krocích vznikne
právě vytištěný součin. Nulový prefix je obsloužen
od prvního svého výskytu: předchozí součin už má
hodnotu0 a všechny pozdější definované faktory
jej ponechají0. Nezávislost A_k se nepředpokládá.

Prázdná rodina by měla P(Ω)=1 a prázdný součin1,
ale tištěný zápis s prvním faktorem používá n≥1.
Knižní odpověď „Induction on n“ tím byla skutečně
provedena, nikoli pouze zopakována.

Historická atribuce Thomas Bayes1763 a přesný
odkaz Philosophical Transactions53,370–418,
proof of Proposition6, nejsou v dostupných
lokálních podkladech doloženy. Jsou výslovně
bibliograficky vynechány; matematika je nezávislá.

## D118: celá15 a přesná role nemožného C

Označme c=P(C), b=P(B∩C), d=P(A∩B∩C).

1. Je-li c>0 a b>0, oba podíly existují a

       P(A|B∩C) P(B|C)=(d/b)(b/c)=d/c
          =P(A∩B|C).

2. Je-li c>0 a b=0, pak d=0 z inkluze.
   Druhý faktor je0, první je podle konvence P(A).
   Obě strany jsou0. Knižní „chain rule,
   conditional on C“ je tedy pravdivé i při
   nulové vnitřní větvi B∩C.

3. Je-li c=0, také b=d=0, ale všechny tři
   podmíněné pravděpodobnosti se podle konvence
   vracejí ke svým nepodmíněným hodnotám. Otázka
   je přesně rovnost

       P(A)P(B)=P(A∩B).

   Ta platí právě když A a B jsou nezávislé.
   Převzatý D093 dokazuje také ekvivalenci
   s úplnou nezávislostí obou indikátorů,
   včetně nulových či jistých událostí.

Výrok tedy není univerzálně pravdivý, jak správně
říká odpověď. Například nechť Ω má dva stejně
pravděpodobné body, A=B je jeden z nich a C=∅.
Levá strana je1/4, pravá1/2. Při P(C)=0 a
nezávislých A,B naopak rovnost platí. Obě části
knižního „unless“ jsou tím doloženy přesně.
Vše používá autorovu konvenci, nikoli spor
s neurčeným podmíněním z jiné učebnice.

## D119: celá16 a oba členy vytištěné disjunkce

Události A a C\A jsou disjunktní a jejich sjednocení
je A∪C. Při P(B)>0 je proto přesný rozdíl

    P(A∪C|B)−P(A|B)
      =P(Ā∩B∩C)/P(B).

Rovnost platí právě když čitatel je0. Při P(B)=0
konvence dává místo obou podmíněných pravděpodobností
nepodmíněné, takže rozdíl je P(Ā∩C). Rovnost
v této druhé větvi platí právě když P(Ā∩C)=0.

Spojením větví dostaneme

    (P(B)>0 a P(Ā∩B∩C)=0)
    nebo (P(B)=0 a P(Ā∩C)=0).

Tištěná odpověď uvádí první větev jako
P(Ā∩B∩C)=0≠P(B) a druhou prostě jako
P(Ā∩C)=0. To je ekvivalentní: když druhá
podmínka platí při P(B)>0, její inkluze
Ā∩B∩C⊆Ā∩C už zaručuje první větev.
Proto vypuštění P(B)=0 z druhého členu
disjunkce nepřidává žádný chybný případ.

Nutnost rozlišit nulové B je konkrétní:
A=B=∅, C=Ω dávají podmíněné hodnoty0 a1,
přestože P(Ā∩B∩C)=0. První vytištěný člen
správně vyžaduje P(B)≠0 a druhý zde neplatí.
Naopak pro P(B)>0 není třeba nulová hmotnost
celého Ā∩C; rozhoduje pouze jeho část uvnitř B.
Tím jsou zkontrolovány oba směry a všechny okraje.

## D120: celá17, horní eso při spodní pikové dámě

Převzat původní karetní model z D092:
rovnoměrných52! permutací52 rozlišitelných karet,
z nichž čtyři jsou esa. Důkaz obou okrajových
a společných pravděpodobností je v
`notes/sequential-mpr-001-003.md`, §D092.

Po zafixování B=Q♠ zbývá51! permutací ostatních
karet. Pro každé konkrétní eso a na vrcholu je
50! permutací, a čtyři takové případy jsou disjunktní.
Piková dáma není eso, proto jsou přípustná všechna
čtyři. Pravděpodobnost je

    (4·50!)/51!=4/51.

Ekvivalentně nepodmíněná společná pravděpodobnost
je4/(52·51) a P(B=Q♠)=1/52; jejich podíl je4/51.
Zadání ani odpověď nespoléhají na falešnou nezávislost
horní a spodní karty. Příslušná podmínka má kladnou
hmotnost; konvence nulových událostí se zde neužije.

## D121: celá18, existence momentů a každý algebraický krok

Nechť konečná reálná čísla m≤M omezují X,
m≤X≤M. Proto |X| a X² jsou omezené; všechny použité
střední hodnoty a rozptyl existují. Pišme μ=EX.
Monotónnost očekávání dává m≤μ≤M.

Bodově je M−X≥0 i X−m≥0, tedy

    (M−X)(X−m)=(M+m)X−X²−mM≥0.

Po očekávání přesně jako v odpovědi

    (M EX)−E(X²)+(m EX)−mM≥0,

čili EX²≤(M+m)μ−mM. Odečtení μ² dává

    var X=EX²−μ²
      ≤(M+m)μ−mM−μ²
      =(M−μ)(μ−m).

Každé znaménko a obě závorky jsou tím zkontrolovány.
Argument potřebuje pouze konečné meze, nikoli
kladnost m nebo M; zahrnuje záporné a smíšené
intervaly. Při m=M je X konstantní a obě strany0.
Je-li m<M, rovnost je ekvivalentní nulovému očekávání
nezáporného součinu, tedy X∈{m,M} skoro jistě.
Je-li μ na konci intervalu, jde opět o konstantu.
Tyto případy potvrzují, že mez má správné okraje
a nelze ji obecně striktně zpřísnit.

Knižní předpoklad maxima a minima konečné meze
poskytuje; důkaz ostatně platí i pro dosažené či
nedosažené konečné dolní a horní meze. Netvrdí
rozšíření na nekonečná M,m.

## E120: již zveřejněná bibliografická oprava odpovědi18

Původní PDF i autorův PS odkazují na C. Davis
a R. Bhatia, AMM107(2000),353–356. Ve veřejných
lokálních erratech err4b/all4b je od13. března2026
výslovná oprava koncové strany na357.

Přímo zobrazena původní sazba
`images/sequential/all4b-09.png` a přečten
zdrojový TeX err4b, řádky678–681. E120 je pouze
known_erratum, nikoli náš nález, a nedostává kartu
ani barevnou lokaci v UI.

Samotný článek ani jeho neuvedená zobecnění nejsou
lokálně dostupné a jsou výslovně vynechány. Nejde
o mezeru v dokázané nerovnosti18: její celý důkaz
je předchozí elementární výpočet. Bibliografický
rozsah353–357 evidujeme jako známou opravu, nikoli
jako nezávisle zkontrolovaný fyzický časopis.

## Úplný rozsah checkpointu

D117, D118, D119, D120 a D121 uzavírají vždy celou
MPR14,15,16,17,18 včetně odpovědi a okrajů.
Šest vrstev errat a tři TeX zdroje byly cíleně
posouzeny podle stran, čísel i pojmů. Jedinou
relevantní změnou je E120; ostatní zásahy do
odpovědí14–18 patří jiným oddílům. Doklad:
`results/sequential/mpr-014-018-elementary-errata.json`.

Původní p14/file34 má dokončené14–18 a dříve20;
19 a21–26 zůstávají otevřené. P372/file392 má
dokončené všechny odpovědi kromě19 a otevřeného
kontextu C046 u8, proto obě stránky zůstávají partial.
Původní velké censy a všechny dřívější důkazy
zůstaly převzaté bez nového běhu.
