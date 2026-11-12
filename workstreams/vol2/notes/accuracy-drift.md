# §4.2.2 TheoremD: úplný důkaz a jednobitová lichá výjimka

Cílem je identita h(h(u))=h(u), kde
h(u)=R(R(u+v)−v), v je pevné plovoucí číslo aR zaokrouhluje
na nejbližší číslo v základu b s p ciframi. Všechny mezivýsledky
jsou v rozsahu exponentů. Pro sudý b se přesné poloviny vybírají
podle pevné parity poslední cifry **před** normalizací přenosu.
Pro lichý b nemohou poloviny v tomto výpočtu nastat: součty a
rozdíly konečných b-adických čísel mají jmenovatel mocninu b,
zato přesná polovina sousedních hodnot by přidala faktor2.

Důkaz pokrývá sudé i liché poloviny. Jediná výjimka je b2,p1,
liché poloviny, u≠0 a v=u/4; tam skutečně h(u)=u/2 a h²(u)=u/4.
Doporučené pravidlo AlgoritmuN tuto binární výjimku neobsahuje,
protože v b2 používá sudé poloviny. Rozšíření na liché vyžaduje
opravuC0085. Původní strany236–237 a217 byly vizuálně přečteny;
čtyři vrstvy errat zkontrolovány. Následuje vlastní důkaz,
nikoli tvrzení o přečtení nedostupného článku Reiser–Knuth1975.

## 1. Základní redukce

Pišme w=R(u+v), z=R(w−v), w2=R(z+v), z2=R(w2−v).
Chceme z2=z. Pokud z=u, závěr je okamžitý determinismem.
Nulové vstupy jsou rovněž okamžité. Změna obou znamének mění
všechny výsledky pouze znaménkem; škálování mocninou b je přesné.

Nejprve předpokládejme |v|>=|u|. Důkaz TheoremC a charakterizace
úlohy20 v `accuracy-exact.md` ukazují, že w−v je přesně
reprezentovatelné, s jedinou možnou výjimkou popsanou dále.
V přesném případě z=w−v, a tedy z+v=w přesně; ihned z2=z.

Ve výjimečném případě mají oba vstupy stejné znaménko a po
škálování jsou kladné celé U=N−j,V=N−k, kde N=b^p,
1<=k<=j a j+k<=b/2; zaokrouhlený součet je w=2N.
Proto k<=b/4 a R(w−v)=R(N+k)=N jednoznačně. Následující
R(N+v)=R(2N−k)=2N opět jednoznačně, takže z2=z i zde.

Dále tedy u>|v| a u>0. Pro v<0 a |v|>=u/2 je u+v přesné
podle Sterbenzovy vlastnosti; následné přičtení−v vrátí přesněu.
Stačí řešit v>0 nebo −u/2<v<0. Nastavme měřítko tak,
aby u bylo celé v[B,N), kde B=b^(p−1), N=b^p.

V této situaci zůstává w kladné a leží v[B/b,2N]. Pro záporné v
je přesný součet větší než u/2>=B/b; krajB/b je reprezentovatelný.
Pro kladné v je součet menší2N a kraj2N je opět reprezentovatelný.
Sousední exponentová pásma mají v těchto jednotkách kroky
1/b podB, 1 meziB aN a b nadN. Binární součet nemůže dosáhnout2N:
oba vstupy jsou nejvýšeN−1 a také2N−2 je reprezentovatelné. U ostatních
základů leží2N ještě v témže horním pásmu. V následujícím textu
r=w−(u+v) značí znaménkovou chybu prvního zaokrouhlení.

## 2. Hrubší pásmo: w>=N

Tato situace vyžaduje v>0. Máme |r|<=b/2 a x=w−v=u+r
splňuje x<=N−1+b/2. Také x>=B. Kdyby x<B, pak
v=w−x>N−B>=B; v by bylo celé a u>=N−B+1. Odtud
x>=N−B+1−b/2>=B pro b>=2,B>=1, spor.
Proto z=R(x) je celé v[B,N].

Je-li z=N, pak N−1/2<=x<=N−1+b/2. Rozdíl
(z+v)−w=N−x tedy leží mezi−b/2+1 a1/2, striktně uvnitř
poloviny hrubého kroku. Pro w>N z toho plyne w2=w.
Pro w=N je z+v=N+v>N a v<=1/2, takže stejný závěr platí
na pravé straně hranice. Vždy z2=z.

Je-li z<N, pak τ=z−x splňuje |τ|<=1/2. Máme z+v=w+τ.
Pro w>N je opět w2=w, protože1/2<b/2. Pro w=N je jediná
zbývající možnost w2≠w přesná dolní polovina τ=−1/2
s lichou volbou; potom w2=N−1.

V této výjimce x=z+1/2, z je liché a
v=N−z−1/2. Jelikož v není celé, musí v<B, tedy z>=N−B.
Nemůže z=B: to by vyžadovalo b2 a lichéB, tedy p1,
ale u=1,v=1/2 se při lichém pravidle nezaokrouhlí na w=N=2.
Proto B<z<N a R(z−1/2)=z díky liché paritě. Jelikož
w2−v=z−1/2, je z2=z i při této změně w2≠w.

