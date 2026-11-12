# Úloha172: zdrojový průchod a nové doplnění

3. listopadu2026. Celé zadání145–146 a odpověď464–466 přečteny
v původním PDF i draftu81–82/168–170, spolu s relevantními erraty.
**Matematické výsledky pro8×8 zůstávají přijaté. Celá úloha je partial**:
zbývají historické originály a výslovná hranice obecného střelcového
vzorce. Nejde o opětovné zpochybnění dokončených výpočtů.

Nové: [F140](F140_KAUTZ_ERRATUM.md), drobná chyba koncového čísla
stránky v erratech2026; [C036](C036_BISHOP_BOUNDARY.md), otázka
chybějícího n≥4. Žádný nový velký výčet ani emailový návrh.

## Obrázky a přijaté výsledky

`check_snakes172_sources.py` přímo dekóduje souřadnice glyfů a mřížek
z PDF trace. Všech **16 desek /305 figur** v každé verzi souhlasí.
Patnáct výsledkových desek je indukovanou cestou či cyklem a každá
nevěžová patří modulo D4 mezi již přijaté svědky. Čtyři věžové
obrázky jsou přímo geometricky validovány. Staré úplné výčty,
nezávislá validace a Burnsideovy počty zůstávají beze změny.

| Strana | Obrázky zleva | Ověřeno |
|---|---|---|
|145|4×4 králové|7figur netvoří cestu; odstranění jediného obsazeného rohu ji vytvoří|
|464|král, jezdec, střelec, věž, dáma|cesty mají32,32,13,15,12 polí|
|465 nahoře|jezdec, věž, věž, dáma, dáma|cesty34,15,15,13,13 polí; obě dámské třídy různé|
|465 dole|král, jezdec, střelec, věž, dáma|cykly31,32,12,16,13 polí|

Králova cesta na464 má konce v sousedních rozích. Dámská **obsazuje**
protější rohy, ale druhý roh není krajním bodem. Kontrola původně
chybně předpokládala protilehlé královy konce a oba dámské rohy jako
konce; před přijetím byla tato chybná lokální podmínka opravena podle
obrázku a textu. Nešlo o chybu knihy ani o změnu starého enumerátoru.
Jezdcový cyklus má půlotáčkovou symetrii; věžový je invariantní vůči
oběma diagonálám, ne vodorovnému/svislému zrcadlení, jak opravuje E010.

## MCC převod a délka vstupu

Každý primární !v volí jedinou možnost. Její barva v:0/1 určuje,
zda vrchol patří do vybrané množiny, a barevné položky sousedů
jednoznačně vynucují odpovídající stupně. U cyklů jsou vybrané
vrcholy stupně2. U cest je start vynuceně vybrán a má stupeň1;
jediná položka E určí druhý konec stupně1. Ostatní vybrané vrcholy
mají stupeň2. Odebrání nesouvislých výsledků dává přesně požadované
objekty. Obráceně každý takový objekt určí jednu možnost pro každý
!v, takže převod žádný neztratí ani neduplikuje při pevném startu.

Zákaz druhého konce vedle startu je bezpečný pro hledané dlouhé
cesty; obecně by vyřadil cestu délky1. Oprava2023 výslovně odstraňuje
prázdnou startovní možnost. Vynechání sousední dvojice vybraných
sousedů vyloučí trojúhelník a je bezpečné pro tyto cesty a cykly
délky≥4, nikoli pro obecné hledání všech třícyklů.

Nový `check_snakes172_counts.py` pouze spočítal možnosti dámského
vstupu, bez řešení MCC. Starý vstup má16788 možností a454380 uzlů;
po vyřazení6366 trojúhelníkových možností10422 a281934. Délka zde
počítá i jeden spacer na možnost. V obou součtech je start vynucen;
přidání jeho prázdné možnosti by původní počet16788 porušilo.

## Obecná matematika

Nový [střelcový důkaz](BISHOP172_PROOF.md) převádí graf na incidence
diagonál. Pro sudá n≥4 dokazuje maximum2n−4, nutný rohový konec
a přesný počet2^(n−3) tříd. Pro cykly dává horní mez2n−4.
Kandidát C036 se týká pouze chybějícího omezení pro n=2.

Králova horní mez plyne z rozdělení na2×2: tři králové v jedné
čtveřici tvoří trojúhelník. Na8×8 proto cesta nemá více než32 polí.
Konkrétní svědci a dřívější úplné výčty uzavírají zbývající konečná
maxima. Obecné věžové formule, pevné body a dvojnásobné ukotvení
byly již dokázány v `CHESS_SNAKES_NOTES.md`; nepočítaly se znovu.

Beluhovův [primární článek](https://ecajournal.haifa.ac.il/Volume2023/ECA2023_S2A16.pdf)
má správnou citaci ECA3:2(2023),S2R16,1–23. Věta1.1 a výklad na2
dávají královské počty2n nebo2n+1 podle parity n/2; věta7.1 na19
dává šest maximálních cyklů při n≥8 dělitelném4. Věta1.3 potvrzuje
jezdcovou asymptotiku, věta5.1 vztah lichého případu ke skládání
známek. Článek sám uvádí vznik výsledků2018. Zde byla ověřena
shoda citovaných tvrzení a mezí, nikoli nezávisle celý23stránkový
důkaz nebo jeho počítačová část. Zápis +O oproti −O při běžné
oboustranné konvenci sám není protipříkladem.

## Errata, historie a přesné mezery

E010 sdružuje známé opravy2023. Naše PDF a draft jsou stále původní:
opravy jsme uplatnili v ověřovaném modelu, nikoli v souborech knihy.
Starý text E010 i celá anglická karta jsou archivovány. Paginace
Kautze z2026 má nový samostatný problém F140; není vydávána za
ověřenou správnou opravu v E010.

Zbývá získat originály Dawson1930/1931, Verbeek1971 a Torbijn;
doložit přesný pořad/attributaci olympiády2008; přečíst Kautz1958
pro tvrzení o zavedení názvu. Metadata vydavatele postačují pro
F140 o stránkách, ale nikoli pro obsah a prvenství termínu.
U citace *Cubism For Fun*17(1991),19 je navíc podezřelé spojení čísla
a roku: [dobový čtenářský záznam](https://www.math.rwth-aachen.de/~Martin.Schoenert/Cube-Lovers/Peter_Beck__cff__19.html)
z prosince1988 už popisuje číslo19. Přesný správný údaj pro Torbijna
zatím chybí, proto nejde o nový potvrzený nález. Veřejný archiv
vydavatele hledaný článek nevystavil; členství se neobcházelo.
Samostatný model14dam s blokováním útoků ještě nebyl převzat z
původního článku ani ověřen. Je odlišný od indukovaného grafu na
prázdné šachovnici; přijatých pět13cyklů jej neověřuje.

Na pokyn uživatele se výslovně nereplikují historické mems:
král6T→270G a3.7T→166G, obecné maximum6.3T→170G; jezdec58G/43G;
střelec13M→54M; věž625G→365G; dáma17G→9.4G. Také se znovu
negeneruje21488110 věžových nesouvislých výsledků. Tyto nákladové
a vedlejší výčetní údaje nejsou nezávisle ověřené. Výslovné vynechání
neuzavírá právě popsané historické mezery nebo C036.

Kontrola procesů12:57UTC: všech11 vlastních dlouhých běhů a jejich
29 procesů mělo nice15. Žádná nová dlouhá fronta nebyla přidána.
Další sekvenční blok je173–174, s převzetím již existující evidence.
