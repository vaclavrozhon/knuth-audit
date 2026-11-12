# Prvních 100 tištěných stran — uzavření podle platného zadání

7. listopadu 2026. Třetí vydání, první tisk 1997; tištěná strana p je
souborová p+12. Uzavřeno 1–100, s příslušnými zadáními a odpověďmi.
Jde o přijetí doložené podrobné revize z 6. listopadu a nové posouzení
jejích výjimek, nikoli o tvrzení, že byl dnes celý text přečten podruhé.
Žádný matematický výpočet nebyl spuštěn. Nový nález nepřibyl.

## Přijaté souvislé bloky

| Text | Spárovaná evidence |
|---|---|
|1–9, §3.1, všech 23 úloh|`sequential-introduction-2026-11-06.md`: náhodné mapy, cykly, konkrétní postupy a jejich tištěné argumenty.|
|10–16, §3.2.1 a §3.2.1.1, 5+14 úloh|`sequential-lcg-modulus-2026-11-06.md`: afinní iterace, modularita, MIX a přenosy.|
|16–26, §3.2.1.2–3, 22+8 úloh|`sequential-multiplier-2026-11-06.md`, `sequential-potency-2026-11-06.md`: periody, potence a binomické kroky.|
|26–40, §3.2.2, 37 původních a přidaná 38|`sequential-other-methods-2026-11-06.md`: generátory, úplné posloupnosti, inverzní metody.|
|41–60, §3.3.1, 25 úloh|`sequential-general-tests-2026-11-06.md`: chí-kvadrát, KS, tabulky a doplňky odpovědí.|
|61–80, §3.3.2, 35 úloh|`sequential-empirical-core-2026-11-06.md`, `sequential-spacings-2026-11-06.md`, `sequential-empirical-tail-2026-11-06.md`: běhy, kolize, mezery, korelace, procházky a monkey test.|
|80–93, §3.3.3, 28 původních úloh a Fineův dodatek|`sequential-dedekind-2026-11-06.md`, `sequential-theoretical-tail-2026-11-06.md`: součty, reciprocita, obdélníky a spojité modely.|
|93–100, začátek §3.3.4|`sequential-spectral-foundations-2026-11-06.md`: periodická mříž, dualita a redukce; celý navazující S a úlohy 1–15 mají již podrobnou kontrolu, včetně číselných částí v `sequential-spectral-numerics-2026-11-06.md`.|

Záznamy obsahují konkrétní argumenty a rozlišují původní sazbu od oprav.
Převzetí není založeno pouze na starém příznaku checked. Staré výpočty
a jejich rozsah zůstávají historickou evidencí; jejich nové provedení
se netvrdí. Celé odpovědní strany 538–579 lze certifikovat. Na 580 jsou
spárovány odpovědi do 15; tento zápis sám necertifikuje zbytek stránky.

## Přesné výjimky a rozhodnutí

- Strana 36: definice a podmíněné kryptografické tvrzení byly zkontrolovány;
  pozdější X0149 spároval odkazy. Stoletý výkonnostní odhad a historické
  velikosti modulů nejsou reprodukovaným měřením.
- Strany 47, 49, 50, 52, 54: nereprodukují se neurčené původní seedy,
  výběry bloků a úplné historické grafy. C0017 zůstává kandidátem,
  protože bez nich nelze záměnu znamének potvrdit.
- Strany 72, 75, 88–91: historická měření a výroky o tehdejší praxi,
  včetně tří krátkých korelací §3.3.3–14, nejsou nově reprodukovány.
  Matematické vztahy jsou posouzené samostatně.
- §3.3.2–25, strany 78/566: numerické intervaly jsou doložené;
  nevyrábí se nový obecný důkaz komentáře o poměrech blízkých −t.
- §3.3.2–31, strany 79/570: C0241 závisí na doslovném rozšíření
  kvalitativní formulace na celou periodu. Zůstává interpretační
  poznámkou; není důvodem nechat přečtenou stránku šedou.
- §3.3.3–19, strany 91/574: vytištěný čtyřčlenný vzorec i zbytek
  jsou zkontrolovány. Nový důkaz ostré doplňkové meze R≤A/8 není
  součástí tohoto zadání; tato konkrétní mez není nezávisle certifikována.
- Strany 93–95: dobové hodnocení síly testu není univerzální zárukou.
  C0243 se vykládá v následně výslovně zavedené periodické mříži;
  žádná chyba samotného algoritmu z něj neplyne.
- Vnější klasické věty, otevřené výzkumné otázky, nepřiměřené censy,
  historická prvenství a nedostupná bibliografie mají přesný rozsah
  v uvedených poznámkách. Jejich nové dokazování ani dohledávání se
  nepožaduje. To nezakrývá žádný dosud nepřečtený souvislý blok.

Historické partial v coverage.json se nemažou: popisují tehdejší silnější
důkazový standard. Autoritativní uzavření pro současné zadání je zde
a v `review-ui/review-certifications.json`. Staré nálezové karty se
nevydávají za nové. Aktuální porovnání autorových errat je v
`integration/2026-11-07-first100/errata-recheck.json`.
