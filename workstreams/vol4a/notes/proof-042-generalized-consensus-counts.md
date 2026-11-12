# Úlohy 7.1.1–32 a 33: zobecněný konsensus a počty prvoimplikantů

Checkpoint X0071, P0670–P0678. Originál: zadání p83/file100,
odpovědi p539–540/file556–557, obrazy file100.png,
proof-file556.png, file557.png. Nový matematický program nebyl potřeba.
Krychle jsou neprázdné kartézské součiny symbolů 0, 1, *; prázdná
rodina může reprezentovat nulovou funkci. Počítáme indexované vstupní
termy, takže duplicity nemohou porušit horní mez.

## 32(a): jediný možný konsensus — P0670

Čtyřsymbolová operace odpovědi má jednoduchý model: symboly
*, 0, 1, • reprezentují množiny ∅, {0}, {1}, {0,1}; operace ⊔
je sjednocení těchto množin. Tím jsou dokázány všechny vytištěné
řádky tabulky, komutativita i asociativita bez závislosti na závorkách.
Mapa h vrací *, 0, 1, * v tomto pořadí. Pro rodinu c₁,…,cₘ, m≥1,
označme q=h(c₁⊔⋯⊔cₘ), po souřadnicích.

Nechť d je maximální krychle ve V=⋃cⱼ a pro každé j platí
d ⊄ ⋃_{i≠j}cᵢ. Každý člen tedy má v d soukromý bod: bod patřící
jen tomuto členu rodiny. Pro libovolnou souřadnici r jsou možnosti:

1. Všechny cⱼ mají *. Sjednocení V je v souřadnici r nezávislé;
   pokud by d měla pevnou hodnotu, její uvolnění by stále leželo ve V.
   Maximalita proto dává dᵣ=*.
2. Mezi pevnými hodnotami se vyskytuje pouze x∈{0,1}, alespoň jednou.
   Hodnota dᵣ=1−x by znemožnila soukromý bod každého člena s hodnotou x.
   Ani dᵣ=* není možné: řez d s hodnotou 1−x musí pokrýt členové
   mající v r hvězdičku. Tyto členy vůbec nezávisí na r, takže pokryjí
   i druhý řez, a tedy celé d. Člen s pevným x pak nemá soukromý bod.
   Zbývá dᵣ=x.
3. Vyskytuje se pevná 0 i pevná 1. Pevná hodnota dᵣ by se minula
   s některým členem, což opět vylučuje jeho soukromý bod. Proto dᵣ=*.

Ve všech souřadnicích nutně d=q. To je obecný důkaz nejvýše jednoho
objektu požadovaného v zadání; existence se z něj neodvozuje.
Pro m=1 je výsledkem právě c₁. Duplicita dvou členů znemožní
nezbytnost každého z nich. Nulární krychle nic nemění: podmínku
splní právě jednoprvková rodina této krychle.

Pro m=2 je tato definice totožná s obyčejným konsensem z 31:
podmínka říká, že krychle není obsažena ani v jednom rodiči.
Jedinou největší takovou krychli a její maximalitu dokládá
proof-041-consensus-algorithm-e.md, P0663/P0664; důkaz se neopakuje.

## Známá oprava a její přesný rozsah — P0671

all4a-pre, p540 řádky 2–3, 19.6.2011, nahrazuje původní
„iff contained“ pouze tvrzením, že q je jediná možná krychle.
Je to skutečné zeslabení. Například pro 0* a *0 vznikne q=00,
která leží ve sjednocení, ale je obsažena v každém původním členu.
Není tedy ani maximální, ani nezbytně pokrytá oběma členy.
Tento již evidovaný příklad a známou chybu nepovažujeme za nový nález.

Příslušné vrstvy all4a-pre, all4a, err4a, all4f0, err4f0
byly nyní prohledány podle stran i výrazů consensus/compatibility,
včetně OCR tvarů; navíc obě vrstvy F1. Pro odpověď 32 nebyla nalezena
další matematická oprava. P120 má jen opravu odkazu z roku 2021.

