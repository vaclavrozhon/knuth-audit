# DLX153 — doplnění původních zdrojů, 3. listopadu 2026

Matematická část je hotová bez nového nálezu. Starší úplné výsledky se
neopakují. Úloha zůstává **partial** kvůli původním údajům o vzniku a vydání
Line Puzzles a autorově poznámce o prvních1000 náhodných pokusech.

## Původní kresby a dřívější výčty

`extract_path153.py` přečetl všech8 dílků zadání na str.144 a všech8 dílků
v každém ze dvou obrázků na str.460, samostatně v PDF a draftu2019.
Vektorová data určují konce jednotlivých podcest; křížení není rozcestí.
Krátká spojnice k terminálu vede od hrany o0.2 šířky pole dovnitř a končí
uprostřed jeho kruhové značky. Kontrola zahrnuje i obě značky každého
obrázku. Všech24 dílků v každé verzi souhlasí se starším přepisem.

**Pravý** obrázek odpovídá(a), **levý** odpovídá(c). Pravý má přesně
inventář zadání; levý obsahuje čtyři dvoucestná domina. V obou jsou dva
terminály a čtyři prázdná pole. Původní dvakrát spočítané množiny mají
po dvou řešeních, navzájem souvisejících půlotáčkou celé desky. Proto je
jednoznačnost až na tuto symetrii správná. Nová kontrola validovala uložené
čtyři modely, jejich souvislost a shodu s původními kresbami.

Starý SAT výčet i původníDLX2 skončily s počtem2 pro(a) i(c); terminální
výstupy, vstupy a modely zůstávají archivované v `results/path_dominoes/`.
Nebylo znovu voláno žádné hledání. Záznam `question_inventory_matches:false`
u starého153c znamená, že(c) úmyslně používá jinou sadu než(a); není to
neúspěšná validace ani chyba knihy.

## Počty a model

Pro(b) vybíráme tři ze šesti připojovacích bodů a jeden z nich určíme
jako terminál. Půlotáčka nemůže zachovat lichou trojici, protože její
bodové orbity mají velikost2. Dostáváme `C(6,3)*3/2 = 30` různých typů,
tedy tři pro každý z10 typů trojice.

Osm domin zabírá16 polí. V desce4×5 zbývají právě4, takže prázdný monomino
má násobnost4. Staré XCC kódování tento počet vynucuje plochou; knižní
AlgorithmM jej může zadat výslovně. Typové položky a pokrytí polí volí
jednotlivé dílky, barevná rozhraní spojují všechny přítomné konce.
Ještě je třeba hlídat jedinou cestu mezi terminály; všechny uložené modely
ji mají a žádná vedlejší smyčka se v úplných výčtech nevyskytla.

Část(c) požaduje dva obyčejné jednocestné kusy, dva terminální kusy
s jednou podcestou a čtyři dvoucestné kusy. Vytištěný příklad toto rozdělení
přesně splňuje. Samotný úspěšný příklad neověřuje statistiku náhodných
výběrů ani autorovu konkrétní posloupnost prvních1000 pokusů.

## Historie a errata

Šest relevantních vrstev errat nemá odpovídající opravu153; hashe jsou
stejné jako při dnešním ověřeném stažení. Blízké opravy str.460/fasciklu268
patří sousedním úlohám154 a156. Žádný nový nález ani nové známé erratum.

Indexovaný text [Peggova popisu](https://www.mathpuzzle.com/dominopat.html)
připisuje Line Puzzles Billu Darrahovi. Plné otevření ale vrátilo ověřovací
bránu, takže nemáme zobrazený původní dokument s datováním.
[Sběratelská stránka](https://www.robspuzzlepage.com/pattern.htm) uvádí
Golf Line od Binary Arts, ale rok v popisku a alternativním textu obrázku
se liší; nelze z toho odvodit chybu knižního údaje. Veřejný katalog Indiana
University rovněž vrátil jen ověřovací stránku. Brány nebyly obcházeny,
žádné zprávy nebyly odeslány.

Otevřené zůstávají přesné původní podklady pro vydání1994/1999 a anekdotu
o prvních1000 pokusech. Toto není matematická mezera ani důvod k opakování
hotových hledání. Následuje154, jehož starší Pellův důkaz je už v repozitáři.
