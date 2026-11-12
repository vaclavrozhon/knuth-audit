# Souvislý průchod §2.3.4.4 — 5. listopadu 2026

X0976. Přímo přečten hlavní text 386–395, všech 33 zadání na 395–399
a odpovědi 588–594 v hranicích oddílu. Přezkoušeny celé tři
parallel/tree-enumeration/PROOFS-*.md, celý trees.py, výsledky a přesné
pramenné doplňky. Přijaté úspěšné výpočty se neopakovaly. Nejsou nové
potvrzené chyby; jedno nové vizuální podezření bylo vyvráceno.

## Multisety, centroidy a kódy

Rozklad kořene na multiset větví dává součin (3); jeho logaritmus je
formální, každý koeficient závisí na konečně mnoha členech. Derivace
dává obě rekurence úlohy 2. Tabulka s_nk používá jen již známá a_j.
Program skutečně počítá do n=100 včetně; zbytky a částečné faktorizace
nejsou nekonečnou aritmetickou větou. Hodnoty (4) a (9) souhlasí
s přesnými uloženými tabulkami a nezávislým Eulerovým součinem.

Po odstranění X má libovolný Y v jeho větvi velikosti s_j váhu alespoň
n−s_j. Při s_j>n/2 přechod do této větve váhu sníží; při s_j=n/2
jsou oba konce hrany jediné dva centroidy; při všech s_j<n/2 je X
jediný centroid. To dokazuje rozklad a úlohy 9–10. Na 387 je známá
oprava: dolní mez potřebujeme pro libovolný Y ve větvi, ne jen Y1.
Dodatek 2023 na 388 výslovně píše maximum, které již plyne z jediné
příliš velké větve. Správný vzorec na 388 proto není novou chybou.
Fig. (6) má váhu D=3 a E=7.

Neunicentroidální zakořeněný tvar se jednoznačně rozloží na dvojici
velikostí k,n−k, k≤n/2. Neuspořádané stejné poloviny se počítají jednou,
různé dvakrát před dělením dvěma. Výsledkem je F=A−A²/2+A(z²)/2.
Šest stromů na 589 i centroidy souhlasí. Lineární algoritmus využívá
size podstromu a protější velikost n−size; každá hrana je zpracována
konstantněkrát.

Binární stromy mají B=1+zB² a b_n=binom(2n,n)/(n+1); binomický rozvoj
a Stirlingova chyba O(4^n n^(−5/2)) souhlasí. Odebrání kořene
uspořádaného stromu a převod lesu dává b_(n−1). Pro t pevných míst
T=1+zT^t dává binom(tn,n)/((t−1)n+1), s prázdným základem.
Čtyři neoznačené zakořeněné, dva volné, pět uspořádaných a šestnáct
označených tvarů na 386–389 odpovídají různým deklarovaným modelům.

V nejmenším-listovém kódu je vždy o jeden zbývající štítek více než
nepřečtených položek. Nejmenší chybějící štítek lze odebrat; jeho rodič
nemohl být odebrán dříve. Každá hrana míří k později odebranému vrcholu,
inverze tedy nemá cyklus. Počet je n^(n−1), s pevným kořenem n^(n−2).
Maticový důkaz má nI−J s vlastními hodnotami 1,n,…,n; n=1 používá
prázdný determinant 1.

Pro q předepsaných nekořenů končí kód jedním z n−q kořenů. Proto
r(n,q)=(n−q)n^(q−1), q<n. q=0 je jediný les izolovaných bodů.
Rozdělení kořenů dává (18), odebrání jediného kořene (19), a tedy
G_m=G_1^m, G_1=exp(zG_1). V (21) jsou analytické předpoklady i f(0)≠0
výslovné; dosazení exp dává (n+1)^(n−1)/n! v (22).

**Vyvrácené podezření na 391:** při prvním vizuálním čtení jsem
přehlédl m v poslední sumě definice G_m. Čerstvé přímé vykreslení
DjVu strany 406 jednoznačně ukazuje správné r(k+m,k). Vykreslení
v původním rozlišení archivního obrazu má identické pixely; nejde
o dvě verze knihy ani o změnu souboru. Doklad:
results/sequential-enumeration-render-check.json; přímo zobrazený
obraz: images/sequential-enumeration/p391-native.png. Nová karta nevzniká.

## Barevné lesy a formální řady

Poslední barva a její pořadové číslo určují pozici kořene t ve slově
barev, tedy jediný posun k. Ostatní čísla rekonstruují cíle. Počet
čtveřic dělený n dává (24). Nulová barva funguje s 0^0=1; její kladný
počet cílů dává nulu. Prázdný celý les má výslovný základ r(0,0)=1.
Rozdělení kořenů dává (25) bez dalšího barevného multinomického faktoru,
barvy již počítají obě r. Odebrání kořene barvy i dává (26); změna
indexů v (27)–(29) větu R. Jedinečnost plyne podle stupně v y, pravá
strana přidává jeden vrchol. T(y)=y exp(T(y)) souhlasí s T=−W(−y).

