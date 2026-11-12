# Souvislý průchod §1.2.9 — 5. listopadu 2026

Přímo přečten původní text87–96 a odpovědi496–499, soubor102–111
a511–514. Na96 začíná algoritmus M; ten není součástí tohoto bloku.
Fibonacciho obsah na496 byl zkontrolován X0942. Přečteny celé důkazy
`generating-basic.md`, `generating-symmetric.md`,
`generating-combinatorial.md`, `carlitz-cyclic-sums.md`,
`gauss-harmonic-formula.md`, `laplace-transform.md`,
`factorial-asymptotic.md` a všechny přijaté pramenné recenze uvedené
v X0112. Uložené výsledky7384 a9657 přesných kontrol byly přečteny;
výpočty se neopakovaly.

## Matematika a fakta

Pokrývá celý hlavní výklad, tabulku(19)–(30), symetrické funkce
a všech26 úloh. Každý formální koeficient se odvozuje z konečně
mnoha příspěvků; analytické derivace, integrály a součiny používají
menší kruh absolutní konvergence. Tvrzení o omezenosti n-tých
odmocnin se vztahuje na n>=1, nikoli na nulový index.

Kořenový filtr, exponenciální konvoluce a obě Stirlingovy řady
souhlasí včetně faktoriálů. Implicitní řady mají jednoznačnou větev
x(0)=1; jejich zdánlivé nulové jmenovatele mají polynomiální význam.
Cauchyho vzorec má správnou orientaci a normalizaci. Newtonovy
identity, jejich inverze a všechny čtyři nízké mocninné součty
odpovídají příslušným součinům. Bernoulliho změna2021 mění konvenci
B_1, nikoli pravdivost původní formule ve staré konvenci.

Kontrola zahrnuje rozkladový součin, omezené násobnosti, dvojitý
kořen z=−1/4 v úloze15, binární součin22, oba koeficientové součty25
a bezpečný obor zobecněných závorek26. Není dovoleno změnit oblast
rozvoje při záměně z za1/z. Původní zadání15/24/25 se liší od
chybných pomocných přepisů; rozhoduje obraz, nikoli Markdown.

Carlitzova otevřená i cyklická suma má polynomiální důkaz, který
zahrnuje nulové proměnné a shodné charakteristické kořeny. Nekonečná
cyklická řada má větev odmocniny s konstantním členem+1; vlastní
Jacobiánový důkaz a přijatá původní determinantová identita se shodují.
Charakteristický polynom pravostranné Pascalovy matice plyne ze
symetrické mocniny dvourozměrné substituce. Ani jeden z těchto
obecných závěrů nestojí pouze na konečném výčtu.

Gaussův harmonický vzorec má správné logaritmické větve a souhlasí
s původním[74]/[75]; nesoudělnost p,q není nutná. Hraniční krok
má úplné zdůvodnění a původní Abelova věta je přijata v přesném
rozsahu X0713. Dobové matematické a historické citace dalších
autorů se přijímají v rozsahu jejich konkrétních recenzí, nikoli
jako úplný audit všech externích článků nebo absolutní priority.

## Dva nálezy a jejich skutečné umístění

C0011 je přesně chyba **dodatku z1.1.2024** k úloze13, nikoli
výslovného tvrzení Re(s)>0 v originálu1997: taková věta tam není.
Původní úloha žádá vyjádřit transformaci; její vztah platí v oboru
konvergence. Teprve dodatek tvrdí, že kladná reálná část s zajistí
existenci integrálu. Pro a_k=2^k,s=log2 je integrál do N roven
(N−1+2^(−N))/log2 a diverguje. Dostačuje sigma=Re(s)>0 a
exp(−sigma)<R, kde R je poloměr G. Tento přesný důkaz zůstává
potvrzený. Původní94 je v mapě související místo, nikoli červená
strana způsobená dodatečně vloženou nepravdivou větou.

C0012 leží v původní odpovědi21 na498. Obecná rodina má při
z=−1/u člen C*u*exp(u); požadovaný rozvoj s vedoucím členem1
má právě C=0. Pro tuto volbu dává integrál exp(−v)/(1−zv) přesný
zbytek s mezí N!|z|^N. Jde o chybějící normalizaci v jinak správné
rovnici a řešení; UI závažnost snižujeme z automatického high na low,
v souladu s již původním označením „drobné upřesnění“. Stav confirmed
se nemění a osobní hodnocení uživatele se nepřepisuje.

Aktuální all1 strany6 a13 byly přímo vykresleny z dnes staženého
PostScriptu a přečteny. Manifest
`sources/sequential-2026-11-05/generating-current-images.json`
obsahuje hashe zdroje i obrazů. Potvrzuje znění C0011 i absenci
C=0 v relevantních změnách. Žádný nový nález nevznikl.

X0109 mapujeme jako původní vady na87,88,89,90,93,95,496–499:
interpunkce a jméno; a0+b0 místo a0*b0; chybějící dolní meze;
pravopis citace; závorka v H_x; faktor1/k!; Girardův titul;
Gaussova znaménka a f(1); argument E1 a Knoppova bibliografie;
svazek Carlitzovy citace a chybějící vysvětlení násobení n!.
Změny Bernoulliho konvence, přejmenování a_m na e_m, explicitní
prázdné produkty h_0/e_0 a ekvivalentní přeznačení indexu nejsou
samy vadami původních vzorců. Nová značka(a) odpovědi23 pouze
zpřehledňuje členění. Oprava n! z28.3.2026 je v úplném all1;
krátké err1 ji neobsahuje, a proto samotné err1 k porovnání nestačí.

## Bibliografické výjimky

Hlavní text se nyní uzavírá podle zadání s přesnými výjimkami:
Henrici1974,kapitola1 (vlastní matematické strany nezískány);
Zave1976,75–77 (obsah nepřečten); alternativní stránkování
Cauchyho prvotisku1826,95–113 (citované Œuvres přečteny);
přesné doložení Wilfova citátu už v1989 (autorství i znění
jsou doloženy vydáním1994). Jde o bibliografii a dataci citátu,
nikoli vynechaný důkaz zde používané matematické věty.
X0112/X0744/X0754 zůstávají pramenně partial, výjimky nejsou
potvrzenými zdroji. Žádné neúspěšné stahování se znovu neopakovalo.

Strany87–95 a496–499 jsou obsahově zkontrolovány s těmito výjimkami.
Strana96 čeká na algoritmus M. Všech26 úloh bylo již checked;
celkových859/932 úloh se nemění. Přibyl uzavřený hlavní oddíl:
16 z51; ani tento ukazatel není procentem všech stránek knihy.
