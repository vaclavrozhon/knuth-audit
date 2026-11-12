# §4.6.3: Erdősova dolní mez, lemma P a úlohy 17–18

Stav 2026-11-04: text od věty E na straně 471 po důsledek na začátku
473 a obě úlohy uzavřeny. Hlavní věta i asymptotický důsledek jsou
správné. C0224 je drobná nepřesnost ostré nerovnosti pro prázdnou volbu
v důkazu; výsledek nemění. Všechny potřebné kroky dokazujeme níže.

## 1. Značení a tvrzení

Sčítací řetězec je rostoucí posloupnost 1=a_0<...<a_r=n, jejíž každý
další člen je součtem dvou dřívějších. Jeho délka je r. Píšeme
lambda(n)=floor(log2(n)); nejkratší délka řetězce je l(n). Malý krok
nezvětší lambda, zdvojení znamená a_i=2a_(i-1). Počet malých kroků je
s=r-lambda(n). Nezdvojovací krok může být malý i velký.

Věta E říká: Pro pevné epsilon>0 existuje alpha<2, pro které počet
řetězců s lambda(n)=m a r<=m+(1-epsilon)m/lambda(m) nepřesáhne alpha^m
pro všechna dostatečně velká m; uvedenou ostrou konečnou mez lze dosáhnout
zvětšením alpha. Důležitý je počet všech řetězců, nejen počet jejich
různých konců. V dalším bereme 0<epsilon<1. Pro epsilon=1 jsou možné
jen řetězce samých zdvojení, pro epsilon>1 žádný takový řetězec.

Dále log znamená logaritmus se základem 2, kromě výslovně uvedeného
přirozeného logaritmu ln. Zápis o(m) znamená funkci, jejíž podíl s m
jde k nule. Budeme používat odhady jednotné pro všechny přípustné
parametry součtu, nikoli jen pro jednotlivou pevnou trojici.

## 2. Úloha 17 a lemma P

Zvolme 0<delta<sqrt(2)-1 a položme b=1+delta, theta=2 log(b)<1.
Minikrok je nezdvojovací krok i, pro který existuje j<i s a_i<a_j*b^(i-j).
Každému minikroku přiřadíme jeden interval (j,i], tvořený celými čísly
j+1,...,i. Minikroky mají různá pravá zakončení, takže jde o různé
intervaly. Nechť t je počet minikroků.

Z rodiny intervalů postupně vyhazujeme interval, jehož vynechání nemění
sjednocení. Ve výsledné neodstranitelné rodině není žádný interval
obsažen v jiném; při seřazení podle pravých konců tedy rostou i levé
konce. Žádný bod nemůže patřit do tří zbývajících intervalů: prostřední
z takové trojice by byl pokryt sjednocením krajních dvou. Každý bod je
proto pokryt nejvýše dvakrát.

Sjednocení rozdělíme na disjunktní souvislé celočíselné intervaly J=(c,d].
Pro jednu takovou komponentu násobíme poměry a_i/a_j přes její ponechané
intervaly. Označíme-li R_k=a_k/a_(k-1)>1, potom se každý R_k, c<k<=d,
v součinu objeví jednou nebo dvakrát. Proto

```text
a_d/a_c <= product(a_i/a_j) < b^(sum(i-j)) <= b^(2(d-c)).
```

Tím dostáváme (28). Je-li rodina prázdná, žádnou komponentu netvoříme
a používáme prázdný součin 1. Celková délka q komponent je aspoň t,
protože každá původní pravá koncová pozice minikroku je ve sjednocení.
Mimo komponenty roste člen nejvýše dvojnásobně. Tedy

```text
2^lambda(n) <= n <= 2^(r-q) * b^(2q)
                  = 2^(lambda(n)+s-(1-theta)q)
                 <= 2^(lambda(n)+s-(1-theta)t).
```

Po porovnání exponentů plyne t<=s/(1-theta), což je lemma P. Celá
argumentace pracuje i s t=0. Oprava z 2. 4. 2000 na konci odpovědi 17
opravuje zápis sjednoceného intervalu; nepřidává další matematickou
podmínku.

## 3. Kódování řetězců: rovnice (29)–(33)

Ve větě E zvolíme delta=2^(epsilon/4)-1, takže theta=epsilon/2.
Kroky rozdělíme na t minikroků, u zdvojení a v ostatních kroků.
Platí t+u+v=r=m+s. Věta A z předchozího bloku dává t+v<=3.271s;
lemma P dává t<=s/(1-epsilon/2). To jsou přesně podmínky (30).

Rozmístění tříd lze zvolit binom(r,t+v)*binom(t+v,v) způsoby. Zdvojení
jsou pak jednoznačná. U ostatního nezdvojovacího kroku a_i=a_j+a_k,
k<=j<i, neplatí definice minikroku pro žádný dřívější index. Proto

```text
delta*a_(i-1) <= a_k <= a_j <= a_(i-1),
a_j <= a_i/b^(i-j) <= 2*a_(i-1)/b^(i-j).
```

