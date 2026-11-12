# Kořenová revize C0053–C0056

Datum 2026-11-01. Kořen přímo zobrazil původní strany 396, 588,
380, 584, 585, 324 a 562 a pročetl odpovídající stabilní podklady
podagentů. Všechny čtyři vrstvy errat byly znovu prohledány podle
stran a souvisejících pojmů. Záznamy na těchto stranách opravují jiná
místa; podagenti mají zdokumentováno i přímé čtení obrazů errat.

C0053: z binomické věty je koeficient výrazu
-sqrt(2 beta)*sqrt(1-z/alpha) roven
(-1)^(n-1)*sqrt(2 beta)*alpha^(-n)*binom(1/2,n).
Tištěný výraz postrádá první faktor a pro všechna sudá n≥2 je záporný,
kdežto počty stromů jsou kladné. Nekonečná podposloupnost vyvrací
asymptotickou ekvivalenci. Závěrečný požadovaný odhad na 396 je správný;
jde o mezivýpočet v odpovědi 4(g) na 588. Potvrzeno bez numerické aproximace.

C0054: zadání skládá argumenty funkce f od nejnovějšího k nejstaršímu,
ale odpověď 23 je přiřazuje v chronologickém pořadí hran. Pro m=k=2
a f(u,v)=1-v zadání generuje 00110011..., zatímco pravidlo odpovědi
vede po hranách 00,01,10,01,... a vynechá 11. Obrácení argumentů
v jediné přiřazovací rovnici obnoví bijekci. Výsledný počet funkcí
se nemění, protože změna pořadí argumentů je sama bijekce všech funkcí.

C0055: pro jediný původní kořen R, hranu r:R→H a smyčku h:H→H
s pořadím vstupů F_H=(r,h) dávají pravidla 584
ALINK(h)=r, BLINK(h)=h, BTAG(h)=1.
Současně BLINK(r)=h, BTAG(r)=0. Poznámka 585 výslovně zmiňuje
jen druhou odchylku u kořene; standard 324-(8) však vyžaduje
RTAG(HEAD)=0. Identifikace BTAG s RTAG je součástí zadání.
Důkaz nepředpokládá nepředepsané ztotožnění ATAG s LTAG.

C0056: pro dobré uspořádání ≺ a doslovné koncové úseky
T[a]={(x,y):x ≻ a} má neprázdná množina použitých indexů
I=(0,1) nejmenší prvek a0. T[a0] obsahuje svislé přímky všech
pozdějších indexů z I, a proto není podmnožinou žádné dyadické S.
Žádný jiný T není jeho vlastní nadmnožinou. Jeho úroveň je tedy 0,
nikoli nespočetná. To nezávisí na sporném významu počtu úrovní
v C0045. Ani interpretace ≻ jako opačně orientovaného dobrého
uspořádání nepomůže: nejmenší použitý index dá počáteční úsek
bez potomků z kolekce, případně prázdnou množinu.

Zamýšlená silnější vlastnost sama existuje. Pro indexy I=R×Z
v lexikografickém pořadí vezměme uzavřené počáteční úseky T[a]
a dyadické svislé S[a,m,n]. Každý T[a] má děti T[(r,k-1)]
a S[a,0,0], každý S své dvě dyadické poloviny a každý uzel má
kontinuum předků. Podklad I×R má mohutnost kontinua. Tato oprava
nepoužívá dobré uspořádání a neřeší odlišnou terminologickou otázku
C0045; všechny její kardinální úrovně jsou opět stejné.

Všechny čtyři nálezy jsou confirmed proti dostupnému prvnímu tisku
a veřejným vrstvám errat. Nejde o tvrzení prvenství ani o ověření
fyzického výtisku; žádné hlášení nebylo odesláno.
