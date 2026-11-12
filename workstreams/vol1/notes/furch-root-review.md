# V1-X0773: Furchova metoda půlení gama integrálu

Citace a konkrétní popis Furchovy metody na s.121 jsou checked.
Root ověřil všech31 souborů a10 vnějších závislostí paketu
`parallel/asymptotic-primary-followup/results/furch1939-manifest.json`,
SHA-256 `d5233e4d79ab700c94ac80e8143b851cc4cb930ce13ebc554c0aec52b651b86d`.
Přímo zobrazil titul časopisu a **celý článek92–95** (PDF96–99),
včetně poznámek a grafu. Titul112, číslo1–2, uvádí dokončení
17.3.1939; přijetí článku13.1.1939 není datem vydání čísla.
Knižní rok i rozsah souhlasí. Jiné články v PDF nejsou auditovány.

Furchova funkce je `Y_n(t)=exp(-t)sum_(j=0)^(n-1)t^j/j!`, tedy
horní gama integrál od t dělený Gamma(n)=(n−1)!. Hledá posun alpha,
pro který Y_n(n−alpha) dobře aproximuje1/2. Je-li gamma(a,t)
dolní gama integrál, převod je přesně

```text
Y_n(n-alpha)=1-gamma(n,n-alpha)/Gamma(n),
x=n-1, y=1-alpha.
```

Zde x a y jsou parametry TAOCP. Rozdělení integrálu v n−1 na93
odpovídá knižním I_1 a I_2. Substituce `q=p-log(1+p)` na94
a rozvoj inverze1/p se shodují s metodou v TAOCP; Furch má
konstantu−1/3 v1/p, kniha2/3 v1+1/p. Oddělený člen1 před jeho
Laplaceovým integrálem je přesně integrál členu1 v knižním tvaru.

Root přímo porovnal Furchovo(10a) s přijatým vzorcem(G2) v
asymptotic-gamma.md. Koeficient hlavní korekce je
`alpha-1/3=2/3-y`; další je
`y^3/6-4/135-(2/3-y)/12=y^3/6+y/12-23/270`.
Oba mají správná opačná znaménka vůči dolnímu gama integrálu.
Furchův slabší zbytek O((n−1)^−2) se silnějším moderním odhadem
nekoliduje. Pro alpha=1/3 vychází jeho8/(405 sqrt(2pi)(n−1)^(3/2)).
Zkoumá tedy polohu půlení a její asymptotickou aproximaci;
netvrdíme přesný uzavřený vzorec pro medián.

V jeho pomocné rekurenci(2) na93 skutečně stojí minus, které
odporuje kladnému explicitnímu součtu(1a), už pro n=2.
Následující integrální rovnice(3) a metoda však používají správný
kladný součet. Tato chyba původního článku se nepřenáší do
prověřovaných vzorců TAOCP a není novým nálezem v knize.

Root znovu přímo četl TAOCP121; celé příslušné matematické odvození
bylo přijato dříve. Hledání všech čtyř úplných vrstev errat je
v paketu; žádná oprava této citace nalezena nebyla. Známé opravy
domén a znamének2024 zůstávají zahrnuté v dřívějším důkazu.
Doetsch1937, na kterého odkazuje Furch, nebyl samostatně čten;
potřebný Laplaceův krok již pokrývá obecný důkaz a X0768.
Žádný nový nález v TAOCP ani opakované matematické testy.
