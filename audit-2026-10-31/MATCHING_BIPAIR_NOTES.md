# Kanonické bipáry úplného grafu: 215–216

Kontrola 1. listopadu 2026. Hlavní 4B strana 473 a autorův Pre-Fascicle 5C
strana 177 byly vizuálně porovnány. Veřejná all4b a all4f5 neobsahují níže
uvedené opravy. Starší opravy 215(e,g) z 17. února 2022 jsou v našem PDF
již zapracované a nejsou novým nálezem.

## F072: posunutá úroveň v 215(d)

Počet uzlů na úrovni l je **2(q−l+1)**, 1≤l≤q, nikoli 2(q−l).
Kořen je na úrovni nula, jak výslovně určuje i strana 105. Pro q=1 má
kořen dvě děti; tiskovaný vzorec by na první úrovni dával nulu.
Celkový počet uzlů je 1+q(q+1).

Obecný důkaz: pro lexikografické pořadí je z každé čtveřice a<b<c<d
povoleno jen párování ab,cd. Po větvi 0k s k>1 se vrchol 1 nedá pokrýt.
Po 01 zbývá stejná úloha na 2,…,2q. Indukce dává profil
1,2q,2q−2,…,2. Stejná logika funguje při omezeném souboru zákazů z (e):
vždy stačí zákazy se sousedními nejmenšími vrcholy i,i+1 a sudým i.
Jejich počet je 2 sum_{r=1}^{q−1} binom(2r+1,2)
=q(q−1)(4q+1)/3.

Pro chytré pořadí (f) je po větvi 0k izolovaný partner 2q+1−k;
profil je 1,2q. Redukovaná sada (g) má (2q)(2q−2) zákazů.
Všechny čtyři konstrukce byly pro q=1,…,10 ověřeny přímým množinovým
prohledáváním a původním DLX2. [40 shodných profilů](results/matching_bipairs/native.json).

## F073: lexikografické pořadí není nejhorší na každé úrovni

Odpověď 216 tvrdí nejhorší případ na každé úrovni. Pro K7 dejme první
možnosti **12,13,23** a za ně ostatní hrany lexikograficky. Z každé čtveřice
vrcholů zakažme dvě párování, která neobsahují nejdřívější hranu, přesně
podle 215(b). Primární položky jsou 0,1,…,6 a používáme MRV, při shodě
nejmenší položku. Profil je **1,6,2,4**, zatímco lexikografický je **1,6,4,2**.
Na třetí úrovni tedy máme 4>2 uzlů. Celkové počty jsou v tomto příkladu
stejné; příklad sám nevyvrací nejhorší celkovou velikost.

Celý strom lze zkontrolovat ručně:

* Kořen větví na 0: 01,02,03,04,05,06.
* Po 01,02,05,06 ihned nastane spor (prázdné položky 2,1,4,4).
* Po 03 se větví na 1, jedinou možnost 12; potom na 4 s 45 a 46.
* Po 04 se větví na 5, jedinou možnost 56; potom na 1 s 12 a 13.
* Všechny čtyři poslední větve jsou listy se sporem.

[Vstup DLX2](results/matching_bipairs/counter-prefix.xcc),
[původní výstup](results/matching_bipairs/counter-prefix.log),
[pořadí a zakázané dvojice](results/matching_bipairs/counter-prefix.json).
Původní autorův DLX2 reprodukuje profil přesně. Druhý kód pracuje jen
s množinami hran a zakázaných dvojic; nepoužívá tančící seznamy.

## Rozsah

Počty 3 binom(2q+1,4) bipárů a 2 binom(2q+1,4) zakázaných dvojic
plynou z přesně tří párování čtyř vrcholů. Jejich nejmenší hrana určuje
jediné preferované párování. Pro K21 je počet zákazů opravdu 11 970.
Historická měření memů a jejich náhodné rozptyly nejsou reprodukovány.
Náhodné vzorky ve skriptu slouží k hledání protipříkladů, ne jako důkaz
obecné meze. Původně očekávaný test úrovňové meze selhal; právě to vedlo
k samostatnému F073.
