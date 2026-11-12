# Učení krátké DNF — SAT 53–61

Kontrola 31. 10. 2026. Primární místa: tabulka 2 na str. 199, rovnice (27)
na str. 198, zadání na str. 321 a odpovědi na str. 557–559.

## F057: pravděpodobnost ve druhém příkladu odpovědi 60

V příkladu se 64 trénovacími body má být **402/2^11 ≈ .196**, nikoli
404/2^11 ≈ .197. Funkce v (27) je

    f = !x2 !x3 !x10 OR !x6 !x10 !x12
        OR x8 !x13 !x15 OR !x8 x10 !x12.

Druhá odhadnutá funkce v odpovědi 60 je

    h = x2 !x13 !x15 x19 OR !x3 !x9 !x19 !x20
        OR !x6 !x10 !x12 OR !x8 x10 !x12.

Obě dohromady závisí na 11 proměnných. Úplný výčet dává 402 rozdílných
hodnot z 2048. Nezávislá inkluze a exkluze na sjednoceních termů dává

    Pr(f=1) = 113/256,
    Pr(h=1) = 11/32,
    Pr(f=h=1) = 603/2048,
    Pr(f XOR h) = 113/256 + 11/32 - 2*603/2048 = 402/2048.

Vizuálně ověřeno ve 4B str. 559 i původním autorově PS, str. 195,
23. září 2015. V all4b ani all4f6 odpovídající oprava nenalezena.
První příklad odpovědi 60 je správně: 102752/2^18.
Fyzický výtisk dosud neověřen. Návrh zprávy je uložen zvlášť.

## Co bylo ověřeno bez nalezení chyby

- Všech 32 dvacetibitových slov tabulky 2 vzniká z po sobě jdoucích bitů
  π/4 a e/4. Prvních 40 řádků v obou sloupcích bylo vypočteno při přesnosti
  250 a 400 desetinných míst; výsledky souhlasí.
- Výběr pěti souřadnic: všech 15504 možností přímo a nezávisle celý
  covering polynom přes podmnožinovou transformaci. Přesně 12 vytištěných
  pětic, správné koeficienty i počet 75 proměnných, 396 klauzulí a délka 2894.
- Všech dvanáct částečných tabulek v odpovědi 57, včetně pořadí čtení
  dvou sloupců shora dolů. Výraz desáté tabulky skutečně používá šest
  binárních operací, jestliže XNOR počítáme jako jednu. Minimum šesti
  operací netvrdíme ani nehledáme; zadání žádá pouze příklad.
- Všechny vytištěné DNF v 54, 55, (27), (32) a Morgensternův příklad
  byly vyhodnoceny přímo na odpovídajících datech.
- SAT 54: maximálně 16, 20 a 28 řádků pro 3, 4 a 5 termů.
  Na hranici existují přímo ověření svědci; další řádek má UNSAT certifikát.
- SAT 55: žádná monotonně rostoucí DNF s nejvýše čtyřmi termy; UNSAT
  certifikát. Vytištěný monotonně klesající čtyřtermový příklad sedí.
- SAT 59: rozdíl (27) a (32) má přesně 7 hodnot z 256; uvedený vzorec sedí.
- SAT 61: (27) má právě jednu reprezentaci s nejvýše čtyřmi termy až na
  pořadí termů. Nezávislý výčet všech 3^8 kostek našel 1065 implikantů,
  včetně neprvoimplikantů. Jejich pokrytí 113 kladných bodů nejvýše čtyřmi
  kostkami po zákazu původní čtveřice je UNSAT, s certifikátem.
  Z toho plyne i tvrzení pro všech 20 proměnných: projekce každého termu
  na osm relevantních souřadnic je implikantem f. Musí dát původní čtyři
  termy. Každý má soukromý kladný bod, a proto nemůže být zúžen žádnou
  z dvanácti irelevantních proměnných. Všechny jejich hodnoty musí pokrýt
  právě tento jediný term. Blokování 24 permutací je tedy v tomto příkladu
  dostatečné. Obecný XOR test v odpovědi je také správně.

## Certifikáty a meze kontroly

`check_learning_dnf.py` kóduje přítomnost kladných a záporných literálů,
přesné hodnoty termů na kladných bodech a neplatnost na záporných bodech.
Nekonzistentní nebo prázdně pokrývající term může být nahrazen kopií
užitečného termu, protože kladná data jsou neprázdná. Požadavek užitečnosti
všech termů je tedy bez újmy na obecnosti. Lexikografické seřazení jejich
vektorů na kladných bodech odstraňuje pouze permutační symetrii.

Kódování bylo nezávisle srovnáno s výčtem všech ternárních kostek a přesným
set-cover DP: 488 trénovacích množin, 1366 SAT dotazů. SAT modely jsou
ověřeny přímým dosazením do dat. UNSAT doklady z Glucose4 ověřil DRAT-trim;
v repozitáři jsou CNF, DRAT, protokoly i SHA-256.

Nástroje jsou v izolovaném `/tmp/knuth-audit-sat-venv`, python-sat 1.9.dev17.
DRAT-trim: https://github.com/marijnheule/drat-trim, commit
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, přeložen z C zdroje.
Externí checker potvrzuje logickou nemožnost CNF; její vztah k DNF vychází
z výše uvedeného důkazu a nezávislé validace. Časy ani počty mems původních
Knuthových solverů nereprodukujeme. Náhodná data jeho trénovacích experimentů
nejsou k dispozici, ověřeny jsou uvedené funkce a pravděpodobnosti.

## C011: rozsah faktoru v odpovědi 58

Text má faktor (3/4)^N. Pro jediný term to souhlasí; pro celou tabulku
2MN parametrů jde o (3/4)^(MN), protože 4^(MN) voleb přejde na 3^(MN).
Příkladem je M=2,N=1: 16 voleb přejde na 9. Po započtení trénovacích
klauzulí navíc poměr zbývajících modelů obecně není žádná taková pevná mocnina.
Znění potvrzuje PDF str. 558 i PS str. 194. Vedeme jako kandidáta na
upřesnění „per term“, ne jako potvrzenou matematickou chybu, protože věta
může implicitně hovořit o možnostech jednoho termu z předchozí věty.

## Vlastní chyby při auditu

První parser tabulek 57 četl dva sloupce po řádcích. Kniha je čísluje po
sloupcích; parser byl opraven, žádná chyba knihy v tabulkách není.
Původní assertion u druhého příkladu 60 převzal číslo 404 z knihy a selhal.
Po vizuální kontrole všech literálů byl výsledek 402 potvrzen samostatnou
metodou, nikoli pouhou změnou očekávané hodnoty.

Skripty: `check_learning_table.py`, `check_learning_dnf.py`,
`check_learning_extras.py`. Výsledky: `results/learning_table*.json`
a `results/learning_dnf/`.
