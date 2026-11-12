# Struktura přesných pokrytí: úplný průchod DLX29–35

Kontrola 1. listopadu 2026. Zadání126–127, odpovědi421–422.
Původní PDF stránky byly zobrazeny, u nového F109 také autorův původní
PostScript, Pre-Fascicle5C, str63 a126. Str71 výslovně zavádí do všech
následujících přesných pokrytí primární i sekundární položky; každá
možnost musí obsahovat alespoň jednu primární položku.

Výsledky a vstupy: `results/dlx_structure/`. Relevantní úplná errata4B
i historického Fascicle5 byla porovnána s aktuálními oficiálními soubory
v18:17:54UTC; všechny čtyři zdroje byly beze změny. Hledání podle stránek,
čísel úloh i výrazů uniform/Hamming/diversity/primary je zaznamenáno
v `errata-check.json`. Oprava F109 nebyla nalezena.

## 29–30: všechny stromy, včetně celého vytištěného příkladu

Obecný indukční důkaz a10880 úplných označených stromů jsou v
`EXACT_COVER_NOTES.md`, `check_search_trees.py` a `results/search_trees.json`.
Tyto hotové výčty nebyly opakovány. Nyní doplněna kontrola všech210prvků
vytištěné matice14×15 v `check_dlx_randomization.py`.

Obrázek v zadání má kořen se dvěma dětmi, každé se třemi neúspěšnými listy.
Po seřazení sloupců do vytištěných bloků se rekurzivně vytvořená matice
shoduje s každým bitem příkladu. Neměnný množinový výčet vrací celý
očekávaný uspořádaný strom; původní DLX1 nezávisle potvrzuje profil1,2,6,
tedy9uzlů, a žádné řešení.

Historická oprava14.12.2019 změnila ochranné řádky z indexů{1,2} na{0,1}
a odpovídající bity matice. Naše4B ji už obsahuje. Oprava22.3.2023 k30
řeší kořen, který sám je řešením: použije se matice0×0. S touto bází
stejná indukce funguje i pro všechny další označené listy.

V konstrukci29 jsou všechny položky primární. Dvě úspěšné sourozenecké
větve musejí obě pokrýt přesně všechny zbývající sloupce, takže jejich
řádky jsou duplicitní. To dokazuje poslední poznámku30 v jejím kontextu.
Na obecná pokrytí se sekundárními položkami se tato poznámka nepřenáší:
možnosti{a,x},{a,y}, kde pouze a je primární, dávají dvě úspěšné větve
bez duplicit. Úloha30 ale výslovně pokračuje v maticové konstrukci29;
toto rozšíření nepožaduje. Není zaznamenáno jako chyba.

## 31: přesné rovnoměrné náhodné volby

V I4 se LEN zvýší **před** vložením nové položky. Má-li starý seznam
m prvků, nový prvek tedy volí jednu z m+1 pozic. Odstraněním posledního
vloženého prvku z libovolné cílové permutace získáme právě jednu předchozí
permutaci a právě jednu pozici. Její pravděpodobnost je1/m!·1/(m+1),
tedy1/(m+1)!. To induktivně dokazuje rovnoměrnost každého seznamu.
Nové náhodné volby pro různá vložení se berou nezávisle.

Při průchodu délek udržujeme dosavadní minimumθ, počet jeho výskytů r
a rovnoměrně vybraný index z těchto r výskytů. Menší délka zahodí starý
výběr a nastaví r=1. Další shoda se přijme s pravděpodobností1/(r+1).
Starší index má potom pravděpodobnost(1/r)·r/(r+1)=1/(r+1), stejně jako
nový. Větší délka nic nemění. Tyto větve jsou alternativy vzhledem
k dosavadnímuθ. Volitelný předčasný konec přiθ=0 z odpovědi9 se při
požadavku rovnoměrné volby mezi **všemi** minimy nepoužije.

`check_dlx_randomization.py` ověřil celé přesné distribuce permutací
délky1–7 a21844vektorů délek (délka1–7, hodnoty0–3). Používá racionální
pravděpodobnosti, nikoli Monte Carlo. Odpověď31 je správná.

## F109: v definici uniformity chybí „primárních“

