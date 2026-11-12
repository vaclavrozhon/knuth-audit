# Úloha30: dualizace libovolného konečného posetu

Zadání68–69/file79–80 a odpověď611/file622. Originál69 zobrazen
v images/tableaux-file-080.png. Následuje celý obecný algoritmus,
jeho invariant i důkaz návratu. Nevyvozuje se z vlastností Youngových
tvarů. Využitý algebraický přístup je ověřen v primárním
[Stanleyho článku](https://math.mit.edu/~rstan/papers/evac.pdf), §2,
zejména Lemma2.2(a) a jeho propojení s promotion; všechny potřebné
kroky jsou zde rozepsány s vlastními invarianty a obory.
Zdroje a výslovná bibliografická hranice jsou v
sources/tableaux-poset-evacuation-source.json.

## P0538: algoritmus na obecném Hasseově diagramu a invariant

Nechť P je konečný poset a f:P→{1,…,n} bijekce, x<y⇒f(x)<f(y).
Při j-tém odstranění smažeme nejmenší zbývající štítek j. Jeho vrchol
je minimální v právě aktivním posetu. Dokud má díra u nějaké horní
pokrytí, vybereme z těchto vrcholů v ten s nejmenším štítkem, jeho
štítek přesuneme do u a díru posuneme do v. Při dosažení maximálního
vrcholu w jej odstraníme z aktivního posetu a do výstupu Φ(f)(w)
zaznamenáme j. Pokračujeme j+1.

Volba je jednoznačná, protože štítky jsou různé. Během jednoho
odstranění tvoří navštívené vrcholy řetězec u_0<u_1<…; jejich
původní štítky striktně rostou. Po kroku t je v u_s původní štítek
u_(s+1) pro s<t, v u_t je díra a všechny ostatní štítky jsou původní.

Po přesunu štítku v do u jsou všechny označené prvky pod u menší:
mimo cestu byly menší než původní štítek u, na cestě jsou nejvýše
rovny původnímu štítku u. Ten je menší než přesouvaný štítek v.
Pro označený prvek z>u vezměme nějaké horní pokrytí c s u<c≤z.
Volba nejmenšího štítku z pokrytí dává f(v)≤f(c)≤f(z);
pokud z není právě nová díra v, je aspoň jedna nerovnost přísná.
Relace ostatních označených prvků se nemění. Invariant proto
zachovává uspořádané označení všude mimo díru; po jejím odstranění
v maximálním vrcholu jde opět o úplné platné označení zbytku.

## P0539: ukončení a skutečně duální výstup

Každý posun díry jde přísně vzhůru, takže při r zbývajících vrcholech
má nejvýše r−1 posunů. Odstraní se právě jeden maximální vrchol a
zbytek je ideál původního P. Celá konstrukce končí po n odstraněních.

Je-li x<y v původním P, musí se y odstranit před x, protože x by
jinak nebyl maximální. Výstupní pořadová čísla odstranění proto
splňují Φ(f)(x)>Φ(f)(y). Jde o požadované duální označení.
Pro prázdný poset je výstup prázdný; singleton neprovádí žádný
posun. Nikde se nepředpokládá souvislost posetu nebo jediný minimální vrchol.

## P0540: přesně platné relace lokálních záměn

Lineární rozšíření zapisujme jako slovo w=(v_1,…,v_n), kde f(v_i)=i.
Operace τ_i prohodí sousední v_i,v_(i+1), jsou-li nesrovnatelné;
jsou-li srovnatelné, nechá slovo beze změny. Prohození nesrovnatelných
sousedů je znovu lineární rozšíření: jiné relativní pořadí se nezmění.

Platí τ_i²=1 a τ_iτ_j=τ_jτ_i pro |i−j|>1. První relace je dvojí
prohození nebo dvojí identita; ve druhé jde o disjunktní dvojice
pozic, jejichž srovnatelnost nemůže druhá operace změnit.
Žádná relace sousedních τ se nepředpokládá.

Všechny níže psané součiny se provádějí zleva doprava.
Položme δ_r=τ_1…τ_(r−1), δ_1=1.

## P0541: proč δ_n je právě jeden normalizovaný posun díry

Při aplikaci δ_n projde pořadí v_2,…,v_n zleva doprava, s aktuálním
„neseným“ vrcholem u, zpočátku v_1. Je-li následující v nesrovnatelný
s u, τ jej přesune o pozici doleva a u pokračuje. Je-li srovnatelný,
musí u<v, protože původní slovo je lineární rozšíření. Pak se u
ponechá na aktuální pozici a neseným vrcholem se stane v.

První takto nalezený v>u má nejmenší původní štítek mezi prvky nad u
a pokrývá u. Kdyby u<z<v, pak by se z díky svému menšímu štítku
zpracoval dříve a u by již nebylo neseno. Je to tedy přesně nejmenší
horní pokrytí z algoritmu P0538.

Při nesrovnatelnosti dostane v po normalizaci o1 menší vlastní štítek.
Při srovnatelnosti dostane u štítek v snížený o1 a díra přejde do v.
Na konci je nesený vrchol maximální a dostane n. Proto δ_n provádí
právě odstranění1, posuny do díry, zápis n+1 do poslední díry a
následné snížení všech štítků o1. Tím je dokázána vazba slova na
konkrétní pohyby, nikoli jen podobnost dvou známých operací.

## P0542: celá konstrukce a trojúhelníkový součin

Po δ_n zmrazíme štítek n v posledním vrcholu a na první n−1 pozic
použijeme δ_(n−1); zmrazíme n−1 a pokračujeme. Zmrazený vrchol byl
maximální, takže zbylé pozice jsou lineárním rozšířením zbylého ideálu.
Srovnatelnost dvou jeho vrcholů je stejná jako v původním P.

Celý výsledný řádný (nikoli duální) labeling je tedy E(f)=γ_n(f), kde

    γ_n=δ_n δ_(n−1) … δ_2, γ_0=γ_1=1.

Jeho záznamy jsou n,n−1,…,1, zatímco knižní Φ zapisuje1,2,…,n.
Pro bodový komplement C(a)=n+1−a proto platí přesně Φ=C E.
Průběžná normalizace aktivních štítků pouze mění jejich pořadové
hodnosti, takže volby nejmenších pokrytí jsou stejné.

## P0543: úplný algebraický důkaz γ_n²=1 bez dalších relací

Indukce po n začíná γ_0=γ_1=1. V součinu γ_n² po zrušení prostředních
dvojic τ_1,…,τ_(r−1) má zbytek přesný tvar

    δ_n δ_(n−1) … δ_(r+1) γ_(r−1)
       ·(τ_r τ_(r+1)…τ_(n−1)) γ_(n−1).                   (1)

Pro r=1 jde přímo o původní součin, protože γ_0=1.
Nyní δ_(r+1)=δ_r τ_r a γ_(r−1) používá pouze indexy≤r−2.
Levý τ_r tedy může přes celý γ_(r−1) komutovat k pravému τ_r,
oba se zruší a δ_r γ_(r−1)=γ_r. Zbytek je přesně(1) pro r+1.

Po r=n−1 zůstane γ_(n−1)², které je1 podle indukce. Důkaz používá
pouze relace P0540 a skutečně platí pro libovolný konečný poset.
Nejde o předpoklad relací symetrické grupy, které by zde nebyly doložené.

## P0544: opakování v obráceném číselném pořadí a Tableau specializace

Označme Φ_rev totéž pravidlo při opačném pořadí štítků: maže n,n−1,…,
volí největší číselný štítek horního pokrytí a zapisuje n,n−1,…
do postupně uvolněných míst. Pod bodovým komplementem všech štítků
se tato definice převede na původní pravidlo, tedy Φ_rev=C Φ C.
Z Φ=C E a C²=1 dostáváme

    Φ_rev Φ=C Φ C Φ=E²=1.

To je přesně návrat požadovaný v úloze. Není třeba obracet vztah
posetu; obrací se numerické porovnání a mazací pořadí štítků.

Pro Youngův diagram je poset dán souřadnicovými nerovnostmi.
Horní pokrytí buňky jsou právě existující buňka napravo a dole.
P0538 je tedy Algorithm S bez sentinelových míst mimo tvar.
Záznam skutečně uvolněného rohu dává knižní duální tableau;
známý vlastní nález C0005 o chybně uvedené výstupní souřadnici
se tím nemění ani znovu nepočítá.

## P0545: konkrétní další vlastnosti a náklady

- Isomorfismus posetů přenáší horní pokrytí i jejich štítky, takže
  komutuje s každým krokem a s celou Φ. Operace nezávisí na kresbě
  Hasseova diagramu.
- Na řetězci je E identita a Φ obrátí štítky1,…,n; při každém
  odstranění se přesune celý zbytek řetězce.
- Na antichainu se nic neposouvá a Φ ponechá každý původní štítek
  na místě; E je bodový komplement. Obě mezní rodiny potvrzují,
  proč je nutné odlišovat duální Φ od řádné E.
- Počet skutečných přesunů štítků je nejvýše
  (n−1)+(n−2)+…+0=n(n−1)/2 a řetězec této meze dosahuje.
  Alternativní slovní konstrukce provádí přesně n(n−1)/2 testů
  srovnatelnosti τ; čas jednoho testu závisí na reprezentaci posetu.
  Není zde bez předpokladů tvrzena jednotková cena libovolného
  dotazu na tranzitivní uzávěr.

To je konkrétní rozsah otevřeného pokynu „explore other properties“.
Neprohlašuje se za klasifikaci všech dalších identit nebo orbit.

Původní referenci Schützenberger1972 a celý obsah van Leeuwenova
§2 z1996 jsme nezávisle nepřezkoumali: primární PDF se načetlo,
ale cílené další načtení oddílu skončilo timeoutem. Bibliografická
výjimka neomezuje výše uvedený úplný argument. Stanleyho potřebné
definice, propojení a důkaz involutivity v §2 byly přečteny.
