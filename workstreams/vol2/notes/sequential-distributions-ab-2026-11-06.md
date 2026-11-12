# Souvislá revize §3.4.1 A–B a základních transformací

6. listopadu 2026. Znovu přečteny původní strany 119–122, 138–139,
584–586; zde je uzavřena jen část A–B a úlohy 1–9, 13–15. Normální
rozdělení od C, úlohy 10–12 a další obsah společných stran navazují.
Sken je první dotisk 1997, pořadí souboru = tištěná strana + 12.
Nejde o nový výpočet starých enumerací ani o potvrzení posledního dotisku.

**C0052 zůstává potvrzený, střední závažnosti.** Nová matematická chyba
v tomto bloku nepřibyla. X0115 zaznamenává revizi, X0116 již zveřejněné
opravy. Nedoložené historické tvrzení na 119 zůstává faktickou mezerou.

## Model a konečné rovnoměrné rozdělení

Strana 119 výslovně předpokládá pokaždé nové nezávislé rovnoměrné reálné U.
To je matematický model transformací, nikoli důkaz nezávislosti skutečného
pseudonáhodného generátoru. Konečnou mřížku kniha odděluje na 120.
Exponenciální čekání v úvodním příkladu čteme v obvyklém modelu homogenního
Poissonova procesu; samotná neurčitá nezávislost událostí by nestačila.
Afinní obraz a+(b−a)U dává rovnoměrný interval a řeší úlohu 1.

Pro J rovnoměrné na {0,…,m−1}, U=J/m, platí

`Pr(floor(kU)=r) = (ceil(m(r+1)/k)−ceil(mr/k))/m`.

Počet celých bodů v polouzavřeném intervalu dává přesnou formuli i její
chybu menší než 1/m; relativní chyba je menší než k/m. U MIX je m=b⁵,
K se vejde do slova a po LDA U, MUL K je horní slovo floor(kJ/m),
dolní slovo kJ mod m. INCA 1 posune výstup do 1,…,k. Matematická
formule není omezena na k≤m, hardware ovšem musí K reprezentovat.
Varování o nízkých bitech odpovídá např. paritě LCG se sudým modulem.
Nečiníme z něj univerzální tvrzení o periodě pro každého společného dělitele.
Porovnání rychlosti dělení/násobení je dobový kontext, nikoli současný benchmark.

Pro zbytky pišme m=qk+s, 0≤s<k. Zbytek r má q+1 reprezentantů, když
r<s, jinak q. Odmítnutí J≥qk dává rovnoměrné zbytky, pokud q≥1.
Právě rovnost v podmínce odmítnutí je známá oprava z 20. srpna 2001.
Neopravuje samostatný příklad C0052. S h=ceil(k/2) totiž

`Pr(J mod k < k/2) = (qh+min(s,h))/m`.

Pro m=3k a sudé k vyjde 1/2. Pro m=256,k=86 je hodnota 129/256.
Při k/m→1/3 a m→∞ je limita 1/2, nikoli 2/3. Tištěný odhad 2/3
odpovídá k přibližně 2m/3; přesně např. m=12,k=8. Původní strana 584
a všechny čtyři vrstvy errat včetně aktuálního TeXu byly znovu prohlédnuty.
Příslušná oprava nenalezena; prvenství a poslední fyzický dotisk neověřeny.

## Nestejné pravděpodobnosti a aliasy

Intervaly kumulativních vah mají délky p_j a rozdělují [0,1), včetně
nulových vah. Srovnávací strom má očekávanou cenu Σp_j d_j. Odkaz na
§2.3.4.5 odpovídá teorii vážené délky cest; obsah 399–404 svazku 1 byl
orientačně porovnán v OCR. Pro pevné pořadí intervalů jde o uspořádaný
strom; obecný Huffmanův strom nelze bez dalšího vydávat za optimální
strom pro pevné pořadí. Kniha zde takový konkrétní algoritmus netvrdí.
Přeskupení alternativ před konstrukcí jejich intervalů je možné.

Součet dvou nezávislých kostek dává trojúhelníkový vektor četností z 36
uspořádaných dvojic. Pro ideální U jsou K=floor(kU) a V=frac(kU)
nezávislé: Pr(K=i,V<v)=v/k. Pro obecnou konečnou mřížku toto přesně
neplatí; kniha již konečnou přesnost oddělila. Nulové váhy umožňují
doplnit počet alternativ na mocninu dvou.

