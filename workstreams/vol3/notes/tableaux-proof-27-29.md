# Tableaux: úlohy27–29 a aktualizovaná odpověď611

Zadání68/file79 a odpovědi611/file622 byly zobrazeny v
images/tableaux-file-079.png a -622.png. U27 se přebírá již dokázané
obecné lemma o dvou insertion cestách P0445 a celá D(c) P0431;
u29 přesný sjednocovací odhad P0414. Neopakují se programy ani
hotové důkazy. U28 je výslovně použit hluboký externí výsledek,
s ověřenými předpoklady a odvozenými důsledky, nikoli tvrzení, že
jsme znovu provedli celou jeho analýzu Riemannova–Hilbertova problému.

## P0527: úloha27(a), obě implikace a rovnosti souřadnic

Nechť i je v buňce(r,c) a i+1 v(s,d) standardního tableau.
Pokud r<s a c<d, existuje buňka(r,d): horní řádek sahá alespoň tak
daleko jako spodní. Její hodnota je striktně mezi i a i+1, což je
nemožné pro po sobě jdoucí celočíselné štítky. Proto r<s nutí c≥d.

Naopak při r≥s a c≥d leží(i+1)-buňka severozápadně od i-buňky;
řádkový a sloupcový růst by dával i+1≤Q_(r,d)≤i. To je spor
a pokrývá i případ shodného řádku nebo sloupce. Tedy c≥d nutí r<s.
Právě sousednost štítků je v první implikaci nezbytná; toto tvrzení
se nepřenáší na libovolné dvě hodnoty.

## P0528: úloha27(b) a počet běhů

P0445 dokazuje pro dva po sobě vkládané různé klíče x,y do libovolného
původního tableau: je-li x<y, druhá nová buňka je striktně napravo
od první; je-li x>y, je slabě nalevo a striktně níže. V recording
tableau Q jsou tyto buňky označené i a i+1. Proto
a_i>a_(i+1) právě tehdy, když c_i≥c_(i+1), a podle P0527 právě tehdy,
když i je nad i+1. Tím jsou vyřízeny obě alternativy i celý prefix,
nikoli jen vložení do prázdného tableau.

Pro n≥1 je počet vzestupných běhů1 plus počet takových sestupových
indexů i; pro prázdný vstup je0. Z Q se tedy určí přesně, jak uvádí
závěr části(b).

## P0529: úloha27(c), dualita bez záměny pořadí

D(c) říká, že obrácení časů i hodnot dává recording tableau Q^S,
chápané v opačném pořadí štítků. Ve změněném vstupu přichází původní
čas i+1 bezprostředně před časem i; odpovídající hodnoty jsou
a_(i+1),a_i. Je to sestup v novém, opačném pořadí právě když
a_(i+1)<a_i v původním pořadí.

Pro použití části(b) lze nové časové štítky přeznačit na n+1−q.
Potom jsou původní i+1 a i po sobě jdoucí vzestupné časové štítky,
takže(b) říká: původní i+1 je nad původním i v Q^S právě při tomto
sestupu. Společně s původní(b) je to přesně požadovaná ekvivalence.
V Q^S se tedy omylem nepoužívají běžné rostoucí řádkové nerovnosti;
duální pořadí je skutečně zohledněno.

## P0530: přesně použitý externí výsledek pro úlohu28

