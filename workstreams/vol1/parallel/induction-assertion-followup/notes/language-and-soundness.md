# Skutečný nástroj pro §1.2.1, úlohu 14

`assertion_tool.py` přijímá program jako konečný graf příkazů a volitelné
aserce, tedy tvrzení o hodnotách proměnných v určitých bodech programu.
Chybějící aserce doplňuje symbolickým provedením všech cest mezi zadanými
body. Symbolické provedení počítá s výrazy místo konkrétních čísel.
Výsledek popisuje přesně stavy dosažitelné z některé dodané aserce; tento
relativní význam je definován v oddílu 3.

Nástroj skutečně přijímá různé programy, nikoli jen parametry Euclidova
algoritmu. Nehledá libovolné invarianty cyklů. U cyklu, který neprochází
žádnou dodanou asercí, oznámí chybějící aserci a nevydá neúplný výčet
za platný výsledek. Oddělená kontrola ověřuje návaznost dodaných tvrzení
a bezpečnost operací. Ukončení běhů nekontroluje.

## 1. Jazyk a přesný kontrakt

Stav je funkce přiřazující každé deklarované proměnné celé číslo.
Používáme neomezená matematická celá čísla, nikoli strojovou aritmetiku.
Všechny proměnné mají hodnotu už při vstupu; neuvedené hodnoty jsou
libovolné, nejsou skrytě nastavené na nulu. Případné vstupní omezení
určuje aserce u vstupního uzlu. Bez ní je předpodmínkou `True`.

Vstupní JSON obsahuje `variables`, `nodes`, `entry`, `exits`, `edges`
a volitelně `assertions`, `name`, `description`. Uzel označuje místo
mezi příkazy. Hrana má `from`, `to`, volitelný `guard` a seznam
`commands`. Chybějící podmínka hrany znamená `True`, chybějící seznam
příkazů znamená prázdný seznam. Podmínka se vyhodnocuje před příkazy
hrany. Z povolených hran se může vybrat kterákoli; jejich podmínky
se smějí překrývat. Mimo výstup musí být v každém dosažitelném stavu
povolena alespoň jedna hrana. Tuto podmínku nástroj zvlášť ověřuje.
Do vstupu nesmí vést hrana a z výstupů nesmějí vést hrany.

Proměnné a uzly mají různé ASCII identifikátory ve svých seznamech.
Jména proměnných nesmějí být klíčovými slovy Pythonu nebo rezervovanými
symboly SMT-LIB uvedenými v `RESERVED_VARIABLES`. Druhé omezení je
nutné pro znovunačtení exportovaných formulí. Interní symboly obsahují
`@`, které vstupní identifikátor nemůže obsahovat. Opakovaný klíč JSON
se odmítá; parser tedy tiše neztratí první ze dvou přiřazení.

Výrazy dovolují celočíselné a booleovské konstanty, proměnné, závorky,
unární `+`, `-`, `not`, operace `+`, `-`, `*`, mocninu s doslovným
exponentem 0 až 8, celočíselná porovnání `==`, `!=`, `<`, `<=`, `>`,
`>=`, jejich řetězení a spojky `and`, `or`. Dále jsou dovoleny `abs(x)`
a `gcd(x,y)`. `gcd` znamená nezáporný největší společný dělitel;
zejména `gcd(0,0)=0`. Aritmetika s booleovskou hodnotou se odmítá.
Obecné volání funkcí, seznamy, atributy, dělení uvnitř výrazu, reálná
čísla a nepovolené syntaktické konstrukce nejsou součástí jazyka.
Zdrojové výrazy se analyzují pomocí AST, nikoli `eval` nebo `exec`.

Příkazy jsou:

| Příkaz | Význam |
| --- | --- |
| `assign`: `target`, `expr` | Pravá strana se vyhodnotí v aktuálním stavu a zapíše do cíle. |
| `parallel`: `updates` | Všechny pravé strany se vyhodnotí v témže starém stavu, pak se současně zapíší. |
| `havoc`: `target` | Cíl dostane libovolné celé číslo; správnost musí platit pro všechny volby. |
| `divmod`: `dividend`, `divisor`, `quotient`, `remainder` | Oba vstupy se vyhodnotí ve starém stavu. Pro kladný dělitel se současně zapíše podíl a nezáporný zbytek. Dva výstupy musejí být různé; smějí se shodovat se vstupními proměnnými. |

Seznam příkazů na hraně je vždy sekvenční. `divmod` pro dělitel `d > 0`
a dělenec `c` znamená jedinou dvojici celých `q,r` splňující
`c = q*d+r` a `0 <= r < d`; je definován i pro záporné `c`.
Pro `d <= 0` jde o chybu běhu, nikoli o větev, kterou smíme vynechat.

Praktické syntaktické meze jsou 1 000 uzlů, 1 000 proměnných,
5 000 hran, 1 000 příkazů na hraně a omezená velikost výrazu.
Samostatný limit počtu rozpracovaných symbolických stavů zabraňuje
neomezenému větvení v běžném použití. Není to polynomiální algoritmus:
počet cest mezi asercemi může být exponenciální a výrazy mohou růst.

