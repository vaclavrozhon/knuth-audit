# Slova na Petersenově grafu, úloha171

Ověřeno 1. 11. 2026 po zapracování celé náhradní odpovědi
z 2. 1. 2025. Původní znění není nový nález.

Použit byl [oficiální seřazený slovník 5 757 slov](https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt).
Jeho pořadí nezávisle souhlasí se všemi šesti rangy příkladu na str.36:
slums1446, total185, awoke1021, tepid2537, using66, stage255.
Soubor, URL, čas stažení a SHA256 jsou archivovány v `sources/`.

`petersen_words.cpp` řeší přímo podmínky: dvě přidělená různá slova
mají společné písmeno právě tehdy, když je mezi vrcholy hrana.
Domény se omezují průnikem bitových množin. Nejde o kódování MCC.
Úplný průchod WORDS834 navštívil1 713 069 uzlů a našel přesně dvě
řešení. Jsou to množiny z knihy, lišící se jen slovem refer/fewer.
Obě používají muddy s rangem834, takže WORDS833 nemá žádné řešení.

Bylo explicitně nalezeno120 automorfismů Petersenova grafu. Jejich
obrazy cesty0–1–2–3 jsou právě všech120 orientovaných cest délky3,
každá jednou. Tím je doložena úplnost odstranění symetrií: nejprve
se na0 umístí slovo s nejnižším rangem, pak se z jeho sousedů zvolí
nejnižší jako1, z dalších sousedů1 nejnižší jako2 a obdobně3.
Každá orbita má přesně jedno takto zvolené zobrazení. U obou
výsledků to bylo navíc ověřeno přímo přes všech120 automorfismů.

Opravená redukce2025 je správná: každá hrana vybere jedno společné
písmeno s barvou1 v obou koncích. U nehrany sekundární položka
zakazuje společné písmeno. Barvy0/1 u každého vrcholu zachovávají
konzistenci se zvoleným slovem a sekundární jméno slova zakazuje
jeho opakované použití.

Každé ze dvou řešení má8 možností výběru písmen na hranách.
Proto je počet řešení MCC při omezení na11 slov obou nalezených
množin přesně2×120×8=1 920. Původní DLX2 tento počet reprodukoval.
Plný slovník834 byl vyčerpán vlastním CSP; omezený MCC slouží jako
nezávislá kontrola převodu a násobností, ne jako druhý úplný výčet.

Doklady: `results/petersen_words/verified.json`, všechny dva svědky,
úplný log a `verify_petersen_words.py`. Při prvním sestavení MCC
kolizovalo pomocné jméno primární položky v0 s písmenem v u vrcholu0;
bylo přejmenováno na V0, původní knižní názvy tuto kolizi nemají.
