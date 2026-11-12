# §3.3.2 J a úlohy28–30: narozeninové mezery a partice

Uzavřený blok1.11.2026. Původní strany71–72,79,568–570 byly
vizuálně přečteny; pořadí v DjVu je o12 vyšší. Kontrolujeme
ideální model nezávislých rovnoměrných narozenin a zvlášť
reprodukovatelné experimenty s generátory. Nové nálezy jsou
C0024–C0028; hlavní asymptotika a tabulka na71 jsou správné.

## 1. Model a přesné počty v28

Nechť m je počet dnů, n počet označených narozenin Y_i z0..m−1.
Po seřazení vytvoříme n kruhových mezer včetně poslední mezery
přes konec roku. R=n−počet různých délek je počet opakovaných
mezer a s počet nulových mezer. Číslo b_nrs(m) počítá n-tice
s těmito parametry. p_n(M) počítá partice M na nejvýše n
kladných částí a je0 pro M<0. Položme N=n(n+1)/2 a
q_n(m)=p_n(m−N), počet particí na n různých kladných částí.

Ukotvěme narozeniny označené1. Máme m možností pro jejich
den. Kladné mezery zapsané po kružnici od této kotvy jsou
uspořádanou kompozicí m, tj. n kladnými celými čísly se součtem m.
Zbylých n−1 označení lze přiřadit v(n−1)! pořadích. Multimnožina
délek s násobnostmi w_1,w_2,... má n!/prod w_i! různých pořadí.
Pro různé délky tedy

```text
b_n00(m) = m n!(n−1)! q_n(m).
```

Jsou-li nulové mezery, rozdělíme označení do j=n−s neprázdných
skupin podle obsazeného dne. Počet takových rozdělení je
Stirlingovo číslo {n\j}. Skupiny jednoznačně označíme například
jejich minimálním prvkem. Kladné mezery odpovídají j různým
narozeninám; s nulových mezer přidá s−1 opakování. Pro s>0:

```text
b_nrs(m) = {n\n−s} b_(n−s,r+1−s,0)(m).
```

Při R=0 se možnosti s=0 a s=1 sčítají. Vytištěné minus
v28(c) je C0024. Také první rovnost v posledním odstavci
odpovědi30 na570 opomíjí b_n01; v kontextu tam jde o vedoucí
asymptotický člen, neboť následující věta výslovně uvádí
zanedbaný příspěvek O(1/n). Tabulka tento příspěvek obsahuje.

## 2. Generující funkce v29

Generující funkce je mocninná řada, jejíž koeficient u z^m
zde ukládá počet dělený m: b_nr(z)=sum_(m>0)b_nr0(m)z^m/m.
Označme D_n(z)=prod_(k=1)^n(1−z^k).

Seřazené kladné mezery mají první hodnotu alespoň1; každé
další místo buď opakuje předchozí hodnotu, nebo ji přísně
zvyšuje. Bit b_k označuje rovnost na hranici k,k+1. Položme
c_0=1, c_k=1+b_k c_(k−1). Součin c_k je prod w_i! z části1.
Při r=sum b_k má daný vzor rovností normalizovaný čitatel

```text
z^(N−sum_(k=1)^(n−1)(n−k)b_k)
  prod_(k:b_k=1)(1−z^(n−k)) / prod_(k=1)^(n−1)c_k,
```

se společným jmenovatelem D_n. Důvod: první hodnota přispívá
z^n/(1−z^n); přísný skok na pozici k přispívá
z^(n−k)/(1−z^(n−k)); rovnost přispívá1. Převedení na společný
jmenovatel dává uvedený výraz. To dokazuje obecný binární
vzorec v knize, včetně vah násobností.

Pro r=0,1,2 vycházejí po dělení n!(n−1)! čitatelé

```text
r0: z^N,
r1: (1/2) z^binom(n,2) sum_(1<=k<n)(z^k−z^n),
r2: z^binom(n−1,2) [
 (1/4) sum_(1<=j<k<n)(z^j−z^n)(z^k−z^(n−1))
 +(1/6) sum_(1<=k<n)(z^k−z^n)(z^k−z^(n−1)) ].
```

V r2 mají dvě oddělené dvojice váhu1/4 a trojice váhu1/6.
Přeindexování druhé oddělené rovnosti o1 dává právě první
součet. Při součtu přes všechna r bez váhy jsou přípustné
všechny kladné kompozice; výsledkem je
(n−1)!z^n/(1−z)^n. Souhlasí i zvláštní případ w=1 v knize,
kde je vlevo navíc dělení n!(n−1)!z^n.

