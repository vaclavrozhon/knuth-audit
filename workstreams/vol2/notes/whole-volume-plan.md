# Pravidla dokončení celého svazku

Uživatel 1. listopadu 2026 zadal pokračovat, dokud nebude celý svazek hotový,
s očekáváním několikadenní práce. Cíl je aktivní; uzavření jednotlivé dávky
není dokončením tohoto cíle. Pracujeme pouze ve větvi `audit/vol2` a její složce.

`coverage.json` sleduje text sekcí, každou původní úlohu včetně její odpovědi,
úlohy přidané v erratech a další části svazku. Počáteční inventář má 33 sekcí
s úlohami a předběžně 919 původních úloh. Počty pocházejí z OCR a je nutné
je ověřovat po jednotlivých sekcích; nejsou certifikovaným počtem úloh knihy.
Úvody nadřazených sekcí se kontrolují s jejich první podsekcí. Kapitola 4
má navíc samostatný úvod na str. 194. Dodatky, rejstřík a přidaná příloha C
se sledují zvlášť. Rozmezí stránek v přehledu jsou orientační: dvě sekce
mohou sdílet jednu stránku a stránkování novějších tisků se může lišit.

Sekce je uzavřena pouze tehdy, když:

1. Je ověřen její inventář a zpracovány změny všech tří časových vrstev errat.
2. Má uzavřený text a všechny původní i dodatečné úlohy, vždy s dokladem
   a popisem metody a rozsahu kontroly.
3. Nezůstává `todo`, `in_progress` ani `partial` u žádné její povinné části.

`checked` znamená dokončenou kontrolu vymezené položky, nikoli absolutní
záruku bezchybnosti. `confirmed` a `known_erratum` mohou také uzavírat
kontrolu položky, pokud je chyba doložena a zbytek položky prověřen.
Pouhé nalezení známé opravy v dlouhé odpovědi nestačí k uzavření celé odpovědi.
Otevřené výzkumné úlohy nevyžadují vynalezení nového řešení: kontroluje se
formulace, publikovaná odpověď, aktuální stav a jeho zdroje. Nevyřešené
pochybnosti o tvrzeních nebo zdrojích zůstávají otevřené.

U matematických výroků preferujeme vlastní důkaz, doplněný podle potřeby
přesnými výpočty. Citované hlubší výsledky lze ověřovat proti primárnímu
zdroji s výslovným uvedením, že jde o kontrolu citace a použitých předpokladů.
Historické a osobní vzpomínky autora nejsou předmětem nového experimentu;
kontrolují se jejich návaznosti, identifikovatelné údaje a známé opravy.

Čitelný přehled obnovuje `python3 workstreams/vol2/render_progress.py`.
Nálezy a samostatné výpočetní bloky nadále eviduje `ledger.json`, jehož
souhrn aktualizuje `python3 scripts/volume_ledger.py vol2`.
Počty nálezů, matematických bloků a úloh se nesčítají jako jeden druh výsledku.
