# §4.5.4-41: počítání prvočísel po blocích

Zadání416 a odpověď666–667 byly vizuálně zkontrolovány. Níže je
vlastní důkaz všech čtyř částí, včetně konkrétního rozvrhu dotazů,
který skutečně potřebuje jen O(N) slov paměti. Testy prošly;
nový nález nevznikl. Známou opravu chybějícího argumentu z21.1.1998
je nutné zapracovat před vyhodnocením vzorce v části(c).

## 1. Značení a rozklad podle počtu faktorů

N je celé číslo alespoň2 a X=N³. Případ N=1 vrací ihned π(1)=0;
níže uvedený netriviální rozvoj listů se používá pro N>=2.
π(x) značí počet prvočísel nejvýše x. Prvočísla v rostoucím pořadí
označujeme p_j, s konvencí p_0=1, a položíme a=π(N).
Číslo přežívající síto do m nemá prvočíselný faktor <=m.
Počet takových kladných čísel nejvýše x je f(x,m); číslo1 přežívá
každé síto. Počet přeživších s právě k prvočíselnými faktory,
počítanými s násobností, je f_k(x,m).

Součin tří čísel větších než N je větší než N³. Proto všichni
N-přeživší do X jsou1, prvočísla>N, nebo součiny dvou prvočísel>N.
Tyto možnosti jsou disjunktní a dávají

```
π(X) = π(N) + f(X,N) - 1 - f_2(X,N).                 (1)
```

Každý součin dvou prvočísel zapíšeme právě jednou jako pq s p<=q.
Pro pevné N<p<=sqrt(X) je přípustných q přesně π(X/p)-π(p)+1.
Označme C(t,2)=t(t−1)/2. Pro b=π(sqrt(X)) dostáváme

```
f_2(X,N) = sum_{N<p<=sqrt(X)} π(X/p) - C(b,2) + C(a,2). (2)
```

Všechny argumenty X/p jsou menší než N². Pro N=10 jsou p rovna
11,13,17,19,23,29,31 a příslušné počty prvočísel jsou
24,21,16,15,14,11,11. Jejich součet minus55 plus6 dává63,
jak uvádí kniha; čtverce prvočísel jsou správně zahrnuty.

## 2. Přesné listy zkrácené rekurze

Přeživší do p_(j-1), kteří jsou násobky p_j, jsou v bijekci
s přeživšími do p_(j-1) nejvýše x/p_j: dělíme je p_j.
Z toho plyne

```
f(x,p_j) = f(x,p_(j-1)) - f(x/p_j,p_(j-1)).           (3)
```

Rozvíjíme f(X,p_a), dokud j=0 nebo x<=N². Uzlu přísluší
znaménko μ(k) a člen f(X/k,p_j), kde k je součin již vybraných
různých prvočísel větších než p_j. Zde μ(k) je Möbiova funkce:
nula, dělí-li k čtverec prvočísla, a jinak(-1)^t, kde t je
počet jeho různých prvočíselných faktorů; μ(1)=1.
Při průchodu stromem se prvočísla vybírají v klesajícím pořadí,
takže každý přípustný součin odpovídá právě jedné cestě.

Listy prvního typu dosáhnou j=0 ještě s k<N. Jsou přesně
všechna bezčtvercová k<N, neboť jejich faktory jsou <=N.
Všechny vlastní mezisoučiny jsou také<N, takže cesta nebyla
ukončena dříve. Jejich příspěvek je μ(k)*floor(X/k).

List druhého typu právě překročí mez součinu: má tvar kp_j,
k<N<=kp_j, a všechny faktory k jsou větší než p_j.
Jeho rodič tedy ještě není list; naopak každá taková dvojice
určuje list. Znaménko se změní z μ(k) na−μ(k) a zbývá
síto do p_(j-1). Dostáváme přesnou formuli

```
f(X,N) = sum_{1<=k<N} μ(k)*floor(X/k)
         - sum_{j=1}^a sum_{ceil(N/p_j)<=k<N}
             μ(k)*f(X/(k*p_j),p_(j-1))*[least(k)>p_j]. (4)
```

Hranatá závorka [P] má hodnotu1, platí-li P, jinak0.
least(k) je nejmenší prvočíselný faktor k, s least(1)=+∞.
Hranice k<N a kp_j>=N odpovídají vytištěné sazbě; nesmějí se
samostatně zaměnit za neostrou a ostrou variantu. Zdrojový článek
LMO používá opačné rozhodnutí na rovnosti, což je také možné,
ale mění oba typy listů současně.

Pro N=10 je první součet1000−500−333−200+166−142=−9.
Nenulové členy druhého součtu, ještě před vnějším minusem, jsou
−f(100,1)−f(1000/14,1)−f(1000/15,2)−f(1000/21,2)
−f(1000/35,3)=−100−71−33−24−9=−237.
Proto f(1000,10)=228 a(1) vrací168.

## 3. Součtový strom a čas

