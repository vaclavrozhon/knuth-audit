# §1.2.3 — úplná mapa tvrzení a 47 úloh, X0991

6. listopadu 2026, `/root/vol1_audit`. Přímo přečteny původní 27–39
a 471–475; rozsah oddílu na sdílených stranách je oddělen. Každé
tvrzení a každá podčást úlohy/odpovědi byly posouzeny, nikoli jen
vzorek starých checked. Počty původních úloh se nemění: rok 2010
nahrazuje 1–3 novými 1–3, nepřidává 48. úlohu.

Přijaty po celé četbě `sums-and-products.md`, `matrices.md`,
`sequential-sums-2026-11-05.md`, `sums-final-root-review.md`,
`kronecker-date-root-review.md`, `binet-cauchy-root-review.md`,
`chebyshev-root-status.md`, `chebyshev-bibliography-root-review.md`,
`euler-waring-sylvester-root-review.md`, `demoivre-vandermonde-root-review.md`
a `cauchy-hilbert-root-review.md`. Čtena také celá
`generating-symmetric.md` pro přesné odkazy na obecné symetrické součty.
Staré výpočty se neopakovaly a žádná obecná identita níže na konečných
testech nezávisí.

Výsledek není bezvýhradné potvrzení starého checked. Znovu otevřeny
dva přesné rozsahy: nevyjádřená konvence u (18), p33, a prázdné
indexové množiny v násobkovém pravidle odpovědi 35, p473. Jsou
**partial, nikoli nové confirmed ani kandidátské karty**. Podmíněná
aritmetická ukázka není zaměněna za prokázaný spor v autorově
nevyjádřené konvenci. Koordinátor dostal obě lokace k posouzení.

## 1. Dvě znovu otevřené otázky přesného oboru

### (18), původní p32 poslední dvě rovnosti a p33 první rovnost/odstavec

Původní definice na p27 považuje součet za konečný, má-li pouze
konečně mnoho **nenulových** členů. P28 výslovně říká, že divergentní
součet neexistuje; nevytváří z něj automaticky rozšířenou hodnotu ∞.
P32 u (17) výslovně předpokládá, že a_j je definováno pro všechna j.

Přesto poslední krok (18) vytýká a_i[R(i)] před součet
Σ_j[i=p(j)]. Je nutné odlišit dvě tvrzení:

1. Je-li p bijekce relevantních indexů, pravidlo (5) je správné podle
   dřívějšího přímého důkazu, při konečných součtech nebo s příslušnými
   konvergenčními předpoklady. Tato matematika se znovu neotevírá.
2. Doslovná poslední formule (18) a následující věta o nebijektivním p
   zavádějí navíc nevážené součty vláken p. Jejich existence neplyne
   z existence původního váženého součtu.

Konkrétní mezní případ: a_i=0 pro každé celé i, R(i) je i=0 a
p(j)=0 pro každé celé j. Levá strana i oba dosud nevytknuté dvojné
součty mají všechny členy 0, tedy hodnotu 0 podle vlastní definice
knihy. Avšak ve vytknutém výrazu při i=0 stojí

    0 · [0=0] · Σ_(j∈Z) 1.

Poslední součet v knižním konvergenčním smyslu neexistuje. V obyčejné
aritmetice tedy tento zápis nemá hodnotu, přestože předchozí člen
rovnosti existuje. Nejde o dva různé konečné součty ani o vyvrácení (5).

Čten i skutečně citovaný Knuthův primární text
`sources/knuth-two-notes-notation.tex`, pasáž ř.425–448. Autor tam
diskutuje „very strong 0“ pro **nepravdivý Iversonův výrok**, který
má vymazat i nedefinovaný druhý faktor, a upozorňuje na obtížné
mezní případy této konvence. To je relevantní možná interpretace,
kterou nelze ignorovat. V uvedeném svědkovi je však R(0) pravdivé;
nulový koeficient je obyčejné a_0, ne výslovně nepravdivá závorka.
Samotná přečtená pasáž proto neurčuje, zda se zde má i tento nulový
koeficient chápat stejně silně. Původní p32–33 takové pravidlo
nevyslovuje. Nelze bez dalšího tvrdit ani že je vyloučeno, ani že je
autorem zamýšleno.

Doplnění při úplné revizi §1.2.6: erratum z11.8.2022 k p57,
šest řádků pod(13), výslovně dává také binomickému koeficientu
C(r,k) silnou nulu pro k<0 nebo k>r=floor(r), schopnou rušit
záporné mocniny0. Konvence tedy není omezena jen na Iversonovy
závorky. Ani tento další přesný výrok však neříká, že každý obyčejný
nulový koeficient a_i vymaže divergentní sumu. Podmíněný svědek
a status partial proto zůstávají; nový kontext je zachycen v
`quality-recovery-section-1.2.6-2026-11-06.md` a jeho výpisu errat.

