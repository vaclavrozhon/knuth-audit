# Úloha 7.1.1–34: průměrné počty krychlí a prvoimplikantů

Checkpoint X0072, P0679–P0689. Zadání p84/file101 má **čtyři**
části (a)–(d); předchozí stručný kurzor „(a)–(c)“ nebyl úplný.
Odpověď je na p540–541/file557–558. Původní sazba prohlédnuta
v images/file101.png, images/proof-file557.png a images/proof-file558.png.
Poslední dva obrazy byly nyní nově vykresleny; PDF file558 je vlastní
výřez knihy. Žádný matematický program ani numerická aproximace neběžely.

Přebírá se přesný konečný pravděpodobnostní argument 33 z proof-042,
P0676–P0678. Bibliografické poznámky nejsou náhradou za následující
důkazy. Veškeré asymptotické vztahy jsou pro n→∞; konstanty mohou
záviset na pevném ε>0, nikoli na přípustném m.

## Přesné střední hodnoty — P0679

Pišme N=2^n, q=m/N a

    R(r)=(m)_r/(N)_r=binom(N−r,m−r)/binom(N,m),

kde index znamená klesající faktoriál a R(r)=0 pro m<r≤N.
Pro dimenzi j je s=2^j a počet všech j-krychlí je
(N/s)binom(n,j): zvolíme j volných souřadnic a pevné hodnoty ostatních.
Linearita střední hodnoty a P0676/P0677 dávají

    c_j=(N/2^j)binom(n,j) R(2^j);
    p_j=(N/2^j)binom(n,j)
          Σ_{l=0}^{n−j}(−1)^l binom(n−j,l)R((l+1)2^j);
    c=Σ_j c_j,   p=Σ_j p_j.

Všechna uvedená r jsou ≤N, protože k+1≤2^k pro k=n−j.
Jde o rovnoměrný výběr právě m bodů, nikoli Bernoulliho model.
Vždy 0≤p≤c a c₀=m. Pro m=0 je c=p=0; pro m=N je
c=Σ_j 2^(n−j)binom(n,j)=3^n a p=1. Pro n=0 je c=p=m.
Tyto okraje ověřují doménu, bez výpočtu a bez nové vady.

## 34(a): horní mez v řídké oblasti — P0680

Předpokládejme 0<m≤N/n. Každý faktor (m−i)/(N−i) je ≤q,
takže R(r)≤q^r. Konkrétně

    c₁=nm(m−1)/(2(N−1)) ≤ (mn/2)(m/N) ≤ m/2.

Pro j≥2 dostáváme

    c_j ≤ (m/2^j)(n^j/j!)q^(2^j−1)
        ≤ m/(2^j j! n^(2^j−1−j)).

To je vytištěná mez v slabé podobě ≤, která zahrnuje i nulové členy.
Protože 2^j−1−j≥j−1≥1 pro j≥2,

    Σ_{j≥2}c_j ≤ (m/n) Σ_{j≥2}1/(2^j j!) = O(m/n).

Tím m≤c≤3m/2+O(m/n), uniformně v této oblasti. Při m=0
jsou obě strany nulové; není třeba dělit m.

## 34(a): dolní mez pro prvoimplikanty — P0681

Z bodového případu 33:

    p≥p₀=N binom(N−n−1,m−1)/binom(N,m)
         =m ∏_{i=1}^{m−1}(1−n/(N−i)).

Pro n≥3 a m≤N/n je N−m≥n a všechny potřebné faktory nezáporné.
Každý je nejméně 1−n/(N−m), takže

    p₀ ≥ m(1−n/(N−m))^m
       ≥ m(1−n/(N−N/n))^(N/n)
       = m exp[(N/n)ln(1−n²/(N(n−1)))].

Druhá nerovnost používá obě monotónnosti: základ s rostoucím m
klesá a zvětšení exponentu čísla v [0,1] hodnotu rovněž zmenšuje.
Exponent je

    −n/(n−1)+O(n/N)=−1+O(1/n).

Proto p≥m/e−O(m/n), což je přesný význam vytištěného
p≥m/e+O(m/n). Spolu s p≤c a P0680 je p=Θ(c), pro m>0
uniformně; při m=0 zůstává ekvivalentní dvojice násobkových
nerovností platná. Malé pevné n nejsou předmětem limitního odhadu.

## 34(b): existence t a jeho rozsah — P0682

