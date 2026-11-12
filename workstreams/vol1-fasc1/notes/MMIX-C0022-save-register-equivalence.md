# MMIX-C0022 — SAVE rozlišuje lokální a globální registry

Confirmed, medium, book; nezávislá kořenová revize přijata v X0074 dne12.11.2026.
Přesné místo: druhý odstavec odpovědi§1.4.1′–10,
p114/file122. Odstavec rozšiřuje irelevanci rozdělení registrů
i na SAVE/UNSAVE/RESUME při absenci PUSH/POP, s výjimkou
globálního cíle SAVE a nemarginal cíle některých RESUME operací.

Proti tomuto rozšíření stačí samotné **správně provedené SAVE**.
Po něm je rL0, takže původní lokální registry čtou jako marginal
nuly; ostatní globální registry zůstávají beze změny. Toto je
normativní vlastnost, nikoli selhání implementace SAVE.

## Dva úplné přípustné programy

`sources/register-permutation-local.mms`:

```
        GREG    0
x       IS      $2
        LOC     #100
Main    SET     x,5
        SAVE    $255,0
        SET     $255,x
        TRAP    0,Halt,0
```

Druhý zdroj, `sources/register-permutation-global.mms`, mění
pouze `x IS $2` na`x IS $254`. To odpovídá permutaci2↔254,
která ponechává$0,$1,$255. Jediný nulový GREG zaručuje v obou
počáteční G254. Při běžném vstupu Main je v obou L2; $2 čte
marginal0 a global$254 je výslovně inicializovaný0. Počáteční
hodnoty tedy **už samy odpovídají této permutaci**. Žádná
nevyřešená interpretace nenulové GREG inicializace sem nevstupuje.

SAVE cíl$255 je v obou případech globální a permutace jej nemění.
Nejsou zde žádné PUSH/PUSHGO/POP, GET rL, PUT rL/rG, RESUME,
vadný UNSAVE obraz nebo pokus o POP prázdného zásobníku. Vstupní
stack má obvyklý platný prostor pro několik desítek osmibajtových
položek. Program žádnou cizí nebo zápornou paměť neadresuje.
V$255 se po SAVE dočasně nachází korektní pointer na uložený
kontext; následující SET jej záměrně zahodí. Žádná instrukce
nepožaduje pozdější UNSAVE a program může platně skončit.

## Úplný přechod a obecná rodina

| Místo | x=$2 | x=$254 |
|---|---|---|
| před prvním SET | L2, x0 | L2, x0 |
| po SET x,5 | L3, local$2=5 | L2, global$254=5 |
| po SAVE $255,0 | L0, $2 je marginal0 | L0, global$254=5 |
| po SET $255,x | $255=0 | $255=5 |
| výsledek Halt |0 |5 |

Normativní řetězec je přímo v`mmix-doc-20131017.w`:
definice marginal zdroje v části před1663 a SAVE2718–2751.
SAVE uloží current locals, vynuluje L, zapíše globals a uvedené
special hodnoty do paměti a vrátí pointer ve svém globálním cíli.
Uložení globálních hodnot není jejich vymazání. Po SAVE smí
program pracovat s novým prázdným lokálním rámcem; dokumentace
varuje konkrétně před POP bez odpovídajícího UNSAVE, který zde není.

V primárním simulátoru2013 i2025 je SAVE větev2273–2288.
Výslovně provede `L=g[rL].l=0`, uloží globální hodnoty čtením
`x=g[k]` a následným zápisem do paměti, a přes`store_x` zapíše
výsledný pointer jen do zvoleného cíle$255. Global$254 tak v druhém
programu opravdu zůstane5. Načítání marginal zdroje vrací0.
Přebírá se již přijatý korektní SAVE kontrakt; celý inverse
SAVE/UNSAVE se znovu nedokazuje ani netestuje.

