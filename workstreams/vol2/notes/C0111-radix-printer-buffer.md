# V2-C0111: příliš krátké a překrývající se tiskové buffery

**confirmed**, 2. listopadu 2026. TAOCP2, třetí vydání, první tisk
1997, odpověď §4.4-13, strany 637–638. Oba původní skeny byly
vizuálně přečteny: [začátek](../images/vol2-p637.png),
[konec programu](../images/vol2-p638.png).

Program ukládá dva řádky po 20 slovech do BUF,...,BUF+39.
Deklarace `BUF ALF .____` a `ORIG *+39` umístí první instrukci
START právě do BUF+40. První OUT má adresu BUF, druhý BUF+20.

Tiskárna MIX však přenáší **24 slov, tedy 120 znaků**. Definice
je ve svazku 1, strana 136, a OUT na straně 137 výslovně zakazuje
měnit zdrojovou paměť do dokončení přenosu. Obě původní stránky
byly přečteny: [velikost bloku](../images/radix-vol1-p136.png),
[asynchronní přenos](../images/radix-vol1-p137.png). Jsou to strany
151 a 152 souboru svazku 1.

Z toho plynou dvě vady téže alokace:

1. Druhý OUT čte BUF+20,...,BUF+43. Poslední čtyři slova jsou
   první čtyři instrukce programu, nikoli mezery. To platí pro
   každý vstup, například m=1 a U+1=0. Již instrukce `ENT2 -40`
   obsahuje nenulové bajty, takže posledních 20 znaků nemůže být
   zamýšleným prázdným koncem řádku.
2. První OUT čte BUF,...,BUF+23. V další smyčce se BUF+20,...,BUF+23
   přepíší prvními dvěma skupinami druhého řádku, aniž se čeká na
   dokončení prvního přenosu. Přípustná rychlost tiskárny proto může
   způsobit, že se tyto dvě skupiny objeví také na konci prvního řádku.

Konečný počet a správnost 180 desítkových číslic tím není zpochybněn;
chyba je ve výstupu celých tiskových bloků. Nevysvětluje ji OCR ani
chybějící vnitřek násobicí smyčky, který nemění adresy bufferů.

Jedna oprava zachovávající překrytí výpočtu s tiskem:

```text
BUF ALF .____
    ORIG *+47              (48 slov; ostatní bajty musejí být mezery)
...
    ENT2 -48              (místo -40)
...
    STA BUF+48,2(2:5)     (místo BUF+40)
    STX BUF+49,2          (místo BUF+41)
...
    OUT BUF+28,2(PRINTER)  (místo BUF+20)
    INC2 4                (nové: přeskočit konec tiskového bloku)
    J2N 8B
```

Při prvním OUT je index −28 a adresa BUF; po přeskočení čtyř
slov začne druhý řádek v BUF+24. Při druhém OUT je index −4,
adresa BUF+24, a po posledním INC2 je index 0. Čtyři koncová
slova každého bloku zůstanou prázdná. Před opětovným použitím
bufferu po návratu je jako u každého asynchronního OUT třeba
počkat na dokončení přenosu.

Přepis `sources/radix-print.mix` obsahuje původní i opravené instrukce.
Simulátor zachovává přesnou vícečetnou aritmetiku, CHAR, části slov
a 24slovný tisk. Ověřuje okamžité i zpožděné dokončení přenosu.
Pro nulový vstup reprodukuje obě vady; opravená verze prošla pro
270 případů s až 64 vstupními slovy a pro kapacity bajtu 64,128,256.
Všech 180 číslic a všechny průběžné zbytky se porovnávají s nezávislým
celočíselným orákulem; 7354krát byla použita větev opravy přenosu.
Relace 59932 skončila exit 0; výsledky v `results/radix-print.json`.

Ve všech čtyřech vrstvách `all2-prepre`, `all2-pre`, `all2`, `err2`
byly prohledány strany 637/638 a výrazy BUF, PRINTER, ORIG,
printer a output. Nalezeny jen nesouvisející náhrady odpovědí 11
a 18; oprava programu 13 nebyla nalezena. Nejnovější fyzický tisk,
priorita ani odměna nejsou ověřeny. Hlášení nebylo odesláno.
