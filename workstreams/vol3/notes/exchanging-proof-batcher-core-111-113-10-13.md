# Batcher: úplné slučování, bitové podmínky, tabulka a geometrie

7. listopadu 2026. Originály111–113/file122–124,134–135/file145–146
a628–630/file639–641 zobrazeny. Souřadnice obrázku jsou **řádek dolů,
sloupec doprava**. Převzaty pouze P0727 (bijekce dvou uspořádaných
podposloupností a cest), P0813–0814 (Prattovy disjunktní inverse)
a P0968 (nutnost kvadratické sériové práce sousedních výměn).
Žádný matematický program ani enumerace.

Pět vrstev v `sources/exchanging-errata-review.json` obsahuje známou
změnu zápisu bitového AND na111 v textu i obrázku17. Význam v originálu
je výslovně definován, takže nejde o změnu algoritmu ani nový nález.
Historický údaj1964 a přesné stránky Batcher1968 zde bibliograficky
neověřovány. Druhý důkaz v§5.3.4 zůstává dopředným odkazem, nikoli
předpokladem následujícího důkazu.

## P0984: M1–M6, všechna pořadí aktualizací a ukončení

N≥2, t=⌈lg N⌉, H=2^(t−1); tedy H<N≤2H. Pro pevné p=2^k,
k=t−1,…,0, je první průchod (q,r,d)=(H,0,p). Následují

    (q,r,d)=(H/2,p,H−p),(H/4,p,H/2−p),…,(p,p,p).

Při p=H tato druhá řada neexistuje. Rozdíl d=q_old−p musí být
vypočten před půlením q; právě to dělá M5. Vždy d>0 a je lichým
násobkem p. Průchodů pro p=2^k je t−k; velkých cyklů t a celkem
A=1+…+t=t(t+1)/2. M6 půlí p až na0. Každý M3 má konečnou
množinu indexů a porovnává pouze platné pozice1,…,N.

Navíc žádný celý M3 není prázdný: při r=0 je i=0 a d=p≤H<N;
při r=p má i=p součet i+d=q_old≤H<N. Tento fakt bude potřebný
u programu, který první klíč čte bez předběžného testu.
Algoritmus mění pouze dvojice záznamů a používá konstantní počet
řídicích proměnných a jeden dočasný záznam. Je tedy in place.

## P0985: bitový test, disjunktnost a celý obrázek17

Piš i=ap+b,0≤b<p. Protože p je mocnina2, i&p určuje paritu a.
Přičtení d, lichého násobku p, zachová b a změní paritu a.
Levé konce všech porovnávaných dvojic mají bit r, pravé opačný.
Levé konce jsou navzájem různé, pravé také; žádný levý proto
nemůže být pravým jiné dvojice. Všechny M4 v jednom M3 mají
disjunktní paměťové pozice, komutují a mohou běžet současně.
Samotné tvrzení, že se liší bity obou konců jedné dvojice, by bez
této společné hodnoty r ještě disjunktnost neprokazovalo.

Binární příklad je 01101 & 10101 = 00101 =5. V obrázku17
vede M3 do M4 právě pro přípustné i, návrat M4 pokračuje stejnou
konečnou smyčkou, po jejím skončení jde řízení do M5. Vždy q≥p,
takže test q>p na návratové hraně je ekvivalentní q≠p v M5.
M6 testuje již rozpůlené p; hrany p≥1 a p=0 jsou úplné. Známá
oprava symbolu AND nemění žádnou tuto hranu.

## P0986: první složení a zachování dvou uspořádaných seznamů

Nechť A_i=K_(2i−1),B_i=K_(2i) jsou neklesající, délek u,v,
kde u=v nebo u=v+1. První průchod nahradí každou existující
dvojici (A_i,B_i) dvojicí (min,max). Obě nové podposloupnosti
zůstávají neklesající. Případný poslední nespárovaný A_(v+1)
je alespoň A_v, tedy také alespoň min(A_v,B_v).

Pro libovolný práh x označ a počet A≤x a b počet B≤x. Po
průchodu jsou tyto počty a′=max(a,b),b′=min(a,b), včetně
nespárovaného posledního A. Rozdíl h=a−b se změní na |h|.
Pro různé klíče a práh rovný hodnotě s je vrchol cesty (a,b),
a+b=s. Proto je změna přesně odrazem částí nad diagonálou.
Nejde pouze o vizuální analogii jednotlivé záměny.

