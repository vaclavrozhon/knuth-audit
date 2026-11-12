# MMIX-C0006 — instrukční stopa postupuje po čtyřech bytech

Stav **confirmed**, závažnost **low**, předběžně pro nezávislý audit. §1.4.3′, úloha 22, tištěná p.93 / file101, první odstavec zadání.

Originální sazba skutečně popisuje vykonané instrukce na adresách `y₁, y₁+1, …, x₂`. MMIX má čtyřbytové instrukce a normální pokračování zvyšuje adresu o 4; vlastní Fetch na p.81, řádek113, provádí `ADDU inst_ptr,loc,4`.

Krátký protipříklad: program skočí na adresu #100, vykoná tam běžnou instrukci a z #104 skočí jinam. Mezi těmito skoky vykoná instrukce na #100 a #104. Nevstupuje postupně na #101, #102 a #103, jak tvrdí uvedený výčet. Oprava je `y₁, y₁+4, …, x₂`. Jde o popis úlohy, nikoli doloženou závadu implementované tracer rutiny.

Sazba ověřena v images/file-101-p093.png; podpůrný text sources/file-089.txt. V úplných relevantních historických i současných lokálních fasciklových erratech nebyla nalezena oprava této posloupnosti; výsledek je v results/errata-073-112.json. Tištěný exemplář nebyl kontrolován, simulátor nebyl spouštěn; pro uvedené dva kroky není běh potřebný.
