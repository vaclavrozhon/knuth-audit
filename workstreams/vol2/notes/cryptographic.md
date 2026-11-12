# §3.5 F: předpovídání bitů, algoritmus L a faktorizace

Stav 1. listopadu 2026. Původní strany 170–176, 183 a odpovědi 598–599
přečteny vizuálně. Níže jsou obecné důkazy všech čtyř lemmat, algoritmu L,
věty G a redukce P; úlohy 40–44 jsou zahrnuty. Výpočetní dolní mez pro
faktorizaci se nedokazuje ani nepředpokládá jako známá věta. Nové nálezy
C0068/C0069 jsou odděleny od pravdivých hlavních tvrzení.

Všechny čtyři vrstvy errat i aktuální TeX prohledány podle stran, názvů
lemmat a témat. Zapracovány opravy 173 (0001->0011, 30.11.1997;
Hadamard místo Walsh, 23.6.2001), 176 (gregoriánský rok, 14.1.2000;
pořadí přibližné rovnosti, 25.1.2003; 535 místo 53.5, 20.9.2005;
„usable“, 29.6.2017), 42(b) (různost vektorů, 26.1.2001) a definice
T(f),T(g) v P4 (30.6.2024). Tyto opravy neřeší C0068/C0069.
Fyzický novější dotisk ani prvenství nejsou ověřeny; návrhy se neodesílají.

## 1. Hybridní argument P1 a úloha 40

N-source je konečný neprázdný multiset N-bitových slov. Náhodný výběr
počítá každou kopii zvlášť. P(A,S) je pravděpodobnost, že algoritmus A
vypíše 1; zahrnuje náhodnost vstupu i vnitřní mince algoritmu. U_N zde
značí rovnoměrný zdroj všech N-bitových slov. Čas T(A) je maximum přes
vstupy ze střední doby běhu přes vnitřní mince. N je kladné.

Pro 0<=k<=N nechť F_k zachová prvních k vstupních bitů, zbytek nahradí
nezávislými férovými bity a spustí A. Položme p_k=P(F_k,S). Potom
p_0=P(A,U_N), p_N=P(A,S) a součet p_(k+1)−p_k je jejich rozdíl.
Předpovídající algoritmus D_k si v simulaci F_k pamatuje první nový
bit C=B'_(k+1) a předpoví

```
D_k = F_k xor C xor 1.
```

Používá pouze prvních k skutečných bitů. Test úspěchu T_k navíc přečte
skutečný další bit B_(k+1) a vypíše 1 právě při správné předpovědi:

```
T_k = [D_k=B_(k+1)] = F_k xor C xor B_(k+1).
```

To je přesně rovnice (39). Symboly D_k a T_k záměrně rozlišují to,
co kniha označuje A_k a A_k^P.

Pro pevný prefix označme q pravděpodobnost skutečného dalšího bitu 1
a a_b pravděpodobnost, že A přijme prefix následovaný b a nezávislým
náhodným koncem. Pak

```
Pr(D_k=1 | prefix) = (1−a_0+a_1)/2,
Pr(D_k=B_(k+1) | prefix) = 1/2+(q−1/2)(a_1−a_0).
```

Druhý člen je právě rozdíl podmíněných přijetí F_(k+1) a F_k.
Zprůměrováním dostaneme P(T_k,S)=1/2+p_(k+1)−p_k a P(T_k,U_N)=1/2.
Prefixy s nulovou pravděpodobností lze ignorovat. Výpočet odpovědi 40
souhlasí, včetně jejích q_b=a_b/2. Pokud je celkový rozdíl alespoň
epsilon, jeden z N přírůstků je alespoň epsilon/N. Záporný rozdíl
vyřeší komplement A. Čas simulace je T(A)+O(N), což dokazuje P1.
Přesný test ověřil 6280 identit pro všechny booleovské testy a všechny
bodové zdroje do N=3; linearitou tím pokrývá všechny směsi těchto zdrojů.

## 2. P2–P4, úloha 41 a V2-C0069

