# AlgoritmusK a všech17 minim v104(b)

7. listopadu 2026. §7.1.1–104, p92/file109 a p553/file570.
Checkpoint X0117, P1092–P1102.
Původní sazba zobrazena, včetně detailu celého zadání104.
Žádný program, LP ani enumerace vstupů. Tato poznámka dokazuje
obecný algoritmusK a celou část(b); konkrétní(a)/(c) se z ní
automaticky neodvozují.

## 1. Přesná doména a inicializaceK

Váhy jsou nezáporná celá čísla seřazená w_1≥…≥w_n; jejich
součet W je kladný a lichý, protože reprezentují neprázdnou
lichou většinu. Nulové poslední váhy jsou dovoleny. Práh je
t=(W+1)/2, takže0<t≤W. Vektor všech nul prohrává, všech
jedniček vyhrává a existuje aspoň jeden prime implicant.

Zpětná inicializační smyčka dává přesně a_j=Σ_{i>j}w_i,
vymaže všechny e_j a nastaví s_1=0. V s_j se udržuje suma
vybraných bitů s indexem menším než j. Proměnná l označuje
právě zpracovávanou pozici; pole s potřebuje též s_{n+1}.

## 2. Úplný invariant, včetně nulových suffixů

Algoritmus je průchod binárním stromem v pevném pořadí indexů,
vždy nejprve větví1 a potom případně větví0. Před vstupem K2
do nové pozice j=l+1 platí:

* prefixová suma s_j je menší než t;
* prefix lze doplnit do pravdivého vstupu: s_j+Σ_{i≥j}w_i≥t;
* všechny dosud nefixované e_i, i≥j, jsou0.

Na začátku to plyne z0<t≤W. K2 nastaví e_j=1 a přičte w_j.
Pokud práh ještě nedosáhne, možnost doplnění se nezměnila:
přidaná váha pouze přešla ze suffixu do prefixu. Proto K3
může bezpečně znovu vstoupit do K2. Nemůže tím překročit n,
protože při j=n už možnost doplnění nutí dosažení prahu.

Po návštěvě nebo po návratu z celé větve1 K5 vymaže e_l.
Všechny hlubší bity jsou již0; to plyne indukcí, protože
každá poslední1 se vymaže v K5 před opuštěním své úrovně.
Větev0 může obsahovat pravdivý vstup právě tehdy, když
s_l+a_l≥t. Vytištěné≥ je nutné a dostačující, protože všechny
suffixové váhy jsou nezáporné. Pak s_{l+1}=s_l obnoví invariant.
Jinak ji lze celou vypustit. K6 přeskočí již vyřízené nulové
větve a vrátí se na nejbližší dosud nezpracovanou nulu po1;
na l=0 skončí. Ani nulové váhy nevytvářejí mimořádnou větev:
nemohou samy poprvé dosáhnout prahu a nedostatečný nulový
suffix neprojde guardem K5.

## 3. Proč každá návštěva je opravdu prime

V K4 je prvního dosažení prahu dosaženo přidáním w_l:

    s_l<t≤s_l+w_l.

Každá dříve zvolená váha w_i, i<l, je nejméně w_l díky
seřazení. Odstranění kterékoliv jedničky proto sníží celkovou
sumu nejméně o w_l, na hodnotu nejvýše s_l<t. Hlubší bity
jsou0. Návštěva je tedy minimální pravdivá podpora.
Předpoklad seřazení zde nelze vynechat; pouhé první dosažení
prahu při libovolném pořadí by minimalitu nezaručilo.

Pro úplnost vezměme libovolnou minimální pravdivou podporu B.
Každý její vlastní prefix prohrává. Při sledování jejích bitů
proto algoritmus neukončí větev před posledním indexem B.
Při každém jejím nulovém bitu guard K5 projde, protože ještě
zbývající jedničky B samy poskytují pravdivé doplnění. Cesta
B tedy dosáhne právě K4. Každá bitová cesta se projde jednou,
takže návštěvy nejsou duplicitní. To dokazuje přesně úplný
seznam prime implikantů, nikoli jen seznam některých svědků.

## 4. Ukončení, práce a paměť

Binární strom má konečnou hloubku n, žádná větev se nevrací
do již dokončeného stavu. To dokazuje ukončení. Označme P
počet návštěv. Každý rozvinutý prefix má pravdivé doplnění;
volba prvních možných jedniček skončí návštěvou podle §3.
Každý navštívený uzel tedy leží na cestě k některému z P
výstupů. Součet délek těchto cest je nejvýše nP, a průchody
zpět lze účtovat stejným hranám. Po inicializaci je proto
práce O(nP), včetně explicitního vypsání n bitů na návštěvu;
pomocná paměť O(n). Při maximální b-bitové váze mají s_j,a_j,t
O(b+log(n+1)) bitů, což dává odpovídající násobek v bitové
aritmetice. Seřazení není součástK: je vstupním předpokladem,
případná permutace se musí uchovat pro správné názvy proměnných.
Žádná z těchto mezí neoznačuje výstupní velikost za malou.

## 5. Pravdivost všech devíti vytištěných řádků104(b)

Pišme z=(x_1x_2x_3x_4)_2 a f_t=[z≥t]. Pro0≤t≤8 je
padding z(82) kladný: f_t je cofactor x_0=1 čisté většiny
s původními váhami(16−2t,8,4,2,1). Vytištěné menší váhy
v pořadí(x_0,x_1,x_2,x_3,x_4) dávají přesně:

