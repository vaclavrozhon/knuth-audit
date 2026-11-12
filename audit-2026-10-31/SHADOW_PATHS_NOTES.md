# Loopless shadows — 7.2.2.2, cvičení 522–524

Stav: uvedené počty, svědecké posloupnosti i matematická tvrzení souhlasí.

## Úplný výčet

C++ program `shadow_paths.cpp` prochází jednoduché cesty v grafu P3×P3×P3.
Po každém kroku musí být sjednocení promítnutých hran v každé ze tří rovin
les. Stav projekce je 12bitová maska; její acykličnost ověřuje disjoint-set
union na devíti vrcholech. Samostatný Python program `check_shadow_paths.py`
prochází stejné matematické úlohy jiným zápisem a testuje acykličnost
odstraňováním listů. Nepoužívá C++ prořezávání zbytkového grafu.

- Cykly bez rohů: žádný, úplný výčet oběma programy.
- Cykly procházející rohem: po fixaci 111,112 a předchůdce 121 existuje 16
  orientovaných svědků, všechny délky 24. Po ztotožnění 48 symetriemi krychle,
  posunem začátku a obrácením směru zbývají přesně **dva**.
- Hamiltonovské cesty začínající v 111 s prvním krokem do 112: 12 svědků,
  **čtyři** třídy symetrie.
- Z vrcholu uprostřed stěny: dva svědci po prvním kroku směrem k hraně,
  žádný po kroku do středu krychle. Jejich třída už je mezi předchozími čtyřmi.

To pokrývá všechny případy. Každý cyklus s rohem lze normalizovat uvedenou
volbou sousedů. Hamiltonovská cesta v tomto bipartitním grafu musí mít oba
konce v početnější barevné třídě, tedy v rohu nebo uprostřed stěny. Stabilizátor
středu stěny má právě dva typy prvního kroku, oba byly prohledány.

Všech šest delta posloupností bylo přečteno přímo z textu p.654, převedeno na
souřadnice a ověřeno. Dvě cyklické posloupnosti představují obě nalezené třídy;
čtyři Hamiltonovské představují všechny čtyři třídy. Nejde pouze o kontrolu
jejich délek.

## SAT kódování a počty

Úplný výčet jednoduchých cyklů rovinné mřížky 3×3 dává 13: čtyři délky 4,
čtyři délky 6 a pět délky 8. Jejich zákazy tedy mají v součtu 240 literálů
ve třech projekcích. Shadow proměnných je 36; samotných proměnných pozice 27T.
Kódování at-most-one z odpovědi 12 zavádí q=floor((n−3)/2) pomocných proměnných
pro n≥3 (pro menší n žádné); zůstane skupina r=n−2q a počet binárních klauzulí
je 6q+binom(r,2). Tento vzorec plyne z rekurzivního oddělení první trojice.

Pro cykly má každá z T vrstev 27 adjacenčních klauzulí (135 literálů) a
216 ternárních klauzulí zavádějících stínové hrany. U cest je takových přechodů
T−1. Po přidání 39 zákazů cyklů a tří jednotek dostáváme přesně:

| Úloha | Proměnné | Klauzule | Literály |
|---|---:|---:|---:|
| Cyklus T=16 | 822 | 6264 | 17439 |
| Cyklus T=24 | 1242 | 9456 | 26199 |
| Hamiltonovská cesta T=27 | 1413 | 10410 | 28701 |

Adjacenční implikace a alespoň jedna jednotka zároveň vynutí neprázdnost všech
slotů. U cyklů ji přenášejí modulo T; u cest dopředu ze začátku. Proto nechybí
samostatné alespoň-jeden klauzule. Časové údaje historických solverů netestujeme.

## Obecný důkaz cvičení 523

Předpokládejme jednoduchý cyklus v Pm×Pn×P2, jehož projekce do první roviny je
strom T. Cyklus leží v T×K2. Každou použitou hranu T musí uzavřená procházka
překročit suděkrát. K dispozici jsou jen její dvě zdvižené hrany, každá nejvýše
jednou, a proto se obě musí použít. Použitý podstrom nemůže mít vrchol stupně
3: každá jeho kopie by už měla tři incidentní hrany cyklu. Podstrom je tedy
cesta. V jejích vnitřních vrcholech jsou obě kopie stupně 2, a tudíž tam nemůže
být svislá hrana. Na obou koncích naopak svislá hrana musí být.

Konce této cesty se liší alespoň v x nebo y. Projekce do příslušné souřadnice
a třetího rozměru obsahuje vodorovný interval v obou vrstvách a oba koncové
svislé spoje — tedy cyklus. Všechny tři stíny proto nemohou být bez cyklů.
Tento důkaz platí pro libovolná m,n a nevyžaduje numerické omezení.

Výsledky a všechny svědecké souřadnice jsou v `results/shadow_paths/`.
