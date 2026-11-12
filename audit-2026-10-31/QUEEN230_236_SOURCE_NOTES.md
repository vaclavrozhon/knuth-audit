# Úlohy 230, 232–236 — celý zdrojový průchod dam

Kontrola 3. listopadu 2026 navazuje na [přijaté výsledky n=16](QUEEN_COST_NOTES.md).
Staré výčty, optimalizace, intervalové certifikáty ani validace jejich modelů
se neopakovaly. Nové kontroly běžely s nice 15: extrakce obrázků a konstrukce
překlopení 1,83 s, aritmetické a zdrojové kontroly 0,029 s.
Úloha **231 zůstává samostatným následujícím blokem**.

## Zdroje a nové F147

Přečten hlavní text 112 a první odstavec 113, otázky na 152 a odpovědi
476–478 v knize i autorově draftu. Převod hlavního textu do draftu je −64
stran, odpovědí −296 stran; PDF přidává 20, respektive 6 stran.
Seznam skutečně zobrazených stránek, výřezů, známých rozdílů a hashů je v
[source-observations.json](sources/queen230_236/source-observations.json).

Ve všech 13 diagramech obou zdrojů jsme získali shodné souřadnice,
celkem **389 vytištěných dam na verzi**. Sedm dříve přijatých diagramů n=16
se přesně shoduje se starými souřadnicemi. Nově byly úplně zkontrolovány
diagramy n=17, 18, 19, 32, 64 a 128. Poslední má jen 127 dam: **F147**,
chybí pole (128, 65). Oba zvětšené dolní okraje byly přímo zobrazeny.
[Důkaz a přesná oprava](F147_MISSING_QUEEN128.md).

U n=64 je šest nezávisle překlápěných čtverců, u **opraveného** n=128 dvanáct.
Jejich řádkové i sloupcové podpory jsou disjunktní. Každé překlopení zachová
množiny obou diagonál a multiset vzdáleností; všechny kombinace proto zůstanou
neútočné a mají stejné ceny. Přímo bylo sestaveno a ověřeno všech 64 a 4096
různých variant. Kontrola nezahrnuje hledání globálního optima.

Technické chyby při vývoji extraktoru jsou zaznamenány odděleně od knihy:
pevný malý okraj nezachytil posunutý počátek některých PDF znaků, další
okraj minul spodní dámu n=64 a globální zaokrouhlení svislých souřadnic
nesprávně seřadilo tři malé draftové diagramy. Konečný parser používá skutečné
mřížky, kontrolované relativní tolerance a vodorovné pásy. Všechny souřadnice
pak souhlasí mezi verzemi; chybějící poslední dáma n=128 zůstala stejná
ve všech pokusech a je navíc viditelná přímo ve zdroji.

## Důkazy a údaje jednotlivých úloh

**230.** Všechna řešení mají d možností. Pro C alespoň tak velké jako nejvyšší
cena je každá doplňková cena nezáporná a celková cena je dC minus původní
součet. Minimalizace doplňku je tedy přesně maximalizace původní ceny.
Předpoklad pevného d je v odpovědi výslovně uvedený.

**232.** Dolní celá část každé ceny má chybu v intervalu [0,1), takže u 16
dam je celková chyba menší než 16. Rozdíl celočíselných cen větší než 16
proto zaručuje i správné pořadí původních reálných součtů. Přijatá data
potvrzují 96 řešení s cenou 84, zatímco obrázek 74(a) má celočíselnou cenu
86. Škálování floor(2^32 d), K=9, osm optim a mezera k devátému řešení
jsou ve starém přesném certifikátu. Mezi maximálními obrázky 74(b,c) se
mění jen prostředních osm řádků, sloupce c se zobrazují na 17−c.

**233.** Logaritmus převádí součin kladných vzdáleností na součet.
Samotné ln d je ve čtyřech středových polích záporné. Starý audit již
výslovně používá posun ln(sqrt(2)d), který pro pevný počet dam pořadí
nemění a dává nezáporné ceny pro DLX5. Tuto již evidovanou normalizaci
nepočítáme jako další nález. Přesné celočíselné součiny a oba nezávislé
výsledky optimalizace zůstávají přijaté.

**234.** Pro libovolnou permutaci q a c=(n+1)/2 je

    Σ[(r−c)² + (q[r]−c)²] = 2Σ(r−c)² = n(n²−1)/6.

Obecný důkaz používá jen to, že q permutuje 1,…,n; platí i pro věže.
Pro n=16 dává 680 a vysvětluje výjimku N=2 ve F076.