## 3. Stejné pásmo: B<=w<N a u+r>=B

Zde |r|<=1/2 a z je nejbližší celé k u+r; i krajníN je
přípustná. Pokud z≠u, nutně r=±1/2 a z−u=2r.
První zaokrouhlení i zaokrouhlení zpět zvolily požadovanou paritu,
takže w i z mají tuto paritu. Potom

```text
z+v = w+r.
```

Pro B<w<N zaokrouhlení w+r znovu vybere w. To platí i při
horní polovině sousedící sN: vybraná parita w ji vrací zpět.
Tedy w2=w a z2=z.

Zbývá w=B. Hodnota r=+1/2 by znamenala, že se B−1/2
zaokrouhlilo naB. To není možné, protože levý krok uB je1/b,
nikoli1. Proto r=−1/2, z=u−1 a
w2=R(B−1/2)=B−1/2 přesně: při sudém b je tato hodnota na
jemné síti1/b, při lichém b zde nemůže nastat první polovina.
Následné w2−v=u−1=z je přesné. Znovu z2=z.

## 4. Dolní hrana zpětného kroku: B<=w<N a u+r<B

Protože u je celé a |r|<=1/2, musí u=B a r<0.
Zároveň v>0: pro záporné v a w>=B bychom měli w=B a r=−v>0.
Pišme w=B+j, v=j+t s j>=0 celé a0<t<=1/2.
Pak z=R(B−t)=B−k/b pro celé k>=0. Při k0 je z=u,
takže předpokládejme k>=1. Je k<=floor(b/2); v lichém základu
je t<1/2, neboť t je b-adické, což vylučuje horní lichou polovinu.

Položme δ=k/b−t. Nejbližší zaokrouhlení dává
|δ|<=1/(2b) a z+v=w−δ. Pro w>B je proto w2=w.
Pro w=B je w2=w, ledaže δ=1/(2b) a zvolíme lichou
polovinu podB; pak w2=B−1/b.

V tomto posledním případě j0, t=(k−1/2)/b a k je liché:
vnitřní zaokrouhlení na z vybralo significand N−k, tedy lichý.
Následný přesný rozdíl je

```text
w2−v = B−(k+1/2)/b = z−1/(2b).
```

Je-li z>B/b, leží tato polovina na jemné síti1/b a lichá
parita z opět vrátí z. Dolní kraj z=B/b by vyžadoval
k=(b−1)B<=b/2. To je možné jedině b2,B1,p1,k1.
Pak u1,v1/4,z1/2,w2=1/2 a z2=1/4. To je právěC0085.
Po obnovení měřítka a znaménka jde o v=u/4.

## 5. Jemnější pásmo prvního součtu: w<B

Zde v<0, |v|<u/2 a |r|<=1/(2b). Pokud u>B, je zpětné
zaokrouhlení z=R(u+r)=u jednoznačné. Pro u=B platí totéž,
s jedinou možností r=−1/(2b) a lichou volbou, která dává
z=B−1/b.

Pišme w=B−k/b. V této možnosti
v=−(k−1/2)/b a k je liché, protože w bylo vybráno lichou
polovinou. Potom z+v=w−1/(2b). Je-li w>B/b, liché
zaokrouhlení vrátí w a zpětný krok vrátí z.

Je-li w=B/b, je k=(b−1)B. Podmínka |v|<B/2 implikuje
(b−2)B<1, tedy b2. Lichost k=B pak vyžaduje p1.
Zde jde o u1,v−1/4,w=z1/2. Následující w2=1/4,
ale z2=1/4+1/4=1/2=z přesně. Tento poslední hraniční
případ je tedy stabilní, na rozdíl od kladné výjimky předchozí části.

Tím jsou vyčerpány všechny možnosti. TheoremD pro doporučené
zaokrouhlování je dokázána; pro liché pravidlo chybí přesně
uvedená jednobitová výjimka.

## 6. Vazba na již dokončené kontroly

Předchozí `verify_accuracy_exact.py` již provedl150640 přesných
případůD včetně sudých i lichých variant pro sudé základy. Jediný
zaznamenaný neúspěch je b2,p1, liché poloviny,u1,v1/4.
Při doplnění tohoto důkazu se úspěšné běhy neopakovaly.

Nové malé průzkumné výpočty ukázaly, proč nelze důkaz zkrátit na
nepravdivý silnější předpoklad w2=w: například b2,p2,sudé poloviny,
u3,v−1/2 dávají w=2 a w2=3/2, ale z=z2=2. Analogicky v b4,p1
s lichými polovinami u1,v1/8 dává w1,z3/4,w2=3/4,z2=3/4.
Tyto příklady odpovídají rozlišení hraničních případů výše;
žádný další knižní nález nepřidávají.

Dodatečná kontrola nově použitých větví a mezikrokových nerovností
v `verify_accuracy_drift_proof.py` ověřila6 096 případů ve28 blocích,
včetně všech šesti větví důkazu. Výsledky jsou oddělené od původních
150640 kontrol finální identity. Všechny nové bloky prošly s exit0.
