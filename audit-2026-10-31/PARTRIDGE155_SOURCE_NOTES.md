# DLX155: původní obrázky, skóre a rozsah ověření

Kontrola 3. listopadu 2026. Zadání 7.2.2.1–155 je na str. 144,
odpověď na str. 460 a odkazované obrázky (62) na str. 92.
Původní PDF má odpovídající souborové strany 164, 480 a 112;
autorský draft strany 86, 170 a 34. Všechny byly vizuálně přečteny.

## Matematika a přímá kontrola tisku

Starší úplný výčet 60 568 řešení autentického inventáře řádu 6 se
neopakoval. Jeho samostatný geometrický validátor zkontroloval všechny
modely a původní porovnání s DLX3 pokrývá 34 malých inventářů.
Úplnost generátoru plyne z první volné buňky: pokrývající čtverec
musí mít právě tam levý horní roh, jinak překryje dřívější obsazenou
buňku. Každá přípustná zbývající velikost se zkouší právě jednou.

Nový `extract_partridge155.py` čte přímo vektorové obdélníky a číselné
popisky obou verzí. Kontroluje souřadnice, nepřekrývání, úplné pokrytí,
násobnosti a všech 114 popisků v každé verzi. Výsledky jsou totožné:

| Obrázek | Inventář | Velikost desky | Afinita |
|---|---|---|---:|
| (62), levý | k čtverců k×k, k=1,…,8 | 36×36 | 165 |
| (62), pravý | k čtverců k×k, k=1,…,8 | 36×36 | 67 |
| odpověď 155, levý | 7−k čtverců k×k, k=1,…,6 | 14×14 | 35 |
| odpověď 155, pravý | 7−k čtverců k×k, k=1,…,6 | 14×14 | 5 |

Skóre je počítáno dvěma způsoby: po jednotkových hranách mřížky a
součtem délek společných hran dvojic stejně velkých obdélníků.
Obě metody souhlasí. Oba vytištěné extrémní svědky lze najít beze změny
souřadnic ve starém archivu všech řešení, na řádcích 7 329 a 47 283.
Starý úplný histogram dává minimum 5 a maximum 35, tedy i optimalitu.
Nevzniklo žádné nové hledání ani nový počet řešení.

Rovnost 8·7 571 = 60 568 je správná. Počet tříd D4 je 7 585,
protože 7 557 tříd má osm obrazů a 28 tříd pouze čtyři:
7 557·8 + 28·4 = 60 568. Kniha netvrdí, že 7 571 je počet tříd.

## Prameny, errata a záměrné vynechání

Šest archivovaných vrstev errat bylo prohledáno podle čísel úloh,
stran, jmen a obsahu. Oprava k 155 nenalezena. Sousední oprava URL
u 154 je E078; změna autorství u 156 bude posouzena zvlášť.

Cílené hledání výrazu Robert Reid spolu s afinitou, minimem a rokem
2000 našlo zejména kopie Knuthova textu. Ty nejsou nezávislým
potvrzením historické poznámky. Wainwrightova kapitola 277–281 uvádí
Reidovo řešení jiného řádu; přehledy jiné Reidovy výsledky. Žádný
z těchto údajů nedokládá ruční minimum 5 v roce 2000. Původní
zprávu ani datovaný záznam o navržení této úlohy nemáme.

Historických **60 Gμ** pro Algorithm M výslovně nereplikuji podle
pokynu uživatele. Tato hodnota není nezávisle ověřena. Vynechání se
netýká úplného počtu 60 568, který již ověřený je. Čas nebo počet
uzlů odlišného programu není reprodukcí dobových mems.

**Výsledek:** matematický blok X155 zůstává checked s rozšířeným
rozsahem; celá DLX155 je partial pouze kvůli původnímu historickému
údaji. Žádný nový F/C/E záznam. Pokračování: 156, bez opakování
hotových partridge výčtů.

## Evidence

- [Přímá kontrola obrázků](results/partridge155/figures-checked.json)
- [Původní matematika 154–158](PARTRIDGE_NOTES.md)
- [Původní strana 92](images/partridge155-original92.png)
- [Draft, strana 28](images/partridge155-draft28.png)
- [Odpověď, strana 460](images/paths152-answer460.png)
- [Historické hledání](sources/partridge155/history-search.json)
- [Kontrola errat](results/partridge155/errata-check.json)
