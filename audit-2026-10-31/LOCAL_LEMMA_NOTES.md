# Lokální lemma: ostrá mez a konkrétní rozdělení

Kontrola 31. 10. 2026. Zatím dokončeny úlohy SAT 315–321.
Úloha 322 a navazující algebra mají vlastní pokračující kontrolu;
níže uvedené výsledky se na ně automaticky nevztahují.

## 315–317: konečné grafy a indukce

Pro maximální stupeň 1 jsou komponenty izolované vrcholy nebo hrany.
Při p<1/2 má každá komponenta kladnou pravděpodobnost vyhnout se
všem událostem. Po podmínění neúspěchu v ostatních komponentách zůstává
z lopsided předpokladu stejná mez p. Postupným přidáváním komponent
proto dostaneme kladnou pravděpodobnost celkového úspěchu.

Obvyklá symetrická podmínka Theorem L optimalizuje θ(1−θ)^d;
maximum je d^d/(d+1)^(d+1). Obecná ostřejší mez Theorem J tedy není
přímým dosazením společného θ do Theorem L.

Pro 317 položme ρ=(d−1)/d a p=ρ^(d−1)/d, d≥2. Nechť α(H) je
pravděpodobnost vyhnout se všem událostem ve vrcholech H. Při odstranění
vrcholu v se stupněm Δ platí z lopsided podmínky

`α(G) ≥ α(G−v) − p α(G−N[v])`.

Každý soused v má po odstranění v stupeň menší než d. Indukční
poměrové meze proto dávají pro Δ>0

`α(G) > (1−pρ^(−Δ)) α(G−v)`.

Pokud Δ≤d−1, pravá závorka je alespoň ρ. Pokud Δ=d, je rovna
(d−2)/(d−1), takže ostrá nerovnost stále dává α(G)>0 i pro d=2.
Při Δ=0 máme přímo α(G)≥(1−p)α(G−v)>ρ α(G−v).
To uzavírá obě indukční tvrzení včetně počátečních případů.

Nezávislý výčet Möbiových polynomů prošel všech 1099 označených grafů
na 1..5 vrcholech a 1000 náhodných grafů na 6..9 vrcholech.
Všechny hodnoty při hranici byly kladné; 9289 kontrol vrcholu se stupněm
menším než d ověřilo i ostrý poměr. Výčet pracuje s extremálními
Möbiovými hodnotami, obecné pravděpodobnostní tvrzení kryje důkaz výše.

## 318: ostrost pomocí úplných stromů

Nezávislé množiny stromu rozdělíme podle přítomnosti kořene. Pro úplný
t-ární strom výšky n dostaneme

```
f_0=1−p, f_1=(1−p)^t−p,
f_(n+1)=f_n^t−p f_(n−1)^(t²), n≥1.
g_0=1−p, g_(n+1)=1−p/g_n^t.
```

Polynomiální rekurence souhlasí s úplným výčtem nezávislých množin
17 stromů, včetně 21vrcholového stromu se 149 057 nezávislými množinami.

**Známá oprava E003:** rozdíl g_n−g_(n+1) na str. 611 má být
`p/g_n^t−p/g_(n−1)^t`, s podmínkou g_n<g_(n−1).
Oprava je zveřejněna v erratech 4B s datem **2. 2. 2024**, proto ji
nepočítáme jako nový nález. Byla zapracována do kontroly důkazu.

Pokud všechna g_n zůstanou kladná, klesají. Z g_(n+1)>0 navíc plyne
`g_n>p^(1/t)`, takže jejich limita λ je přísně kladná. Dosazením
`p=λ^t(1−λ)≤t^t/(t+1)^(t+1)` dostáváme spor pro vyšší p.
Případ p≥1 je již triviální na jediném vrcholu. Tím je ostrost dokázána.

Číselný příklad t=2,p=149/1000 byl ověřen **intervalově s racionálními
konci**, při pevném jmenovateli 10^80 a zaokrouhlování ven. Všechna
g_0..g_44 jsou kladná a celý interval g_45 je záporný:
`g_44≈0.3836294169433`, `g_45≈−0.0124240772750`. Výška 45 tedy souhlasí;
nejde pouze o výsledek plovoucí aritmetiky bez kontroly chyby.

## 319–320: jednodušší mez a prahy cest/kružnic

