# scan_const — přesný kontrakt ztracených celočíselných číslic

7. listopadu 2026, před cílenou reprodukcí. Jde o doprovodný program,
nikoli o chybu správné knižní definice floating formátu nebo zjištění
vyvozené jen z obecného odkazu na IEEE.

`mmix-arith-20131017.w` a `mmix-arith-20250620.w` mají celý oddíl
Floating point input conversion byteově stejný. Řádky1309–1337
definují floating magnitude jako digit string následovaný exponentem
nebo decimal string s volitelným exponentem; počet číslic není omezen
na769. Funkce má vrátit odpovídající floating hodnotu a pozici prvního
nezkonzumovaného znaku. Řádky1381–1395 výslovně vyžadují správné
výsledky i pro dlouhé rozhodující desetinné rozvoje. Přiznaná výjimka
se týká miliardy nebo více **leading zeros**, nikoli769 nul za
prvním nenulovým celým číslem. Přiznaná nepřesnost `exceptions`
(známá oprava2002) je nezávislá na hodnotě `val`.

Přesný první svědek je řetězec `"1" + "0"*769 + "e-769"`.
Má775 znaků, žádné leading zeros, validní floating syntax a přesnou
hodnotu10^769·10^−769=1. Očekávané octabyte je #3ff0000000000000;
nárok není závislý na tie ani na volbě režimu. Volání přímo do
scan_const je jeho deklarované veřejné rozhraní; žádný hypotetický
assemblerový line buffer ani OS filename limit se sem nepřidává.

Buffer je `buf+8` až `buf+777`, tedy769 číslic. Po načtení celého
770místného mantisového řetězce stojí q na buf+777 a obsahuje1
následované768 nulami. Poslední nulová číslice se zahodí a q se již
nezvýší. Při exponentu se dec_pt nastaví na q a exp na−769.
Hodnota implicitně předaná konverznímu jádru je tedy
10^768·10^−769=1/10. Čítač či kompenzace ztraceného celočíselného
místa v původním kódu není. `next_char` přitom spotřebuje všech775
znaků a návratový typ je1.

Celá rodina je `±1` následované768+k nulami, pak `e-(768+k)`;
pro každé1≤k≤231 je matematický výsledek±1, zatímco původní kód
normalizuje±10^−k. Záporné znaménko se aplikuje až ve fpack a
nedodá ztracený faktor10^k. Varianta s tečkou před exponentem
vede na stejný dec_pt. Všechny tyto vstupy mají nejvýše1007
znaků a explicitní exponent má absolutní hodnotu nejvýše999.

Tento rozbor zatím nezavírá celou korektnost print_float/scan_const,
monotonicitu ani širší IEEE decimal rozhraní. Před confirmed je nutné
zobrazit původní sazbu, dokončit sémantickou kontrolu všech errata
vrstev a provést jediný krátký běh s přesnými kontrolami hranice.

Dokončení: originál byl zobrazen,13 vrstev prošlo sémantickou kontrolou
a jediný první běh je uložen. Finální důkaz, omezený rozsah opravy
a přesné výsledky jsou `notes/MMIX-S0009-scan-constant-integer-length.md`.
