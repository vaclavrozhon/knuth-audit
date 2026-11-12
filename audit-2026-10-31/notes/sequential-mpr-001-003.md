# MPR 1–3: definice a podmíněná střední hodnota

Podrobný blok D092–D094, kontrola 6. listopadu 2026. Originály
`images/sequential/file-021.png` až `file-023.png` byly zobrazeny.
Níže je argument pro každé matematické tvrzení v těchto třech stranách,
včetně nečíslovaných příkladů. Nejde o pouhý soupis rovnic.

## D092 — str. 1, pravděpodobnost a nezávislost

**(1), (2) a definice proměnné.** Pro konečnou nebo spočetnou Ω jsou
nezáporné váhy pω se součtem 1 pravděpodobnostním rozdělením. Pro
libovolné A⊆Ω je součet vah v [0,1]. Prázdná množina má součet 0,
Ω součet 1 a disjunktní sjednocení má součet součtů, protože všechny
členy jsou nezáporné. Zápis pomocí [ω∈A] přidává pouze nulové členy.
Pro funkci X na Ω mají její vlákna {ω:X(ω)=x} disjunktní sjednocení Ω;
proto uvedený vzorec pro P(X=x) opět definuje rozdělení. Obraz spočetné
Ω je nejvýše spočetný, i když hodnoty proměnné samy nemusejí být čísla.

**Všechny karetní příklady.** Model výslovně volí rovnoměrně 52!
permutací 52 rozlišitelných karet, nikoli libovolný fyzický způsob míchání.
Po fixování horní karty zbývá 51! permutací; tedy P(T=t)=1/52.
Čtyři esa dávají 4/52=1/13. Každá z 13 hodnot se vyskytuje ve čtyřech
barvách a každá barva ve 13 hodnotách: P(F=f)=1/13, P(S=s)=1/4,
P(F=f,S=s)=1/52. To dokazuje nezávislost podle (3) pro všechny f,s,
nejen pro pikovou dámu. Pro horní a spodní kartu je společná
pravděpodobnost 0 při t=b a 50!/52!=1/(52·51) při t≠b. Obě hodnoty
se liší od 1/52²; vytištěné „for any cards t and b“ je tedy správně.

**(3), k-násobná nezávislost a její směr.** (3) je definice společné
nezávislosti. Při 1≤k<n získáme k proměnných z libovolné skupiny k+1
sečtením společného rozdělení přes poslední hodnotu: pravá strana
se násobí součtem marginálních pravděpodobností 1. To dokazuje
(k+1)-wise ⇒ k-wise, včetně proměnných s nulovými hodnotovými
pravděpodobnostmi. Pro opačný směr vezměme k+1 bitů s rovnoměrným
rozdělením na vektorech sudé parity. Je jich 2^k. Každé přiřazení k
vybraných bitů má právě jedno doplnění, tedy pravděpodobnost 2^−k;
pro menší podmnožiny se nefixované bity sečtou. Všech k+1 bitů však
nemůže mít lichou paritu, kdežto součin jejich marginál dává každému
vektoru kladnou pravděpodobnost. Pro k=1 jsou obě marginály férové,
ale dva bity stejné; pro k=2 dostáváme konkrétní párově nezávislou
trojici. Další nezávislé bity dovolují n>k+1. Tvrzení o rozdílu k a k+1
používá obor 1≤k<n; pro k≥n by mluvilo o neexistujících skupinách.

Odkaz na úlohu MPR6 skutečně míří na konstrukci párové nezávislosti
na str.13. Úloha má i další požadavek; **tímto blokem se celá MPR6
neuzavírá**. Vlastní konstrukce výše dokazuje zdejší tvrzení bez opření
o dosud nezkontrolovanou odpověď. Rovnice (4) je posouzena s její
pokračující podmínkou ze str.2 níže.

## D093 — str. 2, podmínění a očekávání

**(4) a dva podmíněné prostory.** Pro P(B)>0 jsou nové váhy na B
pω/P(B), nezáporné se součtem 1. Součet na A∩B je proto přesně
P(A∩B)/P(B). Pro 0<P(B)<1 totéž platí pro doplněk B. Vytištěné
indikátory dovolují zapsat váhy na celé původní Ω, s nulami mimo větev.
Při P(B)=0 autor výslovně definuje P(A|B)=P(A), nejde o dělení nulou.
Tato konvence není informací o fyzicky pozorované nemožné události,
ale určitou úplnou definicí použitou dále v knize.

**(5), včetně krajů.** A je disjunktním sjednocením A∩B a A∩B̄.
Když mají obě větve kladnou hmotnost, dosazení (4) dá jejich součty.
Když P(B)=0, nezápornost vah dává P(A∩B)=0, P(A∩B̄)=P(A) a pravá
strana je P(A)·0+P(A)·1. P(B)=1 je symetrické. Takže „always“ je
s autorovou konvencí pravdivé, nikoli pouze pro vnitřní případ.

