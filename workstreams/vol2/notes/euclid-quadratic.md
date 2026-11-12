# §4.5.3-11/12: ekvivalentní a periodické rozvoje

Původní zadání 374–375 a odpovědi 647–649 byly přečteny v sazbě.
Značení C, K a maticová identita navazují na `euclid-basic.md`.
Historické atribuce Serret/Euler/Lagrange a indické/japonské
prameny patří do navazujícího kontextového bloku; zde jsou
nezávislé obecné důkazy matematických tvrzení.

## 11: shodné ocasy a celočíselné transformace

Pro iracionální X pišme X=A_0+C(A_1,A_2,...), kde A_0 je celá
část a ostatní podíly jsou kladné celé. Ocas X_j je zbytek po
oddělení j-tého podílu; X_0=X-A_0 a X_j=1/X_(j-1)-A_j.
Jsou-li p_j/q_j konvergenty, matice z úlohy 2 dává

```text
X=(p_m+p_(m-1)X_m)/(q_m+q_(m-1)X_m).                  (1)
```

Při X_m=Y_n eliminujeme společný ocas z obou rovnic (1).
Výsledkem je X=(qY+r)/(sY+t) s celými q,r,s,t a
qt-rs=(-1)^(m-n). To dokazuje nutnost včetně znaménka.

Pro obrácený směr provedeme indukci podle |s|. Všechny čtyři
koeficienty můžeme změnit na opačné, takže s>=0. Při s=0 je
X=Y+c nebo X=-Y+c s celým c. Přičtení celého čísla nezmění
ocas. Negaci ošetří identita 9(d): pro 0<Z<1 je
1-Z=C(1,A_1-1,A_2,...), s odstraněním nuly, pokud A_1=1.
Proto i negace zachová eventualní shodu podílů.

Pro s>0 napišme q=as+s', 0<=s'<s. Pak

```text
X=a+1/Z,  Z=(sY+t)/(s'Y+r-at),
s(r-at)-ts'=sr-tq=-(qt-rs).
```

Indukce dává eventualní shodu Z a Y; úloha 10 ji zachová při
převrácení Z a celá část a ji nezmění. Všechny jmenovatele
jsou nenulové, protože Y je iracionální a determinant je ±1.
Tím je obrácený směr dokázán. Parita posunu při negaci nebo
převrácení je lichá, při přičtení celé části sudá; sledováním
generátorů dostaneme také odpovídající znaménko determinantu.
Jde o existenci vhodných indexů m,n, nikoli o tvrzení, že
libovolně předem zvolená dvojice indexů musí mít stejné ocasy.

## 12(a): přesná celočíselná rekurze

Kvadratická iracionalita má tvar X=(sqrt(D)-U)/V, kde D>0
je celé nesčtvercové číslo a U,V jsou celé, V!=0. Pokud V
nedělí D-U², náhrada

```text
(D,U,V) <- (D V², U|V|, V|V|)
```

hodnotu X nezmění a zajistí požadovanou dělitelnost.
Položme V_0=V, A_0=floor(X), U_0=U+A_0 V. Pak
X_0=(sqrt(D)-U_0)/V_0 je v (0,1). Induktivně definujme

```text
V_(n+1)=(D-U_n²)/V_n,
A_(n+1)=floor((sqrt(D)+U_n)/V_(n+1)),
U_(n+1)=A_(n+1)V_(n+1)-U_n.                            (2)
```

Racionalizace dává 1/X_n=(sqrt(D)+U_n)/V_(n+1), takže
X_(n+1)=(sqrt(D)-U_(n+1))/V_(n+1) je přesně další ocas.
Z U_(n+1)=-U_n modulo V_(n+1) plyne zachování dělitelnosti.
Žádné V_n nemůže být nulové, protože D není čtverec.

S=isqrt(D) označuje největší celé číslo nejvýše sqrt(D).
Pro libovolné celé W a nenulové celé B platí

```text
floor((sqrt(D)+W)/B) =
    floor((S+W)/B),     B>0,
    floor((S+1+W)/B),   B<0.                           (3)
```

Rozdíl sqrt(D)-S je ostře mezi 0 a 1; dělení celým B proto
nemůže překročit jinou celočíselnou hranici než tu zachycenou
v (3). Záporné B vysvětluje přidanou 1. Také doplňující vzorec

```text
V_(n+1)=A_n(U_(n-1)-U_n)+V_(n-1), n>=1,
```

je správný: odečteme dvě po sobě jdoucí rovnosti D-U_j²=V_j V_(j+1)
a použijeme U_(n-1)+U_n=A_n V_n. Výpočet dalších V tedy nepotřebuje
dělení, jak tvrdí odpověď.

## 12(b): konečný stavový prostor a přesný začátek periody

Sdružené číslo Y=(-sqrt(D)-U)/V vznikne změnou znaménka odmocniny.
Stejnou změnou v (1) dostáváme

```text
Y_n=(-sqrt(D)-U_n)/V_n
   =-(q_n/q_(n-1))*(Y-p_n/q_n)/(Y-p_(n-1)/q_(n-1)).     (4)
```

