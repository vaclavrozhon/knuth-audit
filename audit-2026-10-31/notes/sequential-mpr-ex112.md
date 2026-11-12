# MPR112: úplná konstrukce nejmenší rodiny a všechny tabulky

7. listopadu 2026. Zadání p23/file43, odpověď p387–388/files407–408
a autorův PS11.9.2019 p23/file29, p44/file50 přímo zobrazeny.
Kontrola zahrnuje každý krok, včetně tvrzeného zachování cyklických
posunů při neprázdném stabilizátoru. Původní sv1 p72 a488 a sv3
p534 zobrazeny pouze v rozsahu potřebných odkazů. Šest vrstev
errat a tři TeX zdroje posouzeny: E133 je známá již zapracovaná
oprava zadání; F174 je jiná, lokální chyba tří ilustračních tabulek.
Fyzický výtisk ani nezávislé kořenové přijetí se netvrdí.

## Obor a skutečný význam truncation

Nechť n≥1 a 0≤m≤n. Každý řádek obsahuje právě jednou hodnoty
1,...,m a jinde∞. Všechny N řádky se vybírají rovnoměrně, jejich
indexy se zachovávají i v počátečních fázích, kdy jsou některé
částečné řádky stejné. Pro neprázdnou A vítězí prvek s nejmenší
konečnou hodnotou, pokud existuje. Jinak se vítěz vybírá rovnoměrně
z A. Tato poslední volba je pomocná pro definici; nemusí současně
tvořit jednu náhodnou permutaci pro všechny A. Při m=n žádné
pomocné losování nezbývá. Pro m=0 je každý řádek zcela prázdný
a podmínka minwise platí triviálně. Pro n=1 je počáteční m=1
již konečným výsledkem.

Tištěný úvod tvrdí, že truncation libovolné přesně minwise rodiny
zachovává tuto vlastnost. To vyžaduje argument, protože z pouhé
rovnosti nepodmíněných vítězných pravděpodobností nelze bez dalšího
přejít k podmínění na velikost minima. Úplný důkaz je následující.

Pro a a T⊆[n]\\{a}, |T|=t, nechť U=[n]\\(T∪{a}). Inkluze
a exkluze dává pro množinu prvků s obrazem menším než aπ:

```
P({x:xπ<aπ}=T)
 = Σ_{V⊆T} (−1)^|V| P(aπ=min_{x∈U∪V∪{a}} xπ)
 = Σ_{j=0}^t (−1)^j binom(t,j)/(n−t+j)
 = t!(n−t−1)!/n! = 1/(n binom(n−1,t)).                 (1)
```

První rovnost vynucuje, aby každý člen T byl před a a každý
člen U za a; rovnosti obrazů odlišných prvků nejsou možné.
Druhá používá přesně minwise vlastnost. Třetí je integrál
∫_0^1 x^(n−t−1)(1−x)^t dx: rozvinutí posledního faktoru
dává součet, t integrací per partes dává uvedený faktoriálový
podíl. Všechny exponenty jsou nezáporné, takže žádná konvergence
ani hraniční člen není problém.

Pro pevnou neprázdnou A a a∈A nastane konečné vítězství a po
m-truncation právě tehdy, když T⊆[n]\\A a |T|≤m−1.
Součtem(1) přes taková T dostaneme stejnou pravděpodobnost pro
každé a∈A. Událost, že všechny prvky A mají obraz>m, přidá
každému stejný příspěvek P(událost)/|A|. Vítěz je vždy právě
jeden, tedy celková pravděpodobnost každého je1/|A|.

Navíc pro pevnou m-prvkovou množinu T, m≥1, je událost
{pozice hodnot1,...,m jsou právě T} disjunktním sjednocením
událostí z(1) s a∈T a předchůdci T\\{a}. Její pravděpodobnost
je m/(n binom(n−1,m−1))=1/binom(n,m). Proto mají všechny
množiny prázdných pozic stejné četnosti i při truncation hotové
minwise rodiny. Ve vlastní konstrukci tuto vlastnost zároveň
udržujeme přímou indukcí níže; neodkazujeme kruhem na existenci
rodiny, kterou teprve konstruujeme.

##(a): přesný lokální argument pro každou A

Předpokládejme m<n a označme k=n−m>0. Seskupme řádky podle
jejich k-prvkové množiny prázdných pozic B. Ve skupině je R_B
řádků. Předpis lze provést, pokud k dělí R_B, včetně R_B=0:
do každé z k pozic vložíme m+1 v přesně R_B/k řádcích.