Součtový strom je úplný binární strom: listy jsou indikátory
přežití jednotlivých čísel a vnitřní vrchol obsahuje součet svých
dvou dětí. Doplníme nulové listy do nejbližší mocniny2.
Smazání jednoho čísla změní jedinou cestu ke kořeni, tedy O(log N)
vrcholů. Prefix, tj. součet listů od začátku po dané místo,
se rozloží na nejvýše dva celé podstromy v každé hladině;
také stojí O(log N). Čítač se snižuje jen při prvním smazání listu.

V sazbě667 list s indexem 2^m−1+n reprezentuje číslo n+1,
1<=n<=N². To samo není chybný index: pro x>=1 se f(x,p_j)
získá jako1 plus prefix prvních floor(x)−1 listů. Poslední
uložené číslo N²+1 se při dotazech x<=N² nepoužije. Pro x<1
je odpověď0. Test této přesné interpretace zahrnuje i prázdný
prefix a doplněné nulové listy. Vlastní implementace níže
používá přímé indexování skutečných čísel bloku.

Síto do N² provede nejvýše N²*sum_{p<=N}1/p pokusů o smazání.
Elementární horní mez tohoto prvočíselného součtu je O(log log N):
pro σ=1+1/log N je1/p<=e/p^σ; dále

```
sum_{p<=N} p^(-σ)
 <= log product_{p<=N}(1-p^(-σ))^(-1)
 <= log sum_{n>=1} n^(-σ)
 <= log(1+1/(σ-1)).                                  (5)
```

Druhá nerovnost rozvine konečný Eulerův součin a použije
jednoznačný rozklad; poslední porovná kladnou klesající řadu
s integrálem. Není potřeba věta o prvočíslech.
V(4) je nejvýše N*π(N)<=N² dvojic, každý dotaz stojí O(log N).
Celkový čas je tudíž O(N² log N log log N) aritmetických kroků.
Pro libovolné pevné ε>0 je to O(N^(2+ε)). Operandy mají O(log N)
bitů, včetně akumulátorů: hrubá mez pro součty je O(N^4).
Po započtení školní bitové aritmetiky zůstane O(N^(2+ε)).
Paměť celého stromu by byla O(N² log N) bitů; konstanta2
v knižním neformálním odhadu neřeší zaokrouhlení na mocninu2.

## 4. Konkrétní segmentace s O(N) slovy

Předpočítáme prvočísla<=N, μ(k) a least(k) pro k<=N.
Postupně zpracujeme bloky [L,R] délky N pokrývající1,...,N².
Mezi bloky uchováváme pouze a+1 čísel
`B_j=f(L-1,p_j)`, 0<=j<=a. Na počátku bloku je strom samých
jedniček. Před smazáním násobků p_j reprezentuje právě přeživší
do p_(j-1) uvnitř tohoto bloku.

Dotaz x=floor(X/(kp_j)) patří do bloku právě pro

```
max(ceil(N/p_j), floor(X/(p_j*(R+1)))+1)
 <= k <= min(N-1, floor(X/(p_j*L))).                  (6)
```

Pro tato k testujeme μ(k)!=0 a least(k)>p_j. Hodnotu dotazu
dá staré B_(j-1) plus prefix stromu délky x−L+1.
Teprve po všech dotazech tohoto j přičteme ke B_(j-1)
součet celého aktuálního bloku a smažeme násobky p_j.
Po posledním prvočísle aktualizujeme i B_a. Indukce přes j
a přes bloky dokazuje správnost každé hodnoty B_j a každého dotazu.

Pro pevné j jsou intervaly k v(6) disjunktní mezi bloky,
protože každý podíl x patří právě do jednoho bloku. Všechna
kandidátní k proto prohlédneme celkem nejvýše N*π(N) krát;
N*π(N) je i počet dvojic blok/prvočíslo. Segmentace nepřidá
další faktor N k času. Tabulky, jeden strom a průběžné součty
potřebují O(N) slov, tedy O(N log N) bitů.

Také část(2) lze provést s touto pamětí. Po dokončení síta známe
π(N²)=a+f(N²,N)−1, protože žádný složený N-přeživší není<=N².
Prvočísla p v(N,sqrt(X)] generujeme rostoucím segmentovaným
sítem po blocích délky N. Jejich podíly floor(X/p) klesají.
Druhým sítem jdeme od N² dolů a od průběžného π odečítáme
prvočísla, která jsme právě překročili. Obě síta používají
stejný seznam prvočísel<=N a současně uchovávají nejvýše dva
bloky. Každé celé číslo projde každým sítem nejvýše jednou;
příprava bloků i práce síta jsou O(N² log log N).
Počet vygenerovaných p současně určí b v(2).

## 5. Nezávislé kontroly

[Program](../verify_prime_count.py) ukládá tři samostatné checkpointy
do[výsledku](../results/prime-count.json). Běh měl limit300s,
PID1309569/1309570, session19304, exit0; celkem25.193s.

- Pro N=2,...,80:79 rekurzních stromů,8226 vnitřních vrcholů,
  6290 zvláštních listů. Explicitní strom proti úplnému popisu
  listů v(4), hodnoty proti přímému mazání násobků až do N³.
