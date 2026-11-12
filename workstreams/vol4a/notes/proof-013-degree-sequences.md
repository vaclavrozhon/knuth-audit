# Stupňové posloupnosti a Algorithm H: str. 29–31, §7–103 až 107

6. listopadu 2026. Samostatný důkaz, ruční průběhy; žádný program/census.
Sazba file046–048, proof-file544–545. F0 robustní verze algoritmu H
je již v prvním dotisku 4A. U odpovědi 105 aplikovány známé opravy
vynechaného nepotřebného v=c_t a zejména 0≤a_j na 0≥a_j (str. 528).

## Definice a tabulka

Ve grafu na n vrcholech je d_1<n a součet stupňů sudý.
3311 není grafická: oba vrcholy stupně 3 by sousedily s oběma
zbývajícími vrcholy, které pak nemohou mít stupeň 1.
C_j=#{i:d_i≥j} je konjugovaná partition, tedy c_j≥k právě když d_k≥j.
Pro 55544322 dává přímé počítání sloupců 88653.
Po tištěných sedmi hranách 83,82,71,75,64,63,62 jsou zbývající
stupně 43333 a konjugát 5551, jak uvádí str. 30.

## Lemma M a majorizace

Nejprve doložme použitou redukci na jednotkové přesuny.
Máme seřazené x majorizující y se stejným součtem a x≠y.
První odlišná pozice i je přebytek x_i>y_i; vezmi a jako poslední
pozici se stejnou hodnotou x_i a b jako první pozdější deficit x_b<y_b.
Takové b existuje, x_a−x_b≥2, a mezi a a b−1 jsou kumulativní rozdíly
kladné. Sniž x_a o 1 a zvyš x_b o 1. Pořadí zůstane zachováno:
a je konec svého bloku a b začátek svého bloku (jinak by deficit byl dříve).
Nová partition stále majorizuje y a její L1 vzdálenost k y klesne o 2.
Konečným opakováním dostaneme požadovaný rozklad mini-majorizací.

Při jednom přesunu z i do j je d_i≥d_j+2. Existuje soused v vrcholu i,
který není sousedem j a není j: pokud ij je hrana, porovnej
N(i)\{j} a N(j)\{i}; pokud není, porovnej přímo obě sousedství.
Odstraň iv a přidej jv. Nevznikne smyčka ani násobná hrana
a změní se pouze stupně i,j o −1,+1. To dokazuje Lemma M včetně
implicitní podmínky v≠j.

Pro Corollary H porovnej libovolný výběr r=d_n zmenšených položek
x=(d_1,...,d_(n−1)) s výběrem r největších. Pokud menší x_j byla
zmenšena, ale větší x_i ne, přesuň zmenšení z j do i.
V aktuálním zbytku je to přesun jednotky z x_i do x_j−1.
Při x_i>x_j jde o mini-majorizaci, při rovnosti se seřazený multiset
vůbec nemění. Tak se dostaneme ke greedy zbytku; každý jiný zbytek
jej tedy majorizuje. Odstranění n z existujícího grafu dává grafický
zbytek, Lemma M dává grafičnost greedy zbytku a indukce dokazuje H.

## Přesný invariant H1–H4

H1 projde hranice řádkových délek a zapisuje výšky sloupců:
pokud d_j≥k>d_(j+1), musí c_k=j. Tím sestaví právě konjugát.
Je-li d_1=0, všechny stupně jsou nulové. H2 nastaví n=c_1,
tedy odstraní koncové nulové řádky. Při d_1≥n>0 je graf nemožný,
protože žádný soused nemůže mít zbývající stupeň nula.

V H3 je j zbývající počet míst posledního řádku n; t je délka
právě zpracovávaného nejvyššího bloku, i jeho první ještě přípustný
řádek a r jeho původní poslední řádek.
C_j←C_j−1 v H4 odstraní pravý krajní prázdný slot posledního řádku.
M=C_t je potom poslední přípustný řádek aktuálního nejvyššího bloku:
je menší než n, i když původně d_n=t, protože odstranění řádku n
v tomto případě právě snížilo c_t. Nevznikne tedy smyčka.
D_m←D_m−1 a C_t←m−1 odeberou bottommost slot tohoto bloku;
seřazenost ostatních prázdných řádků se zachová.
Každý cílový řádek se použije nejvýše jednou: po vyčerpání bloku
m=i přejde i na původní r+1, tedy za všechny už použité řádky,
i když se jejich snížené délky právě rovnají délce dalšího bloku.
J původně nejvýše n−1 zaručí dostatek různých cílových řádků.
Po j=0 je celý řádek n odstraněn a c je opět konjugát zbývající
seřazené partition; stale hodnota d_n už leží mimo aktivní prefix.
To přesně realizuje greedy krok z Corollary H.