Vztah ke C0002 je nyní přesný: oprava nemění definici 32(a), ani
nevytváří konsensus kompatibilní dvojice. Souřadnicový výpočet q je
ovšem pro kompatibilní rodinu právě její neprázdný průnik. P120
bylo znovu otevřeno v původním obrazu file137-detail.png: užívá název
„generalized consensus“ a odkaz na úlohu 32. Doslovný definovaný objekt
nemusí existovat; pokud název volně označuje souřadnicový kandidát q,
zamýšlený argument funguje. C0002 proto zůstává přesně touto
terminologickou nejistotou, nikoli novou chybou známé odpovědi.
Bipartitní charakterizace je platná pomocí průniku, jak již dokládá
C0002-compatible-consensus.md.

## 32(b): všech 2^m−1 podrodin — P0672

Vytištěná konstrukce má proměnné y₁,…,yₘ,x₁,…,xₘ a členy

    cⱼ = [yⱼ=1, x₁=⋯=xⱼ₋₁=1, xⱼ=0],   1≤j≤m.

Jde přesně o řetězec *^(j−1) 1 *^(m−j) 1^(j−1) 0 *^(m−j).
Pro neprázdnou množinu indexů S položme t=max S. Souřadnicový
kandidát d_S má tyto a jen tyto pevné souřadnice:

    yᵢ=1 pro i∈S;
    xᵢ=1 pro i<t, i∉S;
    x_t=0.

Pro i<t v S se vyskytuje 0 z cᵢ a 1 z c_t, proto je tam *;
všechny ostatní souřadnice jsou také určeny přesně výše uvedenými
třemi případy operace. To ověřuje celý vzorec pro libovolné S.

Každý bod d_S má mezi indexy S nějaké xⱼ=0, protože x_t=0.
Vyberme nejmenší takový index j. Pro i<j je xᵢ=1: buď i∈S
a jde o minimalitu j, nebo i∉S a jde o pevnou podmínku d_S.
Také yⱼ=1. Bod tedy patří cⱼ a d_S⊆⋃_{j∈S}cⱼ.

Každý cⱼ je potřebný: v d_S zvolíme x₁,…,xⱼ₋₁=1 a xⱼ=0.
Zbývající pevné souřadnice tomu neodporují, včetně x_t=0.
Takový bod patří cⱼ a žádnému jinému členu, protože různé členy
požadují různou pozici první nuly v x.

Zvětšeme d_S na libovolnou maximální krychli q uvnitř ⋃_{j∈S}cⱼ;
ta existuje konečností. Soukromé body zůstávají v q, takže každý
člen je stále nezbytný. P0670 dává q=d_S. Tím jsou současně
dokázány existence i maximalita všech požadovaných konsensů.

## Poslední souřadnice je opravdu nadbytečná — P0673

Po vymazání xₘ z každého členu má poslední člen tvar
cₘ=[yₘ=1, x₁=⋯=xₘ₋₁=1]; ostatní se nezmění.
Pro max S<m se předchozí důkaz nemění. Pro max S=m je kandidát
d_S popsán stejnými podmínkami, ale bez posledního x_t=0.
Buď existuje nejmenší j∈S∖{m} s xⱼ=0 a bod kryje cⱼ, nebo mají
všechny souřadnice x hodnotu 1 a bod kryje cₘ.

Soukromý bod pro j<m má první nulu j, pro j=m má všechny x=1.
Zvětšení a P0670 opět dokážou maximalitu. Konstrukce tedy funguje
už v dimenzi 2m−1, včetně m=1, kdy zbývá jediná proměnná y₁.
Nejde jen o tvrzení, že lze souřadnici bez důkazu vypustit.

## 32(c): obecná horní mez — P0674

