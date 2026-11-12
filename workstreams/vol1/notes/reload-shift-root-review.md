# Obrácení bajtů: nezávislá kontrola certifikátu X0700

2. listopadu 2026. Root přečetl celou novou poznámku podagenta,
generátor stavů i souhrnný výsledek. Čtyři soubory z
`parallel/mix-optimality/results/reload-shift-manifest.json`
jsou zmrazené; jejich hashe souhlasí.

Výsledek se týká jediné přesně vymezené rodiny: průchod obnoví
pětibajtový registr A z původního vstupu a provede jeden posun;
po posledním průchodu je dovolen ještě jeden posun. Posun může
pracovat jen s A, nebo se spojenými registry A a X, doleva či
doprava, s doplněním nul nebo kruhově. Druh i délka posunu
smějí záviset na vstupu a měnit se mezi průchody. Rodina nedovoluje
aritmetiku, jiné načítané slovo ani druhý posun uvnitř průchodu.

Protipřípad používá radix64 a deset odlišných nenulových bajtů:
vstup1,2,3,4,5 a počáteční X6,7,8,9,10. Symboly v certifikátu
je pouze přejmenovávají. S nulovým bajtem je jedenáct symbolů;
protože A se obnovuje, budoucí stav určuje jen pět pozic X.
Konečný úplný uzávěr těchto stavů tak pokrývá i neomezený počet
průchodů. Nejde o limit délky zkoušených programů.

Root napsal samostatný validátor
`verify_reload_shift_certificate.py`. Neimportuje ani nespouští
agentův generátor. Každý posun reprezentuje mapou deseti výstupních
souřadnic na deset vstupních souřadnic nebo zvláštní nulovou
souřadnici. Tím nezávisle kontroluje všechny posuny délek0–10;
větší nekruhové délky již dávají stejné nuly a kruhové závisejí
jen na zbytku modulo10. Původní program používá řezy řetězců.

Validátor ověřil tyto skutečnosti nad uloženým certifikátem:

- počáteční X je přítomno a všech983 stavů je dosažitelných;
- všech64 878 přechodů zůstává v množině stavů;
- jejich obrazy jsou přesně všech22 426 uložených dvojic A/X;
- žádná dvojice nemá obrácený vstup v A;
- žádná z1 480 116 možností závěrečného posunu jej také nevytvoří.

Výsledek je v `results/reload-shift-independent-review.json`.
Kontrola uzavřenosti sama již stačí pro vyloučení všech konečných
běhů; dosažitelnost navíc ověřuje tvrzenou přesnost seznamu.
Znaménka nemohou napravit nesprávné pořadí velikostních bajtů.

Přijat je tedy úplný záporný výsledek pro tuto konstrukční rodinu.
Nejde o globální dolní mez sedmi proti osmi slovům v úloze23.
Původní úloha zůstává partial; výsledek pouze vylučuje konkrétní
cestu ke zkrácení Dixonovy smyčky. Nebyly opakovány staré úspěšné
MIX testy; nový certifikát dostal jednu nezávislou validaci.