## 2. Význam výstupů a ověřování

**Řezový bod** je uzel s dodanou asercí; vstup je řezovým bodem vždy.
Odstraníme-li všechny řezové body, zbytek grafu musí být acyklický.
Není-li, nástroj vrátí konkrétní cyklus v diagnostice
`missing_cycle_assertion`. Jde o dostatečný předpoklad naší metody,
nikoli nutnou podmínku ověřitelnosti programu. I nedosažitelný cyklus
bez aserce může vést k této konzervativní odpovědi.

Z každého řezového bodu se nezávisle zahájí symbolický běh ve všech
stavech splňujících jeho dodanou aserci. Při dosažení dalšího řezového
bodu se cesta ukončí a vznikne povinnost dokázat jeho aserci.
Před každým rozvětvením vzniká povinnost pokrytí hran. Před každým
dělením vzniká povinnost kladnosti dělitele. Příkazy přiřazení a volby
jsou v uvedeném jazyce vždy definované.

Nástroj používá Z3 5.3.3. U každé povinnosti hledá model její negace:

- `unsat` znamená `proved`: protipříklad v použité teorii neexistuje;
- `sat` znamená pouze `unproved_model`: jde o model místní povinnosti,
  který nemusí být dosažitelný od skutečného vstupu;
- `unknown` zůstává `unknown`, včetně vyčerpání zdrojů či času;
- `--infer-only` povinnosti nevykoná a neosvědčí správnost.

Navíc je `gcd` v řešiči neinterpretovaná funkce, tedy funkce, které
řešič obecně neurčuje matematický význam. Přidáváme jen konkrétní
platné identity u provedeného dělení, dokázané v oddílu 4. Množina
abstraktních modelů tak zahrnuje skutečné celočíselné stavy. Výsledek
`unsat` je dostačující; model `sat` může mít nesprávnou abstraktní
hodnotu `gcd` a sám o sobě není protipříkladem programu.

`inference_complete` znamená, že byly zpracovány všechny cesty
mezi řezovými body. Samo toto pole neříká, že uživatelovy aserce platí.
`partial_correctness_and_safety_verified` je pravdivé jen při úplném
odvození a úspěchu všech povinností. Znamená: každý konečný dosažitelný
běh ze vstupní předpodmínky splňuje doplněné a dodané aserce, nezůstane
zablokován mimo výstup a nepoužije nedovolené dělení. Dosáhne-li
výstupu s dodanou asercí, splňuje ji. **Neznamená, že výstupu dosáhne.**
Pole `termination` proto vždy obsahuje `not_checked`.

Po vyčerpání počtu stavů je odvození neúplné a všechna pole
`filled_assertion_smt2` jsou `null`. Dílčí cesty zůstávají diagnostikou,
nesmějí se použít jako invariant celého programu. Totéž platí při
nepokrytém cyklu. U úplné analýzy jsou výstupní aserce matematicky
podmíněné správností dodaných řezových tvrzení, dokud nejsou povinnosti
ověřeny. Na tuto podmíněnost výstup výslovně upozorňuje.

## 3. Důkaz přesnosti odvození a zvukovosti osvědčení

Pro cestu `pi` z řezového bodu `s` do uzlu `v`, která nemá vnitřní
řezový bod, označme `R_pi` její relaci vstupních a výstupních stavů.
Dvojice patří do relace právě tehdy, když lze celou cestu provést:
všechny podmínky hran platí, příkazy jsou definované a volby `havoc`
mají nějaké hodnoty. Označme `A_s` množinu stavů splňujících dodanou
aserci u `s`. **Nejsilnější postpodmínka** této cesty je obraz

```text
SP(pi,A_s) = { y : existuje x v A_s takové, že (x,y) patří do R_pi }.
```

Je nejsilnější ve významu logické implikace: každé jiné tvrzení pravdivé
pro všechny výstupy této cesty platí pro tuto množinu. Není to tvrzení,
že všechny stavy `A_s` jsou dosažitelné ze vstupu celého programu.

Symbolický případ ukládá výrazy pro aktuální hodnoty proměnných,
podmínku cesty, čerstvé vstupní symboly a čerstvé hodnoty voleb
a dělení. Pro aktuální stav `y` vytiskne formuli

```text
existují vstupní a čerstvé symboly:
    podmínka cesty AND pro každou proměnnou v: y[v] = její výraz.
```

**Lemma o jedné cestě.** Tato formule vyjadřuje přesně `SP(pi,A_s)`
při matematické interpretaci `gcd`.