Nyní N/n≤m≤(1−ε)N, tedy 1/n≤q≤1−ε. Položme λ=ln(1/q)>0.
Podmínka zadání je

    n^(−4/3) ≤ α=q^(2^t) < n^(−2/3),
    (2/3)ln n < λ2^t ≤ (4/3)ln n.

Polouzavřený interval má poměr krajů 2, takže existuje právě jedno
celé t, a přesně

    t=floor(log₂((4/3)ln n/λ))
     =floor(lg lg n−lg lg(N/m)+lg(4/3)).

Proto t≥0 a t≤lg ln n+O_ε(1). Pišme s=2^t;
pak s=O_ε(ln n), t=O_ε(ln ln n). Nečiníme nepravdivý předpoklad
t→∞: například na dolní hranici m=N/n je t=0.

## Rovnoměrná aproximace výběru bez vracení — P0683

Pro r≤O_ε(n ln n) a dost velké n máme r/m=o(1). Platí

    ln(R(r)/q^r)
      =Σ_{i=0}^{r−1}[ln(1−i/m)−ln(1−i/N)]
      =O(r²/m).

Každý sčítanec je nekladný a absolutně nejvýše 2i/m, takže
konstanta je uniformní. Exponenciace dává
R(r)=q^r(1+O(r²/m)). Pro r=ls získáváme přesně aproximaci
α^l(1+O(l²s²/m)) v odpovědi.

Potřebný podmíněný poměr má pro 1≤l≤n navíc tvar

    R((l+1)s)/R(s)=α^l(1+O(l²s²/m)),

protože součet začíná indexem s a končí (l+1)s−1.
Pro l=0 je poměr přesně 1 a chyba nula. Stejné odvození platí
se s nahrazeným 2s a α nahrazeným α².
Zde je celé použité rozpětí l≤n, nikoli jen pevné l.

Vytištěný ostrý znak R(ls)<α^l lze nahradit ≤; pro r=0 či 1
je rovnost. Tato nepodstatná ostrost se v žádném důkazu nepoužívá.

## Koncentrace středních počtů ve dvou dimenzích — P0684

Poměr sousedních počtů splňuje přesně, pokud c_j>0,

    c_{j+1}/c_j
      = (n−j)/(2(j+1)) · R(2^(j+1))/R(2^j)
      ≤ (n−j)/(2(j+1)) q^(2^j).

Při nulovém c_j jsou nulové i všechny následující, takže případ
nevyžaduje dělení. Pro j<t dovoluje P0683 obrácený poměr:

    c_j/c_{j+1} ≤ O(t/(n√α)) = O(t n^(−1/3)) =: ρ₋.

Pro dost velké n je ρ₋<1/2; sečtení geometrické řady dává

    Σ_{j<t}c_j/c_t = O(t/(n√α)).

Pro t=0 je tato suma prázdná. Toto je silnější než vytištěná
O(t²/(n√α)) při t≥1. Pro horní ocas, j≥t+1, je

    c_{j+1}/c_j ≤ nα²/(2(t+2)) =: ρ₊ = O(n^(−1/3)/(t+2)),
    Σ_{j≥t+2}c_j = O(ρ₊ c_{t+1}).

Také přesně, pro každé d≥0 s t+d≤n,

    c_{t+d}/c_t
      ≤ [n/(2(t+1))]^d α^(2^d−1).

Plyne to z poměru binomických koeficientů a
R(2^(t+d))/R(2^t)≤q^(2^(t+d)−2^t).
Tento odhad nahrazuje vytištěnou hrubší zkratku s n/(2t).
Ta je použitelná pro t≥1; **vynechaný případ t=0 je zde doplněn**,
aniž by se měnil požadovaný výsledek.

Definujme

    K=(N/s)binom(n,t)α,
    A=(n−t)α/(2(t+1)).

P0683 dává c_t=K(1+O(s²/m)) a
c_{t+1}/c_t=A(1+O(s²/m)).
Oba geometrické ocasy tedy dokazují

    c=K(1+A)(1+O_ε((t+1)n^(−1/3))).

To je přesný uniformní význam prvního asymptotického vyjádření
odpovědi a nápovědy: téměř všechny implikanty ve střední hodnotě
mají n−t nebo n−t−1 literálů. Netvrdí se zde koncentrace náhodné
proměnné kolem její střední hodnoty.

## Střídavý součet pro prvoimplikanty — P0685

