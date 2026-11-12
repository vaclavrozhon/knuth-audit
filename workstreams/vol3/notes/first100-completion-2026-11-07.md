# Prvních 100 tištěných stran — uzavření podle platného zadání

7. listopadu 2026. Druhé vydání, první tisk 1998. Přímá kontrola počátku
kapitoly potvrzuje offset **+11**, tedy souborové strany 12–111.
Uzavřený rozsah je hlavní text 1–100 s odpovídajícími úlohami a řešeními.
Přebírá se konkrétní podrobná práce zaznamenaná v proof-audit.json;
nejde o nové přečtení celé knihy ani o nový důkaz všech tvrzení.
Nový nález ani výpočet v této uzávěrce nevznikl.

## Souvislost a hloubka přijaté kontroly

- §5, 1–10: 25 úloh, odpovědi 584–591; dvě chapter5-proof poznámky,
  `opening-cost-models.md` a doplnění v quality-recovery-addenda.md.
- §5.1.1, 11–22: všech 29 úloh a odpovědi 591–597; hlavní i čtyři
  úlohové bloky inversions-proof, včetně doplněné Eulerovy rekurence.
- §5.1.2, 22–35: všech 24 úloh, odpovědi 597–602; multisets-proof
  obsahuje faktorizační argumenty, korespondence i jednotlivé části.
- §5.1.3, 35–47: původní i doplněné úlohy 1–29, odpovědi 602–607;
  runs-proof bloky rozlišují tabulky, rekurence, asymptotiky a předpoklady.
- §5.1.4, 47–72: původní i doplněné úlohy 1–45, odpovědi 607–615;
  tableaux-proof bloky obsahují oba směry algoritmů a inverzí,
  přechody důkazů, momenty i přesné externí závislosti. Zejména starší
  mezera v opravené inverzi úlohy 39 byla následně skutečně uzavřena.
- §5.2, 73–80: všech 13 úloh, odpovědi 615–619; čtyři internal-proof
  bloky kontrolují počítání, cykly, MacLarenův postup i rozdělení.
- §5.2.1, 80–100: přímé, binární, dvousměrné a Shellovo vkládání,
  seznamy, stromy a Program M. Celý úlohový oddíl 1–44 byl již
  podrobně projit až za hranici požadavku; evidence jsou insertion-proof
  poznámky, odpovědi 619–628. Na 99–100 jsou doložené všechny
  instrukce, četnosti, stabilita a varianty Programu M.

Rozsah jednotlivých důkazů je ověřitelný z uvedených poznámek a z
`quality-recovery-2026-11-06.md`; nejde o přijetí starého rychlého průchodu.
Současná uzávěrka certifikuje hlavní strany 1–100 a celé odpovědní
584–627. Na sdílené 628 nepřidává plošnou certifikaci další sekce.

## Co přesně certifikace nezahrnuje

Úplný převzatý seznam jednotlivých výjimek pro tyto sekce je uložen v
`results/first100-exceptions-2026-11-07.json`, s původním ID, místem,
popisem a odkazem. Podstatné skupiny:

- Nákladové heuristiky strany 5, pásková/radixová výhoda v úloze 21,
  neurčené obvyklé poměry rychlosti na 74/79/80 a historický práh IBM
  na 83 se neposuzují jako obecné věty bez modelu.
- Vnější výsledky o diskrétních logaritmech na 10, silnější dvouúrovňové
  distribuční větě v odpovědi 38 a externích dolních mezích Shellsortu
  jsou přijaté jako citované výsledky. Jejich nové důkazy se nevyrábějí;
  přesné dříve zapsané zdrojové mezery zůstávají viditelné.
- V Inversions20 a Tableaux14 se neřeší požadavek na nový alternativní
  důkaz, když kniha žádný nepředkládá. Již zkontrolovaný výsledek zůstává.
- Neopakuje se census 179904 u Tableaux42, historická měření tabulek
  6/7, optimalizační hledání incrementů, empirické fitování ani benchmarky.
- P0365 a obdobné prázdné/nulární okraje se podle zadání dále nehoní.
  Přesně zapsané kandidáty C0001/C0017/C0018/C0021/C0023/C0024 nejsou
  automaticky potvrzené chyby. Čtení jejich textu je dokončené.
- Otevřené optimalizační otázky a nedostupné historické prameny zůstávají
  výjimkami; není tvrzeno jejich vyřešení nebo současný výzkumný stav.

Původní detailní partial záznamy zůstávají nezměněné jako historie
silnějšího standardu. V UI se zobrazuje Reviewed s konkrétními výjimkami.
Při této uzávěrce nepřibyly nálezové karty; dřívější nálezy se nezapočítávají
podruhé. Čerstvé srovnání errat: `integration/2026-11-07-first100/errata-recheck.json`.
