# Souvislý průchod §1.3.3: permutace

5. listopadu 2026 přímo přečteny všechny původní strany164–185 a
odpovědi522–527. Na527 se uzavírá pouze část§1.3.3; následující
odpovědi§1.4.1 vyžadují samostatné porovnání se zadáním. Originály
179–180 jsou v `parallel/permutation-inplace/images/`, ostatní
v `images/vol1-filePPP-pNNN.png`, s posunem+15.

Přečteny celé přijaté důkazy `permutation-a.md`,
`permutation-a-capacity.md`, `permutation-b.md`, `permutation-inversion.md`,
`parallel/permutation-inplace/NOTES.md`, pravděpodobnostní poznámky
`basic-proofs.md`, `arbitrary-function-expectation.md`, `longest-cycle.md`,
`source-audit.md` a `josephus-uniform-tail.md`, dále
`permutation-remaining-working.md`, `permutation-comparison.md`,
`permutation-block-interchange.md` a `permutation-remaining-sources.md`.
Samostatně přijaty kořenové recenze `dickman-original-root-review.md`
a `mitchell-original-root-review.md`. Uložené souhrny výsledků a přesné
certifikáty porovnány; úspěšné strojové běhy ani kvadratury se neopakovaly.

## Násobení permutací a první úlohy

Kniha používá součin zleva doprava. Základní příklady, disjunktní
rozklad, přiřazování přes dočasnou proměnnou i výměny souhlasí.
Šest sloupců dvouřádkového zápisu dává720 zápisů, takže718 dalších;
rotace dvou netriviálních cyklů dávají12 možností v úloze5.

Algoritmus A značí použité hrany cest přes jednotlivé faktory.
První neoznačený výskyt musí začínat dosud nezpracovanou cestu;
bijektivita zajišťuje návrat právě do START. Kopie prvního jména za
posledním je následník, ne další vstupní hrana. Tím je prokázán
disjunktní rozklad pro neprázdné vstupní cykly a dostatečnou paměť.
Ve strojové podobě jsou tagy znaménka a porovnávání pouze magnitude.
Singletony se z výstupu odstraní; prázdný výstup se zapíše jako().

U B je T obraz pod již přečtenou pravou částí součinu. Při přidání
levého cyklu se přesně cyklicky posunou dosavadní obrazy. Jedna
dočasná nula označuje chybějící obraz, doplněný levou závorkou.
Nově objevené jméno bylo v pravých faktorech pevným bodem. Tento
invariant ospravedlňuje dynamickou tabulku jmen i následný rozklad.
ENT3 musí inicializovat0, nikoli původní1: známá oprava2000.
Tabulka2 souhlasí; její znak) znamená dosud neznámý obraz.

Frekvenční rovnice, včetně počtu úplných průchodů A, dávají

    T_A/u = 112NX+304X−2M−Y+11U+2V−11,
    T_B/u = 4F+16Y+80X+21N−19M+9U−16V.

Vnitřní mezery opravují čas A o−8a−2b, nikoli původní+4a+5b;
to je známé erratum odpovědi6 z roku2005. Pro knižní příklad jsou
časy2161u a983u, F=74. Mez F≤N(Y−2M) a oprava za mezery dokazují,
že B je rychlejší pro každý přípustný vstup s dostatečnou kapacitou;
nejde pouze o závěr z jediného příkladu. Úlohy1–11 jsou správné po
uvedených známých opravách. Levostranná varianta B počítá inverzi,
proto potřebuje obrácené závěrečné cykly.

**C0029 potvrzeno:** dva neprázdné cykly s3t+4 vstupními poli mohou
vytvořit t transpozic a4t výstupních polí. Pro t=320 je vstup964 polí
na61 kartách, výstup1280 slov; oba programy vyhrazují1200 slov.
Obecný počet dokazuje vadu nezávisle na simulátoru. Uložený běh A
doložil přepsání OPEN a skutečné selhání; běh B byl záměrně zastaven
před prvním zápisem mimo pole. Oprava A s2MAXWDS+23 slovy se vejde
do4000 slov. Obdobná jednoduchá oprava B výslovně snižuje vstupní
limit na60 karet. Tato změna není zamlčena. Nová anotace UI jmenuje
oba programy a ukazuje přesné alokace na168 a174.

**C0028 nadále kandidát:** zápis() je na164 definován jako identita,
zatímco vstup A je popsán jako součin cyklů. Přesný špatný běh je
doložen, ale není jednoznačné, zda tento zápis patří do povolené
vstupní gramatiky. Doplněná poznámka2005 o nevalidovaném vstupu
tuto doménovou otázku sama nerozhoduje. Nevydáváme ji za druhou
potvrzenou chybu ani za důvod zopakovat kapacitní experiment.