**(6), oba směry a všechny nuly.** Z nezávislosti indikátorů Ij=[Aj]
plyne pro libovolné J součinová pravděpodobnost všech jedniček v J,
protože ostatní hodnoty se sečtou. Obráceně rozdělme indexy na U,
kde předepisujeme jedničku, a Z, kde předepisujeme nulu. Potom

```
P(Iu=1 pro u∈U, Iz=0 pro z∈Z)
 = E(∏u∈U Iu ∏z∈Z (1−Iz))
 = ΣT⊆Z (−1)^|T| P(∩j∈U∪T Aj)
 = ∏u∈U P(Au) · ΣT⊆Z (−1)^|T| ∏t∈T P(At)
 = ∏u∈U P(Au) ∏z∈Z (1−P(Az)).
```

Toto je přesně (3) pro každý nulajedničkový vzor. Všechny součty jsou
konečné; žádná pravděpodobnost se nedělí, proto jsou dovoleny i 0 a 1.
Pro J=∅ znamenají průnik Ω a prázdný součin 1. Odkaz na MPR20 na14
obsahuje právě tento momentový předpoklad pro binární proměnné;
jeho tištěná odpověď se posoudí při průchodu úloh.

**Dvě události a podmíněná rovnost.** Při P(B)>0 je
P(A|B)=P(A) ekvivalentní P(A∩B)=P(A)P(B). Při P(B)=0 platí
obě rovnosti automaticky. Definice na (4) tedy podporuje vytištěnou
ekvivalenci i pro nulovou událost B.

**(7), absolutní konvergence a (8).** Předpoklad z textu je
Σω |X(ω)|pω<∞. Rozdělení Ω na vlákna hodnot dovoluje absolutně
konvergentní řadu přeskupit; získáme Σx xP(X=x). Pro komplexní
hodnoty je argument stejný. Indikátor A je omezený, tudíž integrabilní;
jeho hodnota 1 na A a 0 jinde dává postupně přesně všechny tři součty
v (8) a nakonec P(A). Odkaz do §1.2.10 byl ověřen v originálu sv.1,
str.98, rovnice (2), obrázek `vol1-ref98.png`; zde přesto dokazujeme
potřebné přeskupení pro obecnou spočetnou Ω samostatně.

**Linearita a nezávislý součin.** Pro konečné k a integrabilní Xj platí
Σω |Σj Xj(ω)|pω ≤ Σj E|Xj|<∞. Záměna konečného a absolutně
konvergentního součtu dává EΣjXj=ΣjEXj bez nezávislosti. Při společné
nezávislosti má vektor hodnot součinové rozdělení. Nezáporný součet

```
Σx1,…,xk |x1···xk| ∏j P(Xj=xj) = ∏j E|Xj| < ∞
```

se faktorizuje postupným sčítáním nezáporných řad. Tím je součin
integrabilní a stejná faktorizace absolutně konvergentní řady bez
absolutních hodnot dokazuje E∏jXj=∏jEXj. Pouhá párová nezávislost
pro k>2 nestačí; tisk říká, že proměnné jsou nezávislé, tedy podle (3).

**(9), kovariance a rozptyl.** Je třeba, aby EX,EY,E(XY) existovaly
v uvedeném absolutním smyslu. Například square-integrable X,Y to
zaručují, protože 2|XY|≤|X|²+|Y|². Potom pro m=EX,n=EY:

```
E((X−m)(Y−n)) = E(XY−nX−mY+mn)
              = E(XY)−nm−mn+mn = E(XY)−mn.
```

Samotná integrabilita X,Y by integrabilitu XY nedávala; nečteme tedy
větu mimo již vyhlášenou podmínku existence očekávání. Pro reálné X
je (X−EX)² nezáporné a jeho očekávání je nezáporné, pokud je rozptyl
definován. Pro komplexní X tato bilineární definice nepoužívá komplexní
sdružení a nezápornost se netvrdí. Odkaz na §3.3.2 souhlasí s originálem
sv.2 str.67 dole, `vol2-ref67.png` (file79; OCR dělení stran má jiný
offset). Kontrola odkazu neuzavírá tamní empirický test ani jeho tabulku.
Známá úprava zápisu (E XY)→E(XY) se eviduje jako E114, nikoli nový nález.

**(10), oba součty.** Pro P(A)>0 dává podmíněné rozdělení na A
E(X|A)=Σω∈A X(ω)pω/P(A). Absolutní součet je nejvýše E|X|/P(A),
takže přeskupení podle X=x je oprávněné a dává druhý tištěný součet.
P(A)=0 řeší výslovná věta na začátku str.3 volbou EX. Žádný řetěz
s dělením nulou se v (10) neuplatňuje, protože je definice doplněna
právě touto výjimkou.

## D094 — str. 3, věžová vlastnost a pevná váha bitového slova

