# Tableaux41: přesná vzdálenost a model porovnání

Zadání72/file83, odpověď614/file625. Obě sazby zobrazené.
Znaménko n+ v poslední rovnosti odpovědi je známé erratum
all3-prepre,1.1.2006: správně n−. Není to nový nález.

## P0601: dolní mez pro libovolnou posloupnost přesunů

Jediná operace vyjme právě jeden klíč a vloží jej jinam.
Relativní pořadí všech ostatních klíčů zachová, i když se
změní jejich indexy. Po k operacích se alespoň n−k různých
klíčů nikdy nevyjmulo: opakované vyjmutí stejného klíče tento
počet jen zvětší. Tyto klíče tvoří v původní permutaci
podposloupnost ve stejném pořadí jako ve výsledném seznamu.
Je-li výsledek setříděný, tato podposloupnost je rostoucí.
Pro délku nejdelší rostoucí podposloupnosti L tedy n−k≤L,
čili dis(π)≥n−L. Nevyžaduje se, aby operace přesouvaly
navzájem různé klíče.

## P0602: dosažitelná horní mez včetně všech mezer

Zvolme jednu nejdelší rostoucí podposloupnost a její klíče
ponechme jako nepřesouvané kotvy v_1<…<v_L.
Ostatní klíče zpracujme v rostoucím hodnotovém pořadí.
Každý x vyjmeme a vložíme bezprostředně před nejmenší kotvu>x,
nebo na konec seznamu, pokud taková kotva neexistuje.

Kotvy nikdy nemění vzájemné pořadí. Již přesunuté klíče
ve stejné hodnotové mezeře mezi kotvami stojí ve vzestupném
pořadí, protože nový, větší x se vloží až za ně těsně před
pravou kotvu. Klíče v různých mezerách oddělují kotvy.
Dosud nezpracované ne-kotvy mohou toto uspořádání prokládat,
ale všechny budou při svém jediném přesunu odstraněny.
Na konci je tedy celý seznam setříděný a každá ne-kotva
se přesunula nejvýše jednou. Tím dis(π)≤n−L.

Dohromady dis(π)=n−L. Pro prázdnou permutaci jsou obě strany0;
pro neprázdnou je1≤L≤n. Rostoucí vstup má vzdálenost0,
klesající n−1. Konstruktivní důkaz horní meze neslibuje
optimální čas implementace samotných fyzických přesunů knih.

## P0603: přesný převzatý tableau argument

P0403 (notes/tableaux-proof-47-54.md) již dokazuje, že první
řádek v TheoremA obsahuje minimální možné poslední hodnoty
rostoucích podposloupností každé dosažitelné délky.
Jeho délka je tedy přesně L. S P0601–02 dostáváme opravenou
knižní rovnost dis(π)=n−(délka prvního řádku).
Nejde o nové dokazování celého RSK ani o předpoklad
rovnosti, která by měla nahradit dolní mez P0601.

## P0604: vlastní důkaz ostré algoritmické horní meze

Převzatý invariant P0403 umožňuje udržovat rostoucí pole
t_1<…<t_l minimálních konců podposloupností v přečteném prefixu.
Pro nový x nejprve porovnáme x s t_l. Je-li x>t_l,
připojíme x a l zvýšíme. Jinak binárně najdeme první t_j>x
a nahradíme jej x. První prvek inicializuje t_1 bez porovnání;
všechny klíče jsou různé.

Je-li výsledná délka L, je n−L kroků bez připojení.
Každý potřebuje nejvýše ceil(lg L) dodatečných porovnání,
protože po prvním testu je jen l≤L možných cílových indexů.
Celkový počet je tedy nejvýše

    n+(n−L)ceil(lg L) ≤ 2n+(n−L)lg L.

Pro dostatečně velké n je maximum posledního součinu
n lg n−n lg lg n+O(n). Zde je uniformní odhad, nikoli
předpoklad o „typické“ délce L. S přirozenými logaritmy:

- Je-li L≤n/ln n, pak(n−L)ln L≤n ln n−n ln ln n.
- Je-li L>n/ln n, pišme t=L ln n/n>1. Pro velké n platí
  ln L≥(ln n)/2, a proto
  (n−L)ln L≤n ln n−n ln ln n+n(ln t−t/2).
  Funkce ln t−t/2 je na t≥1 shora omezená konstantou
  (maximum má v t=2).

Převod základu ln ln n na lg lg n přidá jen konstantní
násobek n. Dostáváme požadovanou horní mez
n lg n−n lg lg n+O(n) ve všech vstupech.
Pro L=1 žádné dodatečné binární porovnání není třeba;
konečně mnoho malých n pokrývá lineární člen.
Paměť je O(L), případně O(n) při uchování předchůdců pro
rekonstrukci konkrétní podposloupnosti. Ta pro dis není nutná.

## P0605: ostrá dolní mez a přesná externí závislost

[Primární publikace Fredman1975](https://www.sciencedirect.com/science/article/pii/0012365X7590103X)
uvádí pro n různých prvků lineárně uspořádané množiny
stejnou horní mez a její optimálnost v nejhorším případě.
Použitý výsledek je rozhodovací model, který získává
pořadovou informaci porovnáním dvou vstupních klíčů.

Aplikovatelnost je přesná: každá sada různých klíčů má jedinou
pořadovou permutaci π a všechna porovnání mají stejné výsledky
jako u jejích hodností. LIS i dis se při této náhradě nezmění.
Nejhorší počet porovnání v tomto modelu je proto týž.
Odečtení L od známého n nepřidává žádné porovnání klíčů.

Tato dolní mez netvrdí dolní časovou mez pro algoritmy,
které smějí využívat celočíselné hodnoty jako adresy nebo
provádět libovolné operace s jejich bity. Číselný zápis
permutace1,…,n zde pouze kóduje pořadí; rozsah tvrzení
odpovědi je výslovně porovnávací.

Celý důkaz Fredmanovy dolní meze zde není znovu odvozen.
Přesné tvrzení, model a bibliografii podporuje primární
abstrakt/úvod; plný PDF z univerzitního zrcadla se nepodařilo
v krátkém přístupu načíst. Externí závislost je doložena
v sources/tableaux-fredman-source.json a není vydávána za
samostatně přezkoušený důkaz. Horní mez P0604 je vlastní.
Žádný výpočet nebo enumerace nebyly spuštěny.

