# §1.2.4: celé části, kongruence a reciprocita

Kontrola 1. listopadu 2026, třetí vydání, první dotisk 1997.
Původní s. 39–45 a odpovědi 476–480 byly zobrazeny jako obrazy
`images/vol1-file054-p39.png` až `vol1-file060-p45.png` a
`vol1-file491-p476.png` až `vol1-file495-p480.png`.
Inventář má 49 původních úloh a úlohu 50 přidanou 3. června 2021.
Úlohy 37–38 mají již dokončený důkaz v [floor-sums.md](floor-sums.md);
jejich úspěšné výpočty se neopakovaly. Úlohy 39–40 jsou samostatně
v [replicative-functions.md](replicative-functions.md).

## Definice a hlavní text

`floor(x)` je největší celé číslo nejvýše x, `ceil(x)` nejmenší celé
číslo nejméně x, `frac(x)=x-floor(x)` zlomková část. Tudíž
`x-1<floor(x)<=x<=ceil(x)<x+1`. Obě části jsou shodné právě na celých
číslech, jinak se liší o 1; negace zaměňuje podlahu a záporný strop.
Všech pět číselných příkladů na s. 39 odpovídá těmto intervalům.

Knižní zbytek je `x mod y=x-y floor(x/y)` pro y!=0, a `x mod 0=x`.
Pro nenulové y je `(x mod y)/y=frac(x/y)`. To dokazuje oba znaménkové
intervaly zbytku a vlastnost, že rozdíl x a zbytku je celočíselný
násobek y. Poslední vlastnost platí i pro y=0, kdy je rozdíl 0.
Nulový zbytek je ekvivalentní celočíselnému násobku i při y=0.
Kniha používá `y|x` jen pro kladné celé y.

Kongruence `x≡y (mod z)` znamená shodu zbytků. Pro z!=0 je ekvivalentní
`x-y=qz` s celým q: jedna implikace plyne odečtením definic, druhá
z `floor(y/z+q)=floor(y/z)+q`. Pro z=0 jsou obě tvrzení prostě x=y.
Doplnění z 8. srpna 2025 tuto ekvivalenci vysvětluje, nemění její platnost.
Periodičnost tangens dává příklad na s. 40 všude, kde je tangens
definován; redukce modulo pi zachovává také jeho póly.

`gcd(a,b)` označuje nezáporný největší společný dělitel, s konvencí
gcd(0,0)=0; `a⊥b` znamená gcd(a,b)=1. Kongruenční zákony A–D
pro všechna celá čísla včetně nulových/záporných modulů mají důkazy
u úloh 17–20 níže. Fermatův důkaz na s. 41 je správný: násobení
nenulovým zbytkem a permutuje p zbytků modulo prvočíslo p. Vynásobením
p−1 nenulových zbytků a jejich zkrácením dostaneme a^(p−1)≡1;
případ p|a se ošetří samostatně. Důkaz zahrnuje p=2 a záporné a.
Historické připsání Fermatovi roku 1640 a Iversonovy notace nejsou
samotným matematickým důkazem ověřeny.

## Úlohy 1–16: intervaly a zbytky

- 1: výsledky v pořadí originálu jsou 1,−2,−1,0,5; poslední plyne
  z 2^5<=35<2^6. Markdown prohodil druhý a třetí výraz.
- 2: strop podlahy je podlaha, protože podlaha je celé číslo.
- 3: pro celé n platí `floor(x)<n ⇔ x<n`,
  `n<=floor(x) ⇔ n<=x`, `ceil(x)<=n ⇔ x<=n` a
  `n<ceil(x) ⇔ n<x`. První např. říká floor(x)<=n−1,
  ekvivalentně x<n. Zbylé jsou negace nebo záměna znamének.
  Jejich spojení dává přesně intervaly (e),(f) v zadání.
- 4: z `x<=ceil(x)<x+1` dostaneme `−x−1<−ceil(x)<=−x`.
  Úloha 3(e) dává floor(−x)=−ceil(x). Opravená odpověď z 2013
  používá právě tento postup. Původní odpověď pracuje s floor(x)
  a po náhradě x za −x dává tentýž závěr; výsledek není chybný.
