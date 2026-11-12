# Úlohy 7.2.2–71 a 72: samoodkazující dotazníky

Kontrola 1. listopadu 2026, 4B strany 61 a 411–413.
Tabulka 666, všechny vytištěné příklady, počty a zaokrouhlená časování
jsou správné. F097 níže je samostatná chyba oficiálního doprovodného
programu; doložené knižní výsledky 71–72 nemění.

## Význam odpovědí a nezávislý model

Studentovy volby a_j a známky x_j jsou různé proměnné. Požadujeme
x_j ⇔ f_(j,a_j)(a,x), nikoli jen pravdivost všech zvolených vět.
Proto stejný seznam odpovědí může mít více konzistentních známkování,
nebo žádné. Maximum se bere přes všechny konzistentní dvojice.

Přímý výčet warmupu dává AA→00, BA→00, AB→10 nebo 11, BB→žádné.
Obecná formule F v knize přesně vyjadřuje těchto n implikovaných
ekvivalencí. Příklady f₁C, f₄D a f₁₂A souhlasí: v PDF je u f₁C
a₂ **≠** A, což textová extrakce ztrácí. Dále f₁₄E nutí výskyty
2,3,4,5; protože součet četností je 20, pátá četnost musí být 6.
Volby 10E a 17E dávají x₁₀=¬x₁₇ a x₁₇=x₁₀, tedy spor.

Důležité konvence jsou v modelu explicitní:

- 7 dovoluje více stejně četných maxim. Je tam „An answer“.
- 8 nejprve vyřadí všechny četnosti, které jsou shodné s nějakou jinou.
- 9 sčítá jen správně oznámkované otázky, včetně sebe, pokud je správná.
- 12E neguje čtyři nabízené počty při zachování skutečně zvolené E.
- 18 počítá A a E na prvočíselných pozicích; 0 je čtverec a sudé číslo.
- Pravdivosti globálních vět 20A–E jsou parametry jednotlivých hypotéz.

`check_questionnaires.py` má konečný model v Z3 5.3.3 a zvláštní
doslovný Pythonový hodnotitel. Každý model se nezávisle oznámkuje;
po vyčerpání následuje UNSAT, ne jen ukončení po prvním svědkovi.
Model nepřekládá předčasné řezy původního CWEB programu.

## Úloha 71

Při předpokladu určitého maxima a 20E nepravdivé jsou přesně tři
maximální seznamy se skóre 19. Jsou shodné s (i), (ii), (iii) v knize.
Skóre 20 neexistuje. Varianta s jedinou chybou na pozicích 1–18 nemá
řešení; na 19 je jedno, na 20 dvě.

Globální předpoklady se následně ověří. Pokud by 20E byla pravdivá,
seznam (iii) by měl všech 20 odpovědí správně, včetně 20E, což by
vyvracelo obsah právě této věty. Proto je 20E nepravdivá. Maximum
nemůže být pod 19: seznam (ii), jehož poslední odpověď C je nepravdivá
pro každé maximum pod 20, stále dává 19. Úplný test vylučuje 20.
Seznam (i) dosahuje 19 se správnou 20B, takže vyvrací 20E také přímo.
To uzavírá konzistenci maxima 19 za zde užitou určitou interpretaci 20D.

Propagace při 3C vyžaduje právě shodu pozic 17,18 a nerovnosti všech
ostatních sousedů. V ukázce domén CD,AC,BD,ABE,BCD vede 8B k 7D,
6A a vyřazení 9B. Jde o přímé kroky binární nerovnosti, žádná možnost
se neztrácí. Výpočet originálního programu reprodukuje i metriky:

| Vyžadované chyby | Řešení | Uzly | Memy |
|---|---:|---:|---:|
| žádná | 0 | 52 859 | 3 355 989 |
| jen 15 | 0 | 56 | 4 902 |
| jen 19 | 1 | 184 770 | 10 799 667 |
| jen 20 | 2 | 130 721 | 7 608 471 |

To přesně odpovídá knižním přesným i zaokrouhleným údajům.

## Úloha 72 a význam paradoxu

Obě požadované změny (9E a 15C) byly uplatněny v samostatném modelu
i v autorově `.ch`. Při nepravdivých 20D a 20E zůstává pro skóre
alespoň 19 jen (iii). Proto by všechny maximální seznamy měly 20
špatně, a 20E by musela být pravdivá. Tím by však (iii) získal skóre
20 a 20E by byl opět vyvrácen. Určité maximum alespoň 19 tedy nefunguje.

Pokud je maximum nižší, (iii) nutí 20E pravdivou. Dva seznamy s 20C
nepravdivou dávají 18, a tak by maximum muselo být právě 18. Jenže
existuje přesně 48 seznamů se skóre 18 a 20A pravdivou, což vyvrací
20E. Obě sady i vytištěný svědek jsou úplně ověřené. Kdyby 20D byla
pravdivá, přibude právě zobrazený seznam se skóre 19. S (iii) tak
vzniknou dvě možnosti a opět zdánlivě určité maximum 19.

