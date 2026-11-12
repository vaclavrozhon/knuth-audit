# Souvislý průchod §2.3.4–2.3.4.1 — 5. listopadu 2026

X0973: celý úvod 362–363, volné stromy 363–371 a všech 13 odpovědí
578–580 porovnány s původními obrazy. Přezkoušeny obecné důkazy
`parallel/free-trees/notes/general-proofs.md`, důkaz C0041 a zápisy
pramenné kolace. `check_figures.py` přečten proti přepisu obrázků;
dřívější přijaté výpočty se znovu nespouštěly. Nový nález nepřibyl.

## Definice a věta A

Úvod rozlišuje neuspořádané volné stromy od kořenových uspořádaných
stromů předchozích částí. V původní terminologii může path opakovat
vrcholy; simple path je bez opakování, kromě případného uzavření.
Pozdější walk/path je změna terminologie. Originál 363 dovoluje délku
n≥0, nikoli OCR n>0. Konečná část věty A výslovně předpokládá n>0.

Fig.29 má pět vrcholů a šest hran AB,AC,BD,CD,BE,DE. Šest cyklů
z B je BACDB, BACDEB, BDCAB, BDEB, BEDB, BEDCAB. Fig.30 má
14 vrcholů a 13 hran; všechny jsou spojeny a cyklus nevzniká.

Odstraněním hrany cyklu zůstávají její konce spojeny. Dvě různé
jednoduché cesty naopak určují cyklus mezi prvním rozchodem a dalším
setkáním. Tím platí (a)–(c) i pro nekonečné grafy s konečnými cestami.
V konečném lese platí m=n−c, kde c je počet komponent; odebrání listu
zachová rozdíl n−m. V konečném souvislém grafu lze postupně mazat hrany
cyklů a získat kostru s n−1 hranami. To dává (d) a (e).

Na 364 je skutečná, již zveřejněná chyba důkazu: začít **libovolným**
vrcholem neumožňuje pokračovat k listu, pokud graf obsahuje izolovaný
vrchol. Předpoklad alespoň jedné hrany nevylučuje izolované komponenty.
Oprava z 2. září 1997 vybírá vhodný počáteční vrchol. Upřesnění délky
dvou cest z roku 2020 nepřidává nový matematický problém.

## Toky a všechny obrázky 31–32

Po volbě kostry má každá mimokostrová hrana vlastní fundamentální
cyklus. Jeho souřadnice na této hraně je +1 a na ostatních mimokostrových
hranách nula. Cykly tedy tvoří nezávislou soustavu a libovolné reálné
hodnoty mimokostrových toků se jednoznačně rozšíří na vyvážený tok.
Rozdíl dvou rozšíření je tok podporovaný na stromu, který je nulový:
stačí řez přes libovolnou stromovou hranu. Rozměr je m−n+1.

Přidání e0:Stop→Start dá m−n+2 fundamentálních cyklů; pevné E0=1
ponechá m−n+1 volných hodnot. Rozdělení hrany přidá jeden vrchol
i jednu hranu, takže rozměr nezmění. Konečnost je nutná: na oboustranně
nekonečné cestě existuje nenulový vyvážený tok bez cyklu.

Fig.31 obsahuje 19 vrcholů a 27 hran. Po přidání e0 a rozdělení
hran 13 a 19 má Fig.32 21 vrcholů, 30 hran a 10 mimokostrových
hran 0,2,5,8,13d,17,19d,20,21,25. Konce, směry a znaménka všech
deseti cyklů i všech dvaceti rovnic (6) souhlasí s obrázky. Zejména
C20=e20+e18+e22+e23, C21=e21−e16−e15−e11−e27−e24−e22−e18
a C25=e25+e26−e27. Nejde jen o porovnání vypočtených čísel s OCR.