- 5: `floor(x+1/2)`. Mimo polocelé body je zaokrouhlení liché
  vzhledem k negaci. V polocelých bodech jde vždy k +nekonečnu,
  tedy u záporných hodnot k nule a u kladných od nuly.
- 6(a): pro nezáporné celé k je `k<=sqrt(x)<k+1` ekvivalentní
  `k²<=x<(k+1)²`; celočíselné prahy dovolují nahradit x podlahou.
  (b) obdobně s `(k−1)²<x<=k²` a stropem, pro x>0 a k>=1.
  (c) je nepravda: x=11/10 dává ceil(sqrt(floor(x)))=1,
  kdežto ceil(sqrt(x))=2. Markdown má chybně jinou pravou stranu.
- 7: `floor(x+y)=floor(x)+floor(y)+floor(frac(x)+frac(y))`.
  Rovnost nastane právě pro součet zlomkových částí <1.
  Negací dostaneme `ceil(x)+ceil(y)>=ceil(x+y)`, s rovností právě
  když frac(−x)+frac(−y)<1. To je ekvivalentní původní odpovědi:
  jeden argument je celý, nebo frac(x)+frac(y)>1. Dodatek 2005
  jen doplňuje tuto symetrickou formulaci.
- 8: 1,2,5,−100. 9: −1,0,−2. 10: 1/10,1/100,−9/100;
  desetinné vstupy se zde berou jako přesná reálná čísla.
- 11: kongruence modulo 0 je rovnost. 12: každé celé číslo
  je nesoudělné s 1. 13: s 0 jsou nesoudělná právě ±1.
- 14: z x=2+3q a x≡3 (mod 5) plyne q≡2 (mod 5), tedy
  x=8+15t a požadovaný zbytek 8. Předpoklady samy vynutí celé x.
- 15: pro yz!=0 se při násobení obou argumentů z poměr x/y
  nemění, ani když z<0. Pro z=0 jsou obě strany 0; pro y=0
  obě strany zx. Tyto dvě větve doplňují stručnou odpověď.
- 16: x=z+qy, 0<=z<y dává q<=x/y<q+1, a tudíž z=x mod y.

## Úlohy 17–32: elementární teorie čísel

17. Pišme a=b+qm, x=y+rm, kde q,r jsou celá. Potom rozdíl
součtů/rozdílů je (q±r)m a `ax−by=(br+yq+qrm)m`.
Je-li a−b=krs, je to násobek r i s, včetně r=0 nebo s=0.

18. Je-li a−b=kr a zároveň kr≡0 (mod s), zákon B při r⊥s
dá k=qs. Tedy a−b=qsr. Toto platí i když jeden modul je nula,
neboť druhý musí být ±1. Zákon C plyne okamžitě z
a−b=qm po vynásobení nenulovým n, a obráceně po vydělení n.

19. Rozšířený Eukleidův algoritmus z §1.2.1 dává Bézoutovy
koeficienty u,v s un+vm=1; u je požadovaná inverze. Pro záporné
vstupy se provede na absolutních hodnotách a opraví znaménka.
Případy n=0,m=±1 a m=0,n=±1 mají zjevné koeficienty a nevyžadují
spuštění algoritmu mimo jeho kladný vstupní obor.

20. Z a≡b a ax≡by dostaneme a(x−y)≡0. Násobení inverzí a
dá x−y≡0. To je zákon B. Závislosti nejsou kruhové:
Bézoutův důkaz nevyužívá zákon B.

21. Existence prvočíselného rozkladu byla dokázána v §1.2.1-5.
Jestliže prvočíslo p dělí součin prvočísel q_j a žádné q_j není p,
opakované krácení zákonem B by dalo 1≡0 (mod p), spor.
Společný prvočinitel tedy lze odstranit a indukovat podle n.
Prvočíselný případ ukončuje indukci; pořadí sjednotíme seřazením.