## Inverze, transpozice, kanonický zápis

I obrací cyklus zápornými odkazy a následně obnovuje kladná znaménka.
J má správný invariant po doplnění známé podmínky2023: záporná větev
platí jen bez již zpracovaného předchůdce. Případ h=w při uzavření
cyklu je pokryt. Obě tabulky3/4, příklady i instrukční překlady souhlasí.
Změna inicializačního registru J z roku2024 není opravou špatné inverze;
obě verze jsou správné a mají stejný čas. Nebarví tedy sama178 červeně.

    T_I/u=14n+C+2,
    T_J/u=13n+4A+2,
    EA=(n+1)H_n−n,
    Var(A)=2n(n+2)−(n+1)H_n−(n+1)^2 H_n^(2).

Protože A≥n a C≤n, I je rychlejší na každém vstupu. Rozptylová
rekurence po poloze nejmenšího prvku dává poslední vzorec přesnými
generujícími funkcemi; odečtení konstanty n rozptyl nemění. Strojové
meze fragmentů jsou rozlišeny od skutečně zakončených programů.

Kanonický rozklad začíná cykly minimy a řadí je sestupně, takže
závorky lze obnovit přesně před minimy zleva. Bijekce dokazuje
statistiku počtu cyklů i Stirlingovy koeficienty. Úlohy15/16 včetně
prázdné permutace a devítičlenné orbity souhlasí.
U obdélníkové transpozice je pro0≤x<mn−1 nové místo mx modulo mn−1,
krajní mn−1 je pevné. Třída gcd(x,N)=d má cykly délky ord_(N/d)(m),
v počtu phi(N/d)/ord. Je odlišeno přesouvání do cíle od čtení jeho
inverzního zdroje. Úloha12 je matematicky dokončená; plné nedostupné
historické články jsou níže přeskočeny.

## Pravděpodobnost, nejdelší cyklus a integrabilita

Počet výskytů m-cyklů mezi všemi permutacemi je n!/m. Volba cyklu
ze všech výskytů má průměr n/H_n; cyklus náhodného prvku má průměr
(n+1)/2. Tyto dva náhodné výběry nejsou zaměněny. Krajní n=1 dává
rovnost a není novou vadou kontextového slova „somewhat“.

Derangementy mají D_n=n!sum_(j=0)^n(−1)^j/j!, po opravě chybějícího
n! je argument nejbližšího celého čísla správný. Polynom pevných
bodů je sum_(r=0)^n(z−1)^r/r!. Počty cyklového typu a jejich
rotovaných zápisů vycházejí dělením n! příslušnými symetriemi.
Poissonovský model s parametry w^m/m má konečnou velikost skoro jistě
a geometrické rozdělení P(N=n)=(1−w)w^n. Normalizace a jednoznačnost
nevyžadují dělení nulovým nekonečným součinem. Inkluze–exkluze i
zobecnění na přesně r vlastností platí včetně prázdných případů;
u úlohy27 je výslovně zahrnuta nula v intervalu.

**C0032 potvrzeno:** pro w=1/2, n≥2 lze typu identity přiřadit2^n n!
a jedinému n-cyklu−2^n n. Pak každý konečný průměr phi_n=0, ale
každá velikost přispívá1/2 ke kladné i záporné části očekávání.
Obě jsou nekonečné, Ephi tedy neexistuje. Samotná absolutní
konvergence řady phi_n nestačí. Stačí E|phi|<∞, případně nezáporná
funkce s rozšířeným očekáváním. Autor mohl existenci zamýšlet
implicitně; předchozí lokální definice knihy takovou univerzální
konvenci nestanoví. Úlohy22(d,e) používají oprávněné nezáporné nebo
integrovatelné případy. Přesná lokace je183 a524, nikoli celý oddíl.

Nejdelší cyklus: monotónní l_n/n a l_n/(n+1) dávají omezený rozdíl
d_n=l_n−lambda·n. Uniformně sečitatelný Eulerův–Maclaurinův zbytek
v geometrickém modelu dává Abelův průměr d_n→lambda/2; podmínka
|d_n−d_(n−1)|=O(1/n) a aproximační argument převádějí průměr na
obyčejnou limitu. Periodické další členy až n^(−3) se shodují
s Gourdonovým dokázaným rozvojem; jejich koeficienty nelze zahodit.
Nejkratší cyklus má doložen vedoucí člen exp(−gamma)ln n, nikoli
převzatý nedokázaný silnější zbytek O(1).

