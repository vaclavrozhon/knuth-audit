# Nezávislá krátká revize §2.2.2-17 a podmíněného případu -18

Vyžádal kořenový agent 1. 11. 2026; nepřebíráme audit §2.2.2.
Přečteny původní obrazy s. 247, 248, 254 a 544. Kontrola všech
vrstev errat a globální klasifikace zůstávají u kořenového agenta.

## 1. Počet přetečení, úloha 17

Kapacitou zásobníku j rozumíme
`c_j = BASE[j+1] - BASE[j]`. Je-li před vložením vše prázdné
a c_j=0, větev (a) na s. 247 vezme jednu buňku nejbližšímu
neprázdnému úseku vpravo. Přesně zvýší c_j o 1 a sníží kapacitu
dárce o 1. Následné odebrání položky kapacity nemění.

Pro n=M=4 a počáteční (11), tedy c=(0,0,0,4), dostáváme:

| Vklad, vždy po dokončení předchozího páru vklad/odběr | Nové c | Celkový počet přetečení |
| --- | --- | --- |
| I3 | (0,0,1,3) | 1 |
| I2 | (0,1,0,3) | 2 |
| I1 | (1,0,0,3) | 3 |
| I3 | (1,0,1,2) | 4 |
| I2 | (1,1,0,2) | 5 |

Sekvence `I3 D3 I2 D2 I1 D1 I3 D3 I2` je legální. Při
počáteční (13) má každý zásobník kapacitu 1, kterou nikdy
nepřekročí, takže s1=0. Tvrzení by dalo 5≤0+4. Je proto
jednoznačně nepravdivé, bez jakékoli asymptotické interpretace.
Ve slovním důkazu na s. 544 selže tvrzení o nové rekordní
velikosti: druhý I3 znovu přeteče při velikosti pouze 1.
Oprava slova less na more tuto část argumentu nezachrání.

Obecná rodina: pro n=M začněme z (0,...,0,n). V kole r,
1≤r≤n−1, proveďme páry `Ij Dj` pro j=n−1,n−2,...,r.
Indukcí má stav před kolem r první r−1 kapacit rovno 1,
další až po n−1 nulové a poslední kapacitu n−r+1. Jedna
buňka postupně putuje od n po r; každý vklad přeteče.
Po kole je nově c_r=1 a ostatní popsané hodnoty se zachovají.
Celkem tedy s0=n(n−1)/2, zatímco při rovnoměrné počáteční
alokaci s1=0. Pro n≥4 je rozdíl větší než M.

## 2. První přebalení, úloha 18

Při povoleném počátku (11), n≥2 a M=n² je první `I1`
přetečení. Už samotné G1 na s. 248 výslovně volá G2 pro
všech n zásobníků, takže tato jediná operace stojí Ω(n).
Úloha však nastavuje alfa_1=0, protože před ní ještě nebylo
žádné přebalení. Její pravá strana je tedy O(1).

Pod touto inicializací a s konstantou O nezávislou na n je
protipříklad správný. Důkaz na s. 544 skutečně začíná teprve
stavem po přebalení s rovnoměrnou minimální rezervou. Přidání
počátečního O(n) členu umožní zaplatit první přebalení; jeho
přesun nejvýše dosud vložených položek lze účtovat operacím.

Na rozdíl od úlohy 17 je tu textová interpretační mez: věta
„Initially, the tables are set as before“ na s. 248 může být
čtena jako odkaz jen na bezprostředně předcházející (13),
nebo na dříve povolené počáteční alokace včetně (11). Text
žádné číslo vzorce v této větě neuvádí. Při (13) má každý
zásobník alespoň n míst, takže první přetečení vyžaduje
alespoň n+1 vkladů; uvedený jednostupňový protipříklad
pak neplatí a O(n) režie se může amortizovat do m.

Závěr revize: matematický protiklad pro (11) je přesný,
avšak pro posouzení nevyjádřené inicializační podmínky je
rozumné zatím ponechat tuto položku jako `candidate`.
