# Vlastní MIX řešení cvičení1.4.3.2–6

[selftrace_program.py](selftrace_program.py) sestavuje skutečný MIX program,
který interpretuje a vypisuje vlastní instrukce. Při jeho běhu není žádná
MIX instrukce nahrazena Pythonem; všechny kroky provádí nezměněný
`mix_machine.py`/`mix_io.py`. Python pouze sestaví a nahraje počáteční obraz
paměti a v testech sleduje výsledek. Řešení rozvíjí obecný simulátor M,
nikoli krátký původní tracer se společnými pracovními buňkami.

**Reentrantní** zde znamená, že tatáž rutina může působit na další
vnořené úrovni, aniž přepíše pracovní stav předchozí úrovně. Každá
úroveň interpretuje stejný MIX program, který sám interpretuje stejný
program atd. Výpis přímo prováděného interpretu má úroveň0; výpis, který
pochází z jeho interpretovaného programu, se před odesláním označí
o jedna větší úrovní.

## Paměťový model a skutečný program

Fyzické adresy0–1999 jsou slovník dvojic `(logická adresa, hodnota)`.
Fyzické adresy2000–2999 obsahují neměnný obraz zdrojového programu,
dále označený ROM. Slovo ROM zde znamená jen oblast, do které tento
program nezapisuje, nikoli nové zařízení MIX. Právě vykonávaný program
a jeho proměnné jsou na3000–3535; zbytek horního tisíce slov je nulový.
Obraz ROM vzniká při sestavení stejně jako ostatní datové konstanty.
Duplicitní kód v ROM obsahuje původní adresy3000..., ne přeložené adresy.

Počáteční logická paměť `V[m]`, pro `0<=m<4000`, je:

```text
0 <= m < 2000:       +0
2000 <= m < 3000:    ROM[m]
3000 <= m < 4000:    ROM[m-1000]
```

VREAD nejprve hledá m ve slovníku; při zásahu vrátí uloženou hodnotu,
jinak uvedenou počáteční hodnotu. VWRITE nahradí existující hodnotu
nebo přidá jednu dvojici. VREAD vrací celé podepsané slovo v rA a
zachovává rX; VWRITE bere celé slovo z rX. Obě rutiny zachovávají I1
včetně znaménka nuly a ostatní pomocné indexové registry, které
potřebuje simulátor M. Adresu předává I5. Obsazená délka USED je sudá,
nikdy neklesá a nepřekročí přidělenou kapacitu. Další alokace skočí
na MEMFULL před zápisem do ROM. Standardní kapacita je2000 slov,
tedy1000 dvojic; testovat lze i menší přidělenou oblast.

Oproti M jsou přes VREAD/VWRITE vedeny **všechny** logické přístupy:
fetch instrukce, MEMORY, druhé čtení paměťového slova ve STORE, samotný
STORE a každý zdroj/cíl MOVE. Druhé čtení ve STORE je důležité:
nesmí se použít fyzické slovo ani zničit mezivýsledek v rX. Rozsah
logické paměti je rozšířen na všech4000 adres. CYCLE po fetch vypíše
instrukci; pak znovu načte INST, aby tisk nezměnil znaménko rA potřebné
pro následné sestavení efektivní adresy.

Logovací rutina připraví24slovný řádek tiskárny. První dvě slova jsou
deset desetinných číslic úrovně, další dvě adresa instrukce, další dvě
její velikost jako desetimístné číslo; sedmé slovo nese samostatný znak
znaménka. Tím je zachováno i záporné nulové slovo. `CHAR` používá pevně
deset číslic; to stačí pro všechny MIX radice64–100, protože
`b^5-1<=9999999999`. Zbytek řádku jsou mezery.

Simulované OUT na jednotku18 přečte všech24 logických slov přes VREAD,
zvýší zakódovanou úroveň o1 pomocí NUM/CHAR a vytiskne řádek skutečným
OUT. Skutečné JBUS počká na dokončení přenosu. Logická tiskárna je
poté ready; JBUS/JRED nad ní mají odpovídající chování. Jiné druhy I/O
toto samotrasovací řešení nepotřebuje a odmítá je. Všechny tiskové
záznamy vytvořené samotným programem mají požadovaný formát, který
se přeposíláním zachovává. Nejde o slib převodu libovolného cizího
výstupního formátu ani o podporu floating point.

## Důkaz oddělení stavů a rekurze

Invariant slovníku: logická hodnota V[m] je poslední hodnota zapsaná
na m; pokud se tam dosud nezapisovalo, je to hodnota počátečního obrazu.
Jedinečnost klíčů a úplnost vložení plyne z lineárního hledání všech
USED/2 dvojic před novou alokací. VREAD tento invariant přímo realizuje.
Znaménko hodnoty je součástí slova a nikde se při uložení nezahazuje.

