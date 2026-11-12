# Kografy, hranice R(G) a involuční polynomy

Kontrola 31. 10. 2026, SAT 341,343,345. Nálezy F033–F035 jsou
potvrzeny v hlavním PDF i v Knuthově Pre-Fascicle 6A z 23. 9. 2015.
V úplných erratech 4B ani Fascicle 6 odpovídající opravy nejsou.

## F033: kladná hodnota M_G nestačí ani pro kografy

Úloha 343 na str. 347 tvrdí pro libovolný kograf ekvivalenci
`p∈R(G) ⇔ M_G(p)>0`. Odpověď na str. 615 ji odvozuje z údajné
monotonicity v každé souřadnici. Obě tvrzení jsou nepravdivá.

Vezměme **G=K₂⊕K₂**, dvě disjunktní hrany 12 a 34. Jde o kograf,
protože vzniká disjunktním sjednocením dvou úplných grafů. Přímo ze
seznamu nezávislých množin nebo z odpovědi 336 plyne

`M_G(p)=(1−p₁−p₂)(1−p₃−p₄)`.

Pro všechny p_i=3/4 vychází **M_G=1/4>0**. Avšak při snížení p₃,p₄
na nulu dostaneme **−1/2**, takže p není v R(G) podle definice na
str. 271. Záporná hodnota už na indukované hraně stačí k vyvrácení.
V téže oblasti je derivace podle p₁ kladná: snížení p₁ tedy M_G
snižuje, v rozporu s první větou odpovědi.

### Skutečná soustava nevyhnutelných událostí

Protipříklad není jen formální manipulace s polynomem. Nechť U,V
jsou nezávislé rovnoměrné veličiny na {0,1,2,3} a

```
A₁=[U≠0], A₂=[U≠1], A₃=[V≠0], A₄=[V≠1].
```

Každá má pravděpodobnost 3/4. Dvojice událostí na různých hranách
závisejí na nezávislých veličinách, takže (133) platí dokonce s rovností
pro všechna podmínění kladné pravděpodobnosti. Ale A₁∨A₂ nastane vždy;
pravděpodobnost vyhnutí všem čtyřem je nula, nikoli kladné číslo.
Výčet všech 16 stavů a 12 netriviálně definovaných podmínění to ověřuje.

Pouhé doplnění souvislosti grafu nepomůže: spojme oba konce obou hran
s novým univerzálním vrcholem 5. Tento souvislý kograf na pěti vrcholech
má `M_G=(1−p₁−p₂)(1−p₃−p₄)−p₅`. Při prvních čtyřech p_i=3/4
 a p₅=1/10 je hodnota **3/20>0**, ale obsahuje stejnou nevyhovující
indukovanou hranu.

### Opravené rozhodovací pravidlo

Kogreaf má rozkladový strom, jehož listy jsou vrcholy a vnitřní uzly
jsou disjunktní sjednocení nebo úplné spojení dětí. Platí:

**p∈R(G) právě tehdy, když je Möbiova hodnota kladná v každém uzlu
zvoleného rozkladového stromu, včetně listů.**

Nutnost plyne z uzavřenosti R vůči indukovaným podgrafům. Pro
postačitelnost postupujeme zdola. List má 1−p_i>0 a tento výraz je
neklesající při snižování p_i. U disjunktního sjednocení jsou
polynomy dětí kladné na celém příslušném boxu, proto je jejich součin
rovněž kladný a monotónní. U úplného spojení je polynom součtem
polynomů dětí minus (počet dětí−1); kladnost v horním rohu a
monotonicita dětí tedy zajišťují kladnost na celém boxu. Tím se
indukce uzavře. Test pouze v kořeni ztrácí informaci o znaménkách
obou záporných faktorů, jak ukazuje protipříklad.

`check_cographs.py` prošel všech **535 označených kografů na 1..5
vrcholech** a všechny vektory z {1/4,1/2,3/4}^n: celkem **119 145**
kombinací. Opravený test v uzlech stromu přesně souhlasí s kontrolou
všech indukovaných podgrafů. Ta je ekvivalentní kontrole celého boxu,
protože polynom je multiafinní a minimum na boxu je v některém rohu.
Původní tvrzení selhalo ve 27 kombinacích na čtyřech a 3075 na pěti
vrcholech; jsou to další instance F033, nikoli nové samostatné nálezy.

