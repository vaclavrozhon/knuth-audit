# V2-C0241: možné příliš široké tvrzení za polovinou periody

**Candidate, nízká závažnost**, 6. listopadu 2026. Původní strana 570,
odpověď §3.3.2–31, odstavec těsně nad grafem. Nejde o závadu hlavního
79bitového výpočtu ani o chybný obrázek.

Text popisuje vymizení převahy jedniček kolem poloviny periody 2047
a říká, že pak jsou pravděpodobnější nuly, s výjimkou zmínky o celé
periodě. Doslovné tvrzení pro všechny délky mezi polovinou a koncem
neplatí. Zůstává však nejisté, zda autor zamýšlel takové tvrzení,
nebo jen hrubý popis velké střední části grafu. Samotný obrázek
návrat nad 1/2 u pravého konce ukazuje. Proto zatím **nepotvrzujeme
novou chybu**, pouze uchováváme přesný interpretační kandidát.

Pro maximální binární rekurenci stupně k≥2 je N=2^k−1. Součet znamének
Z=2Y−1 v celé periodě je 1. Okno délky N−2 vynechá dvě sousední
znaménka, takže jeho součet je 1−Z_a−Z_(a+1). Je záporný právě
tehdy, když oba vynechané bity jsou 1. Dvě různé výstupní lineární
formy jsou nezávislé nad F_2; vzor 11 se objeví přesně 2^(k−2)krát
mezi N nenulovými stavy. Tedy

    Pr(S_(N−2)>0)=(3·2^(k−2)−1)/(2^k−1).

Pro knižní k=11 a délku 2045 to je 1535/2047≈0.74988, tedy výrazná
převaha jedniček, přestože ještě nejde o celou periodu. Dříve uložený
úplný výčet 2047 fází pro všechny délky dává stejný počet 1535.
Žádný výčet znovu spuštěn: nová kontrola porovnává obecný dvoubitový
důkaz s příslušným uloženým řádkem. Další příklady jsou uloženy
v `results/sequential-walk-endpoint.json`.

Původní strana 570 i rekonstruovaný obrázek byly nově vizuálně
porovnány. Čtyři vrstvy errat a aktuální TeX znovu prohledány
6. listopadu; známá oprava 570 se týká pouze roku Szekeresova článku.
Oprava tohoto odstavce nenalezena. Čerstvé zdrojové otisky jsou
v `sources/sequential-2026-11-06/errata-manifest.json`.

Možné zpřesnění textu: nuly převažují ve velké části druhé poloviny
periody, ale blízko jejího konce se převaha jedniček vrací. Před
případným uzavřením nálezu posoudit výslovnou výjimku celé periody
i původní graf. Poslední fyzický dotisk a prvenství neověřeny.