Každý H4 vytvoří jednu hranu. H1 stojí O(n+d_1), další režie O(e);
u úspěšné realizace bez izolací je n≤2e a d_1≤2e, tedy čas O(e).
Při započtení čtení všech vstupních vrcholů je přirozená mez O(n+e).
Není třeba prohledávat množinu grafů.

## Úlohy 103–104: oba úplné ruční průběhy

První průběh vytváří hrany po dávkách podle posledního vrcholu:
8:{3,2}; 7:{1,5}; 6:{4,3,2}; 5:{1,4,3}; 4:{2,1};
3:{2,1}; 2:{1}.
To dává přesně všech 15 hran a obě symetrické pozice v tištěné tabulce.

Druhý průběh pro 866444444:
9:{1,3,2,8}; 8:{1,3,2}; 7:{1,6,5,4}; 6:{1,3,2};
5:{1,4,3}; 4:{2,1}; 3:{2,1}; 2:{1}.
Zbývající partition jsou postupně
75544443, 6444444, 544333, 43333, 3322, 222, 11, prázdná.
Těchto 22 hran přesně souhlasí s oběma konci každého záznamu odpovědi.

V druhém průběhu začíná i=1,t=8,r=1; po hraně 9–1 přejde
i=2,t=6,r=3 a vytvoří 9–3,9–2; potom i=4,t=4,r=8 a 9–8.
Význam i,r je tak ověřen konkrétně i obecným invariantem výše.

## Úloha 105: lineární test, včetně postačitelnosti

Označ s=max{k:d_k≥k}. Pro k≤s je
Σ_(j≤k)c_j=k²+Σ_(j>k)min(k,d_j).
Proto tištěná podmínka je právě Erdős–Gallai
Σ_(j≤k)d_j≤f(k)=k(k−1)+Σ_(j>k)min(k,d_j).
Je nutná: levá strana počítá nejvýše k(k−1) vnitřních incidencí
a od vnějšího vrcholu j nejvýše min(k,d_j) hran.
Pro k≥s platí f(k+1)−f(k)=2k−d_(k+1)≥d_(k+1);
další podmínky tedy automaticky vyplývají z té pro s.

Doplňujeme podrobný kontrolní argument postačitelnosti z odpovědi.
Nechť a_k=Σ_(j≤k)(d_j−c_j)+k a vznikne po greedy kroku první
porušení a_k>0, k≤s. Velká písmena D,C,A,N,S označují stav před krokem.
Greedy krok odstraní řádek N délky r a sníží p řádků délky >t,
potom q dolních řádků délky t, kde r=p+q, q≥1, p<r≤t a t≥S.
Označ u=C_t. Nerovnost t≥S plyne takto: kdyby t<S, vybráno by
bylo alespoň S řádků délky ≥S, ale r=D_N≤t, spor.
Před tímto krokem H2 již zaručil D_1<N.

Minimalita k dává 1≤a_k≤d_k−c_k+1, takže c_k≤d_k a k≤d_k.
Pokud D_k>t, je k≤p a A_k=a_k: ve všech prvních k řádcích
i sloupcích klesl právě jeden slot. Pokud D_k<t, pak k<t a
A_k=a_k+r−min(k,r)≥a_k. Zbývá D_k=t.

Jestliže t>S, pak u≤S. Pro k<j≤u máme
d_j≥t−1≥d_k−1≥c_k−1≥c_j−1, tedy a_u≥a_k.
Protože r≤u≤S<t, rozdíly prefixových součtů řádků a sloupců
se v u vyruší a A_u=a_u>0. Zbývá t=S.

