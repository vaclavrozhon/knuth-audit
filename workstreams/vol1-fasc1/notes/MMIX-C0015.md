# MMIX-C0015 — RESUME ropcode 1 přepíše uložený operand rY

**Confirmed, medium;** §1.4.3′, odpověď 14, p. 123 / file 131,
řádek 168 `BOD resuming,Install_Y`. Digitální vydání 3, květen 2023;
fyzický výtisk neověřen.

Zadání na p. 92 definuje ropcode 1 jako provedení vložené instrukce
s y=rY a z=rZ místo běžných operandů. Platný konkrétní stav:

- rG=32, rL=0; X=255 je globální, tedy není marginal;
- rX=#0100000022fffefd: ropcode 1 a `ADDU $255,$254,$253`;
- rY=1, rZ=2, $254=100; rW=#104 je platná následující textová adresa.

`RESUME 0` má vložit ADDU a dát $255=1+2=3. Kontroly odpovědi 14
projdou: opcode má povolenou vedoucí číslici 2, X je global a opcode
není RESUME. resuming se nastaví na −1. Řádky 166–167 načtou y=1,z=2.
Řádek 168 však přeskočí do Install_Y; ADDU má Y_is_source_bit a
řádky 203–207 znovu načtou $254 do y. Vložený hostitelský ADDU tak
spočte 100+2=102 a zapíše je do simulovaného $255.

Žádná nejasnost ohledně aliasingu, zaokrouhlení ani výjimek se tohoto
příkladu netýká. Všechna čísla jsou malá, použité registry globální.

Primární autorův MMIXware 1.0 potvrzuje konvenci: soubor
sources/mmix-sim-20131017.w, řádky 1738–1749 vynechávají celou
běžnou instalaci operandů pro zvláštní ropcodes; řádky 2646–2648
přímo dosadí y=g[rY], z=g[rZ]. Zdroj pochází z
[autorova archivu](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html),
metadata sources/mmix-20131017-metadata.json. Žádný build/run.

Sazba řádku 168 a následného GetReg ověřena v images/file-131-p123.png
a images/file-092-p084.png. V historických i aktuálních lokálních
erratech nebyla nalezena odpovídající oprava; results/errata-C0015.json.

Oprava musí zachovat rY/rZ a obejít jejich běžné znovunačtení.
Pouhou změnu cíle skoku neprohlašuji za úplnou opravu všech opcodes:
například NEG a operace s immediate Y vyžadují zvláštní převod
hostitelské instrukce. Protipříklad ADDU je úplný i bez takového návrhu.
