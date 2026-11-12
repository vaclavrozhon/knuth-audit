# Úplný zdrojový průchod úlohami 180–188

Kontrola 3. listopadu 2026. Celé zadání str. 147, odpovědi str. 468
a pokračování 188 na str. 469 porovnány s autorovým draftem str. 83,
172–173. Knižní PDF má posun +20, draft +6. Navazující definice
a formule (74)–(85) přečteny v kontextu.

Úlohy 180–183 a 186–188 mají dokončený průchod. 184–185 jsou partial
pouze kvůli nízkému kandidátu [C038](C038_EMPTY_SIZE_SCOPE.md) na
výslovné vyloučení nulových rozměrů. Pro kladné rozměry matematika
souhlasí. U 183 dokončený průchod znamená ověření formulace a mezí,
nikoli vyřešení otevřené výzkumné otázky.

## Rozsah nových kontrol

Přijímáme bez opakování `results/doomsday.json` a
`results/extreme_cover.json`: 32 192 strict matic / 50 674 MRV voleb,
1162 předepsaných počtů, 5296 rozkladů, 30 smíšených modelů, šest
rodin čtyřcyklů, koeficienty a aktualizace do n=80. Jejich přesné
rozsahy a obecné důkazy zůstávají v `EXACT_COVER_NOTES.md` a
`EXTREME_COVER_NOTES.md`.

Nově `check_extreme180_188_sources.py` přímo dekóduje celý obrázek 182:
16 uzlů, 15 hran a 69 buněk matic na verzi. Kontroluje každý vytištěný
přechod, nikoli další výčet řešení. Také dekóduje všech 21 čísel
trojúhelníku 188 a kontroluje jeho sčítací vztahy. Obě verze souhlasí.
Vytištěné konstanty 181, součet 10 000 v 184 a obě řady příkladů 186
se porovnají s již přijatými hodnotami; staré programy se nespouštějí.

Samostatný `certify_original181.py` doplňuje nový obecný certifikát
pro původní číselnou rekurenci. Dosavadní obecný certifikát se týkal
opravené rekurence F017. Jde o krátké celé počty, nikoli hledání
přesných pokrytí. Žádný nový solver ani dlouhý běh; vše pod nice 15.

## 180: publikované schodiště a dřívější F018

E090 je známá náhrada zadání z 15. 2. 2026. Opravuje index dalších
možností na o_(t′+q) a podmínku výskytu na q<t+r−t′. Naše PDF i
draft stále mají staré p+q a nesprávné minus před r. Přijatý důkaz
a výčet již pracovaly se správným publikovaným zněním.

Krátká indukce: nejkratší možnost s právě t průniky je singleton,
jinak by její položky měly shodné sloupce. Při pokračování prefixu
přibývá alespoň jeden nový prvek a další protínající možnost.
Rovnost v minimálním počtu průniků nutí jediný nový prvek, jinak
by nové sloupce byly stejné. Tak vznikají prefixy i1…ip a zvenku
jejich suffixy; to dává přesně opravenou podmínku.

F018 se týká jiného místa: odpověď nejprve omezuje výskyty i2 na
o2,o3,o4,o5, ale pak ho znovu přidá do o6. Vynechání i2 v o6 je
stále nutné, publikované erratum zadání ho neopravuje. Starý krátký
strict příklad i původní karta zůstávají beze změny. Autorův
[původní článek z 10. 1. 2008](https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html)
obsahuje příslušnou strukturální analýzu a čtyřcyklový příklad.

## 181: původní konstanty opravdu řeší původní rekurenci

Vytištěný vektor (188,248,320,425,566)/96 je správný pro D s původním
základem D0=D1=1. To je jiné tvrzení než to, že D omezuje skutečné
stromy; to druhé vyvrací F017. Po opravě D1=2 platí dříve dokázaný
vektor (200,263,350,464,608)/96. Nejde o další samostatnou chybu.

Nový konečný certifikát pro původní vektor definuje F prvními 15
hodnotami a vzorcem F(5q+r)=4^q c_r−1/3 pro q≥3. Přímé konečné
rovnosti ověří definici maximem do n=47, jednoznačné maximum (4,0)
pro 19≤n≤47, neklesání a F(n+5)≥4F(n)+1. Od indexu 14 je poslední
vztah přesná rovnost, která se opakuje podle zbytku modulo pět.