Zdroj je posuvově symetrický, mají-li všechna jeho souvislá okna stejné
délky stejné rozdělení. Pak lze D_k aplikovat na posledních k bitů před
B_N místo prvních k bitů; společné rozdělení kontextu a cílového bitu
se nezmění. Tím se dokazuje P2. Je důležité použít předpověď D_k,
nikoli test její správnosti T_k.

Právě zde je **V2-C0069**: důkaz P2 na straně 172 použije A_k^P na
B_(N−k)...B_(N−1)00...0. Podle (39) tím vyjde F_k xor C, tedy opak
správné předpovědi. Nejkratší protipříklad je N=1, S={1}, A(B)=B.
Rozdíl přijetí je 1/2 a k=0. Simulace dává F_0=C, ale vytištěná
konstrukce A'_0=A_0^P(0)=C xor C=0 předpoví vždy špatně.
Správný D_0=C xor C xor 1=1 předpoví vždy správně.

V obou větvích důkazu P2 stačí použít A_k místo A_k^P; poslední
věta má mluvit o pravděpodobnosti správné předpovědi při rovnoměrném
vstupu, nikoli obecně o pravděpodobnosti A'=1. Stejné rozlišení chybí
v odpovědi 41 na straně 598: její poslední součet je pravděpodobnost
správné předpovědi. Například N=1, S={0}, A(B)=1−B dává D_0=0,
přesto je tento součet roven 1. Hlavní tvrzení P2 a zadání 41 jsou
správná; chybný je popis konstrukce a jejího výstupu.

Úloha 41 má úplnou konstruktivní opravu: zvolme k rovnoměrně z
0,...,N−1 a použijme D_k na koncový kontext. Úspěch je přesně
1/2+(P(A,S)−P(A,U_N))/N. Rovnoměrné k z férových bitů lze získat
odmítáním v očekávaném O(log N), tedy v povoleném O(N) čase.
Znaménko rozdílu není nutné odhadovat, chceme-li redukci pro oba směry:
spustíme následnou konstrukci pro A i jeho komplement. Jeden směr
má potřebnou kladnou výhodu; čas se zvětší jen konstantně.

Iterativní zdroj má tvar f(g(x)),...,f(g^N(x)) pro rovnoměrné x
z konečné množiny, kde g je permutace. Permutace zachovává rovnoměrnost,
proto je zdroj posuvově symetrický; totéž platí pro obrácení všech slov.
Aplikace opraveného P2 na obrácený zdroj dokazuje P3. Z daného y=g(x)
lze pak spočítat f(y),f(g(y)),...,f(g^(N−2)(y)) a předpovědět f(x).
To dává P4 s časem T(A)+O(N)(T(f)+T(g)). Pro N=1 je kontext prázdný.
U kongruenčního příkladu modulo 2^e je permutační předpoklad splněn
pro liché a; nelze jej automaticky přenést na sudé násobitele.

## 3. Úloha 42, V2-C0068 a algoritmus L

Párová nezávislost znamená nezávislost každé dvojice různých veličin;
nevyžaduje nezávislost všech najednou. Pro veličiny se stejným konečným
průměrem mu a rozptylem sigma² a s nulovými vzájemnými kovariancemi
má součet X průměr n mu a rozptyl n sigma². Pro t>0 a sigma²>0
nezápornost (X−n mu)² dává

```
n sigma² >= t n sigma² Pr((X−n mu)²>=t n sigma²).
```

Vydělením kladným prahem vznikne požadovaná Čebyševova nerovnost.
Pro obecná rozdělení lze tento argument psát jako nerovnost veličin
a jejich středních hodnot; není potřeba předpokládat diskrétní rozdělení.

**V2-C0068:** Zadání 42(a) nepředpokládá sigma²>0. Pro n=1, X_1=0
jistě a t=2 má levá strana pravděpodobnosti hodnotu 1 a pravá mez je 1/2,
protože událost je 0>=0. Stačí doplnit kladný rozptyl (a obvyklé t>0),
nebo změnit v události >= na >. Při nulovém rozptylu je totiž součet
konstantní a přísné překročení má pravděpodobnost nula. V aplikaci níže
je deterministický krajní případ bez problémů řešitelný zvlášť.