22. Bez nesoudělnosti nelze krátit: 2·1≡2·0 (mod 2), ale
1 není kongruentní 0. Obecná rodina m=ax z odpovědi má stejné
vlastnosti pro a>1,x>0. 23. Pro r=s=2,a=2,b=0 jsou obě jednotlivé
kongruence pravdivé, kdežto kongruence modulo 4 je nepravdivá.

24. Pro reálné proměnné vždy platí A pro sčítání/odčítání a C
pro nenulový reálný násobek; jejich důkazy vyžadují jen celé
koeficienty q,r. Násobení v A univerzálně neplatí:
a=b=1/2,x=1,y=0,m=1 splní předpoklady, nikoli závěr.
B selže i při zachování celých nesoudělných a,m:
a=b=2,m=3,x=3/2,y=0. Nesoudělnost není v knize pro obecná reálná
čísla definována. D však dál platí pro reálná a,b a celé nesoudělné
r,s: rozdíl a−b patří do průniku rZ a sZ, což je rsZ.
Ani dopředná část D neplatí pro libovolné reálné moduly:
r=s=1/2,a=1/4,b=0. Tím je přesně odlišeno, které proměnné
mohou být reálné; stručná knižní odpověď A,C je správná.

25. Fermat plus krácení dává zbytek 1, když p nedělí a;
jinak je zbytek 0, neboť p−1>=1. 26. Pro p liché a p nedělící a
je b²≡1, takže (b−1)(b+1)≡0. Prvočíslo p musí dělit jeden faktor.
Případ p|a dává b≡0. Exponent (p−1)/2 je kladné celé číslo.

27. Eulerova funkce phi(n) počítá nesoudělné zbytky 0,...,n−1.
Pro p^e jsou nevyhovující právě p^(e−1) násobky p, tedy
phi(p^e)=p^e−p^(e−1). Zvláštní hodnota phi(1)=1 počítá zbytek 0.

28. Násobení a nesoudělným s m permutuje nesoudělné zbytky:
inverze dokazuje bijektivitu a součin nesoudělných čísel zůstává
nesoudělný. Součin všech těchto zbytků lze zkrátit a získat
a^phi(m)≡1. Pro m=1 platí každá kongruence; zvlášť jej ošetřujeme
bez potřeby nenulových zbytků. Inverze n^0 mod1=0 je správná i
pro n=0 podle dříve stanovené konvence 0^0=1.

29. Pro nesoudělná kladná r,s jsou množiny prvočinitelů disjunktní.
Proto (a) (rs)^c=r^c s^c (kladné základy), (b) rs je bez čtvercového
dělitele právě když jsou taková obě r,s, (c) počty různých prvočinitelů
se sčítají, a (d) lze přeskupit součin dvou násobných funkcí.
Při c=0 a n=1 v (c) platí knižní 0^0=1.

30. Zobrazení (x,y)↦(sx+ry) mod rs z nesoudělných zbytků modulo
r a s je injektivní: redukce modulo r a s a krácení určí oba vstupy.
Každý jeho výstup je nesoudělný s rs. Obráceně libovolný nesoudělný
zbytek z určí x=s^(-1)z mod r a y=r^(-1)z mod s a zákon D zajistí
správný výstup. Funguje i r=1 či s=1. Tudíž phi je násobná,
phi(n)=n product_{p|n}(1−1/p), a phi(10^6)=400000.

31. Každý kladný dělitel rs má jednoznačný tvar cd, c|r,d|s,
opět díky disjunktním prvočinitelům. Dvojitý konečný součet
f(cd)=f(c)f(d) se rozpadne na součin dvou součtů.
Pro nezápornou f je stejně správné doplnění s maximem: maxima
konečných neprázdných množin součinů nezáporných hodnot se násobí.

32. Dvojice kladných dělitelů (c,d) s c|d|n jsou v bijekci
s dvojicemi (c,e), c|n,e|(n/c), pomocí d=ce. To dokazuje identitu
pro libovolné f. Běžný obor těchto dělitelových součtů je n>0;
pro záporné nenulové n je důkaz také konečný a platí. Pro n=0
by byly množiny nekonečné a bez konvergence nelze tvrdit konečnou
identitu pro libovolné f; takové rozšíření zde neprovádíme.

