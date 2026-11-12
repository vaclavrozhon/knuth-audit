# V4A-C0003 — funkčnost podsítě v důkazu Theorem M

Candidate, střední dopad; §7.1.4 str.214–215 / file231–232.
Původní sazba obou stran prohlédnuta. Jde o mezeru v předloženém důkazu,
nikoli protipříklad samotné horní meze B(f).

Na214 stačí globální podmínka: každému vstupu x odpovídá právě jedno
ohodnocení všech vodičů, konzistentní s funkcemi modulů. Důkaz potom tvrdí,
že levá část při řezu definuje funkci A(b), která závisí jen na levých x,
a na215 posílá pravé straně její celou tabulku. Tato implikace není obecná.

Tři moduly, každý s vlastním x_i, mohou mít po jednom vodiči v obou směrech
na každém rozhraní. Označme vpřed u,a a vzad v,b. Zvolme totální booleovské
funkce modulů:

```
M1: u = v                      (x1 se ignoruje)
M2: a = u,  v = u XOR b         (x2 se ignoruje)
M3: b = a XOR x3,  f = a
```

Z u=v=u XOR b plyne b=0. Pak a=x3 a u=v=a=x3. Pro každý vstup(x1,x2,x3)
je tedy všech pět signálů určeno jednoznačně; síť splňuje vytištěnou definici.

Při odříznutí M3 však rovnice levé části pro b=0 dovolují a=0 i a=1,
zatímco pro b=1 nemají řešení. Funkce A(b) tedy neexistuje. Navíc pro stejné
levé vstupy a stejné skutečné b=0 musí výstup a jednou být0 a jindy1 podle
x3; nelze potíž vyřešit volbou A(0) nezávislou na pravých vstupech.

Důkaz potřebuje silnější předpoklad funkčnosti podsítí nebo jinou redukci.
Možný implicitní význam slova „network“ a platnost meze zůstávají otevřené;
proto candidate, bez tvrzení o potvrzené chybě věty. Žádný program použit.

6.11.2026 prohledány all4a-pre/all4a/err4a/all4f1/err4f1. Fasciklový offset132:
zde214/215 odpovídá F1p82/83. Doplněk214 z8.6.2012 přidává atribuci
McMillanovi. Oprava215 z19.5.2025 mění formulaci příkladu před(34) na
„We can make M_k compute“ a rozšiřuje úlohu45. Ani jedna nepřidává podmínku
funkčnosti řezů a neopravuje uvedený krok A(b). Relevantní F1 položka chybí.

Doklady: `images/file231.png`, `images/file232.png`,
`sources/file231-270-ocr.txt`, `sources/file231-270.pdf`.
