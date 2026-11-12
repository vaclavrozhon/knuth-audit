# Mersennova prvočísla: seznam, záznamy objevů a úloha 16

> Sekvenční doplnění6.11.2026: úloha16 je nyní partial, protože výzkumná otázka není vyřešena; starší checked níže znamenalo pouze tehdejší rešerši.

Rozsah: §4.5.4, kontext na str. 409, seznam (26), navazující
historické aktualizace errat a výzkumná úloha 16 na 413.
M_p=2^p−1 označuje **Mersennovo číslo**; Mersennovo prvočíslo je
takové M_p, které je prvočíslem. Nutná prvočíselnost exponentu p
neznamená automaticky prvočíselnost M_p.

Věta L a obecné Lucasovy posloupnosti jsou již uzavřeny v
[primality-lucas.md](primality-lucas.md). Tento blok jejich
výpočty neopakuje. Starší historie před rokem 1979 na 407–408
a odstavec o anonymním autorovi na 412 nejsou uzavřeny tímto
záznamem.

## 1. Co bylo skutečně ověřeno

Původních 36 exponentů na 409 a dalších 11 v all2-prepre souhlasí
s aktuálními záznamy GIMPS. Pět dalších dodatků přivádí seznam
na 52 hodnot, pokud se opraví C0163 níže. U všech 52 exponentů
byla prvočíselnost dokázána přímým dělením do odmocniny.
To je důkaz pro p, **nikoli pro celé M_p**.

Všech 52 uváděných počtů číslic bylo nezávisle ověřeno přesnými
racionálními intervaly pro log_10(2), tedy logaritmus 2 o základu
10. Používáme vztah

    počet číslic M_p = floor(p*log_10(2))+1.

Pro p>0 jsou 2^p a mocniny 10 celá čísla. Je-li
10^d<2^p<10^(d+1), odečtení 1 stále ponechá alespoň 10^d.
Proto počet číslic M_p odpovídá tomuto vzorci; není nutné
ukládat celé největší číslo.

Přesné meze se získají ze vzorce

    log((1+t)/(1−t)) = 2*sum_(j>=0) t^(2j+1)/(2j+1), 0<t<1.

Po m členech je kladný zbytek nejvýše
2*t^(2m+1)/((2m+1)*(1−t²)). Pro t=1/3 dostaneme přirozený
logaritmus 2, pro t=2/3 logaritmus 5. Součet těchto dvou
logaritmů je logaritmus 10. Intervalový podíl při m=64
má šířku menší než 10^(−23); oba konce dávají stejnou
celočíselnou část pro všech 52 exponentů. Prvních 23 počtů,
do p=11213, navíc souhlasí s přímým převodem celého M_p do
desítkové soustavy.

Příklady relevantní pro text a errata:

| Exponent p | Počet číslic M_p |
|---:|---:|
| 1257787 | 378632 |
| 2976221 | 895932 |
| 57885161 | 17425170 |
| 74207281 | 22338618 |
| 77232917 | 23249425 |
| 82589933 | 24862048 |
| 136279841 | 41024320 |

Malá Mersennova prvočísla do p=11213 již mají vlastní dvojí
ověření z předchozího bloku. U větších čísel je zde ověřena
shoda s primárními záznamy a rozsah jejich externí certifikace,
nikoli nový místní výpočet všech milionů čtvercování.
Například GIMPS u M77232917 uvádí nezávislé ověření programy
Prime95, gpuOwL, CUDALucas a Mlucas. U M136279841 odlišuje
první pravděpodobnostní test z 11. října 2024 od důkazu
Lucasovým–Lehmerovým testem z 12. října a dalších kontrol
na CPU i GPU, dokončených do 19. října.

Samotné tvrzení o složenosti M8191 lze doložit bez historického
svědectví: vlastní dělitel je 338193759479. Přímé dělení
(2^8191−1) tímto číslem i dvě modulární metody dávají nulový
zbytek. Prvočíselnost dělitele k tomuto důkazu není potřeba.
Prvočíslo 8191 tedy opravdu nemůže být přidáno do seznamu (26).

