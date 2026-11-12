# Obnova §4.2.2: celá věta B a všechny větve úlohy 12

7. listopadu 2026. Původní 236, zadání 243 a celá odpověď 614
porovnány po jednotlivých vztazích. Důkaz níže pokrývá (45)–(46),
každou ze sedmi pojmenovaných větví odpovědi 12, všechny čtyři
pomocné přesné rozdíly a cenu pěti operací. Bez numerického běhu.

## Přesný cíl (45) a každá ekvivalence (46)

Přebírá se model i celá věta A z
`recovery-accuracy-theorem-a-2026-11-06.md`: nejbližší R,
normalizované vstupy, všechny použité operace definované,
libovolná pevná volba půlek. Označení zůstává

`w=R(u+v)`, `r=u+v−w`,
`u'=R(w−v)=u−r−t`, `v''=R(w−u')=v+t`.

Věta A již dává přesné `u'+v''=w`. Chceme (45):

`u+v = w + ((u⊖u')⊕(v⊖v''))`.

Vnější plus je přesné sčítání; nepřidává šesté zaokrouhlení
ani netvrdí, že u+v musí být uložitelné v jediném p-ciferném slově.
Vnitřní přesné rozdíly jsou

`u−u'=r+t`, `v−v''=−t`, jejich součet je r.

Proto první přesnost v důkazu je `R(r+t)=r+t`, druhá
je `R(−t)=−t` a třetí `R(r)=r`. Representovatelnost t
a −t je ekvivalentní nezávisle na pravidlu půlek, takže druhou
lze psát `R(t)=t`, přesně jako v (46). Teprve po důkazu
těchto tří přesností je korekce rovna r a vnější rovnost
plyne z w+r=u+v. Samotná věta A tedy bez (46) nestačí.

Je-li u=0 nebo v=0, je w druhý vstup; přímo z (41) mají
všechny chybové rozdíly hodnotu 0. Je-li w=0, u+v=0
a výše popsaný nulový případ A rovněž dává r=t=0.
Tyto případy jsou tím uzavřeny před exponentovými redukcemi.

## Blízké exponenty: úplný důkaz obou ciferných tvrzení

Nyní jsou relevantní vstupy i w nenulové. Stejně jako u A
přeznačíme jednotky tak, aby exponent w byl p; při libovolných
půlkách se přenáší vybrané pravidlo, jak je tam přesně dokázáno.
Pišme N=b^p, B=N/b. Potom w je celé, B≤|w|<N a |r|≤1/2.
Předpokládejme `|e_u−e_v|<p`.

Nechť E=max(e_u,e_v), m=min(e_u,e_v), d=E−m≤p−1.
Na společné nejjemnější mřížce `g=b^(m−p)` má součet tvar
`u+v=(U b^d+V)g`, kde U,V jsou podepsaná celá čísla
s absolutními hodnotami nejvýše N−1. Proto pro K=U b^d+V

`|K|≤(N−1)(b^d+1)≤(N−1)N<N²=b^(2p)`.

Použito je `b^d+1≤b^(p−1)+1≤b^p`, platné i pro p=1.
Součet má tedy nejvýše 2p významných cifer, jak tvrdí text;
případná znaménková kompenzace jejich počet pouze zmenší.

Je-li K již p-ciferné, r=0. Má-li přesně L cifer s
p<L≤2p, nejbližší p-ciferné zaokrouhlení na této celočíselné
mřížce vybírá násobek `H=b^(L−p)`. Platí to i při přenosu
do dalšího pásma: jeho hraniční mocnina b je násobkem H.
Chybový koeficient je celé číslo velikosti nejvýše
`H/2≤b^p/2<b^p`, tedy má nejvýše p cifer. Po násobení g
zůstává nejvýše p významných cifer. Tím je dokázáno
`R(r)=r` včetně přenosu, půlek a záporného součtu.

## Proč jsou oba vstupní exponenty nezáporné

Je třeba dokázat i poslední větu tištěného důkazu, nikoli
pouze předpokládat podobnou velikost operandů. Kdyby E≤p−2,
pak obě absolutní hodnoty vstupů jsou nejvýše
`(N−1)b^(E−p)≤(N−1)/b²`. Z toho

`|u+v|≤2(N−1)/b²≤(N−1)/b=B−1/b`.