|t|Váhy|Délka|Cofactor x_0=1|
|---:|---|---:|---|
|0|10000|1|1|
|1|31111|7|x_1∨x_2∨x_3∨x_4|
|2|21110|5|x_1∨x_2∨x_3|
|3|32211|9|x_1∨x_2∨(x_3∧x_4)|
|4|11100|3|x_1∨x_2|
|5|23211|9|x_1∨(x_2∧(x_3∨x_4))|
|6|12110|5|x_1∨(x_2∧x_3)|
|7|13111|7|x_1∨(x_2∧x_3∧x_4)|
|8|01000|1|x_1|

Každá pravá strana je přímo rozklad binárního porovnání podle
prvního vysokého bitu, který může dosáhnout t. Současně plyne
z uvedených vah po odečtení váhy x_0 od většinového prahu.
Například u t=3 je test2x_1+2x_2+x_3+x_4≥2, u t=5 test
3x_1+2x_2+x_3+x_4≥3. Zbývající řádky jsou obyčejné OR
nebo OR s konjunkcí. Všechny hodnoty jsou tak dokázané na
všech vstupech bez16případových tabulek.

## 6. Proč minimálnost rozšíření dokazuje původní minimum

Uvažujeme délku jedné ploché liché většiny, jak požaduje103/104,
nikoli počet hradel v obvodu. Případné páry x_j,¬x_j a0,1
lze zrušit podle(85). Podstatné vstupy monotónní funkce potom
musejí mít kladnou polaritu. Nepodstatné lze zafixovat a změnit
jejich případné výskyty na konstanty bez zvětšení délky.

Pro t<8 je N(f_t)=16−t>8. Většina obsahující pouze nulové
konstanty by splňovala f_t≤Df_t, protože přechod k duálu
mění tyto nuly na jedničky. Pak by N(f_t)≤16−N(f_t), spor.
Bez konstant by funkce byla self-duální a měla N=8, také spor.
Po zrušení párů tedy zbývají pouze jedničkové konstanty.
Jejich nahrazení jednou proměnnou x_0 dává čistou self-duální
většinu stejné délky s cofactorem f_t při x_0=1. Toto rozšíření
je jednoznačně určeno (druhý cofactor je Df_t), podle102.
Minimální délka f_t je proto přesně minimální čistá většinová
délka tohoto pětiproměnného rozšíření. Případy t=8 a konstanty
mají přímou dolní mez1 a jsou v tabulce dosaženy.

## 7. Dolní meze pro všechny použité typy

Pracujeme s právě určenými self-duálními rozšířeními, proto
všichni jejich podstatní proměnní účastníci musí mít alespoň
jeden hlas a celková délka musí být lichá.

* Projekce v t=0/8 vyžaduje nejméně1 a tuto mez dosahuje.
* Tříproměnná většina v t=4 má tři podstatné vstupy, tedy
  délku nejméně3, dosaženou v tabulce.
* Typy t=2/6 mají čtyři podstatné vstupy: centrum váhy2
  a tři listy váhy1. Centrum s libovolným listem je minimální
  vítězná dvojice. Lichá délka je proto nejméně5, dosažená.
* Typy t=1/7 mají pět podstatných vstupů a právě čtyři vítězné
  dvojice, hvězdu s centrem váhy3. Délka5 by nutně dala jeden
  hlas každé proměnné, tedy žádnou vítěznou dvojici
  (obyčejnou většinu pěti). Je nemožná; nejméně7 je dosaženo.
* Typy t=3/5 mají pět podstatných vstupů a právě dvě vítězné
  dvojice se společným centrem váhy3. Dva listy mají váhu2,
  další dva vstupy váhu1. Poslední dva jsou také podstatné:
  každý spolu s oběma váhově2 listy tvoří minimální pravdivou
  trojici. Délka5 opět nemá žádné vítězné dvojice. Při délce7
  zbývají po jednom hlase pro každý vstup právě dva hlasy navíc.
  Mohou dát pouze váhy(3,1,1,1,1), které mají čtyři vítězné
  dvojice, nebo(2,2,1,1,1), které mají jedinou. Ani jedna
  možnost nemá přesně dvě. Nejmenší možná délka je proto9,
  a tabulka ji dosahuje.

Toto vyčerpává každé menší liché číslo pro všech devět řádků.
Nejde jen o nalezené krátké reprezentace nebo horní meze.

## 8. Všech osm zbývajících prahů

Pro0≤t≤16 platí přesně

    Df_t(x)=1−[15−z≥t]=[z≥16−t]=f_{16−t}(x).

Dualita mění konstantní jedničky v mediánu na nuly a zachovává
délku. Je involucí, takže zachovává i minimální délku, v obou
směrech. Pro t=9,…,16 tedy vezmeme řádek16−t tabulky a dosadíme
x_0=0. Dostaneme všech osm chybějících optim, včetně konstanty0
při t=16. Všech17 případů104(b) je uzavřeno.

Kontrola errat zahrnuje p92/p553, AlgorithmK a104 ve všech
vrstvách4A/F0. Žádná relevantní oprava ani nový nález. Ostatní
konkrétní části104 a zejména tvrzení o censu devíti proměnných
se touto poznámkou nepovažují za ověřené.
