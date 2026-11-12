# V2-C0023: iracionální souřadnice nestačí pro jednoznačný kód

**Confirmed**, 1.11.2026. §3.3.2-27, odpověď str.567, odstavec
pod trojúhelníkovým obrázkem. Třetí vydání, první dotisk1997;
originál `images/vol2-p567.png` vizuálně přečten.

## Protipříklad i s různými počátečními souřadnicemi

Kniha přiřazuje šest číslic šesti **ostrým** uspořádáním tří
souřadnic x,y,z, jejichž součet je1, a tvrdí, že všechny body
s iracionálními barycentrickými souřadnicemi získají jednoznačný
nekonečný kód. Barycentrické souřadnice zde znamenají nezáporné
váhy tří vrcholů trojúhelníku, normalizované na součet1.

Položme a=sqrt(2)/4 a zvolme

```text
(x,y,z) = (a/3, 5a/6, 1−7a/6).
```

Všechny tři souřadnice jsou kladné, iracionální a navzájem různé;
platí x<y<z, takže první číslice je0. Transformace mezer dává

```text
(3x, 2(y−x), z−y) = (a,a,1−2a).
```

Protože0<1−2a<a, další bod leží na společné hranici oblastí4
(z<x<y) a5(z<y<x). Nesplňuje žádné z šesti ostrých uspořádání.
Druhá číslice tedy podle uvedené definice neexistuje. Při použití
uzávěrů oblastí je možné obojí4 a5; obrazy obou hranic se shodují.
Nejde jen o bod s rovnými počátečními souřadnicemi, který by
vylučovala první závorka odpovědi27.

## Přesná oprava

Lze buď přidat jednoznačné pravidlo pro rovnosti při třídění,
nebo tvrzení omezit na body, jejichž žádný iterát nemá dvě stejné
souřadnice. Vyloučené body leží ve spočetném sjednocení racionálních
nadrovin, tedy mají objem0. Nejsou však všechny racionální.
Postačující silnější podmínkou je například lineární nezávislost
1,x,y nad racionálními čísly; pouhá iracionalita x,y,z nestačí.

Každé nekonečné slovo určuje nejvýše jeden bod: inverzní větve
zmenšují vzdálenost měřenou součtem absolutních rozdílů alespoň
faktorem2/3 v každém kroku. Tento kladný výsledek, obecnou verzi
pro n mezer a geometrii obrázku dokazuje `spacings.md`.

## Doklady a omezení

`verify_spacings.py`, blok `irrational_boundary`, ověřuje uvedené
identity a nerovnosti symbolicky. Matematický důkaz nevyžaduje
číselné přiblížení sqrt(2). Všechny vrstvy errat a aktuální TeX
prohledány1.11.2026: str.567–568, odpověď27, permutační kód
a iracionalita; oprava nenalezena.

Metadata Danielsova článku1962 ověřena u vydavatele; úplný text
nebyl dostupný. Nález se týká formulace v Knuthově knize a
nepřipisuje chybu Danielsovi. Nejnovější fyzický tisk a prvenství
neověřeny. ASCII draft neodeslán.
