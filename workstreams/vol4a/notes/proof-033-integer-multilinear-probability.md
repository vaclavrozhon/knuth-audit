# §7.1.1–12 a 13: celočíselný rozvoj a celá reálná krychle

6. listopadu 2026, X0063. Zadání p80/file97; odpovědi p535–536,
file552–553. Originály images/file097.png, proof-file552.png,
proof-file553.png. Číselný program ani enumerace se nespouštěly.
Rozlišujeme booleovskou funkci f od jejího polynomu F na reálných
vstupech. U koeficientové meze je níže výslovný nulární okraj.

## P0577: existence, jednoznačnost a úvodní příklad úlohy 12

Pro a∈{0,1}ⁿ definuj váhu
λ_a(x)=∏_(j:a_j=1)x_j · ∏_(j:a_j=0)(1−x_j).
Na booleovském vrcholu b je λ_a(b)=[a=b]. Proto

    F(x)=Σ_a f(a) λ_a(x)

má celočíselné koeficienty, je multilineární a na každém vrcholu
se rovná f. Při n=0 jde o jedinou prázdnou váhu 1 a konstantu f().

Jedinečnost nad celými nebo reálnými čísly: každý multilineární
polynom se jednoznačně dělí na G(u)+xₙH(u). Jeho hodnoty na
posledních vrstvách 0/1 určují G=P(u,0) a H=P(u,1)−P(u,0).
Indukce od nulární konstanty proto vylučuje dva různé polynomy
se stejnými vrcholovými hodnotami. Nejde o modulo 2.

Úvodní příklad převádějící (19) na
1−xy−xz−yz+3xyz je správný: při vahách vstupu 0,1,2,3 dává
postupně 1,1,0,1, tedy právě booleovský polynom
1⊕xy⊕xz⊕yz⊕xyz. Mintermový rozvoj i tato jednoduchá kontrola
všech čtyř symetrických případů dávají stejnou jedinečnou funkci.

## P0578: úloha 12(a), celý vytištěný polynom

Pro funkci (22) je při w=0 tabulka 11001001. Při y=0 je
hodnota 1−xz a při y=1 je xz. Celočíselný polynom této větve je

    A(x,y,z)=(1−y)(1−xz)+y·xz
            =1−y−xz+2xyz.

Při w=1 je funkce x. Proto F=(1−w)A+wx, a rozepsáním dostáváme

    F=1−y−xz+2xyz−w+wy+wx+wxz−2wxyz,

přesně odpověď. Dosazování 1−x za komplement v úplných mintermech
dává totéž: na booleovských vrcholech jsou mintermy disjunktní,
takže jejich OR je jejich obyčejný součet. Na celé krychli jde
o jejich interpolující součet, nikoli obecnou aritmetizaci OR.

## P0579: celočíselné koeficienty a tříproměnný dodatek 12(b)

Pro F(x)=Σ_S a_S ∏_(j∈S)x_j platí f(1_T)=Σ_(S⊆T)a_S. Inverze je

    a_U = Σ_(T⊆U) (−1)^{|U|−|T|} f(1_T).

Po dosazení pravé strany se koeficient libovolného a_S rovná
Σ_(S⊆T⊆U)(−1)^{|U|−|T|}=(1−1)^{|U∖S|}; přežije právě S=U.
To je obecný důkaz, včetně U=∅, kdy a_∅=f(0).

Tříproměnný zápis v odpovědi má proto koeficienty
f₀₀₀,f₀₀*,f₀*₀,f₀**,f*₀₀,f*₀*,f**₀,f***
u členů 1,z,y,yz,x,xz,xy,xyz, kde hvězdička nyní znamená
příslušný střídavý rozdíl. Například

    f**₀=f(1,1,0)−f(1,0,0)−f(0,1,0)+f(0,0,0).

Tento znakový vzorec i všechny ostatní koeficienty vyplývají
z jedné obecné inverze, nikoli z extrapolace jediného příkladu.