Nechť V=⋃_{j=1}^m cⱼ a p je libovolná maximální krychle V.
Vyberme podmnožinu S⊆{1,…,m}, která pokrývá p a je inkluzně
minimální. Je neprázdná a každý člen je pro pokrytí p nezbytný.
Navíc p je maximální i uvnitř ⋃_{j∈S}cⱼ, protože větší krychle
tohoto sjednocení by byla větší krychlí celého V. Je tedy konsensem S.

Zvolíme-li deterministicky například lexikograficky první takovou
minimální podrodinu, dostaneme z každého prvoimplikantu jeden
neprázdný S. Dva různé prvoimplikanty nemohou zvolit stejný S,
protože P0670 dovoluje jediný jeho konsensus. Jde o injekci, a proto
je počet prvoimplikantů nejvýše 2^m−1.

Tím je upřesněn stručný výraz odpovědi, že prvoimplikant „meets“
podmnožinu termů. Není potřeba a netvrdíme, že minimální pokrytí
je samo jednoznačné, ani že jde o všechny termy s neprázdným
průnikem. Například ** lze minimálně pokrýt 0*,1* nebo *0,*1;
jednoznačnost potřebná v důkazu jde opačným směrem: podrodina
určuje nejvýše jeden prvoimplikant. Uvozovkový neformalizovaný
výraz nepovyšujeme na samostatný nález; požadovaná mez má úplný důkaz.

Prázdná DNF má nula prvoimplikantů a splňuje 2^0−1=0. Konstantní
pravdivá funkce má jedinou maximální krychli a mez také splňuje.

## 32(d): přesně 2^m−1 prvoimplikantů celé funkce — P0675

Funkce v odpovědi je právě disjunkce členů cⱼ z P0672. To samo
o sobě ještě nestačí: maximalita d_S v menší podrodině nezaručuje
maximalitu v celé rodině. Následující svědci dodávají chybějící krok.

V d_S nastavme yᵢ=0 pro i∉S. Každé možné uvolnění jedné jeho
pevné souřadnice vpustí bod mimo celou funkci:

- Při uvolnění yⱼ, j∈S, zvolíme yⱼ=0 a první nulu v x na místě j.
  Jediným možným aktivním členem je cⱼ, ale jeho yⱼ je nula.
  Ostatní podmínky d_S zůstávají splněny, včetně x_t=0.
- Při uvolnění xᵢ=1, i<t, i∉S, zvolíme první nulu právě i.
  Jediným možným členem je cᵢ a yᵢ=0.
- Při uvolnění x_t=0 zvolíme všechny x=1. Pak neplatí žádný člen.

Kdyby existovala větší krychle ve V, obsahovala by i některé takové
jednosouřadnicové uvolnění, což je spor. Všechna d_S jsou tedy
prvoimplikanty celé funkce. Jsou navzájem různá, protože jejich
množina pevně jedničkových souřadnic y je přesně S. Je jich nejméně
2^m−1; P0674 poskytuje opačnou mez, a tím úplný přesný počet.

I varianta s odstraněným xₘ má stejný počet: první dva druhy svědků
zůstávají; pro j=m je soukromý x-vzor samé jedničky. Je-li t<m,
při uvolnění x_t=0 zvolíme samé jedničky, ale yₘ=0, protože m∉S.
Je-li t=m, žádná pevná souřadnice x_t se již neuvolňuje.

To dokládá exponenciálně velký výstup uváděný v dodatku k algoritmu P
odkazem na úlohu 32. Odkaz na 116 a průměrná tvrzení 34 se tím
neuzavírají; P0662 zůstává v tomto užším rozsahu partial.

## 33(a): pravděpodobnost implikantu — P0676

Položme N=2^n, s=2^(n−k), 0≤k≤n, 0≤m≤N. Náhodný experiment
je rovnoměrný výběr m-prvkové pravdivé množiny z N bodů, nikoli
nezávislé volby s pravděpodobností m/N. Term x₁∧⋯∧x_k označuje
pevnou krychli C₀ velikosti s. Je implikantem právě tehdy, když
všech s bodů patří do výběru. Zbývajících m−s bodů lze zvolit
z N−s bodů, takže pravděpodobnost je

    binom(N−s,m−s) / binom(N,m).