Nezávislý úplný průchod219456 narozeninovými slovy ve42 modelech
n=1..6,m=1..7 ověřil28(a,b) i opravené28(c). Druhý model
generuje292022 seřazených particí a váží je n!/prod w_i!;
2160 koeficientů pro n=1..9,m=1..48 souhlasí s obecným
binárním vzorcem. Ověřeno24 zjednodušených čitatelů pro r<=2.
Obě metody používají jinou reprezentaci objektů; nejde o dva
běhy téhož algoritmu. Viz `results/birthday-spacings.json`.

## 3. Asymptotika a její přesnost v30

[Samostatný certifikát](partition-certificate.md) dokazuje
hlavní asymptotické vzorce pro p_n(m),q_n(m), m=n³/alpha,
pevné alpha>0, s relativním zbytkem O(n^(-3)). Používá
polynomiální příspěvek pólu1 a explicitní meze všech ostatních
kořenů jednotky. Nezávislé rozvoje v1−z ověřují76 malých
modelů; symbolický rozvoj potvrzuje všechny vytištěné koeficienty.

Pro pravděpodobnostní závěr stačí i konečné diference. Z téhož
polynomiálního rozvoje po h derivacích, pro každé pevné h, plyne

```text
Q_n^(h)(m+u)/q_n(m) = (n/m)^h (1+O(1/n)),   |u|=O(n),
```

kde Q_n je polynomiální příspěvek k q_n, nikoli derivace
diskrétního počtu. Zbývající kořeny jednotky jsou menší než
libovolná mocnina1/n relativně k hlavnímu členu, i po konečných
diferencích. Derivování pevných h členů nezhorší odhad zbytku
v certifikátu: faktor (n−1−2k)_h je nejvýše n^h.

Faktor z^(−k)−1 v generující funkci znamená dopřednou diferenci
q_n(m+k)−q_n(m). Opakovaná integrace předchozího odhadu
ukazuje, že h takových faktorů násobí hlavní člen
(n/m)^h prod k, s relativní chybou O(1/n), rovnoměrně pro
1<=k<n. Pro r rovností dominují neadjacentní hranice, každá
s vahou1/2. Součet jejich součinů indexů je

```text
(sum_(k=1)^(n−1) k)^r/r! + O(n^(2r−1)).
```

Vynechané vzory mají sousední rovnosti, tedy nejvýše r−1
volných indexů, a přispívají O(1/n) po normalizaci. Proto
příspěvek kladných mezer k Pr(R=r) je

```text
exp(−alpha/4) (alpha/4)^r/r! + O(1/n).
```

Pravděpodobnost jakýchkoli shodných narozenin je nejvýše
binom(n,2)/m=O(1/n), takže stejný závěr platí pro všechny
mezery. To dokazuje požadované r=0,1,2 i tvrzení pro pevné r.
Jde o Poissonovo rozdělení s parametrem alpha/4, tj. rozdělení
s pravděpodobnostmi exp(−lambda)lambda^r/r!.

Tvrzení o průměru nelze odvodit pouze z konvergence jednotlivých
pravděpodobností. Zde je samostatný odhad: při kladných mezerách
je pravděpodobnost rovnosti dané dvojice

```text
sum_(t>=1) binom(m−2t−1,n−3) / binom(m−1,n−1)
 = (n−1)/(2(m−1)) + O(n²/m²).
```

Součet po jedné paritě se od poloviny celého součtu liší
nejvýše polovinou největšího členu, protože sčítance jsou
monotónní. Celý součet vyhodnotí hokejková binomická identita.
Pravděpodobnost rovnosti dané trojice je O(n²/m²), obdobně
součtem po každém třetím indexu. Součet dvojic shodných mezer
se od R liší nejvýše počtem shodných trojic. Tedy
E R=alpha/4+O(1/n) v kladném modelu, neboť n³·n²/m²=O(1/n).
Při s nulových mezerách je jejich příspěvek nejvýše s,
E s<=binom(n,2)/m. Podmíněný průměr opakovaných kladných mezer
pro libovolných j<=n obsazených dnů je O(j³/m), rovnoměrně
omezený. Událost s>0 proto změní průměr jen o O(1/n).

Pro konkrétní n512,m2^25 certifikát v racionální aritmetice
potvrzuje všechny čtyři devítimístné pravděpodobnosti na71;
největší chyba je menší než2.401·10^(-38). Potvrzuje i všech
19 číslic prefixu q_512(2^25)/10^1514 na570. Samostatné
vyhodnocení tištěné tříčlenné aproximace pomocí střídavého
rozvoje exp(−1) dává7.08069350134618..., tedy správně vytištěné
7.080693501. Tato aproximace není přesný počet.

## 4. Pomocný sedlový důkaz a errata

Taylorova identita pro g(se^t) je obvyklá Taylorova věta
s integrálním zbytkem, po zavedení theta=z d/dz. Použití
operátoru a integrační cesty je správné. V derivaci theta^j f
jsou však dvě chyby: j! místo(j−1)! a opačné znaménko
pravidelného součtu; viz C0025. Bernoulliho konvence v celém
svazku se21.3.2021 změnila na B_1=+1/2. Navazující opravy
strany569 z22.3.2021 jsou s ní konzistentní a samy chybou nejsou.

