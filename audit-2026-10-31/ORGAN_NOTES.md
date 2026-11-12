# Varhany, 7.2.2–79

Kontrola 1. listopadu 2026, zadání str.63, odpovědi 414–415.
`check_organ.py` počítá přesně celé vytvářející polynomy P, S, G a Q,
včetně všech 160 příspěvků P_k/S_k/G_k. Nezávislý model vychází pouze
z booleovských pravidel zadání. Výsledek: F099 ve vzorci h a F100
v počtu Q_811; ostatní uvedené koeficienty a části (a–f) souhlasí.

## Nezávislý výpočet bez knižních vytvářejících funkcí

Při pevném nastavení rejstříků nezávisí různé tóny manuálů na sobě.
Každý místní výstupní vzor označíme množinou nastavení rejstříků, která
jej umějí vytvořit. Celý zvuk je hratelný právě tehdy, když průnik
těchto množin přes všechny tóny není prázdný. Stav dynamického programu
je tento průnik, nikoli počet realizací vstupů. Každý odlišný zvuk tak
projde právě jednou; více kombinací kláves/rejstříků se nesčítá opakovaně.

Pedál se rozpadá podle tónu modulo 12: osm řetězců tří kláves a čtyři
řetězce dvou kláves. Pro každé z 32 nastavení se místní vzory přímo
vypočítají pro všech 8 či 4 vstupů. Vznikne 191 a 85 různých vzorů,
nejvýše 44 dosažitelných průnikových stavů. Manuály mají skupiny
12 dolních a 44 horních tónů. Swell potřebuje nejvýše 79 stavů, Great 60.

Výsledný průnik navíc určuje nejmenší nastavení k, a tím přesně kanonický
příspěvek P_k/S_k/G_k definovaný v knize. Každý celý polynom byl porovnán
s odpovídajícím vzorcem. Shoda platí po jediné změně závorky v h.
Finální konvoluce dává všech 813 koeficientů Q. Nejde o aproximaci ani
o vyčíslení několika prvních členů. Jsou uloženy v `results/organ/verified.json`.

## F099: −1 patří za celý součin

Správně má být

    h(w,z) = (1+3wz²+2w²z³+w²z⁴+w³z⁴)^8
             (1+2wz²+w²z³)^4 − 1.

V knize je odečet 1 uvnitř závorky za druhým faktorem. To vyřazuje i
všechny neprázdné zvuky, které používají jen prvních osm tónových tříd.

Nejkratší svědek: k=11 znamená c0=c1=c15=1, c2=c16=0.
Každý z 32 jednotlivých pedálů vytvoří jiný třípíšťalový zvuk
{(0,j),(1,j),(0,j+12)}. Žádné menší nastavení rejstříků jej neumí:
potřebujeme oba nezávislé rejstříky a oktávové rozšíření. Koeficient
[z³]P_11 má proto být 32; tisk h(z,z) dává pouze 8.

Při třech klávesách jedné tónové třídy má 8 vstupů velikosti
0,3,3,3,5,5,6,7. Při dvou klávesách jsou to 0,3,3,5.
Prázdný zvuk se odečítá až po vynásobení všech dvanácti tříd.
Pro obecnou větev h je nepřekrývající se rejstřík zároveň svědkem
stisknutých kláves; pro P_31 plní tuto roli c2, a dvě překrývající se
řady dávají substituci h(z,z²).

Ve větvi q se lokální sjednocení sousedních kláves deduplikuje:
na tříklávesovém řetězci má sedm vzorů váhy 0,2,2,2,3,3,4,
na dvouklávesovém čtyři vzory 0,2,2,3. Zvuky dosažitelné dřívějším
čistým nebo čistě posunutým rejstříkem se odečtou inkluzí–exkluzí,
což dává přesně uvedený q. Zbylé případy bez překryvu jsou prosté
binomické mocniny. Tím je doložen i obecný původ všech větví P_k.

