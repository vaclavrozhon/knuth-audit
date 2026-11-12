# Obnova §4.2.2: celá věta A, (40)–(44) a celá úloha 11

7. listopadu 2026. Původní 235/file247, zadání 243/file255
a odpověď 614/file626 znovu přečteny. Níže jsou všechny
tištěné mezikroky, včetně nul, změny měřítka, hraničního
přenosu a slabšího dodatku odpovědi 11. Žádný výpočet neběžel.

## Model, význam ocasu a rozsah přesnosti

Pracujeme se základem b≥2 a p≥1, s abstraktním nejbližším
zaokrouhlením R a definovanými operacemi. Vstupy u,v jsou
normalizované, nula má konvenci ze strany 215. Ideální soustava
s celými exponenty umožňuje oddělit počet významných cifer od
kontroly konečného exponentového rozsahu. Věta A výslovně
vylučuje podtečení i přetečení všech použitých operací.
Konkrétní Program A s C0251 není tímto důkazem opraven.

V (44) je e celé, `h=b^e>0`, a t je ocas x modulo h, právě když
`x−t∈h Z` a `|t|≤h/2`. Congruence neznamená, že x nebo t
musí být celé. Při půlce mohou existovat dvě dovolené hodnoty t,
lišící se o h; argument musí pokrýt obě.

Tvrzení, že `x−R(x)` je vždy ocas x, potřebuje určit vhodné h.
Pro nenulové `y=R(x)` s exponentem E zvolme `h=b^(E−p)`
(excess je zde zahrnut do E). Hodnota y je celočíselný násobek h.
Vzdálenost y od kteréhokoli bezprostředního souseda je nejvýše h:
uvnitř pásma h, pod jeho dolním koncem h/b, nad koncem h.
Jestliže R zvolí y, leží x nejvýše uprostřed mezi y a jedním
z těchto sousedů; proto `|x−y|≤h/2`. Tím platí obě části
(44). Pro y=0 je v tomto modelu x=0 a libovolné h vyhovuje.
Tento argument nevybírá jednu z půlek a funguje pro obě znaménka.

## Celá úloha 11: každý případ Lemma T

Cílem je přesná representovatelnost `x−t`, tedy
`R(x−t)=x−t`. V silné verzi (44) navíc ukážeme i
representovatelnost t na nejvýše p významných cifrách.
Je-li konečný exponent potřebné hodnoty nepovolený, nejde
o definovanou operaci; přesnost cifer není slibem jiného rozsahu.

Pro x=0: `t∈h Z` a `|t|≤h/2` vynucují t=0; závěr je
přesný. Pro nenulové representovatelné x obraťme případně
znaménko a vynásobme x,t stejnou mocninou b, aby
`0≤x<b^p=N` bylo celé. Tím se modulus h pouze změní na
jinou celočíselnou mocninu b a počet významných cifer se
nezmění. Nevoláme zde znaménkovou symetrii zaokrouhlování
na půlkách: jde o přesnou representovatelnost čísel.

1. **e≤0.** Celé x je násobkem h, protože `1/h=b^(−e)`
   je celé. Congruence tedy činí také t násobkem h. V intervalu
   `[-h/2,h/2]` je jediným takovým násobkem nula, tedy t=0
   a x−t=x. Tím je doložena první věta odpovědi, včetně e=0.
2. **0<e≤p.** h je kladné celé a dělí N; t je celé.
   Z `|t|≤h/2≤N/2<N` plyne nejvýše p cifer pro t.
   Číslo x−t je násobek h. Protože `x−t>−h`, nemůže být
   záporným násobkem h. Protože `x−t<N+h`, nemůže být
   větší než N. Má tedy nejvýše p+1 cifer a je dělitelné b,
   skutečně dokonce b^e. Poslední e cifer jsou nuly; zbývá
   nejvýše `p+1−e≤p` významných cifer. Krajní N je mocnina
   b a nula je zvlášť representovatelná. To dokazuje přesně
   oba tištěné dílčí závěry: délku p+1 a nulovou poslední cifru.
3. **e>p.** Z celočíselnosti exponentů `h≥bN≥2N`.
   Máme `0≤x<N≤h/2`, ve skutečnosti x<h/2. Jediný
   násobek kh, který je od x vzdálen nejvýše h/2, je 0;
   tedy x−t=0 a t=x. Obě hodnoty jsou representovatelné.

V každém případě je R(x−t)=x−t, a (9) dává Lemma T.
V silné verzi je i t p-ciferné; pozdější použití s kladným
i záporným ocasem je proto legitimní v ciferovém modelu.

## Celý slabší dodatek odpovědi 11

Odpověď dovoluje místo `|t|≤h/2` také `|t|<h`.
Znovu ověřme každý případ, protože není důsledkem předchozí
silnější hypotézy:

