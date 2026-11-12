# P0221 — oddělená geometrie, vstupní data a tři vytištěné hrany

6. listopadu 2026. P24/file41, první odstavec; originál
`images/file041.png`. Celková P0221 zůstává **partial**, ale následující
části jsou samostatně doložené v P0505–P0507. Samotný výpočet 381
nikdy nenahrazoval geometrickou větu ani kontrolu skutečných souřadnic.

## P0505: přesná geometrická věta a její důkaz

Nechť P je konečná množina n≥3 různých bodů v rovině, žádné tři neleží
na přímce a žádné čtyři na kružnici. Tato obecná poloha je **postačující
předpoklad** následujícího argumentu. Hranu uv určeme existencí kružnice
přes u,v, v jejímž otevřeném vnitřku není žádný bod P. Hrany tvoří
přímkovou triangulaci konvexního obalu P.

Zvedni p=(x,y) do p̂=(x,y,x²+y²). Kružnici se středem c a poloměrem r
odpovídá rovina

    z = 2c_x x + 2c_y y + r²−|c|².

Rozdíl výšky zvednutého bodu a této roviny je |p−c|²−r². Bod uvnitř
kružnice je pod rovinou, na kružnici v ní, vně nad ní. Prázdná kružnice
je tedy právě nevertikální dolní podpůrná rovina konvexního obalu
zvednutých bodů. Každý zvednutý bod leží na dolním obalu: rovina
z=2p·(x,y)−|p|² se ho dotýká a pro každý q≠p je odstup |q−p|²>0.

Pro n≥4 je zvednutý obal trojrozměrný: společná nevertikální rovina
čtyř bodů by znamenala čtyři body na kružnici, vertikální by znamenala
jejich kolinearitu. Každá dolní stěna má právě tři vrcholy, protože
čtvrtý by byl na její kružnici, a projekce stěny je nedegenerovaný
trojúhelník. Pro n=3 je výsledkem přímo jediný trojúhelník.

Dolní stěny se promítají bez překrývání vnitřků: nad bodem konvexního
obalu P je nejnižší bod zvednutého konvexního obalu jednoznačnou výškou.
Dvě různé rovinné stěny se nemohou shodovat na celé otevřené projekční
oblasti. Každý bod konvexního obalu má neprázdný kompaktní svislý řez
zvednutým obalem, tedy minimální výšku; projekce dolních stěn proto
pokrývají celý konvexní obal. Všechny body P jsou jejich vrcholy díky
výše uvedeným striktním tečným rovinám. To dává triangulaci.

Je-li uv na prázdné kružnici, její podpůrná stěna obsahuje û,v̂
a nejvýše jeden další zvednutý bod. V obou možných případech je ûv̂
hrana této dolní stěny. Obráceně každá hrana dolní triangulace leží
na některé trojúhelníkové dolní stěně, jejíž rovina poskytuje požadovanou
prázdnou kružnici. Tím je dokázána ekvivalence, nejen jeden směr.

K cyklické hranici konvexního obalu přidej vrchol INF a spoj jej se
všemi hraničními vrcholy v druhém disku sféry. Tento disk je triangulován
vějířem. Výsledkem je triangulovaná sféra na n+1 vrcholech; stereografické
promítnutí z bodu mimo kresbu dává rovinný graf. Již dokázaný Eulerův
argument P0151 dává E=3(n+1)−6. Dosazení n=128 je stará P0220,
nikoli nově měřený počet hran výstupu generátoru.

## Proč P0221 přesto zůstává partial

Primární `sources/sgb-gb_plane.w`, řádky 152–180, výslovně uvádí
podmínky různých bodů, žádných tří kolineárních a žádných čtyř
kokružnicových bodů. Při jejich porušení používá symbolickou malou
perturbaci; řádky 191–200 předepisují souřadnice pod 2¹⁴ a různé ID
pro rozhodování degenerací. Kód predikátů tuto zvláštní větev skutečně
má. To nebyl skrytý předpoklad, který by bylo správné přejít aritmetikou.

Bez takového omezení nelze obecnou ekvivalenci prostě převzít pro jednu
zvolenou triangulaci: čtyři rohy čtverce leží na společné prázdné
kružnici, takže kružnicové kritérium připustí obě diagonály, zatímco
přímková triangulace zvolí jen jednu. To je **test obecného předpokladu,
nikoli protipříklad konkrétních 128 knižních měst**, a není to nález.