## Úlohy 33–36: skládání celých částí

33. Dva čitatele n+m a n−m+1 mají opačnou paritu. Jedna polovina
je celé číslo a druhá polocelé, jejich součet je n+1/2. Součet
podlah je proto n a součet stropů n+1, i pro záporná m,n.

34. Nutně b je celé: při x=b je levá podlaha 1, ale pro necelé
b je floor(log_b floor(b))<=0. Pro celé b>=2 jsou všechny prahy
b^k, k>=0 celé, takže interval `b^k<=x<b^(k+1)` zachovává podlaha x.
Stropová varianta také vyžaduje celé b (znovu x=b) a je správná
podle intervalů `b^(k−1)<x<=b^k`. Zadání originálu má x>=1.

McElieceovo obecné tvrzení v odpovědi je správné. Nechť f je spojitá
a přísně rostoucí na intervalu A, který s x obsahuje i floor(x),
ceil(x). Nutnou a postačující podmínkou pro obě komutační identity
je: celočíselná hodnota f(x) může nastat jen na celočíselném x.
Nutnost plyne z přísné monotonie: je-li f(x)=k celé a x necelé,
pak f(floor(x))<k<f(ceil(x)), takže selžou obě identity.
Pro dostatečnost by `floor(f(floor(x)))<floor(f(x))` díky spojitosti
dalo y v (floor(x),x] s celočíselnou f(y), což je nemožné.
Stropová varianta má stejný argument v [x,ceil(x)).

35. Pro celočíselné m,n, n>0, má lineární funkce (x+m)/n
celočíselnou hodnotu jen při celočíselném x; předchozí důkaz tedy
platí. Přímá kontrola v odpovědi rovněž správně využívá, že zlomková
část celočíselného čitatele děleného n je nejvýše (n−1)/n.
Stropová varianta se získá negací a náhradou m za −m.

36. Při n=2t se členy podlah sdružují do součtu t²; při n=2t+1
přibude t. Výsledek je floor(n²/4). Součet stropů je
ceil(n(n+2)/4), protože ceil(k/2)=k−floor(k/2).
Také n=0 dává prázdné součty 0.

## Úlohy 41–44: součty skokových funkcí

41. a_n=k právě když k(k−1)/2<n<=k(k+1)/2. Pro celé n>=1
to znamená `(k−1/2)²<2n<(k+1/2)²`, a tudíž
`a_n=floor(sqrt(2n)+1/2)`. Kniha uvádí také
`ceil(sqrt(2n)−1/2)`, `ceil((sqrt(8n+1)−1)/2)` a
`floor((sqrt(8n−7)+1)/2)`. Všechny čtyři mají přesně stejný
interval pro a_n=k. Polocelá sqrt(2n) nemůže nastat pro celé n.

42(a). Po rozepsání rozdílů je koeficient každého a_j v
`n a_n−sum_{k=1}^{n−1} k(a_(k+1)−a_k)` roven 1.
(b) Položme L=floor(log_b n), b>=2 celé,n>=1.
Skok nastane právě při k+1=b^t, 1<=t<=L; jeho váha je b^t−1.
Odečtení geometrického součtu dává
`(n+1)L−(b^(L+1)−b)/(b−1)`, přesně jako v knize.
Oprava 2005 na s. 479 mění typografický řez podmínky pod součtem.

43. Pro h=floor(sqrt(n)), n>=0, nastávají skoky při k=t²−1,
2<=t<=h. Tedy součet je `nh−sum_{t=2}^h(t²−1)`.
Použitím součtu čtverců, který lze ověřit rozdílem pro sousední h,
dostaneme `h(n−(2h+5)(h−1)/6)`, přesně odpověď. Případ h=0
dává 0 přímo a nepotřebuje prázdný rozsah přepisovat polynomem.

