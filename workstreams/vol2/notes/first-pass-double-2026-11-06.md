# §4.2.3 — první průchod dvojitou přesností

6. listopadu 2026, V2-X0136. Přečten celý výklad246–253,
všech9 zadání a odpovědi617–619. Převzaty uzavřené důkazy
`double-precision.md`, `double-precision-context.md`,
`dekker-recursive.md` a C0091. Žádný nový výpočet ani nález.

Posouzen dvouslovný formát, aproximace A/M/D, znaménka a normalizace,
konverze a meze relativních chyb. Kniha zde výslovně nepožaduje
správné zaokrouhlení. Prostá rekurze Dekkerova postupu v úloze9
je předmětem zkoumání, nikoli tvrzením, že musí dosáhnout čtyřnásobné
přesnosti. Archivní protipříklad proto není chyba knihy.

C0091 zůstává potvrzený, závažnost **low**: chybné jsou údaje o změně
celkového času, nikoli vypočítané hodnoty ani chybové meze.
Nulový součet přidá3u místo úspory3u; přesnější násobení může
ušetřit normalizační posun. Již známá oprava22→23 zapracována,
další čtyři vrstvy errat pokryty starším dokladem.

Známé změny NaN/infinity a subnormal nejsou naše nálezy. Přibližné
průměrné časy nejsou přesné průměry nedoložené vstupní distribuce.
Ikebe1965 má ověřenou citaci, plný článek nebyl dostupný; historická
priorita ani staré výkonové experimenty se znovu neprověřují.

Strany246–252 a617–618 mají celostránkový první průchod. Navazující
část253 a619 je zahrnuta v X0137, aby nevznikla předčasná zelená stránka.
