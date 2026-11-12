# Úlohy 68–70: svědek Y, obecná reprezentace a flip prime bodu

Checkpoint X0096, P0905–P0915. Originál zadání p89/file106
a odpovědi p547/file564 přečten; podrobný výřez je
`images/proof-y59-detail.png`. Žádný matematický program,
census ani procházení všech obarvení. Přesně se přebírá
celá kondenzace a selfdualita Y z proof-066, prime antichain
z proof-035/proof-065 a průnik prime termů z proof-059, P0826.

## 68: prime implikant je právě minimální Y — P0905

Y je monotónní podle P0902. Jeho prime implikanty proto
odpovídají minimálním pravdivým množinám pozic, přesně podle
P0609–P0611 a P0890. Množina černých pozic je pravdivá právě
když obsahuje souvislou podmnožinu dotýkající se všech stran.
Pokud je pravdivá množina minimální, touto podmnožinou musí
být ona sama. Obráceně Y, které přestane být Y po odebrání
kteréhokoli vrcholu, je minimální pravdivá množina: kdyby
obsahovalo menší Y, odstranění vrcholu mimo ně by nevadilo.
Počet proměnných v prime termu je tedy přesně počet kamenů.

## Všech 59 kamenů z odpovědi 68 — P0906

Použijme v(r,j)=(j,r−j,15−r), stejně jako v proof-066.
Původní obrázek dává tyto úplné černé řádky:

| r | černá j |
|---|---|
| 0 | žádné |
| 1 | žádné |
| 2 | žádné |
| 3 | 1,2 |
| 4 | 1,3 |
| 5 | 1,4 |
| 6 | 1,5 |
| 7 | 1,3,4,6 |
| 8 | 0,1,3,5,6,8 |
| 9 | 3,8 |
| 10 | 1,2,4,5,6,7,9 |
| 11 | 1,3,8,10 |
| 12 | 2,4,5,7,8,10 |
| 13 | 1,2,6,7,11,12 |
| 14 | 1,4,5,9,10,13 |
| 15 | 2,3,4,6,7,8,9,11,12,13 |

Počty jsou 0,0,0,2,2,2,2,4,6,2,7,4,6,6,6,10, součet 59.
Všechny kameny v pořadí tvoří tuto jedinou cestu:

    (8,0)—(8,1)—(7,1)—(6,1)—(5,1)—(4,1)—(3,1)
    —(3,2)—(4,3)—(5,4)—(6,5)—(7,6)—(8,6)—(8,5)
    —(7,4)—(7,3)—(8,3)—(9,3)—(10,4)—(10,5)—(10,6)
    —(10,7)—(11,8)—(12,8)—(12,7)—(13,7)—(13,6)
    —(12,5)—(12,4)—(11,3)—(10,2)—(10,1)—(11,1)
    —(12,2)—(13,2)—(13,1)—(14,1)—(15,2)—(15,3)
    —(15,4)—(14,4)—(14,5)—(15,6)—(15,7)—(15,8)
    —(15,9)—(14,9)—(14,10)—(15,11)—(15,12)—(15,13)
    —(14,13)—(13,12)—(13,11)—(12,10)—(11,10)—(10,9)
    —(9,8)—(8,8).

Žádná hrana mimo cestu nechybí v této kontrole: vodorovné
hrany jsou sousední j v řádkové tabulce, celkem 22.
Mezířádkové dvojice j→k mezi r a r+1 jsou úplně:

| r | j→k |
|---|---|
| 0,1,2 | žádné |
| 3 | 1→1,2→3 |
| 4 | 1→1,3→4 |
| 5 | 1→1,4→5 |
| 6 | 1→1,5→6 |
| 7 | 1→1,3→3,4→5,6→6 |
| 8 | 3→3,8→8 |
| 9 | 3→4,8→9 |
| 10 | 1→1,2→3,7→8,9→10 |
| 11 | 1→2,3→4,8→8,10→10 |
| 12 | 2→2,5→6,7→7,10→11 |
| 13 | 1→1,12→13 |
| 14 | 1→2,4→4,5→6,9→9,10→11,13→13 |

Těchto 36 hran doplňuje přesně 58 hran uvedené cesty.
Jediný černý bod na x straně je (8,0), na y straně (8,8).
Cesta má také černé body na spodní straně r=15. Každé Y
musí spojit oba koncové body, a proto obsahovat celou cestu.
Odstranění jakéhokoli bodu Y zničí. Je tedy doložen skutečný
prime implikant velikosti 59 a dolní mez optima pro n=15.
Nevyvozuje se horní mez 59 ani počet všech takových řešení.

## První dvě optima bez enumerace — P0907

Pro n=1 jsou vrcholy tři rohy. Každé dva už tvoří Y,
jediný nikoli; všechny minimální Y mají velikost 2.

