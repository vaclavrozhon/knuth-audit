# D169–D170 — celé MPR67–68

7. listopadu 2026. Původní zadání p18/file38 a celé odpovědi
p380–381/file400–401 byly přímo zobrazeny. Totéž platí pro
autorův PS p18/file24 a p37/file43. Kontrola všech šesti vrstev
errat a tří TeX zdrojů je uložena v hashovaném manifestu.

Žádný číselný běh. Převzat je přesný obecný přechod od
férových přírůstků k martingalu a od historie bitů k vlastní
historii z D098. Předchozí omezené zastavení D099 zůstává
platné; není použito pro neomezený konečný čas bez důkazu.

## 67: model a rozlišení času

Nezávislé rovnoměrné bity T₀,T₁,… mají T_j=1 pro prohru
a T_j=0 pro výhru. Používáme přesný model z tištěné odpovědi.
Pokud prvních j pokusů prohrálo, j-tá sázka při indexování
od0 má velikost2^j. Po první výhře jsou všechny další
platby i přírůstky0. Počet pokusů znamená skutečný počet
odehraných sázek, ne největší index sázek.

### 67(a): ukončení s pravděpodobností1 a čistý zisk

Nechť K je počet proher před první výhrou. Pak
P(K=k)=2^{−k−1}, k≥0, a pravděpodobnost alespoň r
počátečních proher je2^{−r}. Proto
P(K=∞)=lim_{r→∞}2^{−r}=0.

Na události K=k přijmeme při poslední sázce2^{k+1},
zaplatili jsme1+2+⋯+2^k=2^{k+1}−1. Rozdíl je1.
Konečný čistý zisk je tedy1 skoro jistě a má očekávání1.
Nulový případ nikdy nekončící hry nemusíme vydávat za
konečnou realizaci; libovolné doplnění na této nulové
události pravděpodobnost ani očekávání nezmění.

### 67(b): všechny platby a nekonečný součet

Položme X_j=2^j[T₀=⋯=T_{j−1}=1], včetně X₀=1.
Má hodnotu2^j s pravděpodobností2^{−j}, jinak0,
takže EX_j=1 pro každé j≥0. Celková platba je
X=∑_{j≥0}X_j. Parciální součty jsou nezáporné a rostou,
proto monotónní konvergence dává

    EX=lim_{r→∞}∑_{j=0}^{r−1}EX_j=lim r=∞.

Přitom X=2^{K+1}−1 je konečné skoro jistě. Nekonečná
střední hodnota neznamená kladnou pravděpodobnost
nekonečné jednotlivé platby; ani nevyžaduje nezávislost
různých X_j, která zde neplatí.

### 67(c): správný martingale a chyba jednoho indexu

Označme
Y_j=(−1)^{T_j}2^j T₀⋯T_{j−1}.
Prázdný součin při j=0 je1. Pro historii před j-tou
sázkou je 2^j T₀⋯T_{j−1} známá hodnota. Nový
nezávislý bit má E(−1)^{T_j}=0, a tudíž

    E(Y_j|T₀,…,T_{j−1})=0.

Všechny konečné přírůstky jsou integrabilní, neboť
|Y_j|≤2^j. Zisk po přesně n pokusech je

    Z₀=0,    Z_n=∑_{j=0}^{n−1}Y_j.                    (1)

Pro H_n=(T₀,…,T_{n−1}) platí
E(Z_{n+1}|H_n)=Z_n; Z_n je funkcí H_n.
D098 dovoluje přechod na vlastní historii Z₀,…,Z_n,
takže jde o požadovaný martingale.

Tištěná odpověď má místo (1) součet Y₀+⋯+Y_n.
Tím vypočítává zisk po n+1 pokusech. Přesný svědek
T₀=T₁=1 má pravděpodobnost1/4: po jediném pokusu
je zisk−1, ale tištěné Z₁=−1−2=−3. Dokonce celý
zákon po1pokusu je férové±1, zatímco tištěný
součet pro n=1 má hodnoty1,−3 s vahami3/4,1/4.
To je lokální chyba indexu F165, nikoli nepravdivost
martingalové vlastnosti: posunutá posloupnost je
také martingale. Stačí poslední index součtu n−1.

Pro kontrolu kompatibility s(a) má správné Z_n
hodnotu1 s pravděpodobností1−2^{−n} a hodnotu
1−2^n s pravděpodobností2^{−n}. Proto EZ_n=0
pro každý konečný n, přestože Z_n→1 skoro jistě.
Negativní očekávaná část má velikost1−2^{−n};
nelze bez další podmínky zaměnit limitu a očekávání.
Dřívější věta o omezeném zastavení se tím nevyvrací.

