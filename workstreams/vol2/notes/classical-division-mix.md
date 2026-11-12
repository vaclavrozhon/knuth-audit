# §4.3.1: úplný program MIX D a jeho čas

Uzavřený instrukční blok2.11.2026. Originály273–275 a626 byly vizuálně
přečteny, včetně doplnění D1/D8 v odpovědích25/26. Matematický algoritmus
D a jeho konečné kontroly jsou již v [division.md](division.md) a nebyly
opakovaně spouštěny. Tento blok přidává skutečné instrukce, znaménka,
přenosy, všechny důležité vzácné větve a přesné časování.

Základ jednoho bajtu MIX je beta, velikost slova `b=beta^5`. Dělíme
nezáporné U o nejvýše m+n slovech kladným V o n slovech, `n>=2,m>=0`.
Nejvyšší slovo V je nenulové. Normalizační faktor d násobí oba vstupy
tak, aby nejvyšší slovo dV bylo alespoň b/2; dV má stále n slov.
MIX má sudé beta, takže starost o lichý základ z errat2026 zde nenastává.
Čísla řádků níže jsou původní1997; v knize po opravě D1 mají další řádky
čísla o4 vyšší.

## Verze a úplný přepis

[classical-division.mix](../sources/classical-division.mix) spojuje
Program D s odpověďmi25 a26. Tři tečky v normalizaci jsou doplněny přesně
podle odpovědi13. Zahrnuje tyto zveřejněné změny:

- 23.1.1998: D1 používá `d=floor(b/(v_(n-1)+1))`, s výjimkou přetečení
  při `v_(n-1)=b-1`; celé nové řádky002–010.
- 19.3.1998: původní045 má `LDA U+N-1,2` místo U+B-1,2.
- 4.4.2011: DIV v novém008 dělí TEMP, tedy v_(n-1)+1; původní chybný
  operand je v opravě2011 citován jako V+N+1, v přepisu1998 byl V+N-1.
  Zamýšlená cílová instrukce DIV TEMP je jednoznačná.
- 4.4.2011: D8 snižuje registr1 a testuje J1NN (původní106/107,
  nová110/111), nikoli registr2. Komentář j+1 se mění na j-1.

Komentář `quotient=b` se od2005 čte `quotient>=b`. Nemění instrukci:
DIV nastaví overflow pro každý neuložitelný podíl.

## D1 a D8: úlohy25,26,27

Pro vedoucí číslici a<b-1 uloží D1 do TEMP hodnotu a+1. rAX=(1,0)
představuje b, takže DIV TEMP vypočte správné d. Při a=b-1 součet a+1
přeteče; JOV přeskočí dělení a uloží d=1. Neplatný vstup a=0 zachytí
přetečení DIV jako DIVBYZERO; takový vstup neleží v oboru algoritmu.

Je-li d=1, stačí vytvořit dodatečnou nulu u_(m+n). Jinak se nejprve
násobí V a pak U krát d, stejně jako v odpovědi13. Po V je rX=0,
protože dV<b^n; proto jej další smyčka nemusí znovu nulovat. U může
mít nenulové nové nejvyšší slovo, které se uloží samostatným STX.

D8 je krátké dělení shora dolů, nyní v paměti na místě. Před každým
DIV je zbytek v rA menší než d, takže nedojde k přetečení; SLAX5 přesune
nový zbytek z rX do rA. Dlouhé dělení předtím vrátí
`dU mod dV = d(U mod V)`, což dokazuje úlohu27 i přesnou dělitelnost.
Pokud smyčka D8 skutečně proběhne, na konci je rAX=0. Při přímém odchodu
pro d=1 není registr rX tímto argumentem vynulován; výstupní smlouva
podílu a zbytku jeho hodnotu nevyužívá. Závěrečnou větu odpovědi26 o
rAX=0 proto používáme jen na cestě přes vlastní dělení, které ta věta
bezprostředně popisuje.

