# §1.2.10 — úplné obnovení důkazů, 6. listopadu 2026

Posouzen **celý hlavní text 96–104, všech 23 zadání 104–107 a celé
odpovědi 500–502**, včetně všech dřívějších checked. Původní sazba
byla přímo zobrazena; vzorce nepřebíráme z pomocného Markdownu.
Každé matematické tvrzení níže má vlastní argument nebo přesně
určený, celý přečtený důkaz. Četba všech stran není automaticky
uzavřením historie ani nevyřčených doménových podmínek.

Úplně přečtené důkazové poznámky:

| Zkratka | Důkaz a přijatý rozsah |
|---|---|
| R | `analysis-records.md`: celý algoritmus, distribuce, všechny vyšší momenty, opakované hodnoty, pevné násobnosti a rekordy. |
| P | `analysis-probability.md`: všechny PGF, momenty, kumulanty, normální limity, směsi a složení. |
| T | `analysis-tails.md`: všechny obecné a speciální nerovnosti s obory a krajními případy. |
| F | `analysis-findings.md`: přesné protipříklady a opravené důkazy C0013–C0015. |

Přečteny také celé `analysis-errata-and-scope.md`,
`sequential-analysis-2026-11-05.md` a pět pramenných revizí vyjmenovaných
v §5. Celé oba kontrolní programy i uložené výsledky byly přečteny;
jejich funkce, meze a numerické certifikáty jsou posouzeny v §4.
**Žádný matematický program se znovu nespouštěl.**

## 1. Přesná zbývající doménová otázka na 104

První odstavec p104 definuje normální rozdělení nulovostí všech
kumulantů kromě střední hodnoty a rozptylu. Oprava 4.1.2024 mění
„zero except“ na „zero except possibly“ (`all1`6, `err1`6).
V témže odstavci se tvrdí, že odchylka od středu menší než jedna
směrodatná odchylka nastává přibližně v 68.268949213709 % případů;
následují údaje pro dvě a tři odchylky.

Tyto tři procentní věty platí pro **σ>0**. Pro konstantní X=0 je
log E exp(tX)=0, tedy všechny kumulanty jsou nulové, μ=σ=0,
a přesto `Pr(|X−μ|<σ)=Pr(0<0)=0`. Totéž platí pro násobky σ.
Konstantní veličina proto vyhovuje doslovně napsané podmínce
o kumulantech, nikoli následujícím procentním větám.

Možný správný výklad vyhrazuje zde „normal distribution“ nenulový
rozptyl a odděluje degenerované normální rozdělení. P tuto hranici
správně uvádí, ale samotné přidání podmínky v auditním důkazu
nedokládá, že ji knižní odstavec výslovně stanovil. **Partial je
pouze tento doménový výklad**, nikoli normální integrál, jeho
číselné vyhodnocení nebo limitní výsledky. Není založena nová
confirmed karta. Všechny čtyři vrstvy jsou v přiloženém manifestu;
žádná z jejich změn na p104 výslovně nepřidává σ>0.

## 2. Každé tvrzení hlavního textu

