# Slova 231 a prvočísla 237–238 — celý zdrojový průchod

3. listopadu 2026. Přečteny otázky 231, 237, 238, jejich odpovědi a hlavní
text od převodu X$ na C$ na 113 po konec prvočíselných příkladů na 114.
Následující USA graf zůstává pro další blok. Oba zdroje mají shodné všechny
**450 číslic prvočíselných obrázků a 80 písmen odpovědi 231**; byly porovnány
skutečné vektorové pozice znaků, nikoli jen ruční přepis.
[Kontrola zdrojů](results/words_primes231_238/source-checked.json).

Žádná nová chyba se nepotvrdila. Dříve přijaté optimalizace 5×5, kontrola
844 modelů a síto pro sedmimístná prvočísla se neopakovaly.

## 231: výplně, ceny i maxima souhlasí

Pravidlo slovníků je v poznámce na hlavní straně 36: pro pět písmen seznam
Stanford GraphBase, pro jiné délky OSPD4 v autorově pořadí. Použili jsme již
archivované `words5-from-sgb` a `words4-from-OSPD4`, nikoli pětipísmenný
OSPD4. Hashe jsou ve výsledcích. Obecná starší otázka pořadí C014 zůstává
odděleně; tady souhlasí všechny vytištěné počty, maxima i výplně.

Při indexování od nuly jsou bonusy: dvojnásobek slova (0,0), trojnásobek
písmene (1,1), dvojnásobek písmene (2,3), trojnásobek slova (3,4).
Každé ze čtyř vodorovných a pěti svislých slov se skóruje samostatně.
Vytištěný příklad WATCH/AGILE/RADAR/TREND má jednotlivé příspěvky
26,10,7,18,14,9,5,7,24, celkem **120**.

| Slov v každém seznamu | Všechny výplně | Maximum | Všechny maximální výplně | Nové hledání |
|---:|---:|---:|---|---:|
| 1000 | 27 | 139 | MAPLE/ARRAY/SMOKE/TYPES | 0,039 s |
| 2000 | 8017 | 176 | HAPPY/EXILE/ALLOW/PELTS | 0,418 s |
| 3000 | 310077 | 197 | JAMBS/EQUIP/TUMOR/SASSY; MAGMA/EQUIP/OUNCE/WAKED | 5,660 s |

Nový [výčet](word231_census.cpp) vyplňuje políčka zleva doprava po řádcích.
U každého písmene protne možné pokračování příslušného řádkového a
sloupcového trie. Tím neodmítne žádnou platnou výplň: každý její prefix je
v obou trie. Každá úplná výplň má jedinou cestu, takže se neopakuje.
Otázka nezakazuje opakování slov; algoritmus je proto dovoluje.

Cena může být sčítána po políčkách: hodnota písmene krát jeho násobitel
krát součet násobitelů daného řádku a sloupce. To je jen přeuspořádání
součtu všech devíti slov. V každém listu C++ znovu zkontroluje původní
slovníky a skóre po jednotlivých slovech. Samostatný Python pak zkontroloval
**všech 318121 výplní**, jejich různost, slovníky i ceny a porovnal celou
množinu maxim. Před ostrými případy souhlasilo 27 malých úplných testů
s nezávislým kartézským součinem řádků.
[Běhy a kontrola](run_word231_bounded.py),
[neměnné výsledky](results/words_primes231_238/word-runs.json).

Každý nový hledací běh měl limit 20 s a nice 15; všechny skončily úspěšně.
Uvedené časy jsou hledání, nikoli rekonstrukce historických memů.

## Hlavní 113–114: převod a úplnost modelu

Nákladové ořezávání z X$ platí i pro C$: nezáporná cena každé vybrané
možnosti se přičte a při návratu odečte. Barevné podmínky mění přípustnost
dalších možností, nikoli součet cen. Tím je podložen přechod k XCC; nejde
o formální verifikaci celé pozdější implementace C$.

Deset primárních položek v (110) vybírá právě jedno prvočíslo do každého
řádku a sloupce. Každé pole má jednu barevnou sekundární položku, která
vynutí shodu obou číslic. Nebarevná sekundární položka pro každé prvočíslo
zaručí jeho nejvýše jedno použití. Obráceně každý čtverec s deseti různými
prvočísly určuje právě tyto možnosti. Převod je tedy obousměrný.

Všech deset čísel v ukázce (109) je různých prvočísel pod 30000, včetně
správně popsané možnosti pro řádek 11069. Z dřívější přijaté kontroly platí
8363 prvočísel, 83630 možností a redukce na 62900. V prvním řádku a sloupci
nemůže být 0, protože by protilehlé číslo mělo méně než pět číslic. V posledním
řádku a sloupci může být pouze 1,3,7,9, protože pěticiferné prvočíslo nemůže
končit sudou číslicí ani 5. To vysvětluje popsané redukce.

