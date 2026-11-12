# §2.2.3: topologické třídění a diagnostika cyklu

Pokrývá hlavní text s.261–268, obrázky6–9, Algorithm/Program T,
matematickou část úloh11 a16–24. Úloha25 je oddělena jako práce
s vnější pamětí. Všechny uvedené původní stránky i odpovědi546–549
byly přečteny z obrazů. Historické priority mají vlastní zdrojový stav.

## 1. Obecný důkaz T

Vstup je konečná posloupnost hran j→k na vrcholech1,...,n.
Hrana znamená požadavek, aby j předcházelo k. Souběžné hrany
se počítají s násobností. Topologické pořadí je permutace vrcholů,
v níž zdroj každé hrany stojí dříve než její cíl.

V T1–T3 je po přečtení libovolného počtu hran COUNT[k] přesně
počet dosud přečtených hran s cílem k. TOP[j] ukazuje na seznam
všech dosud přečtených hran se zdrojem j, v opačném pořadí jejich
čtení. Nový uzel se přidá pouze do jednoho seznamu, takže seznamy
hran jsou disjunktní. Tato vlastnost plyne indukcí přímo z T3.
Po vstupní fázi proto odpovídají skutečným stupňům a sousedům.
Obrázek8 souhlasí s deseti hranami(18), zvláště TOP[7]=(4,5)
a TOP[9]=(5,2), nikoli opačně.

Na začátku každého T5 platí:

* Již vypsané vrcholy mají všechny své předchůdce dříve ve výstupu.
* Pro dosud nezařazený vrchol k je COUNT[k] počet hran přicházejících
  z dosud nevypsaných vrcholů.
* Fronta od F do R obsahuje přesně dosud nevypsané vrcholy
  s nulovým aktuálním počtem předchůdců, každý právě jednou.
* U již zařazených vrcholů smí být bývalé pole COUNT využito
  jako QLINK; žádná ještě nezrušená hrana do nich nevede.
* QLINK[R]=0. Pokud fronta neobsahuje žádný vrchol, F=0.

T4 nastaví tento invariant. Je-li F≠0, jeho vypsání nemůže porušit
pořadí. T6 zruší přesně všechny hrany z tohoto F a pro každý cíl
sníží jeho počet jednou za každou takovou hranu. Přechod z kladného
počtu na nulu nastane u daného vrcholu nejvýše jednou; v tom okamžiku
je zařazen do fronty. Nulová hodnota se zároveň stane jeho koncovým
QLINK, tedy QLINK[R]=0 není nutné explicitně nastavovat.
Je bezpečné přepsat COUNT: žádná dosud nezrušená příchozí hrana
již neexistuje, a nikdy proto nepřijde pozdější decrement tohoto pole.

T7 se provádí až po T6. To je důležité, když fronta před vypsáním
obsahovala pouze F: nově připojený uzel se vloží právě za tento
stále dostupný F, a T7 jej pak načte. V úloze19 to dokazuje
minimální případ n=2, hrana1→2. Předčasné `F=QLINK[F]` by
nastavilo F=0; následné připojení2 by už F neobnovilo a třídění
by neprávem oznámilo cyklus. Tištěné zdůvodnění je správné.

Každým úspěšným T5 klesne N o1. Hrana se prochází v T6 nejvýše
jednou, takže algoritmus končí v O(n+m) operacích a potřebuje
O(n+m) buněk. Jestliže při F=0 zbývá N>0 vrcholů, každý z nich
má v indukovaném zbytku předchůdce. Opakovaným přechodem
k předchůdci vznikne v konečné množině opakování, tedy orientovaný
cyklus. Pokud původní graf žádný cyklus neměl, tato situace není
možná a výstup obsahuje všech n vrcholů. Toto je zároveň důkaz
existence lineárního rozšíření konečného částečného uspořádání.

Opakované hrany (úloha21) zvýší počet i počet odpovídajících
odečtení stejným číslem. Smyčka j→j udrží alespoň jeden vstupní
stupeň kladný, a právě proto správně vede k diagnostice cyklu.
Uživatel může dodat hrany transitivně odvozené z jiných hran;
řazení se tím nestane neplatným.