Tato poslední diskuse je zamýšlený sémantický paradox slova
„indeterminate“. Není to důkaz existence konzistentního globálního F
pro všechny současně vynucené významy. Výpočet poctivě uvádí
podmíněné pravdivosti 20D/20E; nepovažuje jejich volnou volbu za
řešení samoodkazu.

Malý dvouotázkový rekurzivní příklad byl vyčerpán přes všechny čtyři
hypotézy jeho dvou globálních vět. Jediný pevný bod má obě pravdivé:
AA a AB nelze oznámkovat, BA a BB mají známky 01, maximum 1.
U jednootázkového příkladu jsou oba pevné body b=0 a b=1 možné;
F(A,1)=b, F(A,0)=¬b, maxima tedy 0 nebo 1. Kniha to popisuje správně.

Celkem je uložených 63 originálních běhů s nejvýše jednou chybou
a všech 190 vzorů dvou chyb modifikované verze. Z3 a originál mají
stejná řešení u všech knižních případů, včetně 48 posledních A
a dvou posledních chybných C. Všech sedm vytištěných seznamů je
porovnáno znak po znaku a přímo oznámkováno.

## Prameny a známé erratum

Staženy a zahashovány aktuální originály z
[Knuthova seznamu programů](https://www-cs-faculty.stanford.edu/~knuth/programs.html):
`back-20q.w` a obě změny `backmod9,15` a `backmod9,15-indet`.
Komentář původce popisuje Woodsův návrh z roku 2000, úpravu 2001
a další společné úpravy 2015. Přímá Woodsova odpověď na
[MathPuzzle](https://www.mathpuzzle.com/twentyqs.htm) obsahuje také
závěrečný výrok citovaný v knize. Text účastníků diskuse výše má
jiné výklady otázky 7 a paradoxního známkování; nepoužíváme je místo
explicitní knižní formalizace.

Známá změna z 24. října 2020 opravuje Table 666, 9D z [61..67]
na [59..67]. Naše kniha i aktuální program už mají správně [59..67].
Ve zdroji err4b.textxt jsou ještě drobné redakční poznámky k
interpunkci p.412 a úvodu p.413; numerické výsledky nemění.
Zobrazené stránky jsou `images/vol4b-questionnaire-p61.png`,
`vol4b-estimation-431.png`, `vol4b-questionnaire-432.png`
a `vol4b-questionnaire-433.png`.

## F097: samostatná chyba v oficiálním programu BACK-20Q

Aktuální soubor `back-20q.w`, zpracování otázky 18, obsahuje dva
po sobě jdoucí řádky:

```
 if (!u && j) goto okay;@+goto bad;
 if (u && !j) goto okay;@+goto bad;
```

První `goto bad` je bezpodmínečný. Když má být otázka 18 chybná
(u=1), program se nikdy nedostane ke správnému druhému testu.
Vynechá proto všechny takové seznamy, ačkoli existují.

Příkaz `back-20q 18 20` má mít právě jeden výsledek:

```
A E B C D B C B C A B E C A C D D b E c
```

Malá písmena jsou právě dvě chyby. Na prvočíselných pozicích jsou
samohlásky jen 2E a 19E; jejich počet 2 není čtverec, takže 18B
je nepravdivá. Otázka 20C tvrdí maximum 20 a je také nepravdivá
(skutečné maximum původní tabulky je 19). Všechny ostatní věty
jsou pravdivé; například součet v 9C je přesně 48.

Původní program vrací 0 řešení (626 229 memů, 15 857 uzlů).
Po odstranění prvního `goto bad` vrací právě uvedené jedno řešení
(9 730 196 memů, 159 915 uzlů). Nezávislý model a doslovné známkování
potvrzují jeho úplnost i platnost. Oprava je v `back-20q-fix18.ch`.
Reprodukce: `check_back20q_bug.py` v auditním prostředí se Z3.

To je nález ve veřejném zdrojovém programu, **nikoli nová chyba
tištěného výsledku úloh 71–72**. Nemá potvrzení obrázkem PDF/PS;
dokladem je původní stažený zdroj se SHA a uvedené běhy. Zdroj byl
stažen přímo 1. listopadu 2026 a tehdy chybu stále obsahoval.
Nic nebylo odesláno a prvenství netvrdíme.

Při čtení je podezřelé také společné zpracování pravdivého a
nepravdivého 15C v základním programu. Při jeho povoleném rozsahu
nejvýše dvou chyb ale nezávislý model nenašel žádný platný seznam
s nepravdivým 15C. Tento lokální rozdíl tedy nepočítáme jako další nález.

## Reprodukce

`run_questionnaires.py` sestaví nezměněné originály a spustí 63 případů.
Samostatný spouštěč jen zahodí neurčenou návratovou hodnotu starého
`main`; ukončení a počet řešení se kontrolují z kompletního výstupu.
`run_questionnaire_pairs.py` projde 190 dalších případů.
`check_questionnaires.py` řeší nezávislé modely.
`check_questionnaire_results.py` porovná výsledky a knižní svědky.
Podrobnosti, verze řešiče, příkazy a časy jsou v `results/questionnaires/`.
