# §4.5.1-15/16: překlad programů a intervalové experimenty

Audit 2. listopadu 2026. Obě experimentální úlohy ze str. 333
jsou provedeny v níže vymezeném rozsahu. Výsledky někdy zlepší
přesnost jednoduchého racionálního výsledku, jindy ji výrazně
zhorší. Nejde o obecný příslib přesnější aritmetiky ani o rychlostní
srovnání strojových implementací. Bez nového nálezu v knize.

## 15: skutečná upravená překladová cesta

`sources/slash_compiler.py` obsahuje lokální front-end k Python
kompilátoru: zdroj se nejprve rozebere na abstraktní syntaktický
strom, tedy strukturu výrazů a příkazů, ten se přepíše a výsledný
strom zpracuje běžná funkce `compile`. Nainstalovaný interpreter
se nepřepisuje. Vstupní programy se ručně neupravují pro slash
aritmetiku; transformace pracuje s jejich původními funkcemi.

Podporovaný rozsah jsou skalární reálné výpočty, celočíselné
řídicí proměnné, běžné kontejnery a funkce Pythonu, sčítání,
odčítání, násobení, dělení a celé mocniny. Floating point literály
a volání `float` se mění na slash hodnoty. Dělení se přepíše i
při dvou celých operandech. Záporná celá mocnina celého základu,
která by jinak vytvořila float, se rovněž převede; nezáporná celá
mocnina dvou celých operandů zůstává celočíselná. Vstupní reálné
argumenty se převádějí při zavolání funkce přes adaptér experimentu.

Volání vybraných skalárních funkcí `math` a NumPy včetně `sqrt`
a `log` se obalí převodem slash -> binary64 -> původní knihovní
funkce -> slash. Používá se skutečná původní knihovní funkce,
nikoli nová implementace logaritmu či odmocniny. Počítadlo volání
ověřuje, že se tento obal opravdu vykonal. Běžný `print` zachová
desetinný výstup; `print(x, fractional=True)` vypíše zlomek.
Ověřený příklad tiskne nejprve `0.1`, potom `1/10`.

Každá aritmetická operace spočítá přesný racionální výsledek
a jednou jej zaokrouhlí mediánovým pravidlem z
[rational-slash.md](rational-slash.md). Celočíselný operand
smíšené operace se nejprve převede do formátu. Nula nemá znaménko;
nekonečna a neurčená hodnota používají pravidla z rational-basic.
Znaménkové porovnání konečných hodnot se provádí přesně.
Literál nejprve dostane stejnou binary64 hodnotu jako v běžném
Python parseru a teprve poté se převádí do slash formátu;
experiment tedy nepřisuzuje všem desítkovým literálům dodatečně
přesný desítkový význam.

To není úplný překladač libovolného Pythonu: obecná NumPy pole,
komplexní čísla, jiné balíky, reflexe typů, přejmenování vyhrazených
builtin funkcí a necelé mocniny nejsou součástí podporovaného
rozsahu. Některé takové konstrukce se výslovně odmítají při
překladu, další při provedení nepodporované operace. Dynamické
modifikace globálních jmen a introspektivní programy nejsou
považovány za přeložené touto sémantikou. Není tvrzeno, že se
automaticky změní aritmetika uvnitř libovolného cizího rozšíření.

## Existující programy a nezávislá reference

