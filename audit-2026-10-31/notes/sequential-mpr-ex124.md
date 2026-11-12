# MPR 124: úplný importance-sampling důkaz po známém E002

D222, 7. listopadu 2026. Zadání p25/file45 a odpověď
p390/file410 i autorův PS p25/47,file31/53 zobrazeny.
Známé E002 se zachovává bez karty; původní C004 se
uzavírá jako confirmed/low pod stejným ID, protože
jeho chybné kroky nejsou publikovanou opravou odstraněny.
Jde o potvrzení pracovníka; nezávislé přijetí kořenem
se netvrdí. Původní F008 je rozšířeno o opakování
téhož podporového problému v úvodu124, bez nového ID.
Žádný nový matematický běh, enumerace ani restart.

## Definice a nezbytná podpora

Pišme I(f)=E f(Y), R(t)=ρ(t)=y(t)/x(t).
Pro y≪x a nezáporné f lze přímo sečíst

    E[R(X)f(X)]=Σ_(x(t)>0)x(t)R(t)f(t)
               =Σ_t y(t)f(t)=I(f).

U reálné f platí tentýž vztah, pokud E|f(Y)|<∞;
kladnou a zápornou část lze sečíst odděleně.
Na x>0 je R konečné, na společných nulových bodech
je jeho volba bez vlivu. Při x>0,y=0 je R=0.

Úvodní tvrzení124 „for any function f“ odkazuje
na121 a samo y≪x nepřidává. Opakuje proto F008:
x=(1,0),y=(1/2,1/2),f≡1 dává I(f)=1, ale
E[R(X)f(X)]=1/2. Je to tentýž přesný problém ztráty
cílové hmoty mimo podporu zdroje; přibývá jen přesná
lokace p25/file45, nikoli nový nález. E002, které
mění pozdější mez chyby, tento úvod neopravuje.

Pro obě konečné výběrové meze však vztah
n=c⁴2^D s konečným kladným n a0<c<∞ již vyžaduje
D<∞. D je opravená součtová divergence D219, takže
D<∞ automaticky zajišťuje y≪x. Nezávislé X_i
mají zákon x, jak zadání výslovně stanoví.
Pro netriviální horní mez předpokládáme
||f||²=E f(Y)²<∞; pak E|f(Y)|≤||f|| a všechny
potřebné střední hodnoty existují. Pokud je norma
nekonečná, horní mez je pouze triviální, kde je
I(f) vůbec definováno; nevyhodnocujeme∞−∞.

n je kladné celé. Rovnost n=c⁴2^D určuje c pro
dané n,D, nebo omezuje přípustné volby c. Nejde
o předpis používat neceločíselný počet vzorků.
Při D=∞ žádný takový konečný experiment neexistuje.

## E002 opravuje očekávanou chybu, nikoli bodovou

Původní zadání má |I(f)−I_n(f)|≤pravá strana.
Oficiální oprava z15.7.2025 mění levou stranu na

    E|I_n(f)−I(f)|.

Byla zobrazena v původním all4b,file3 a porovnána
s TeX265–268 a oběma textovými vrstvami4B.
Toto známé E002 není naše nová chyba. Následující
důkaz ověřuje právě opravenou nerovnost.

Zaveďme m=c²2^D>0, A={t:R(t)>m},
Δ=Pr(Y∈A), g(t)=f(t)[R(t)≤m].
Pak 0≤Δ≤1 a g(Y)=f(Y) mimo událost pravděpodobnosti
Δ; mohou se shodovat i uvnitř A, například při f=0.
Tištěné „except with probability Δ“ tedy znamená
uvedenou výjimečnou množinu, ne nutně přesný zákon
nerovnosti g(Y)≠f(Y).

## Přesný Cauchy–Schwarzův krok

Pro čtvercově integrovatelné U,V je
E(U−sV)²≥0 pro každé reálné s. Pokud EV²>0,
dosadíme s=E(UV)/EV² a dostaneme
|EUV|²≤EU²EV². Při EV²=0 je V=0 skoro jistě
a nerovnost přímá. Součin je integrabilní například
z2|UV|≤U²+V². Tento argument pokrývá i spočetné
zákony; konečné sumy nejsou skrytým omezením.

