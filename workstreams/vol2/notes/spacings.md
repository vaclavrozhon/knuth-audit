# §3.3.2-26/27: rozdělení a iterování spojitých mezer

Uzavřeno1.11.2026. Zadání78–79 a odpovědi566–568 přečteny
v původní sazbě. [C0018](C0018-circular-spacing-labels.md)
opravuje označené kruhové mezery; nové drobné mezitvrzení
[C0022](C0022-spacing-cdf-index.md) a geometrickou formulaci
[C0023](C0023-irrational-spacing-code.md) evidujeme samostatně.
Hlavní výsledky pro seřazené mezery a jejich transformaci mají
následující obecné důkazy. Zde n>=2.

## Proč seřazení odstraní problém C0018

Simplex D je množina vektorů s nezápornými souřadnicemi se
součtem1. Rovnoměrná pravděpodobnost na D má hustotu(n−1)!
v prvních n−1 souřadnicích. Původní mezery S knihy mají místo
toho hustotu n! S_n: poslední mezera obsahuje pevný počátek.
Jejich hustota vzhledem k rovnoměrné pravděpodobnosti je n S_n.

Pro libovolnou symetrickou funkci g, tedy funkci invariantní
při permutaci souřadnic, dává symetrie rovnoměrné míry

```text
E_original g(S) = n E_uniform[S_n g(S)]
               = E_uniform[(S_1+...+S_n)g(S)] = E_uniform g(S).
```

Vektor seřazených mezer má proto přesně stejnou distribuci
v obou modelech. Ve všech dalších výpočtech seřazených mezer
můžeme používat rovnoměrný simplex. To neopravuje původní
tvrzení o **označeném** vektoru v26(a) ani rovnosti jeho zákona
se zákonem transformovaného vektoru v27.

## Distribuce v26(b,c)

Pro nezáporné prahy s_i s celkovým součtem T<=1 posun
souřadnic o s_i zmenší simplex faktorem1−T v každé z n−1
dimenzí. Rovnoměrný model tedy má společnou horní pravděpodobnost
(1−T)^(n−1). Je-li T>1, pravděpodobnost je0. Tím je dokázán
opravovaný geometrický výpočet26(a).

Označme S_(k) k-tou nejmenší mezeru a F_k(s)=Pr(S_(k)<=s).
Pro s>=0 je

```text
Pr(S_(1)>=s) = (1−ns)_+^(n−1),    x_+ = max(x,0).
```

Pro s<0 je F_k(s)=0; formule využívající posun nezáporných
souřadnic nelze bez tohoto omezení mechanicky extrapolovat.
Nechť G_j(s) označuje pravděpodobnost právě j mezer menších
než s. Inkluze a exkluze nad vybranou j-prvkovou množinou dávají

```text
G_j(s) = binom(n,j) sum_(l=0)^j binom(j,l)(−1)^(j−l)
                     (1−(n−l)s)_+^(n−1).
```

Při n>=2 nemají jednotlivé mezery atomy, takže ostré/neostré
nerovnosti nezmění tyto pravděpodobnosti. Událost S_(k)>s má
nejvýše k−1 malých mezer, včetně možnosti **nuly**. Opravené
sečtení G_0 až G_(k−1) a identita pro částečný alternující
binomický součet dávají správný tištěný výsledek

```text
1−F_k(s) = sum_(l=0)^(k−1) binom(n,l) binom(n−l−1,k−l−1)
                 (−1)^(k−l−1) (1−(n−l)s)_+^(n−1).
F_n(s) = sum_(l=0)^n binom(n,l)(−1)^l(1−ls)_+^(n−1).
```

Poslední vzorec má i nezávislé odvození: komplement události,
že některá mezera přesahuje s, opět inkluzí a exkluzí.
Součet n nezávislých rovnoměrných veličin má pro x>0 hustotu

```text
sum_(l=0)^n (−1)^l binom(n,l)(x−l)_+^(n−1)/(n−1)!
 = x^(n−1) F_n(1/x)/(n−1)!.
```

První rovnost plyne derivováním objemu části jednotkové krychle
pod rovinou součtu x; přesahy přes její stěny odečte inkluze
a exkluze. Tím je ověřena také závorka o součtu uniformních veličin.

## Transformace a momenty: nezávislý exponenciální důkaz

E_1,...,E_n nechť jsou nezávislé exponenciální veličiny s hustotou
exp(−x) pro x>=0 a T jejich součet. Změna proměnných E_i=T S_i
má jakobián T^(n−1), proto S=E/T je rovnoměrný na D a nezávislý
na T. Seřaďme E a položme E_(0)=0,

```text
Z_j = (n−j+1)(E_(j)−E_(j−1)),  j=1,...,n.
```

Seřazený vektor E má hustotu n! exp(−sum E_(j)). Inverzní
trojúhelníková substituce na Z má determinant1/n! a zachová součet:
sum E_(j)=sum Z_j. Hustota Z je tedy exp(−sum Z_j), což dokazuje
nezávislé exponenciální složky. Jejich normalizace Y=Z/T je opět
rovnoměrná na D a je právě transformací mezer uvedenou v27.

Platí S_(k)=sum_(j<=k)Y_j/(n−j+1). Integrace monomů na D dává
E Y_j=1/n, E Y_j²=2/[n(n+1)] a E Y_iY_j=1/[n(n+1)] pro i!=j.
Definujme H_r=sum_(j=1)^r1/j a H_r^(2)=sum_(j=1)^r1/j²,
s nulovou hodnotou pro r=0. Píšeme-li h=H_n−H_(n−k) a
h2=H_n^(2)−H_(n−k)^(2), dostáváme

