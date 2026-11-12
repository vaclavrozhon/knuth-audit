# §3.1-23: Foatovo–Fuchsovo kódování funkcí

Kontrola 1. listopadu 2026. [Zadání na str. 9](../images/vol2-p009.png)
a [odpověď na str. 543](../images/vol2-p543.png) souhlasí s následujícím
kódováním i jeho inverzí. Oba desetiprvkové příklady také souhlasí.
Relevantní vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2`, `err2.textxt`
neobsahují nalezenou opravu této odpovědi.

## Konstrukce kódu

Nechť `f` je funkce na označených vrcholech `0,...,m-1`, kde `m>=1`.
Cyklický vrchol leží na orientovaném cyklu grafu šipek `v -> f(v)`.
Ostatní vrcholy tvoří stromy orientované k těmto cyklům. List zde znamená
vrchol, do něhož nevede žádná šipka; množina listů je doplněk obrazu `f`.

Na cyklických vrcholech je `f` permutací. Vezmeme její **inverzní**
permutaci a zapíšeme každý cyklus počínaje jeho nejmenším prvkem.
Cykly uspořádáme sestupně podle jejich minim a odstraníme závorky.
To je „unusual correspondence“ ze svazku 1, §1.3.3. Získaná posloupnost
je počáteční část kódu; označme její délku `k` a její prvky za navštívené.

Nyní procházíme listy ve vzestupném pořadí. Z listu `l` jdeme po šipkách
`f` až do prvního již navštíveného vrcholu `a`. Všechny nově prošlé
vrcholy označíme za navštívené. Cestu zapíšeme obráceně, od `a` směrem
k `l`, ale samotný list `l` vynecháme; tento zápis připojíme ke kódu.

Každý necyklický vrchol leží nad nějakým listem, a proto bude navštíven.
Přidaná část každé cesty má tolik prvků, kolik nových vrcholů cesta
obsahovala. Celý kód tak má přesně `m` pozic. Navíc každý nový vrchol
přidá do kódu právě svého rodiče, tedy svůj obraz pod `f`. Cyklická část
již obsahuje obrazy všech cyklických vrcholů. To dokazuje vlastnost (i):
kód a seznam hodnot funkce mají stejnou multimnožinu prvků, včetně násobností.

## Inverze

Z libovolné posloupnosti délky `m` nad `0,...,m-1` vezmeme nejdelší
počáteční úsek s různými prvky; jeho délku označme `k`. Tento úsek
rozdělíme při každém novém minimu zleva. V každém bloku nastavíme
obraz každého prvku na jeho předchůdce v bloku, s cyklickým návratem.
Tím obnovíme cykly `f` z kanonického zápisu její inverze.

Zbývající část čteme zleva doprava. Každá pozice určuje rodiče nového
vrcholu. Pokud další položka ještě nebyla nikde přečtena, je jménem
tohoto vrcholu. Jinak jde o dosud nepojmenovaný list, jehož rodiče si
poznamenáme; poslední pozice rovněž určuje rodiče nepojmenovaného listu.
Po skončení přiřadíme nepoužitá jména vzestupně nepojmenovaným listům
v pořadí jejich vzniku.

Každý nový pojmenovaný vrchol má rodiče mezi již známými vrcholy;
nepojmenované listy připojujeme až na konci. Nevznikne tedy žádný další
cyklus. Počet nepojmenovaných listů se rovná počtu jmen chybějících
v posloupnosti, takže přiřazení je úplné. Jednotlivé úseky mezi návraty
k již známému jménu jsou právě obrácené cesty z konstrukce kódu.
Vzestupné označení listů obnovuje pořadí jejich procházení. Oba postupy
jsou proto vzájemně inverzní, což dokazuje (ii) a zároveň bijekci všech
`m^m` funkcí se všemi `m^m` posloupnostmi.

## Zbývající vlastnosti

První připojená cesta začíná v cyklickém vrcholu, tedy opakuje položku
počáteční části. Proto je tato část přesně nejdelším počátečním úsekem
různých prvků, jak vyžaduje (iii). U permutace zaujímá celý kód.

Nový prvek uvnitř cyklického bloku má za obraz předchozí prvek bloku,
protože byl použit cyklus inverzní permutace. Výjimkou je jeho nejmenší
prvek, kterým blok začíná. Nový prvek v připojené cestě má také za obraz
předchozí prvek; to je přímo směr obrácené cesty. Tím je ověřeno (iv).

Funkce je permutací právě tehdy, když jsou všechny vrcholy cyklické:
kód je potom přesně kanonickým zápisem její inverze. Opačně kód bez
opakování nemá žádné připojené stromy. To dokazuje (v).

Pro `m>=2` platí `x_0=x_1` právě tehdy, když `k=1`. Jediný cyklický
vrchol je pak pevný bod a všechny ostatní vrcholy tvoří strom k němu.
Po vynechání prvního znaku dostáváme právě kód stromu z úlohy svazku 1
§2.3.4.4-18, který připojuje stejné obrácené cesty od listů.
To je vlastnost (vi). Pro `m=1` existuje jediná funkce i kód; výraz
`x_1` z (vi) se v tomto triviálním případě nepoužívá.

## Příklady a nezávislé kontroly

```text
f = (3,1,4,1,5,9,2,6,5,4)
code(f) = (4,9,5,1,1,3,4,2,6,5).

code = (3,1,4,1,5,9,2,6,5,4)
decode(code) = (6,4,9,3,1,1,2,5,4,5).
```

[verify_intro_extra.py](../verify_intro_extra.py) používá oddělené
funkce `encode` a `decode`. Pro všech 50 069 funkcí s `1<=m<=6` ověřil
inverzi, jedinečnost kódu, shodu multimnožin, počáteční cyklickou část
a vlastnosti (iv), (vi). Permutační případ (v) plyne i přímo z kódu
kanonické počáteční části. Výsledek: [intro-extra.json](../results/intro-extra.json).

Tato konečná kontrola je doplněk uvedeného obecného důkazu, nikoli
náhrada za něj. Původní článek je v odpovědi citován jako zdroj bijekce;
její správnost jsme zde prověřili vlastní konstrukcí a inverzí.
