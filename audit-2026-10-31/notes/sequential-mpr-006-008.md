# MPR 6–8: Pólyova urna, martingaly a zastavování

D097–D099, 6. listopadu 2026. Zobrazeny všechny tři původní stránky
`file-026.png` až `file-028.png`. Diagram P je kontrolován celý,
nikoli vzorkem. Při kontrole vnitřních odkazů byly zobrazeny také
zadání na file39–40 a odpovědi na file401–403. Jejich celkový obsah
se tím neuzavírá; níže je přesně uveden převzatý rozsah.

## D097 — str. 6, definice a všechny výroky o urně

**(26), první krok a (28).** Martingale má integrabilní reálné členy;
rovnost (26) je jeho definice vzhledem k vlastní historii. Dosazení n=0
dává právě E(Z1|Z0)=Z0, jak text výslovně říká. V (28) je podstatná
také adaptovanost: každé Zj musí být funkcí X0,…,Xj. Pak je celá
historie Z0,…,Zn funkcí X0,…,Xn. Potřebná implikace na vlastní
historii je dokázána v D098 níže; nelze libovolně zaměnit podmiňující
informaci. Odkaz MPR63 na str.18 skutečně požaduje konkrétní první
krok pro ternární proměnné; celou úlohu63 tento blok nepřebírá.

**Model a všechna políčka diagramu.** Ve stavu (r,b) je r+b koulí,
z nichž r je červených a b černých. Při rovnoměrném výběru má další
červená pravděpodobnost r/(r+b) a mění stav na (r+1,b); černá má
pravděpodobnost b/(r+b) a mění jej na (r,b+1). Kořen je (1,1).
Po n tazích je tedy r+b=n+2 a r,b≥1. V každém tahu roste součet
právě o1, takže všechny hrany směřují o jednu úroveň dolů a model
nemá v konečné historii cyklus.

Na str.7 bylo přepsáno všech10 viditelných uzlů, čtyři štítky úrovní
a všech20 pravděpodobností na hranách, včetně osmi dolních pahýlů.
U každé levé hrany sedí b/(r+b), u pravé r/(r+b); oba štítky se
sečtou na1. Úplná mapa je
`results/sequential/mpr-007-polya-figure.json`. Její dolní cíle jsou
označeny jako odvozené, protože jejich uzly už obrázek nezobrazuje.
Pólyův diagram se nezaměňuje s Friedmanovým diagramem v úloze74.

Popisek pod obrázkem je pravidlo násobení podmíněných pravděpodobností:
pro konkrétní cestu každý další faktor podmiňuje na celé dosavadní
historii. Urnové pravidlo závisí jen na jejím posledním stavu. Tím
P(cesta)=součin štítků; netvrdí se nezávislost tahů.

**Rovnoměrné rozdělení všech n+1 uzlů.** Cesta z (1,1) do (r,b)
má r−1 červených a b−1 černých tahů, n=r+b−2. Její čitatelé jsou
1·2···(r−1) a1·2···(b−1), její jmenovatele2·3···(n+1).
Proto má každá taková cesta pravděpodobnost

```
(r−1)!(b−1)!/(n+1)!.
```

Počet pořadí těchto tahů je C(n,r−1); jejich disjunktní součet je
1/(n+1). To platí i pro krajní r=1 či b=1 pomocí0!=1 a pro kořen
n=0. Uzly odpovídají všem r=1,…,n+1, je jich tedy přesně n+1
a jejich pravděpodobnosti mají součet1.

**Nepodmíněná pravděpodobnost další červené.** Průměr r/(n+2)
přes právě dokázané rovnoměrné uzly je

```
(1/(n+1)) Σr=1..n+1 r/(n+2) = 1/2.
```

Jde o nepodmíněnou hodnotu, nikoli o tvrzení, že každá větev má
pravděpodobnost1/2. Při r>b je další červená pravděpodobnější;
očekávaný nový rozdíl počtů je
(r−b)+(r−b)/(r+b), tedy původní rozdíl posílený kladným faktorem.
To dává konkrétní význam kvalitativní poznámce o přetrvávání nerovnováhy.

**Předstižení po první černé: úplný důkaz 2 ln2−1.** Podmiňme na
prvním černém tahu, jehož pravděpodobnost je1/2. Začínáme v (1,2).
Označme každý další červený tah +1 a černý−1. Počáteční rozdíl
červených minus černých je−1, takže první přísné předstižení nastane,
když součet nových přírůstků poprvé dosáhne2. To může být pouze
po2k tazích, k≥1, z nichž k+1 je červených a k−1 černých.