Úloha32(d), str127, tvrdí sudou Hammingovu vzdálenost pro možnosti se
stejným počtem **všech položek**. Odpověď na422 však používá stejný počet
**primárních položek**. Tyto podmínky nejsou ekvivalentní podle definice
na71. Nejmenší potřebný rozdíl v počtu možností dává tento vstup:

    a b | x y
    a b
    a x
    b y

Primární jsou a,b; sekundární x,y. Každá možnost má přesně dvě položky.
Platná řešení mají vektory(1,0,0) a(0,1,1): první používá jedinou možnost,
druhé dvě disjunktní možnosti. Jejich Hammingova vzdálenost je3, tedy lichá.
Jsou to právě všechna řešení, což potvrzuje jak přímý výčet8podmnožin,
tak neupravený autorův DLX1. Žádná možnost není prázdná ani čistě sekundární
a žádné dva řádky nejsou stejné.

Oprava: definovat zde uniformitu stejným počtem **primárních** položek
v každé možnosti. Tento počet k je podle definice na71 kladný. Každé
řešení pak má přesně N1/k možností, takže dvě řešení ztratí a získají
stejný počet souřadnic a jejich vzdálenost je sudá.

Shodné chybné zadání je v PDF i původním PS. Odpověď již zamýšlenou
podmínku má, takže stačí opravit zadání. Fyzický exemplář zatím neověřen.
Jde o jiné tvrzení než F078, přestože příčinou obou je započítání
nepovinných sekundárních položek. Doplnění jedné opravy neopraví druhé
místo automaticky. Nejde o tvrzení o prvenství nálezu.

## Zbytek32: malé vzdálenosti a kvaziuniformita

(a) Jedna změněná souřadnice by přidala nebo odebrala možnost bez změny
pokrytí primárních položek. Taková možnost by musela být čistě sekundární,
což definice vylučuje. Vzdálenost1 není možná.

(b) Při vzdálenosti2 nemohou být obě změny jen přidáním ani jen odebráním,
protože každá možnost má primární položku. Vyměněné možnosti proto musejí
mít stejné primární projekce. Příklad{a,x},{a,y} výše dává vzdálenost2.

(c) Při vzdálenosti3 je na jedné straně jedna a na druhé dvě možnosti.
Primární projekce té první je disjunktní sjednocení projekcí těch dvou.
Příklad se všemi položkami primárními: {a,b},{a},{b}; řešení(1,0,0)
a(0,1,1). Knižní odpověď uvádí nutnou podmínku, nikoli tvrzení, že
libovolné tři řádky s touto vlastností zaručují rozšíření do dvou řešení.

(e) Neprázdná podmnožina primárních položek Q s konstantním počtem k
v každé možnosti dává při existenci řešení k>0 a přesně|Q|/k zvolených
možností. Stejný argument jako v opraveném(d) dokazuje sudost. Je-li k=0,
nemůže být žádná položkaQ pokryta, a tedy nejsou řešení a tvrzení je
prázdně pravdivé. Identifikace poloviční vzdálenosti s počtem přemístěných
pojmenovaných dílků v pokrytí polyformami je správná: každý změněný dílek
odebere jednu možnost starého umístění a přidá jednu možnost nového.

`check_cover_diversity.py` doplňuje důkazy úplným výčtem10435problémů
s nejvýše4položkami a5různými možnostmi, pro všechny neprázdné množiny
primárních položek až na přejmenování. Celkem14668řešení; ověřeny všechny
páry. Zvlášť zahrnuty3případy duplicitních možností a tři celé množiny
řešení porovnány s původním DLX1.

## 33: přidání právě jednoho řešení

Původní Matsuiho konstrukce je správná. Nová primární položka se vyskytuje
jen ve dvou přidaných možnostech. Výběr poslední zakryje všechny položky
a vyloučí každý původní neprázdný řádek; dává právě jedno nové řešení.
Výběr předposlední zakryje pouze novou položku a zbytek je přesně původní
problém. Rozměry(m+2)×(n+1) i bijekce řešení souhlasí, také pro0×0,
kde vzniknou dvě jednořádková řešení nad jednou položkou.

Známá změna12.10.2025 doplňuje požadavek efektivní konstrukce. Náhrada
20.12.2025 připisovaná N.Postingovi pro n>0 jednoduše přidá řádek samých
jedniček; ten je jediným novým řešením. Ostatní řešení se nemění, protože
žádný starý řádek není nulový. Pokud se chceme vyhnout duplicitě již
přítomného plného řádku, funguje původní konstrukce s novým sloupcem.