## 2. C0163: složený exponent přidaný erratem z roku 2019

Na str. 11 dokumentu all2-pre.pdf, v dodatku z 24. dubna 2019
ke str. 409, je vizuálně přečteno 77232017. Správná hodnota je
77232917. Nejde o OCR omyl: nula je v původní sazbě PDF.

Chybná hodnota dokonce není prvočíslem:

    77232017 = 19 * 29 * 140167 = 19 * 4064843.

Pro kladná a,b platí 2^(ab)−1=(2^a−1)*sum_(j=0)^(b−1) 2^(aj).
Proto M77232017 má vlastní dělitel 2^19−1=524287 a nemůže být
Mersennovým prvočíslem. Dělitelnost byla zkontrolována i
přímým modulárním mocněním. Opravený exponent potvrzuje
[oficiální zpráva GIMPS](https://www.mersenne.org/primes/?press=M77232917)
o objevu Jonathana Pace z 26. prosince 2017, zveřejněná
3. ledna 2018. Žádná další vrstva našich errat tuto číslici
neopravuje.

## 3. C0162: rok prvočíselnosti M216091

Sken str. 409 tvrdí, že M216091 bylo prokázáno prvočíslem
v roce 1984. [Dobová zpráva SGI/Cray z 3. září 1996,
uchovaná Landonem Curtem Nollem](https://www.isthe.com/chongo/tech/math/prime/prime_press.html)
uvádí u tohoto Slowinského rekordu rok 1985. Stejný rok
má aktuální primární tabulka GIMPS. Oprava je **1984→1985**.

Přesný zářijový den se mezi katalogy rozchází; nález jej
nepředepisuje a opírá se jen o shodný rok. Údaje 1983 pro
M132049 a 1988 pro M110503 jsou v souladu s těmito záznamy.
Rok 1984 nebyl opraven v žádné ze čtyř vrstev errat ani
v aktuálním TeXu. Novější fyzický výtisk neověřen.

## 4. Objev versus oznámení: M1257787 není další potvrzená chyba

Současná tabulka GIMPS uvádí u M1257787 datum 3. září 1996,
zatímco kniha mluví o počátečním ověření 12. dubna 1996.
[Woltmanův vlastní newsletter č. 6](https://www.mersenne.org/newsletters/?id=6)
z 3. září výslovně říká, že objev nastal začátkem dubna a jeho
zveřejnění bylo na Slowinského žádost odloženo. Woltman dostal
žádost o nezávislé ověření 15. dubna. Rozdíl duben/září je tedy
vysvětlen, nikoli nález chyby v knize.

Přesný den 12. dubna tento newsletter nezávisle nedokládá,
ale nevyvrací jej. Čas kolem 6 hodin uvedený v primárních
zprávách neodporuje knižní horní mezi 8.3 hodiny.
Pro M2976221 potvrzuje [newsletter č. 12](https://www.mersenne.org/newsletters/?id=12)
srpen 1997, 15 dnů na 100MHz Pentiu i následné ověření
Slowinským. Knižní údaj necelých 900000 číslic souhlasí
s přesnými 895932.

## 5. C0164: datum M42643801 zůstává sporné

All2-prepre, str. 24, tiskne u Strindmova objevu
**12 April 2009**. Aktuální [tabulka GIMPS](https://www.mersenne.org/primes/)
a jeho [milníky](https://www.mersenne.org/report_milestones/)
mají 4. června 2009. Avšak samotná
[oficiální tisková zpráva](https://www.mersenne.org/primes/?press=M42643801)
má v záhlaví také 12. dubna, přestože v jejím těle stojí
první nezávislé ověření 12. června. Starší zpráva GIMPS
o M77232917 opakuje měsíc duben.

Proto je tento bod **candidate**, nikoli confirmed. Dubnové
datum není pouhý výmysl Knuthova textu. Je třeba odlišit
případný původní výpočet, zjištění výsledku, ověření a
zveřejnění, nebo doložit chybu v původní tiskové zprávě.
Z dnešního katalogu samotného by byla definitivní oprava
na 4. června předčasná. Sazba errata byla zobrazena;
žádné opravné erratum nalezeno nebylo.

## 6. Historická úplnost a aktuální stav

[Newsletter č. 11 z 26. května 1997](https://www.mersenne.org/newsletters/?id=11)
potvrzuje otestování všech exponentů pod milionem. Šlo
o první průchod, nikoli již o dvojí kontrolu celého rozsahu:
aktuální historické milníky datují její dokončení na
30. října 1997. Kniha pouze říká, že exponenty byly zkontrolovány;
nedělá z toho tvrzení o dvou kontrolách.

Snapshot milníků z 3. listopadu 2026, aktualizovaný zdrojem
v 18:30 UTC, uvádí:

- všechny exponenty pod 83708267 byly otestovány a ověřeny;
- pod 142651277 proběhl alespoň jeden test;
- M82589933 má od 4. září 2026 potvrzené pořadí 51;
- největší známé M136279841 je v tabulce stále označeno
  hvězdičkou u pořadí 52: potenciálně menší neodhalený člen
  není totéž jako pochybnost o prvočíselnosti tohoto čísla.

Dodatek z května 2026 o kontrole exponentů pod 80 miliony
odpovídá milníku z 9. února 2026. Přesnou historickou hranici
70832851 uvedenou pro 10. prosinec 2024 zde nelze vyvodit
jen ze současných milníků: uvádějí 71 milionů k 12. prosinci.
Není nalezen rozpor, ale přesný prosincový mezistav nebyl
nezávisle rekonstruován.

Úprava z prosince 2024 s „next 17“ sedí na 17 exponentů
od M1398269 do M82589933 a následující Durantův rekord.
Jeho primární zpráva dokládá infrastrukturu ve 17 zemích
a více než 41 milionů číslic. Obecné dějiny projektu,
Woltmanův začátek roku 1996 a podíl Gage na třech záznamech
z 90. let souhlasí s dobovými zprávami.

## 7. Výzkumná úloha 16

Otázka, zda existuje nekonečně mnoho Mersennových prvočísel,
zůstává otevřeným výzkumným problémem. Carl Pomerance ji
výslovně označuje jako nevyřešenou v úvodu primárního článku
[Cyclotomic primes](https://math.dartmouth.edu/~carlp/cyclotomicprimesjrev.pdf),
publikovaného v J. Number Theory 276 (2025), 198–208.
Přečtena a zobrazena první strana autorské verze s datem
3. listopadu 2024; zbytek článku zde není označován za auditovaný.
Aktuální záznamy GIMPS dokládají konečný počet 52 známých příkladů.

Jednotlivé neověřené internetové preprinty tvrdící vyřešení
nejsou samy důvodem měnit stav této otázky. Nebyl nalezen
přijatý důkaz infinitudy ani konečnosti. „Checked“ u úlohy 16
znamená audit jejího znění a současného výzkumného stavu,
**nikoli vyřešení otázky**. Žádný konečný seznam ani ověření
velkého intervalu nedokazují nekonečnost.

## 8. Reprodukce a omezení

verify_mersenne_context.py má limit 60 s a skončil s exit 0.
Výsledky obsahují přesné logaritmické intervaly, 52 kontrol
exponentů a číslic, 23 přímých převodů a dva krátké doklady
složenosti. Starší úspěšné Lucasovy výpočty se neopakovaly.

Stažené primární HTML odpovědi jsou beze změny uloženy gzipem;
metadata obsahují hash původní odpovědi i komprimovaného
souboru. Seznam 52 řádků byl extrahován z tohoto snapshotu.
Všechny čtyři vrstvy errat a aktuální TeX byly prohledány.
C0162 a C0163 jsou confirmed v našich podkladech, C0164
zůstává candidate. Priorita a pozdější fyzické výtisky
neověřeny. Nic neodesláno.
