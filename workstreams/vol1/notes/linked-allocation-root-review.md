# §2.2.3: převzetí a nezávislá revize

Koordinátor 1. listopadu 2026 převzal zmrazenou složku
`parallel/linked-allocation/`. Přečetl všech osm obecných důkazových
poznámek, zprávu, stavy jednotlivých jednotek a přesný rozsah pramenů.
Původní stránky obou nálezů byly samostatně zobrazeny při jejich
potvrzení; znovu byly zobrazeny s.269–270 pro opravu OCR inventáře.
Podagent prohlédl celý přidělený originál, s.254–273 a odpovědi545–551.
Netvrdíme, že koordinátor podruhé prohlédl všechny tyto stránky.

Inventář má 30 původních úloh, bez přidaného čísla. Náhrada úlohy30
z roku2021 je druhou verzí stejné úlohy. Původní obtížnosti úloh10,
13 a14 jsou M21, M48 a M21; novější zadání13 má HM48. Úloha25 nemá
tištěnou odpověď.

## Důkazy podstatné pro převzetí

Invarianty fondu volných uzlů a fronty zahrnují prázdný stav, poslední
odebraný uzel, znaménka registrů a obnovu volajícího. Kontrola návěští
OVERFLOW odlišuje návrat na rJ−2 od běžného návratu; nula v programu
alokace podprogramů se posuzuje po známé opravě z roku2008.

Topologické třídění udržuje přesný počet zbývajících vstupních hran.
Znovupoužití COUNT jako QLINK nastává až při nulovém počtu, takže
se nepřepíše potřebná informace. Duplicity se odečítají stejně často,
jako byly započteny. Přesunutí T7 před T6 selže už pro hranu1→2.
Časová konvence knihy zahrnuje vydání I/O, vynechává čekání JBUS
a závěrečný HLT; při této konvenci se vzorec shoduje s instrukcemi.

U Booleovy mřížky koordinátor zkontroloval zejména konstanty v důkazu
Brightwellovy–Tetaliho meze: převod nerovností podmíněné entropie
mezi dvěma pravidelnými vrstvami, exponenty stupňů v rekurenci,
limitní přechod od uspořádání do řetězce k lineárním rozšířením
a volbu parametru. Výsledná mez skutečně nemá vnější exp. Zkontrolován
je také přechod od součinu faktoriálů vrstev k ostré logaritmické
asymptotice včetně konstanty −3/2. Chybný zbytek ve starší opravě2001
je již odstraněn odpovědí2018 a není dalším novým nálezem.

Pro externí třídění byla zkontrolována obecná konstrukce s max-plus
násobením: součin nahradí násobení sčítáním a sčítání maximem, a tak
počítá délky nejdelších omezených procházek. Nuly na diagonále
umožňují doplnit kratší cesty. Po zdvojení mezní délky nad n zachytí
kladná diagonála cyklus; bez cyklu určují délky pořadí. Konstrukce
má výslovně velké pracovní soubory O(n^3+m), nepředstírá optimálnost.

Herní důkaz rozlišuje výherní, proherní a remízové stavy a přiděluje
výherním tahům klesající celočíselný rank. Pouhý tah do proherního
stavu může bez této volby opakovat cyklus; klesající rank dává
skutečnou konečnou vítěznou strategii. Pro režim s prohrou při
opakování se ukládá historie, nikoli pouze aktuální pozice.

## Výpočty a zachované meze

Převzaty byly úspěšné výsledky 4494 kontrol programů, 448 skutečných
MIX běhů třídění a diagnostiky, 160 alokačních případů, všech52
pořadí příkladu, počtů Booleovy mřížky pro n=0,…,5, 190 případů
páskového modelu a nezávisle certifikovaných 2640 herních stavů.
Již úspěšné testy nebyly bez důvodu opakovány. Čísla pro n=6,7 jsou
ověřena proti primární publikaci, nikoli novým výpočtem zde.

V1-C0036 a V1-C0040 jsou již potvrzeny a zůstávají dvěma nálezy.
Matematika všech30 úloh je dokončena v uvedeném rozsahu; úlohy13
a28 mají celkový stav partial kvůli pramenům. Otevřené zdroje jsou
přesně Kahn1962, Sha–Kleitman1987, Winning Ways3 kap.21 a starší
Sierpiński1928 s.158. Jejich obsah ani absolutní historické prvenství
nejsou potvrzeny dostupnými metadaty. Hlavní text proto také zůstává
partial. Přesné URL, čtené rozsahy a hashe jsou v SOURCE_STATUS.json.
