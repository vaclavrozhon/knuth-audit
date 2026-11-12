# Úlohy 193–198: párování a omezené permutace

Kontrola 3. listopadu 2026. Zrevidována celá zadání a odpovědi, včetně
obrázku (89), matice 198 a odkazů. Nová chyba nepřibyla. Dřívější F001,
F003, F004 a F005 zůstávají doložené; známá oprava 198(a) má nyní E092,
opravený odkaz za (86) má E093.
Chybějící obecné důkazy asymptotik 196(f,h) jsou níže, takže M196 lze uzavřít.
Fyzický výtisk ani prvenství nálezů nebyly ověřeny.

## Zdroje a rozsah

Použitý svazek: první vydání, druhý dotisk 2022, soubor
`books/taocp-vol4b-ed1-print2-2022.pdf`; stránky knihy 102–103, 148–149,
469–470 mají pořadí PDF o 20 vyšší. Autorský `fasc5c.ps`, převedený do PDF,
má odpovídající hlavní text na 38–39, otázky na 84–85, odpovědi na 173–174;
pořadí PDF je o 6 vyšší. Všechny uvedené stránky byly zobrazeny, textová
extrakce slouží k navigaci. Úplná evidence je v
`sources/matching193_198/source-observations.json`.

Nový `check_matching193_198_sources.py` čte pouze dosud nekontrolované
detaily zdrojů. V obou verzích dekóduje všech 18 vrcholů a 66 hran (89):
K9, prostřední vrchol, K8 a dvě spojovací hrany. Jedna zdrojová úsečka
prochází prostředním vrcholem, proto představuje dvě hrany. Bílé plochy
za popisky nejsou vrcholy. To potvrzuje právě kreslený příklad q=r=4.
Matice 198 má v každé verzi všech 81 prvků shodných s přijatým přesným
výsledkem. Kontrola trvala méně než sekundu při nice 15; žádný řešič.

Převzaty beze změny:

- `results/complete_matching.json`: K0…K11, obě podlahové formule pro
  q=1…100 s 500 ciframi a devět grafů (89) pro 2≤q,r≤4.
- `results/bounded_updates.json`: všech 625 přípustných vektorů pro n≤7,
  knižní n=9, rodiny (g,h) do n=10; původní nezávislá kontrola duality.
- `results/bounded_permutations.json`: opravené bijekce a oba polynomy
  pro stejných 625 vektorů.
- `results/matching_probabilities.json`: 625 vektorů, knižních 1 728
  řešení a 67 527 instancí poměrové identity.

Žádný z těchto běhů nebyl opakován. Konečné zkoušky samy o sobě nejsou
obecnými důkazy; obecné argumenty jsou následující.

## 193–194: rekurence, celé části a zbytky

Pro K_(t+1) stojí pokrytí prvního vrcholu t+1 aktualizací. Každá z t
voleb partnera stojí dalších t aktualizací a zanechá K_(t−1). Proto
U(t+1)=1+t+t²+tU(t−1), s U(0)=0 a U(1)=1. Tím jsou (87),(88) dokázány
pro všechny přípustné velikosti. Počet listů v lichém případě je (2q)!!;
počet úplných párování v sudém případě je (2q−1)!!, včetně 105 pro K8.

Obecná rekurence X(t+1)=a_t+tX(t−1) dává

    X(2q+1) = (2q)!! Σ_(k=0)^q a_(2k)/(2k)!!,
    X(2q)   = (2q−1)!! [X(0)+Σ_(k=0)^(q−1) a_(2k+1)/(2k+1)!!].

Pro a_t=1 je lichá nekonečná suma √e. Kladný odříznutý chvost po
vynásobení (2q)!! je menší než 1: první člen je 1/(2q+2), další poměry
jsou nejvýše 1/(2q+4). Platí i q=0. Proto je částečný součet právě
dolní celou částí √e(2q)!!.

Pro sudou větev a X(0)=1 označme

    S = Σ_(k≥0) 1/(2k+1)!! = √(eπ/2) erf(1/√2).

Identitu lze odvodit bez numeriky: F(z)=Σ z^(2k+1)/(2k+1)!! splňuje
F′=1+zF, F(0)=0, tedy F(z)=exp(z²/2)∫_0^z exp(−u²/2)du a S=F(1).
Sudý chvost má první člen 1/(2q+1) a další poměry nejvýše 1/(2q+3).
Pro q≥1 je tedy také v (0,1). Odpověď 194(b) je
floor((1+S)(2q−1)!!). Zde se držíme kladného q jako v původní kontrole;
nepřisuzujeme nevypsanému součtu zvláštní interpretaci pro q=0.