Příklad E2=2,E8=0,E0=1 vynutí E3=−1. Samostatný kladný cyklus K–L
vedle průchodu Start–Stop ukazuje další nutnost souvislé podpory.
Naopak konečný nezáporný celočíselný vyvážený tok se souvislou
kladnou podporou má Eulerův tah po přidání e0. Rozpojení v e0 dá
hledaný průchod. Výklad výslovně nezná sémantiku podmínek programu;
netvrdí, že každé takové řešení realizuje konkrétní programový vstup.

## Úlohy 1–9

1–4: původní definice a počet cyklů souhlasí. Úloha 3 má cestu
1,2,6,7,9,10,11,12,14. Nulovost toku na konečném stromu platí
i se zápornými hodnotami, jak ukazuje řezový důkaz výše.

5: všech 15 rovnic pro počty průchodů vrcholy souhlasí. Inverze je
E8=A−1, E2=A−B, E5=A−D, E13d=G−1, E17=J, E21=J−H,
E20=Q, E19d=K−Q, E25=S. Počet devíti nezávislých měření se nemění.
Obě C mají počet 1+E8 a vrchol 1 má počet 1.

6: E přijímá právě hrany spojující různé dosavadní komponenty.
Výsledkem je kostra právě tehdy, když přijme n−1 hran; jinak je graf
nesouvislý. Pro n=1 je správný prázdný seznam. Lineární prohledání
grafu řeší stejný problém; přesná sazba §2.3.5A bude další kontrola.

7: pět uvedených cyklů a rovnic souhlasí s každým obloukem obrázku.
Například C6=e6−e2+e4 a C8=e8−e9−e4−e3; proto
E4=1+E6−E7−E8 a E9=1−E8.

8: slučují se výstupy **téhož původního vrcholu**, ne všechny výstupy
později sloučeného supervrcholu. Surjektivitu redukce dokládá rozbor
dvou hran e:u→v,f:u→w se součtem S. Pro v=w se e volí libovolně
a f=S−e. Pro tři různé vrcholy vynutí původní bilance e=d(v),f=d(w).
Pro smyčku u=v≠w je f=d(w),e=S−f. Redukovaná bilance zajistí zbytek.
Záporné toky jsou zadáním dovoleny; důkaz neslibuje nezápornost.
Jen první případ snižuje počet volných toků o jeden.

Izomorfismus příchozí a odchozí redukce plyne z bipartitního grafu:
každý původní oblouk u→v propojí L(u) s R(v). Označí-li C komponentu,
v obou výsledcích odpovídá původnímu vrcholu v hrana
C(R(v))→C(L(v)). Po uzavření diagramu e0 má každý vrchol vstup i výstup.
Příklad má uzly Start,U={A,B,D,Stop},C, šest oblouků a vztahy
s=t=1,b=c. Stačí tři nezávislá měření a,c,d. Originál 579 již správně
říká tři; doplnění 2021 pouze vysvětluje, proč není nutné měřit e0.

9: smyčka má nulový incidenční sloupec a tvoří samostatný cyklus.
Z paralelních hran se zvolí jedna a ostatní vytvoří cykly e_i−e
nebo e_i+e podle orientace; zbývající konstrukce kostry je nezměněná.

## Úlohy 10–13 a C0041

10: spojení n≥1 terminálů potřebuje n−1 vodičů; n=1 potřebuje nulu.
11: z nejlevnější hrany přes řez lze výměnou v libovolné minimální
kostře získat jinou minimální kostru, která ji obsahuje. Funguje to
i při rovnostech a libovolných reálných cenách. Kontrakce musí uchovat
konkrétní konce vybraných hran, jak zadání vyžaduje. Fig.33 souhlasí
se všemi zadanými souřadnicemi, minimálními řezy a výslednou délkou
7+2√2+2√5. Přijatý programový doklad se znovu nespouštěl.

