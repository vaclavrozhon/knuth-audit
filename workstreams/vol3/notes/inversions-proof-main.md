# Inverze: jednotlivé argumenty hlavního textu

S. 11–17; zároveň uzavřeny důkazy úloh §5.1.1-3,10,14,15,25,
které hlavní text používá. Přebírá se bijekce inverzních tabulek a
obecný převod na páskách z V3-P0030/31. Neproběhl žádný výpočetní
test ani enumerace. Prohlédnuta sazba obrázku13, diagramu14 a tabulek
15–16. Známá errata jsou v sources/inversions-errata-review.json;
žádný nový nález.

## Definice, příklady a inverzní tabulka

- U3142 jsou špatně právě páry(3,1),(3,2),(4,2). Nulový počet
  inverzí nutí každou dvojici ve správném pořadí, tedy identitu.
  Determinant na11 je definován Leibnizovým součtem; změna znaménka
  při sousední transpozici plyne z níže dokázané změny inverzí o1.
- Pro591826473 má tabulka po sloupcích počty2,3,6,4,0,2,2,1,0,
  součet20. Všechny vytištěné mezistavy rekonstrukce vznikají vložením
  j za b_j již umístěných větších prvků. Rozsah0≤b_j≤n−j je nutný
  a takto i postačující. Jednoznačnost a počet n! se přebírají z
  V3-P0030; rovnoměrná permutace odpovídá nezávislým rovnoměrným b_j.
- j je maximum zprava právě tehdy, jsou-li všichni větší vlevo,
  tedy b_j=n−j. Pravděpodobnost je1/(n−j+1), proto očekávání H_n.
  Z nezávislosti plyne pravděpodobnostní GF ∏_(k=1)^n(z+k−1)/k.
  U příkladu jsou maxima zprava3,7,8,9, jak uvádí text.
- Sousední prohození mění pouze vzájemné pořadí prohozených prvků;
  vztah každého z nich k ostatním zůstává stejný. Inverzí přibude
  či ubude1. Každá sestupná cesta v obrázku proto má délku inv(π).

## Obrázek13 a úloha10

Pro vrchol π vezmi jeho inverzní vektor(a′₁,a′₂,a′₃,a′₄), odečti
(5/2,…,5/2) a použij ortonormální souřadnice
x=(a′₁+a′₂−a′₃−a′₄)/2,
y=(a′₁−a′₂+a′₃−a′₄)/2,
z=(a′₁−a′₂−a′₃+a′₄)/2.
Dostaneme právě24 permutací souřadnic(0,±1,±2). Prohození sousedních
pozic π znamená prohození dvou sousedních hodnot v a′ a má délku√2.
Tři sousedé každého vrcholu v kresbě odpovídají právě třem takovým
prohozením; zobrazené štítky dávají všech24 permutací.

Konvexní těleso má šest čtverců v rovinách x_i=±2 a osm pravidelných
šestiúhelníků v rovinách ±x±y±z=3. Všechny hrany mají délku√2,
každý vrchol stupeň3; E=36 a24−36+14=2. Jde o komolý osmistěn.
Vrcholy mají normu√5 a jsou ve dvojicích antipodální, tedy maximální
vzdálenost2√5. Po normalizaci hrany na1 je průměr√10, odpověď10.

Vektorová alternativa odpovědi10: součet(e_u−e_v) přes inverze má
j-tou složku c_j−b_j=j−a′_j, tedy je izometrický překlad záporného
inverzního vektoru. Pro4321 je(−3,−1,1,3), vzdálenost√20 oproti
hraně√2. Starší chybný seznam 3D vektorů opravilo erratum21.3.2019.
Konzistentní směry pro21,31,32,41,42,43 jsou postupně
(1,1,0),(1,0,1),(0,−1,1),(0,1,1),(−1,0,1),(−1,1,0), dělené√2;
mají délku1, aditivní vztahy mezi kořeny a součet(0,2,4)/√2.

Také zmínku o vyplnění prostoru lze doložit přímo. P={|x_i|≤2,
|x|+|y|+|z|≤3} je Voronoiova buňka mřížky
L=4Z³ ∪ ((2,2,2)+4Z³). Sousedé(±4,0,0),… a(±2,±2,±2)
dávají právě uvedené nerovnosti. Pro další bod2a s komponentami
a stejné parity potřebujeme x·a≤Σa_i². Je-li a sudé, plyne to z
2Σ|a_i|≤Σa_i². Je-li a liché a |a₁|≥|a₂|≥|a₃|≥1,
maximum na P je2|a₁|+|a₂|≤Σa_i²; pro(1,1,1) je rovnost,
pro větší lichou složku je nerovnost přísná. Žádný další bod tedy
buňku neomezuje. Voronoiovy buňky mřížky pokryjí prostor s disjunktními
vnitřky. Historické atribuce Archimédovi a údaj o Pappově seznamu13
těles jsou ponechány bibliografii.

