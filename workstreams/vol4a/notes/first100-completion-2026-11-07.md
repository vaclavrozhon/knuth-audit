# Prvních 100 tištěných stran — uzavření podle platného zadání

7. listopadu 2026. První vydání, první tisk 2011; hlavní strany1–100 jsou
souborové18–117. Přebírá se podrobná argumentová kontrola §7 a §7.1.1
z proof-obligations.json a příslušných proof poznámek; nové dočtení uzavírá
hlavní78–100, otázky117–133/odpovědi557–561 a začátek Boolean Evaluation.
Jeden nový nález: **V4A-F0010**, odpověď132(b), str560. Nejde o známé
doplnění y0 z roku2011. Podrobnosti a krátký protipříklad jsou v
[F0010-bent-permutation-arguments.md](F0010-bent-permutation-arguments.md).

## Co bylo skutečně zkontrolováno

Dřívější podrobné poznámky pokrývají úvodní kombinatorické příklady, grafy,
algoritmusH, produkty, barvení a všechny141 úlohy §7 s odpověďmi514–533;
dále booleovské funkce49–77 a úlohy1–116 s odpověďmi534–557. Přijatá
argumentace zahrnuje opravy dříve příliš rychlého průchodu, nikoli jen jeho
čtenářské značky. Doplňkově byly znovu přečteny proof-014 a proof-016:
matematická konstrukce orientovaných stupňů a argumenty barvení jsou
odděleny od doslovných nulových větví a velkých klasifikačních tvrzení.

Nově uzavřený blok:

- Canalizing functions78–79, seznam14 tříd a zadání/odpovědi117–133:
  antichainová mez pro prvoimplikanty, symetrické a dvousymetrické funkce,
  cestová reprezentace, orbits, canalizing/Horn kritéria, inclusion–exclusion,
  bent funkce a náhodné monotónní funkce. Otázky a odpovědi čteny spolu;
  původní sazba95–96 a558–561 prohlédnuta kvůli diagramům a negacím.
- U120 je vytištěná konstrukce49 krychlí kompatibilní s rozkladem na14
  vynucených hran a35 párování prostřední vrstvy. U121 souhlasí počty
  mřížkových cest, self-duální parita i binomické výrazy. U126 kritéria
  Chowových komponent a čtyř bitových souhrnů vyjadřují plnou/prázdnou
  polovinu pravdivostní tabulky. U129 souhlasí opravy průniků včetně
  lineárních funkcí; u130 binomická inverze dává114.
- U132(a,c,d) byly zkontrolovány vytištěné Fourierovy kroky, Parsevalova
  identita, dualita a paritní omezení stupně. Původní rodina132(b) funguje;
  její závěrečné zobecnění selhává: F0010 má souhlas40/64 s afinní funkcí
  proti povoleným36. Jediný nový matematický výpočet je tento64bodový
  potvrzovací příklad, doložený i nezávislým krátkým součtem.
- Boolean Evaluation96–100: mux, řetězce/formule/hloubka, normalizace
  pěti operátorů, tabulka výpočtu S2, všech15 funkčních výrazů v obr9 a
  AlgorithmL včetně argumentu minimality a rekonstrukce operátorů.
  S123 v obr9 je OR rozdílů12,34,13; správně vylučuje jen0000 a1111.
  U S23/S12 byla kontrolována dvojice shodných/různých posledních bitů.
- S tím byly čteny otázky1–11 a odpovědi561–562, související49/570 a
 77/576–577. Rozdělení tabulky v3, centroidový argument4, Fibonacciho
  řetězec5, distributivita6 a normalizace7 navazují na text. U11 byly
  sledovány množiny stop, jejich průnik/sjednocení a pořadí aktualizace;
  kvůli souvislosti dočten první odstavec101. U49 byla zkontrolována
  dosazená růstová mez a exponenciální úbytek, ne vyráběn nový externí důkaz.

## Přesné meze certifikace

Strojově čitelný soupis převzatých výjimek s původním ID, místem a důvodem:
`results/first100-exceptions-2026-11-07.json`. Historické partial položky
se nemažou a nepředstírají se dodatečné velké výpočty. Platné zadání je
kontrola vytištěného textu s následujícími konkrétními výjimkami:

- Úvodní Langfordovy/latinské censy, SGB slovníkové a geografické datové
  soubory, velké grafové/booleovské censy, extrémy prime implicants a
  threshold parametrů se znovu nepočítají. Příklady, argumenty a již
  existující konkrétní certifikáty se přijímají podle jednotlivých poznámek.
- Historické memové benchmarky, provenience citátů a původních dat,
  nedostupné bibliografické důkazy a otevřené výzkumné problémy nejsou
  předmětem nové reprodukce. Citované hluboké asymptotické/klasifikační
  věty jsou externí vstupy, nikoli zde nově dokázané výsledky.
- §7–108/p528: známý guard j>0 použit; matematická výměnová konstrukce
  ověřena. Doslovný zděděný H1 pro nulové výstupní stupně a nevyužité
  čtení c0 v nulových zbytcích nejsou nově implementačně certifikovány.
- Grafy: úplnost soupisu310 maximálních queen cliques, minimalita
  Brinkmannova grafu a maximální symetrie čtyř diagramů zůstávají
  klasifikačními výjimkami. Úplný geografický census a minimum cover
  US49 se znovu nezískávají; odkazy P0133/P0371/P0372 zachovávají rozsah
  původně ověřených svědků. Nevyžaduje se nové očíslování každé hrany
  schémat Fig5 a produktového obrázku49.
- Booleovské části: neformální nákladový model prime-cube bit scan
  (C0004), velké tabulky3–5, příklady Y/ZDD a externí Horn asymptotiky
  jsou odděleny od zkontrolovaných tištěných kroků. U116 platí přesné
  výjimky v single-review-symmetric-2026-11-07.md: silnější optimální
  rekurence, celá dlouhá posloupnost a ostrá paritní konstanta.
- U117 nepřidáváme nový obecný antichainový důkaz; u118,123,124 se
  znovu nepočítají velké úplné klasifikace. U119/131 se neřeší otevřené
  nebo citované asymptotické výsledky. U132 se neobnovuje census bent
  funkcí; samotný konkrétní chybný obecný vzorec byl ověřen samostatně.
- Obr9: funkce řetězců zkontrolovány, úplné hledání všech kratších
  řetězců a všech kompromisů cena/hloubka nebylo znovu provedeno.
  Křížová úloha77, Redkinova dolní mez AND/OR/NOT pro paritu: tištěný
  čtyřpřípadový argument byl přečten, jeho úplná podrobná certifikace
  eliminace hradel se přijímá jako nepřiměřeně náročná výjimka P0526.
- Nulární funkce, prázdné grafy, triviální prázdné domény a kandidáti
  závislí na nepřirozeném výkladu se podle uživatele dále nehoní.

Certifikace: celé hlavní1–100 a odpovědní514–561. Z odpovědní562 jsou
přečteny příslušné1–11, nikoli celý následující obsah stránky; ta proto
nedostává novou celostránkovou značku. Kontrola errat je doložena také
v integration/2026-11-07-first100/errata-recheck.json. Žádný pomocník
ani starý výpočet nebyl spuštěn.
