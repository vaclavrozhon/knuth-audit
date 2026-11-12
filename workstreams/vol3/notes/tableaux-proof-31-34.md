# Tableaux31–34: symetrické věže, momenty, Schurovy identity a háčky

Zadání69/file80, celé odpovědi611–612/file622–623. Originály zobrazeny
v images/tableaux-file-080.png, -622.png a -623.png. Zohledněny známé
opravy: doplnění „involution number“ v32 (2005); správný jmenovatel
Δ(k+l,…,0), superfactorial a obě větve důkazu34 (2006); bibliografické
strany Littlewood49–70 (2022). Sazba matematických oprav je zobrazená
v images/tableaux-errata-answers33-35-file029.png. Nejde o nové nálezy.
Pět vrstev je již v sources/tableaux-errata-review.json; nyní byly
znovu cíleně spárovány uvedené stránky a úlohy, bez dalšího výpočtu.

## P0546: úloha31, dvě diagonály a involuce na párech

Rozmístění n neútočících věží je permutace π: v řádku i stojí věž
ve sloupci π(i). Odraz podle hlavní diagonály dává π⁻¹, takže první
symetrie znamená π²=id. Označme r(i)=n+1−i. Druhý odraz dává
rπ⁻¹r, a spolu s první podmínkou tedy přesně πr=rπ.

Reverze r má m=floor(n/2) dvouprvkových orbit a při lichém n jediný
pevný bod. Komutující π musí tento jediný bod fixovat. Na m párech
indukuje involuci σ. Je-li pár pevný pod σ, π na něm buď fixuje oba
prvky, nebo je zamění: dvě možnosti. Jsou-li dva páry zaměněny,
obraz jednoho z jejich prvků určuje komutací druhý obraz; jsou dvě
možnosti a π²=id pak jednoznačně určí zpětné obrazy. Všechny takto
konstruované π naopak mají obě symetrie. Proto x_n=a_floor(n/2).

## P0547: rekurence, exponenciální řada a malý údaj

V konfiguraci na m párech vyberme jeden pár. Buď je pevný (dvě
možnosti a_m−1), nebo je spojen s jedním z m−1 dalších párů (dvě
orientace a_m−2). Tedy a_0=1, a_1=2 a

    a_m=2a_(m−1)+2(m−1)a_(m−2), m≥2.

Pro A(z)=Σa_m z^m/m! dostáváme A′=2A+2zA, A(0)=1, a tedy
A(z)=exp(2z+z²). Již dokázaná involuční řada exp(z+z²/2)
(P0461–0462) dává vytištěný čtverec. Konkrétně a_2=4+2=6,
takže x_4=6. Také x_0=x_1=1 a x_(2m+1)=x_(2m) přesně.

## P0548: momentový integrál pro a_m

Hustota Y se středem2 a rozptylem2 je
g(t)=exp(−(t−2)²/4)/(2sqrt(π)). Všechny absolutní momenty jsou
konečné. Protože g′(t)=−(t−2)g(t)/2, integrace per partes dává

    E Y^(m+1)=2E Y^m+2m E Y^(m−1).

Okrajový člen t^m g(t) v obou nekonečnech mizí; pro m=0 dostaneme
E Y=2 a E1=1. Rekurence P0547 proto určuje

    a_m=(1/(2sqrt(π)))∫_R t^m exp(−(t−2)²/4)dt.          (1)

Záporná polovina integrálu se při lichém m nevynechává bez důkazu.

## P0549: úplný Laplaceův odhad obou polovin bez domněnky o ocasech

Pro t>0 položme

    F_+(t)=m log t−(t−2)²/4,
    F_−(t)=m log t−(t+2)²/4.

