# Incerpi–Sedgewick: celá konstrukce, věta I a úloha 41

7. listopadu 2026. Původní sazba 91–92/file102–103 a odpověď
627/file638; zadání41 na105/file116. Převzaty již prokázané K
a přesný počet mezer dvou nesoudělných generátorů (P0774–0779).
Nově je níže doložen každý přechod (8)–(10), růst báze,
konstanta ve větě I i prvočíselná limitní konstrukce.

Známé opravy: `sources/insertion-errata-review.json`, všech pět
vrstev. Na92 je správný pravý konec rozsahu(9) přísný a ve větě I
patří N místo n. Odpověď41 má od28.10.2000 faktor1/lnρ,
(k−2)² a exponent−2 u log log N. Sazba opravy zobrazena v
`images/insertion-errata-41-file031.png`. Nejde o nové nálezy.

## P0825: báze existuje, roste a je po dvojicích nesoudělná

Pevně ρ>1. Po již zvolených a₁,…,aₖ₋₁ označ jejich součin P.
Čísla mP+1 jsou libovolně velká a nesoudělná s P; množina
přípustných celých čísel≥ρᵏ je tedy neprázdná a má minimum aₖ.
Definice přímo dává gcd(aᵢ,aⱼ)=1 pro i≠j a aₖ≥2.

Navíc aₖ>aₖ₋₁. Číslo aₖ₋₁ je nově vyloučeno. Každé menší
číslo≥ρᵏ bylo již≥ρᵏ⁻¹ a při předchozím výběru neprošlo
nesoudělností; přidání dalšího dělitele to nemůže změnit.
Tento argument nevyžaduje, aby prahy byly celá čísla.

## P0826: všech deset členů báze a čtrnáct přírůstků

Pro ρ=5/2 jsou přesné dolní celočíselné prahy

    3,7,16,40,98,245,611,1526,3815,9537.

Uvedená aₖ jsou

    3,7,16,41,101,247,613,1529,3821,9539.

Všechna zamítnutá čísla mezi prahem a uvedeným aₖ mají ve
`results/insertion-incerpi-example.json` explicitní gcd>1
s předchozím součinem. U každého přijatého čísla je gcd=1.
Tím je prověřena také **minimalita**, nikoli jen nesoudělnost
tištěných členů. Jeden krátký přesný výpočet s nice15 dále
dosadil do(8), bez generování permutací:

    1,3,7,21,48,112,336,861,1968,4592,13776,33936,86961,198768.

## P0827: uzavřený tvar(8), všechny hranice a monotónnost

Polož Tᵣ=r(r+1)/2, Hᵣ=∏ⱼ₌₁ʳaⱼ, H₀=1. Pro r≥1 platí

    h_(Tᵣ−j)=Hᵣ/aⱼ       (1≤j≤r),
    h_(Tᵣ)=Hᵣ.

Pro r=1 jsou to h₀=1, h₁=a₁. Indukční krok pro
s=Tᵣ₋₁+u, 1≤u≤r, použije s−r=Tᵣ₋₂+u−1:
je-li u<r, předchozí blok dává h_(s−r)=Hᵣ₋₁/a_(r−u);
pro u=r dává Hᵣ₋₁. Násobení aᵣ je přesně(8) a oba uvedené
vzorce. Počátek je tedy 1; a₁; a₂,a₁a₂; a₁a₃,a₂a₃,a₁a₂a₃.

Uvnitř bloku j klesá a aⱼ přísně roste, proto h přísně roste.
Přechod z Hᵣ₋₁ na první nový člen Hᵣ/aᵣ₋₁ má poměr
aᵣ/aᵣ₋₁>1. Neexistují duplicity ani nepřiznaně obrácené
přírůstky. Součet indexů faktorů je vždy s, takže

    hₛ≥ρˢ.                                                    (A)

Toto dolní omezení je přímé a nepoužívá prvočíselnou větu.

## P0828: obě předchozí hodnoty, gcd a celý posloupnostní odhad

Pro Tᵣ₋₂≤s<Tᵣ₋₁ dej j=Tᵣ₋₁−s, tedy 1≤j≤r−1.
Uzavřený tvar a(8) dávají

    h_(r+s)=aᵣhₛ,   h_(Tᵣ₋₁)=aⱼhₛ,
    gcd(h_(r+s),h_(Tᵣ₋₁))=hₛ.

Oba indexy jsou větší než s a navzájem různé: r+s≥Tᵣ₋₁+1.
Čísla aᵣ,aⱼ jsou nesoudělná. To dokazuje celé(9), včetně
nutnosti přísného pravého konce, kde by se objevil neexistující a₀.

