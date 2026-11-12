# Kandidát: nesprávné pole CMP5 v odpovědi §2.3.1-22

Kořenový stav při předání: **V1-C0047, confirmed**. Globální ID přidělil koordinátor; lokální dočasné označení a níže zachovaná historie revize slouží návaznosti evidence.
Dočasné označení `morris-index-compare`; kořenově potvrzeno jako V1-C0047. Originály přečteny: 134 (`../../images/vol1-file149-p134.png` vzhledem ke složce parallel/tree-traversal), 325, 568. Konkrétní změna níže je naše oprava, nikoli publikované erratum.

## Kontrakt a nezávislý ruční důkaz

Odpověď 22 na straně 568 výslovně používá konvence programů T a S. Na straně 325 jsou `LLINK EQU 1:2` a `RLINK EQU 1:2`: levý odkaz je v bajtech 1–2 slova uzlu, pravý ve stejných bajtech následujícího slova. Adresa P je v rI5. Program U má na řádku 05 `CMP5 1,6(RLINK)` a na řádku 06 `JE 5F`; komentář požaduje skok právě tehdy, když `RLINK(Q)=P`.

Pravidlo CMPi na straně 134 je analogické CMPA: vybírá **stejné pole v registru i v paměti**, nikoli celý index proti vybranému poli. Celé doplnění pro indexové registry výslovně stanoví, že jejich bajty 1, 2 a 3 se při porovnání považují za nuly; příklad v závorce říká, že při F=(1:2) nemůže výsledek být GREATER. Proto má uvedená instrukce levou hodnotu 0 pro každou adresu P. Testuje `RLINK(Q)=0`, nikoli `RLINK(Q)=P`.

Nejkratší selhávající neprázdný strom má dva uzly. Zvolme `HEAD=900`, kořen `P=1002`, jeho levý list `Q=1004`; oba pravé odkazy a levý odkaz Q jsou nulové. Správné inorder pořadí je Q,P.

| Krok | Důsledek |
| --- | --- |
| `LD5 HEAD(LLINK)` | rI5 = 1002 |
| `J5Z DONE` | neskáče |
| `LD6 0,5(LLINK)` | rI6 = 1004 |
| `J6Z U6` | neskáče |
| `CMP5 1,6(RLINK)` | porovná 0 s 0, nastaví EQUAL |
| `JE 5F` | skočí k odstranění domnělé nitě |
| `STZ 1,6(RLINK)` | znovu zapíše již nulový pravý odkaz Q |
| `JMP VISIT` | navštíví pouze P |
| `LD5 1,5(RLINK); J5NZ U3` | rI5 = 0, skončí |

Levé dítě Q nebylo navštíveno. S jedním uzlem se žádné CMP5 nevykoná, proto jsou dva uzly minimální. Důkaz platí pro každý radix 64 až 100 a nevyužívá výsledek simulátoru. Obecně původní U pouze prohledá pravý hřbet levého podstromu až k nulovému odkazu, chybně usoudí, že našel nit, a levý podstrom přeskočí. Navštěvuje tudíž jen pravý hřbet celého stromu.

## Místní opravy a registry

Průhledná oprava vloží mezi řádky 04 a 05 přípravu adresy ve správném poli A a změní CMP5 na CMPA:

```text
       ENTA  0,5
       SLA   3
U4     CMPA  1,6(RLINK)
       JE    5F
```

Při radixu b a platné adrese P < b^2 má A po posunu hodnotu P*b^3, tudíž jeho pole (1:2) je právě P. Při opakování U4 se P nemění. Po každé návštěvě, která může změnit A, se před dalším hledáním příprava opakuje. Oprava mění navíc A; ostatní původně nezměněné registry zachovává. Tuto dodatečnou změnu A nelze zatajit, pokud volající požaduje jeho zachování. Běžný vstupní kontrakt traversal programů uvádí rI5, nikoli zachování A.

Varianta zachovávající všechny původně nedotčené datové registry používá jen stávající pracovní rI4 a jedno samomodifikované adresní pole. Nahradí řádky 05–06 takto:

```text
U4     ST5   TEST(1:2)
       LD4   1,6(RLINK)
TEST   DEC4  0
       J4Z   5F
```

První instrukce nastaví operand TEST na P, takže rI4 po TEST obsahuje `RLINK(Q)-P`. Rozdíl dvou platných adres se vejde do indexového registru. Při nerovnosti následující původní řádek 07 nastaví rI4 znovu na Q; při rovnosti není stará hodnota rI4 dále potřebná. Původní U již používal rI4, rI5, rI6, J a příznak porovnání. Tato oprava nepřidává zásah do A, X, rI1–rI3; navíc zapisuje vlastní operand TEST. Její rozdílná konečná hodnota příznaku porovnání není zachovávacím kontraktem původního U zaručena. Varianta je vhodná jen pro obvyklý zapisovatelný MIX program.

## Časy a reprodukce

Pro neprázdný strom značí n počet uzlů, a počet nulových pravých odkazů a b počet uzlů na pravém hřbetu (zde b není radix). Zamýšlený počet průchodů U4 je `2n-2b`. První oprava přidá 3u při každém ze `2(a-1)` vstupů do hledání, tedy její čas je `21n+12a-9-14b`. Druhá přidá 3u při každém průchodu U4, tedy `27n+6a-3-20b`. Jde o inorder průchod, počítá se instrukce skoku k VISIT, ale ne externí práce VISIT a jeho návrat. Prázdný strom má v obou případech 3u a musí být oddělen od formulí pro n>0.

`check_mix.py` obsahuje celý původní program i první opravu. Záznamy běhů jsou v `results/mix.json`; první selhání původního U je zachováno v `results/mix-run2.log`. Konečné testy doplňují ruční důkaz; nejsou základem závěru o CMPi. Společné MIX jádro ani assembler se neměnily.

Čtyři erratové vrstvy byly prohledány podle stran 134, 325 a 568 i témat CMP5, RLINK, Morris, comparison a compare. Přilehlé původní erratové stránky byly prohlédnuty v inventární kontrole. Známá oprava odpovědi 22 přidává ukončovací značku, nemění CMP5. Přesný nový hledací výstup: `results/morris-errata-search.txt`.
