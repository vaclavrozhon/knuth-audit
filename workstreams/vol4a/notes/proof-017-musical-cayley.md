# Hudební graf a Cayleyovy grafy, §7–133 až 136

6. listopadu 2026. Původní file061–062, detail proof-musical.png,
odpovědi proof-file548.png. Bez programu, simulace či opakování censů.

## 133: konkrétní struktura a všechny základní parametry

V diagramu jsou po obvodu dvojice (C,a),(G,e),(D,b),(A,f♯),(E,c♯),
(B,g♯),(F♯=G♭,d♯=e♭),(D♭,b♭),(A♭,f),(E♭,c),(B♭,g),(F,d).
Každá dvojice má vnitřní hranu a dvě sousední dvojice jsou úplně
propojené; jiná hrana není. Tím je celý diagram popsán jako K₂ strong C₁₂.
Piš dvojici P_i={x_i,y_i}, i modulo12.

(a,b,l) Vrcholů je24, stupeň1+2+2=5, hran24·5/2=60.
(c) P_i a libovolný bod P_(i+1) tvoří trojúhelník, tedy girth3.
(d) Vzdálenost různých dvojic je jejich vzdálenost v C₁₂; uvnitř je1.
Maximum je6 (též přímý důsledek uzavřené metriky silného součinu).
(e) Nezávislá množina bere nejvýše jeden bod z dvojice a nesmí brát
sousední dvojice; α≤6 a výběr x₀,x₂,...,x₁₀ rovnost realizuje.
(f,h) Dvě sousední dvojice jsou K₄, tři různé dvojice kliku netvoří.
ω=4; parita indexu a rozlišení x/y dávají čtyřbarvení, tedy χ=4.
(g) Pět hranových barev je nutných stupněm5. Svislé hrany x_i y_i
obarvi5; stejné vrstvy mezi P_i,P_(i+1) barvou1 pro sudé i a2 pro liché;
zkřížené hrany mezi těmito dvojicemi obdobně3 a4. U každého vrcholu
jsou všechna čísla1,…,5 právě jednou, takže χ′=5.
(i) Součinový popis je výše; (j) minimum cover má24−α=18;
(k) dvanáct hran x_i y_i je perfect matching a více než12 není možné.

(m) Explicitní K₅ minor: čtyři singletony P₀∪P₁ tvoří K₄;
pátou větev tvoří souvislé sjednocení P₂∪…∪P₁₁.
Každý z prvních čtyř bodů se této větve dotýká přes P₂ nebo P₁₁.
Graf je proto neplanární. Tvrzení o minimálně12 kříženích je externí
výsledek Chimaniho výpočtu, zde nereprodukovaný; známý přídavek F0.
(n) Po smazání nejvýše3 vrcholů zmizí nejvýše jedna celá dvojice.
Zbývající neprázdné dvojice tvoří cyklus nebo cestu s úplnými spoji,
tedy graf zůstane souvislý. Smazání dvou nesousedních celých dvojic
jej rozdělí: vertex connectivity je přesně4.
(o) Ano v knižní konvenci dvou opačných oblouků na hranu.
(p) Strom není, obsahuje trojúhelník.
(q) Hamiltonovský cyklus je x₀,x₁,…,x₁₁,y₁₁,y₁₀,…,y₀,x₀.
Historický význam hudebních modulací a stránka73 Wilson–Watkins
nebyly samostatně ověřeny; nejde o vstup do grafových argumentů.

## 134: všechny automorfismy

Dva vrcholy v téže P_i mají stejné uzavřené sousedství,
P_(i−1)∪P_i∪P_(i+1). Žádné dvě různé dvojice toto sousedství nemají.
Každý automorfismus tudíž permutuje právě těchto dvanáct invariantních
dvouprvkových tříd a indukuje automorfismus jejich cyklu C₁₂.
Ten má12 otočení a2 orientace. V každé dvojici lze nezávisle zaměnit
x/y. Počet je proto24·2¹²=98304, ekvivalentně24·2¹¹·2 z odpovědi.
Argument dokazuje nejen existenci těchto symetrií, ale také úplnost.

## 135: spektrum, všechny vzorce a přesná hodnota

Uplatněny obě známé opravy23.5.2011: ω=exp(2πi/12) a mocnina2m
v TD^(2m)T⁻¹. S původním ω=exp(2πi/6) by Fourierova matice nebyla
invertibilní; jde o již zveřejněnou opravu, ne nález.

Při součinovém pořadí je A=J₂⊗(I+Q+Q⁻¹)−I₂₄.
Fourierovy vektory S_ij=ω^(ij) diagonalizují Q, vlastní čísla jsou
ω^j (případně jejich inverze podle řádkové konvence, součet stejný).
H₂ diagonalizuje J₂ na2,0. Proto T=H₂⊗S dává dvanáct čísel
λ_j=1+4cos(jπ/6), j=0,…,11, a dalších dvanáct čísel−1.
Všechny jsou nenulové, A je invertibilní.

