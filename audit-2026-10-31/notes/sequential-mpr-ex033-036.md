# D135–D138 — celé MPR33–36

6.–7. listopadu2026. Původní zadání p15/file35 a odpovědi
p376/file396 jsou přímo zobrazeny, také autorův Pre-Fascicle5A
p15/file21 a p33/file39. Konvence nulového podmínění z p3
je převzata přesně z D094 a uzavřeného C045; dřívější důkaz
věžové identity z D100 se nepřepočítává. Níže je celý nový
rozsah každé úlohy, včetně tištěných mezikroků.

Pracujeme ve spočetném diskrétním modelu z p1. Pro rovnosti
konečných očekávání předpokládáme příslušnou integrabilitu,
jak vyžaduje definice(7). Podíl při podmínění se používá jen
na kladném vlákně. Na nulové události autor stanoví
E(U|A)=EU; ve vzorcích níže se takové vlákno nikdy nedělí nulou.

## D135, 33: všechna vlákna a rozdělení nové proměnné

Z G(w,z)=E(w^Xz^Y)=pw+qz+rwz, kde p,q,r>0 a p+q+r=1,
čteme právě tři kladné atomy

    (X,Y)=(1,0),(0,1),(1,1),    hmotnosti p,q,r.

Čtvrtý binární atom(0,0) má hmotnost0. Marginální hmotnosti
Y jsou p a q+r; obě jsou kladné. Proto

    E(X|Y=0)=1,
    E(X|Y=1)=(0·q+1·r)/(q+r)=r/(q+r)=:a.

Máme0<a<1. Náhodná proměnná U=E(X|Y) má tedy hodnotu1
na prvním atomu a hodnotu a na druhém i třetím. Pro reálné z>0

    E(z^U)=p z+(q+r)z^a.

Součet hmotností je1; derivace tohoto výrazu v z=1 je
p+(q+r)a=p+r=EX, v souladu s(12). Protože oba exponenty
jsou kladné, výraz má také spojitou hodnotu0 v z=0.
Pro obecné komplexní z by bylo nutné zvolit větev z^a;
pro zadaný výpočet nic takového není potřebné.

Toto zpravidla není obyčejná mocninná řada s celočíselnými
exponenty, přestože původní X,Y byly binární. Například
p=q=r=1/3 dává a=1/2. V tomto přesném smyslu je doložen
vysvětlující dovětek o nevhodnosti obvyklých jednorozměrných
generujících funkcí pro podmíněné náhodné proměnné.
Není z něj činěn zákaz jiných transformací reálných proměnných
ani tvrzení, že každé podmíněné očekávání je neceločíselné.

## 33: každý koeficient obecného vzorce

Pro společnou distribuci nezáporných celých X,Y pišme
p_{j,k}=Pr(X=j,Y=k). Je-li EX konečné, pak

    G(w,z)=∑_{j,k≥0}p_{j,k}w^jz^k,
    [z^k]G(1,z)=∑_j p_{j,k}=Pr(Y=k),
    [z^k](∂G/∂w)(1,z)=∑_j j p_{j,k}=E(X[Y=k]).

Derivuje se podle w před dosazením w=1. U konečné binární
distribuce jde jen o polynom. Obecně lze derivovat pro0≤w<1
a přejít monotónně k1; nezáporné členy a konečné EX opravňují
také seskupení podle k. Tím je plně doložen tištěný čitatel.
Pro Pr(Y=k)>0 dává jeho podíl s jmenovatelem E(X|Y=k).
Pro nulovou marginální hmotnost se podle dřívější konvence
použije EX; podíl0/0 není samostatnou novou definicí.

V tomto konkrétním příkladu jsou G(1,z)=p+(q+r)z a
(∂G/∂w)(1,z)=p+rz. Koeficienty k=0,1 vracejí přesně1,a.
Pro jiná k je vlákno nulové. Podmínky p,q,r>0 zaručují,
že oba skutečně použité podíly mají kladný jmenovatel.

## D136, 34: každý přechod dvojnásobného součtu

Položme p_ω=Pr(ω), Ω₊={ω:p_ω>0}, B_y={ω:Y(ω)=y}
a q_y=Pr(B_y). Ze všech očekávání lze odstranit body mimoΩ₊,
protože mají nulovou váhu. Pro ω∈Ω₊ je q_{Y(ω)}≥p_ω>0.
Definice(13), čtená s konvencí z D094, proto dává

    E(E(X|Y))
      =∑_{ω∈Ω₊}p_ω∑_{ω′∈Ω₊}
          X(ω′)p_{ω′}[Y(ω′)=Y(ω)]/q_{Y(ω)}.

Když indikátor není0, jsou oba y stejné; když je0, celý
člen je0 a oba jmenovatele naΩ₊ jsou kladné. Můžeme tedy
ve všech členech přesně nahradit q_{Y(ω)} za q_{Y(ω′)},
jak činí druhý řádek odpovědi. Pro absolutní hodnoty máme

    ∑_{ω,ω′∈Ω₊}p_ω |X(ω′)|p_{ω′}
        [Y(ω′)=Y(ω)]/q_{Y(ω′)}
      =∑_{ω′∈Ω₊}|X(ω′)|p_{ω′}
         (∑_{ω:Y(ω)=Y(ω′)}p_ω)/q_{Y(ω′)}
      =E|X|<∞.

