# §2.1: uzly, odkazy a devět úloh

Kontrola 1. 11. 2026. Autoritativní podklad: první tisk třetího vydání,
1997; původní obrazy s. 232–237 a částí odpovědí na s. 534–536 jsou
v `../images/` a byly přečteny. Soupis 1–9 je ze skenů potvrzen.
Matematika a programy mají stav `checked`; nový nález nevznikl.
Historické a bibliografické podrobnosti mají samostatnou poznámku.

## Reprezentace a význam předpokladů

Uzel je zde záznam uložený v souvislých slovech paměti. Odkaz na uzel
je adresa jeho prvního slova; nulový odkaz Λ je reprezentován číslem 0,
které není adresou žádného uzlu. Pole je pojmenovaná část záznamu.
F(L) značí konkrétní proměnnou v poli F uzlu s nenulovým odkazem L.
Samotné jméno F ještě neoznačuje konkrétní uloženou hodnotu.

Kartový uzel má dvě slova. První obsahuje TAG v bajtu 1, SUIT v bajtu 2,
RANK v bajtu 3 a NEXT v bajtech 4–5; druhé obsahuje pět znaků TITLE.
TAG je 0 pro líc nahoru a 1 pro líc dolů. Ukazatel TOP vede na první
kartu nebo je Λ. Zásobník karet je konečný řetěz vzájemně různých
uzlů zakončený Λ. Podle samotného významu „nové karty“ není vkládaný
uzel již součástí řetězu a nekoliduje s ukazatelovými proměnnými
ani kódem. Cyklus v NEXT by nebyl reprezentací této hromádky karet.

V obrázku (2) je řetěz 242 → 386 → 100 → Λ. Karty mají pořadí
2 kárová, 3 piková, 10 křížová, s poslední kartou otočenou lícem dolů.
Všechny hodnoty v (4) a odpovědi 1 z toho přímo vyplývají.
Nesprávné TITLE poslední karty v obrázku (3) je známé erratum
z 10. 8. 1997; ostatní pole i odkazy souhlasí.

## Algoritmy A a B

A1 nastaví NEXT nové karty na dosavadní TOP; A2 nastaví TOP na novou
kartu; A3 smaže její TAG. Nový řetěz je tedy přesně nová karta
následovaná starým řetězem, s novou kartou lícem nahoru. Zbytek uzlů
se nezmění. Důkaz zahrnuje prázdnou původní hromádku.

Při vstupu do B2 je N počet již navštívených karet a X odkaz na další
dosud nenavštívenou kartu, případně Λ za poslední kartou. B1 tento
invariant zavádí pro prázdný navštívený prefix; B3 jej rozšíří o jeden
uzel. Po konečně mnoha krocích X=Λ a N je celkový počet karet.
Na žádné cestě se nevyhodnocuje NEXT(Λ).

MIX implementace A na s. 236 načte adresu nové karty do I1 a starý TOP
do A, zapíše jeho poslední dva bajty do NEXT nové karty, uloží I1 jako
nový TOP a vynuluje právě TAG. Dvoubajtové adresy se vejdou do indexových
registrů pro každou povolenou velikost MIX bajtu. SUIT, RANK i TITLE
zůstávají stejné. Je to přesná realizace A1–A3, ne zápis adresy buňky TOP
do seznamu.

## CONTENTS, LOC a kopie uzlu

CONTENTS(a) je proměnná uložená v celém slově na adrese a; LOC(V) je
adresa slova, které obsahuje proměnnou V. Pro celočíselné slovo V je
CONTENTS(LOC(V))=V definitoricky. Opačný výraz LOC(CONTENTS(V))=V je
smysluplný, když V představuje platný nenulový odkaz na takové slovo.
Ve cvičení 2 je V symbol pro proměnnou, jak byl zaveden v textu;
odpověď popisuje příslušný typ a vyloučení Λ. Nejde o důkaz, že
CONTENTS nikdy nesmí dostat konstantní adresu: text sám uvádí CONTENTS(1000).

NODE(TOP) označuje celý záznam a CARD je proměnná s týmž záznamovým
typem. Kopie c slov v (7), pro 0≤j<c, kopíruje právě všechny části
záznamu. Konvence běžných samostatných proměnných zaručuje disjunktní
úložiště, případně totožný celý uzel; svévolné částečné překrytí dvou
proměnných není zadáním této notace. Původní obraz má v (7) správně
0≤j, přestože OCR ztrácí rovnost.

## Úlohy 1–7

1. NEXT(TOP)=386, proto SUIT(NEXT(TOP))=4. Třetí NEXT od TOP je Λ.
   V žádném výrazu se pak již nepoužije pole nulového odkazu.
2. Platný nenulový odkaz, jak je vysvětleno výše.
3. NEWCARD dostane původní TOP. Pro neprázdný řetěz se TOP posune na
   následníka, čímž se odstraní právě první uzel; pro prázdný řetěz
   zůstane TOP=NEWCARD=Λ. TAG se nemá obnovovat: zadání říká „essentially
   undoes“ a požaduje odstranění uzlu, nikoli rekonstrukci starého líce.