Bezpečný obecný důkaz používá součet po aktivních i s R(i) a a_i≠0,
nebo ponechá koeficient uvnitř vnitřní sumy. Při konečné podpoře
vážené dvojné posloupnosti či její absolutní konvergenci je každé
vlákno s nenulovým koeficientem konečné: nekonečné opakování stejné
nenulové absolutní hodnoty by jinak divergovalo. Potom

    Σ_j a_(p(j))[R(p(j))]
      = Σ_(i:R(i),a_i≠0) a_i · #{j:p(j)=i}

platí bez nedefinovaných násobků. Toto je vlastní dostatečná úprava,
nikoli důkaz, že původní vytištěná konvence znamená právě toto.
Zbývá rozhodnout pouze rozsah původní pomocné formule, ne správnost
všech předchozích pravidel pro součty.

### Úloha35 p37 a odpověď35 p473, druhé násobkové pravidlo

Zadání výslovně žádá definici suprema, pokud R neplatí pro žádný
index. Odpověď nejprve určí sup∅=−∞ a poté říká, že pro nezáporná
a_i,b_j platí součin suprem rovný iterovanému supremu součinů.
Nevyslovuje v tomto druhém pravidle neprázdnost obou indexových
množin ani operace s nekonečny. Stará vlastní poznámka správný
důkaz pro **neprázdné** množiny uvedla, ale tím bez upozornění
zúžila rozsah posuzované odpovědi.

Vezměme a_i=b_j=1 pro všechna celá i,j a obě podmínky R,S vždy
nepravdivé. Všechny zadané hodnoty jsou nezáporné, oba indexové
obory jsou prázdné. Pravá strana je −∞ podle navržené definice;
levá je (−∞)(−∞). **Při obvyklé aritmetice rozšířené reálné
přímky** je to +∞, takže tato interpretace dává spor. Pokud se
pravidlo součinu chápe jen pro konečná reálná suprema, levá strana
do jeho oboru nepatří. Kniha zde neříká, že násobení výslovně
probíhá v celé rozšířené přímce. Proto se uvedený podmíněný spor
nepovyšuje na confirmed; přesná chybějící doména zůstává partial.

Pro neprázdné množiny nezáporných reálných čísel s konečnými
supremy α,β je vzorec správný. Každý součin je ≤αβ; pro αβ>0
volíme oba prvky dost blízko jejich supremům a součiny se blíží
αβ zdola. Je-li αβ=0, jeden obor obsahuje jen 0 a všechny součiny
jsou 0. Při neprázdných neomezených oborech je součinové supremum
∞, pokud druhý obor obsahuje kladný prvek; je 0, pokud druhý obor
obsahuje pouze 0. Je-li některý indexový obor prázdný, supremum
součinů je −∞ a tento případ je třeba formulovat samostatně.
To dává úplné vlastní pravidlo, nikoli potvrzení nevyjádřeného
univerzálního násobkového zápisu odpovědi.

Pravidla pro součet, přejmenování, záměnu a sjednocení mají níže
samostatné důkazy; nejsou touto výhradou zpochybněna. Úloha35 se
v inventáři vrací na partial **pouze pro tento dodatečný výrok
odpovědi a jeho konvenci prázdných množin**.

Pro obě místa přečteny všechny relevantní bloky all1-prepre,
all1-pre,all1,err1 podle p27–39 a p471–475. Změny „range“ na
„relevant values“ u p28/33 (2001) a sup→max v odpovědi35 (2024)
nevymezují tyto dvě domény. Původní obrazy p32/33/37/473 jsou
uložené v `images/vol1-file047-p32.png`, `vol1-file048-p33.png`,
`vol1-file052-p37.png`, `vol1-file488-p473.png`.

## 2. Mapa všech hlavních tvrzení

