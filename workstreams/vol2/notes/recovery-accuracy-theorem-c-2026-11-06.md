# Obnova §4.2.2: celá věta C a celá úloha 20

7. listopadu 2026. Originály 236, 244 a 616 znovu porovnány
včetně všech neostrých znamének. Níže je každý krok důkazu
(47), obě nerovnosti i zlomková mez odpovědi 20 a přesná
nutná a postačující klasifikace. Bez nového nebo opakovaného běhu.

## Doména, nuly a přesný význam dvou operací

Použijeme již úplně dokázané A/B, normalizované vstupy,
nejbližší R s libovolným pevným výběrem půlek a předpoklad
definovaných operací. Ve větě C je b≤3 a |u|≥|v|.
Vlastní úloha 20 naopak dovolí libovolné b≥2 a hledá
všechny poruchy (47) při |u|≥|v|.

Nechť `w=R(u+v)`, `r=u+v−w` a `v'=R(w−u)`.
Jestliže je **w−u přesně representovatelné**, pak v'=w−u
a také R(u−w)=u−w=−v', bez předpokladu znaménkové
symetrie na nejednoznačných půlkách. Druhá operace kratší
korekce je proto

`R(R(u−w)+v)=R(v−v')=R(u+v−w)=R(r)=r`.

Poslední přesnost je již dokázaná (46). To je přesně
pravá korekce (47); vnější w+r je obyčejný přesný součet.
Tištěný řetězec v důkazu přes v⊖v' i zápis skutečné
korekce přes u⊖w jsou tedy zvlášť zdůvodněny.

Pokud v=0, je w=u a korekce je 0. Pokud u=0, velikostní
podmínka nutí také v=0. Je-li w=0, u+v=0 a korekce
R(R(u)+v)=0. Žádný z těchto případů nemůže být poruchou.

Po známém w je výpočet `a=u⊖w`, `r=a⊕v` právě
dvě plovoucí operace. Jedno porovnání absolutních hodnot
vybere pořadí operandů tak, aby |u|≥|v|; porovnání
normalizovaných kódů je pevné porovnání exponentu a zlomku,
nikoli další zaokrouhlený aritmetický výpočet. Samotný
výpočet w je jedna předchozí operace navíc.

## Každý tištěný krok věty C

Pro nenulový w změňme jednotku jako v A/B tak, aby e_w=p,
a absorbujme excess do exponentů. Přenesení libovolného
pravidla půlek při této změně je již dokázané v obnově A.
Pak w je celé a |r|≤1/2. Normalizace dává z |u|≥|v|
také e_u≥e_v. Důkaz skutečně funguje pro tuto slabší
exponentovou podmínku, jak uvádí text.

**Větev e_u≥p.** Hodnota u je celé číslo; w je rovněž
celé. Proto `r=u+v−w≡v (mod 1)` a |r|≤1/2, takže
r je ocas v. Lemma T dává

`v'=R(w−u)=R(v−r)=v−r=w−u`.

První vnitřní rovnost je w−u=v−r, druhá je právě
přesné odečtení ocasu. Následně celý korekční řetězec
z předchozího oddílu dává (47). Tato větev funguje
pro **každý** základ b, nikoli pouze b≤3.

**Větev e_u<p.** Z e_v≤e_u a exponentu w=p nutně
e_u=p−1. Úplný argument z obnovy B lze převzít ve stejném
rozsahu: kdyby oba exponenty byly ≤p−2, pak
`|u+v|≤2(b^p−1)/b²≤b^(p−1)−1/b`; poslední mez
je representovatelná a její zaokrouhlení nemůže dát w
s velikostí alespoň b^(p−1). Není k tomu třeba hypotéza
blízkých exponentů; v B byla použita až v dalším kroku.

Položme B=b^(p−1), N=b^p. Hodnota u je násobek 1/b
a w celé, takže w−u je násobek 1/b. Takový násobek
je přesně representovatelný, pokud
`|w−u|<B+1/b`: po vynásobení b je jeho celočíselný
obsah velikosti menší než N+1, tedy nejvýše N.
Pod N má nejvýše p cifer a krajní N je mocnina b.
To dokazuje vytištěnou podmínku přesnosti, včetně kraje B.

Každý krok následujícího odhadu je:

1. `|w−u|≤|w−u−v|+|v|` trojúhelníkovou nerovností.
2. `|w−u−v|=|r|≤1/2`.
3. e_v≤p−1 dává `|v|≤(N−1)/b=B−1/b`, včetně
   největšího representovatelného zlomku v tomto pásmu.
