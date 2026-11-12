# Dvě prokládané třídy: celý mřížkový argument a úlohy11–14

Zdroj86–88/file97–99, zadání102/file113, odpovědi620
a případ h=2 odpovědi16 na621. Původní sazba zobrazena.
Pět vrstev: `sources/insertion-errata-review.json`.
Známé zaokrouhlení0.15→0.16 z2015 je oddělené od
nálezů. Žádný program ani opakování starých výpočtů.
Rozptyl a úplná úloha15 se zde ještě nepovažují za
doložené; pokračují samostatně po tomto bloku.

## P0725: počet a skutečná rovnoměrnost2-ordering

Polož a=ceil(n/2),b=floor(n/2). Vyber b hodnot pro
sudé pozice a seřaď je; zbylých a hodnot seřaď do
lichých pozic. To je obousměrná bijekce všech
2-ordered permutací s b-prvkovými podmnožinami,
tedy počet choose(n,b). Každý takový výstup má přesně
a!b! původních permutací: hodnoty na obou třídách se
mohly libovolně přeuspořádat jen uvnitř této třídy.
Při rovnoměrném původním vstupu jsou tedy výstupy
skutečně rovnoměrné. To není automatický důsledek
samotného počtu výstupů; konstantní počet vzorů je nutný.

## P0726: všechny počáteční hodnoty a vypsaných šest případů

Pro n=1 je jediná permutace1. Pro n=2 jsou12 a21,
pro n=3 jsou123,132,213, s počty inverzí0,1,1.
Pro n=4 každá volba dvou sudých hodnot dává právě
jeden z vypsaných případů1324,1234,1243,2134,2143,3142;
jejich počty jsou1,0,1,1,2,3. Proto A₁=0,A₂=1,A₃=2,A₄=8.
Nejde o extrapolaci obecného vzorce z těchto dat.

## P0727: oba směry mřížkové bijekce

Čteme hodnoty1,…,n podle velikosti. Hodnota v liché
pozici udělá svislý krok D, hodnota v sudé krok R.
Je právě a kroků D a b kroků R, takže cíl je(a,b).
Naopak z cesty přiřadíme číslům s krokem D postupně
liché pozice a číslům s R sudé. V obou třídách
jsou čísla automaticky vzestupná. Obě konstrukce
jsou vzájemně inverzní, včetně krajních cest.

## P0728: svislá váha počítá všechny inverze právě jednou

Před krokem(i,j)→(i+1,j) přichází(i+1)-ní lichý
prvek O, umístěný v pozici2i+1. Přesně j sudých
hodnot je menších než O, zatímco přesně i sudých
pozic je před ním. Je-li j≥i, tvoří inverzi s O
právě j−i menších sudých prvků za ním. Je-li j<i,
jsou to právě i−j větších sudých prvků před ním.
V obou případech je počet |i−j|.

Uvnitř třídy nejsou žádné inverze; každá zbývající
inverze má jediný lichý konec. Součet svislých vah
je proto přesně celý počet inverzí, bez dvojího
započtení. Pro poslední lichý prvek při lichém n
je i=b, takže argument stále používá existující
sudé pozice a nic nepočítá za koncem pole.

## P0729: úloha13, vodorovné váhy v přesné souřadnici

Krok(i,j−1)→(i,j) přidává j-tý sudý prvek E
na pozici2j. Před ním je j lichých pozic a přesně
i lichých **hodnot** je menších než E. Jestliže
i≥j, dává i−j menších lichých prvků za E inverze;
jinak j−i větších lichých prvků před E. Váha je
tedy |i−j| u kroku **končícího** v(i,j), nikoli
váha se stejnými startovními souřadnicemi jako u D.
Každá inverze má jediný sudý konec, takže také
součet vodorovných vah dává tentýž celkový počet.

## P0730: úloha12, plocha i lokální záměna kroků

V řádkovém pásu mezi i a i+1 leží svislý krok
dané cesty na sloupci j_i. Schodová cesta DRDR…
ho má na sloupci i. Právě |j_i−i| jednotkových
čtverců leží v tomto pásu mezi oběma cestami.
Sečtení přes všechny pásy dává svislou váhu P0728,
tedy počet inverzí i při opakovaném křížení cest.
Počítá se skutečná plocha s absolutními šířkami,
nikoli orientovaná plocha, která by se mohla rušit.

Při lokální změně DR→RD ze startu(i,j) se dvě
po sobě jdoucí hodnoty k,k+1 prohodí mezi pozicemi
2i+1 a2j+2. Ostatní hodnoty jsou buď menší než obě,
nebo větší než obě, takže se změní jen jejich
vzájemná inverze. Je to+1 pro i≤j a−1 pro i>j.
Totéž přímo plyne z rozdílu vah
|i−j−1|−|i−j|. Tím je dokázán i stručný lokální
argument odpovědi včetně diagonálního případu.

