# §1.3.1-17(b): jiná podmínka povolených zápisů

Kořenová revize 2. listopadu 2026, V1-X0724. Root přímo přečetl
původní142/508 a původní důkaz X0678.
Tento doplněk posuzuje dosud netestovaný návrh z předání agenta.
Nový program má nejhorší čas6013u, ovšem zapisuje i za N.
Není náhradou staršího programu zachovávajícího každou buňku
mimo0..N. Globální optimalita úlohy17(b) zůstává otevřená.

V zadání se požaduje vynulovat0..N, 0<=N<=2999, s počátkem3000;
výslovná věta o zachování ostatní paměti zde není. Dřívější X0678
splňuje silnější podmínku zachování celé paměti mimo0..N. Zde
výslovně zkoumáme slabší podmínku: dodatečný zápis do N+1..2999
je povolen. Přenos řízení na3999 končí měřený program; HLT se
nepožaduje. Radix b je počet hodnot bajtu, 64<=b<=100, a u je
knižní jednotka instrukčního času. Počáteční registry a paměť
jsou libovolné kromě rI2=N a zavedeného kódu.

```text
3000 ENT1 0
3001 STZ 0,1
3002 STZ 1,1
     ...
3994 STZ 993,1
3995 INC1 994
3996 MOVE 0(6)
3997 DEC2 1000
3998 J2NN 3001
3999 [pokračování]
```

Program má999 instrukcí a nevyžaduje žádná pomocná data.
Na začátku k-tého průchodu, číslováno od0, jsou rI1=1000k
a rI2=N−1000k. Přímé zápisy vynulují1000k..1000k+993.
INC1 posune cíl na1000k+994 a MOVE přenese šest již nulových
slov0..5 do1000k+994..1000k+999. Po něm je rI1=1000(k+1).
DEC2 a J2NN opakují průchod právě když zbývající N−1000(k+1)
je nezáporné. První průchod vytvoří i vlastní nulový zdroj,
takže nezávisí na původním obsahu paměti.

Počet průchodů je q=floor(N/1000)+1. Zapsány jsou přesně
adresy0..1000q−1, všechny kladnou nulou; adresy od1000q dále
se nemění. Protože1<=q<=3, kód od3000 zůstává nedotčen.
Všechny adresy i mezihodnoty indexů jsou platné již v radixu64.
Pro původní−0 v rI2 odečtení1000 dává−1000 a závěr je stejný.

Každý průchod stojí994*2+1+(1+2*6)+1+1=2004u. Včetně
prvního ENT1 je přesný čas

```text
T_block(N)=1+2004*(floor(N/1000)+1).
```

Nejhorší čas je6013u. Starší silnější varianta X0678 má čas
`2N+3 floor(N/994)+7` a maximum6014u. Srovnání maxim o1u je
platné jen při společném slabším požadavku, kdy obě varianty
vyhovují. Nová varianta není rychlejší pro každý vstup: například
proN=0 stojí2005u oproti7u a zapisuje navíc999 buněk.
Není doloženo, že slabší interpretace je jediným záměrem autora.

Samostatný checker nového programu ověřuje přesný výstup,
množinu všech zápisů, zachování zbytku paměti, indexy i čas
na hranicích průchodů ve všech37 radixech a obě nuly na vstupu.
Všech481 nových kontrol prošlo jednou; výstup je uložen v
results/mix-block-zeroing-relaxed.json.
Zobecnění plyne z výše uvedeného invariantu, ne z konečného testu.
Staré úspěšné testy se neopakují. Čtyři vrstvy errat a jejich
již provedená kontrola16/17 jsou převzaty z X0678; žádné nové
tvrzení o chybě TAOCP se touto horní mezí nezakládá.