Pro testovanou neprázdnou A, která není podmnožinou B, už každý
řádek této skupiny má v A nějakou hodnotu≤m. Její minimum se
vložením vyšší hodnoty m+1 nezmění. Je-li A⊆B, před vložením
vítězí každý a∈A s pravděpodobností1/|A|. Po vložení jej zvolíme
přímo s četností1/k; pokud vložíme mimo A, zůstane uniformní
tie. Pro každé a∈A je tedy nová pravděpodobnost

```
1/k + (k−|A|)/(k |A|) = 1/|A|.
```

To dokazuje zachování minwise vlastnosti uvnitř každé skupiny,
bez předpokladů o závislosti různých řádků. Lze proto skupiny B
vyplňovat v libovolném pořadí; smíšený mezistav, kde některé
řádky mají m a jiné m+1 hodnot, zůstává minwise. Přesně to je
potřebné pro prostřední tabulky příkladu.

##(b): počty, dělitelnost, ukončení a minimalita

Minwise rodina vyžaduje celé N/k pro každé k=1,...,n, tedy
L=lcm(1,...,n) dělí N. Volíme N=L a d=N/n, celé kladné číslo.
Počáteční tabulka má hodnotu1 v pozici j právě v řádcích
(j−1)d+1,...,jd. Tím je každá pozice prvního minima stejně
častá. Pro A velikosti a vítězí daný prvek přímo s četností1/n;
v ostatních n−a skupinách je pomocná uniformní tie, takže
1/n+(n−a)/(na)=1/a. Počáteční rodina je minwise.

Indukční invariant na konci fáze m:
každý řádek má1,...,m právě jednou a každá množina B velikosti
k=n−m obsahuje právě R_m=N/binom(n,m) prázdných řádků.
Pro m=1 platí R_1=d. Jestliže z každé skupiny B vložíme m+1
rovnoměrně, daná nová prázdná množina C velikosti k−1 vznikne
z B=C∪{q} pro každé z m+1 možných q∉C, pokaždé R_m/k-krát.
Její počet tedy je

```
(m+1)R_m/k = N/binom(n,m+1).
```

Potřebná celočíselnost není předpoklad. Tištěný rozklad je

```
R_m/k = N/[k binom(n,m)]
      = N Σ_{j=0}^m (−1)^j binom(m,j)/(k+j).          (2)
```

Pravý součet je ∫_0^1 x^(k−1)(1−x)^m dx, tedy
m!(k−1)!/(k+m)!=1/[k binom(n,m)]. To je přesně případ
x=k, stupeň m v původní úloze sv1 1.2.6–48; původní zadání
p72/file87 i odpověď p488/file503 byly zobrazeny. Používáme
jen kladná celá k a nezáporná celá m, nikoli nedoložené obecné
rozšíření beta-funkce. Každé k+j leží mezi1 a n a dělí N,
takže každý člen pravé strany(2) je celé číslo. Levá strana je
kladná, a tedy je kladné celé číslo, jak algoritmus potřebuje.

V každé skupině B vybereme k dosud nevyplněných řádků a do
každého vložíme m+1 v jiné pozici B. Po R_m/k dávkách je
skupina hotova. Vyplněný řádek má již jen k−1 prázdných pozic,
takže se znovu nezapočítá mezi nevyplněné k-prázdné řádky.
Každá dávka snižuje počet nevyplněných řádků o k. Každá fáze
končí po N vloženích a n−1 fází po N(n−1) vloženích.
V konečném m=n má každý řádek všechny hodnoty1,...,n, je tedy
permutací; opakované(a) dokazuje minwise vlastnost. Dolní mez
N≥L a dosažení N=L dokazují minimalitu.

Odkaz na uniform probing, sv3 §6.4, byl přímo porovnán s p534/
file545: relevantní tvrzení je právě rovnoměrnost všech množin
obsazených pozic. Zde je však invariant plně dokázán vlastní
indukcí; nepřebíráme další tvrzení o hashování nebo nezávislosti
obsazenosti jednotlivých buněk.

## Cyklické posuny, včetně periodických prázdných množin

Následující argument doplňuje nevypsanou existenci v odpovědi.
Nechť G=C_n působí pravými rotacemi pozic. Zachováváme d
indexovaných orbit řádků, každou o délce n; orbitu j tvoří
řádky j,d+j,...,(n−1)d+j. Každý částečný řádek má jedinou1,
proto žádná nenulová rotace řádek nefixuje. Orbity řádků jsou
volné, i když různé indexované orbity mohou mít zatím stejné
hodnoty. Počáteční tabulka tuto vlastnost má.