```text
E S_(k) = h/n,
E S_(k)² = (h²+h2)/[n(n+1)],
Var S_(k) = (h2−h²/n)/[n(n+1)].
```

Vše souhlasí s26(d). Nezávislá kontrola integruje výše uvedenou
distribuční funkci přes E X^r=r integral s^(r−1) Pr(X>s) ds.
Beta integrál je

```text
integral_0^(1/a) s^(r−1)(1−as)^(n−1) ds
 = (r−1)!(n−1)! / [a^r(n+r−1)!].
```

Program porovnal oba přístupy přesně pro464 dvojic(n,k),
n=2..30, a2320 hodnot distribučních funkcí; všechny souhlasí.

## Geometrie, kód a původní obrázek

Třídění rozdělí D na n! oblastí. V jedné z nich je inverzní
zobrazení transformace

```text
s_(j) = sum_(i=1)^j y_i/(n−i+1).
```

Sloupce této lineární mapy jsou rovnoměrné váhy posledních
n,n−1,...,1 souřadnic. Mají součet1 a determinant1/n!, proto
inverze zmenší(n−1)-rozměrný objem1/n!. Jiná větev pouze permutuje
řádky. Původní vrcholy i objemová změna v odpovědi27 jsou správné.
Čtverec vzdálenosti vrcholů s j a k nenulovými stejnými vahami
je|1/j−1/k|; obrazové vrcholy mají vzdálenost sqrt(2).

Každé dva sloupce inverzní mapy mají společnou hmotnost alespoň1/n.
Pro dva vektory se stejným součtem se proto jejich vzdálenost
měřená součtem absolutních rozdílů zmenší nejvýše faktorem1−1/n:
rozložme rozdíl na kladnou a zápornou část stejné hmotnosti
a odečtěme překryv jejich obrazů. Každé nekonečné slovo tedy
vymezuje vnořené kompaktní simplexy s průměrem směřujícím k0,
a tudíž jediný bod. Opačná jednoznačnost vyžaduje vyloučit
hranice nebo zadat pravidlo pro rovnosti; viz C0023.

`results/spacings-triangles.svg` rekonstruuje všech36 popisků
obrázku na567. Vizuální porovnání s originálem souhlasí.
Přesné souřadnice, obsahy a správné kódy těžišť byly ověřeny
na prvních třech úrovních, celkem258 trojúhelníků. Všech366
společných hran sousedních dvojic má kódy lišící se jedinou
číslicí. Obecně při přechodu přes stěnu dvě třídicí permutace
zamění stejné sousední hodnoty; následné obrazy na stěně se
shodují. Liší se tedy jen číslice v prvním stupni tohoto přechodu.
Sousedství zde znamená společnou stěnu, nikoli pouhý společný vrchol.

## KS test a konečná přesnost

Částečné součty prvních n−1 souřadnic rovnoměrného D jsou
uspořádaná nezávislá uniformní pozorování. Přímá substituce
do definic KS statistik proto dává oba vzorce na79, včetně
znamének a normalizace sqrt(n−1). Po první transformaci platí
tento závěr i pro původní kruhové mezery. Jednotlivé iterované
vektory mají správné marginální rozdělení, ale nejsou navzájem
nezávislé; celý postup je deterministický.

Pro n=2 je první souřadnice po transformaci2 min(x,1−x).
Mimo0,1/2,1 je to uvedené zdvojení modulo1 s případným
prohozením souřadnic. U dyadického x=k/2^e se při každém
nehraničním kroku zkrátí jmenovatel o faktor2, následně
1/2 ->1 ->0. Celkem nejvýše e+1 kroků vede k(0,1).
Kontrola32780 dyadických vstupů pro e=1..14 i všech16 vytištěných
Grayových kódů souhlasí.

Pro n>=3 není závěr o jediném koncovém vrcholu oprávněný:
(3/8,1/2,1/8) je netriviální pevný bod už pro n=3. Kniha uvedla
mez e+1 výslovně pro n=2; tento příklad tedy není její vyvrácení.
Obecně na pevné konečné mřížce vznikne konečný funkční graf
a trajektorie nakonec periodická. To omezuje opakované používání
testu, ale samo nezaručuje, že každá trajektorie někdy překročí
zvolený kritický práh jediné KS statistiky.

## Zdroje, errata a přesný rozsah

Všechny matematické závěry výše mají vlastní důkazy. Pět bloků
`verify_spacings.py` prošlo, session39887 skončila0; podrobnosti
jsou v `results/spacings.json`. Oprava Whitworthovy atribuce
z18.9.2002 zahrnuta. Všechny čtyři řady errat a aktuální TeX
prohledány1.11.2026; C0022/C0023 v nich nenalezeny.

Bibliografická kontrola je v `sources/spacings-bibliography.json`.
Vydavatelské záznamy potvrzují Barton–David1956 a Daniels1962;
institucionální záznam potvrzuje Sukhatme1937. Pykeho rozsah
395–449 zahrnuje následnou diskusi, takže kratší metadata samotného
článku395–436 nejsou chybou knihy. Durbinova vlastní oprava1966
cituje původní rozsah41–55; dnešní záznam41–65 je s tím i
s následujícím článkem57–63 v rozporu a není důvodem měnit Knutha.
Plné původní články ani Whitworthova Proposition LVI nebyly
v tomto bloku přečteny. Historické prvenství tedy není nově
potvrzeno a úplnost tohoto bibliografického pátrání se netvrdí.