Po podmínění, že daná t-krychle je pravdivá, z P0677 plyne

    p_t/c_t
      =Σ_{l=0}^{n−t}(−1)^l binom(n−t,l)R((l+1)s)/R(s).

P0683 dovoluje nahradit podmíněný poměr α^l, ale je třeba
kontrolovat **součet absolutních chyb**, ne jen každý člen zvlášť:

    |error| ≤ O(s²/m) Σ_l l² binom(n−t,l)α^l
            ≤ O(n² α(1+α)^n s²/m).

Identita pro součet l² plyne dvakrát derivováním (1+z)^k:
Σ l² binom(k,l)z^l=kz(1+z)^(k−1)+k(k−1)z²(1+z)^(k−2).
To dokazuje i přesný druh chybového členu vytištěný v odpovědi.

Protože α<n^(−2/3), máme (1+α)^n≤exp(nα)≤exp(n^(1/3)),
zatímco m≥2^n/n a s=O_ε(ln n). Chyba je tudíž exp(−Ω_ε(n)).
Je exponenciálně menší i než hlavní člen
(1−α)^(n−t)≥exp(−O(n^(1/3))). Nedochází ke skryté ztrátě
relativní přesnosti rušením střídavých členů.

Dále ln(1−α)=−α+O(α²), takže

    (1−α)^(n−t)
      =e^(−nα)(1+O(tα+nα²))
      =e^(−nα)(1+O_ε((t+1)n^(−1/3))).

Tedy p_t/c_t∼e^(−nα), uniformně. Dosazením 2s a α² do téhož
argumentu dostaneme p_{t+1}/c_{t+1}∼e^(−nα²), také uniformně.

## Celkový asymptotický vzorec pro p — P0686

Ještě je nutné ověřit, že malé c-ocasy neovládnou p, jehož
hlavní člen může být menší. Položme x=nα a

    M=e^(−x)+A e^(−x²/n).

V našem rozsahu x≤n^(1/3), takže e^(−x²/n)=1+O(n^(−1/3)).
Pro x≤1 je M≥e^(−1); pro x≥1 je
A≥x/(4(t+1)) pro dost velké n. Proto současně

    M≥const/(t+1),   M≥const·A.

Jelikož 0≤p_j≤c_j, dolní ocas vůči c_t M je
O(ρ₋(t+1)) a horní O(ρ₊). Oba jsou o(1), uniformně.
Spolu s P0685 tedy platí celý vytištěný výsledek, nyní s mezí chyby:

    p=K [e^(−nα)+A e^(−nα²)]
          (1+O_ε((t+1)² n^(−1/3))).

Tato chyba mizí díky t=O_ε(ln ln n). Důkaz zahrnuje i t=0
a nepředpokládá, že první nebo druhý člen vždy převažuje.

## 34(c): speciální posloupnost a známá oprava logaritmu — P0687

Nechť t→∞ je celé,

    L=ln t−ln ln t=ln(t/ln t),
    β=2^(−2^t),   n=floor(L/β),   m=2^(n−1).

Pak q=1/2, nβ=L+O(β), a t splňuje intervalovou definici z části (b)
pro všechna dost velká t: −ln β/ln n→1. Proto α=β a

    e^(−nα)=(ln t)/t ·(1+O(β)),
    A=L/(2(t+1)) ·(1+O(t/n))+O(β/t),
    e^(−nα²)=1+O(L²/n).

Chyby P0684/P0686 jsou v této posloupnosti menší než uvedené
logaritmické chyby. Dostáváme

    c/c_t=1+O((ln t)/t),
    p/c_t=(ln t)/t+(ln t−ln ln t)/(2t)+O((ln t)/t²)
          =(3/2)(ln t)/t+O((ln ln t)/t),
    c/p=(2/3)t/(ln t)·(1+O((ln ln t)/(ln t))).

Z n=floor(L·2^(2^t)) plyne lg lg n=t+o(1), takže poslední vzorec je

    c/p=(2/3) [lg lg n / (ln lg lg n)]
          ·(1+O(log log log log n / log log log n)).

Smíšené základy v hlavním faktoru jsou podstatné. all4a-pre,
p541, řádek 3 odpovědi 34(c), 16.10.2013, právě nahrazuje
původní lg lg lg n výrazem ln lg lg n. Oprava je nezbytná
a zde zohledněná; nejde o nový nález.

## 34(d): obecná mez poměru — P0688

