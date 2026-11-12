# §1.2.6-51: Hurwitz a stromové křížové odkazy

Kořenová revize 2. listopadu 2026, V1-X0719. Celá úloha 51 je
nově checked. Původní článek i přesné převody obou stromových odkazů
doplňují přijatou matematiku X0072. Hautusova atribuce v úloze 52
zůstává samostatnou mezerou. Nový nález nevznikl; testy se neopakovaly.

Před změnou evidence root ověřil všech 14 souborů, 650762 bajtů,
a 13 vstupů zmrazeného balíku
`parallel/binomial-next-origins/hurwitz/`. Hash MANIFEST.json je
`702a135c0f0e4a9d4e03a625be565d3c25a52a58e990da148eb13b5bdaaa5e35`.
Ověřeny navíc čtyři textové erratové vstupy podle jejich hashů.
Root přečetl obě poznámky a HANDOFF, obrazově celý původní článek
199–203 a knižní 72, 488, 398–399 a 592 v rozsahu uvedených úloh.
Podrobný audit se vztahuje na Hurwitzovy (I)–(III); další (IV)–(VI)
jsou přečtený kontext, nikoli nově úplně prověřené obecné věty.
Podpis listopad 1901 a tiskové paty červen/červenec 1902 jsou odlišeny.

Nechť N je množina n indexů vah z_i. Pro A podmnožinu N položme
Z_A=sum_(i in A)z_i a B=N minus A. Hurwitzova funkce je

```text
F_(r,s)(u,v)=sum_(A subset N)(u+Z_A)^(r+|A|)(v+Z_B)^(s+|B|).
```

Jeho formule (II) dává F_(-1,0)=(u+v+Z_N)^n/u. Root ověřil
indukci na 201–202: derivace podle v i podle každé váhy má podle
indukčního předpokladu hodnotu n*(u+v+Z_N)^(n−1)/u. Rozdíl tedy
závisí jen na u a dosazení v=z_i=0 ho anuluje. Hurwitz sám poté
nahradí v proměnnou v−Z_N. Násobení u dává přesně knižní
nesymetrickou identitu. Prázdný člen u*u^(-1) je nejprve zkrácen
na 1; výsledná polynomiální identita zahrnuje u=0 i n=0.

Z Hurwitzovy rovnice (3) plyne (III):
F_(-1,-1)=(1/u+1/v)*(u+v+Z_N)^(n−1). Po násobení u*v jde o
symetrickou formuli úlohy 2.3.4.4-30. Aby byl doložen i opačný
knižní odkaz ze symetrické na nesymetrickou formu, definujme
P_empty(x)=1, P_A(x)=x*(x+Z_A)^(|A|−1) pro neprázdnou A a

```text
S_N(x,y)=sum_A P_A(x)P_B(y),
Q_N(x,y)=sum_A P_A(x)*(y+Z_B)^|B|.
```

Rozštěpení činitele y+Z_B dává konečnou rekurenci

```text
Q_N(x,y)=S_N(x,y)+sum_(i in N)z_i*Q_(N minus {i})(x,y+z_i).
```

Proto ze stromové formule S_N=(x+y)*(x+y+Z_N)^(n−1) indukcí
plyne Q_N=(x+y+Z_N)^n. Záměna y za y−Z_N dává přesně vzorec
na 488. Prázdná N má S_N=Q_N=1 po odstranění zdánlivé singularity.
Pro všechny stejné váhy totéž převádí symetrickou Abelovu konvoluci
z úlohy 2.3.4.4-29. Její E_k(r,t)=r*(r+k*t)^(k−1)/k! a E_0=1
po násobení konvoluce n! skutečně dávají knižní koeficienty.
Další odkaz na II 4.7-22 a Torelliho úlohu 34 již uzavřelo X0710.

Převody jsou konečné algebraické identity; prázdné skupiny, znaménko
společné váhy −z v Abelově původní podobě a polynomiální pokračování
jsou výslovně ošetřeny. Čtyři vrstvy errat nemění Hurwitzovu citaci;
známé opravy indexů na 399/592 a sousedního Hautusova odstavce
zůstávají oddělené. Přesná zdrojová URL je v agentově protokolu.

Převzat je rovněž celý vnější balík binomial-next-origins: 28 souborů,
1202171 bajtů, všechny délky, hashe a vstupy souhlasí. Vnější manifest
má SHA-256
`515d655e47ab022ea4540c99d0f12db88c4626302336a1d21a0b22947adbf759`.
Root přečetl i obě poznámky o zbývajících mezerách. Nové knihovní
stopy nepřinesly Dicksonovy 383–384; jeho citace je erratovým dodatkem
k původní 484. Hautusův konkrétní původ zůstává nedoložený: kniha
neuvádí publikaci ani dopis a nebudeme je domýšlet. Tato dvě zjištění
zužují dostupnostní nejistotu, ale neuzavírají úlohy 10 a 52.
