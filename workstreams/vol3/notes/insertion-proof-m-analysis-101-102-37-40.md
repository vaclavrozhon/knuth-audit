# §5.2.1: celá analýza M101–102 a37–40

2026-11-07. P0910–0926. Originály101/file112,104/file115,
105/file116 a626–627/files637–638 zobrazeny. Použity známé opravy:
průměrný čas v38, správné faktorové koeficienty37 a index NM(2000).
PDF errat31 zobrazen. Nejsou nálezy. Nový C0026low se týká pouze
dvou číselných koeficientů po spojování na101; obecný postup třídí správně.
Malé přímé racionální dosazení tří parametrů je v
`results/multiple-list-coefficients.py/.json`, spuštěno s nice15.
Žádná simulace, náhodné vstupy či enumerace.

## P0910–0911: oba podmíněné průměry a všechny kroky(15)–(17)

P0900/P0906 stanovily iid výběr intervalů a rovnoměrné relativní
pořadí různých klíčů v každém intervalu. Obsazení pevné buňky X je
Bin(N,1/M). Původní důkazy maxim/inversí dávají E(A_j|X=n)=H_n,
E(B_j|X=n)=binom(n,2)/2, s H₀=0. Podmínění a součet přes M
stejně rozdělených buněk tedy dávají přesně(15),(16). Nezávislost
jejich velikostí se nevyžaduje a také neplatí.

Identita binom(N,n)binom(n,2)=binom(N,2)binom(N−2,n−2)
počítá výběr n-prvkové množiny a označené dvojice v ní v obou pořadích.
Pro N≥2 po vytažení p², p=1/M, zbytek součtu(16) je úplný binomický
součet(p+(1−p))^(N−2)=1. Dostáváme

    E B=binom(N,2)/(2M).

N=0,1 mají B=0 přímo. Alternativně každá původní dvojice je ve stejném
intervalu s pravděpodobností1/M a pak v inverzi s pravděpodobností1/2.
Odkaz1.2.6-(20) nepřidává neověřenou podmínku: potřebná instance
identity je zde samostatně dokázána.

## P0912–0913: celý harmonický transformát a ostrý rozsah zbytku

Položme q=1−1/M. Geometrická suma dává
H_n=∫₀¹(1−x^n)/(1−x)dx. Je to konečný součet; pro X binomické lze
bez otázky konvergence zaměnit očekávání a integrál. Substituce t=q+x/M
pak dává

    E H_X=∫_q^1 (1−t^N)/(1−t)dt
         =Σ_(k=1)^N(1−q^k)/k
         =H_N−ln M+Σ_(k>N)q^k/k.                         (A)

Poslední krok používá absolutně konvergentní −ln(1−q)=Σ q^k/k,
0≤q<1. Po vynásobení q^(−N) pro M>1 je to přesně transformát
citovaný na101 jako Theorem1.2.7A, včetně jeho levé strany
Σ binom(N,n)(M−1)^(−n)H_n. Nemusíme importovat celou externí větu.

Pro M>1 je ε=Σ_(k>N)q^(k−N)/k kladné a

    ε < (1/(N+1)) Σ_(r≥1)q^r = (M−1)/(N+1).

Nerovnost je striktní, protože členy r≥2 jsou kladné a jejich
jmenovatel je větší. Proto δ=M q^N ε splňuje přesně(18):

    E A=M(H_N−ln M)+δ,
    0<δ<M²q^(N+1)/(N+1).                                (B)

Pro dříve oddělený M=1 platí E A=H_N,δ=0; transformát s(M−1)^(−n)
se na tento degenerovaný případ vůbec nedosazuje. Nejde o novou chybu
strictních mezí uvnitř výpočtu, který již vyžaduje M>1.
Pro pevné M>1 je δ exponenciálně malé. Při M=N/α je horní mez
řádu N e^(−α)/α²: je stejně velkého řádu jako výsledek. Samotné
zanedbání δ proto nedá správný lineární koeficient; to přesně
vysvětluje přechod knihy k úloze40.

## P0914: všechna minima a maxima(19)

