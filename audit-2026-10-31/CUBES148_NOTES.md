# DLX 148 — jedenáct kostek ze tří barev

Zrevidováno 3. listopadu 2026. Zadání 4B str.143, odpověď str.458;
autorův draft2019 str.79/162. **Celá úloha je správná a uzavřená.**

Pro každou dvojici protilehlých stěn je 3·2 možných barev; orientovaných
barevných kostek je tedy6³=216. Pod vlastními rotacemi se dělí na
**11 typů**: tři orbity velikosti8 a osm orbit velikosti24. Zrcadlové
obrazy se při definici fyzického typu automaticky neztotožňují.

Burnsideův důkaz nevyžaduje hledání sestav. Identita fixuje216 obarvení.
Osm rotací o120° kolem tělesových úhlopříček rozděluje stěny na dvě
trojice; jejich barvy musí být různé, proto každá fixuje3·2=6 obarvení.
Zbývajících15 rotací vynutí shodné barvy alespoň jedné protilehlé
dvojice, a tedy nefixuje nic přípustného. Počet typů je
(216+8·6)/24 = **11**. Malý úplný výčet tento důkaz kontroluje.

Z vektorů původního PDF i draftu přečteno všech **66 označení stěn**
jedenácti vytištěných kostek. Obě verze jsou stejné a představují přesně
celou množinu11 typů, bez opakování a se všemi protilehlými barvami různými.

Vytištěný tensor7×7×7 má **343 znaků**, z toho52 barevných stěn.
Obsahuje právě11 kostek: čtvercovou střední vrstvu3×3 a po jedné kostce
na obou stranách jejího středu. Každá barvená stěna patří některé z těchto
kostek; žádné nevysvětlené značky nezbývají. Všech11 rotačních typů je
použito jednou a všech14 vnitřních kontaktů souhlasí.

Geometrický tvar má16 prostorových symetrií, včetně středové souměrnosti.
Samotné obarvení je asymetrické i při globálním přejmenování tří barev.
To není rozpor: zadání požaduje souměrný **tvar**, nikoli souměrné
obarvení. Originál i draft byly vizuálně prohlédnuty a jejich všechny
maticové znaky se shodují.

Šest aktuálních/historických vrstev errat prohledáno, hashe stále shodné
s oficiálním stažením3.11.2026v05:37UTC. Odpovídající oprava nenalezena;
zachycená str.266 patří jiné větě, nikoli této úloze. Žádný nový nález,
žádná historická citace k dořešení, žádný vynechaný výčet. Ověření běželo
s nice15 a nepotřebovalo hledání sestav.

Reprodukce: `python3 check_cubes148.py`. Výsledky a závislosti:
`results/cubes148/checked.json`, `results/cubes148/errata-check.json`.
Dokončenou kontrolu není potřeba automaticky opakovat.