Dosazením a_t=1+t+t² dostáváme konstanty

    C  = Σ_(k≥0) (1+2k+4k²)/(2^k k!) = 5√e,
    C′ = Σ_(k≥0) (1+(2k+1)+(2k+1)²)/(2k+1)!! = 3+5S.

První rovnost používá první dva momenty exponenciální řady. Pro druhou
jsou dílčí sumy S, 1+S a 2+3S, což plyne posunem indexu.

Zůstává důležitý absolutní odhad O(1), který samotné malé zkoušky
neprokazují. Oba chvosty mají t=2q+2, respektive t=2q+1, a první člen
a_t/t=t+1+1/t=2q+O(1). Druhý člen
a_(t+2)/(t(t+2))=1+3/t+1/(t(t+2)) je rovnoměrně omezený pro q≥1.
Poměr následujících členů je nejvýše (t+2)/t²≤5/9 pro t≥3,
protože a_(t+2)/a_t≤((t+2)/t)². Zbytek od druhého členu je tedy omezen
geometrickou řadou nezávisle na q. Dostáváme přesně

    U(2q+1)=C(2q)!!−2q+O(1),
    U(2q)=C′(2q−1)!!−2q+O(1).

Kladnost chvostů současně dokazuje ostré horní meze 8.244 na list a
10.054 na řešení v hlavním textu. Číselné hodnoty C a C′ jsou převzaté
z již přijatého výsledku, nová vysokopřesná numerika neběžela.

