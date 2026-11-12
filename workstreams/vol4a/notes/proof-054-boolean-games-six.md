# Úloha 7.1.1–52: všechny čtyři hry pro n=6

Checkpoint X0083, P0776–P0781. Zadání p86/file103, odpověď
p544/file561; stejné původní rendery jako proof-052/053.
Píšeme abcdef, první hráč P a druhý Q. Žádný matematický
program ani enumerace stavů.

## Obecná remízová oblast pro všechna n≥5 — P0776

P0769 lze rozšířit: jestliže je pozice1 stále * a ukazatel
je alespoň3, oba hráči mohou zajistit remízu, i když zbývají
další nepřiřazené pozice. Každý z nich může použít politiku

    z3 jít do5; z2 jít do4; z m≥4 jít do m−1.

Všechny tyto tahy jsou pro n≥5 legální. Soupeř dostane tah
z2 jen po našem tahu3→2, který politika vylučuje.
Náš vlastní tah z2 nikdy nejde do1. Nikdo tedy nemůže
přiřadit pozici1, bez ohledu na případné jiné soupeřovy skoky
do vyšších pozic. Konečný stav se nakonec zopakuje a nastane remíza.

Proto pro **každé n≥5 a každou f** vede druhý tah2→4
při nejlepší hře přesně k remíze. Druhý hráč má vždy možnost
neprohrát a ve všech zbývajících výherních větvích je nutné
zkoumat jeho volbu2→1. Toto není závěr z četnosti hodnot funkce.

## n=6, hra(a): druhý hráč vyhraje — P0777

Q může vynutit celou cestu

    0→2→1→3→5→4→6.

Všechny P-tahy na ní jsou nucené. Q s identitou j nastaví
a=1−j a poslední f=j. Vnější dvojice (a,f) pak rozhoduje
lexikografické porovnání abcdef s fedcba: jeho hodnota je j.
Žádné vnitřní b,c,d,e na tom nic nezmění. Q vyhraje jako0 i jako1.

## n=6, hra(b): druhý hráč vyhraje — P0778

Táž vynucená cesta nechá Q přiřadit poslední f. P0765 dává
možnost nastavit výslednou paritu na svou identitu.
To dokazuje oba případy „second player wins“.

## n=6, hra(c): přesně „1 loses if first“ — P0779

Je-li P hráč1 a Q hráč0, Q použije uvedenou cestu a nastaví
e=f=1. Sousední dvojice11 zaručí0 nezávisle na P-bitech.
Proto začínající hráč1 prohraje.

Zbývá P=0, Q=1. Pravá větev je podle P0776 remízová.
Pro levou větev P nastaví b=c=1. Hodnotu a necháme libovolnou.

### Q při čtvrtém tahu zvolí3→2

B se přepne na0. P jde2→4 s d=1. Q má dvě možnosti:

* Q4→6: P musí6→5 a nastaví e=1; dvojice de=11 dá0.
* Q4→3 přepne c na0: P3→5 nastaví e=1, Q musí5→4
  a přepne d na0; P4→6 nastaví f=1. Dvojice ef=11 dá0.

V obou případech P vyhraje bez další volby Q.

### Q při čtvrtém tahu zvolí3→5

P musí5→4 a nastaví d=1. Pokud Q4→6, hra skončí s bc=11,
tedy P vyhraje. Jinak Q4→3 přepne c na0; P je na tahu z3
a f je jediná *. Máme b=1,c=0,d=1 a e zvolené Q.

Při e=0 P3→5 přepne e na1, Q musí5→4 a přepne d na0;
P4→6 nastaví f=1 a vyhraje přes ef=11.

Při e=1 označme tento úplný stav

    S: ukazatel3, P na tahu, slovo a1011*.

P použije následující úplný postup:

    P3→5: e=0;
    Q5→4: d=0 (nucené);
    P4→3: c=1.

Teď má Q z3 dvě možnosti.