| Původní místo | Důkaz, předpoklady a výsledek |
|---|---|
| 96, účel analýzy, Algorithm M | n je kladné celé číslo a prvky jsou porovnatelné v úplném uspořádání. Na vstupu do M2 je `m=max{X[i]:k<i≤n}`, j je největší index tohoto maxima. Inicializace m=X[n],j=n,k=n−1 invariant splňuje. M3 ponechá stav při X[k]≤m, jinak M4 nastaví nové maximum; M5 sníží k. Tím invariant pokračuje. Po n−1 sníženích k=0 a výstup je pravý krajní výskyt celkového maxima. Pro n=1 je nulový průchod tělem a j=1. Známá oprava 2024 doplňuje n>0. |
| 97, počty M1–M5 a Fig.9 | Přesně `1,n,n−1,A,n−1`. Z n−1 porovnání jde A do M4 a n−1−A přímo do M5; vstupní a výstupní toky každého uzlu souhlasí. Klesající k dokazuje ukončení i cenu, nikoli jen empirický běh. Pomocná paměť je pevný počet slov. Převod četností na čas předpokládá uvedené pevné ceny jednotlivých operací; nejde o univerzální bitovou cenu čtení libovolně dlouhých hodnot. |
| 97–98, minimum, maximum, příklad šesti pořadí | A=0 právě když X[n] je maximum; A=n−1 právě když X[1]>…>X[n]. Pro tři různé hodnoty je seznam A podle knižních šesti pořadí `0,1,0,1,1,2`, tedy průměr 5/6. Pořadí velikostí určuje chování; rovnoměrnost všech n! pořadí je skutečný předpoklad pravděpodobnostní části. |
| 98, definice rozptylu, odchylky a Čebyševův odhad | P a T. Pro konečný druhý moment je `σ²=E(X−μ)²=EX²−μ²`. Pro r>0 a σ>0 má událost |X−μ|>rσ buď pravděpodobnost 0, nebo její příspěvek ke druhému momentu je ostře větší než r²σ² krát její pravděpodobnost; tudíž pravděpodobnost je <1/r². σ=0 znamená X=μ skoro jistě a prázdnou událost. Ostrá nerovnost odpovídá knižnímu „exceeds“; pro ≥ by byla jen ≤. |
| 98–99, (1)–(5), počáteční podmínky a opravený index | R dokazuje rekurenci vložením minima. Přesně knižní odstranění prvního prvku funguje také: je-li X[1] největší, přidává jeden rekord; pro každou permutaci zbylých n−1 pořadových velikostí je tak jeden vstup. Není-li největší, jeho pořadovou velikost lze zvolit n−1 způsoby a A se nezmění. Tedy `P[n,k]=P[n−1,k−1]+(n−1)P[n−1,k]`, n≥2, P[1,0]=1, mimo 0≤k<n nula; dělením n! vznikne pravděpodobnostní rekurence. Chybný index n−k je známá oprava 1997. |
| 99, (6)–(9), Fig.10 | Sečtení konečné rekurence dává `G_n(z)=(z+n−1)G_(n−1)(z)/n`, G_1=1, tedy `G_n=(z+1)…(z+n−1)/n!`. Binomický podíl má v z=−n odstranitelnou singularitu a znamená tentýž polynom. Rekurence pro unsigned Stirlingova čísla cyklů je totožná, proto `[z^k]G_n=c(n,k+1)/n!`. Všech 12 koeficientů G_12 je v přečteném výsledku; střed 58301/27720≈2.10, rozptyl 47279063/30735936≈1.54 a sloupce obrázku odpovídají těmto koeficientům. |
| 100, poznámka o všech vyšších momentech | R odvozuje formálně `E(A+1)^r=[z^n](1−z)^−1 Σ_k S(r,k)log(1/(1−z))^k`, pro každé celé r≥0. Derivuje se podle u v `(1−z)^−u`, tedy konečný koeficient, nikoli nepodložená analytická záměna. V nezávislém Bernoulliho modelu s parametry 1/j se k-tý faktoriálový moment liší od H_n^k pouze součtem opakovaných indexů, nejvýše `C(k,2)H_n^(k−2)Σ_j1/j²`; převod pomocí S(r,k) dává `E(A+1)^r∼(ln n)^r`. r=0,1 řešíme přímo. Obsah věty je dokázán i bez Roesovy bibliografie. |
| 100, (10)–(14) | Pro PGF nezáporné celočíselné veličiny je G(1)=1 a absolutní konvergence na |z|≤1. Derivace pro z<1 a monotónní přechod z↑1 dávají G'(1)=EX a G''(1)=E X(X−1). Při konečném druhém momentu vznikne `var=G''(1)+G'(1)−G'(1)²`; neodečítají se dvě nekonečna. Derivace rekurence G_n v1 dává A_n=1/n+A_(n−1), A_1=0, tedy H_n−1∼ln n. |
| 101, Theorem A, (15)–(16) | Přímé pravidlo pro první a druhou derivaci GH při G(1)=H(1)=1 ruší smíšený člen rozptylu. Věta je algebraická při existenci uvedených derivací; interpretace jako nezávislý součet vyžaduje nezávislost. Pro Q_j=(z+j−1)/j jsou mean=1/j,var=1/j−1/j²; součtem j=2,…,n vzniknou min0,maxn−1,meanH_n−1,dev√(H_n−H_n^(2)). n=1 dává samé nuly. |
| 101–102, (17)–(19), Fig.11 | Poslední nezávislý pokus s parametrem p dává rekurenci, s q=1−p, 0≤p≤1; explicitní počátek G_0=1 je oprava2024. Indukcí G_n=(q+pz)^n, μ=np,σ²=npq. Rozsah 0,…,n je dosažitelný pro 0<p<1; koncová p dávají deterministickou veličinu. Pro n12,p3/5 je μ36/5=7.2,σ6√2/5≈1.697. Binomické koeficienty určují relativní výšky všech sloupců. Slovo „stable“ znamená σ/n→0 při pevném p, ne jistotu na každém vstupu. |
| 102–103, (20)–(22), obě nečíslované derivace | n≥1 celé; `(z+…+z^n)/n` dává uvedený podíl a odstranitelnou singularitu v1. Pro čitatel první derivace A=n z^(n+1)−(n+1)z^n+1 je A'=n(n+1)z^(n−1)(z−1). Druhý čitatel je A'(z−1)−2A, tedy přesně vytištěný výraz. Konečný Taylorův rozvoj má `[w^r]G(1+w)=C(n+1,r+1)/n` pro r≥1, konstantu1. Proto μ=(n+1)/2, G''(1)=(n²−1)/3 a σ²=(n²−1)/12. n=1 degeneruje správně; σ∼n/√12≈0.289n dává uvedené srovnání s binomickým případem. |
| 103, charakteristická funkce, konvoluce, očekávání a Iverson | `G(e^(it))=Σp_k e^(ikt)` existuje absolutně, pro reálné t. Koeficienty GH jsou konečné konvoluce, rozdělení X+Y při nezávislosti. `E z^X` a `E[S]=Pr(S)` jsou přímo definice očekávání a indikátoru. `EX²−(EX)²` předpokládá konečný druhý moment. |
| 103, (23), všechny derivace κ1,κ2, aditivita | P dává K=log M s M(t)=Eexp(tX), kde M existuje u0. Konečný řád r lze odvodit z konečných momentů jako formální Taylorův polynom; samotná existence všech momentů neimplikuje analytickou MGF. Řetězové pravidlo dává κ1=G'(1), κ2=G''(1)+G'(1)−G'(1)²; log součinu přidává všechny kumulanty. Známá oprava indexu κ2 je z1997. |
| 104, normální rozdělení a všechny tři procentní údaje | P dokazuje: z nulových vyšších kumulantů a σ>0 dostáváme po standardizaci liché momenty0, sudé(2r−1)!!. Monotónní řada cosh dává E cosh(tY)=e^(t²/2), takže E e^|tY|≤2e^(t²/2); lze zaměnit charakteristickou řadu a očekávání. Funkce e^(−t²/2) pak určuje normální rozdělení, s vlastním důkazem jednoznačnosti níže. Integrál hustoty dává všechna procenta, jejich přesné zaokrouhlení dokládá §4. Doménový výklad σ=0 je jediná nová partial z§1. |
| 104, přibližná normalita (8),(18) | Přesné standardizované limity jsou celé dokázány v úlohách13,14 níže; n→∞, u binomické distribuce pevné 0<p<1. |
| 104, (24),(25), podlahy, stropy, optimalizace | T: na {X≤r},0<x≤1 je x^(X−r)≥1; na {X≥r},x≥1 totéž. Mimo událost je výraz nezáporný, tedy očekávání dává odhad x^(−r)G(x). r může být reálné; podlaha/strop přesně zachovají neostré události. Při G(x)=∞ dostaneme pouze triviální mez. Infimum přes dovolená x zůstává horní mezí, bez tvrzení, že se vždy dosahuje. |
| 104, obecný princip a exponenciální specializace | Je třeba f≥0 na celé podpoře a f≥s>0 na sledované události. Potom `[X≥r]≤f(X)/s`. Toto je úplný důkaz; nezápornost doplnilo známé erratum2007. Pro f(t)=x^t,s=x^r vznikne(25). Historické atribuce mají přesné oddělené meze v§5. |