## P0580: ostrá horní mez a explicitní limit nulární arity

Pro neprázdné U, |U|=k, má koeficientový součet právě 2^{k−1}
kladných a 2^{k−1} záporných znamének. Každá vrcholová hodnota
je 0 nebo 1, tudíž |a_U|≤2^{k−1}. Konstantní člen splňuje
|a_∅|≤1. Při n≥1 tedy mají všechny koeficienty absolutní hodnotu
nejvýše 2^{n−1}.

To je úplný důkaz pro **n≥1**. Kniha dříve výslovně pracuje i
s nulárními funkcemi. Pokud by se vytištěná věta „arbitrary n-ary
function“ v odpovědi vztahovala doslova také na n=0, konstanta 1
má koeficient 1, zatímco 2^{−1}=1/2. Úplná mez pro n≥0 je
max(1,2^{n−1}), popřípadě samostatná nulární věta |a_∅|≤1.
Tento drobný doménový bod zůstává v P0580 označen **partial**;
pozitivně aritní tvrzení je prokázané. Nezakládám samostatnou
kartu nálezu a neskrývám předpoklad n≥1 v označení checked.

## P0581: dosažitelnost meze a celý symetrický polynom parity

Pro n≥1 a booleovské x má součin ∏_j(1−2x_j) hodnotu
(−1)^{Σx_j}. Proto

    P(x)=(1−∏_j(1−2x_j))/2

dává právě XOR všech vstupů. Po roznásobení je

    P=e₁−2e₂+4e₃−…+(−2)^{n−1}eₙ,

kde e_k je součet všech součinů k různých proměnných.
U každého neprázdného S je koeficient (−2)^{|S|−1};
nejvyšší tedy má absolutní hodnotu 2^{n−1}. Horní mez je
dosažena a výrok o maximu není pouze odhad. n=1 dává P=x₁
s koeficientem 1, jak má.

## P0582: přesný Hadamardův vztah po známé opravě

All4a-pre, oprava 28. 11. 2013, nahrazuje původní tvrzení o celé
expanzi tvrzením o jednotlivém koeficientu s k hvězdičkami.
Vlastní read-only výřez svazku 2, p501/file513, obsahuje původní
rovnici §4.6.4–(38):

    H_g(s)=Σ_(t∈{0,1}^k) (−1)^{Σ_j s_j t_j} g(t).

Zdroj books/taocp-vol2-ed3-print1-1997.djvu, edice3/dotisk1;
uloženy pouze vlastní sources/proof-vol2-file513-p501.pdf a
images/proof-vol2-p501.png. Žádný soubor svazku 2 nebyl měněn;
jeho celá stránka ani algoritmus transformace se tím neaudituje.

Omez f na souřadnice U a ostatní nastav na nulu, čímž vznikne h.
P0579 říká a_U=(−1)^k H_h(1,…,1). Pokud místo h použijeme
g(t)=h(1−t), pak přesně a_U=H_g(1,…,1), bez globálního znaménka.
To je explicitní transformovaný koeficient odpovídající opravené
větě. Celý vektor multilineárních koeficientů není zaměněn
s jedinou plnou Hadamardovou transformací původní tabulky.

Historické přejmenování Walsh/Hadamard v erratech svazku 2
nemění zkontrolovanou rovnici; priorita těchto názvů se zde neřeší.

## P0583: úloha 12(c), všechny reálné vstupy krychle

Pro 0≤x_j≤1 je každá λ_a(x) nezáporná a

    Σ_a λ_a(x)=∏_j (x_j+(1−x_j))=1.

F je proto vážený průměr čísel f(a)∈{0,1}, tedy 0≤F(x)≤1.
Nejde jen o argument na vrcholech. Při hraničních x_j=0 nebo1
některé váhy zmizí; součet stále zůstává 1. Pro n=0 je jediná
váha 1, takže výrok platí i tam.

