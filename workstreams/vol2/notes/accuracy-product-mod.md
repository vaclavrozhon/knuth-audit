# §4.2.2-21/23: přesný součin a odečtení zlomkové části

Původní zadání244 a odpověď616 byly přečteny vizuálně. Zapracována
oprava1999 v21: e_u=e_v=p. Čtyři vrstvy errat zkontrolovány.
R je zaokrouhlení na nejbližší plovoucí číslo; při binární soustavě
se používají doporučené sudé poloviny. Všechny mezivýsledky musí
ležet v dostupném exponentovém rozsahu. To může být silnější nárok
než pouhá reprezentovatelnost konečného součinu.

## 1. Rozdělení operandu, úloha21

Pro p1 jsou součiny binárních mocnin přesné a stačí w=uv,w'=0.
Dále p>=2, N=2^p, s=ceil(p/2), t=floor(p/2), H=2^(s−1).
Znaménky a násobením mocninami2 redukujeme na celé vstupy
N/2<=u,v<N. Konstanta c=2^s+1 je reprezentovatelná.
Veltkampův rozklad počítá

```text
u'=R(uc),    u1=R(R(u−u')+u'),    u2=R(u−u1),
```

a stejně v1,v2. Dokážeme u=u1+u2, u1 násobek2^s,
N/2<=u1<=N a |u2|<=H.

Pišme u'=2^s u+u−e. Součinuc má krok zaokrouhlení2^s,
nebo při horním přenosu2^(s+1). Proto |e|<=2^s a u' je
násobek2^s. Je-li u=N/2, je součin přesný. Jinak
u−u'=−2^s u+e leží mezi −2^s N a −2^s N/2,
včetně krajů, kde je zaokrouhlení totéž jako na síť s krokem2^s.
Tedy R(u−u')=−2^s u+T(e), kde T zaokrouhluje na tuto síť s odpovídající volbou poloviny.
Proto následující přesný součet je u+T(e)−e, násobek2^s,
a liší se od u nejvýšeH. Jde o nejbližší násobek2^s k u,
takže leží v[N/2,N] a je reprezentovatelný; finálníR jej nezmění.
Rozdíl u2=e−T(e) je celé s |u2|<=H a rovněž reprezentovatelný.

## 2. Proč jsou všechny korekční operace přesné

Všechny čtyři součiny u1v1,u1v2,u2v1,u2v2 jsou reprezentovatelné:
první po vytknutí2^(2s) má velikost nejvýše2^(2t)<=2^p,
krajní rovnost je mocnina2. Smíšené součiny po vytknutí2^s
mají velikost nejvýše2^t H=2^(p−1). Poslední má velikost
nejvýše H²=2^(2s−2)<=N/2.

Položme w=R(uv), r=uv−w; w je násobkemN/2 a |r|<=N/2.
První rozdíl u1v1−w je násobkemN/2. Jeho velikost nepřesáhne

```text
|r|+|u2v1+u1v2+u2v2| <= N/2+2HN+H² <= N(2^s+1).
```

Pro p>=4 má po vyděleníN/2 velikost nejvýše2^(s+1)+2<N,
a je tedy reprezentovatelný. Zbývající p2,p3 jsou konečných20 dvojic
u,v: všechny jsou přesně vypsány a ověřeny v reprodukčním JSON.
To zde nahrazuje hrubý odhad, který na těchto dvou malých přesnostech
sám o sobě nestačí; netvrdí se jeho platnost tam.

Po přičtení u1v2 dostaneme u1v−w=r−u2v. Tato hodnota je násobkem
2^s a její velikost je nejvýšeN/2+HN; po vydělení2^s dostaneme
nejvýše2^(p−s−1)+N/2<N. Další přičtení u2v1 dává
r−u2v2, celé s velikostí nejvýšeN/2+H²<=N. I krajníN je
reprezentovatelná mocnina2. Poslední přičtení u2v2 dává přesněr.

Tím všechny korekční kroky v tištěném pořadí proběhnou bez chyby:

```text
w' = R(R(R(R(u1v1−w)+u1v2)+u2v1)+u2v2) = uv−w,
w+w'=uv.
```

Násobení uv samotné zůstává zaokrouhlené; jeho chyba se právě
ukládá do w'. Původní odpověď je po opravě exponentového indexu správná.

## 3. Úloha23: kdy vrátí odečtení zlomku dolní celou část

Symbol u(mod)1 znamená R(u−floor(u)), nikoli IEEE zbytek po dělení.
Pro u>=0 nebo u<=−1 je přesná zlomková část reprezentovatelná:
pro |u|>=1 má nejvýše p−1 zlomkových míst a u s ještě větším
exponentem je celé; pro0<=u<1 jde přímo o u. Také floor(u)
je reprezentovatelné. Celý výpočet je proto přesný.

Zbývá −1<u<0. Položme h=b^(−p) a
r=R(1+u)−(1+u). Je |r|<=h/2 a vypočtený výsledek je
−R(1+r). Horní soused1 má odstupbh, dolní soused odstuph.
Proto může být R(1+r) různé od1 pouze v jediné situaci:
r=−h/2 a při zaokrouhlení1−h/2 se vybere dolní1−h.

Pro sudé b a sudé poloviny se na této hranici vždy zvolí1,
protože její significand před přenosem je sudé b^p. Pro liché b
nemůže nastat už první přesná polovina: vstup1+u má jmenovatel
mocninu lichého b, ale potřebný bod má ještě faktor2 ve jmenovateli.
Tím je dokázáno, že se sudými polovinami identita vždy platí.

Knižní pravidlo volí liché poloviny právě při b dělitelném4.
Pak se na vnější hranici zvolí1−h. Aby vnitřní zaokrouhlení
R(1+u) mělo chybu−h/2, musí (1+u)/h být k+1/2 pro liché k.
Jelikož1/h=b^p je sudé, je to ekvivalentní podmínce

```text
u mod(2h) = 3h/2.
```

Takový reprezentovatelný u nutně splňuje |u|<1/b: jinak by u/h
bylo celé. Proto1+u>1−1/b>=1/b a vnitřní zaokrouhlení opravdu
používá krokh, nikoli jemnější binadu. Podmínka je tedy nutná
i postačující, přesně jako v tištěné odpovědi.

Tištěný příklad b8,p3,u=−(.0124)_8=−21/1024 má tři významné
cifry, přestože za čárkou jsou čtyři znaky. Dostaneme
R(1+u)=501/512 a výsledkem je−511/512 místo−1. Není to nový
nález; kniha tento příklad správně uvádí.

## 4. Kontroly

`verify_accuracy_product_mod.py` kontroluje každou jednotlivou
operaci rozkladu a každé korekční přičtení, vedle finální identity.
Pro malé přesnosti se projdou všechny dvojice; při větších se rozsah
výslovně označí za vzorek. Úloha23 se porovnává s celou ekvivalencí,
včetně varianty sudých polovin v každém základu. Dokončeno7 532 dvojic součinu a47 400 případů modulo. Všech35 bloků
prošlo s exit0. Pro p2..7 jsou dvojice součinu vyčerpávající; p8,9
jsou výslovně vzorkované. Důkazy mají obecný rozsah uvedený výše.
