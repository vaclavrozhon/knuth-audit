# §4.5.1-10: libovolně dlouhé propojené zlomky

Zadání na str. 333 přečteno v originálu. Úloha žádá rozšířit
propojené celočíselné rutiny z §4.3.1-34 na racionální čísla;
samostatná odpověď v knize není. Dodaná implementace je
`sources/linked_rational.py`, navazující na již prověřený
`sources/linked_integer.py`. Bez nového nálezu.

## Reprezentace a vlastnictví paměti

Jeden zlomek vlastní dva oddělené propojené seznamy číslic:
podepsaný čitatel u a kladný jmenovatel a. Jejich hodnoty splňují
gcd(u,a)=1. Nula má prázdný seznam čitatele a jednociferný
jmenovatel 1. Seznam číslic, obousměrné odkazy a seznam volných
uzlů jsou definovány v [classical-linked.md](classical-linked.md).
Zde se nemění celočíselné operace ani jejich předchozí výsledky.

Všechny aritmetické operace vracejí nově vlastněné seznamy;
vstupy pouze čtou. Tentýž zlomek lze použít jako oba operandy.
Výstup uvolňuje volající pomocí `close()`. Hlavičky dočasných
celých čísel spravuje `Temps`, který uvolní všechny ponechané
objekty také při výjimce. Délky nemají pevnou číselnou mez:
omezením je pouze dostupná kapacita poolu, včetně prostoru
potřebného na mezivýsledky.

Python zde vykonává model slov a odkazů. Racionální aritmetika
nikdy neskládá celé víceslovné číslo do Python integer; používá
pouze dříve prověřené operace nad seznamy. Metody `from_ints`
a `to_pair` jsou výslovně označené vstupní/testovací adaptéry.
Nejde o tvrzení o rychlosti vůči produkční knihovně velkých čísel.

## Gcd, normalizace a čtyři operace

`gcd_linked` zkopíruje velikosti obou vstupů a opakuje dělení
se zbytkem. Pro a>=0,b>0 platí a=qb+r a 0<=r<b, takže se gcd
při nahrazení (a,b) dvojicí (b,r) nemění a druhá složka přísně
klesá. Smyčka skončí na (g,0), kde g je nezáporné gcd.
Před další iterací se podíl a nepotřebný starý dělenec uvolní;
počet současně vlastněných hlaviček zůstává konstantní.

`exact_quotient` používá běžné propojené dělení a ověřuje nulový
zbytek. Vstupní konstruktor odmítne nulový jmenovatel, vydělí
obě složky jejich gcd a převede znaménko do čitatele. Protože
jmenovatel není nulový, gcd je kladné. Důkaz jednoznačnosti
redukovaného tvaru je v [rational-basic.md](rational-basic.md).

Násobení nejprve křížem krátí gcd(u,b) a gcd(a,v), potom násobí
zmenšené složky. Dělení pro nenulové v analogicky krátí gcd(u,v)
a gcd(a,b), obrátí druhý zlomek a opraví znaménko jmenovatele.
Nulový dělitel je odmítnut před alokací. Pro sčítání/odčítání
jsou d=gcd(a,b), A=a/d, B=b/d, t=uB+/-vA, h=gcd(t,d);
výsledkem je (t/h, A*(b/h)). Všechny podíly jsou přesné a
výstupy redukované podle obecných důkazů v rational-basic.
Tyto důkazy zahrnují nulu, různé znaménkové kombinace i totožné
vstupy, takže implementace nemusí výsledek znovu normalizovat.

Porovnání použije kladné jmenovatele a porovná podepsané celé
součiny ub a va. Přetečení slova se nevyskytne: součiny dostávají
další uzly. Vyčerpání poolu se ovšem stále může ohlásit jako
`MemoryError`; požadavek na libovolnou délku není příslib nekonečné
fyzické paměti. Jedna vrstva racionálních operací drží konstantní
počet celočíselných objektů. Jejich délky a mezivýsledky jsou
lineární v součtu délek vstupních složek; čas gcd závisí na
jednotlivých Eukleidových děleních a není zde vydáván za lineární.

## Nezávislé kontroly

`verify_rational_linked.py`, `results/rational-linked.json` a `.log`:
relace 34775, PID 1093507, exit 0, všechny tři checkpointy prošly.

- 2116 úplných malých dvojic v základech 2,3,10,256; 108 větších
  dvojic až s 1024bitovými složkami, také v základu 2^32;
  92 vstupních aliasů a 272 normalizací se zápornými jmenovateli.
  Každá dvojice prošla čtyřmi operacemi a porovnáním proti
  nezávislému Python Fraction orákulu. Kontrola struktury ověřila
  oba směry odkazů, disjunktnost živých uzlů a úplnost volného seznamu.
- 251 vynucených selhání, postupně na každé alokaci jednoho
  konkrétního úspěšného běhu konstruktoru a pěti operací.
  Každé obnovilo původní živé vstupy bez úniku uzlů. Vedle toho
  ověřeno skutečné naplnění poolu a násobení v rozptýlené paměti
  s 500 ponechanými jednocifernými objekty a 86 nesousedními odkazy.
  Tato úplnost se týká všech alokací uvedených scénářů, nikoli
  všech možných velikostí a větví celého programu.
- Gaussova–Jordanova eliminace nad těmito zlomky invertovala
  Hilbertovy matice H[i,j]=1/(i+j+1), i,j=0,...,n-1, pro n=1,...,5.
  Jde o konkrétní Cauchyho matice doporučované textem. Všech 55
  výstupních prvků souhlasilo s celočíselným vzorcem pro inverzi;
  nezávislý součin původní matice s výsledkem přes Fraction byl
  jednotková matice. Největší absolutní prvek pro n=5 byl 179200.

Původní celočíselná testovací sada se neopakovala. Čtyři vrstvy
errat prohledány pro §4.5.1-10 a jeho odkaz; další oprava nenalezena.
Úloha 10 je tím dokončena jako konkrétní programovací konstrukce,
nikoli pouze návrh využít obecnou knihovnu racionálních čísel.