Primární [Baik–Deift–Johansson, verze2](https://arxiv.org/pdf/math/9810105v2),
PDF2–3, Theorems1.1–1.2, se týká rovnoměrného rozdělení na S_n,
stejně jako zadání. Pro délku L_n nejdelší rostoucí podposloupnosti
a X_n=(L_n−2sqrt(n))/n^(1/6) dokazuje X_n⇒X a konvergenci všech
pevných kladných celočíselných momentů. Limitní rozdělení F je dáno
(1.4)–(1.6); zdroj a přesný rozsah převzetí jsou v
sources/tableaux-bdj-theorems.json.

Tento externí theorem je přijatá analytická závislost, nikoli
nezávisle zopakovaný důkaz všech60 stran článku. Následující aplikace
a rozlišení pravděpodobnostních modelů jsou ověřeny zde.

## P0531: požadovaný průměr, včetně momentové podmínky

Z konvergence prvního momentu je E X_n=E X+o(1), s konečným E X.
Tedy E L_n=2sqrt(n)+n^(1/6)(E X+o(1)), a po dělení2sqrt(n) jde
poměr k1. To je přesně úloha28. Samotná distribuční konvergence
by tento přechod k průměru neospravedlnila.

P0453 ztotožňuje L_n s délkou první řádky RSK tableau. Náhodný
vstup je rovnoměrná permutace, tedy rovnoměrný pár(P,Q) odpovídající
této permutaci; nejde o rovnoměrnou volbu samotného tableau.
Parentetická interpretace v zadání tak má správný pravděpodobnostní model.

## P0532: rozptyl a přesná Θ-mez z opravy2000

První a druhý konvergující moment dávají
Var(L_n)/n^(1/3)=Var(X_n)→Var(X). Limit je konečný a kladný:
F je netriviální spojité, striktně rostoucí rozdělení, jak plyne
z definice v primárním theorem. Proto směrodatná odchylka je
Θ(n^(1/6)), přesně jak nahrazuje známé erratum23.3.2000 starší
odstavec. Slabší O(n^(1/4)) je tím matematicky také důsledkem,
ale historický obsah Talagrandova článku ani simulace1994 se tím
nevydávají za znovu ověřené.

## P0533: limitní formule, znaménko a ostrá nerovnost v erratu

Článek volí řešení u~−Ai a knižní oprava volí v~Ai. Přechod v=−u
zachovává rovnici v''=2v³+xv a čtverec řešení. Limit v obou případech je

    F(t)=exp(−∫_t^∞ (x−t)v(x)² dx).

Znaménková konvence tedy není chyba. Rovněž knižní „less than“
a článek s≤ mají stejnou limitu: práh lze ohraničit hodnotami
t−δ a t pro každé pevné δ>0, použít distribuční konvergenci a pak
spojitost F při δ↓0. Je tím ošetřena i celočíselnost L_n, bez
nepravdivého tvrzení, že jednotlivé bodové pravděpodobnosti jsou přesně0.

## P0534: úloha29, přesný očekávaný počet a horní mez

Pro celé0≤l≤n má každá pevná l-tice pozic rostoucí hodnoty
s pravděpodobností1/l!, protože všechna jejich relativní pořadí
jsou stejně častá. Očekávaný počet takových podposloupností je
binom(n,l)/l!, jak uvádí odpověď. Existence znamená, že jejich
počet je alespoň1, takže Markov/sjednocovací odhad P0414 dává

    Pr(L_n≥l)≤binom(n,l)/l!≤n^l/(l!)².                    (1)

Pro l>n jsou obě příslušné počítané veličiny0; l=0 lze chápat
s jedinou prázdnou podposloupností. Přebírá se hotový obecný odhad,
nově se níže odvozují přesné mezní škály zadání.

## P0535: škála l=e sqrt(n)+O(1)

Stirlingova formule dává

    n^l/(l!)²=(1+O(1/l))/(2πl) · exp(2l log(e sqrt(n)/l)).

Pišme l=e sqrt(n)+δ_n s omezeným δ_n. Pak
2l log(e sqrt(n)/l)=−2δ_n+O(n^(−1/2)), tedy je omezený.
Předřazený faktor je O(n^(−1/2)). Rovnice(1) proto dává přesně
O(1/sqrt(n)). Bez faktoru1/(2πl) by se tato síla horní meze
z pouhého (e²n/l²)^l neodvodila. Zaokrouhlení prahu se zahrne do δ_n.

## P0536: škála3sqrt(n) a uvedená konstanta c

Již hrubší nerovnost l!≥(l/e)^l z P0414 dává
Pr(L_n≥l)≤exp(2l log(e sqrt(n)/l)).
Pro l=3sqrt(n)+O(1) je exponent

    −(6 log3−6)sqrt(n)+O(1).

Konstanta c=6log3−6 je kladná a omezené zaokrouhlení pouze mění
násobnou konstantu. Dostáváme O(exp(−c sqrt(n))) v požadovaném
smyslu. Pro malé n s l>n je událost prázdná; asymptotická věta
nevyžaduje existenci neceločíselné délky.

## P0537: oboustranná poznámka v odpovědi29

Pro každou permutaci platí L_n D_n≥n, kde D_n je nejdelší klesající
délka: její RSK tvar s n buňkami leží v obdélníku této šířky a výšky.
Proto L_n≤sqrt(n)/e implikuje D_n≥e sqrt(n). D_n má stejnou distribuci
jako L_n, například bijekcí, která všechny hodnoty komplementuje.

Horní práh e sqrt(n), zaokrouhlený vzhůru na celé číslo, spadá do
P0535. Pravděpodobnost každé z událostí L_n≥e sqrt(n) a
L_n≤sqrt(n)/e je proto O(1/sqrt(n)); jejich sjednocení také.
To dokazuje celou závěrečnou větu odpovědi, včetně slabých krajních
nerovností, bez použití hlubokého výsledku z úlohy28.

Historická prvenství Schützenberger/Dixon/Vershik–Kerov/Logan–Shepp
nebyla samostatně auditována. Publikační metadata BDJ a přesné
použité věty jsou ověřeny přímo; jejich numerické konstanty ani
programy se zde nereprodukují. Úloha30 a další zůstávají dalším blokem.
