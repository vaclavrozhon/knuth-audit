# V2-C0104: přísná nerovnost při nulové chybě

**confirmed**, 2.11.2026. Drobná chyba nerovnosti v důkazu, nikoli
chyba algoritmu R ani jeho výsledné meze. TAOCP2, třetí vydání,
první dotisk1997, §4.3.3, str.312, předposlední zobrazená řádka.
[Původní stránka](../images/vol2-p312.png) vizuálně přečtena.

Zde δ_k=1/v−z_k označuje chybu aproximace převrácené hodnoty.
Tištěný řetězec obsahuje `0<=v δ_k^2<δ_k^2`. Při nulové chybě
je ovšem prostřední nerovnost0<0.

Vstup v=1/2=(0.1000...)_2 je povolen. Inicializace R1 dává
`z_0=(1/4) floor(32/4)=2`, tudíž δ_0=0. Všechna V_k také jsou1/2
a každá následující iterace ponechá z_k=2. Nejde tedy o stav, který
by byl v algoritmu nedosažitelný.

Stačí nahradit prostřední `<` znakem `<=`. Obecný důkaz výsledné
přesnosti pokračuje beze změny: chyba po iteraci je rozdíl dvou
nezáporných členů, z nichž první je nejvýše požadovaná mez a druhý
je menší než tato mez. Podrobnosti a také jednodušší obecný důkaz
z_k<=2 jsou v [fast-reciprocal.md](fast-reciprocal.md).

Všechny čtyři vrstvy all2-prepre,all2-pre,all2,err2 byly prohledány
podle312/313, rovnic54/55, reciprocal/Newton i výrazu chyby. Relevantní
známé erratum ze15.5.1998 na str.313 pouze doplňuje tečku za
`constant factor`; původní stránka errata byla zobrazena v
`fast-errata-prepre-p18.png`. Oprava této nerovnosti nebyla nalezena.

Poslední fyzický dotisk, priorita a odměna neověřeny. Neodesláno.