Jestliže k<t, konjugace dává t≤c_k≤d_k≤t, tedy c_k=d_k=t.
Případ r=t by dal c_k=N−1=t, a tedy N=t+1, ale pak byly zmenšeny
všechny zbývající řádky a d_k=t není možné.
Pro r<t musí u=t: kdyby u>t, i řádek t+1 by po zmenšení měl délku
alespoň t−1≥k, což odporuje c_k=t. Potom
A_(t−1)=a_(t−1)−1≥a_k−1≥0 a A_t=A_(t−1)+1>0.
Opět dostáváme porušení už před krokem.

Zbývá k=t=S. Platí t=s≤c_t≤d_t≤D_t=t, a proto
a_t=a_(t−1)+1=1 a a_(t−1)=0.
Pro p≤j<t−1 z rovnosti a_(j+1)=0 dostáváme
a_j=c_(j+1)−t−1≥q−1≥0, ale minimalita porušení dává a_j≤0.
Zde je nutná známá oprava znaménka v prvním dotisku.
Tedy zpětnou indukcí a_j=0, q=1; když p=t−1, plyne q=1
rovnou z p+q=r≤t. Pro p<t−1 také c_r=t+1=N−1,
takže N=t+2. Při p=t−1 dává totéž c_t=N−q−1=t.
Proto D_j=t+1 pro j≤p (horní mez D_j<N), D_j=t pro p<j≤t+1,
a D_N=p+1. Součet D je 2p+t(t+1)+1, lichý.
Tato jediná výjimka je tedy vyloučena předpokladem sudého součtu.

Každé porušení po kroku H se tak přenese před něj. Pokud by H nakonec
selhal pro d_1≥n>0, už a_1=d_1−n+1>0. Zpětným přenosem by
porušení existovalo na vstupu. Splnění podmínek a parity proto zaručuje
úspěch H a grafičnost. To uzavírá i použití testu v textu na str. 31.

Po rychlém odmítnutí d_1≥n lze konjugát sestavit v O(n), potom jedním
průchodem prefixových součtů ověřit všechny k≤s a paritu. Pro nulovou
partition jsou podmínky prázdné. Lineární mez nepočítá generování hran.

## Úlohy 106–107

106: Při d=0 dostáváme n izolací, při d=1 matching; pro n≥d+2
nejde o souvislý graf. Ostatní malá přípustná n dávají K1 nebo K2.
Pro d≥2 před vytvořením prvních n−1 hran má algoritmus jedinou
rostoucí stromovou komponentu a zbytek jsou dosud nedotčené izolace.
Nedotčené vrcholy mají zbytkový stupeň d a tvoří prefix; dotčené
nevyřízené vrcholy stromu mají menší stupeň a tvoří následující blok.
V H2 tedy bere poslední dotčený vrchol a přednostně připojuje izolace,
které mají největší zbývající stupeň. Dokud nějaké izolace zbývají,
strom má nevyřízený list, protože jeho aktuální stupeň 1 je menší než d.
Komponenta se tedy nemůže uzavřít dřív, než zahrne všechny vrcholy.
Prvních n−1 hran právě postupně připojí všechny izolace a tvoří strom.
To dokazuje i silnější větu z tištěné odpovědi.

107: Komplementující permutace φ mění stupeň d na n−1−d.
Po seřazení tedy d_j+d_(n+1−j)=n−1.
Podle již dokázané úlohy 78 má φ cykly délky 4r a nejvýše jeden
fixní bod. φ² dává v každém takovém cyklu dvě sudé orbity, na nichž
je stupeň konstantní. Každá hodnota stupně má tedy sudou násobnost,
kromě možné centrální hodnoty (n−1)/2. V horní polovině seznamu
jsou proto d_1=d_2,d_3=d_4,...; dolní polovina plyne komplementací.
To je přesně opravený vzorec d_j=d_(j−(−1)^j), 1≤j≤n/2,
z errata 9. 1. 2019. Původní párování přes celý lichý seznam se nepřebírá.

Dodatečná konverzní klasifikace Clapham–Kleitman v závorce je externí
vstup; její článek a algoritmus zde nejsou ověřeny. Stejně jsou explicitně
přeskočeny historické odkazy Havel a Erdős–Gallai; matematické argumenty
této poznámky jsou samostatné a na ověření atribuce nezávislé.

Další: §7–108 až 111 a sítě od druhé části str. 31. Odpověď 528 byla
přečtena celá, ale argumenty 108–111 budou doplněny v dalším bloku.