P0904 doložil skutečnou cenu T=7B+31N−3A+4M+2. Pro buňku
velikosti n≥1 má poslední prvek příspěvek−3 do7B−3A.
Každý další má b menších napravo,0≤b≤m při m již přítomných prvcích,
a příspěvek7b−3[b=m]. Jeho minimum je0 při b=0, maximum7m−3
při b=m; přechod od b=m−1 k m má kladný přírůstek4. Tím se
dokazuje minimum i maximum pro každý seznam, nikoli nezávislá
optimalizace B a A, která by mohla být neslučitelná.

Je-li U počet neprázdných seznamů, minimum je B=0,A=U. Nejvíce
U=min(M,N), takže přesná obecná dolní hodnota pro N≥1 je

    T_min=31N+4M+2−3min(M,N).

Knižní31N+M+2 je proto správně v uvedeném režimu pevné M,N→∞,
kdy N≥M. Nedosazuje se bezmyšlenkovitě do M>N. Maximum při pevných
velikostech je každá buňka sestupná: B=Σ binom(n_j,2),A=N.
Sloučením dvou buněk a,b vzroste počet dvojic o ab, takže globální
maximum nastane v jediné sestupné buňce:

    T_max=7binom(N,2)+28N+4M+2
         =3.50N²+24.5N+4M+2.

Jako u ostatních permutačních extrémů se předpokládá dost klíčových
hodnot pro příslušnou konfiguraci. Asymptotický model nefixuje
konečnou kapacitu jednoho fyzického MIX slova při N→∞.

## P0915: celý průměr(19) a přesný smysl zrychlení

Dosazení(17),(B) do přesného T dává identicky

    E T=(7/4)N²/M+31N−3MH_N+3M ln M+4M−3δ
        −(7/4)N/M+2.

To jsou všechny členy vytištěného průměru. Pro pevné M a N→∞
je vedoucí člen7N²/(4M), protože H_N=O(log N) a δ je malé.
Poměr k M=1 proto směřuje k1/M; příklad M=10 je asymptotické
zrychlení přibližně desetkrát, nikoli deset pro každý vstup či N.
Maximální vedoucí člen nezávisí na M a při M≈N může být stále
kvadratický oproti lineárnímu průměru. Shluknutí do jediné buňky
je skutečně prokázaný extrém, ne jen heuristika.

## P0916:37, celý více-seznamový GF

P0080 doložil g_n(z)=∏_(k=1)^n(1+z+…+z^(k−1))/n!,g₀=1.
Pro pevné obsazení(n₁,…,n_M) existuje N!/(n₁!…n_M!) přiřazení
indexů do buněk, každé s pravděpodobností M^(−N). Podmíněně na
tomto přiřazení jsou vnitřní relativní pořadí nezávislé rovnoměrné
permutace: iid hodnoty v disjunktních sadách indexů zůstávají
nezávislé po podmínění každé z nich na její vlastní interval.
Proto podmíněný GF součtu B je součin g_(n_j). Všechny takové
případy sečteme a dostaneme přesně první vzorec odpovědi37.
Násobením M^N w^N/N! a Cauchyho součinem konečných koeficientů
plyne požadovaná identita

    G_M(w,z)=Σ_(N≥0)g_NM(z) M^N w^N/N!
            =(Σ_(n≥0)g_n(z)w^n/n!)^M.

Jde o formální mocninné řady; derivace v z a koeficientové porovnání
nepotřebují analytické konvergenční předpoklady.

## P0917: všechny koeficienty tří vytištěných polynomů

Pro N=4 mají obsazení typ4,31,22,211,1111. Jejich přesné multinomické
váhy po vytažení M jsou1,4(M−1),3(M−1),6(M−1)(M−2),
(M−1)(M−2)(M−3). Proto

    g_4M=[g₄+4(M−1)g₃+3(M−1)g₂²+6(M−1)(M−2)g₂
              +(M−1)(M−2)(M−3)]/M³.

Přitom g₂=(1+z)/2,g₃=(1+2z+2z²+z³)/6 a součin P0080 dává
24g₄ koeficienty(1,3,5,6,5,3,1). Přímá malá algebra:

    M=1: g₄=(1,3,5,6,5,3,1)/24;
    M=2: g₄₂=(35,71,55,22,5,3,1)/192;
    M=3: g₄₃=(213,283,105,38,5,3,1)/648.

