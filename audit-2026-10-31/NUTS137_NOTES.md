# DLX137 — Drive Ya Nuts

Kontrola 2. listopadu 2026. Zadání: tištěná strana 140 / PDF 160;
odpověď: strana 452 / PDF 472. Finální matematické výsledky dosavadní
kontroly jsou v [accepted.json](results/nuts137/accepted.json).
Celá úloha zůstává `partial`: historické mezery a přesná konvence
patnáctiuzlového ručního stromu jsou vypsané níže.

## Přesný model a všechny tři původní obrázky

Rozlišujeme 120 cyklických typů. Zápis začíná číslicí 1 a pokračuje proti
směru hodinových ručiček. Povolené jsou rotace; zrcadlení mění typ.
Globální otočení celé sestavy odstraníme podmínkou, že jednička střední
matice míří nahoru. Proto má každé geometrické řešení právě jeden zápis.

Sedm pozic a sedm různých matic dává 14 primárních položek, dvanáct
kontaktů dává 12 barevných sekundárních položek. Pro střed stačí sedm
orientací typu, na obvodu je 6 × 7 × 6 možností: dohromady 259.
U součtu 7 se na jednom konci každého kontaktu používá doplňková barva
7 − d. Shoda barev v XCC pak přesně vyjadřuje součet 7.

Původní typy:

```
123456 125634 135246 135426 142356 153264 165432
```

Typy v odpovědi (d):

```
125463 135642 142563 145326 146325 146352 164235
```

| Sada | Pravidlo | Úplný počet řešení |
|---|---|---:|
| Zadání, část (a) | Rovnost | 1 |
| Zadání, část (b) | Součet 7 | 0 |
| Odpověď (d) | Rovnost | 1 |
| Odpověď (d) | Součet 7 | 1 |

Ve všech čtyřech případech se shodují celé množiny výsledků původního
DLX2 a nezávislého výčtu permutací obvodových matic. Ten po volbě středu
využívá jednoznačně určenou orientaci každé vnější matice; nepoužívá
XCC ani jeho tabulku hran.

Z PDF je přečteno všech **126 číslic**: 42 v zadání a 84 v odpovědi.
Každá skupina šesti číslic byla přiřazena také k samostatnému černému
obrysu matice. Kontakty byly určeny z geometrie obrázků, nezávisle na
číslování pozic modelu. Všechny tři vytištěné sestavy jsou platná řešení;
dvě sestavy v (d) mají stejných sedm typů.

## Ruční důkaz

Pro pevný střed lze pro každou z šesti pozic sestavit tabulku šesti
kandidátů. Poloha čísla směřujícího dovnitř určí otočení celé matice.
V každém poli tabulky stačí ponechat dvě čísla mířící k sousedům.

Používáme pouze dvě pravidla: odstranit kandidáta bez možného souseda
na jedné ze dvou stran; a odstranit matici z ostatních pozic, pokud je
někde jedinou možností. Takto šest středů skončí prázdnou doménou a
střed `135426` má šest jednotlivě vynucených sousedů.

| Střed | Počet doložených odstranění | Výsledek |
|---|---:|---|
| 123456 | 31 | Spor |
| 125634 | 13 | Spor |
| 135246 | 25 | Spor |
| 135426 | 30 | Jediné řešení |
| 142356 | 11 | Spor |
| 153264 | 30 | Spor |
| 165432 | 6 | Spor |

[Certifikát](results/nuts137/hand-certificate-checked.json) uchovává každý
krok; druhá kontrola přehrává jeho důvod přímo na geometrických hranách
otočených matic. Jde o sedm případů pro střed, bez dalšího větvení.
Při počítání kořene a šesti vynucených vložení má tento postup 14 uzlů;
počítání jednotlivých inferencí by dalo jiné číslo. Knižní konkrétní
strom velikosti 15 jsme tím nereprodukovali. Je doložena proveditelnost
krátkého ručního rozboru.

