# §4.5.2 — gcd, algoritmy a jednotlivé argumenty

6. listopadu 2026, V2-X0143. Přečten původní text 333–356 a
odpovědi 640–647. Mapa jednotlivých rovnic, algoritmů, tvrzení
a všech 42 úloh je v `results/sequential-gcd-evidence.json`.
Přebírají se uzavřené důkazy a výpočty; nic se znovu nespouštělo.

Základní algebra, Eukleidovy algoritmy E/A, binární B, rozšíření
C/X, tabulky a přesné ceny MIX mají argumenty v `gcd-basic.md`.
Lehmer L má invariant sevřených poměrů, důkaz všech slovních mezí
včetně dočasných součinů a ukončení. Celočíselné soustavy mají
bijektivní změny proměnných a klesající lexikografickou míru;
viz `gcd-extensions.md`. Harris, dávkování, Penk a Brent–Kung
mají samostatné důkazy v `gcd-extremal.md` a `gcd-variants.md`.

Věta D a rozdělení gcd jsou přesné limity konečných rovnoměrných
modelů, nikoli rovnoměrná pravděpodobnost na všech celých číslech.
`gcd-probability.md` uzavírá i dopředný odkaz z §4.5.1 na 61 %.
`gcd-bins.md` dokládá celý jednorázový přechodový počet, pevný
menší operand i váhy 11/27 a 5/27. Poslední dvě úlohy mají vlastní
algebraické důkazy v `gcd-arithmetic.md`.

Spojitý Brentův model je odlišen od konečných celočíselných vstupů.
Rozvoje, rezidua a jejich konvergence jsou v `gcd-model.md` a
`gcd-second.md`; přechody v hlavním textu v `gcd-text.md`.
Odvození z rozkladů (41)/(42) jsou podmíněna právě jejich výslovně
předpokládanou existencí a dovoleným přeskupením. Empirické fits
(62)/(65) nejsou důkazy konstantních zbytků O(1). Uložená numerika
potvrzuje nižší přesnost konstant, nikoli všech 40 vytištěných číslic.
Původní milionové pokusy nemají dostupný přesný soubor vstupů.

Morrisovy existence a spektrální/asymptotické věty se přebírají
jako označené externí vstupy s přesným modelem. Vlastní přepočet
normalizace, vedoucích konstant a pokračování G do pravé poloroviny
je v `gcd-research.md`; celý 71stránkový důkaz není náš nový audit.
Nová úloha 34 má právě tento vlastní argument s externím vstupem.

Otevřené části se nyní v souhrnu neskrývají za uzavřenou kontrolu
formulace nebo dílčího tvrzení:

- **31 partial:** nová koeficientová domněnka z roku 2016 není
  dokázána. Původní poměr konstant je doložen jako důsledek
  Morrisovy věty; jde o odlišná tvrzení.
- **32 partial:** doložená jednoznačnost pro absolutně spojité
  funkce neřeší všechny spojité pevné body. Norma 2 jednoduchý
  kontrakční argument vylučuje; není to protipříklad k zadání.
- **33 partial:** správnost a ostré nejhorší meze Harrise jsou
  dokázány, obecná průměrná asymptotika nikoli.
- **40 partial pouze kvůli dovětku odpovědi:** požadovaná mez
  počtu kroků je dokázána, stejně jako rekurzivní rodina; empirická
  limita se zlatým řezem a navazující otázka o větším počtu kroků
  zůstávají otevřené. Nález C0128 to nenahrazuje.

Sekce proto má 38/42 úloh uzavřených v celém evidovaném rozsahu.
Staré důkazy se neruší. Dopředné odkazy na průměrný počet běžných
Eukleidových dělení (337/340) a rozdělení podílů a délku dávek
(345/346) budou spárovány v §4.5.3; zatím jsou výslovně odložené.

Závažnost starších vad podle dopadu: C0119 **medium** (doslovná
trojková varianta se může zacyklit), C0123 **medium** (chybná přesná
střední hodnota), C0126/127 **medium** (neexistující derivace a
divergentní řada). C0117/118/121/122/124/125/128/129 **low**:
okrajové meze, pomocný důsledek, komentář, znaménko v převodu
hustoty, číselný příklad, chybějící exponenciální zbytek při jinak
správné asymptotice, záměna logaritmu za strop a bibliografie.
C0120 zůstává **candidate/low** kvůli implicitnímu oboru vstupů.
Žádný nový nález v tomto bloku nevznikl.

Všechny relevantní vrstvy errat a původní sazba jsou v převzatých
blocích. Známé opravy 2001/2004/2013 a Penkova algoritmu nejsou
naše karty. Historický rozsah a přeskočené originály zůstávají
výslovné v `gcd-context.md` a `gcd-inventory.md`.

Další kurzor: 356/file368, §4.5.3, analýza Eukleidova algoritmu.
Strana 647 je partial kvůli začátku odpovědí nové sekce; přesné
ostatní mezery v mapě stran mají vlastní popis.
