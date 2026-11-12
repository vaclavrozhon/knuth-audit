# Multisety: jednotlivé argumenty úloh14–21

Zadání32–34, odpovědi599–601. Důkaz C0003 a q-multinomiální důkaz
V3-P0149 se přebírají bez opakování. Sazba600/601 ověřena, zejména
obě nezáporné nerovnosti v úloze21; OCR je chybně čte jako ostré.
Bez výpočetního běhu a bez nového nálezu. Historické citace přeskočeny.

## 14: stabilní transpozice

Označme N_ij počet sloupců i/j a R(N) slovo, v němž jsou dolní
písmena pod každým horním písmem seřazena. Stabilní výměna řádků I
splňuje I(π)=R(Nᵀ): původní horní řádek byl seřazen, takže po
stabilním sdružení podle dolního písmene je každý nový blok seřazen.
Proto I²(π)=R(N), I³(π)=I(π), ale obecně I²(π)≠π.
Například baa přejde v aba a tam zůstane. Pro tištěné cabddabdad
jsou nové fronty acd,ad,a,bbdd, tedy acdadabbdd.

Interkalace sčítá matice četností. Obě strany identity
I(α⊤β)=I²(I(α)⊤I(β)) jsou proto R(N_αᵀ+N_βᵀ), což dokazuje
přesnou tištěnou rovnost.

Slovo je samoinverzní právě když N=Nᵀ a všechny jeho fronty jsou
seřazeny. Jedna taková matice dává jediné slovo. Její diagonála
dává jednočlenné cykly(x_j), a N_jk=N_kj pro j<k dává N_jk
kopií(x_j x_k). Seřazení nejprve podle j, uvnitř bloku nejprve
smyčky a pak podle k, má v každé frontě právě rostoucí sousedy.
To dokazuje uvedenou jedinou faktorizaci předepsaného tvaru.
Příklad(a),(ab),(ab),(bc),(c) má fronty abb,aac,bc, a je samoinverzní.
U dvou písmen lze zvolit N_12=0,…,min(m,n), tedy min(m,n)+1 slov.
U tří písmen určují x=N_12,y=N_13,z=N_23 diagonály jednoznačně;
jejich nezápornost je přesně x+y≤l,x+z≤m,y+z≤n.

Pro pevnou matici N je počet slov∏n_i!/∏N_ij!, výběrem pořadí
v každé frontě. Protože součty řádků i sloupců jsou n_i, transpozice
počet zachová. Alternativní inverze otočí pořadí prvočinitelů a
obrátí každý jednoduchý cyklus. Je dobře definována: záměna
disjunktních sousedních faktorů se i po obrácení stane dovolenou
záměnou. Druhé obrácení vrátí původní slovo a matice četností se
transponuje, protože všechny hrany obrátí orientaci.

Chybějící faktor z^K ve fixované inverzní GF je již potvrzený C0003;
důkaz se neopakuje. Navazující požadavek stejného počtu inverzí
při transpozici přesto má správnou algebraickou oporu: K(N)=K(Nᵀ),
protože dvojice buněk(i,u),(j,v) s i<j,u>v se po transpozici a
záměně jejich pořadí opět stane právě jednou takovou dvojicí.
Také q-faktoriálový poměr je při transpozici invariantní. Tedy
opravené GF obou matic souhlasí. Neformální hledání „přirozené“
involuce se nevydává za vyřešený výzkumný problém.

## 15: poslední výstupy a cyklické reprezentace

Pro každé písmeno x s kladnou četností nechť f(x) je poslední
položka jeho fronty. To je přesně orientovaná hrana ze zadání,
po známé opravě indexů m/n. Pevná reprezentace cyklu začínající
písmenem y musí postupně odebírat první hrany front; pořadí je
tedy deterministické. Zapisujeme navštívené vrcholy před odchody,
nikoli rotaci přes poslední y, která by při opakovaných y nebyla platná.

Pokud tento průchod použije všechny hrany a skončí v y, poslední
odchod z každého jiného v vede buď do y, nebo do vrcholu s pozdějším
posledním odchodem. Po odstranění hrany f(y) tedy zbývá orientovaný
strom směřující do y. Funkční graf f má právě jeden cyklus a y leží na něm.

