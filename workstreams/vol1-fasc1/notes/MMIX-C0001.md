# MMIX-C0001 — první bity a zaokrouhlení

Stav: **confirmed**, nízká závažnost; předběžný závěr pro nezávislý audit.

Tištěná p. 8 = file 16, §1.3.1′, poslední odstavec pod (7). Původní sazba výslovně říká „first 64 bits of the binary representation“ φ⁻¹ s binární čárkou vlevo. Odkazuje na (2), které končí 00010110; stejně hexadecimální příklad (4) je #9e3779b97f4a7c16. Obrázky file-010-p002.png a file-016-p008.png prohlédnuty.

Položme B=2⁶⁴ a a=#9e3779b97f4a7c16. Kladným kořenem rostoucího polynomu f(x)=x²+Bx−B² je B/φ. Přesný celočíselný výpočet dává

- f(a−1)=−39252198824741414471 < 0,
- f(a)=1995974887614534116 > 0.

Proto a−1 < B/φ < a; prvních 64 bitů tedy tvoří **#9e3779b97f4a7c15**. Navíc 4f(a−1/2)=−74512447874253760711 < 0, takže uvedené a je správné zaokrouhlení na nejbližší celé číslo. Formulace o prvních bitech není formulací o zaokrouhlení; explicitní binární čárka v kontextu dává přesný význam prefixu.

Nejmenší oprava je nahradit tvrzení o prvních 64 bitech tvrzením o zaokrouhlení na 64 zlomkových bitů. **Neměnit konstantu v příkladech:** součin (7), jeho horní polovina #61c8864680b583ea a identita rH=B−a jsou správné. Jde o chybu v matematickém popisu, nikoli o chybu instrukce nebo násobení.

Důkazní výstup: `results/golden-ratio-exact.json`. Reprodukce vyžaduje jen dosazení dvou celých čísel do uvedeného polynomu; spuštěný malý výpočet měl nice 15. Relevantní kumulativní i krátká errata viz `results/errata-first-32.json`; odpovídající oprava nenalezena. Fyzický výtisk ani prvenství nebyly ověřeny.
