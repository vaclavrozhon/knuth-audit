# V2-C0006: přesná rovnost v erratu k §3.2.1.3-8 vyžaduje podlahu

**Stav: confirmed, 1. listopadu 2026.** Nález se týká veřejného errata
ze 14. května 2016 aplikovaného na předchozí opravu z 27. února 2004.
Není tvrzením o neprohlédnutém novějším fyzickém dotisku ani o prvenství.
Hlavní vysvětlení statistické vady generátoru zůstává správné.

## Původní sazba a posloupnost oprav

První dotisk má v odpovědi na [str. 551](../images/vol2-p551.png)
přibližnou rovnost pro deset intervalů. Erratum z 27. 2. 2004 mění
zadání na dvacet intervalů a milion trojic
([sazba](../images/all2-prepre-p04.png), all2-prepre strana souboru 4).
Odpověď nahrazuje vzorcem

```
Y_(n+2) ~= (10 + 6(Y_(n+1)+epsilon_1) − 9(Y_n+epsilon_2)) mod 20,
0 <= epsilon_1 < 1, 0 <= epsilon_2 < 1.
```

Viz [all2-prepre strana souboru 31](../images/all2-prepre-p31.png).
Erratum ze 14. 5. 2016 pro str. 551, řádek 2, mění přibližnou rovnost
na přesnou. [Přímý render původního PS](../images/all2-pre-p13-direct.png)
potvrzuje, že jde opravdu o znak `=`, nikoli chybu OCR či převodu PDF.
Tento záznam navíc píše index n+1 na obou stranách šipky, zatímco
rovnice v doložené opravě 2004 má n+2. Hlavní níže uvedená chyba
zůstává i při přirozeném čtení zamýšleného indexu n+2.

## Přesný protipříklad

Použijeme přesně generátor ze zadání:
m=2^35=34359738368, a=2^17+3=131075, X_0=1,
X_(n+1)=a X_n mod m a Y_n=floor(20 X_n/m).
Podlaha floor(t) je největší celé číslo nejvýše t.

```
n       X_n             Y_n
75      12020024059       6
76      27570145521      16
77       5701049043       3
```

Hodnoty byly získány opakováním rekurence a nezávisle ověřeny jako
a^75,a^76,a^77 modulo m. Jde o přímo testovanou nepřekrývající se
trojici s indexem 25, nikoli o jinou počáteční podmínku.

Přesná rovnost bez podlahy by vyžadovala

```
3 = (52 + delta) mod 20,
delta = 6 epsilon_1 − 9 epsilon_2,
−9 < delta < 6.
```

Z první rovnosti by delta=11 modulo 20. Nejbližší dvě možnosti jsou
−9 a 11, obě mimo otevřený interval (−9,6). **Neexistuje tedy ani
libovolná dvojice povolených epsilon**, která by takovou přesnou
rovnost splnila. Nejde pouze o volbu nesprávných zlomkových částí.

## Oprava a důkaz

Protože všechny X_n jsou liché a
a^2=2^34+6a−9 modulo m, platí
X_(n+2)=2^34+6X_(n+1)−9X_n modulo m.
Po násobení 20/m a rozdělení na celou a zlomkovou část dostaneme

```
Y_(n+2) = floor(10 + 6(Y_(n+1)+epsilon_1)
                  − 9(Y_n+epsilon_2)) mod 20,
epsilon_1 = 20 X_(n+1)/m − Y_(n+1),
epsilon_2 = 20 X_n/m − Y_n.
```

Vnější podlaha před redukcí modulo celočíselné 20 je přesná a opravuje
rovnici. Lze také ponechat původní aproximaci; při požadavku na rovnost
je vhodnější podlahu výslovně uvést.

Podlaha dovoluje rozdíl −9,−8,...,5 modulo 20, tedy 15 možných třetích
intervalů pro každou první dvojici. Pět dalších je nemožných, což
vysvětluje alespoň 2000 prázdných buněk mezi 8000 možnými trojicemi.
Rovnost bez podlahy by nesprávně vyloučila ještě rozdíl −9.

## Reprodukce a rozsah

[verify_potency.py](../verify_potency.py) kontroluje opravený vzorec
na milionu nepřekrývajících se trojic a samostatně uvedený protipříklad
pomocí modulárních mocnin a přesných zlomků. Výsledek je v
[potency.json](../results/potency.json). Výpočet nenahrazuje intervalový důkaz.

Prohledány všechny vrstvy all2-prepre, all2-pre, all2, err2 a err2.textxt
z 1. 11. 2026, podle strany 551, sekce i obsahu vzorce. Nebyla nalezena
další oprava podlahy, rozsahu epsilon ani indexu v položce 2016.
Formulace nálezu se vztahuje právě k těmto doloženým podkladům.
[Anglický ASCII draft](../reports/C0006-quantized-equality-draft.txt) nebyl odeslán.
