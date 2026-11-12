# Individuální grafové argumenty: str. 13–16 a úlohy 39–53

6. listopadu 2026. Původní sazba hlavních stran 30–33 a zadání 56 přečtena;
odpovědi 521/file538 a začátek 522/file539. Nový F0001 již evidován,
neopakujeme jeho kontrolu. Žádný matematický program ani census.

## Definice, počty a vzdálenosti

Hrany jsou dvouprvkové množiny: sousednost je symetrická a bez smyček.
Indukovaný podgraf obsahuje přesně všechny hrany s oběma konci ve zvolené
množině; Carrollovy grafy s omezeným slovníkem proto jsou indukované podgrafy.
Kn má binom(n,2) hran, Pn má n−1 a Cn má n pro běžný rozsah; výjimky C1/C2
jsou multigrafy podle již zapracovaného fasciklového errata.
Součet stupňů je 2e, protože každá hrana má dva konce.

Ve Fig. 2 se pro P5,C5,K5,Q3,Petersen ověřují počty (5,5,5,8,10) vrcholů
a (4,5,10,12,15) hran a uvedené stupně přímo z modelů. U Chvátalova obrázku
je vidět 12 vrcholů stupně 4, tedy 24 hran; úplná adjacency certifikace a
girth 4 zde zůstávají partial. Šest alternativních kreseb krychle(16)
nemá dosud individuální mapy isomorfismu; jejich první čtení není takovým důkazem.

Automorfismus definovaný pouze zachováním hran jedním směrem stačí:
permutace indukuje injekci konečné množiny E do sebe, tudíž bijekci.
Pro Q3 obraz000 má 8 možností a jeho tři sousedé mohou být permutováni
6 způsoby. Tím je zbytek určen: vrcholy váhy2 jsou druhé společné sousedy
dvojic sousedů000 a vrchol111 je jediný ve vzdálenosti3. Všech 8·6=48
možností realizují posuny XOR a permutace souřadnic.

Metrické tvrzení na16: v knižním slepení dvou cest zvol nejmenší r s
u_r=v_s. Žádný předchozí u_i neleží na druhé cestě; prefix u_0..u_r a
suffix v_s..v_q tedy vytvoří cestu bez opakování, délky r+q−s≤p+q.
To dokazuje trojúhelníkovou nerovnost, včetně rozšíření na∞. Dostupnost
je reflexivní/symetrická/tranzitivní, takže dává komponenty.

Všechny nové globální vzdálenosti a velikosti SGB komponent na16, včetně
15:1 po známé opravě podmínky a 1198→1186, zůstávají explicitně partial.
U cesty(21) sousední slova mění jedno písmeno; izolovanost celé komponenty
není tím ověřena. Ve stromu(22) je horní cesta6 hran, dolní cesta5 hran,
navíc trees–treed,tweed–tweet,tweet–sweet,sweet–sweat. Všech15 hran mění
jedno písmeno, všech16 vrcholů je různých a graf je strom obsahující tři
terminály. Dává tedy horní mez15; neexistence14hranového řešení je partial.

## Petersenův graf

Označ v běžném obrázku vnější pentagon O_i, vnitřní hvězdu I_i (i mod5):
hrany O_iO_(i+1), O_iI_i, I_iI_(i+2).
Zobrazení O_i↦{2i,2i+1}, I_i↦{2i+2,2i+4} modulo5 převádí sousednost
přesně na disjunktnost dvouprvkových podmnožin pětiprvkové množiny.

Tři navzájem disjunktní dvojice neexistují; dvě různé dvojice mají nejvýše
jednoho společného souseda. Proto nejsou trojúhelníky ani 4-cykly.
Vnější pentagon dokládá girth 5.

Každá čtyřprvková rodina navzájem se protínajících dvojic musí být hvězda
všech dvojic obsahujících pevný symbol. Jinak z {a,b},{a,c} vznikne
{b,c} a rodina již nemůže mít čtvrtou dvojici. Je tedy právě pět maximálních
nezávislých čtveřic. Automorfismus je permutuje a každý vrchol je určen
dvěma z těchto hvězd, do nichž patří. Aut se tak vkládá do S5.
Všech 120 permutací pěti symbolů zachovává disjunktnost, tudíž |Aut|=120.

