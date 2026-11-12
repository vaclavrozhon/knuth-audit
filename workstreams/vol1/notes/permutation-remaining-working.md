# Obecné důkazy §1.3.3-28–38

Dokončena matematická a strojová část hlavním agentem1.11.2026.
Originály184–185,526 a527 přečteny;527 je v
`parallel/subroutines/images/p527.png`. Také původní sazba doplňků
37–38 a jejich odpovědí byla zobrazena. Relevantní errata prohledána
ve všech4 vrstvách. Přesný stav primárních odkazů je oddělen
v `permutation-remaining-sources.md`; nedostupné citace nejsou
vydávány za přečtené. Fyzický výtisk nebyl ověřen.

Permutace zde skládáme zleva doprava. Cyklus(a_1...a_k) posílá a_i
na a_(i+1) a poslední prvek na první. Identitu značíme e nebo().
Velikosti n a parametry Josephovy úlohy jsou kladná celá čísla;
pro úlohu31 navíc m>1. Délky datových bloků mohou být i nulové.

## 28: součin pro Josefovu permutaci

Josefova permutace přiřazuje původnímu místu člověka jeho pořadí
vyřazení. Udržujme živé osoby v pořadí, v jakém se od aktuálního
počátku počítá. Otočení celé fronty o m−1 míst doleva dostane první
vyřazovanou osobu na pozici1. Na indexech jde o faktor
`(n n−1 ... 1)^(m−1)`. Potom zůstane pozice1 pevná a otočíme jen
pozice2..n; následně3..n atd. Po každém kroku je další konečná pozice
vyplněna vyřazovanou osobou. Součin faktorů tak přesně dává uvedenou
permutaci původních indexů na pořadí vyřazení. Pro n=8,m=4 jsou
pořadí na původních místech5,4,6,1,3,8,7,2, tj. `(1536824)(7)`.
Pozdější odkaz Herstein/Kaplansky1974§3.5 (14.10.2008) ještě přečíst.

## 29–30: dokonalé proložení a pevné body při m=2

Nechť L=2n+1 a S(j)=2j mod L na1..2n. Člověk, kterého mineme,
dostane nové číslo n+1,n+2,...; člověk vyřazený jako k-tý má aktuální
číslo2k. Nové číslo j=n+i mělo dříve číslo2i−1=2j−L=S(j).
Z čísla2k se tedy opakovaným S, dokud jsme nad n, vrátíme na původní
místo. Proto první návrat S na podmnožinu1..n představuje INVERZNÍ
Josefovu permutaci: k se zobrazí na původní místo k-tého vyřazeného.
První návrat permutace na podmnožinu se získá vyškrtnutím ostatních
symbolů z cyklů. Obrácení cyklů pak dá požadovanou Josefovu permutaci.
Tím je obecně doloženo pravidlo úlohy29.

Pro explicitní vzorec doplněný7.4.2003 označme d=L−2k. Jeden zpětný
krok pro číslo nad n zdvojnásobí jeho doplněk do L. Zastavíme právě
když je tento doplněk mezi n+1 a2n. Proto je původní místo

```
L − d * 2^floor(log2(2n/d)).
```

Jde o přesný celočíselný vzorec, nikoli numerickou aproximaci logaritmu.
Bibliografii Shams2002 je ještě třeba ověřit.

Pro pevný bod k položme r=floor(log2(2n/(L−2k))). Rovnice k pro
původní místo dává

```
k = (2^r−1)L / (2^(r+1)−1).
```

Hodnota r=0 dává k=0 mimo doménu, tedy r>=1. Naopak je-li pravá
strana celočíselná pro r>=1, nesoudělnost čitatele a jmenovatele
znamená2^(r+1)−1 | L. Doplněk L−2k je proto kladný lichý integer
L/(2^(r+1)−1); jeho2^r-násobek leží mezi n+1 a2n. Zvolený r tedy
skutečně odpovídá zastavení a k je pevné místo. To dokazuje obě
implikace a opravenou verzi úlohy30 (1.1.2006). Původní posun
exponentů připouštěl také nesprávné k=0; jde o známé erratum.

## 31: obecná rekurence a průměr pevných bodů

Předpokládáme m>1, jak výslovně doplňuje erratum14.10.2008. Při
průběžném přečíslování vyřazujeme přesně čísla km. Číslo x>n bylo
přiděleno člověku, jehož předchozí číslo je (x−n)-tý kladný integer
nedělitelný m, tedy

