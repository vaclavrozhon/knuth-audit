# D122 — MPR19(a–g), binární číslice a jejich momenty

6. listopadu 2026. Původní celé zadání p14/file34 a odpověď
p372–373/file392–393 zobrazeny, také autorův Pre-Fascicle 5A,
p14/file20 a p29–30/file35–36. Všech sedm zadaných podúloh je
dokázáno níže. Navíc je dokázán každý součet, produkt, mezikrok
a tvrzení o transcendentnosti v odpovědi. **D122 a celá položka19
zůstávají partial pouze kvůli výzkumné poznámce o Eulerově konstantě.**
Bibliografické výjimky jsou uvedeny zvlášť; nejsou matematickým důkazem.

## Model, konečnost a existence všech použitých momentů

Pracujeme na Ω=N₀ s P(X=x)=2^{−x−1}. Normalizace je geometrická
řada ∑_{x≥0}2^{−x−1}=1. Každý výsledek x je konečné nezáporné celé
číslo, a proto má jen konečně mnoho nenulových binárních číslic.
X_n je číslice na pozici n, Y_n je číslice X+1 na stejné pozici.
S=∑X_n, R=⊕X_n a T=∑Y_n jsou tedy bodově dobře definované;
žádná neurčená parita nekonečného počtu jedniček nevzniká.

S≤X a T≤X+1. Generující funkce X je 1/(2−t), |t|<2.
Derivace v t=1 dávají EX=1, E[X(X−1)]=2, tedy EX²=3.
Proto ES²≤3 a ET²≤E(X+1)²=6. Všechny následující výměny
očekávání a nezáporných řad lze provést Tonelliho větou; pro rozdíly,
rozptyly a limity druhých momentů máme navíc tyto integrabilní meze.

## (a) Každá marginála, její binární zápis a odkaz na masky

Položme q=2^n. Číslice X_n je 1 právě pro
x=(2r+1)q+s, r≥0, 0≤s<q. Proto

    p_n=EX_n
       =∑_{r≥0}∑_{s=0}^{q−1}2^{−(2r+1)q−s−1}
       =2^{−q}(1−2^{−q})/(1−2^{−2q})
       =(2^q−1)/(2^{2q}−1)=1/(2^q+1).

Všechny řady jsou nezáporné a geometrické; q≥1 a jejich jmenovatele
jsou nenulové. V binárním zlomku p_n=∑_x X_n(x)2^{−x−1} jsou číslice
právě hodnoty bitu n po sobě jdoucích celých čísel. Dostáváme
0.010101…, 0.00110011…, 0.0000111100001111… pro n=0,1,2.
Obecně se opakují bloky q nul a q jedniček. Součet jejich geometrické
řady je znovu (2^q−1)/(2^{2q}−1). Jelikož jmenovatel po zkrácení
2^q+1 je lichý a větší než 1, nevzniká dvojznačnost končícího zápisu.

Přímo byl zobrazen citovaný vztah 7.1.3(47), 4A p141/file158.
Jeho maska μ_n=−1/(2^{2^n}+1) má při čtení od nejnižšího bitu
bloky jedniček a nul, každý délky q. Platí racionální vztah p_n=−μ_n;
reflexe směru zápisu a doplnění bitů vysvětlují uvedené binární zlomky.
Nezaměňujeme 2adickou masku s reálnou řadou bez konvergence.

## (b) Každý konečný vzor a úplná nezávislost

Pro zadané x₀,…,x_{n−1}∈{0,1} položme
l=∑_{j<n}x_j2^j a L=2^n. Vzor je ekvivalentní X=l+rL, r≥0,
takže

    P(X₀=x₀,…,X_{n−1}=x_{n−1})
      =2^{−l−1}/(1−2^{−L})
      =2^{L−1−l}/(2^L−1).

Čitatel odpovídá přesně knižnímu exponentu
(x̄_{n−1}…x̄₀)₂=L−1−l. Součin marginál je

    ∏_{j<n} p_j^{x_j}(1−p_j)^{1−x_j}
      =2^{∑_{j<n}2^j(1−x_j)} / ∏_{j<n}(1+2^{2^j})
      =2^{L−1−l}/(2^L−1).

Poslední jmenovatel plyne z konečné identity
∏_{j<n}(1+t^{2^j})=(1−t^{2^n})/(1−t), pro t=2. Identitu
dokazuje opakované použití (1−u)(1+u)=1−u²; nedělíme nulou.
Všechny vzory mají součinové pravděpodobnosti, tedy celá rodina
X₀,…,X_{n−1} je nezávislá. Jakoukoli konečnou podrodinu zahrneme
do dost dlouhého prefixu a vynechané bity vysčítáme. Tím je doložena
i nezávislost celé spočetné rodiny v obvyklém konečném smyslu.
Prázdný prefix n=0 má pravděpodobnost a prázdný součin 1.

