# §3.5-35–37,39: výběry, bloky bitů a dolní mez discrepancy

Stav1.11.2026. Původní zadání183 a odpovědi598 přečteny vizuálně.
Všechny čtyři vrstvy errat a aktuální TeX zkontrolovány podle stran,
indexů a témat. Pro39 je známá jen změna obtížnostiHM45->HM42 z8.9.2016;
nové C0066/C0067 níže tím nejsou opraveny. Novější fyzický tisk ani
prvenství nejsou ověřeny. Návrhy hlášení zůstávají neodeslané.

R4 vyžaduje nekonečnou distribuci při každém vypočitatelném injektivním
přeskupení indexů; R5 povoluje rozhodovat o výběru aktuálního členu jen
podle dříve viděné minulosti, v původním pořadí. R6 dovoluje navíc
adaptivní pořadí čtení dosud neviděných členů. Přesné definice, skládání
pravidel a plnou míru R6 poskytuje `selection-randomness.md`.
Dolní a horní hustota znamenají dolní a horní limitu podílu výskytů.

## 1. Úloha35 a V2-C0066: nezačínat na nule či jedničce

Nechť s_0,s_1,... je vypočitatelná injektivní posloupnost nezáporných
indexů. Označme nu(K)=sum_(j<K) X_(s_j). Chceme dokázat
liminf nu(K)/K<=1/2<=limsup nu(K)/K pro každé binární R5 X.

Tištěná odpověď začíná a_0=s_0 a pokračuje

```
a_(m+1) = max{s_j: 0<=j<2^(a_m)}.
```

Pro povolené s_j=j dostaneme a_m=0 pro všechna m. Všechny intervaly
[a_m,a_(m+1)) jsou prázdné; pravidlo nevybere nic a závěrečný podíl
nu(a_m)/a_m je0/0. Ani zákaz nuly samotný nestačí: pro s=(1,0,2,3,...)
je a_m=1 pro všechna m a intervaly jsou opět prázdné.
To je **V2-C0066**, chyba inicializace pomocného důkazu, nikoli tvrzení35.
Stačí a_0=max(2,s_0), nebo jednoduše a_0=2. Pro a_m>=2 má množina
2^(a_m) různých nezáporných čísel maximum alespoň2^(a_m)−1>a_m,
takže opravené meze přísně rostou.

Zde je úplný důkaz s opraveným začátkem. Položme K_m=2^(a_m) a na
každém intervalu[a_m,a_(m+1)) vybírejme n právě když n=s_j pro některé
j<K_m. Pravidlo je totální a vypočitatelné: konečně dopočte meze a
příslušný seznam indexů. Nezávisí ani na hodnotách X, což je dovoleno.

Označme A_m množinu indexů vybraných před a_(m+1) a T_m={s_j:j<K_m}.
Protože K_m rostou, A_m je podmnožinou T_m. Všechny prvky T_m mezi
a_m a a_(m+1) jsou vybrány; chybět mohou jen indexy pod a_m a jeden
index rovný a_(m+1). Tedy

```
|T_m \ A_m| <= a_m+1,
|A_m| >= K_m−a_m−1,
(a_m+1)/K_m -> 0.
```

Výběr je nekonečný, a R5 proto dává správnou četnost1/2 v jeho prefixech.
Porovnání množin pak dává nu(K_m)/K_m->1/2. To dokazuje obě požadované
nerovnosti, i když celková limita přeskupené posloupnosti neexistuje.

Tištěný poslední displej používá nu(a_m)/a_m. Po opravě inicializace
je pravdivý také; nejde však o totéž porovnání prefixů jako výše.
Pro úplnost jej lze dokázat dvěma pravidly: zvlášť pro sudá a lichá m
na intervalu[a_(m−1),a_(m+1)) vybírejme prvky{s_j:j<a_m}.
Každá taková rodina intervalů je disjunktní a navazující. Před horním
koncem je její výběr podmnožinou tohoto prefixu, s nejvýše a_(m−1)+1
chybějícími indexy. Všechny potřebné indexy nepřesahují a_(m+1),
protože a_m<2^(a_m). Poměr(a_(m−1)+1)/a_m jde k0. R5 dává limitu1/2
zvlášť pro obě parity, a tím i pro celé m.
Draft: `reports/C0066-loveland-initial-boundary-draft.txt`.

## 2. Úloha36: převod bitů na rostoucí bloky