Vynásobení čitatelů216,27,8 dává všechny vytištěné koeficienty
s jmenovatelem5184. Jednotlivé čitatele se sečtou na příslušný
jmenovatel. Nejde o permutační enumeraci. Pro pevné N navíc
Pr(B>0)≤E B=binom(N,2)/(2M)→0, což přesně vysvětluje
ilustrovaný posun rozdělení ke krátkým seznamům při růstu M.

## P0918–0919: každá derivace, oba momenty a rozptyl

P0088–0089 již dokazují E I_n=binom(n,2)/2 a
var(I_n)=n(n−1)(2n+5)/72. Z E[I_n(I_n−1)]=var+mean²−mean
algebraicky plyne g_n''(1)=(3/2)binom(n,4)+(5/3)binom(n,3).
To nejsou nové neověřené momentové předpoklady.

Pro S(w,z)=Σ g_n(z)w^n/n! máme S(w,1)=e^w a

    S_z(w,1)=(w²/4)e^w,
    S_zz(w,1)=(w⁴/16+5w³/18)e^w.

Faktoriály jsou podstatné: Σ binom(n,r)w^n/n!=w^r e^w/r!.
Právě chybějící4!,3! v první sazbě odpovědi jsou známé erratum2000,
nikoli nový nález. Derivace G=S^M dává úplně

    G_z(w,1)=(M/4)w²e^(Mw),
    G_zz(w,1)=M(M−1)e^((M−2)w)(w²e^w/4)²
              +M e^((M−1)w)(w⁴/16+5w³/18)e^w
             =(M²w⁴/16+5Mw³/18)e^(Mw).

Po porovnání koeficientů a vydělení M^N/N!:

    g_NM'(1)=binom(N,2)/(2M),
    g_NM''(1)=[(3/2)binom(N,4)+(5/3)binom(N,3)]/M².

Použitá identita binom(N,2)²=6binom(N,4)+6binom(N,3)+binom(N,2)
plyne rozdělením uspořádaných dvojic dvouprvkových množin podle
průniku velikosti0,1,2. Odečtení čtverce průměru tedy dává přesně

    var(B)=[binom(N,3)/6+(2M−1)binom(N,2)/4]/M².

Směrodatná odchylka je kladná odmocnina, pro N=0,1 nula. M=1
vrací původní n(n−1)(2n+5)/72; všechny koeficienty zůstávají
nezáporné pro celé M≥1. Opravený index NM je použit důsledně.

## P0920:38 se přebírá pouze v prokázaném rozsahu

P0381 v `opening-cost-models.md` již samostatně dokázal přesnou
párovou identitu, E B=(1/2)binom(N,2)Σp_j², nerovnost
Σp_j²≤||f||²₂/M a průměrné O(N) pro M/N→c>0,f∈L².
Pro spojité f tam je také úplný důkaz asymptotické ekvivalence
MΣp_j²→∫f² přes buněčné průměry. Tyto důkazy se neopakují.
P0904 nyní navíc uzavírá dříve jen porovnané přesné MIX koeficienty;
0≤A≤N a cena spojování O(N+M) zachovají tutéž lineární mez.

Poznámka, že konstanta∫f² může být velká, má konkrétní spojitý příklad:
f_c(x)=2c(1−cx) na0≤x≤1/c a0 dále, c≥1. Integrál je1 a
∫f_c²=4c/3, tedy bez společné horní meze. **P0383 zůstává partial**:
odkaz na silnější uniformní konstantu jiného dvouúrovňového algoritmu
Theorem5.2.5T tím není dokázán. Není to nová chyba ani druhá mezera
duplikující již evidovanou. Opravy2000 odlišují průměr od nejhoršího
času a asymptotickou ekvivalenci od doslovné konvergence.

## P0921:39, minimum čas×paměť a skutečný řád M

Pro kladné A,B,C a M>0 je

    (A/M+B)(C+M)=AC/M+BM+A+BC.

Derivace proměnné části je B−AC/M²: záporná pod sqrt(AC/B),
kladná nad ní. Druhá derivace2AC/M³ je kladná. Jediné spojité
minimum je tedy sqrt(AC/B); celočíselné minimum leží na přípustné
podlaze nebo stropu, případně na hranici M≥1/paměťové kapacity.
Nulové koeficienty jsou degenerované monotónní případy, ne skrytá
division-by-zero aplikace. Odpověď používá obvyklé kladné náklady.