Binomický koeficient s dolním indexem mimo 0,…,horní index je nula.
Všechny horní indexy používané zde jsou nezáporné.

## 33(b): prvoimplikant a inkluze–exkluze — P0677

Pro každou z k pevných souřadnic má C₀ sousední krychli Cᵢ,
která se liší právě opačnou pevnou hodnotou této souřadnice.
Krychle C₀,C₁,…,C_k jsou po dvou disjunktní, každá velikosti s:
různí sousedé mají nulu na různých pozicích a na ostatních pevných
pozicích jedničku. C₀ není maximální právě tehdy, když je alespoň
jedna Cᵢ celá pravdivá. Každé větší nadkrychli předchází takové
jednosouřadnicové zvětšení, takže jde o nutnou i postačující podmínku.

Při vynucení l vybraných sousedů spolu s C₀ musí výběr obsahovat
(l+1)s různých bodů. Inkluze–exkluze proto dává přesně vytištěný součet

    Σ_{l=0}^k (−1)^l binom(k,l)
        binom(N−(l+1)s,m−(l+1)s) / binom(N,m).

N−(l+1)s≥0 plyne z l+1≤k+1≤2^k; indukce 2^k≥k+1 je platná
i pro k=0. Nulové koeficienty tak správně řeší i m<(l+1)s.

## Bodový případ a krajní domény — P0678

Při k=n je s=1. Daný bod musí být pravdivý a všech jeho n odlišných
sousedů musí být nepravdivých. Dalších m−1 pravdivých bodů se volí
ze zbývajících N−n−1, tedy

    binom(N−n−1,m−1) / binom(N,m).

To současně dokazuje zjednodušení součtu, bez formální manipulace
se střídavými koeficienty. Známý dodatek z 20.6.2011 pouze odkazuje
na rovnici 1.2.6–(24); zde je potřebná identita doložena přímým
počítáním a nezávisí na novém čtení této staré rovnice.

Pro k=0 je term prázdný součin, tedy celá krychle, a je prvoimplikantem
právě při m=N. Pro m=0 nevznikne žádný implikant. Pro n=k=0 je N=1
a oba vzorce dávají 1 při m=1 a 0 při m=0. Podmíněná či asymptotická
pravděpodobnost nebyla zaměněna za tento přesný konečný experiment.

## Úplná mapa p83 a hranice této kontroly

- Úvodní pokračování 31, všechny pravidlové vzorce, příklad bez konsensu,
  rozměrová mez a celý algoritmus E: P0663–P0669 v proof-041.
- 32(a), definice a přechod k m=2: P0670/P0671 s aplikovaným erratem.
- 32(b), včetně dodatku o poslední souřadnici: P0672/P0673.
- 32(c), přesný směr jednoznačnosti: P0674.
- 32(d), maximalita v celé funkci a úplný počet: P0675.
- 33(a)/(b), uzavřený tvar a všechny konečné domény: P0676–P0678.

To pokrývá všechny matematické věty a úlohy této stránky i odpovídající
části odpovědí. Odkaz na pozdější implementaci v 7.1.3–142 není použit
jako důkaz nákladů; zdejší operace mají vlastní explicitní realizaci
v P0669. P539 zůstává partial kvůli C0004 a průměrným tvrzením P0662;
p540 zůstává partial kvůli dosud neprověřené úloze 34.

Bibliografická výjimka: Tison 1967, Sloan–Szörényi–Turán 2008 (včetně
citovaného výsledku o klasifikaci všech konstrukcí), Chandra–Markowsky
1978 a Laborde 1980 nebyly ověřeny v primárních článcích. Žádný z jejich
externích výsledků není předpokladem uvedených důkazů. Historické
priority nejsou potvrzeny. Kromě známého errata nevznikl nový nález.
