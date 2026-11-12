# Planární Langfordovy posloupnosti a ukazatel průběhu: DLX27–28

Úplný průchod 1. listopadu 2026. Zadání na126, odpovědi na421,
vzorec(27) na73. Původní stránky zobrazeny. Obě úlohy jsou ověřené;
nevznikl nový nález. Výsledky jsou v `results/planar_langford/verified.json`
a `results/completion_ratio.json`.

## 27: proč sekundární položky přesně rozpoznají křížení

Výskyty čísla i leží na pozicích j a k=j+i+1. Jejich knižní obdélníkový
oblouk má výšku H=ceil(i/2)=floor((k−j)/2). Zabírá svislé body (j,h),
1≤h≤H, vodorovné body (x,H), j<x≤k, a zbývající svislé body (k,h),
1≤h<H. Bod ve stejné polorovině představuje jednu sekundární položku.
Primární položky vylučují společné konce různých oblouků.

Dva takové oblouky mají společnou položku právě tehdy, když se jejich
konce na základně střídají. Pro disjunktní intervaly je tvrzení zřejmé.
Při vnoření j<p<q<k je vnější interval nejméně o2 delší, tedy jeho
výška alespoň o1 větší. Vnitřní oblouk se proto nedotkne ani jeho
vodorovného vršku, ani svislých stran. Při proložení j<p<k<q označme
výšky H a G. Je-li H≤G, dotknou se v bodě(p,H); je-li H>G,
dotknou se v bodě(k,G). Záměna obou intervalů pokrývá druhou orientaci.
To je obecný důkaz, nikoli extrapolace z konečného výčtu.

Graf, jehož vrcholy jsou dvojice a hrany jsou střídající se konce,
musí být bipartitní: každá jeho hrana vyžaduje opačné strany základny.
Naopak každé jeho dvoubarvení dává bezkolizní oblouky popsanou konstrukcí.
Ponechání největšího čísla pouze nahoře odstraní globální odraz.
Má-li graf c komponent, zůstane 2^(c−1) přiřazení stran pro tutéž
posloupnost. Tím je vysvětleno i knižní upozornění na opakované výstupy.

`check_planar_langford.py` provedl198906 kontrol dvojic s různými konci
pro n1–16. Nezávislý výčet běžných Langfordových posloupností a následný
test bipartitnosti byl porovnán s **celými množinami** výstupů původního
DLX1 pro n1–11, včetně konkrétního přiřazení horní/dolní strany.
Nenulové počty planárních posloupností jsou2 pro n3,8 pro n8 a32 pro n11.
Při n4 a n7 žádné neexistují; ostatní testované n nepřipouštějí ani
běžnou Langfordovu posloupnost. Ve všech těchto případech je násobnost1.
Počet8 pro n8 odpovídá čtyřem příkladům po ztotožnění obrácení v4A§7–8.

Vytištěný příklad n12 je platný a má dvě komponenty: {1,2,3} a
{4,5,6,7,8,9,10,11,12}. Proto dává přesně2 výstupy. To bylo ověřeno
zvlášť jak bipartitním grafem, tak původním DLX1 s fixovanou posloupností.
Historické erratum k Fascicle5 z6.8.2021 doplnilo vynechanou8 do tohoto
příkladu; v našem4B je již zapracováno. Nejde o nový nález.

## 28: přesný smíšený poziční zápis

Položme T=t0···tℓ a

    K = sum((cj−1) · t(j+1)···tℓ, j=0..ℓ).

Knižní vzorec je přesně ρ=(2K+1)/(2T). Pro pevné kladné radixy tj
probíhá K všechna celá čísla od0 doT−1 právě jednou. To plyne obvyklým
postupným dělením posledním radixem, i když některé radixy jsou1.
Nahrazení cj číslem tj+1−cj změní K naT−1−K, tedy ρ na1−ρ.
Jednoznačnost zápisu proto dává ρ=1/2 právě pro tj=2cj−1 při každém j.

Čitatel2K+1 je lichý. Krácení nemůže odstranit faktor2 ze jmenovatele2T,
takže zkrácený jmenovatel je vždy sudý. Zejména ρ nikdy není1/3.
Pro ℓ+1 opakování dvojice(c,t)=(2,4) dává geometrická řada přesně
ρ=1/3+1/(24·4^ℓ), takže1/3 lze libovolně dobře aproximovat shora.

`check_completion_ratio.py` porovnal přímý součet zlomků s nezávislým
celočíselným Hornerovým výpočtem. Ověřil111110 případů pro1364 vektorů
radixů (hloubka1–5, radixy1–4), celou bijekci, komplementy, podmínku
pro1/2 a paritu zkráceného jmenovatele. Dále ověřil30 aproximací1/3.
Obecná tvrzení stojí na důkazu výše, nikoli na omezení testovaných radixů.

Tato kontrola potvrzuje vzorec a celou úlohu28. Nepovažuje heuristický
ukazatel za záruku skutečně zbývajícího času a neuzavírá další výkonové
údaje hlavního textu na73.