Hodnota B−1/b je representovatelná a je menší než B.
R je neklesající a fixuje oba konce intervalu
`[−(B−1/b),B−1/b]`, proto by také |w|≤B−1/b<B,
ve sporu s exponentem w=p. Musí tedy E≥p−1.
Z d≤p−1 plyne `m=E−d≥0`. Tím jsou e_u,e_v≥0;
obě možnosti záporného exponentu z poslední věty textu
jsou skutečně vyloučeny, včetně b=2,p=1 a přenosu.

## Dokončení (46) v obou větvích pomocného exponentu

Je-li u'=0, pak u−r=0 a t=0; r+t=u je již vstup.
Zbývá nenulové u' a `e=e_{u'}−p` jako ve větě A.

Pro e>0 dává již celý důkaz A buď `t=−r`, nebo
`t=r=±1/2`. V prvním případě je t representovatelné
jako znaménkově obrácené r a r+t=0. Ve druhém je t=r
representovatelné a r+t=±1. Obě zbývající přesnosti (46)
jsou tedy doloženy samostatně; nejde o nové použití R na r.

Pro e≤0 jsou tištěné congruence
`t+r≡u (mod b^e)` a `t≡−v (mod b^e)` správné:
první z `u'=u−r−t`, kde u' je násobek b^e, druhá z A.
Následující podmínky `e_u≥e`, `e_v≥e` jsou splněny,
protože jsme dokázali dokonce e_u,e_v≥0≥e. Pro úplný
ciferný závěr doplňme tento argument v aktuálním rozsahu:

Zaokrouhlení R zachovává každou mřížku `b^k Z`. Po změně
jednotky je totiž její vstup celé číslo; má-li nejvýše p cifer,
je přesný, jinak se zaokrouhlí na násobek kladné celé mocniny b,
který je také celý. Přenos ani volba půlky na tom nic nemění.

Z e_u,e_v≥0 jsou u,v a celé w násobky `b^(−p)`.
Také w−v, jeho zaokrouhlení u', a proto t=(w−v)−u'
jsou na stejné mřížce. Stejně tak r=u+v−w a r+t.
Z `|t|≤b^e/2≤1/2`, `|r|≤1/2` plyne `|r+t|≤1`.
Každý násobek b^(−p) velikosti menší než 1 má nejvýše
p významných cifer; hraniční ±1 jsou mocniny b. Takto jsou
t i r+t přesně representovatelné. Nevytrháváme podmínku
„provided e_u≥e and e_v≥e“ z ostatních hypotéz blízkého
případu a nevydáváme ji za izolovanou větu o libovolných
congruencích. Každý skutečný krok tištěného důkazu je nyní
v jeho celém aktuálním rozsahu doložen.

## Úloha 12: redukce a úplné rozdělení vstupů

Zbývá `|e_u−e_v|≥p`. Nuly už byly uzavřeny. Záměnou
vstupů dejme větší exponent u, změnou jednotek e_u=p a
případně změnou znamének u>0. Stejně jako škálování se
libovolná volba půlek může zrcadlit do jiného nejbližšího
pravidla; nevyžaduje se její původní znaménková symetrie.
Obě pořadí operandů budou pokryta všemi čtyřmi přesnými
rozdíly uvedenými na konci odpovědi.

Máme celé `B=b^(p−1)≤u<N=b^p`, e_v≤0 a |v|<1.
Rozlišujeme u>B a u=B, přesně jako zdroj. Symboly r,t
zde mohou být přeškálovány s případem; pro samotný rozklad
vždy r=u+v−w a t=u−r−u'.

## Případy 1a, 1b, 1c, 2a a 2b po jednotlivých hodnotách

Pro u>B mají sousedé v rozsahu u±1 celočíselné hodnoty.
Vstup u+v je mezi u−1 a u+1, takže w je u−1,u,u+1.
Horní kraj N je dovoleno použít jako přesný hraniční bod.

