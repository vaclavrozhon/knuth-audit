# §1.2.1-15: dobrá uspořádání a význam explicitní definice

Kořenová revize 2. listopadu 2026, V1-X0718. Celé matematické cvičení
15 je checked s výslovnou kvalifikací neformální poznámky části (c).
Nevzniká nový nález. Knižní slovo „explicit“ nemá určený formální
význam; níže uvedené čtení není vydáváno za jediný autorův úmysl.

Root ověřil 51 souborů, 6681534 bajtů, a 16 read-only vstupů balíku
`parallel/well-ordering-followup/`. SHA-256 MANIFEST.json je
`ccf04f2167e34e688de4361b85195882f1f7e33779fb5b5fc71c13f8b656f67a`.
Přečetl celé předání a obě poznámky. Obrazově četl knižní 20/469,
Gödelovy 221/223, Fefermanovy 325 a §4 na 340–342 včetně celého
důkazu 4.11, a Kanoveiho–Lyubetského 1–4 v rozsahu věty 1.1(I)
a celého jejího Cohenova důkazu. Širší agentova četba Gödelových
220–224 je doložena jeho protokolem. Úspěšné testy se neopakovaly.

## Přijaté čtení

Dobré uspořádání je úplné uspořádání, v němž má každá neprázdná
podmnožina nejmenší prvek. ZF je Zermelova–Fraenkelova teorie množin,
AC axiom výběru a ZFC jejich spojení. Formule bez parametrů je zde
konečný výraz množinového jazyka se dvěma volnými proměnnými pro
dva porovnávané prvky, bez další předem dodané množiny.

ZFC dokazuje existenci dobrého uspořádání reálných. Z poznámky však
přijímáme pouze přesnější požadavek: nalézt jednu takovou formuli,
o níž samotné ZFC dokazuje, že dobře uspořádává všechna reálná čísla.
Při konzistenci ZF to podle Fefermanovy věty 4.11 nelze. Na 342 autor
výslovně formuluje konzistenci ZFC, dokonce i se zobecněnou hypotézou
kontinua, spolu se schématem, že žádná jednotlivá bezparametrická
formule dobré uspořádání kontinua neurčuje. Nejde o popření existence
uspořádání v takovém modelu; AC ji zaručuje.

Root sledoval konkrétní spor důkazu: ze sjednocení tříd posloupností,
které se liší od jednotlivých generických řádků jen konečně mnoha
bity, se definovaným uspořádáním vybere nejmenší prvek. Změna jednoho
dosud neurčeného bitu zachová tuto množinu i formuli uspořádání,
ale změní vybraný prvek. Vzniknou dva různé nejmenší prvky. Používají
se publikované pomocné věty o forcingu, tedy metodě stavby modelů;
zde nejsou znovu kompletně dokazovány. Předpoklad konzistence je
přímo vysloven i v úvodu na 325.

## Proč Gödel není protipříklad k tomuto čtení

Konstruktibilní univerzum L se tvoří po ordinálních stupních, v nichž
se přidávají podmnožiny definovatelné nad předchozím stupněm. Ordinál
je možný pořadový typ dobrého uspořádání. Gödel na 221 uvádí
definovatelné dobré uspořádání konstruktibilních množin a na 223
odvozuje AC za předpokladu, že jsou všechny množiny konstruktibilní,
dnes V=L. Jeho předpis bez tohoto dodatečného předpokladu nemusí
pokrýt všechna reálná čísla. Zakazovat definovatelné uspořádání
ve všech modelech a za všech dalších axiomů by tedy bylo chybné.

OD znamená definovatelnost s konečně mnoha ordinálními parametry.
Samostatná novější věta Kanoveie–Lyubetského 1.1(I) říká, že každá
spočetná OD množina binárních posloupností v Cohenově rozšíření
patří původnímu modelu. Kdyby rozšíření L[a] mělo OD dobré uspořádání
všech posloupností, ordinální pozice by z každé posloupnosti udělala
OD prvek. Její singleton by patřil L, tedy i ona. To odporuje nové
posloupnosti a. Jde o dodatečnou oporu pro ordinální parametry,
nikoli důsledek bezparametrické Fefermanovy formulace. S reálným
parametrem a naopak relativizovaná Gödelova konstrukce v L[a]
uspořádání poskytuje. Libovolné množinové parametry by umožnily
použít samo uspořádání jako parametr, což je ještě jiný požadavek.

## Rozsah uzavření

Dřívější obecné důkazy částí (a)–(g) z `notes/induction.md`, §6,
zůstávají přijaty; u (f) se zachovává použití závislých voleb.
Knižní obvyklé číselné uspořádání nezáporných reálných není dobré,
protože kladná reálná nemají nejmenší prvek.

Neformální poznámka je tím posouzena za uvedeného obhajitelného
čtení. Není certifikováno doslovné historické „nobody has yet“
ani určena autorova nevyjádřená definice explicitnosti. Nedokládáme
tím algoritmickou rozhodnutelnost relace ani celý základ teorie
forcingu. Tyto meze jsou součástí závěru, nikoli skrytým tvrzením
o nezávisle prověřené univerzální historii. Všechny čtyři vrstvy
errat a současný TeX byly v předání porovnány; známá oprava 15(e)
zůstává oddělená a změna poznámky 15(c) nalezena nebyla.
