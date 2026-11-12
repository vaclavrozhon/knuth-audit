# Ménage: úloha 7.2.2.1–14

## F105 — indexy v rozepsané konečné identitě

Na str. 418 je správně vytištěn kompaktní součet

    u_n/n! = sum_{j=0}^{floor(n/2)} (-1)^j T_(n-2j)/(j! (n-1)^under_j),
    T_m = sum_{k=0}^m (-2)^k/k!.

Hned za ním se ale rozepsané čitatele mění po jedničce: T_(n-1),
T_(n-2), T_(n-3). Musejí se měnit po dvojce: **T_(n-2), T_(n-4),
T_(n-6)**. Jde o chybu v explicitně vypsané rovnosti; kompaktní součet
vlevo už má správné indexy. Obecná oprava plyne přímo dosazením j=1,2,3.

Nejkratší kladný příklad je n=3. Existuje právě jedno přípustné usazení,
tedy u_3/3!=1/6. Přitom T_3=-1/3, T_2=1 a T_1=-1:

    správně:  T_3 - T_1/2 =  1/6;
    vytištěno: T_3 - T_2/2 = -5/6.

Pro n=4 dává správná rovnost 1/12, chybná 19/36. Na všech těchto malých
příkladech jde o přesné zlomky, nikoli numerické zaokrouhlení. Platnost
následujícího asymptotického rozvoje tímto protipříkladem nevyvracíme.

Vizuálně zkontrolována [PDF str. 418](images/vol4b-p418.png) i
[původní autorův PS, str. 122](images/fasc5c-menage-p122.png), datovaný
11. září 2019, PDF pořadí 128. Oba obsahují tytéž chybné tři indexy.
Fyzický výtisk zatím ověřen není.

Aktuální i úplná historická errata 4B a Fascicle 5 byla prohledána podle
stran 418/226, odpovědi 14, slov ménage/Touchard/Kaplansky/Wyman a tvaru
identity. Nalezené opravy na historické str. 226 se týkají jen odpovědi 12.
Odpovídající oprava identity nebyla nalezena; podklady a jejich SHA256 jsou
v [errata-check.json](results/menage/errata-check.json). To není důkaz
prvenství ani příslib odměny.

## Nezávislé početní kontroly a zbývající rozsah

[check_menage_identity.py](check_menage_identity.py) nezávisle usazuje
manžely do volných míst. Bitový dynamický program pro n=2..16 nezávisí
na uvedené rekurenci, inkluzi a exkluzi ani na algoritmu X. Úplný výčet
všech permutací pro n=2..9 dává stejné výsledky. Všech osm publikovaných
počtů n=3..10 souhlasí.

Přesná racionální kontrola n=2..80 porovnala Touchardův vzorec, uvedenou
rekurenci a opravenou konečnou identitu. Ověřila také 3318 jednotlivých
členů předcházejícího přepisu a prvních 51 koeficientů vytištěné obyčejné
vytvářející funkce. Výsledky jsou v
[finite-identity.json](results/menage/finite-identity.json).

Celá úloha 14 zatím zůstává `partial`: zbývá doplnit obecné důkazy dalších
identit a asymptotických tvrzení a původní historické citace. Memové údaje
180/275 na řešení byly následně ověřeny níže. Konečné numerické kontroly
nenahrazují obecný důkaz.
Nález F105 sám je již doložen nezávislým protipříkladem a oběma originály.

## Přibližné memové náklady 180/275

Z [oficiálního indexu programů](https://www-cs-faculty.stanford.edu/~knuth/programs.html)
byl získán veřejný [DLX1](https://www-cs-faculty.stanford.edu/~knuth/programs/dlx1.w).
Soubor je archivován beze změny, SHA256
`a5ca5db64c2efe759bdb134ff257a883283f29178b98d526a3f36f06b1ffb697`.
MRV běží v tomto neupraveném autorově programu. Varianta bez MRV používá
náš explicitní [change file](dlx1-nomrv.ch), který pouze vybírá první
aktivní položku; není vydávána za nalezený původní autorův nemrv program.
Sestavení do izolovaného adresáře a všechny hashe zaznamenává
[build_dlx1_audit.py](build_dlx1_audit.py).

Při střídavém pořadí primárních položek S0,M0,S1,M1,...,S9,M9 dostaneme:

| Varianta | Řešení | Hledací memy | Memy na řešení |
|---|---:|---:|---:|
| neupravený DLX1 s MRV | 439792 | 79383697 | 180.5028217885 |
| první aktivní položka | 439792 | 121737116 | 276.8061174373 |

Obě hodnoty tedy souhlasí s přibližnými knižními 180/275; při zaokrouhlení
na nejbližší násobek pěti vyjdou přesně tato čísla. Přípravných 5059 memů
je podle autorovy konvence odděleno. Jde o počty logických přístupů,
nikoli převod naměřených sekund na memy.

Pořadí primárních položek není bezvýznamné: při všech S před všemi M
jsou hledací náklady 79862253 s MRV a94357502 bez MRV. Tuto odlišnost
neoznačujeme za chybu přibližného, pořadím podmíněného údaje knihy.

[check_menage_dlx1.py](check_menage_dlx1.py) porovnal celé množiny modelů
obou variant pro n=2..8 s nezávislým výčtem permutací: všech14 případů
souhlasí a každý vypsaný model splňuje omezení. Čtyři velké běhy n10
ověřují počty proti dřívějšímu bitovému DP; nearchivují všechny velké
modelové seznamy. Vstupy, příkazy, logy a přesná čísla jsou v
[dlx1-verified.json](results/menage/dlx1-verified.json), build v
[dlx1-build.json](results/dancing_links/dlx1-build.json).