Pro n=2 jsou tři rohy a tři středy stran. Tři středy tvoří
trojúhelník a minimální Y velikosti 3. Větší minimální Y není:
obsahuje-li všechny tři středy, už má pravdivou trojici.
Obsahuje-li přesně dva středy, pokrývají dvě strany; kterýkoli
roh na třetí straně je sousední alespoň jednomu z nich,
a tyto tři body tvoří Y. Pokud takový roh není přítomen,
zbývá k oběma středům nejvýše jediný roh mimo třetí stranu,
tedy nejvýše tři body celkem. Při nejvýše jednom středu jsou
souvislé komponenty tvořeny tímto středem a jeho nejvýše
dvěma sousedními rohy, nebo izolovanými rohy; opět nejvýše
tři body na komponentu. Maximum je proto přesně 3.

## Co v 68 zůstává nedoloženo — P0908/P0909

P0908 zůstává partial pro jednotlivé vytištěné horní meze

    n=3..15: 4,6,8,11,14,18,23,27,33,39,45,52,59,

a pro přesný census 258594 řešení při n=15. Hodnoty pro
n=1,2 jsou dokázané výše; explicitní 59kamenná cesta dává
jen dolní mez pro n=15. Žádná z ostatních položek tabulky
není uzavřena odkazem na tuto cestu ani na vytištěnou odpověď.
Reprodukce globálních optim/censu by byla nové prohledávání,
které zde neběží. Dosavadní přesné důkazy jiných svazků
neobsahovaly tento konkrétní census.

P0909 samostatně ponechává tvrzení o „fairly small ZDDs“
k pozdějšímu auditu §7.1.4. Kondenzace je booleovský obvod,
sama o sobě nedokazuje malou velikost ZDD prime rodiny.
Kniha zde neudává konkrétní počet uzlů ani obecnou asymptotickou
mez; takové číslo nebylo domyšleno.

## 69: libovolná volba proměnných a všechny prime termy — P0910

Nechť f má prime termy p_0,...,p_m a m≥1. Každé dva termy
mají společnou proměnnou podle již dokázaného P0826, takže
požadovaný výběr T_abc vždy existuje. Převeďme jeho indexy na

    i=a,  j=a+b+1;   0≤i<j≤m,

s inverzí (a,b,c)=(i,j−i−1,m−j). Každý vrchol tak nese
proměnnou společnou p_i,p_j. Strany jsou i=0, j=i+1 a j=m.
Při přechodu po hraně se obě čísla i,j změní nejvýše o 1.

Každá souvislá Y množina musí použít pro každé k∈{0,...,m}
některý vrchol s i=k nebo j=k. Pro k=0 a k=m to plyne
přímo z dotyku stran. Pro 0<k<m předpokládejme opak.
Vrcholy bez indexu k se dělí na tři oblasti

    j<k;    i<k<j;    i>k.

Žádná hrana nevede mezi oblastmi: musela by některým indexem
přeskočit k bez hodnoty k. Souvislá množina je tedy uvnitř
jediné oblasti. První nemůže dosáhnout strany j=m, třetí
strany i=0 a prostřední strany j=i+1. Žádná nemůže být Y.
To dokazuje přesně tvrzení odpovědi „at least one variable
in each p_j“, nikoli jen dotyk prvního a posledního termu.

Je-li Y(T(x))=1, její černé vrcholy proto obsahují aspoň
jednu proměnnou s hodnotou 1 z každého p_k. V komplementu
x se tedy každý prime term stane nepravdivým, takže
f(¬x)=0 a selfdualitou f(x)=1. Máme Y(T(x))≤f(x).

Složená funkce Y(T(x)) je selfduální i při opakování proměnných:
komplement x komplementuje každou pozici T. Nerovnost pro
¬x dává po komplementaci opačnou nerovnost pro x. Proto
Y(T(x))=f(x) pro každý vstup a každou povolenou volbu T.
Nepoužívá se žádný census funkcí ani jen ověření příkladu.

## Přesný příklad 69 — P0911

Položme p_0=wx, p_1=wy, p_2=wz, p_3=xyz. Všech šest
zobrazených buněk trojúhelníku je přípustných: tři horní w
jsou ve dvojicích p_0/p_1, p_0/p_2, p_1/p_2 a spodní
x,y,z ve dvojicích p_0/p_3, p_1/p_3, p_2/p_3.
Tyto čtyři prime termy i identita s M_5(x,w,y,w,z) jsou
přesně případ P0897 se zdvojeným w, tedy hotový důkaz se neopakuje.

Pro přímou kontrolu indexace dává první kondenzace w,
m(w,x,y), m(w,y,z). Poslední medián je při w=0 roven xyz,
při w=1 roven x∨y∨z, tedy přesně wx∨wy∨wz∨xyz.

## Projekční větev 69 — P0912, partial jen rozsah konstrukce

Má-li f jediný prime term, selfdualita a monotónnost nutí
f=x_i podle P0826. Pak m=0 a vytištěný řád m−1 je −1;
neprázdný trojúhelník takového řádu není definován. Samotná
projekce má samozřejmě reprezentaci jednobodovým Y řádu 0.
Obecný důkaz P0910 pokrývá každou uvedenou existující síť;
vynechanou projekční konstrukční větev vedeme stručně jako
partial, bez nové chybové karty a bez tvrzení, že nelze f vyjádřit.