**Vlastní most charakteristických funkcí a distribučních funkcí.**
V úloze13 jsou Y_n=(X_n−μ_n)/σ_n standardizované, E Y_n=0,
E Y_n²=1. Přímo přečtené Gnedenko–Kolmogorov53–54 dokazují obecnější
větu přes těsnost a jednoznačnost. Pro tento přesný rozsah postačí
následující samostatný důkaz, který také vysvětluje oba přechody.

Nechť Z je nezávislá standardní normální veličina a δ>0.
Y_n+δZ má hustotu
`h_(n,δ)(x)=E[(δ√(2π))^−1 exp(−(x−Y_n)²/(2δ²))]`.
Gaussův Fourierův integrál (čtverec integrálu v polárních souřadnicích
dává normalizaci; derivování a integrace per partes dávají Fourierovu
funkci e^(−t²/2)) a Fubini z integrabilního e^(−δ²t²/2) dávají

`h_(n,δ)(x)=(2π)^−1∫ exp(−itx) φ_n(t) exp(−δ²t²/2) dt`.

Jestliže φ_n(t)→e^(−t²/2), dominantní konvergence dokazuje stejnoměrnou
konvergenci těchto hustot ke Gaussově hustotě rozptylu1+δ²: supremum
rozdílu je nejvýše integrál absolutního rozdílu Fourierových funkcí.
Na každém omezeném intervalu tedy konvergují integrály. Chvosty jsou
jednotně malé z Čebyševa, neboť E(Y_n+δZ)²=1+δ²; tím konvergují
i celé distribuční funkce k `Φ(x/√(1+δ²))`.

Pro a>0 je

`Pr(Y_n+δZ≤x−a)−Pr(|δZ|>a) ≤ Pr(Y_n≤x)
 ≤ Pr(Y_n+δZ≤x+a)+Pr(|δZ|>a)`.