Pro skutečný M program nejde doslova o A/M+B, protože obsahuje i4M
a maxima. Přesto závěr M=Θ(N) rigorózně platí: z0≤A≤N máme

    E T≥7N(N−1)/(4M)+28N+4M+2.

Paměť je N+M+O(1) slov v dané reprezentaci. Volba M=N dává
čas O(N), součin O(N²). Pokud M/N→0, člen N³/M jej překoná
neomezeným faktorem; pokud M/N→∞, totéž udělá člen M².
Optimalizující poměr se proto musí držet mezi dvěma kladnými
konstantami. Kniha netvrdí přesnou optimální konstantu pro celý
program, kterou by zjednodušený model nemusel vystihovat.

## P0922:40, obecné odvození celé výsledné expanze

Nechť α>0 je pevné, M=N/α,N>α. Při celočíselném použití se bere
příslušná posloupnost přípustných N,M; při zaokrouhlování je nutno
v následujícím vzorci ponechat skutečné α_N=N/M, jinak se může změnit
konstantní člen. Důkaz je uniformní pro α v každém kompaktním
podintervalu(0,∞), takže pokrývá i tuto verzi.

Substituce u=N(1−t) v přesném(A) dává zvlášť jednoduchý tvar

    E A=(N/α)∫₀^α [1−(1−u/N)^N]/u du.                  (C)

Pro N≥2α a0≤u≤α má logaritmická řada se svým geometricky omezeným
zbytkem tvar N ln(1−u/N)=−u−u²/(2N)+O_α(u³/N²). Po exponenciaci

    (1−u/N)^N=e^(−u)[1−u²/(2N)+O_α((u³+u⁴)/N²)].

Po dělení u je zbytek stále integrabilní i u0; po vynásobení N/α
je O_α(N^(−1)). Tedy, při J(α)=∫₀^α(1−e^(−u))/u du,

    E A=N J(α)/α + [1−(1+α)e^(−α)]/(2α)+O_α(N^(−1)). (D)

Konstantní člen plyne integrací u e^(−u); je zahrnut celý, nejen
vedoucí Poissonův průměr. To dokazuje požadovanou absolutní chybu.

## P0923:40, také celý pomocný ocas z odpovědi

Jeho ε_N=Σ_(n>N)n^(−1)(1−α/N)^(n−N) je přesně
−N^(−1)+Σ_(k≥0)(N+k)^(−1)(1−α/N)^k. Položme h=1/N,x=kh,
f(x)=e^(−αx)/(1+x),g(x)=x f(x). Číslo
d_N=−N ln(1−α/N)−α=α²h/2+O_α(h²) je kladné. Nerovnost
|e^(−v)−1+v|≤v²/2 pro v≥0 dává **pro všechna x≥0**

    (1−α/N)^k=e^(−αx)[1−α²hx/2+O_α(h²(x+x²))].

Není třeba neuniformně zanedbat velká k. Na původní řadě lze také
odříznout k>N^(1+ε): z geometrického odhadu je ocas
O_α(e^(−αN^ε)), menší než každá pevná mocnina1/N.

f'' je absolutně integrabilní. Součtem lichoběžníkové chyby na
intervalech délky h, nejvýše(h²/8)∫|f''|, proto

    hΣ_(k≥0)f(kh)=∫₀^∞f+h f(0)/2+O_α(h²).

Pro g postačí obdélníková chyba≤h∫|g'|=O_α(h).
Vážený zbytek má součet hΣ e^(−αkh)(kh+(kh)²)/(1+kh)=O_α(1),
např. stejným obdélníkovým odhadem pro hladkou integrabilní funkci.
Celkem s I=∫f=e^α E₁(α) a ∫g=1/α−I:

    ε_N=−h+I+h/2−(α²h/2)(1/α−I)+O_α(h²)
       =e^α E₁(α)(1+α²/(2N))−(1+α)/(2N)+O_α(N^(−2)).

