# Kinkelin a Glaisher: převzetí X0688

2. listopadu 2026. Přijat samostatný zmrazený balíček 61 souborů,
53 420 799 bytů. Všechny hashe a 14 vnějších závislostí souhlasí.
Root přečetl celé předání, matematickou poznámku i inventář;
přímo porovnal knihu 116/504, Kinkelina 122/124/126/131–134/138,
celého Glaishera 43–47, tituly obou svazků a obsah Messengeru vii.
U Kinkelina 138 root ověřil konec článku a dataci, neodvozoval
znovu tamní pomocné integrační aplikace. Četba zbývajících stran
Kinkelina je převzata od agenta s jeho přesně uvedenými mezemi.

Úkolem je ověřit obsah konkrétních citací v odpovědi 1.2.11.2-7,
nikoli všechny věty a mezivýpočty obou článků. Úspěšné staré
testy ani 1915 kontrol se neopakovaly. Přijatý obecný důkaz
rozvoje se zbytkem je nadále `notes/euler-products.md`, (P1)–(P5).

## Shoda konstant a obecného postupu

Hyperfaktoriál K_n znamená součin k^k pro k=1,...,n. Konstanta A
je kladný vedoucí faktor jeho asymptotického rozvoje, přesně
definovaný limitou (C1) v předané poznámce. Kinkelinovo G je
funkce definovaná jeho rovnicí (7) na 124; na 126 výslovně platí
G(n+1)=K_n. Jeho kladná konstanta varpi z 131 se od A liší.
Přímé srovnání vedoucího vzorce 134 s (C1) dává

```text
A = exp(1/12) sqrt(varpi).
```

Kinkelin na 124 výslovně určuje, že parametr k jde do nekonečna;
vzorce 134 se tedy nečtou jako přesné identity pro konečné k.
Konvergentní řada pro log(varpi)/2 na 133 je správně převedena
do moderního značení v (C6); značka log zde znamená přirozený
logaritmus. Její převod přes integrál rozdílu logaritmů gama
funkce a teleskopický součet 1/6 byl kořenově algebraicky ověřen.

Glaisher přímo používá A. Jeho koeficienty 43 souhlasí s (P1),
včetně exponenciálního koeficientu
`-1/5040+1/(2*720^2)=-1433/7257600`. Root rovněž prošel
argument 44–47 a jeho přesnou moderní podobu (C8)–(C11).
Pro sudé n je poměr součinů sudých a lichých k^k přesně
`2^(n (n+2)/2) K_(n/2)^4/K_n`. Dosazení vedoucí asymptotiky
dává faktor `A^3*2^(-1/3)`. Druhá cesta přes součin
`((j+1)/j)^j` pro lichá j dává tentýž poměr a rovnici (C10).
Oddělení členu j=1 ponechá absolutně konvergentní dvojitý
součet: pro r>=2 je součet j^(-r) přes lichá j>=3 nejvýše
`4*3^(-r)`. To ospravedlňuje záměny a přechod k limitě;
divergentní asymptotický součet se nepoužívá jako konvergentní.
Integrální varianta na 47 souhlasí s (C11).

## Bibliografie a známé opravy

Kinkelinův titul svazku potvrzuje 57 a 1860; konec 138 datuje
rukopis červencem 1856. Glaisherův celý svazek nese 1878, ale
obsah vii přímo mapuje jeho měsíční čísla: strany 43–47 patří
do července 1877. Knižní 1877 je tedy správně. Je zachován
rozdíl mezi rokem článku, rokem souborného svazku a sepsáním.

Root přímo porovnal známé změny v all1-prepre 36, all1-pre 15,
all1 7 a 13; další vrstva err1 a její shody byly převzaty ze
zmrazeného soupisu. Doplnění jména a citace 2005, oprava horní
meze součtu 2021, rozsahu 122–138 v 2023 a pojmu hyperfactorial
v 2026 jsou veřejné opravy, nikoli nové nálezy.

X0688 uzavírá obě konkrétní historické citace. Celá úloha 7
zůstává partial pouze pro konkrétní pasáž de Bruijn §3.7,
ne pro její již dokázané matematické identity. X0135 navíc
obsahuje jiné nezávislé mezery. Žádný nový kandidát nevznikl.

Strojový inventář agenta ukládá u Glaishera pod klíčem title
údaje titulní strany svazku. Název článku je v poznámce i
původním 43 správně; normalizovaný kořenový záznam jej uvádí
zvlášť jako `On the Product 1^1.2^2.3^3...n^n`.
Zmrazený inventář se kvůli tomuto rozlišení nepřepisuje.