## 70: změna dvou komplementárních bodů — P0913

Původní vzorec je

    g(x)=(f(x) AND [x≠t]) OR [x=¬t].

Pro n≥1 jsou t a ¬t různé. Funkce má g(t)=0, g(¬t)=1
a na ostatních vstupech je f. Komplementace páru {t,¬t}
ukazuje selfdualitu g, ať je t jakýkoli. Algebraicky lze
vzorec také psát (f(x) OR [x=¬t]) AND [x≠t]; komplement
jeho hodnoty v ¬x se po De Morganovi vrátí k původnímu
výrazu, protože 1−f(¬x)=f(x). Tím jsou doloženy všechny
rovnosti první části odpovědi a její tvrzení o libovolném t.

Jestliže t je indexový vektor prime implikantu, je minimální
pravdivý bod: f(t)=1 a f(u)=0 pro každé u<t. Selfdualitou
je ¬t maximální nepravdivý bod: f(v)=1 pro každé v>¬t.
Proto se hodnoty v obou uvedených bodech skutečně obrátí.

## 70: obecný důkaz monotónnosti pro n≥2 — P0914

Pro n≥2 má t nejméně jednu 1, protože f(0)=0. Nemůže být
samé 1: pak by minimalita říkala f(x)=AND_i x_i, což není
selfduální pro n≥2 (na libovolném nekrajním x jsou f(x)
i f(¬x) rovny 0). t tedy má také 0. t a ¬t jsou proto
neporovnatelné v souřadnicovém pořadí.

Pro u≤v může g(u)>g(v) nastat pouze kvůli jedné změněné
hodnotě, jinak by odporovalo monotónnosti f. Je-li u=¬t,
pak v=¬t dává g(v)=1; pro v>¬t je f(v)=1 a v≠t díky
neporovnatelnosti, takže opět g(v)=1. Je-li v=t, pak
u=t dává g(u)=0; pro u<t je f(u)=0 a u≠¬t, tedy g(u)=0.
Jiné změny zvyšující dolní nebo snižující horní hodnotu nejsou.
Proto g je monotónní. Důkaz platí i pro projekci s více než
jednou formálně uvedenou proměnnou; není nutné omezit se
na funkce závisící podstatně na všech vstupních bitech.

## 70: skutečný jednobitový protipříklad — P0915 / F0008

Pro n=1 vezměme f(x)=x. Je monotónní, selfduální a má jediný
prime implikant x, tedy t=1. Vzorec dává g(0)=1, g(1)=0.
g je negace, a proto není monotónní. Původní zadání má „any
monotone and self-dual Boolean function“ bez n≥2 či vyloučení
projekcí; definice na p63 i singletonová větev p64 je výslovně
připouštějí. Odpověď selhává ve větvi y=t, x=¬t: tvrdí
g(x)=0, ačkoli je 1. Nejde jen o chybějící důkaz pravdivého
závěru; závěr s touto doménou je nepravdivý.

Přesná nejmenší oprava je přidat n≥2. Její dostatečnost
dokazuje celý předchozí oddíl, takže nejde o neověřený návrh.
Samostatná stručná evidence je ve F0008-unary-prime-flip.md.
Závažnost low: pouze chybějící dolní mez arity; selfdualita
zůstává pravdivá a všechny případy n≥2 fungují.

## Errata a bibliografie

Dne 2026-11-07 cíleně prohledány `all4a-pre`, `all4a`,
`err4a`, `all4f0`, `all4f1` podle 89/547, 68–70,
prime implicant, selfdual, Meyerowitz, Bioch, Ibaraki a Y.
Historická F0 náhrada 68 (p166, 25. 8. 2008) je již
zahrnuta v prvním dotisku 4A; neověřuje sama census.
Přesuny 67 a oprava p547 line −5 se netýkají 70.
Žádné relevantní erratum nepřidává n≥2 k 70 ani nemění flip.

Meyerowitzova autorská bibliografie v primárním
[FAU dokumentu, p97](https://www.fau.edu/iea/documents/pdf/pr2015/mathss2015.pdf)
uvádí článek Maximal Intersecting Families, European Journal
of Combinatorics 16 (1995), 491–501. DOI a primární IEEE
text Bioch–Ibaraki byly při této kontrole nedostupné;
celé články, datum objevu 1989 a nezávislost objevů nejsou
ověřené. Jsou to explicitní bibliografické výjimky; žádný
matematický krok výše na těchto externích výsledcích nestojí.

Úlohy 71/72/73/74/76 se na dalším místě přesně převezmou
z proof-063/064; nebudou znovu řešeny. Zbývá abstraktní 75
a hlavní text p67. P68 census/ZDD, projekční rozsah P0912
a všechny starší přesné mezery brání celostránkovému uzavření.
