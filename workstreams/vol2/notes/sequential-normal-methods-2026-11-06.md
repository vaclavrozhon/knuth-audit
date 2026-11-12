# Souvislá revize §3.4.1 C: normální generátory

6. listopadu 2026. Původní strany 122–132, 139–140 a 586–588 byly
znovu zobrazeny. Revidujeme matematiku P/M/F/R, Levův doplněk a úlohy
10–12, 20–21 v níže uvedeném rozsahu. Wallaceova metoda a její empirická
hodnocení na 132 patří k úloze 31; začátek D pokračuje dalším blokem.
Sken je třetí vydání, první dotisk 1997, file page = printed page + 12.

C0054 a C0055 zůstávají potvrzeny, ale jejich dopad je užší než starší
priorita v UI: **C0054 medium**, **C0055 low**. První neovlivňuje
praktickou volbu parametru algoritmu R, druhý mění jen odhad spotřeby U.
Nový **C0246 je candidate, low**: nejasný popisek obrázku 13.
X0117 zaznamenává revizi, X0118 známé matematické opravy.

## Polární metoda P a odmítání

Hustota standardní normály má integrál 1 (Gaussův integrál), lichý první
moment 0 a druhý moment 1 integrací per partes. Pro bod rovnoměrný
v jednotkovém disku jsou S=V₁²+V₂² a úhel nezávislé, S je uniformní.
R=√(−2 ln S) má hustotu r exp(−r²/2), úhel hustotu 1/(2π).
Kartézský Jacobián proto dává součin dvou normálních hustot, včetně
nezávislosti výstupů. Obě záměny integrálů na 123 odpovídají tomuto výpočtu.

U ideálního reálného vstupu nastává S=0 s pravděpodobností 0. Na konečné
mřížce ale U₁=U₂=1/2 může nastat, takže původní P4 narazí na log(0)
a dělení nulou. Známé erratum z 7. února 2000 v této větvi vrací dvě nuly.
To je definice konečného algoritmu; nečiní z diskrétního vstupu přesnou
spojitou normálu. Geometrické momenty počtu pokusů už prověřil blok A/B:
průměr 4/π≈1.27, SD≈.590, nikoli .587. Tato oprava zůstává v X0116.

Obecné odmítání při f≤cg má společnou hmotnost přijetí a X∈B rovnou
(1/c)∫_B f. Přijetí má pravděpodobnost 1/c, takže podmíněná hustota je f
a počet pokusů průměr c. Poměr 0/0 na nulové hmotnosti g lze dodefinovat.
Obnovovací rovnice na 125 je stejný důkaz. Dolní/horní levné meze mohou
rozhodnout přijetí/odmítnutí před přesným výpočtem podílu.

## Směs M a úloha 10

Pro polonormální hustotu f(x)=√(2/π)exp(−x²/2), h=1/5 a s_j=(j−1)/5
mají obdélníky hmotnost p_j=h f(s_j+h), klíny
p_(j+15)=F(s_j+h)−F(s_j)−p_j, j=1,…,15. Ocas je 1−F(3), pomocná
barva 32 má nulovou hmotnost. Součet je 1 a všechny skutečné složky
jsou nezáporné. Obrázek zobrazuje p_j f_j, nikoli normalizované f_j.
Překreslení obrázku 9 z roku 2000 bylo porovnáno s původní sazbou.
Součet obdélníků .91830983477… vysvětluje 92 %; ocas .00269979606…
odpovídá přibližně jednomu výstupu z 370.

Po uspořádání dvou uniformních veličin je jejich hustota konstantní 2
v trojúhelníku 0≤U≤V≤1. V algoritmu L má přijímaný svislý řez délku
f(s+hU)/b. Po substituci x=s+hU je tedy marginální hustota úměrná f.
Podmínka V≤a/b je bezpečná dolní mez, horní mez nepřekročí 1.
Nulové krajní úseky a rovnosti mají ve spojitém modelu nulovou míru.
Samotná existence hustoty s uvedenou obálkou vynucuje h,b>0.

Na intervalech do 1 je klínová hustota konkávní; tečna v pravém konci
je horní obálka a rovnoběžka přes levý konec spodní. Za 1 je hustota
konvexní; horní obálkou je sečna a spodní rovnoběžná tečna. Přísná
konvexita a věta o střední hodnotě dávají právě jedno místo tečny
uvnitř příslušného intervalu. Úprava „the root“→„satisfies“ z roku 2024
nevynucuje volit jiný kořen mimo tento interval.

Přímé zjednodušení dává

`f_j(X)/b_j = E_j [exp((s_(j−14)²−X²)/2)−1]`, j=16,…,30,