Invariant konstrukce v odpovědi 7: zbývá n nezáporných vah q_i se
součtem n/k. Pro n>1 zvolíme různé indexy minima a maxima, takže
q_min≤1/k≤q_max. Nastavíme P_i=kq_min, alias na maximum a od donorovy
váhy odečteme 1/k−q_min. Zbývající váhy zůstanou nezáporné a jejich
součet je (n−1)/k. Poslední sloupec má P=1 a nepoužitý alias.
Doslovný poslední krok s jediným zbylým párem znovu vloží stejnou váhu;
výstup už je nastaven a iterace končí, takže tím nevzniká chybný výsledek.
Váhy pouze klesají; původní váha menší než 1/k se tedy nemůže stát donorem.

Tabulka na 121 má

`9P = (0,0,4,8,9,7,9,9,9,7,7,8,4,0,0,0)`

a aliasy `(5,9,7,4,*,6,*,*,*,8,4,7,10,6,7,8)`. Hmotnost výsledku 7
je `(5/9+1+1/9+1)/16=1/6`; všechny ostatní výsledky souhlasí s kostkami
v přijaté přesné kontrole. Úloha 8 jen nahrazuje podmínku V<P_i
podmínkou U<(i+P_i)/k v příslušném sloupci.

Známé minimum→maximum z 4. října 1999 opravuje směr optimalizace ΣP_i.
Greedy konstrukce se optimum pouze snaží zvětšit, netvrdí jeho dosažení.
NP-těžkost přesného maxima lze odvodit přímo z 3-partition: pro 3m čísel
a_i v (B/4,B/2), Σa_i=mB, vezmeme k=4m barev. V jednotkách sloupce
má m velkých barev váhu 2, ostatní váhu 1−a_i/B. Celková hmotnost je 4m.
Platí ΣP_i≤Σmin(1,w_i)=3m. Rovnosti lze dosáhnout právě tehdy, když
se deficity a_i/B přiřadí po celých malých sloupcích velkým donorům
s kapacitou 1. Každý donor musí dostat přesně tři položky o součtu B.
To je původní 3-partition. Nejde o tvrzení, že celý aliasový sampling
je NP-těžký; týká se jen této optimalizační varianty.

Primární dlouhá verze Matias–Vitter–Ni je nyní dostupná; předchozí neúspěch
stažení zůstává v historickém metadatovém souboru. Její věta 8 uvádí
očekávanou konstantní dobu aktualizace i generování a lineární prostor.
Četli jsme abstrakt, úvod, model a konstrukční nástin k větě 8, nikoli
celý důkaz článku. RAM model zahrnuje konstantní aritmetiku omezené
přesnosti, celočíselný binární logaritmus a náhodná celá čísla. Dvouúrovňová
redukce používá malé předpočítané tabulky a odmítání. Bibliografie [19]
potvrzuje krátkou verzi SODA 1993, 361–370. To ověřuje citované tvrzení
v jeho modelu, ne nezávisle všechny detaily externího algoritmu.
Zdroj: https://theory.stanford.edu/~matias/papers/MVN03.dynamic_rv_gen.pdf

## Inverze, maxima, minima a směsi

Pro spojitou přísně rostoucí F a 0<U<1 je
Pr(F⁻¹(U)≤x)=Pr(U≤F(x))=F(x). Krajní U=0 je nulová událost ideálního
modelu; konečný algoritmus musí krajní hodnotu zpracovat výslovně.
Pro nezávislé veličiny mají maximum a minimum CDF F₁F₂ a F₁+F₂−F₁F₂.
Identita pro minimum plyne nejbezpečněji z komplementárních událostí
X_i>x a platí i pro atomy. V původním řešení s ≥ je kontext spojitý.
Maximum t uniformních veličin má CDF xᵗ a stejné rozdělení jako U¹ᐟᵗ.

**Vyřešená čtenářská nejasnost, nikoli chyba:** malý náhled 585 jsem
nejprve přečetl jako minimum≤x. Zvětšený výřez původního skenu jasně
ukazuje minimum≥x. Žádný nový kandidát tím nevznikl. Doklad je
`images/vol2-p585-answer4-detail.png`; OCR zde není rozhodující.

Pro F(x)=px+qx²+rx³, nezáporné váhy se součtem 1, první konstrukce
volí počet dalších nezávislých uniformních veličin a jejich maximum.
MacLarenova varianta použije podmíněně přeškálované původní U, které
je uvnitř vybrané větve opět rovnoměrné. Větev s nulovou vahou nemůže
být vybrána, takže nevznikne dělení nulou ani při nulových p,q,r.
Rozšíření na mocninné řady čteme se stejnými nezápornými koeficienty
a součtem 1; není to metoda pro každý polynom se zápornými koeficienty.

Čtvrtkruh z úlohy 6 má přijímací pravděpodobnost π/4 a CDF

