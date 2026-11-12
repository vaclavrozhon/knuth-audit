# Algoritmus B: str. 22–23, §7–70 až 72

6. listopadu 2026. Původní sazba file040.png a odpovědi
proof-file539-540-2.png / proof-file541.png. Bez spuštění programu;
níže je kontrola větví a invariantů. Známé erratum ASIZE 24→20
na str. 523 z 23. 5. 2011 je aplikováno; žádná nová karta.

## Úplnost, správnost a čas

COLOR se změní z −1 na 0/1 právě při vložení do zásobníku. Každý vrchol
se proto vloží a odebere nejvýše jednou. Zásobník obsahuje právě obarvené
neprozkoumané vrcholy kromě právě zpracovávaného u. Rodič nového vrcholu
má opačnou barvu; rodiče tvoří les, protože nový vrchol byl neobarvený.

Po průchodu seznamu u jsou všichni jeho sousedé obarveni a všechny jeho
hrany mají různé koncové barvy, pokud algoritmus neselhal. Po vyprázdnění
zásobníku mají tedy všechny obarvené vrcholy obarvené sousedy.
B2 zachovává tento invariant a postupně kontroluje všechny n vrcholů
sestupným w. B3 případně založí dosud nedotčenou komponentu.
Při úspěchu jsou všechny vrcholy obarvené a každá hrana byla zkontrolována.

Při konfliktu jsou konce hrany ve stejném rodičovském stromu:
další kořen se zakládá až po úplném uzavření dosavadní komponenty.
Cesta ve stromu mezi stejně barevnými konci je sudá; s konfliktní
hranou tvoří lichý cyklus. Proto selhání skutečně vylučuje bipartitnost.
Podrobnější kratší konstrukce lichého cyklu je ověřena níže v 72.

Každý seznam oblouků se projde jednou a každý uzel jednou vloží/vyjme.
Při úspěchu je B1 jednou (n inicializací), B2 n+1, B3 n, B4 n,
B5 m+n, B6 m, B7 m, B8 n. Toto jsou přesně počty z odpovědi 70.
Každý krok kromě B1 má konstantní cenu; i neúspěšný běh stojí O(m+n).
Prázdný graf projde B1 a B2 a úspěšně skončí.
Známé zpřesnění odkazu 7.4.1→7.4.1.2 z 2021 zohledněno.

## Úloha 71: MMIX

Kontrola je pro autorovy zvolené platné reprezentanční konvence:
32bitové relativní ukazatele v Pool, nula rezervovaná pro null,
vrcholy zarovnané na 8 bajtů, COLOR na offsetu 8 a LINK na 12,
velikost vrcholu 32. To jsou podmínky k použitému sdílenému octa zápisu.
Zdroj významu instrukcí: books/taocp-vol1-fasc1-mmix-digital3-2023.pdf,
str. 4 (M8 ignoruje tři spodní bity), 6–8 (LDT/LDTU/STCO) a
9 (NEG); navigace text/vol1-fasc1.txt.

BZ n,Success ošetří n=0. MUL n,32 a ADDU vytvoří koncovou adresu,
STT ukládá signed −1 do každého COLOR a smyčka končí přesně za polem.
0H ubere 32, 3H přeskočí již obarvený w do testu 2H.
STCO 0,link,w zapíše octa obsahující offsety 8–15:
MMIX zaokrouhlí adresu s offsetem 12 dolů na 8, takže současně
vynuluje COLOR i LINK. Není to zápis osmi bajtů začínající offsetem 12.

4H odebere vrchol ze zásobníku, LDTU načte nulově rozšířený ukazatel,
NEG $1,1,$1 vypočte 1−COLOR(u). První 5H ošetří prázdný seznam.
Druhý 5H načítá TIP; zpětný skok 5B jde právě sem, protože po B7
už je známo, že a≠0. Zdvojená lokální značka je tedy správná.

U 6H jsou právě tři případy:
COLOR(v)=opačná barva → PBZ přeskočí na B7;
COLOR(v)=barva u → CMP není 0 a BNN končí Failure;
COLOR(v)=−1 → oba skoky selžou a proběhne obarvení a push.
STT barvy je signed 0/1, STTU a LDTU zachovají 32bitový pointer.
B7 přejde na NEXT, B8 pokračuje při neprázdném zásobníku,
2H při w≠v0 přejde na 0H. Při w=v0 padne do Success.
Všechny změny souhlasí s B1–B8; nejsou třeba dynamické testy.
ASIZE se v těle programu nepoužívá, ale známá oprava konvence na 20
zůstává zaznamenána.

## Úloha 72: přesný zásobníkový invariant

(a) Je-li v níže než u v zásobníku, PARENT(v) je předek u.
Na začátku je zásobník jednoprvkový. Odebrání vršku zachová všechny
relace mezi zbývajícími položkami. Při zpracování odebraného u mají
všechny dosavadní položky v rodiče mezi předky u; každý nový vršek x
má rodiče u. Tedy rodič každého nižšího v je předek x.
Další nově vložené děti u pod novým vrškem také splňují podmínku,
protože jejich společný rodič je u. To dokazuje invariant indukcí.

(b) Před prvním konfliktem mají všechny hrany již prozkoumaného
vrcholu různé koncové barvy. Konfliktní v tedy nemůže být prozkoumaný.
Je obarvený a v≠u, neboť vstup je graf bez smyček, takže leží v zásobníku.
Nemůže být právě novým dítětem u, protože to má opačnou barvu.

(c) Jeho rodič p je podle (a) předkem nynějšího u (použij stav
zásobníku před odebráním u). V nemá v této situaci nulového rodiče:
kořen se odebral před prvními potomky. Vrchol v není předkem u,
protože předci už byli prozkoumáni, v však dosud leží v zásobníku.
Rodičovská cesta u,...,p, v je tedy prostá a s hranou v–u dává cyklus.
COLOR(u)=COLOR(v), COLOR(p)≠COLOR(v), takže cesta u,...,p má lichou
délku a dvě přidané hrany zachovají lichost.
Tištěné opakování „output u; u←PARENT(u) until u=PARENT(v);
then output u,v“ vypíše přesně tuto posloupnost. Obejde se bez LCA.
Jediný výpis stojí O(n), proto celková mez zůstává O(m+n).
F0 erratum z 2010 k inclusive ancestors je již v prvním dotisku 4A.

## Konec str. 23 a následující odpovědi

Údaje roget: 1022 vrcholů / 5075 oblouků; book jean: 80 / 254 hran;
bi_book jean: 80+356 / 727 hran zůstávají partial. Jejich přesnost vyžaduje
spárování parametrů s příslušnou historickou verzí dat a generátorů.
V této kontrole se nepouštěl generátor ani census. Stejně tak nebyla
nezávisle ověřena faktická shoda ukázkových vazeb s Thesaurem/románem.
Formální bipartitnost incidence postava–kapitola plyne přímo z typů konců.

Celá odpovědní str. 523 a 524 byla nyní přečtena; část 73–78 byla pouze
přečtena a má být jednotlivě doložena v navazujícím bloku. Horní str. 525
byla přečtena z OCR pro navigaci, nikoli považována za celou prověřenou stránku.
Relevantní vrstvy errat: all4a-pre, all4a, err4a, all4f0, err4f0;
v tomto bloku byly zohledněny konkrétní známé opravy, žádné nové podezření.
