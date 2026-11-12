# D111–D112 — MPR8 a celá MPR9

6. listopadu 2026. Celá obě zadání13/file33 a odpovědi
372/file392 přímo zobrazeny, také autorův Pre-Fascicle5A,
13/file19 a29/file35. D111 má úplný matematický důkaz
MPR8 pro všechny kladné dimenze, ale nechává otevřený
výklad závěrečné věty odpovědi v dimenzi1 (C046).
D112 uzavírá celé MPR9. Žádný výpočet není potřeba.

## MPR8: úplná distribuce a každá vlastní marginála

Pro kladné celé n má binární vektor x hmotnost

```
P(X=x)=(2+(−1)^{νx})/2^{n+1}.
```

Každá sudá váha tedy dostává3/2^{n+1}, každá lichá
1/2^{n+1}; obě hodnoty jsou kladné. Změna kteréhokoli
jednoho bitu je bijekce sudých a lichých vektorů, takže
každých je2^{n−1}. Součet hmotností je
(3+1)2^{n−1}/2^{n+1}=1. Tím je ověřena normalizace,
nikoli jen pozdější marginály.

Zafixujme r<n souřadnic a libovolný konkrétní vzor
jejich hodnot. Existuje2^{n−r} doplnění. Protože je
alespoň jedna souřadnice volná, přepnutí její hodnoty
páruje sudé a liché celkové parity mezi doplněními,
a ponechává fixovaný vzor. Součet pravděpodobností je

```
(3+1)2^{n−r−1}/2^{n+1}=2^{−r}.
```

Pro n≥2 tak jednotlivé bity mají obě hodnoty s1/2
a každý společný vzor libovolných r<n bitů má přesně
součinovou pravděpodobnost2^{−r}. To dokazuje všechny
řády1≤r≤n−1, nikoli jen vybranou sadu nebo jeden vzor.
Celý n-prvkový vektor však není nezávislý: například
samé nuly mají skutečnou pravděpodobnost3/2^{n+1},
zatímco součin n marginálních pravděpodobností je
2^{−n}=2/2^{n+1}. Pro n≥2 je tedy nejvyšší dostupný
řád nezávislosti přesně n−1, jak uvádí odpověď.

Pro r=0 je prázdný vzor celá pravděpodobnostní množina
a má pravděpodobnost1; párování také dává správný
výsledek. Pro r=n už žádný volný bit není, takže se
párovací argument nesmí použít. Právě toto rozlišení
je potřebné pro poslední krok.

## MPR8: jednosouřadnicový okraj a C046

Při n=1 je zadané rozdělení stále platné:
P(X₁=0)=3/4 a P(X₁=1)=1/4. Rodina obsahující jedinou
náhodnou veličinu je nezávislá: pro každou její hodnotu
je společná pravděpodobnost totožná s jediným marginálem.
Proto zde1-násobná (a tedy n-násobná) nezávislost platí.

Odpověď nejprve správně omezí vlastní marginály na
0<r<n, ale potom bez dalšího omezení uzavře, že
n-násobná nezávislost neplatí. Při doslovném zahrnutí
n=1 je tento závěr nesprávný. Původní zadání8 samo
n≥2 neuvádí a na rozdíl od úlohy7 výslovně neříká,
že zobecňuje předchozí úlohu6. Ta n≥2 výslovně má;
je tedy možné, že v tomto souvislém bloku autor
nevyřčeně mínil pouze netriviální dimenze n≥2.

C046 je proto pouze interpretační kandidát na chybějící
omezení, nikoli potvrzený nález. Případná úprava by byla
malá: výslovně n≥2, nebo doplnit výjimku n=1.
Hlavní paritní konstrukce a důkaz pro n≥2 jsou správné.
Nulová dimenze zde nepřidává další podezření: vzorec
by tam neměl normalizovaný součet a běžné zadání
X₁,…,X_n používá kladnou dimenzi.

Matematická klasifikace všech kladných n je tedy úplná,
ale D111/MPR8 zůstává partial pouze kvůli neuzavřenému
výkladu tištěného rozsahu. Kandidáta nelze propagovat
na confirmed bez rozhodnutí, zda je n≥2 dostatečně
určeno kontextem. Přesná anglická poznámka je
`notes/C046-one-coordinate-parity.md`.

## MPR9: závislé dvojice a celá podmíněná nezávislost

Odpověď předepisuje dvě atomy:

```
P(X=00…0)=1/2,
P(X=11…1)=1/2,
ostatní pravděpodobnosti0.
```

Pro n≥2 jsou oba vektory různé, všechny hmotnosti
nezáporné a součet1. Každý bit je férový. Pro kteroukoli
dvojici různých souřadnic i,j však

```
P(X_i=1,X_j=1)=1/2 ≠ (1/2)(1/2)=1/4.
```

Každá taková dvojice je tedy závislá, jak požaduje
první část. Také společné01 a10 mají pravděpodobnost0,
zatímco součin marginálů by byl1/4; konstrukce neskrývá
jen výjimku jedné dvojice.

Nyní zafixujme libovolný index j a zjistěme X_j=b,
kde b je0 nebo1. Obě podmiňovací události mají
kladnou pravděpodobnost1/2. Podmíněně se celý zbývající
vektor rovná bb…b s pravděpodobností1. Pro libovolný
vzor y na ostatních n−1 souřadnicích tedy

```
P(X_i=y_i pro všechna i≠j | X_j=b)
 = [všechna y_i=b]
 = ∏_{i≠j}[y_i=b]
 = ∏_{i≠j}P(X_i=y_i | X_j=b).
```

To je plná společná nezávislost všech n−1 zbývajících
proměnných, nikoli jen párová. Stejný argument platí
pro každou jejich podmnožinu, každý j a obě zjištěné
hodnoty b. Nezávislé veličiny smějí být deterministické;
právě tento rozdíl vysvětluje jednoduchost odpovědi.
Žádné podmiňování nulovou událostí ani konvence0/0
zde není potřeba.

Pro nejmenší netriviální n=2 zbývá po podmínění
jediná konstanta a argument stále platí. Při případném
n=1 je tvrzení o všech dvojicích prázdné a zbývající
prázdná rodina je nezávislá s prázdným součinem1;
to konstrukci nevyvrací. Obsah „libovolné dvě jsou
závislé“ má konkrétní svědky pro n≥2.

## Errata a uzavřený rozsah

Šest místních vrstev errat a tři dostupné TeXy pro
stejné původní strany13,372 a Fascicle5 str.184 byly
převzaty z bezprostředně předchozího vyhledávání
a znovu věcně posouzeny. MPR8 ani MPR9 v nich nemá
příslušnou opravu. Původní sazba knihy i autorova PS
obsahuje dotčený závěr odpovědi8. Fyzický výtisk ani
historické prvenství se netvrdí; neprobíhá žádná
komunikace s autorem.

D112 uzavírá celou MPR9 a odpověď bez nálezu.
D111 ponechává MPR8 partial pouze pro C046; všechny
jeho výpočty i korektní rozsahy jsou dokázány výše.
File33 a392 zůstávají partial také pro další úlohy.
Žádný numerický běh, dlouhý census nebo restart.