Nechť T_n=n(n+1)/2. Reálný člen U_n má jako konečný binární rozvoj bity
X_(T_n),...,X_(T_(n+1)−1), tedy n+1 bitů, následované nulami.
Všechny bloky jsou disjunktní a dohromady pokrývají všechny pozice X.
Konstrukce je dobře definovaná v[0,1), i když blok obsahuje samé jedničky.

Fixujme základ b>=2, adaptivní čtecí algoritmus S nad Y_n=floor(bU_n)
a pravidlo R vybírající nekonečnou podposloupnost Z. Ještě než S čte
nový blok, víme z dosavadní minulosti, zda jej R vybere. Binární
algoritmus S' simuluje S: v daném novém bloku přečte všechny bity,
z nich přesně vypočte Y_n a předá jej S. Žádný bit nečte dvakrát.

Pro pevnou přesnost K vybírá R' z každého vybraného bloku jeho prvních
min(K,n+1) bitů. Toto rozhodnutí lze pro každý bit učinit před jeho
přečtením. R6 pro X proto dává R5 náhodnost a následně nekonečnou
distribuci vybrané binární posloupnosti. Pouze konečně mnoho bloků
je kratších než K; po odstranění tohoto konečného prefixu se bity
seskupují do K-slov. VětaC zaručuje, že tato slova mají rovnoměrné
četnosti2^(−K). To platí i po pevném posunu začátku seskupování.

Z každého vybraného U známe tedy rovnoměrně distribuovanou dyadickou
buňku délky2^(−K), ve které leží. Interval[a/b,(a+1)/b) má nejvýše
dvě částečně protínané krajní buňky. Dolní a horní hustota Z=a se
proto od1/b liší o méně než2/2^K. K->infinity dává přesně1/b.
Pro knižní cílovou chybu1/2^k stačí v tomto odhadu číst K=k+1 bitů;
jediná buňka pro libovolně položený interval sama nestačí. Například
při b=3,K=3,a=1 je vnější pokrytí4/8, vzdálené od1/3 o1/6>1/8.
Toto je upřesnění důkazu aproximace, nikoli protipříklad k tvrzení36
nebo jeho výsledným nulovým limitním chybám.

Proto každé b a každá dvojice S,R dávají správnou1-distribuci;
U splňuje R6. Nevyžaduje to rozhodovat přesné porovnání nevypočitatelných
reálných čísel: každý U_n je konečný racionální blok a b je celé.

Dodatky odpovědi platí také:

- Pro R5 procházejme bloky i bity v původním pořadí; stejná simulace
  je obyčejné pravidlo R5 a opět dává rovnoměrné K-prefixy.
- Pro R4 je pořadí bloků předem vypočitatelné a injektivní. Získávání
  prvních K bitů každého vybraného bloku je vypočitatelná injekce bitových
  indexů. R4 pro X dává jejich nekonečnou distribuci; seskupení libovolného
  počtu po sobě jdoucích K-bloků dokazuje všechny dimenze reálné R4.
- Pro pouhou R1 tvrzení selže. V nekonečně distribuované binární
  posloupnosti vynulujme všechny trojúhelníkové indexy T_n. Mají hustotu0,
  a proto zachovají každou pevnou distribuci oken (správný odhad je
  počet zasažených bitů krát délka okna). Každý U_n má potom první bit0,
  takže všechna U_n<1/2. Zdrojový index binom(n,2) označuje tutéž
  množinu trojúhelníkových pozic.

## 3. Úloha37: úplný mírový důkaz Coppersmithovy konstrukce

Začněme nezávislými rovnoměrnými U_i v[0,1). Pro n>=2 tvoří blok
I_n={(n−1)^2+1,...,n^2} celkem2n−1 pozic. Prvních2n−2 členů nezměníme.
Nechť delta_n je parita počtu z nich, které leží pod1/2. Poslední
člen nahradíme

```
V_(n^2) = (U_(n^2)+delta_n)/2.
```

U_0,U_1 ponecháme. Různé bloky jsou nezávislé. V každém bloku je
vynucen právě jeden vztah mezi nejvyššími bity: jejich celková parita
je sudá (počet vnitřních bitů je sudý). Všechny nižší bity zůstávají
nezávislé a rovnoměrné. Každá **vlastní podmnožina** pozic bloku má
součinový rovnoměrný zákon: obsahuje-li poslední pozici, zbývá alespoň
jeden nepoužitý vnitřní bit, který činí delta rovnoměrnou nezávislou
na všech viděných hodnotách; neobsahuje-li poslední, je to okamžité.