Po odstranění posledního +1 kroku mají přípustné cesty délku2k−1,
končí v1 a nikdy nepřekročí1. Bez tohoto omezení je jich
C(2k−1,k−1). Cestu, která dosáhne2, zrcadlíme až do prvního dosažení2
podle přímky výšky2: získáme cestu ze4 do1 stejné délky, a obráceně
každá taková cesta musí poprvé zasáhnout2 a lze ji zrcadlit zpět.
Těchto zakázaných cest je C(2k−1,k−2). Rozdíl je

```
C(2k−1,k−1)−C(2k−1,k−2) = (2k)!/(k!(k+1)!),
```

s obvyklou nulou pro záporný dolní index, takže k=1 je zahrnuto.
To je přímý důkaz potřebného Catalanova čísla, nikoli neověřený odkaz.

Jedna cesta s těmito počty tahů z (1,2) má pravděpodobnost

```
(1·2···(k+1)) (2·3···k) / (3·4···(2k+2))
 = 2(k+1)!k!/(2k+2)!.
```

Pro k=1 je druhý součin prázdný a rovná se1. Po vynásobení počtem
cest je pravděpodobnost prvního předstižení právě v čase2k rovna
2/((2k+1)(2k+2)). Tyto události jsou disjunktní. Pravděpodobnost
předstižení do konečného času je jejich konečný součet; jeho rostoucí
limita dává požadované „ever“ v témže smyslu limit konečných prostorů,
který kniha výslovně používá v odpovědi88 na str.383. Proto

```
Σk≥1 2/((2k+1)(2k+2))
 = 2 Σk≥1 (1/(2k+1)−1/(2k+2)) = 2 ln2−1.
```

Identita alternující harmonické řady s ln2 plyne integrací konečné
geometrické řady na[0,1]; zbytkový integrál má absolutní hodnotu
nejvýše1/(M+2) po M+1 členech a jde k0. Pro číselné zaokrouhlení
se použije ln2=2Σj≥0 (1/3)^(2j+1)/(2j+1), z integrálu2/(1−u²)
na[0,1/3]. Šest členů a geometrická horní mez ocasu potvrzují
0.38629<2 ln2−1<0.38630, tedy tištěné ≈.386.
Doklad je `results/sequential/mpr-006-log2-bound.json`.

Z kořene (1,1) první červená už vítězí; po první černé platí právě
odvozená hodnota. Nepodmíněná pravděpodobnost předstižení je proto
1/2+(2 ln2−1)/2=ln2. Tím je pokryta MPR88(a), včetně významu
ostrého S>1/2: sup je >1/2 právě tehdy, když to platí pro některý
konečný člen. Části88(b,c) a další tvrzení o supremu na konci odpovědi
se nepřebírají; celá úloha88 zůstává partial.

**(27), obě barvy a martingalový mezikrok.** X0=1 a Xj pro j>0
je indikátor červeného tahu. Po n tazích je počet červených
R=Σj=0..n Xj=1+Σj=1..n Xj. Počet černých je
1+Σj=0..n(1−Xj)=1+n−Σj=1..n Xj. Jejich součet je n+2,
jak text potřebuje. Je-li současný stav (r,b), očekávaný nový poměr je

```
[r/(r+b)] [(r+1)/(r+b+1)] + [b/(r+b)] [r/(r+b+1)]
 = (r²+r+br)/((r+b)(r+b+1)) = r/(r+b).
```

To ověřuje každý tištěný mezikrok. Poměr Zn=R/(n+2) je funkcí
dosavadních X a leží v[0,1], takže je integrabilní a splňuje (28).
Podle D098 je tedy martingale i vzhledem k vlastní historii.

## D098 — str. 7, férovost, filtr informace a celé MPR77

**Věžová identita pro dvě historie.** Nechť H je funkcí K a W je
integrabilní. Pro každou hodnotu h s kladnou pravděpodobností
rozdělme její vlákno na disjunktní vlákna K=k. Vážený průměr
E(W|K=k) s vahami P(K=k)/P(H=h) je přesně součet W(ω)pω/P(H=h)
přes celé H=h. Absolutní konvergence zaručuje přeskupení, a proto

```
E(E(W|K)|H) = E(W|H).
```

Nulová vlákna doplňuje již vyhlášená konvence; žádná pravděpodobnost
ani očekávání na nich nezávisí. Podmíněné rovnosti v martingalových
argumentech se používají na realizovatelných historiích, tedy skoro
jistě. U všech zdejších konečných protipříkladů jsou atomy kladné.

