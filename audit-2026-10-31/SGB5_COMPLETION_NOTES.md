# Dokončený výčet dvojitých slovních čtverců — DLX87

Převzetí 2. listopadu 2026. Navazuje na [původní kontrolu 87–90](DOUBLE_WORDS_NOTES.md)
a historický záznam X087. Původní hledání se neopakovalo.

Wrapper 862562 skončil v 18:53:21 UTC s návratovým kódem 0. Původní DLX2
s autorovou úpravou z úlohy 83 dokončil **323 264 řešení** nad přesnými
5 757 slovy ze Stanford GraphBase. Každý čtverec má deset různých slov;
transpozice proto nemá pevný bod. Omezení prvního řádku ponechává právě
jednu orientaci každé transpoziční dvojice.

[Samostatný přijímací program](accept_sgb5_terminal.py) prošel všech
323 264 uložených modelů. Přímo z řádků vytvořil sloupce, zkontroloval
příslušnost všech deseti slov do slovníku, jejich různost, jedinečnost
čtverců i transpozičních tříd a celý histogram nejhoršího slovního pořadí.
Všechny součtové i XOR hashe souhlasí s validačním záznamem původního běhu.
Nezávisle také rekonstruoval všech 57 570 řádků vstupní matice a ověřil
hashe zdrojů, binárky, vstupu, logu a výsledků.

Výsledek souhlasí s dříve dokončeným nezávislým buňkovým výčtem:

```text
(1 787 056 všech čtverců − 1 140 528 s opakovanými slovy) / 2
    = 323 264 transpozičních tříd.
```

Celé surové modely staršího buňkového výčtu nebyly archivované. Jde tedy
o shodu dvou úplných počtů a přímou kontrolu všech nynějších uložených
modelů; netvrdíme přímé porovnání dvou uložených úplných množin.

Nejlepší nejhorší pořadí je 1 720 s jedinou třídou, další 1 800 se třemi
třídami. To znovu potvrzuje již přijaté omezené výčty k úloze 88.

## Historický náklad zůstává otevřený

Původní log uvádí tyto počty paměťových operací (*mems*):

| Složka | Přesný počet |
|---|---:|
| Inicializace | 350 349 033 |
| Hrubé hledání | 18 357 857 861 641 |
| Údržba délek sekundárních položek | 4 073 343 716 664 |
| Hledání po odečtu údržby | 14 284 514 144 977 |

Efektivních **14,284514144977 T** přesně nereprodukuje knižních **15 T**.
Rozdíl samotný nedokazuje chybu: historické pořadí položek, možností a
verze programu nejsou plně doložené. Celá úloha 87 proto zůstává `partial`;
nový D081 uzavírá jen přesný počet, uložené modely a jejich validaci.
Nevzniká nový nález ani kandidát.

## Doklady

- [Přijatý výsledek a hashe](results/double_words/sgb5-terminal-checked.json)
- [Koncová metadata běhu](results/double_words/dlx-all-sgb5-run.json)
- [Výsledek, histogram a svědci](results/double_words/dlx-all-sgb5.json)
- [Všechny dvojité modely](results/double_words/dlx-all-sgb5-double-models.txt.gz)
- [Původní log DLX2](results/double_words/dlx-all-sgb5.log)
- [Dříve přijatý nezávislý počet](results/word_rectangles/cell-5x5.json)

Surový stdout DLX2 má průběžně vypočítaný hash, ale není uchovaný celý.
Kompletní odvozený seznam řádkových slov všech řešení je archivovaný.
Neopakovat hotová hledání; případná další práce se týká historického
benchmarku a samostatných otevřených úloh.
