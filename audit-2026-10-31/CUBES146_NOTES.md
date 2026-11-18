# DLX 146 — třicet barevných kostek

Kontrola 3. listopadu 2026. Zadání 4B str. 142–143 (PDF 162–163),
odpověď str. 455–456 (PDF 475–476); autorův draft 2019 str. 78–79,
159–160. Lokální kniha je první vydání, druhý dotisk 2022; neověřujeme
fyzický výtisk ani úplnou nejnovější digitální verzi.

Matematická část prošla. Celá položka zůstává **partial** kvůli dvěma
konkrétním historickým mezerám a kandidátu C034. Nejde o otevřenou
matematickou nesrovnalost. Drahý počet 163 088 368 je samostatně evidované
vynechání podle pokynu uživatele, nikoli ověřený výsledek.

## Obecné argumenty

Stěny zapisujeme v pořadí U,D,F,B,L,R. Každá kostka má všech šest barev.
24 vlastních rotací působí volně na 720 permutacích: vzniká přesně
30 fyzických typů. Zvolíme horní barvu a; spodní má pět možností.
Nejmenší ze čtyř zbývajících barev dáme dopředu, čímž odstraníme rotaci
kolem svislé osy. Zadní barva má tři možnosti a zbylé dvě pořadí vlevo/vpravo.
Tím získáme právě knižní jména; zrcadlové typy zůstávají různé.

V řadě šesti kostek má každá barva šest výskytů. Čtyři jsou na čtyřech
viditelných dlouhých stranách, tedy zbývají dva skryté. Každý vnitřní
kontakt spotřebuje dva stejné výskyty. Pět kontaktů proto používá pět
různých barev a šestá musí být na obou koncích. To dokazuje (a) i oprávnění
použít šest cyklických h-položek v Algorithm C.

Model má 6 primárních pozic, 24 primárních položek stranových barev,
30 sekundárních fyzických typů a šest obarvených sekundárních kontaktů.
Každá možnost je konkrétní orientace jednoho typu v jedné pozici: 4320
možností. Všechny podmínky řady odpovídají přesně těmto položkám a naopak.
Vytištěná možnost pro první kostku je správná. Globální přejmenování barev
má 720 prvků a na první orientaci působí volně, proto fixování první kostky
na abcdef dělí počet právě 720. Není to další geometrická normalizace.

16 prostorových rotací/odrazů zachovávajících osu řady a šest cyklických
posunů dávají 96 operací. Po každé operaci znovu přejmenujeme barvy podle
první kostky. Odrazy jsou povolené, protože máme všech 30 typů. Výčet
ověřuje uzavřenost této akce na celé množině řešení a orbit–stabilizer.

## Krátké výpočty a obrázky

`extract_cubes146.py` přečetl všech **216 označení stěn** z vektorů původního
PDF i draftu: 30 typů a šest kostek v řadě. Obě verze jsou stejné, typy jsou
různé, všechny kontakty i viditelné strany sedí. Šest vytištěných jmen
odpovídá skutečným orientacím.

Přímý levopravý CSP v C++ dokončil **2176** normalizovaných řad po 11 844
uzlech (0,054 s). Původní DLX2 s jiným větvením dokončil stejný počet
po 10 565 uzlech (0,373 s; 44 733 697 čistých memů). Porovnány **celé
množiny**, každý model přímo validován. Oba běhy měly limit 60 s a nízkou
prioritu. Dokončené běhy se neopakují.

Akce 96 operací má **33 orbit**. Počty orbit se stabilizátory
1,2,4,6,12 jsou přesně **17,9,3,1,3**. Kontrola součtu:
17·96 + 9·48 + 3·24 + 1·16 + 3·8 = 2176. Vytištěná řada má
12 automorfismů. Celkem pojmenovaných řad je 720·2176 = **1 566 720**.

Normalizované řady dávají 1892 různých šestiprvkových množin typů.
Po všech globálních přejmenováních barev je jejich úplné sjednocení
**15 500**. Tím se potvrzuje vstup pro závěrečný exact cover.