## P0987: libovolná další mezera a celý druhý vzorec skládání

Pro d=2m−1,m≥1 se porovnává B_i s A_(i+m), pro všechny
existující dvojice. Menší hodnota zůstává na dřívější sudé
pozici B_i, větší na pozdější liché A_(i+m). Změněná sudá
podposloupnost je bodové minimum dvou neklesajících seznamů;
změněná lichá část bodové maximum. Nezměněný lichý prefix je
≤ změněnému lichému ocasu. Nezměněný sudý ocas je ≥ změněnému
sudému prefixu. Obě celé podposloupnosti tedy zůstávají uspořádané.

Pro stejný práh x je

    a′=min(a,m)+min(max(a−m,0),b)=min(a,b+m),
    b′=a+b−a′=max(b,a−m),
    h′=min(h,2m−h)=m−|h−m|.

První m lichých pozic nejsou porovnávány; všechny další existující
liché pozice mají sudého partnera, protože u≤v+1 a m≥1. To
zdůvodňuje vzorec i při nestejných délkách. Pokud m≥u, nejsou
žádné dvojice a vzorec správně dává a′=a,b′=b.

Pro permutaci zůstává a′+b′=s. Každý vrchol h>m se odrazí
o přímku h=m, ostatní zůstávají. To dokazuje skutečné složení
celé cesty, včetně úseků mezi porovnávanými hodnotami.

## P0988: ukončení slučování, nepravidelné délky a stejné klíče

Má-li místní posloupnost délku L≤2^s, po prvním průchodu
platí0≤h≤⌈L/2⌉≤2^(s−1). Pro s≥2 následují m=2^(s−2),… ,1.
Jestliže0≤h≤2m, vzorec předchozího odstavce dává0≤h′≤m.
Indukce proto končí0≤h≤1 pro každý práh. Pro s=1 stačí první
dvojice; i případ L=1 splňuje závěr a všechny nadbytečné průchody
jsou prázdné.

Tento závěr znamená úplné uspořádání i při shodných klíčích.
Kdyby A_i>B_i, práh x=B_i by dal a≤i−1,b≥i, tedy h≤−1.
Kdyby B_i>A_(i+1), práh x=A_(i+1) by dal a≥i+1,b≤i−1,
tedy h≥2. Ani jedna sousední inverse tedy není možná. U různých
klíčů se zároveň musí cesta střídat dolů/doprava a končit
v(⌈L/2⌉,⌊L/2⌋). Důkaz nepoužívá neplatné nahrazení shodných
klíčů stabilními pořadovými čísly; metoda stabilní není.

## P0989: celé M6 a redukce na dva seznamy

Před velkým cyklem p je soubor2p-ordered. To je na počátku
prázdná podmínka, protože2p=2^t≥N. V každé třídě pozic
a,a+p,a+2p,…,1≤a≤p, tvoří střídavé položky dva uspořádané
seznamy. Při zápisu i=pq+b má bit p paritu místního indexu q.
Místní vzdálenosti jsou1,H/p−1,H/(2p)−1,…,1 a první průchod
bere sudá q, další lichá q. Jde přesně o již dokázané slučování
s kapacitou2^t/p a skutečnou délkou≤této kapacity.

Po celém cyklu je každá třída uspořádaná, tedy soubor p-ordered.
M6 půlením p obnoví předpoklad dalšího cyklu. Poslední p=1
uspořádá celý soubor. Pro p≥2 jsou všechny vzdálenosti sudé,
takže liché a sudé původní pozice se skutečně zpracovávají
nezávisle, jak říká112. Tím je odvozeno i8-,4-,2-,1-uspořádání
v šestnáctiprvkovém příkladu, bez předpokladu N mocniny2.

## P0990: celé10(a), orientace a konce obou druhů kroků

P0727 již dokazuje bijekci. Zde kontrolujeme konkrétní souřadnice.
Před hodnotou A_k je k−1 menších lichých položek a A_k−k
menších sudých. Její svislý krok tedy vede

    (k−1,A_k−k) → (k,A_k−k).

Před B_k je k−1 menších sudých a B_k−k menších lichých, takže
vodorovný krok vede

    (B_k−k,k−1) → (B_k−k,k).