C0057 na 393: n=1,q=0 je výslovně dovolená doména, ale t=f(V_q)
ani poslední barva prázdného slova neexistují. Oddělený základ q=0
dává multinomický počet n!/∏n_i!. Vzorec (24) zůstává správný.
Raney 1964 tento základ odděluje; nezávislý protipříklad nepotřebuje
historickou atribuci. Obrázek 392 a tabulka 393 jsou správné.

## Asymptotiky a jiné neoznačené stromy

Z a_n≤4^(n−1) plyne α≥1/4; z H=A/z>exp(zH) dostáváme
z<log(H)/H≤1/e, tedy α≤1/e<1. H je na [α/2,α) omezená a roste;
A konverguje na uzavřeném kruhu. S(z)=Σ_(k≥2)A(z^k)/k je analytická
pro |z|<sqrt(α), její ocas je stejnoměrně geometricky omezen.
A(α)≠1 by implicitní větou odstranilo kladnou singularitu.
Přímé derivace dávají F_z=β>0 a F_ww=α.

Kladné koeficienty u z,z² vynutí přísnou trojúhelníkovou nerovnost
na zbytku kružnice. Inverze lokálního vztahu
z−α=−α(w−1/α)²/(2β)+… dává odmocninu. Záporné znaménko plyne
z růstu H k 1/α zdola. Cauchyho kontura v proříznutém okolí převádí
zbytek (1−z/α)^(3/2) na O(α^(−n)n^(−5/2)); není jen formálně zahozen.

C0053 na 588: koeficient je
(−1)^(n−1)sqrt(2β) α^(−n) binom(1/2,n). Bez střídavého faktoru
je tištěná verze záporná na všech sudých n≥2. Závěrečný kladný odhad
zadání na 396 je správný; 396 se proto kvůli C0053 nebarví červeně.
Konstanty 2.955765285652 a 0.439924012571 souhlasí s uloženým výpočtem
se 70 číslicemi a odhady ocasů; nejde o certifikovanou intervalovou
aritmetiku a výpočet se neopakoval.

5: rozklad podle alespoň dvou dětí dává
1+2C−z=∏(1−z^k)^(−c_k); prvních devět koeficientů souhlasí.
MacMahonův později získaný skutečný model slučuje asociativní a
komutativní sérii i paralelu. Normální tvar má alternující značky S/P;
pro n>1 dva výběry značky kořene, pro n=1 jedinou hranu. Nejde
o rovnost číselných odporů ani obecnou izomorfii grafů.

