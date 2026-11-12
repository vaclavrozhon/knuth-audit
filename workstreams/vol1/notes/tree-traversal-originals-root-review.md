# První strany původních stromových článků — kořenová revize

Root převzal celý zmrazený parallel/tree-traversal-originals.
FINAL_MANIFEST.json, SHA-256
1f6df0eede9a157a0aefddf8caf15214336d8f5828d01c645c590687398637bd,
obsahuje 116 souborů o 8 451 713 bytech a 32 externích vstupů.
Všechny délky a hashe byly porovnány. Starší dílčí Dwyerův
manifest je uvnitř a nepředstavuje další nezávislou kontrolu.

Root přečetl HANDOFF, REPORT, oba strojové stavy, obsahovou
kolaci, přístupové meze a Dwyerovy datovací doklady. Agent
i root přímo přečetli všechny čtyři získané první strany:
Morris 197, Robson 12, Lindstrom 47 a Dwyer 143. Root přímo
porovnal knižní 567–568 a vydavatelský rejstřík 2001 na 339.
Žádné úspěšné matematické testy U/W se neopakovaly.

## Co jednotlivé stránky dokládají

Morris, Traversing Binary Trees Simply and Cheaply,
IPL 9(5), 16. prosince 1979, 197–200, DOI 10.1016/0020-0190(79)90068-1:
197 přímo dokládá autora, datum, deklarovaný lineární čas
a dva pracovní ukazatele bez zásobníku/bitů v uzlech.
Začíná odvození inorder pomocí nejpravějšího uzlu levého
podstromu. Věta pokračuje na 198; úplný pseudokód, rozpoznání
vláken, obnova a preorder/postorder varianty zde nejsou.
Chybějí 198–200.

Robson, An Improved Algorithm for Traversing Binary Trees
Without Auxiliary Stack, IPL 2 (1973), 12–14,
DOI 10.1016/0020-0190(73)90018-5: strana 12 přímo popisuje
zásobník v odkazech již navštívených listů. Na zásobníku
jsou uzly se dvěma neprázdnými podstromy, jejichž levý
podstrom je dokončen a pravý se právě prochází. To přesně
podporuje konkrétní odstavec knihy 567. List znamená uzel
vstupního stromu bez potomků, nikoli volnou paměťovou buňku.
Původní program Fig. 1 na 13–14 stále chybí; netvrdíme jeho
úplnou kontrolu ani samostatně prověřenou dostupnost listu
při každém vložení na zásobník.

Lindstrom, Scanning List Structures Without Stacks or Tag
Bits, IPL 2 (1973), 47–51, DOI 10.1016/0020-0190(73)90012-4:
47 potvrzuje bibliografii, přijetí 15. ledna 1973 a rozlišení
stromů, sdílených podstromů a cyklů. Rozlišuje průchod
v předepsaném pořadí od skenování s opakováním uzlů.
Vlastní rotační algoritmus ani pozorování o každé třetí
návštěvě z knihy 568 zde ještě nejsou. Chybějí 48–51.

Dwyer, Simple Algorithms for Traversing a Tree Without an
Auxiliary Stack, IPL 2 (1974), 143–145,
DOI 10.1016/0020-0190(74)90052-0: 143 obsahuje celé T1–T4.
Při každé návštěvě otáčí levý, pravý a zpětný odkaz
a pokračuje do bývalého levého potomka. To je přesně
rotační jádro knižního W5. Dwyer reprezentuje chybějícího
potomka odkazem na sebe; kniha používá nulu, pomocný koncový
symbol a W2 k obejití prázdné větve. Nejsou to totožné
instrukční zápisy. Doklad původní rotační myšlenky je přímý;
pokračování důkazu, varianty, bibliografie i přímá opora
nezávislosti na Lindstromovi chybějí na 144–145.

Čteny jsou tedy 4 z 15 původních stran. Zbývajících 11 je
výslovně určeno, nikoli nahrazeno novějšími učebnicemi.
Přijaté matematické důkazy knižních U/W tím nejsou znovu
otevřeny. Celá §2.3.1–21 / X0398 zůstává partial.

## C0090: rok Dwyerovy citace

Kniha 567 společně uvádí Lindstroma a Dwyera pod rokem 1973.
Dwyerova původní 143 tiskne 1974 a přijetí 15. prosince 1973.
Archivovaná stránka celého čísla 2(5) uvádí 123–151 (1974);
vydavatelská Crossref data uvádějí leden 1974. To silně
podporuje 1974 jako bibliografický rok samotného článku.

Proti tomu stojí původní sazba vydavatelského rejstříku
IPL 78 (2001), 339: Dwyerova položka 96 má 2(5) (1973), 143–145.
Rok 1973 zde mají všechny články čísla 2(5), zatímco od
položky 99, čísla 2(6), už 1974. Není to tedy jednotná konvence
roku začátku celého ročníku. Případné odlišné nominální
datum čísla oproti záhlaví článku nemáme doloženo.
Původní obálka/tiráž 2(5) stále chybí. Datum přijetí samo
nevylučuje pozdní prosincové vydání a neprokazuje den tisku.

Root proto ukládá rozpor jako C0090 candidate, nikoli
confirmed. Pravděpodobná úprava by oddělila citace a dala
Dwyerovi 1974; nevztahuje se k času objevu ani k jeho
nezávislosti. Přesný zbytek je bibliografické datování čísla,
ne matematická chyba W.

Všechny čtyři vrstvy errat byly agentem tematicky prohledány
a relevantní obrazy přímo přečteny; root přečetl jejich
výpisy a přesné vymezení. Opravy formulace triple order
a křížových odkazů na 568/570 nemění citované roky.
Lokální ASCII návrh nebyl odeslán.