Nerovnost e^x>1+x při x=1/(d−1) dává
`1/(ed)<(d−1)^(d−1)/d^d`, tedy i tvrzení s neostrou levou mezí.

Pro cestu P_m je `f_m=f_(m−1)−p f_(m−2)`, s f_0=1,f_1=1−p.
Při `p=1/(4cos²θ)` splňuje rekurenci i počáteční podmínky

`f_m = sin((m+2)θ)/((2cosθ)^(m+1) sinθ)`.

Pro kružnici m≥3 je `g_m=f_(m−1)−p f_(m−3)`, tedy
`g_m=2cos(mθ)/(2cosθ)^m`. První kořeny jsou proto
`ρ(P_m)=1/(4cos²(π/(m+2)))` a `ρ(C_m)=1/(4cos²(π/(2m)))`.
Vlastní indukované podgrafy jsou sjednocení kratších cest, jejichž
prahy jsou větší; první kořen celého grafu tudíž opravdu určuje
Shearerovu hranici. Chebyshevovy vzorce v odpovědi souhlasí přesně
s výčtem nezávislých množin 16 cest a 14 kružnic.

## F030: dvě chyby v jedné tabulce odpovědi 321

Značme `θ=(2−√2)/2`, `θ′=θ(1−θ)` a `c=(p−θ)/(1−θ)`.
Šest uvedených tříd bitových výsledků má násobnosti 1,4,4,2,4,1:
žádná událost, jedna, dvě sousední, dvě protější, tři, všechny čtyři.

Správné pravděpodobnosti jednotlivých zástupců jsou

```
0
θ′(1−c)^3
2θ′c(1−c)^2
θ²(1−c)^2 + 2θ′c(1−c)^2
θ²c(1−c) + 3θ′c²(1−c)
2θ²c² + 4θ′c³.
```

V tisku má čtvrtý řádek místo `2θ′c(1−c)^2` výraz `2θ′(1−c)^3`.
V šestém řádku chybí faktor 2 před θ²c². Pro požadované p=3/10 vychází
čtvrtá pravděpodobnost v tisku přibližně **0.4859202**, zatímco vlastní
číselný výsledek knihy **0.08815** odpovídá opravenému vzorci.
Součet všech 16 vytištěných hmotností je **1.79553073707918869**, ne 1.
Opravený poslední člen je 0.0000181720784, což též souhlasí s 0.00002
v knize; tiskovaný výraz dává asi 0.00000950656065.

Obě chyby jsou viditelné v PDF na str. 611 i v původním autorském
Pre-Fascicle 6A (23. 9. 2015), str. 247. V úplných erratech 4B a
Fascicle 6 pro tuto odpověď žádná oprava není. Vedeme je společně
jako **jeden nález F030 — chybná tabulka rozdělení**, nikoli jako
opakovaná hlášení jednotlivých nevyhovujících pravděpodobností.

### Nezávislé odvození

Na hranici p=θ dejme každému ze čtyř singletonů hmotnost θ′ a každé
ze dvou protějších dvojic θ². Součet je 4θ′+2θ²=1, marginály jsou θ,
protilehlé události mají průnik θ² a žádná konfigurace není prázdná.
Nyní každou dosud neplatnou událost nezávisle zapněme s pravděpodobností c.
Tím marginály vzrostou na θ+(1−θ)c=p a nezávislost obou protilehlých
dvojic zůstane zachována. Přímým sečtením těchto přechodů vznikají přesně
opravené vzorce. Program ověřuje normalizaci, čtyři marginály a dva
průniky symbolicky pro celé c, nikoli jen numericky v p=3/10.

Samotné zadání má i jednoduché racionální řešení: každý singleton
má hmotnost **1/5**, každá sousední dvojice **1/200**, každá protější
**9/100** a ostatní konfigurace nulu. Pak je součet 1, každý marginál
3/10 a oba protilehlé průniky 9/100; alespoň jedna událost vždy nastane.

## Reprodukce a doklady

`python3 check_local_lemma.py` vytváří `results/local_lemma.json`.
Soubor obsahuje přesné intervaly stromové rekurence, rozsahy výčtů,
číselné porovnání F030 a kompletní alternativní racionální tabulku.
Znění: `images/local-lemma-631.png` a
`images/fasc6a-local-lemma-255.png`. Fyzický výtisk dosud neověřen.