Souřadnice jsou nezáporné a cílem je(⌈N/2⌉,⌊N/2⌋).
Odpověď628 používá tutéž orientaci, nikoli obvyklou osu x doprava.

## P0991: celé10(b) a všechny ostré/neostré přechody

Pro existující A_k,B_k a různé hodnoty platí

    A_k>B_k ⇔ A_k≥2k ⇔ B_k≤2k−1.

Jestliže A_k>B_k, před A_k leží alespoň k−1 lichých a k sudých
hodnot, proto A_k≥2k; před B_k nanejvýš k−1 od každého druhu,
proto B_k≤2k−1. Jestliže A_k<B_k, opačné počty dávají
A_k≤2k−1 a B_k≥2k. Tím jsou zdůvodněny obě implikace.

Svislý krok A_k leží nad diagonálou právě při k≤A_k−k;
vodorovný B_k právě při B_k−k≤k−1. Jde o přesně stejné
dvojice. P0986 navíc dokazuje, že současné záměny odrazí všechny
dotčené vrcholy; pouhé prohození orientací krajních kroků by
bez toho nebylo úplným důkazem skládání.

## P0992: celé10(c), včetně obou početních sporů v odpovědi

Piš x=A_(k+m),y=B_k,H=2k+m. Potom

    x<y ⇔ x<H ⇔ y≥H.

Je-li x<y, před x je nejvýše k+m−1 lichých a k−1 sudých
hodnot, takže x≤H−1; před y je alespoň k+m lichých a k−1
sudých, takže y≥H. Je-li x>y, před x je alespoň k+m−1
lichých a k sudých, tedy x≥H; před y je nejvýše k+m−1
lichých a k−1 sudých, tedy y≤H−1.

Tytéž počty přímo kontrolují oba spory odpovědi629: x,y<H by
vyžadovalo alespoň H prvků pod H; x,y≥H, z nichž jeden je
ostře větší, by neumístilo všech H prvků≤H do nejvýše H−1
pozic. Předpoklad různých hodnot je zde skutečně využit.

Začátek svislého kroku x má výšku2k+2m−1−x; konec
vodorovného kroku y výšku y−2k. Celé tyto kroky leží alespoň
m pod diagonálou právě při x<H a y≥H. Jsou tedy přesně
vyměňovanou dvojicí. P0987 dodává odraz všech mezilehlých vrcholů.

## P0993: všechny části obrázku18

Pro každou část udáváme výšky h(s),s=0,…,16. Souřadnice vrcholu
jsou((s+h)/2,(s−h)/2); tím je určena každá jednotková hrana.

    a: 0,1,2,1,0,−1,−2,−3,−4,−5,−4,−3,−4,−3,−2,−1,0
    b: 0,1,2,1,0, 1, 2, 3, 4, 5, 4, 3, 4, 3, 2, 1,0
    c: 0,1,2,1,0, 1, 2, 3, 4, 3, 4, 3, 4, 3, 2, 1,0
    d: 0,1,2,1,0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1,0
    e: 0,1,0,1,0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0

Vstup a je1,3,2,4,10,5,11,6,13,7,14,8,15,9,16,12.
První průchod mění páry s lichým začátkem5,7,9,11,13,15:

    b =1,3,2,4,5,10,6,11,7,13,8,14,9,15,12,16.

Pro d=7,m=4 jsou páry(2,9),(4,11),(6,13),(8,15); mění se
jen(6,13), tedy

    c =1,3,2,4,5,9,6,11,7,13,8,14,10,15,12,16.

Pro d=3,m=2 jsou začátky2,4,6,8,10,12; mění se poslední
čtyři dvojice, tedy

    d =1,3,2,4,5,7,6,8,9,10,11,12,13,15,14,16.

Poslední d=1,m=1 mění(2,3),(6,7),(14,15) a dá identitu.
Každý výškový řádek vzniká z předchozího přesně mapami
|h|,4−|h−4|,2−|h−2|,1−|h−1|. Souřadnice byly porovnány
s celými čarami originálu; tečkované části ukazují předchozí
položení a přerušované diagonály příslušnou osu skládání.

## P0994: každá dvojice, šipka a řádek tabulky1

Indexy v následující tabulce jsou **jedničkové začátky** dvojic;
pravý konec je vždy o d dál. J je celá množina porovnání,
S její podmnožina skutečných výměn, ručně určená z hodnot.