## Inverzní permutace a Rotheho diagram

Z definice a′_j=k právě když a_k=j plyne inverze591826473→359716842.
Pole(i,j) obsahuje křížek právě když j<a_i a i<a′_j. To je bijekce
na inverze(a_i,j), a počet v j-tém sloupci je b_j. V tištěném diagramu
jsou řádky křížků {1,2,3,4}, {1,2,3,4,6,7,8}, ∅,
{2,3,4,6,7}, ∅, {3,4}, {3}, {3}, ∅; přesně20 polí.
Transpozice permutační matice vytvoří inverzní permutaci a podmínka
křížku je vůči transpozici symetrická. Tedy inv(π)=inv(π⁻¹).
V determinantovém součtu se po transpozici matice pouze nahradí
π zaπ⁻¹ a přeznačí index součinu; znaménko zůstane, proto det A=det Aᵀ.

## Generující funkce, tabulka a malé koeficienty

I_n(0)=1. Pro jedinou inverzi musí právě jedna z b₁,…,b_(n−1)
být1 a ostatní0, tedy I_n(1)=n−1. Obrácení celého pořadí mění
b_j na n−j−b_j: větší prvky před/za j se zamění. Tím je současně
dokázána úloha3 a symetrie I_n(k)=I_n(binom(n,2)−k).

Nezávislé volby b_j dávají G_n(z)=∏_(r=1)^n(1+…+z^(r−1))
=∏(1−z^r)/(1−z)^n. Násobení po řádcích poskytuje celé nenulové
řádky tabulky1, bez generování permutací:

1; 1,1; 1,2,2,1; 1,3,5,6,5,3,1;
1,4,9,15,20,22,20,15,9,4,1;
1,5,14,29,49,71,90,101,101,90,71,49,29,14,5,1.

Všechny zobrazené koeficienty tabulky a její nuly souhlasí.
Z (1−z)G_n=(1−z^n)G_(n−1) plyne úplná rekurence
I_n(k)=I_n(k−1)+I_(n−1)(k)−I_(n−1)(k−n).
Pro0≤k<n je poslední člen0, což dokazuje(9).

Pro n≥k lze čitatel nahradit nekonečným produktem do stupně k.
Franklinův důkaz níže dává1−z−z²+z⁵+z⁷−… . Koeficient
z^r v (1−z)^−n je binom(n+r−1,r). Spojením prvních1−z dostaneme
první binomický člen(10); zbývající pentagonální mocniny dávají přesně
oba uvedené členy pro každé j. První čtyři případy jsou
I_n(2)=binom(n,2)−1, I_n(3)=binom(n+1,3)−n,
I_n(4)=binom(n+2,4)−binom(n+1,2),
I_n(5)=binom(n+3,5)−binom(n+2,3)+1, s vytištěnými mezemi n.
Počet nenulových pentagonálních členů je
2sqrt(2k/3)+O(1)=1.63299…sqrt(k)+O(1), tedy uvedené přibližné1.6sqrt(k).

## Franklinova involuce, úloha14

Pro rozklad na k různých částí λ₁>…>λ_k=m nechť j je délka
počátečního úseku, kde sousední části klesají přesně o1.
Je-li m>j, odeber1 z prvních j řádků a přidej poslední část j.
Vznikne opět rozklad na různé části, kromě případu j=k,m=k+1;
tehdy by se poslední část opakovala. Je-li m≤j, odstraň poslední
část m a přidej1 do prvních m řádků. Opět to funguje, kromě
případu m=j=k, kdy po odstranění posledního řádku není dost řádků.

V prvním platném případě má nový nejkratší řádek délku j a
počáteční úsek délku alespoň j, takže druhá operace vrátí původní
rozklad. V druhém případě má nový počáteční úsek délku m a
nejkratší řádek delší než m, takže jej vrátí první operace.
Součet částí se nemění, počet částí se změní o1. Nepárové rozklady
jsou (2k−1,…,k) a(2k,…,k+1), součtů k(3k−1)/2 a k(3k+1)/2,
se znaménkem(−1)^k; navíc prázdný rozklad dává1. To dokazuje
pentagonální identitu i úlohu14. Pro7 jsou uvedené pětice rozkladů
úplné a jejich znaménkový součet−1+3−1=1.

Obyčejné rozklady mají GF ∏_(j≥1)(1−z^j)^−1 volbou násobnosti
každé části. Násobení pentagonálním produktem a porovnání koeficientů
dává uvedenou rekurenci p(n), s p(0)=1 a p(t)=0 pro t<0.

## Pravděpodobnost a index

Přebírá se již ověřený rozklad na nezávislé uniformní b_j:
g_n=∏h_k, E h_k=(k−1)/2 a var h_k=(k²−1)/12. Součty dávají
E inv=n(n−1)/4 a var inv=n(n−1)(2n+5)/72, tedy σ~n^(3/2)/6.
Nový běh k těmto dříve uzavřeným vzorcům nebyl proveden.