Použity jsou původní funkce `r8_hypot` a `r8_log_2` Johna
Burkardta, určené pro double precision. První počítá délku
vektoru (x,y) jako větší velikost krát odmocninu z 1 plus čtverce
poměru; druhá počítá logaritmus o základu 2 podílem dvou
přirozených logaritmů. Původní soubory, autorské a licenční
komentáře byly zachovány; metadata a SHA-256 jsou v
`sources/slash-programs-manifest.json`. Překládají se nezměněné
zdrojové úseky těchto funkcí; jejich samostatné kontrolní součty
jsou také ve výsledcích.
[R8_HYPOT](https://people.math.sc.edu/Burkardt/py_src/r8lib/r8_hypot.py),
[R8_LOG_2](https://people.math.sc.edu/Burkardt/py_src/r8lib/r8_log_2.py).

Třetím programem je již existující `algorithm_s_float` v
`verify_collision_test.py`, napsaný v předchozí části auditu pro
binary64 simulaci kolizního testu. Kolize je opakované obsazení
stejné přihrádky při n nezávislých volbách z m přihrádek. Program
rekurencí počítá pravděpodobnosti a vybrané hodnoty jejich kumulativní
distribuční funkce, tedy pravděpodobnosti nepřekročení určitého
počtu kolizí. Ani tato funkce se pro slash variantu ručně nemění.

Pro každou funkci běží původní binary64 verze a dvě slash verze:
q=27 odpovídá 32bitovému uložení, q=58 uložení 64bitovému.
Při přímém srovnání stejně velkých slov je tedy relevantní q=58;
q=27 je navíc menší experimentální formát. Reference odmocnin
a logaritmů používá 100 desetinných míst v mpmath. Jde o numerickou
referenci, nikoli rigorózní intervalový důkaz posledního místa.
Pravděpodobnosti mají přesnou celočíselnou referenci z inkluze
a exkluze: pravděpodobnost právě j obsazených přihrádek je

```text
binom(m,j) * sum_{k=0}^j (-1)^k binom(j,k) (j-k)^n / m^n.
```

Tento počet je nezávislý na testované rekurenci. Z něj se přesně
sčítají potřebné koncové pravděpodobnosti.

## Co vyšlo lépe a co hůře

Pro m=10,n=2 má původní program součet 1+2^-52 a překročí poslední
práh 1. Obě slash verze dávají přesně 1 a dokončí tabulku.
Samotný správný součet však není měřítkem jednotlivých hodnot:

| Parametry kolizí | Největší absolutní chyba vypsané CDF, binary64 | q=27 | q=58 |
|---|---:|---:|---:|
| m=17,n=12 | 2.3653e-16 | 6.6051e-7 | 3.5742e-17 |
| m=64,n=25 | 4.4740e-17 | 2.9700e-7 | 1.6680e-16 |

Sloupec q=58 tedy obsahuje zlepšení i zhoršení vůči stejně velkému
binary64 slovu. Přesné chyby jsou uložené jako zlomky. Původní
práh pro zanedbání malých pravděpodobností 1e-20 se v obou slash
formátech zaokrouhlí na nulu. Zachování zdrojového programu tak
neznamená zachování původního významu jeho tolerancí.

Pro délku vektoru (3,4) dávají všechny tři verze přesně 5. Pro
(1,2^-15) vrátí obě slash verze 1, s chybou přibližně 4.6566e-10;
binary64 má v tomto případě chybu přibližně 1.0842e-19. U q=58
je poměr i jeho čtverec přesný, ale součet 1+2^-30 už zaokrouhlí
na 1 ještě před voláním odmocniny.

Pro log2(1+2^-40) vrátí obě slash verze 0, zatímco původní
program má chybu přibližně 1.1062e-28. Příčinou je už zaokrouhlení
vstupu: nad 1 je v q=58 soused (2^29-1)/(2^29-2). Jeho medián
s 1 je 1+1/(2^29-1). Vstup 1+2^-40 leží pod touto mezí,
takže se musí zaokrouhlit na 1. To vysvětluje ztrátu malého
přírůstku bez odvolání na kvalitu knihovního logaritmu.

Také rozsah je podstatně menší: délka vektoru (1e20,1e20)
má v binary64 konečný výsledek, zatímco oba slash vstupy přetečou
na nekonečno a následné inf/inf dává neurčenou hodnotu. Tyto
výsledky patří ke standardním neškálovaným formátům zadání;
nejsou tvrzením o všech rozšířených racionálních formátech.

## 16: intervaly se zaručeným obsažením

`sources/slash_intervals.py` reprezentuje interval dolním a horním
slash koncem. Konečné konce mají přesné racionální hodnoty;
nekonečna vyznačují neomezené strany. Každý přesný dolní výsledek
se zaokrouhlí na největší reprezentovatelné číslo nepřevyšující
jeho hodnotu; horní výsledek analogicky směrem nahoru. Tyto dva
konce poskytuje již dokázaná procedura `bracket`.

Součet používá součet dolních a součet horních konců. Odčítání
obrací konce druhého intervalu. Násobení vezme minimum a maximum
čtyř součinů konců; u neomezených intervalů se používají příslušné
jednostranné limity, s 0*inf=0 při výpočtu krajních hodnot.
To je konvence pro součiny množin konečných reálných hodnot,
nikoli změna pravidla 0*inf pro samostatná čísla v úloze 8.
Monotonicita součtu a bilinearita součinu dokazují, že se do takto
získaného intervalu vejdou všechny kombinace vstupních hodnot.
Následné vnější zaokrouhlení jej může pouze rozšířit.

Neobsahuje-li dělitel nulu, převrátíme jeho konce v opačném pořadí
a provedeme intervalové násobení. Obsahuje-li jeho interval nulu,
vrátí se celá reálná osa a příznak `domain_issue`. Ten výslovně
říká, že nulový dělitel není vyloučen; nejde o tvrzení, že dělení
nulou je definováno. Příznak se propaguje dalšími operacemi.
Může být konzervativní, pokud nula vstoupila do intervalu až jeho
předchozím rozšířením.

Běžné mediánové zaokrouhlení obou krajů není správné: při q=4
se přesná hodnota 1/10 zaokrouhlí na 0, takže bodový interval
[0,0] ji neobsahuje. Vnější zaokrouhlení dává správné [0,1/7].
Závislost mezi opakovanými výskyty stejné proměnné se obecně
ztrácí: pro X=[1/3,1/2] dostaneme X-X=[-1/6,1/6], přestože
matematický výraz x-x je vždy 0. To je očekávané rozšíření,
nikoli porušení záruky obsažení.

Experiment se součtem 1+1/2+...+1/100 kontroloval obsažení po
každém kroku. Šířky výsledných intervalů byly 346/21 pro q=8,
50/809627 pro q=27 a 413/27485014946238616 pro q=58.
Přesný součet je uložen ve výsledcích. Dalším experimentem byl
determinant 3x3 racionální matice z příkladu přiloženého k primární
poznámce Matuly a Kornerupa z roku 1988. Přesná hodnota 5/13 byla
ve všech intervalech obsažena; pro q=58 se výstup zúžil přesně
na [5/13,5/13]. Původní stránka příkladu je v
`images/rational-response-3.png`; tento experiment nepředstírá
úplný audit všech tabulkových hodnot jejich článku z roku 1979.

## Běhy a reprodukovatelnost

`verify_rational_compiler.py` a `results/rational-compiler.{json,log}`:
1586 kontrol operací, převodů a tisku; osm vstupů dvou Burkardtových
funkcí a tři vstupy kolizního programu, každý ve třech režimech.
Šest nepodporovaných konstrukcí bylo odmítnuto. První běh 19521
skončil exit 1 na vlastní chybě přepisu AST (`ast.Load()` místo
typu `ast.Load` v `isinstance`). Po opravě běh 58011 exit 0.
Následně doplněno samostatné měření jednotlivých CDF proti přesné
inkluzi a exkluzi; běh 93615 exit 0 přeskočil tři hotové checkpointy.
Doplnění řešilo konkrétní obavu, že správná celková hmotnost může
skrývat chyby jednotlivých pravděpodobností.

`verify_rational_intervals.py` a `results/rational-intervals.{json,log}`:
relace 2644 exit 0, dva checkpointy. Celkem 6000 intervalových
operací na 2000 dvojicích vstupních intervalů, devět kombinací
vzorků pro každou operaci; dále 17994 kontrol dělení nenulovou
hodnotou, neomezené případy, tři součtové a determinantové
experimenty. Popisek výsledku byl opraven z `nearest` na `mediant`
bez změny čísel nebo opakování úspěšných testů.

Čtyři vrstvy errat prohledány pro úlohy 15/16 a pravidla slash
aritmetiky. Nová oprava se zde nenavrhuje. Cílem úloh je
experiment; výsledek neposkytuje univerzální pořadí obou aritmetik.