```
floor((m(x−n)−1)/(m−1)).
```

Začneme x=km. Pro n<x<=mn je nové x kladné a ostře menší. Proto
postup skončí na původním místě1..n a dává přesně k-tého vyřazeného.

Pro pevné místo j a k kroků zapišme jednotlivá dělení jako
`x_(i+1)=(m(x_i−n)−d_i)/(m−1)`, kde1<=d_i<=m−1. Indukcí je
podmínka x_0=jm,x_k=j ekvivalentní

```
a_k*j = b_k*n+t_k,
a_k = m^(k+1)−(m−1)^k,
b_k = m*(m^k−(m−1)^k),
t_k = sum_{i=0}^{k−1} m^(k−1−i)*(m−1)^i*d_i.
```

Protože a_k−b_k=(m−1)^(k+1) a b_k je nesoudělné s m−1, jsou
a_k,b_k nesoudělné. Všechny (m−1)^k hodnot t_k jsou různé: modulo m
se jednoznačně určí poslední cifra d_(k−1), pak indukce. Jejich rozsah
je menší než a_k, takže dávají různé třídy n modulo a_k. Pro pevné k
jsou případné podmínky předchozího nezastavení splněny pro všechna
dostatečně velká n v těchto třídách: koeficient u n v x_i je
`m−m^(i+1)*(m−1)^(k+1−i)/a_k`, větší než1 pro i<k a menší než1
pro i=k. Každá třída tedy přispívá hustotou1/a_k.

Ještě zdůvodněme, že každá přípustná reziduální třída skutečně dává
celočíselnou iteraci. Vytvořme x_i nejprve uvedenou racionální rekurencí.
Jmenovatel x_i dělí (m−1)^i. Rovnice a_k*j=b_k*n+t_k dává x_k=j celé.
Jestliže x_(i+1) je celé, pak m*x_i je celé; protože m je nesoudělné
s každou mocninou m−1, je celé i x_i. Zpětnou indukcí jsou všechny
mezivýsledky celé. Jediná cifra1<=d_i<=m−1, která činí podíl celým,
pak dává přesně předepsanou podlahu. Pro dostatečně velké n jsou
současně všechny podmínky předchozího nezastavení splněny, jak ukázáno
výše. Tím je průměr pro pevné k rigorózně určen.

K záměně limity a nekonečného součtu je potřeba uniformní odhad.
Položme q=m−1, r=q/m, h=n−j a y_i=mn−x_i. Potom
`y_0=mh`, `y_(i+1)=T(y_i)=floor(my_i/q)+1` a na pevném bodu
`T^k(mh)=qn+h`. Iterace T nezávisí na n, takže pro pevné k a h
existuje nejvýše jedno n. Z T(y)>=y/r plyne h<=Nr^k pro n<=N.
Počet A_k(N) všech pevných bodů s právě k kroky přes n<=N tedy
splňuje `A_k(N)<=Nr^k+1`. Celočíselnost dává ještě
`T(y)>=(y+1)/r−1`, a proto k<=log_(1/r)(mN+1).

Pro všechna K tak máme

```
(1/N) sum_(k>K) A_k(N)
 <= m*r^(K+1) + O_m(log N/N).
```

Nejprve necháme N růst, pak K. Ocas jde k nule, takže průměr
celkového počtu pevných bodů opravdu konverguje k
`sum_(k>=1) q^k/(m^(k+1)−q^k)`. Každý sčítanec leží ostře mezi
r^k/m a r^k/q; geometrické součty dávají ostré meze q/m a1.
Úplný pomocný důkaz, včetně h=0 a všech nerovností, je v
`../parallel/permutation-probability/notes/josephus-uniform-tail.md`.
Byl kořenově znovu odvozen a posouzen. Odkaz CMath§3.3 s.80–81
byl přečten; obsahuje přesně zpětné přečíslování a transformaci,
nikoli tvrzení, že pouhá konvergence řady hustot stačí.

## 32: blízká cyklická permutace

Každá z obou vrstev sousedních transpozic v zadání mění index nejvýše
o1, proto jejich součin nejvýše o2. U sudého k první vrstva může
poslat k na k+1 a druhá zpět nebo dále; při neprovedení první vrstvy
může druhá poslat k na k−1. Tedy k−1<=π_k<=k+2. Pro liché k obdobně
k−2<=π_k<=k+1, včetně okrajů po vynechání neexistujících sousedů.

