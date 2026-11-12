# V2-C0034: výjimka periody2 v odpovědi20

**Confirmed**,1.11.2026. §3.3.3-20, poslední vzorec na
tištěné str.574 a definice na575 ([574](../images/vol2-p574.png),
[575](../images/vol2-p575.png)). Oba skeny přečteny vizuálně.

Parametry a=1,c=1,m=2 dávají plnou periodu0,1. Událost
`X_n>X_(n+1)>X_(n+2)` má pravděpodobnost0. Vytištěný
vzorec však dává1/8: všech devět součtů S1,...,S9 je0,
všechny pilovité funkce jsou0 a zůstane `1/4−1/(4m)`.

Chyba je omezena na periodu2. Pišme s(x)=(ax+c) mod m,
x' pro stav se s(x')=0 a x'' pro stav se s(s(x''))=0.
Při rozvinutí součinu dvou indikátorů poklesu mají
delta členy tvar

```text
(−[x=0]+[x=x'])/2,
(−[x=x']+[x=x''])/2.
```

Jejich součin má součet−1/4 pro m>2. Pro m2 se však
x''=0 a součet je−1/2. Ve vytištěném vzorci tedy chybí
`−[m=2]/(4m)`, nebo je třeba výslovně předpokládat m>2
a případ m2 uvést zvlášť.

Přímé počítání trojic ve všech2133 plnoperiodových
modelech s m<=60 potvrdilo, že jedinou odchylkou je
(a,m,c)=(1,2,1); obecný rozvoj vysvětluje výjimku
bez spoléhání na konečnou kontrolu. S9 i ostatní členy
souhlasí. Viz [výsledky](../results/theoretical-tests.json).

Všechny čtyři vrstvy errat a aktuální TeX prohledány1.11.2026
podle574,575, answer20, descending a permutation. Žádná
odpovídající oprava nenalezena. Nejnovější fyzický dotisk
a prvenství neověřeny; hlášení neodesláno.