Před hₛ-sortem byly oba větší přírůstky použity, pokud jsou<N.
Je-li některý≥N, jeho uspořádání je prázdnou podmínkou a platí
automaticky. Věta K uchovává již dosažená uspořádání. V každé
hₛ-třídě proto platí aᵣ- i aⱼ-uspořádání.

Je-li vzdálenost generovatelná aᵣ,aⱼ, monotónní cesta uvnitř
třídy brání inversi. Z P0779 je počet kladných negenerovatelných
vzdáleností právě b(aᵣ,aⱼ)=(aᵣ−1)(aⱼ−1)/2. Každý pravý
prvek má nejvýše tolik inversí; insertion sort přesune předchozí
záznam právě jednou za inversi. Proto Bₛ≤N b(aᵣ,aⱼ).

Pro r=2,3,4,… a j=r−1,…,1 tak dostáváme přesně všechny řádky(10),
bez nezávislostního nebo průměrového předpokladu.

## P0829: skutečné použití prvočíselné věty

Přebíráme jako explicitní vnější větu

    π(x)=li(x)+O(x exp(−c√ln x)),  c>0,

ověřenou v primárním formálním zdroji Song–Yao a v DLMF27.12.5;
odkazy a rozsah v `sources/insertion-incerpi-pnt.json`. Znovu
neprovádíme analytický důkaz prvočíselné věty ani její formalizaci.
Její aplikaci na **chamtivě zvolenou nesoudělnou bázi** je však
třeba doložit, ne pouze najít nějaké prvočíslo v intervalu.

Pokud prvočíslo p≥ρᵏ dělí některé dřívější aⱼ, pak p bylo při
volbě aⱼ samo přípustné: p≥ρʲ a žádné ještě starší aᵢ není s p
soudělné. Minimalita nutí aⱼ≤p, zatímco p|aⱼ nutí aⱼ≥p;
tedy aⱼ=p. Mezi prvočísly≥ρᵏ je tak nejvýše k−1 zakázaných.

PNT dává v [ρᵏ,ρᵏ⁺¹] počet

    (ρᵏ⁺¹/(k+1)−ρᵏ/k)/lnρ + Oρ(ρᵏ/k²).

Rozdíl otevřených/uzavřených konců je nejvýše2 a je absorbován
zbytkem. Pro pevné ρ>1 je vedoucí člen asymptotický
(ρ−1)ρᵏ/(k lnρ), a proto je nakonec větší než k−1.
Existuje nezakázané prvočíslo a minimalita dává aₖ≤ρᵏ⁺¹.
Po absorbování konečného počtu prvních členů: aₖ=Oρ(ρᵏ).
Opravený faktor1/lnρ je tedy skutečně potřeba, ale pouze známý.

## P0830: význam praktického růstu hₛ≈ρˢ

Dokonce platí ρˢ≤hₛ≤Cρρˢ pro pevné ρ; ≈ zde nevykládáme
jako poměr konvergující k1. Abychom neakumulovali faktor C
jednou za každý člen báze, použijeme silnější, stále přímý
důsledek téže PNT.

Polož x=ρᵏ, δ=k⁻². Počet prvočísel v [x,x(1+δ)] je

    ∫ₓˣ⁽¹⁺δ⁾dt/ln t + Oρ(x exp(−cρ√k))
      ∼ x/(k³ lnρ) > k−1.

Předchozí argument se zakázanými prvočísly dává pro velká k
1≤aₖ/ρᵏ≤1+k⁻². Součin ∏ₖ(aₖ/ρᵏ) proto konverguje
ke konečnému Cρ≥1: logaritmus je nezáporný a ocas omezený
konvergentním součtem∑k⁻². Každý hₛ je podle P0827 součin
různých aₖ, jejichž indexy sečtou na s. Jeho podíl hₛ/ρˢ je
částečný součin těchto poměrů a leží mezi1 a Cρ.

Přesný limit1 by byl jiné tvrzení. Například při ρ=2.5 jsou
podposloupnosti s=Tᵣ a s=Tᵣ−1 asymptoticky Cρ a Cρ/(3/2.5).
Kniha píše≈, nikoli∼; tento rozdíl není hlášen jako chyba.

## P0831: úloha41(a), přesná geometrická suma

Prvních binom(k,2) členů(10) je právě množina všech b(aᵢ,aⱼ),
1≤i<j≤k. Z jednoho uniformního aᵢ≤Cρρⁱ vychází

    ∑ᵢ<ⱼ b(aᵢ,aⱼ) ≤(Cρ²/2)∑ᵢ<ⱼ ρⁱ⁺ʲ = Oρ(ρ²ᵏ),
    ∑₁≤ᵢ<ⱼ≤ₖ ρⁱ⁺ʲ
      =ρ³(ρᵏ−1)(ρᵏ⁻¹−1)/((ρ²−1)(ρ−1)).