Správné P_3=22848 je už v knize; chybný vzorec by dal 22704.
Také uvedené P_10=324113168 a všechny Q_1,...,Q_10 jsou správně.
F099 je chyba vzorce, nikoli těchto číselných výsledků.

## F100: Q_811 je 8, nikoli 12

Když mlčí právě jedna píšťala, všechny pedálové rejstříky musí být
zapnuté: vypnutí kteréhokoli odstraní nejméně 12 píšťal. Z ranku 2
vidíme, že je vypnut právě jeden pedál p_j. Při všech ostatních vstupech
1 mlčí pouze (2,j) právě tehdy, když 12≤j<20. Pro j<12 by mlčely i
(0,j),(1,j); pro j≥20 mlčí také (0,j+12),(1,j+12), protože p_(j+12)
už je mimo rozsah 0,...,31.

Konkrétně p_20=0 vypne (2,20), (0,32), (1,32). Knižní interval
12≤j<24 tedy zahrnuje čtyři neplatné příklady; správný je 12≤j<20.
Na Swell ani Great jediná chybějící píšťala nevznikne: každý nezbytný
vypnutý rejstřík odstraní nejméně 44 píšťal, každý vypnutý tón při
plné registraci odstraní nejméně čtyři, respektive šest.

Tento důkaz potvrzuje nezávislý přímý test všech 812 možností, která
píšťala chybí. Pro každé nastavení rejstříků vezmeme všechny klávesy,
jejichž zvuk je podmnožinou cílového zvuku. Jejich sjednocení je díky
monotonicitě největší možný přípustný výstup; cílový zvuk je dosažitelný
právě při rovnosti. Oracle nepoužívá vytvářející funkce.

Také již správně vytištěný člen P_119=8 spolu se stupni P=120,
S=312, G=380 vyžaduje Q_811=8. Opravit je třeba část (g) a závěrečný
člen 12z^811 v části (h); jde o jeden společný nález F100.

## Ostatní části a primární zdroj

Doslovná pravidla dávají přesně 812 možných píšťal, 700 hratelných
singletonů a všech 256 dvojic z (e) přesně podle knižní podmínky.
Oba pětipíšťalové příklady i osmičlenný příklad v zadání byly přímo
vypočteny. Monotonicita plyne z užití pouze AND/OR s nezápornými
literály. Spojky lze odstranit nahrazením vstupů s,g za s*,g*;
výstupy tím zůstanou totožné, což bylo navíc zkoušeno na 1000 případech.
Nezávislost tří divizí pak dokazuje Q=P S G.

Pro manuály je po zvolení nejmenšího nastavení buď třeba alespoň jeden
libovolný tón (f), nebo alespoň jeden horní tón (g); dolní tóny jsou
nezávislé. Zvláštní S_32 správně vynechává 12 němých dolních kláves;
G_k s c13=c14=1 správně nic nového nepřidává.
Souhlasí i S_n>G_n pro 1≤n≤107; pro n=108 už je nerovnost obrácená,
a všech devět zaokrouhlených poměrů vůči binomickým koeficientům.

[Knuthův vlastní popis varhan](https://cs.stanford.edu/~knuth/organ.html)
potvrzuje 16 řad, 812 píšťal a jejich rozdělení 120/312/380, rozsahy
a sdílené basové píšťaly. Hratelnost zde znamená přesně booleovský
model zadání, bez omezení počtu rukou nebo dostupného vzduchu.

Zobrazeny strany 63, 414, 415 a autorův PS `fasc5b` str.53.
Historická oprava Fascicle 5 p.223 z 9. dubna 2020 mění z²z⁴ na w²z⁴;
naše 4B ji obsahuje. Neopravuje závorku ani Q_811. Všechny prověřené
vrstvy jsou v `results/connected/errata-check.json`.
Návrhy F099/F100 jsou ASCII, neposlané, bez kontroly fyzického výtisku.