Obráceně nechť f má jediný cyklus a y leží na něm. Hladový průchod
frontami z y nemůže skončit jinde než v y, díky vyrovnaným stupňům.
Pokud by zbyly nepoužité hrany, množina S vrcholů s neprázdnou
zbývající frontou by neobsahovala y a byla by uzavřená vůči f:
poslední hrana z v∈S není použitá a vyrovnané zbývající stupně
nutí f(v)∈S. Konečná neprázdná S by obsahovala jiný cyklus f,
spor. Proto se použijí všechny hrany. Přesně vrcholy jediného
cyklu jsou tedy možné počáteční znaky; každému odpovídá jedna
reprezentace. Jejich počet je délka cyklu, jak zadání tvrdí.

V tištěném příkladu jsou fronty dcb,ac,aab,dc. Poslední hrany
jsou a→b,b→c,c→b,d→c, jediný cyklus b↔c. Dva deterministické
průchody začínající b/c dávají právě(baddcacabc) a(caddcacbab).
Tím je odpověď doložena bez závislosti na odkazovaném stromovém teorému.

## 16: inverzní tabulky a obdélníkové rozklady

Obecný q-multinomiální důkaz posledním písmenem je již V3-P0149.
Odpovědní alternativu lze také doložit: počty větších písmen před
postupnými kopiemi x_j tvoří0≤b_j1≤…≤b_j,nj≤N_j, kde
N_j=Σ_(k>j)n_k. Obráceně, po vložení všech větších písmen,
jednoznačně vložíme kopie x_j za předepsaný počet větších písmen;
shodné hodnoty jen znamenají sousední nerozlišitelné kopie. Volby
pro jednotlivá j jsou nezávislé a jejich součet je počet inverzí.

GF rozkladů do obdélníku m×N splňuje
F(m,N)=F(m−1,N)+z^m F(m,N−1): buď má nejvýše m−1 kladných
částí, nebo všech m částí zmenšíme o1. Okraje F(0,N)=F(m,0)=1.
Tutéž rekurenci splňuje [m+N choose m]_z podle q-Pascala.
Součin [n_j+N_j choose n_j]_z přes j teleskopicky dává
n!_z/∏n_j!_z. Citovaná Franklinova konstrukce nebyla dohledána;
matematický výsledek je však nezávisle dokázán dvěma uvedenými způsoby.

## 17: střední hodnota, rozptyl a odchylka

Normalizovaná GF je g=h_n/∏h_nj, h_r=r!_z/r!. Pro D=z d/dz
platí E X=(D log g)(1) a var X=(D² log g)(1), což plyne
z dosazení z=e^t do momentové GF. Logaritmy proto dávají rozdíly
dříve dokázaných momentů obyčejných permutací, aniž se předpokládá
nějaká neexistující nezávislost v podílu GF.

E X=(n²−Σn_j²)/4=(1/2)Σ_(i<j)n_i n_j.
var X=[n(n−1)(2n+5)−Σn_j(n_j−1)(2n_j+5)]/72
     =(n³−Σn_j³)/36+(n²−Σn_j²)/24.
Směrodatná odchylka je nezáporná odmocnina tohoto výrazu.
Jednopísmenný multiset má oba momenty0, včetně degenerovaného případu.

## 18: index a inverze multisetů

MacMahonova konstrukce se rozšíří takto: každému prvku multisetu q_j
přiřaďme index j, všechny dvojice seřaďme podle klesající hodnoty
a při shodě podle rostoucího j. Získáme slovo a_1…a_n a hodnoty Q_i.
Položme d_i=počet sestupů a od i doprava a p_i=Q_i−d_i.
Při sestupu a_i>a_(i+1) musí Q_i>Q_(i+1), takže p_i jsou slabě
klesající nezáporné. Obráceně Q_i=p_i+d_i jsou slabě klesající
a při shodě jsou indexy a_i neklesající, tedy vzniknou přesně
původní multisety q_j. Jde o bijekci, sΣQ_i=Σp_i+ind(a).

GF voleb q_j je∏(z;z)_nj^−1, GF voleb p je(z;z)_n^−1.
Proto indexová GF slov je(z;z)_n/∏(z;z)_nj, stejná jako
již doložená inverzní GF. Známé erratum upřesňuje označení všech
n_j prvků indexem j; použita tato opravená verze.

