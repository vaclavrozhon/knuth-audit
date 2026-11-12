# V2-C0159: chybějící nesoudělnost v úplnosti F a pravděpodobnosti

**Stav: confirmed.** Úlohy 4.5.4-12/13 na str. 412–413 a
odpovědi 659–660. Sazba byla zobrazena; předpoklady E jsou
na str. 397. F je správný v obvyklém použití po odstranění
prvočinitelů obsažených ve faktorové bázi. Toto omezení však
není v těchto zadáních ani v tvrzení o úplnosti F uvedeno.
Dixonův postup na str. 401 je má a tento nález ho nevyvrací.

## Úplnost F: šest skutečných výstupů E

Vezměme N=155, k=29 a bázi p_1=2,p_2=3,p_3=5. Číslo
kN=4495 není čtverec a báze vyhovuje filtru na str. 397.
Prvních šest výstupů E s opravenou inicializací z roku 2001 je:

| Výstup | X | (e_0,e_1,e_2,e_3) |
|---|---:|---|
| 1 | 80 | (0,0,2,1) |
| 2 | 152 | (0,0,2,0) |
| 3 | 30 | (1,1,1,1) |
| 4 | 109 | (1,1,3,0) |
| 5 | 25 | (0,0,0,1) |
| 6 | 139 | (1,1,3,0) |

F uloží první řádek pod pivot 3. Třetí vstup po vynásobení
prvním vytvoří uložený řádek `(75;1,1,3,2)` s pivotem 2.
Všechny čtyři návštěvy F5 mají postupně páry

```
(x,y)=(152,3),(115,40),(140,15),(40,40).
```

První tři mají x+y=N, poslední x=y. F tedy žádný faktor
nevrátí. Naproti tomu čtvrtá a šestá původní relace dávají

```
109²=139²=-2*3³ (mod 155),
x=109*139 mod 155=116,
y=-2*3³ mod 155=101,
x!=y, x+y!=155, gcd(x-y,155)=5.
```

To je přesně řešení (18), které je možné odvodit z dodaných
výstupů. E4 smí po šestém výstupu skončit. Pokud pokračuje,
F později faktor najde; to neobnovuje tvrzení o úplnosti
pro již dodaných šest výstupů. Násobení nejednotkou 75 modulo
155 ztratilo rozlišení potřebné pro kombinaci čtvrtého a šestého
výstupu. První relace už sama prozrazuje faktor gcd(80,155)=5,
ale F takový předtest nemá.

## Pravděpodobnost úlohy 13

Pro N=15 a bázi 2,3 mají pevné sudé exponenty `(0,0,2)`
pravou stranu 9. Kořeny v rozsahu 0<x<N jsou právě 3 a 12.
Při nulové předchozí bázi jsou exponenty lineárně závislé;
F5 použije y=3 a oba kořeny zahodí. Pravděpodobnost neúspěchu
je 1, zatímco d=2 různým prvočinitelům odpovídá tvrzené 1/2.
Relace `(12;0,0,2)` skutečně vzniká v E pro k=9.

Navíc pro sudé N=8 a nulové exponenty má 1 čtyři kořeny
1,3,5,7. Dva se zahodí; skutečná pravděpodobnost je 1/2,
zatímco d=1 by dávalo 1. Počet `2^d` z odpovědi tedy vyžaduje
liché N a jednotkovou pravou stranu.

## Oprava a ověření

Stačí výslovně omezit F a úlohu 13 na N nesoudělné se všemi
prvočísly faktorové báze; při p_1=2 tím vznikne i lichost.
Alternativně se malé faktory odstraní před vstupem do F.
Pro úplnost F pak platí homomorfismus závislostí do kořenů
jednotky modulo znaménko; pro úlohu 13 čínská věta o zbytcích
dává přesně 2^d stejně pravděpodobných kořenů. Podrobné obecné
důkazy jsou v `notes/factoring-contfrac.md`, §3–4.

Protipříklad F byl ověřen rekurzí E, nezávislými nezkrácenými
konvergentami, přímou stopou F i úplným výčtem podmnožin.
Doklady jsou v checkpointu `counterexamples` souboru
`results/factoring-contfrac.json`. Záznam obsahuje i gcd
párů, které F5 zahodí; samo testování netriviálnosti tam faktor
nevrací, přestože u nejednotek může být gcd vlastní i při x=-y.

Dne 3. listopadu 2026 byly prohledány všechny čtyři řady errat
a aktuální TeX podle úloh, stran, E/F a nesoudělnosti.
Oprava E1 z roku 2001 byla zahrnuta; doplnění těchto podmínek
nalezeno nebylo. Poslední fyzický dotisk ani priorita nálezu
nejsou ověřeny. Snímky: `vol2-p397`, `vol2-p412`, `vol2-p413`,
`vol2-p659`, `vol2-p660` a `vol2-p401` ve složce `images/`.
