# MMIX-C0004 — NextChar ztratí část vstupu za nulovým bytem

**confirmed / medium**, předběžné pro nezávislý audit. Chyba kódu §1.4.2′ na p.68/file76, řádek21. Zadání p.67/file75 výslovně používá osmibitové znaky a jako ignorovaný whitespace definuje **každý byte ≤ #20**, tedy i #00. Žádné vyloučení nulového bytu zde není.

Sémantika Fgets je uvedena na p.42/file50: čte znaky až do newline nebo size−1 a až poté přidá ukončovací nulu. Nula uvnitř vstupu není uvedena jako podmínka zastavení. Původní sazby definice, zadání, NextChar i následných korutin byly prohlédnuty. Důkaz se vztahuje k tomuto explicitnímu knižnímu kontraktu; běh konkrétního simulátoru netvrdíme.

Protipříklad je osm bytů

`61 00 62 2e 0a 63 2e 0a` = `a NUL b . LF c . LF`.

Zadání vyžaduje `ab. LF`: ignorovat NUL a skončit prvním bodem. Ruční průchod programu:

1. Fgets naplní buffer `a NUL b . LF NUL` prvním řádkem. NextChar vrátí `a`.
2. Další volání přečte vnitřní NUL. Řádek21 `BZ $0,1B` skočí na nové Fgets a **zahodí b . LF**.
3. Druhé Fgets naplní buffer `c . LF NUL`; NextChar vrátí `c`.
4. Další volání vrátí tečku. Korutina Out ukončí výstup jako **`ac. LF`**.

Protipříklad nepoužívá EOF, vágní chybové výsledky ani číslicovou replikaci. Jde o nesoulad s dovoleným vstupem. Krátká oprava specifikace by mohla výslovně zakázat #00 na vstupu. Chce-li zachovat celé zadání, rutina musí sledovat počet načtených bytů nebo konec bufferu odděleně od hodnoty #00.

Relevantní errata bez této opravy: `results/errata-033-072.json`. Obrázky: `images/block2-coroutines-075.png`, `-076.png`, `-077.png`, `-078.png` a `images/file-050-p042.png`. Fyzický výtisk neověřen.