4. Tedy `|w−u|≤1/2+B−1/b`.
5. Pro b≤3 platí `1/2<2/b`, a proto
   `1/2+B−1/b<B+1/b`, přesně vytištěné ostré zakončení.

Výsledný rozdíl je tedy representovatelný, korekce je r
a (47) platí. Pro b=4 je poslední porovnání pouze rovnost;
text proto správně potřebuje odlišný argument pro případné
další základy. Žádný krok pro b=2,3 nevybral konkrétní půlku.

## Úloha 20: obě počáteční nerovnosti a mez zlomků

Úloha hledá všechny poruchy, nikoli jen jeden příklad.
Stále používejme měřítko e_w=p pro tento oddíl a |u|≥|v|.
Předchozí větev e_u≥p funguje pro každý b, takže případná
porucha vyžaduje e_u=p−1 a e_v≤p−1. V rozdílu w−u,
který je násobek 1/b, by při velikosti <B+1/b nenastala
porucha. Nutně tedy platí přesně vytištěný řetězec

`|v|+1/2 ≥ |w−u| ≥ B+1/b`.

První neostrá nerovnost je tentýž trojúhelníkový odhad;
druhá je nutná podmínka nerepresentovatelnosti rozdílu.
Neříká se, že každá hodnota nad touto mezí nutně selže.

Odtud `|v|≥B−1/2+1/b`. Tato mez je větší než B/b:
`B(1−1/b)−1/2+1/b≥1/2>0`, protože B≥1.
Proto e_v nemůže být menší než p−1. Oba vstupy tedy mají
**stejný exponent p−1**. Jejich zlomky jsou |u|/B a |v|/B,
a velikostní pořadí nyní skutečně dává |f_u|≥|f_v|.
Po vydělení dolní meze pro |v| hodnotou B dostáváme

`|f_u|≥|f_v|≥1−(b/2−1)b^(−p)`.

To ověřuje každý znak i faktor vytištěné následné meze.
Stejný exponent nebyl tiše odvozen jen z pořadí hodnot.

## Přesná klasifikace mimo možné přetečení zlomku

Pro celý důkaz změňme nyní měřítko na e_u=p, takže
`B≤|u|<N` a |u| je celé; nejde o stejné měřítko jako
v předchozím oddíle. Jestliže e_w≤e_u, už dokázaná
první větev C (po vhodném přeznačení) dává přesnost
w−u a platnost (47) pro libovolné b.

Při opačných znaménkách je `|u+v|≤|u|`; neklesání R
a přesnost obou konců ±|u| vynucují také `|w|≤|u|`.
Proto zde e_w≤e_u a porucha nemůže nastat.

Zbývají stejná nenulová znaménka a přenos součtu do vyššího
pásma. Zrcadlením přenesme případné záporné pravidlo na
kladné hodnoty; dále tedy u≥v>0. Předchozí argument o
největším exponentu zaručuje e_w≤e_u+1; v této větvi
má w krok b a `N≤w≤2N`. Horní mez používá u+v<2N
a representovatelnost 2N; je platná i v binárním kraji,
kde w=2N ve skutečnosti nemůže nastat.

Je-li w<2N, je jako násobek b nejvýše 2N−b.
Protože chyba zaokrouhlení je nejvýše b/2, máme
`u+v≥w−b/2`. Podmínka u≥v dává
`u≥w/2−b/4`, a tedy

`0<w−u≤w/2+b/4≤N−b/4<N`.

Rozdíl je celé číslo s nejvýše p ciframi, takže korekce
je opět přesná. Jediná zbývající možnost poruchy je
**w=2N**. Tím je nutnost konkrétního horního zaokrouhlení
odvozena, nikoli jen přečtena z odpovědi.

## Kdy přesně w=2N nastane a proč vždy způsobí chybu

Pokud by v mělo nižší exponent než u, pak
`u+v≤(N−1)(1+1/b)`. Aby se součet zaokrouhlil na 2N,
musel by ležet alespoň na půlce `2N−b/2` mezi 2N−b a 2N.
To není možné, protože

`2N−b/2−(N−1)(1+1/b)
 = N(1−1/b)+1+1/b−b/2 ≥ b/2+1/b>0`.

Nutně tedy i v má exponent p. Pišme
`u=N−j`, `v=N−k`, kde j,k jsou celá,
`1≤j≤k` a oba vstupy patří do [B,N).
Přesný součet je `2N−(j+k)`. Platí

