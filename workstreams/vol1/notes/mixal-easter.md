# §1.3.2-14–15: velikonoční program a jeho perioda

Stav 1. listopadu 2026. Zadání s.159–160, odpovědi s.516–518,
první dotisk třetího vydání; originální stránky zobrazeny. Technická
kontrola je oddělena od historie výpočtu Velikonoc na s.518.
`mixal_easter.py` obsahuje přepis programu a vlastní úplný program
pro úlohu15. `check_mixal_easter.py` porovnává strojový výsledek,
nezávislý výpočet absolutního dne a dvě enumerace periody.

## Značení a kalendářní pravidlo

Y je rok, G=Y mod19+1 jeho zlaté číslo, C=floor(Y/100)+1,
X=floor(3C/4)−12 a Z=floor((8C+5)/25)−5. Modulo zde vždy vrací
nezáporný zbytek. Označme E0=(11G+20+Z−X) mod30. Upravený epakt E
vznikne zvýšením E0 o1 právě pro E0=24 nebo E0=25 a G>11.
Číslo N označuje den od počátku března, takže duben d má N=31+d.
Nejprve N=44−E, případně N+30, aby21<=N<=50. To je tabulkový
velikonoční úplněk, nikoli nutně astronomický úplněk.

Položme D=floor(5Y/4)−X−10. Číslo (D+N) mod7 je den týdne
březnového dne N, s nedělí0. Důkaz: pro c=floor(Y/100) platí
floor(3(c+1)/4)=c−floor(c/4), tedy

```
D = Y + floor(Y/4) − floor(Y/100) + floor(Y/400) + 2.
```

Absolutní číslo dne před1.březnem je
365Y−306+floor(Y/4)−floor(Y/100)+floor(Y/400), počítáme-li1.leden1
jako pondělí s číslem1. Rozdíl od D je násobek7. Krok E7 proto
přičítá7−((D+N) mod7), nejmenší kladný posun na neděli.
Výsledek leží mezi22.březnem a25.dubnem, včetně.

Nezávislý pramen: N. Dershowitz a E. M. Reingold, *Calendrical
Calculations*, Software—Practice and Experience20(9),1990,899–928,
s.904–906 a919–920. Jejich `shifted-epact` je (E0+6) mod30.
Zvýšení pro shifted=0 nebo shifted=1 a Y mod19>10 přesně odpovídá
výjimkám E0=24,25. Odečtení upraveného shifted od19.dubna dává
stejný N. Jejich `Kday-on-or-before(moon+7,0)` dává následující
neděli. Jde tedy i o algebraickou shodu, nejen test několika let.
Čtený rozsah a originály jsou evidovány v metadatech zdroje.

## Násobení místo dělení v MIX

B=b^5 je velikost strojového slova,64<=b<=100. Výraz a//d v MIXAL
je floor(aB/d). Násobení nezáporného V konstantou floor(aB/d)+1
vrací v rA celé číslo floor(aV/d+Vδ/B), kde0<δ<=1. Jestliže dV<B,
není dodatek schopen překročit další celočíselnou hranici: zlomek
části aV/d má jmenovatel d a Vδ/B<1/d. Výsledek je floor(aV/d).
To zahrnuje i případ, kdy aV/d už celé je.

V programu potřebujeme (a,d)=(1,100),(3,4),(8,25),(1,4).
Pro dělení roku V<=99999; v prostředních dvou případech V=C+60<=1060.
Všechny nerovnosti dV<64^5 platí. Tím je tvrzení o všech velikostech
bajtu a celém rozsahu1583<=Y<100000 dokázáno bez enumerace každého
strojového běhu.

Po prvním násobení a INCA61 je rA=C+60. Další násobení dává
floor(3(C+60)/4)=X+57. Násobení C+60 hodnotou8//25+1 vrací Z+24.
Výpočet přes rI1=G a rI2 postupně tvoří2G,4G,5G,10G,11G+773.
Instrukce XPLUS57 následně vytvoří

```
11G + 20 + Z − X + 720.
```

Číslo je kladné v zadaném rozsahu; hrubá mez X<=738,Z>=0,G>=1
už dává alespoň13. Přesnější minimum není pro správnost nutné.
Adresní konstanty jsou nejvýše1060 a mezivýsledek rI2 nejvýše982,
takže se vejdou i do nejmenšího indexového registru b²=4096.
Přičtení720 je násobek30 a zajišťuje, že DIV počítá nezáporný epakt.