## Pravděpodobnosti a kandidát C032

Předem zvolený pokus má 1 000 000 nezávisle generovaných sedmic,
seed `20261102137`, generátor MT19937-64. Výběr různých typů používá
odmítání opakovaných hodnot a odmítání přebytku při převodu na rozsah
0–119. Za předpokladu rovnoměrných nezávislých bitů tedy každá ze
**59 487 568 920** sedmic má stejnou pravděpodobnost výběru.

| Počet řešení při rovnosti | Počet ve vzorku | Odhad podílu | Kniha |
|---|---:|---:|---:|
| 0 | 932 090 | 93,2090 % | asi 93 % |
| 1 | 53 421 | 5,3421 % | asi 5 % |
| 2 | 11 057 | 1,1057 % | asi 1 % |
| alespoň 3 | 3 432 | **0,3432 %** | zbývající 1 % |

Jednoznačných pro obě pravidla bylo 4 242 sad, tedy **0,4242 %**;
to souhlasí s knižním přibližným 0,4 %.

Všech milion devítibajtových záznamů je archivováno a agregace byla
znovu ověřena. Nový C++ čítač nejprve prošel 131 zkušebními sadami.
Z velkého vzorku bylo následně vybráno 227 sad: prvních 128 a zástupci
všech 16 kombinací tříd počtů pro obě pravidla. **454 úplných výčtů**
DLX2 se shoduje s celými množinami výsledků nezávislého Pythonu;
necenzurované počty C++ souhlasí také. Výběr obsahuje všech pět vzorků,
které mají alespoň tři řešení při obou pravidlech.

Pro poslední řádek vychází individuální 95% Wilsonův interval přibližně
0,3319–0,3549 %. Tento interval předpokládá nezávislé rovnoměrné vzorky;
není důkazem nezávislosti pseudonáhodného generátoru ani přesným
výčtem celé populace.

**C032 je kandidát na zpřesnění údaje.** Kniha už první
tři podíly hrubě zaokrouhluje a čtvrtý doplňuje do 100 %. Proto zatím
není označen jako potvrzená matematická chyba. Znění má také autorův
draft z 11. září 2019, strana 156. V příslušných erratech oprava není.

## Úplný přesný výpočet části (c)

Doplňkový výpočet i jeho úplný nezávislý verifier úspěšně doběhly.
Počty sad podle počtu řešení jsou nyní přesné:

| Počet řešení | Počet sedmic | Podíl |
|---|---:|---:|
| 0 | 55 439 557 440 | 93,195198 % |
| 1 | 3 180 020 160 | 5,345689 % |
| 2 | 662 739 120 | 1,114080 % |
| alespoň 3 | **205 252 200** | **0,345034 %** |
| Celkem | 59 487 568 920 | 100 % |

Postup využívá všech 720 přejmenování čísel a prochází řešení s typem
`123456` ve středu. Pro orbitu sad se stabilizátorem h se její počet
takových řešení c přepočítá na q = ch/6 řešení každé sady; orbita má
720/h různých sad. Všechna přejmenování zachovávají pravidlo rovnosti.
Před spuštěním bylo všech 86 400 hodnot transformací i 34 kanonických
příkladů porovnáno s přímým Pythonovým výčtem všech 720 permutací.

Výčet dává **43 500 008** řešení s pevným středním typem a **5 623 238**
orbit neprázdných sad. Druhý algoritmus vybírá nejprve čísla na šesti
sdílených hranách vnějšího prstence, pak permutace zbývajících tří čísel
na každé matici. Jeho 1 144 přípustných konfigurací hran nezávisle dává
stejných 43 500 008 řešení.

