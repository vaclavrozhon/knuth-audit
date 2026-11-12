# Krajní rozdělení a srovnávací nerovnosti: SAT 344–345

Kontrola 31. 10. 2026. Nový nález zde nepřibyl; při přechodu na hranici
je zapracována již evidovaná oprava F035. Základní konstrukce a všechny
části 344 jsou platné v rozsahu níže.

## Přesný vzorec pro atomové pravděpodobnosti

Nechť π_I=Π_(i∈I)p_i, pokud je I nezávislá množina, a jinak 0.
Möbiovou inverzí jsou hmotnosti přesných konfigurací

`q_S = Σ_(T⊇S) (−1)^|T\S| π_T`.

Není-li S nezávislá, q_S=0. Je-li nezávislá, musí všechny další
vybrané vrcholy ležet mimo její **uzavřené okolí** N[S]. Proto

`q_S = (Π_(i∈S)p_i) M_(G\N[S])(p)`.

To je úplný argument pro 344(a). Je-li p∈R(G), všechny potřebné
indukované Möbiovy hodnoty jsou kladné, takže q_S≥0. Jejich součet je
π_∅=1; jde tedy o legitimní rozdělení. Nulové p_i nevadí.
Vzorec výslovně odstraňuje i sousedy S, aby nevznikl nesprávný obecný
výraz používající jen G\S.

Ve čtyřudálostním příkladu uvedeném v odpovědi by záporný atom S={1,4}
nemohl nastat, kdyby se po odstranění N[S] zachoval nejvýše jeden vrchol,
protože 1−p_i≥0. Případ negativního atomu proto opravdu vede k uvedenému
polynomu na {2,3}. Nečteme tento zkrácený argument jako obecnou identitu
pro libovolný atom; nevzniká tím další nález.

## Nezávislost a vyhýbání událostem

Pokud I a J jsou disjunktní a nemají mezi sebou hranu, platí
`π_(I∪J)=π_I π_J`, i když některá strana obsahuje hranu uvnitř.
Momenty všech součinů indikátorů se tedy faktorizují; rozvinutím
součinů (1−B_j) plyne nezávislost celých vektorů událostí na těchto
dvou množinách. Zejména platí rovnost (147) pro všechna definovaná
podmínění na neuskutečnění nesousedních událostí.

Pravděpodobnost vyhnout se všem událostem na J je

`β(J)=Σ_(I⊆J)(−1)^|I|π_I=M_(G[J])(p)`.

Tím je dokázána 344(c). Zároveň platí obrácená charakterizace:
jsou-li atomy legitimní a β(V)>0, pak β(J)≥β(V)>0 pro každé J,
tedy p∈R(G). Kladnost ve všech rozích boxu stačí, protože M je
multiafinní. Na uzavřené hranici obdobně odpovídá nezápornost všech
atomů nezápornosti všech indukovaných Möbiových hodnot.

## Srovnání 344(d)

Pro libovolné skutečné události splňující lopsided podmínku (133)
pišme α(J)=Pr(všem událostem na J se vyhneme). Indukcí dokazujeme
silnější lokální poměr

`α(J∪i)/β(J∪i) ≥ α(J)/β(J)`.

Označme J′=J\N(i). Podmínka (133) a zahrnutí událostí dávají

```
α(J∪i) ≥ α(J)−p_i α(J′),
β(J∪i) = β(J)−p_i β(J′).
```

Po vynásobení kladnými jmenovateli je požadovaný rozdíl alespoň

`p_i(α(J)β(J′)−α(J′)β(J)) ≥0`.

Poslední nerovnost je indukční předpoklad aplikovaný postupně na
J′⊆J. Prázdná množina má poměr 1, takže α(J)≥β(J) pro všechna J.
To je Shearerova srovnávací mez; nevyžaduje vzájemnou nezávislost
sousedních událostí.

## Lovászovy parametry 344(e)

Nechť `p_i=θ_i Π_(j∈N(i))(1−θ_j)`, s 0≤θ_i<1.
Současně indukujeme β(J)>0 a
`β(J∪i)≥(1−θ_i)β(J)`.

Z již dokázaných poměrů na menších množinách máme
`β(J)/β(J′)≥Π_(j∈J\J′)(1−θ_j)`. Součin definující p_i obsahuje
všechny tyto faktory a případné další nejvýše jedničkové faktory.
Proto `p_i β(J′)≤θ_i β(J)` a rekurence β dává požadovanou mez.
Je přísně kladná, jelikož θ_i<1. Součinem lokálních poměrů dostáváme
`β(J)≥Π_(j∈J)(1−θ_j)>0`, a tím p∈R(G) i hlavní Theorem L.
Důkaz tedy nepředpokládá předem kladnost, kterou má teprve ukázat.

## 345 po opravě F035

Pro p mimo R(G), s jednotlivými p_i∈[0,1], postupujme po paprsku
od nuly k prvnímu nulovému bodu p′=t p. Pro každé ε>0 leží
(1−ε)p′ uvnitř R, tedy má legitimní krajní rozdělení. Jeho atomy
jsou polynomy v p; limita dává legitimní krajní rozdělení také v p′,
s q_∅=M(p′)=0. F035 upozorňuje, že snížení pouze jedné souřadnice
nemusí z hraničního bodu udělat bod s kladným M. Radiální limitní
argument toto nepotřebuje.

Nyní přidejme každé události nezávislé zapnutí s pravděpodobností
`c_i=(p_i−p′_i)/(1−p′_i)`. Pokud p′_i=1, pak také p_i=1 a lze vzít
c_i=0. Události B_i=B′_i∨C_i mají požadované marginály p_i.
Dřívější nevyhnutelnost zůstane zachována, protože události se pouze
zvětšují. Nezávislost od celého vektoru nesousedních událostí zůstane
také zachována: vektor B′ ji má a všechna nová zapnutí jsou navzájem
 i od B′ nezávislá. Tím je konstrukce 345 úplně ověřena.

## Přesné konečné kontroly

`check_extreme_distribution.py` provedl:

- **41 055** systémů atomových vah na všech grafech s nejvýše čtyřmi
  vrcholy a pravděpodobnostech 0,1/4,1/2,3/4,1; **648 210** kontrol
  uzavřeného vzorce přes N[S].
- **12 206** legitimních rozdělení, z toho 6100 uvnitř a 6106 na
  hranici; **298 105** přesných rovností závislosti, včetně následných
  **6106** nezávislých zapínání událostí z hraničního rozdělení.
- Všech **33 296** dvojic (soustava událostí, graf) na rovnoměrném
  čtyřbodovém prostoru s nejvýše třemi událostmi. Podmínku (133)
  splnilo 19 734; z toho 4605 mělo p∈R. Prošlo **53 239** silných
  poměrových nerovností.
- **16 932** parametrizací θ z {0,1/4,1/2,3/4} na všech grafech
  s nejvýše čtyřmi vrcholy; **530 564** lokálních poměrových mezí
  a všechny součinové meze.

Vše používá celočíselnou aritmetiku se společnými jmenovateli, včetně
nulových hodnot a hraničních případů. Data jsou v
`results/extreme_distribution.json`. Konečné výčty doplňují obecné
důkazy výše; počet zkoušek není počet nezávislých vět.
