# §4.6.3: věta G a úlohy 23–24

Stav **checked**, 4. listopadu 2026. Rozsah: nerovnost (50) na 478,
definice, věta G a její příklad pod tabulkou na 479, úlohy 23–24
na 483 a odpovědi na 695. Tyto stránky byly vizuálně přečteny.
Tabulka 1, číselné odhady na 477–478, nový příklad 5784689 a obecný
Scholzův problém nejsou tímto blokem uzavřeny. Nový nález žádný.

## 1. Označené řetězce a cíl transformace

Sčítací řetězec je rostoucí seznam `1=a_0<...<a_r=n`, v němž každý
nový člen vzniká součtem dvou dřívějších. Hvězdový řetězec vždy
používá poslední předchozí člen. Označený řetězec, v knize l^0-řetězec,
má některé členy podtržené a pro každý a_i platí

```
a_i = b + a_k,
```

kde b je poslední podtržený člen menší než a_i a k<i. Jeho nejmenší
možnou délku pro n označujeme l^0(n); obecné a hvězdové minimum jsou
l(n) a l*(n). Proto `l(n)<=l^0(n)<=l*(n)`. Číslo 1 musí být
podtržené, aby mohl vzniknout další člen; poslední n lze vždy
podtrhnout navíc. Pro n=1 podtrhneme jediný člen.

Pro kladné celé q položme `R(q)=2^q-1`. Věta G převádí označený
řetězec délky r pro n na takový řetězec délky r+n-1 pro R(n).
Výsledná nerovnost je

```
l^0(2^n-1) <= n-1+l^0(n).
```

## 2. Přesný důkaz konstrukce G

Nechť `1=b_0<...<b_t=n` je podposloupnost podtržených členů vstupu.
Do výstupu zahrneme všechny R(a_i), podtržené právě když a_i,
a pro každý interval po sobě jdoucích podtržených členů b,b'
také podtržená čísla

```
2^h R(b),  1<=h<=b'-b.
```

Vše seřadíme. První rodina obsahuje r+1 lichých čísel a druhá
n-1 sudých. Různé intervaly se nepřekrývají, protože jejich
pomocné členy leží ostře mezi R(b) a R(b'). V rámci každého
intervalu jsou zjevně různé. Délka tedy opravdu činí r+n-1.

Pomocné členy vznikají zdvojením svého předchozího podtrženého
členu: v jejich intervalu se nenachází žádné jiné podtržené
R(a_i), takže vložené nepodtržené členy tomu nepřekážejí.

Pro původní člen `a_i=b+a_k`, kde b je poslední podtržený člen,
je `1<=a_k<=b'-b`. Číslo `T=2^a_k R(b)` je proto pomocným
podtrženým členem. Platí

```
R(a_i) = T + R(a_k),   0<R(a_k)<T.
```

Číslo R(a_k) již ve výstupu je. Následující pomocný podtržený
člen, pokud existuje, je 2T; poslední nerovnost proto zaručuje,
že T je opravdu **poslední** podtržený člen před R(a_i).
V případě a_i=b' se interval uzavírá právě podtrženým R(b').
Tak je prokázána podmínka l^0, nikoli jen platnost obyčejného řetězce.

Při n=1 není žádný interval a výsledek je jediný člen 1, takže
není třeba tuto okrajovou možnost vylučovat.

**Úloha 23:** zvolíme minimální hvězdový řetězec pro n a podtrhneme
všechny jeho členy. Ve výstupu jsou potom také podtržené všechny
členy, takže je hvězdový. Dostáváme přesně Brauerovu nerovnost
`l*(2^n-1)<=n-1+l*(n)`, tedy (50). Samotné porovnání l^0 a l*
by k této silnější levé straně nestačilo; rozhoduje vlastnost konstrukce.

## 3. Obecný základ B: úloha 24

Pro celé B>1 definujme

```
R_B(q) = (B^q-1)/(B-1) = 1+B+...+B^(q-1),  q>=1.
```

Je to číslo s q jedničkami v zápisu o základu B. Zvolme označený
řetězec `1=c_0<...<c_h=B`, s podtrženým koncovým B. Vstup pro n
zůstává `a_0,...,a_r` s podtrženými `b_0,...,b_t`. Použijeme členy

```
R_B(a_i),                                  0<=i<=r,
c_k B^(s-1) R_B(b_j),  0<=j<t, 1<=s<=b_(j+1)-b_j, 1<=k<=h.
```

První rodinu podtrháváme podle a_i, druhou podle c_k. To je přesně
odpověď 24, s přejmenováním lokálních indexů kvůli přehlednosti.