* e≤0: t je násobek h a ostrá mez |t|<h stále dává pouze t=0.
* 0<e≤p: t je celé, `|t|<h≤N`, tedy má nejvýše p cifer.
  Z `−h<x−t<N+h` a dělitelnosti h plyne `0≤x−t≤N`.
  Opět nejvýše p+1 cifer a alespoň jedna koncová nula stačí.
* e>p: `0≤x<N<h`; nerovnost `|x−kh|<h` připouští
  jen k=0 nebo k=1. Tedy `x−t=0` nebo `x−t=h=b^e`.
  Přesně druhou možnost uvádí dodatek a obě výsledné hodnoty
  mají nejvýše p významných cifer.

Dodatek dokazuje vždy `R(x−t)=x−t`. Ve slabé verzi ale t
nemusí samo být p-ciferné: b=10,p=1,x=1,e=3 dovolí
t=−999, zatímco x−t=1000 je přesné. Pokud se ⊖ interpretuje
výhradně jako instrukce se dvěma uloženými p-cifernými vstupy,
je navíc nutné, aby t byl takovým vstupem. Jako matematický
zápis `R(x−t)` podle (9) je rozšířený závěr správný i bez
toho. Věta A používá silný ocas, takže tato oblast významu
jejího důkazu se nemění a žádný nový nález z dodatku nevzniká.

## Všechny definice (41) a vztahy (40), (42), (43)

Položme `w=R(u+v)`; v (41) je přesně

`u'=R(w−v)`, `v'=R(w−u)`,
`u''=R(w−v')`, `v''=R(w−u')`.

Čtyři definice mají odlišné argumenty a nelze je zaměňovat.
V (40) je první člen v' a druhý u'', takže jde o přesný
součet `v'+u''=w`. Záměna u,v dává druhý přesný součet
`u'+v''=w`; tím je (40) ekvivalentní oběma rovnostem (42).
Názvy s čárkami jsou intuitivně opravené části vstupů; kniha
v této větě netvrdí kvantitativní mez jejich přiblížení k u,v.

Z (42) plyne (43) zaokrouhlením **celého přesného součtu**:
`R(u'+v'')=R(w)=w` a `R(u''+v')=R(w)=w`, protože
w je representovatelné. Přesná rovnost je silnější než
samotné zaokrouhlení na w: například v b=10,p=1 je
R(1+.01)=1, avšak přesný součet je 1.01. Tento příklad
ukazuje logickou sílu tvrzení, ne další protipříklad k větě A.

## Nula a oprávnění ke změně měřítka

Je-li w=0, z vlastnosti R vyplývá u+v=0. Proto
u'=u, v'=v, u''=u, v''=v: každý rozdíl má již
representovatelný přesný výsledek. Obě (42) i (40) platí.

Pro nenulové w změňme jednotku mocninou b tak, aby jeho
nezatížený exponent byl p. Potom w je celé,
`b^(p−1)≤|w|<N=b^p`. Povolený konečný exponentový interval
se při tomto důkazovém přeznačení posune spolu s hodnotami;
nejde o skutečnou další instrukci, která by mohla přetéct.

Při pevném N5 je škálování konzistentní. Důkaz má ale platit
i při libovolném deterministickém výběru půlek. V tomto širším
rozsahu nepředpokládáme bez důkazu `R(b^k x)=b^k R(x)`
pro stejnou původní funkci R. Místo toho přeneseme její vybrané
nejbližší výsledky stejným škálováním na nové hodnoty. Nejbližší
vzdálenosti i půlky se zachovají; tak vznikne jiná dovolená
volba půlek. Následující argument platí pro **každou** takovou
volbu, a tedy po zpětné změně jednotky i pro původní výpočet.
Stejný argument v každém opakovaném volání má tutéž volbu.

## Chyba součtu a pomocný ocas

Pišme `u+v=w+r`, tedy `r=u+v−w`. Výše dokázaný fakt
o chybě zaokrouhlení při exponentu w=p dává `|r|≤1/2`
a `r≡u+v (mod 1)`: r je přesně vytištěný ocas modulo 1.

První pomocná hodnota je
`u'=R(w−v)=R(u−r)=u−r−t`.
První rovnost je (41), druhá používá w=u+v−r, třetí
**definuje** `t=(u−r)−R(u−r)`. Je-li u' nenulové,
pro `e=e_{u'}−p` je t ocas u−r modulo b^e podle
obecného faktu o R. Pokud u'=0, je w−v=u−r=0
a t=0; v''=R(w)=w a sledovaná rovnost platí okamžitě.
Není třeba přiřadit nulové hodnotě fiktivní vysoký exponent.
V doslovném konečném formátu má po přeznačení minimum exponentu
nejvýše p, neboť w je v rozsahu; i nulový exponent by proto
vedl do následující větve e≤0.

## Větev e≤0: každá kongruence a přesná operace

Celé w je násobkem b^e, neboť b^(−e) je celé. Proto

