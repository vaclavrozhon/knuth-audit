# V2-C0015: nesprávný percentil v odpovědi §3.3.1-5

**Stav:** potvrzený nesoulad v dostupném třetím vydání, prvním tisku
(1997), str. 559, odpověď 5. Přesný dopad: chybná doprovodná procentní
hodnota; statistiky i závěr nezamítnout jsou správné. Novější fyzický
výtisk, prvenství a případná odměna nejsou ověřeny. Draft neodeslán.

## Zdroj a konvence

Vizuálně ověřeno v [původní sazbě](../images/vol2-p559.png), strana
souboru 571. Odpověď tiskne K+_20=1.15, K-_20=0.215 a uvádí
„94% and 86% levels“. Data jsou na [str. 58](../images/vol2-p058.png).

Pro distribuční funkci statistiky píšeme `H_n(s)=Pr(K_n <= s)`.
Text na str. 50 a záhlaví tabulky 2 na str. 51 používají procentní
úroveň ve významu této distribuční funkce: například 75 % odpovídá
pravděpodobnosti, že K_20 nepřekročí 0.7975. Pro druhou statistiku
z úlohy 5 jde o přibližně **12. percentil**, nikoli 86.

## Přesný výpočet

Pro n seřazených pozorování u_j z [0,1] je

```
D- = max_j (u_j-(j-1)/n),  K- = sqrt(n)*D-.
```

Z 20 vytištěných dat vyjde D-=0.048=6/125. Maximum nastává například
pro u_2=0.098. Z knihy (25), s t=nD-=24/25<1, zůstává jediný člen k=0:

```
Pr(K-_20 <= sqrt(20)*6/125)
  = (6/125)*(1+6/125)^19
  = (6/125)*(131/125)^19
  = 0.11697838135556601251310821352537364....
```

Pro druhé znaménko jsou distribuce stejné, jak dokazuje reflexe
`u_j -> 1-u_(n+1-j)`. Hodnota K+_20 je sqrt(20)*129/500 a její percentil
94.2001854999... %, takže první ze dvou knižních procent souhlasí.

Nezávislá kontrola obou pravděpodobností: přímá integrace polynomů
přes uspořádaný simplex s dolními mezemi max(0,j-t). Její přesné
racionální výsledky souhlasí s oběma uzavřenými součty (25), (26).
Viz [ks.json](../results/ks.json), položka `exercise5.independent_validation`,
a [verify_ks.py](../verify_ks.py).

Již tabulka 2 odhalí nesoulad bez integrálů: pro n=20 platí
`0.1298 < 0.215 < 0.3461`, takže hodnota leží mezi 5. a 25. percentilem.
Nemůže být na 86. percentilu.

## Alternativní interpretace a navrhovaná oprava

Pokud by „level“ u druhého výsledku mělo znamenat horní ocas distribuce,
vyšel by 88.3021618644... %. To by se lišilo od předchozí konvence
v tabulce a textu; správný dolní percentil je každopádně jednoznačný.
Nález nestojí jen na rozdílu mezi přibližnými 86 a 88 procenty, nýbrž
na chybném směru percentilu při standardní konvenci knihy.

Minimální oprava je nahradit 86 % za 12 %. Žádná změna závěru testu
není potřeba: obě statistiky zůstávají uvnitř intervalu 5.–95. percentilu.
Volné slovní hodnocení blízkosti hranice není předmětem nálezu.

## Errata

Dne 1. listopadu 2026 prohledány všechny čtyři řady:
`errata/text/all2-prepre.txt`, `all2-pre.txt`, `all2.txt`, `err2.txt`,
a aktuální původní TeX `sources/err2.textxt`. Vyhledány str. 559,
číslo úlohy, hodnoty 0.215, 94 a 86 i slovní varianty procentních úrovní.
Žádná oprava odpovědi 5 nalezena. Nejbližší změna na téže stránce je
`max -> sup` v odpovědi 6 z 18. června 2024; ta tento údaj nemění.
Lokální řady byly dříve tohoto dne porovnány s aktuálním stažením.
Vydavatelský náhled 2026 neobsahuje odpovědi, proto ho jako potvrzení
přetrvávání této chyby nepoužíváme.