Jejich jediné kladné stacionární body jsou
ρ=sqrt(2m+1)+1 a σ=sqrt(2m+1)−1. Pro m>0 jsou to maxima,
protože F_±″(t)=−m/t²−1/2≤−1/2 na celém kladném oboru.
Pro každý pevný u tedy F_+(ρ+u)−F_+(ρ)→−u²/2; totéž pro σ
a F_−. Taylorův zbytek na pevném okolí mizí, neboť
F_±‴(t)=2m/t³=O(m^(−1/2)).

Globální silná konkávnost současně dává

    F_+(ρ+u)−F_+(ρ)≤−u²/4, u>−ρ,

a stejnou mez pro σ. Po rozšíření integrandu nulou na zbývající
část reálné osy je exp(−u²/4) společná integrabilní majoranta.
Dominovaná konvergence proto opravdu dokazuje

    ∫_0^∞ exp(F_+(t))dt ~ sqrt(2π) exp(F_+(ρ)),
    ∫_0^∞ exp(F_−(t))dt ~ sqrt(2π) exp(F_−(σ)).          (2)

Tím je pokryt celý integrál, včetně obou vzdálených ocasů.

## P0550: všechny konstanty v31 a parita n

Pišme N=2m a q=sqrt(N). Z
sqrt(N+1)=q+1/(2q)+O(q^(−3)) plyne

    log ρ=log q+1/q+O(q^(−3)),
    log σ=log q−1/q+O(q^(−3));

člen řádu q⁻² v obou logaritmech se zruší. Dále
(ρ−2)²=N+2−2sqrt(N+1) a (σ+2)²=N+2+2sqrt(N+1).
Odtud

    F_+(ρ)=N log N/4−N/4+sqrt(N)−1/2+O(N^(−1/2)),
    F_−(σ)=N log N/4−N/4−sqrt(N)−1/2+O(N^(−1/2)).

Poměr záporné a kladné poloviny(1) má absolutní velikost
exp(−2sqrt(N)+o(1)) a mizí, ať je m sudé nebo liché.
Faktor sqrt(2π)/(2sqrt(π)) z(1)–(2) je1/sqrt(2). Dostáváme

    x_N ~ exp(N log N/4−N/4+sqrt(N)−1/2−(log2)/2), N sudé.

To je přesně vytištěná asymptotika. Pro liché n se použije N=n−1
a přesná rovnost x_n=x_(n−1); nahrazení N lichým n uvnitř celého
exponentu se bez dalšího netvrdí. Asymptotika se netýká n=0.

## P0551: úloha32, normální momenty se skutečnými hranicemi

Pro X se středem1 a rozptylem1 pišme
φ(t)=exp(−(t−1)²/2)/sqrt(2π), m_n=∫t^nφ(t)dt.
Platí φ′=−(t−1)φ, všechny absolutní momenty jsou konečné a t^nφ(t)
na obou koncích mizí. Integrace per partes tedy pro n≥1 dává

    m_(n+1)−m_n=−∫t^nφ′(t)dt=n m_(n−1).

Pro n=0 je rozdíl0; m_0=1 a m_1=1 (také přímo symetrií t−1).
Je to přesně involuční rekurence P0458, s t_0=t_1=1. Indukcí
m_n=t_n pro každé celé n≥0. Oprava názvu t_n pouze odstraňuje
možnou záměnu s jinými dříve používanými počty.

## P0552: úloha33, determinant a všechna celá a_i

Polynom binom(X,j) má stupeň j a vedoucí koeficient1/j!.
Sloupcové eliminace nižších mocnin proto dávají

    det_(i,j=1)^m binom(a_i,j−1)
      =∏_(i<j)(a_j−a_i)/∏_(r=0)^(m−1)r!
      =Δ(a_1,…,a_m)/Δ(1,…,m).                          (3)

Knižní Δ používá obrácenou orientaci rozdílů; znaménko se v podílu
zruší. Žádná nerovnost ani různost a_i pro determinantovou identitu
není potřeba. Pro záporné a je binom(a,j)=(−1)^j binom(−a+j−1,j)
celé, pro nezáporné a jde o obvyklá celá čísla včetně nul.
Determinant je tedy vždy celé číslo. Opakované a_i dávají0,
prázdný determinant i prázdné Δ dávají1.

