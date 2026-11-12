# V4A-F0003: lichá konstrukce skoro regulárního grafu selže pro n=d+1

Potvrzeno 6. listopadu 2026 v doloženém prvním dotisku.
Místo: §7–110, odpověď na str. 528 / file545, Case 1, d=2k+1.
Závažnost medium: explicitní konstrukce produkuje jiné stupně než zadané.
Existenční tvrzení zadání je správné.

## Sazba a předpoklady

Zadání str. 43 / file060 předpokládá
n>d_1≥...≥d_n≥d_1−1 a sudý součet stupňů.
Není zde silnější podmínka n>d+1.
Původní sazba images/proof-file545.png dává pro liché d=2k+1
základní posuny
{2,3,...,k+1, n−k−1,...,n−3,n−2}
a navíc hrany 1–2,3–4,...,(p−1)–p, kde p vrcholů má stupeň d.

## Přímý protipříklad

Vezměme n=4 a požadovanou posloupnost 3333. Platí 4>3, všechny stupně
se liší nejvýše o 1 a jejich součet 12 je sudý. Realizací je K4.

V odpovědi je d=3, k=1, p=4, q=0. Množina základních posunů modulo 4
je {2}: obě její tištěné části se kryjí. Základní hrany jsou tedy
{1,3} a {2,4}. Přidávaný matching má hrany {1,2} a {3,4}.
Výsledný jednoduchý graf má právě čtyři hrany
{12,13,24,34}; každý vrchol má stupeň 2, nikoli 3.

Obecně se to děje pro n=2k+2=d+1 a k≥1: posun k+1=n/2
je antipodální a započte se jen jednou, takže základ nemá zamýšlený
stupeň 2k. Nejde o OCR ani o počítání orientovaných hran;
zadání chce obyčejný jednoduchý graf.

## Oprava a rozsah

Při lichém d a n≥d+2 jsou obě poloviny posunů disjunktní
a původní argument stupňů platí.
Hraniční n=d+1 lze vyřešit zvlášť: začni K_n a odstraň matching
pokrývající právě q vrcholů, které mají mít stupeň d−1.
Q je sudé, protože n je sudé a součet stupňů nd−q je sudý.
Tím zůstane p vrcholů stupně d a q vrcholů stupně d−1.
Tato oprava nemění samotné existenční tvrzení.

## Známá errata

Prohledány relevantní historické/aktuální vrstvy
errata/text/all4a-pre.txt, all4a.txt, err4a.txt, all4f0.txt, err4f0.txt,
podle odpovědi 110, stránky 528 a historického offsetu F0 148,
a podle Case 1, Wang/Kleitman, 2k a konstrukčních výrazů.

Na odpovědi 110 existuje známá oprava z 23. 5. 2011:
v Case 2 se d=2k mění na d=2k>0. Je aplikována; lichého Case 1
a protipříkladu 3333 se netýká. Opravy sousedních odpovědí 105/108
rovněž nemění tuto konstrukci. Odpovídající oprava nenalezena.

Chybová lokace je pouze str. 528 / file545. Zadání na str. 43 je
správné. Tištěný exemplář nebyl nezávisle porovnán a prvenství se netvrdí.