Stejný druhý odhad platí pro a_k. Z delta<=2/b^(i-j) plyne konstantní
horní mez na i-j a i-k, závislá jen na delta. Například lze vzít beta
rovné nejmenšímu kladnému B s b^B>2/delta. Počet voleb obou indexů
je pak nejvýše beta^2 a za všechny takové kroky nejvýše beta^(2v).

Pro minikroky vybereme v každém řetězci jedno vyjádření a_i=a_j+a_k.
Dvojice (j,k) jsou různé: jedna dvojice by dala stále stejný součet,
zatímco řetězec je rostoucí. Možných dvojic 0<=k<=j<r je r(r+1)/2.
Jejich neuspořádaná t-prvková množina, rozmístění tříd a indexy ostatních
kroků určují celý řetězec nejvýše jedním způsobem.

To poslední tvrzení potřebuje důkaz, jinak by chyběl faktor t!. Postupujme
po prefixech. Při minikroku vezmeme nejmenší součet mezi dosud nepoužitými
dvojicemi, jejichž indexy jsou již známé. Dvojice určená pro tento krok
je dostupná. Každá dostupná dvojice určená pro pozdější minikrok má
striktně větší součet. Dvojice s dosud neznámým indexem nemůže dát
aktuální součet: příslušný budoucí člen je již sám alespoň tak velký.
Takto se původní prefix jednoznačně rekonstruuje. Nekonzistentní kódy
prostě žádný řetězec nereprezentují.

Počet možností je tudíž nejvýše binom(r(r+1)/2,t), a tedy nejvýše
binom(r^2,t). To je potřebná horní mez (33). Přesná rekonstrukce byla
navíc zkontrolována pro všechny řetězce délky nejvýše osm, viz §7.

## 4. C0224: prázdná množina dvojic

Na straně 472 je před (33) a ještě jednou za ní uvedeno „fewer than“.
To není pravda při t=0: existuje právě jedna prázdná volba a
binom(r^2,0)=1. Příklad 1,2,4 má r=2, s=t=v=0, u=2; stejný příklad
samých zdvojení existuje pro libovolně velké m a splňuje podmínky věty
pro každé pevné 0<epsilon<1. Problém tedy nelze odstranit volbou
dostatečně velkého m.

Oprava je v obou místech „at most“. V odpovědi 18 na straně 694 je
také třeba před výrazy obsahujícími dělení t říci, že pro t=0 má
příslušný faktor hodnotu 1. Jde o společný vynechaný okrajový případ,
ne o chybu asymptotické věty. Stejná ostrá formulace se vyskytuje
i v původním článku na straně 79. Netvrdíme, že jsme tento okrajový
případ objevili první.

Skeny 472 a 694 byly vizuálně zkontrolovány. Ve všech šesti vrstvách
Knuthových errat, včetně druhého vydání a aktuálního TeXu, nebyla
nalezena odpovídající oprava. Úplné relevantní stránkové bloky jsou
v `sources/powers-basic-errata.txt`. Zpráva v
`reports/C0224-ministep-empty-choice.txt` je pouze neodeslaný návrh.
Tištěný exemplář novějšího dotisku nebyl zkontrolován.

## 5. Úloha 18: jednotný asymptotický odhad

Položme L=lambda(m), w=t+v a c=1-epsilon/2. Ze (30) pro velká m plyne

```text
r=m+s <= 2m,
w <= C*m/L                 (C je konstanta),
t <= ((1-epsilon)/(1-epsilon/2))*m/L <= c*m/L.
```

Poslední nerovnost používá 1-epsilon<=(1-epsilon/2)^2. Přípustných trojic
(s,t,v) je nejvýše (2m+1)^3. První binomický faktor má logaritmus
O(m log(L)/L): pro w>=1 použijeme binom(r,w)<=(e*r/w)^w a monotonnost
pravé strany pro w<=r; pro w=0 je faktor 1. Druhý faktor je nejvýše
2^w. Rovněž beta^(2v)<=max(1,beta)^(2v). Všechny tyto příspěvky mají
logaritmus o(m), jednotně pro přípustné trojice.

Zbývá poslední faktor. Pro t=0 je 1. Pro t>=1 platí

```text
log binom(r^2,t) <= t*log(e*r^2/t)
                 <= T*log(4e*m^2/T),       T=c*m/L.
```

Funkce x*log(e*N/x) je rostoucí pro 0<x<=N, jak je vidět z derivace
log(N/x). Dosazením T dostáváme

```text
T*log(4e*m^2/T)
  = (c*m/L)*(log(m)+log(L)+log(4e/c))
  = c*m + O(m*log(L)/L),
```

