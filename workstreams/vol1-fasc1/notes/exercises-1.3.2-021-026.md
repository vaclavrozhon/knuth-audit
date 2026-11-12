# §1.3.2′ — úlohy 21–26, samostatné argumenty

Zadání p. 47 / file 55; odpovědi p. 104–108 / file 112–116.
Převzaté důkazy a výpočty se znovu nespouštěly. Zde je ověřena sémantika
popsaných rutin; nejde o test konkrétní pipeline nebo hostitelského systému.

## 21 a 22 — Fareyovy zlomky

Matematiku přebírám z `workstreams/vol1/notes/mixal-farey.md`: při
`bc−ad=1` má každý zlomek `p/q` mezi `a/b` a `c/d` jmenovatel
`q=(cq−dp)b+(bp−aq)d ≥ b+d`. Pro `h=floor((b+n)/d)` platí
`n−d < hd−b ≤ n` a determinant nového páru zůstává 1. To dokazuje
kladnost jmenovatele, redukovanost, úplnost a zastavení v `1/1`.
Převzatý důkaz zahrnuje také počet `1+Σφ(q)=3n²/π²+O(n log n)` a
konkrétní seznam pro řád 7. Původní velké testy se neopakovaly.

Odpověď MMIX 21 obsahuje pouze zástupné `Farey SET y,1; ... POP`.
Proto vlastní úplné tělo je v `sources/farey21.mms`. Předpokládá
`1 ≤ n < 2^32`, disjunktní čtyřbajtově zarovnaná pole X a Y s kapacitou
celé posloupnosti a platný návratový rámec. X a Y jsou globální adresové
registry přidělené volajícím, místní registry $0 až $9 jsou pracovní.
Nejde o znovu prokázanou obecnou sémantiku zásobníku.

Invariant: před smyčkou obsahují `(a,b),(c,d)` poslední dva sousedy;
`off` je čtyřnásobek indexu druhého z nich. Obě položky již byly uloženy.
Při `c=d` jde díky redukovanosti o `1/1` a rutinu ukončíme. Jinak DIV
vypočte kladné h, dva součiny a rozdíly další zlomek a posun o 4 uloží
právě další položku. Počáteční zápisy `0/1,1/n` pokrývají i n=1.
`hd=b+Y≤2n`, `hc=a+X≤2n`, takže všechny aritmetické mezivýsledky
jsou menší než `2^33`; kladná signed DIV/MUL zde dávají přesný výsledek.
Ukládané čitatele a jmenovatele jsou nejvýše n, tedy se vejdou do tetrabyte.
Platnost adres a dostatečná kapacita polí zůstávají běžnou vstupní podmínkou,
nikoli důsledkem samotného `n<2^32`.

Historie Haros/Farey/Cauchy je převzata v přesném rozsahu z
`workstreams/vol1/notes/mixal-farey-sources.md`: obsah přečtených přetisků
ano, nedostupné původní Harosovo stránkování a úplná historie názvu ne.
Známá oprava Philomathique → philomatique je již v erratech, ne nový nález.

## 23 — nulování paměti

Předpoklad: `n≥0` je signed octabyte a celý interval je platně zapisovatelný.
První BZ vrátí prázdný interval bez zápisu. Smyčka 1H zapisuje po jednom
bajtu do zarovnání na 8 nebo do vyčerpání n. Její návrat přes Zero vždy
znovu zkontroluje n. Každý zápis posune a o vlastní délku a zmenší n o
stejnou délku, takže zachovává invariant již vynulovaného prefixu.

Pro n≥64 smyčka 2H doplní osmibajtové zarovnání na 64. Spotřebuje nejvýše
56 bajtů, proto nečte záporný zbytek ani nepřeskočí konec. Smyčka 4H
zapíše přesně osm octabytes na adresách a+0,8,…,56, pouze pokud n≥64.
Těsně po odečtení 64 je připraven CMP pro rozhodnutí o dalším bloku.
PREST je výkonnostní nápověda pro právě zapisovanou cache line. Smyčka 6H
zpracuje zbytek po osmi a 8H po jednom. Žádný zápis nepřesáhne interval.
V dlouhé části je jedna paměťová operace na osm bajtů, tedy minimum
pro maximálně osmibajtové běžné zápisy. **Partial:** zadáním požadovaná
měření různých pipeline/cache konfigurací nebyla provedena; globální
rychlost vůči všem možným implementacím není tvrzena.

## 24 — kopírování řetězce

Označme `i=8(s mod 8)`, `o=8(d mod 8)` pro původní adresy s,d.
`m=(2^64−1)>>i` maskuje zdrojový prefix před řetězcem. Vždy platí,
že `$0` ukazuje do právě načteného zdrojového octabyte a `$0+$1`
identifikuje odpovídající cílový octabyte. Instrukce LDOU/STOU ignorují
spodní tři adresní bity. Předpokládáme nepřekryv zdroje a cíle jako zadání.