4. Použijeme pomocnou počáteční buňku s adresou S=LOC(TOP) a polem
   NEXT(S)=TOP, což odpověď výslovně předpokládá. C2 postupuje po
   řetězu, dokud X není jeho poslední uzel; pro prázdný seznam zůstane
   X=S. C3 připojí novou kartu právě za X, ukončí ji Λ a nastaví TAG=1.
   Tím správně zahrnuje i prázdný případ. Pole pomocné buňky se má
   interpretovat přes uvedenou explicitní konvenci, ne jako nový kartový uzel.
5. Invariant D2 je Y=NEXT(X), přičemž Y je aktuální karta a X její
   předchůdce nebo S. Je zachován při X←Y, Y←NEXT(Y). Proto po
   NEXT(Y)=Λ odpojení NEXT(X)←Λ odebere právě poslední kartu a
   NEWCARD←Y ji vrátí. U jediné karty je X=S a TOP se správně vynuluje.
   Zmínka o „next-to-last card“ v závěrečném komentáři je zde přirozeně
   čtena s touto výslovnou pomocnou buňkou; algoritmus singleton nevynechává.
6. SUIT(LOC(CARD)) a SUIT(TOP) jsou správné. CARD je záznamová hodnota,
   ne odkaz; CONTENTS(CARD) proto není vhodně typovaný výraz.
7. LDA TOP(NEXT) čte pole 4:5 proměnné TOP, tedy TOP samotný.
   LD1 TOP; LDA 0,1(NEXT) provede ještě dereferenci a vrátí NEXT(TOP).
   V příkladu jsou obě hodnoty různé: 242 oproti 386. Příklad LDA X
   proti ENTA X správně rozlišuje hodnotu proměnné a její adresu.

## Úloha 8: MIX realizace B

ENTA 0 a LD1 TOP zavádějí N a X. J1Z *+4 přeskočí všechny tři
instrukce smyčky, je-li řetěz prázdný. Jinak INCA 1; LD1 0,1(NEXT)
zpracují jeden uzel a J1NZ *−2 opakuje právě tuto dvojici. Žádná jiná
instrukce A nebo I1 nepřepisuje. Invariant algoritmu B platí doslova;
po návratu z fragmentu je A počet karet a I1 nulový odkaz. Fragment
nemění paměť. K testu byl pouze připojen HLT za jeho konec.

## Úloha 9: výstup a překrývající se konstanty

I2 ukazuje na další kartu. Prázdný případ skočí rovnou na výstup
předem vloženého textu PILE EMPTY. Neprázdná smyčka načte TAG a
počká na dokončení předchozího výstupu **před** prvním zápisem do PBUF.
Podle TAG připraví tři slova, do prostředního zkopíruje pět znaků
z druhého slova uzlu, posune I2 na NEXT a spustí OUT. Poté buď
pokračuje další kartou, nebo zastaví výpočet. Poslední I/O se může
dokončit po HLT, stejně jako v jiných programech knihy.

Čtyři konstantní slova na s. 536 mají přesně obsah

```
PAREN:  "    ("
BLANKS: "     "
        ")    "
        "     "
```

MOVE PAREN(3) tedy připraví otevírací závorku, prázdné prostřední
slovo a zavírací závorku. MOVE BLANKS(3) připraví prázdné krajní
slovo a závorku **jen v prostředním slově**, které se vzápětí úplně
přepíše názvem karty. Tato překrývající se konstanta není chyba.
MOVE zároveň zvýší I1, ale další přístup k PBUF používá přímou
adresu a další iterace I1 znovu inicializuje.

Zbylých 21 slov tiskového řádku zůstává prázdných podle obecné
konvence MIXAL na s. 151: nespecifikované buňky se při načtení
obvykle nulují (s výjimkou oblasti zavaděče, kterou kód nemá používat).
Nulový znak je mezera. Nejde tedy o nově chybějící inicializaci PBUF.
Předpokládáme standardní umístění programu a dat mimo zavaděč.

## Provedené kontroly a rozsah

`../check_intro_programs.py` využívá již ověřený assembler, celočíselný
MIX a model asynchronního I/O, aniž je mění. Nezávislá očekávání jsou
obyčejné seznamy a řetězce. Prošlo 1260 kontrol, včetně:

* A a B pro všechny báze bajtu 64–100 a délky 0,1,2,7,52;
* dlouhého řetězu 1001 karet a hraniční adresy uzlu 3998;
* zachování ostatních polí/paměti a rozdílu obou sekvencí úlohy 7;
* 48 tiskových případů s prázdnou hromádkou, oběma hodnotami TAG,
  smíšenými kartami a zpožděním I/O 0,1,97 jednotek;
* zachování původních uzlů a TOP během tisku a ochrany obsazeného bufferu.

Výsledek je v `../results/intro-programs.json`. Úspěšné běhy nebyly
bez nové pochybnosti opakovány. Obecnou správnost zdůvodňují předchozí
invarianty; konečné případy navíc kontrolují věrnost přepisu strojových
instrukcí, skoků, polí a konstant.