Pro 0<m≤N/n dává P0681 poměr O(1). V hustší oblasti použijeme
P0684/P0686, kde A∼x/(2(t+1)) a e^(−x²/n)∼1.

Pro velká t položme H=ln t−ln ln t>0. Jsou dva případy:

- Je-li x≤H, potom p_t/c je nejméně
  (ln t)/t−O(((ln t)/t)²), až na již doložené uniformně menší chyby.
  Důvod: e^(−x)≥e^(−H)=(ln t)/t a 1+A≤1+O((ln t)/t).
- Je-li x>H, potom p_{t+1}/c je nejméně
  (1/2)(ln t)/t−O((ln ln t)/t).
  Funkce A/(1+A) roste s x a v bodě H je
  H/(2(t+1)+H)=(1/2)(ln t)/t+O((ln ln t)/t).

Obě větve dávají p/c≥const·ln t/t a tedy c/p=O(t/ln t).
To ověřuje oba odhady odpovědi, včetně směru nerovností.
Pro omezená t, zejména t=0 či 1, se logaritmický práh nepoužije:
při x≤1 je e^(−x)≥e^(−1), při x≥1 je A≥const/(t+1).
V obou případech (1+A)/(e^(−x)+A)=O(1) pro omezená t.

Nakonec t≤lg ln n+O_ε(1) a funkce t/ln t je pro t>e rostoucí.
Tím pro všechny 1≤m≤(1−ε)N dostáváme

    c(m,n)/p(m,n)=O_ε(log log n / log log log n).

Pro m=0 je doslovný poměr 0/0 nedefinovaný; ekvivalentní nerovnost
c≤B(n)p však platí. Tento triviální okraj pouze explicitně oddělujeme,
nevytváříme kvůli němu kartu. Nenulový výsledek i jeho asymptotická
ostrost podle části (c) jsou dokázány.

## Co přesně plyne pro dodatek k algoritmu P — P0689

Předchozí mez je **poměr dvou středních hodnot** E[C]/E[P].
Není bez dalšího důkazem E[C/P], ani výrokem o každém náhodném vstupu.
Vytištěný dodatek na p539 používá první, správný význam.

Při opraveném řízení P2 z P0661, nebo při jeho diskutovaném
konstantním bit-scanu, má náklad mez O(nm+nC). Linearita střední
hodnoty, c≥m a nyní dokázaná mez dávají

    E[T]=O_ε(n p log log n / log log log n).

Tento závěr je podmíněn uvedeným nákladovým modelem/opraveným řízením;
C0004 o doslovném opakovaném scanu j se tím neuzavírá.
Přídavný faktor n z errata odpovědi 30 se neztrácí. Kvalitativní
„nearly proportional“ není prohlášeno za konstantní faktor ani
za měřený benchmark. Odkaz 32 na velký výstup již dokládá P0675;
v P0662 zůstává otevřen pouze samostatný odkaz na úlohu 116.

## Mapa stránky 540 a hranice

Celá matematika p540 má nyní přesné argumenty:

- pokračování 32(a), konstrukce 32(b)/(d), horní mez 32(c):
  proof-042, P0670–P0675, se známou opravou;
- oba vzorce 33 a bodový případ: proof-042, P0676–P0678;
- všechny součty, nerovnosti a střední hodnoty 34(a):
  P0679–P0681;
- interval a t, aproximace výběru, dolní/horní ocasy, dominantní
  dimenze, střídavý součet a konečné asymptotiky 34(b): P0682–P0686.
  Omezení vytištěné pomocné zkratky s 1/t je výslovné a t=0 doplněno.

P84 zůstává partial kvůli úloze 35. P541 má hotové 34(c)/(d),
ale odpovědi 35–37 čekají. P539 zůstává partial kvůli C0004
a dosud nepokrytému odkazu 116.

Relevantní vrstvy all4a-pre, all4a, err4a, all4f0, err4f0 byly
prohledány podle stránek, úlohy 34 i asymptotických výrazů;
jediná související změna 34 je známá oprava základu logaritmu.
Bibliografická výjimka: články Mileto–Putzolu 1964/1965 a Weber 1983
ani jejich historická priorita či samostatné tvrzení o varianci
nebyly ověřeny; nejsou vstupem našeho argumentu. Bernoulliho model
v posledním bibliografickém odstavci je výslovně jiný než zdejší
výběr pevného počtu bodů. Žádný nový nález ani kandidát.