## F034: v rekurenci odpovědi 341 chybí w_ij

První zobrazená rekurence na str. 615 má správně být

`W(S)=w_ii x W(S\{i}) − Σ_(j∈S,j≠i) w_ij W(S\{i,j})`.

Tisk vynechává w_ij před každým sčítancem. Už pro dva vrcholy,
w₁₁=w₂₂=1,w₁₂=2, je podle definice W=x²−2, zatímco vytištěná
rekurence dává x²−1. Následující slovní odstavec používá váhy správně.

### Správnost věty o kořenech

Dělením W(S) součinem diagonálních vah přejdeme k monickým polynomům
H_S a kladným hranovým vahám λ_ij=w_ij/(w_ii w_jj):

`H_S=xH_(S\i)−Σ_j λ_ij H_(S\{i,j})`.

Indukce současně dokazuje reálné jednoduché kořeny a ostré prokládání
po odstranění libovolného vrcholu. Nechť r₁<...<r_n jsou kořeny H_n.
Každý monický polynom H_(n\j) je v r_k znaménka (−1)^(n−k), protože
jeho n−1 kořenů leží ostře mezi sousedními r. Proto

`sign H_(n+1)(r_k)=(−1)^(n−k+1)`.

Kladné λ brání vzájemnému vyrušení. Střídání znamének, monický vedoucí
člen a obě nekonečna dávají n+1 odlišných reálných kořenů mezi r
 a v obou vnějších intervalech. To vyčerpá celý stupeň a uzavírá důkaz.
Při povolení nulových vah zůstane reálnost kořenů limitním přechodem,
ale ostré prokládání a jednoduchost se obecně ztratí.

Nezávislý program vybral involuce z úplných permutací, spočítal jejich
cyklové váhy a porovnal součty s opravenou rekurencí. Pro **84 soustav
kladných celočíselných vah**, n=1..7, prošlo 4212 involučních členů,
84 přesných Sturmových kontrol počtu reálných jednoduchých kořenů
 a **1344** kontrol ostrého prokládání pomocí racionálních izolačních
intervalů. Obecnou větu dokazuje argument výše.

## F035: po snížení jedné souřadnice může hraniční M_G zůstat nula

Odpověď 345 na str. 615 tvrdí, že po škálování na první nulový bod
M_G se hodnota stane kladnou, jakmile se sníží libovolné p′_j.
Pro tentýž graf dvou oddělených hran vezměme

`p′=(1/2,1/2,1/2,1/2)`.

Je to první nulový bod na paprsku z počátku. Avšak

`M_G(1/4,1/2,1/2,1/2)=(1/4)·0=0`.

Ostrost při změně jedné souřadnice tedy neplatí. Na rozdíl od F033
zde zůstává platná vlastní konstrukce nevyhnutelných událostí; jde
 o nesprávné pomocné tvrzení v jejím důkazu.

Stačí použít **nezápornost** na uzavřeném boxu do p′. Případně lze
zmenšit radiálně všechny kladné souřadnice: (1−ε)p′ leží uvnitř R.
Extrémní rozdělení z 344 pro tyto vektory jsou legitimní a jeho
atomové hmotnosti jsou polynomy v pravděpodobnostech. Limita ε→0
proto dává legitimní rozdělení v p′ s nulovou pravděpodobností
vyhnutí. Následné nezávislé zapínání událostí, jak je uvedeno v 345,
zvyšuje marginály na požadované p a zachovává nevyhnutelnost i
nezávislost na nesousedních událostech. Není potřeba předpokládat
kladnost po změně jednotlivé souřadnice.

## Doklady a omezení

Znění: `images/vol4b-p347.png`, `images/traces-635.png`,
`images/fasc6a-p163.png`, `images/fasc6a-p251.png`.
Výsledky: `results/cographs.json`, `results/involution.json`.
F033 je chybná věta, F034 vynechaný faktor a F035 chybná pomocná
ostrost. Fyzický výtisk dosud neověřen; zprávy jsou pouze návrhy.
Navazující plný audit 344 je ještě oddělený úkol, nikoli výsledek
těchto testů.
