# MPR 117–118: všechny Fourierovy a momentové kroky

D215–D216; 7. listopadu 2026. Původní zadání str.24/file44,
odpovědi str.389/file409 a autorův PS str.24,45–46/file30,51–52
byly přímo zobrazeny. Žádný nález, kandidát, běh ani restart.
Dvě přesně vymezené bibliografické výjimky jsou na konci.

## 117: doména, binomická transformace a inverze

Nechť n je nezáporné celé, m kladné celé a p∈[0,1], q=1−p.
Pro m=1 je zbytek vždy0. Všechny vzorce níže platí i tehdy
(prázdný součet nenulových frekvencí). Konečná informativní
pravá strana vyžaduje npq>0; degenerované případy řešíme zvlášť.
Pravděpodobnosti B_n(p) mají součet(p+q)^n=1. Pro n=0 nebo
p∈{0,1} se obvyklé binomické mocniny vykládají spojitě podle
tohoto polynomu, nikoli jako neurčité jednotlivé výrazy0^0.

Položme ω=exp(2πi/m). Binomická věta dává přesně

    E ω^(jX) = Σ_{k=0}^n binom(n,k)p^k q^(n−k)ω^(jk)
             = (q+pω^j)^n.

Všechny součty jsou konečné. Pro každé celé z platí
Σ_{j=0}^{m−1}ω^(jz)=m, když m|z, a0 jinak: v druhém případě
je ω^z≠1 a geometrický součet má čitatel1−ω^(mz)=0.
Dosazením z=X−r a očekáváním vznikne inverze

    P(X mod m=r)=(1/m)Σ_{j=0}^{m−1}ω^(−jr)E ω^(jX).

Člen j=0 je1/m. Jelikož |ω^(−jr)|=1, trojúhelníková nerovnost
pro zbývající konečný součet dává

    |P(X mod m=r)−1/m| ≤ (1/m)Σ_{j=1}^{m−1}|E ω^(jX)|.

Tím je zkontrolován záporný exponent i každá normalizace1/m;
nepředpokládá se nezávislost pomocných Fourierových veličin.

## 117: norma, sinus, každý faktor8/16 a párování

Protože p,q jsou reálné a konjugát ω^j je ω^(−j), máme

    |q+pω^j|² = q²+p²+pq(ω^j+ω^(−j))
               = (p+q)²−2pq(1−cos(2πj/m))
               = 1−4pq sin²(πj/m).

Funkce sin(πt) je konkávní na[0,1/2], neboť její druhá
derivace je−π²sin(πt)≤0. Leží tedy nad tětivou mezi0 a1/2,
což dokazuje sin(πt)≥2t v celém použitém intervalu.
Pro0≤j≤m/2 z toho plyne

    |q+pω^j|² ≤ 1−16pq j²/m² ≤ exp(−16pq j²/m²).

Výraz u=16pq j²/m² patří do[0,1], protože pq≤1/4.
Nerovnost1−u≤exp(−u) plyne například z konvexity exponenciály
a tečny v0. Obě strany jsou nezáporné; umocnění na n/2 při
n>0 je tedy oprávněné a dává přesně

    |E ω^(jX)| ≤ exp(−8npq j²/m²).

To vysvětluje přechod faktoru16 na8, včetně nulové normy
p=1/2,j=m/2. Pro j≥m/2 je sin(πj/m)=sin(π(m−j)/m),
takže transformace mají stejné absolutní hodnoty pro j a m−j.
Všechny indexy1,…,m−1 se tím rozdělí na dvojice s
1≤j<m/2 a případně jediný nepárovaný j=m/2, je-li m sudé.
Každý kladný index do floor(m/2) tedy přispívá nejvýše dvakrát.
S a=8npq/m²>0 dostaneme

    (1/m)Σ_{j=1}^{m−1}|E ω^(jX)|
      ≤ (2/m)Σ_{j=1}^{floor(m/2)}exp(−a j²)
      < (2/m)Σ_{j=1}^∞exp(−a j²).

Poslední nerovnost je ostrá, protože všechny přidané členy jsou
kladné a existují indexy nad konečnou mezí. Nevyžaduje ostrou
nerovnost v některém předchozím kroku, takže funguje i pro m=1,
m=2 a rovnost v sinusovém odhadu. Řada konverguje: j²≥j dává
majorantu Σ exp(−aj)=exp(−a)/(1−exp(−a)). Tím je celá tištěná
ostrá mez dokázána bez numerického součtu nebo limitní záměny.

Při npq=0 je X deterministické (X=0 pro n=0 nebo p=0,
X=n pro p=1) a pravá řada se rovná+∞. Konečná levá strana
je tedy stále menší v rozšířeném smyslu; o přibližné rovnoměrnosti
v tomto režimu nic neplyne. Pro pevné m a0<p<1 platí a→∞,
takže geometrická majoranta→0 a rezidua jsou asymptoticky
rovnoměrná. Také pro proměnlivé m stačí npq/m²→∞. Žádná
uniformita v degenerovaných parametrech se netvrdí.

