# Audit §1.4.2: korutiny

Kontrola 1. 11. 2026, třetí vydání, první dotisk z května 1997.
Zobrazeny původní tištěné strany 193–200 a odpovědi na 529;
strana 530 již začíná odpověďmi k §1.4.3.1. Fyzický exemplář nebyl
ověřen. Obrázky jsou v `../images/p193.png` až `p200.png` a `p529.png`.

Značení: rA, rX, rI1 až rI6 a rJ jsou registry MIX; CI je porovnávací
indikátor se stavy less, equal a greater. Báze bajtu je b, kde
64 <= b <= 100. Pokračování korutiny znamená adresu, odkud se má
obnovit její pozastavený výpočet. Zde jsou pokračování uložena
v adresních polích instrukcí AX, BX, případně CX. Vstup tvoří konečný
proud znaků ukončený tečkou podle zadání; mezery se ignorují.
Předpokládáme platné paměťové oblasti a dokončení zahájených I/O operací.

## Hlavní text a program

**Vazba (1), s. 194 — checked.** Při přechodu z A do B uloží
`B STJ AX` adresu za volajícím JMP do AX a BX provede dříve uložené
pokračování B. Symetricky přechod z B do A mění jen BX. Indukcí přes
počet přechodů je v každé pozastavené korutině uložen právě její
poslední bod pokračování. Před prvním vstupem příslušný slot obsahuje
A1 nebo B1. Volající JMP, STJ a závěrečný JMP mají celkem 1+2+1 = 4u.
Známé erratum mění na s. 194 zkratku J na rJ; algoritmus nemění.

**Příklad (2)–(3), s. 195 — checked with known spacing erratum.**
Číslice d před následujícím znakem znamená d+1 opakování tohoto
znaku, i když je tento další znak sám číslicí. Program zastaví při
první vydané tečce. Příklad skutečně dává skupiny

```
ABB BEE EEE E44 446 66F GZY W22 220 0PQ 999 999 999 R.
```

V poslední dvojici sporných skupin je číslice 0, nikoli písmeno O;
potvrzuje to originál a `../images/p195-example-crop.png`.
Záměna vznikla při prvním vlastním přepisu, není nálezem v knize.

**NEXTCHAR, s. 195–196 — checked.** rI6 označuje příští slovo aktuální
karty; nula znamená, že je nutná nová karta. rX obsahuje dosud
neodebrané znaky posledního načteného slova. Je-li rX nula, rutina
načte další slovo, případně nejprve IN a JBUS dokončí čtení karty.
ENTA 0 a SLAX 1 přesunou nejbližší znak do rA. JANZ vrátí každý
nenulový znak; nuly odpovídající mezerám přeskočí. Načtením dalšího
slova se nepřeskakuje žádný nenulový znak. Existující koncová tečka
zaručuje, že se požadavek na znak nakonec vrátí. rX a rI6 mohou být
změněny, zatímco rI4 a rI5 se zachovávají pro spolupracující části.

**IN, s. 196 — checked.** Kódy číslic jsou 30 až 39. Po odečtení 30
jde záporná hodnota nebo hodnota alespoň 10 přímou větví; INCA 30
obnoví původní znak. Pro číslici d je nastaveno rI5=d a NEXTCHAR
načte její následující znak. Smyčka nejprve tento znak vydá, pak
snižuje rI5 a opakuje při nezáporné hodnotě. Vydá jej tedy právě
d+1 krát. OUT zachovává A, X, I5 a I6, takže replikace i čtení mohou
navázat. IN zachovává rI4 jako ukazatel do výstupního bufferu.

**OUT a inicializace, s. 196–197 — checked with known contract erratum.**
Šestnáct slov obsahuje po třech výstupních znacích a dvou mezerách.
MOVE postupným překrývajícím se kopírováním vyplní celý buffer pěti
mezerami z předchozího slova. Pro rI4 od -16 do -1 se ukládají znaky
do polí 1:1, 2:2 a 3:3 aktuálního slova; každé JE po porovnání s
PERIOD včas ukončí i poslední neúplnou skupinu. Jinak se po 48 znacích
vydá plná karta a cyklus začne znovu. JBUS před přepsáním bufferu
zajistí dokončení děrování, včetně nenulové latence zařízení.
OUT mění I1 a I4: výslovné doplnění I4 do kontraktu je známá oprava
z roku 2018. Zachovává A, X, I5 a I6; celý program zachovává I2 a I3.
Počáteční nastavení I6 a X a první vstup do OUT připraví oba buffery
před předáním prvního znaku.