## P0553: Schurova specializace a přesný význam počtu členů

Nyní předpokládejme 0<a_1<…<a_m, a_i celá. Tvar
λ_i=a_(m+1−i)−(m+1−i) je nezáporný a slabě klesající, protože
mezery mezi a_i jsou nejméně1. Posunuté délky L_i=λ_i+m−i
jsou a_(m+1−i)−1. Již úplně dokázaná enumerace P0509–0513 dává

    S_λ(1,…,1)=Δ(L_1,…,L_m)/Δ(m−1,…,0)
              =Δ(a_1,…,a_m)/Δ(1,…,m).

Zde S_λ je přesně součet vah semistandardních tableaux: řádky
slabě rostou, sloupce striktně rostou. „Počet členů“ počítá členy
před sloučením stejných monomů, tedy s násobnostmi; příklad níže
má dva stejné monomy. Nulové řádky jsou povolené a nepřidávají buňky.

## P0554: proč je definovaný polynom opravdu symetrický

Stačí zaměnit sousední proměnné x_r,x_(r+1). V tableau spárujme
výskyty r a r+1 ve stejném sloupci a ty ponechme pevné. Ve sloupci
mezi nimi nemůže být jiná buňka, protože neexistuje celá hodnota
striktně mezi r a r+1.

V každém řádku tvoří nespárovaná r a r+1 jeden blok r^a(r+1)^b.
Spárovaná r jsou před ním: je-li r spárováno v určitém sloupci,
všechny r vlevo mají pod sebou buňku s hodnotou≤r+1 a>r, tedy také
r+1. Obdobně spárovaná r+1 jsou za blokem, neboť nad všemi r+1
napravo musí být r. Nahraďme volný blok r^a(r+1)^b blokem
r^b(r+1)^a.

Řádkový růst se zachová. Změněné r na r+1 nemá pod sebou r+1
(jinak bylo spárováno), takže dolní soused je nejméně r+2.
Změněné r+1 na r nemá nad sebou r, takže horní soused je nejvýše
r−1. V každém sloupci je nejvýše jeden volný výskyt těchto hodnot;
vzájemné změny tedy nepřidají novou hrozbu. Nevznikne ani nezmizí
žádný pevný pár. Opakování operace vrátí původní bloky.

Jde o involuci, která zamění celkové násobnosti r a r+1, zatímco
pevné páry přispívají oběma stejně. Váhy se tím přesně převedou
záměnou x_r,x_(r+1); sousední záměny generují všechny permutace.

## P0555: všech osm vytištěných tableaux a monomů

Pro λ=(2,1) nad1,2,3 napišme první řádek jako ab a dolní buňku c.
Podmínky jsou a≤b a a<c. Při a=1 jsou c=2,3 a b=1,2,3,
při a=2 je c=3 a b=2,3; a=3 nelze. Úplný seznam je

    11/2, 11/3, 12/2, 12/3, 13/2, 13/3, 22/3, 23/3.

V tomto pořadí jsou váhy x1²x2, x1²x3, x1x2², x1x2x3,
x1x2x3, x1x3², x2²x3, x2x3², přesně jako v sazbě.
Podíl Δ(1,3,5)/Δ(1,2,3) je16/2=8; různých monomů je7,
ale součet koeficientů8, jak vyžaduje P0553.

## P0556: první Cauchyho identita včetně formálního významu

Vezměme libovolnou m×n matici nezáporných celých četností c_ij.
Už dokázaná plná obousměrná korespondence P0446–0447 ji převádí
na dvojici semistandardních tableaux stejného tvaru λ, jedno nad
abecedou1,…,m a druhé nad1,…,n. Obsahy jsou řádkové a sloupcové
součty, tedy váha matice ∏_(i,j)(x_i y_j)^c_ij je přesně součin
vah obou tableaux. Součtem přes všechny matice dostáváme

    Σ_λ S_λ(x_1,…,x_m) S_λ(y_1,…,y_n)
       =∏_(i,j)Σ_(c≥0)(x_i y_j)^c=∏_(i,j)(1−x_i y_j)^−1.

