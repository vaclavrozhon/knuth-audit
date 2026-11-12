# Individuální audit SGB: str.9–12 a §7–25 až38

6. listopadu2026. Nově přečteny celé odpovědi519–520/file536–537, na521/file538
cíleně37–38. Tam byl také zachycen F0001 v46(b), viz samostatný důkaz.
Žádný matematický program ani nový census. Konkrétní slova vyhledána v již
uloženém primárním audit-2026-10-31/sources/sgb-words.txt.

## Text str.9–12

Přebírá se5757 slov, which…pupal, pět ranků, vzdálenost²2415, svědci pokrytí
20/24/25 písmen, čtverec(9) s maximálním rankem372 a symetrická krychle(10)
s rankem2968: results/first-pass-sanity.json. Nic se neopakovalo.
Globální maximum vzdálenosti yucca/abuzz, horní mez24 pro pět SGB slov,
nejnižší rank krychle, počty3/83576 krychlí a390 miliard memů jsou partial.

Hammingova hrana přesně odpovídá jednopísmennému kroku, takže nejkratší
transformace je nejkratší cesta. Posloupnost(11) mění postupně pozice
1,2,5,4,3,2; posloupnost(12) pozice5,4,5,3,1,3,5,1. Všechna slova jsou v SGB.
Tvrzení o766-slovném TeX podgrafu a parametrech implementace se nepřepočítala.

Opravená cesta(13) z2013 je chaos,chose,chore,score,store,stare,spare,space,peace.
Společné podposloupnosti sousedů: chos,choe,core,sore,stre,sare,spae,pace.
Orientovaná cesta(14) words,dross,soars,orcas,crash,sharp,graph vždy obsahuje
v cíli multiset čtyř posledních písmen předchůdce. Nejkratší délka6 zůstává
partial; platnost svědka neprokazuje minimálnost.

Historické citace a obsah ostatních SGB dat byly bibliograficky přeskočeny.
Známé opravy názvu eseje, odkazu naweb, cesty(13) a TeX formulace se přebírají
z pěti4A/F0 vrstev; nejde o nové nálezy.

## Úlohy25–30

25: stela/telas/elast/laste/astel jsou cyklické posuny pěti různých písmen,
proto Latin. Slovníková přípustnost archaických tvarů/prefixu elast je partial.

26: vlastní svědek „Every night, tired minds enjoy quiet walks under clear skies.“
má deset slov délky5. Také všech16 slov původní odpovědi má délku5.
Známá náhrada odpovědi2025 je jiný svědek, nikoli náš nález.

27: čísla4+163+1756+3834 dávají5757; mamma/esses mají četnosti3+2.
Úplný histogram se nově nepočítal.

28: rozdílové vektory needs/offer=(+,+,+,+,−), ghost/hints=(+,+,−,+,−),
strut/rusts=(−,+,+,−,−), robed/spade=(+,+,−,−,+), vždy velikost1.
Adder/beefs,sheer/tiffs,sneer/toffs mají všude+1. Konkrétní členství a
ranky needs180/offer384 sedí. Počet38, úplnost tří monotónních párů a
čtyř výjimek zůstávají partial.

29: level/dewed jsou palindromy; devil/lived,knits/stink,smart/trams,
faced/decaf jsou obrácené. Členství/ranky level184,dewed5688 sedí.
Počty18/34 a krajnost jsou partial.

30: first,below,floor,begin,cells,empty,hills,abbey,pssst,mossy mají
neklesající písmena; mecca,zoned nerostoucí. Počty105/37, frekvenční pořadí
a globální lexikografická krajnost se nově neenumerovaly.

## Úlohy31–35

31: krajní vektory aritmetické trojice musí souhlasit modulo2 v každé
souřadnici; jejich průměr je jediný kandidát na prostřední slovo.
Rozdělení do32 paritních tříd odůvodňuje algoritmus; „about32“ je heuristika
o rozložení tříd, nikoli univerzální přesný faktor. Přímo sedí průměry
power/visit=slugs,marry/solve=photo,risky/vague=tempo a žádná krajní
souřadnice se neshoduje. Druhé dvě trojice mají ranky≤2000 (max1137/1676).
Úplné počty119 a2 zůstávají partial.

32: střídavé pozice peopleless dávají polls/epees, ranky1581/4355.
Pozitivní odpověď je doložena; „only reasonably common“ je neověřený
lexikální úsudek.

33: vytištěné dvojice ab,bc,…,za sedí, někdy s mezerou. Dvakrát first
pokrývá rs/st; crazy záměrně nabízí opačné zy místo chybějícího yz.
Neexistence yz, minimální mezery a nejnižší ranky zůstávají partial.

34: obě slova v každé z32 kategorií mají odpovídající masku0..31
(první písmeno je nejvyšší bit). Např.queue01111,ouija/aioli11101.
Součet tabulky4889 plus868 vynechaných slov dává5757. Četnosti/ranky jsou
partial. Mimo SGB mají ooops/ooooh/ooooo masky11100/11110/11111; jejich
internetová přípustnost nebyla ověřována.

35: po s je větvení h/t, pak sh:e/o a st:a/e; dále
she:e/l,sho:r/w,sta:l/r,ste:a/e. Poslední větvení dává vytištěné dvojice
sheep/sheet,shelf/shell,shore/short,shown/shows,stalk/stall,stars/start,
steal/steam,steel/steep. Všech16 slov má rank≤978, rovnost u stalk.
Existence úplného trie je tedy ověřená; nemožnost před978 není.
U ostatních breakpointů sedí vytištěné ranky konkrétních slov, nikoli
nový důkaz jejich minimality. Obrácený16slovný příklad má po koncovém k
větvení c/n,a/i,l/r a dvě první písmena. Ternárních81 slov je partial.

Hortonova–Strahlerova charakterizace: úplný binární podstrom výšky h
vznikne v jednom potomku nebo ze dvou podstromů výšky h−1. Kapacita je
tedy max(h1,h2+1) pro dva nejsilnější potomky. Ve čtyřvrstvém trie je
dosažení4 přesně existence úplného binárního stromu hloubky4.

## Úlohy36–38

36: symetrie identifikuje tři směry a uspořádání pevných dvou souřadnic.
Typů slov je tedy n(n+1)/2 místo3n², pro n5 patnáct místo75.
Šestinásobná symetrie konkrétní krychle je již uzavřená.
Stove→store,event→erect současně mění orbitu(2,4,4),(4,2,4),(4,4,2)
z v na r a diagonálu(4,4,4) z n na c. Varianta stole/elect mění tutéž
orbitu na l a diagonálu na c. Obě zachovávají symetrii; nové ranky
189/1170 a1013/1129 jsou≤3000. Úplnost tří krychlí zůstává partial.

37: maximum stupně25 právě u bares/cores je partial; žádný grafový census.

38: tears→raise→aisle→smile a varianta reals splňují pravidlo. Vlastní
tears→arise→riles→smile také. Chybějící i,l,m vyžadují alespoň3 vložení.
Opačně je třeba odstranit i,l,m, ale první krok nutně odstraní s,
takže jsou třeba alespoň4 kroky. Svědek smile→miler→liter→irate→tears
dosahuje4; ranky375,3626,2162,2725,430 potvrzují členství. Oba směry jsou
tím optimální bez prohledávání grafu.