Logaritmus je rostoucí a mění součin na součet. Deset zaokrouhlených cen
má celkovou chybu menší než deset jednotek. Přijaté rozdíly mezi příslušnými
cenami a nejbližší vyloučenou cenou jsou 17209307 a 228763, takže poslední
hranici nemohou zaokrouhlení přehodit. Všech deset vytištěných čtverců i jejich
pořadí souhlasí se starými certifikáty. Ty stojí na úplném původním DLX5 a
nezávislé validaci modelů, nikoli na druhém úplném optimalizátoru.

Transpozice zachová součin. Nemá zde pevný bod: symetrický čtverec by měl
stejný i-tý řádek a i-tý sloupec, což zakazují různé prvočíselné položky.
Zobrazená optima proto tvoří dvojice. U těchto pěti nejmenších a pěti
největších cen jsou všechny páry doložené; 237 ukazuje, proč se tato vlastnost
nesmí zobecnit na jedinečnost každého součinu.

## 237: krátký protipříklad

V původním obrázku

    12113
    11003
    10103
    10369
    31391

prohodíme pouze pole (2,3) a (3,2), s indexy od nuly. Dostaneme třetí
řádek 10133 a čtvrtý 10069; ostatní řádky zůstanou stejné. Šest vytištěných
rovností mezi páry souřadnic zaručuje, že se dvě řádková prvočísla prohodí
s odpovídajícími dvěma sloupcovými prvočísly. Množina všech deseti faktorů
zůstane shodná. Nový čtverec se liší od původního i od jeho transpozice.
Starý přesný součin 348481964984280547398266650188504126298613 je přijatý.

Tento protipříklad úplně odpovídá na otázku. Dodatečný údaj o přibližně
třech miliardách speciálních řešení a o tom, že vytištěné je „smallest“,
nemá novou nezávislou reprodukci; viz vynechání níže.

## 238: svědci a malé úplné optimum

Všech deset obdélníků se přesně shoduje mezi zdroji a se starými ověřenými
svědky. Pro n=7 zůstává přijatých 586081 sedmimístných a 143 trojmístných
prvočísel, tedy 3·586081+7·143 = **1759244 možností**.

Nově byl krátce uzavřen případ n=3. Je třeba projít 143 trojmístných
prvočísel v řádcích. První řádek nesmí obsahovat nulu (128 možností),
poslední obsahuje jen 1,3,7,9 (30 možností); obě omezení jsou nutná pro
platnost sloupců. Přímá kontrola 128·143·30 = **549120 trojic** proto
nevynechá žádné řešení. Dostali jsme **29490** mřížek, minimum
24659220812503 a maximum 426974010540948041. Každého dosahuje právě
vytištěný obrázek a jeho transpozice. Výpočet měl nice 15 a trval 5,48 s.
[Malý nezávislý postup](check_prime238_small.py),
[výsledek](results/words_primes231_238/prime238-n3.json).

## Přesný rozsah vynechání a další práce

Podle pokynu uživatele z 3. listopadu se následující drahé reprodukce
výslovně vynechávají a mají v registru `verified:false`:

- 231: historické náklady X$ 6/80/483 Gμ, X 5/95/781 Gμ a trie
  12 Mμ / 628 Mμ / 13 Gμ. Počty a maxima jsou úplně ověřené, tyto náklady ne.
- Hlavní 113–114: historický Monte Carlo odhad přibližně 6·10^14 čtverců;
  náklady 440 Gμ s redukcí, 1270 Gμ bez ní, 280 Gμ za redukci a 22 Gμ
  pro největší ceny. Odhad není přesný počet; optima a redukce jsou přijaté.
- 237: přibližný počet tří miliard mřížek se šesti symetrickými rovnostmi
  a dodatečné tvrzení „smallest“ pro vytištěný příklad. Nejsou potřeba pro
  krátký protipříklad, který je úplný.
- 238: globální minima a maxima n=4,5,6,7 a historický náklad 20 Gμ
  pro n=7 bez redukce. Platnost svědků i počet možností jsou ověřené,
  globální optimum těchto větších instancí není naším nezávislým závěrem.

Šest archivovaných vrstev errat bylo prohledáno podle obsahu a obou
stránkování. Pro tento blok nebyla nalezena relevantní oprava. Okolní opravy
232 a 235 jsou již E105/E104; změny odpovědi 239 patří do následujícího bloku.
Žádný nový nález ani zpráva Knuthovi. Úlohy 231, 237 a 238 mají dokončený
průchod s výše uvedenými mezemi; další jsou 239–246 a hlavní USA příklady.
