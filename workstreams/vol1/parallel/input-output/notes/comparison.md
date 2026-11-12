# Odpověď 1.4.4-12 přepisuje porovnávací indikátor

Stav: potvrzeno v kontrolovaném prvním dotisku a všech čtyřech
prohledaných vrstvách errat; kořenová revize a globální ID čekají.
Vlastní označení je `CONTROL-input-end-clobbers-CI`.

CI označuje porovnávací indikátor MIX se stavy less, equal a greater.
Původní Program B na 223 provádí jen JMP, J6Z, IN, LD5 a DEC6;
vazba přidává STJ a JMP. Žádný z těchto příkazů CI nemění. Text
doporučuje sporadicky vkládat JRED CONTROL(U) do COMPUTE. Původní
varianta tím zachovává rozpracované porovnání stejně jako rA.

Odpověď na 533 přidává porovnání posledního znaku karty s tečkou.
rA před ním uloží a po něm obnoví, ale CI zůstane změněn. Pro
koncovou kartu je equal, bez ohledu na předchozí stav COMPUTE.
Při nekoncové kartě obsahuje výsledek srovnání jejího posledního
znaku s tečkou, opět bez vazby na porovnání COMPUTE.

Konkrétní reprodukce používá dvě skutečné karty a dva buffery.
První karta je prázdná, druhá má tečku ve sloupci 80. COMPUTE
provede ASSIGN první karty; tím je prvé čtení dokončeno a druhé
zahájeno. JBUS zajistí dokončení druhého přenosu. Následuje

```
ENTA 0
CMPA =1=
JRED CONTROL(16)
JL SUCCESS
```

Před JRED je CI=less. Původní Program B vrátí less a JL skočí.
Úprava z odpovědi 12 vrátí equal a JL neskočí. Není nutné žádné
neurčené počáteční CI, přístup do aktivního bufferu nebo čtení za
koncem vstupu. Obě vstupní karty jsou zpracovány a n=0.

V `programs.py` vytváří `comparison_example()` úplnou reprodukci.
`ring_routines(termination='printed')` je přesný kód odpovědi 12;
varianta `none` má původní Program B. Varianta `preserve_ci` nejprve
uloží rA a pomocí JL/JG zakóduje staré CI jako -1,0,1. Po kontrole
tečky vybere konečnou větev a před obnovením COMPUTE či řádným
pokračováním řídicí smyčky provede LDA CISAVE; CMPA =0=; LDA ASAVE.
Tím obnoví CI i rA. Jde o lokální návrh opravy, sdílené modely ani
kniha nebyly měněny.

`check_comparison.py` provedl 54 běhů a 162 kontrol: báze 64 a 100,
latence 0,17,10000u nad základní cyklus I/O, všechny tři počáteční
stavy CI a všechny tři varianty programu. Tištěná úprava volí chybnou
větev v každém případě, kdy je původní CI less nebo greater (12 běhů).
Obě kontrolní varianty volí vždy správnou větev. rA se zachovává i
v chybné tištěné úpravě. Výsledky jsou v `../results/comparison.json`.

Původní stránky jsou `../images/p222.png`, `p223.png`, `p227.png`
a `p533.png`. Text a známé opravy byly prohledány podle stran i
výrazů pro CONTROL, JRED, tečku a porovnávací indikátor, včetně
OCR variant bez písmene c. Žádná nalezená oprava neřeší odpověď 12.
Známá změna odpovědi 14 na téže straně se týká počtu volných bufferů.
Návrh anglického ASCII hlášení je
`../reports/CONTROL-input-end-clobbers-CI.txt`.
