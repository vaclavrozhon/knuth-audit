# V2-C0176: Fibonacciho krok nezachovává vytištěný invariant

**Stav: confirmed.** Odpověď §4.5.4-40(b),666, předpokládá
`binom(2m,m) mod n!=0` a `binom(2(m+s),m+s) mod n=0`,
pro s=F_j,s'=F_(j+1). Její aktualizace může druhou podmínku zrušit.
Původní sazba666 a416 byla přečtena.

Vezměme n=35; předchozí větev má b=4,4! mod35=24,
8! mod35=0,gcd(4!,35)=1. Základ z odpovědi je A=2^128.
Počáteční stav s=5,s'=8,m=8 má m=F_(j+1) a splňuje:

```
binom(16,8)=12870       =25 (mod35),
binom(26,13)=10400600   = 0 (mod35).
```

Použijme už opravené přiřazení s'←r z18.5.2002.
Nové s=3,s'=5 a testuje se

```
binom(22,11)=705432     = 7 (mod35).
```

Proto se m zvětší na11. Nový horní konec m+s=14 ale dává

```
binom(28,14)=40116600   =20 (mod35),
```

což odporuje deklarované druhé podmínce. Všechny mocninné registry
a extrakce byly nezávisle zkontrolovány; A je větší než2^28.

Příčinou je použití binomického testu mimo interval, v němž je
jmenovatel (z!)² nesoudělný s n. Vlastní oprava, která stále
používá O(log n) operací a pevný počet registrů, je v
[shamir-factor.md](shamir-factor.md),§3–4: zvolit s<=b<s',
m=b−s, horní konec b a test za b nahradit známým true.

Nález se týká invariantu a chybějícího omezení inicializace.
Nejde o protipříklad hlavní Shamirově větě, ani o tvrzení,
že tištěný postup na n=35 nutně vrátí špatný faktor.

Všechny čtyři vrstvy errat a err2.textxt prohledány3.11.2026;
jediná relevantní oprava666 z18.5.2002 mění s←r na s'←r a tento
problém neřeší. Pozdější fyzický dotisk a priorita neověřeny.
Anglický návrh zůstává neodeslán.
