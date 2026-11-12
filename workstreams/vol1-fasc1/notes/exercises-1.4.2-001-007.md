# §1.4.2′ — úlohy 1–7

Recovery7November2026: The historical partial labels for6/7 below are superseded by `exercises-1.4.2-006-007-recovery.md`, which supplies the complete context protocol and optimal MMIX program. The old note is retained as evidence of the earlier scope.

Zadání p. 72–73 / file 80–81; odpovědi 1–6 p. 115–116 / file 123–124.
Pro 7 není dodán hotový program. Nejde o opakování starých kontrol NUL.

**1.** Jediné místo předávání v jedné korutině lze obsloužit obyčejnou
subrutinou s jediným návratem. Dvě či více míst se dají zakódovat stavovým
přepínačem, který při vstupu vybere pokračování. Smysl coroutine linkage
se proto projeví hlavně při mnoha pokračováních; tvrzení o obtížnosti
najít jednoduchý didaktický příklad je zdůvodněná autorská zkušenost,
nikoli univerzální dolní mez velikosti programu.

**2.** Při startu In se první znak vydá GO na Out1. Out1 ale nejprve
nastaví outptr a hned provede GO pro další znak, před prvním STBU.
První $0 se tedy ztratí. Například `a.` by dalo jen period, pokud by
ostatní vstup splnil kontrakt NextChar. Knižní odpověď je správná.

**3.** Každý znak stringu v TETRA se rozšíří na celé tetrabyte, nejde
o jednu slepenou patnáctibajtovou konstantu. Patnáctkrát 00000020,
potom 0000000a a 00000000 vytváří přesně 16 trojic znakových míst,
15 oddělovacích mezer, newline a null. Detailní offsety V0133.

**4.** Při přechodu A→wrapper B uloží GO pokračování A do a. B uloží
aktuální rR do rR_A, obnoví rR_B a GO t,b se vrátí do posledního
pokračování B. Wrapper A dělá opačné uložení/obnovení. Indukčně má
každá korutina při pokračování svůj poslední rR. Počáteční soukromé
hodnoty musí být inicializovány stejně jako počáteční a/b. Vazba má
GO 3υ + GET 1υ + PUT 1υ + GO 3υ =8υ; $255 je scratch dle konvence.

**5.** PUSHJ $255,B dočasně schová všechny aktuální lokály a rJ
obsahuje pokračování A. Wrapper B jej uloží do a, obnoví rJ=b a
POP 0 zruší právě vytvořený dočasný rámec. Lokály se tím vrátí do
původního stavu a kontrola přejde na pokračování B. Opačný wrapper
je symetrický. Cena je 1+1+1+3=6υ, dvakrát základní GO vazba, pořád
konstantní. Nejde o vytvoření dvou samostatných zásobníků.

**6 — partial pro samostatné kontexty.** Pokud A ponechá na zásobníku
rámec a aktivuje B, musí B před aktivací A vrátit základ, počet i obsah
chráněných lokálů do stejného stavu. B smí mezitím dělat libovolné řádně
vnořené PUSH/POP; indukce na těchto dvojicích dokazuje zachování rámce A.
Přepnutí uvnitř neukončeného B rámce by naopak změnilo interpretaci A
registrů. Samostatné context switch pomocí SAVE/UNSAVE je pouze návod
„with care“: není zde úplně implementován a nepřebírá se jako důkaz
přesné SAVE/UNSAVE inverze či bezpečné správy jeho ukazatelů.

**7 — optimalita kódování doložena, úplný MMIX partial.** Po odstranění
oddělovacích whitespaces rozdělme cílový text před period na maximální
běhy stejného znaku. Token vstupního kódu vydává pouze jeden opakovaný
znak, takže nemůže spojit dva různé běhy; optimum je součtem jejich
nezávislých optim.

Pro běh nondigit délky `l=10q+r`, 0≤r<10, stojí nejkratší kód
`2q+min(r,2)`. q plných bloků se kóduje jako `9c`; zbytek délky 1
jako samotné c, délky 2–9 jako `(r−1)c`. Dolní mez: a dvojznakových
tokenů a s literálů pokryje nejvýše 10a+s znaků při ceně 2a+s.
Pro a≤q je cena nejméně l−8a≥2q+r; pro a≥q+1 nejméně 2q+2.
Minimum obou mezí je uvedený vzorec a konstrukce ho dosahuje.

Digit nelze vydat samotným literálem, proto pro jeho běh délky l je
nutných aspoň ceil(l/10) tokenů a cena je `2 ceil(l/10)`. Bloky délky
nejvýše 10 této meze dosahují; jediný digit c se zapíše jako `0c`.
Závěrečná period se vydá jediným literálem, prefix opakování by pouze
prodloužil kód. Případ `0z` je proto správně označen za zbytečný.

Stačí průběžně držet znak běhu a čítač 1–10, plné desítky vydávat hned
a zbytek vydat při změně znaku nebo period. Není potřebná neomezená
paměť ani počítadlo celé délky. Newlines lze vkládat bez vlivu na zadané
minimum. **Partial:** úplný požadovaný MMIX program s korektním čtením
všech povolených vstupů a formátováním není zde nově vytvořen; výše je
obecný optimální algoritmus a důkaz, nikoli tvrzení o spuštěném programu.