## P0584: úloha 12(d), uspořádání se zachová v celé krychli

Jsou-li f(a)≤g(a) na všech booleovských vrcholech, potom

    G(x)−F(x)=Σ_a (g(a)−f(a)) λ_a(x) ≥ 0

pro každé x∈[0,1]ⁿ. Všechny členy jsou nezáporné. Tím je
doložen přesně požadovaný přenos z vrcholů do celého spojitého oboru.

## P0585: úloha 12(e), monotónnost polynomu

Pro kteroukoli souřadnici j rozděl polynom na
F(x)=(1−x_j)G(x_{−j})+x_jH(x_{−j}), kde G,H jsou celočíselné
reprezentace booleovských cofactorů při x_j=0 a 1.
Monotónnost f na vrcholech dává G≤H na všech zbývajících vrcholech;
P0584 ji prodlouží na celou menší krychli. Proto

    ∂F/∂x_j = H−G ≥ 0.

Lze se obejít i bez integrační věty: zvýšení x_j na y_j při
pevných ostatních souřadnicích změní F o (y_j−x_j)(H−G)≥0.
Zvyšuj souřadnice postupně; pro každé 0≤x≤y≤1 tak vyjde F(x)≤F(y).
To dokazuje všechny vstupy i hranice, ne pouze kladnost derivace
v izolovaném bodě. Nulární případ je konstantní a triviální.

## P0586: úloha 13 a její přesná pravděpodobnostní interpretace

Předpoklad zadání je vzájemná nezávislost jednotek, nikoli jen
zadané jednotlivé pravděpodobnosti p_j∈[0,1]. Pro stavový vektor
a je proto pravděpodobnost právě λ_a(p). Událost f=1 je disjunktní
sjednocení stavů s f(a)=1, takže

    Pr(f=1)=Σ_a f(a) λ_a(p)=F(p).

Je to **právě** již jednoznačný celočíselný multilineární polynom,
jak tvrdí odpověď, nikoli jen nějaký multilineární pravděpodobnostní
výraz. Krajní pravděpodobnosti 0/1 i nulární případ jsou přípustné.

Příklad v zadání x₁∧(¬x₂∨¬x₃) skutečně znamená pracující první
jednotku a alespoň jednu selhávající z dalších dvou; jeho dostupnost
je p₁(1−p₂p₃). Symetrická S₃ značí právě tři pracující jednotky,
její dostupnost je součet λ_a(p) přes |a|=3, případně prázdná nula
pro n<3. Tyto slovní modelové příklady nezůstaly bez argumentu.

## Meze, stránka 535 a pokračování

Všechny matematické části 12(a)–(e) a 13 mají argumenty výše.
P0580 ponechává výslovný nulární rozsah partial; žádný nový nález
nebo kandidát není vytvořen. Pět relevantních vrstev errat bylo
pro tento blok zohledněno; známý Hadamardův text se nepřičítá
k nálezům. Historické názvy polynomu, Zhegalkinova terminologie
a autorství zůstávají bibliografickou výjimkou.

Celá **p535/file552** nyní má přesnou obsahovou mapu:
úloha5 P0557–P0561/proof-030; 6–7 P0562–P0567/proof-031;
8–11 P0568–P0576/proof-032; začátek12 a celá odpověď12(a)
P0577/P0578 v tomto souboru. Na p535 není koeficientová mez
12(b), která začíná až na p536. Bibliografie Bernstein/Schröder/
Jevons/Zhegalkin je samostatně výslovně přeskočena.
P536 zůstává partial, protože obsahuje úlohy 14–21 a nulární
doménový bod P0580. P80 také zatím není celá: pokračuje úlohou14.

Další úloha14: optimální self-dual rozhodnutí podle pravděpodobností,
pak 15 a následující. Hlavní text p54/file71 a parity P0526
zůstávají v odděleném kurzoru.