protože L<=log(m)<L+1. Součet z úlohy 18 je tedy nejvýše
2^((1-epsilon/2)m+o(m)). Pro libovolné pevné eta s 0<eta<epsilon/2
je nakonec menší než alpha^m, kde alpha=2^(1-eta)<2. Toto dokončuje
úlohu 18 i větu E. Nepotřebujeme numericky hádat, od kterého m odhad
začne platit.

## 6. Důsledek (34): hustota výjimek a volba f(n)

Přirozená hustota množiny S je limita počtu jejích členů mezi 1 a N,
děleného N, pokud limita existuje. „Pr=0“ v (34) znamená hustotu nula.
Pro pevné epsilon se počet příliš krátkých konců v každém bloku
2^m<=n<2^(m+1) omezuje počtem řetězců alpha^m. Sečtení geometrické řady
dává pro n<=N horní mez O(N^(log(alpha))), což je o(N).

Pro n>=4 definujme normalizovanou chybu
h(n)=(l(n)-lambda(n)-lambda(n)/lambda(lambda(n))) /
     (lambda(n)/lambda(lambda(n))). Horní odhad (25) dává h(n)<=g(n)
pro nějakou nezápornou funkci g(n)->0. Z dolního odhadu má množina
{n:h(n)<=-1/k} hustotu nula pro každé kladné celé k.

Zvolme rostoucí N_k tak, aby pro N>=N_k tato množina měla mezi 1 a N
nejvýše N/k členů, a také aby g(n)<1/k pro n>=N_k. Položme f(n)=2/k
pro N_k<=n<N_(k+1). Potom f(n)->0. Kladná odchylka nedosáhne f(n).
Je-li N ve k-tém bloku, pak pro n<=N platí f(n)>=2/k, až na pevný
úvodní úsek, a proto záporné výjimky jsou podmnožinou {h(n)<=-1/k}.
Jejich podíl je nejvýše 1/k plus zanedbatelný úvod. To dokazuje přesně
(34), včetně absolutní hodnoty a jediné funkce f platné pro všechna n.
Konečně mnoho malých n s nedefinovaným jmenovatelem v asymptotickém
zápisu se vynechá; na hustotu nemá vliv.

## 7. Přesné konečné kontroly a primární zdroj

`verify_powers_counting.py` prošel ve dvou blocích:

- Všech 32768 rodin z patnácti intervalů na pěti bodech: zachování
  sjednocení, násobnost nejvýše dvě a správné sloučení komponent.
- Všech 81773 řetězců délek 0–8, pro delta=1/8,1/4,1/3: celkem
  245319 přesných kontrol lemmatu P, intervalových mezí, omezených
  indexů a jednoznačné rekonstrukce z neuspořádané množiny dvojic.

Logaritmická nerovnost lemmatu byla testována výhradně celočíselně:
pro b=p/q je ekvivalentní 2^t*q^(2t)<=2^s*p^(2t). Žádné zaokrouhlování.
Počty řetězců přesných délek jsou 1,1,2,6,25,135,913,7499,73191.
Nejde o nové hledání jejich minim; kontrolují se zde jiné matematické
vlastnosti než v předchozích blocích. Časy 0.867718950 a 6.832633503 s,
oba exit 0, limit 240 s, session 21103. Nic nezůstává běžet a úspěšné
kontroly se nemají opakovat.

[Erdősův původní článek](https://matwbn.icm.edu.pl/ksiazki/aa/aa6/aa618.pdf),
Acta Arithmetica 6 (1960), 77–81, byl přečten vizuálně celý na třech
dvojstranách 76–77,78–79,80–81. Pravá strana první dvojstrany obsahuje
začátek článku; levá patří předchozí práci. Na 78–80 je původní
rozdělení do tří tříd, kódování dvojicemi, intervalový argument a
asymptotický odhad. Autorství, rok i rozsah stran souhlasí s knihou;
přijetí rukopisu je datováno 20. 8. 1959. Zobecnění na více sčítanců
a řetězce s odčítáním na straně 81 jsou zde pouze přečtena, nikoli
zahrnuta do důkazu tohoto bloku.

Vizuálně byla přečtena i původní časopisecká oprava na straně 114,
v pravé části třetí dvojstrany souboru `aa6110.pdf`. Opravuje výraz pro
počet disjunktních intervalů za (7) na straně 78, nikoli prázdnou volbu
z C0224. Náš důkaz místo tohoto původního pomocného odhadu používá již
ověřenou Knuthovu větu A a výše uvedený samostatný intervalový argument.

Přístup přes Rényiho archiv a webový odkaz vydavatele vrátil při lokálním
stahování nebo otevření HTTP 403; webový text Rényiho kopie byl dostupný,
ale nekvalitní OCR nebylo použito jako autoritativní sazba. Fungoval
archiv ICM. Vyhledávání nejprve odkazovalo na předchozí článek `aa617.pdf`,
který obsahuje pouze přesah začátku Erdősova článku na poslední straně.
Správný úplný zdroj je `aa618.pdf`. Rozdíl byl ověřen z vykreslených
stran; nepřičítá se jako chyba knize ani článku.