Nechť B je náhodná binární matice k krát R se všemi bity nezávislými
a férovými. Součty i součiny vektorů nyní počítáme modulo 2. Dva různé
nenulové vektory c,c' délky k jsou lineárně nezávislé: v tělese dvou
prvků je jediný nenulový násobek vektoru on sám. Pro každý sloupec B
je tedy dvojice (cB,c'B) rovnoměrná na dvou bitech, a přes různé sloupce
je nezávislá. Celá dvojice vektorů je rovnoměrná na 2^(2R) možnostech.
To dokazuje 42(b) se známou opravou c!=c'.

Pro x=0 položme s=E_z (-1)^G(z)>0 a n=2^k−1. Pro pevnou souřadnici i
jsou veličiny X_c=(-1)^G(cB+e_i), c!=0, párově nezávislé, mají průměr
s a rozptyl 1−s². e_i je vektor s jedinou jedničkou na pozici i.
Jejich součet je lichý, takže není nikdy nula. Pokud je záporný,
odchylka od jeho průměru n s přesáhne n s. Proto

```
Pr(sum X_c<0) <= (1−s²)/((2^k−1)s²) <= 1/((2^k−1)s²).
```

Pro s=1 jsou všechny X_c jistě kladné a chyba je nulová; nepoužíváme
zde dělení nulovým rozptylem. Součet chybových pravděpodobností pro
R souřadnic je horní mez pravděpodobnosti, že x(0) není nulový vektor.

Pro obecné x definujme G'(z)=G(z) xor (x·z), kde tečka je skalární
součin modulo 2. Jeho průměrná znaménková hodnota je příslušný
koeficient s z rovnice (40). Přímá algebra dává

```
h'_i(b)=(-1)^(x_i) h_i(b+Bx),
x'(b)=x(b+Bx)+x.
```

Značka x(b) znamená kandidáta vypisovaného algoritmem L pro b,
kdežto x bez argumentu je hledaný vektor. Jelikož žádné h_i(b) není
nula, znaménková rovnost platí bez výjimky. Jak b probíhá všechny
k-bitové vektory, probíhá je i b+Bx. Nulový kandidát pro G' tedy
odpovídá kandidátu x pro G. Pokud 2^k>ceil(2R/s²), je součet chyb
nejvýše 1/2. To dokazuje větu G a odpověď 42(c).

Všechny h_i(b) jsou Hadamardovou transformací pole s nulou na c=0
a hodnotami (-1)^G(cB+e_i) jinde. Rozklad transformace podle jednoho
bitu počítá pro každou dvojici součet a rozdíl. Má k stupňů, každý
2^k operací, celkem O(k 2^k R). Vyhodnocení G je R(2^k−1), což
souhlasí s uvedenou horní mezí 2^k R. Při randomizovaném G lze použít
nezávislé nové mince pro každé dvojici (i,c) a výsledek pak použít ve
všech b; párová nezávislost v důkazu zůstává platná a s zahrne i tyto
mince. Ekvivalentně lze předem vylosovat samostatnou nezávislou pásku
pro každý pár (i,c) a všechny tyto pásky zahrnout do pravděpodobnostního
prostoru. Jediná společná páska opakovaná od začátku při všech voláních
by obecně potřebnou párovou nezávislost nezaručila; viz podrobný rozbor
v `recovery-linear-guesses-2026-11-06.md`.

Přesný soupis kontroluje všech 16 booleovských funkcí dvou bitů pro
k=1,...,5 a všech 256 funkcí tří bitů pro k=2, vždy přes všechny matice.
Ověřuje skutečné pravděpodobnosti chyby vyznačeného kandidáta b=Bx
i celé výstupní listiny. Celkem jde o 336 tabulek parametrů, 38208
kombinací funkce/matice, 215296 nezávisle přepočtených transformovaných
položek a 27 úplných párových rozdělení. Rovněž všech 16 koeficientů
vytištěného čtyřbitového příkladu souhlasí po opravě 0001->0011.

## 4. Věta P: průměrná redukce na faktorizaci

Blumovo číslo je zde M=P Q se dvěma různými prvočísly shodnými s 3
modulo 4 a v uvedených intervalech. Ty implikují 2^(R−1)<M<2^R a
Q−P>(1−1/sqrt(2))2^(R/2)>.29·2^(R/2). Množina invertibilních
kvadratických zbytků modulo M se označí QR(M): jsou to druhé mocniny
čísel nesoudělných s M. Čínská věta o zbytcích rozkládá QR(M) na
součin dvou grup lichých řádů (P−1)/2 a (Q−1)/2. Mocnění na druhou
je v grupě lichého řádu bijekce. Každý prvek QR(M) má přesně čtyři
invertibilní odmocniny modulo M, z nichž právě jedna je opět v QR(M).

Použijme g(x,z,M)=(x² mod M,z,M) a f(x,z,M)=x·z mod 2. Maska z má
R nezávislých férových bitů. Po prvním umocnění rovnoměrného
invertibilního seedu je x rovnoměrné v QR(M), takže dostáváme
iterativní zdroj. Je nutné zachovat stejné rozdělení M ve zdroji a
v následném průměru faktorizace. Označme je mu_M. Při jednom výskytu
každé trojice (x,z,M) v množině X z knihy je mu_M úměrné |QR(M)|,
nikoli rovnoměrné přes různá M. Pokud se M losuje rovnoměrně,
pracujeme s odpovídající váženou směsí zdrojů. Následující důkaz platí
pro obě konvence se stejnou mu_M; nezaměňuje jejich průměry. Tištěné
slovo „random M“ samo neupřesňuje, kterou z těchto konvencí zvolit.

Opravené P4 a 41 z testu s rozdílem alespoň epsilon vyrobí odhad G
s globálním znaménkovým průměrem alespoň 2 delta, kde delta=epsilon/N,
a časem T(A)+O(NR²). Pro dvojici (x,M), x v QR(M), označme s_(x,M)
jeho průměr přes z a vnitřní mince. Protože s_(x,M)<=1, z celkového
průměru >=2 delta plyne

```
Pr_(x,M)(s_(x,M)>=delta) >= delta.
```

Například rozdělením průměru na tuto událost H a její doplněk dostaneme
2 delta<=Pr(H)+delta, což stačí. Platí to i se zápornými koeficienty.

Na vstupu M vyberme X_0 rovnoměrně z 1,...,M−1. Je-li gcd(X_0,M)>1,
známe faktor. Jinak y=X_0² má rovnoměrné rozdělení v QR(M). Algoritmus L
použijeme na funkci z->G(y,z,M) s

```
k=ceil(lg(1+2N²R/epsilon²)).
```

Pro dvojici s_(x,M)>=delta zahrne jeho seznam jedinou QR-odmocninu x
hodnoty y s pravděpodobností alespoň 1/2. Z výstupu vybereme libovolnou
správnou odmocninu ověřením x²=y modulo M. Výstup závisí na y a
vnitřních mincích, nikoli na volbě X_0 mezi jeho čtyřmi odmocninami.
S pravděpodobností 1/2 proto x není ani X_0, ani −X_0. Tehdy

```
gcd(X_0−x,M), gcd(X_0+x,M)
```

jsou dva prvočinitelé M. Celkový úspěch je alespoň delta/4=epsilon/(4N).
Větev s nesoudělným seedem tento odhad nezhoršuje: pro každé M uspěje
jistě a její směs s podmíněným úspěchem nemůže být menší než on.
Není nutné podmiňovat celý průměr přes různá M na nesoudělnost.

Počet volání G je O(N²R² epsilon^(−2)). Jejich čas je tedy
O(N²R² epsilon^(−2)T(A)+N³R⁴ epsilon^(−2)). Transformace, konstrukce
matice, ověřování odmocnin a gcd se vejdou do druhého členu.
Z epsilon>=2^(−N) plyne k=O(N+log R), a tím se potřebný transformační
faktor také absorbuje. Oba směry znaménka testu lze spustit za dvojnásobný
čas. Tím je doložena i konstruktivnost, bez hledání nejlepšího k v P1.

Nezávislý soupis prověřil všech 11 povolených modulů do R=12: všechny
invertibilní seedy, bijektivitu na QR(M), čtyři odmocniny a 18788 voleb
odmocniny pro návrat faktorů. Tyto malé moduly pouze kontrolují algebru;
nejsou experimentem dokazujícím obtížnost faktorizace.

Úloha 43: libovolné pevné M lze faktorizovat algoritmem s jeho faktory
zapsanými v programu. Věta kvantifikuje přes všechny rychlé algoritmy,
nejen ty, jejichž program dnes umíme nalézt. Smysluplný předpoklad
obtížnosti proto musí mluvit o celé rodině vstupů a jejím rozdělení.
Nejde o tvrzení, že každý jednotlivý modul je fakticky snadný.

## 5. Číselné příklady a úloha 44

Průměrný gregoriánský rok má 365.2425 dne; jeden MIP-rok tedy odpovídá
31556952000000 instrukcím. Dosazení do historické hypotetické funkce
exp(R^(1/4)(ln R)^(3/4)) dává pro R=50000 přibližně 1.75254·10^25
MIP-roků, správně zaokrouhlených v knize na 2·10^25. Odpovídající
mez pro test při N=1000 je 70101.43 MIP-roků, takže uvedených 70000
je konzervativní. Další dvě meze jsou 74861242823.86 MIP-roků a
534964250361481.92 MIP-roků. Souhlasí s 7.486·10^10 a s opravenými
535 teraMIP-roky. Výpočet používá 90 desetinných míst. Jsou to pouze
podmíněné aritmetické příklady, nikoli současné doložené bezpečnostní meze.
Dopředná záruka pro variantu bez masky se prověří samostatně v §4.5.4-43.

Úloha 44 má grafový argument: vrcholy jsou všechny konečné tabulky
stejné délky, hrana mění jednu číslici. Tento graf je souvislý, protože
libovolné dvě tabulky lze propojit postupnou změnou lišících se pozic.
Neprázdná vlastní třída „náhodných“ tabulek proto nemůže být uzavřená
na všechny jednotlivé překlepy. Aspoň jeden překlep překročí její hranici.
To neříká, že každý překlep v každé tabulce zničí náhodnost, ani že
pravděpodobnostní zdroj přestane být náhodný po známé bijektivní změně.
Tištěná odpověď má tento přesný rozsah.

## Zdroje a reprodukovatelnost

`verify_cryptographic.py --resume` ukládá pět bloků do
`results/cryptographic.json`. První běh 48775 skončil až na chybné
kontrolní interpretaci zaokrouhleného 2·10^25 jako dolní meze;
čtyři přesné bloky již byly uloženy. Opravena pouze tato kontrola,
číselný blok následně prošel s exit 0, předchozí bloky se neopakovaly.
Log zachovává i původní chybu ověřovacího programu.

Primární Goldreich–Levinův autorský text (verze práce ze STOC 1989)
byl přečten v úvodu a formulaci hlavního výsledku, strany 1–4.
Potvrzuje redukci hádání skalárního součinu na inverzi i práci s obecnými
rozděleními; jeho jiné kvantitativní algoritmy se zde celé neauditují.
Levinův autorský přetisk textu z roku 1993 (arXiv 2012) byl přečten
včetně matematické části a poděkování. Obsahuje právě párové výběry,
transformační zrychlení a připisuje zjednodušení Rackoffovi a Venkatesanovi.
To odpovídá směru známé opravy atribuce na straně 179; prvenství se
samostatně neprohlašuje. Přesné adresy, otisky a rozsah čtení jsou
v `sources/cryptographic-sources.json`.

Citovaný GGM (1986), věta 4 na stranách 803–804, byl přečten vizuálně
včetně celého důkazu. Používá náhodný hybridní index a teleskopický
průměr úspěchů; tím je doložena věcná souvislost odkazu v odpovědi 40.
Zbytek článku se zde neprohlašuje za auditovaný.