s E_(i+15)=25/i pro i≤5 a 1/(exp((2i−1)/50)−1) pro i≥6.
Index s_(j−14) je pravý konec klínu. M4–M6 proto přesně realizují L.
Po odmítnutí zůstáváme ve stejném klínu; návrat k výběru nové složky
by nesprávně změnil směšovací váhy, ale kniha jej nedělá.

Aliasové sloupce z odpovědi 7 zde čteme s barvami 1,…,32 a konečným
přejmenováním 32 na 0. Všechny donory jsou obdélníky 1,…,15.
Pro donor k je Z_j=1/[5(1−P_j)] a Y_j=k/5−Z_j, což převádí zbylé
uniformní f∈[P_j,1) na [(k−1)/5,k/5). Vlastní obdélník používá
Q_j=1/(5P_j). P₀=0 zajišťuje, že se nepoužije neexistující S₀/Q₀.
P₉=1 zajišťuje, že Y₉/Z₉ nejsou potřeba; formální dělení nulou pro
nepoužitý sloupec se neprovádí. Známé pomlčky v tabulce to vyjasňují.
M1 oddělí znaménkový bit, M2 index a podmíněně rovnoměrný zbytek.
M9 tak připojí nezávislé znaménko. Obrázek 12 má správné cíle všech větví.

Celý `verify_normal_methods.py` i log byly přečteny. Jeho 226 čísel
porovnáváme s tabulkou 128 a odpovědí 10 na 586. Známé opravy Y₄,Y₅,Z₄,Z₅
z roku 2000 souhlasí, stejně jako pomocné p_j,a_j,b_j a kořeny tečen.
Intervaly používají 90 desetinných míst, přesný racionální zbytek Taylorovy
integrace a 230 kroků půlení monotónní funkce. Každý krok aliasové
konstrukce má intervalově oddělené pořadí a donor; součet hmotností všech
hotových větví je kontrolován samostatně. Pouhá středová aproximace
nerozhoduje nerozlišené pořadí. Tabulka výslovně upozorňuje na zaokrouhlení;
není určena k přesnému generování doslovným použitím několika vytištěných cifer.

Úloha 11: návrhová hustota e^(9/2)x exp(−x²/2), x≥3, má integrál 1.
Inverze dává X=√(9−2 ln V); přijetí 3/X vrací normální ocas.
Odmítání .08622910387… je přibližně jedna dvanáctina. U konečného
programu je nutné vynechat V=0; spojitý důkaz je skoro jistý.

## Liché/sudé délky F a Brentův odhad

Pro V₀=h∈[0,1] je Pr(K>k)=hᵏ/k!: k nových bodů pod h musí mít jediné
pořadí z k!. Rozdíl dvou sousedních ocasů a součet přes lichá K dává
Pr(K liché)=exp(−h), zatímco E K=exp(h). Tím je doložen obecný algoritmus
pro hustotu úměrnou exp(−h(x)), nejen normální zvláštní případ.

Polonormální kvantily a_j splňují S(a_j)=2⁻ʲ. Volba j první nulou
nezávislých bitů má pravděpodobnost 2⁻ʲ a zbývající bity dávají podmíněně
nezávislý návrh v [a_(j−1),a_j). V konečné verzi je pravděpodobnost
j=t+1 rovna 2⁻ᵗ, zbytek bitů prázdný a výstup v absolutní hodnotě a_t.
Přibližná přesnost je v algoritmu výslovná; nejde o přesnou spojitou normálu.

Pro Millsův integrál M(x)=∫₀∞ exp(−xt−t²/2)dt platí M′(x)<0 pro x≥0.
Položíme-li y²=a_(j−1)²+2 ln 2, pak S(y)<S(a_(j−1))/2, tedy y>a_j.
Proto a_j²−a_(j−1)²<2 ln 2 a 0≤h_j(x)<ln 2<1. Tím je úloha 12
vyřešena obecně; známé obrácení znaménka v nápovědě je nutné.
Tištěný alternativní důkaz integrací per partes na 586 dává totéž.

Původní F4 po sudém K použije podmíněný starý U jako nový návrh.
Podmíněně je U omezen předchozí sestupnou posloupností, a není proto
čerstvě uniformní. Známá oprava z 30. září 2003 před návratem do F3
losuje nový U a zachovává j a znaménko. Tato oprava je algoritmicky
podstatná a v X0118 má vyšší dopad než tabulkové překlepy.

V intervalu j označme A_j průměr exp(−h_j) a B_j průměr exp(h_j).
První návrh spotřebuje jedno U, každý neúspěch další návrh. Obnovovací
rovnice proto dává cenu F rovnou Σ2⁻ʲ(B_j+1)/A_j=2.53946624… .
Brent recykluje poslední vzestup pomocí

`W=(V_K−V_(K−1))/(1−V_(K−1))`.