44. Hermitova identita z již prověřené úlohy 38 dává pro každé k
`sum_{1<=j<b} floor((n+j b^k)/b^(k+1))
 = floor(n/b^k)−floor(n/b^(k+1))`.
Součet do K se tedy teleskopuje na `n−floor(n/b^(K+1))`.
Poslední podlaha je pro velké K rovna 0 při n>=0 a −1 při n<0.
Výsledky jsou n a n+1; od jistého K jsou už všechny sčítance nulové,
takže tu není problém s nekonečnou konvergencí.

## Úlohy 45–47: reciprocita a kvadratické zbytky

45. Nyní jsou m,n kladná celá, jak doplnila errata z 15. října 2007.
Symetrie prvního vzorce plyne z úlohy 37 a symetrie gcd(m,n).
Bez doplněného m>0 např. m=−1,n=1,x=1 dává 1 proti prázdnému
součtu 0. V druhém vzorci musí být **stropy**, jak je v originálu.
Počet j s floor(mj/n)=r je
`ceil((r+1)n/m)−ceil(rn/m)`, 0<=r<m. Vynásobením f(r), součtem
a přeskupením dostaneme

```text
sum_{0<=j<n} f(floor(mj/n))
 = sum_{0<=r<m} ceil(rn/m)(f(r−1)−f(r)) + n f(m−1).     (R)
```

Člen r=0 má koeficient 0. Pro f(r)=C(r+1,k), kde C je binomický
koeficient, Pascalova identita dává f(r)−f(r−1)=C(r,k−1).
To je přesně druhý vzorec v zadání, včetně k=0 při obvyklých
konvencích pro nezáporný horní index.

46. Nechť alpha>0, N=ceil(alpha n), R=ceil(alpha m).
Pro r=0,...,R−2 jsou počty stejné jako v úloze 45, zatímco poslední
blok má N−ceil((R−1)n/m) členů. Je nezáporný, neboť R−1<alpha m.
Stejné přeskupení dává přesnou knižní odpověď

```text
sum_{0<=j<alpha n} f(floor(mj/n))
 = sum_{0<=r<alpha m} ceil(rn/m)(f(r−1)−f(r))
   + ceil(alpha n) f(ceil(alpha m)−1).                  (G)
```

Zahrnuty jsou celočíselné i neceločíselné koncové body a R=1.

47. Pro liché prvočíslo p definujme h=(p−1)/2. Knižní Legendreův
symbol (q/p) je znaménko zbytku q^h z úlohy 26, s hodnotou 0 pro p|q.
(a) Pro p nedělící q napišme 2kq=p t_k+r_k, 0<r_k<p,
1<=k<=h. Jelikož p je liché, r_k má stejnou paritu jako t_k.
Číslo (−1)^t_k r_k je tak kongruentní sudému zbytku 2,...,p−1.
Dva takové výstupy mohou splývat jen když k≡±l (mod p);
v rozsahu 1,...,h to znamená k=l. Součinem a krácením všech
sudých zbytků dostaneme `(q/p)=(−1)^sum t_k`.
Argument platí také pro záporné q.

(b) Pro q=2 je t_k=1 právě když k>p/4. Počet je n pro p=4n+1
a n+1 pro p=4n+3. Dostáváme znaménka +,−,−,+ pro p mod8=1,3,5,7.

(c) Opravený předpoklad je q liché a p nedělící q. Sudé indexy
2,4,...,p−1 větší než h zaměňme za p−j, kde j je liché
a 1<=j<=h. Protože jq/p není celé,
`floor((p−j)q/p)=q−1−floor(jq/p)≡floor(jq/p) (mod2)`.
Zbývající sudé indexy a tyto liché indexy tvoří přesně 1,...,h.
Oba součty v zadání tedy mají stejnou paritu. Bez výjimky p|q
selže např. p=q=3: součty jsou 2 a 1. Oprava je z 23. června 2010.

