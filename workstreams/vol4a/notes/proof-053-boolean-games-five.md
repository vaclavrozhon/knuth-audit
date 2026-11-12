# Úloha 7.1.1–52: všechny čtyři hry pro n=5

Checkpoint X0082, P0769–P0775. Původní zadání p86/file103,
tabulka a komentáře p544/file561. Doklady proof-file103.png
a proof-file561.png. Navazuje na úplnou sémantiku P0758;
žádná enumerace stavů ani matematický program.

Píšeme slovo abcde a označíme prvního hráče P, druhého Q.
První tah je do pozice2; druhý tah má právě dvě možnosti,
do1 („levá větev“) nebo do4 („pravá větev“). V obou případech
třetí tah musí jít do3. Další dvě volby z3 jsou2 a5.

## Univerzální remízová oblast s poslední * na1 — P0769

Předpokládejme, že jediná * je na pozici1 a ukazatel je
v některé z pozic3,4,5. Každý z hráčů, nezávisle na hodnotách
bitů a na konkrétní funkci f, může zaručit, že se slovo nedokončí:

    Při svém tahu z3 volit5; při svém tahu z2 volit4.
    Z4 a5 je tah nucený.

Soupeř dostane tah z2 pouze tehdy, když náš hráč předtím
zvolí3→2, což uvedená strategie nikdy nedělá. Pokud naopak
soupeř zvolí3→2, tah z2 má náš hráč a zvolí4, nikoli1.
Jedinou hranou do1 je2→1, takže pozice1 zůstane nepřiřazená
bez ohledu na soupeřovy volby.

Konečnost úplného stavu zajistí opakování a remízu.
Proto oba hráči mají strategii neprohrát a tato oblast je
přesně remízová pro každou ze čtyř funkcí, nikoli jen pro paritu.
Nezáleží na historii, pokud se hra dosud neukončila; případné
dřívější opakování ji pouze ukončí toutéž remízou.

## Pravá druhá volba vede při nejlepší hře vždy k remíze — P0770

Po 0→2→4→3 jsou neznámé právě1 a5 a Q je na tahu.
Q může zvolit5 a dostat remízovou oblast P0769, takže
si vždy zajistí alespoň remízu.

P si rovněž zajistí alespoň remízu: pokud Q zvolí5, už jsme
v uvedené oblasti; pokud Q zvolí2, P zvolí4 (přepne d),
Q musí z4 do3 a P pak z3 do5 (přiřadí e).
Zbývá pouze * na1 a ukazatel je5. Hodnoty bitů nejsou
pro tento argument podstatné. Pravá větev je proto přesně
remízová pro libovolnou f, bez předpokladu o budoucích
náhodných nebo optimálních bitech.

## Hra(a): druhý hráč vždy vyhraje — P0771

Porovnání abcde s edcba je rozhodnuto už podle a a e,
pokud jsou různé; střední c se při rovnosti stejně neporovnává.
Druhý hráč Q s identitou j∈{0,1} zvolí levou větev a nastaví

    a=1−j, pak při tahu z3 zvolí5 a nastaví e=j.

První hráč může určit b,c a při nuceném posledním tahu
z5 do4 také d, ale nemůže změnit krajní a,e. Proto f=j
nezávisle na všech jeho volbách. Partie končí po pěti tazích.
To dokazuje obě počáteční identity, tedy celý údaj „second“.

## Hra(b): remíza — P0772

V pravé větvi platí P0770. V levé větvi může první hráč
vynutit, že přiřadí poslední *, a tedy podle P0765 vyhraje:

* Zvolí-li Q při čtvrtém tahu3→5, P při pátém5→4
  přiřadí poslední d.
* Zvolí-li Q čtvrtý tah3→2, P jde2→4 a přiřadí d,
  Q musí4→3 a P jde3→5, kde přiřadí poslední e.

Všechny možné volby Q jsou tím pokryty. Q tedy pravou větví
zabrání prohře, ale nemůže porazit P v žádné větvi. Výsledek
je remíza pro obě identity prvního hráče.

## Hra(c): remíza — P0773

Znovu stačí prokázat, že v levé větvi umí P vždy vyhrát;
pravá je podle P0770 remízová. Při první volbě b a třetí c
použije P následující strategie.

Je-li P hráč0, nastaví b=c=1. Zvolí-li Q čtvrtý tah3→5,
P posledním5→4 ukončí hru a dvojice bc=11 už zaručuje0.
Zvolí-li Q3→2, přepne b na0. P pak jde2→4 s d=1,
Q musí4→3 a přepne c na0; P skončí3→5 s e=1.
Teď zaručuje0 dvojice de=11. Nezáleží na Q-výběru a.

Je-li P hráč1, nastaví b=0,c=1. Zvolí-li Q3→5,
P skončí5→4 s d=0: slovo a010e nemá11.
Zvolí-li Q3→2, přepne b na1. Rozlišíme oba možné a:

* a=0: P jde2→4 s d=0, Q musí4→3 a přepne c na0;
  P skončí3→5 s e=0. Výsledkem je01000.
* a=1: P jde2→1 a přepne a na0, Q musí1→3 a přepne c na0;
  P jde3→5 s e=0 a Q musí5→4, kde smí zvolit libovolné d.
  Obě možná slova01000 a01010 nemají11.

To vyčerpává veškeré odpovědi druhého hráče, včetně toho,
že v poslední podvětvi poslední bit určuje soupeř.
P proto v levé větvi vyhraje jako0 i jako1. Celá hra je remíza.

## Hra(d): přesně „1 loses if first“ — P0774

Pokud P je hráč1, Q je0 a vybere levou větev s a=1.
Pak při tahu z3 vybere5 s e=0. První hráč musí posledním
tahem5→4 dokončit slovo s hodnotou alespoň16 a sudou.
Ta je složená nezávisle na b,c,d. Q tedy vynutí výhru0.

Pokud P je hráč0, nastaví při prvním tahu b=1.
Pravá větev je remízová a P v ní použije P0770.
Pro levou větev nastaví při třetím tahu c=0:

* Jestliže Q zvolí3→5 s libovolným e, P skončí5→4 s d=0.
  Hodnota je16a+8+e, tedy8,9,24 nebo25, vždy složená.
* Jestliže Q zvolí3→2, přepne b na0. P jde2→4 a zvolí d=0,
  Q musí4→3 a přepne c na1; P skončí3→5 s e=0.
  Hodnota je16a+4, tedy4 nebo20, opět složená.

P tedy levou větev vyhrává a pravou remizuje. Q si pravou
větví remízu zajistí. Začíná-li0, je výsledek přesně remíza;
začíná-li1, vyhrává0. To souhlasí s výslovnou definicí poznámky.

## Závislé srovnání a zbývající povinnosti — P0775

Pro n=5 si hráč1 vede v(c) přísně lépe než v(d):
při vlastním začátku v(c) remizuje, v(d) prohraje;
při začátku hráče0 jsou oba výsledky remízové.
Tím je tato konkrétní položka závěrečného komentáře dokázána,
nezávisle na porovnávání náhodných pravděpodobností.

Nyní jsou celé řádky n=2,3,4,5 uzavřené. P0768 ponechává
přesně šestnáct buněk n=6,…,9 a odpovídající komentáře;
zejména tvrzení o palindromickém efektu při n=7 čeká.
Žádná úplná stránka se nepovyšuje. Další přesný případ n=6,
main-text p60/file77 a čtení p218/file235 zůstávají oddělené.
