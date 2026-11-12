# Burks–Warren–Wright 1954 a obrácený preorder

Root přijal neměnný dílčí `BURKS_MANIFEST.json` z adresáře
`parallel/other-trees-originals`, SHA-256
283c07dd20b1718313f5778bf7b89be13773a8a417cdcc42e7c9cd7d84fd6c1c.
Všech 25 lokálních souborů a 17 externích vstupů hashově souhlasí.
Ostatní soubory tohoto adresáře nadále slouží aktivnímu agentovi.

Přímo byly nezávisle přečteny všechny původní strany článku 53–57,
obálka čísla, knižní strany 359 a 575 a oprava v all1-prepre 42.
PDF 5–9 odpovídá článku; celý digitalizovaný sešit má 77 stran,
jejichž zbytek se tímto neoznačuje za auditovaný. Zdroj je veřejná
digitalizace původní sazby MTAC VIII, č. 46, duben 1954:
https://archive.org/details/sim_mathematics-of-computation_1954-04_8_46.
Přesné stažení a SHA-256 jsou v agentově pramenné poznámce a manifestu.

## Shoda postupu

Prefixový zápis řadí operátor před jeho argumenty. Při čtení zprava
doleva tedy zpracuje všechny podvýrazy dříve než jejich operátor.
Článek definuje na s. 53 váhu znaku W<=1 a jeho stupeň D=1-W,
který na s. 55 výslovně identifikuje s počtem argumentů. Konečná
abeceda neomezuje postup jen na unární a binární operace.

Definice 7 na s. 55 bere prvních D již hotových hodnot a nahradí
je výsledkem operátoru; zbývající konec seznamu zachová. To přesně
odpovídá zásobníkovému kroku F2/F3 v obráceném preorder. Hodnoty
argumentů jsou od vrcholu v původním pořadí zleva doprava. Popis
stroje na s. 56 výslovně posílá znaky od pravého konce a registr
posouvá o W=1-D. Věta III dává zřetězení hodnot pro celý les výrazů,
takže souhlasí i závěrečné pořadí kořenů v knižní odpovědi 2.

Vlastní již přijatý důkaz v `notes/other-trees-sequential.md`
byl porovnán s tímto postupem: průchod podstromem zachová dosavadní
zásobník a přidá jedinou hodnotu jeho kořene. Indukce pro děti
zpracované zprava dává správné argumenty i pro obecnou lokální
funkci. Článek realizuje konkrétní konečný logický model; knižní
zobecnění není doslovným přepisem jeho programového rozhraní.

## Uzavření položky

Původní odpověď 575 má krok P<-P-1. Veřejná oprava z 29. 8. 1997
jej mění na P<-P-c, kde c je počet slov jednoho uzlu. Tato známá
oprava byla již zahrnuta v matematickém důkazu a není novým nálezem.
Agentovo společné hledání čtyř vrstev errat nezjistilo změnu citace.

X0291 a celá úloha §2.3.3–2 jsou nově checked. Nový X0816 eviduje
rozsah pramenné kontroly; není druhým matematickým výsledkem téže
úlohy. Úplná certifikace všech externích vět článku ani absolutní
historické prvenství autorů se netvrdí. Staré úspěšné testy se
neopakovaly. Nová chyba TAOCP nevznikla.