Fixujme vypočitatelnou injekci s a rozměr k. Indikátor členství k-okna
V_(s_j),...,V_(s_(j+k−1)) v daném racionálním boxu má od určitého j
správný průměr p: každé okno používá jen k souřadnic a konečně mnoho
malých bloků se v injekci objeví jen konečněkrát. Dvě nepřekrývající
se k-okna používají nejvýše2k pozic. Po vynechání konečně mnoha bloků
s délkou<=2k jsou tyto dvě události nezávislé podle předchozího odstavce.
Překrývajících se dvojic oken je jenO(kN), a proto rozptyl součtu N
indikátorů jeO(kN).

Čebyševova nerovnost pro prefixy N=m^2 má summabilní pravděpodobnosti
odchylky od p. Borelovo–Cantelliho lemma dává skoro jistou konvergenci
podél těchto prefixů; mezi m^2 a(m+1)^2 se podíl změní nejvýšeO(1/m).
Limita p tedy platí pro všechny prefixy. Spočetné sjednocení výjimek
pro všechny s,k a racionální boxy má míru0. Skoro každá takto vzniklá
V splňuje R4. Není zde tvrzení o všech nevypočitatelných injekcích.

Naopak R5 selže skoro jistě. Pravidlo v binárním základu vybírá pozici
n^2 právě když parita předchozího vnitřku I_n je0. Toto rozhodnutí zná
z minulosti, protože vnitřní členy se nezměnily. Každý vybraný člen má
V_(n^2)<1/2, tedy vybraný bit je0. Parity různých bloků jsou nezávislé
rovnoměrné bity, takže výběr je skoro jistě nekonečný. R5 proto neplatí.
Průnik obou událostí míry1 dokazuje existenci požadované posloupnosti.

IBM autorská metadata potvrzují článek *On two criteria for infinite
random sequences*, Advances in Mathematics14(1974),333–334,
DOI10.1016/0001-8708(74)90035-8. Plný článek ani Herzogova disertace1975
nebyly přečteny; publisher web byl nedostupný. Důkaz výše je vlastní
úplná kontrola knižní konstrukce. Metadata a omezení:
`sources/coppersmith-1974-criteria.json`.

## 4. Úloha39: primární Schmidtův důkaz a V2-C0067

**Oprava revize 12. listopadu 2026:** C0067 je dismissed. Původní sazba
na straně 183 definuje počet přes `j <= n`, nikoli `j < n` použité níže.
Pro `N=1,n=0,U_0<u<1` je tedy `nu_0(u)=1` a tvrzený protipříklad
nefunguje. Následující historická analýza standardní konvence jej
nedokládá; viz `../../../integration/2026-11-12-novelty-review/notes/vol2-c0067-dismissal.md`.

Pro n bodů definujme počet Z(n,u)=#{0<=j<n: U_j<u}, podepsanou
odchylku f(n,u)=Z(n,u)−nu a nenormalizovanou hvězdovou discrepanci
D(n)=sup_(0<=u<1)|f(n,u)|. Slovo discrepancy zde měří největší odchylku
počtu bodů v počátečním intervalu od jeho očekávané délky krát n.

Primární článek W. M. Schmidt, *Irregularities of distribution,VII*,
Acta Arithmetica21(1972),45–50 byl přečten celý vizuálně a zkontrolován.
PDF má čtyři dvojstrany; OCR je prázdné. Vlastní PDF a SHA jsou
v `sources/schmidt-1972-irregularities-vii.{pdf,json}`.
[Primární PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa21/aa21138.pdf).
Věta1 dává pro každé N>=1 nějaké1<=n<=N s D(n)>0.01 lnN.

Pro kontrolu hlavní indukce definujme h(I,u)=max_(n in I)f(n,u)−min_(n in I)f(n,u),
kde I je konečný interval celočíselných časů. Parametr u prodlužujeme
periodicky. Pro J,J' podintervaly I a d(n)=f(n,v)−f(n,u) položme

```
H(J,J';u,v) = max(min_J d−max_J' d, min_J' d−max_J d).
```

Klíčová čistě algebraická nerovnost je

```
h(I,u)+h(I,v) >= H(J,J';u,v)
  + [h(J,u)+h(J,v)+h(J',u)+h(J',v)]/2.                 (A)
```