Použijeme důkaz simulátoru M z NOTES.md. Náhrada fyzického přístupu
abstraktním VREAD/VWRITE mění pouze reprezentaci paměti, nikoli význam
instrukce. Kontrola rozsahu, polí a registrů zůstává stejná. Každý
dokončený sledovaný krok proto odpovídá jednomu kroku přímého MIX se
stavem V a s příslušnými oddělenými registry/PC/J/příznaky. Přeposlaný
výstup se liší pouze označením úrovně, jak požaduje výpis rekurze.

Interpretem sledovaný program má **tentýž počáteční obraz**, včetně
své vlastní ROM a prázdného vlastního slovníku. Jeho instrukce VWRITE
při vykonávání mění pouze jeho logickou paměť, tedy slovník nadřazeného
interpretu; nezapisují přímo do fyzického pracovního kontextu. Proto
provádí stejnou správnou interpretaci na další úrovni. Indukce podle
počtu vnořených úrovní a podle počtu jejich dokončených kroků dává
správnost každého konečného prefixu, který se vejde do paměti. Nevzniká
přepis PREG a dalších aktivních buněk jako v původních cvičeních4/5.

Každý přístup i každý krok konečné úrovně skončí, protože slovník je
konečný a fyzická tiskárna při normální činnosti dokončí přenos. Program
opakovaně dospěje ke spuštění stejného programu na další úrovni.
Je-li na vnitřní úrovni obsazeno n slov jejího slovníku, vnější úroveň
musí reprezentovat zápisy do všech těchto n logických nízkých adres
a navíc alespoň jednu pracovní buňku horní oblasti. Potřebuje proto
nejméně `2(n+1)` fyzických slov svého slovníku. Rekurzivně tak potřeba
paměti roste alespoň jako `U(d+1)>=2(U(d)+1)`, kde U(d) je potřeba při
d aktivovaných vnitřních úrovních a U(0)=0. Tedy
`U(d)>=2^(d+1)-2`: libovolná konečná kapacita musí nakonec vyvolat
MEMFULL. Konkrétní rozložení4000slovného MIX omezuje slovník na2000
slov; rutina netvrdí, že může realizovat skutečně nekonečnou paměť.

## Provedené kontroly a přesné meze

[check_selftrace.py](check_selftrace.py) porovnává po každém dokončeném
sledovaném kroku skutečný program s přímým vykonáním stejného obrazu.
Porovnává osm registrů se znaménky, PC, J, oba příznaky, přesnou množinu
zapsaných logických adres a jejich hodnoty. Kontroluje též, že fyzická
ROM zůstala nezměněna. Posloupnost výpisů úrovně0 se musí přesně rovnat
posloupnosti původních PC/instrukcí. Všechny hlubší výpisy musí být
přesně výstupem referenčního programu s úrovní zvýšenou o1.

- Výchozí2000slovná kapacita:100 sledovaných instrukcí ve všech37
  radicích, celkem3737 porovnání úplného stavu na hranici CYCLE.
- Přidělená128slovná kapacita: celé běhy až po MEMFULL v radicích64
  a100; každý má4 465 344 skutečných MIX kroků,8329 zkontrolovaných
  stavů,8329 výpisů úrovně0 a42 výpisů úrovně1. Poslední instrukce
  byla vypsána před pokusem o alokaci; při vyčerpání není označena
  za úspěšně dokončený sledovaný krok.
- [check_self_memory.py](check_self_memory.py) navíc ověřuje VREAD/
  VWRITE, stínění pracovního kódu i ROM, znaménko nuly, opakovaný zápis
  bez nové alokace a skutečný přechod1998→2000 obsazených slov, po němž
  další nový klíč musí skončit na MEMFULL. Opět všech37 radixů.

Plný běh s výchozí kapacitou2000 až do jejího vyčerpání nebyl použit
jako důkaz: je mnohem delší. Jeho obecné chování zajišťují uvedené
invarianty a rekurzivní důkaz, podporované explicitním testem samotné
maximální alokační hranice. Nebyl sepsán formální důkaz emulátoru.

Dosažitelný mezistav navíc dokládá třetí úroveň bez opakování drahého
vnějšího prefixu. `check_self_checkpoint.py` nejprve přímo vykoná
12310 instrukcí stejného obrazu do místa před jeho prvním výpisem
úrovně1. Tento přesný logický stav uloží do184slovného slovníku
vnějšího interpretu. Ten běžnými11549 MIX instrukcemi vytvoří záznam
úrovně2 o instrukci na3000 a zachová odpovídající stav sledovaného
stroje. Ověřeno pro b=64 i100. Je to kontrola od explicitně
dosažitelného mezistavu, ne předstíraný nepřerušený běh celé tříúrovňové
interpretace od počátku.

Úplné načítací obrazy jsou `results/selftrace-load64.mixal` a
`results/selftrace-load100.mixal`. Obsahují obyčejné ORIG/CON/END a
jejich zpětné sestavení se přesně shoduje s testovaným obrazem, včetně
ROM a vstupní adresy3000. JSON soubory stejného jména obsahují adresy
symbolů a kontrolní součet obrazu.