Přijatý intervalový certifikát lambda má poloměr2.07e−73. Rozdíl
proti40místnému číslu v knize je kladný4.2620180529…e−41, takže
číslice i následné plus jsou správně. Důkaz certifikátu nezávisí
na diskutabilním kroku původního Mitchellova numerického odhadu.
Dickmanův výpočet stejné konstanty i převod značení byly již přímo
ověřeny v přijaté recenzi. Časopisecká343 Knuth–Trabb Pardo zůstává
bibliografickou výjimkou; obsahová identita je v primárním reportu.

## Zbývající konstrukce, 28–38

Josephova permutace přiřazuje pozici pořadí vyřazení. Součin rotací
živé fronty dává28; první návrat zdvojovací permutace na1..n dává
inverzi, proto se v29 cykly obracejí. Opravený vzorec pevných bodů30
vylučuje falešnou nulu. Pro31 je nutné m>1 a opravená mocnina(m−1)^k.
K hustotám reziduálních tříd je doplněn uniformní ocas: parametr
h=n−j určuje n pro pevné k nejvýše jednou a počet případů je nejvýše
N((m−1)/m)^k+1. Součet přes možné k=O_m(log N) opravňuje limitu
nekonečné řady; samotná její konvergence by nestačila.

V32 každá vrstva posune prvek nejvýše o1. Volitelné sousední
transpozice spojují různé cykly, nikdy je nerozdělují; konečná
sousední cesta zajistí jediný cyklus. V33 komutátor konjugovaných
pěti-cyklů vytváří logickou konjunkci. Involuce dovolují obracet
bloky; m se umocňuje na druhou, délka násobí4. Vlastní konstrukce
testu i<j má délku4^(l+1)−2·3^l, lze ji doplnit identitami na
požadované6^(l+1)−4^(l+1). Netvrdí se optimálnost.

Blokové přesuny34/35 mají gcd cykly. Virtuální druhá kopie prostředního
bloku se při návratu přeskočí jediným krokem. Známá oprava2006 mění
hranici operandů druhé metody35: γ''β s γ', ne γ'' s βγ'. Vlastní
MIX řešení36 zachovávají celá slova včetně−0 a pracují s virtuální
délkou6000 v plném slově, nikoli dvoubajtovém registru. Časy
38+25g+24l+29m+22n+d a65+14P jsou pro konkrétní doložené rutiny,
ne globální minima. Doplněk37 má úplnou indukci rozkladu sudé
permutace na dva n-cykly;38 je přejmenování cyklů konjugací a dává
36 řešení části(c), žádné části(d), pravdivé(e,f).

## Výjimky, známé opravy a stav

Přeskočené plné prameny: Huang1981; Berman1958 a Windley1959;
Cate–Twigg1977 mimo získaný původní kód, úplný Fich1995 a audit
celých externích Fortran programů; přesná sazba IFIP1971 proti
přečtenému primárnímu reportu. Dále Todhunter1860§762 a titul
Chelsea1967, vyčerpávající historie prvenství/rozšíření inkluze–exkluze;
časopisecká343 Knuth–Trabb Pardo; Herstein–Kaplansky1974§3.5,
Shams2002, Alpern1978 a Mohammed–Subi1987. U Barringtona je přijat
primární konferenční důkaz1986, nikoli nezískaná časopisecká verze1989;
Fletcherův kód je primární přetisk, ne obraz původní časopisecké326.
Není nově tvrzena absence vztahu lambda ke všem klasickým konstantám.
Přijaté pramenné recenze uvádějí přesné již přečtené stránky; dnes
nebyly všechny historické skeny znovu zobrazovány.

Všechny čtyři aktuální textové vrstvy errat byly znovu porovnány
pro164–185 a522–527. Přímo přečteny obrazy all1-prepre15,16,38,39,
all1-pre11 a all1 8,14, včetně přidaných zadání i odpovědí37/38.
Změna písmene m→n v(25), konvence pi^− místo pi^(−1), doplnění
symbolu p_m, nový registr J a nové reference nejsou samy původní
matematické vady. Mapa červeně označuje skutečné vadné lokace.

Úlohy12,23,28,29,32,35 se uzavírají s uvedenými bibliografickými
výjimkami. Všech36 původních a2 přidané úlohy sekce jsou nyní
matematicky uzavřené. Hlavní text zůstává partial kvůli C0028 a
neuzavřené historické prioritě; tyto mezery neskrývá procento úloh.
Nové neznámé chyby0. Další souvislý průchod začíná§1.4 na186.