To je přesně prostřední expanze626, se správným Eulerovým krajovým
členem a kontrolovaným nekonečným ocasem. Kombinace(B),
H_N=ln N+γ+1/(2N)+O(N^(−2)) a
(1−α/N)^N=e^(−α)(1−α²/(2N)+O(N^(−2))) také vrací(D):
oba α²E₁ členy se zruší. Tato druhá kontrola je algebraický most
mezi vytištěnými mezikroky, nikoli opakovaný numerický běh.

## P0924: přesná identita s E₁ a Eulerovou konstantou

Obě strany J(α)=ln α+γ+E₁(α) mají derivaci(1−e^(−α))/α.
Konstantu lze určit přímo z definice γ=lim(H_N−ln N):

    H_N−ln N
      =∫₀¹ [1−(1−t/N)^N]/t dt
        −∫₁^N (1−t/N)^N/t dt.

V prvním integrálu je integrand≤1 (Bernoulliho nerovnost), ve
druhém je po doplnění nulou za N majoranta e^(−t)/t. Dominovaná
konvergence dává γ=J(1)−E₁(1). Derivací tedy identita platí pro
všechna α>0. Tak je nezávisle doložen i dopředný odkaz5.2.2-43,
bez prohlašování celé budoucí úlohy za již hotovou.

## P0925: tři průměry maxim, tři časy M a jejich přesnost

Z(D), přesného E B a ceny P0904 plyne koeficient N

    a(α)=J(α)/α,
    t(α)=31+7α/4+4/α−3a(α).

Výsledné hodnoty pro α=1,2,10:

| α | a(α) | t(α) |
|---|---|---|
|1|0.7965995993|34.3602012021|
|2|0.6596316781|34.5211049657|
|10|0.2879804915|48.0360585255|

Zaokrouhlení přesně souhlasí s0.7966,0.6596,0.2880 v odpovědi40
a34.36,34.52,48.04 na101. Výpočet nepoužívá speciální numerickou
knihovnu: integrací exponenciální řady je
J(α)=Σ_(k≥1)(−1)^(k+1)α^k/(k k!). Racionálních60 členů a první
vynechaný člen dají dolní/horní mez; po60 jsou velikosti klesající
pro všechny tři parametry. Stejně je omezeno e^(−α). Decimal výstup
se zaokrouhluje směrem ven, přesná šířka je též uložena. I proα=10
je chyba koeficientu menší než10^(−22), mnohem méně než pro tisk
potřebných0.005. Tím je doložena číslicová část, ne nový experiment.

Násobení opravdu spotřebuje10N jednotek z přesné četnosti09.
Pro M=N/α je celý průměr lineární; správnost a dobrá distribuce jsou
oddělené požadavky. Odkaz na zlepšení5.2.5 je oznámení dalšího tématu,
nikoli zde uzavřený algoritmus.

## P0926: prázdné seznamy, přesné spojování a C0026

Indikátor prázdné buňky má pravděpodobnost q^N. Linearita tedy dává
E E=M q^N, a nepotřebuje nezávislost prázdných buněk. P0908 již
ze všech instrukcí35 dokazuje T_join=4N+7M−2E+2. Pro M=N/α
má očekávaný koeficient

    s(α)=4+7/α−2e^(−α)/α.

Proto koeficient celkového času je t+s, nikoli t+4+7/α−e^(−α)/α.

| α | s(α) | t(α)+s(α) | zaokrouhlení |
|---|---|---|---|
|1|10.2642411177|44.6244423198|44.62|
|2|7.3646647168|41.8857696825|41.89|
|10|4.6999909200|52.7360494456|52.74|

Vytištěné44.99 a41.95 jsou tedy chybné;52.74 zůstává správně
zaokrouhleno. Nesprávné dva údaje odpovídají úspoře jen E místo2E;
to je shoda vzorců, nikoli prokázaná historie vzniku chyby. Jedinou
instrukcí vynechanou prázdným seznamem nad rámec ostatních četností
je ST3 na28, která stojí2u. Model je tentýž jako správných94u
v36, kde E=0 a chyba se neprojeví. Bez optimalizace s END, přesně
pro původní program, který text jmenuje.

`V3-C0026-multiple-list-total-times.md` a pětivrstvý záznam ve
`sources/multiple-list-total-time-errata-review.json` oddělují tento
confirmed/low číselný nález od známých oprav37 a38. Konstanty se
týkají očekávaného času, nikoli správnosti či asymptotického řádu.