[OEIS A010844](https://oeis.org/A010844) skutečně připisuje podlahovou
formuli Michaelu Somosovi s datem 26. března 1999. To dokládá knižní
historickou poznámku; netvrdíme tím absolutní prvenství.

## 195: dvě větve grafu (89)

Pro q,r>1 má prostřední vrchol jako jediný stupeň 2, takže jej MRV
zvolí první. Levá volba zanechá K_(2q) a K_(2r). Menší sudá klika se
vyřeší celá a při každém jejím řešení se znovu prochází větší klika.
Pravá volba zanechá dvě liché kliky K_(2q+1), K_(2r−1); algoritmus
nejprve vyčerpá menší z nich a větev skončí bez řešení.

Pro s=min(q,r), t=max(q,r), h=min(q,r−1), M(2j)=(2j−1)!! je přesný počet

    4+2q+2r + U(2s) + M(2s)U(2t) + U(2h+1).

Konstanta na kořeni zahrnuje obě volby prostředního vrcholu. Celkový
počet řešení je M(2q)M(2r). Tato formule je tatáž, kterou starý výčet
potvrdil na devíti grafech; zde je její obecné vysvětlení.

Po vydělení počtem řešení hlavní člen směřuje k C′, když q+r→∞.
U(2s)/(M(2s)M(2t))≤C′/M(2t)→0. Pravá neúspěšná větev je zanedbatelná
i bez předpokladu q≈r: při h→∞ platí

    (2h)!!/[M(2q)M(2r)] ≤ (2h)!!/[M(2h)M(2h+2)] → 0.

Poměr poslední posloupnosti v h+1 a h je
(2h+2)/((2h+1)(2h+3)), tedy směřuje k nule. Při omezeném h je čitatel
omezený a jmenovatel roste. Také kořenový lineární člen je zanedbatelný.
Knižní asymptotické popisy obou fází proto platí; nevztahujeme je na
q=1 nebo r=1, kde přestává platit jednoznačnost první MRV volby.

## 196: dualita, přesné vzorce a oba chybějící odhady

Předpoklady hlavního textu jsou 1≤a1≤…≤an≤n a a_j≥j. Dvojice X_jY_k
existuje právě pro k≤a_j. Po obrácení obou pořadí a záměně stran vznikne
duální diagram s b_k=#{j:a_j≥n+1−k}. Inverze permutace prohodí strany,
obrácení a doplnění indexů poskytne přesně bijekci odpovědi (b).
Příklad dává b=135778899. Nejde o tvrzení, že samotná inverze bez
změny indexů už automaticky splňuje b.

Na úrovni j je Π_j=∏_(i=1)^j(a_i−i+1) uzlů; všechny jejich částečné
volby jsou rozšiřitelné. Zbývající problém má n−j položek na každé
straně a první stupeň a_(j+1)−j. Kořenová práce 196(c) je
1+a1(n+1): pokrytí X1 stojí 1+a1, každé následné Y stojí n.
Sečtení přes všechny úrovně dává obecně

    U = Σ_(j=0)^(n−1) Π_j[1+(a_(j+1)−j)(n−j+1)]
      = 1+Σ_(j=1)^n(n+3−j)Π_j−Π_n.

Tím je dokázán i součin počtu řešení Π_n a jeho rovnost duálnímu
součinu. Pro a_j=n máme Π_j=n!/(n−j)!; po dělení n! je

    U/n! = 1/n!−1+Σ_(k=0)^(n−1)(k+3)/k! → 4e−1.

Pro a_j=min(j+1,n) platí Π_j=2^j pro j<n, Π_n=2^(n−1).
Konečná geometrická suma dává U=6·2^n−2n−7 pro n≥1.

Pro a_j=min(2j,n), s q=floor(n/2), rozlišíme obě parity:

    n=2q:   Π_j=(j+1)! pro j≤q,  Π_n=q!(q+1)!,
    n=2q+1: Π_j=(j+1)! pro j≤q,  Π_n=(q+1)!².

Právě zde patří oba faktoriály z F004. Položme m=ceil(n/2). Pro 0≤k≤m
platí Π_(n−k)/Π_n=1/k!. V přesné formuli je tudíž hlavní část

    2+Σ_(k=1)^m(k+3)/k!,

nikoli řada začínající 6+4/1! (F005). Každý zbývající prefixový poměr
je nejvýše 1/m!, počet členů je nejvýše n a koeficient nejvýše n+2.
Jejich součet včetně 1/Π_n je O(n²/m!). Chvost exponenciální řady
Σ_(k>m)(k+3)/k! je O(1/m!) jednoduchým poměrovým odhadem.
Proto

    U/Π_n = 4e−1+O(n²/m!) = 4e−1+O(n²/Γ(n/2+1)).

Pro dostatečně velké n je m!≥Γ(n/2+1); konečné malé n asymptotiku
neovlivní. To doplňuje chybějící obecný důkaz přesně na požadovanou
chybu, nejen limitu. Původní tvrzení M196 o chybějícím důkazu zůstává
uchované v poli s předchozím stavem.

MRV je pro obě rodiny (g,h) slučitelné s uvedeným pořadím X. Po j
výběrech prvních X má rodina (g) nejmenší stupeň min(2,n−j), nejmenší
stupeň Y je stejný. U (h), dokud j≤floor(n/2)−1, má první X stupeň
j+2 a poslední Y stupeň ceil(n/2)+1; potom už zůstává úplný bipartitní
graf. S pořadím X před Y se tedy vybírá první X při každé remíze.

V obecném případě (i) stačí rekurze vektoru mezí. Je-li a1≤b1, vezmeme
d=a1 a reziduum (a2−1,…,an−1). Jinak d=b1 a reziduum
(min(a1,n−1),…,min(a_(n−1),n−1)); všechny sousední řádky vybraného Yn
mají původní mez n a jsou z hlediska počtu stejné. V obou případech

    U(a)=1+d(n+1)+d U(reziduum),  U(prázdný vektor)=0.

Remízy mezi X a Y rozhoduje uvedené pořadí. Knižní příklad po prvním
Y9 vybere X1, nikoli X2: jejich délky jsou 2 a 4 (F003). Dřívější
záznam naměřené větve Y9,X1,Y8 se zachovává beze změny.

## 197: obě bijekce a vytvářející funkce

Po F001 musí být j≤t_j≤a_j. Knižní a_n dovolí už pro a=(1,2)
permutaci (2,1), která není přípustná. Při zápisu součinu používáme
knižní konvenci aplikace faktorů zleva doprava, jako v přijatém programu.

Obecnější věta odpovědi platí: σ_(s,t) může být libovolná permutace
posílající s do t a nezvyšující jiný prvek. Musí fixovat vše mimo [s,t]:
pod s postupně od nejmenšího prvku, nad t postupně od největšího.
Máme-li součin Qσ_(1,t), Q fixuje 1, takže výsledné p1=t. Ostatní
zasažené hodnoty leží v [1,t], proto nepřekročí a_i≥a1≥t. Obráceně
z přípustného p určíme t=p1 jednoznačně a σ_(1,t) od hodnot odpárujeme.
Výsledek fixuje 1 a stále respektuje ostatní meze, neboť všechny
změněné hodnoty jsou nejvýše t≤a1≤a_i. Indukce na zbývajících prvcích
dává bijekci a jedinečnost všech t_j pro kteroukoli pevně zvolenou rodinu σ.

Pro transpozice t_j=j přidá samostatný cyklus; t_j>j vloží j do cyklu
obsahujícího t_j. Počet cyklů je tedy #{j:t_j=j}. Pro cyklus
(t,t−1,…,j) se zbývající hodnoty přečíslují se zachováním pořadí,
zatímco nový prvek přidá t_j−j inverzí. Tudíž

    Σ_p z^C(p) = ∏_(j=1)^n (z+a_j−j),
    Σ_p z^I(p) = ∏_(j=1)^n (1+z+…+z^(a_j−j)).

Odkaz 4A, 7.2.1.5–29 je správný: na zobrazené straně 435 je (a)
inverzní polynom n!_y a (c) obecný součin pro věže. Při t=0, m=n a
obráceném pořadí výšek dává (c) právě druhou formuli. Tím není proveden
audit všech tvrzení svazku 4A.

Dworkinův bibliografický odkaz potvrzuje [autorova stránka NIST](https://www.nist.gov/people/morris-j-dworkin)
i metadata vydavatele přes Crossref: Morris Dworkin, *Factorization of
the Cover Polynomial*, JCT B 71(1), 1997, 17–53, DOI
[10.1006/jctb.1997.1745](https://doi.org/10.1006/jctb.1997.1745).
Jeho [abstrakt přednášky na MIT z roku 1996](https://math.mit.edu/combin/1996sp.html)
popisuje faktorizaci pro Ferrersovy diagramy a potvrzuje relevanci odkazu.
Plné PDF se nepodařilo získat (403; API vrací jen metadata, PDF 406).
Kontrola tohoto „see also“ je tedy bibliografická a tematická; netvrdíme
kontrolu celého článku ani konkrétního jeho číslovaného teorému. Výše
uvedený důkaz knižních formulí na získání článku nezávisí.

## 198: obecná pravděpodobnost a známá oprava

Je-li s>a_r, je π_rs=0. Jinak q=min{j:a_j≥s}≤r. Vynecháním pozice r
a hodnoty s dostaneme nový problém s původními mezemi
a′_j=a_j−[j≥q] pro j≠r. Součin počtu řešení 196(d) po vydělení Π_n dává

    (a_r+1−r)π_rs = ∏_(j=q)^(r−1) (a_j−j)/(a_j+1−j).

Při a_j=j může být čitatel nula; v důkazu se takové faktory nekrátí.
Pro s<s′ je q≤q′. Když π_(r,s′)>0, je r≥q′ a

    π_rs/π_(r,s′) = ∏_(j=q)^(q′−1) (a_j−j)/(a_j+1−j),

což nezávisí na r. S knižní podmínkou nenulových jmenovatelů je tím
dokázáno (b), včetně případu nulových čitatelů.

Pro a=255667999 sedí všech 81 vytištěných prvků. Originální PDF už má
správné a_j≥s při definici q; draft má a_j≤s. Oprava byla zveřejněna
11. července 2022 pro Fascicle 5, str. 278, odpověď 198, řádek 2.
Přímo zobrazena strana 14 úplných errat; zaznamenáno jako E092,
nikoli nový objev.

## Evidence errat a navázání

Prohledány úplné i krátké texty errat 4B a Fascicle 5 a oba TeXové
zdroje, podle obsahu, úloh i posunutých stránek. Hashované výsledky
jsou v `results/matching193_198/errata-check.json`. Dnešní živé kontroly
z předchozích bloků potvrzují shodu veřejných souborů s archivem.
F001/F003/F004/F005 v těchto šesti vrstvách nadále nemají opravu.
U E092 je historie a stav jednotlivých verzí výslovný.

Za (86) má draft také starý odkaz na 188; správně je 189, jak již stojí
v našem PDF. Tato oprava byla zveřejněna rovněž 11. července 2022,
pro Fascicle 5, str. 100, řádek 9. Je samostatně evidována jako E093.
Na straně 102 tím uzavíráme tento odkaz a úvod k párování; předchozí
část o extrémních pokrytích není tímto blokem prohlášena za kompletně
zdrojově zrevidovanou.

193–198 jsou zrevidované v knižním rozsahu; externí články nejsou
automaticky zrevidované celé. Další blok: 199–201, kde již existují
přijaté výpočty, F002 a kandidáti C002/C003. Tyto výpočty se neopakují;
zbývají obecné důkazy a úplné porovnání zdrojů.