**(28)⇒(26), (29)⇒(30).** Položme K=(X0,…,Xn), H=(Z0,…,Zn).
Adaptovanost znamená H=g(K). Věžová identita a (28) dávají

```
E(Zn+1|H)=E(E(Zn+1|K)|H)=E(Zn|H)=Zn.
```

Tištěný důkaz MPR77 nejprve vloží do podmínění H iK; to je stejné
jako K právě díky adaptovanosti celé historie. Následující odstranění
vnějšího podmínění Zn je oprávněné, protože Zn je souřadnicí H.
Pro férové Y se namísto Zn na pravé straně objeví0, takže
E(Yn+1|Y0,…,Yn)=0 úplně stejným argumentem. To dokazuje oba výroky
hlavního textu. Definice bez pomocné posloupnosti lze použít přímo;
vždy lze také zvolit vlastní historii jako pomocnou.

**F158, chybná doplňující věta v odpovědi77.** Celé zadání a celé
řešení77 byly porovnány s originálem na19,381–382 a s autorovým PS.
Jeho parentetické tvrzení o libovolném martingalu a konstantní pomocné
posloupnosti neplatí. Z0=0, Zn=ξ pro n≥1, kde ξ=±1 férově,
je martingale; konstantní informace jej nemůže současně adaptovat
a splnit první podmíněnou rovnost. To platí i pro pomocnou posloupnost
Xn=Y s jednou pevnou náhodnou proměnnou Y. Přesný důkaz a rozsah
opravy jsou v `notes/F158-martingale-constant-information.md`.
Výrok, že nefunguje *každá* pomocná posloupnost, zůstává správný.
Celá úloha77 má s touto lokální opravou uzavřený rozbor.

**(29), (30) a ekvivalence s přírůstky.** Férovost vyžaduje nulovou
podmíněnou střední hodnotu členů Yn+1 pro n≥0; nevyžaduje EY0=0.
Pro Yn=Zn−Zn−1, n>0, Y0=Z0 je každý Yn funkcí historie Z a
integrabilní jako rozdíl dvou integrabilních členů. Linearita dává
E(Yn+1|Z0,…,Zn)=Zn−Zn=0, přesně tištěný výpočet. Obráceně
Zn=Σj=0..n Yj je integrabilní a adaptovaný na Y; jeho další
podmíněné očekávání je Zn+0. Předchozí implikace v obou směrech
dovolují přejít k vlastní historii. Teleskopický součet znovu vrátí
původní Zn, tedy jde skutečně o ekvivalentní popis.

**Nezávislé nuly a předvídatelné násobení.** Je-li Yn+1 nezávislé
na celé předchozí historii a EYn+1=0, každé kladné podmínění má
stejné rozdělení jako nepodmíněné; tím je posloupnost férová.
Pro Y′n=fn(X0,…,Xn−1)Yn je faktor na každé historii do n−1 pevné
číslo. Podmíněné očekávání je proto tento faktor krát0. Předpoklad
E|Y′n|<∞ odůvodňuje všechny součty; fn nemusí být omezená jednou
konstantou, pokud součin zůstane integrabilní. Pro n=0 lze f0 chápat
jako konstantu, ale férovost žádnou podmínku na počáteční člen neukládá.
Důležité je, že fn nesmí používat nový Yn: pro férový bit Yn=±1
by volba fn=Yn vytvořila Y′n=1 a zničila férovost. Pokud fn=0 pro
všechna n od jistého bodu, všechny další přírůstky jsou0 a součet se
stane konstantním, jak text tvrdí.

**(31) a přesný význam indexu.** Pravidlo Nn má hodnotu0 nebo1,
závisí pouze na minulosti před krokem n a po první nule zůstává nulové.
Každá realizace má tedy prefix jedniček délky N, po němž následují
nuly; možná je i nekonečná délka. Proto
N=Σn≥1 Nn∈{0,1,…,∞} a Nn=[N≥n]. N0=1 je konvence pro počátek,
který se nezapočítává do počtu kroků. Tím je vysvětleno i autorovo
upozornění, že indikátor znamená spíš pokračovat než zastavit.
Zastavení je předvídatelné v potřebném smyslu: rozhodnutí, zda provést
krok n, nepoužívá jeho nový náhodný výsledek.

## D099 — str. 8, zastavení, Ace Now a submartingaly