Také tvrzení o rozšíření Foatovy konstrukce má přímý argument.
Pro poslední písmeno t vybírej v prvním případě označené prvky
x≤t, jestliže první prvek≤t; jinak vybírej x>t. Rozděl prefix
na bloky xα a změň je naαx. V prvním případě se inverze prvků
α vůči odebranému t nahradí inverzemi vůči x, takže počet zůstane.
Ve druhém zmizí právě n−1 inverzí. Rekurzivní f(h(a))t pak
přidá na indexu0 nebo n−1 podle stejného případu. Bloky lze
jednoznačně rozdělit zpětně podle jejich konců a rekonstruovat,
takže jde i při opakování písmen o bijekci se stejným multisetem.

## 19: Möbiova funkce

Množina S různých prvočíselných levých faktorů neprázdného π je
neprázdná. Každé dva jsou disjunktní podle důkazu C. Levé faktory
λ sμ(λ)≠0 jsou přesně součiny podmnožin S: jejich vlastní
prvočinitelé jsou disjunktní a lze je přesunout na začátek, obráceně
libovolnou podmnožinu S lze odebrat z disjunktních front.
Podmnožina je jednoznačná a μ(λ)=(−1)^|podmnožina|, tedy
Σ_(λ levý faktor) μ(λ)=(1−1)^|S|=0. Pro ε má součet hodnotu1.

Při opakovaném indexu jsou Vandermondův součin iμ nulové.
Jinak má součin znaménko(−1)^inv. Cyklus délky l má znaménko
(−1)^(l−1), proto při t cyklech je znaménko(−1)^(n−t)
=(−1)^(n+t), rovněž(−1)^(počet sudých cyklů). Násobení(−1)^n
dáváμ=(−1)^t, přesně19(b), se známou opravou j/i v zadání.

## 20: Master Theorem

Hmotnostν je součin vah sloupců; interkalace sloupce jen stabilně
přeskupí, takžeν(π⊤ρ)=ν(π)ν(ρ). Koeficient monomu s četnostmi n_i
ve∏_i(Σ_j a_ij x_j)^n_i vybírá dolní řádek pod pevně daným
horním řádkem. Je proto součtem vah všech příslušných slov.
Volba a_ij=z pro i=j a1 jinak dává jeden faktor z za každý
pevný sloupec. Vytištěné členy G pro m=2 vzniknou z prázdného
slova, dvou jednopísmenných a čtyř dvoupísmenných slov přesně takto.

Rozvinutí det(I−A diag(x)) podle vybraných neidentitních řádků S
dáváΣ_S(−1)^|S| det(A_SS)∏_(j∈S)x_j. Každá permutace S má
koeficient(−1)^|S| sign(π)=μ(π) podle19(b). Dostáváme přesně
D=Σ_π μ(π)ν(π)·monom(π), neboť opakovaná písmena majíμ=0.

Nejdříve násobme formální řady v algebře interkalace. Koeficient
neprázdného slova π v D⊤G jeν(π)Σ_(λ levý faktorπ)μ(λ)=0;
prázdný koeficient je1. Pro každý stupeň jde o konečné součty.
Přechod ke komutativním monomům je homomorfismus, takže DG=1
a G=1/D. Pro všechna a_ij=1 mizí všechny hlavní minory řádu≥2,
tedy D=1−Σx_j; geometrická řada dává multinomiální koeficient,
jak uvádí příklad. Není zapotřebí žádný analytický konvergenční předpoklad.

## 21: omezené sestupy

V sazbě platí d≥0 a a_(j+1)≥a_j−d. Odstranění všech m ze
slova zachová podmínku: při slepení sousedů přes blok m je pravý
soused alespoň m−d, tedy alespoň levý soused minus d.
Obráceně lze bloky m vložit přesně před každý existující znak≥m−d
a za celé slovo. Počet mezer je1+Σ_(k=m−d)^(m−1)n_k.
Rozdělení n_m stejných prvků do těchto mezer dává
choose(n_m+…+n_(m−d),n_m) způsobů, nezávisle na pořadí menších prvků.
Indukce po m dává vytištěný součin. Konvence n_k=0 pro k≤0
řeší začátek abecedy; d=0 dovoluje pouze rostoucí bloky a dává1,
prázdný multiset také dává1. V rámci diskrétních indexů je d celé.