6–7: neuspořádaná dvojice dává G=1+z(G²+G(z²))/2. Pro F=1−zG
platí F(z²)=2z+F(z)². Kritický bod má ρG(ρ)=1; funkce
D=1−2z−z²G(z²) má jednoduchý kořen s D'<0 a jedinou dominantní
singularitu. Proto g_n~sqrt(−ρD'(ρ))/(2ρsqrt(π)) · ρ^(−n)n^(−3/2).
Konstanty 2.483253536173 a 0.7916031835775 souhlasí. Doplnění
chybějících dětí dává bijekci na plné neuspořádané binární stromy
s n+1 listy, včetně prázdného základu; doplněk 2018 platí.

## Úlohy 13–33 a krajní případy

13/18: oba stromy slova 3,1,4,1,5,9,2,6,5 porovnány po hranách.
Rodiče jsou (5,6,1,1,0,5,3,4,2,9) a (3,9,0,1,1,2,4,6,5,5).
Druhé kódování obrací úseky od vzestupně řazených listů; opakovaný
štítek zahajuje větev. Chybějící štítky jsou listy a jejich vzestupné
přiřazení jednoznačná inverze. 14 se týká existující poslední položky,
prázdný kód ji nemá. Tuto implicitní podmínku nelze přenést na
samostatnou úlohu 16. V 15 je pořadí odebrání topologické, ale obecná
FIFO ho nezaručuje; vzestupná musí být i inicializace prioritní fronty.
Není tím slíbena změna jediné instrukce doslovného MIX programu.

C0058 na 590: i po známém zkrácení D1 na j<n přejde n=1 do D3
a čte neexistující f(V1). Guard před D2 má vrátit jediný kořen.
Pro n≥2 má C[v] počet zbývajících výskytů; k monotónně prochází
štítky a nový list l<k se zpracuje ihned. Nejvýše n posunů a n−1
odebraných hran dávají O(n).

17: souvislá funkce má jeden cyklus délky k. Volba cyklu a lesa
dává binom(m,k)(k−1)! · k m^(m−k−1); pro k=m je poslední faktor 1.
Součet je m^(m−1)Q(m). Obrázek m=13 a jeho kód souhlasí.
C0059 na 590: čistý cyklus nemá poslední odstraněný list, slovo
délky m−1 nemá m posledních různých členů. Stačí oddělit (m−1)!
čistých cyklů; výsledný počet je správný.

C0071 zůstává candidate: Rubin–Sitgreaves 19A má titul datovaný
22.1.1954 a tutéž formuli, Katz shodu uznává. To dokládá starší
zdroj, nikoli datum Katzova soukromého objevu. Výlučné „first
obtained“ zůstává neuzavřené; úloha 17 je partial v tomto bodě.

19–24: výskyty štítku jsou počty dětí, chybějící štítky listy.
Počet s k listy je n!/k! · S(n−1,n−k), stupňová specifikace
n!(n−1)!/[∏k_j!∏(j!)^(k_j)]. Plný binární případ má n=2m+1,
k_0=m+1,k_2=m. Uspořádaný tvar nemá netriviální automorfismus
zachovávající pořadí; počet štítkování je n!, celkem
(2n−2)!/(n−1)! a s pevným kořenem při n=4 právě 30.

26: k=7, cíle (4,8,3,2,2,6,8), kořeny 8,9. Všech sedm hran
a devět barev souhlasí. 27: složené U→V→U umožňuje vybrat nejmenší
V nezablokované nečtenými cíli; poslední cíl je jeden z p kořenů.
Obousměrná bijekce dává pq^(r−1). 28 se zafixovaným U1 dává
n^(m−1)m^(n−1).

29: Lagrange pro u=t log x dává [z^k]x^r=r(r+kt)^(k−1)/k!.
k=0 je polynomický základ 1 i při r=0; t=0 dává exp(rz).
Násobení dává Abelovu konvoluci; obě chybné sumy na 592 jsou známé.
30 rozděluje celé komponenty mezi první x a poslední y kořeny;
prázdná skupina má faktor 1. Součet dává Hurwitzovu identitu.
Na 399 je známé e1 místo ε1 v exponentu.

31: H=z+H²/(1−H) pro uspořádané větve bez unárních uzlů.
Řešení H(0)=0 má [z^10]H=103049 a bijekci s disekcemi polygonu.
Historická formulace o Hipparchovi zachovává nejistotu; Acerbiho
model není jistou kolací antických rukopisů. Schröderův originál
počítá ekvivalentní závorkování, ne doslovně polygonální slovník.

32: Σj n_j=n−1 dává n_0=1+Σ_(j≥2)(j−1)n_j. Postorder má kladné
prefixové součty Σ(1−d_j) a celkový součet 1. Jediný přípustný
cyklický začátek je za posledním minimem prefixu, výsledek
(n−1)!/∏n_j!. Známá oprava posouvá horní index minima z k na k−1.
Oba směry původní reflexní bijekce a Bergmanova redukce přezkoušeny
obecně, ne jen konečným testem. Pro f kořenů je součet f a právě
f označených pozic přípustných i u periodických slov. Proto počet
lesů je f(n−1)!/∏n_j!. 33 používá pevné typy se stupni e_i;
tentýž důkaz dává w=Σz_iw^(e_i) a w^f. Jedinečnost je formální
podle celkového stupně. Monom má konečnou podporu i při nekonečně
mnoha typech.

## Prameny, výjimky a mapa

Pozdější předání uzavřela Ottera, Raneye 1960, Riordana, Joyalovy
relevantní strany, Cayleyovu atribuci, MacMahona, Wedderburna,
Schrödera a Acerbiho. Přesné rozsahy jsou v
notes/source-followup-root-review.md a citovaných předáních.
Staré tabulky nedostupných pramenů již pro ně neplatí. Přijetí
dokladů není novou druhou četbou všech článků hlavním pracovníkem.

Přeskočeno dle aktuálního zadání: celý Good 1965 a oprava 1968;
nepřečtené příklady v celém Species; plný Goldman 1971 a široké
prvenství; celý Neville 1953; Peirce 1976 strany a rukopis;
Dvoretzky–Motzkin 1947; Bergman 1978. Vlastní matematická tvrzení
mají úplné důkazy. Goldmanovy NBS zprávy dokládají jeden průchod
a přípravu 1970, nikoli absolutní prioritu. C0071 má konkrétní
protievidenci, proto se neschová pod nedostupnou citaci.

Čtyři aktuální vrstvy znovu prohledány po stranách i tématech
(enumeration-errata-extract.json): 24 různých položek. C0053/57/58/59
ani Katzova priorita jimi nejsou vyřešeny. Původní matematické
nebo faktické vady X0504 leží na 387,395,398,399,589,590,592,593,594.
Sazba, gramatika, nové doporučené prameny a upřesnění maxima na 388
se jako matematické vady nemapují.

Hlavní text checked s výjimkami; 10,18,32 nově checked. Úloha 17
zůstává partial pro C0071; ostatních 32 úloh má uzavřenou kontrolu.
Celé stránky 386–398 a 588–593 jsou obsahově probrané, ale 590
ponechává partial pro C0071. Na 399/594 zbývá další oddíl.
C0053 má lokaci pouze 588, C0057 pouze 393, C0058/59 pouze 590;
správná zadání nejsou přidána jako chybné stránky.

Závažnost C0058 v UI snížena z automaticky importované critical na
medium: jde o chybějící jediný základ n=1, obecný algoritmus pro n≥2
je správný. Osobní uživatelská hodnocení se nemění.