Volba a=√δ dává chybovou pravděpodobnost nejvýše δ. Nejdříve n→∞,
potom δ↓0 a spojitost Φ dokazují Pr(Y_n≤x)→Φ(x) pro každé x.
Obráceně taková konvergence CDF dává těsnost výběrem konců velkého
intervalu. Na něm aproximujeme omezenou spojitou funkci e^(itx)
po částech konstantní funkcí; rozdíly CDF dávají limitu integrálů,
a rovnoměrná spojitost plus malé chvosty dovolí zjemnit dělení.
Tak vznikne zpět φ_n(t)→e^(−t²/2).

Stejné vyhlazení dokazuje použitou jednoznačnost: dvě rozdělení
se stejnou charakteristickou funkcí mají po přičtení δZ tutéž
hustotu. Když δ↓0, jejich CDF konvergují v bodech spojitosti
k původním CDF (tentýž elementární sendvič). Shoda na společných
bodech spojitosti, které jsou husté, a pravostranná spojitost
dávají shodu rozdělení. Není nutné nevyřčeně předpokládat hustotu
původních diskrétních veličin nebo neexistenci jejich atomů.

## 3. Každá úloha i další tvrzení celé odpovědi

| Úloha | Přesný argument a podčásti |
|---|---|
| 1 | R: G_n(0)=1/n; v každé ze stejně pravděpodobných n pozic může ležet maximum, bez aktualizace právě v poslední. n=1 dává1. |
| 2 | P a §2(10)–(14): součet k(k−1)p_k plus kp_k je druhý moment; odečtení μ² dává(13). Konečný druhý moment je potřebný. |
| 3 | R: přesně min0,max999,μ=H_1000−1,σ²=H_1000−H_1000^(2). Přijaté racionální intervaly dávají zaokrouhlení6.49 a2.42. Odhad H_n^(2)≈π²/6 má chybu mezi0 a1/n z integrálu chvostu Σj>n1/j²; návaznost na již úplně dokázané§1.2.7 je dostatečná. |
| 4 | Výběr k úspěchů mezi n nezávislými pokusy má `C(n,k)p^kq^(n−k)`. Mimo 0≤k≤n nula, koncová p vyložíme přímo nebo polynomicky s0^0=1. |
| 5 | Dosadíme n12,p3/5 do np a npq:36/5,√(72/25)=6√2/5. |
| 6: všechny tři distribuce i obecný rovnoměrný κ_r | P: log(q+pe^t) má první tři koeficienty p,pq,pq(1−2p). Násobení n dává npq(q−p); součet s p=1/j dává H_n−3H_n^(2)+2H_n^(3). Pro uniformní rozdělení K=t+J(nt)−J(t), J'=1/(1−e^−t)−1/t, tedy κ_r=(n^r−1)B_r/r pro r≥2 aκ3=0. Poznámka, že jednoduchý vzor u t^4 nepokračuje, je doložena κ4=pq(1−6pq), získaným čtvrtým členem logaritmu; nejde o další faktor1−3p. Známé opravy závorky1997, argumentu2002 a Bernoulliho konvence2021 ponechány. |
| 7 | R fixuje rozklad pozic do m neprázdných bloků a rovnoměrně přiřadí m! uspořádaných hodnot. Rekordem může být jen pravý kraj každého bloku, proto A má p_(m,k), nezávisle na rozkladu. Všech šest slov pro n5,m3 v odpovědi je právě šest přiřazení hodnot uvedeným blokům. U n3,m2 je šest slov 122,212,221,211,121,112; pevná násobnost dvou2 a jedné1 omezí na první tři a mění distribuci. Tím je podmínka „otherwise random subject to this constraint“ odlišena od pevné násobnosti. |
| 8 | R: pro M≥1 a n≥1 je pravděpodobnost všech různých rovna padajícímu M^(under n)/M^n; je0 při n>M. Pro pevné n je součin Πj0..n−1(1−j/M) neklesající a →1. Oprava1999 odstraňuje nadbytečný faktoriál. |
| 9 | Nejprve S(n,m) rozkladů pozic, potom M^(under m) přiřazení hodnot, dělenoM^n. Přidání poslední pozice dává přesně obě části rekurence q_(n,m). Nula mimo0≤m≤min(n,M), počátek q_(0,0)=1. |
| 10: distribuce i oba výrazy střední hodnoty | R: směs q_(n,m)p_(m,k) ruší m! a dává `M^−n Σ_m C(M,m)S(n,m)c(m,k+1)`. Sečtení pravděpodobností rekordů na jednotlivých suffixech a konečná geometrická řada dávají `E A+1=H_M−Σ_m(1−m/M)^n/m`. Bernoulliho výraz z opravy2023 má navíc −(n−1)/M. Jeho rozdíl pro n a n−1 je `(1/n)Σ_k0..n−1 C(n,k)B_k/M^k−1/M`. Koeficient t^(n−1) v `(e^(Mt)−1)/(e^t−1)=Σ_v0..M−1e^(vt)` jej ztotožní s `M^−nΣ_v0..M−1v^(n−1)`; rozdíl znaménka B1 právě vytváří −1/M. Počátek n1 je1, tedy indukce dokazuje všechny M≥1. |
| 11 | P: log(e^(nt)G(e^t))=nt+K(t), proto se κ1 zvětší o n a ostatní zůstanou. Jako PGF požaduje celočíselné nezáporné posunutí; centrální momenty dále používají tutéž identitu pro reálný posun náhodné veličiny. Oprava term→factor2024 je známa. |
| 12: MGF, celá suma, κ1–κ4 a centrální varianta | P rozvíjí log(1+U), U=Σ_j M_jt^j/j!. Pro Σj k_j=r,K=Σk_j je příspěvek doκr `(-1)^(K−1)r!(K−1)!Π_j M_j^k_j/(k_j!(j!)^k_j)`, přesně celý vzorec. Z toho κ1=M1,κ2=M2−M1²,κ3=M3−3M1M2+2M1³,κ4=M4−4M1M3−3M2²+12M1²M2−6M1^4. Posunutí ke středu má m1=0, takže vynecháme k1>0; κ2=m2,κ3=m3,κ4=m4−3m2². Pro konečný řád stačí příslušné momenty; analytická rovnost celé MGF řady potřebuje její konvergenci. |
| 13: definice, vlastní limita i celý Gamma postup | P: μ=H_n−1,σ²=H_n−H_n^(2)→∞,μ/σ²→1. Proδ=e^(it/σ)−1 platí jednotně `log G_n(1+δ)=δμ+O(|δ|²)`, protože Σ1/j² je omezená. Po odečtení itμ/σ vznikne −t²μ/(2σ²)+O(μ/σ³)+O(1/σ²)→−t²/2. Knižní Gamma tvar je stejný: Eulerův součin a chvostΣj>n1/j²=O(1/n) dávají `G_n(z)=n^(z−1)/Γ(z+1)(1+O(1/n))` stejnoměrně pro|z−1|≤1/2. Tím je dovoleno dosadit n-závislé z=e^(it/σ). Předchozí vyjádření přes e^−z(n+z)^(z−1)(1+z/n)^n má tutéž jednotnou chybu: log(1+z/n)=z/n+O(1/n²), s omezeným z a pevnou větví u1. Gnedenko–Kolmogorovův přesný most a převod < versus≤ pokrývá§2. |
| 13: celá poznámka o jednotném exponenciálním chvostu | **C0013 ponecháno.** n2 dává A uniformně0,1,μ=σ=1/2 a|standardizace|=1 skoro jistě. Prox1/2 je levá strana1, pravá e^−a/2<1 pro každéa>0. Citovaný Flajolet–Soria má nezbytný násobný C. F také dokazuje vlastní opravu `Pr(|Y_n|>x)≤2e^(1/4)e^(−x/2)` pro n≥2,x≥0: nezávislé centrované Bernoulliho přírůstky mají|Z_j|≤1, `E e^(tZ_j)≤exp(var(Z_j)t²)` při|t|≤1; σ²≥1/4 dovolí t=±1/(2σ). Součin a Markov pro obě znaménka dávají výsledek. Bez tohoto argumentu by samotné malén nebylo důkazem opravené obecné věty. |
| 14 | P: pevné0<p<1,q=1−p. Po centrování je charakteristická funkce n-tá mocnina `q e^(−itp/√npq)+p e^(itq/√npq)=1−t²/(2n)+O(n^−3/2)`. Logaritmus je−t²/2+O(n^−1/2). Degenerovanép0,1 nelze dělitσ; daná standardizace se jich netýká. Přesná atribuce de Moivrovi je v§5, známá závorka1997 ponechána. |
| 15(a)–(c) | Proλ≥0 se e^−λΣ(λz)^k/k!=e^(λ(z−1)), logMGF=λ(e^t−1), tedy všechnaκr=λ. Proλ=np→∞, pevnép>0, je centrovaný log charakteristické funkce `np(e^(it/√np)−1−it/√np)=−t²/2+O(n^−1/2)`. λ0 je deterministická hranice, nikoli dělení nulou. Opravené znaménko kvadratického členu2001 zachováno. |
| 16 | Směs má g=Σw_i g_i,w_i≥0,Σw_i=1. Při konečných druhých momentech jeμ=Σw_iμ_i,var=Σw_iv_i+Σ_i<jw_iw_j(μ_i−μ_j)². Rozklad posledního součtu je Σw_iμ_i²−μ². Nulové váhy lze vynechat. |
| 17(a) | **C0014 ponecháno** pro slovo „polynomials“, nikoli pro správný závěr. Pišme `[z^k]f^j=a_(j,k)≥0`; potom h_k=Σ_jq_j a_(j,k). Tonelli dává Σ_kh_k=Σ_jq_jΣ_ka_(j,k)=1, čímž je každý koeficient konečný. Pro|z|≤1 je výměna také absolutní. Není-li f0=0, příspěvky do h0 pocházejí z neomezeně mnoha q_j: f=(1+z)/2,g=1/(2−z) dáváh=2/(3−z),h0=2/3. Žádný univerzální konečný polynom nepokryje všechna q_j: pro každou konečnou sadu indexů zvolíme dvě vyšší mocniny g=z^N a z^(N+1), shodné na této sadě a s různým h0. |
| 17(b),(c), celý příklad generací | Nezávislé Y_i sPGFf a nezávisléN sPGFg dávají součetΣ_i1..NY_i; podmínění N=j vede k f^j a potomg(f). Při konečných druhých momentech E součtu=μ_gμ_f, Var= v_gμ_f²+μ_gv_f; lze použít podmíněné momenty nebo dvakrát řetězové pravidlo. Generace potomků má přesně tuto interpretaci při shodném rozdělení a nezávislosti individuálních počtů potomků. |
| 18: celý produkt, vložení a0/0 | R: K_r=Σ_i≥r k_i, K_1=n>0. Postupně vkládáme menší hodnoty, nezávisle a rovnoměrně jedním z C(K_r,k_r) způsobů. Součin počtů možností je n!/Πk_r!, tedy každé konečné slovo má stejnou pravděpodobnost. Nový rekord přibude právě s novou hodnotou na pravém konci, s pravděpodobností k_r/K_r. Proto G_A=z^−1Π_{K_r>0}(k_rz+K_(r+1))/K_r. Faktor největší přítomné hodnoty je z a ruší z^−1; nulové K_r znamenají vynechání, tj.0/0=1. Všechny hodnoty shodné dávajíG=1. Známá oprava2007 doplňuje krajní faktor a/z; pomocný Markdown/z ztrácí. |
| 19 | a_k=l⇔b_l=k. Výrok∀j<k:a_j<l je ekvivalentní∀j>l:b_j>k, protože žádná hodnota větší nežl nesmí ležet vlevo odk. To jsou přesně oba rekordní výroky s jejich správnými indexy. |
| 20: obě maxima, rovnosti a počet odečítání | R: nerecordní k má dřívější j s a_j≥a_k,b_j≤b_k, tedy a_j−b_j≥a_k−b_k. Opakování j<k skončí v rekordním maximu. Obrácení pořadí a znamének dokazuje rekordní minimum pro b_i−a_i. Maximum obou je max|a_i−b_i| i při rovnostech. Pro rovnoměrnou permutaci různýcha je očekávaný počet rekordů každého druhuH_n. Překryv v pozicik má pravděpodobnost `(k−1)!(n−k)!/n!=1/(n C(n−1,k−1))`; pro n≥2 je součet≤3/n. Tedy počet různých pozic vyžadujících odečet má průměr2H_n−O(1/n)∼2ln n, nejen horní mez. Tvrzení se týká odečtů, nikoli celého času hledání rekordů. |
| 21: obě zadané meze a všechny zesilující věty | T: při0<ε<q minimalizátor `x=(p+ε)q/[p(q−ε)]` dává exp(−nD_p(ε)). Je to minimum: derivace log mezefunkce podle logx je rostoucí, protože druhá derivace binomického logMGF je kladná. Nerovnosti ln u≤u−1 a `(q−ε)ln(q/(q−ε))=ε−Σ_k≥2 ε^k/(k(k−1)q^(k−1))` dávají e^(−nε²/(2q)). Dolní ocas vznikne záměnou p,q. ε0dává1,εqlimitu,ε>qprázdný horní ocas; koncováp deterministicky. `D_p''=1/((p+ε)(q−ε))` je≥1/(pq) pro p≥1/2 a≥4 pro všechna p, tedy obě původní zesilující meze jsou správné. |
| 21: dodatek2023 | **C0015 zůstává pouze erratový nález.** V `S(ε)=Σ_k≥1 2^(2k−1)ε^(2k)/(2k²−k)` chybí násobení n: n2,ε1/4 dáváS≤1/6<1/4=2nε², takže psané e^−S≤e^(−2nε²) neplatí. Ani vloženín neopraví „allp“: n8,p1/4,ε1/2 dává Pr(X≥6)=277/65536>1/256, zatímcoS(1/2)=ln2. Proε>1/2 řada diverguje i při neprázdné události. Platná oprava je p≥1/2,0≤ε≤q a exp(−nS(ε)); porovnání D_p''≥S''=1/(1/4−ε²) a dvou nulových počátků je důkazem. Univerzální e^(−2nε²) původní knihy zůstává správné. |
| 22(a) | T: pro0≤p_k≤1 jeG(r)=Π(1+(r−1)p_k)≤e^((r−1)μ). Volba x=r v(24)/(25) dává přesně `(r^−r e^(r−1))^μ`, se správným směrem při r≤1 či r≥1. μ0jeX0 a mez1. Není vyžadována shoda jednotlivýchp_k. |
| 22(b), včetně dodatku2023 | Záporný log základu h(δ)=(1+δ)ln(1+δ)−δ. Pro−1<δ≤0 je h''≥1, tedyh≥δ²/2. Na0≤δ≤1 je derivace h−δ²/3 rovna konkávní funkci ln(1+δ)−2δ/3, nezáporné v obou koncích (ln2>2/3 plyne z kladné atanhřady); tedyh≥δ²/3. Pro všechnaδ≥0 dává derivace ln(1+δ)−2δ/(2+δ) nezáporný výrazδ²/((1+δ)(2+δ)²), a pak derivace h−δ²/(2+δ)≥δ²/(2+δ)². Opravená znaménka1999 a celý dodatek2023 jsou tak prokázány; v pravděpodobnosti se exponent násobíμ. δ−1 lze vzít limitou. |
| 22(c), oba číselné prahy a Poissonova poznámka | c(r)=e^(1−1/r)/r klesá pro r>1, neboť(logc)'=−1/r+1/r²<0, a→0. Proto pro velkér je mez≤2^(−μr). Racionální intervaly§4 dávajíc2<.825 ac4.32<.5, tedy i všechny většír. Poissonova PGF=e^(μ(r−1)) dává při stejné volbě x=r přesně tutéž mez. Atribuci metody podporuje přesně publikovaný Chernoff1952 v§5. |
| 23: definice, celý dolní i horní ocas a všechny opravy | p,n>0 reálné,q=p+1; koeficienty `(q−pz)^−n` jsou kladné rising(n,k)p^k/(k!q^(n+k)), součet1,radiusq/p>1,μ=np,var=npq. Dolní optimum x=(p−ε)q/(p(q−ε)) pro0≤ε<p dáváf_−''=−1/((p−ε)(q−ε))≤−1/pq, nulové f_−(0),f_−'(0), tedy exp(−nε²/(2pq)); εpřešílimita,ε>pprázdnýocas. Horní x=(p+ε)q/(p(q+ε)) leží v[1,q/p), pro všechnaε≥0 dáváexp(nf_+(ε)), kde f_+=(q+ε)ln(1+ε/q)−(p+ε)ln(1+ε/p). Na0≤ε≤p je f_+'=ln(1−ε/(q(p+ε)))≤−ε/(2pq), tedy poslední oprava2024 exp(−nε²/(4pq)). Starší6pqje slabší platná mez po omezení oboru1998. Proε>pse tato kvadratická mez netvrdí. |