12: **C0041 zůstává confirmed, critical, přesně na straně 580.**
Pro c14=1,c12=2,c24=3,c34=10,c23=20,c13=30 začne algoritmus
a=(1,3,10). Po prvním kroku je a=(∞,2,10), po druhém a=(2,∞,10):
neomezená aktualizace vrátí vybranému vrcholu 1 konečnou hodnotu.
Poslední krok vybere opět hranu 12. Výstup 14,21,12 nechává 3 izolovaný.
Nejsou zde shody cen ani nulové či nekonečné vstupní ceny; diagonálu
lze vynechat. Oprava aktualizuje jen dosud nevybrané j≠i. Pak
a_j=min_{v∈S} c(j,v), b_j∈S, a řezový důkaz zajišťuje minimum
v O(n²). Následující varianta se seznamem nevybraných vrcholů je správná.
Přijatých 760 srovnání s nezávislým Kruskalem se neopakovalo.

13: transpozice podél hran nespojí různé komponenty. V souvislém grafu
t1⋯t(k−1)tk t(k−1)⋯t1 zamění konce cesty, a generuje tedy všechny
permutace. Stačí n−1 hran kostry, n−2 nestačí. Identita při j=n−1
v indukčním zápisu není požadavek na neexistující netriviální transpozici.

## Prameny, přesné výjimky a stránková mapa

Převzaté pramenné čtení dokládá Kirchhoffovy zákony a konstrukci cyklů,
Ball–Larusovo rozmístění čítačů, Jarníkův i Primův postup, čtyřstránkovou
Dijkstrovu práci a KNOWN test v programu MILES_SPAN. Jarníkova německá
část na 62–63 nemění správný údaj 57–61 pro českou část. Prim na 1400
odstraňuje vybrané sloupce, a tedy nemá chybu C0041. Data GraphBase
již uzavírá X0699: autorská errata a rozhovor z prosince 1993 dokládají
vydání 1993; samotný copyright 1994 je nevyvrací.

Zůstávají výslovně přeskočené bibliografické části, nikoli matematika:

- Kirchhoff 1845: originální fyzická paginace časopisu nepřístupná;
  použit autorský souborný přetisk 1882. U článku 1847 kontrolovány
  relevantní strany 22–24, ne celý fyzikální výklad a příloha.
- Ball–Larus 1994: ověřena konkrétní opora tvrzení v titulu, abstraktu
  a §3.2 na 1328–1329, nikoli celý 42stránkový článek.
- Úloha 8: Knuth–Stevenson 1973 má ověřená nakladatelská metadata
  a relevantní text autorského přetisku na 43–49 a bibliografii 53.
  Originální sazba BIT 13,313–322 a SIMULA příloha přetisku 49–52
  nejsou kolacionovány. Nahapetian, Acta Informatica 3 (1973),37–41
  má ověřená metadata a abstrakt, ne plný pětistránkový text.
- Budoucí odkazy §7.4.1.2 a §7.5.4 nejsou v dodaných dokončených
  svazcích; jsou evidovány jako neověřený budoucí odkaz.

Úloha 8 se proto uzavírá s oddělenými bibliografickými výjimkami.
Všech 13 úloh i hlavní text mají matematiku/fakta zkontrolované.
Čtyři dnešní vrstvy errat jsou nově prohledány po celých blocích
362–371/578–580 i tematicky; SHA-256 a výpisy jsou v příslušném JSON.
Oprava C0041 v nich není. Fyzický výtisk a prvenství nejsou ověřeny.

Mapa X0341 označuje červeně jen věcnou chybu důkazu na 364.
Na 367 **již náš originál má velké E_j**, nikoli chybné e_j.
Na 370 náhrada obrázku mění C z kruhu na obdélník; všechny směry,
konce a označení hran jsou původně správné. Jde o rozlišení typu
symbolu ve vývojovém diagramu, ne jiný graf. Tyto položky, změny
terminologie a dodané citace nevytvářejí nové červené matematické stránky.
C0041 má přesnou lokaci pouze 580, nikoli správné zadání na 371.
Celé 362–371 a 578–579 jsou nyní pokryty; 580 zůstává částečná,
protože obsahuje také odpovědi následujícího oddílu. Další kurzor:
§2.3.4.2, tištěná 372 / soubor 387.