`t ≡ u−r ≡ w−v ≡ −v (mod b^e)`.

První congruence je definice t; prostřední identita je
w=u+v−r; poslední používá právě celočíselnost w.
Současně `|t|≤b^e/2`. Tím t splňuje obě části definice
ocasu −v; ekvivalentně −t je ocas v.

Lemma T aplikované na v a −t dává `R(v+t)=v+t`.
Tato aplikace nevyžaduje symetrické zaokrouhlování půlek,
protože v+t je **přesně representovatelné**. Dosazením
u'=u−r−t a w=u+v−r získáme každou vytištěnou rovnost

`v''=R(w−u')=R(v+t)=v+t`.

Pak `u'+v''=(u−r−t)+(v+t)=u+v−r=w`, přesně.
Záměna u,v dodá původní podobu (40) i druhou rovnost (42).

## Větev e>0: všechny meze a jediný hraniční přenos

Nyní u'≠0 a jeho exponent je alespoň p+1, tedy `|u'|≥N`.
Sousedy N na menší straně jsou N−1 a N; při záporných
hodnotách jde o jejich zrcadlo. Nejbližší volba s velikostí
alespoň N tedy vynucuje `|u−r|≥N−1/2`. Pod touto
půlkou by N−1 (se správným znaménkem) bylo blíž než
jakákoli hodnota velikosti alespoň N.

Z `|r|≤1/2` a trojúhelníkové nerovnosti plyne
`|u|≥|u−r|−|r|≥N−1`. Každé normalizované plovoucí
číslo takové velikosti je celé: už pásmo s exponentem p
má jednotkový krok a vyšší pásma mají celočíselné kroky b,b²,….
Proto jsou u i w celá a
`r=u+v−w≡v (mod 1)`. Spolu s |r|≤1/2 je r ocas v
modulo 1, přesně jak uvádí tištěný důkaz.

**Je-li u'=u**, pak `t=u−r−u'=−r`. Znaménkově obrácený
ocas v je ocas −v, takže opět Lemma T dává přesnost v+t
a tím rovnost u'+v''=w jako v předchozí větvi.

**Je-li u'≠u**, zůstanou jen následující možnosti. Vstup
u−r je od representovatelného u vzdálen nejvýše 1/2.
Jestliže |u|>N, nejbližší odlišný representovatelný soused
je vzdálen alespoň b≥2, a nemůže tak být nejbližší k u−r.
Při |u|=N může půlka směrem dolů zvolit N−1 v absolutní
hodnotě, ale to by mělo exponent p, proti e>0; všechny
ostatní sousední vzdálenosti jsou nejméně b.

Zbývá jedině `u=σ(N−1)` s σ=±1. Aby nejbližší výsledek
měl velikost nejméně N a byl odlišný od u, je nutně

`r=−σ/2`, `u−r=σ(N−1/2)`, `u'=σN`.

Tím jsou samostatně prokázány všechny vytištěné hodnoty
`|u|=N−1`, `|r|=1/2`, `|u'|=N` a dále
`t=(u−r)−u'=−σ/2=r`. Congruence r≡v modulo 1 pak
znamená také `t=r≡−r≡−v (mod 1)`, protože 2r=±1
je celé. A |t|=1/2. Tedy i tentokrát je t ocas −v.

Toto poslední použití má **modulus 1**, ačkoli původní
zaokrouhlovací ocas t mohl být zaveden modulo b^e.
Jeho nově doložená vlastnost modulo 1 je právě to, co
postačí pro Lemma T. Následuje v''=v+t a přesný součet w.
Pro liché b nemusí být hraniční půlka dosažitelná ze vstupů
u,v; důkaz ji však nepotřebuje vyloučit a je podmíněně správný
pro obě znaménka i každé p, včetně p=1.

## Celá věta, výběr půlek a další rozsah

Tím jsou vyčerpány w=0, u'=0, e≤0 a e>0 včetně obou
podpřípadů. Tentýž argument po záměně u,v dokazuje druhou
rovnost (42), takže i přesně vytištěnou (40); (43) už bylo
samostatně odvozeno. Žádný krok nepoužil konkrétní paritu
zaokrouhlení. Každá půlka může být vybrána kterýmkoli
nejbližším směrem, je-li R pevně určená funkce.

Úvodní věty o užitečnosti porovnávacích rutin a o „nepoddajnosti“
axiomů jsou motivace; zde se prokazují konkrétní identity,
nikoli obecné empirické soudy o numerických programech.
Všechny čtyři vrstvy errat i aktuální TeX byly prohledány:
pro větu A, Lemma T a odpověď 11 není relevantní oprava.
Starý důkaz v `accuracy-exact.md` byl znovu posouzen a jeho
nezapsané okraje jsou nyní doloženy výše. Celá úloha 11 je
uzavřena v matematickém rozsahu včetně slabšího dodatku;
věty B,C a další úlohy tím zatím uzavřeny nejsou.