## P0731: všechny části Fig11 a příklad(1)

V permutaci2134657 10 8 11 9 12 14 13 15 jsou liché
hodnoty2,3,6,7,8,9,14,15 a sudé1,4,5,10,11,12,13.
Slovo kroků je

    R D D R R D D D D R R R R D D.

Starty osmi svislých kroků jsou
(0,1),(1,1),(2,3),(3,3),(4,3),(5,3),(6,7),(7,7),
s vahami1,0,1,0,1,2,1,0, součet6. Přesně tomu
odpovídá silná cesta do(8,7). Šest stínovaných buněk
má levé horní souřadnice(0,0),(2,2),(4,3),(5,3),(5,4),(6,6).
Vytištěné řady kurzivních vah jsou postupně
|i−0|,…,|i−7| pro i=0,…,7; jejich nulová diagonála
i obě rostoucí ramena odpovídají definici.

Inverze lze také přímo přiřadit těmto krokům:
(2,1),(6,5),(10,8),(10,9),(11,9),(14,13).
Tím je ověřen nejen součet, ale i přesná interpretace
všech zvýrazněných částí obrázku.

## P0732: úloha11, celý vytištěný tvar cesty

Liché hodnoty vstupu1,2,5,3,7,4,8,6,9,11,10,12
jsou1,5,7,8,9,10 a sudé2,3,4,6,11,12. Cesta je

    D R R R D R D D D D R R,

tedy její lomové body jsou(0,0),(1,0),(1,3),(2,3),
(2,4),(6,4),(6,6). To přesně určuje a potvrzuje
celou vytištěnou kresbu odpovědi, ne jen koncový bod.

## P0733: počty cest přes úsek a všechny meze vzorce(2)

Mezi(a,b) a(a′,b′) se volí pořadí a′−a kroků D
a b′−b kroků R, tedy choose(a′−a+b′−b,a′−a).
Platí i při nulovém rozdílu jedné souřadnice.
Přes konkrétní svislý úsek(i,j)→(i+1,j) je počet

    choose(i+j,i) choose(n−i−j−1,b−j),

protože prefix a suffix se nezávisle spojí tímto
jedním krokem. Skutečné meze jsou0≤i<a,0≤j≤b.
Vynásobení |i−j| a součet dávají oba vzorce(2).

V sudém případě n=2m tisk rozšiřuje i až na m.
Pro i=m,j<m je druhý binomický koeficient0, protože
dolní index m−j převyšuje horní m−j−1. Diagonální
roh i=j=m má nulovou váhu a lze ho předem vypustit;
není třeba mu přisuzovat počet skutečných svislých
kroků. V lichém případě n=2m+1 jsou celé meze
0≤i,j≤m skutečně platné. Toto rozlišení je nutné
pro následující symetrizaci.

## P0734: úloha14(a), přesná symetrizace

Označ L=2m−i−j−1. Po záměně i,j v sudém součtu
jsou druhé koeficienty choose(L,m−j) a choose(L,m−i).
Mimo nulový diagonální roh je L≥0 a

    choose(L,m−i)=choose(L,m−j−1).

Pascalovo pravidlo je tedy sečte na
choose(2m−i−j,m−j), což je druhý koeficient lichého
součtu. První koeficient i absolutní váha jsou
symetrické. Odtud2A_(2m)=A_(2m+1).
V nulovém rohu váha0 dovoluje vypuštění dříve,
než se použije Pascal na záporný horní index.
Pro m=0 je tvrzení A₁=2A₀=0 přímo, definujeme-li A₀=0.

## P0735: úloha14(b), vlastní důkaz použité binomické GF

Pro k≥0 polož S_k(z)=∑_(i≥0)choose(2i+k,i)z^i,
t=sqrt(1−4z), C=(1−t)/(2z), tedy C=1+zC².
Vše jsou formální řady, t(0)=C(0)=1.

Poměr sousedních centrálních binomických koeficientů
dává(1−4z)S₀′=2S₀, S₀(0)=1; jediné řešení je S₀=1/t.
Dále choose(2i+1,i)=choose(2i+2,i+1)/2, takže
S₁=(S₀−1)/(2z)=C/t. Pascalovo pravidlo pro k≥1 dává

    S_k=S_(k−1)+zS_(k+1).

Řady C^k/t splňují tutéž rekurenci díky C=1+zC²
a obě počáteční hodnoty. Indukcí tedy

    ∑_(i≥0)choose(2i+k,i)z^i=C^k/t.

To samostatně dokazuje veškeré zde potřebné případy
identity převzaté zadáním ze svazku1. Pokud se
parametr k nahradí obecným s, koeficient každého z^i
je na obou stranách polynom v s stupně nejvýše i
(vpravo použij exp(s log C)). Shoda pro všechna
nezáporná celá s dává i tuto obecnou formální identitu.