V první změně pořadí pro absolutní hodnoty lze použít Tonelli;
výsledná konečnost potom opravňuje změnu pořadí původní řady.
Dostáváme tištěný třetí řádek

    ∑_{ω′∈Ω₊}X(ω′)p_{ω′}
        ∑_{ω∈Ω₊}p_ω[Y(ω)=Y(ω′)]/q_{Y(ω′)}.

Vnitřní součet je q_{Y(ω′)}/q_{Y(ω′)}=1; výsledek je EX.
Nulová vlákna, kde E(X|Y)=EX podle autorovy konvence, do
vnějšího očekávání přispívají0. Tím je algebraické odvození(12)
z(7),(13) úplné, ne jen převzetí již známého tvrzení.

## D137, 35(b): celý protipříklad

Vezměme čtyři dvojice(X,Y)∈{0,1}², každou s hmotností1/4,
a Z=X. Pro obě hodnoty Y mají X=0 a1 podmíněnou hmotnost1/2,
takže E(X|Y)=1/2 jako konstanta. Podmíněním konstanty na Z
získáme stále1/2, zatímco E(X|Z)=X, protože Z=X.
Rozdíl je+1/2 na obou atomech X=0 a−1/2 na obou atomech X=1.
Tvrzení(b) tedy selže s pravděpodobností1; nejde o nulovou výjimku.

## 35(*), 35(a) a skutečný odkaz91

Správná věžová identita

    E(E(X|Y,Z)|Z)=E(X|Z)                         (*)

byla již dokázána z absolutně konvergentních podmíněných
součtů v notes/sequential-mpr-009-010.md pro D100/úlohu91.
Přebíráme právě tento důkaz a jeho potřebnou integrabilitu X.
Pro úplné spárování s tištěným krokem: v každém kladném
vlákně Z=z tvoří Y rozklad podmíněného prostoru. Použití
již dokázané(12) v tomto prostoru dává pravou stranu(*).
Nulová společná vlákna mají v tomto průměru nulové váhy.
Při Pr(Z=z)=0 jsou obě strany podle konvence EX, protože
E(E(X|Y,Z))=EX; také zde není rozpor.

Dosazení Z=Y v(*) dává část(a): vektor(Y,Y) má právě stejná
vlákna jako Y, a tudíž E(X|Y,Y)=E(X|Y). Je tedy pravda
E(E(X|Y)|Y)=E(X|Y). To ověřuje i tištěnou větu o této instanci.
Odkaz91 je už úplně pokryt D100: obecný podmíněný součet
Q po rostoucích historiích tvoří martingale právě použitím(*).
Celá91 se znovu nepočítala ani neotevírala.

## D138, 36(a): funkce známé proměnné a přesný nulový okraj

Nechť f(X) je integrabilní. Na každém kladném vlákně X=x
je f(X) konstantní f(x), takže

    E(f(X)|X=x)=f(x),
    Pr(E(f(X)|X)=f(X))=1.

To je obvyklý pravděpodobnostní význam vytištěného f(X).
Pokud se ponechají v Ω také nulové body a vyžaduje se
bodový reprezentant na celé Ω, autorova konvence dává přesně

    E(f(X)|X)(ω)=f(X(ω)), pokud Pr(X=X(ω))>0,
                  E f(X), pokud Pr(X=X(ω))=0.

Na nulovém vlákně proto netvrdíme dodatečnou bodovou rovnost
s libovolně předepsanou hodnotou f(X(ω)). Výsledná náhodná
proměnná je s f(X) rovna s pravděpodobností1. Tato standardní
volnost nulových reprezentantů není nový nález ani návrat k C045.
Je zde zapsaná výslovně, aby se důkaz netvářil jako silnější
bodové tvrzení, než jaké je pro očekávání oprávněné.

## 36(b): všechny součty, integrabilita a generalizace(12)

Předpokládejme E|g(X)|<∞ a E|f(Y)g(X)|<∞; v konečném
modelu s konečnými hodnotami funkcí je to automatické.
Pro q_y>0 je

    E(g(X)|Y=y)=∑_x g(x)Pr(X=x,Y=y)/q_y.

Z trojúhelníkové nerovnosti na každém vlákně vyplývá

    ∑_y q_y |f(y)E(g(X)|Y=y)|
      ≤∑_{x,y}|f(y)g(x)|Pr(X=x,Y=y)<∞.

Levá náhodná proměnná je tudíž integrabilní; oba tištěné
součty lze seskupovat v libovolném pořadí. Přímo dostáváme

    E(f(Y)E(g(X)|Y))
      =∑_y f(y)E(g(X)|Y=y)q_y
      =∑_{x,y}f(y)g(x)Pr(X=x,Y=y)
      =E(f(Y)g(X)).

V nulových vláknech je první člen0, i když je podmíněná
hodnota definována jako E g(X); ve společném součtu jsou
všechny odpovídající hmotnosti rovněž0. Je tedy pokryt i
tento tištěný mezikrok. Nastavením f≡1,g(x)=x dostaneme
právě(12), čímž je ověřena věta o zobecnění.

## Rozsah a zdroje

Všechny čtyři celé úlohy jsou checked/reviewed. D094 a D100
jsou převzaty pouze v přesném doloženém rozsahu, staré důkazy
a výsledky zůstávají beze změny. C045 zůstává dismissed.
PDF+PS a6errat+3TeX byly zkontrolovány; jiné sekce mají
opravy čísel33–35, ale žádná se netýká tohoto MPR bloku.
Přesné kontexty obsahuje mpr-033-036-conditioning-errata.json.
Bibliografická výjimka zde není. Žádný nový nález ani běh.
File35 zůstává partial pro37–40, file396 pro37–38.