| Rozsah | Důkaz, předpoklady a skutečný výsledek |
| --- | --- |
| (1)–(2), n=0, podmínky, vázané indexy | Konečný součet podle asociativity/komutativity, prázdný součet0. Indexy jsou celá čísla, n může určovat neceločíselnou mez. Příklad nejednoznačného vázání j/k skutečně vyžaduje určit volný index; obě čtení jsou různé rodiny součtů. Konvence po2010/2022 viz §4 níže. |
| (3), nekonečné součty | Dvě oddělené konečné jednostranné limity. Známá oprava1997 odstraní dvojí nulu. Symetrická hlavní hodnota není použita místo těchto limit. |
| (4), celý příklad2×3 | Konečná distribuce dává všech šest součinů jednou. Pro dvě konvergentní řady je to iterovaný součet A·B, viz úloha5; netvrdí se libovolná enumerace všech párů. |
| (5)–(6), přejmenování/substituce | Jediný vzor pro každý relevantní index zachovává členy s násobností1. Původní(6) skutečně posunuje j na j−1; pomocný Markdown má navíc jinou třetí rovnost. Posuny a obrácení konvergentních oboustranných řad mění jen konečný prostředek a mizející ocasy. |
| Absolutní konvergence a libovolná permutace | `sums-and-products.md` §1: konečná množina zachytí vše kromě libovolně malého absolutního ocasu. Její obrazy/vzory se nakonec objeví v částečných součtech; obě jednostranné řady konvergují absolutně. |
| (7)–(10), (8), obecné projekce | Přesně stejná množina párů; S' je projekce, R' členství. Trojúhelník je 1≤j≤i≤n. Pro absolutní dvojnou konvergenci viz doplnění níže; konečný počet vnějších součtů dovoluje konečnou linearitu limit. |
| (11)–(12), sjednocení/průnik | Každý člen má násobnost [R]+[S]=[R∨S]+[R∧S]. U(12) výslovné1≤m≤n dává jediný průnik m. Úloha6 rozšiřuje na tři konvergentní řady. |
| Example1, oba přepisy a meze | Disjunktní sudá/lichá část, bijekce2j a2j+1; poslední lichá mez je j<n/2. Pro zápornou horní mez jsou všechny dotčené množiny prázdné; běžný výklad příkladu je n≥0 celé. |
| Example2 a(13), všechny mezikroky | Dolní a horní trojúhelník se překrývají přesně na diagonále. Čtverec sumy dává dvojitou násobnost mimodiagonálních monomů; přidání Σa_i² a dělení2 dává požadovaný součet, i pro n=0. |
| Example3,(14) | G−xG=a−ax^(n+1), n≥0,x≠1. Všechny přesuny krajních členů jsou dovolené. Pro x=0 se nultá mocnina čte jako1, pro x=1 samostatná úloha11. |
| Example4,(15) | Obrácení j↦n−j, dvojice má hodnotu2a+bn, celkem n+1 členů. n=0 zahrnuto. |
| (16)–(17) | Pravdivostní indikátor a podmínka definovaných a_j. Nulové členy mimo R nemění žádný částečný součet. |
| (18) a věta pro nebijektivní p | Správná násobnost při existenci všech potřebných sum; přesná nová výhrada §1, nikoli univerzální checked. |
| (19) a historie | Definice Kroneckerovy delty je přesně indikátor rovnosti. Historický rok1868 má již potvrzený C0088; nová matematická chyba se nepřidává. |
| (20), součiny a analogie(b),(c),(d) | Konečné produkty zachovávají násobnost všech faktorů, prázdný produkt1; podrobně úloha22. Pro nekonečné produkty je třeba vlastní konvergenční obor, nelze převzít bezpodmínečné přeuspořádání. Text zde žádnou novou definici nedefinovaných nekonečných produktů nedává. |
| Násobné indexy, dvě ukázky, (21) | Součet přes množinu párů; opravený indikátor [1≤j≤i] dává trojúhelník. Rovnost indikátorů v(21) plyne přímo z definic projekcí. |
| (22), úplný seznam pro5 | Nerostoucí pětice součtu5 jsou přesně11111,21110,22100,31100,32000,41000,50000. Úplnost již doložena rozdělením podle největší části a partition konstrukcí v X0989, ne pouhým přepisem sedmi řádků. |
| Úvod determinantů p37 | `matrices.md` §1: permutační definice dává multilinearitu a alternování, z nich všechny tři operace. Rozvoj přes jeden pevný řádek/sloupec a transponované kofaktory dávají A·adj(A)=adj(A)·A=det(A)I. Pro n=1 je kofaktor1, známý dodatek2020. |
| Tři vypsané druhy matic | Přesná definice x_j^i s exponenty1..n, xI+yJ, 1/(x_i+y_j). Cauchyho popisek s y_i je známá oprava1997; samotná matice je správná. |

