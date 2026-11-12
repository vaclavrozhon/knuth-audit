# Celá úloha 83: vážená služba, monotónnost a efektivní algoritmus

Checkpoint X0105, P0983–P0990. Zadání p91/file108,
odpověď p549–550/file566–567 a detail všech teček nad
operacemi minus v `images/proof83-formula-detail.png`
byly přečteny v originálu. Všechny výpočty níže jsou
obecné algebraické argumenty, žádný program ani census.

Máme ρ>0, u_0=v_0 a minimalizujeme

    Σ_(i=1)^t (d(u_(i−1),u_i)+ρ d(u_i,v_i)).

Na rozdíl od konkrétní optimální volby v82 zde není
předepsáno u_t=v_t; při ρ<1 by to obecně bylo nesprávné.
Vytištěné zadání83 takovou podmínku nepřidává.

## Přesná booleovská DP a omezení rozdílu — P0983

Pro suffix požadavků v_i,...,v_t a předchozí stav a∈{0,1}
definujme jeho minimální cenu J_i(a), s J_(t+1)(a)=0.
Konečná optimalizace dává

    J_i(a)=min_(b∈{0,1})(|a−b|+ρ|b−v_i|+J_(i+1)(b)).

Každá pevná budoucí posloupnost mění při změně a pouze
první pohyb o nejvýše 1. Použitím optimální posloupnosti
z jednoho počátku také v druhém a naopak tedy

    |J_i(1)−J_i(0)|≤1.

Označme D_i=J_i(1)−J_i(0). Cílem není vypočítat dvě
velké ceny, ale pouze tyto rozdíly v intervalu [−1,1].

## Celá zpětná recidiva — P0984

Položme Q_b=ρ|b−v_i|+J_(i+1)(b) a
Δ=Q_1−Q_0=D_(i+1)+ρ(1−2v_i). Z recidivy plyne

    J_i(0)=min(Q_0,1+Q_1),
    J_i(1)=min(1+Q_0,Q_1).

Pro Δ<−1 je jejich rozdíl −1, pro −1≤Δ≤1 je Δ
(a zahrnuje oba hraniční případy), pro Δ>1 je +1.
Proto přesně

    D_(t+1)=0,
    D_i=clip(D_(i+1)+ρ(1−2v_i),−1,1), i=t,...,1.

Všechny operace jsou jediný součet a dvě porovnání;
žádné hledání mezi všemi posloupnostmi není potřeba.

## Optimální selector, všechny rovnosti a první tištěná větev — P0985

Pro předchozí stav a=0 je rozdíl mezi cenou volby 1
a cenou volby 0 roven 1+Δ. Zvolíme tedy 1 právě když
Δ≤−1, což je ekvivalentní D_i=−1. Pro a=1 zvolíme
0 právě když Δ≥1, ekvivalentně D_i=1. V rovnosti je
optimálních více voleb; naše konvence v ní zvolí
opačný stav. Dostáváme funkci

    F_i(0,v_i,...,v_t)=[D_i=−1],
    F_i(1,v_i,...,v_t)=[D_i<1].

Jinak řečeno: pro D_i=−1 zvolíme 1, pro D_i=1 zvolíme
0 a pro −1<D_i<1 ponecháme a. Každá volba dosahuje
minima přesně v DP recidivě, a následná indukce na
délce suffixu dokazuje optimalitu celé přední rekonstrukce.
Jde o f_(t+2−i) z tištěné odpovědi, se správným počtem
argumentů a závislostí na zbývajícím suffixu.

Je-li a=0 a v_i=0, pak Δ≥ρ−1>−1, takže F_i=0,
přesně podle první tištěné větve. Symetrická větev
platí při a=v_i=1. Pro jediný zbývající opačný požadavek
se stav změní právě když ρ≥1; při ρ=1 jde o optimální
rovnost a při ρ<1 se správně zůstane. Pro t=0 není
žádné rozhodnutí a cena je 0.

## Plná monotónnost včetně počátečního argumentu — P0986

Změna některého požadavku v_j z 0 na 1 změní přírůstek
v jeho zpětném kroku z +ρ na −ρ. D_j se tím nezvětší;
clip i všechny další zpětné součty jsou neklesající
funkce svého vstupu, takže se nezvětší ani D_i pro i≤j.
Tím je dokázána souřadnicová nerostoucnost D_i ve všech
budoucích požadavcích, bez předpokladů o jejich bězích.