Hamiltonovská kružnice by použila sudý počet paprsků O_iI_i, tedy2 nebo4.
Při2 by jejich indexy musely sousedit jak na vnějším pentagonu (rozdíl±1),
tak na vnitřní hvězdě (±2), nemožné. Při4 lze vynechaný paprsek dát do0.
Vnější vybrané úseky pak musí být O1–O0–O4 a O2–O3, vnitřní I2–I0–I3
a I1–I4. Spolu se čtyřmi paprsky vzniknou dvě 5-kružnice, nikoli jedna.
Graf je tedy nehamiltonovský. Je také nerovinný: při girth5 by Eulerovo
f=15−10+2=7 vyžadovalo 2e≥5f, tedy30≥35. Tvrzení „nejmenší kubický graf
s oběma vlastnostmi“ zůstává partial, protože zde nebyla klasifikována
všechna uspořádání na8 vrcholech.

## Úlohy 39–45

39: G\e má stejné V, tedy je spanning; indukovaný podgraf na celém V by
musel mít celé E. Při předpokládaném e∈E proto induced není.

40(a): libovolná podmnožina E dává jediný spanning podgraf, počet2^e.
40(b): libovolná podmnožina V dává jediný induced podgraf, počet2^n.
Počítají se grafy s danými vrcholy, ne třídy isomorfismu.

41(a): n(n−1)/2=n−1 dává n1 nebo2, oba fungují; P0 je podle odpovědi
nedefinován. 41(b): pro n≥3 rovnost stupňů n−1=2 vynutí n3; odpověď
navíc používá prázdný C0=K0. C1/C2 jako multigrafy odpovídající Kn nedají.

42: součet stupňů13·5=65 je lichý, takže takový graf neexistuje.

43: první kresba má vnější9-cyklus 0..8 (0 nahoře, dále po směru hodin)
a střed9. Navíc hrany09,39,69,15,27,48. Vnější pentagon Petersenova modelu
může být (0,1,2,3,9), jeho protilehlé vnitřní vrcholy jsou (8,5,7,4,6);
vnitřní hrany přesně skáčou o2. Tím je první isomorfismus doložen.
Další dvě mapy i rozdílnost čtvrté kresby jsou dosud partial, nikoli
uzavřeny pouhým převzetím odpovědi. Historická oprava girth4→3 ve F0
je již ve4A zapracována.

44: obrázek ukazuje osm dihedrálních symetrií; úplný argument vylučující
další automorfismy Chvátalova grafu nebyl zde uzavřen.

45: řádky mapy(17) střídavě používají palety {0,2} a {1,3}, v řádku
barvy střídáme. Všechny hrany kresby vedou mezi sousedy téhož řádku nebo
do sousedního řádku, proto to je4-barvení. Pět sousedů NV tvoří cyklus
CA–OR–ID–UT–AZ–CA, takže vyžaduje tři barvy a NV čtvrtou.
Počet značek je49. Faktická správnost všech geografických hran a tvrzení
o nulové automorfní symetrii mapy zůstávají partial.

## Úlohy 46–53

46(a): maximální jednoduchý rovinný graf je souvislý (jinak lze spojit
komponenty) a nemá artikulaci: dvě po sobě jdoucí hrany u–v,u–w vedoucí
po odstranění u do různých komponent lze bez křížení doplnit hranou vw.
Stěny tak mají hranice tvořené jednoduchými cykly. Ve stěně s≥4 vrcholy
vezmi čtyři po sobě jdoucí a,b,c,d. Obě diagonály ac a bd nemohou být již
nakreslené v komplementárním disku, protože jejich konce se střídají;
alespoň jedna chybí a jde ji přidat uvnitř stěny. Spor s maximalitou.
Každá stěna je tedy trojúhelník. Použitý topologický vstup je běžná
separační vlastnost jednoduché uzavřené křivky.

46(b): vytištěný kontrakční krok je F0001. Správný samostatný důkaz:
n−e+f=2 a3f=2e dávají e=3n−6. Eulerův vztah zde plyne odstraněním hran
mimo pevný spanning tree: každá taková ne-mostová hrana slije dvě stěny,
tedy současně sníží e,f o1; strom má e=n−1,f=1. Pro obecný jednoduchý
rovinný graf n≥3 lze doplnit hrany do maximality, takže e≤3n−6.
Tím je také doložena nerovinnost K5.

47: při hypotetickém rovinném K3,3 jsou všechny stěny délky≥4, takže
2e≥4f. Euler pak dává e≤2n−4=8, zatímco K3,3 má9 hran. Závěr správný;
důkaz nepoužívá chybnou kontrakci46.

