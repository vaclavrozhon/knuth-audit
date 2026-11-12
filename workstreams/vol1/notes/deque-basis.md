# §2.2.1-13: báze zakázaných vzorů a stav literatury

V1-X0019, 1. listopadu 2026. **Částečná kontrola:** přesný přepis věty,
obecná nutnost zákazu, úplný nezávislý konečný test do n=9 a ověření
primárních odkazů. Nejde o nový nezávislý důkaz úplnosti nekonečné báze
ani o certifikaci celého citovaného lineárního rozhodovacího programu.
Tyto meze jsou výslovně ponechány v mapě auditu.

## 1. Přesné tvrzení a zdroj

Permutace obsahuje vzor p, jestliže některá její podposloupnost má stejné
vzájemné pořadí hodnot jako p; podposloupnost nemusí být souvislá.
Věta na s. 539 zakazuje pro každé k>=1 dva vzory délek 4k+1 a 4k+3:

```text
5,2,7,4,...,4k+1,4k-2,3,4k,1;
5,2,7,4,...,4k+3,4k,1,4k+2,3,
```

a v obou případech též varianty se záměnou posledních dvou pozic,
hodnot 1 a 2, nebo obojího. Přesně tato věta je v článku
[V. R. Pratt, STOC 1973, s. 273–274](https://sites.math.washington.edu/~billey/japan/references/p268-pratt.pdf).
Pratt ji zapisuje rotací lichých položek identity o dvě místa doleva
a při sudém (d-5)/2 ještě záměnou hodnot 1 a 3, kde d je délka.
Sudé položky zůstávají beze změny. Rozdělení na d=4k+1 a d=4k+3
dává právě knižní zápis. Kontrola obou konstrukcí pro liché délky
5 až 101 navíc prošla doslovným porovnáním.

Originální stránky článku 273–274 jsou uloženy jako
`images/pratt-1973-file006.png` a `file007.png`; byly zobrazeny.
Celý článek a jeho hash jsou v `sources/pratt-1973-deques.*`.

## 2. Proč tyto vzory nelze získat

Vklady lze odkládat do okamžiku, kdy jsou potřebné pro příští výstup:
vynechání dosud nepoužitého prvku nebrání odběru jiného prvku z konce.
Takto redukovaná historie je určena bloky vstupů před novými maximy
výstupu. Samotné maximum lze vložit a hned odebrat na kterémkoli konci.

U základního vzoru po vložení 1,...,4 a průchodu 5 musí být možno
odebrat 2. Pořadí vytvořené samotnými vklady na konce je klesající
směrem k 1 a rostoucí od 1. Proto jediná možnost s 2 na konci je
2134 nebo její zrcadlový obraz. Po odběru 2 zbývá 134, až na zrcadlení.

Aby po průchodu 7 mohl odejít 4, musí se nový prvek 6 vložit na
opačný konec; zbude 613. Aby po průchodu 9 mohl odejít 6, musí se 8
vložit na opačný konec; zbude 138. Tato vynucená alternace pokračuje.
Jádro 1,3 zůstává uvnitř a poslední sudé číslo leží střídavě na jednom
konci. Při délce 4k+1 je následující požadovaná 3 zablokovaná mezi 1
a posledním sudým číslem; při délce 4k+3 je obdobně zablokovaná 1.
Prohození posledních dvou výstupů tuto dřívější překážku neodstraní.
Při prohození hodnot 1 a 2 se stejný argument vede s jádrem 2,3.

Pokud větší permutace obsahuje některý z těchto vzorů a měla by legální
historii, vymazáním operací ostatních prvků bychom získali historii
zakázaného vzoru. Proto je také nedosažitelná. Tím je dokázán jeden
směr věty pro všechny velikosti.

Prattův opačný směr sleduje zpětně nejlepší částečnou historii od prvního
zablokovaného prvku a izoluje střídající se řetěz nucených vkladů.
Přečteny definice na s. 271–272 a důkaz na s. 273–274. V této dávce
je však tento směr stále závislý na publikovaném důkazu; vlastní úplný
rozpis jeho případů není hotov. Konečný test níže tuto mezeru nenahrazuje.

## 3. Nezávislá konečná kontrola

`check_deque_basis.py` porovnává dva modely:

- přímé všechny operace deque, bez redukovaných historií a bez vzorů;
- vyhýbání se vzorům, ověřované rekurzivně odstraněním každé hodnoty
  a přeznačením zbývajících hodnot na 1,...,n-1, spolu s kontrolou
  nových zakázaných vzorů přímo v délce n.

Druhý model je úplný: každý kratší vzor je obsažen v některém odstranění
jednoho prvku. Výsledné množiny, nejen počty, souhlasí pro všech
409 114 permutací velikosti 0 až 9. Počty dosažitelných jsou

```text
1,1,2,6,24,116,634,3762,23638,154816.
```

Všechny bázi odpovídající permutace délek 5,7,9 jsou zároveň minimální:
každé odstranění jediného prvku už dává dosažitelnou permutaci.
Běh trval přibližně 12 sekund, skončil úspěšně a použil nejvýše
538 MiB podle ru_maxrss. Výsledky: `results/deque-basis.json`;
průběžný log: `results/deque-basis-run.log`.

## 4. Pozdější vývoj a problém citovaného algoritmu

Odkaz v zadání na Rosenstiehla a Tarjana, J. Algorithms 5 (1984),
s. 389–390, je potřeba číst s pozdější opravou. Denton popisuje
protipříklad 254163 a opravu údržby spodní dvojice zásobníků po odběru
v [§4 své práce z roku 2012](https://arxiv.org/abs/1208.1532).
Protipříklad se týká třídění vstupní permutace do identity; náš operační
model naopak vytváří výstup z identity. Tyto konvence se převádějí
inverzí permutace a nesmějí se zaměnit. Jde o zveřejněný problém
citovaného článku, nikoli o nově nalezenou chybu charakterizační věty.
V Knuthových prohledaných erratech k s. 243/539 tento doplněk nalezen nebyl.

Počítání se od prvního dotisku posunulo: Elvey Price a Guttmann dávají
vytvářející funkci počtů deque permutací prostřednictvím funkce pro dva
paralelní zásobníky; viz [jejich Theorem 3.9](https://arxiv.org/abs/1508.02273v2).
Elvey Price následně dokazuje rovnost příslušných růstových konstant
v [práci z roku 2019](https://arxiv.org/abs/1912.00056).
Tato bibliografická zjištění neznamenají, že jsme zde nezávisle ověřili
všechny důkazy těchto článků nebo přesnou konstantu asymptotického růstu.
Není správné prezentovat úlohu jako stále zcela nevyřešenou na základě
prvního dotisku nebo samotného článku z roku 2012.

Tři pozdější články jsou uloženy ve vlastním `sources/`, včetně URL,
data a hashů v `deque-literature-metadata.json`. Prohledány všechny
historické i aktuální vrstvy Knuthových errat podle stránek a názvů
Pratt, deque, Rosenstiehl, Tarjan a Denton. Nová potvrzená chyba knihy
z této kontroly nevzešla.

## Aktualizace stavu 2. listopadu 2026

Starší průběžné výhrady této poznámky k úplnosti důkazu jsou
vyřešeny v X0219 (Prattova postačitelnost) a X0664 (opravený
lineární deque program). Historická mez původního článku
Rosenstiehl–Tarjan 1984 zůstává v X0220. Přesné propojení je
v `deque-followup-root-review.md` a `inventory-reconciliation.md`.
Výše zachovaný pracovní text není aktuálním soupisem otevřených
matematických bodů.
