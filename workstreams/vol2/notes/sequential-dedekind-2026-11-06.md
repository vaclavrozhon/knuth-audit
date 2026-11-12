# Souvislá revize §3.3.3: P, B, D, K a úlohy 1–17

6. listopadu 2026, X0101–X0102. Původní text 80–89, zadání 90–92
a odpovědi 572–574 byly porovnány s dřívějšími důkazy a s původní
sazbou. Tento checkpoint pokrývá úlohy 1–17 a novou Fineovu úlohu
z roku 2001; úlohy 18–28 a zbytek strany 90 navazují zvlášť.

Hlavní matematické vzorce jsou správné v níže vymezeném oboru.
Znovu potvrzen C0032, chybný index pomocné Cauchyovy nerovnosti.
Nový C0242 sdružuje dva nízkozávažné okraje při jednotkovém
modulu: ostrou mez věty P a logaritmickou mez počtu kroků.
Úloha 14 nově `partial`, protože přesná globální korelace
nenahrazuje nedoložená tři historická měření krátkých úseků.

## Přijaté důkazy a výpočty

Přečten celý `verify_dedekind.py`, všech sedm výsledných bloků,
log a úplné poznámky `dedekind.md` i C0032. Program používá
přímou definici pilovitých součtů odděleně od Eukleidovy
rekurence; korelace navíc počítá přímo z celých orbit.
Uložené výsledky se přijímají po kontrole programu, nepouští se
znovu. 312 komplexních kontrol při 90 desetinných místech je
pouze numerická kontrola, nikoli intervalový důkaz.

Přezkoumány zejména tyto obecné kroky:

- Rozklad zbytků modulo k/g dokazuje součet podlah pro celé h,
  kladné k a reálné c, včetně záporného h a h=0. Replikační zákon
  pilovité funkce zahrnuje hodnoty 0 v celých bodech. Obrázek 7,
  Fourierovy koeficienty i střední hodnota na skocích souhlasí.
  Fineův součet teleskopuje a jeho absolutní hodnota je <1.
- Oba důkazy P jsou správné pro m>1. Přesný počet poklesů je
  (m+2(c mod d)−d)/2. Úloha 4: potence 10 modulo 10^10 nutí
  v5(a−1)=1; největší d je 2^10·5 a tištěná mez je správná.
- Rozvinutí obou pilovitých funkcí dává přesnou korelaci (17),
  včetně dvou okrajových stavů x=0 a x'=−a^(-1)c mod m.
  Odhad sigma používá normu sigma(1,m,0), nikoli sigma(a,m,0).
  To je přesně C0032 v odpovědi 12; zadání úlohy platí.
- Symetrie, škálování a posun c vycházejí ze změny indexu,
  replikačního zákona a polovičních skoků pilovité funkce.
  Bézoutův vztah dává posunutou reciprocitu B. Pro reálné c se
  c² správně nahrazuje floor(c)ceil(c).
- Konečný Fourierův filtr má faktor 1/k; na straně 85 je
  skutečně zeta=exp(2pi i/h). Rezidua a druhá derivace dávají
  klasickou reciprocitu. Případ h=k=1 vyřízen přímo; samotný
  pólový rozklad bez konstanty v tomto případě neplatí.
- Vážené počítání mřížových bodů v úloze 7 je nezávislý důkaz;
  konstantní člen původní odpovědi je +1/4. V úlohách 8/9
  zkontrolována rezidua součinu tří kotangent i rozdělení kvádru
  podle jediného maxima i/p,j/q,l/r. Po rozvinutí podlah a použití
  klasické reciprocity vzniká přesně Rademacherův vztah.
- Teleskopování reciprocity, konvergentů a indikátorů e dává
  všechny konstanty věty D. Vážené součtování per partes dává
  úlohu 16. Pomocný mocninný dělený rozdíl při shodných c je
  vykládán spojitě; vlastní kvadratická formule žádné 0/0 nemá.
- Invarianty A,B,p,p',s dokazují algoritmus D; při konci je
  p původní k. Přenášení násobků k z B do A zachovává přesnou
  hodnotu. Výpočetní model programu je neomezená celočíselná
  aritmetika; netvrdíme nový pevný počet bitů pro každý mezivýraz.

