# V3-C0021 — chybějící hranice s v §5.2.1–22

Stav: candidate/low, 7. listopadu 2026. Lokace: tištěná103,
file114, úloha22, tvrzení o nereprezentovatelnosti
2^s(2^s−1)−1. Originál `images/insertion-file-114.png` zobrazen.

Pro s=1 je toto číslo1 a první generátor2^s−1 je také1.
Koeficienty a_0=1, a_1=a_2=…=0 dávají reprezentaci, kterou
zadání popírá. Formulace v úloze výslovně neříká s≥2.

Úplný intervalový důkaz v `notes/insertion-proof-22-semigroups.md`
ukazuje, že největší mezera je v minusové rodině skutečně
2^s(2^s−1)−1 pro s≥2, ale pro s=1 není žádná nezáporná mezera.
Počet kladných mezer má správnou formuli i pro s=1. Plusová
varianta odpovědi je platná už pro s≥1. Dopad je tedy pouze
vynechaný mezní případ, nikoli chyba obecné konstrukce či nákladů.

Navržené zpřesnění: přidat „For s≥2“ do minusového zadání;
případ s=1 uvést jako triviální generátor1. Případná implicitní
konvence, že se zde bere pouze netriviální s, zůstává otázkou
výkladu. Z tohoto důvodu se položka neoznačuje confirmed.

Všech pět vrstev errat, včetně přesunutých prvovydaných odpovědí
600–601, bylo zkontrolováno po stránkách, podle čísla úlohy
i klíčových slov; žádná úprava tohoto rozsahu nebyla nalezena.
Přesná evidence je v `sources/insertion-semigroup-boundary-errata-review.json`.