Na intervalu [−1,1] jsou oba selectory [D=−1] a [D<1]
nerostoucí v D. F_i je tedy neklesající v každém
požadavku. Zbývá samotný počáteční argument a:

| D_i | F_i(0,...) | F_i(1,...) |
|---|---|---|
| −1 | 1 | 1 |
| −1<D_i<1 | 0 | 1 |
| 1 | 0 | 0 |

Ve všech třech řádcích první hodnota nepřevyšuje druhou.
**Celá funkce F_i je monotónní ve všech svých argumentech.**
Tím je doplněn vytištěný „somewhat delicate proof“,
nikoli pouze monotónnost některého cofactoru.

## Selfdualita a přípustnost každého grafového kroku — P0987

Komplementování všech požadavků obrátí znaménko každého
D_i: platí to pro D_(t+1)=0 a pro každý krok, protože
clip je lichá funkce. Z obou explicitních selectorů
plyne

    F_i(1, complement(v_i,...,v_t))
      =[−D_i<1]=1−[D_i=−1]=1−F_i(0,v_i,...,v_t).

Druhá počáteční hodnota plyne stejně či komplementováním
uvedené rovnosti. F_i je self-duální, přesně s tištěnou
konvencí pro první argument 1.

Theorem P nyní říká, že F_i je mediánový term. Aplikace
na prvky libovolné mediánové algebry proto zůstává uvnitř
algebry. Není nutné tento potenciálně velký term skutečně
konstruovat; pro výpočet použijeme krátkou zpětnou recidivu
na štítcích.

Pro grafové štítky P0945 je celková vážená cena součtem
booleovských cen. Každá grafová posloupnost má alespoň
součet jednotlivých booleovských optim. Rekonstrukce
používá F_i na skutečném u_(i−1),v_i,...,v_t, takže
podle předchozího odstavce zůstává vrcholem grafu, a
současně dosáhne booleovského optima v každém bitu.
Součet dolních mezí je tedy dosažen. Tím je doložen
celý grafový závěr i požadovaný optimální algoritmus.

## Vytištěný vzorec s běhy a dotminus — P0988

Zbývá ověřit, že odpověď používá právě tento F. U a=0
je případ v_1=0 už hotový. Jinak nechť požadavky začínají
jedničkovým během, mají k střídavých běhů a jejich délky
jsou a_k,...,a_1≥1, číslované od konce stejně jako v knize.
Pišme x dotminus y=max(0,x−y). Originál má dotminus
**i v posledním výrazu 1 dotminus a_1ρ**.

V jednom běhu se zpětně opakuje přírůstek téhož znaménka.
Proto a_j opakovaných clip kroků je právě jeden krok
clip(D+a_jρσ_j,−1,1), kde σ_j=+1 pro nulový běh,
σ_j=−1 pro jedničkový. Rovnost plyne indukcí: dosažení
meze ve směru přírůstku se dalšími stejnými přírůstky
nemůže zrušit.

Nechť D^(j) je rozdíl na začátku suffixu od běhu j
a E_j=1−σ_j D^(j). Pro poslední běh začínáme D=0,
tedy

    E_1=1 dotminus a_1ρ.

Pro j≥2 je σ_(j−1)=−σ_j a před běhovým přírůstkem
σ_j D^(j−1)=E_(j−1)−1. Jelikož E_(j−1)≥0 a ρ>0,
spodní ořez na −1 se neuplatní; horní ořez dává

    E_j=max(0,2−a_jρ−E_(j−1))
       =(2 dotminus a_jρ) dotminus E_(j−1)
       =α_j dotminus E_(j−1).

Poslední rovnost platí i při a_jρ≥2, kdy jsou oba
výrazy nulové. Každé E_j leží v [0,2]. První běh je
jedničkový, takže σ_k=−1 a E_k=1+D_1. Proto

    F_1(0,v_1,...,v_t)=[E_k=0],

což je přesně celé vytištěné vnoření α_k dotminus
(α_(k−1) dotminus (...(α_2 dotminus (1 dotminus a_1ρ))...)).
Pro k=1 vnoření končí přímo E_1. Důkaz platí pro každý
kladný ρ a všechny délky běhů, včetně všech prahových rovností.