## 68: přesný zastavený náhodný pohyb

Zde indexujeme nové nezávislé férové bity T₁,T₂,… od1
a nezastavené přírůstky ξ_j=(−1)^{T_j}. Položme
S₀=0, S_n=∑_{j=1}^n ξ_j a N=inf{n≥1:S_n=1},
zatím s možností N=∞. První kladný stav je nutně1,
protože každý krok má velikost1.

### 68(a): férovost a zastavení

Událost N≥n závisí jen na prvních n−1 bitech.
Y_n=ξ_n[N≥n] má tedy podmíněnou střední hodnotu0
vzhledem k této historii. Definujme
Z₀=0, Z_n=∑_{j=1}^nY_j=S_min(n,N), s přirozeným
výkladem při N=∞. Máme |Z_n|≤n, integrabilitu
a adaptovanost. D098 dává martingale i vzhledem
k vlastní historii. Po dosažení1 zůstává Z_n=1.
Tvrzení P(Z_N=1)=1 je dokončeno až důkazem
P(N<∞)=1 v následující části; nepředpokládáme
ukončení kruhem při zavádění N.

### 68(b): rozklad cest a každý koeficient

Definujme g(z)=∑_{n≥1}P(N=n)z^n, pro0≤z<1,
přičemž případ N=∞ nepřispívá. Při prvním kroku+1
je délka1. Po prvním−1 musí konečná cesta nejprve
poprvé přejít z−1do0 a pak poprvé z0do1.
Každý z těchto dvou úseků je přeloženou kopií
první průchodové cesty z0do1. Rozklad je jednoznačný.
Součiny pravděpodobností2^{-délka} se násobí;
disjunktní konečné délky dávají konvoluci, bez
předpokladu už dokázaného konečného zastavení.
Proto

    g(z)=z(1+g(z)²)/2.                                 (2)

Větev s g(0)=0 je
g(z)=(1−√(1−z²))/z=z/(1+√(1−z²)).
Druhá algebraická větev má pól v0 a nemůže být
pravděpodobnostní vytvořující funkcí. Hodnotu v0
doplňujeme limitou0.

Konečný první průchod má délku2k+1. Po odebrání
posledního+1 kroku zbude cesta délky2k z0do0,
která nepřekročí0. Všech mostů je binom(2k,k).
Odražením prefixu do prvního+1 kroku se nepřípustné
mosty bijektivně zobrazí na všechny cesty délky2k
z0do−2, jejichž počet je binom(2k,k+1). Inverze
odrazí prefix do prvního−1 kroku; koncový stav−2
zaručuje jeho existenci. Počet přípustných mostů je

    C_k=binom(2k,k)−binom(2k,k+1)
       =binom(2k,k)/(k+1).

Každá úplná cesta má pravděpodobnost2^{−2k−1}.
Proto

    P(N=2k+1)=C_k/2^{2k+1},    P(N=2k)=0.

To je přesný tištěný koeficient s indikátorem parity,
včetně P(N=1)=1/2. Z monotónní konvergence řady
a g(z)→1 pro z↑1 plyne ∑P(N=n)=1. Tím je
P(N<∞)=1 doloženo a dovětek(a) uzavřen.

Při dalším používání nového úseku po prvním
dosažení hladiny se nezávislost budoucích bitů
od minulého konečného úseku dokládá přímo:
pro pevný okamžik a pevnou minulou posloupnost
je budoucí konečný blok nezávislý; sečtení přes
disjunktní možné časy a minulosti dává stejný
součin. Žádná obecná neprokázaná zastavovací
věta se tak pro další rekurence nepotřebuje.

### 68(c): celý ocas a jeho parita

Pro0≤z<1 a konečné N je
∑_{n=0}^N z^n=(1−z^{N+1})/(1−z).
Po očekávání a sečtení nezáporných členů

    ∑_{n≥0}P(N≥n)z^n
      =(1−zg(z))/(1−z)
      =√(1−z²)/(1−z)
      =(1+z)/√(1−z²).                                 (3)

Rozvoj (1−w)^{-1/2}=∑_{k≥0}binom(2k,k)w^k/4^k
plyne z binomické řady (případně z koeficientové
rekurence a₀=1, a_{k+1}/a_k=(2k+1)/(2k+2)).
Dosazení w=z² a násobení1+z tedy dává

    P(N≥n)=binom(2floor(n/2),floor(n/2))/4^floor(n/2).

