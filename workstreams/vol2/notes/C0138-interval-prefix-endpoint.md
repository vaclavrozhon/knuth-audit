# V2-C0138: chybějící krajní případ v odpovědi 4.5.3-39

Stav: **confirmed**, obecný postup na straně 654. Baseballový
výsledek 287 je správný. Dodatečný návod pro nejmenší jmenovatel
v uzavřeném intervalu však může přehlédnout racionální kraj.
Známá oprava z 2000-01-08 tuto druhou vadu neřeší.

Používáme kanonický konečný rozvoj
[0;x_1,...,x_s], kde x_i jsou kladná celá čísla a x_s>=2.
Za posledním členem, stejně jako v knize, umístíme symbol
nekonečna. Slovo X je prefixem slova Y, pokud Y začíná všemi
členy X. Konečný prefix sám určuje racionální číslo.

## 1. Přesný protipříklad

Vezměme uzavřený interval [a,b]=[2/5,1/2]. Platí 0<a<b<1
přesně podle zadání obecného postupu. Rozvoje jsou

```
a=[0;2,2],       b=[0;2].
```

První odlišná pozice je j=2: x_2=2, y_2=infinity.
Knižní předpis pro sudé j volí

```
z_j=x_j+[x_(j+1)!=infinity]=2+0=2,
c=[0;2,2]=2/5.
```

Jmenovatel c je 5. Přitom horní kraj 1/2 leží v intervalu
a má jmenovatel 2; žádné celé číslo v intervalu není, takže
2 je skutečné minimum. Selhání není jen otázkou ostrého versus
neostrého porovnání: obecný odstavec výslovně pracuje s [a,b].

Chybný je i pomocný výrok, že všechny zlomky v intervalu mají
po společném prefixu ještě člen z_j. Zde se horní kraj na
společném prefixu již zastaví. Jeho jmenovatel se nedá počítat
dosazením nekonečného posledního podílu do formule určené
pro konečnou posloupnost.

Jde o celou rodinu. Pro celá k,t>=2 použijme

```
a=[0;k,t]=t/(kt+1),    b=[0;k]=1/k.
```

Předpis vrátí a se jmenovatelem kt+1, zatímco skutečné
minimum je k, dosažené horním krajem b. Pokud q<k, kladný
zlomek p/q je alespoň 1/q>1/k, tedy neleží v intervalu.

## 2. Opravený obecný postup a jeho důkaz

Nejprve zjistíme nejdelší společný prefix obou kanonických
rozvojů. Pokud se jeden rozvoj na tomto prefixu zastaví,
vrátíme příslušný kraj intervalu. Jinak lze použít knižní
pravidlo pro první odlišné konečné členy. Doplňovaný krok
je podstatný; pouhá zmínka o připsání nekonečna nestačí.

Pro důkaz označme společný prefix W=(w_1,...,w_k).
Continuant K(W) je definován rekurencí K()=1,
K(w_1,...,w_k)=w_k K(w_1,...,w_(k-1))+K(w_1,...,w_(k-2)),
s pomocnou hodnotou K záporné délky rovnou 0. Položme

```
C=K(W),        D=K(W bez posledního),
```

kde pro prázdné W je C=1,D=0. Připojení úplného podílu
u=P/Q, P,Q kladných nesoudělných celých čísel, transformuje
zlomek lineárně lomeným zobrazením

```
H(u)=[0;w_1,...,w_k,u],
q(H(P/Q))=C P+D Q.                                   (I1)
```

Zápis q znamená kladný jmenovatel po zkrácení. Žádné další
krácení v (I1) nenastane: matice transformace má determinant
+1 nebo -1, takže zachovává nesoudělnost. Pro k=0 je H(u)=1/u.
Zobrazení H je na u>=1 monotónní; znaménko jeho derivace je
(-1)^(k+1).

**Když je jeden kraj samotný prefix.** Tento kraj je H(infinity)
s jmenovatelem C. Zbytek intervalu odpovídá konečným u>=u_0>=1.
Každý jeho racionální bod má P,Q>=1, a tedy podle (I1)
jmenovatel alespoň C+D>C, protože k>=1 a D>=1. Kratší
prefixový kraj je proto jediné minimum. Tím je nový krok dokázán.

**Když se oba rozvoje liší konečnými členy.** Nechť j=k+1
a lo<hi jsou úplné podíly obou krajů za W v rostoucím pořadí.
Jejich celé části se liší. Položme z=ceil(lo); pak lo<=z<=hi.
Pro libovolný racionální úplný podíl P/Q v tomto intervalu
platí P>=ceil(lo Q)>=ceil(lo)=z a Q>=1. Z (I1) tedy

```
q(H(P/Q)) >= C z+D = q(H(z)).                         (I2)
```

Celý podíl z tudíž poskytuje minimální jmenovatel. Je-li j
liché, nižší úplný podíl patří hornímu kraji b; je-li j sudé,
patří dolnímu kraji a. Úplný podíl je celé číslo právě tehdy,
když na tomto členu příslušný kanonický rozvoj skončí.
Proto z přesně odpovídá knižnímu předpisu

```
z = y_j+[y_(j+1)!=infinity],  když j je liché;
z = x_j+[x_(j+1)!=infinity],  když j je sudé.
```

Argument platí i pro iracionální kraje s nekonečnými rozvoji:
pro a<b se rozvoje liší po konečném počtu členů. Případ
konečného prefixového kraje však musí být stále vyřízen zvlášť.

## 3. Baseballový výsledek zůstává správný

Zaokrouhlená hodnota .334 odpovídá intervalu mezi
667/2000=.3335 a 669/2000=.3345. Konvence na přesných půlkách
výsledek neovlivní, protože nalezený zlomek leží uvnitř.

Je-li p/q v tomto intervalu, číslo h=3p-q je kladné celé
číslo, neboť interval leží nad 1/3. Horní mez dává

```
1<=h<=7q/2000,       tedy q>=286.
```

Pro q=286 je nutně h=1, ale pak 3p=q+1=287, což není možné.
Pro q=287, p=96 naopak platí

```
667*287=191429 < 96*2000=192000 < 669*287=192003.
```

Proto je nejmenší počet pokusů 287 a počet zásahů 96.
Rozvoje krajů jsou [0;2,1,666] a [0;2,1,94,1,1,3].
Jejich první rozdíl je na liché pozici 3; oba členy jsou
konečné, takže platná část knižního pravidla dává
[0;2,1,95]=96/287. Jmenovatel je 3*95+2=287.

## 4. Prameny a errata

Zadání 378 a celý obecný odstavec odpovědi 654 byly vizuálně
přečteny. Všechny čtyři řady all2-prepre, all2-pre, all2 a err2
byly 2026-11-03 prohledány podle stránek 654/378, odpovědi 39
a formulací o nejmenším jmenovateli. Kontrolován i aktuální
TeX err2. Oprava z 2000-01-08 odstraňuje pouze poškozený
text na prvním řádku odpovědi; obecný odstavec nemění.
Opravy odpovědi 39 na 646 patří jinému oddílu 4.5.2.

Poslední fyzický dotisk a priorita nálezu nejsou ověřeny.
Návrh hlášení je neodeslán. Obecný stromový alternativní
algoritmus a jeho důkaz jsou v euclid-stern-brocot.md.
