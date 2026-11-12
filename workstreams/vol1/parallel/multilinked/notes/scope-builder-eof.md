# §2.4-13: ukončení konstrukce SCOPE dereferencuje sentinel

Pracovní nález bez globálního ID. Originální obrazy s. 428, 429, 434 a 606
byly přímo přečteny. Stav: doložený protipříklad, čeká na nezávislou kořenovou
revizi. Nejde o kontrolu fyzického exempláře ani tvrzení o prvenství.

## Přesný předpis a nejmenší neprázdný vstup

Odpověď 13 na s. 606 předepisuje použít algoritmus A ze s. 428–429 bez
nastavování NAME, PARENT, CHILD a SIB. Při každém odebrání zásobníkového
záznamu v A5 se má nastavit `SCOPE(P1) <- Q-1`. Při vyčerpání vstupu v A2
se pouze nastaví `L <- 0` a pokračuje; ukončení pro L=0 nastává až v A7.

V A1 se zásobník inicializuje jediným pomocným záznamem `(0,NULL)`.
Originální A5 má dvě větve:

```
if L1 > L:
    remove top entry
    (L1,P1) = new top entry
    repeat A5
if L1 < L: signal error
# now L1 == L
SIB(P1) = Q           # removed by answer13
remove top entry
(L1,P1) = new top entry
```

Na legálním vstupu tvořeném jedinou datovou položkou `1 A`, umístěnou
v tabulce na adrese 1, po běžném zpracování vznikne zásobník
`[(0,NULL),(1,1)]`. Při EOF se nastaví L=0. Dopřejme odpovědi i správné Q=2,
tj. adresu za poslední datovou položkou; problém tedy nezávisí na sporném
výkladu další alokace v A2.

1. V A5 je 1>0. Nastaví se SCOPE(1)=1, skutečný záznam se odebere.
2. Novým vrcholem je `(0,NULL)`, takže L1=L=0. Nastává druhá větev A5,
   která má odebrat i sentinel.
3. Doslovný doplněk „Whenever removing the top stack entry“ požaduje
   SCOPE(NULL)=1. Navíc A5 žádá nový vrchol již prázdného zásobníku.
4. Test ukončení v A7 se tedy nedosáhne korektním výpočtem.

Totéž nastane po **každém** konečném neprázdném legálním vstupu: všechny
skutečné úrovně jsou kladné, a proto je L=0 postupně odstraní a skončí
rovností u pomocného záznamu. Nejde o omezení malého numerického testu.

Doslovné pokračování uvnitř A2 a dále přes A3 navíc alokuje falešný uzel
Q a mění `LINK(P)` posledního jména. Například pro jedinou položku A začne
LINK(A) ukazovat na adresu 2, která není platnou položkou vstupu. Tento
další důsledek nevyužíváme jako jedinou oporu nálezu, protože neformální
slovo „continue“ může být čteno různě; chyba sentinelu v A5 přetrvává i při
vstřícném vynechání A3.

## Oprava a obecný invariant

Na EOF není třeba simulovat běžnou položku. Nechť N je adresa posledního
skutečného uzlu, adresy jsou jednotkově po sobě, a zásobník stále obsahuje
pomocný záznam a dosud neuzavřené skutečné položky. Proveďme přímo v A2:

```
while top.level > 0:
    (level,node) = pop()
    SCOPE(node) = N
stop
```

Nenastavují se PREV ani LINK, nealokuje se nový uzel a neodstraňuje se
sentinel. Prázdný vstup se ukončí bez iterace.

Invariant: před novou skutečnou položkou na adrese Q obsahuje zásobník
právě ještě neuzavřené položky poslední aktivní cesty. Pokud se položka
v A5 odstraní, všechny její potomky jsme již přečetli a poslední položka
jejího podstromu je Q−1. Tato položka je listem, protože jinak by její
potomci následovali ještě před Q. Proto běžné přiřazení SCOPE(P1)=Q−1
je správné. Na EOF je poslední položkou každého dosud neuzavřeného podstromu
právě N, takže závěrečná smyčka dokončí všechny zbývající hodnoty. Každý
skutečný záznam se odebere jednou, čas zůstává lineární.

## Všechny známé vrstvy errat

Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1` podle stran 428–434,
605–607 i hesel SCOPE, Data Table, Algorithm A, stack, exhausted, Dahm.
Přímo zobrazeny příslušné originály PDF: all1-prepre 28 a 46; all1-pre 18;
all1 10 a 15; err1 9 a 14. Na 606 se známé opravy týkají jen odlišení názvů
algoritmů v odpovědích 12 a 14 (6. 1. 2011), doplnění čárek u C' na 607
(24. 6. 2016) a B'' v odpovědi 12 (7. 7. 2023). Žádná neopravuje odpověď 13
ani její závěrečný L=0. Ostatní opravy se týkají formulace kvalifikace,
přiřazovací šipky, příkladů MOVE a bibliografie Lawson 1962.

## English ASCII draft

In answer 2.4-13 (page606), the end-of-input instruction L<-0 does not
reach the termination test in A7 safely. After all real entries have been
popped in A5, the top entry is the sentinel (0,NULL). Since L1=L=0, A5
then pops this sentinel and attempts to read the new top of the empty stack;
the added SCOPE assignment also attempts to write SCOPE(NULL). This happens
even for the one-item input "1 A".

At end of input, instead pop only the remaining positive-level entries,
setting their SCOPE fields to the address of the last real data item, and
terminate directly in A2. This also avoids creating a dummy data item and
changing its symbol-table LINK through A3.