Všechny pomocné členy pro interval b,b' jsou větší než R_B(b)
a menší než R_B(b'). Uvnitř intervalu mají pořadí nejprve podle s,
potom podle k: `2<=c_k<=B`, a tudíž poslední člen jedné skupiny
předchází prvnímu členu další. Ke kolizi s hlavní rodinou nedojde:
R_B(a) je modulo B rovno 1; pomocné členy se s>=2 jsou rovny 0,
a při s=1 jsou rovny c_k modulo B, tedy nikdy 1. Máme přesně
r+1+(n-1)h různých členů.

Pro pomocný člen c_k Q, kde `Q=B^(s-1)R_B(b)`, je předchozím
podtrženým členem c_j Q, kde c_j je předchozí podtržený člen
řetězce pro B. Rozdíl je c_v Q pro dřívější c_v. Je přítomen
buď v témže bloku, nebo při c_v=1 jako jeho první člen Q:
ten pochází z předchozího bloku, případně je samotné R_B(b).
Ostatní podtržené hlavní členy leží až mimo interval b,b'.

Pro hlavní člen a_i=b+a_k máme identitu

```
R_B(a_i) = B^a_k R_B(b) + R_B(a_k).
```

První sčítanec T je podtržený konec příslušného bloku (c_h=B).
Druhý je dřívější hlavní člen a splňuje `0<R_B(a_k)<T`.
Další pomocný člen, pokud existuje, je nejméně 2T, protože c_1=2.
Proto je T posledním podtrženým členem před R_B(a_i).
Výstup je l^0-řetězec. Po volbě minimálních vstupů získáme

```
l^0(R_B(n)) <= (n-1)l^0(B)+l^0(n).
```

Pro druhou část zvolíme B=2^m s celým m>=1. Zdvojování i obvyklá
dolní mez dávají `l^0(2^m)=m`. Rozklad
`2^(mn)-1=(2^m-1)R_(2^m)(n)` a faktorová konstrukce dávají

```
l(2^(mn)-1) <= l(2^m-1)+m(n-1)+l^0(n).
```

To je požadovaná nerovnost; případ n=1 je zahrnut. Netvrdíme, že
výstupní řetězce jsou minimální nebo že tato mez vždy zlepší G.

## 4. Původní doklady, příklad a známé opravy

Příklad na 479 začíná řetězcem `1,2,4,5,8,10,12,18`, v němž jsou
podtržené 1,2,4,8,18. Konstrukce dává všech 25 vytištěných čísel
a právě tři nepodtržené výstupy: 31,1023,4095. Bylo ověřeno celé
pořadí i všechna podtržení; pouhá rovnost posledního čísla nestačí.

Brauerův původní článek *On Addition Chains*, Bull. AMS 45 (1939),
736–739, je uložen z [kopie původního článku na univerzitním serveru](https://wwwhomes.uni-bielefeld.de/achim/Brauer_on_addition_chains_1939.pdf).
Všechny čtyři stránky přečteny textově i vizuálně. Jeho (6)–(8)
na 738 jsou právě hvězdová konstrukce úlohy 23; v (6) jsou neostré
nerovnosti, navzdory OCR. Označená varianta a zobecnění pro
B=2^m jsou v Hansenově původním Satz 3 na 135–136, který byl
vizuálně přečten již v předchozím bloku. Výše uvedený důkaz pokrývá
i obecnější B požadované Knuthem. Bibliografické připsání souhlasí.

Šest vrstev errat je zaznamenáno v `sources/powers-basic-errata.txt`.
Na 479 jsou známé změny 27. 12. 2003 (slovo „some“), 17. 9. 2005
(nahrazení již neaktuální otázky l=l^0 a přidání příkladu 5784689)
a 24. 9. 2024 (nový závěr odstavce). Konstrukce G ani odpovědi
23–24 se nemění. Důkaz existence a minimality nového číselného
příkladu bude veden s úlohou 42, nikoli předstírán zde.

Při této kontrole byl doplněn záznam známé opravy z 18. 12. 2000
v předchozí úloze 19(a): v zadání na 483 chybí faktor p za znaménkem
součinu. `powers-hansen.md`, jeho manifest a stav úlohy nyní tuto
opravu uvádějí. Jde o doplnění evidence, žádný nový nález ani důvod
opakovat úspěšné matematické kontroly.

## 5. Přesné testy

`verify_powers_scholz.py` nezávisle generuje všechny přípustné dvojice
řetězce a podtržení do dané délky. Každý další člen je součet
posledního označeného členu a libovolného dřívějšího; obě volby
jeho označení se projdou. Koncový člen požadujeme označený.
Validátor naproti tomu vyhledává poslední označený člen přímo
v hotovém seřazeném seznamu a ověřuje, že rozdíl již existuje.
Počet členů, absence duplicit a cílová hodnota mají samostatné kontroly.

- Binární blok: všech **52 610** označených řetězců délky nejvýše 7,
  celkem 1 484 975 výstupních čísel; zvlášť hvězdová vlastnost
  všech plně podtržených vstupů a přesný tištěný příklad.
- Radixový blok: 634 vstupů délky nejvýše 5 a 92 řetězců pro základ
  délky nejvýše 4. Celkem **58 328** transformací, z nich 57 694
  s B>2, cíle až 125 bitů. Test zahrnuje různá platná podtržení
  téhož číselného řetězce, nikoli pouze minimální řetězce.

Oba bloky prošly napoprvé, bez opakování: 5.881008849 s a
9.899042265 s, celkem **15.780051114 s**. Session 9569,
PID 1352059/1352069, limit 240 s na blok, exit 0.
Výstupy jsou v `results/powers-scholz.json` a `.log`.
Obecný důkaz je výše; konečné výsledky ho nenahrazují.