Existenci v (d) dokládá následující rozdělení. Každý řádek uvádí šest
orientací U,D,F,B,L,R; všech 30 fyzických typů je použito právě jednou:

```text
abcdef ecabfd febadc bdfeca dfecab cadfbe
abcfed beacdf dabefc efdbca fcedab cdfabe
acbfde dbfaec fdaecb caedbf bedcfa efcbad
adbefc fedacb eafcbd cbafde dfcbea bcedaf
adbfce bfdcea dbceaf ceadfb fceabd eafbdc
```

Hledání prvního svědka navštívilo devět uzlů. Každá řada byla ověřena
včetně koncových stěn. **Počet 163 088 368 všech rozdělení se nepočítal**:
uživatel výslovně dovolil vynechat dlouhé úplné reprodukce. Existence,
15 500 vstupních množin a správnost exact-cover modelu jsou doložené;
z toho ale neplyne ověření tohoto velkého počtu.

## Errata a historie

Šest vrstev errat se shoduje hashem s oficiálním stažením 3. 11. 2026
v 05:37 UTC. **E073** je známá oprava z 13. 3. 2026: ročník Scientific
American **235 → 239**. V našem PDF i draftu ještě zůstává 235.
[Vydavatel článku ze září 1978](https://www.scientificamerican.com/article/mathematical-games-1978-09/)
potvrzuje 239(3). Článek začíná na str. 20; knižní odkaz na str. 26
je legitimní odkaz na konkrétní odstavec, nikoli chyba v počáteční stránce.

[Původní číslo ze září 1978](https://www.wkbpic.com/wkbx/SA/1978/1978-09-01.pdf),
str. 26 (PDF 28), skutečně pokládá otázku rozdělení všech třiceti kostek
do pěti řad. To odpovídá knižní **(d)**, zatímco historická poznámka uvádí
**(c)**, která se ptá na počet řad až na symetrie. **C034** je kandidát
na opravu odkazu; samostatná poznámka obsahuje přesný rozsah a limit závěru.
Úplný text pokračování str. 30 rovněž uchován, bez dodatečného potvrzení
otázky na počet tříd řad. Není to nový potvrzený matematický nález.

[Gardnerova kniha z roku 1992](https://bobson.ludost.net/copycrime/mgardner/gardner14.pdf),
str. 96–97 (PDF 103–104), přisuzuje řešení Perjésovi a zobrazuje pět řad.
Originál str. 97 byl vizuálně prohlédnut; rok 1992 potvrzuje tiráž.
Tato stránka sama nedokládá rok 1981. Institucionální
[katalog MTA](https://real-eod.mtak.hu/view/year/1981.html) uvádí report
*Tori of colored cubes*, KFKI-1981-57. Tělo reportu se nepodařilo získat:
oficiální HTTPS i alternativní HTTP ukončily spojení. Nepředstíráme jeho četbu.

Zbývají přesně tyto historické mezery: původní znění problému na str.
168–174 v březnu 1961 a úplné doložení datace Perjésova řešení do roku 1981
včetně tvrzení o pěti symetrických řadách. Vydavatel potvrzuje metadata
[článku z března 1961](https://www.scientificamerican.com/article/mathematical-games-1961-03/),
nikoli dostupnost jeho celého textu. Neúspěšné přístupy jsou zaznamenané.
Tyto mezery nejsou omluveny výjimkou pro dlouhé výpočty.

Výsledky: `results/cubes146/accepted.json`; úplné modely, akce symetrií,
15 500 množin, svědek a metadata původních běhů jsou v `bounded/`.


## Druhý průchod,17. listopadu2026

C034 je nyní confirmed jako chybný odkaz(c)→(d); viz [aktuální argument](notes/C034-colored-cubes-cross-reference.md). Toto úzké zjištění nepotřebuje úplnou historii z roku1961. Originál Perjésova reportu1981 byl získán; jeho §5 na str.5 výslovně definuje rozdělení všech30 kostek do5 řad a uvádí konstrukce. Jeho celá klasifikace ani podrobnosti pěti symetrických řad se nově necertifikují. Staré výpočty nebyly zopakovány.
