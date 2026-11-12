# V2-C0008: konstantní maximální cifra v přidané §3.2.2-38

**Stav: confirmed, 1. listopadu 2026.** Jde o malou chybějící výjimku
v úloze přidané veřejnými erraty 21. dubna 2019 na str. 40 a 559.
Obvyklý důkaz pro nekrajní ciferné posloupnosti zůstává správný.

## Přesné zadání a protipříklad

Úloha uvažuje libovolnou periodickou posloupnost cifer x_n v základu b,
tedy celá 0<=x_n<b, s periodou lambda. Definuje celé číslo X z jednoho
bloku cifer, d=gcd(X,b^lambda-1), m=(b^lambda-1)/d a X_0=X/d.
Rekurence X_(n+1)=bX_n mod m má splňovat |X_n/m-x_n/b|<1/b.

Přímý render původního PS potvrzuje slovo libovolná i přísnou nerovnost:
[zadání, strana souboru 4](../images/all2-pre-p04-direct.png).
[Odpověď, strana souboru 13](../images/all2-pre-p13-direct.png) navíc
tvrdí bX_n=m x_n+X_(n+1) pro všechna n.

Položme b=2, lambda=1 a x_n=1 pro všechna n. Potom

```
X=1, d=1, m=1, X_0=1, X_1=X_2=...=0.
|X_0/m-x_0/b|=|1-1/2|=1/2,
bX_0=2, ale m x_0+X_1=1.
```

Přísná nerovnost i identita v odpovědi selžou. Počáteční hodnota X_0=m
také neleží v normalizovaném intervalu [0,m). Její předběžná redukce
modulo m problém neopraví: pak je chyba stále přesně 1/2.
Pro b=10 a všechny cifry 9 je po prvním kroku chyba dokonce 9/10,
takže by nestačilo nahradit `<` znakem `<=`.

## Oprava a úplný důkaz zbývajícího případu

Stačí vyloučit posloupnost x_n=b-1 pro všechna n. Označme B=b^lambda-1
a R_n celé číslo tvořené cyklicky otočeným blokem
x_n,...,x_(n+lambda-1). Rotace splňuje

```
b R_n = B x_n + R_(n+1).
```

Protože gcd(b,B)=1, mají všechny R_n stejný největší společný dělitel
d s B. Není-li blok celý maximální, je 0<=R_n<B pro všechna n.
Po dělení d tedy X_n=R_n/d leží v [0,m), splňuje předepsanou rekurenci
i identitu z odpovědi a

```
X_n/m-x_n/b = X_(n+1)/(bm),  0 <= X_(n+1)/(bm) < 1/b.
```

Tento důkaz pokrývá i samé nuly (m=1, X_n=0), pokud připouštíme
triviální modul 1. Požadujeme-li m>1, je přirozené vyloučit obě konstantní
krajní posloupnosti.

## Primární zdroj a reprodukce

Odkazovaný preprint z roku 2004 na plala.or.jp nebyl dostupný; netvrdíme,
že jsme jej přečetli. Dostupná primární publikace autorů Hiroshi a Naoya
Nakazawa [US20100030829A1](https://patents.google.com/patent/US20100030829A1/en),
odstavec 0009, obě krajní konstantní posloupnosti výslovně vylučuje před
převodem na zlomek v (0,1). To podporuje navrženou podmínku, ale samotný
nález je doložen výše uvedeným přesným protipříkladem. Archiv a metadata:
[nakazawa-sources.json](../sources/nakazawa-sources.json).

[Přesný program](../verify_shuffling_boundaries.py) ověřil opravený
důkaz na všech 14 999 nekrajně maximálních blocích délek 1–5 pro b=2–6,
celkem 158 081 přechodech. Rekurenci porovnává s nezávislou rotací
cifer a racionální čísla počítá přesně. U všech 25 vyřazených bloků
potvrzuje rovnost chyby s 1/b při n=0.
[Výsledky](../results/shuffling-boundaries.json).

Prohledány všechny vrstvy all2-prepre, all2-pre, all2, err2 a err2.textxt
podle str. 40/559, Nakazawa, čísla 38 a konstrukce. Novější oprava
výjimky nebyla nalezena; starší all2-prepre tuto úlohu ještě nemá.
Novější fyzický dotisk ani prvenství neověřeny.
[ASCII draft](../reports/C0008-universal-max-digits-draft.txt) nebyl odeslán.

Dodatečná vizuální kontrola 1.11.2026: stejné zadání je na
[str.40 náhledu osmého digitálního vydání, červenec 2026](../images/publisher-preview-p040.png).
[Tiráž](../images/publisher-preview-copyright.png) a
[metadata](../sources/publisher-preview-9780133488791.json) uloženy.