Rovnost je formální mocninná řada: při každém pevném celkovém
stupni vstupuje jen konečně mnoho matic a tvarů. Není zapotřebí
nevyřčený analytický předpoklad konvergence. Prázdný tvar dává1;
při prázdné abecedě přispívá právě on.

## P0557: binární korespondence pro druhou Cauchyho identitu

Pro m×n matici s c_ij∈{0,1} seřaďme přítomné dvojice (i,j)
podle rostoucího i, uvnitř stejného i podle klesajícího j.
Jde o striktně klesající j v každém bloku. Rozlišme výskyty obou
souřadnic pořadím ve vstupním seznamu: značky i* jsou vzestupné
a všechny j* jsou různé. Použijme obyčejnou RSK na tento biword.

V recording tableau R* dostávají po sobě jdoucí značky téhož i
rohy ve striktně klesajících úrovních (vyšší čísla řádků), podle
již dokázaného P0445 pro klesající vložené j*. Po zapomenutí značek
má R striktní řádky a slabé sloupce: dvě stejná i nemají stejný
řádek. Transpozice R^T je proto semistandardní tvaru λ^T.

Insertion tableau P má naopak slabé řádky a striktní sloupce.
Důkaz poslední přísnosti: v inverzním biwordu se stejné původní j
čtou podle pořadí původního vstupu, tedy podle rostoucích i*.
Symetrie RSK a P0445 proto umísťují jejich značky v P* do striktně
rostoucích sloupců. Vymazání značek je nesloučí ve sloupci.
Váhy P a R jsou sloupcové a řádkové součty původní binární matice.

## P0558: skutečná inverze binární korespondence a druhá identita

Vezměme libovolné semistandardní P tvaru λ a Q tvaru λ^T.
Položme R=Q^T. Kopie stejné hodnoty v P označme zleva doprava
podle sloupců, v R shora dolů podle řádků. V P jsou příslušné
sloupce různé, v R jsou různé řádky. Obě označení tak dávají
obyčejná tableaux P*,R*: v možných rovnostech zachovávají právě
řádkový, respektive sloupcový vzestup.

Obyčejná inverze RSK dává biword s rostoucími i*. V jednom bloku
původního i jsou buňky R* po rostoucích řádcích, takže příslušné
po sobě vložené j* musejí klesat. Kdyby rostly, P0445 by druhý
roh umístil do téhož nebo vyššího řádku.

Ještě je třeba vyloučit rovná původní j v tomto bloku. Značky
téhož j v P* jsou po rostoucích sloupcích. V inverzním biwordu
tedy podle symetrie a opačné implikace P0445 odpovídající i*
rostou. Kopie každého původního j se proto v původním vstupu
vyskytují právě v pořadí svých značek. Dvě takové kopie nemohou
patřit do jednoho klesajícího bloku j*. V něm jsou původní j
striktně klesající; každá dvojice(i,j) se tak objeví nejvýše jednou.

Obnovené značky jsou přesně značky předpisu P0557. Oba směry jsou
inverzní a důkaz nepředpokládá bijektivitu nové varianty předem.
Váhovým součtem proto dostáváme

    Σ_λ S_λ(x_1,…,x_m) S_(λ^T)(y_1,…,y_n)
       =∏_(i,j)(1+x_i y_j).

Z konstrukce nejprve vychází transponované pořadí faktorů;
přejmenování λ↔λ^T dává právě vytištěný tvar. Na obou stranách
jde o polynom; přispívající diagramy leží v příslušném obdélníku.

## P0559: dělitelný součin a opravený superfactorial