(d) Položme v (G) m=q,n=p,alpha=1/2 a f(r)=r.
Dostaneme součet podlah kq/p a součet stropů rp/q roven
ceil(p/2)(ceil(q/2)−1)=(p+1)(q−1)/4. Pro různá prvočísla
nejsou zlomky rp/q ve vnitřním rozsahu celé, takže každý strop
je podlaha plus 1. Součet obou podlah je proto (p−1)(q−1)/4.
Části (a),(c) nyní dávají přesně zákon kvadratické reciprocity.
Stejnou rovnost lze nezávisle vidět rozdělením obdélníku
1<=k<=h,1<=r<q/2 přímkou r=kq/p, která neobsahuje mřížový bod.
Eisensteinův původní článek *Geometrischer Beweis des Fundamentaltheorems
für die quadratischen Reste*, Crelle 28 (1844), 246–248, byl přečten
z obrazů v `sources/eisenstein-geometric-reciprocity-1844.pdf`.
Na s. 246 používá sudé zbytky a převod parity; na s. 247 počítá
mřížové body v obdélníku. Citace tedy opravdu dokládá tuto myšlenku.
[Knihovní výřez](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0028/LOG_0027.pdf)
neobsahuje odkazovanou tabuli II; její obraz zde není prohlášen za ověřený.
Metadata téhož svazku evidují také jeho články o reciprocitě odvozené
z Gaussových vzorců, *Lois de réciprocité* a důkaz pro bikvadratické
zbytky. Toto ověřuje existenci dalších citovaných prací, nikoli
správnost všech jejich výsledků.

## Úlohy 48–50: další identity a charakterizace

48(a). Pro n>0 pišme m=qn+r, 0<=r<n. Obě strany jsou
q+[r>0]. Pro n<0 neplatí obecně, např. m=0,n=−1 dává 2 versus 0.
Vyloučení n=0 doplněné 14. května 2020 je nutné kvůli dělení.
(b) Pro libovolné celé n máme postupně

```text
floor((n+2−floor(n/25))/3)
 = ceil((n−floor(n/25))/3)
 = ceil(ceil(24n/25)/3)
 = ceil(8n/25)
 = floor((8n+24)/25).
```

První a poslední rovnost jsou (a) s kladným jmenovatelem;
prostřední užívá úlohu 35 a celočíselný posun stropu.

49. Důležitá oprava z 7. ledna 1998 požaduje **celočíselnou funkci**.
Bez ní je f(x)=x protipříklad. Při opraveném předpokladu platí
f(0)=f(f(0))=f(0)+f(0), tedy f(0)=0 a posuny dávají f(j)=j
pro celé j. Označme k=f(1/2). Jestliže k<=0, číslo N=1−2k
je kladné celé a druhý zákon s x=1/2,n=N dává
`k=f(f(1/2−k)/(1−2k))=f(0)=0`.
Pokud f(1/(n−1))=0, pak f(1/n)=0 plyne z druhého zákona
s x=1/(n−1) a násobkem n: vnitřní hodnota f(n/(n−1)) je 1.
Indukcí tedy f(1/n)=0 pro všechna n>=2.

Pro 1<m<n položme a=ceil(n/m), takže 0<=am−n<m.
Indukce podle m pro pevné n dává f(am/n)=1, a proto
`f(m/n)=f(f(am/n)/a)=f(1/a)=0`. Posuny pokryjí všechna
racionální čísla a f se na nich rovná podlaze.
Jestliže k>0, funkce g(x)=−f(−x) splňuje stejné zákony
a g(1/2)=1−k<=0. Předchozí případ pak dává f(x)=ceil(x) na Q.

Rozšíření na všechna reálná x neplyne. Na bázi R jako vektorového
prostoru nad Q obsahující 1 a sqrt(2) zvolme Q-lineární h s h(1)=1,
h(sqrt(2))=0; ostatní bázové hodnoty lze zvolit libovolně.
Potom f=floor∘h má posunový zákon a druhý zákon díky
`floor(floor(nt)/n)=floor(t)`. Ale f(sqrt(2))=0, což není
podlaha ani strop sqrt(2). Existence takové báze používá výběr;
nejde o explicitně vypočitatelnou funkci na všech reálných číslech.
Navíc graf h obsahuje všechny body `(a+b sqrt(2),a)` pro a,b∈Q.
Invertibilní lineární zobrazení převádí hustou množinu Q² na tuto
hustou podmnožinu roviny. Proto je h neomezená na každém otevřeném
intervalu. To výslovně dokládá i knižní poznámku o neomezenosti.