## „Nejvzdálenější“ proměnná: nutnost, nikoli volba tie — P0989

Zpřesníme malé ε v tištěném příkladu na libovolné
0<ε<1/2 a ρ=1−ε. Pro každé k≥2 mají požadavky t=2k
přesný tvar

    11 (01)^(k−2) 0 x,

a počáteční stav je 0. To je argumentový seznam
f_(2k+1)(0,1,1,0,1,0,...,1,0,x) v knize.

Pro x=0 mají první a poslední běh délku 2 a vnitřních
2k−4 běhů délku 1. Poslední E_1=0, protože 2ρ>1.
Krok pro singleton je T(E)=(1+ε) dotminus E, který
střídá 0 a 1+ε. Sudý počet vnitřních běhů vrátí E=0.
Suffix za prvními dvěma jedničkami má proto D=1.
Před první jedničkou je neomezovaný rozdíl

    Δ_1=(1−ρ)−ρ=2ε−1>−1.

Volba 0 je **striktně** levnější než 1, o 2ε.

Pro x=1 je poslední běh singleton, E_1=ε. Vnitřních
2k−3 singletonů je lichý počet; T střídá ε a 1,
a výsledkem před prvním dvojitým během je E=1.
Suffix za jeho dvěma jedničkami má D=0, takže

    Δ_1=−ρ−ρ=−2+2ε<−1.

Volba 1 je **striktně** levnější než 0, o 1−2ε.
Tedy každá optimální první rozhodovací funkce musí
vrátit x; nejde pouze o to, že náš konkrétní selector
tak vyřešil rovnost. Délka suffixu je neomezená při
pevném ρ∈(1/2,1), takže žádný pevný krátký lookahead
v tomto váženém problému obecně nestačí.

## Efektivnost a přesný numerický model — P0990

Pro b souřadnic štítků a t požadavků:

1. V každé souřadnici spočteme t hodnot D_i zpětně.
2. Předním průchodem z daného u_0 použijeme selector
   P0985 při každém i. Hodnoty D_i závisejí jen na
   požadavcích, takže je nerepočítáváme pro každý suffix.

Je to O(tb) přesných aritmetických operací a porovnání,
nikoli O(t²b) opakovaných běhových výpočtů. Lze zpracovat
souřadnice postupně; potřebujeme O(t) pomocných čísel
mimo vstup/výstup a O(tb) bitů pro všechny výstupní štítky.
Přípustnost štítků je dokázána P0987, nikoli ověřována
hledáním nebo backtrackingem.

Pro přesně zadané racionální ρ=p/q>0 škálujeme vše q:
D_i q jsou celá čísla v [−q,q], aktualizovaná přičtením
±p a ořezáním na ±q. Mezivýsledky mají O(log(p+q)) bitů.
Bitová cena je tudíž O(tb log(p+q)) plus čtení/výstup;
všechny prahové rovnosti se rozhodují přesně. Pro obecný
reálný parametr je výše uvedený počet v modelu přesné
reálné aritmetiky, nikoli záruka při zaokrouhlování floatů.
Kniha neurčuje jiný numerický model.

Je-li požadován původní identifikátor vrcholu místo
štítku, lze předem vložit n daných b-bitových štítků
do binárního trie za O(nb) a každému výsledku přiřadit
vrchol v O(b). To nezvětší O(tb) průběžnou cenu a
nepředpokládá konstantní vyhledávání v hash tabulce.
Jednovrcholový graf či t=0 jsou triviální nulové případy.

## Errata, úplnost a další kurzor

Všech pět vrstev errat pro83/549–550 prověřeno. F0 p169,
18.1.2010 obsahuje úplné nové znění odpovědi83; je již
zahrnuto v našem prvním4A dotisku a důkaz výše odpovídá
právě této verzi. Žádný nový nález ani další bibliografický
předpoklad zde není.

Všechny části odpovědi83 jsou nyní uzavřeny: rekurzivní
forma, nutná závislost na posledním bitu, obě první větve,
všechny běhové/dotminus operace, selfdualita, monotónnost,
přenos na graf a efektivnost. Celá p549 má tedy argumenty
pro78 P0958,79 P0959–P0963,80 P0973–P0976,81 P0945,
82 P0977–P0982 a začátek83 P0983–P0990. P550 zůstává
partial od84; samotné dokončení83 ji nepovyšuje.