|p,q,r,d|J|S|
|---|---|---|
|8,8,0,8|1,2,3,4,5,6,7,8|3,5,7|
|4,8,0,4|1,2,3,4,9,10,11,12|prázdná|
|4,4,4,4|5,6,7,8|7|
|2,8,0,2|1,2,5,6,9,10,13,14|1,2,5,13|
|2,4,2,6|3,4,7,8|prázdná|
|2,2,2,2|3,4,7,8,11,12|prázdná|
|1,8,0,1|1,3,5,7,9,11,13,15|všechny|
|1,4,1,7|2,4,6,8|prázdná|
|1,2,1,3|2,4,6,8,10,12|4,6,8,12|
|1,1,1,1|2,4,6,8,10,12,14|2,4,10,12,14|

Ze vstupu503,87,512,61,908,170,897,275,653,426,154,509,612,677,765,703
jsou po neprázdných S následující celé řádky; po ostatních průchodech
se přesně opakují předchozí řádky:

    1:503,87,154,61,612,170,765,275,653,426,512,509,908,677,897,703
    3:503,87,154,61,612,170,512,275,653,426,765,509,908,677,897,703
    4:154,61,503,87,512,170,612,275,653,426,765,509,897,677,908,703
    7:61,154,87,503,170,512,275,612,426,653,509,765,677,897,703,908
    9:61,154,87,275,170,426,503,509,512,653,612,703,677,897,765,908
    10:61,87,154,170,275,426,503,509,512,612,653,677,703,765,897,908.

Všechny odpovídají originálu včetně šipek. Počty porovnání jsou
8,8,4,8,4,6,8,4,6,7, součet63. Počty výměn3,0,1,4,0,0,8,0,4,5
mají součet25 a souhlasí s odpovědí12. Čas939u zde ještě nepřebíráme;
vyžaduje samostatnou kontrolu programu a jeho režie.

## P0995: paralelní hloubka55 a oba Prattovy počty40/73

P0985 dovoluje jedinou paralelní vrstvu na každý M3. P0984
počítá přesně t(t+1)/2 neprázdných vrstev, tedy pro N=1024,t=10
celkem55. Jde o model souběžných porovnání disjunktních párů,
nikoli počet sériových instrukcí nebo tvrzení o minimální hloubce.

Prattovy přírůstky2^p3^q<1024 mají pro q=0,…,6 počty
10,9,7,6,4,3,1, celkem40. Pro q≥7 už3^q>1024. Převzaté
P0813–0814 dokazují disjunktnost skutečných výměn i zachování
ostatních inversí. Proto lze nejprve všechny sousední páry v
každé h-třídě současně porovnat a pak současně provést pouze
disjunktní výměny: to je knižní model40 kroků s překryvem čtení.

Při zákazu překrývajících se porovnání rozdělíme hrany každé
h-třídy do dvou střídavých matchingů. Druhý matching po prvním
stále pozná stejné zbývající inverse podle P0814. Stačí tedy dva
kroky pro h<512 a jeden pro h≥512. Sedm přírůstků v[512,1024)
je512,768,576,864,648,972,729. Výsledkem je7+2·33=73.
Nejde o optimalitu této implementace, pouze o realizaci uvedeného
počtu. Historické „about as fast as any general method known“
a označení nejbližšího konkurenta nejsou zde certifikovány jako
současný přehled všech modelů a metod; další diskuse§5.3.4 čeká.

## P0996: celé13 pro Batcherovu metodu

N=3, vstup záznamů[2a,2b,1], kde označení a,b nemění klíč.
První p=2 porovná pozice1,3 a dá[1,2b,2a]. Při p=1 už
žádná výměna nenastane. Relativní pořadí shodných klíčů se
obrátilo: M není stabilní. Odpověď navíc zmiňuje Q a R; tyto
dvě odlišné části čekají na audit příslušných algoritmů a zde
se za ověřené nevydávají.

## Rozsah

Celé matematické jádro111–112, Batcherova geometrie113, všechny
části10 a Batcherova část13 mají obecné argumenty. Program12,
maximalizace11, počty14–15 a průměr16 se touto poznámkou
neuzavírají. Na113 není paušálně uzavřená obecná praktická
efektivita ani následující Quicksort. Nový nález nevznikl.