## Větve úplňku a neděle

Po DIV30 má rX=E0. Větve DECX/JXN/JXP/J1NP společně vrací
rX=20−N, kde N je tabulkový úplněk:

- E0<24: rX=E0−24;
- E0>=26: rX=E0−54;
- E0=24: N=49 a rX=−29;
- E0=25,G<=11: N=49 a rX=−29;
- E0=25,G>11: N=48 a rX=−28.

STX(0:2) přenese i znaménko do adresní části ENN1, takže rI1=N−20.
Po násobení Y hodnotou1//4+1, přičtení Y a odečtení X+57 je
rA=D−47. INCA67,1 vytvoří D+N; DIV7 vrátí zbytek r.
SLAX5 a DECA−4,1 vytvoří31−Nfinal, kde Nfinal=N+7−r.
Záporné rA tedy rozpozná duben a CHAR převede jeho velikost na den
v dubnu. Pro březen DECA31 udělá −Nfinal, CHAR opět převede velikost.
CHAR nepoužívá znaménko; nejde o zapomenutou změnu znaménka.

JBUS čeká před všemi změnami výstupního bloku. Měsíc v rA a den
v rX přežijí čekání; po zápisu se rok zvlášť převede CHAR a vytiskne.
Počáteční STJ zachová návrat do řídicího programu. Další volání přes
EASTER+1 toto místo nepřepisují. rI6 od−50 do0 dává roky1950–2000
včetně, tedy51 řádků; podprogram rI6 nemění.

## Úloha15: první špatný rok

Chybná varianta používá u záporného raw=11G+20+Z−X zbytek se
znaménkem dividendu. Pouhá zápornost raw ještě neznamená chybný den.
Položme h(C)=27+floor((8C+5)/25)−floor(3C/4), takže raw=11G+h(C).
Pro C<=98 máme h(C)>26.2−0.43C>=−15.94, tedy h(C)>=−15.
Pro C=99,100,101 je h(C)=−16. Do konce roku10099 je proto
raw>=−5; při záporném raw musí G=1. Pro raw=−1,...,−5 vedou
správný i chybný epakt ke stejnému úplňku44−raw. Výjimka E0=25
se pro G=1 neuplatní.

Pro C=102,103 je h(C)=−17. Nové případy mají G=1,raw=−6,
a nastávají přesně v letech10108+19k,0<=k<=10. Správný úplněk je
N=49, chybný N=50. Neděle po nich by se lišily jen tehdy, kdyby
N=50 samo bylo nedělí. Zbytky (D+50) mod7 jsou v uvedeném pořadí
4,6,2,5,1,2,5,1,4,6,2: žádný není0.

Pro C=104 dostáváme h(C)=−18. První G=1 nastane roku10317;
raw=−7. D=12820, správný epakt23 dává úplněk21.března a neděli
25.března. Chybný epakt−7 dává úplněk N=51 a výsledek N=53,
tedy22.dubna. Rok10317 je proto skutečně první chybný rok.
Příklad14250 dává správně14.dubna, chybně42.dubna, jak kniha uvádí.

`search_program()` je úplné vlastní MIX řešení: od roku1583 volá
stejné aritmetické jádro dvakrát. Přepsáním konstanty EPBASE na773
nebo53 zapíná či vypíná přídavek720. Jádro vrací31−Nfinal;
řídicí program porovná výsledky, zvětšuje rok uložený v paměti
(a nikoli v příliš malém indexovém registru) a první rozdíl vytiskne.
To je doplnění řešení úlohy, nikoli vydávání vlastního programu za
kód z knihy. Ve zkoumaném rozsahu do10317 je správná varianta
z předchozího důkazu platná.

## Přesná perioda5700000

P=5700000. Posun Y o P ponechá G, zvýší C o57000, X o42750,
Z o18240; raw se změní o−24510=−817·30. D se zvýší
od floor(5Y/4) o7125000 a po odečtení změny X celkem o7082250,
což je7·1011750. Epakt, výjimka i neděle se tedy opakují pro
každý rok. Toto tvrzení je o matematickém algoritmu bez horní
meze roku, nikoli o omezeném MIX podprogramu.

