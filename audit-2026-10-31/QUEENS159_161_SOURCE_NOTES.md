# DLX159–161: zdrojové obrázky, symetrie a obecná kódování

Kontrola 3. listopadu 2026. Zadání str. 144, odpovědi str. 461,
hlavní text a obrázek (65) str. 94. V autorově draftu jde o strany
80, 165 a 30. Původní stránky byly zobrazeny. Starý úplný výčet
4 860 rozmístění a výpočty všech variant zůstávají přijaté;
žádný z těchto výčtů se neopakoval.

## Přímé čtení obrázku (65)

Z vektorových zdrojů obou verzí odečteno všech 72 čar mřížek a
20 symbolů dam. Souřadnice všech čtyř desek přesně souhlasí s dřívějším
ručním přepisem. Všechny desky dominují, třetí splňuje variantu (ii)
a čtvrtá variantu (i), jak uvádí zadání161. Počítáno od nuly shora zleva:

| Obrázek zleva | Buňky dam | Velikost komponenty z přijatého grafu |
|---|---|---:|
| 1 | (1,3), (2,4), (3,1), (5,0), (6,7) | 3804 |
| 2 | (0,3), (2,2), (3,5), (5,2), (6,5) | 3804 |
| 3 | (2,2), (2,3), (2,4), (3,5), (4,3) | 3804 |
| 4 | (0,2), (2,7), (3,3), (5,0), (7,5) | **20** |

MCC(64) používá uzavřené okolí každého vrcholu: vybraná dáma pokrývá
i své vlastní pole. Každá buňka má násobnost [1,m], znak # přesně m.
Proto je výběr možností v bijekci s m-prvkovými dominujícími množinami.
Nově doplněna i přímá kontrola obou počátečních větvení22: pole00 a,
po volbě dámy00, pole17. Starých deset omezených počtů ze strany94
zůstává přijato bez opakování. Odstavec o slovních obdélnících níže
na stránce do této kontroly nepatří.

## 159: deset kvadrantových případů je úplných

Každé rozmístění pěti dam určuje čtveřici nezáporných násobností se
součtem5. Je jich C(8,3)=56. Osm symetrií čtverce permutuje kvadranty;
starý ověřený rozklad těchto56 čtveřic má přesně deset disjunktních orbit.
Vytištěné čtveřice jsou reprezentanty všech deseti, s vahami
4,4,8,4,8,8,4,8,4,4. Záměna # za #_(2 floor(i/4)+floor(j/4)) tedy
vynutí danou čtveřici. Při nulové násobnosti se možnosti daného
kvadrantu vynechají. Symetrie bijektivně převádí řešení mezi členy
orbity, proto váhy platí i tehdy, když samotná rozmístění mají stabilizátory.

Přijaté počty134,884,33,23,34,1,16,0,22,0 dávají vážený součet4860.
Nevynásobujeme každé řešení automaticky osmi. Tím by se zaměnila
symetrie násobností se symetrií jednotlivých rozmístění.

Návrh devíti oblastí pro větší n je platný: diagonály a u lichého n
prostřední řádek a sloupec tvoří invariantní zvláštní oblast; zbylé
buňky tvoří osm otevřených oktantů, které D4 permutuje. Opět lze
vybrat reprezentanty orbit jejich násobností. Text netvrdí konkrétní
rychlost nebo odstranění všech symetrií uvnitř každé oblasti.

Historické náklady95,348,60,23,75,8,19,2,10,0 Mμ ani původních13 Gμ
znovu neměřím. Pouze aritmetika těchto uvedených údajů souhlasí:
součet640 Mμ a podíl13000/640=20,3125 odpovídají zaokrouhlenému
zrychlení20. Výslovně evidováno jako nereplikovaný benchmark,
nikoli jako nově změřený výsledek.

## 160: F067 má krátký samostatný validátor

Starý úplný histogram má589 komponent,388 izolovaných vrcholů,
obra3804 a dalších200 komponent velikostí2,3,4,5,18,20. Součet
velikostí je4860. První tři obrázky jsou v obrovi, čtvrtý v komponentě20.
Dva chybné údaje12 a8 zůstávají čitelné v PDF i autorském draftu.

Pro vlastní kontrolu stačí:

```bash
cd audit-2026-10-31
python3 verify_f067.py
```