**Zastavený proces a quit-when-ahead.** Pro Y′0=Y0 a Y′n=NnYn
je násobení předvídatelné a |Y′n|≤|Yn|. Je to tedy férový přírůstek.
Součet má bodově tvar

```
Z′n = Y0+Σj=1..n [N≥j]Yj = Zmin(n,N),
```

kde pro N=∞ znamená pravá strana Zn. Po zastavení se už nemění.
Pravidlo Nn+1=[Z′n≤0] pokračuje při nulovém či záporném zůstatku
a poprvé přestane při kladném. Poté kladný zůstatek zůstává stejný,
takže pravidlo už nepřepne zpět na1. Splňuje tudíž i požadovanou
absorpci nul, nejen závislost na historii.

**Omezené zastavení a indexová poznámka.** Pokud N≤m,
Z′m=ZN=Z′N. Z′ je martingale a opakovaná věžová identita dává
EZ′m=EZ′0=EZ0, což dokazuje všechny rovnosti a závěr textu.
Žádná limita v m ani neoprávněné nezávislé podmínění na N se nepoužívá.
Přesně N_m≡0 znamená N≤m−1, zatímco N≤m znamená N_{m+1}≡0.
Textův vysvětlující dovětek s N_m proto dává o krok silnější postačující
podmínku. Například N1=1,N2=0 má N=1, ale N1≠0. V kontextu volby
libovolného konečného horního omezení lze m zvětšit o1; hlavní věta
ani následující rovnosti se nemění. Rozdíl přesných indexů je zde
transparentně uveden jako kontextová poznámka, nikoli nová karta.

**Ace Now, všechny strategie.** Po k odkrytých kartách, 0≤k≤51,
nechť A je počet zbývajících es a C=52−k počet zbývajících karet.
V rovnoměrně promíchaném balíčku je příští eso s pravděpodobností A/C.
Pro C≥2 je očekávaný nový podíl

```
(A/C)(A−1)/(C−1) + (1−A/C)A/(C−1) = A/C.
```

Vzorec je platný i pro A=0 nebo A=C; nemožná větev má koeficient0.
Proces podílů je tedy martingale až do51 odkrytých karet, pak jej lze
ponechat konstantní. Nepoužívá se poměr0/0 po odstranění poslední
karty. Strategie rozhoduje podle minulých karet a musí zastavit před
posledním odkrytím; počet N předem odkrytých karet je0 až51.
Omezené zastavení dává E(A_N/C_N)=4/52=1/13. Podmíněný čistý zisk
při volbě další karty je12·A_N/C_N−1·(1−A_N/C_N)=13A_N/C_N−1.
Jeho očekávání je0 pro každou strategii. Nejlepší i nejhorší strategie
jsou tedy z hlediska očekávaného zisku rovnocenné; pravděpodobnost
výhry je vždy1/13. To odpovídá všem otázkám hlavního textu a odkazu82.
Celá tištěná odpověď82 včetně doplňující zobecněné urny ještě není
samostatně převzata jako úplný rozbor úlohy.

**(32), oba směry a monotónnost očekávání.** Submartingale je
integrabilní a má podmíněný přírůstek≥0; supermartingale≤0.
Pokud platí oba směry, je to rovnost, tedy martingale. Očekávání
podmíněné nerovnosti a věžová vlastnost dávají EZn+1≥EZn,
respektive≤. Jde o neklesání/nerůst, nikoli nutně ostrou změnu;
konstantní martingale je již v textu případem obou.

**Konvexní transformace, správný důkaz.** Pro martingale Z a konvexní
f předpokládejme, že všechna f(Zn) jsou integrabilní. Při H=(Z0,…,Zn)
dává podmíněný Jensen

```
f(Zn)=f(E(Zn+1|H)) ≤ E(f(Zn+1)|H).
```

Historie G=(f(Z0),…,f(Zn)) může obsahovat méně informace než H.
Je proto nutné *obě strany znovu podmínit na G*. Levá je už funkcí G;
věžová vlastnost na pravé dává E(f(Zn+1)|G). Výsledkem je přesně
submartingalová nerovnost pro f(Zn).

**F159 v odpovědi84(a).** Originál odpovědi označí pravou stranu
před druhým podmíněním rovnou té po něm. To je nepravdivý mezikrok:
tři kladné atomy (Z0,Z1)=(-1,-1),(1,0),(1,2) s vahami1/2,1/4,1/4
a f=z² dávají E(Z1²|Z0)=1 či2, ale E(Z1²|Z0²)=3/2.
Všechny předpoklady martingalu jsou splněny. Správná nerovnost
zůstává1≤3/2. Viz `notes/F159-convex-martingale-conditioning.md`.
Chyba patří jen odpovědi na382, ne hlavní větě na8 ani zadání na20.