* Q3→2 přepne b na0. P2→4 přepne d na1.
  Pokud Q4→6, dvojice cd=11 dá0.
  Pokud Q4→3, přepne c na0; P3→5 přepne e na1,
  Q5→4 přepne d na0 a P4→6 nastaví f=1. Dvojice ef=11 dá0.
* Q3→5 přepne e na1. P musí5→4 a přepne d na1.
  Pokud Q4→6, dvojice de=11 dá0.
  Pokud Q4→3, přepne c na0 a vrátí přesně stav S:
  a se nezměnilo, b=1,c=0,d=1,e=1,f=*, ukazatel3 a P na tahu.
  Jde o druhou návštěvu, tedy remízu.

P tak v levé větvi zaručí výhru nebo remízu pro všechny Q-volby.
Q může pravou větví remízu zaručit, takže při začátku0 je
výsledek přesně remíza. Spolu s výhrou0 při začátku1 je
doložena celá vytištěná buňka, nejen její půlka.

## n=6, hra(d): přesně „1 loses if first“ — P0780

Pokud P je1, Q je0 a použije vynucenou cestu z P0777,
s a=1 a posledním f=0. Výsledná hodnota je sudá a alespoň32,
tedy složená; Q vynutí0.

Pokud P je0, zvolí b=c=1 v levé větvi. Pravá větev má
jeho bezpečnou strategii P0776. V levé větvi rozlišíme
opět veškeré možnosti Q; a je už známo před volbou c.

### Q při čtvrtém tahu zvolí3→2

B se přepne na0. P2→4 nastaví d=a.

* Q4→6 přiřadí f; P musí6→5 a nastaví e=0.
  Hodnota je 36a+8+f, tedy8,9,44 nebo45, vždy složená.
* Q4→3 přepne c na0; P3→5 nastaví e=0,
  Q5→4 přepne d na1−a a P4→6 nastaví f=0.
  Hodnota je4+28a, tedy4 nebo32, vždy složená.

### Q při čtvrtém tahu zvolí3→5

P musí5→4 a nastaví d=a·e, tedy součin již známých bitů.
Pokud Q4→6 přiřadí poslední f, výsledná hodnota je:

* pro a=0 libovolná z24,25,26,27;
* pro a=1,e=0 jedna z56,57;
* pro a=1,e=1 jedna z62,63.

Všechna tato čísla jsou složená: liché25,27,57,63 jsou
násobky5 nebo3 a sudé hodnoty jsou větší než2.

Pokud Q místo toho zvolí4→3, přepne c na0. P3→5 přepne e,
Q musí5→4 a přepne d; P4→6 nastaví f=0.
Výsledná hodnota je sudá a alespoň16, protože b zůstalo1.
Opět vyhraje0.

P tedy levou větev vždy vyhraje; Q může pravou větví
remizovat. Při začátku0 je výsledek přesně remíza,
při začátku1 vyhraje0, jak uvádí tabulka.

## Převzaté výsledky, úplnost a další rozsah — P0781

Všechny svědecké větve jsou legální podle n=6:
z1 se jde pouze do3, z5 pouze do4 a z6 pouze do5.
U každé Q-volby z2/3/4 je uvedena odpověď; žádná další
volba není zatajena. Ve vítězných větvích se úplný stav
neopakuje; v jediné remízové větvi je přesná rovnost S
výslovně zkontrolována. Při případném dřívějším opakování
by bezpečná strategie stále poskytla stejnou remízu.

Pro n=6 mají(c) a(d) totožný výsledek pro obě počáteční
identity, takže hráč1 není v(c) horší ani lepší než v(d).
To uzavírá tuto část srovnávacího komentáře.

Celé řádky n=2,…,6 jsou nyní doložené. P0768 ponechává
přesně dvanáct buněk n=7,8,9 a jejich závislé dodatky.
Další n=7, bez brute-force censu; main-text p60/file77
a čtení p218/file235 zůstávají oddělené.
