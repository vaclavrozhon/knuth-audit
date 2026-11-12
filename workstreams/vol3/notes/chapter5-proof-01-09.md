# Důkladná kontrola: úvod kapitoly 5 a úlohy 1–9

Rozsah: matematické/algoritmické výroky na s. 1–6, §5-1 až9,
odpovědi 584–586. Záznamy jednotlivých tvrzení jsou v proof-audit.json.
Jde o nové doplnění důkazů, nikoli opakovaný numerický běh. Sazba
už byla přečtena; podezřelé místo a programy byly prohlédnuty v
images/intro-file-596.png a 597.png. Errata úvodu se přebírají z
sources/opening-errata-review.json. Nově vznikl pouze C0016.

## Tvrzení hlavního textu

- S. 2, seskupování shod: jestliže i<j<k a v_i=v_k ve vzestupné
  posloupnosti, v_i≤v_j≤v_k, tedy v_j=v_i. Každá hodnota tvoří interval.
- S. 2, shody mezi soubory: u k vzestupných seznamů porovnáme aktuální
  klíče; menší klíče postupně přeskočíme až na maximum aktuálních klíčů.
  Žádný přeskočený záznam již nemůže odpovídat neprošlému záznamu ze
  seznamu s větším klíčem. Při shodě zpracujeme celé skupiny shodných
  klíčů. Ukazatele se pouze zvětšují. Výrok znamená nalezení shodných
  záznamů/skupin, ne slib konstantní paměti pro kartézský výstup duplikátů.
- S. 2–3, technika kompilátoru: třídění podle (identifikátor, priorita)
  seskupí výskyty a umístí definice před užití. Připojená informace se
  pak vrátí na původní místa tříděním podle unikátního původního indexu.
  To dokazuje popsaný princip; historická implementace LARC a konkrétní
  přečíslování na polskou notaci nejsou tímto tvrzením nezávisle ověřeny.
- S. 4, trichotomie/transitivita: a<a je vyloučeno trichotomií a pro
  různé a,b je právě jeden směr; s transitivitou jde o ostré totální
  uspořádání. Konečný neprázdný soubor má minimum: postupně ponechávej
  menší z dosavadního kandidáta a dalšího prvku. Po odstranění minima
  opakuj, což induktivně dává seřazení. Relace ≤ má odpovídající
  neostré vlastnosti včetně antisymetrie.
- S. 4, stabilita: lexikografické klíče (K_j,j) jsou navzájem různé
  a totálně uspořádané. Jejich vzestupné pořadí splňuje (1) i (2)
  a každé stabilní pořadí musí být právě tímto pořadím. Tím se přebírá
  již uzavřený argument z opening-first-pass, bez nového výpočtu.
- S. 4, přímé/nepřímé pořadí: bijekce p určuje buď permutaci fyzických
  záznamů, nebo čtení R_(p(1)),…,R_(p(N)) přes tabulku. Satelit se musí
  přesouvat se svým záznamem; hodnoty klíčů se tím nemění.
- S. 4, sentinely: rozšíření klíče o značku −1/0/+1 a běžným klíčům
  značka0 realizuje dvě skutečně krajní hodnoty. Rovnost původních
  klíčů se zvolenou číselnou konstantou tak lze odstranit přidaným
  testem/značkou. Samotná rovnost se sentinelovou konstantou bez úprav
  není tvrzena jako přípustná.
- S. 5, Θ(N log N) porovnání: pro N různých klíčů má binární rozhodovací
  strom alespoň N! listů. Kraftova nerovnost a konvexita dávají průměrnou
  hloubku při rovnoměrných permutacích alespoň log₂(N!). Integrální
  odhad součtu log j dává log(N!)=N log N−O(N). Merge sort dosahuje
  nejvýše N ceil(log₂ N) porovnání a O(N log N) přesunů. Výrok o zhruba
  log N průchodech odpovídá tomuto algoritmu, není tvrzením o každé
  implementaci. Pro model T(N)=cN log N je T(2N)/T(N)=2+2log2/logN.
- S. 5, N(log N)²: N různých klíčů vyžaduje nejméně log₂N bitů pro
  pevně široké kódování. Θ(log N) bitů na jeden úplný přesun/porovnání
  spolu s Θ(N log N) operacemi vysvětluje tuto heuristiku. Kniha ale
  v poznámce nespecifikuje bitový model ani práci s prefixy či odkazy;
  univerzální bitová dolní mez tím dokázána není. Záznam partial,
  nikoli nový potvrzený nález.