Oprava12.4.1999 správně mění c^3 na c_3, nikoli znaménko.
Oprava7.1.2004 chybně zahrnuje kubický člen do O(n^(-3));
c_3=1/(3sqrt(n))+O(n^(-9/2)), viz C0026. Vytištěný c_1 po
opravě2021 a konstantní faktor jsou správné: exponent
konstantního faktoru mimo exp(alpha/4) je
(alpha/4−alpha²/72)/n−alpha²/(48n²)+O(n^(-3)); jeho
exponenciála dává přesně koeficienty na569.

Pro q_n je dodatečný faktor exp(−rho N) správný, ale přírůstek
c_1 musí být delta N, viz C0028. Reciprocity particí vyžaduje
znaménko(−1)^(n−1), které je v poslední větě ztraceno, viz C0027.
Všechny výsledné asymptotické formule přesto potvrzuje vlastní
důkaz. Ten také dodává explicitní rovnoměrné meze příspěvků
ostatních pólů místo stručného odhadu vedlejších oblouků v knize.

## 5. Praktická část J a zdrojový rozsah

Pro rekurenci X_n=X_(n−24)+X_(n−55) modulo m platí
X_n+X_(n−86) ≡ X_(n−24)+X_(n−31). Obě strany jsou kongruentní
s X_(n−24)+X_(n−55)+X_(n−86); z toho plynou obě rovnosti
rozdílů modulo m. Původní sazba skutečně obsahuje kongruence.
Pokud příslušné dvojice sousedí po kružnici, mají stejnou mezeru.
Výběr každého druhého prvku nemůže obsahovat všechny čtyři
uvedené indexy, protože31 je liché a ostatní rozdíly sudé.
To odstraňuje právě tento mechanismus, nedokazuje úspěch ve
všech testech, pro všechna semena nebo velikosti vzorku.

`experiment_birthday_generators.py` používá n512,m2^25,
2000 pokusů na řádek a tři předem pevně zvolené55slovné stavy.
Stavy i jejich SHAKE256 zdrojové řetězce jsou ve výsledném JSON.
Referenční deterministický proud SHAKE256 slouží jen pro srovnání;
netvrdíme jeho skutečnou nezávislost. Čtyřkategoriální chi-kvadrát
statistika používá certifikované pravděpodobnosti z části3.

|Proud|Průměr R|Chi-kvadrát|Horní ocas pro3 stupně volnosti|
|---|---:|---:|---:|
|SHAKE256 reference|0.979|1.1981|0.7535|
|55/24, stav0, krok1|2.587|4925.05|1.93·10^(-1068)|
|55/24, stav1, krok1|2.657|5122.05|3.30·10^(-1111)|
|55/24, stav2, krok1|2.574|5024.35|5.37·10^(-1090)|
|55/24, stav0, krok2|0.9515|3.4132|0.3322|
|55/24, stav1, krok2|1.0125|0.8520|0.8370|
|55/24, stav2, krok2|0.957|2.9285|0.4028|

Extrémní malé hodnoty ocasu jsou hodnoty asymptotického
chi-kvadrát modelu, nikoli přesné pravděpodobnosti. Experiment
silně podporuje popsané selhání i zlepšení při kroku2. Slovo
„typically R≈2“ je kvalitativní shrnutí; naše průměry jsou2.57–2.66.
Neznáme historická semena ani přesný algoritmus odstranění
kongruenčních shod ve statistice R′, takže ji nereprodukujeme
a tvrzení „usually“ evidujeme jako empirickou zprávu autora.

Původní článek Marsaglia–Zaman–Tsang1990, všech pět stran35–39,
byl vizuálně přečten. Jeho test používá lineární mezery a100
pokusů; uvádí selhání subtraktivních generátorů97/33 a55/24.
Podporuje kvalitativní závěr, ale nejde o totožný kruhový test
ani rekonstrukci Knuthových čísel. Svazek časopisu9 odpovídá
oficiálním metadatům a známé opravě knihy z2002; první stránka
samotného článku má v záhlaví chybně8. Metadata i PDF uloženy.

Další bibliografické odkazy a přesné hranice jejich čtení jsou
v `sources/birthday-bibliography.json`. Szekeres1953 odpovídá
známé opravě1093->1953 z1999. Celé práce Szekerese, Pólyi ani
de Bruijnova kapitola zde nejsou označeny za přečtené. Vlastní
důkazy výše na jejich nekontrolovaném použití nezávisí.

Všechny čtyři historické/aktuální vrstvy errat a aktuální TeX
prohledány1.11.2026. Nejnovější fyzický dotisk a prvenství
nálezů nejsou ověřeny; návrhy hlášení zůstávají neodeslané.