Násobení transpozicí dvou prvků z různých cyklů tyto cykly spojí:
rozpojí se dvě odchozí hrany a překříží, takže vznikne jediný cyklus.
V pořadí faktorů zadané dvouvrstvé permutace volíme transpozici
právě pokud její sousedé aktuálně patří různým cyklům. Cykly se tak
nikdy nedělí. Po zpracování každé sousední dvojice zůstane tato
 dvojice až do konce v témže cyklu. Řetěz všech sousedních dvojic
spojuje celou množinu, takže nakonec zůstane právě jeden cyklus.
Reference Alpern1978 Superhamiltonian graphs: primární metadata
nalezená, celý text zatím403.

## 33: induktivní ortogonalita na pěti prvcích

Složení permutací je zleva doprava. Položme c=(12345),
p=(14)(23),q=(15)(24),e=identita. Základ l=0,m=2,n=2 je v zadání
odpovědi: A_0=(p,q),B_0=(e,e), A_1=(e,e),B_1=(p,q).
Přímý součin p*q=c i všechny čtyři prokládané základní dvojice byly
ověřeny. Konečná kontrola prošla také celými hladinami l=1,2.

Induktivní krok: jsou-li všechny jednotlivé faktory involuce a
P_ij=A_i1 B_j1 ... A_in B_jn je c právě pro i=j, jinak e, vezmeme
indexy I=(i,i'),J=(j,j') a čtyři bloky délky n. První dva jsou
konjugované A_i,B_j permutací s=(23)(45), pak A_i',B_j' permutací
t=(345). Třetí blok prohodí role A/B a obrátí pořadí původních n
faktorů, stále s konjugací s; čtvrtý obdobně pro i',j' a t.
Protože faktory jsou involuce, výsledkem je

```
s^(-1) P_ij s * t^(-1) P_i'j' t *
s^(-1) P_ji^(-1) s * t^(-1) P_j'i'^(-1) t.
```

P_ij=P_ji (oba jsou pouze c nebo e), takže dostaneme komutátor.
Pokud jedna rovnost indexů neplatí, je e. Pokud platí obě, explicitní
součin čtyř konjugovaných pěti-cyklů je c; malé násobení bylo
přímo ověřeno. Nové faktory jsou znovu involuce. m se umocní
na druhou a n násobí4, takže m=2^(2^l),n=2^(2l+1).

Pro doplněný příklad nerovnosti i<j lze použít lexikografický rozklad
`(i<j) OR ((i=j) AND (i'<j'))`, jehož části se vzájemně vylučují.
Konjugace pevně obracející c na c^(-1) nahrazuje potřebu obracet
celý program; AND se tak sestaví jako komutátor délky2E+2T, kde
E je délka testu rovnosti a T délka testu menší. Přímým součinem
obou disjunktních možností získáme T_new=3T+2E, E_l=2*4^l,T_0=2,
tj.T_l=4^(l+1)−2*3^l. To nepřevyšuje tištěnou délku
6^(l+1)−4^(l+1); na ni lze doplnit identity. Konkrétní základ, všechny
konjugující konstanty, úplná indukce i398 doplňkových kontrol jsou
v `permutation-comparison.md`; tato část je již uzavřena.

## 34–36: blokové přesuny

34. Posun o m modulo N=m+n má d=gcd(m,n) cyklů, po jednom v každé
třídě modulo d. Jde o průchod podgrupou generovanou m v Z/NZ.
Každý cyklus obsahuje jediné j<d, proto zastavení po návratu do j
je ekvivalentní následníkovi<d. Jedna pomocná hodnota uchová původní
x_j; postupnými přiřazeními z následníka do předchůdce se provede
celý cyklus. Nulový celkový rozsah se vyřídí samostatně.

35. Pro délky l,m,n označme M=l+m+n,N=l+2m+n. Doplňme za αβγ
ještě kopii β. Otočení rozšířeného pole o l+m pak dává γβαβ.
Je-li k'≥M, jde o druhou kopii β; její další následník pod posunem
je stejná pozice v první kopii, protože pro k'=M+r je
`(k'+l+m) mod N=l+r`. Při indukovaném posunu na skutečné pozice
0..M−1 se proto každá vynechaná pozice přeskočí jediným dalším
krokem. Výsledek je přesně γβα. Počet cyklů zůstává
`gcd(l+m,m+n)`, protože všechny zbytkové třídy mají zástupce< M.

