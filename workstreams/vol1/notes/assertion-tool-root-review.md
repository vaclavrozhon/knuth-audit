# Převzetí obecného doplňování asercí, §1.2.1-14

Root 2. listopadu 2026 přebírá technickou část zmrazeného balíku
`parallel/induction-assertion-followup/`. Obecný program přijímá
graf celočíselného programu a doplňuje tvrzení o hodnotách proměnných
mezi dodanými asercemi. Původní zadání s. 20 skutečně žádá program
pro nějaký jazyk, který se o doplnění pokusí; nevyžaduje úplný
rozhodovací postup pro všechny algoritmy.

## Přímá kontrola implementace a důkazu

Root přečetl celý `assertion_tool.py`, definici jazyka a obecný
důkaz v `notes/language-and-soundness.md`, přepis Euclida,
`check_euclid_output.py` a podstatnou část samostatného konkrétního
interpretu v `check_tool.py`. Přímo zobrazeny původní s. 14–15 a 20;
obrázek 4 obsahuje právě A1–A6 použité při porovnání.

Jazyk zahrnuje neomezená celá čísla, přiřazení, současné přiřazení,
nedeterministickou volbu a dělení se zbytkem. **Řezové body** jsou
uzly s dodanými asercemi. Odstraněním těchto uzlů musí vzniknout
acyklický graf. Pak je mezi nimi konečně mnoho cest, které program
skutečně všechny projde. Chybějící tvrzení je sjednocením přesných
obrazů dodaných stavů pod jednotlivými cestami, vyjádřeným pomocí
existenciálních kvantifikátorů. Je to nejsilnější postpodmínka
**vzhledem k dodaným řezovým asercím**, nikoli výpočet přesné
dosažitelnosti od počátku celého programu.

Zkontrolovány rozhodující kroky důkazu a jejich implementace:

- Podmínky hran omezují stavy před sekvenčními příkazy; pravé
  strany současného přiřazení se počítají ve stejném starém stavu.
- `havoc` zavádí čerstvou libovolnou celočíselnou hodnotu.
- Dělení nejdříve vydá povinnost kladnosti dělitele. Až poté
  přidá definující rovnici a meze zbytku. Neplatné dělení se tedy
  neschová do prázdné množiny následných stavů.
- Dvě přidané identity pro největší společný dělitel jsou obecné
  důsledky `c=q*d+r`, nikoli zakódované Euclidovy aserce.
- Každé rozvětvení má zvláštní povinnost pokrytí stavů některou
  hranou. Neexistuje tiché vynechání nedosažitelnosti odhadnuté
  pomocí řešiče; i nesplnitelné cesty zůstanou ve výčtu.
- Při vstupu do dalšího řezového bodu se ověří jeho aserce.
  Indukce po těchto úsecích dokazuje částečnou správnost.
- Cyklus bez řezové aserce a vyčerpání limitu nevydají neúplné
  sjednocení jako platnou doplněnou aserci. Odpověď řešiče
  `unknown` ani model negace místní povinnosti nejsou úspěchem.

Neinterpretovaná funkce gcd v Z3 má více modelů než skutečný
matematický gcd. Proto nemožnost modelu negované povinnosti
postačuje k důkazu, ale nalezený abstraktní model nemusí být
skutečným protipříkladem. Výstup to výslovně uvádí. Důvěra
v obecný osvědčující běh zahrnuje správnost Z3 a překladu;
exporty SMT-LIB nejsou nezávisle zkontrolované důkazové certifikáty.

## Přesný požadovaný případ

`examples/euclid.json` obsahuje pouze A1, A4 a A6. A2, A3 a A5
nejsou vstupními asercemi. Nástroj je odvodil a následný oddělený
program prokázal všech šest implikací jejich ekvivalence s tiskem.
Root přečetl uložené výsledky, nikoli znovu spouštěl inferenci.

Obousměrná přesnost je navíc přímo patrná: E1 dává právě A2.
Každý stav splňující tištěnou A3 lze získat dělením z A6 se stejnými
koeficienty, c,d a libovolnými starými q,r. Nerovnosti `0<=r<d`
zajišťují d>0. První průchod z A2 přidává pouze podmnožinu,
protože A2 implikuje A6. Omezení r!=0 pak dává přesně A5.
Přepis E4 zachovává tištěné sekvenční pořadí a jeho invariant
plyne z `(a'-q*a)*m+(b'-q*b)*n=c-q*d=r`.

Uloženo 13/13 prokázaných Euclidových povinností, 6/6 následných
implikací a celkově 45 povinností osmi různých programů.
Samostatný konkrétní interpret nezávisle spočítal 2 226 stavů
a 1 655 svědků odvozených formulí; při vyhodnocení používá
skutečný matematický gcd, nikoli řešič. Dalších 122 sond ověřuje
obě inkluze ve dvou příkladech. Osm záporných kontrol zachycuje
konkrétní chybné chování nebo neúplnost, 12 chybných vstupních
struktur je odmítnuto. Oprava rezervovaných názvů má samostatný
záznam 49 odmítnutých jmen a 107 načtených exportů.

Obecný nástroj automaticky neprokazuje ukončení; to není zaměněno
za částečnou správnost. Euclidovo ukončení je už dříve dokázáno
v `notes/induction.md`. Technická mezera úlohy 14 je uzavřena
pro výslovně vymezený jazyk a knižní příklad. Nejde o nový nález
chyby TAOCP.

## Přesné pramenné meze

Přímo přečteny agentovy obrazy titulního listu IFIP a obsahu
vii–viii: konference Ljubljana 23.–28. srpna 1971, kniha
North-Holland 1972. Floydův příspěvek začíná na s. 7, Kingův
na s. 234. Obsah dokládá názvy a počáteční stránky, nikoli obsah
článků nebo automaticky jejich poslední stranu.

Root dále přímo přečetl položky původní Stanfordovy bibliografie
na s. 25 a B-10: Floyd, AIM-150, STAN-CS-71-235, září 1971,
12 stran. Varianta „Iterative“ na s. 25 se liší od „Interactive“
na B-10; není chybou TAOCP. Samotný report nebyl získán. Soubor
`king1969-thesis.pdf` obsahuje pouze titul disertace z roku 1969;
root jeho jedinou stránku také zobrazil. Není to obsah disertace
ani odkazovaný IFIP článek.

Plné původní texty Floyda a Kinga zůstávají **partial**. Proto
se celá úloha 14, ani složená historická položka X0029, nepřevádí
na checked. Agent prohledal všechny čtyři vrstvy errat V1;
známá oprava relevantních výstupních šipek X0026 je zahrnuta,
nikoli hlášena znovu. Root četl odpovídající výtah a přesný rozsah
v `notes/sources-and-errata.md` zmrazeného balíku.

## Integrita předání

Jednou ověřeno všech **200 souborů, 43 049 042 bajtů**, a všech
18 vnějších vstupů. Všechny délky a SHA-256 souhlasily.
Hash `MANIFEST.json` je
`2e627289c295ece58d4b6a257e1abb63ef12f421f54cf222a570f94358882311`.
Zmrazené soubory zůstaly nezměněny. Wheel Z3 je součástí předání;
rozbalená reprodukovatelná cache vendor je ignorována. Při převzetí
nebyly opakovány úspěšné matematické testy ani původní
`check_induction.py`. Kořenový manifest zachycuje samostatně
tuto recenzi a přesný přijatý balík.