Pro t≥15 stačí 4^floor(t/5)≥2t (pět základních případů a krok +5).
Monotónnost a kladný přídavek v periodickém růstu potom dávají
ostrou dominanci F(n) nad každou takovou větví. Pro t≤14 a n≥43
jsou všechny použité argumenty v periodické oblasti. Pro mezeru G
mezi F(n) a kandidátem platí

```
G(n+5) = 4G(n) + 4−t          pro t′=0,
G(n+5) = 4G(n) + 1−t+3t′      pro t′>0.
```

Pět zbytků n=43,…,47 dává 595 celočíselných certifikátů:
G>0 a 3G+c≥0 kromě (4,0), kde G=c=0. To zachovává znaménka
při každém kroku +5 a dokazuje maximum pro všechna n≥19.
Vzorec úlohy proto platí pro všechna požadovaná n≥3.
Nový certifikát nezahlazuje F017 ani neobnovuje chybnou mez stromů.

## 182–183: celý obrázek a výzkumná otázka

Kořen má čtyři singletony a čtyři hrany cyklu. Všechny další matice
v obrázku jsou právě zbytky po odstranění zvolené možnosti a možností,
které ji protínají; pivot je vždy nejkratší sloupec. Všechny hrany
i všech sedm prázdných úspěšných listů odpovídají této operaci.
Není zde skrytý neúspěšný list ani chybné políčko. Největší větvení je t=3.

U k disjunktních kopií MRV dokončí rozpracovanou kopii dříve, než
vstoupí do další. T_k=9+7T_(k−1), T_0=1 dává (5·7^k−3)/2 uzlů
a 7^k řešení. Starých šest změřených případů se neopakovalo.
Rozměr je 8k možností, tedy dolní exponenciální mez 7^(1/8).
Opravený důkaz F017 zachovává horní exponenciální mez 4^(1/5).

183 žádá přesné limsup mezi těmito mezemi. Odpověď je výzkumná
nápověda, nikoli tvrzení určité hodnoty; obdobnou otázku klade již
Eppsteinův primární zdroj. Úlohu jsme nevyřešili a krátké hledání
zdrojů nedokazuje, že je stále otevřená ve veškeré současné literatuře.
Nezahajujeme systematický výčet velkých instancí ani nepovažujeme
timeout za výsledek. Audit formulace, nápovědy a obou doložených mezí
je dokončen; `research_problem_solved: false` zůstává výslovné.

## 184–185: konstrukce a okrajové rozměry

Pro n≥1 obsahuje konstrukce 184 všechny neprázdné podmnožiny
prvních n−1 položek a vybrané řádky s poslední položkou. Řádek
velikosti n−j s poslední položkou ponechá j volných položek, tedy
B_j dokončení. Kapacita je binom(n−1,j). Indukční rozklad do těchto
kapacit funguje včetně t=0 i t=B_n; singletony rozliší všechny
původní sloupce. Konkrétní vytištěný součet dává přesně 10 000
a jeho koeficienty se vejdou do kapacit. Dřívější alternativní
rozklad je jiný, ale stejně platný; reprezentace není jednoznačná.

Pro N1≥1 dává plná rodina všech podmnožin s primární položkou
nejvíce řešení v 185. Rozklad primárních položek do m bloků má
S(N1,m) možností. Každá sekundární položka se buď nepoužije, nebo
patří do jednoho z m bloků, což dává (m+1)^N2. Úplná matice má
různé řádky a různé sloupce. Tím je maximum dosažené a vzorec platí.

