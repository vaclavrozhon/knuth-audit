# Strana 65: distributivita přímo z axiomů mediánu

Checkpoint X0092, P0864–P0876. Originál p65/file82 v
`proof-file082.png`; zadání 71/72/74/76 na p89–90/file106–107,
odpovědi p547–548/file564–565 v `proof-median-answer-1/2.png`.
Níže je ověřen obecný algebraický důkaz, nikoli kontrola pouze
booleovského modelu. Nepoužívá se program, enumerace, princip
0/1 ani předem předpokládaná distributivita.

Pro nejobtížnější vazbu byl přečten a rozvinut
[primární algebraický důkaz zveřejněný Veroffem a McCunem](https://www.cs.unm.edu/~veroff/MEDIAN_ALGEBRA/knuth_proof.html).
Lokální zdroj a metadata: `sources/median-distributivity-hand-proof.html`
a `.json`. Žádný původní běh Otter/Prover9 se neopakoval.

## Přesné předpoklady a pomocný binární zápis — P0864

Operace m:M³→M splňuje právě (50)–(52):

    m(a,a,b)=a;
    m je invariantní při všech permutacích tří argumentů;
    m(a,r,m(b,r,c))=m(m(a,r,b),r,c).

Pro pevné r zaveďme a *_r b=m(a,r,b). Je to asociativní,
komutativní a idempotentní binární operace přímo podle těchto
tří axiomů. Všechny níže prováděné změny závorkování se týkají
**jednoho pevného r**; různé středy se nesmějí libovolně míchat.

Booleovský medián axiomy splňuje: při r=0 je *_r konjunkce,
při r=1 disjunkce, takže obě potřebné asociativity platí.
Majorita a všech šest permutací byly doloženy v P0821.
Další důkaz je platný v každém M, bez konečnosti, uspořádání
nebo číselných souřadnic. V jednoprvkovém M platí všechny identity;
pro prázdné M jsou univerzální identity vakuózní a žádný interval
s konci u,v se nezadává.

## Absorpce (55) a oba vytištěné zvláštní případy — P0865

Pouze asociativita se středem b dává

    m(m(a,b,c),b,c)=m(a,b,m(c,b,c))=m(a,b,c).            (A)

Poslední rovnost je většinový axiom. To je přesně (55).
Dosazení y=u,z=v v (53) redukuje pravou stranu na m(x,y,z),
a levou stranu na tutéž hodnotu podle (A). Pro (54) se pravá
strana v tomto dosazení rovněž zredukuje pomocí (A).

Dosazení u=y v (53) dává

    m(m(x,y,z),y,v)=m(x,y,m(z,y,v)),

tedy právě (52). Pro druhý vytištěný zvláštní případ x=u
položme q=m(y,u,v). Potom

    m(m(u,y,z),u,v)
      =m(m(v,u,y),u,z)=m(q,u,z)
      =m(m(q,u,v),u,z)=m(q,u,m(v,u,z))
      =m(u,m(y,u,v),m(z,u,v)).

První a čtvrtá rovnost používají asociativitu se středem u,
vložení m(q,u,v)=q je (A); ostatní jsou permutace. Tím je
zkontrolován celý řetězec přímo na p65, bez užití obecného (53).

## Klíčová absorpce projekce — P0866

Pro libovolné x,u,v,z položme t=m(x,u,v), q=m(z,u,v).
Dokážeme

    m(x,t,q)=t.                                        (B)

Úplný řetězec s vyznačenými středy je

    m(x,t,q)
      =m(m(t,x,v),x,q)                    podle (A)
      =m(t,x,m(v,x,q))                    asociativita, střed x
      =m(t,x,m(t,v,z))                    asociativita, střed v
      =m(m(x,t,v),t,z)                    asociativita, střed t
      =m(t,t,z)=t.                        (A), potom majorita

Třetí řádek používá přesně

    m(v,x,m(z,u,v))=m(x,v,m(u,v,z))
                  =m(m(x,v,u),v,z)=m(t,v,z).

Žádná z těchto rovností nepředpokládá distributivitu.

## Jednoznačný společný medián; úloha 74 — P0867

Nechť w=m(w,x,y)=m(w,x,z)=m(w,y,z), a t=m(x,y,z).
Potom

    w=m(y,x,w)=m(y,x,m(z,x,w))
     =m(m(y,x,z),x,w)=m(t,x,m(w,y,z))=t.

Třetí rovnost je asociativita se středem x, poslední je (B)
s prvním argumentem x a společnými parametry y,z. Použity
jsou jen tři uvedené předpoklady o w. Naopak (A) zaručuje,
že t sám všechny tři rovnosti splňuje. Průnik tří intervalů
má proto právě tento jediný bod, jakmile intervaly ztotožníme
s pevnými body v P0872.

To řeší celou 74. Vytištěný řetězec odpovědi je také platný:
tři počáteční dosazení nahrazují w jeho třemi danými mediány,
potom se použije asociativita se středem x. Poslední krok
je zvláštní případ (53), který je nezávisle dokázán níže;
(B) ukazuje, že tento poslední krok dokonce obecné (53) nepotřebuje.

## Tři projekce proti dvěma — P0868

Fixujme u,v a pišme p(s)=m(s,u,v). Pro a=p(x), b=p(y), c=p(z)
ukážeme identitu

    m(a,b,c)=m(x,b,c).                                 (E)

Z (B) máme a *_x b=a a a *_x c=a. Položme e=a *_x c
a d=m(x,b,c). Potom

    m(a,b,c)
      =m((a *_x b) *_x c,b,c)
      =m((a *_x c) *_x b,b,c)
      =m(m(e,b,x),b,c)
      =m(e,b,m(x,b,c))=m(e,b,d)=d.

První vložení používá obě rovnosti z (B); přeskupení má jediný
střed x a další přeskupení jediný střed b. Poslední rovnost je
nové použití (B), tentokrát s prvním argumentem b, společnými
parametry x,c a posledním vstupem a: d=m(b,x,c), e=m(a,x,c).
Identita (E) zatím **neobsahuje** p(m(x,y,z)); nejde tedy o
kruhové předpokládání distributivního zákona.

## Přenos dvou proměnných — P0869

Ze stejného (B) plyne b=m(y,b,c). Asociativita se středem c dává

    m(x,b,c)=m(x,m(y,b,c),c)
            =m(m(x,y,c),b,c).                         (F)

Toto platí pro b=p(y),c=p(z) a libovolné x.

## Pomocná vazba pro obraz mediánu — P0870

Nechť t=m(x,y,z), a=p(t), b=p(y), h=m(x,y,a). Použitím (F)
na x a dvojici p(y),p(t) dostaneme m(a,x,b)=m(h,a,b).
Z (B) se společnými parametry x,y plyne m(a,h,t)=h;
z (B) se společnými parametry u,v plyne m(t,a,b)=a. Tudíž

    m(a,x,b)=m(h,a,b)=m(m(h,a,t),a,b)
            =m(h,a,m(t,a,b))=m(h,a,a)=a.              (G)

Jediné přeskupení v řetězci má střed a. Toto je přesný
pomocný zákon, nikoli tvrzení, že p zachovává libovolný medián.

## Krátká i dlouhá distributivita; úloha 71 — P0871

Opět t=m(x,y,z), a=p(t), b=p(y), c=p(z). Z (G) a permutace
y/z máme m(a,x,b)=a a m(a,x,c)=a. Identita (E), nyní pro
trojici vstupů y,t,z, dává

    m(a,b,c)=m(y,a,c)=a,

kde poslední rovnost je (G) s prvním vstupem y a druhým z.
Podle již dokázané jednoznačnosti P0867 je proto a medián
trojice x,b,c. Dostáváme přesně

    p(m(x,y,z))=m(x,p(y),p(z)),                        (53)

a (E) současně dává i dlouhou formu (54).

Pro přesné zadání 71 lze dlouhou formu z krátké odvodit ještě
přímo řetězcem vytištěné odpovědi. Z (A) máme p(p(s))=p(s), takže

    p(m(x,y,z))
      =p(p(m(x,y,z)))
      =p(m(p(y),x,p(z)))
      =m(p(y),p(x),p(p(z)))
      =m(p(x),p(y),p(z)).

Druhý a třetí krok jsou (53), poslední idempotence p a permutace.
Tím je 71 dokázána v požadované implikační podobě. Celý obecný
důkaz (53) výše má závislosti A→B→(jednoznačnost,E,F)→G→(53);
nikde nevyužívá závěr jako předpoklad.

## Definice ideálu, interval a celé Lemma M — P0872

Definice ideálu vyžaduje uzavřenost m(a,b,z) pro a,b∈C a z∈M;
nevyžaduje, aby do C patřily jen dvě určité hodnoty. Interval
[u..v] je obraz mapy p(s)=m(s,u,v). Obsahuje u=p(u),v=p(v)
podle majority a je symetrický v koncích podle komutativity.

Z (A) plyne p(p(s))=p(s). Každý bod obrazu je tedy pevný bod p;
obráceně každý pevný bod x=p(x) do obrazu patří sám za sebe.
To dokazuje oba směry x∈[u..v] ⇔ x=m(u,x,v).

Pro libovolné a=p(s), b=p(t) a z∈M dává (53), s prvním
argumentem z,

    m(a,b,z)=m(z,p(s),p(t))=p(m(z,s,t))∈[u..v].

Tím je dokázána ideálová uzavřenost pro **každý** třetí argument,
nikoli jen pro z v intervalu. To je přesně rovnost v důkazu knihy.

## Vlastnost (58); první část 72 — P0873

Každý bod obrazu [u..u] je m(s,u,u)=u, a u v něm skutečně je.
Proto [u..u]={u}; v∈[u..u] implikuje v=u. To ověřuje
implikaci i její následný množinový přepis na p65.

## Vlastnost (59); druhá část 72 — P0874

Z předpokladů x=m(u,x,v), y=m(u,y,x) dostaneme

    m(u,y,v)=m(v,u,m(x,u,y))
            =m(m(v,u,x),u,y)=m(x,u,y)=y.

Použita jen asociativita se středem u a oba předpoklady.
Tedy y∈[u..v]. Kvantifikace přes všechna taková y dává přesně
[u..x]⊆[u..v], pokud x∈[u..v].

## Vlastnost (60); třetí část 72 — P0875

Je-li x=m(x,u,v), y=m(y,u,z)=m(y,v,z), pak (53) dává

    m(x,y,z)=m(m(x,u,v),y,z)
            =m(x,m(u,y,z),m(v,y,z))=m(x,y,y)=y.

Proto y∈[x..z]. Pro pevné x∈[u..v] jde přesně o množinové
tvrzení [u..z]∩[v..z]⊆[x..z] pro každé z, vytištěné dole.
Všechny tři části odpovědi 72 jsou tedy jednotlivě ověřeny.

## Úloha 76 bez distributivity — P0876

Definujme [uxv] právě rovností x=m(u,x,v). Pro axiom (i)
[uvu] je v=m(u,v,u)=u. Pro axiom (ii), předpoklady [uxv]
a [xyu], je y=m(x,y,u), x=m(u,x,v); tentýž řetězec jako
P0874 dává y=m(v,y,u), tedy [vyu]. Tento řetězec nepoužívá (53).

Pro axiom (iii) je t=m(x,y,z) mezi každou dvojicí x,y,z
podle (A). Jednoznačnost přesně dokazuje P0867, který používá
jen (A)/(B), nikoli distributivitu. Proto jsou všechny tři
betweenness axiomy odvozeny z (50)–(52), jak zadání vyžaduje.
Rovnost, kterou rozepisuje odpověď 76, je právě (B) s parametry
y,z a vstupem w; každý její krok je výše doložen s pevným středem.

## Úplná mapa p65 a bibliografické meze

| obsah stránky | odpovídající argument |
|---|---|
| definice tří axiomů, booleovská asociativita | P0864 |
| obecné implikace (53)/(54) z právě těchto axiomů | P0866–P0871 |
| (55), případ y=u,z=v, specializace y=u a řetězec x=u | P0865 |
| definice ideálu/intervalu, oba konce a oba směry pevného bodu | P0872 |
| celý důkaz Lemma M | P0872 |
| (58), (59), (60) a všechny množinové přepisy | P0873–P0875 |

Matematický rozsah p65/file82 je úplný. Navazující úlohy
71,72,74,76 mají již nyní přesné argumenty a později se
neopakují. Samostatná 75 o **abstraktně zadané** relaci
mezi body zůstává k ověření; není použita jako skrytý vstup
do výše uvedeného algebraického důkazu.

Dne 2026-11-07 prohledány `all4a-pre`, `all4a`, `err4a`,
`all4f0`, `all4f1` podle stran 65/66/547/548, čísel 71–76
a témat median/Sholander/Kolibiar. Relevantní oprava tohoto
matematického bloku nenalezena. F0 p195/answer76 se týká
pozdějšího algoritmu a změny nákladového výrazu, nikoli této
úlohy; F1 p162/answer75 patří bitovým operacím.

Primární web Veroffa/McCuna potvrzuje mechanický důkaz v roce
2005 i uvedené axiomy; jeho algebraické kroky jsou zde skutečně
zkontrolovány. Starší přisouzení jednotlivých objevů Birkhoffovi,
Kissovi, Kolibiarovi/Marcisové a Sholanderovi se v tomto bloku
nezávisle nereprodukovalo. Hodnocení, že nebyl znám „simple proof“,
je historický úsudek o obtížnosti, nikoli formální negativní věta;
nejde o naši certifikaci všech důkazů existujících k roku 2011.
Tyto bibliografické meze zůstávají výslovné a nemění obecné
odvození matematiky uvedené výše.