Důkaz je indukcí podle příkazů. Na začátku jsou vstupní symboly
libovolným stavem splňujícím `A_s`. Podmínka hrany jen omezí stavy,
ve kterých se hrana smí vykonat. Sekvenční přiřazení nahradí výraz
jedné proměnné jeho pravou stranou vyhodnocenou v aktuálních výrazech;
ostatní výrazy ponechá. U současného přiřazení se všechny pravé strany
spočítají před aktualizací slovníku. `havoc` zavede nový nezávislý
celý symbol, takže pokrývá právě všechny povolené volby. `divmod`
zavede `q,r` s přesnou definující rovnicí a mezemi; ty při `d > 0`
charakterizují jediný skutečný výsledek. Obecné identity gcd jsou podle
oddílu 4 redundantní. Výstupní existenciální kvantifikace odstraní
paměť minulých hodnot a ponechá právě dosažitelné aktuální stavy.
Tento argument platí v obou směrech, nikoli pouze jako aproximace.

**Lemma o úplném výčtu.** Acykličnost mimo řezové body zaručuje konečně
mnoho cest bez vnitřního řezového bodu. Fronta v `infer` prochází každou
z nich, bez testu dosažitelnosti a bez vyřazení větve podle odhadu.
I neproveditelná cesta může být ve výstupu; její podmínka je nepravdivá,
a proto nepřidává žádný stav. Dosáhne-li výpočet konce bez limitu,
disjunkce případů u `v` je přesně sjednocení všech `SP(pi,A_s)`.
Prázdné sjednocení je `False`. U vstupu nejsou příchozí cesty;
jeho dodaná předpodmínka se tím nenahrazuje.

**Věta o zvukovosti.** Jestliže jsou všechny vydané povinnosti platné
a výčet je úplný, jsou všechny doplněné aserce pravdivé na dosažitelných
stavech a program má výše uvedenou částečnou správnost a bezpečnost.

Důkaz: Vstupní stav splňuje vstupní řezovou aserci předpokladem.
Každý konečný úsek do následujícího řezového bodu odpovídá jednomu
vyčtenému případu. Lemma o jedné cestě dává správnou aserci v každém
vnitřním bodě. Povinnost při příchodu do řezového bodu zaručuje jeho
dodanou aserci, a indukce tedy může pokračovat dalším úsekem.
Povinnosti pokrytí a kladnosti dělitelů zaručují, že žádný konečný
dosažitelný prefix neselže uvedeným způsobem. Každý konečný prefix
nekonečného běhu má stejné zdůvodnění; nic z toho nevynucuje ukončení.
Při ověření přes Z3 používáme navíc předpoklad správnosti jeho odpovědí
`unsat` a správnosti překladu a implementace. Exportované povinnosti
umožňují audit, nejsou však formální certifikáty z nezávislého jádra.

## 4. Obecné věty pro dělení a gcd

Nechť `c,q,r` jsou celá čísla, `d > 0` a `c = q*d+r`.
Každý kladný společný dělitel `c,d` dělí také `r = c-q*d`.
Naopak každý kladný společný dělitel `d,r` dělí `c = q*d+r`.
Obě dvojice mají tedy stejnou množinu kladných společných dělitelů,
a tudíž `gcd(c,d) = gcd(d,r)`. Pro `r = 0` je tento gcd roven `d`.
K důkazu identity není potřeba nezápornost `c`, ani meze zbytku;
ty patří definici příkazu a zajišťují jednoznačnost výsledku.

Právě tyto dvě obecné identity přidává obsluha každého `divmod`.
Nezná jména uzlů, název programu ani Euclidovy koeficienty.
Vypnutí pomocí `--no-gcd-lemmas` vede u správného Euclida ke čtyřem
neprokázaným místním povinnostem, protože libovolná abstraktní funkce
nemusí tyto identity splňovat. To dokládá rozdíl mezi neúplnou teorií
řešiče a chybou vstupního programu.

## 5. Praktické meze

Metoda neobjevuje nové řezové invarianty, neověřuje terminaci,
nezahrnuje pole, haldu, procedury, vstup a výstup, strojové přetečení
ani libovolné knihovní operace. Výstupní nejsilnější postpodmínky
mohou obsahovat existenciální kvantifikátory. Vstupní jazyk asercí je
užší a neumožňuje každou výstupní formuli znovu zapsat do vstupního JSON;
úplný výstup je ve standardním SMT-LIB. Nelineární celočíselná
aritmetika obecně nemá úplný rozhodovací postup a řešič může vrátit
`unknown`. Tyto meze nebrání tomu, aby program skutečně plnil omezenou,
užitečnou verzi zadání „attempts to fill in“ a konkrétní cíl Algorithm E.

Dokumentace použitého řešiče byla ověřena v jeho primárních zdrojích:
[aritmetika Z3](https://microsoft.github.io/z3guide/docs/theories/Arithmetic/)
a [kvantifikátory Z3](https://microsoft.github.io/z3guide/docs/logic/Quantifiers/).
Čtecím rozsahem jsou popis celočíselné/nelineární aritmetiky a meze
rozhodování, respektive úvod o neúplnosti obecné podpory kvantifikátorů;
nejde o audit implementace řešiče. Verze a hash lokálního balíku jsou
v `sources/z3-dependency.json`.