Podmíněně na historii před posledním losováním je W uniformní a nezávislé
na X i K. Recyklovat lze po odmítnutí i po přijetí, takže asymptotická
spotřeba nových U je C=Σ2⁻ʲB_j/A_j. Počáteční jediný los se amortizuje.

**C0055:** uložený certifikát uzavírá C mezi 1.377460505889 a 1.377460505893.
Tištěné 1.37446 na 130 je tedy nesprávné; správně 1.37746. V 40 intervalech
jsou kvantily určeny dyadickými závorkami a nezávisle ověřenými znaménky
Taylorovy CDF. B_j používá kladné momenty polynomů a zbytek nejvýše 2/31!.
Protože A_j>1/2 a B_j<2, nekonečný ocas C je menší než 4·2⁻⁴⁰.
Alternativní vyčíslení přes erfi se shoduje. Výsledek není simulace.

Znovu přečtena metoda a analýza 704–705 původního článku, obě stránky
také vizuálně. Rovnice (4) opakuje 1.37446, komentář Fortranu na 705
uvádí 1.37746. Celý Fortran ani dobové benchmarky nebyly auditovány.
Knižní odkaz 704–705 pokrývá tuto analýzu, proto jeho konec nepovažujeme
za další bibliografickou chybu, ačkoli článek končí na 706.
Zdroj: https://maths-people.anu.edu.au/brent/pd/rpb023.pdf

## Poměrová metoda R, plochy a C0054

Pro v=xu má změna souřadnic Jacobián u. Oblast u>0,u²≤g(v/u) má nad
intervalem dx plochu g(x)dx/2. Při konečném nenulovém integrálu g tedy
poměr V/U má požadovanou normalizovanou hustotu. Pro g(x)=exp(−x²/2)
je hranice |v|=2u√(−ln u); její maximum √(2/e) je při u=e⁻¹ᐟ².
Obdélník R1 tedy obsahuje celou oblast. Logaritmické nerovnosti v (28)
plynou z exp z≥1+z a pro c>0,u>0 jsou správné, včetně společné tečny u=1/c.
R2 i R3 jsou bezpečné a R4 je přesný rozhodovací test.

Každá oblast plochy B navštívená při pokusu přispívá B/A návštěvami
na jeden výsledek, protože pravděpodobnost přijetí je A/R. To dává všechny
čtyři sloupce tabulky 131 a odpověď 20. Celkem 16 četností a čtyři plochy
souhlasí s uloženými intervaly; E při skutečném parametru bylo navíc
porovnáno nezávislou kvadraturou. Žádné tyto běhy se neopakovaly.

Pro R2 je I=0 při c≤e⁻¹; jinak a=4(1+ln c), b=4c a
I=(8/15)a^(5/2)/b². Horní konec a/b≤1 plyne z ln c≤c−1.
Logaritmická derivace 5/[2(1+ln c)]−2 mění znaménko právě v ln c=1/4.
Jde tedy o skutečné globální maximum, jak žádá úloha 21.
Primitivní funkce na 587–588 byly znovu odvozeny substitucí; faktor a
v první a faktor 2 v obou plochách chybí již podle errata z roku 2005.

**C0054:** po této známé opravě stále zůstává problém obecného E.
Parametr x z odpovědi 21 dává hranici v²=4e^(x−1)u−4xu². Pro x=1
jsou průsečíky s v=√(2/e) rovny r a 1−r, kde
r=(1−√(1−2/e))/2. Oba leží v (0,1). Odmítaná oblast má dvě shodné
části zrcadlené u↔1−u. Opravený tištěný integrál zahrnuje jen první:
.121847890228149… proti skutečným .243695780456298… .
Pro libovolné reálné x lze psát

`E=2∫₀¹ max(0, √(2/e)−√(4e^(x−1)u−4xu²)) du`.

Odmocnina je reálná: e^(x−1)≥x pro x>0 a pro x≤0 je výraz zjevně
nezáporný. Praktické x=−.35 má jen levou oblast, takže jeho .29410,
tabulka 131 a samotný algoritmus R jsou správně. Závažnost proto medium,
nikoli dřívější high.

Vedlejší tvrzení o r(x) má obecný důkaz: při u*=e⁻¹ᐟ² je obálka vždy
alespoň skutečná hranice 2/e a rovnost nastane jen pro x=1/2. Menší
průsečík tedy nepřesáhne u*, kde jej dosahuje. Diskriminant
e^(2x)−2ex má u x=1/2 dvojnásobnou nulu, jeho odmocnina vytváří
závislost na |x−1/2|, a proto je r v maximu nediferencovatelná.
V x=0 je tištěný podíl interpretován spojitým limitem r=1/2.
Naopak **globální optimum skutečné plochy E poblíž −.35 jsme nedokázali**.
Kniha odkazuje na výpočetní experimenty; její tvrzení zůstává oddělenou
numerickou/faktickou mezerou, nikoli důsledkem kontroly jednoho parametru.
Úloha 21 proto přechází na partial: její požadované maximum I a opravený
obecný vzorec E jsou doložené, dodatečný maximální údaj v odpovědi nikoli.