Pro absolutně konvergentní dvojnou řadu lze starý argument o konečném
ocasu rozepsat bez neodůvodněného Fubiniho kroku. Je-li
Σ_i A_i<∞, A_i=Σ_j abs(a_ij), zvolíme konečnou množinu řádků I,
jejíž vnější ocas je <ε/2. V každém z těchto konečně mnoha řádků
zvolíme konečný sloupcový úsek s ocasem <ε/(2 max(1,#I)). Jejich
sjednocení J dává konečný obdélník I×J, mimo který je celková
absolutní hmotnost <ε. Každá jednotlivá sloupcová řada má absolutní
částečné součty omezené Σ_i A_i; tedy konverguje. Supremum součtů
přes konečné obdélníky je v obou pořadích totéž, a uvedený ε-odhad
dává shodné komplexní limity. Tento důkaz funguje i s podmínkou
S(i,j), po vynulování nevybraných dvojic.

## 3. Všechny původní úlohy a odpovědi

V tabulce `S` znamená přesný příslušný oddíl `sums-and-products.md`,
`M` znamená `matrices.md`. Pouhý souhlas s odpovědí není argument.

| Úloha / části | Přijatý argument a doplnění |
| --- | --- |
| 1 původní | Celé indexy mezi1a3.14 jsou1,2,3, tedy a1+a2+a3. Pozdější nahrazení viz §4. |
| 2 oba součty | První indexy0..5 dávají1,1/3,1/5,1/7,1/9,1/11; druhé indexy−2..2 dávají1/9,1/3,1,1/3,1/9. |
| 3 | n↦n² vynechá3,5 a zdvojí vzory1,4. Podmínka jediné preimage není splněna; správné pravidlo(b) není porušeno. |
| 4 obě strany | Všechny6položky trojúhelníku při n=3, po řádcích a11;(a21,a22);(a31,a32,a33), po sloupcích(a11,a21,a31);(a22,a32);a33. |
| 5 | Pro konvergentní A=Σa_i,B=Σb_j je každá vnitřní řada a_iB a vnější řadaAB. Není nutná absolutní konvergence pro toto iterované pořadí. |
| 6 všechny čtyři možné chybějící řady | Identita indikátorů platí na každém konečném úseku obou poloos. Vyjádřit kterýkoli čtvrtý částečný součet jako lineární kombinaci ostatních tří; limity existují a dávají(d). |
| 7 | Při j↦c−j se poloosy vymění; přes0 se přesune konečný počet členů. Zbytek koncových rozdílů jsou ocasy konvergentních jednostranných řad. |
| 8 původní a2022 | a_(i+1,i)=1,a_(i,i+1)=−1 pro i≥0, ostatní0. Všechny řádkové/sloupcové součty existují; jediný nenulový řádek má−1 a jediný nenulový sloupec+1. Dvojitě nekonečná celočíselná posloupnost splňuje i nové znění. |
| 9,10 | Odvození(14) vyjímá člen a z prázdného oboru, proto není platné pro n=−1 ani−2. Pro−1 samotná formule náhodou dává0; pro−2 dává−a/x při x≠0,1 proti množinovému0. |
| 11 | x=1 dává n+1 stejných členů a, tedy(n+1)a. |
| 12 | (14) s a=1,x=1/7 dává(7/6)(1−7^(−n−1)), n≥0. |
| 13 | n−m+1 členů aritmetické řady začínající m: (n(n+1)−m(m−1))/2, i pro m=n a záporné celé meze. |
| 14 | Distribuce součinu dvou předchozích sum, pro m≤n,r≤s; při obráceném množinovém oboru výsledek0, nikoli neomezené dosazení do polynomu. |
| 15 počáteční hodnoty a nalezení vzorce | S§3 dává0,2,10,34,98,258 pro n=0..5 a přesným odečtením posunuté řady(n−1)2^(n+1)+2. Není použita indukce jako pouhé ověření odhadu. |
| 16 | (1−x)T=Σ_(j=1)^n x^j−nx^(n+1); dosazení geometrického součtu dává celý vytištěný čitatel a(x−1)². n≥0,x≠1, x=0 též v pořádku. |
| 17 | Konečná S: počet prvků. Pro nekonečnou S alespoň jedna poloosa obsahuje nekonečně indexů a její součet jedniček roste bez omezení. Konečnost doplněna známým erratem2025. |
| 18 | Pro kladné celé n je projekce1≤j<n, protože i=n je přípustné; po volbě j zbývá i>j a i dělí n. Úplné ostatní celočíselné obory doplněny v §4. Nezaměňují se volné a vázané proměnné. |
| 19 | Teleskopování pro m≤n; pro množinovou konvenci(a_n−a_(m−1))[m≤n]. Orientovaná alternativa bez indikátoru má vlastní model; C0004 dismissed se neobnovuje. |
| 20(a),(b),(c) | Pro n≥0: 9Σ_(k=0)^n(n−k)10^k+n+1=Σ_(k=0)^n10^k. Náhrada9→b−1,10→b dává obecnou polynomiální identitu. Odečtení posunuté U dává(b−1)U=Σ_(k=1)^n b^k−n. Ciferný zápis1…n potřebuje celé b≥2 a n<b; polynom platí i mimo cifernou interpretaci. |
| 21 | [R]+[S]=[R∨S]+[R∧S], vynásobit a_j a použít(8),(17). Původní odkaz na(a) je známé erratum2004. |
| 22 všechny čtyři analogy | (5) přejmenuje faktory s násobností1; (7) oba pořadí násobí stejné dvojice; analog(8) je Π(b_i c_i)=Πb_i·Πc_i; analog(11) je rovnost násobností v sjednocení/průniku. Nuly jsou dovoleny, žádné dělení nulovým faktorem. Nekonečné produkty potřebují další konvergenční doménu. |
| 23 oba neutrální prvky | 0+x=x a1·x=x zachovají slučování disjunktních oborů, i když jeden obor je prázdný. |
| 24 indukce | Základ prázdný: log_b1=0. Přidání kladného faktoru používá log_b(uv)=log_bu+log_bv. b>0,b≠1 a konečnost jsou nutné. |
| 25 každý problematický krok | Druhý krok zamění dvě různé vazby indexu; při skutečném zastínění je třetí krok Σ_i n, neΣ_i1. Už n=2,a1=a2=1 dává4 proti2. Nenulové a_i jsou implicitní definiční obor zlomků. Známá2025 věta vazby vyjasňuje. |
| 26 požadovaná manipulace a rozšíření odpovědi | Viz §4: rozdělení faktoru a_r podle jeho výskytu dává n+2, platí i pro nuly/komplexní hodnoty. C0003 je stávající chyba odmocnění v dodatku2020; první dotisk ji neobsahuje. |
| 27 | Q_k=Π_(j≤k)(1−a_j): 1−Q_n=Σ_j a_j Q_(j−1)≤Σa_j, protože0≤Q≤1. Platí i širší0≤a_j≤1 a n=0. |
| 28 | Teleskopovat(j−1)/j a(j+1)/j: (n+1)/(2n) pro n≥1; n=1 prázdný produkt1. Pro celé n≤0 je množinový produkt též1, ale tento racionální vzorec se tam nepřenáší. |
| 29(a) | Σ_(0≤k≤j≤i≤n)a_i a_j a_k. |
| 29(b), obecný odkaz v odpovědi | S§4 rozliší tři různé indexy, právě dva stejné a tři stejné; koeficienty dávají(S1³+3S1S2+2S3)/6. `generating-symmetric.md` (S1)–(S2) přesně dokládá odkaz na obecné(38) pro libovolný počet indexů, včetně prázdného produktu. |
| 30 identita bez indukce | Roznásobit oba součiny sum; diagonály se zruší a spojit(j,k),(k,j). Výsledek přesněBinet, bez faktoru2. |
| 30 komplexní specializace a nerovnost | V původní sazbě je abs(Σw_j z_j)², bez konjugace z_j uvnitř této sumy. Dané a=w,b=conj(z),x=conj(w),y=z dávají vytištěné nezáporné čtverce; změna z↦conj(z) dá obvyklou seskvilineární podobu. OCR tyto dvě podoby chybně mísí. |
| 30 dodatek o integrálech | V `binet-cauchy-root-review.md` přesný převod přes Riemannovy součty pro spojité reálné funkce; pro čtvercově integrovatelné obecné funkce nezápornost ∫(αf+βg)² dává diskriminantovou nerovnost a nulový okraj. Nejde o audit všech externích článků. |
| 31 identita a monotónní dodatek | a=u,b=1,x=v,y=1 vBinetovi dává nΣuv−ΣuΣv. Pro obě neklesající reálné posloupnosti je každý(u_j−u_k)(v_j−v_k)≥0. n=0/1 nepřidává záporné členy. |
| 32 | Každá distribuce vybere jedno i_j pro sloupec j; výběry jsou přesně n-tice. n=0: jediná prázdná n-tice a produkt1; m=0,n>0: obě strany0. |
| 33 všechny čtyři příklady, tři r-případy | Lagrangeovy L_j(t) mají hodnoty[i=j]; polynom stupně≤n−1 je určen n různými uzly. Koeficientt^(n−1) dává0 či1; pro r=n použít t^n−Π(t−x_k), vedoucí koeficientΣx_k. Včetně n=1. |
| 33 knižní indukce a obě alternativy | Viz §4 pro přesný rozdíl dvou(n−1)-uzlových sum. Pro r=n jsou koeficienty pomocnéhoP stupně≤n−2 nezávislé na j (známé upřesnění2009). Reziduová metoda má R>max abs(x_k), tudíž stejnoměrně absolutně konvergentní geometrické řady; integruje se právě koeficientz^−1. Obecný výsledek je h_(r−n+1), r≥0, se záporným indexem0. |
| 34 zadání, příklad, obecnější odpověď | Pro monický f stupně n−1 platíΣf(y_k)/Π_(r≠k)(y_k−y_r)=1; vzít y_k=k,f(t)=Π_(r≠m)(x+t−r). Obecná odpověď má f(t)=Π_(r=1)^(n−1)(t−z_r) a různé y_k. Všechny čtyři n=4,m=2 čitatele/jmenovatele odpovídají dosazení k=1..4. |
| 35(a), součtový analog | Pro neprázdné množiny s konečnými supremy jsou všechny součty≤α+β, prvky vε-blízkosti dají dolní přiblíženíα+β−2ε. Rozšířit lze tam, kde nevzniká∞−∞. Konečný základ a+max(b,c)=max(a+b,a+c) je správný. |
| 35(b),(c),(d), prázdno | Přejmenování a záměna vybírají tutéž množinu hodnot; supremum sjednocení je max obou suprem. sup∅=−∞ je vhodný neutrální prvek pro tuto operaci. Právě násobkové dodatečné tvrzení zůstává partial podle §1. |
| 36 | M§1: přímá suma span(1,…,1) a podprostoru součtu0, vlastní hodnoty x+ny a x; determinant x^(n−1)(x+ny). Dále přesný knižní eliminační stav v §4. |
| 37 oba důkazy | M§2: faktoryx_j, rozdíly x_j−x_i, celkový stupeň a koeficient identické permutace1. Knižní řádkové kroky samostatně ověřeny v §4; nulové/shodné uzly zachyceny polynomiální identitou. |
| 38 | M§3: po dvou etapách rozdílů a vytýkání zbývá Cauchy řádu n−1. Produkt dvou záporných rozdílů dává správné znaménko; počátek n=1. Všechny x_i+y_j≠0; shody uvnitř x či y dávají obě strany0. |
| 39 | J²=nJ dává součin s((x+ny)I−yJ) rovnýx(x+ny)I. Pro n≥2 je podmínka jmenovatele ekvivalentní invertibilitě. Pro n=1 se musí nejdříve zkrátit na1/(x+y), včetně x=0,y≠0; nezkrácené0/0 není vyhodnocováno. Staré explicitní omezení je zachováno. |
| 40 vzorec, vysvětlení koeficientu, ověření BA | M§2: Σ_j B_ij t^j=(t/x_i)Π_(k≠i)(x_k−t)/(x_k−x_i). Dosadit t=x_s, dostaneme[i=s]. Jmenovatel v originálu obsahuje x_k−x_i; OCR obrací znaménko. Různé nenulové uzly jsou přesná nutná podmínka inverze. |
| 41 oba důkazy | Transponované kofaktory z38 dávají vzorec. Druhý polynomiální důkaz na474 má stupeň≤n−1 a n různých bodůt=x_j+y_s; v každém přežije jediný člen s. Hodnota t=0 dává AB=I. n=1 též pokryto. |
| 42 | Každý řádek inverze kombinatorické matice má součet1/(x+ny), celkem n/(x+ny), i po skalárním zkrácení. |
| 43 výsledek a pomocná tvrzení | g(t)=Σ_(i,j)B_ij t^j má g(0)=0,g(x_k)=1, tedyg(t)=1−Π(1−t/x_k). t=1 dává součet. Řádek či sloupec jedniček v invertibilníA dává součetB=1 z AB=BA=I. Opravená alternativní metoda2011 přidává různé uzly0,1,x_k, pokud žádné x_k=1. |
| 44 sloupce, součet, dodatek2024 | M§3: aplikace33 na monický polynom stupněn−1 dává c_j=Π(x_j+y_k)/Π_(k≠j)(x_j−x_k); druhá aplikace na polynom stupněn dáváΣx+Σy. Grinbergova identitaΣ_(i,j)(x_i+y_j)A_ij B_ji=Σ_i x_i(AB)_ii+Σ_j y_j(BA)_jj je přímá konečná distribuce i pro m×n a n×m; pro inverzi poskytne totéž. |
| 45 specializace, inverze, celé prvky, součet | M§4: x_i=i,y_j=j−1, protoΣx+Σy=n². Kofaktory dají factorial formuli, tři binomické přepisy doloženy přesnými definicemi. Všechny indexy1..n a n≥1 zajišťují definované faktoriály. |
| 45 všech osm dělitelností | M§4 dokazuje i,j,n,i+j−1,i+n−1,j+n−1,n−i+1,n−j+1 explicitními binomickými přepisy a symetrií, nikoli testem několika prvků. Podrobné doplnění algebraických zkrácení v §4. |
| 45 špatná podmíněnost, velikost, vstupní chyba | Gramův integrál dává pozitivní definitnost. Koeficienty(1−t)^(n−1) dávají Rayleighovu mez κ₂(H)≥(2n−1)C(2n−2,n−1); inverze má stejné κ. Identita inverzní perturbace odděluje chybu vstupu od algoritmu. Pro celočíselný vstup je nutný dostatečný rozsah. |
| 45 kofaktorové „inductive closure“ tvrzení | Minory Cauchyho matice jsou opět Cauchyho matice na vybraných x/y; jejich determinanty s příslušným znaménkem jsou kofaktory. Hilbertův minor po vynechání vnitřní řady/sloupce obecně už nemá posloupné parametry. Například zH₃ vynechat2.řádek/2.sloupec dává[[1,1/3],[1/3,1/5]], což není H₂. Známé2007 upřesnění matrix/determinant zachováno. |
| 46 obecný důkaz a(i)–(v) | M§5: multilineární rozvoj po k1,…,km, opakované indexy zmizí, seskupení m! pořadí dá součin minorů. m=n determinant součinu; m=1 skalární součin; B=Aᵀ součet čtverců minorů, nezáporných pro reálnéA; m>n oba výsledky0; m=2 právě30. Pro komplexníA se nezápornost vyžaduje až s konjugovanou transpozicí. |
| 46 knižní ε a celý rozvoj | ε(k1,…,km)=signΠ_(i<j)(k_j−k_i) je parita pořadí pro různé indexy a0 při shodě. V obou případech det(B_k)=ε(k)det(B_sorted). Známé k_i≤m→n opraveno; další seskupení je přesně předchozí multilineární argument. |
| 47 n=3, obecný n, oba důkazy, Cauchyho porovnání | M§6: determinant koeficientů má všechny faktory p_i−q_j, správný stupeň a konstantu ze specializacep=0,q=1. Vlastní invariant knižních dvou eliminačních etap v §4. Polynomiální identita zahrnuje shodné parametry. Ztotožnit n−2 společných p_i=q_i, potom jde o řádkově škálovanou Cauchyho matici. Známý počet parametrů2007 zachován. |

## 4. Doplněné mezikroky, okraje a převzaté historické rozsahy

**Orientované sumy.** Přijímá se poslední X0762, nikoli starý
candidate v původní poznámce. Pro libovolnou oboustrannou posloupnost
c_k existuje rekurzivně F(k)−F(k−1)=c_k. U_c(p,q)=F(q)−F(p−1)
má spojovací zákon pro všechna celá p,q,r; T_c(p,q) je oproti tomu
množinový součet a při p>q nula. Nová úloha1 z2010 řeší tečkový
zápis orientovanou konvencí: a2+…+a0=−a1. Dodatek2022 tuto konvenci
nabízí jako alternativu levé sigmy, ne jako dokázaný globální příkaz
ke změně všech ostatních úloh. Proto rozdíl T=0,U=−1 pro c_j=1,
p=2,q=0 nezakládá rozpor odpovědi19. Obě nahrazené úlohy2/3 mají
stejné výše doložené součty a bijekční argument jako původní1–3.

**Úloha18.** Pro každé nenulové celé n je úplná projekce
1≤j<abs(n), neboť kladní dělitelé n jsou kladní dělitelé abs(n)
a jejich maximum je abs(n). Vnitřní podmínka zůstává i dělí n,
i>j. Pro n=0 je každý kladný i dělitelem0, takže projekce je
j≥1 a vnitřní podmínka i>j. Tyto formule doplňují ostatní případy;
vytištěná projekce1≤j<n odpovídá kladnému n. Žádné tvrzení o
záměně nekonvergentních nekonečných řad v případu n=0 se z pouhé
rovnosti indexových množin neodvozuje.

**Úloha26 skutečně manipulací produktů.** Rozdělíme a_i a_j a
v druhé části zaměníme pořadí:

    P = (Π_(i=0)^n a_i^(i+1)) (Π_(j=0)^n a_j^(n−j+1))
      = Π_(r=0)^n a_r^(n+2) = (Π_(r=0)^n a_r)^(n+2).

Žádné odmocňování, dělení faktorem ani podmínka kladnosti. Právě
tím se odlišuje platný výsledek od chybného dodatečného kroku C0003.

**Knižní indukce33.** Pro S_n(r)=Σx_j^r/D_j je rozdíl dvou
(n−1)-uzlových sum (jedna bez x_(n−1), druhá bez x_n), dělený
x_n−x_(n−1), roven S_n(r). Pro r<n−2 jsou obě0, pro r=n−2
obě1 a pro r=n−1 jsou jejich hodnoty součty uzlů; rozdíl je
x_n−x_(n−1), tedy výsledek1. Případ r=n pak používá
Π(t−x_k)=t^n−(Σx_k)t^(n−1)+P(t), degP≤n−2. P( x_j ) má
stejné koeficienty pro každé j, a jeho nižší mocninné součty
už mizí. Základ n=1 je přímý, nulový polynom nemá vynucený
kladný stupeň. Tím je zkontrolován i vlastní vytištěný důkaz,
nikoli pouze jiná interpolační cesta ke stejnému výsledku.

**Eliminace36 a37.** V xI+yJ po odečtení sloupce1 od sloupců
2..n má sloupec k>1 hodnotu −x v řádku1 a x v řádku k, jinde0.
Přičtení řádků2..n k řádku1 dává první řádek(x+ny,0,…,0);
zbývající blok je xI. U Vandermondovy matice po odečtení sloupce1
a klesajícím průchodu řádků r=n,…,2 operací ř_r−x1 ř_(r−1)
má první sloupec pouze x1 nahoře a v řádku r≥2, sloupci j>1
stojí x_j^(r−1)(x_j−x1). Vytknutí x1 a rozdílů nechává přesně
Vandermonde s exponenty1..n−1 na x2,…,xn. Klesající pořadí
řádků je nutné pro použití dosud nezměněného předchozího řádku.

**Hilbertovy algebraické formy.** Identita

    i C(−i,n) C(n,i)
      = (−1)^n (i+n−1)! / ((i−1)!² (n−i)!)

po dvojím použití dává první binomický tvar na474 z faktoriálového.
V posledním tvaru na475 platí

    C(−i−j,n−i) = (−1)^(n−i)(n+j−1)! /
                 ((n−i)!(i+j−1)!).

Součin obou takových členů a(i+j−1)C(i+j−2,i−1)² má znaménko
(−1)^(i+j) a po zkrácení přesně původní jmenovatel. Prostřední
tvar s faktorem j se získá stejným rozepsáním čtyř obyčejných
binomických koeficientů. Z něj je dělitelnost j přímá;
jC(n,j)=nC(n−1,j−1)=(n−j+1)C(n,j−1) dává n a n−j+1.
Po prvním ztotožnění ještě
nC(i+n−1,i−1)=(i+n−1)C(i+n−2,i−1), což dává i+n−1.
Symetrie dodá i,n−i+1,j+n−1 a poslední binomický tvar dává
i+j−1. Každý zbývající činitel je celé číslo v uvedených oborech.

Také tvrzení o velkých celých číslech má obecnou oporu:
B_nn=(2n−1)C(2n−2,n−1)²≥(2n−1)4^(n−1), protože
C(2m,m)=Π_(k=1)^m(m+k)/k≥2^m. Týž odhad podpírá růst
Rayleighovy meze podmíněnosti. Nejde o nové plovoucí experimenty.

**Obě etapy vytištěného postupu47.** Původní sloupec k je
P_k(t)=Π_(h<k)(t+p_h)Π_(h>k)(t+q_h). V etapě j=1,…,n−1
se pro k=n,…,j+1 odečte sloupec k−1 a vytkne p_(k−j)−q_k.
Před touto operací jsou v obou aktivních sloupcích příslušné
společné faktory a platí přesně

    Π_(h≤k−j)(t+p_h)Π_(h>k)(t+q_h)
    − Π_(h≤k−j−1)(t+p_h)Π_(h>k−1)(t+q_h)
    = (p_(k−j)−q_k)Π_(h≤k−j−1)(t+p_h)Π_(h>k)(t+q_h).

Klesající k ponechává zdrojový sloupec ještě nezměněný. Po všech
j zbývá B_k(t)=Π_(h>k)(t+q_h) a vytknuté faktory jsou právě
všechny p_i−q_k s i<k, každý jednou.

Druhá etapa má j=1,…,n−1 a k=1,…,n−j. Před krokem mají
sloupce k a k+1 tvar t^(j−1)Π_(h≥k+j)(t+q_h) a
t^(j−1)Π_(h≥k+j+1)(t+q_h). Odečtení q_(k+j) násobku druhého
dává t^jΠ_(h≥k+j+1)(t+q_h). Rostoucí k opět zachovává zdrojový
sloupec. Konečné sloupce jsou t^(n−k); determinant při t=x_i
je Π_(i<j)(x_i−x_j). Obě konečné trojúhelníkové smyčky končí.
Při nulových vytýkaných faktorech se důkaz nejprve provede jako
polynomiální identita pro obecné parametry a potom specializuje;
nedělí se numerickou nulou. Shoduje se nezávislý koeficientový důkaz M§6.

**Prameny a stav.** Přesné dřívější recenze dokládají omezený
obsahový rozsah Fourier/Iverson, Binet/Cauchy a integrální rozšíření,
Čebyševovu nominální/tištěnou dataci, Euler/Waring/Sylvesterovy různé
publikační vrstvy, de Moivrovo druhé vydání a Cauchyho původní vzorec.
Nepřisuzuje se jim celé nově auditované externí dílo ani absolutní
historické prvenství. Přesná nedostupná Apostolova kapitola1957
zůstává výslovně přeskočena. C0088, C0003 a známé opravy se nemění;
C0004 zůstává dismissed. Žádná z těchto pramenných výjimek neuzavírá
nové dvě interpretační mezery v §1.

Všech47úloh je nyní posouzeno v celém rozsahu. Matematické důkazy
46úloh obstály; úloha35 je partial jen kvůli pomocnému násobkovému
pravidlu odpovědi. Hlavní text se vrací na partial pro přesnou
konvenci(18). X0036 a X0936 se odpovídajícím způsobem znovu otevírají,
jejich ostatní důkazy se nezahazují. Další sekce je1.2.4.