P má prvočíselné dělitele2,3,5,19. Každá vlastní perioda konečné
kruhové posloupnosti délky P by způsobila i periodu P/p pro některý
z těchto prvočinitelů. Formálně lze vzít gcd(P,q) libovolné další
periody q a pak její násobek P/p. Na jednostranné posloupnosti je
stejný argument platný, protože každou fázi lze posunout o P do
jejího definičního oboru. Rok1583 má N=41. Posuny P/2,P/3,P/5,P/19
mají postupně N=27,48,55,34. Každý se liší, takže P je nejmenší
kladná perioda.

## Proč jsou všechny četnosti dělitelné25

V jednom celém cyklu dovolme formálně roky0<=Y<P; díky periodicitě
má libovolný cyklus začínající po1582 stejné četnosti. Pišme
Y=100c+y,0<=y<100, c=100k+s,0<=s<100,0<=k<570.
Pro pevná s,y platí

```
G−1 = (6k+5s+y) mod19,
E0  = (11G+27+floor((8s+13)/25)−floor(3(s+1)/4)−43k) mod30.
```

Zobrazení k na dvojici(6k mod19,−43k mod30) je bijekce z570 hodnot
na19·30 dvojic: násobení6 modulo19 a−43 modulo30 je invertibilní
a moduly19,30 jsou nesoudělné. Pro každé pevné s,y tedy všechny
dvojice G=1,...,19 a E0=0,...,29 nastávají právě jednou.

Den týdne závisí z c pouze na t=c mod4=s mod4. Skutečně
D=125c+floor(5y/4)−floor(3(c+1)/4)+2 a pro c=4a+t je koeficient
a roven497=71·7. Zbývá

```
D mod7 = (125t−floor(3(t+1)/4)+floor(5y/4)+2) mod7.
```

Každé t=0,1,2,3 má mezi s=0,...,99 přesně25 výskytů; pro každý
z nich už jsou všechny dvojice(G,E0) rovnoměrné. Celá četnostní
tabulka je proto25krát tabulka pro4·100·19·30=228000 čtveřic
(t,y,G,E0). To dokazuje dělitelnost, nikoli pouze její pozorování
na výsledku enumerace. Checker tuto menší enumeraci porovnává s
přímým průchodem5700000 let a s nezávislým absolutním kalendářem.
Ověřené četnosti jsou:22.března27550,19.dubna220400,
25.dubna42000; druhý den je nejčastější, první a třetí dva nejméně časté.

## Errata a dosud oddělený historický rozsah

Prohledány všechny čtyři vrstvy `all1-prepre`, `all1-pre`, `all1`,
`err1` podle stran160,516,518 i hesel Easter,Victorius,Wermuth:

-10.března2002: závorky a slovosled poznámky k neděli v E4;
-31.srpna1998: oznámení Wermuthovy úspory9,10 nebo12u, bez kódu;
-10.ledna2003: odkaz na druhé vydání Calendrical Calculations(2001);
-27.srpna2014: Aquitania → Aquitaine;
-18.ledna2025: doplněn Neri–Schneider, SPE53(2023),937–970.

Oznámená Wermuthova optimalizace nemá dostupný kód v erratu; úloha
nevyžaduje důkaz globální optimality a správnost tištěného programu
na tom nezávisí. Historická tvrzení o prvenství Victoriova algoritmu
a o jediné netriviální aplikaci aritmetiky ve středověké Evropě
zatím nejsou tímto technickým důkazem ověřena. Rovněž atribuční
údaje O'Beirne/Hill vyžadují oddělené prameny; vlastní důkaz periody
a četností jejich přijetí nepředpokládá.

Kontrola skončila úspěšně:11405398 tvrzení,4477 jednotlivých běhů
podprogramu,4 celé tabulky a2 úplná strojová hledání. Celý cyklus
5700000 let byl porovnán s druhým kalendářem a menší228000-prvkovou
enumerací. Výsledek v `results/mixal-easter.json`; neopakovat bez
změny nebo konkrétní pochybnosti. Historický stav nyní upřesňuje
`mixal-easter-sources.md`, včetně C0025 a otevřeného C0026.
