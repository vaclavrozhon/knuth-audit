# Úloha 7.1.1–52: obecná remízová oblast a přesná část n=8

Checkpoint X0085, P0788–P0794. Zadání p86/file103 a odpověď
p544/file561 zůstávají stejné originály jako v proof-055.
Bez programu, procházení herního grafu nebo odhadu z četností.

## Zobecněný prefix — P0788

Argument P0782 nepotřebuje konkrétní hodnoty b=c=1. Pro každé
n≥5 může první hráč P zvolit b=β a c=γ a po levém začátku
2,1,3 udržovat ve všech rozhodovacích stavech Q z3 invariant

    Q na tahu z3, slovo a β γ d *…*.

Při Q3→2 použije P2→1, nucené Q1→3 a P3→2. Následné
Q2→1 a P1→3 obnoví přesně původní stav; Q2→4 a P4→3 obnoví
invariant s přepnutým a a změněným d. Dvě přepnutí b a c
obnovují β a γ nezávisle na jejich počáteční hodnotě.

Buď Q3→5 odejde do koncovky, nebo se opakuje některý ze šesti
stavů (a,d)∈{0,1}×{*,0,1}. Dřívější opakování také znamená remízu.
Pro konkrétní funkci je třeba dokázat bezpečnou koncovku pro obě
možnosti: d dosud * nebo d již přiřazené. Samotný prefix nedokazuje,
že P umí vyhrát či remizovat po odchodu Q do5.

## Obecná chráněná nepřiřazená pozice — P0789

Nechť k≥1, n≥k+4, x_k=* a ukazatel m≥k+2. Každý z obou
hráčů může nezávisle zaručit remízu touto politikou svých tahů:

    z k+1 do k+3;
    z k+2 do k+4;
    z každého m≥k+3 do m−1.

Je nutné vysvětlit i první řádek, ačkoli počáteční m≥k+2:
soupeř z k+2 může ustoupit na k+1 a předat nám tah tam.
Naše odpověď k+1→k+3 je legální. Soupeř naproti tomu nemůže
dostat tah z k+1: museli bychom sami z k+2 ustoupit o1,
což politika vylučuje. Nikdo proto nikdy nepřiřadí x_k.
Ukazatel zůstane alespoň k+1 a jiný vstup do k zespodu se
nemůže objevit. Všechna předepsaná zvýšení jsou legální díky
n≥k+4; ostatní tahy klesají o1. V konečném prostoru stavů
musí dojít k opakování a hra skončí remízou.

Na předpokladu m≥k+2 záleží. Při m=k+1 může aktivní hráč
sám ustoupit na k a chráněnou pozici přiřadit. Pokud ovšem
chce zajistit remízu, zvolí k+1→k+3 a vstoupí do doložené
oblasti. Z této situace netvrdíme univerzální remízu bez
zohlednění aktivního hráče a jeho první volby.

Pro n≥8 a k=4: po odchodu Q3→5, pokud d=*, může aktivní P
zvolit5→7. Nyní m=7≥6 a d stále *, takže P remízu zaručí
pro libovolnou funkci a všechny hodnoty ostatních bitů.
P0776 je přesně případ k=1; jeho hotový důkaz se neopakuje.

## n=8, hra(a): draw pro oba začínající hráče — P0790

P s identitou j zvolí b=1−j; c lze zvolit libovolně.
Použije prefix P0788. Nekonečný prefix dává remízu. Po odchodu
do5 s d=* remizuje podle P0789. Zbývá případ d již přiřazené.

P5→7 nastaví g=j, Q musí7→6 a přiřadí f, P6→8 nastaví
poslední h=j. Všechny jiné bity už byly přiřazené; protihráč
nemá v této koncovce jinou volbu směru.

Pro j=1 platí a≤h=1; při rovnosti b=0<g=1. Slovo je tedy
striktně menší než jeho obrácení a P vyhraje1. Pro j=0 platí
a≥h=0; při rovnosti b=1>g=0. Slovo je striktně větší a P
vyhraje0. Vnitřní c,d,e,f nejsou pro tento závěr relevantní.

P může proti levé větvi vždy neprohrát; Q pravým druhým tahem
2→4 zaručí remízu podle P0776. Oba počátky tedy přesně remizují.

## n=8, hra(b): draw pro oba začínající hráče — P0791

P použije P0788 s libovolnými pevnými β,γ. Prefix bez odchodu
remizuje; odchod s d=* remizuje podle P0789. Pro d již přiřazené
P5→7 přiřadí g, Q7→6 přiřadí f a P6→8 přiřadí poslední h.
Podle P0765 nastaví h na paritu potřebnou ke své výhře.

Tím P zaručí neprohru. Pravá větev poskytuje Q remízu;
obě počáteční identity proto mají přesně vytištěný výsledek draw.

## n=8, hra(c), začíná0: draw — P0792

P=0 nastaví β=γ=1. Prefix a koncovka s d=* jsou bezpečné
podle P0788/P0789. Pro přiřazené d použije cestu5,7,6,8,
přičemž během ní b ani c nejsou změněny. Dvojice bc=11
proto zaručí0 při libovolných volbách g,f,h.

To dokazuje neprohru P a spolu s pravou větví přesnou remízu
při začátku0. Nedokazuje to remízovou strategii při začátku1:
analogické β=γ=0 nezabrání dvojici de=11, kterou může vytvořit Q.
Tuto chybějící polovinu nelze uzavřít symetrií, protože predikát
„neobsahuje11“ se při výměně identit nekomplementuje.

## n=8, hra(d), začíná0: draw — P0793

P=0 opět nastaví β=γ=1 a použije tentýž prefix/chráněnou oblast.
Pro přiřazené d zvolí cestu5,7,6,8 s posledním h=0. Konečná
hodnota je sudá a alespoň64, neboť b=1 se nezměnilo. Je složená.

P tedy zaručí neprohru a pravá větev dává Q přesnou remízu.
Výherní strategie0 proti začínajícímu1 není tímto argumentem
dokázána; původní tabulka tuto chybějící polovinu nenahrazuje.

## Přesná zbývající mezera — P0794, partial

Z n=8 zbývá doložit:

* (c) remízu, když začíná1;
* (d) výhru0, když začíná1.

Celé řádky n=2,…,7 a celé buňky(a)/(b) pro n=8 jsou uzavřené.
P0768 nyní obsahuje šest neuzavřených buněk: dvě právě uvedené
částečné buňky n=8 a čtyři celé buňky n=9. Závislé srovnání(c)/(d)
pro n=8,9 se nepovyšuje na checked. Kromě zde uvedených strategií
nebyl pro tyto případy vytvořen herní certifikát ani proveden census.

Tato mezera zůstává otevřená pro další samostatný rozklad;
nezadržuje samostatnou kontrolu navazujícího hlavního textu o Kromových
klauzulích a komicích na p60–62. Čtení218/file235 beze změny.