| Větev | Proč platí podmínky | u' | v' | u'' | v'' |
| --- | --- | --- | --- | --- | --- |
| 1a | w=u+1 vyžaduje v≥1/2; odtud e_v=0. Přesný w−v leží v (u,u+1/2]. | u nebo u+1, druhá možnost jen na půlce v=1/2 | 1 přesně | u přesně | 1 nebo 0 podle u' |
| 1b | w=u vyžaduje |v|≤1/2; v'=0. | při doporučené paritě u; libovolná půlka navíc dovolí u+h s h=±1 pouze pro v=−h/2 | 0 | u | 0, nebo −h ve výjimečné půlce |
| 1c | w=u−1 vyžaduje v≤−1/2; e_v=0. Přesný w−v leží v [u−1/2,u). | u nebo u−1, druhá možnost jen na půlce v=−1/2 | −1 přesně | u přesně | −1 nebo 0 podle u' |
| 2a | u=B,w=u+1 má stejnou horní jednotkovou mřížku a v≥1/2,e_v=0. | jako 1a | 1 | u | jako 1a |
| 2b | u=B,w=u,|v|≤1/2,u'≥u; podrobnost níže. | u | 0 | u | 0 |

V každém řádku jsou v'=w−u, u''=w−v' a v''=w−u'
již malé representovatelné celé rozdíly, proto je R nemění.
Volba u' je jedinou uvedenou nejistotou; bez půlky je jediná.

Pro tvrzení v 1b o doporučeném pravidlu: při v=±1/2
volba w=u znamená, že ciferná parita u je preferovaná.
Tatáž parita je pak preferovaná i v druhé půlce u−v,
a u'=u. Pod horní hranicí N se parita posuzuje na původní
jednotkové mřížce před případným přenosem, jako v N5.
Pro liché b nelze v=±1/2 vyjádřit konečným počtem cifer;
tedy tato výjimka nevznikne. Při obecné volbě půlek je
alternativa u'=u+h, v''=−h možná, ale její znaménko
musí splňovat v=−h/2, jak přesně popisuje řádek.

V 2b je dokonce u'=u pro každé nejbližší pravidlo. Je-li
v≥0, pak w−v≤u a monotonie dává u'≤u; s hypotézou
u'≥u vznikne rovnost. Je-li v<0, výběr w=u na jemnější
dolní mřížce vynucuje |v|≤1/(2b); proto je w−v=u+|v|
jednoznačně bližší u než hornímu sousedu u+1. Formulace
„like (1b)“ tedy zahrnuje správné hodnoty a její další
obecné alternativy zde nejsou dosažitelné.

Všechny tyto řádky lze pro přesnost rozdílů spojit bez
ztráty jejich podmínek: pišme `w=u+j`, `u'=u+h`.
Pak v'=j, u''=u, v''=j−h a r=v−j je ocas v modulo 1.
Je-li h=0, zůstává r. Je-li h≠0, z výše určené půlky
nutně `r=−h/2`, takže `r+h=−r` je také representovatelné.
Každý ze závěrů konce odpovědi je proto:

`u−u'=−h` přesné, `v−v''=r+h` přesné,
`u−u''=0` přesné, `v−v'=r` přesné,
`w−u−v=−r` přesné.

Samotné r je representovatelné jako silný ocas
representovatelného v podle úplné úlohy 11. Korekční součet
`−h+(r+h)=r` je také přesný, což uzavírá (45) i (46)
ve všech pěti uvedených větvích.

## Případ 2c: každá hodnota a všechny chyby

Nyní u=B,w=u, |v|≤1/2 a u'<u. Monotonie nutí v>0.
Zaokrouhluje se B−v v dolní mřížce s krokem 1/b, takže

`u'=u−j/b`, kde j je celé, `1≤j≤b/2`.

Dolní mez j≥1 vyjadřuje u'<u. Horní mez: v≤1/2;
pro sudé b je b/2 celé a bližší vyšší j nelze zvolit;
pro liché b je v=1/2 nemožné a j≥(b+1)/2 by vyžadovalo
v≥1/2. Platí to i p=1, kdy nejmenší dotčená kladná
hodnota leží alespoň na dolní hranici pásma.

Položme `v=j/b+v₁`. Z volby nejbližšího j/b plyne
`|v₁|≤1/(2b)`. Proto v₁ je silný ocas v modulo 1/b.
To doloží i representovatelnost v₁ a j/b z úlohy 11.
Z definic (41) je přesně

`v'=0`, `u''=u`, `v''=j/b`.

Čtyři vytištěné přesné rozdíly jsou nyní j/b, v₁, 0 a v
v pořadí u−u', v−v'', u−u'', v−v'. Také
`w−u−v=−v` je representovatelné. Korekce je
`j/b+v₁=v=r`, tedy už vstupní p-ciferná hodnota.
Tím jsou ověřeny jak všechny hodnoty řádku 2c, tak všechny
závěrečné přesnosti a (46).