## D3: odhad číslice podílu v omezených registrech

Nechť u je aktuální (n+1)-slovné okno a v=dV normalizovaný dělitel.
Invariant `0<=u<bv` byl obecně dokázán dříve. Z něj plyne, že nejvyšší
slovo u_n je nejvýše a=v_(n-1). Bez overflow vypočte DIV běžný odhad
h a zbytek r z horních dvou slov. Při overflow je nutně u_n=a;
program nastaví h=b-1 a r=u_(n-1)+a. Je-li tento součet alespoň b,
je druhý test automaticky splněn, protože `h v_(n-2)<b^2<=br+u_(n-2)`.
JOV tedy může ihned přejít do D4 bez uložení r mimo rozsah slova.

Jinak porovnává dva součiny dlouhé dvě slova: `h v_(n-2)` a
`r b+u_(n-2)`. Nejprve porovná horní slova, při shodě dolní. Snížení
h o1 zvýší r o a; případné přetečení r znovu dovolí okamžitý přechod
na D4. Každé snížení je podloženo tím, že h je příliš velké, takže
nesníží horní odhad pod správný podíl q. Po D3 `q<=h<=q+1`.

LDA U+N,2(1:5) v prvním řádku D3 zahodí případné znaménko záporné
nuly, aby měl následný DIV nezáporný podíl. Simulátor toto znaménko
při mezikrocích zachovává; nula nebyla předčasně normalizována.

## D4–D6: znaménková aritmetika a výpůjčky

Při postupném odčítání h krát číslice v_i označme k přenos do aktuálního
řádu; `-(b-1)<=k<=0`. Program drží `c=k+1` v rX a potom v CARRY.
Po MUL a SLC5 jsou v registrech horní a dolní části **záporného**
součinu -h v_i. Přičtení c k dolní části může přetéct jen záporně;
DECX tehdy sníží horní část. Po těchto krocích stále platí přesná rovnost
`b*rX+rA=-h v_i+c`.

Následující ADD U a ADD WM1 k tomu přičtou u_(i+j)+b-1. Součet je
`T+b`, kde `T=u_(i+j)-h v_i+k` je matematická odčítaná hodnota.
Případné přetečení této dvojice instrukcí je kladné a je nejvýše jedno;
INCX je přenese do horní části. Výsledný spodní registr je `T mod b`
a horní je `floor(T/b)+1`, právě další zakódovaný přenos c. Dolní nula
může mít záporné znaménko, jak upozorňuje kniha.

Opakování pro i=0,...,n používá v_n=0. Protože h=q nebo q+1, celé okno
po odečtení leží mezi -v a v. Konečné rX je tedy0 při záporném výsledku
a1 při nezáporném; JXP správně rozhodne o D6. V záporném případě je
uloženo `b^(n+1)+(u-hv)`. Přičtení v v D6 má zaručený přenos z poslední
pozice, který cyklus ukončí a zruší původní výpůjčku. Nevzniká neomezené
propagování do další paměti. Výstupní h se sníží o1 a zbytek je správný.

Tím je doložena instrukční realizace všech matematických invariantů,
nejen konečná shoda testovaných výsledků.

## Úloha30: podíl v již nepotřebném místě dělence

Q může začínat na U+n. Po D4 není původní slovo u_(j+n) dále potřeba,
proto tam D5 uloží q_j. Při D6 se musí vynechat poslední slovo i=n:
změna původního094 z J1NP na J1N to zajistí. Přenos z n nízkých slov
je v D6 zaručen, a tak se závěrečná podmínka skutečně vykoná; větev
JNOV nemůže z poslední nízké pozice odejít zpět a přepsat q_j.
Zbytek na konci zůstane ve slovech U,...,U+n-1. Této úpravě odpovědi30
odpovídají i cílené běhy s opravou podílu. Jiná část odpovědi30, týkající
se násobení, obsahuje [chybný index C0097](C0097-multiplication-alias.md).