**Vazba (4), s. 198 — checked.** STA HOLDA při opuštění IN uloží
jeho rA a LDA HOLDA před návratem z OUT jej obnoví. Jedna uložená
hodnota stačí, když se vyžaduje zachování A jen pro IN. Obě korutiny
se vykonávají kooperativně, takže tyto dva okamžiky se párují.

**Průchody, obr. 22 a diskuse s. 198–200 — checked in stated model.**
Když každá fáze produkuje proud položek pro další a nepotřebuje
výsledky z budoucího konce proudu, lze zápis na mezilehlou pásku
nahradit předáním položky další korutině a požadavek na další vstup
návratem producentovi. Obrázek zachovává pořadí A, B, C, D i směr
všech datových toků. Tím zmizí mezilehlé balení, zápis a čtení.
Text současně rozebírá větší paměťové nároky a pomalejší paměť jako
možný opačný vliv na čas; nevydává výhodu za záruku na libovolném
hardwaru. Rozdělení práce a srozumitelnost jsou praktická doporučení.
Zpětná potřebná informace, například další tah ve vzájemné hře,
brání prostému rozdělení na hotový průchod A a potom B. Naopak
potřeba konečného součtu z celého vstupu brání popsanému okamžitému
předávání bez dalšího průchodu či uložení vstupu. Vtip na s. 200
ilustruje právě potřebu budoucí informace. Výslovné omezení těchto
převodů v textu je podstatné. UNIX a seznam filtrů mají dvě známé
typografické/redakční opravy. Vnitřní odkazy a dobové plány dalších
kapitol jsou vymezeny v `sources.md`.

## Cvičení 1–7 a odpovědi

**1 — checked.** „Calls ... only once“ znamená jediné místo volání
v kódu, jak potvrzuje následující věta o dvou odlišných místech.
Pevné místo pokračování lze použít jako vstup podprogramu. Při více
místech lze někdy potřebné rozlišení odvodit z dat nebo uložit jako
přepínač; četnější předávání lépe ukazuje užitek pokračování.
Odpověď netvrdí, že jedno místo volání smí být vykonáno jen jednou.

**2 — checked.** Při prvním vstupu do IN se vytvoří znak a skok OUT
nejprve spustí OUT1. Ten teprve inicializuje buffer a skočí zpět do
IN; první již vytvořený znak se tak neuloží. U periodického konce
na první pozici se může dokonce ztratit ukončovací znak. Oprava v
odpovědi předem inicializuje rI4 a buffer a nastaví první OUTX na
řádek 39, který uloží již připravený znak; pak platí běžný invariant.
Příklady AB., 2A. a 0A. ověřují ztrátu právě prvního expandovaného
znaku při nezměněné chybné inicializaci.

**3 — known_erratum, oprava 17. 7. 2006.** Původní odpověď postihuje
replikovanou tečku, ale opomíjí počáteční neurčený stav CI. Po
odstranění tří CMPA v OUT například vstup A. a počáteční CI=equal
skončí již po A. Vstup 0.A. při CI=less vydá .A. namísto samotné
tečky. To jsou reprodukce známé chyby, nikoli nové nálezy.

Opravená optimalizace vloží CMPA PERIOD za čtení replikovaného znaku
mezi řádky 26 a 27 a CMPX PERIOD po nulování X mezi 59 a 60.
První instrukce nastaví CI pro všechny kopie replikovaného znaku.
Pro přímý znak s kódem alespoň 30 je dřívější CMPA =10= equal právě
pro tečku s kódem 40. Přímý znak s kódem pod 30 nechává CI beze
změny: počáteční CI je nově less a po jakémkoli dříve předaném
neterminálním znaku není equal. Indukcí tedy JE pozná právě tečku.
CI se pak stává součástí kontraktu mezi korutinami, jak oprava říká.

**4 — checked against primary manuals.** Přesné stránky a přístupové
meze jsou v `sources.md`. Následující argumenty vycházejí z instrukcí
na původních stránkách manuálů, nikoli z pozdějšího emulátoru.