Pro přesnost C≈sigma/m stačí označit N=−3+6(m−x'−c).
Pak |N|≤6m−9, |sigma/m|<1 a

```text
|C−sigma/m| = |sigma/m+N|/(m²−1) < 6/m, m≥2.
```

Podrobně přezkoumán také odhad aproximace (39). S označením
T=(1−6c/m+6(c/m)²)/a, q=c mod a a
E=−sigma(m,a,c)+6q/a−3[q≠0] dává reciprocita přesný vztah

```text
C−T = (mE+a+1/a+T−3+6(m−x'−c))/(m²−1).
```

Centrované vektory mají součty čtverců (a²−1)/(12a)
a (a−1)(a−2)/(12a); tedy |E|≤a−1 pro a≥2, E=0 pro a=1.
Spolu s |T|≤1/a dostáváme horní mez
(m(a+5)+a+2/a−9)/(m²−1). Rozdíl po vynásobení jmenovatelů
od požadované meze (a+6)/m je

```text
m²−m(a+2/a−9)−a−6 ≥ 7m−5 > 0,
```

protože 1≤a≤m−1. Odhad tedy platí obecně, ne jen v malých
modelech. Kořeny čitatele T jsou 1/2±sqrt(3)/6.

Příklady 1/2, úloha 14 a všech 22 podílů příkladu 4 souhlasí
s uloženými přesnými zlomky. Příklad 2 má potence 3 a
sigma=−31.6926653544; příklad 4 meze −55 a 67.5.
Přesné tabulky jsou v `results/dedekind.json`.

## Věta K a primární zdroj

Znovu vizuálně přečten [Knuth 1977, strany 304–317](https://matwbn.icm.edu.pl/ksiazki/aa/aa33/aa3341.pdf)
z uloženého PDF. Nově zachované obrazy 304–315 doplňují již
existující obraz 316–317. Síťové otevření 6.11. vrátilo 403;
netvrdíme nový download ani novější verzi zdroje.

Odčítací Eukleidův důkaz maximalizace nejprve přesune zbytek
do dolní poloviny, pak zmenší kladné podíly B na 1. Konvexita
a nezáporné rozdíly konvergentů ukazují, že nejpozdější ukončení
dává maximum mezi nenulovými c. Nulové c se kontroluje zvlášť.
Algebra v (4.17)–(4.22), včetně posledního podílu 1, dává
horní mez; inverze h modulo k a obrácení posloupnosti dávají
dolní mez (4.23). Zdroj navíc obsahuje explicitní odchylky
extrémů s reciprokými podíly; tvrzení o těsnosti tedy nestojí
jen na testovaných konečných případech.

Kniha indexuje od 1, článek od 0 a vyžaduje sudý počet podílů.
Pro sudý počet a součty O,E na lichých/sudých knižních pozicích
dává zdroj −O/2−E+1/2 ≤ sigma ≤ O+E/2−1/2. Knižní dolní
mez je slabší o 1/2. Pro lichý počet se poslední A rozloží
na A−1,1: O přejde na O−1 a E na E+1. Pak dostáváme přesně
knižní dolní mez a ještě o 1/2 silnější horní mez. h=k=1 se
ověří přímo. Věta K tedy platí v celém svém uvedeném oboru.

Úplný audit ostatních tvrzení článku tímto checkpointem
neprohlašujeme. Algoritmus 2 zdroje není samostatně certifikován.

## Errata a otevřené části

Čtyři vrstvy errat a aktuální TeX prohledány 6.11.2026. Výřez
80–93 a 572–577 uložen se SHA-256; oprava na 577 již patří
§3.3.4 a změna m≪N na 572 patří předchozí odpovědi 35.
Pro tento blok platí doplnění (6), změna odkazu pod (10),
nahrazení staré úlohy 2 / přečíslování Fourierovy úlohy / nová
Fineova 3, rok 1978→1977, index a_t→a_j na 90 a math.→Math.
v odpovědi 9. Známé chyby zvlášť eviduje X0102.

Nedostupná bibliografie nepřekrývá matematické mezery:

- Fineova konkrétní strana 401 a Carlitzův celý článek nebyly
  přečteny; samostatné důkazy výše na nich nestojí.
- Historické atribuce Riemann/Dedekind, Coveyou, Greenberger,
  Dieter a Popeova citace nejsou v tomto checkpointu vydávány
  za kontrolu původních zdrojů. Zachované metadatové doklady
  a rozsah dřívějšího čtení zůstávají uvedeny ve zdrojových JSON.
- Tři korelace 0.2–0.3 v úloze 14 nemají počáteční stavy ani
  přesné párování. To je chybějící reprodukce měření, nikoli
  bibliografická výjimka; strany 89 a 91 zůstávají částečné.
- Obecné historické tvrzení na 88 o více než desetiletém používání
  nejběžnějších vadných generátorů a jeho příčině není doloženo
  konkrétními údaji o tehdejší praxi. Tato část zůstává otevřená,
  ačkoli matematika obou příkladů na stránce je přezkoumána.
- Průměr součtu podílů na 90 má dopřednou závislost §4.5.3–35.
  Markovův krok po přijetí tohoto průměru funguje pro výběr
  invertibilního násobitele. Obecná ostrá mez v úloze 19 je
  stále otevřená a navazuje v dalším bloku.

Celé stránky 80–87, 572–573 jsou v doloženém rozsahu zapsány
do UI; 88–92 a 574 zůstávají částečné. Sdílené části 80/572
z §3.3.2 byly uzavřeny v předchozím checkpointu. Nález může
obarvit červeně i stránku s jinou dosud otevřenou částí.
Žádný drahý běh nebyl restartován, vznikl jen přímý výpočet
jednotkových protipříkladů. Nové emailové návrhy nevznikly.
