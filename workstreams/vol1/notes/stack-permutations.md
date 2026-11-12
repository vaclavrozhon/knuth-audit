# §2.2.1: permutace získatelné zásobníkem

Kontrola 1. listopadu 2026. Položky V1-X0004, V1-X0009 až V1-X0011.
Výsledek: cvičení 3–5 jsou správná; příslušné důkazy a vzorce byly
nezávisle ověřeny. Tři níže popsané vady odpovědí jsou zveřejněná errata.

## Zdroj a význam tvrzení

Zadání je na tištěných stranách 242–243, zejména
[s. 243 / strana souboru 258](../images/vol1-file258-p243.png).
Odpovědi byly vizuálně zkontrolovány na
[536](../images/vol1-file551-p536.png),
[537](../images/vol1-file552-p537.png) a
[538](../images/vol1-file553-p538.png).

Vstup přichází v pořadí 1,...,n. Zásobník dovoluje vkládat i odebírat
pouze na vrcholu. S značí vložení příštího vstupu, X odebrání vrcholu
do výstupu. Přípustné slovo má n znaků S a n znaků X a nikdy se
nepokouší odebírat z prázdného zásobníku. Permutace p_1,...,p_n je
výsledné pořadí výstupu. Vzor 312 znamená trojici pozic i<j<k,
v nichž `p_j < p_k < p_i`.

## Cvičení 3: přípustnost a jednoznačnost

Ve všech počátečních úsecích slova musí být počet X nejvýše počet S.
To je nutná i postačující podmínka: rozdíl je aktuální výška zásobníku.
Při n znacích S nelze vyčerpat vstup před nepovoleným dalším vkládáním.

Pokud dvě různá přípustná slova mají tentýž začátek a potom se liší jako
S a X, zásobník je v tomto bodě neprázdný. Druhé slovo vypíše starý
vrchol v. První vloží nový prvek u a musí vypsat u dříve než v.
Výstupní permutace se proto liší. Každá přípustná historie dává jiný výstup.

## Cvičení 4: počet a obecné koeficienty

Označme `binom(a,b)` počet b-prvkových podmnožin a-prvkové množiny;
pro celé b mimo 0,...,a jej položíme roven nule. Ze všech
`binom(2n,n)` slov s n znaky každého druhu odečteme nepřípustná.
Záměnou S a X v úseku končícím prvním dosažením výšky -1 získáme
bijekci na slova s n+1 znaky S a n-1 znaky X. Inverze zamění úsek
do prvního dosažení výšky +1. Počet přípustných slov je tedy

```text
C_n = binom(2n,n) - binom(2n,n-1) = binom(2n,n)/(n+1).
```

Těmto číslům se říká Catalanova čísla. Pro n=0 je jedno prázdné slovo.

Obecně nechť g(L,h) je počet přípustných počátečních úseků délky L,
které končí ve výšce h>=0. Tentýž odraz dává pro shodnou paritu L,h

```text
g(L,h) = binom(L,(L-h)/2) - binom(L,(L-h)/2-1).          (1)
```

Pro různou paritu je počet nulový. Záporné dolní indexy v (1) taktéž
dávají nulu. Vzorce pro sudou a lichou délku na konci s. 537 jsou
přesně dvěma zápisy (1).

### V1-X0009: posunutý exponent ve vytvářející funkci

Vytvářející funkce ukládá počty jako koeficienty mocninné řady:
`G(x,z) = sum_{L,h>=0} g(L,h) x^h z^L`.
Kniha zavádí řadu f(w) s konstantním členem 1, pro niž
`r_2(z)=z f(z^2)`. Koeficient `A_k(r,-2)` je v tomto použití
koeficient w^k v mocnině `f(w)^r` (odkaz §1.2.6-25).

Z již odvozeného `G = r_2/(z(1-r_2 x))` nutně plyne

```text
G(x,z) = sum_{h>=0} x^h z^h f(z^2)^(h+1).
```

Koeficient x^h z^(2k+h) je tedy A_k(h+1,-2), nikoli A_k(h,-2), jak
má první dotisk. Už pro h=0,k=1 by nesprávný zápis dával 0
(koeficient w v f(w)^0), zatímco g(2,0)=1 díky slovu SX.
Přesnou opravu obsahuje `all1-prepre`, s. 40, datum 1. ledna 2006
([obraz](../images/errata-all1-prepre-file040.png)).

### V1-X0010: okrajová podmínka rekurence

Při výšce h=0 nemůže poslední krok přijít z výšky -1. Rekurence musí
pro nezáporné indexy znít

```text
g(L+1,h) = [h>0] g(L,h-1) + g(L,h+1),
```

kde `[h>0]` znamená 1, když h>0, jinak 0; při h=0 se první člen
vynechává. Alternativou je explicitně definovat g(L,-1)=0.
To je přesně úprava z 2. května 2024 v `all1` a `err1`, s. 537.
Bez této konvence je původní zápis na hranici nedourčený; netvrdíme,
že dává nesprávné číslo při přirozeném doplnění nulové hodnoty.

## Cvičení 5: obě implikace

Je-li ve výstupu vzor 312, před vypsáním p_i už vstoupily menší
p_j a p_k. Obě zůstávají v zásobníku, protože se mají objevit později.
Ale p_j < p_k znamená, že p_k leží nad p_j. Nelze tedy nejprve vypsat
p_j a teprve potom p_k. Vzor 312 je překážkou.