- IBM 650: v zápisu `LDD    A` je datová adresa prázdná a A je
  instrukční adresa. SOAP ji doplní adresou následující instrukce
  zdrojového programu. LDD načte celé toto pokračovací slovo do
  distributoru D a pokračuje na A. `A STD BX AX` uloží kopii do BX
  a vykoná AX. Symetrický vstup B aktualizuje AX a vykoná BX.
  Každé instrukční slovo IBM 650 obsahuje výslovnou adresu další
  instrukce, proto zkopírované pokračování dále naváže do původního
  kódu. AX a BX se před prvním vstupem naplní prvními instrukcemi
  příslušných korutin. Nejde o načtení obsahu adresy A do D.
- IBM 709: je-li volací TSX na adrese p, uloží do indexového registru
  4 dvojkový doplněk p. SXA uloží tento doplněk do adresního pole
  opačného slotu AXT. Při obnovení AXT načte doplněk zpět a
  `TRA 1,4`, jehož efektivní adresa vzniká odečtením indexu,
  skočí na p+1. Inicializace hodnotou 1-A1 obdobně dává vstup A1.
  Aritmetika adres je v patnácti bitech. Registry akumulátoru a MQ
  se touto vazbou nepoužívají.
- CDC 1604: označme A a B=A+1 dvě po sobě jdoucí 48bitová slova.
  V každém jsou horní a dolní instrukce. SLJ 4 zapisuje adresu
  následujícího celého slova do adresního pole horní instrukce cíle
  a začne jeho dolní instrukcí. Při přechodu do A tedy aktualizuje
  horní skok A na pokračování B; dolní ALS 0 nemění stav a projde
  do horní instrukce následujícího slova B, která míří na pokračování
  A. Při přechodu do B aktualizuje jeho horní skok na pokračování A
  a dolní SLJ A vykoná horní skok A na pokračování B. Počáteční B1
  a A1 v horních skocích jsou proto správně prohozeny. Volání v
  horní půlce samo přeskakuje dolní půlku volacího slova: to je
  výslovná nativní sémantika return-jump, nikoli chyba této vazby.

**5 — checked.** Je třeba uchovávat dvě hodnoty. Při opuštění IN
se uloží rA do HOLDAIN a obnoví HOLDAOUT; při opuštění OUT se uloží
HOLDAOUT a obnoví HOLDAIN. Tím má každá korutina vlastní snímek A.
Před prvním vstupem se počáteční hodnota příslušného uloženého A
určí stejně jako jiné počáteční údaje korutiny. Odpověď uvádí obě
dvojice instrukcí na správných místech před OUTX a INX.

**6 — checked with known typo.** Pro orientovaný přechod i -> j
nejprve STJ uloží návrat do slotu iX a následný JMP vykoná jX.
V zobrazeném rozvržení má 6 přechodů dohromady 12 slov: sloty AX,
BX a CX jsou současně některými z těchto JMP. U libovolné
posloupnosti přechodů se mění právě pokračování opouštěné korutiny;
všechna ostatní jsou nedotčena. Při m možných orientovaných
přechodech jde o 2m slov; úplná síť má m=n(n-1).

Číselnou mez 3n+2 pro kompaktní vazbu lze doložit rezervováním I1
jako ukazatele na slot právě aktivní korutiny. Pro každou korutinu i
stačí tři slova

```
Ei  STJ 0,1
    ENT1 Xi
Xi  JMP start_i
```

a společné dvě inicializační instrukce `ENT1 Xinitial; JMP start_initial`.
Volání má stále tvar JMP Ei. První instrukce uloží opouštěné
pokračování přes staré I1, druhá nastaví novou aktivní korutinu a
třetí vykoná její uložené pokračování. Tato konkrétní realizace
spotřebuje I1; obecné tvrzení v poznámce nevyžaduje jeho zachování.
Oprava z 28. 12. 1997 pouze doplňuje chybějící slovo „hard“.

**7 — checked by an independently written full MIX solution.** Na
s. 529 není tištěná odpověď 7. Úplný vlastní program je v
`../coroutine_programs.py`, proměnná ENCODER, a pro přímé čtení v
`../results/inverse-encoder.mixal`. Používá shodný NEXTCHAR pro karty
se skupinami po třech znacích, potom kóduje nejdelší souvislé úseky
stejného znaku. Výstup plní všech 80 míst karty a končí tečkou.

