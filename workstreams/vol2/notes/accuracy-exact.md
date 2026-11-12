# §4.2.2: přesné rozklady součtu

Obnova X0215–X0217 nyní porovnala každý skutečně tištěný mezikrok,
všechny nuly, půlky, exponentové větve a celé odpovědi11/12/20.
Podrobné argumenty jsou v `recovery-accuracy-theorem-a-2026-11-06.md`,
`recovery-accuracy-theorem-b-2026-11-06.md` a
`recovery-accuracy-theorem-c-2026-11-06.md`.
Ostatní starší souhrnné rozsahy níže se při obnově přebírají jen
podle individuální strukturované mapy; konečné testy se neopakují.

Kontrolované originály235–237, úlohy11,12,20,25 na243–245,
odpovědi614,616,617 vizuálně přečteny. Čtyři vrstvy errat prohledány;
větyA–C a odpovědi11,12,20 nemají relevantní opravu. Tato poznámka
zatím neuzavírá TheoremD: konečné kontroly nenahrazují jeho obecný důkaz.

Značení b,p,q,R,⊕,⊖ přebíráme z [základního bloku](accuracy-basic.md).
Změnou měřítka mocninou b lze brát q=0. Operace musejí zůstat
v povoleném rozsahu. Proměnná w=R(u+v) je vypočtený součet, zatímco
r=u+v−w je jeho přesná chyba. „Reprezentovatelné“ znamená, že R(x)=x.

## 1. Ocas čísla: Lemma T a úloha11

Ocasem x modulo b^e nazýváme t s x−t celočíselným násobkem b^e
a |t|<=b^e/2. V polovině mohou být dva ocasy. Pro reprezentovatelné x
jsou reprezentovatelné **jak t, tak x−t**. Stačí změnit znaménko
a měřítko, aby x bylo celé a0<=x<b^p.

Je-li e<=0, musí t=0. Pro0<e<=p je t celé, |t|<=b^e/2<b^p;
x−t má nejvýše p+1 cifer a alespoň e koncových nul, tedy nejvýše
p významných cifer. Pro e>p je |x|<b^p<=b^e/2, takže t=x a x−t=0.
To dává LemmaT: x⊖t=x−t. Pro slabší podmínku |t|<b^e z odpovědi
se při e>p může objevit i x−t=b^e; je opět reprezentovatelné.

## 2. Theorem A

Definujeme

```text
u'=R(w−v),  v'=R(w−u),
u''=R(w−v'), v''=R(w−u').
```

Tvrzení je **přesná** rovnost w=u'+v''=u''+v'. Pro w=0 je v=−u
a vše je přesné. Jinak měřítkem nastavíme exponent w na p, takže
w je celé a r je ocas u+v modulo1. Pišme u'=u−r−t, kde t je ocas
u−r modulo b^e a e je exponent u' minus p. V případě nulového u'
lze pro t=0 použít libovolně malý odpovídající exponent.

Pro e<=0 je w celočíselný násobek b^e. Proto t≡u−r=w−v≡−v
modulo b^e a |t|<=b^e/2. LemmaT dává v''=R(v+t)=v+t, a tedy
u'+v''=u+v−r=w.

Pro e>0 musí |u−r|>=b^p−1/2. Jelikož |r|<=1/2, je |u|>=b^p−1,
a u je celé. Proto je r ocas v modulo1. Je-li u'=u, pak t=−r,
tedy ocas−v. V opačném případě vzdálenost |r|<=1/2 dovoluje změnu
na vyšší řád jen v hraniční situaci |u|=b^p−1,|r|=1/2,|u'|=b^p;
potom t=r, které je rovněž ocas−v modulo1. Opět LemmaT dává v''=v+t.
Pro druhou rovnost zaměníme u a v. Tento důkaz nezávisí na výběru poloviny.

## 3. Theorem B, blízké exponenty

Chceme přesně získat

```text
u+v = w + R(R(u−u')+R(v−v'')).
```

Předchozí značení dává u−u'=r+t a v−v''=−t. Stačí ukázat, že
r,t,r+t jsou reprezentovatelné. Znaménko−t pak nic nemění.

Nejprve |e_u−e_v|<p. Přesný součet má nejvýše2p významných cifer;
po odebrání zaokrouhlených p horních cifer má r nejvýše p cifer,
včetně případné změny exponentu. Je-li e>0, z důkazuA máme t=−r
nebo t=r=±1/2; v druhém případě r+t=±1. Tyto hodnoty jsou přesné.

Je-li e<=0, platí t+r≡u a t≡−v modulo b^e. Navíc
|t|<=b^e/2<=1/2 a |r+t|<=1. Z nerovnosti |e_u−e_v|<p a exponentu
součtu p plyne e_u,e_v>=0: větší exponent je nejméně p−1 a menší
je nejméně větší−p+1. Proto oba vstupy i uvedené zbytky leží na
mřížce b^(-p), případně hrubší. Velikost nejvýše1 znamená nejvýše
p významných míst (krajní1 je mocnina b), takže jsou reprezentovatelné.
Tím jsou všechny tři operace v korekci přesné.

## 4. Theorem B, vzdálené exponenty: úloha12

Symetrií a škálováním vezměme u=U celé, B=b^(p−1)<=U<b^p=N,
|v|<1, tedy e_v<=0. Nulový v je triviální. Následující přímé rozdělení
ověřuje i přesnost všech pomocných odečtení, bez předpokladu o polovinách.