## P0736: úloha14(b), celý součet bez skrytých faktorů2

Lichý součet je symetrický v i,j a diagonála má
váhu0. Po vydělení dvěma z P0734 tedy

    A_(2m)=∑_(0≤i≤j≤m) (j−i) choose(i+j,i)
                              choose(2m−i−j,m−j).

Polož k=j−i a l=m−i−k. Pak i,l,k≥0, i+l+k=m
a druhý koeficient je choose(2l+k,l). Proto

    ∑_(m≥0)A_(2m)z^m
      =∑_(k≥0) k z^k S_k(z)²
      =1/t² · ∑_(k≥0) k(zC²)^k
      =1/t² · zC²/(1−zC²)².

Z C=1+zC² plyne1−zC²=tC, takže poslední výraz
je z/t⁴=z/(1−4z)². Koeficient dává
A_(2m)=m4^(m−1) pro m≥1. S P0734 dostaneme

    A_n=floor(n/2)·2^(n−2), n≥1.

Přeskupení formálních řad je platné, protože každý
koeficient používá pouze konečně mnoho trojic i,l,k.
Obecný vzorec nepochází z numerického odhadu ani
z neověřeného přímého kombinatorického tvrzení.

## P0737: přesný průměr, obě parity a známé zaokrouhlení

Rovnoměrnost P0725 dává E inv=A_n/choose(n,floor(n/2)).
Pro n=2m a centrální binomický odhad ze Stirlinga

    choose(2m,m)=4^m/sqrt(πm)·(1+O(1/m))

vychází E inv=(sqrt(π)/4)m^(3/2)(1+O(1/m)).
Pro n=2m+1 je A dvojnásobné a
choose(2m+1,m)=(2m+1)/(m+1) choose(2m,m),
takže se průměr změní faktorem2(m+1)/(2m+1)=1+O(1/m).
V obou paritách je tedy

    E inv=sqrt(π/128) n^(3/2)(1+O(1/n)).

Konstanta je přibližně0.1567, tedy0.16 na dvě
desetinná místa. To je již známá oprava z7.3.2015,
nikoli nový nález v původní vytištěné hodnotě0.15.

## P0738: ostré maximum, včetně případu h=2 úlohy16

Polož n=2m nebo2m+1 a a=ceil(n/2). Svislé kroky
mají sloupce0≤j₀≤…≤j_(a−1)≤m. Chceme maximalizovat
F=∑|i−j_i|. Pro m>0 lze každý takový vektor napsat
jako konvexní kombinaci vektorů v^(k), které mají
prvních k souřadnic0 a všechny další m:
váhy jsou j₀/m,(j₁−j₀)/m,…,(j_(a−1)−j_(a−2))/m,
1−j_(a−1)/m. Jsou nezáporné a součet je1.
Konvexita absolutní hodnoty tedy omezuje F maximem
na těchto a+1 vektorech; nejde o enumeraci permutací.

Protože i≤m, platí

    F(v^(k))=m(m+1)/2−k(m+1−k), 0≤k≤a.

Maximum je m(m+1)/2. Dosáhne ho cesta nejprve se
všemi R a potom D, tedy přes pravý horní roh obrázku.
Pro sudé n je a=m a každý k>0 dává přísně menší
hodnotu. Rovnost v konvexním odhadu pak vynutí
všechnu váhu u k=0: jediná maximální permutace je

    m+1,1,m+2,2,…,2m,m.

Pro liché n je maximální i opačná krajní cesta;
jedinečnost se netvrdí. Pro m=0 je jediný prvek
a maximum0 přímo. Obecně tedy maximum je
choose(floor(n/2)+1,2)=n²/8+O(n).
Část úlohy16 pro obecné h a celé úlohy17 tím dosud
nejsou uzavřeny; lze později převzít právě tento lemma.

## P0739: všechny čtyři počáteční GF na88

Z úplných malých případů P0726 jsou polynomy

    h₁(z)=1,
    h₂(z)=1+z,
    h₃(z)=1+2z,
    h₄(z)=1+3z+z²+z³.

Tyto h_n počítají permutace **n** prvků. Úloha15
používá místně h_n pro cesty délky **2n**; přechod
indexu se v následném rozptylovém důkazu musí zachovat.
Z pouhých čtyř polynomů neplyne tvrzení o asymptotické
směrodatné odchylce; to zůstává předmětem následující15.

Celé86–87, vzorce průměru/maxima na88 a úlohy11–14
mají samostatné argumenty. Nové matematické mezery
ani nálezy nevznikly; další krok je úplná15 s odpovědí620–621,
nikoli přeskočení přímo na obecné TheoremH.
