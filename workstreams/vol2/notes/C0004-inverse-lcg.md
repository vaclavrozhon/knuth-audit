# V2-C0004: inverzní kongruenční vzorec závisí na volbě zástupce

Stav: **confirmed**, 1. listopadu 2026. §3.2.1, odpověď 5,
[str. 543](../images/vol2-p543.png), druhý řádek vystaveného vzorce.
Kontrolován svazek 2, třetí vydání, první dotisk 1997.
Přesný bibliografický doklad je v [mapě zdrojů](source-map.md).

## Předpoklady a protipříklad

Lineární kongruenční generátor má přechod `X_(n+1)=(a*X_n+c) mod m`,
kde `m` je kladný celočíselný modul, `a` násobitel, `c` přírůstek
a stav `X_n` patří do `{0,...,m-1}`. Při `a>=2` je `b=a-1>=1`.
Odpověď předpokládá `gcd(a,m)=1` a volí celé `a'` tak, že
`a*a'=1 (mod m)`; to je multiplikativní inverze modulo `m`.
Její druhý vystavený řádek tvrdí

```text
X_(n-k) = (a'^k * X_n + (a'^k-1)*c/b) mod m.
```

Zvolme `m=8, a=3, c=1, b=2, a'=3, X_0=0`, tedy `X_1=1`.
Všechny uvedené předpoklady platí, zvláště `3*3=1 (mod 8)`.
Pro `n=k=1` vychází

```text
vytištěný druhý řádek: (3*1 + (3-1)*1/2) mod 8 = 4,
správný první řádek:   (3*1 - 3*1) mod 8       = 0.
```

Veškeré dělení je celočíselné, takže rozpor nevyužívá necelý zbytek
ani sporný způsob zaokrouhlování. Hodnota 4 ani není předchůdcem 1:
`(3*4+1) mod 8=5`.

## Obecné vysvětlení a možnosti opravy

Označme `S_k=1+a'+...+a'^(k-1)` pro `k>=1`. Opakování správného
inverzního kroku dává přírůstek `-a'*c*S_k`; vytištěný druhý řádek
používá `(a'-1)*c*S_k/b`. Jejich rozdíl v racionální aritmetice je

```text
c*S_k*((a'-1)+a'*b)/b = c*S_k*(a*a'-1)/b.
```

Z dělitelnosti `a*a'-1` číslem `m` neplyne, že po dělení `b` bude
výsledek opět násobkem `m`. Právě tento neoprávněný krok vzorec porušuje.

Nejjednodušší oprava je druhý řádek vypustit. První řádek se součtem
je správný pro každou celočíselnou inverzi modulo `m`.
Chceme-li druhý řádek zachovat, stačí výslovně požadovat silnější volbu
`a*a'=1 (mod m*b)`. Taková inverze existuje, protože `gcd(a,m)=1`
a `gcd(a,a-1)=1`. Navíc pak `a'=1 (mod b)`, takže dělení je celé,
a výše uvedený rozdíl je násobek `m`. V příkladu funguje `a'=11`,
inverze 3 modulo 16: `(11+(11-1)/2) mod 8=0`.

Formulace „there is a number a'“ umožňuje existenci vhodného zástupce,
ale jediná uvedená podmínka je kongruence modulo `m`. Správnost druhého
řádku na volbě zástupce závisí; běžný nejmenší kladný zástupce 3 v příkladu
selže. Nález tedy vyjadřuje chybějící podmínku, nikoli nemožnost takový
vzorec opravit.

## Errata a nezávislé kontroly

`all2-prepre`, str. 30, oprava z 24. 1. 2003 přidává před vzorec
„if b=a-1“. [Původní sazba](../images/all2-prepre-p30-direct.png) byla
zobrazena přímo z PostScriptu. Tento dodatek výše uvedený příklad splňuje,
proto chybu neodstraňuje. Vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`
a `err2.textxt` byly 1. 11. 2026 prohledány podle stránky, úlohy a vzorce;
jiná oprava nenalezena. Změna str. 543 z 23. 12. 2024 se týká odpovědi 3.

[Přesný validátor](../verify_lcg_intro.py) porovnává skutečné iterace
se správnou inverzí a s opravou modulo `m*b` pro všechny přípustné
`m<=20`, `a,c,X_0` a `1<=k<=6`. Chybný vzorec se počítá přesnými zlomky;
zvlášť se počítají celočíselná a neceločíselná selhání.
[Výsledky](../results/lcg-intro.json). Obecný důkaz a uvedený malý
protipříklad nezávisí na úplnosti testovacího rozsahu.

Novější fyzický dotisk ani prvenství nálezu nejsou ověřeny.
[Anglický návrh](../reports/C0004-inverse-lcg-draft.txt) nebyl odeslán.