Verifier následně pro **každou z 5 623 238 orbit** prověřil všech
720 přejmenování, kanonické minimum, stabilizátor a celý počet řešení
její reprezentativní sady druhým čítačem. Vážený součet je přesně
5 220 000 960, tedy 120násobek nezávisle spočteného počtu s pevným
středním typem. Další neprázdná orbita by tento součet zvětšila.
Zbytek celé populace proto tvoří právě sady bez řešení.

Nejvyšší možný počet je **20 řešení**, dosahuje ho 360 různých sad.
Jedna taková sada i příklady všech čtyř dosažených řádů stabilizátoru
1/2/3/6 byly navíc ověřeny původním DLX2; opět se shodují celé množiny
řešení s Pythonem. [Přijatý úplný cenzus](results/nuts137/census/accepted.json)
obsahuje i rozdělení pro každé dosažené q.

Výpočet uzavírá numerickou nejistotu části (c). **C032 zůstává kandidátem
kvůli interpretaci hrubého zaokrouhlení v knize**, nikoli kvůli neověřenému
počtu. Podíl jednoznačnosti současně při součtu 7 je nadále podložen
milionovým vzorkem; celý S6 součet 7 nezachovává, takže jsme na něj
váhy rovnostního cenzu nepřenesli.

## Prameny a otevřený rozsah

Ověřeny všechny šest vrstev errat 4B a Fascicle 5. Čtyři oficiální
zdrojové soubory byly znovu staženy 2. listopadu 2026 v 14:10 UTC a mají
shodné hashe. Šest nalezených kontextů patří úlohám 121 a 138;
žádný neopravuje 137. Historická oprava 96/6 = 12 → 16 patří až 138.

Z [archivu Hasbro](https://www.hasbro.com/common/instruct/DriveYaNuts.PDF)
máme přímo výrobní list s řešením, označený copyrightem 1987. Jeho
42 číslic bylo přepsáno z obrázku a shoduje se s jediným řešením (a).

[Původní americký patent](https://patents.google.com/patent/US1558165A/en)
potvrzuje G. H. Haswella, datum 20. října 1925, sestavy 7/19/37 hexagonů
a obě pravidla spojování. Strana 2 původního PDF byla vizuálně přečtena.
Abstrakty [GB149473](https://patents.google.com/patent/GB149473A/en)
a [GB173588](https://patents.google.com/patent/GB173588A/en) potvrzují
uvedená jména, data a devatenáct dílků; první používá součet 7, druhý
shodu. Úplné britské originály zatím nemáme a jméno Super Dom v získaných
abstraktech není.

[Zarecky a Parker](https://www.wittenberg.edu/sites/default/files/media/computer_science/forms/sumInSMC.pdf)
zpracovali stejný hlavolam polynomiálními rovnicemi.
[Rob Stegmann](https://robspuzzlepage.com/pattern.htm) zveřejnil vlastní
ruční tabulkovou metodu. U obou se sedm zapsaných typů přesně shoduje
s knihou po převodu směru zápisu. Tento audit nekontroluje všechny
výpočty těchto dalších autorů.

Zbývá nezávisle doložit přesné uvedení na trh v roce 1970, tvrzení
o zapomenutém vynálezci a jméno Super Dom. Neúspěšné pokusy o původní
britské dokumenty a záznam ochranné známky jsou uložené; nejsou
nahrazeny domnělým potvrzením z pouhého výsledku vyhledávání.

## Reprodukce

Bez opakování úplných hledání lze ověřit hashe, koncové stavy a vazby
již přijatých výsledků:

```bash
python3 accept_nuts137.py
```

Původní čtyři běhy a nezávislé modely:
[book-cases-checked.json](results/nuts137/book-cases-checked.json).
Výsledky simulace:
[statistics-checked.json](results/nuts137/sampling/statistics-checked.json).
Vstupy a výstupy všech 454 kontrolních běhů jsou v
`results/nuts137/sampling/native-calibration.tar.gz`; manifest uvádí
hashe každého členu. Zdrojové programy ani probíhající starší výpočty
se při této kontrole neměnily.
