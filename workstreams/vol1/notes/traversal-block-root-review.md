# Kořenové převzetí §2.3 a §2.3.1

Datum 2026-11-01. Kořen přečetl celé intro-proofs.md, traversal-proofs.md,
tary-generalization.md, HANDOFF.md, progress.json a oba přehledy pramenů
ve zmrazeném parallel/tree-traversal/. Nálezy C0045–C0050 mají oddělené
kořenové revize původních obrazů a matematických či instrukčních důkazů.
Manifest s 208 soubory byl ověřen. Pozdější odstranění chybného dodatku
o hypotéze kontinua je zachyceno aktualizovaným manifestem
f4bec6cbf9af2a0e5328db162e68c921b4cb4d2d3f6e39173db2ab1598921e50.

Přijaty důkazy definic stromu a lesa, adresování, příbuzenství a úloh
úvodu, s výjimkou explicitně evidované terminologické nejistoty C0045.
Při rekonstrukci ze zásobníkové permutace musí být před vyjmutím 1
odstraněny všechny později vložené prvky; jeho k-tá výstupní pozice
proto skutečně určuje levý blok 2,...,k. U konečné vnořené kolekce
maximální podmnožiny určují děti, ale samotná inkluze neurčuje pořadí
sourozenců. Nekonečné kolekce se nesmějí automaticky zaměnit za
induktivně definované konečné stromy.

Pro průchody je silný invariant s libovolným vnějším prefixem zásobníku
dostatečný pro indukci T a jeho variant. Následníky, vložení, kopie,
porovnání a odřezání podstromu mají v důkazech zahrnutou hlavičku,
prázdný vstup a zachování odkazů mimo zpracovávaný podstrom. Kopie
předpokládá disjunktní zdrojové a nově alokované cílové uzly. Ruční
instrukční revize a přesné časové konvence u nálezů jsou rozhodující;
velké konečné testy doplňují obecné invarianty. Není požadována změna
sdílené sémantiky MIX.

Úloha 35 má vlastní podstatné řešení: pevný počet t dětských pozic,
t+1 pořadí návštěv, maskový kód, pokračovací nit v prvním odkazu,
kopii bez zásobníku a cyklické rotace. Rezervy kopie se vytvářejí
zprava doleva, takže jejich pokračovací nitě mají správné preorder
pořadí. Rotační algoritmus obnovuje všech t polí po t+1 návštěvách;
bez další informace neslibuje rozpoznání konkrétní fáze. Otevřenost
zadání nevyžaduje klasifikaci všech představitelných zobecnění.

Celkově zůstávají partial oba hlavní texty, úvodní úloha 15 a průchodové
úlohy 13 a 21 kvůli konkrétním původním zdrojům či osobním atribucím.
C0045, C0046 a C0049 zůstávají candidates; příslušné úlohy se nepočítají
jako úplně checked. C0047, C0048 a C0050 jsou uzavřené technické revize
s potvrzenou chybou, nikoli potvrzení správnosti tištěného řešení.
K C0045 přibyl odlišný potvrzený nález C0056, který míří pouze na
navazující poznámku o dobrém uspořádání; terminologickou otázku neřeší.

Při kořenovém čtení byl odvolán doplňkový argument z hypotézy kontinua:
předci jsou prvky kolekce podmnožin R, nikoli nutně prvky R. Z CH
tedy uvedená mez počtu jejich mohutností bez dalšího důkazu neplyne.
Tento chybný dodatek nebyl použit v reportu C0045 ani v jeho přímém
výpočtu všech úrovní. Vlastník zmrazené složky odstranil jen tento
odstavec a přegeneroval manifest; nezměněné testy se neopakovaly.

Pramenné čtení podagenta je přijato v přesně deklarovaném rozsahu,
bez předstírání nového kořenového čtení všech článků. Ze 42 známých
datovaných položek errat je jedna chybná náhrada C0050; nelze všechny
označit za správné opravy. Další části svazku zůstávají v práci.