## 4. Kódy a číselná evidence bez opakování běhů

Celé `check_analysis_records.py` (213 řádků) a
`check_analysis_pgf.py` (133 řádků) byly přečteny. Konečné permutace
a slova v prvním programu kontrolují přímo Algorithm M, pravý kraj
maxima, počty kroků, distribuce, podmíněné rozklady, pevné násobnosti,
inverzní rekordy a odečítání. **168264 kontrol není obecný důkaz**;
obecné důkazy jsou R,P,T a tabulky výše. Druhý program má150 kontrol
algebry, momentových rozkladů a dvou číselných prahů; Sympy zde
nenahrazuje vlastní derivace ani důkazy všech parametrů.

Intervalové operace ze znovu identifikovaného `check_gamma_constants.py`
mají již přijaté důkazy v dřívějších blocích této recovery. Jejich
fingerprint, oba programy a oba výsledky stále přesně odpovídají
`artifact-manifest-analysis.json`; ověření hashů je v novém manifestu.
Racionální zaokrouhlení porovnává oba konce intervalu, ne jen střed.

Pro n1000 jsou certifikované intervaly

```text
μ: [6.485470860550344912656518204333900176521679169,
    6.485470860550344912656518204333900176521679170],
σ: [2.416927035280292674296412137499105348360331396,
    2.416927035280292674296412137499105348360331397].
```