Obecně vezměme libovolný lokální index j<G, jiný globální
index k≥G a globální SAVE cíl d≠k. Před SAVE nechť je hodnota
proměnné v obou přejmenovaných verzích stejné nenulové64bitové
v. Po SAVE je L0, tedy čtení j vrátí0 a čtení k vrátí v.
Zápis výsledného pointeru do d žádný z těchto dvou zdrojů
neovlivní. Je to celá rodina rozporů pro každé v≠0, nejen
výsledek několika náhodných testů. Pro v0 rozdíl správně mizí.

## Jediná cílená reprodukce nových svědků

`verify_register_permutation_save.py` jednou sestavil současný
primární MMIX a **poprvé** spustil každý čtyřinstrukční zdroj.
Oba sestavovací kroky i oba běhy uspěly napoprvé:

* lokální varianta skončila procesním návratem0;
* globální varianta skončila procesním návratem5;
* obě vykonaly4 instrukce, nominálně20μ+8υ.

Celkem1.4355s včetně sestavení, nice15. Úplné listingy,
profily, příkazy a source/object SHA256 jsou v
`results/register-permutation-save*.json` a odpovídajících
`register-permutation-{local,global}-{listing,profile}.txt`.
Shodná tabulková cena SAVE neznamená shodný počet skutečně
uložených položek; tabulka je předem deklarovaný nominální model.
Nebyl spuštěn žádný starý verifier, žádný tištěný NNIX SAVE
program ani dřívější SAVE/UNSAVE inverse test. Běhy neopakovat.

## Originál, známá errata a oprava rozsahu

Originál122 je uložen a zobrazen jako
`images/recovery-subroutine-answers-122.png`. Jde o evidované
digitální vydání3 zkvětna2023, nikoli ověřený fyzický výtisk.
Zkoumaný druhý odstavec skutečně zmiňuje SAVE a připouští jen
uvedenou podmínku globálního cíle; oba svědci ji splňují.

`results/errata-C0022.json` obsahuje13 vrstev s otisky a kontexty
shod. Fasciklová oprava114 doplňuje PUT rJ vodpovědi9; opravy39
upravují definici GREG a97 označení marginal$X. Žádná neopravuje
rozšíření vodpovědi10. Ostatní svazkové permutation/equivalent
výskyty patří nesouvisející matematice nebo bibliografii.

Dva relevantní odkazy z upstream indexu byly navíc přímo přečteny:
[SAVE v kernel mode](https://mmix.cs.hm.edu/bugs/bug1.html) opravuje
nesprávný stack-alert příznak v MMIX-PIPE při záporném kernel
stacku; náš obyčejný program žádný takový stack nepoužívá.
[UNSAVE infinite loop](https://mmix.cs.hm.edu/bugs/bug_unsave.html)
opravuje neplatné malé G načítané z vadného obrazu; zde není
žádné UNSAVE. Oba původní veřejné reporty jsou uchovány jako
`sources/C0022-upstream-relevant-reports.txt`. Tyto známé opravy
se nezapočítávají jako nové nálezy a nemění kontrakt rL←0.

Správná výuka má výslovně říci, že po SAVE všechny dřívější
lokální hodnoty **nejsou přístupné jako current locals**, kdežto
globals kromě cíle zůstávají. Rozšíření obecné zaměnitelnosti na
SAVE proto v uvedené podobě neplatí. Po řádném UNSAVE příslušného
obrazu lze hodnoty obnovit; tento samostatný správný inverse
se nálezem nezpochybňuje. Žádná oprava doprovodného programu
není navrhována. Správné definice SAVE vknize nejsou chybné
stránky a nemají být tímto nálezem vybarveny.

Vzorové zásady: platné počáteční stavy, přesná obecná rodina,
všechny účinky transformace a rozlišení vadného odvozeného
tvrzení od správné základní operace. Samotný numerický běh
nenahrazuje stavový důkaz. Další počáteční GREG otázka v prvním
odstavci je oddělená od tohoto protipříkladu.