Pro celá a,k,l≥0 uvažujme
R=∏_(j=0)^l binom(a+j,k)/binom(k+j,k). Jmenovatel je kladný.
Vandermonde na seznamu

    (a+l,…,a+1,a,k−1,…,1,0)

se rozpadá na rozdíly uvnitř obou bloků a mezi nimi.
Vnitřní součiny jsou ∏_(s=1)^l s! a ∏_(s=1)^(k−1)s!;
smíšený součin je ∏_(j=0)^l k! binom(a+j,k).
Po dělení Δ(k+l,…,1,0)=∏_(s=1)^(k+l)s! a zkrácení vyjde
přesně R, protože binom(k+j,k)=(k+j)!/(k!j!).

Oba seznamy mají délku k+l+1, proto P0552 dokazuje R∈Z.
Při a<k se v horním seznamu opakuje a a součin obsahuje nulové
binom(a,k); obě strany jsou0. Pro k=0 je R=1 a druhý blok je
prázdný. Prázdné součiny řeší i l=0. Zvláštní hodnota
Δ(k,…,1,0)=k!(k−1)!…1! je přímý součin rozdílů.
Použit je opravený jmenovatel a faktoriálový rozsah z roku2006.

## P0560: úloha34, délka cesty a přesně určená spodní hranice

Tvar má délky řádků λ_i a sloupců λ′_j. Háček buňky(i,j)
má dolní konec A=(λ′_j,j) a pravý konec B=(i,λ_i).
Každá cesta po buňkách z A do B s jednotkovými kroky nahoru
a doprava má λ′_j−i+λ_i−j+1 buněk, tedy délku háčku.

Zvolme cestu, která jde doprava vždy, když existuje buňka napravo
(a nebyla dosažena cílová pravá souřadnice); jinak jde nahoru.
Na pravé hranici stoupá až do B. To je přesné „hug the bottom“.
Před krokem nahoru platí λ_x=y. Před krokem doprava z(x,y)
do(x,y+1) platí x=λ′_(y+1): v tomto sloupci jsme začali na
spodním konci, nebo jsme vystoupali z posledního sloupce právě
k prvnímu řádku, který buňku y+1 obsahuje. U posledního sloupce
už krok doprava nenastává.

## P0561: obě opravené větve a násobek ab

Nechť délka tohoto háčku je a+b pro kladná celá a,b a cestu
číslujme (x_1,y_1),…,(x_(a+b),y_(a+b)). Podívejme se na krok
mezi a-tou a (a+1)-ní buňkou.

Je-li y_(a+1)=y_a, jde o krok nahoru. Pak λ_(x_a)=y_a,
a buňka(x_a,y_1) má dolní konec A a pravý konec(x_a,y_a).
Její háček má přesně tolik buněk jako první část cesty, tedy a.

Jinak jde o krok doprava. Pak λ′_(y_(a+1))=x_(a+1)=x_a,
a buňka(x_(a+b),y_(a+1)) má dolní konec(x_(a+1),y_(a+1))
a pravý konec B. Délka jejího háčku je délka zbývající části
cesty, tedy b. Obě uvedené buňky ve tvaru existují díky jeho
uzavřenosti vlevo a nahoru. To dokazuje silnější tvrzení z odpovědi
v přesně opravené podobě2006.

Má-li tvar háček délky ab, indukujme po kladném b. Pro b=1 je
výsledek přímý. Pro b>1 rozepišme ab=a+(b−1)a; silnější tvrzení
dá buď přímo a, nebo (b−1)a, odkud výsledek plyne indukcí.

Historická prvenství a úplné zdroje Lucas1891, Mitchell1881,
Littlewood1936 a Nakayama1940 nebyly nezávisle přezkoumány;
u Littlewooda je použita aktuální oprava stran. Matematická tvrzení
všech těchto odpovědí mají výše vlastní argument. Žádný nový
numerický běh ani nový nález nevznikl.
