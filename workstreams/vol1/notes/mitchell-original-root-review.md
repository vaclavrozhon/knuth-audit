# V1-X0786: Mitchellův originál a certifikát konstanty

Root přijímá původní Mitchell1968 a nový rigorózní intervalový
výpočet z `parallel/permutation-cycle-originals/`. Knižních
40desetinných míst i následné znaménko plus na525 jsou správné.
Žádný nový nález v TAOCP nevzniká. Celá úloha §1.3.3–23 zůstává
partial pouze kvůli dosud nezískané původní časopisecké straně343
Knutha–Trabb Parda; odpovídající matematika již byla ověřena
v původním Stanfordském reportu.

## Rozsah nezávislého převzetí

Root přečetl celou poznámku `notes/mitchell1968.md`, celý úspěšný
program `certify_lambda.py`, výsledné intervaly, záznam prostředí
a kontrakt knihovny Arb. Přímo zobrazil všech pět původních stran
411–415; překontroloval integrální vzorce, rekurence, odhady chyby,
vytištěnou konstantu a bibliografii. Neopakoval výpočet jednotlivých
hodnot funkce R z tabulky1 ani starý úspěšný výpočet mpmath.
Knižní525 a relevantní errata byly přímo prohlédnuty v tomto
navazujícím bloku; všechny čtyři textové vrstvy jsou prohledány.

Původní AMS PDF z veřejného archivního snímku2024 má361604bajtů,
SHA-256 `b8512a9931a75e76c9289bb4e5e9e9842fafce1205294e7d7e78d15d2554d2c6`.
Článek je *Mathematics of Computation*22(1968),411–415; uvedené
datum přijetí25.července1967 není rokem vydání. Celý zmrazený
archiv včetně neúspěšných cest a zvláštního statusu journal343
se přebírá podle `MANIFEST.json`; Dickmanova samostatná věcná
kontrola je zaznamenána v X0784.

## Proč původní odhad a nový certifikát rozlišujeme

Označme lambda limitní poměr očekávané délky nejdelšího cyklu
k počtu prvků náhodné permutace. Mitchellova kladná klesající
funkce R je rovna1 na[1,2] a dále splňuje
`R'(Y)=-R(Y-1)/(Y-1)`. Původní článek uvádí dvě reprezentace:

```text
lambda = integral(1,infinity) R(Y)/Y^2 dY
       = integral(0,infinity) exp(-x-E1(x)) dx,
E1(x) = integral(x,infinity) exp(-t)/t dt.
```

Pro logaritmus R dostaneme derivaci menší než −1/Y.
Integrace této nerovnosti dává
`R(Y)<=R(Y0)*Y0/Y` proY>=Y0>=2 a mez ocasu
`integral(Y0,infinity) R(Y)/Y^2 dY <= R(Y0)/(2Y0)`.
To je správná rovnice9. V kombinaci se zdrojovými numerickými
odhady dává uváděnou slabší chybu5.5e−54.

Na413 však autor odůvodňuje silnější odhad směrem monotónnosti
podílu `q(Y)=R(Y-1)/R(Y)`, který pro tento účel nestačí.
Dokonce na2<Y<3 platí
`q(Y)=1/(1-log(Y-1))` a q roste. Tím netvrdíme nic neprokázaného
o jeho monotónnosti naY>=32. Silnější rovnici10 nepotřebujeme.
Ani numericky tvrzená mez kumulované chyby a pravděpodobně malé
zaokrouhlení z původního textu nejsou samy reprodukovatelným
intervalovým certifikátem. Tento rozdíl je v převzetí zachován.

## Kontrola analytických mezí nového výpočtu

Arb počítá s intervaly zahrnujícími zaokrouhlení směrem ven.
Program používá256Taylorových členů a75desetinných pracovních
míst, s přesně odůvodněným zbytkem každé konečné řady.
Eulerovu konstantu označme gamma. Celá funkce
`Ein(z)=sum(n>=1) (-1)^(n+1)*z^n/(n*n!)` dává na kladné
poloose `E1(x)=-gamma-log(x)+Ein(x)`. Integrand tedy má celé
pokračování `F(z)=exp(gamma)*z*exp(h(z))`, `h(z)=-z-Ein(z)`.

Na|z|=2 platí|h(z)|<=1+exp(2). Cauchyho odhad koeficientů
proto omezuje chybu integrace prvníchN=256členů na[0,1] číslem
`exp(gamma+1+exp(2))*2^(1-N)/(N+2)`. Kontrola znamének
v koeficientech h a zvláštního lineárního členu prošla.

Další úseky mají konce1,2,4,8,16,32,64,128,180. Pro středc,
poloviční délkud a poloměrr=c−1/2 je celý pomocný kruh
vRe(z)>=1/2 a d/r<=1/2. Integrální definice E1 dává
`|E1(z)|<=2*exp(-1/2)`, tedy
`|F(z)|<=M=exp(-1/2+2*exp(-1/2))`. Zbytek integrálu je nejvýše
`2*d*M*(d/r)^N/(1-d/r)`. Koeficienty E1 kolem c vznikají z
její intervalové hodnoty a derivace−exp(−z)/z; integrují se
jen sudé členy symetrického polynomu. Tyto konečné řadové
operace dávají skutečné počáteční Taylorovy koeficienty.
Zbylý kladný ocas je v[0,exp(−180)]. Žádný použitý kruh
nepřekračuje řez E1 a větvení logaritmu nezasahuje do důkazu.

Výsledný certifikát obsahuje

```text
lambda = 0.624329988543550870992936383100837244179642620180529286973551902495638089
         +/- 2.07e-73.
```

Rozdíl proti knižnímu40místnému číslu leží přísně mezi0 a0.5e−40;
konkrétně je4.2620180529286973551902495638089e−41 s uvedenou
chybou. To dokládá zaokrouhlení i plus. Rozdíl proti Mitchellově
54místnému číslu je9.73551902495638089e−55 s toutéž chybou,
tedy menší než3e−54 i bez sporného kroku jeho původního argumentu.
Úspěšný nový certifikát nebyl při převzetí znovu spuštěn.

## Zbývající pramen

`notes/knuth-trabb-pardo-journal-limit.md` a jeho log přesně
rozlišují skutečné veřejné odpovědi: metadata/coredata, prázdné
archivní výsledky, chyby přístupu a autorský bibliografický seznam.
Žádná z nich neobsahuje cílovou časopiseckou343. Známá veřejná
oprava373 na343 z2022 je ověřená, ale cílová sazba nadále chybí.
Nejde o novou matematickou mezeru v identifikaci konstanty.