Nechť souvislý úsek znaku c má délku n=10q+r, 0 <= r <= 9. Každých
deset znaků zapíšeme `9c`. Zbytek délky jedna zapíšeme samotným c,
pokud c není číslice; jinak zbytek zapíšeme dvojicí `(r-1)c`.
Samostatná číslice musí být zapsána jako `0c`. Tečku zapíšeme přímo.
Minimální počet znaků pro jeden úsek je tedy

```
číselný znak:   2 ceil(n/10),
jiný znak:     2q + min(r,2).
```

Důkaz optimality: jedna přípustná vstupní jednotka vytvoří jen
souvislý úsek téhož znaku, takže nepřekročí hranici dvou různých
znaků. Pro číselný znak stojí každá jednotka dva znaky a vydá nejvýše
deset. Pro ostatní znaky stojí přímý výskyt jeden znak a vydá jeden;
dvojice stojí dva a vydá nejvýše deset. Kód délky t proto vydá
nejvýše `10 floor(t/2) + (t mod 2)` stejných nečíselných znaků.
Inverzí této meze dostaneme uvedený vzorec. Konstrukce jej dosahuje
pro každý úsek. Za tečkou se nic nečte a samotná tečka má minimální
cenu jedna. Součet nezávislých minim je proto globálním minimem.

Program drží délku aktuálního úseku v I5 pouze do 10; plnou desítku
ihned vydá, takže ani velmi dlouhý úsek nepřeteče. Při odlišném znaku
uloží tento další znak do LOOKAHEAD, vydá předchozí úsek a obnoví jej.
PUTCHAR postupuje přes pět jednobajtových polí každého z 16 slov;
pole F mají hodnoty 9,18,27,36,45, všechny přípustné i pro b=64.
Před opětovným použitím plného bufferu čeká JBUS. Uložené návraty
EMITRUN a PUTCHAR jsou oddělené. Při tečce na posledním místě plné
karty nevydá navíc prázdnou kartu. Vzorový minimální výstup je
`A2B5E3426FGZYW3210PQ89R.`.

## Errata, inventář a konečná kontrola

Z původní s. 200 je potvrzeno přesně sedm cvičení; odpovědi 1–6 jsou
na s. 529 a vlastní řešení úlohy 7 je doloženo výše. Žádné nové
cvičení do §1.4.2 není ve čtyřech kontrolovaných vrstvách errat.
Nové odpovědi na s. 527 patří §1.3.3, nikoli §1.4.1 či §1.4.2.

Známé opravy: s. 194 rJ (19. 12. 2001); s. 195 mezery v příkladu
(13. 6. 1999); s. 196 „three-character groups“ (14. 6. 1999);
s. 196 explicitních pět mezer v ALF a s. 197 I4 ve výstupním
kontraktu (obě 28. 2. 2018); s. 198 UNIX (9. 7. 1997) a filtry
B,C,D (22. 7. 1997); s. 529 odpověď 3 (17. 7. 2006) a chybějící
„hard“ v odpovědi 6 (28. 12. 1997). Přesné vyhledávání podle stran
i témat je v `../results/errata-search.json`; zobrazeny příslušné
originální PDF stránky všech čtyř vrstev a prohledán i aktuální TeX.

`../check_coroutines.py` provedl 9 398 úspěšných kontrol. Výsledek
je uložen v `../results/coroutines.json`: 222 případů původního
dekodéru, 222 opravené optimalizace, tři případy ztráty prvního znaku,
1 006 případů optimálního encoderu a 12 přechodů tří korutin.
Kontroly běží v bázích 64 a 100, včetně nenulových latencí I/O,
hranic karet, všech znakových kódů a všech replikačních číslic.
Pro encoder se délka výsledku porovnává s nezávislou dynamickou
optimalizací přes všechny přípustné jednotky kódu, nikoli jen se
stejným hladovým algoritmem. Konečné testy doplňují obecné důkazy;
nejsou vydávány za vyčerpání všech vstupů. Úspěšné běhy se neopakovaly.

Výsledek: celý přidělený oddíl je zkontrolován v popsaném rozsahu.
Nový neopravený rozpor zde nebyl doložen.