Pro r=1,2,3 procentní integrál je `200/√(2π)∫_0^r e^(−t²/2)dt`.
Program sečte Taylorův polynom do k80. Z integrálního Taylorova
zbytku pro e^−u,u≥0 je skutečný integrál mezi tímto součtem a
součtem minus `r^163/(2^81·81!·163)`. Protože exponent zbytku má
pevné znaménko, tento odhad platí i před oblastí klesání členů.
Přijatý racionální intervalπ a kladná odmocnina dávají přesně
zaokrouhlené hodnoty68.268949213709,95.449973610364,99.730020393674.
Nejde o aproximaci bez odhadu chyby.

Pro další prahy uložené intervaly dávají

```text
c(2) ∈ [0.824360635350064073424325393907081785826888050,
        0.824360635350064073424325393907081785826888051] < .825;
log(2c(4.32)) ∈ [−0.001589703177555115882930647254859884448450313,
                −0.001589703177555115882930647254859884448250312] < 0.
```

Konečné koeficientové algoritmy v kódech končí díky explicitním
omezeným indexům, enumerace kvůli konečným sadám. Žádná cena těchto
pomocných ověřovačů není přisuzována knižnímu algoritmu ani globální
pravděpodobnostní větě. Nový dlouhý či opakovaný běh nebyl potřebný.

