# MIX: odkazy odpovědi 25 a minimum prostoru v 24(a)

Kořenová revize 2. listopadu 2026 uzavírá dvě konkrétní mezery
X0153/X0154. Přímo byly přečteny původní zadání na straně 143,
odpovědi na 509–510 a níže uvedené cíle. Nový programový test
není potřeba: správnost obou řešení 24 již pokrývá X0150.

## §1.3.1-25: všechny konkrétní odkazy mají správný cíl

Odpověď navrhuje rozšíření stroje, která zachovají význam dříve
platných programů. Nepřímé adresování znamená, že další část
výpočtu adresy přečteme z paměti. Přerušení uloží stav programu,
předá řízení obsluze a dovolí později ve výpočtu pokračovat.
Bitové operace pracují jednotlivě s dvojkovými číslicemi slova.

| Odkaz na straně 510 | Přímo přečtený cíl | Ověřená vazba |
|---|---|---|
| §2.2.2-3, 4, 5 | Svazek 1, 251–252 | Rozšířený indexový údaj, dvojité indexování a nepřímé adresování; jeho příklady a omezení. |
| §1.4.4-18 | Svazek 1, 228 | Záporné adresy, normální a řídicí stav, uložení registrů a instrukce INT. |
| §2.5-28 | Svazek 1, 455 | Nová operace XOR: přepnutí bitů rA podle jedniček v paměťovém operandu. |
| §5.2.2-12 | Svazek 3, 134 | MIX program Batcherova algoritmu s AND a dvojkovým posunem SRB. |
| §6.3-9 | Svazek 3, 508 | Program digitálního vyhledávání; výslovně dovoleny SLB a podmíněný skok JAE. |
| Program 4.5.2B | Svazek 2, 339–340 | Dvojkový největší společný dělitel; definice a použití SLB, SRB, JAE, JAO, JXE a JXO. |
| §6.4-(24) | Svazek 3, 529 | Druhá rozptylovací funkce používá SLB a bitové OR s jedničkou. |
| §7.1 | Svazek 4A, 47 | Úvod Zeros and Ones výslovně rozvíjí logické a bitové operace. |

Jde o kontrolu správného umístění a obsahu odkazů, nikoli nový
audit celých cílových kapitol jiných svazků. V použitém prvním
dotisku svazku 4A z roku 2011 už slíbená §7.1 existuje; nejde
o tvrzení, že byla vydána při tisku svazku 1 v roce 1997.

Identifikace knih a jejich kontrolní součty jsou převzaty z
`inventory/books.json`: svazek 2 je třetí vydání, první dotisk 1997;
svazek 3 druhé vydání, první dotisk 1998; svazek 4A první vydání
a první dotisk 2011. Mapy stran souboru jsou po řadě p+12, p+11
a p+17; pro svazek 1 je p+15. Obrazy a hashe zaznamenává
`results/mix-crossrefs-root-manifest.json`.

Všechny čtyři vrstvy errat byly kontrolovány v původním bloku
`mix-scope.md`; nové cílené vytažení stran 143–144 a 509–510 je
v `results/mix-crossrefs-errata.json`. Opravy kódu odpovědi 26
na 510 se nesmějí zaměnit s odkazy odpovědi 25. Žádná zveřejněná
oprava kontrolované sady odkazů nebyla nalezena. X0669 uzavírá
úlohu 25; historické zdrojové mezery v X0154 zůstávají samostatně.

## §1.3.1-24(a): přesné minimum jsou dvě paměťová slova

Označme B počet hodnot bajtu, tedy základ číselné soustavy MIXu.
Písmena a,...,i označují libovolné hodnoty bajtů 0,...,B−1.
Zadání má kladná znaménka a požaduje změnu

```
rA = (0,a,b,c,d), rX = (e,f,g,h,i)
na
rA = (a,b,c,d,e), rX = (0,f,g,h,i).
```

Počítáme všechna slova programu i jeho předem připravené konstanty
a pomocnou paměť. Ostatní počáteční registry a paměť nejsou zadány
a nemohou poskytovat bezplatnou předepsanou konstantu. Úloha 24
na rozdíl od 22 a 23 nepožaduje HLT. Po skončení úseku má být
dosažen požadovaný stav; navazující instrukce není součástí řešení.

Knižní řešení používá jedno DIV a druhé slovo s hodnotou B^4.
Celé desetibajtové číslo rAX má podíl (a,b,c,d,e) a zbytek
(0,f,g,h,i) při dělení B^4. Podíl se vejde do pěti bajtů,
takže nedojde k přetečení. Dvě slova proto stačí.

Jedno slovo nestačí. Muselo by obsahovat jedinou instrukci;
samotný přechod vyžaduje obecně změnit A i X. Jednoslovná smyčka
se skokem nemění oba registry, zatímco instrukce měnící oba
registry se sama nevrací na tutéž adresu. Vykonávání dalších
paměťových slov nebo dodatečně načteného programu by je také
započítalo do prostoru. Samomodifikace tedy tuto redukci neobchází.

V úplné sadě MIXu mění obě hodnoty současně jen sdružené posuny
rAX, MUL, DIV a CHAR. Ostatní instrukce mění nejvýše jeden
z registrů A a X. To platí také pro plovoucí operace: svazek 2,
strana 224, výslovně říká, že žádný jiný registr než A neovlivňují.

- MUL a CHAR nepoužívají původní X, takže nemohou zachovat jeho
  libovolné poslední čtyři bajty.
- Sdružený posun nebo rotace nemůže ponechat všechny poslední
  čtyři pozice na místě a zároveň přesunout e z X do A. Zachování
  například libovolného bajtu f na téže pozici vynutí nulový
  posun, respektive rotaci o násobek deseti; ta požadovanou
  změnu neprovede. Posun jen A nebo jen X zase nemění oba registry.
- U DIV zvolme vstup A=0 a X=B^4. Požadovaný výstup je A=1,
  X=0. Podíl jedna se zbytkem nula vynucuje kladného dělitele
  přesně B^4. Při jediném započteném slově by jej instrukce
  musela číst sama ze sebe. Každé pole o nejvýše čtyřech bajtech
  má velikost menší než B^4. Pětibajtové pole obsahuje operační
  kód DIV, tedy poslední bajt 4, zatímco B^4 má poslední bajt 0.
  Ani jedna možnost tedy nedá potřebného dělitele.

Všechny možnosti jednoslovného řešení jsou vyloučeny. X0670 tak
uzavírá globální dolní mez prostoru pro 24(a) v uvedeném modelu.
Časové minimum v 24(b) se tím nedokazuje; zůstává v X0153.