- S. 5, průměr O(N) pro známé spojité rozdělení: při dostupném výpočtu
  distribuční funkce F v O(1) převedeme F(X) na rovnoměrné [0,1] a
  rozdělíme do N stejně pravděpodobných košů. Je-li n_i obsazení koše,
  EΣn_i²=N+N(N−1)/N=2N−1. Vkládání do košů a kvadratické třídění
  jednotlivých košů tedy mají očekávaný O(N) čas. Cena výpočtu F nebo
  kvantilů pro libovolné známé spojité rozdělení v textu specifikována
  není; tento předpoklad zůstává explicitní modelovou mezerou partial.

Historické citace, statistika času třídění, slovníkové/terminologické
atribuce a empirické výroky o konkrétním hardwaru se přebírají jako
výslovně přeskočená bibliografie/faktografie, ne jako matematické důkazy.

## Úlohy 1–4

1. Přebrán důkaz pomocí (K_j,j) výše. Alternativní knižní argument:
   první rozdíl p(i)≠q(i) nutí rovnost obou klíčů a stabilita současně
   p(i)<q(i) a q(i)<p(i). Použita známá oprava n→N v odpovědi.
2. Alice po skupinách získá klíče (K,k,j); Chris je získá přímo.
   Bill po prvním stabilním řazení získá (k,j); druhé stabilní řazení
   podle K zachová tento pořádek uvnitř každé skupiny K. Výsledek je
   opět (K,k,j). Bez stability nemusí být výsledky stejné: dvě shodné
   dvojice klíčů mohou měnit pořadí; nestabilní druhý krok u Billa může
   dokonce zvrátit minor keys. Použita známá oprava R_(p(n))→R_(p(1)).
3. Netranzitivita dává tři různé klíče a<b<c<a. Cesty abc,bca,cab
   splňují sousední nerovnosti (1). Do jakékoli cesty x₁<…<x_m vložíme
   v: je-li v<x₁, dopředu; jinak před první x_i s v<x_i, nebo na konec,
   pokud takový není. Předchozí prvek pak je <v z trichotomie.
   Relativní pořadí původního trojcyklu se nemění, takže zůstávají tři
   různé výsledky. Skupiny stejných klíčů zachovají původní vnitřní
   pořadí. (1) je zde řetězec sousedních nerovností, nikoli všechny
   párové nerovnosti, které by bez tranzitivity nevyplývaly.
4. Pro samotnou velikost písmen dává (lowercase(α),α) s malým písmenem
   před velkým požadovaný výsledek: primární klíč řadí slova nezávisle
   na velikosti, sekundární pouze rozliší varianty téhož slova. Všechny
   uvedené příklady této základní varianty souhlasí. Rozšíření o
   interpunkci ale nedává vytištěný výsledek; konkrétní uzavřený
   protipříklad a,A,a- je v notes/V3-C0016-dictionary-punctuation-order.md.

## Úloha 5: celý prefixový kód

ρ(0)=0; pro n=(1α)₂ je ρ(n)=1ρ(|α|)α. Indukce na max(m,n): nula
začíná0, každý kladný kód1. Pro dva kladné vstupy s různými délkami
α rozhodne pořadí prefixově nezávislých kódů délek; menší délka
znamená menší číslo. Při stejné délce jsou prefixy shodné a stejně
dlouhé payloady se porovnají jako binární čísla. Ani v jednom případě
nemůže být různý kód prefixem druhého. Rekurze končí, protože |α|<n.

L(0)=1 a L(n)=1+L(λ(n))+λ(n), λ(n)=floor(lg n). Rozvinutím dostaneme
přesně vytištěný součet iterovaných λ plus lg* n+1, včetně n=0 a1.
Pro celá t≥2 platí λ(t)≤t/2, takže ocas iterací λ má geometricky
omezený součet a počet nenulových iterací je O(λ(n)); tím L(t)=O(log t).
Znovu použitá rekurence pak dává L(n)=floor(lg n)+O(log log n).

Vytištěné hodnoty byly ověřeny symbolicky: ρ1=10, ρ2=1100,
ρ3=1101, ρ4=1110000; 1009=(1111110001)₂, ρ9=11101001,
tedy ρ1009=111101001111110001. Dále ρ16=1⁴0⁸,
ρ65536=1⁵0²⁴ a ρ(2^65536)=1⁶0⁶⁵⁵⁶⁰. Není třeba vytvářet
obrovský vstup ani spouštět test.

## Úlohy 6–8: MIX

Použité sémantické definice: text/vol1.txt, §1.3.1, tištěné125
(radix bytu 64≤b≤100),131–132 (ADD/SUB/MUL/DIV),135 (skoky a posuny).
Zejména ADD s nulovým výsledkem zachová původní znaménko rA; posuny
znaménka obou registrů nemění. To je podstatné pro první program min.

6. Nechť W=b⁵−1 je největší kladné slovo. A=W, B=−1 jsou přípustné,
   ale SUB vytvoří +0 a overflow místo správného kladného rozdílu b⁵.
   Test nuly by chybně hlásil rovnost. CMPA porovnává hodnoty bez
   takového odečítání do omezeného registru, takže doporučená oprava
   je správná. Plošná historická poznámka o všech počítačích se neověřuje.
