# V2-C0005: periodické prodloužení výpůjček může porušit počáteční stav

Stav: **confirmed**, 1. listopadu 2026. Jde o neplatné mezitvrzení
v důkazu §3.2.1.1-12(d), [str. 546](../images/vol2-p546.png), odstavec
za větou „A rigorous proof ...“. Hlavní vztah k desetinnému rozvoji
je správný; problém se týká tvrzení, že po uvedeném prodloužení platí
všechny rekurence také přes počáteční index.

## Co počáteční podmínky skutečně dovolují

Položme `m=9999998999`, `a=999999900`, tedy `10*a=1 (mod m)`.
`x_n` jsou desetinné cifry, `b_n` bity výpůjčky a `X_n` kongruenční stav.
Odpověď 12(c) používá pro `n>=0`

```text
x_n = (x_(n-10)-x_(n-3)-b_n) mod 10,
b_(n+1) = [x_(n-10)-x_(n-3)-b_n < 0],
X_n = (x_(n-1)...x_(n-10))_10 - (x_(n-1)x_(n-2)x_(n-3))_10 - b_n.
```

Hranatá závorka znamená indikátor podmínky; ciferný řetězec v závorkách
je obvyklá hodnota v základu 10. Požaduje se pouze inicializace `X_0=1`.
Zvolme `x_-10=2`, ostatních devět dodaných cifer nulu a `b_0=1`.
Pak opravdu `X_0=2-0-1=1`. První krok dává `x_0=1`, `b_1=0`.
Od této chvíle je celý stav stejný jako při obvyklejší inicializaci
`x_-10=1`, ostatní cifry a `b_0` nulové.

## Proč uvedené prodloužení selže

Nechť `lambda` je nejmenší kladné celé číslo s `10^lambda=1 (mod m)`.
Platí `lambda>10`: pro exponenty 1 až 9 je zbytek `10^j`, pro 10 je
1001; žádný není 1. Pro `n>=0` vlastní algebraický důkaz v
[poznámce o přenosech](carry-generators.md) dává

```text
X_n = a^n mod m,
10*X_(n+1) = X_n + m*x_n.
```

Z toho mají výstupní cifry od indexu 0 periodu dělící `lambda`.
Jejich hodnoty na indexech používaných v knižním prodloužení jsou přesně

```text
X_(lambda-10)=1001, X_(lambda-9)=1000000000,
x_(lambda-10)=(10000000000-1001)/m=1;
X_(lambda-3)=1000, X_(lambda-2)=100,
x_(lambda-3)=0.
```

Kniha předefinuje `x_n=x_(n mod lambda)` pro `n<0`, obdobně `b_n,X_n`,
a tvrdí platnost rekurencí pro všechna celá `n`. Tím se však původní
`x_-10=2` změní na 1, zatímco `b_0=1` zůstane: index 0 není záporný.
Rekurence pro `n=0` pak vyžaduje

```text
x_0 = (1-0-1) mod 10 = 0,
```

ale skutečně generovaná hodnota je 1. Stejně selže výraz pro `X_0`:
po předefinování počátečních cifer dává `1-0-1=0`, místo uložené 1.
Výpočet periody `lambda` ani její úplné vypsání nejsou potřeba.

## Oprava důkazu a význam nálezu

Stačí zpřísnit inicializaci na stav konzistentní s periodickým minulým
výstupem. Ještě jednodušší je ponechat obecné přípustné počátky a v (d)
prodloužit pouze `X_n` pomocí inverzního kongruenčního generátoru;
pro všechna celá `n` potom definovat
`x_n=(10*X_(n+1)-X_n)/m`. Pro `n>=0` to jsou již dokázané výstupní cifry.
Opakováním identity `X_n/m=x_(n-1)/10+X_(n-1)/(10*m)` získáme desetinný
rozvoj. Výpůjčky vůbec není nutné prodlužovat ani tvrdit zachování jejich
původní inicializace. To dokazuje hlavní závěr pro oba výše uvedené počátky.

## Errata a doklady

Původní sazba byla zobrazena. Všechny vrstvy `all2-prepre`, `all2-pre`,
`all2`, `err2`, `err2.textxt` zkontrolovány 1. 11. 2026 podle str. 546,
počátečních podmínek, výpůjček a periodického prodloužení. Změny na
str. 546 z let 1999–2010 opravují jiné indexy, znaménka a mocněnec;
tento krok v 12(d) nemění. Upřesnění úlohy 14 na str. 547 z 13. 5. 2016
definuje periodu `lambda`; rovněž nepředefinuje `b_0` v úloze 12.

[Malý přesný kontrolní skript](../verify_borrow_extension.py) a jeho
[výsledek](../results/borrow-extension.json) ověřují obě počáteční
reprezentace, shodu jejich následujících stavů a uvedený rozpor.
Novější fyzický tisk ani prvenství neověřeny.
[Anglický draft](../reports/C0005-borrow-periodic-extension-draft.txt) neodeslán.
