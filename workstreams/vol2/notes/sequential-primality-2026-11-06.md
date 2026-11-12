# §4.5.4 — souvislé argumenty: tabulka prvočísel a závěrečné testy

6. listopadu 2026, V2-X0148. Hlavní text od nadpisu The largest
known primes na 407 po historický odstavec na 412. Zadání 413–414,
odpovědi 660–664; původní sazba byla vizuálně přečtena a při tomto
párování znovu porovnána s textovým přepisem. Párovány celé úlohy
15, 16, 19, 20, 23, 24, 25, 26 a 27. Šest je uzavřeno v níže
uvedeném rozsahu, tři zůstávají partial. Jednotlivé číselné položky
i argumenty mají záznam v results/sequential-primality-evidence.json.

Žádný nový ověřovací běh ani nález. Dříve uzavřené důkazy,
certifikáty, malé protipříklady a záznamy zdrojů se přebírají.
Přesné historické hranice nejsou zaměněny za současný stav.

## Tabulka 408 a Mersennovy seznamy

`prime-table.md` dokládá všech 46 řádků a všech 460 prvočísel,
nikoli jen první sloupec. Základní Lucasovo kritérium, úplná
faktorizace n−1 a kontrola řádů dávají vlastní důkaz každého
prvočísla. První sloupec a horní mezery mají dřívější certifikáty
z `primitive-polynomials.md`; dalších 414 položek používá
1173 nových certifikačních vazeb a 10202 svědků složenosti
pro mezery mezi uvedenými čísly. Výsledky už byly zkontrolovány;
teď se jen připojuje přesná adresa řádku a buňky. Tím je uzavřeno
i tvrzení, že jde právě o deset největších prvočísel pod každým N.

`mersenne-context.md` obsahuje 52 opravených exponentů a počtů
číslic. Prvočíselnost exponentu je oddělená od prvočíselnosti
celého M_p. U 23 hodnot do p=11213 se přebírá vlastní Lucasův–
Lehmerův důkaz a uložené výpočty; vyšší hodnoty mají primární
externí zprávy GIMPS, nikoli nové místní miliony čtvercování.
Počty číslic mají vlastní racionální intervalový důkaz.
Složenost M8191 má konkrétní vlastní dělitel 338193759479.

C0162 mění pouze rok M216091 z 1984 na 1985. C0163 je nový
chybný exponent uvnitř errata: 77232017=19·29·140167, správně
77232917. Není to známá opravená chyba. C0164 zůstává candidate:
primární zdroje se rozcházejí v dubnovém a červnovém datu,
takže se nedá mechanicky přepsat datum v knize podle katalogu.
Tyto dva nálezy v dodatcích nemají uměle přiřazenou červenou
stranu původní knihy, na níž se jejich znění nevyskytuje.

Snapshot milníků GIMPS je z 3. listopadu 2026. Knižní milionová
hranice 1997 má dobový newsletter, údaj pod 80 miliony má
archivovaný milník 2026. Přesný mezistav 70832851 k 10. prosinci
2024 nebyl rekonstruován. Přesný 12. duben u M1257787 také není
samostatně doložen; dubnový objev a zářijové oznámení se ovšem
nevylučují. Podmíněný historický čas není nový benchmark.

## Lucasův test, věta L a faktorizace p±1

`primality-lucas.md`, §1–5, dává samostatné argumenty všech
identit (27)–(38), maticové vyhodnocení za O(log n), existenci
a dělitelnost nejmenšího indexu, zvedání na prvočíselné mocniny
včetně p=2,3 a obecný důkaz celé úlohy 15. Nezbytkový případ
kvadratické algebry se nesměšuje s rozloženým případem.
Zvlášť je uzavřen kratší důkaz věty L i každý krok tištěného
delšího důkazu včetně vyloučení dvou prvočinitelů.

Výjimka C0160 je jen v doprovodném předtestu na 660:
N=5,Q=−1 dává |QD|=N a prvočíslo, které text nesprávně odmítá.
Přesná podmínka nálezu složenosti je 1<gcd(N,QD)<N; zahrnuje
i degeneraci QD=0. Hlavní Lucasovo kritérium zůstává platné.

`factoring-pminusplus.md` dokládá obě celé úlohy 19–20:
dělitelnost, obě fáze, modulární provedení, dávky a účinné
doplnění s náhodnou bází či parametrem. Vysoká pravděpodobnost
se opírá o vlastní obecný důkaz pro doplněný postup, nikoli
o přejmenování výsledku gcd=N na faktor. U p−1 se kontrolují
i dvojkové mezistupně, u p+1 normová grupa Lucasových kořenů.