Druhá metoda v odpovědi: při l<=n rozdělme γ=γ'γ'' s |γ''|=l.
Nejprve vyměňme stejně dlouhé α a γ'', čímž dostaneme γ''βγ'α.
Pak prohoďme sousední bloky **γ''β a γ'**. Dostaneme γ'γ''βα.
Původní pokyn prohodit γ'' s βγ' by dal βγ'γ''α a je chybný;
právě hranici mezi oběma operandy opravuje erratum1.1.2006.
V první pracovní verzi této poznámky byl omylem zopakován původní
chybný pokyn a oprava popsána jako pořadí operandů. Vizuální revize
originálu errat, strana38, tento náš přepis opravila; nejde o nový
nález v knize. Pro l>n napišme α=α'α'' s |α'|=n. Napřed vyměníme α' s γ,
čímž získáme γα''βα'. Následně prohodíme sousední bloky α'' a βα':
výsledek je γβα'α''=γβα. Oba případy tak používají jednu výměnu stejně dlouhých
krajních částí a jeden sousední posun. Reference Mohammed/Subi1987
zůstává v samostatném zdrojovém auditu.

36. Obě úplné rutiny a jejich kontrakty, obecné časové vzorce a
9312 kontrol v1552 bězích jsou v `permutation-block-interchange.md`
a `../mixal_block_interchange.py`. Cyklická metoda zahrnuje virtuální
délku až6000 i při bázi64. Srovnávací metoda používá čtyři reverze.
Hotové výsledky pokrývají všechny délky0–8, všech37 bází i fyzickou
mez3000 datových slov. Obecný časový rozbor uzavírá úlohu36.

## 37: dvě n-cyklické permutace

Znaménko permutace je (−1)^(n−počet_cyklů); každá transpozice je
obrátí. Součin dvou n-cyklů je proto sudý. Naopak indukujeme podle n;
n<=2 je přímo. Pro n>2 vybereme a,b<n s π(a)=b, což lze, protože
jen jeden prvek může mít obraz n. Permutace ρ=(n a)π(b n) fixuje n
a její restrikce na1..n−1 je sudá. Indukcí ρ=AB, kde A,B jsou
(n−1)-cykly; otočme jejich zápisy tak, že A=(α a),B=(b β).
Pak π=(n a) A B (b n)=(n α a)(b β n), součin dvou n-cyklů.
Tím je doplněné cvičení obecně dokázáno. Původní tisk
errata2010 byl zobrazen a primární Jacques et al.1968 získán;
přesný přečtený rozsah je v poznámce k pramenům.

## 38: konjugace

Definice π^τ=τ^(-1)πτ je ve zvolené levostranné konvenci změna
jmen: cyklus(a_1...a_k) přejde na(τ(a_1)...τ(a_k)). Z toho:
(a) π^τ=π právě když πτ=τπ; (b) uvedené přejmenování;
(c) dvě3-cyklické orbity lze přiřadit dvěma způsoby, jejich počátky
zvolit3*3 způsoby a2-cyklus otočit2 způsoby, celkem36 řešení.
Konkrétní tři vytištěné příklady i všech36 řešení byly přímo ověřeny.
(d) cyklové délky3,2,3 a4,4 se liší, řešení není.
(e) každá permutace je konjugovaná své inverzi: na každém cyklu
obrátíme pořadí jmen. (f) obě identity jsou asociativita a zrušení
ττ^(-1); (πσ)^τ=π^τσ^τ a π^(στ)=(π^σ)^τ.
Původní sazba zadání i odpovědi2023 byla zobrazena. Primární
Netto1892§46 je zpracován zvlášť v poznámce k pramenům.


## Reprodukovatelné kontroly a rozsah závěru

`check_permutation_remaining.py` prošel77054 kontrolami (1.65s).
Zahrnuje rodiny28–30, samotnou rekurenci31, všechny permutace do7
pro32 a37, celé hladiny0–2 pro33, rozměry0–12 pro35, sousední
posuny do39 a všech36 konjugací z38(c). Samostatné checkery porovnání
33 a MIX36 přidaly398 a9312 kontrol; přesný rozsah je v jejich
poznámkách a JSON výsledcích. Úspěšné běhy se bez změny neopakují.

Obecné důkazy nad těmito konečnými kontrolami jsou rozhodující:
nejde o závěr pro všechny vstupy odvozený jen z testování. Nová
neopravená matematická chyba v28–38 nebyla zjištěna. Zbývající
bibliografické meze jsou vyznačeny zvlášť v poznámce k pramenům.