Potřebný odkaz1.2.3–30 je přesně Cauchy–Schwarzova
nerovnost. Přečtené převzetí v
workstreams/vol1/notes/quality-recovery-section-1.2.3-2026-11-06.md
rozlišuje původní Binetovu formu, komplexní zápis
a integrální rozšíření. Zde je úplný potřebný
reálný pravděpodobnostní argument uveden přímo;
další části oné úlohy se tím neuzavírají.

Použitím na |f(Y)| a1_A dostáváme

    E_Y(|f|1_A)≤||f||√Δ.

## Horní mez: každý ze tří členů zvlášť

Nejprve platí bodová trojúhelníková nerovnost

    |I(f)−I_n(f)|≤|I(f)−I(g)|
                    +|I(g)−I_n(g)|+|I_n(g)−I_n(f)|.

První člen je deterministický a nejvýše
|E_Y(f1_A)|≤E_Y(|f|1_A)≤||f||√Δ.

Pro poslední člen použijeme trojúhelník ve
vzorkovém součtu a potom očekávání:

    E|I_n(f)−I_n(g)|
      ≤(1/n)Σ_i E[R(X_i)|f(X_i)|1_A(X_i)]
      =E_Y(|f|1_A)≤||f||√Δ.

Tady je očekávání zásadní; bodová mez pro
jednotlivý vzorek není tvrzena.

Pro prostřední člen je E[R(X)g(X)]=I(g).
Oříznutí zajišťuje konečný druhý moment a

    Var(R(X)g(X))
      ≤E[R(X)²g(X)²]
      ≤m E[R(X)f(X)²]
      =m||f||².

Druhá nerovnost platí bodově: na R≤m máme R²≤mR
a mimo tuto množinu je g=0. Nezávislost vzorků
ruší každou kovarianci, proto

    E[(I_n(g)−I(g))²]=Var I_n(g)
                      =Var(R(X)g(X))/n
                      ≤m||f||²/n=||f||²/c².

Cauchy–Schwarz s druhou proměnnou1 pak dává
E|I_n(g)−I(g)|≤||f||/c. Sečtením tří
očekávaných členů dostaneme přesně opravené

    E|I_n(f)−I(f)|≤||f||(1/c+2√Δ).

Konstanta2 pochází z obou oddělených ořezávacích
chyb. Tento důkaz dokonce platí pro každé c>0;
zadání využívá větev c>1.

## C004: přesné rozpory, které E002 neodstranilo

Staré výsledky a celý check_information_asymptotics.py
byly přečteny, nikoli spuštěny. Jejich přesní svědci
splňují i opravené zadání:

1. Zvolme x=(15/16,1/16), y=(1/2,1/2),
   f=(0,−1), n=4. Pak 2^D=8/√15,
   c⁴=√15/2>1 a m²=32/√15. Jelikož3<√15<4,
   máme2<m<4, zatímco R=(8/15,8). Tedy g=0.
   Na vzorku samých nul, který má pravděpodobnost
   (15/16)^4>0, je I_n(f)=0, I(f)=−1/2.
   První tištěná rovnost tvrdí1/2=−1/2.
   Ani implicitní očekávání ji neopraví: očekávání
   tištěné pravé strany je I(f)+E I_n(f)=−1,
   zatímco levá absolutní chyba je nezáporná.
   Chybí trojúhelníková nerovnost i absolutní hodnoty
   vnějších členů, nezávisle na známém E002.

2. Zvolme x=y=(1/2,1/2), f=(0,1), n=2.
   D=0, c=2^(1/4)>1, m=√2>R=1, takže g=f.
   I_n(g)=J/2, J~Bin(2,1/2), I(g)=1/2.
   Jeho čtvercová chyba je0 nebo1/4, zatímco
   Var I_n(g)=1/8. Tištěná bodová rovnost
   se rozptylem je tedy nepravdivá; správně
   je před čtvercem očekávání.

3. Pro bodový odhad posledního ořezávacího členu
   lze v prvním svědkovi vzít f=(0,1).
   Stále g=0, Δ=1/2 a ||f||√Δ=1/2.
   Vzorek samých jedniček má pravděpodobnost
   (1/16)^4>0 a dává |I_n(f)−I_n(g)|=8.
   Správná mez platí po očekávání, jak výše.

Všechny zákony mají shodnou kladnou podporu, D je
konečné, norma je konečná a n celé. Chyby tedy
nejsou následkem F008 nebo nedefinovaných mezí.
Původní PDF i PS mají všechny uvedené kroky;
šest vrstev errat a tři TeX zdroje opravují jen
zadání E002, žádný z těchto kroků odpovědi.
C004 je proto lokálně confirmed/low. Hlavní
opravená horní i dolní mez zůstávají platné.
ID se nemění a E002 se nepřeklasifikuje na nález.