Po skončení na acyklickém vstupu tvoří QLINK[0] a následující
QLINK celý vypsaný řetězec (úloha18): pole se po připojení
následníka už nemění. Poslední hodnota je0. Při cyklickém vstupu
zůstává takto propojena vypsaná část, nikoli nevypsané COUNT.

Úloha20 nahrazuje frontu zásobníkem připravených vrcholů. Volba
připraveného vrcholu nemá vliv na výše uvedený invariant stupňů;
stačí vrchol odstranit ze zásobníku před přidáváním nových.
Knižní nové T4–T6 to dělají. Složitost zůstává O(n+m), pořadí
výstupu se může změnit a zásobníkové odkazy výstup neuchovávají.

## 2. Vstupy, výstupy a přesný MIX program

Páska má100slov na záznam a dvojice se nikdy nerozdělí mezi
záznamy. Úvodní dvojice(0,n) se přeskočí; posun bufferového
ukazatele o2 zachovává zarovnání. Slovo−1 hned za bufferem
se nachází přesně tam, kde by se četla příští první složka po
50dvojicích. Záporná hodnota spustí nový IN a reset ukazatele;
nula ukončí vstup. Všechny skutečné první složky jsou kladné.
`JBUS` zaručuje, že se před dokončením IN nečte buffer.

Tabulka X[0..n] se nulová i s pomocným X[0]. Hrany se alokují
postupně za X[n]; n+m se podle předpokladu textu vejde do paměti.
Pole2:3 pro počty a čísla vrcholů stačí: obě hodnoty jsou menší
než4000 a nejmenší povolený radix dává dvěma bajtům rozsah4096.

Výstupní index rI5 je záporný počet ještě volných slov. První
výstup se zapisuje do BUFFER, po100 nenulových číslech se vydá
OUT a index se obnoví na−100. Koncová nula je zapsána před testem
ukončení a patří do posledního OUT, včetně případu n násobku100.
Před každým zápisem do sdíleného bufferu se čeká na dokončení
předchozího OUT. Poslední IOC na stejné pásce čeká na její poslední
OUT; vlastní mechanické převinutí může pokračovat při zastavení.
Neinterpretovaná slova za první nulou posledního záznamu nejsou
součástí protokolu. Případy na hranicích49/50dvojic a99/100čísel
jsou také výslovně pokryty exekucí.

MIX prochází v T4 počáteční nulové vrcholy sestupně. Proto pro(18)
dává `9123745860`, kdežto vzestupné T4 v abstraktní verzi dává
`1932745860` (úloha17). Oba výstupy splňují všechny hrany.

### Časová konvence

Označme a počet původních zdrojů, b=ceil((m+2)/50) počet vstupních
záznamů a c=ceil((n+1)/100) počet výstupních záznamů. Frekvence
u kódu platí pro n≥1 a úspěšný acyklický vstup. Všechny se získají
z toho, že každý vrchol a každá hrana jsou zpracovány právě jednou:
pozdější připojování do fronty nastane n−a krát, první prohledání
připojuje a krát, čtení vnitřního bufferu narazí na b−1 záporných
sentinelů a jednou na koncovou nulu.

Součet frekvencí s cenami instrukcí dá knižní

```
(32m + 24n + 7b + 2c + 16)u
```

při konvenci: započítat základní1u za vydání IN, OUT a IOC,
nezapočítat čekací smyčky JBUS ani konečné zastavení HLT. Tedy
nejde o součet s úplným odstraněním všech instrukcí s I/O opcode;
vynechává se vlastní přenos, čekání a zastavení. To odpovídá
skutečným počtům v knižní tabulce. Samotný CPU součet po úplném
vynechání opcode34–38 a se zahrnutím1u za HLT je
`32m+24n+6b+c+15`; vydání b+c+2 I/O operací a odebrání HLT
obnoví knižní vzorec. Tuto konvenci uvádíme výslovně, místo
abychom pokládali neurčené čekání za chybu konstanty.