V úloze není požadován algoritmus; inverze má m konečných členů
a její vyhodnocení opakovaným čtvercováním stojí O(m(1+log(n+1)))
komplexních aritmetických operací po určení mocninω, bez tvrzení
o bitové přesnosti. Důkaz celé nekonečné meze má uvedenou přesnou
majorantu; nemusí se spouštět výpočet řady.

## 118: převzetí přesně použitelného druhého momentu

Pišme μ=EX, ν=E X². Netriviální podíl v zadání má doménu
0<ν<∞ a0≤x≤μ. Konečný druhý moment zajišťuje E|X|<∞,
tedy všechny níže rozvíjené první i druhé momenty existují.
X nemusí být nezáporné a není třeba nezávislost.

D149 v `notes/sequential-mpr-ex045-049.md`, část47, už úplně
dokázal následující přesný rozsah: pro reálné Y s EY≥0
a0<EY²<∞ platí P(Y>0)≥(EY)²/EY². Důkaz tam používá
Y_+=max(0,Y), obě bodové dominance a druhý moment nezáporné
proměnné; obsahuje všechny nulové okraje. Tento argument
přebíráme bez opakování původních kontrol.

Položme Y=X−x. Potom EY=μ−x≥0 a

    E Y² = ν−2xμ+x² = var(X)+(μ−x)².

Pokud tento výraz není0, D149 přímo dává tištěný první řetěz

    P(X≥x) ≥ P(X>x)
            ≥ (μ−x)²/[ν−x(2μ−x)].

První krok je inkluze událostí; druhý používá ostrou událost
Y>0, takže přítomnost atomu v x není zaměněna za rovnost.

## 118: všechny tři jmenovatele a původní slabší výsledek

Pro0≤x≤μ platí x(2μ−x)≥xμ≥x²≥0. Proto

    A=ν−x(2μ−x) ≤ B=ν−xμ ≤ C=ν−x² ≤ ν.

Přitom A=var(X)+(μ−x)²,
B=var(X)+μ(μ−x), C=var(X)+(μ−x)(μ+x).
Jsou tedy nezáporné. Pro x<μ jsou všechny přísně kladné;
pro x=μ a var(X)>0 jsou také kladné. Společný čitatel
(μ−x)² je nezáporný, tudíž v této doméně dostáváme přesně

    (μ−x)²/A ≥ (μ−x)²/B ≥ (μ−x)²/C ≥ (μ−x)²/ν.

První tři zlomky jsou vytištěné v odpovědi, poslední je
požadovaná mez zadání. Pro x=0 všechny jmenovatele splývají;
pro x=μ s kladným rozptylem jsou všechny čitatele0. Řetěz
proto nevyžaduje přísné nerovnosti a nevynechává koncové body.

Pokud A=0, pak X=x=μ skoro jistě. Přímo máme P(X≥x)=1
a P(X>x)=0; neurčité zesílené zlomky0/0 nevyhodnocujeme.
Pro x=μ>0 je původní zlomek ze zadání definovaný a roven0,
takže požadovaná nerovnost1≥0 platí. Pokud navícν=0,
pak X=μ=x=0 skoro jistě; levá strana je1 a izolovaný podíl
0/0 z původní meze má přirozené dolní doplnění0. Tento
degenerovaný zákon se řeší přímo, bez nové kandidátní vady.
Stejná konvence už byla přesně stanovena u47–49.

Pokudν=+∞, ale μ je konečné, pravá strana původní meze
je0 v rozšířeném smyslu a výsledek je triviální. Formulaci
s neurčitými nekonečnými prvními momenty nepoužíváme;
není součástí momentového argumentu. Tím jsou všechny
případy potřebné k zadání i tištěnému zesílení vymezeny.

## Bibliografie a errata

117: původní autorský preprint Janson–Knuth, Shellsort with
three increments, arXiv cs/9608105, Lemma3 na str.6 byl
celý přečten i zobrazen. Souhlasí transformace, exponenty,
řada i její použití. Primární Stanford profil a autorův
seznam uvádějí RSA10(1997),125–142. Přesné umístění na
finálních časopiseckých str.130–131 nebylo přímo ověřeno:
to je první, čistě bibliografická výjimka. Selhání rychlého
načtení autorova dalšího archivu nebylo vydáváno za obsah.

118: primární stránky Cambridge potvrzují všechny tři
historické svazky/roky/rozsahy:26(1930),337–357;26(1930),
458–474;28(1932),190–205. Původní text důkazu Lemma19
a přesná historie atribuce nebyly rychle dostupné; druhá
bibliografická výjimka výslovně zahrnuje obsah tohoto
historického tvrzení. Matematický důkaz118 na něm nezávisí
a je celý uveden výše. Autorovo hodnotící slovo „dubious“
není změněno na prokázané tvrzení o prvenství.

Šest vrstev errat a tři TeX zdroje prohledány podle
čísla úlohy, obou vydání a stránek i slovních klíčů.
Není použitelná oprava117 nebo118. Opravy114 a121 na
stejných fasciklových stránkách jsou jiný rozsah. Plný
otisk hledání je uložen samostatně. Celé117–118 checked;
file44 a409 zůstávají partial pro následující úlohy.