## Případ 2d: dolní sousedé, obě půlky a přesnost

Nyní u=B a w<u, takže v<0. Pro p≥2 je
`u+v>B−1≥B/b`, kde poslední mez plyne z B≥b.
Pro p=1 je B=1: při e_v=0 má |v|≤(b−1)/b,
tedy u+v≥1/b; při e_v<0 je |v|<1/b a rovněž
u+v>1−1/b≥1/b. Ani v tomto nejmenším formátu se
součet nedostane pod potřebné dolní pásmo.

Zaokrouhlený w tedy má tvar `u−j/b` pro celé
`1≤j≤b`. Při p=1 je ve skutečnosti j≤b−1,
ale tištěná slabší mez j≤b zůstává pravdivá.
Položme `v=−j/b+v₁`; nejbližší výběr w dává
`|v₁|≤1/(2b)` a v₁=r je silný ocas v modulo 1/b.

První pomocná hodnota zaokrouhluje `w−v=u−r`.
Je-li r≤0, je u−r nad u o nejvýše 1/(2b)<1/2,
tedy se jednoznačně vrátí na u. Je-li 0<r<1/(2b),
je jednoznačně bližší u než u−1/b. Jen při
`r=1/(2b)` dovoluje půlka oba výsledky. Pišme tedy

`u'=u−h/b`, h∈{0,1}, přičemž h=1 jen při r=1/(2b).

Zbývající hodnoty jsou přesné:

`v'=−j/b`, `u''=u`, `v''=(h−j)/b`.

Čísla j/b a (h−j)/b mají nanejvýše jednu významnou
cifru, nebo jsou ±1 či 0, proto je R nemění. Pro h=0
jde o vytištěnou dvojici `(u',v'')=(u,−j/b)`;
pro h=1 o `(u−1/b,(1−j)/b)`, a nastává pouze při
uvedené kladné půlce. Tím jsou obě vytištěné alternativy
i jejich nutná podmínka samostatně doloženy.

Rozdíly z konce odpovědi jsou nyní

`u−u'=h/b`, `v−v''=r−h/b`,
`u−u''=0`, `v−v'=r`, `w−u−v=−r`.

Při h=0 je druhý rozdíl r, při h=1 je r−1/b=−r.
Ocas r a jeho negace jsou representovatelné podle úlohy 11,
stejně h/b a nula. Korekce je přesně
`h/b+(r−h/b)=r`. Jsou tedy ověřeny všechny závěrečné
rovnosti odpovědi 12 a (46) i v poslední větvi.

## Úplnost úlohy 12, cena a rozsah uzavření

Pro u>B jsou 1a–1c všechny tři možnosti w. Pro u=B
jsou w>u, w=u s u'≥u, w=u s u'<u a w<u přesně
2a–2d; nic dalšího nezbývá. V každém případě jsou
u−u', v−v'', u−u'', v−v' a w−u−v representovatelné,
takže záměna původních vstupů zachovává i druhou verzi
korekčního rozkladu. Tím původní redukce většího exponentu
na u neztrácí žádný případ. Celá úloha 12 je uzavřena,
nikoli jen její požadovaný konečný vzorec.

Po již spočítaném w potřebuje korekce přesně těchto pět
operací: `u'=w⊖v`; `v''=w⊖u'`; `a=u⊖u'`;
`c=v⊖v''`; `r=a⊕c`. Každý vstup je před použitím
známý a poslední tři operace jsou prokázaně přesné.
Výpočet samotného w je jedna další operace, pokud jej
nemáme. Vnější přesné plus v (45) popisuje dvojici
hlavní hodnoty a korekce; není vydáváno za další přesnou
strojovou operaci s jedním p-ciferným výsledkem.

Úvodní srovnání významnosti A a B je hodnotící motivace;
konkrétní výhoda B je doložený přesný korekční vzorec a
uvedená cena. Následující úspora pro b=2,3 bude uzavřena
samostatně s větou C a úlohou 20. Původní sazba i všechny
čtyři vrstvy errat a aktuální TeX byly porovnány; pro B
a odpověď 12 nebyla nalezena relevantní oprava. Žádný nový
nález, žádná nová konečná kontrola ani opakování staré.