C0161 zůstává praktická chyba předepsané pevné báze: pro
knižní 2^214+1 i zbytek n6 mají oba dotčené prvočinitele stejný
řád báze 2, totiž 428. Proto změna exponentu při zachování
báze 2 nedá vlastní faktor. Ověřená báze 3 jej oddělí.
Správná sazba 33≤r≤3334 obsahuje oba konce; opačný OCR přepis
není nález. Obecné pravděpodobnostní doplnění není připisováno
stručné původní odpovědi.

## Jacobi, pevné báze, explicitní formule a Proth

`primality-jacobi.md` obsahuje vlastní důkazy všech částí 23,
Monierova vzorce i podmínky chyby větší než čtvrtina. Prvočíselná
reciprocita je vstup výslovně dovolený zadáním. Je uveden invariant
algoritmu a konvence J(a,1)=1; jejich potřeba nevytváří novou kartu.
Bibliografická C0129 na 662 je druhý výskyt téže chyby z 341.

`primality-deterministic.md` uzavírá konečný neuniformní seznam
v 24 a jednu rostoucí nekonečnou posloupnost s kvadratickým počtem
testů. C0156 opravuje mezikrok 6≤21/4 pro n=9,N=12, závěrečná
věta je platná. Výzkumný dodatek s jedinou posloupností a O(log n)
testy nemá zde řešení, proto je celá aktualizovaná 24 partial.
Úloha 26 má plný řádový důkaz i pro tištěnou mez r≤f+1.

`riemann-explicit.md` přesně převádí von Mangoldtovu párovanou
formuli a dokazuje obě opravy 25. Analytická věta o této formuli
a Landauova věta o součtu x^rho jsou pojmenované externí vstupy;
jejich celé původní důkazy zde nejsou nezávisle rekonstruovány.
Vlastní odvození dává reálnou část uvnitř limitního procesu,
správný půlskok, omezený zbytek, všech 40 číslic konstanty a
logaritmickou divergenci nepárované imaginární části pro x=p^k.
C0179 tedy není jen volba zápisu. C0180 opravuje přesný zbytek;
samotný neurčený člen O(1) znaménkem půlskoku vyvrácen není.

Hlavní úloha 27 pro 5·2^n+1, obecný Prothův důkaz a rychlá
redukce mají úplné argumenty. C0157 je pouze vynechaná výjimka 3.
Všech 57 konkrétních prvočísel má uložené vlastní certifikáty;
úplnost obou seznamů do 300000 je výslovně externí výsledek
ProthSearch, porovnaný se snapshotem z 18. července 2026.
Známý doplněný exponent 54792 nevytváří kartu.

Celou 27 nyní ponecháváme partial kvůli rozsahu dodatku na 663:
hledání Jacobiho nezbytku v předem omezeném jednoslovním rozsahu
nemá obecnou záruku v našem důkazu. Nulový Jacobiho symbol musí
vyřídit gcd větev; pro N=49 by pouhé čekání na symbol −1 neskončilo.
Konkrétní svědci uvedených 57 čísel tuto obecnou záruku nedokazují.
Nejde o vyvrácení hlavního testu pro k=5 ani o nový potvrzený nález.

## Zbývající historické a výzkumné meze

Úloha 16 je partial: nekonečnost ani konečnost Mersennových
prvočísel není vyřešena. Primární článek Pomerance 2025 dokládá
stav uvedený ve svém úvodu, nikoli úplnou rešerši veškeré pozdější
literatury. Dřívější označení checked popisovalo rešerši a je
pro požadovanou hloubku nahrazeno přesnějším stavem.

`prime-history.md` dokládá Mersennův původní §XIX, geometrickou
faktorizaci, kontext dokonalých čísel a Powersovy zprávy 1911/1914.
C0186 opravuje celé století místo všeho času. C0187 na 412
zůstává pouze candidate; abstrakt Picuttiho není plný originál.
Přesné starší události a nepřerušená řada světových rekordů
nejsou kompletně rekonstruovány. Nedostupné listy Eulerova,
Pervušinova, Kraitchikova a Williamsova pramene i další citace
mají explicitní skip; matematika na nich nezávisí.

Další blok: zbývající úlohy 38–43,45–46 na 415–417 a odpovědi
665–671. U BBS43 se vrátit k dopřednému odkazu z původní strany36.
Celkem je nyní spárováno 39 ze 47 úloh oddílu; nejsou tím
uzavřeny jeho výzkumné otázky ani starší kandidáti.