Jde o stejný koeficient pro n=2k a n=2k+1.
Pro n=0,1 má hodnotu1; pro n=2,3 má hodnotu1/2.
Všechny indexy a mocniny v tištěné části(c) jsou správné.

### 68(d): nekonečná střední hodnota a lokální F164

Označme s=√(1−z²). Přímá derivace g=z/(1+s)
dává g′(z)=1/[s(1+s)], takže g′(z)→∞ pro z↑1.
Nezápornost členů umožňuje
EN=lim_{z↑1}∑ nP(N=n)z^{n−1}=g′(1−)=∞.

Druhá tištěná cesta používá bodovou identitu
N=∑_{n≥1}[N≥n], tedy EN=∑_{n≥1}P(N≥n).
Tento součet diverguje, ale vytištěný ekvivalent
P(N≥n)∼1/√(πn) má chybnou konstantu.

Úplné nezávislé integrální sevření je zapsáno
v notes/F164-gambling-tail-constant.md. Pro
q_k=binom(2k,k)/4^k dokazuje bez Stirlingova
vzorce a bez numeriky

    2/(π(2k+1))≤q_k²≤1/(πk).

Proto √(πk)q_k→1 a pro k=floor(n/2) platí
√(πn)P(N≥n)→√2, nikoli1. Správný ekvivalent je

    P(N≥n)∼√(2/(πn)).

Dolní sevření současně přímo dokazuje divergenci
součtu ocasů (např. seskupením k mezi j² a(j+1)²,
kde každý blok dává kladný příspěvek oddělený od0).
EN=∞ a přesné formule ostatních částí se nemění.

### 68(e): minimum a každá rekurence

Nechť M=−min_{n≥0}Z_n. Protože Z₀=0 a N je konečné
skoro jistě, M je konečné nezáporné celé číslo.
Označme p_m=P(M≤m), jak v odpovědi. Událost znamená,
že pohyb zasáhne1 dříve než−m−1.

Pro m=0 musí první krok být+1, tedy p₀=1/2.
Pro m>0 má první+1 úspěch s vahou1/2.
Po prvním−1 musí nejprve přijít návrat do0 bez
zásahu−m−1 a potom úspěch z0do1 bez téhož zásahu.
Přeložením prvního úseku o1 je jeho pravděpodobnost
p_{m−1}; pravděpodobnost druhého je p_m.
Rozklad konečných cest a nezávislost nových bitů
z(b) dávají

    p_m=(1+p_{m−1}p_m)/2.

Neztrácí se možnost navždy zůstat mezi bariérami:
ze všech vnitřních stavů by nejvýše m+2 kroků+1
zaručilo odchod, s pravděpodobností aspoň2^{−m−2}.
Opakované bloky tedy omezují přežití po r blocích
číslem (1−2^{−m−2})^r→0.

Proto p_m=1/(2−p_{m−1}); jmenovatel je≥1.
Indukce dává p_m=(m+1)/(m+2). Položíme-li p_{−1}=0,
pak pro všechna m≥0

    P(M=m)=p_m−p_{m−1}=1/((m+1)(m+2)).

Součet teleskopuje na1. Dovětek o nekonečné
střední hodnotě je rovněž doložen:

    EM=∑_{m≥1}P(M≥m)
      =∑_{m≥1}(1−p_{m−1})
      =∑_{m≥1}1/(m+1)=∞.

Pro m=0 dává přesná pravděpodobnost1/2 první
výherní krok; nejde o opomenutí výchozího času0.

### 68(f): počty návštěv včetně výchozí návštěvy0

Položme L_m=#{n≥0:Z_n=−m}, m≥0, a
g_m(z)=E z^{L_m}. Po zastavení je stav1, takže
L_m je konečné skoro jistě. Pro L_m=0 používáme
v g_m(0) hodnotu0⁰=1 jako pravděpodobnost nulové
návštěvnosti; je to konstantní člen řady.

Pro m=0 se počítá také počáteční čas0. Při prvním+1
už žádná návštěva0 nepřijde. Při prvním−1 nastane
návrat do0 skoro jistě podle přeloženého výsledku(b),
a od tohoto návratu začíná nová kopie počtu L₀.
První návštěva i v této větvi je čas0 původní hry.
Tedy

    g₀(z)=z(1+g₀(z))/2=z/(2−z).