Naopak pro požadovaný výstup postupujeme hladově: pokud požadovaný
prvek ještě nevstoupil, vkládáme právě tolik prvků, abychom jej dosáhli,
a pak jej odebereme. Pokud již vstoupil, pokusíme se jej odebrat ihned.
Selhání může nastat jen tehdy, když je požadovaný p_j zakryt větším
prvkem p_k, který má vyjít později. Ten byl vložen při přípravě nějakého
dřívějšího výstupu p_i; musí platit p_i>p_k, protože jinak by p_k
byl právě tehdy odebrán. Máme i<j<k a p_j<p_k<p_i, tedy vzor 312.
Jeho nepřítomnost proto zaručuje úspěch konstrukce.

### V1-X0011: známá úprava slovního důkazu

`all1` a `err1`, položka s. 538 z 7. července 2023, nahrazují část
slovního argumentu prvního směru. Proto zde staré znění nepovažujeme
za nový nález; výše uvedený samostatný důkaz se obejde bez této formulace.
Doklad pro tuto i předchozí položku je
[strana 14 errat](../images/errata-all1-file014.png).

## Nezávislá výpočetní kontrola a omezení

[Program](../check_first_blocks.py) generuje přímo všechny přípustné
historie a ověřuje, že nikdy nedostane dvakrát stejný výstup.
Nezávisle prochází všechny permutace a hledá zakázané trojice indexů.
Pro každé 0<=n<=8 se obě množiny přesně rovnají a mají velikosti

```text
1, 1, 2, 5, 14, 42, 132, 429, 1430.
```

Zahrnuto bylo 46 234 permutací včetně prázdné. Zvlášť bylo porovnáno
902 koeficientů g(L,h) pro L<=40: přímé legální přechody výšky versus
vzorec (1). Vše prošlo; [výstup](../results/first-blocks.json).

Errata byla prohledána napříč `all1-prepre`, `all1-pre`, `all1`, `err1`
a `err1.textxt`, podle s. 242–243, 536–538 a příslušných formulí.
Bibliografické změny a oprava „konvexního“ polygonu v motivaci odpovědi 4
jsou mimo matematický rozsah této kontroly. Neověřujeme cvičení o deque,
celou kapitolu o lineárních strukturách ani všechny odbočky odpovědi 4.

## Doplnění 1. listopadu 2026: obecný ballot vzorec a motivace

V1-X0021 rozšiřuje matematickou kontrolu odpovědi 4. Nechť l,m jsou
nezáporná celá čísla a h>=1 je celé. Počítáme slova s l znaky A a m
znaky B, jejichž některý prefix dosáhne výšky h; výška je počet A
minus počet B. Sken s. 536 dává

```text
f(l,m,h) = binom(l+m, min(m,l-h)).
```

Je-li l>=m+h, musí každý celý průchod do konečné výšky l-m dosáhnout h;
počet je tedy binom(l+m,m). Je-li l<m+h, zaměníme A a B v prefixu
do prvního dosažení h. Dostaneme slovo s l-h znaky A a m+h znaky B.
Každé takové slovo končí pod výškou -h, a tedy má jednoznačný první
prefix dosahující -h; jeho záměnou získáme inverzi. Počet je
binom(l+m,l-h), včetně nuly při l<h. Oba případy dávají knižní vzorec.
Pro l>=h plyne i uvedená symetrie f(l,m,h)=f(m+h,l-h,h).

Formální odvození dvojité vytvářející funkce na s. 537 lze také uzavřít
bez heuristiky. Definice g(L,h) a G(x,z) jsou výše. Opravená rekurence
dává [z(x^2+1)-x]G=zG(0,z)-x. Malý kořen r(z) této kvadratické
rovnice má nulový konstantní člen, takže dosazení x=r(z) do formální
řady je legální. Vynutí G(0,z)=r(z)/z a následně
G=r(z)/(z(1-r(z)x)). Počáteční podmínka a rekurence určují všechny
koeficienty jednoznačně. Záměna A_m(n,-2) za A_m(n+1,-2) byla
zdokumentována výše; dodatek k rozsahu součtu m,n>=0 je v `all1`
z 7. července 2023 a odpovídá zde použitým indexům.

Motivační ekvivalence se stromy, závorkováním a triangulacemi mají stejnou
rekurenci c_0=1, c_n=sum_(i=0)^(n-1)c_i c_(n-1-i):
kořen úplného uspořádaného binárního stromu rozděluje n vnitřních uzlů
na levý a pravý podstrom; poslední operace rozděluje plné závorkování
n+1 operandů; trojúhelník při zvolené straně konvexního (n+2)-úhelníku
rozděluje zbytek na dvě menší konvexní oblasti. Tato rekurence má
jednoznačné řešení Catalanovými čísly odvozenými výše.

**V1-X0020: známé doplnění konvexity.** `all1`, `err1` a `err1.textxt`
na s. 536, datum 7. července 2023, doplňují slovo „convex“. Je skutečně
potřebné: jednoduchý čtyřúhelník s vrcholy (0,0),(2,0),(1/2,1/2),(0,2)
v tomto pořadí má jen jednu vnitřní úhlopříčku, a tedy jedinou
triangulaci; konvexní čtyřúhelník má dvě. To je doklad známého omezení,
nikoli nový nález.

Bibliografickou opravu připisující odrazový argument J. Aeblymu a
D. Mirimanoffovi namísto D. Andrého obsahuje `all1-prepre`, s. 39,
z 1. ledna 2009. Matematický argument na autorství nezávisí. Samotný
historický článek z roku 1923 a všechny dějinné údaje o de Moivrovi
v této dávce ještě porovnány nebyly; cvičení 4 proto zůstává v úplné
mapě `partial`, přestože jeho zde vypsané matematické formule jsou
prověřené. Nové bloky o deque jsou nyní v `deques.md` a `deque-basis.md`.