## 5. Prameny, přesné bibliografické výjimky a všechny vrstvy errat

Celé přečtené revize jsou `demoivre-normal-root-review.md`,
`gnedenko-kolmogorov-root-review.md`, `chernoff-published-root-review.md`,
`thiele-hald-root-review.md`, `analysis-final-history-root-review.md`.
Přijímáme jejich přesně zaznamenanou historickou četbu, nikoli
automaticky celé citované knihy. Matematický obsah potřebný zde
má vlastní důkazy výše nebo úplné R,P,T,F.

- De Moivre1738, zejména241–242, má obecné kladné váhy a:b;
  přepočet p=a/(a+b) dává μ=np,σ²=npq i normální kvadratický exponent.
  Latinský tisk1733 a absolutní priorita nejsou vydávány za čtené.
- Gnedenko–Kolmogorov1954, §13, tištěné53–54, byly v tomto bloku
  navíc přímo zobrazeny a celé přečteny. Nerovnost přes sinc funkci
  dokazuje těsnost, potom limitní rozdělení a jednoznačnost. Přesné
  použití, jeho předpoklady a samostatný dostatečný důkaz jsou v§2.
  Citace nemá rozpor mezi < a≤ díky spojitosti limitní CDF.
- Publikovaný Chernoff1952, Theorem1 na495 a důkaz(3.9)–(3.11) na496,
  dokládá exponenciální metodu. Článek končí507, známá oprava509→507
  je správná. Rozdílné Bernoulliho parametry i konkrétní konstanty
  neodvozujeme pouze z jeho stejnoměrného modelu; vlastní důkaz jeT.