Pro m>0 má první+1 počet návštěv−m rovný0.
Při prvním−1 rozdělíme cestu na úsek do prvního
návratu0 a zbytek. Po posunutí o1 má první úsek
zákon návštěv−(m−1), tedy g_{m−1}; druhý má
zákon g_m. Na společném konci0 není pro m>0
žádná návštěva−m, takže nic nepočítáme dvakrát.
Ověřená nezávislost nových úseků dává

    g_m(z)=(1+g_{m−1}(z)g_m(z))/2
          =1/(2−g_{m−1}(z)).                          (4)

Pro0≤z≤1 je 0≤g_{m−1}(z)≤1, tedy jmenovatel≥1.
Definujme h_m(z)=2m−(2m−1)z. Potom h₀=z,
h₁=2−z a h_{m+1}=2h_m−h_{m−1}.
Z g₀=h₀/h₁ a (4) indukcí plyne g_m=h_m/h_{m+1},
přesně jak je vytištěno. Pro m≥1 a0≤z≤1 je
h_m≥1, takže se nezavádí žádný pól v oboru PGF.

V bodě1 je h_m(1)=1 a h′_m=1−2m. Proto

    g′_m(1)=h′_m(1)−h′_{m+1}(1)=2.

Derivace PGF s nezápornými koeficienty je očekávaný
počet návštěv (nejprve z<1 a potom monotónní limita);
konečný racionální výraz ukazuje E L_m=2 pro každé m≥0.

Také přesný zákon lze zkontrolovat přímo rozvojem:

    P(L_m=0)=m/(m+1),
    P(L_m=r)=[1/(2(m+1)²)]·[(2m+1)/(2m+2)]^{r−1},
                                                   r≥1.

Pro m=0 jde o geometrické pravděpodobnosti2^{−r}.
Pro m>0 jejich kladný součet je1/(m+1), což souhlasí
s pravděpodobností dosažení−m z(e). Po podmínění
na dosažení má L_m střední hodnotu2(m+1); násobení
pravděpodobností dosažení dává znovu2.
Dovětek „finite mean“ je tedy správný a nevylučuje
nekonečné EN ani EM z předchozích částí.

## Bibliografie: co bylo skutečně posouzeno

[Primární korespondence v překladu Pulskampa](https://www.gtfp.cs.rhul.ac.uk/pulskamp/NBernoulli/correspondence_petersburg_game.pdf),
první strana, uvádí dopis Nicolase Bernoulliho Montmortovi
z9.9.1713 a původní p402. Je zde otázka plateb rostoucích
geometricky s časem prvního úspěchu. Ověřen je tento
text v překladu; celý originální Montmortův svazek
ani všechny historické nároky se tím neuzavírají.

[Daniel Bernoulli, překlad v Econometrica1954](https://theparticle.com/cs/bc/dsci/Bernoulli_1738.pdf),
p23 a p31 (§17), přímo dokládá původní ročníkV,
strany175–192, označení Nicolase jako bratrance,
odkaz na Montmortovu p402 a geometrický platební
příklad s nekonečným očekáváním. Netvrdíme audit
celé Bernoulliho teorie užitku. Původní sazba
ročníku1730/1731 ani kauzální historie pozdějšího
názvu paradoxu nejsou tímto překladem plně prověřeny.

[Univerzitní obsah Fellerova svazku2](https://unina2.on-line.it/sebina/repository/catalogazione/documenti/An%20Introduction%20To%20Probability%20Theory%20And%20Its%20Applications%202.pdf)
potvrzuje druhé vydání1971 a existenci XII.2
„Duality. Types of Random Walks“. Text samotné
sekce nebyl rychle dostupný a přesné matematické
přiřazení citace se bibliograficky vynechává.
Na žádné Fellerově větě výše uvedený důkaz nezávisí.

Výslovné bibliografické/historické výjimky jsou:
Casanovova ztráta v1754 a příslušné místo autobiografie;
originální Montmortova p402 nad rámec překladu;
původní datování Bernoulliho ročníku a vznik pojmenování
paradoxu; obsah Feller XII.2. Žádná z těchto výjimek
nezakrývá matematickou mezeru v67–68.

## Rozsah

Celé67(a–c) a68(a–f), všechny tištěné mezikroky,
koeficienty, parity, limity a oba dovětky o střední
hodnotě jsou assessed; správné matematické výsledky
mají úplný důkaz. F164 opravuje pouze asymptotickou
konstantu68(d), F165 pouze index součtu67(c).
Oba lokální problémy jsou na p380/file400, nikoli
na správném zadání p18 či odpovědi68(f) p381.
File400 je po tomto bloku celý posouzen s explicitní
bibliografií; file38 zůstává partial pro začátek69
a file401 pro další odpovědi. Žádný běh ani restart.