### C018: nula sloupců v publikované náhradě

Pouze kandidát na upřesnění: náhrada má formální okraj n=0.
Matice0×0 nemá nulové řádky a její jediné řešení je prázdné. Přidání
řádku délky0 však vytvoří prázdnou možnost, zakázanou definicí na71.
Stačí použít původní konstrukci i pro tento případ nebo předepsat n>0.
Výsledek o obtížnosti ani původní knižní konstrukce tím nejsou dotčeny.
Kvůli možné implicitní konvenci o kladné šířce matice jde jen o kandidáta;
není započítán jako nová potvrzená chyba knihy.

Důsledek NP-těžkosti platí: z libovolné instance rozhodování existence
v polynomiálním čase vytvoříme instanci s alespoň jedním řešením; více
než jedno má právě tehdy, když původní měla řešení.

## 34: omezení sloupců na tři výskyty, s publikovanou opravou

Známé erratum2.1.2025 mění druhou skupinu z011α na001α. Po této opravě
mají obě přidané možnosti společnou první novou položku, takže se musí
zvolit právě jedna. Je-li původní vybraný řádek z první poloviny, připojí
se ochranný řádek101; je-li z druhé, připojí se110. Zvolený ochranný řádek
zablokuje opačnou polovinu a druhá zbývající položka vynutí právě jeden
řádek správné poloviny. Ostatní původní položky se nemění. To je bijekce
všech řešení, s jednoznačným rozšířením každého původního.

Potenciál T=sum(max(cj−3,0)) klesne při každém kroku přesně o1:
sloupec délky t>3 nahradí sloupce délek2, floor(t/2)+1, ceil(t/2)+1.
Ostatní délky se nezmění. Proto je přesný počet kroků T a rozměry
narostou o2T řádků i2T sloupců. Původní PDF i PS používají **tečkované
minus**, tedy právě max(cj−3,0); převod do textu tečku nezachová.
Zdánlivý problém záporného T byl chybou čtení, nikoli nálezem v knize.

Každý původní řádek má po kroku stejný počet jedniček a nové řádky mají2.
Omezení řádků na nejvýše3 se tedy zachová. Pro úplnost lze NP-těžkost
případu s malými řádky odvodit přímo z obecného přesného pokrytí:
možnost{s1,…,sk} s k>3 nahradíme možnostmi{si,ai,bi} a{bi,a(i+1)}
pro i=1..k, s cyklickými indexy a novými primárními ai,bi. Rovnice pokrytí
ai a bi vynutí buď všechny možnosti prvního typu, nebo všechny druhého.
První volba představuje přijetí původního řádku, druhá jeho odmítnutí.
Tento polynomiální převod dává řádky nejvýše3; následná knižní konstrukce
omezuje i sloupce na3 a zachová řešení. Příslušnost do NP je bezprostřední
kontrolou zvolené podmnožiny řádků. Důsledek knihy je tedy správný.

Poznámka o MRV je vysvětlením ztráty informace v délkách sloupců, nikoli
obecnou větou, že každý takto převedený problém musí mít delší běh.

## 35: přesně tři výskyty

Nové tři sloupce mají samy přesně tři jedničky. Ve starém sloupci délky c
přibude[ c<3 ]+[ c<2 ]+[ c<1 ]=3−c jedniček. Délka je tedy také3.
První tři nové možnosti pokrývají vždy dvě z nových tří položek. Každé
dvě se protínají a jedna samotná nestačí. Musí se proto vybrat poslední
nový řádek se všemi třemi položkami; ten vyloučí ostatní nové řádky
a ponechá přesně původní problém. Platí i pro prázdné sloupce a0×0.

`check_cover_reductions.py` ověřil5217vstupů, všechny původní podmnožiny
a celé množiny řešení po převodech. Projekce řešení je bijektivní,
v35 je poslední řádek vždy nucený. Zkontrolováno3379jednotlivých štěpení
a přesný pokles potenciálu i obě dimenze. Zahrnuty duplicity, neobsazené
sloupce,0×0 a sloupce až s20výskyty. Tři příklady původním DLX1 navíc
potvrzují4řešení původní matice,2po starém chybném převodu a4po známé
opravě. Tato chyba se vykazuje jako publikované E025, nikoli nový F nález.