Všech24 vytištěných řádků tabulky index/inverze na16 bylo posouzeno
přímo součtem pozic sestupů a počtem větších předchůdců. Po skupinách
počátečního prvku mají dvojice(index,inv) následující hodnoty:

1: (0,0),(3,1),(2,1),(3,2),(2,2),(5,3).
2: (1,1),(4,2),(2,2),(3,3),(2,3),(5,4).
3: (1,2),(4,3),(3,3),(4,4),(2,4),(5,5).
4: (1,3),(4,4),(3,4),(4,5),(3,5),(6,6).

Souhlasí všechny vytištěné hodnoty i jejich stejné okrajové četnosti.

## MacMahonova bijekce a úloha15

Stabilně seřaď q podle klesající hodnoty s pořadím indexů a₁,…,a_n.
Označ D množinu sestupů a a d_i=|{j∈D:j≥i}|. Pak p_i=q_(a_i)−d_i.
Máme p_i−p_(i+1)=q_(a_i)−q_(a_(i+1))−[i∈D]≥0; při sestupu je
rozdíl q alespoň1 díky stabilitě. Také p_n=q_(a_n)≥0. Součet
odečtených d_i je Σ_(j∈D)j=ind(a), což dokazuje váhový vztah(15).

Inverze je q_(a_i)=p_i+d_i. Pokud se dvě sousední takto obnovené
hodnoty rovnají, musí být i∉D, a tedy a_i<a_(i+1). Seřazení je
proto právě původní stabilní seřazení; obě konstrukce jsou inverzní.
Pro vytištěné q=(3,1,4,1,5,9,2,6,5) je a=685931724, D={2,4,5,7},
d=(4,4,3,3,2,1,1,0,0), p=(5,2,2,2,2,2,1,1,1). Součty jsou36
a18 a index18, jak vyžaduje(15).

Pro nezáporné rozdíly r_i=p_i−p_(i+1)≥0, s p_(n+1)=0, platí
Σp_i=Σi r_i. Proto P_n(z)=∏_(i=1)^n(1−z^i)^−1. Také přímo
Ferrersova konjugace p′_j=#{i:p_i≥j} převádí nejvýše n řádků na
části nejvýše n a zachovává počet buněk; inverse počítá sloupce.
To úplně dokazuje úlohu15 i použití(16). Libovolná n-tice q má
GF(1−z)^−n; váhová bijekce tedy dává Q_n=H_nP_n, a H_n=G_n.

## Foata–Schützenberger, úloha25

Piš a=x₁α₁…x_kα_k t, kde t je poslední prvek a x_j jsou všechny
prvky na stejné straně t jako první prvek. Definuj h(a)=α₁x₁…α_kx_k.
Při a₁<t otočení bloků přidá Σ|α_j| inverzí a odebrání posledního t
jich právě tolik ubere, tedy inv h=inv a. Při a₁>t otočení ubere
Σ|α_j| a odebrání t dalších k, tedy inv h=inv a−(n−1).

Definice f(a)=f(h(a))t, s jednobodovou bází, je bijekce. Z posledního
prvku h totiž zjistíme stranu t a jedinečně rozřežeme h do bloků α_jx_j;
jejich obrácením obnovíme a. Rekurzivně invertujeme kratší f.
Poslední prvek f(h(a)) je x_k, takže připojení t zvýší index o0,
resp. n−1. Indukce dává ind f(a)=inv a.

Uvnitř h se přehazují pouze páry ležící na opačných stranách t;
mezi nimi stojí t, takže nemohou být dvěma po sobě jdoucími hodnotami.
Poloha t zůstává poslední. Indukce tak zachová relativní pořadí každé
dvojice j,j+1, neboli ind((f(a))⁻¹)=ind(a⁻¹).

V obou tištěných příkladech dává postupné h tyto kratší řetězce:

198263745 → 98162734 → 9182637 → 192638 → 91263 → 1296 → 192 → 91 → 9.
192687345 → 91687234 → 1968237 → 918623 → 19826 → 9812 → 918 → 19 → 1.

Poslední odebírané prvky v obráceném pořadí dávají f(198263745)=912638745
a f(192687345)=198263745. Oba vytištěné výsledky tedy souhlasí.

Označ R inverzi permutace. Bijekce g=R∘f⁻¹∘R∘f∘R má
inv g(a)=ind a a ind g(a)=inv a: použij postupně inv R=inv,
ind f=inv a ind Rf=ind R. Je to přímo složení inverzí obou právě
dokázaných bijekcí. Tím je uzavřeno(25b) i symetrie společného
rozdělení indexu a inverzí tvrzená na17.

Aktivní pořadí dalších úloh začíná §5.1.1-1 na17/file28.
Hotové3,10,14,15,25 a obecný důkaz5 se později pouze odkážou.
