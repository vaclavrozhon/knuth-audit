# MMIX-C0010 — historický kandidát: počet chunků versus počet bytů

**Aktualizace 12. listopadu 2026:** kořenová revize potvrzuje chybu
vytištěného důkazu; neprohlašuje číselný závěr za vyvrácený.
Přesné vymezení a nové ověření pramenů jsou v
`MMIX-C0010-bookwise-proof-review.md`. Následující původní kandidátský
rozbor zůstává zachován jako historie hodnocení.

**Candidate, medium**. Řešení1.4.3′–21, p.126/file134, odhad hloubky rekurzivní simulace.

Text definuje n_k jako počet chunků, dává horní rekurentní odhad4+ceil((2^12+16+(2^12+24)n_k)/2^12), n_0=0, a z prvního překročení2^61 při k=6066 vyvozuje alespoň100^6065 simulovaných instrukcí před problémem.

Otázka jednotek: datový segment má2^61 **bytů**, zatímco každý uzel chunku zabírá2^12+24bytů. Kapacita je tedy menší než2^49 **chunků**, jak také uvádí odpověď4 na p.117 (559670633304293uzlů). Přímé porovnání počtu chunků n_k s2^61 tedy nepodporuje deklarovanou dolní mez hloubky. Menší kapacita se nesmí zaměnit za počet bytů.

Zůstává candidate, protože n_k je uveden jako horní odhad a překročení příliš velkého horního limitu samo o sobě nedokazuje, kdy skutečná simulace selže. Není zde přesná reprodukce rekurze ani doklad skutečné chybné instrukce před100^6065. Pro nezávislý audit je třeba vyjasnit číslování úrovní a vztah paměťového odhadu k počtu instrukcí; dlouhý běh není potřebný.

Sazba p.126 a117 ověřena v images/file-134-p126.png a file-125-p117.png. Relevantní errata bez opravy tohoto tvrzení; results/errata-113-134.json.