Konvergenty p_n/q_n se blíží X, které je od Y různé. Oba poslední
rozdíly tedy mají pro dost velké n stejné znaménko; q_n jsou kladné.
Odtud Y_n<0. Protože X_n>0 a X_n-Y_n=2sqrt(D)/V_n, vyjde V_n>0.
Dále U_n<sqrt(D), a pro následující dostatečně velké indexy

```text
V_n <= A_n V_n = U_n+U_(n-1) < 2sqrt(D).
```

Z X_n<1 plyne U_n>sqrt(D)-V_n. Je-li V_n<=sqrt(D), dostáváme
U_n>0 přímo. Jinak U_n=A_n V_n-U_(n-1)>sqrt(D)-U_(n-1)>0.
Všechna pozdější celočíselná U_n,V_n tedy leží v konečné množině.
Rekurze (2) je deterministická, takže se některý stav opakuje
a od něj jsou stavy i podíly periodické.

Odpověď navíc správně určuje stavy na cyklu. Uvažujeme stále
přípustné stavy procesu, tedy také 0<(sqrt(D)-U)/V<1 a
dělitelnost z (2). Za těchto podmínek definujme redukovaný stav
nerovnostmi

```text
0<U<sqrt(D), 0<V<sqrt(D)+U.                            (5)
```

Přímé dosazení do (2) ukazuje, že redukovaný stav přejde na
redukovaný stav (U',V'). Podrobně, V'>0 a V'<sqrt(D)+U;
tedy A>=1 a U'<sqrt(D). Pokud V'>sqrt(D), máme U'>V'-U>0;
pokud V'<sqrt(D), plyne U'>sqrt(D)-V'>0 z nového ocasu <1.
Nakonec sqrt(D)+U'=A V'+sqrt(D)-U>V'.

Předchůdce redukovaného stavu je jednoznačný, protože

```text
(sqrt(D)+U')/V'=A+V/(sqrt(D)+U),
0<V/(sqrt(D)+U)<1.
```

Z nového stavu tedy určíme A podlahou, pak U=A V'-U' a
V=(D-U²)/V'. Zobrazení konečné množiny redukovaných přípustných
stavů do sebe je prosté, a tedy je permutací; každý takový stav
je na cyklu. Obráceně každý cyklus má již dokázané meze a
sqrt(D)+U_n=A_n V_n+sqrt(D)-U_(n-1)>V_n. Proto je (5)
opravdu přesným kritériem cyklického stavu.

## 12(c): normová a smíšená identita

Norma zde znamená součin čísla s jeho sdruženým číslem.
Pro konvergenty p_n/q_n definujme

```text
N_n=V p_n²+2U p_n q_n+((U²-D)/V)q_n²
   =V(q_n X-p_n)(q_n Y-p_n).
```

Rovnice (4) a její nesdružená verze dávají
N_n/N_(n-1)=X_n Y_n=-V_(n+1)/V_n.
Počátek N_0=-V_1 tedy dokazuje N_n=(-1)^(n+1)V_(n+1),
což je přesně zadání. Pro smíšený výraz z odpovědi označme

```text
M_n=V p_n p_(n-1)+U(p_n q_(n-1)+p_(n-1)q_n)
       +((U²-D)/V)q_n q_(n-1).
```

Máme M_0=U_0, kde p_(-1)=1,q_(-1)=0, a rekurze konvergentů
dává M_n=A_n N_(n-1)+M_(n-1)=(-1)^n U_n. Tím jsou ověřeny
obě tištěné identity se všemi znaménky.

## 12(d): obrácení tvrzení o periodicitě

Předchozí konečnost dokazuje jednu implikaci. Je-li naopak
nekonečný pravidelný rozvoj periodický od určitého místa, jeho
periodický ocas t je pevným bodem složení map z->1/(a+z)
s kladnými celými a. Matice tohoto složení má tvar [[A,B],[C,D]]
s B,C>0. Rovnice t=(At+B)/(Ct+D) je proto skutečná kvadratická
rovnice Ct²+(D-A)t-B=0. Ocas je podle úlohy 6 iracionální;
nemůže tedy jít o racionální kořen. Po připojení konečného
prefixu je X celočíselnou Möbiovou transformací t a zůstává
kvadratickou iracionalitou. Tím je ekvivalence úplná.

## Přesné nezávislé kontroly

`verify_euclid_quadratic.py` má dvě odlišné realizace: tištěnou
celočíselnou rekurzi a přímou aritmetiku a+b sqrt(D) s racionálními
koeficienty. Podlahy druhé realizace ověřují racionální intervaly
odmocniny získané celočíselným odmocňováním, nikoli vzorec (3).
Kontrola zahrnuje záporné jmenovatele, počáteční škálování,
oba normové vzorce, obrácení cyklu a bezdělicí výpočet V.
Samostatně generované unimodulární transformace porovnávají
přesné ocasy včetně parity. Rozvoj sqrt(8/29) z textu 358
souhlasí s přesnou periodou. Počty a dokončené checkpointy
jsou v `results/euclid-quadratic.json`.

V tomto matematickém bloku nebyl nalezen další nový problém knihy.