`F(x)=(2/π)(arcsin(x)+x sqrt(1−x²)), 0≤x≤1`,

se správným pokračováním 0 a 1. Počet pokusů N má geometrické rozdělení,
E N=4/π a SD N=(4/π)sqrt(1−π/4)=0.58982997… . To nezávisle vysvětluje
známé .587→.590 na 122. Obrázek A4 odpovídá stejnému plošnému modelu;
publikované překreslení z roku 2005 nemění matematiku.
V úloze 9 je f″(x)=(x²−1)f(x), proto na nezáporné polose f konkávní
do 1 a konvexní za 1. Erratum zde jen sjednocuje terminologii.

## Kovariance, škálování a konvoluce

Pro Y=μ+AX s nezávislými standardními normálními X je E Y=μ a
Cov(Y)=AAᵀ. Symetrická pozitivní semidefinitnost C je nutná i postačující:
spektrální odmocnina dává faktor A. Trojúhelníkový faktor existuje také
v singulárním případě. Při nulovém diagonálním pivotu v PSD matici
vynucují hlavní minory 2×2 nulový příslušný řádek a sloupec; při kladném
pivotu je Schurův doplněk PSD. Indukce proto nepředpokládá pozitivní
definitnost. Ortogonální převod na trojúhelníkový faktor zachovává AAᵀ.

Úloha 14 správně rozlišuje c>0, c=0 a c<0. Pro záporné c používá
spojitost F, která je v zadání výslovná; pro atomy by byl třeba levý limit.
Úloha 15 má CDF konvoluci ∫F₁(x−t)dF₂(t). Za výslovného předpokladu
hustot dostáváme ∫f₁(x−t)f₂(t)dt; Tonelli zaručí normalizaci a nezápornost.
Nejsou potřeba konečné momenty a netvrdí se existence hustot pro každý CDF.

## Přijaté výpočty a errata

Celý `verify_distributions_basic.py`, celý log a jeho výsledky byly
přečteny. Žádný blok se znovu nespouštěl. Přijímáme:

- 20 480 celočíselných modelů a 1 648 640 jednotlivých četností;
- 31 816 racionálních aliasových rozdělení a 567 028 prahových kontrol;
- přesný kostkový vektor, symbolické identity a vysoce přesné momenty;
- 280 přesných Gramových modelů, z toho 228 singulárních, v dimenzích 1–7.

Log zachovává první chybu pomocného kovariančního validátoru, kde celočíselné
dělení přešlo na float. Opravený blok s Fraction skončil úspěšně; prvotní
neúspěch nepočítáme jako úspěšnou kontrolu. Konečné modely podporují
obecné důkazy výše, nenahrazují je.

Čtyři historické/aktuální vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
a `errata/originals/err2.textxt` prohledány podle stran i slov.
Errata byla aktuálně stažena 6. listopadu 2026 a shodují se s archivem.
Příslušné strany `all2-prepre` 7, 8, 32 zobrazeny. X0116 zahrnuje
matematické opravy .587→.590 (122), >→≥ (584), minimum→maximum (585).
Terminologii úloh 3/9 a překreslení A4 nezapočítáváme jako další vady.
Známé úpravy polar algoritmu a dalších částí C patří následujícímu bloku.

## Přesné zbývající meze

119 zůstává partial: matematický úvod je prověřen, ale obecné dobové
tvrzení o nepraktičnosti všech jiných přímých generátorů nemá ověření.
Kniha sama odkazuje na téměř přímou Wallaceovu metodu v úloze 31;
vrátit se při jejím souvislém přezkoumání. Jde o faktickou mezeru,
nikoli automatickou bibliografickou výjimku. Globální prioritu neurčitých
atribucí von Neumann/Marsaglia/Ahrens/Dieter jsme nezjišťovali.

120–121 a 585 jsou v daném stránkovém rozsahu matematicky probrány.
122, 138–139 a 586 obsahují navazující neprobranou látku a zůstávají partial.
584 má sice nyní dokončeny odpovědi 3.4.1-1 až 3, ale nadále obsahuje
otevřený C0244 v odpovědi 3.3.4-30. Celý §3.4.1 proto nyní nelze
označit za bezvýhradně uzavřený podle staršího souhrnu.

Bibliografické výjimky: celé původní Walkerovy články 1974/1977,
úplný algoritmický důkaz Matias–Vitter–Ni a priorita MacLarenovy varianty
nebyly znovu prověřeny. Dostupný primární článek potvrzuje uvedená
metadata krátké verze a explicitní výrok s modelem. Tyto výjimky nejsou
důkazem nepravdivosti uvedených atribucí ani novými nálezy.