Hamelův článek *Eine Basis aller Zahlen und die unstetigen Lösungen
der Funktionalgleichung: f(x+y)=f(x)+f(y)*, Math. Annalen 60 (1905),
459–462, byl přečten v původních obrazech. Konstrukce báze a aditivních
funkcí je na s. 459–461; hustota grafu je dokončena na s. 462.
[Výřez GDZ](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0060/LOG_0047.pdf)
chybně končí už na s. 461; poslední stránka je doplněna z
[obrazu celého svazku](https://gdz.sub.uni-goettingen.de/content/PPN235181684_0060/1000/0/00000480.jpg)
v `sources/hamel-1905-p462.jpg`. Jde o mez digitálního výřezu,
nikoli chybu Knuthovy citace. Datace rukopisu listopadem 1904 není
v rozporu s vydáním svazku 1905.
Citace Eisele–Hadeler 1990 zůstává zdrojově otevřená: vydavatelská
metadata potvrzují článek na s. 466–477, kniha odkazuje na jeho
podrozsah 475–477, ale tento text nebyl získán.

50 (přidáno 2021). Čísla 3142 a 3143 mají obě floor(n/pi)=1000,
zatímco ceil(1000pi)=3142; obousměrnost je tedy nepravdivá.
Přesné racionální meze pro pi již byly certifikovány v
`results/elementary-constants.json`; postačuje např. 3.14159<pi<3.14160.
Obecně pro beta>=1 z ceil(m beta)=n plyne
`m<=n/beta<m+1/beta<=m+1`, a tedy floor(n/beta)=m.
Pro 0<beta<=1 z floor(n/beta)=m plyne
`m beta<=n<(m+1)beta<=m beta+1`, což vynutí ceil(m beta)=n.
Oba důkazy platí pro všechna celá m,n včetně záporných.

## Rozsah výpočtu, errat a zbývajících pramenů

Jediný běh `check_integer_functions.py` skončil úspěšně; přesné počty
jsou v `results/integer-functions.json`. Používá jen celá čísla a zlomky.
Vedle přímých kontrol číselných identit porovnává celé vektory
koeficientů obecné reciprocity pro 11 776 kombinací parametrů,
takže pro každou z nich kontroluje libovolnou funkci f současně.
Konečný výčet doplňuje obecné důkazy; analytický výsledek úlohy 40
je doložen zvlášť, nikoli numerickým experimentem. Úlohy 37–38
nebyly znovu počítány.

Prohledány všechny čtyři časové vrstvy `all1-prepre`, `all1-pre`,
`all1`, `err1` a aktuální originál `err1.textxt`, stav 1. listopadu 2026.
Významové opravy 45,47,48,49 a Fourierovy exponenciály v odpovědi 40
jsou odděleně evidované známé chyby. Redakční opravy zahrnují smazání
„both“ na s. 39 (1999), interpunkci zákona A (2000), kurzivu v úloze 6
a chybějící závorku úlohy 21 (1997), „i“→„is“ v odpovědi 34 (1997)
a sazbu podmínky součtu v odpovědi 42 (2005). Dodatečné vysvětlení
kongruence z 2025, odpověď 4 z 2013 a doplnění odpovědi 7 z 2005
byly ověřeny výše. Nový nález tento blok nepotvrdil.

Otevřené prameny: Iversonova notace a Fermatovo historické datum
v hlavním textu; Busche a Hermite v odpovědi 38; Mordell v odpovědi
40; Eisele–Hadeler v odpovědi 49. Dřívější `checked` u úlohy 38
vyjadřovalo hotový matematický důkaz. Úplná mapa je nyní zpřesněna
na `partial`, dokud se neověří také její citace; důkaz se nezpochybňuje.