Knižní AND/complement popis masek říká totéž koeficientově:
průnik příslušných bitových indikátorů vybere právě třídu l modulo L.
Nejde o tvrzení, že obyčejný součin racionálních čísel je operace AND.
Lukacsův odkaz 1960, p119 nebyl rychle dostupný; je výslovně vynechán.

## (c) Nekonečný součet, rozptyl a skutečný obsah odkazu 41(c)

Tonelli dává ES=∑_{n≥0}p_n. Pro S_N=∑_{n<N}X_n plyne
z právě prokázané nezávislosti var S_N=∑_{n<N}p_n(1−p_n).
Protože S_N→S a 0≤S_N²≤X² s EX²=3, dominovaná konvergence
dává ES_N→ES a ES_N²→ES². Po limitě

    ES=∑_{n≥0}1/(2^{2^n}+1),
    var S=∑_{n≥0}2^{2^n}/(2^{2^n}+1)².

Zobrazeny byly skutečné 4A p187/file204 a odpověď p589/file606,
úloha 7.1.3–41(c). Její vztah lze také přímo dokázat: pro |z|<1
je generující funkce bitu n

    ∑_{x≥0}X_n(x)z^x
      =z^q(1+z+⋯+z^{q−1})/(1−z^{2q})
      =z^q/((1−z)(1+z^q)),       q=2^n.

Součtem přes n dostaneme

    ∑_{x≥1}ν(x)z^x=∑_{n≥0}z^{2^n}/((1−z)(1+z^{2^n})).

Absolutní konvergenci dvojité řady zaručuje ν(x)≤x a ∑x|z|^x<∞.
Při z=1/2 je třeba násobit 1/2, neboť P(X=x)=z^x/2; výsledkem
je přesně ES výše. Citovaný vztah tedy opravdu platí pro tento model.
Polynomické/racionální masky μ_n(z) v odpovědi 4A mají tuto hodnotu
pro |z|<1. Jejich formální racionální dosazení z=2 dává 2adickou
masku, nikoli konvergentní reálný součet v z=2.

## (d) Parita, nekonečný produkt, reciproká řada a transcendentnost

Pišme τ(x)=ν(x) mod 2. Pak R=τ(X) a

    ER=∑_{x≥0}τ(x)2^{−x−1}=(0.0110100110010110…)₂.

Prvních 16 vytištěných bitů vzniká přímo z parit x=0,…,15;
nejsou odhadnuty numerickou expanzí aproximace. Z konečného rozvoje
součinu ∏_{j<N}(1−z^{2^j}) a jednoznačnosti binárního zápisu dostaneme,
po absolutně konvergentní limitě pro |z|<1,

    F(z)=∏_{j≥0}(1−z^{2^j})=∑_{x≥0}(−1)^{τ(x)}z^x.

Proto E(−1)^R=F(1/2)/2=1−2ER, čili

    ER=1/2−P/4,       P=∏_{j≥0}(1−2^{−2^j}).

Konvergence, analytické vlastnosti F a kladnost P jsou podrobně
dokázány v `notes/sequential-mpr-ex019-transcendence.md`, §1.
Protože R je bit, R²=R a var R=(ER)(1−ER).

Také tištěná dodatečná reciproká řada má přesný teleskopický důkaz.
Položme a_k=2^{2^k}, D_k=∏_{j<k}(a_j−1), A_k=a_k/2 a P_k=D_k/A_k.
Prázdný součin D₀=1, a₀=2. Pro

    H_k=(a_k−1)/(2D_k)=1/P_k−1/(2D_k)

platí a_{k+1}=a_k², D_{k+1}=D_k(a_k−1), tedy

    H_{k+1}−H_k
      =(a_k+1)/(2D_k)−(a_k−1)/(2D_k)=1/D_k.

H₀=1/2. Součet pro k<N dává
1/P_N−1/(2D_N)=1/2+∑_{k<N}1/D_k. Pro N≥1 je D_N≥3^{N−1},
a proto D_N→∞ a řada konverguje. Po limitě dostáváme přesně

    1/P−1/2=∑_{k≥0}1/∏_{j<k}(2^{2^j}−1).

První dva členy řady jsou oba 1; dolní index 0 tedy není omyl.