48: dvě cesty z kořene ke koncům hrany se stejnou paritou délek by spolu
s hranou daly lichý uzavřený sled. Z nejkratšího takového sledu odstraníme
opakované vrcholy: alespoň jedna ze dvou částí je lichá, dokud nevznikne
lichá kružnice. Při jejím zákazu proto d(w,u),d(w,v) mají opačné parity.
Knižní barvení nové komponenty tedy vždy dává vrcholu v barvu d(w,v) mod2,
bez ohledu na pořadí návštěv. Všechny hrany mají opačně barevné konce.

49: neprázdný kubický jednoduchý graf má sudý počet vrcholů a každou
komponentu alespoň4. Do6 tedy zbývají řády4 a6. Při4 je jenK4.
Komplement grafu řádu6 je2-regulární, tedy C6 nebo dvě C3; původní grafy
jsou trojboký hranol a K3,3. To jsou přesně tři třídy v odpovědi; známé
doplnění názvu hranolu2015 není vlastní nález.

50: při r neprázdných komponentách je počet3-barvení dělitelný3^r,
proto24 vynutí souvislost. Bipartice má velikosti m,n>0. Úplný K_m,n má
3(2^m+2^n−2) barvení (jedna strana jednobarevná, dvojí započtení6);
odstraněním hran počet neklesá. Z ≤24 plyne {m,n}={1,1},{1,2},{1,3},{2,2}.
První dva případy mají6/12 barvení. K1,3 má24; pro2+2 je P4 s24 nebo
C4 s18. Právě K1,3 aP4 tedy vyhovují.

51: incidence sítě je bipartitní a4-cyklus by znamenal dvě přímky se dvěma
společnými body. Jedna třída dává les hvězd; dvě dávají subdivizi K_n,n′,
tedy girth8 pro n,n′≥2, jinak∞. Při≥3 třídách vyber dvě přímky protínající
se v p a třetí z další třídy, která p neobsahuje. Tři různé průsečíky
dají6-cyklus. Tím jsou všechny případy uzavřeny v běžném nedegenerovaném rozsahu.

52: na nejkratší kružnici délky g vyber vrcholy s kruhovou vzdáleností
floor(g/2). Kratší cesta v celém grafu by spolu s kratším kruhovým obloukem
obsahovala kružnici délky<g. Jejich vzdálenost je tedy floor(g/2) a průměr
alespoň tato hodnota. Případ g=∞ je správně vyňat.

53: zařazení happy/world do SGB komponent zůstává partial. Bibliografie
původu grafů, mapy a historických tvrzení se rychle neověřovala.

Doplnění X0053 po obnově: P0131 má úplný důkaz minimální velikosti
v proof-021 s explicitním Kuratowského vstupem, bez klasifikačního censu.
P0132/P0148 mají v proof-022 přesnou horní mez osmi automorfismů;
rohy se invariantně rozliší počtem čtyřcyklů a určují zbytek zobrazení.
Girth již pokrývá P0495. Starší partial u těchto přesných částí je tím
nahrazeno. Šest kreseb krychle P0127 a tři zbývající obrázky P0147
zůstávají samostatnými otevřenými povinnostmi.

X0054: P0127 uzavřena šesti jednotlivými izomorfismy, P0504 doplňuje
rovinné realizace. Proof-023 obsahuje také úplnou mapu všech matematických
tvrzení p14/file31 na konkrétní argumenty, včetně relevantních odpovědí.
Pouze tato stránka nově má review_depth=argument; historická bibliografie
i reading metadata zachovány. Okolní stránky/prefix se nepovyšují.
Dále P0147, tři zbývající grafy úlohy 43; první P0146 se neopakuje.

X0055: P0147 nyní celý v proof-024. Druhý/třetí diagram mají explicitní
Petersenovy mapy; čtvrtý má trojúhelník, Hamiltonův cyklus a rovinné
vložení přes lokální rozšíření vrcholu Q3. Nejen neizomorfnost, ale
všechny matematické dodatky odpovědi 43 jsou pokryty. Žádný census.
Další konkrétní algoritmický dluh P0246, stop-podmínka board pro p<0;
starší neuzavřené datové/censové/research položky tím nejsou přeskočeny
bez záznamu a zůstávají ve svých partial stavech.