Pro cesty délky2m k vrcholu ve stejném nebo opačném listu dvojice k:
W_(±,k)=(Σ_j λ_j^(2m) exp(−2πijk/12))/24 ± [k=0]/2.
Toto plyne přímo z T⁻¹=(H₂/2)⊗(conj(S)/12), nikoli z numerické simulace.
Označ X=(13+4√3)^m, Y=(13−4√3)^m, Z=9^m, R=25^m.
Pro k=0,…,6 dává Fourierův součet tyto čitatele dělené24:

| k | čitatel pro vrchol velkého písmena |
|---|---|
|0 (C)|R+2X+2Y+3Z+16|
|1 (G)|R+√3(X−Y)−1|
|2 (D)|R+X+Y−3|
|3 (A)|R−3Z+2|
|4 (E)|R−X−Y+1|
|5 (B)|R−√3(X−Y)−1|
|6 (F♯)|R−2X−2Y+3Z|

Pro opačný list k=0 se odečte1; jinde oba listy souhlasí.
Symetrie k↔12−k dává zbytek. To ověřuje všechny vytištěné vzorce.

Přesná čísla při m=6 lze spočítat krátkou celočíselnou rekurzí.
U_m=X+Y a V_m=√3(X−Y) mají společnou rekurzi t_m=26t_(m−1)−121t_(m−2),
protože oba základy mají součet26 a součin121.
Hodnoty U₀,…,U₆ jsou2,26,434,8138,159074,3151226,62683922;
V₀,…,V₆ jsou0,24,624,13320,270816,5429496,108398160.
Dosazení R=244140625,3Z=1594323 dává přesně
15462617,14689116,12784356,10106096,7560696,5655936,5015296.
Pravděpodobnost návratu je15462617/5¹²≈6.33%.

Nejpravděpodobnější je návrat po každém kladném sudém počtu kroků:
(A^(2m))_uv je skalární součin řádků A^m pro u,v.
Všechny mají díky vertex-transitivity stejnou normu.
Cauchy–Schwarz proto dává nejvýše diagonálu. Rovnost pro různé řádky
by vyžadovala jejich shodu (součty obou jsou5^m a normy stejné),
což invertibilita A^m vylučuje. Maximum je tedy jednoznačné.
Dominantní vlastní číslo je5 a další největší absolutní je1+2√3;
jeho čtverec/25=(13+4√3)/25<0.8. Proto všechny pravděpodobnosti
jsou1/24+O(0.8^m), jak je uvedeno.

## 136: Petersen není Cayleyův graf

Standardní Sylowova/Cauchyho věta je zde explicitní algebraický vstup:
grupa řádu10 má normální cyklickou podgrupu řádu5 a involuci.
Konjugace na této podgrupě je identita nebo inverze; grupa je C₁₀
nebo D₅. Rekonstrukce obecných grupových vět není součástí úlohy.

Generátory obyčejného kubického Cayleyova grafu tvoří tříprvkovou
inverzně uzavřenou množinu S bez jednotky. Musí generovat celou grupu:
jinak by komponenta měla1,2 nebo5 bodů; kubický jednoduchý graf
takové velikosti neexistuje (pro5 z parity součtu stupňů).
V C₁₀ musí S={5,a,−a}; pro liché a vznikne po přeznačení
deseticyklus s protilehlými tětivami, pro sudé a pětiboký hranol.
Hodnoty a=0,5 jsou vyloučené jednoduchostí, ostatní jsou tím pokryty.

V D₅ buď S obsahuje jednu reflexi a pár inverzních rotací, což dává
dva pěticykly spojené matchingem, nebo tři reflexe.
Automorfismy D₅ působí afinně na jejich pěti indexech a tranzitivně
na třípodmnožinách (komplement je dvojice). Stačí tedy
S={b,ab,a³b}, a⁵=b²=1, bab=a⁻¹.
První dvě reflexe dávají deseticyklus s vrcholy
v_(2j)=a^(−j), v_(2j+1)=a^(−j)b; třetí propojí v_i s v_(i+5).
Obě výsledné třídy mají čtyřcykly: u hranolu mezi dvěma sousedními
paprsky; u druhé třídy0,1,6,5. Petersen má girth5 podle již uzavřeného
proof007, takže do žádné nepatří. Žádné nové hledání grafů není potřeba.
Dodatečné tvrzení o raman generátoru a bibliografie Holton–Sheehan
zůstávají explicitní externí poznámkou bez zdejší rekonstrukce SGB.

Další kurzor: §7–137, file062/p45, odpověď532/file549.