Používá pouze standardní Python a uložených20 poloh. Zkontroluje jejich
dominanci, souvislost a všech5900 přemístění jedné dámy z těchto poloh.
Žádné platné přemístění z množiny nevychází: jde tedy o celou komponentu
s20 vrcholy a26 hranami. Běh trval0,188 s při nice15. Nepotřebuje seznam
všech4860 řešení ani jejich hledání. Přímé dekódování obrázku zároveň
potvrzuje, že počáteční poloha validátoru je skutečně čtvrtý obrázek (65).

Přemístění znamená libovolné nahrazení jedné buňky dam jinou volnou
buňkou, jak bylo doloženo dříve shodou ostatních počtů knihy. Přísnější
grafy legálních šachových tahů mají jiné počty a nejsou s tímto smíchány.
Nález **F067 není nový**; jeho původní text a status se nemění.

## 161: všechny tři formulace platí pro obecný jednoduchý graf

V základní formulaci označme otevřené okolí vrcholu v jako N(v).
Jeho možnost je # spolu s {v} sjednoceno N(v); všechny vrcholové
položky mají násobnost[1,m]. Pro každou variantu platí oba směry:

- **(i)** Sekundární neobarvená položka hrany se objeví v možnostech
  obou konců. Povolí nejvýše jeden z nich, a tím přesně nezávislost.
  Nezávislá dominující množina je maximální nezávislá množina:
  nedominovaný vrchol by šel přidat; naopak k dominující množině
  nelze žádný vrchol nezávisle přidat.
- **(ii)** Vynechání samotného v nechá možnost # spolu s N(v).
  Každý vrchol včetně vybraných musí být pokryt jiným vybraným
  sousedem. To je přesně totální dominance.
- **(iii)** Vybrané v používá sekundární v-hat s barvou1 a sekundární
  položky všech nesousedů s barvou0. Dva vybraní nesousedé by měli
  u položky každého z nich obě barvy, což je zakázané. Pro kliku žádný
  konflikt nenastane: položka vybraného vrcholu má jen1, nevybraného
  jen0 nebo se nepoužije. Primární položky nadále vynucují dominanci.

Úplné dřívější počty728,352,20 pro velikost5 souhlasí. Také počty
jader velikostí6,7,8 jsou6912,2456,92. Činitel8 v728=8×91 lze odůvodnit
bez nového výčtu: množinu pěti nezávislých dam na sudé desce nefixuje
žádná netriviální symetrie. Rotace by vyžadovala orbitu liché délky,
která zde neexistuje. Zrcadlový pár dam se navzájem napadá; kdyby
všechny ležely na ose, také by se napadaly. Každá orbita má proto8 členů.

Odkaz7.1.4–241(a) byl přímo ověřen ve svazku4A: zadání277,
odpověď672, fyzické stránkyDjVu294 a689. OCR dělení má na tomto místě
o dvě stránky menší index, proto byla lokace ověřena obrazem. Polynomiální
koeficienty souhlasí. Starší oprava názvu „8 queens“ a doplnění odkazu
na(C6),(C7) v části(d) čísla nemění. Historické atribuce a ostatní části
svazku4A zde nejsou předmětem nového auditu.

## Stav a evidence

Všech šest vrstev errat4B/Fascicle5 zkontrolováno podle původních i
posunutých stran, čísel úloh a tématu. Oprava159–161 aniF067 nenalezena;
to nedokládá prvenství. Tištěný exemplář nadále neověřen.

Celé úlohy159,160,161 jsou **reviewed**, druhá s dřívějšímF067.
Celá odpovědní strana461 je tím zrevidovaná;144 zůstává částečná
kvůli předchozím úlohám,94 kvůli dalšímu textu. Nevznikl nový nález,
emailový návrh ani velký výčet. Další úloha:162.

- [Přímé dekódování a přijaté staré výsledky](results/queens159_161/source-checked.json)
- [Krátký validátor F067](verify_f067.py) a [jeho výsledek](results/queens159_161/f067-direct-checked.json)
- [Starší úplné důkazy](QUEEN_DOMINATION_NOTES.md)
- [Errata](results/queens159_161/errata-check.json)
- [Přesný odkaz do4A](sources/queens159_161/reference-check.json)
- [Priority vlastních procesů](results/queens159_161/process-priorities.json)
