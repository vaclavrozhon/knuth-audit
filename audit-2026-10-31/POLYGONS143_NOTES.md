# DLX 143: konvexní mnohoúhelníky v trojúhelníkové síti

Zadání: 4B strany 141–142; odpověď: strany 454–455. Pracujeme s nenulovou
plochou, tedy s počtem trojúhelníků `N ≥ 1`. Degenerované úsečky nejsou
mnohoúhelníky zadané úlohy. Obrázek, parametrizace, algoritmus, šest tvarů
pro N = 24 i citace OEIS byly prověřeny. **F137** opravuje nepravdivé
tvrzení o nepokrytelnosti jednoho ze šesti tvarů. **E069–E071** jsou známá
errata, nikoli další nové chyby.

## Graf a původní obrázek

Pro `simplex(7,7,5,3,0,0,0)` souhlasí všech **23 vrcholů, 51 hran a
29 vnitřních trojúhelníků**. Všechny trojciferné popisky a všechny hrany
obrázku byly přímo dekódovány z původního PDF i autorova draftu.
Obvodová posloupnost `503412` je správně při vhodné orientaci počátku.

Původní implementace `simplex` ze Stanford GraphBase byla skutečně spuštěna.
U všech deseti grafů (příklad, tři grafy odpovědi a šest kanonických tvarů)
se shodují celé množiny vrcholů i hran s přímou konstrukcí podle definice.
Tři grafy v části (a) mají přesně tvary úlohy 140.
[Grafy](results/polygons143/sgb/checked.json),
[původní obrázek](results/polygons143/figure-checked.json).

## Obecná klasifikace a obsah

Směry v celočíselné bázi jsou `(1,0), (0,1), (−1,1), (−1,0), (0,−1), (1,−1)`.
Uzavřenost obvodu dává přesně dvě knižní rovnice
`x0+x1=x3+x4` a `x1+x2=x4+x5`.
Položme `δ=x0−x3=x2−x5=x4−x1`. Otočení o lichý násobek 60° mění znaménko
δ, takže můžeme zvolit δ ≥ 0. Otočení o 120° cykluje trojici `(x3,x5,x1)`
a zrcadlení vymění její poslední dvě složky. Lze ji tedy jednoznačně
uspořádat jako `b ≥ c ≥ d`. Položíme `a=b+δ` a dostáváme

```text
a ≥ b ≥ c ≥ d ≥ 0,
(x0,x1,x2,x3,x4,x5) = (a,d,a−b+c,b,a−b+d,c).
```

Rovnosti mezi parametry mohou dát více zobrazení téhož tvaru, nikoli další
kanonickou čtveřici. Tím je doložena úplnost i jednoznačnost normalizace.

Začněme rovnostranným trojúhelníkem se stranou `s=a+c+d` a odřízněme
tři rohové trojúhelníky se stranami `b,c,d`. Uspořádání parametrů zaručuje,
že se odřezané vnitřky nepřekrývají. Zbývající obsah v jednotkových
trojúhelnících je

```text
N = (a+c+d)² − b² − c² − d².
```

Stejná konstrukce dává odpověď (d):
`simplex(a+c+d,a+c,a+d,a−b+c+d,0,0,0)`.
Pro N > 0 jsou první tři meze kladné, takže zde nula neukončuje dimenze
GraphBase předčasně. Přímá souřadnicová kontrola souhlasí pro všech
**990 nenulových čtveřic s a ≤ 10**. Normalizace byla navíc ověřena pro
**5 022 uzavřených obvodů** s jednotlivými délkami nejvýše 9.

## Algoritmus po známé opravě parity

Pro dané c,d je nejmenší možný obsah při a=b=c roven `2c(c+2d)`.
To odůvodňuje oba omezené cykly. Definujeme `x=N+c²+d²`; potom

```text
x = s²−b² = (s−b)(s+b).
q = s−b > 0,  q² ≤ x.
```

Čísla q a x/q musejí mít stejnou paritu. Každá taková dvojice dělitelů
jednoznačně obnoví `s=(x/q+q)/2`, `b=(x/q−q)/2` a `a=s−c−d`.
Test a ≥ b ≥ c odstraní právě nepřípustné čtveřice. Obráceně každá
přípustná čtveřice má právě svého dělitele q, takže algoritmus nic
nevynechá a nic neopakuje. Případ x mod 4 = 2 správně nemá řešení.