**235.** Definujeme w=4d². Cena 4d⁴ je přesně w²/4. Tři vytištěné
obrázky dávají 127760, 127760, 187760; první dva mají různé multisety
vzdáleností, jak odpověď uvádí. Přijatý výčet má 16 minimálních rozmístění
ve čtyřech třídách a osm maximálních v jedné třídě. Proto K=17 a K=9
postačují k získání následující, odlišné ceny. Starý draft má v otázce
jiné škálování; jde o známé E104, nikoli novou chybu.

**236.** Pro konečně mnoho kladných cen uspořádaných sestupně rozhodne při
N→∞ nejvyšší cenová hladina, na které se liší jejich násobnosti. Její
příspěvek nakonec převáží konečný součet všech nižších hladin. Správný
postup tedy postupně minimalizuje a fixuje počty na hladinách (Algorithm M).
Fixovat jednotlivé možnosti v libovolném pořadí nestačí. Čtyřřádkový
protipříklad z knihy má přesně dvě pokrytí: náklady 3^N+2^N a 3^N+1.
Přímá kontrola všech 16 podmnožin potvrzuje uvedené selhání ostrého minimaxu.

F075 a F076 mají nyní také [krátký samostatný verifier](verify_f075_f076.py).
První cena N=20 je přesně 130230066663839627189/64, druhá
130915446232517223025/64. Vytištěná zaokrouhlená čísla odpovídají
1024násobku těchto hodnot. Při N=2 jsou všechna rozmístění optimální.
Starý úplný certifikát kladných celých exponentů, včetně hranice 21 a
obecné meze 16·113^80 < 117^80 od 160, zůstává přijatý bez přepočtu.
Obecné tvrzení o reálných exponentech z tohoto certifikátu nevyvozujeme.

## Primární článek a známá errata

Fischetti–Salvagnin, [arXiv:1907.08246v1](https://arxiv.org/abs/1907.08246),
oddíl 5, používá postup po hladinách hodnot 4d². Příloha potvrzuje stejné
multisety pro n=32 a 64 a přesně stejnou permutaci pro opravené n=128.
Reference 18 uvádí Knuthovu soukromou komunikaci v červnu 2018. Listopad
2017 u jiné reference se týká lexikografického problému, nikoli této úlohy.
Záznam [history-search.json](sources/queen230_236/history-search.json)
odlišuje již archivovanou verzi od delšího aktuálního PDF na autorově webu.
Výrok o odpoledním výpočtu n=47 není přesně doložený benchmark.

Šest vrstev errat bylo prohledáno včetně přepočtu stránek:

- **E103, 23. 12. 2021:** vykřičník po větě o obou Σ za (108). Kniha 112
  má opravu, draft 48 má původní tečku.
- **E104, 18. 10. 2020:** d⁴ → 4d⁴ v otázce 235. Kniha 152 opravená,
  draft 88 původní.
- **E105, 18. 10. 2020:** nahrazení chybné odpovědi 232. Kniha 476 má
  96 řešení s cenou 84 a vysvětlení zaokrouhlení; draft 180 má původní
  nesprávné tvrzení o shodných optimech a cenách 182/202.

Odpovídající opravy F075, F076 ani F147 nebyly nalezeny. Nejde o tvrzení
prvenství; fyzický výtisk a celá poslední digitální verze zůstávají neověřené.

## Přesně vynechané náročné reprodukce

Na pokyn uživatele z 3. listopadu se tyto údaje nezaměňují za nezávisle
ověřené výsledky (`verified:false`):

- Globální optimalita velkých diagramů n=17,18,19,32,64,128. Geometrie je
  prověřená, n=128 je opraveno; článek je doložením zdroje, nikoli naším
  nezávislým důkazem globálního optima.
- Historické náklady hlavního textu: úplný výčet n=16 za 40 Gμ, minima a
  maxima za 3,7/0,8 Gμ; 233 za 1,2+0,2 Gμ; 235 za 1,3/9,7 Gμ.
  Matematické výsledky n=16 mají již přijaté nezávislé důkazy.
- Přesný historický výkon „n=47 za jedno odpoledne“. Neprovádí se nová
  dlouhá optimalizace ani rekonstrukce tehdejšího hardware/programu.

Věta, že rotační symetrie zřejmě nastává jen pro n=1,4,5,16,32, je v knize
výslovně domněnka. Zkontrolováno je znění a symetrie vytištěných příkladů;
domněnka pro všechna n nebyla dokázána. Výzkumnou výzvu určit co nejvíce n
neoznačujeme za vyřešený nekonečný problém.

Úlohy 230 a 232–236 mají dokončený zdrojový průchod s těmito výslovnými
mezemi. Další je 231 (slova a ceny), potom 237–238 a prvočíselné čtverce
na hlavních stranách 113–114. Ostatní starší mezery zůstávají otevřené.