- 133 vstupů N=2,...,129,200,255,256,257,1000. Prvních132
  výsledků proti nezávislému úplnému sítu do257³=16974593;
  poslední proti externí přesné tabulce π(10^9)=50847534.
  Všech42275 zvláštních dotazů má ověřenou jedinečnost a úplnost
  podle nezávislé enumerace všech dvojic(j,k). Pro N<=32 navíc
  všech554 hodnot ověřeno přímým testem gcd s primoriálem (součinem prvních j prvočísel).
- 40585 prefixových dotazů pro N=2,...,24 kontroluje přesné
  knižní listy n+1 proti přímé nesoudělnosti.

Pro N=1000 vyšlo f=81515102,f_2=30667735,a=168.
Bylo14182 zvláštních dotazů,165708 prohlédnutých dvojic a3233
dotazů v části(b); modelovaná mez paměti7391 buněk. Pole
validátoru a uložené stopy nejsou součástí paměťové meze algoritmu.
Testy nejsou asymptotický důkaz; ten podávají §2–4.
Úspěšné bloky se bez změny či nové pochybnosti neopakují.

## 6. Errata a primární zdroje

Všechny čtyři vrstvy all2-prepre,all2-pre,all2,err2 byly
prohledány. Relevantní sazba: all2-prepre42,all2-pre15,all2-11.
Opravy:21.1.1998 druhý argument p_(j-1) v(4);30.9.2009
přepracovaný historický odstavec;25.5.2015 uzavírací hranatá
závorka;29.–30.12.2022 rekord a odkaz na novou metodu.
Staré tvrzení, že rekord Deléglise/Rivat používá analytickou
metodu, se neopakuje: už je opraveno v roce2009.

Primární autorův[LMO preprint](https://www-users.cse.umn.edu/~odlyzko/doc/arch/meissel.lehmer.pdf)
má47 stran souboru, odlišně od časopiseckých537–560.
Vizuálně přečten titul, tištěné3,6–22 a45–46, tj. formulace
větyA, celý základ a sekvenční důkaz, bibliografie. Paralelní
část a jemnější optimalizace nebyly znovu auditovány.
Preprint obsahuje vlastní překlepy: např. v(3.1) chybí−1,
v(3.2) je dolní exponent1/4 místo1/3 a bibliografie uvádí
Meissel1871 jako525–525. Kniha má všechny tyto údaje správně;
nejde o nálezy proti TAOCP. Vlastní důkaz je na nich nezávislý.
Časopisecké PDF AMS vrátilo403; autorova verze byla získána
a její původ, hash i neúspěšné pokusy jsou v metadatech.

Oliveira e Silva,[2006](https://sweet.ua.pt/tos/bib/5.4.pdf):
vizuálně759,766,768. Bibliografie potvrzuje LMO, Lehmera,
Deléglise/Rivata i analytický článek. Tabulka766 má správnou
hodnotu π(10^20)=2220819602560918840; π(10^23)=1925320391606803968923
je modrý **dodatek po publikaci**, nikoli původní tabulka z2006.
Úvod výslovně vysvětluje modré anotace. Bibliografické údaje
čtyř Meisselových článků a Lehmera byly navíc porovnány
s metadaty vydavatelů uloženými u Crossref; jejich celé původní
texty nejsou prohlášeny za přečtené.

Lagarias/Odlyzko,[analytická metoda](https://www-users.cse.umn.edu/~odlyzko/doc/arch/analytic.pi.of.x.pdf):
vizuálně strany3 a8 autorovy24stránkové verze. Potvrzují
O(x^(1/2+ε)) a značnou další práci potřebnou pro implementaci;
úplný analytický důkaz nebyl v tomto bloku znovu odvozen.
Soud o nepraktičnosti v erratu2009 je dobový. Nelze jej
vykládat jako nemožnost implementace: Plattův následný
[článek](https://arxiv.org/abs/1203.5712) uvádí rigorózní
nepodmíněný výpočet π(10^24); vizuálně přečteny strany1–2
verze v3 z29.10.2013. Ani tento obrovský výpočet
jsme zde nereprodukovali.

Erratum2022 uvádí π(10^29)=1520698109714272166094258063.
Přesné číslo, jména David Baugh/Kim Walisch a rok2022
souhlasí s[jejich záznamem](https://github.com/kimwalisch/primecount/blob/master/doc/Records.md),
který datuje výpočet28.2.2022 a popisuje opakovanou kontrolu
s jiným parametrem. To je ověření primárního záznamu,
nikoli naše nezávislé přepočítání π(10^29).
Hirsch/Kessler/Mendlovic,[arXiv v2](https://arxiv.org/abs/2212.09857v2)
z27.12.2022 má opravdu60 stran; titul a úvod byly vizuálně
přečteny. Odkaz uvádí elementární algoritmus, čas přibližně
sqrt(x) až na logaritmické faktory; celý60stránkový důkaz není
součástí tohoto ověření bibliografického dodatku.

Rozsah je tedy úplný vlastní důkaz úlohy41 a doložená kontrola
jejího doprovodného textu, nikoli nový audit všech citovaných
článků či současných rekordních výpočtů. Fyzický dotisk
a prvenství případných chyb nejsou ověřeny; nic nebylo odesláno.