Při `o≥i` nastaví rutina `r=o−i`, `l=64−r`. První MUX zachová levý
cílový prefix ve zdrojové orientaci. `tt=in>>r` dodá pravou část nového
slova a MUX s maskou `(2^64−1)>>r` zachová levou část v out. Při dalším
průchodu `out=in_previous<<l` a nový vstup doplní právě zbývajících
64−r bitů. Při `o<i` nastaví `r=64+o−i`, `l=i−o` a zmenší rozdíl adres
o 8. První vstup vyplní jen levou část out a krok 2H připojí část dalšího
vstupu. Právě tento posun adres zaručuje, že první zápis pořád zasahuje
první cílový octabyte. Obě větve pak sdílejí invariant spojení dvou
sousedních zdrojových slov `previous<<l | current>>r`. Posuny o 64 jsou
podle MMIX nulové, takže zvláštní případ stejného zarovnání je správný.

BDIF s `ones` dává hodnotu 1 právě v nulových bajtech. Úvodní AND s m
vyloučí nuly před řetězcem. Nula v části právě vydávané do cíle je
odhalena `t>>r`; nula v zadrženém ocasu přejde přes 5H jako `t<<l`.
Proto se nezapíše žádný celý další octabyte po první nule. V závěru
MOR s `flip` obrátí pořadí bajtů; `mm & ~(mm−1)` vybere nejnižší
nenulový bit, tedy první nulu v původním směru. Obrácení zpět a odečtení
1 vytvoří masku bajtů **za** terminátorem. Poslední MUX zachová tyto
původní cílové bajty, kdežto prefix včetně nulového terminátoru převezme
z out. První cílový prefix byl zachován úvodním MUX. Funkční správnost
pro všechna zarovnání tak plyne z invariantů, nikoli z několika vzorků.

Triviální kód provede n+1 čtení i zápisů; úvodní SUBU stojí 1υ,
každý průchod 4υ, poslední špatně predikované PBNZ navíc 2υ:
`(2n+2)μ+(4n+7)υ`. U dlouhé části nové rutiny je na osm bajtů právě
jedno čtení, jeden zápis a osm instrukcí, tedy hlavní člen
`(n/4)μ+nυ`. **Partial:** přesné konstanty pro všechny kombinace
zarovnání a malých n, a tedy univerzální prahové tvrzení n≥8,
nezávisle uzavřeny nejsou. Přibližný vzorec není vydáván za přesný profil.

## 25 — četnosti přes wydes

Tabulka count má `2^16` octabytes, tedy `2^19` bajtů, a předpokládá se
počáteční nulová paměť. Pro každou dvojici bajtů (u,v) je adresa
`count+8(256u+v)`. SRU o 45 ponechá ještě tři bity dalšího bajtu,
ale zarovnání LDO/STO je správně zahodí. Čtyři průchody po SLU o 16
zpracují celý nenulový octabyte; při absenci nul nemůže mezilehlý zbytek
omylem zaniknout dříve.

Ve finálním octabyte se nejdřív započte wyde a potom testují jeho dvě
nuly. Pokud terminátor leží v druhém bajtu, potřebujeme započítat
`count[u,0]`; pokud leží v prvním, přebytečný bajt se může objevit pouze
v `count[0,v]`. Druhá fáze pro j=1,…,255 počítá přesně
`count[j,0]+Σ(k=1..255)(count[j,k]+count[k,j])`, takže druhou možnost
správně zahodí. Diagonální count[j,j] je dvakrát, jak vyžadují dva stejné
znaky. Proměnné p,b,t procházejí přesně tyto řádky/sloupce: p=8j,
row=count+256p, t=p+2048k. Výsledek tedy dává všech 255 požadovaných
četností před první nulou. Předpokládáme četnosti v rozsahu signed ADD.

Vedlejší číselná porovnání `n<2^17` a poměr asi `10/17` při `n≈10^6`
se zde nepřebírají jako doložené bez konkretizace porovnávané rutiny a μ/υ.
Bourne–Ford 1961, 48–67 nebyl nově získáván; bibliografická výjimka.

## 26 — rozvržení pipeline

První hlavní smyčka střídá extrakci následujícího bajtu s načtením,
zvýšením a uložením aktuálního čítače. Po loadu v hlavní smyčce je
vložena nezávislá instrukce; závislé zvýšení přichází až potom. Každý
bajt vyvolá právě jeden read–increment–write. Koncová 3H větev zpracuje
bajty postupně včetně nulového čítače a zastaví po nule; čítač nuly je
mimo 255 požadovaných výsledků. Její bezprostřední LDO/INCL není důkazem
stejného rozvržení jako dlouhá hlavní smyčka.

Druhá varianta ukládá střídavé bajty do dvou tabulek freq/freqq. Pak
součet po složkách vrací tytéž četnosti. Dvě tabulky jsou nutné pro tento
konkrétní rozvrh: při stejných sousedních znacích by dva předběžné loady
z jedné tabulky načetly c a obě store zapsaly c+1 místo c+2. Hodnota
`2^19` pro velikost předchozí wyde tabulky je přesná; tvrzení, že se
na menší cache obecně nevyplatí, závisí na distribuci přístupů.
**Partial:** ve zdroji vynechané unrolled úseky nejsou kompletní program
a žádná konkrétní pipeline konfigurace ani výkonová převaha nebyla měřena.
