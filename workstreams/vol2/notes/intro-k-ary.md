# §3.1-19: náhodná funkce několika předchozích hodnot

Kontrola 1. listopadu 2026. Zadání je na [str. 9](../images/vol2-p009.png).
První tisk neobsahuje odpověď; `all2-prepre` ji doplňuje k str. 542
dne 8. 5. 2005 a ve stejný den mění zadání na asymptotické řešení.
Zbývající vrstvy `all2-pre`, `all2`, `err2`, `err2.textxt` neobsahují
nalezenou další aktualizaci tohoto řešení.

## Model a přesná část

Nechť `m` je počet symbolů a `k>=1` pevný počet předchozích hodnot,
na nichž závisí následující symbol. Funkce `f` se vybírá rovnoměrně
ze všech `m^(m^k)` zobrazení k-tic symbolů do jednoho symbolu; počáteční
k-tice je nezávislá a rovnoměrná. Stav posloupnosti je celé posouvající
se okno `W_n=(X_n,...,X_(n+k-1))`. Jeho ocas má délku `mu` a cyklus
délku `lambda`; položíme `T=mu+lambda`.

Pevný bod oknového procesu musí být konstantní k-tice `(j,...,j)`
a potřebuje `f(j,...,j)=j`. Existuje přesně `m` kandidátů a hodnoty
funkce na nich jsou nezávislé. Proto je přesně

```text
Pr(žádný konečný cyklus délky 1)=((m-1)/m)^m.
```

To dokazuje první větu nové odpovědi pro všechna `m,k`.
Nejde o rovnoměrnou náhodnou funkci na `m^k` stavech: každý další stav
musí sdílet `k-1` symbolů s předchozím. Nelze tedy bez důkazu dosadit
`m^k` do všech výsledků unárního modelu.

Do prvního opakování okna však každé nové volání `f` odhaluje novou
nezávislou rovnoměrnou hodnotu. Posloupnost tak lze do této chvíle
ztotožnit s nezávislými rovnoměrnými symboly a studovat první opakovaný
úsek délky `k`. To je přesná vazba na model v citovaném článku.

## Publikované asymptotické výsledky a rozsah ověření

Erratum cituje R. Pemantla, *J. Algorithms* 54 (2005), 72–84;
[vydavatel potvrzuje bibliografii](https://doi.org/10.1016/j.jalgor.2003.09.002).
Dostupný [autorův preprint z roku 2004](https://arxiv.org/abs/math/0404103)
obsahuje celý argument pro čas prvního opakování a v §4 náčrty
dalších dvou výsledků použitých v erratu. [Lokální kopie](../sources/pemantle-2004-k-ary-maps.pdf)
a [metadata](../sources/pemantle-2004-k-ary-maps.metadata.json).

Pro pevné `k` a `m` jdoucí do nekonečna věta 1.2 dává
`Pr(T^2/(2*m^k)>x) -> exp(-x)`, `x>0`. Autorův index prvního opakování
obsahuje proti oknovému indexu posun závislý na `k`; při tomto limitním
přechodu je zanedbatelný. Věta 1.1 dokládá pro `k=2` také konvergenci
momentů. Pro obecné `k` ji nelze získat ze samotné konvergence rozdělení.

Náčrt §4 popisuje asymptoticky rovnoměrnou relativní pozici prvního
opakovaného okna, nezávislou na normalizovaném čase. To odpovídá erratu

```text
Pr(T^2 > 2*m^k*x a lambda/T <= y) -> y*exp(-x),
pro x>0 a 0<y<1.
```

Přechod od relativní délky ocasu k relativní délce cyklu je náhrada
`U` veličinou `1-U`; obě jsou rovnoměrné na `[0,1]`. Preprintová formulace
věty 4.1 sama zjevně vypouští normalizační faktory. Kontrola se proto
opírá o vysvětlení rozdělených intenzit v okolním textu a o přesnou
normalizaci věty 1.2, nikoli o doslovné převzetí poškozené věty 4.1.

Následující odstavec §4 výslovně odvozuje řád
`Pr(lambda=1)=Theta(m^(-k/2))` pomocí výskytů konstantních oken a
Poissonovy aproximace. `Theta(h(m))` znamená horní i dolní kladný
konstantní násobek `h(m)` pro dost velká `m` a pevné `k`.
**V samotném erratu je však vytištěno `Theta(m^(k/2))`, bez minusu.**
To je potvrzená chyba [V2-C0003](C0003-k-ary-exponent.md): pro pevné
`k>=1` by taková pravděpodobnost rostla nad 1. Přímé vykreslení původního
PostScriptu potvrdilo, že nejde o vadu OCR nebo převodu do PDF.
První pracovní verze této poznámky nevědomky přebrala správné znaménko
z primárního článku a odpověď uzavřela jako bezchybnou; vizuální kontrola
vedla k opravě hodnocení na `confirmed`.

Primární zdroj tedy dokládá opravené tvrzení. Zde neposkytujeme nezávislý
úplný důkaz zdrojového aproximačního lemmatu ani těchto náčrtů.
První část odpovědi je výše dokázána nezávisle; chybu znaménka dokazuje
už obecná mez pro pravděpodobnost, nezávisle na aproximacích.

## Zbývající výzkumné otázky

Aktuální Knuthova errata nadále označují k-rozměrné analogie úloh 13
a 14, tedy průměr nejdelšího cyklu při nejlepší volbě počátku a průměr
počtu různých cyklů, za nevyřešené. Pemantle v §4 končí souvisejícím
otevřeným problémem pro nejdelší trajektorii přes všechny počátky.
To je jiný problém než doba prvního opakování z náhodného počátku.

Rešerše 1. 11. 2026 podle přesného názvu článku, jména autora a spojení
„k-ary maps“, „longest cycle“, „number of cycles“, „conjecture solved“
nenašla následný primární zdroj řešící tyto dvě části. Je to zaznamenaný
stav dostupných zdrojů, nikoli důkaz neexistence pozdější práce.
Nezaměňovat jiné modely náhodných zobrazení, náhodných permutací nebo
režim rostoucího `k` za zdejší limit s pevným `k`.

Úloha je uzavřena s potvrzenou chybou ve smyslu auditu formulace, doplněné odpovědi,
předpokladů a dostupného publikovaného stavu. Neoznačujeme ji za nově
vyřešený výzkumný problém. Finální časopisecké PDF nebylo dostupné;
porovnávána byla bibliografie a autorův preprint s výše popsanými omezeními.
