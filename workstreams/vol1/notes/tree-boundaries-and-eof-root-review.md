# Kořenová revize čtyř mezních případů a ukončení SCOPE

Kořen přímo přečetl originály 390,392,393,397,590,405,596 a
428,429,434,606. Prohledal všechny čtyři vrstvy errat; konkrétní
stránkové výskyty jsou v results/tree-boundary-and-eof-errata.json.
Zobrazeny byly také původní PDF opravy D1 na all1-prepre 44 a
opravy názvů algoritmů na all1-prepre 46; žádná nemění níže uvedené
protipříklady. Podagentí rozšířené tematické hledání je v jejich
samostatných důkazových podkladech. Fyzický exemplář stále chybí.

## C0057: barevný les bez hran

Na 393 je doména výslovně tvořena nezápornými vektory n a q.
Pro jednu červenou tečku a žádnou hranu je celkové n=1,q=0,k=1.
Platí všechny čtyři podmínky definice na 392. Předepsané t=f(V_q)
neexistuje, protože posloupnost odstraněných vrcholů je prázdná.
Inverzní postup navíc potřebuje poslední barvu prázdné posloupnosti.
Nejde o interpretaci pořadí, ale o chybějící větev výslovně dovolené
domény. Doplňme q=0 zvlášť: počet přiřazení barev je multinomický
koeficient n!/(n1!...ns!). Počítací formule zůstává správná.
Potvrzena pouze tato drobná mezní vada konstrukce. Historický Raney
slouží jako doplňkový podklad podagenta, nikoli jako nutný předpoklad
tohoto nezávislého kořenového protipříkladu.

## C0058: lineární dekodér a jeden vrchol

Definice na 390 výslovně zapisuje první číslo pouze pro n>1.
Kód jednoho vrcholu je tedy prázdný; zadání 16 na 397 neomezuje n>=2.
I po veřejné opravě D1 z 8. 11. 2005 nastaví D1 C[1]=0,k=0,j=1,
D2 nastaví k=l=1 a D3 čte neexistující f(V1). Správný výstup má
jediné PARENT[1]=0. Je nutný samostatný základ před D2 nebo výslovné
omezení domény. Sousední úloha 14 o posledním členu prázdný kód
implicitně nepoužívá, ale její doménu nelze automaticky přenést na
samostatně formulovanou úlohu 16. Potvrzená mezní chyba algoritmu.

## C0059: souvislá funkce tvořená pouze cyklem

Odpověď 17 chce z funkce s m vrcholy a cyklem délky k odstraňovat
m-k listů, pak podle f(V_(m-k)) navázat zbytek cyklu. Pro k=m není
poslední odstraněný list. Navíc posloupnost délky m-1 nemůže mít
posledních m členů různých. Například f(1)=2,f(2)=1 splňuje přesně
zadání s m=k=2. Proto obecně formulovaná bijekce neplatí na celé
své doméně. Počet funkcí ani závěrečná formule nejsou chybné:
pro k=m je (m-1)! cyklických uspořádání, což odpovídá také dosazení
do vzorce. Potvrzena drobná mezera v popsaném důkazu, nikoli chybný
výsledek enumerace. Oprava je vyřídit tento případ před bijekcí.

## C0060: Huffmanův H a jedna váha

Zadání 13 na 405 dovoluje m=1. Rozšíření prázdného binárního stromu
je jeden vnější kořen, pole L a R jsou prázdná a A[1]=w1 je celý
výsledek. I když algoritmu velkoryse povolíme pracovní sentinel
A[2]=infinity, H1 dává x=1,i=2,j=0,k=1, H2 vybírá sentinel y=2
a H3 píše L[0],R[0],A[0]. Test k=1 v H4 již přijde pozdě.
Potvrzená mezní chyba H; oprava je skončit po zkopírování vah pro
m=1. Nejde o zpochybnění správnosti pro záporné váhy při m>=2;
podagentův invariant dvou front tuto netriviální část řeší zvlášť.

## C0061: závěrečné vyprázdnění zásobníku SCOPE

Originální A5 odstraňuje i záznam s úrovní rovnou L a následně
čte nový vrchol. Po jediném legálním vstupu „1 A“ obsahuje zásobník
(0,NULL),(1,1). Předpis odpovědi 13 na 606 při konci vstupu nastaví
L=0. Dokonce při správném Q=2 a přeskočení nežádoucího A3 nejprve
odstraní (1,1), pak při rovnosti odstraní sentinel (0,NULL), zapíše
SCOPE(NULL) a čte prázdný zásobník. Test v A7 jej nezachrání.

Chyba nastává po každém konečném neprázdném legálním vstupu,
protože všechny skutečné úrovně jsou kladné. Oprava má být přímo
v A2: při konci vstupu odstranit pouze kladné úrovně, jejich SCOPE
nastavit na poslední skutečnou adresu N a ukončit. Tento konec
nevytváří novou položku ani nepřepisuje tabulku jmen. Invariant
preorder intervalu podstromu dokazuje SCOPE=N pro všechny zbývající
otevřené položky. Jde o potvrzenou algoritmickou chybu; na rozdíl
od předchozích čtyř není omezena na malý mezní vstup.

U všech pěti položek je jednoznačný matematický nebo instrukční
rozpor s doslovným předpisem. To odůvodňuje stav confirmed proti
našemu skenu, nikoli předpověď autorova redakčního posouzení,
prvenství nebo odměny. Všechny původní velké úspěšné testy zůstaly
neopakovány; zde postačují krátké nezávislé ruční průběhy.