## Dolní větev: každá událost a každý odhad

Nyní0<c<1, f≡1 a0<a<1. Tentýž m>0 splňuje
n/m=c². Z E R(X)=1 a Markovovy nerovnosti plyne

    Pr(R(X)>m)≤1/m.

Přísná událost >m je obsažena v ≥m; žádný
rovnostní případ na prahu se neztratí.
Dále přesnou změnou míry

    E[R(X)1_(R(X)≤m)]=Pr(R(Y)≤m)=1−Δ.

Pokud I_n(1)≥a a současně žádné R(X_i)>m,
pak celý součet je roven oříznutému součtu.
Máme tedy inkluzi do sjednocení těchto dvou
událostí a potom

    Pr(I_n(1)≥a)
      ≤Pr(max_i R(X_i)>m)
        +Pr(Σ_i R(X_i)1_(R(X_i)≤m)≥na)
      ≤Σ_i Pr(R(X_i)>m)
        +E[Σ_i R(X_i)1_(R(X_i)≤m)]/(na)
      ≤n/m+(1−Δ)/a
       =c²+(1−Δ)/a.

Všechny oříznuté proměnné jsou nezáporné a
integrabilní, a práh na je kladný. Tento
důkaz dolní větve používá jen sjednocení,
linearitu a Markova; nezávislost je potřeba
pro rozptyl v horní větvi, nikoli zde.
I(1)=1 přesně z normalizace cílového zákona.

## Kraje, interpretace a výpočetní rozsah

Δ=0 nebo1 nevyžaduje jiné dělení; všechny
předchozí kroky zůstávají platné. Pokud ||f||=0,
pak f=0 Y-skoro jistě a Rf=0 X-skoro jistě;
odhad i střed jsou0. Na bodech s y=0 se
použije R=0, nikoli neurčitý součin.
n=1 je zahrnuto. c=1 není ani jedna přísná
větev zadání, ale obecný důkaz obou mezí
stále funguje, jsou-li parametry přípustné.
Při D=0 je y=x a n=c⁴≥1 nutí c≥1;
dolní větev zde nemá přípustný kladný počet vzorků.

„Relatively accurate“ je kvantifikováno normou
||f||, nikoli podílem chyby a |I(f)|. Ten by
například při I(f)=0 nebyl definován. Podobně
dolní pravá strana může být≥1 a pak je mez
triviální; text neposkytuje další univerzální
odstup chyby od0. Přesné dvě nerovnosti jsou
platné v celém výše vymezeném oboru.

Výpočet I_n má invariant S_j=Σ_(i≤j)R(X_i)f(X_i).
Každý z n kroků přidá jeden konečný člen, po n
krocích vrátí S_n/n. Po zajištění generátoru
a hodnot x,y,f používá O(n) aritmetických operací
a O(1) pomocných akumulátorů; cena získávání
vzorků nebo hustot ani bitová složitost se netvrdí.

## Primární zdroj a úplné uzavření

Autorský arXiv:1511.01437v3 byl stažen a zobrazen
v přesném potřebném rozsahu: p1 podpora, p3
Theorem1.1, p21–první část22 celý jeho důkaz.
Autorův důkaz má trojúhelníkovou nerovnost
i očekávání na všech potřebných místech.
S L=(ln2)D a t=4ln c pro horní větev, respektive
t=−4ln c pro dolní, dostaneme přesně knižní
parametry; ve druhé větvi δ=1−a.
Další věty, obrázky a aplikace článku se zde
neuzavírají. Vydavatelská Crossref metadata
potvrzují AAP28(2),2018,1099–1135,
DOI10.1214/17-AAP1326. Žádná bibliografická výjimka.

Starých2650 horních konfigurací a60 dolních
nastavení (každé se3prahy) zůstává uloženo.
Dalších1665 nastavení bylo už tehdy označeno
boundary_or_not_applicable a nepočítá se za
úspěšné testy. Nic z toho se neopakovalo.

Celá124 je checked po E002, potvrzení C004
a přesném rozšíření F008. File410 je reviewed
s dřívější jedinou historickou výjimkou123;
file45 zůstává partial pro125–128.

