# V2-C0114: interpretace nezměněné rutiny při dělení nulou

**candidate**, 2. listopadu2026. §4.5.1-8, odpověď639; stejná
[původní stránka](../images/vol2-p639.png) obsahuje také odpověď4.

Odpověď8 uvádí x/0=sign(x)*infinity pro konečné nenulové x
„without change to the algorithms described“. Odpověď4 však
výslovně předepisuje při nulovém čitateli dělitele chybové hlášení.
Doslovná implementace této kontroly proto na(1/1)/(0/1) hlásí
dělení nulou a nevrátí1/0. Je nutné zvláštní hodnoty rozlišit
před původní rutinou nebo změnit obsluhu nulového dělitele.

Neoznačujeme to za potvrzenou matematickou chybu: věta může
mínit aritmetické jádro po přirozené změně obsluhy výjimek.
Zamýšlená pravidla lze konzistentně implementovat, jak dokládá
`extended_op` a144 případů v `results/rational-basic.json`.
Navrhované upřesnění by mělo výslovně vyjmout původní chybové
hlášení. Hodnotu sign(0) nepoužíváme jako předpoklad pro nález;
už explicitní chybová větev stačí k uvedenému rozdílu chování.

Čtyři vrstvy errat prohledány, odpovídající upřesnění nenalezeno.
Poslední fyzický dotisk a autorův zamýšlený rozsah věty neověřeny;
žádné hlášení neodesláno. Další matematické podrobnosti jsou v
[rational-basic.md](rational-basic.md).