**Běžný případ:** U>B, nebo U=B a w>=U a u'>=U.
Pišme w=U+j, j∈{−1,0,1}, a r=v−j, |r|<=1/2.
Je u'=U+h, h∈{−1,0,1}; nenulové h je možné pouze při
r=−h/2. TheoremA (nebo přímá celočíselná reprezentace) dává
v''=j−h. Proto u−u'=−h a v−v''=r+h. Pro h=0 je druhá hodnota
ocas v modulo1; pro h≠0 je r+h=−r. Obě jsou reprezentovatelné
a součet je r, opět reprezentovatelný ocas.

**U=B,w=U,u'<U:** v>0 a0<v<=1/2. Pišme u'=U−j/b,
kde j je nejbližší celé k bv. Potom v''=j/b a u−u'=j/b jsou přesné;
v−v''=v−j/b je reprezentovatelný ocas v modulo1/b. Jejich součet
je v=r, který je vstupem a tedy reprezentovatelný.

**U=B,w<U:** v<0 a w=U−j/b pro kladné celé j<=b.
Pro p1 může normalizovaný výsledek mít i menší exponent; přesto
má tento tvar, protože při e_v=0 je v násobkem1/b a při e_v<0
je |v|<1/b. Položme r=v+j/b; jde o ocas v modulo1/b, |r|<=1/(2b).
Pak u'=U−h/b, kde h=0, nebo h=1 pouze při r=1/(2b).
Je v''=(h−j)/b přesné, u−u'=h/b přesné a v−v''=r−h/b je
buď r, nebo−r, tedy také přesné. Součet znovu dává r.

Tím je pokrytá celá úloha12. Ve všech případech je navíc v'=w−u přesné a u''=u; korekce po záměně
operandů je proto rovnou reprezentovatelný ocas v−v'=r. Tím platí
i druhá symetrická verzeTheoremB. Konečný model kontroluje obě verzeA,
jednotlivé přesné rozdíly i celkovou identituB.

## 5. Theorem C a úplná charakterizace20

Předpokládejme |u|>=|v|. Zkrácený vzorec je

```text
u+v = w + R(R(u−w)+v).
```

Pokud exponent u není menší než exponent w, po škálování w na celé
je také u celé. Pak r je ocas v modulo1, takže LemmaT dává
w−u=v−r přesně; finální korekce je reprezentovatelné r. To pokrývá
i opačná znaménka a případy bez změny exponentu součtu.

Zbývá přenos do vyššího exponentu, u,v stejného znaménka. Obraťme
znaménka na kladná a měřítkem nastavme u=U celé, B<=U<N=b^p.
V tomto případě w je násobkem b a |w−u−v|<=b/2. Je-li w<2N,
potom w<=2N−b a protože v<=u,

```text
u >= w/2−b/4,
0 <= w−u <= w/2+b/4 <= N−b/4 < N.
```

Číslo w−u je celé s nejvýše p ciframi, tedy opět přesné; vzorec platí.
Proto může selhat pouze při **w=2N**. To vyžaduje, aby v mělo stejný
exponent jako u (při menším je v<= (N−1)/b a součet nemůže být tak velký).
Pišme U=N−j,V=N−k,1<=j<=k. Zaokrouhlení na2N nastává právě když

```text
j+k < b/2,
nebo j+k=b/2 a pravidlo poloviny vybere2N.
```

Pak j<=b/4, takže R(U−2N)=−N jednoznačně. Vypočtená korekce je−k,
ale přesná je−j−k. Vzorec **vždy selže**. To je nutná i postačující
podmínka odpovědi20, vyjádřená bez neurčitého slova„essentially“.

Pro b<=3 je j+k>=2>b/2, takže selhání není možné: TheoremC.
Při b4 a doporučených lichých polovinách dokonce také žádné selhání
nenastane; při sudých polovinách u=v=3 v p1 selže. Větší základy
mohou selhat i mimo přesnou polovinu. Konečná kontrola testuje uvedené
kritérium jako ekvivalenci, nikoli pouze generuje vybrané protipříklady.

## 6. Cancellation: úloha25

Je-li 0<=v<=u<=2v, odečtení u−v je přesné (Sterbenzova vlastnost).
Pro stejné exponenty jde o rozdíl celých significandů menší než b^p.
Pro sousední exponenty pišme u=bU a v=V v jemnějších jednotkách,
kde U,V mají nejvýše p cifer. Pak0<=bU−V<=V<b^p, opět nejvýše p cifer.
Jiné exponenty nejsou při u<=2v možné. Stejné znaménko záporných
čísel řeší symetrie. Podtečení zůstává mimo zdejší předpoklady.

Ztráta významných cifer při odčítání proto často odhalí již existující
chybu vstupů: pokud u,v aproximují velká blízká skutečná čísla,
jejich absolutní chyby se vůči malému rozdílu relativně zvětší.
Příklady odpovědi jsou přesné algebraické identity:

```text
(x+ε)²−x² = ε(2x+ε),
sqrt(x+ε)−sqrt(x) = ε/(sqrt(x+ε)+sqrt(x)).
```

Příslušné definiční obory a nenulový jmenovatel se předpokládají.
To neznamená, že původní výpočet funkcí nebo následné dělení je bezchybné.

## 7. Výsledek konečných kontrol a stavD

Ověřeno20 940 ocasů a230 348 dvojic proA/B/C včetně libovolné velikosti relativního exponentu pokryté důkazy. Model navíc zkontroloval150 640 případůD; jediná nalezená výjimka jeC0085, b2,p1, liché poloviny. Všechny úspěšné bloky uloženy a při obnovení neopakovány. Obecný důkazD byl následně dokončen v `accuracy-drift.md`, včetně přesné klasifikace jednobitové liché výjimky. Primární vydavatelská metadata Reiser–Knuth1975 získána vXML, celý článek nikoli.
