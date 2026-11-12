# C0160: předtest Lucasovy metody chybně vylučuje hraniční prvočísla

**Stav:** confirmed v dostupném skenu; třetí vydání, první
dotisk (1997), §4.5.4, odpověď 15, str. 660, odstavec Note.
Nejde o vyvrácení hlavní věty úlohy 15.

Poznámka volí P=1, D=1−4Q a požaduje `gcd(N,QD)=1`.
Pokud tato podmínka selže, tvrdí, že už víme, že N není
prvočíslo, s výjimkou `|QD|>N`. Ve skutečnosti je nutné
zahrnout i rovnost.

Přesný protipříklad:

```
P=1, Q=-1, N=5,
D=P²-4Q=5, QD=-5,
gcd(N,QD)=5>1, ale |QD|=N, nikoli |QD|>N.
```

P,Q jsou nesoudělná celá čísla a 5 je prvočíslo
(stačí zkusit jediného možného prvočíselného dělitele 2).
Pravidlo v závorce by je nesprávně prohlásilo za složené.
Další příklad je N=3,Q=1,D=−3. Navíc pro povolené Q=0
je QD=0 a nefungovala by ani samotná změna > na >=.

Nejpřesnější místní oprava je: ze selhání nesoudělnosti
plyne složenost jen tehdy, když `gcd(N,QD)<N`.
Ekvivalentně se závorka může změnit na výjimku
`gcd(N,QD)=N`. Tím se ošetří i Q=0.

Sazba na 660 byla zobrazena a znak > přečten vizuálně.
Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2`
i aktuální zdroj `err2.textxt`; žádná relevantní oprava
nebyla nalezena. Důkaz, testované rozsahy a zdroje jsou
v [primality-lucas.md](primality-lucas.md),
`results/primality-lucas.json` a `sources/primality-lucas.json`.
Novější fyzický tisk a prvenství neověřeny. Nic neodesláno.