Poslední identitu lze ověřit pro k=1 (obě strany0) a odečtením
hodnoty při k−1: v obou případech přibude
ρᵏ∑ᵢ₌₁ᵏ⁻¹ρⁱ=ρᵏ⁺¹(ρᵏ⁻¹−1)/(ρ−1). Pro pevnéρ>1 jsou
oba jmenovatele nenulové konstanty. Tím je doložena i algebra
tištěného mezikroku, nejen řád výsledku.

## P0832: celá věta I, konstanta i režie

Pro N≥2 dej L=logρN. Z(A) plyne, že použitých přírůstků hₛ<N
je T≤ceil L, včetně případu celočíselného L. Zvol k tak, že

    binom(k−1,2)<L≤binom(k,2).

Prvních T nezáporných členů(10) je obsaženo v prvních binom(k,2).
Z P0831 je proto B=Oρ(Nρ²ᵏ). Dále

    (k−2)²≤(k−1)(k−2)<2L,
    ρ²ᵏ≤ρ⁴ exp(√(8 lnρ) √ln N).

To je opravený mezikrok odpovědi41(b), platný i pro k=2.
ProgramD má již prokázaný čas9B+10NT+13T−10S−3A+1.
Nezáporné A,S lze pro horní odhad zahodit; T=Oρ(logN).
Pro každé pevné c=√(8lnρ)>0 je logN=Oρ(exp(c√lnN)), protože
u²e⁻ᶜᵘ je na u≥0 omezená funkce. Režie tedy patří do stejné meze:

    time_D=Oρ(N exp(c√lnN)).

Jde o běh ProgramuD s danou tabulkou přírůstků, stejně jako
v předchozích analýzách. Není zde skrytý odhad času generování
prvočísel. Pro libovolné pevné ε>0 máme c√lnN≤εlnN pro
N≥exp((c/ε)²); tedy čas je Oρ,ε(N¹⁺ε). Konstanta není
uniformní pro ρ→1. Dřívější Prattův O(Nlog²N) má menší
asymptotickou horní mez, neboť (lnN)² exp(−c√lnN)→0.

## P0833: prvočíselná limitní konstrukce a opravený exponent

Pro každé pevné K je při dostatečně malém ρ−1>0 všech K prahů
ρᵏ v(1,2). Nejmenší číslo≥2 nesoudělné s předchozími prvočísly
je další prvočíslo: každé menší složené číslo má již použitý
prvočíselný dělitel. Indukcí tedy konečný prefix a₁,…,a_K
stabilizuje na prvních K prvočíslech. Nejde o substituciρ=1
do definice (ta by dovolila1) ani o uniformní limit věty I.

U samostatné báze aᵣ=pᵣ použijeme stejné součinové vzorce
a gcd důkaz. Pokud ještě proběhne přírůstek z bloku
Tᵣ₋₁≤s<Tᵣ, je jeho minimum Hᵣ₋₁<N. Proto

    lnN>∑ⱼ₌₁ʳ⁻¹ln pⱼ ≥∑ⱼ₌₁ʳ⁻¹ln(j+1)=ln(r!).

Už posledních nejméně r/2 faktorů dává ln(r!)≥(r/2)ln(r/2),
takže r=O(lnN/lnlnN). (Pro velké L=lnN by r≥4L/lnL
porušilo uvedenou nerovnost.) Z pⱼ=O(j ln j), přímého důsledku
PNT, plyne pro všechny použité páry až do indexu r+1

    ∑ᵢ<ⱼ≤ᵣ₊₁ b(pᵢ,pⱼ)
      ≤¼(∑ⱼ≤ᵣ₊₁pⱼ)²=O(r⁴(ln r)²)
      =O((lnN)⁴/(lnlnN)²).

Posun r+1 zahrnuje také oba faktory u posledního neúplného
bloku a nemění odhad. Počet průchodů O(r²) je menší řád.
Celý čas je tedy O(N(logN)⁴(loglogN)⁻²), jak zní oprava2000.
Původní exponent−3 nepřebíráme. Všechny limitní kvantifikátory
jsou tím rozlišeny od pevného ρ>1.

## Stav a výjimky

P0825–0833 jsou uzavřeny s výslovnou vnější závislostí PNT.
Přímý kontrolní výpočet se týkal pouze vytištěných malých čísel.
Žádný nový nález. Bibliografické detaily Incerpi–Sedgewick1985
a1996 nebyly v tomto bloku dohledávány; zde je vlastní důkaz
tvrzení, nikoli potvrzení historického prvenství.

Strana92 pokračuje průměry, porovnáním a extremálními příklady
N=8, proto se tím celá stránka neuzavírá. Stejně zůstává627
partial kvůli dosud neuzavřeným40/42. Další kurzor: praktický
odstavec92 a celá tabulka5 na93, poté94.
