# V2-C0099: chybějící dělení základem v přesném dělení zprava

**confirmed**,2.11.2026. TAOCP2,3.vydání,1.dotisk1997, §4.3.1,
odpověď40,str.629, řádek6–7 odpovědi. Originál vizuálně přečten:
[629](../images/vol2-p629.png). Zadání284 vyžaduje přesné dělení
2n-místného čísla n-místným číslem. Chyba je v explicitní rovnici pro u',
ne v hlavní myšlence obousměrného dělení.

Po q_0=v' u_0 mod b tisk uvádí `u'=u-q_0 v`, potom další číslici
`q_1=v' u'_0 mod b`. První rovnice činí nejnižší číslici u'_0 vždy nulovou,
takže doslovný postup má q_1 vždy0. Správná aktualizace je
`u'=(u-q_0 v)/b`. Kniha označuje číslice podílu w_i, zde používáme q_i.

Přesný svědek splňuje i délky zadání:

```
b=2, n=4,
U=165=(10100101)_2,
V=15=(1111)_2,
Q=11=(1011)_2, U=VQ.
```

V je liché a jeho inverze modulo2 je1. Dostaneme q_0=1. Tištěné u'=150
je sudé, takže q_1=0, ale správný druhý bit Q je1. Po opravě je u'=75,
což dává q_1=1. Záměnu nelze vysvětlit jen vynecháním vedoucích nul;
jde o chybějící posun nejnižšího místa.

Obecná identita U=V(q_0+bQ_1) přímo dává(U-q_0V)/b=VQ_1.
Podrobná správná konstrukce a kontrola nezávislým celočíselným orákulem
jsou v [classical-exact.md](classical-exact.md) a
[JSON](../results/classical-exact.json), blok missing_shift.
Předtisk Krandick–Jebelean1994,str.6 také výslovně dělí základem.

Všechny čtyři vrstvy all2-prepre,all2-pre,all2,err2 a uložený aktuální
err2 TeX prohledány podle629,answer40,exact division a výrazu aktualizace.
Relevantní známá změna28.12.2000 pouze nahrazuje bibliografii odpovědi40;
na stejné straně jsou také změny41 a42, které tuto rovnici neopravují.
Originál změny2000 viz `images/classical-errata-all2-prepre-38.png`.

Poslední fyzický dotisk, priorita a případná odměna neověřeny.
Návrh hlášení zůstává neodeslaný. Silnější uniformní časová mez celé
úlohy40 je oddělená otevřená otázka, není součástí tohoto nálezu.
