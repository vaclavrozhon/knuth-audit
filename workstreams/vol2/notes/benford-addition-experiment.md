# §4.2.4-2: další měření plovoucího sčítání

Dokončeno 2.11.2026. Celkem179552 operací ve12 blocích, plus5019
přesných kontrol klasifikátoru. Skript `experiment_benford_addition.py` používá
racionální aritmetiku a dříve ověřený model `Arithmetic`; každý výsledek
zaokrouhluje k nejbližšímu číslu, poloviny k sudému. Exponent je neomezený.
Formáty `(b,p)` jsou `(2,53),(10,16),(16,14),(64,9)`, kde b je základ
a p počet jeho číslic. Jde o přibližně srovnatelné délky mantisy, nikoli
stejné množiny reprezentovatelných čísel nebo model konkrétních procesorů.

## Výpočty a definice statistik

- Horner: polynom `sum_{k=0}^{12}(-1)^k x^k/(k+1)` v1001 rovnoměrných bodech
  od−0.95 do0.95, přesně12012 sčítání.
- Gauss: přímá eliminace bez pivotování a zpětný chod pro24×24 silně diagonálně
  dominantní matici `A_ij=20[i=j]+((17i+23j) mod31−15)/64`, indexy od0.
  Pravá strana je přesný součet řádku před vstupním zaokrouhlením;
  přesné řešení jsou samé jedničky. Celkem4876 sčítání/odčítání.
- Oscilátor:2000 kroků klasického Rungeho–Kuttova schématu4.řádu pro
  `x′=v,v′=−x`, počátek `(1,0)`, krok1/100;28000 sčítání.
  Každý mezivýsledek je zaokrouhlen, násobení a dělení se do počtu sčítání nezahrnuje.

Rozdíl exponentů měříme před operací; nulový operand se jako v tabulce1
zařadí do „over5“, ale vynechá z průměru rozdílu. Normalizační posun
je rozdíl většího vstupního exponentu a exponentu přesného součtu.
Záporná hodnota−1 znamená posun vpravo. Nulový výsledek by se zařadil
do „left>4“ jako v knize, ale vynechal z průměru počtu levých posunů.
Také evidujeme exponent zaokrouhleného výsledku: ve všech12 blocích
byl stejný jako u přesného součtu. Podíly v tabulce níže mají za jmenovatel
všechna sčítání daného bloku.

## Naměřené výsledky

| Výpočet | b | Průměr rozdílu exponentů (nenulové operandy) | Vpravo1 (%) | Bez posunu (%) | Průměr levých posunů (nenulový výsledek) |
|---|---:|---:|---:|---:|---:|
| horner | 2 | 2.03917 | 21.370 | 49.151 | 0.32001 |
| gaussian | 2 | 8.28194 | 1.825 | 94.750 | 0.03856 |
| oscillator | 2 | 4.48535 | 20.829 | 78.143 | 0.01261 |
| horner | 10 | 0.68950 | 7.409 | 74.900 | 0.17691 |
| gaussian | 10 | 2.57823 | 0.103 | 99.528 | 0.00390 |
| oscillator | 10 | 1.41566 | 3.871 | 95.829 | 0.00311 |
| horner | 16 | 0.63000 | 1.474 | 88.961 | 0.09565 |
| gaussian | 16 | 2.21400 | 0.287 | 98.872 | 0.00841 |
| oscillator | 16 | 0.85625 | 1.432 | 98.282 | 0.00296 |
| horner | 64 | 0.21125 | 1.474 | 94.056 | 0.04471 |
| gaussian | 64 | 1.28631 | 0.472 | 98.482 | 0.01046 |
| oscillator | 64 | 0.79031 | 6.079 | 93.779 | 0.00143 |

Úplné celočíselné četnosti všech kategorií a výsledky výpočtů jsou
v [JSON](../results/benford-addition.json), protokol v [logu](../results/benford-addition.log).
V každém formátu bylo81 nulových vstupních dvojic v tom smyslu, že
alespoň jeden operand byl nulový; žádný výsledek nebyl přesně nulový.
Vstupní znaménka ani exponenty nebyly uměle nezávisle generovány.

Rozdíly vůči Sweeneyho tabulkám jsou velké a závisejí na úloze.
Například binární Gauss má průměr rozdílu exponentů8.28 proti tištěnému3.1,
zatímco Horner má2.04. U oscilátoru má základ64 více pravých posunů
než základ16, přestože průměr vyrovnávacích posunů klesá.
Tabulky proto lze používat jen s odpovídajícím předpokladem o zátěži;
nejsou obecnými pravděpodobnostními zákony. Tato studie není replikací
šesti historických programů a nepovažujeme odlišné četnosti za chybu knihy.

## Kontrola a omezení

Klasifikátor byl porovnán s nezávislým konečným katalogem exponentových
intervalů na5019 dvojicích včetně nul, rušení a malých základu2/3/10.
Hlavní běh ověřuje přesnou konzervaci četností a přípustné směry posunů
pro stejná či opačná znaménka. Předchozí úspěšné testy kvantizátoru
nebyly opakovány. Ukládání probíhalo po každém dokončeném bloku.
Kontrolní matematické výsledky odpovídají očekávání: chyba řešení soustavy
je nejvýše2e−15; energetická odchylka oscilátoru přibližně2.78e−11
obsahuje i diskretizační chybu Rungeho–Kuttovy metody.
Žádná statistická reprezentativnost, nezávislost jednotlivých operací ani
interval spolehlivosti pro „všechny programy“ se netvrdí.
Časování Pythonu měří pouze provedení experimentu, nikoli rychlost základů
na skutečném stroji. Původní Sweeneyho surová data nebyla získána.