U konkrétních dat bylo nyní prokázáno 128 různých souřadnic a níže
uvedené hrany. Nebyla ověřena nepřítomnost všech kolineárních/
kokružnicových degenerací nebo jejich relevance pro všechny dolní
stěny. Nebyl proveden úplný důkaz celého inkrementálního Delaunay kódu
ani nový běh triangulace. Jeho citovaná monografie *Axioms and Hulls*
je explicitní externí zdroj, nikoli zde zrekonstruovaný algoritmus.
Historická geografická přesnost každého řádku vstupních dat se rovněž
netvrdí. Proto nelze celou původní P0221 povýšit na checked.

## P0506: přesný vstup a normalizace souřadnic

Primární soubory `sources/sgb-gb_plane.w`, `sources/sgb-gb_miles.w` a
`sources/sgb-miles.dat` pocházejí beze změn z již archivovaného autorova
taru; vedle každého jsou metadata cesty, členského data a SHA-256.
`gb_miles.w`, řádky 308–316, převádí datový řádek [lat,lon] na

    a=lat−2672,       x=12312−lon,       y=a+⌊a/2⌋.

Je to konkrétní rovinná reprezentace, nikoli vzdálenosti na zeměkouli.
Přímé čtení původních městských řádků dalo 128 měst a 128 různých
souřadnic. N=128 ve vytištěném volání vybere všechna, nuly ve vahách
mění jen pořadí shodně vážených měst. `extend=1` přidává jeden INF,
tedy 129 vrcholů; `prob=0` nevyřazuje žádnou Delaunay hranu, protože
zdrojová podmínka porovnává nezápornou náhodnou hodnotu s nulou.
Tím je ověřen vrcholový počet a význam parametrů, nikoli globální
geometrické předpoklady nebo nový výstupní počet hran.

## P0507: tři konkrétní hrany — silnější, striktní certifikáty

Vybraný datový přepis podle stejné transformace:

| město | původní [lat,lon] | bod (x,y) |
|---|---|---|
| Seattle, WA | [4760,12233] | (79,3132) |
| Vancouver, BC | [4927,12312] | (0,3382) |
| Toronto, ON | [4365,7938] | (4374,2539) |
| Rochester, NY | [4316,7761] | (4551,2466) |

Pro dvojici u,v vezmi kružnici s průměrem uv, středem m=(u+v)/2
a R²=|u−v|²/4. Pro každý další bod w je přesně

    |w−m|²−R² = (w−u)·(w−v).

Přímé celočíselné vyhodnocení této pravé strany pro všech ostatních
126 bodů dalo následující **kladná minima**; všechny jednotlivé hodnoty
jsou v `results/plane-miles-named-edges.json`:

| dvojice | střed | R² | nejmenší odstup ostatního bodu |
|---|---|---|---|
| Seattle–Vancouver | (79/2,3257) | 68741/4 | 15726, Tacoma, WA |
| Toronto–Rochester | (8925/2,5005/2) | 18329/2 | 48688, Syracuse, NY |

V obou případech nejsou další body ani uvnitř, ani na kružnici. Její
dolní podpůrná rovina se proto dotýká právě û,v̂ a určuje skutečnou
hranu, nezávisle na případných degeneracích jinde. Striktní kladné
odstupy se zachovají při dostatečně malé symbolické perturbaci.

Vancouver je navíc jediný bod s x=0; ostatní mají x≥9. Přímka x=0
je tedy podpůrná a dotýká se konvexního obalu pouze ve Vancouveru.
Ten je vrcholem hranice a má uvedenou hranu k INF. I tento striktní
odstup přežívá malou perturbaci.

Použit jediný cílený příkaz

    nice -n 15 python3 workstreams/vol4a/checks/plane-miles-named-edges.py

Jde o lineární kontrolu dvou pevných dvojic a jedné podpůrné přímky.
Nevytváří triangulaci, neprochází všechny trojice/čtveřice a netestuje
všechny dvojice měst. Pomocná racionální mez pro střed byla také uložena,
ale v obou případech vyšel přímo t=0, tedy výše uvedená průměrová
kružnice. Žádný opakovaný běh/census, nový nález nebo celostránkové
argumentové uzavření. Další souvislý blok pokračuje na p47; uvedené
reziduální meze P0221 zůstávají přístupné v inventáři.
