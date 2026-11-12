# MMIX-C0011 — odpověď1.3.1′–52 vynechává tři opcodes umožňující no-op

**Stav confirmed, severity low.** Digitální release3, May2023; tištěná p.97 = file105, odpověď52. Jde o neúplný klasifikační seznam v řešení, ne o chybu uvedených existujících no-op příkladů. Předběžné pro závěrečný nezávislý audit uživatele.

Zadání p.27–28 žádá pro každý opcode rozhodnout, zda vhodná X,Y,Z vyrobí no-op pro libovolné počáteční obsahy registrů/paměti. Odpověď na p.97 obsahuje soupis takových opcodů, ale nezahrnuje ZSNZ, CSZI ani PUTI. Nejsnazší samostatný důkaz je ZSNZ; na další implementaci není závislý.

## Přesné doplnění

1. **ZSNZ $255,$255,$255**, opcode7a, tetrabyte7affffff. Je-li původní x=$255 nenulové, instrukce kopíruje x do stejného registru. Je-li x=0, nastaví tentýž registr na0. V obou případech výsledek x·[x≠0]=x. Podle p.16 platí rG≤255, takže$255 je vždy global; nedojde k přidání lokálního registru ani změně rL. Instrukce nemění paměť či jiné speciální registry, nemá aritmetickou výjimku a naváže na@+4, stejně jako SWYM.

2. **CSZ $255,$255,0** s immediate variantou **CSZI**, opcode63, tetrabyte63ffff00. Při x=0 zapíše0, při x≠0 nic nemění. Opět je cílový registr vždy global a stav je zachován. Předpis odpovědi pro register varianty CSN,CSZ,…,CSEV (`X=Z=255`) tento immediate případ nepokrývá: Z zde znamená hodnotu0, nikoli obsah registru$255.

3. **PUT rL,255** s immediate variantou **PUTI**, opcodef7, tetrabytef71400ff (rL má kód20=14hex, Y=0). Z invariantů0≤rL≤rG≤255 a pravidla p.19 „pokus zvýšit rL jej nezmění“ plyne, že zápis255 rL vždy zachová: buď jde o zvýšení, nebo už rL=255. Jiný registr/paměť se nemění. Přesné pravidlo je v [originální p.19, odstavec GET/PUT](../images/file-027-p019.png): „If a program tries to increase rL with the PUT command, rL will stay unchanged.“ Vlastní interpret na p.118/file126 obsahuje PutL s rL←min(z,rL); pro z=255 je to totéž. Tento interní kód je doplňující souhlas, nikoli potřebný simulátorový důkaz.

Všechny tři mají podle tabulky1 čas1υ jakoSWYM. Uvažujeme stejný programový stav a stejnou konvenci no-op jako zadání a odpověď (náklad času může být ignorován). Nepřidáváme skrytou podmínku o předem známém obsahu registru.

## Sazba a errata

Původní sazba prohlédnuta: images/file-105-p097.png (celá odpověď52), images/file-018-p010.png (CSZ,ZSNZ definice), images/file-024-p016.png (global/marginal), images/file-027-p019.png (PUT rL). Zadání je v již prohlédnutých images/file-035-p027.png a file-036-p028.png. Opkódové hodnoty jsou jen doplňující a vycházejí z tabulky1 p.20.

Dne6.11.2026 prohledány historické i aktuální místní vrstvy errata/originals/err1f1.textxt, errata/text/all1f1.txt a errata/text/err1f1.txt podle p.97/answer52 a CSZI/ZSNZ/PUTI/no-op/rL. Na p.97 jsou pouze oprava odpovědi42 NEGU→NEG (8.12.2006) a zápisu `$X is marginal` (10.1.2009). Žádné doplnění uvedených tří opcodů nalezeno nebylo. Viz results/errata-C0011.json.

Doporučená oprava je přidat tyto tři položky s uvedenými operandy. Úplnost všech zbývajících negativních případů úlohy52 ještě není tímto důkazem uzavřena; k prokázání neúplnosti odpovědi stačí první konkrétní případ.