Transcendentnost ER je dokázána celá v samostatné poznámce:
nejprve transcendentnost funkce F z radiálních nul ve všech dyadických
kořenech jednotky; potom pomocný celočíselný polynom vysokého řádu
nuly, iterace F(z)=(1−z)F(z²) a nenulový celočíselný resultant.
Pro předpokládaný algebraický stupeň d stačí N=2d a řád
M=N²+2N>2Nd. Nezůstává zde převzatá neověřená Mahlerova věta.

## Jediná krátká číselná kontrola a její úplný ocas

`verify_mpr019_numeric.py` byl spuštěn jednou s nice 15;
`results/sequential/mpr-019-numeric.json` uchovává přesné racionální
intervaly, čas 0.0008363639935851097 s a prioritu 15. Žádný restart.
Použito bylo jen prvních osm členů. Pro r=2^{−2^8} platí

    ∑_{j≥8}2^{−2^j}=∑_{i≥0}r^{2^i}≤r/(1−r),

protože 2^i≥i+1. Tím je shora omezen ocas ES i var S. Pro produkt
P je ocas mezi 1−r/(1−r) a 1, z konečné nerovnosti
∏(1−u_j)≥1−∑u_j a limity. Interval ER plyne afinně z produktu;
interval jeho rozptylu využívá růst t(1−t) na [0,1/2]. Interval
var T používá dokázaný vzorec z části (g) a monotónnost t² pro t≥0.

Všechny rozhodující nerovnosti i porovnání se středem zaokrouhlovacího
intervalu jsou racionální. Decimal slouží pouze k čitelnému výpisu.
Potvrzeny jsou ES≈0.59606, var S≈0.44148, var R≈0.242336,
var T≈0.17237 a všech 40 desetinných míst vytištěného ER.
Knižní konec „30895−“ je správný: zaokrouhlené číslo leží nad ER;
nejde o chybnou truncaci konce „30894…“. Stejný malý běh přímo
ověřil čtyři vytištěné šestnáctibitové prefixy. Jeho konečný rozsah
nenahrazuje obecné argumenty výše.

## (e) Událost pro π a přesně vymezená Eulerova otázka

Je-li π iracionální, nemůže mít konečný binární rozvoj. Má tedy
nekonečně mnoho číslic p_n=1. Každý výsledek X má konečně mnoho
jedniček, takže požadovaná událost je dokonce prázdná a má
pravděpodobnost 0. Alternativní eventualita samých jedniček
by také znamenala racionální číslo, a u π proto nenastává.

Pro úplnost zde lze doložit i použitou iracionalitu π, bez odkazu na
nepročtený výsledek. Předpokládejme π=a/b s kladnými celými a,b a
položme f_n(x)=x^n(a−bx)^n/n!. Derivace v nule jsou celá čísla:
nenulový koeficient u x^{n+j} se po derivování násobí (n+j)!,
takže jeho jmenovatel n! se vykrátí. Rovnost f_n(π−x)=f_n(x)
ukazuje totéž pro derivace v π. Položme

    G_n=f_n−f_n″+f_n⁽⁴⁾−⋯+(−1)^n f_n⁽²ⁿ⁾.

Pak G_n+G_n″=f_n. Integrace derivace G_n′sin x−G_n cos x dává

    I_n=∫₀^π f_n(x)sin x dx=G_n(π)+G_n(0),

kladné celé číslo. Avšak 0≤f_n(x)≤(bπ²/4)^n/n!, takže
0<I_n≤2(bπ²/4)^n/n!→0. Spor. Tím je potřebná iracionalita π
skutečně odůvodněna, nikoli pouze uvedena jako název věty.

Pro Eulerovu konstantu γ je přesná podmínka jiná, než pouhé obecné
slovo „iracionalita“. U kanonického binárního rozvoje (bez konce
samých jedniček) je pravděpodobnost 0, pokud rozvoj má nekonečně
mnoho jedniček. Pokud končí, pak pro K=∑_n p_n2^n je pravděpodobnost
2^{−K−1}>0. Jde tedy o otázku, zda γ je dyadické racionální číslo.
Racionální číslo s jiným jmenovatelem by zde také mělo pravděpodobnost 0.