E091 je doplnění odkazu z 10. 8. 2023, chybějící v obou místních
verzích. [OEIS A113547](https://oeis.org/A113547) má ekvivalentní
trojúhelník: knižní hodnota pro N1,N2 je T(N1+N2+1,N1+1).
Posunutí indexu ve Stirlingově součtu to přímo dokazuje.

C038 pouze ponechává otevřené, zda kladné rozměry mají být uvedeny
výslovně: pro n=0 v 184 nelze získat nula řešení a pro N1=0,N2≥2
v 185 neexistuje strict instance. Stará početní data platí; nejde
o potvrzený nový nález v zamýšlené nenulové doméně.

## 186–187: aktualizace a generující funkce

Při prvním cover se z možností velikosti k odstraní k−1 dalších
uzlů. Proto u_n=1+(n−1)2^(n−2) pro n≥1. Při volbě řádku velikosti k
se další seznamy zkrátí na úplné úlohy řádů n−1,…,n−k+1.
Součet přes velikosti dává knižní v_n a rekurenci x_n; n=0 se
ošetřuje samostatně. Obě vytištěné šestice se přesně shodují se
starými měřeními, které se neopakovaly.

Pro B(z)=exp(exp(z)−1) a T=T_(0,0) platí B′=exp(z)B a
T′=exp(z)T+1. Obecně

```
T_(r,s)′ − exp(z) T_(r,s) = z^r exp(sz),  T_(r,s)(0)=0.
```

Tím se znovu zdrojově potvrzuje F019: tisk v obecné derivaci
odpovědi 187(b) postrádá exp(sz). Pro skutečně požadované s=0
je vzorec správný. Úplné důkazy integrací per partes, krajního
členu a explicitního X(z) jsou již v přijatých poznámkách; symbolické
testy se nespouštěly znovu. Všechny ostatní indexy a koeficienty
zadání i odpovědi v obou zdrojích souhlasí.

## 188: celý trojúhelník včetně pokračování a historie

První řádek n=1 je úmyslně nula; kombinatorický výklad odpovědi
výslovně předepisuje n>1. Není to omyl v první hodnotě Gouldovy
posloupnosti. Pro vnitřní pozice odečteme rozklady, kde je 1
ekvivalentní následujícímu prvku; po kontrakci jde o předchozí řádek.
Pravý okraj odpovídá odstranění samostatné jedničky. Tyto bijekce
dávají všechny sčítací vztahy; 21 vytištěných čísel souhlasí v PDF i PS.

Byl zobrazen i původní Peirceův trojúhelník 4A 7.2.1.5–(12),
tištěná str. 418, skutečná strana DjVu 435. Jde pouze o kontrolu
křížového odkazu, nikoli o dokončení části samostatného auditu 4A.

Pokračování na str. 469 uvádí při počátečních 0,0,1 koeficienty
0,0,1,1,4,14,54,233. Souhlasí s T_(1,0)′=exp(z)T_(1,0)+z
a nulovou počáteční hodnotou: po 1,1 následují
3+1=4, 6+4+4=14, 10+10+20+14=54 a 15+20+60+84+54=233.
Žádný nový dlouhý výpočet není potřeba.

[Guyův dopis Sloaneovi](https://oeis.org/A002186/a002186.pdf) je datován
24. 6. 1968 na PDF str. 1; str. 3 připisuje Moserovi pozměněné
počátky, výslednou posloupnost a generující funkci. To dokládá
historickou cestu zmiňovanou v knize. Guyův přepis integrálu má
nadbytečný faktor e; [Knuthova zpráva z 29. 1. 2018](https://oeis.org/A040027/a040027.txt)
na tuto odchylku výslovně upozorňuje. Knižní integrál je správně.
[A046936](https://oeis.org/A046936) a [A298804](https://oeis.org/A298804)
mají očekávané opačné pořadí sloupců a různé počáteční indexy.

## Errata a zachování evidence

Prohledány dlouhé i krátké seznamy 4B a Fascicle 5 a oba jejich
TeXové zdroje. E090 a E091 mají přesné přepisy i určení stavu verzí.
F017–F019 nejsou v těchto šesti vrstvách opraveny. Křížové opravy
str. 102 a starý odkaz 188→189 se týkají následujícího kontextu;
nejsou automaticky započítány jako nový nález tohoto bloku.

F017–F019 a X180/X184 si zachovají původní závěry a důkazy, pouze
se připojí nový zdrojový rozsah. Osobní anotace a dosavadní anglické
karty se nemění. Další úplný blok je 189–192, včetně historického
odstavce a obrázku znamének, které staré početní kontroly nepokrývají celé.