## Přesný čas a tištěná aproximace

M=m,N=n jsou délky uvedené v programu. Nechť E je počet snížení h
v řádcích047–049, K,K' počty návštěv070/074. Pokud dočasně vynecháme
vzácné větve (overflow odhadu, rovnost horních slov při porovnání a D6),
pro d=1 a a<b-1 vychází přesně

```
T0 = 29(N+1)(M+1) + 45(M+1) + 28E + 36 + K + K'.
```

Vnitřní D4 má29 cyklů plus jednotlivé návštěvy070/074. Ostatní pravidelné
kroky na jednu číslici podílu mají45. Jedno snížení odhadu přidává28.
Příprava a závěr mají36; změna D1 z1998 přidala proti původní verzi5.
Dosazení přibližných `K+K'=(N+1)(M+1)` a `E=M/2` dá
`30MN+30N+89M+111`, tedy opravuje původní106 v souladu s erratem1998.

Při d>1 je další přesný čas
`66N+23M+K_V+K_U+4`, kde K_V,K_U počítají návštěvy INCX při normalizaci
obou vstupů. Dosazení `(K_V+K_U)~(M+2N)/2` dá
`67N+23.5M+4`, tedy známou opravu235M z2011. Odhady přenosů nejsou
považovány za přesný průměr pro libovolnou distribuci vstupů.

Pro úplnou reprodukci včetně vzácných větví ještě definujme:
O = počet overflow při prvním DIV D3 (návštěvy044),
R = počet přetečení součtu r+a v052,
H = počet porovnání dolních slov v059,
F = počet těchto porovnání, která ukončí test bez snížení h,
J = počet vstupů do D6,
P = celkový počet iterací sčítání v D6 (návštěvy087),
C = počet jeho přenosů (návštěvy093),
B = indikátor a=b-1 v původním vstupu. Úplná korekce k T0 je

```
-14B + 9O -17R +3H +F +6J +10P +C,
```

plus uvedený příplatek normalizace pro d>1. Bez aliasu P=(N+1)J,
s aliasem P=NJ. Každý člen byl odvozen z rozdílu větví instrukčního
seznamu; všechny běhy porovnávají tuto formuli s nezávislým účtováním
jednotlivých provedených instrukcí.

## Výsledky a meze

[verify_classical_division.py](../verify_classical_division.py) a
[classical-division.json](../results/classical-division.json):
900 běhů pro beta64,100,256, m0–4,n2–6; z nich450 s d>1 a450 s d=1.
Přesný výsledek i každý dílčí zbytek se porovnává s celočíselným divmod.
Čítače a přesná časová formule souhlasí ve všech případech.

Dalších36 cílených běhů obsahuje18 vstupů do větve overflow odhadu,
30 snížení h,36 porovnání dolních slov,18 přičtení zpět v D6 a6 běhů
s přetečením r+a. Polovina cílených běhů používá společné místo pro podíl
a horní část dělence. Samostatných375 běhů ověřuje opravený alias M.

První běh dokončil900 případů, ale závěrečná kontrola pokrytí cíleného
bloku zjistila, že zvolený vstup nevyvolal overflow r+a. Aritmetická ani
časová kontrola neselhala. Po změně cíleného vstupu se znovu provedl pouze
tento blok a dosud neprovedené aliasy; uložených900 případů se neopakovalo.
Výsledný obnovený proces skončil s kódem0. Limit instrukcí v obecném
simulátoru byl doplněn jako volitelná hodnota; původní výchozí1000 zůstává.

Všechny čtyři errata znovu prohledány pro273–275,625–627 i příslušný
obsah. Vizuálně přečteny all2-prepre16/17/37/38, all2-pre7/14 a relevantní
současná oprava282 z2005 v historickém seznamu. Tento blok nenahrazuje
historický audit citací ani starší důkaz C0001; poslední fyzický dotisk
zůstává neověřený.
