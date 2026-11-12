# Souvislý průchod §3.2.1.2: násobitel a perioda

6. listopadu 2026, V2-X0087–X0088. Původní sazba str. 16–23 a
odpovědi 547–550 porovnány s úplnými poznámkami `multiplier-periods.md`
a `lagged-periods.md`. Inventář 22 úloh souhlasí. Strany 16 a 547 jsou
tím uzavřené; strany 23 a 550 obsahují další sekci a zůstávají částečné.

## Přijaté důkazy a hranice tvrzení

- Lemma P: binomické koeficienty dávají přesný zdvih valuace o 1;
  výjimka p^e=2 je správně vyloučena. Lemma Q: perioda součinu složek
  je nejmenší společný násobek, délka ocasu jejich maximum.
- Věta A a lemma R: úplný cyklus vyžaduje nesoudělný přírůstek,
  a≡1 modulo všech prvočísel modulu a modulo 4, pokud 4 dělí modul.
  Případ a=1 je oddělen, m=1 triviální; při m=2 normalizace a<m
  odstraňuje zdánlivý spor s nutností podmínky v odpovědi 2.
- Věty B a C: maximální řád, binární výjimky, zdvih lichých
  prvočíselných mocnin a spojení čínskou větou. „Primitivní“ zde
  znamená prvek nejvyššího řádu, nikoli nutně generátor celé grupy.
  Nulový počátek zůstává konstantní, vzorec φ(p^(e−f)) se používá
  pro nenulový počátek f<e.
- Věta D: pro e≥5 musí binární složka dodat faktor 2^(e−2), zatímco
  pětková dodává 5^(e−1). Znovu porovnáno všech 32 uvedených zbytků
  modulo 200 a všech 16 společně primitivních zbytků z odpovědi 17.
- Úlohy 1–8: konkrétní perioda 10^10, posun o polovinu periody,
  square-free příklady, největší možný ocas a binární dělení
  geometrického součtu. V odpovědi 6 je správně 0≤k≤8.
- Úlohy 9–18: obě afinní substituce, klasifikace λ=φ, přesné řády,
  konstrukce prvku řádu lcm, kořenová mez polynomu a existence
  primitivního kořene bez kruhového použití věty B.
- Úlohy 19–21: přijata tabulka maximálních řádů pro 92 modulů,
  redukce m′=m/gcd(A,m) a identita gcd(X_s,m)=s. Odpověď 20 má
  v originálu správně čárku u m′; nejde o chybu sazby.

Původní důkaz součinu prvků nesoudělných řádů na 549 zaměňuje
předem definované λ s řádem součinu. Oprava z roku 2005 zavádí λ′
a dokazuje obě dělitelnosti; opravuje skutečnou mezeru, nikoli novou
matematickou větu. Jde o již známé erratum.

## Uložené výpočty a certifikáty

Přečten celý `verify_multiplier_periods.py`, celý `verify_lagged_periods.py`
a celý nezávislý `verify_ecpp.py`; tabulka 30 velkých prvočísel v
`certify_lagged_primes.py` porovnána s originálem. Znovu přečteny
souhrny výsledků a poslední dokončovací řádky logu. Nic nebylo spuštěno.

U malých případů je uložených 278 784 trajektorií nezávislých na vzorcích
periody; tabulka maximálních řádů používá přesné modulární svědky a
dříve certifikované rozklady. Čtyři desetinné příklady na 550 mají
přesně periody 2494304880, 4999999500, 5000000499 a 130668528.

Pro b=2^32−5 a m=b^43−b^22+1 je rozklad m−1 úplný, s 17 různými
prvočíselnými faktory a největším o 99 cifrách. Všichni modulární
svědkové a certifikáty jsou zachováni. Důkaz pro nenulovou inicializaci
s c₀=0 správně dává 1≤X₀≤m−1; perioda výstupních cifer je stejná
jako perioda stavů, neboť rozdíl dvou periodicky posunutých stavů by
jinak musel být dělitelný libovolnou mocninou b.

Nezávislá ECPP validace skutečně kontroluje nesingularitu křivky,
inverzibilitu jmenovatelů, nenulový bod řádu q a celočíselnou dostatečnou
mez q>(ceil(N^(1/4))+1)^2. Rekurze končí Lucasovými certifikáty,
ne pravděpodobnostním predikátem. Hasseova věta je použitý známý základ,
nikoli zde nově dokázaný výsledek. Uložený výstup dokládá všech 31 cílů
a 17 faktorů, 2870 článků a 237 koncových certifikátů. Starý návrat
tool session 143 není vydáván za exit 0; přijat je dokončený výstup
a log ve spojení s kontrolou kódu a uloženými certifikáty.

Neprovádí se nová faktorizace m−1 pro všech 30 velkých modulů.
Text ji neuvádí a jeho doporučení o míchání a pravděpodobnosti 1/q
jsou heuristická: 1/q je přesné pro rovnoměrný prvek cyklické grupy,
nikoli dokázaná distribuce pevně svázaných parametrů b a m.
Narozeninový test a Lüscherovo ředění budou hodnoceny v jejich sekcích.
Zde se netvrdí prokázaná statistická kvalita všech parametrů.

## Errata, fakta a bibliografie

Prohledány všechny čtyři aktuálně potvrzené řady errat. **X0088**
mapuje původní strany 17 (Greenberger 163–167), 18 (chybějící
„period of“), 20 (kladný exponent a prvočíselnost p), 548 (order,
nikoli period), 549 (opravený důkaz úlohy 15) a 550 (jazyková oprava).
Pouhé typografické změny ani přidané odkazy nejsou nové nálezy.

Znovu přečtena věta 1 na 233 v archivovaném primárním článku
Hulla–Dobella: tři postačující podmínky odpovídají popisu na 17.
Uložená metadata vydavatele Greenbergerova článku potvrzují JACM 8(2),
163–167. Jeho úplný článek a historické prvenství zůstávají přeskočeny.
Totéž platí pro přesné odstavce Gaussovy knihy a dodanou Lagrangeovu
historickou citaci. Marsaglia–Zaman mají ověřená metadata 1(3),462–480,
ale konkrétní text 474–475 nebyl nově dostupný; číselný výsledek zde
dokládají vlastní certifikáty, nikoli tvrzení o přečteném článku.

Nová chyba v tomto bloku nepotvrzena. Další kurzor: §3.2.1.3 od 23.