`w=2N ⇔ j+k<b/2`,
nebo `j+k=b/2` a konkrétní pravidlo zvolí horní půlku 2N.

Při takové volbě `j≤(j+k)/2≤b/4<b/2`.
Vnitřní rozdíl u−w je −N−j. Nejbližší hodnota je
**jednoznačně −N**: vzdálenost j je menší než b−j
k dalšímu sousedu −N−b, a každý soused směrem k nule
je ještě dál než −N. První korekční operace tedy ztratí j.
Druhá operace má přesný výsledek
`−N+v=−k`, representovatelný malý celý vstup.
Vypočtená korekce je −k, zatímco pravá korekce je −j−k.
Rozdíl j≥1 se už nemůže opravit a (47) vždy selže.

To prokazuje současně nutnost i dostatečnost. Po obnovení
obecného měřítka a znaménka je úplná odpověď:

Existuje celočíselná mocnina `λ=b^a>0` a znaménko σ∈{−1,1}, že

`u=σλ(N−j)`, `v=σλ(N−k)`, `1≤j≤k`,

a `j+k<b/2`, nebo `j+k=b/2` s výběrem
`R(σλ(2N−j−k))=σλ2N`. Všechny potřebné výsledky
musejí být v povoleném exponentovém rozsahu. Pak vypočtená
pravá strana (47) minus skutečný součet je σλj.
Pokud žádná taková reprezentace a skutečná půlková volba
neexistuje, (47) platí. Pro asymetrické pravidlo je půlková
podmínka výslovně vztažena ke skutečnému znaménku σ.

## Konvence N5, malé základy a přesné příklady

Protože j+k≥2, pro b=2,3 nemůže nastat ani jedna větev:
to potvrzuje větu C druhým, obecnějším argumentem.
Pro b=4 zbývá jedině j=k=1 a horní půlka. Doporučené
N5 ale zaokrouhluje na lichou poslední cifru; horní
ciferný obsah `2N/b=2b^(p−1)` je sudý, takže vybere
dolní možnost. V tomto konkrétním pravidle tedy funguje
(47) i pro b=4. Při pravidle na sudé může selhat.

Pro b≥5 funguje j=k=1 mimo půlku, protože 2<b/2:
už u=v=N−1 dává poruchu bez ohledu na volbu půlek.
Obecně v sudém základu na hranici j+k=b/2 volí N5
horní sudý obsah právě tehdy, když b/2 je liché
(b≡2 modulo4); při b/2 sudém jej odmítá.

| Formát a pravidlo | w | R(u−w) | kratší korekce | přesný součet a pravá strana (47) |
| --- | --- | --- | --- | --- |
| b=4,p=1,u=v=3, půlky na sudé | 8 z půlky mezi 4 a 8 | −4, nejbližší k −5 | −1 přesně | 6 proti 7: porucha |
| b=4,p=1,u=v=3, N5 na liché | 4 | −1 přesně | 2 přesně | 6 proti 6: platí |
| b=5,p=1,u=v=4 | 10, vzdálenost2 oproti3 k5 | −5, nejbližší k−6 | −1 přesně | 8 proti9: porucha |

Každá z uvedených hodnot je p-ciferná v příslušném
základu; exponentový rozsah zvolíme tak, aby zahrnul
tyto operace. Tabulka je ruční aritmetický důkaz, ne nový běh.

## Výklad poslední věty odpovědi a zdrojový rozsah

„Zlomek zaokrouhlený na 2“ se vztahuje k dočasnému
nenormalizovanému součtu zlomků před přenosem. Nejde
o uložený normalizovaný zlomek velikosti 2: po posunu
doprava se ukládá právě 2/b. V celočíselném měřítku
výše je to přesně událost w=2N, a proto má poslední
věta odpovědi doložený nutný i postačující význam.

Hodnocení „velmi vzácný případ“ nemá uvedenou distribuci
operandů; neověřuje se jako pravděpodobnostní věta.
Při cíleně zvolených datech výše nastává pokaždé. Autorství
S. Linnainmaa je přečtený kredit knihy; samostatný primární
pramen autorství nebyl získán a tento bod je výslovně vynechán.
Všechny čtyři vrstvy errat i aktuální TeX byly zkontrolovány;
pro C ani odpověď20 nebyla nalezena relevantní oprava.
Celá matematická klasifikace úlohy20 a věta C jsou uzavřeny.
Tvrzení o libovolných půlkách ve větách A–C nyní má doložený
rozsah; širší věta D a ostatní zaokrouhlovací tvrzení následují.