**Všechny vyjmenované konvexní transformace.** Pro |z| plyne
|pz+qw|≤p|z|+q|w| z trojúhelníkové nerovnosti. Maximum dvou
afinních funkcí z,c je konvexní, protože každá hodnota v kombinaci
je≤odpovídající kombinace jejich maxim. Konvexitu z²,e^z, z³ na
(0,∞),1/z,ln(1/z) a z ln z již dokazují konkrétní derivace v D095
(pro z³ druhá derivace6z≥0). Každý vyjmenovaný příklad proto splňuje
závěr, když existuje jeho očekávání. Samotná integrabilita Zn by
např. nezaručovala integrabilitu e^Zn; obecná podmínka existence
očekávání se nepomíjí. Kladnost Z je u poslední čtveřice přesně doména
zde použitých konvexních funkcí.

**Doplněný rozsah MPR84(b).** Je-li Z jen submartingale a f je navíc
neklesající, máme f(Zn)≤f(E(Zn+1|H))≤E(f(Zn+1)|H); opět podmíníme
na G a získáme submartingale. Bez monotónnosti to obecně neplatí:
deterministické Z0=0,Zn=1 pro n≥1 je submartingale, ale pro f(z)=−z
je první očekávaný přírůstek−1. Obecně jakýkoli pokles f(x)>f(y)
při x<y dává stejný dvoustavový protiargument. Tím jsou části(a,b)
zadání i podstatná odpověď posouzeny. Doplňující Gilatovo tvrzení,
že každý nezáporný submartingale má reprezentaci jako absolutní
hodnota martingalu, zde však nemá převzatý přesný důkaz ani pramenné
ověření předpokladů. **Celá MPR84 zůstává partial.** To je matematická
mezera auditu, nikoli nová chyba, a není zamaskována bibliografickou výjimkou.

**Zastavení submartingalu a poslední odstavec.** Označme
ΔZk=Zk−Zk−1. Předvídatelný indikátor Nk je nezáporný, takže
E(NkΔZk|minulost)=Nk E(ΔZk|minulost)≥0. Zastavený proces je tedy
opět submartingale, s integrabilními členy. Pro N≤m navíc

```
Zm−ZN = Σk=1..m (1−Nk)ΔZk.
```

Každý člen má nezáporné očekávání, protože1−Nk je opět známý
v minulosti. Konečný součet proto dává EZm≥EZN=EZ′N=EZ′m,
přesně řetězec v textu. Nevyžaduje nezápornost samotných Zk.
Zastavovací pravidlo zde smí používat tu historii, vůči níž platí
submartingalová podmínka; předem odhalená budoucnost by ji nesplňovala.

Poslední věta str.8 pokračuje rovnicí(33) na9. Její slibovaný důkaz
je již uzavřen: pro nezáporný submartingale a x>0 zastavíme při prvním
Zj≥x, nejpozději v pevném čase n. Pak ZN≥x·[max_{0≤j≤n}Zj≥x],
takže xP(max Zj≥x)≤EZN≤EZn. To je (33). Tím není posouzen zbytek
strany9, který bude následujícím blokem.

## Rozsah a další stav

- File26–28: reviewed s uvedenými bibliografickými výjimkami.
- MPR77: reviewed s lokální opravou F158; celé zadání i odpověď
  a analogie pro férovost mají vlastní argument.
- MPR84: partial, části(a,b) dokázány s opravou F159; Gilatova
  doplňující reprezentace zatím bez pramenného/důkazního převzetí.
- MPR88: partial, pouze(a) a konkrétní podmíněná hodnota hlavního
  textu uzavřeny; (b,c), další supremové meze a citovaná hlubší věta otevřené.
- Odkazy MPR63,67,82 byly posouzeny jen v rozsahu uvedeném výše;
  jejich registry se tímto blokem neprohlašují za celé reviewed.
- Historie názvu martingale, Doob1953, Eggenberger–Pólya1923 a
  historie hry Ace Now se bibliograficky vynechávají. Žádná potřebná
  matematická věta není těmito bibliografickými údaji nahrazena.
- F158/F159 mají původní PDF, autorův PS, přesné kladné atomy a
  kontrolu všech šesti vrstev errat. Karty patří jen file402.
- Žádný dlouhý výpočet, starý test nebo census se znovu nespouštěl.
