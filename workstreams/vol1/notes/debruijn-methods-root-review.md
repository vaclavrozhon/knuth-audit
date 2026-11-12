# V1-X0774–X0775: de Bruijnovy metody a přesné vydání

Obsahová návaznost obecného doporučení na s.121 je checked
v přímo čteném vydání1958. Sazba citovaného druhého vydání1961
nebyla kolacionována; tato užší ediční otázka zůstává partial.
Není důvod hlásit chybný rok: konkrétní institucionální katalog
KIT potvrzuje druhé vydání, Amsterdam, North-Holland1961, XII+200s.
Root přečetl uložený katalogový HTML záznam, nikoli fyzickou tiráž1961.

Root ověřil všech16 souborů a28 vnějších závislostí zmrazeného
`parallel/asymptotic-primary-followup/results/debruijn-methods-manifest.json`,
SHA-256 `6dd1ad0927f470c96a7c2329c5b7449d24cf9812bb0f246f3369075e54a64c5b`.
Přímo zobrazil titul1958 a dvojstrany36–39,42–47 z původních Rice
skenů v parallel/robson-tree-followup. Rozhodující nová root četba:
§3.4 na37–38 a celé§3.9 na43–46; jiné části zobrazených dvojstran
nejsou tímto zápisem automaticky nově auditovány. Agent četl celé
§3.1–3.9 a začátek3.10; jeho přesná mapa je ve stavovém souboru.
Starý přenosový log s vypnutým ověřením tehdy neúplného TLS řetězce
Rice zůstává mezi závislostmi, nezastíráme původ těchto souborů.

V§3.4 jsou členy `a_k(n)=4^k binom(n,k)^2`. Poměr sousedních členů
lokalizuje maximum u2n/3. Významné okno má šířku řádu sqrt(n),
ve větším okně n^(2/3) se použije Stirlingova formule a mimo ně
zanedbatelný ocas. To je konkrétní stejná struktura metody jako
v úloze14. V§3.9 je `f_n(x)=exp(-alpha x^2/n)`, alpha>0,
a součet přes celá k od−n do n. Eulerova–Maclaurinova formule
s integrálním zbytkem dává pro každé pevné m chybu O(n^(1/2−m)).
Škálování x=sqrt(n/(2alpha))y na44 ukazuje, proč konstanta smí
záviset na m. Následný rozbor45–46 odděleně kontroluje rostoucí m
a porovnává odhad s transformací theta řady; nejde o neoprávněné
dosazení proměnného m do dřívějšího pevného O-odhadu.

Takto je ověřeno více než bibliografický titul: kniha skutečně
rozvíjí doporučené metody. Přečtené pasáže však neobsahují doslova
celé pětidílné zadání14 s osobní atribucí de Bruijnovi. Nevydáváme
shodnou metodu za určení původu každé části úlohy. Dosavadní
matematický checked stav14 a přijaté důkazy zůstávají beze změny.

TAOCP121 root znovu přímo četl. Všechny čtyři vrstvy errat byly
prohledány podle jména, tématu a stran; nová oprava nebyla nalezena.
Žádný nový nález ani opakované úspěšné testy. Zbývající ediční
kolace1961 je výslovně zaznamenaná, nikoli nahrazená metadaty.