Kontrolní součet jednotlivých bloků: inicializace bez IN je4n+9;
čtení a ukládání hran včetně všech IN je21m+7b−2; začátek T4
včetně IOC je4; vlastní T4 je5n+3a; zbývající bloky dohromady
11m+15n−3a+2c+5. Součet souhlasí a parametr a se vyruší.

Úloha22 správně požaduje validaci n, obou indexů a hranice poolu.
Ve skutečné implementaci je třeba testovat plné vstupní slovo
před jeho načtením do dvoubajtového registru, aby neplatné
velké číslo nevyvolalo nedefinované LDi. Také je nutné rozpoznat
ukončovací(0,0) a nepovažovat jej za běžnou hranu. Odpověď je
návrhem doplnění testů, ne tvrzením, že původní program přijímá
libovolně poškozenou pásku bez chyby.

## 3. Diagnostika cyklu, úlohy23–24

Doplněné `TOP[F]=Λ` po zachránění hlavy seznamu v T5 ponechá
v TOP pouze hrany z nevypsaných vrcholů. Při N>0 všechny cíle
těchto hran také zůstaly nevypsány; jinak by měly při zařazení
kladný stupeň. Reset QLINK a T9–T10 vyberou každému zbylému
vrcholu jednoho jeho předchůdce. Výsledek je funkce p ze zbylých
vrcholů opět do této množiny. Ostatní QLINK jsou0.

T11 najde nenulový QLINK, protože zbytek je neprázdný a každý
jeho vrchol má předchůdce. T12 sleduje p a značkuje navštívené
vrcholy v TOP. V konečné množině musí nejpozději po N+1 návštěvách
narazit na značku; od tohoto vrcholu tvoří další sledování p
prostý cyklus. T13 při tisku značky maže. Na cestě po cyklu
žádný dříve nenavštívený vrchol není, takže první smazaná značka
ukončí přesně po návratu do počátku. T14 jej zopakuje. Každá
sousední dvojice výstupu je skutečná vstupní hrana v opačném
směru. Pro smyčku na jediném vrcholu se správně vytiskne j,j.
Přípravná fáze a hledání/tisk stojí O(n+m).

MIX varianta značí TOP[k]=k namísto1; všechny možné značky jsou
kladné, takže nulové testy jsou ekvivalentní. rI1 drží značku
právě vypisovaného vrcholu a přežije převod CHAR i tisk. Tisk
před posledním testem zajišťuje zopakování počátku. JBUS chrání
překryv LINE1 a LINE2 i opětovné použití VALUE.

**Nový nesoulad:** poznámka předpovídá výstup jiného pořadí
skenování. Přesný ruční důkaz a návrh opravy jsou v
[cycle-example-output.md](cycle-example-output.md). Samotný
program24 je správný. Pro kontrolu výstupů se nesmí vyžadovat
jediný konkrétní cyklus na obecném vstupu; validátor kontroluje
skutečné hrany, prostotu a shodné první/poslední číslo.

## 4. Úlohy11 a16

Permutace řádků a sloupců matice relace podle topologického
pořadí přesune každou jedničku přísného uspořádání nad diagonálu.
Na diagonále zůstanou nuly; v reflexivní verzi by byly jedničky,
což nemění horní trojúhelníkovost. To dokazuje úlohu16.

Pro úlohu11 je množina všech pořadí určena rekurzí: první může
být právě aktuální minimální vrchol a zbytek libovolné pořadí
po jeho odebrání. Indukce podle počtu vrcholů dokazuje úplnost
i disjunktnost větví. Nezávislé rozvinutí této rekurze na grafu6
je porovnáno s množinou rozvinutou z tištěného součtu546; obě
obsahují52 různých pořadí. Tisk se dělí do disjunktních skupin
2+4·8+6·3=52. Zde je konečný úplný výčet adekvátní důkaz
konkrétního příkladu, nikoli nahrazení obecného důkazu algoritmu.