Vyberme jednu orbitu prázdných množin a reprezentanta B,
|B|=k. Stabilizátor H={g∈G:gB=B} má h prvků. Na jednotlivých
pozicích působí volně, takže B je disjunktním sjednocením k/h
H-orbit, každé o h pozicích. Jedna indexovaná orbita řádků
s prázdnými množinami v G·B obsahuje právě h řádků s blank-setem
B. Je-li vložená pozice v reprezentativním řádku q∈B a ve všech
jeho rotacích se vložení otočí stejně, těchto h řádků dostane
m+1 právě jednou do každé pozice Hq.

Položme c=R_m/k, kladné celé číslo podle(2). Indexovaných orbit
řádků přispívajících k B je R_m/h=(k/h)c. Rozdělíme je mezi
k/h H-orbit pozic po c kusech. Každé přiřazené orbitě vybereme
jeden q v její H-orbitě a vložení rozrotujeme do všech n řádků.
V každé pozici B tak vznikne přesně c vložení. Stejně je tomu
v každé rotaci B; nevzniká dvojí přiřazení, protože zpracováváme
celou orbitu blank-setů najednou. Tím platí(a) a zároveň se
zachovají všechny indexované cyklické vztahy.

Tento argument pokrývá h>1, nikoli jen obecné aperiodické B.
Pro n=4,B={2,4} je H={0,2},h=2,k/h=1. Jedna řádková
orbita už dodá obě pozice; dvě volby orientace q=2 nebo4
jsou právě poslední dvě tištěné větve po opravě F174.

## Lze současně zajistit různé konečné permutace

Rodina nemusí skončit jako multiset. Zpřesníme předchozí výběr
bez změny počtů nebo cyklické symetrie. Pro danou orbitu B
seskupme indexované orbity řádků, které zatím obsahují stejné
částečné řádky. Nechť určitý typ má r kopií; v každé kopii
zvolíme týž reprezentativní řádek p s blank-setem B.

Všechny kopie jednotlivých typů ponecháme za sebou a přiřazujeme
jim k/h H-orbit pozic cyklicky, jedním průběžným čítačem přes
celý seznam. Protože celková délka je (k/h)c, každá H-orbita
pozic dostane přesně c kopií. V bloku r shodných typů připadne
na jednu H-orbitu nejvýše ceil(r/(k/h)) kopií. Uvnitř každého
takového bloku rozdělíme konkrétní q rovnoměrně cyklicky mezi
h pozic dané H-orbity. Každý konkrétní q dostane nejvýše

```
ceil(ceil(r/(k/h))/h) = ceil(r/k)
```

kopií. Dvě různé pozice q vytvářejí různé nové řádkové orbity:
rotace, která by je ztotožnila, by po vymazání m+1 fixovala p,
což kvůli jediné1 může být jen identita. Různé staré typy se
také nemohou slít, protože vymazáním m+1 bychom získali stejné
staré typy. Maximální násobnost proto v každé fázi k klesne
z r na nejvýše ceil(r/k).

Z počáteční násobnosti d=N/n dostaneme po všech fázích nejvýše
ceil(d/(n−1)!)=ceil(N/n!)=1, protože L dělí n!. Identita pro
vnořené stropy plyne z toho, že ceil(x/b) je nejmenší celé q
s bq≥x; platí pro kladná celočíselná b. Výsledné d seedy
nejsou cyklickými posuny jeden druhého a všech N řádků je různých.
To uzavírá i silnější setový význam slova rodina.

Konkrétní konečný postup lze implementovat tříděním podle
blank-setů a kanonických rotací, bez hledání nebo backtrackingu.
Pro explicitní tabulku je paměť O(nN) hodnot. Při přímém
porovnávání n-symbolových slov a zkoušení všech n rotací dává
výše popsaný způsob například O(n³N+n²N log N) symbolových
operací celkem. Netvrdíme efektivitu v samotném n ani
reprodukci publikovaného kompaktního vzorkovače.

## Každá položka příkladu n=4 a F174

Zde N=lcm(1,2,3,4)=12,d=3. Počátečních d řádků s1 v každé
pozici je přesně12. Při m=1 musí každá ze tří zbývajících
pozic dostat2 jednou. Až na přejmenování tří totožných počátečních
seedů to v cyklické konstrukci nutí seedy1200,1020,1002
(0 zde značí blank). Jejich rotace jsou přesně všech12 slov
tabulky na konci p387. Každý blank-pár se objevuje dvakrát.

Pár B={3,4} mají řádky1=1200 a6=2100. Jsou právě dvě
vyvážené volby: nové3 vložit do pozic(3,4), nebo(4,3).
Po propagaci rotací jsou správné řádkové orbity:

```
první volba:
 j1: 1230 0123 3012 2301
 j2: 1020 0102 2010 0201
 j3: 1032 2103 3210 0321

druhá volba:
 j1: 1203 3120 0312 2031
 j2: 1020 0102 2010 0201
 j3: 1302 2130 0213 3021.
```