Kniha tuto otázku označuje za nevyřešenou. Primární preprint
[Kalisch et al., 9. října 2026](https://arxiv.org/abs/2610.13919)
v abstraktu uvádí, že iracionalita γ není dokázána. To ověřuje širší
výzkumný kontext, **nikoli samo o sobě otevřenost užší dyadické otázky**.
Tuto užší otázku zde neřešíme ani nevydáváme za prokázaně rozhodnutou.
Přesná redukce je dokázána, vlastní výzkumná poznámka zůstává partial.
Článek nebyl celý matematicky auditován; přečtena byla metadata
a abstrakt. Z této otevřené poznámky nevytváříme podezření na erratum.

## (f) Posunuté rozdělení a závislost číslic Y

Pišme Y=X+1. Pro k≥1 je P(Y=k)=2P(X=k), zatímco P(Y=0)=0.
Jako míry na N₀ tedy přesně platí P_Y=2P_X−δ₀.

Každý nekonečný bitový řetězec s konečně mnoha jedničkami určuje
jediné k. Pro k=0 je P_X=1/2 a dvojnásobek modulo 1 je 0;
pro k≥1 je P_X<1/2 a dvojnásobek se modulo 1 nemění. Řetězec
s nekonečně mnoha jedničkami má u obou rozdělení pravděpodobnost 0.
To dokazuje přesně knižní tvrzení pro **každý** nekonečný řetězec

    P(Y₀Y₁…=x₀x₁…)=2P(X₀X₁…=x₀x₁…) mod 1.

Knižní posun binárního zápisu doleva je zde posun zápisu těchto
pravděpodobností; netvrdí mylnou rovnost X+1=2X.

Pro každou nezápornou nebo integrabilní h s h(0)=0 plyne z měr
Eh(Y)=2Eh(X). Použitím bitových funkcí dostaneme E Y_n=2p_n.
Použitím jejich součinu pro m≠n a nezávislosti X z (b) dostaneme

    E(Y_mY_n)=2E(X_mX_n)=2p_mp_n=(EY_m)(EY_n)/2,
    covar(Y_m,Y_n)=−(EY_m)(EY_n)/2<0.

Kladnost p_n z (a) zaručuje ostrou zápornost pro všechny různé
pozice. Zejména E(Y₀Y₁)=2/15, ale (EY₀)(EY₁)=4/15,
takže požadovaná dvojice nezávislá není. Pro m=n platí stále
E(Y_m²)=2E(X_m²); nepoužívá se pak součin marginál.

## (g) Oba momenty T a každý krok rozptylu

Funkce h(k)=ν(k) i h(k)=ν(k)² mají h(0)=0. Všechny momenty
jsou konečné podle úvodní meze, takže měrová identita dává

    ET=2ES,       ET²=2ES².

To souhlasí také s tištěným odvozením dvojitou sumou: Tonelli
umožňuje sumovat E(Y_mY_n)=2E(X_mX_n) přes všechna m,n,
včetně diagonály. Proto

    var T=2ES²−(2ES)²
         =2(var S+(ES)²)−4(ES)²
         =2 var S−2(ES)²≈0.17237.

Nezávislost číslic Y se zde nikde nepředpokládá. Jejich záporné
kovariance z (f) jsou se zmenšením rozptylu konzistentní.

## Prameny, errata a rozsah uzavření

Původní sazba i autorův PS souhlasí ve všech výše prověřených
formulích. Šest textových vrstev errat a tři zdrojové TeX soubory
byly prohledány podle původních i fasciklových stran, čísla19 a
pojmových hesel. Relevantní nová oprava nebyla nalezena;
`results/sequential/mpr-019-binary-errata.json` uchovává dotazy,
kontext a hashe. Sousední oprava bibliografie18 je již E120,
fasciklové změny21 a24 nejsou změnou této úlohy.

[HAKMEM, Item122](https://www.inwap.com/pdp10/hbaker/hakmem/series.html)
byl přečten ve veřejném přepisu původního reportu. Souhlasí vztah
paritních bitů a produktu; jeho historické váhání o autorství
transcendentnosti není převzato jako důkaz. Metadata autorů,
reportu239 a února1972 odpovídají
[primárnímu katalogu MIT](https://dspace.mit.edu/handle/1721.1/6086).
Originální PDF vracelo HTTP429 a nebylo opakovaně stahováno.
Přepis je výslovně označen jako draft z roku1995, nikoli jako
ověřený faksimile původní sazby.

Mahlerův sken1929, p342,343,366, byl zobrazen; p343 skutečně
obsahuje použitý produkt a funkční rovnici. Celý historický důkaz
ani původní oprava1930 nebyly převzaty. Lukacs1960 p119, originální
HAKMEM sazba a znění opravy1930 jsou explicitní bibliografické výjimky.
Matematické tvrzení o transcendentnosti má úplný nezávislý důkaz.

Část19(a,b) na file392 je tím uzavřena; sama tato strana zůstává
partial kvůli C046 u úlohy8. Na file393 jsou dokončeny všechny
matematické části19(c–g) kromě uvedené Eulerovy výzkumné poznámky,
a dřívější odpověď20. Ostatní odpovědi na file393 se tím neuzavírají.
File34 zůstává partial pro dosud nezkontrolované21–26. Žádný nový
nález, žádný dlouhý výpočet, žádný restart starého censu.
