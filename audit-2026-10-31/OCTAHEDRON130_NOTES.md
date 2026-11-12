# DLX 130: MacMahonovy trojúhelníky na třech osmistěnech

Kontrola 2. listopadu 2026, lokální 4B, první vydání, druhý dotisk.
Zadání str. 139 a odpověď str. 449 byly prohlédnuty v původním PDF.
Oba obrázky jsou ověřeny přímo z vektorové kresby. Výsledek: nebyl
nalezen rozpor v matematických tvrzeních, počtech ani obrázcích.
Přijetí druhého nativního terminálu a uzavření registru eviduje
`results/octahedron130/checkpoint-checked.json`.

## Souřadnice a orientace

Vrchol `0**` znamená `(1,0,0)`, `1**` znamená `(-1,0,0)`;
analogicky pro druhou a třetí osu. Stěna `xyz` obsahuje právě
vrcholy s příslušnými třemi znaménky. Její hrany jsou `*yz`,
`x*z`, `xy*`. Takto vznikne šest vrcholů, dvanáct hran a osm stěn;
každá hrana patří právě dvěma sousedním stěnám.

Hrany však nelze všude číst ve stejném pořadí: při lichém `x+y+z`
se poslední dvě vymění. Pro stěnu 000 je vnější normála kladná ve
všech složkách; změna jednoho znaménka obrací determinant. Pythonový
model odvozuje orientaci vektorovým součinem skutečných vrcholů;
nezávislý C++ výčet používá právě tuto paritní formuli. Všech osm
pořadí souhlasí. Zrcadlově obrácený trojbarevný dílek se nezaměňuje
za jeho původní cyklický typ.

Počet typů trojúhelníků je `(64+4+4)/3=24` podle Burnsideovy věty
pro tři cyklické rotace. Čtyři jednobarevné typy mají jednu orientaci,
ostatních dvacet tři. Na každé stěně je tedy 64 možností, celkem 512.
Osm názvů stěn je primárních, 24 názvů dílků a 12 barevných hran
sekundárních. Primární položky vynutí právě jednu možnost na stěnu;
neobarvené sekundární dílky zakážou opakování typu a barevné hrany
vynutí shodu sousedů. Obráceně každé přípustné fyzické skládání
určuje právě jedno takové pokrytí. Všechny tři vytištěné příklady
možností jsou ve vstupu doslova obsažené.

## Úplné počty

`octahedron130_edges.cpp` nečte generátor XCC ani jeho tabulku sousedů.
Prochází všech `4^12 = 16 777 216` obarvení hran duální krychle,
z každého vypočte osm orientovaných typů a přijme právě případy
s osmi různými typy. Výsledek:

| Veličina | Počet |
|---|---:|
| Označená obarvení osmistěnu osmi různými dílky | 2 723 472 |
| Různé osmiprvkové podmnožiny dílků | 45 356 |
| Rozdělení všech 24 dílků do tří přípustných sad | 1 615 452 |

Všech 45 356 sad má uloženou četnost a explicitní dvanáctibarevný
svědek v `edge-sets.tsv`. Každý svědek byl ověřen samostatným modelem
odvozeným z prostorových souřadnic. Součet četností je 2 723 472.
Soubor není seznamem všech obarvení: úplnost počtu plyne z vyčerpání
celého konečného prostoru, nikoli z počtu uložených vzorků.

Pro druhý stupeň přímý algoritmus vybere A jako sadu obsahující `aaa`.
Potom B obsahuje nejmenší dosud nepoužitý typ a musí být disjunktní
s A. C je doplněk jejich sjednocení. Členství C mezi 45 356 sadami
se testuje přesnou adresací 24bitovou maskou. Každé neuspořádané
rozdělení má právě jednu takovou trojici; žádné dělení faktoriálem
ani odhad zde není. Prošlo 3 782 829 disjunktních dvojic A,B,
z nich 1 615 452 má přípustný doplněk. Každý tisící kladný případ
je uložen a samostatně ověřen, celkem 1 615 vzorků.