Pro důkaz zvolme orientaci H=min_J d−max_J' d. Pak d(p)−d(q)>=H pro
všechna p v J,q v J'. Dosadíme jednou p maximalizující f(.,u) v J
s q maximalizujícím f(.,v) v J', podruhé p minimalizující f(.,v) v J
s q minimalizujícím f(.,u) v J'. Přičteme čtyři rovnosti max−min pro
oba parametry v J,J'. Výsledná levá strana jsou dvě rozdílové dvojice
pro parametr u a dvě pro v; každá je nejvýše příslušné h(I,.).
Vyjde2h(I,u)+2h(I,v)>=2H+součet čtyř h, tedy(A).

Schmidtova indukce dokazuje pro každý interval I délky alespoň4^t

```
(1/4^t)*sum_(j=1)^(4^t) h(I,beta+j/4^t) >= t/32.     (B)
```

Základ: rozdíl přírůstků f při parametrech beta,beta+1/2 v sousedních
časech je celé číslo minus1/2. Proto h(I,beta)+h(I,beta+1/2)>=1/2,
a součet přes čtyři body má dokonce dolní mez1, větší než4/32.

Pro krok nechť q=4^t. Z I vybereme první a třetí q-časový interval J,J'.
Pro jemnou síť u_j=beta+j/(4q) nechť z_j počítá prostředních q bodů
v j-té buňce modulo1; z_j jsou nezáporná celá čísla, sum z_j=q.
Pro n v J,n' v J' je přírůstek počtu bodů v této buňce alespoň z_j,
zato přírůstek očekávaného počtu menší než3/4. Tudíž
H(J,J';u_(j−1),u_j)>=z_j−3/4>=z_j/4, pokud z_j>=1.
Pro z_j=0 stačí triviální h(I,.)>=průměr h(J,.),h(J',.).
Sečtením(A) přes všech4q buněk a rozdělením jemné sítě na čtyři
posunuté hrubé sítě dostaneme

```
2*sum_j h(I,u_j) >= q/4 + q*t/4 = q*(t+1)/4.
```

To je(B) pro t+1. Následuje max|f|>=t/64. Pro4^t<=N<4^(t+1),t>=9
je tato mez větší než0.01 lnN. Menší N pokryje D(1)>=1/2. Tím je
primární věta včetně konstanty ověřena, bez závislosti na nečteném
předchozím článkuVI. Jeho potřebné lemma(A) je zde dokázáno přímo.

**V2-C0067.** Kniha má místo1<=n<=N podmínku0<=n<N a stále píše
„for any N“. Při N=1 připouští pouze n=0: Z(0,u)=0 a c ln1=0,
takže požadovaná ostrá nerovnost0>0 nemůže platit pro žádné u.
Stačí doplnit N>=2. Pro N>=3 použijeme Schmidtovu větu na N−1;
ln(N−1)>=lnN/2. Pro N=2 vezmeme n=1 a u=1/2. Opravené zadání tedy
platí například s c=1/200, při nezměněné horní podmínce n<N.
Alternativně lze přejít na původní1<=n<=N, čímž funguje i N=1.
Draft: `reports/C0067-discrepancy-empty-prefix-draft.txt`.

Poznámka o „best possible c“ není tvrzení, že její hodnotu tento audit
určil. Novější primární úvod Clément2024, §1, stále popisuje mezeru
mezi známými asymptotickými konstantami pro jednorozměrné posloupnosti
[arXiv2406.18132v1](https://arxiv.org/html/2406.18132v1).
Tato asymptotická optimalizace není automaticky totožná s nejlepším c
v konečné formulaci pro každé N. Z vymezené rešerše neděláme tvrzení
o úplném stavu literatury do roku2026 ani nepřevádíme numerické
experimenty na důkaz optimální konstanty.

## 5. Reprodukovatelné konečné kontroly

`verify_selection_extensions.py` má čtyři samostatně uložené bloky:

- 5040 permutací prvních sedmi indexů,10080 kontrol množin v opraveném
 Lovelandově výběru; oba původní pevné začátky0 a1 reprodukovány.
- 4216 dyadických pokrytí intervalů ověřuje bezpečnou chybu2/2^K.
- 672 vlastních podmnožin souřadnic v Coppersmithových blocích délek
 3,5,7,9 má přesně rovnoměrný zákon; celá vedoucí parita je sudá.
- 6561 dvojic malých funkcí ověřuje algebraické lemma(A). N=1 je
 samostatně evidován jako přesný protipříklad k tištěné formulaci.

Vše prošlo, běh24124 skončil0; výsledky `results/selection-extensions.json`.
Tyto konečné rozsahy pouze doplňují obecné důkazy. Nejsou důkazem
všech algoritmů, nekonečných limit ani optimální konstanty.