7. STJ uloží návratovou adresu do instrukce 9H. Na vstupu iterace k=rI1
   jsou všechny vyšší dvojice stejné. LDX/CMPX porovná a_k,b_k;
   první nerovnost proto správně určí lexikografický výsledek. JNE
   nezmění CI a vrátí jej; při rovnosti DEC1 sníží variantu k a J1P
   pokračuje pouze pro k>0. Po n shodách zůstává EQUAL. Užitý datový
   registr je jen rX a index rI1; návratový rJ a pole kódu jsou běžný
   mechanismus MIX subrutiny. Algoritmus skončí nejvýše po n porovnáních.

8a. Označ a=2u+r, b=2v+s, kde u,v jsou podíly zaokrouhlené k nule,
   |r|,|s|≤1 a zbytky mají znaménka vstupů. Prvních deset instrukcí
   právě tyto veličiny vytvoří. T=u−v nemůže přetéct, |T|≤2floor(W/2)≤W.
   Potom R=r−s leží v [−2,2]. SRAX1 z něj udělá rA s nulovou velikostí
   a zachovaným znaménkem. ADD T dá znaménko a−b: pro T≠0 plyne
   shoda znamének z monotonicity celočíselného podílu; pro T=0 ADD
   zachová znaménko R. ENTX1; SLAX5 vytvoří σ=±1 s tímto znaménkem.
   Rovnost a=b nevadí, protože tehdy R=0.

   MUL R a STX vytvoří AB3=σR. Další LDA/ADD/SUB vytvoří
   r+s−σ(r−s), tedy 2s při a≥b nebo 2r při a<b. Po dělení dvěma je
   z=s nebo r. Závěrečné instrukce počítají u+v+z−|u−v|=min(a,b).
   Čtení AB1(1:5) je právě absolutní hodnota T, bez znaménka.

   Veškeré mezivýsledky jsou přípustné pro libovolný radix bytu,
   nikoli jen sudý: první součty zbytků mají velikost≤2; z+u má
   velikost≤floor(W/2)+1; u+v+z má velikost≤W, protože pro z=r
   platí |u|+|r|≤ceil(W/2), |v|≤floor(W/2), analogicky pro z=s.
   Výsledek posledního SUB je platný vstup a nebo b. Násobení ±1·R
   dává velikost≤2. Před každým DIV je horní rA nulové, takže
   overflow z dělení nemůže nastat. Tím je ověřen každý blok kódu
   i všechna rozhraní; jde o důkaz bez emulace.

8b. Po každém dělení dvěma jsou v rI1,rI2 podepsané bity d_a,d_b
   z množiny {−1,0,1}. Tři INC1 vytvoří adresový posun d_a+3d_b.
   Devět položek tabulky je pro posuny −4,…,4 postupně
   C,B,B,A,C,B,A,A,C. Přesně tedy volí A při d_a<d_b, B při d_a>d_b,
   jinak ponechá předchozí vítězné C. Vlastní čtení LDA0,3 opravdu
   dereferencuje vybranou adresu; STA C uchová vítězný původní klíč.
   Invariant po j kolech: C označuje minimum podepsaných j nejnižších
   bitů; nový vyšší odlišný bit převáží všechny nižší, shodný je
   nechává rozhodnout. Když 2^k>10¹⁰>b⁵−1, byly přečteny všechny bity.
   Adresový posun je v [−4,4], všechna dělení mají nulové horní rA,
   proto nepřetečou. Rozvinutých k kopií neobsahuje žádný skok.

## Úloha 9: oba tvary distribuční funkce

Po známé opravě n→N nechť 1≤r≤N a 0≤x≤1. Počet hodnot≤x je
Bin(N,x), takže F_r(x)=Σ_(k=r)^N binom(N,k)x^k(1−x)^(N−k).
Derivace teleskopuje na
F′_r(x)=r binom(N,r)x^(r−1)(1−x)^(N−r); F_r(0)=0.
Integrace dává tištěný beta integrál. Rozvineme-li (1−t)^(N−r)
a integrujeme po členech, koeficient x^(r+j) je
(-1)^j r binom(N,r)binom(N−r,j)/(r+j)
=(-1)^j binom(r+j−1,j)binom(N,r+j), přesně tištěný součet.
Rozsah j je0,…,N−r. Mimo [0,1] se CDF prodlouží hodnotami0 a1;
ostrý/neostrý test má stejnou pravděpodobnost díky spojitosti.

Další systematická úloha: §5-10, s.6 / file17; zbytek odpovědi11
pokračuje na587. Otevřené modelové mezery úvodu na5 jsou vedeny
samostatně, není kvůli nim tvrzena úplná důkazová certifikace celé stránky.