Odděleně původní `dlx2.w` řeší 512 možností první úlohy a pak
45 356 možností přesného pokrytí s 24 primárními názvy dílků.
První terminál potvrdil 2 723 472 řešení; všech 2 723 vypsaných
vzorků má správné prostorové hrany a osm různých typů. Druhý
terminál potvrdil **1 615 452 rozdělení**, všech 1 615 vypsaných
trojic je disjunktních a pokrývá všech 24 typů. Oba procesy skončily
návratovým kódem nula a úplným terminálním souhrnem; vstupy, zdroje,
binárky i výstupy mají kontrolní součty. Celá úloha 130 je uzavřená.

## Původní obrázky

Malá drátěná kresba v zadání má šest vrcholů a dvanáct hran.
Čtyři tečkované úsečky úmyslně končí těsně před zvlášť nakresleným
skrytým vrcholem. Po jejich spojení má každý vrchol stupeň čtyři;
chybějící tři dvojice tvoří perfektní párování. Graf je tedy přesně
`K6` bez perfektního párování, tj. graf osmistěnu.

Z odpovědi bylo extrahováno všech **72 barevných výsečí**.
Každý osmistěn je vyobrazen jako čtyři kosočtverce, po dvou stěnách,
které se dotýkají středovým vrcholem. Čtyři vnější rohy se při
složení identifikují s opačným pólem; osm zbývajících vrcholů se
po dvojicích identifikuje se čtyřmi rovníkovými vrcholy. Kontrola
nepředpokládá, že všechny společné hrany už v rovinné kresbě splývají.

Po tomto složení má každý obrázek všech osm stěn, každou hranu
právě dvakrát se shodnou barvou a osm různých orientovaných dílků.
Dohromady používají každý z 24 typů právě jednou. Druhý osmistěn
obsahuje všechny čtyři jednobarevné dílky, ostatní žádný. Orientace
všech 24 trojúhelníků souhlasí s vnější prostorovou orientací.

Vyčerpáním všech 24 permutací barev a všech 24 vlastních rotací
osmistěnu vyšly právě čtyři barevné symetrie celého rozdělení:

| Permutace barev a,b,c,d | Pohyb osmistěnů |
|---|---|
| a,b,c,d | Každý zůstává na svém místě. |
| b,a,d,c | Každý zůstává na svém místě, vhodně otočený. |
| c,d,a,b | První a třetí se vymění, druhý se otočí. |
| d,c,b,a | První a třetí se vymění a vhodně otočí. |

Počet čtyři zahrnuje identitu. Jde o Kleinovu čtyřgrupu; explicitní
rotace každého obrázku jsou uložené v `original-figure-checked.json`.
Výrok „one of the most interesting“ je subjektivní komentář,
nikoli tvrzení o optimalitě. Odkaz na budoucí §7.2.3 zde neudává
žádný další počet neizomorfních tříd, který by bylo třeba odhadovat.

## Errata a rozsah

Prohledány úplné i krátké seznamy 4B a Fascicle 5 a oba původní
TeXové soubory, tedy šest relevantních vrstev. Vyhledávání zahrnuje
strany 139/449, historické 137/257 a prefasciklové 75/153, názvy,
osmistěny a všechny tři počty. Žádný odpovídající záznam nenalezen.
SHA256 zdrojů souhlasí s jejich kontrolou proti oficiálnímu webu
2. listopadu v 08:06 UTC; oba TeXové seznamy byly znovu otevřeny
na webu při tomto bloku. Přesná metadata a dotazy jsou v
`errata-check.json`. Tato absence nezaručuje novost budoucích nálezů.

Nová chyba ani kandidát nevznikly. Úloha neobsahuje historickou
atribuci nebo externí citaci s neověřeným originálem. Strany 139
a 449 jako celek zůstávají částečné, protože obsahují další úlohy
a 449 i dosud neuzavřenou historii úlohy 129.