V knize vytištěné `q ≡ x (mod 2)` je známá chyba **E069**, opravená
20. prosince 2022 na `q ≡ x/q (mod 2)`. Nejmenší N, při kterém původní
podmínka vrátí necelé parametry, je **20**: pro c=d=0 a q=4 dostaneme
a=9/2, b=1/2. Toto není nový nález.

Opravený algoritmus souhlasí se všemi **5 200 zveřejněnými hodnotami
OEIS A096004**. Pro N=1,…,100 se navíc shodují celé množiny s nezávislým
přímým průchodem parametrů a výpočtem obsahu ze souřadnic obvodu.
Konečná mez tohoto průchodu je oprávněná: při a>b platí N≥2a−1;
při a=b a N>0 platí c+d≥1, a tedy N≥2a.
[Výsledky a původní hashe](results/polygons143/geometry-and-algorithm-checked.json).

## N = 24 a oprava nepokrytelnosti

Knižní algoritmus vypíše přesně šest čtveřic, ve správném pořadí:

| Pořadí | (a,b,c,d) | Pokrytí Langfordovou sadou |
|---|---|---|
| 1 | (7,5,0,0) | Žádné; dva úplné nezávislé výčty. |
| 2 | (5,1,0,0) | Třetí tvar úlohy 140(a), již ověřen. |
| 3 | (12,12,1,0) | **Pokrytelný pás 12 × 1; F137.** |
| 4 | (6,6,2,0) | První tvar úlohy 140(a), již ověřen. |
| 5 | (2,2,2,2) | Žádné; dva úplné nezávislé výčty. |
| 6 | (4,4,3,0) | Druhý tvar úlohy 140(a), již ověřen. |

Třetí tvar má 206 472 pojmenovaných sestavení a 8 603 tříd po přejmenování
barev. Přímá validace kontroluje každý uložený model a porovnává celé
množiny obou řešičů. Pro samotný protipříklad stačí dva řádky barev
v [F137_TRIANGLE_STRIP.md](F137_TRIANGLE_STRIP.md) a krátký
[samostatný verifier](verify_f137.py).

Původní kontrolní wrapper přebral knižní hypotézu „počet je nula“.
Po úspěšném dokončení výčtu třetího tvaru proto skončil na této nepravdivé
assertion. Zachovali jsme jeho zdroj, log i oba dokončené terminály.
Navazující program hledal pouze dosud nespuštěný pátý tvar a poprvé
spustil nezávislý řešič. **Žádný dokončený výčet nebyl opakován.**

## Prameny, známé opravy a záznam běhu

Primární OEIS záznam potvrzuje autora **Paul Boddington, 27. července 2004**;
rok a odkaz v knize jsou správně. Pozdější b-file je s algoritmem ve shodě.
Připojený článek z roku 2025 je uložen, ale jeho úplný audit netvrdíme.
Původní `gb_basic.w` je z oficiálního archivu Stanford GraphBase.

**E070**, 13. února 2023: „the boundary of“ → „the boundary path of“ na
straně 142. **E071**, 21. října 2021: třetí čtveřice `(5,1,1,0)` →
`(12,12,1,0)` ve Fascicle 5, strana 263. E071 je v našem 4B již zapracovaná;
autorův draft z roku 2019 ji ještě nemá. Všechny relevantní kontexty a
šest vrstev oprav jsou v [errata-check.json](results/polygons143/errata-check.json).

Geometrický checker zapsal konečný soubor i zprávu PASS až po všech
assertions. Obalující terminál přesto oznámil návratový kód 143.
Evidujeme oba fakty a příčinu kódu neodhadujeme. Hotové výpočty jsme
neopakovali; hashe programu a výsledku jsou ve
[záznamu pozorování](results/polygons143/geometry-terminal-observation.json).

Celá úloha 143 je po doložení F137 a známých oprav uzavřená ve smyslu
registru průchodu. Tím se neuzavírá celý svazek, starší historické mezery
ani ověření fyzického výtisku.
