# §1.3.3-33: doplněná konstrukce testu i<j

Na s.527 kniha navíc uvádí existenci prokládaného součinu délky
n=6^(l+1)−4^(l+1) pro0<=i,j<m=2^(2^l), který je c=(12345) právě
pro i<j, jinak identita e. Následující vlastní konstrukce dává i kratší
posloupnost; doplněním identit dostaneme přesně uvedenou délku.
Nejde o tvrzení nového výsledku ani optimální délky.

Prokládaný program tvoří posloupnosti A_i a B_j a vyhodnocuje se jako
A_i1 B_j1 ... A_in B_jn, součiny zleva doprava. Konjugace g^s=s^(-1)gs
se aplikuje zvlášť na každý faktor. Všechny faktory níže jsou involuce,
tj. jejich druhá mocnina je identita.

Položme p=(14)(23),q=(15)(24); přímo p q=c. Vyberme r, které přejmenuje
cyklus c²=(13524) na c: r má obrazy(1,4,2,5,3) na jménech1..5.
Pro dvě možné jednociferné hodnoty definujme

```
A_0=(p^r,p^r), A_1=(e,e),
B_0=(e,e),     B_1=(q^r,q^r).
```

Jediný netriviální případ je0<1: jeho součin je (p q)² konjugované r,
tedy c. Ostatní tři případy jsou e. Základ má délku2.

Vezměme s=(23)(45),t=(345) jako v knižní ortogonální konstrukci a
v=(25)(34), které obrací c na c^(-1). Jsou-li dva programy P,Q vždy
c nebo e, jejich konjunkci realizuje součin čtyř bloků

```
P^s Q^t P^(vs) Q^(vt).
```

Pokud jeden vstupní výsledek je e, zbývající bloky se zruší. Pokud
oba jsou c, výsledek je komutátor c^s c^t (c^s)^(-1)(c^t)^(-1)=c.
Všechny konstanty i poslední rovnost byly přímo ověřeny v S_5.

Pišme nový index I=im+i' a J=jm+j'. Pak

```
I<J  <=>  (i<j) OR ((i=j) AND (i'<j')).
```

Pravé dvě možnosti jsou disjunktní, takže můžeme jejich programy prostě
zřetězit: nikdy nevznikne c². K rovnosti i=j máme ortogonální konstrukci
délky E_l=2*4^l. Má-li test menší délku T_l, dostaneme tedy
`T_(l+1)=T_l+2E_l+2T_l=3T_l+2E_l`. S T_0=2 vyjde

```
T_l=4^(l+1)−2*3^l <= 6^(l+1)−4^(l+1).
```

Pro l=0 je rovnost; pro l>=1 například (6/4)^(l+1)>=9/4>2,
takže nerovnost plyne už z6^(l+1)>2*4^(l+1). Přidáme-li rozdíl
počtu dvojic(e,e), je výsledný součin stejný a má přesně knižní délku.
To je úplná induktivní konstrukce příkladu s nerovností.

`check_permutation_comparison.py` prošel398 kontrolami. Pro hladiny
l=0,1,2 ověřil všechny4,16,256 dvojice indexů; pro l=3 dalších104
včetně rovností a obou krajů. Ověřena je skutečná délka po doplnění
identit i involutivnost všech faktorů. Zkrácené délky jsou2,10,46,202,
knižní délky2,20,152,1040. Výsledek v `results/permutation-comparison.json`.
Původní ortogonální konstrukce měla samostatnou již úspěšnou kontrolu;
nekopírujeme ji jako nový nález.