## C0246: popisek obrázku 13

Popisek na 130 přisuzuje normální rozdělení délkám čar s poměrem
souřadnic x. Doslovná eukleidovská délka úsečky uvnitř oblasti je ale

`L(x)=√(1+x²) exp(−x²/4)`.

Platí L(1)=√2 e⁻¹ᐟ⁴>1=L(0), zatímco standardní normální hustota je
v 1 menší než v 0. Ani vodorovná projekce exp(−x²/4) není profil
standardní normály. Správný argument je plocha podle sklonu x,
rovná (1/2)exp(−x²/2)dx, jak správně uvádí hlavní text na 131.

Starší poznámka popisek četla volně ve světle správného textu.
Nyní nejasnost uchováváme výslovně jako **candidate, low**, ne jako
prokázané selhání generátoru. K potvrzení je třeba rozhodnout zamýšlený
význam „lengths“; doslovné čtení je vyvráceno výše. Původní sazba byla
zobrazena, všechny vrstvy errat a aktuální TeX prohledány podle strany,
čísla obrázku a slov. Odpovídající oprava nenalezena. Prvenství neověřeno.

## Levův doplněk a zbývající rozsah

Přečten celý `verify_leva.py`, jeho výsledky/log a hlavní funkce RANDN
a RANDN0 primárního Netlib programu, včetně přesných desetinných konstant.
Testovací tabulka pseudonáhodných vstupů nebyla znovu přehrávána.
Otevřený interval (0,1) v kontraktu programu vylučuje dělení nulovým U.
Zdroj: https://netlib.org/toms/712

Na v≥0 je Q(u,v) přísně rostoucí ve v; dolní mez derivace je .01141638112.
Skutečná hranice u=exp(−t²),v=2t exp(−t²) je pro t∈[0,8] pokryta
296 souvislými intervaly; každý používá průnik přímého dosazení a
Taylorova odhadu. Kontrola souvislosti listů i pravého konce je v kódu.
Zbytek t≥8 je uzavřen jedním obdélníkem. Na celé hranici je r₁<Q<r₂,
takže oba rychlé testy jsou bezpečné. Archiv uchovává souhrn a úspěšný
log, nikoli jednotlivé listy; v tomto průchodu se výpočet nereprodukoval.

Obě oříznuté elipsy mají plochy A₁,A₂ v horní polorovině, pro jejichž
výpočet kód dělí interval podle všech průsečíků s hranami obdélníku.
Očekávaná cena logaritmů je 2(A₂−A₁)/√(π/2)=.01170898922357…,
tedy zveřejněných .012 je správně. Kontrolována primitivní funkce,
intervalové meze a oddělená kvadratura. Uložené konce intervalů byly
rozšířeny směrem ven; souhrnné hodnoty hranice jsou jen desetinné aproximace.

Afinní normální transformace na 132 má správné momenty. Bivariantní
vzorec pro σ₁,σ₂>0 a |ρ|≤1 má kovarianci σ₁σ₂ρ; zahrnuje nezávislý
případ ρ=0 i degenerované krajní ρ=±1. Není potřeba přidávat nález
kvůli obecnému slovu „dependent“ v popisu této rodiny.

Čerstvé rychlé pokusy o AMS Ahrens–Dieter 1973 a ACM 1972 skončily 403,
Stanford Forsythe 1972 timeoutem. Nepokračujeme v dlouhé bibliografické
odbočce. Úplných 47 externě uvedených hodnot, osobní prioritu a rychlostní
srovnání na dobových strojích nevydáváme za nezávisle ověřené. Celé
články Box–Muller, Marsaglia 1961/1964/1976, Kinderman–Monahan 1977,
Ahrens–Dieter 1988 a časopisecké PDF Leva nebyly v tomto bloku přečteny.
Matematika přetištěných algoritmů má výše samostatné důkazy.

Strany 122–129, 131 a 139 lze uzavřít s uvedenými bibliografickými
výjimkami a známými erraty. 130 má C0246; 132 čeká Wallaceovy empirické
výroky, globální optimum E a začátek D. Strana 586 čeká odpověď 16,
587–588 jiné úlohy, 140 jiné úlohy. Tyto společné strany zůstávají partial.
Celá 3.4.1 nadále není bezvýhradně dokončená. Nový matematický výpočet
se v tomto bloku nespustil; žádná zpráva ani emailový návrh nevznikl.