**(11), oba mezikroky.** Pišme By={Y=y}, qy=P(By). Pro qy>0
je qy E(X|By)=Σω∈By X(ω)pω; pro qy=0 je příspěvek 0, jak podle
konvence E(X|By)=EX, tak podle nulových vah na By. Vlákna rozdělují Ω,
a navíc Σy |qyE(X|By)| ≤ E|X|. Sečtením tedy dostaneme první rovnost
(11). Uvnitř každého nenulového vlákna použijeme (10); nulové vlákno
má autorovo rozdělení P(X=x|By)=P(X=x), jeho očekávání je EX a
součin s qy je opět 0. Druhá rovnost je tudíž také správná pro každé y.

**(12), význam náhodné proměnné a (13).** Definujme
g(y)=E(X|Y=y) s předchozí konvencí v nulových vláknech. Proměnná
G(ω)=g(Y(ω)) je funkcí na celé Ω, stálou na vláknech Y. Platí
E|G|=Σy qy|g(y)|≤E|X| a E G=EX podle (11), což dokazuje (12).
Je-li Y binární, G může nabývat dvou hodnot g(0),g(1); obecně není
konstantou g(1). Například férový bit X=Y má G=Y, kdežto E(X|Y=1)=1.
To konkrétně ověřuje obě varování ve výkladu.

Pro qY(ω)>0 dosazení (10) do g(Y(ω)) dává přesně čitatel a jmenovatel
(13). Stejný argument pro vektor (Y1,…,Yr) dokazuje uvedené zobecnění
na současně fixované hodnoty. Nulové vlákno je už určeno předchozí
konvencí: G(ω)=EX, pokud qY(ω)=0; jinak platí zobrazený podíl (13).
Text nový zápis výslovně zavádí jako přepsání (11), takže jej není důvod
chápat jako zrušení konvence z horní části téže stránky. Dvouatomový
příklad ukazuje pouze potřebu této již uvedené větve, nikoli dva různé
definované výsledky. Původní podezření C045 bylo po druhém posouzení
celé návaznosti **dismissed**, viz `notes/C045-zero-mass-conditioning.md`.
Tím je (13) i jeho vektorová verze bodově uzavřena na celé Ω.

**Počet bitových vektorů a EX1.** Pro celá n≥0 a 0≤m≤n volí každá
podmnožina m z n pozic právě jeden bitový vektor, tedy je jich C(n,m).
Rovnoměrné rozdělení je invariantní vůči permutacím pozic. Pro n≥1
jsou proto všechna EXj stejná a ΣjEXj=EΣjXj=m; tedy EX1=m/n.
Krajní m=0 a m=n dávají deterministické nuly a jedničky. Pro n=0
neexistuje X1 a obecná (14) nemá žádný index, takže se m/n neužije.

**X2 a (14), včetně nemožných prefixů.** Podmiňme na konkrétním
prefixu délky k−1, který má r jedniček a nenulovou pravděpodobnost.
Zbývá N=n+1−k≥1 pozic a s=m−r jedniček, 0≤s≤N. Každé z C(N,s)
doplnění mělo původně stejnou pravděpodobnost, a po podmínění je
tedy opět rovnoměrné. Symetrie pozic a konstantní součet s dávají
E(Xk|prefix)=s/N. Alternativně pro 1≤s≤N je podíl počtů
C(N−1,s−1)/C(N,s)=s/N; při s=0 je počet vhodných doplnění 0.
Pro k=1 jde o EX1, pro k=n je poslední bit determinován. Pro k=2
a n≥2 vznikají obě vytištěné větve m/(n−1) a (m−1)/(n−1).
Pokud m=0 nebo m=n, jedna z formálních větví není dosažitelná;
tisk ji nepotřebuje hodnotit, protože žádné ω má tento prefix.
Na prostoru přípustných vektorů mají všechna ω kladnou hmotnost a
každý skutečný prefix je přípustný. Rovnost náhodných proměnných
v závěrečné větě je tudíž bodová, nikoli jen skoro jistá.

Závěrečný odstavec „Inequalities“ pouze oznamuje následující metody;
žádná další kvantitativní mez na této straně není. Na těchto třech
stranách nejsou obrázky, tabulky ani algoritmy s dalším invariantem
nebo nákladovou povinností.

## Rozsah, zdroje a stav

- File21 a22: reviewed; matematické důkazy výše, vnitřní odkazy
  posouzeny. Úlohy6/20 a vzdálené stránky jiných svazků se samy
  za reviewed neoznačují.
- File23: reviewed. Nulová vlákna v (13) řeší výslovná předchozí
  konvence, C045 je dismissed; všechna tvrzení mají uzavřený argument.
- E114: známá redakční změna (9) z25.12.2022, potvrzená původním
  TeX a obrazem `images/sequential/all4b-03.png`.
- Při posuzování C045 zobrazen také autorův původní Pre-Fascicle5A, tištěná3,
  file9, `images/sequential/fasc5a-09.png`; zápis a nulová konvence stejné.
- Šest vrstev errat s SHA256, okolní opravou a negativním výsledkem
  pro (13): `results/sequential/mpr-001-003-errata.json`.
- Žádný dlouhý výpočet, starý test ani census se nespouštěl.