Pořadí uvnitř orbity jsou indexy j,j+3,j+6,j+9. První
tištěná větev chybně použije v řádcích3,9,12 hodnoty druhé
větve1302,0213,3021, ale v řádku6 ponechá2103 z první.
Proto ani její multiset není uzavřený na rotace. Stejné tři
chybné hodnoty se opakují v obou navazujících tabulkách.
Druhá původní větev je naopak celá správná.

Rozpor není jen estetická ztráta symetrie. Vezměme A={2,3}.
V první větvi mají řádky3 a10 před vložením3 právě tyto
prázdné pozice. Tisk do obou vloží3 v pozici2, čímž původní
dva příspěvky1/2 k vítězství pozice2 nahradí dvěma příspěvky1.
V ostatních řádcích je v A už hodnota≤2, takže vložení3
vítěze nemění. Z původní pravděpodobnosti1/2 proto vznikne
1/2+1/12=7/12, zatímco pozice3 má5/12. Pozdější vložení3
do blank-páru{2,4} ani závěrečné4 tyto výsledky nemění.

Například první dokončení vytištěné dolní tabulky má přesně
tyto dvojice obrazů pozic2,3:

```
23 32 34 12 13 14 41 41 21 34 24 42.
```

Pozice2 vítězí ve slovech s indexy1,3,4,5,6,10,11: sedmkrát
z12, místo požadovaných šesti. Všechny výsledné řádky jsou
platné různé permutace; selhává minwise vlastnost.

Oprava ve třech tabulkách p388, vždy indexy3,9,12:

```
1302 → 1032, 0213 → 3210, 3021 → 0321.
```

Potom zbývající orbita j2 má pro B={2,4} dvě možnosti:
1320,0132,2013,3201 nebo1023,3102,2310,0231.
To jsou přesně tištěné nové položky obou dolních větví.
Závěrečné vložení4 je jednoznačné a všechny tři opravené
mezitabulky i obě dokončené rodiny jsou minwise a cyklické.

`verify_mpr112_tableaux.py` kontroluje všech šest původních
tabulek, tři lokální opravy a čtyři dokončení. Pro každou
z15 neprázdných podmnožin počítá přesně racionální pravděpodobnosti
včetně uniformních tie, ověřuje i celý multiset rotací a všechny
indexované orbitové vztahy. Uloženo všech13 tabulkových kontrol,
všechny řádky i každá podmnožina; jediné spuštění nice15 trvalo
0.015221287962049246s. Nešlo o enumeraci rodin ani nový census.
Každá zde opsaná položka byla porovnána s originálním PDF a PS.

F174: low, lokální vada devíti ilustračních položek na jediné
straně p388/file408. Platná konstrukce a tvrzení minimální
velikosti zůstávají po uvedené opravě plně doloženy. Chybné
tabulky nejsou vysvětleny přeznačením řádků: pravděpodobnost7/12
je na pořadí řádků nezávislá.

## Errata a bibliografický rozsah

E133 je známá oprava Fascicle5 z26.2.2020: v úvodní truncation
podmínce min_{a∈π} má být min_{a∈A}. Originální stránka3
all4f5 a TeX byly přímo přečteny. Svazek4B již má správné A.
Tato oprava nemá kartu ani chybovou lokaci. Oprava krokC6 na
Fascicle5 p44 je z jiné části publikovaného fasciklu; náhodná
shoda s p44 pre-fasciklu obsahujícího zdejší odpověď neznamená
opravu tabulek. Také errata cvičení112 o Torto na p443 svazku4B
a algoritmů SAT na p44 Fascicle6 se netýkají MPR112.

Primární IEICE metadata potvrzují oba citované články, rok2000,
E83-A, rozsahy646–655 a747–755. První článek má autory Takei
a Itoh, druhý Takei, Itoh a Shinozaki; společnou knižní citaci
čteme jako odkaz na tyto dvě související práce. Plné historické
články nejsou rychle dostupné z vydavatelského webu bez nákupu;
jejich přesnou konstrukci a kompaktní vzorkovač výslovně
vynecháváme. Všechna matematika požadovaná úlohou je dokázána
výše nezávisle; nejde o skrytou závislost na bibliografické výjimce.

Výsledek: celá112 doložena včetně obecného cyklického kroku,
různosti permutací, každého mezistavu a všech tabulek. F174
vyžaduje uvedenou opravu; E133 zůstává pouze známou opravou.
File407 lze uzavřít včetně jeho části112, file408 zůstává
partial kvůli113–115 a file43 kvůli113–115.