- Thiele1889: původní momentová rekurence s_(r+1)=Σ_j C(r,j)s_(r−j)μ_(j+1)
  po normalizaci dává M'=K'M, tedyK=logM. Nezávislost a aditivita
  odpovídají uvedeným originálním stranám19,33,35–36; známé datum1903→1889
  není nový nález. **Přesně Hald2000,137–153, se výslovně přeskakuje**;
  inventář rukopisů ani abstrakt není obsah článku.
- Bienaymé1853,320–321, obsahuje rozptylový argument se stejnou
  konečností druhého momentu; relativní chronologie je doložena
  přesně popsanými tisky. Kolmogorovův přetisk1973,37, obsahuje
  obecný nezáporný odhad; Bernsteinovy autorské spisy1964,71–73,
  exponenciální metodu a Bernoulliho aplikaci. **Kolace původního
  Kolmogorova1933, Bernsteina1924 a absolutní prvenství se přeskakují.**
- **Foster–Stuart1954 hlavní článek1–13 a Roes1966 citovaná342 se
  výslovně přeskakují.** Dostupná diskuse19–22 nenahrazuje hlavní
  článek. Veškeré tvrzené rekordní formule a vyšší momenty mají
  úplný vlastní důkaz R; neuzavřená bibliografie tento důkaz neruší.
- Gončarov1944 a Flajolet–Soria1993 mají přesné dříve přečtené rozsahy
  v `analysis-errata-and-scope.md`. Citovaný tvar jednotného chvostu
  s násobnou konstantou je navíc nezávisle dokázán v F. Netvrdíme
  nový audit celé jejich obecnější rodiny distribucí.

`results/quality-recovery-analysis-errata-2026-11-06.json` obsahuje
hash, velikost a všechny relevantní textové bloky čtyř úplných
lokálních vrstev (23/4/17/16 bloků; zahrnuto sousední p107).
Rozbitá hlavička opravy úlohy18 je zachována v předchozím bloku.
Přímo zobrazeny původní rozhodné obrazy all1-prepre11/35 a all1 6/13;
starší další obrazy jsou přesně v přijatém inventáři. Samotný OCR
text není důkaz znamének, indexů ani závorek.

Známá errata zůstávají známá. C0013,C0014 jsou neopravené výroky
původních odpovědí; C0015 je výhradně nesprávný dodatek25.4.2023.
Všech23 úloh zůstává checked v přesně doloženém rozsahu s těmito
nálezy. Hlavní text zůstává partial pro přiznané prameny a novou
úzkou doménovou otázku§1. Žádná nová confirmed ani candidate karta.
