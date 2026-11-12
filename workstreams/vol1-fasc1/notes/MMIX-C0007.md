# MMIX-C0007 — SAVE skončí po prvním globálním registru

**Confirmed, medium**, předběžně pro nezávislý audit. Řešení1.4.3′–11, p.120/file128; `BNZ t,1F` hned za `INCL ss,8`.

Původní sazba opravdu obsahuje BNZ. Zadání p.92 vyžaduje po zásobníku uložit všechny globální registry, příslušné speciální registry a nakonec kombinaci rG/rA. Vezměme platný stav rG=254 a instrukci SAVE $254,0. Vstupní kontrola globálního registru projde.

V první iteraci ukládání globálů je y=8·254=2032. `CMPU t,y,8*(rZ+1)` porovnává2032 s224 (rZ má kód27), takže t=1. PBNZ přeskočí sestavení závěrečného octabytu a uloží se $254. INCL ss,8 nemění t. Chybné `BNZ t,1F` proto okamžitě skočí na závěrečné `SET oo,ss` a XDone. $255 ani žádný z požadovaných speciálních registrů se neuloží. Závěrečný octabyte rG/rA také chybí.

Správný test je **BZ t,1F**, protože pouze y=224 označuje dokončený závěrečný octabyte. Komentář u větve právě tuto podmínku popisuje. Tento krátký průchod nepotřebuje spuštění simulátoru; žádný běh zde netvrdíme.

Sazba: images/file-128-p120.png. Kontrakt: sources/file-100.txt. Ve všech relevantních lokálních historických i současných fasciklových erratech není odpovídající oprava; results/errata-113-134.json. Fyzický výtisk neověřen.
