# §1.1: algoritmy E/F, průměry a přepisovací model

V1-X0022, kontrola 1. listopadu 2026. Zobrazen hlavní text s. 1–9,
zadání devíti cvičení na s. 9, odpovědi s. 466–467 a čtenářská procedura
na s. xiii–xiv. Tato poznámka pokrývá základní matematiku a cvičení 1–8;
simulace a závěrečná poznámka cvičení 9 jsou v `simulation.md`.
Historická část a hlubší asymptotika z jiného svazku zůstávají samostatnými
závislostmi, proto hlavní text celé sekce ještě není označen jako hotový.

## 1. Algoritmus E, schéma a jeho stavový model

Pro kladná celá m,n je gcd(m,n) největší kladné celé číslo d, které dělí
obě. Dělení se zbytkem dává m=qn+r s 0<=r<n. Dělitelé společní m,n
jsou přesně dělitelé společní n,r. Pokud r=0, je odpověď n; jinak se
dvojice změní na (n,r). Druhá složka je kladná a striktně klesá, takže
algoritmus skončí a zachovává gcd. Obrázek na s. 3 má správné větvení
i návrat. Výklad pořadí přiřazení a pomocné proměnné při výměně je správný.

Pro vstup (119,544) jsou po jednotlivých děleních zbytky
119,68,51,17,0. Odpověď 17 je správná. Přídavný krok E0 při m<n
ušetří první dělení se zbytkem m; poznámka o „asi polovině případů“
vyžaduje přibližně symetrické rozdělení obou vstupů, nejde o univerzální
pravděpodobnost pro každé rozdělení.

Počet kroků není omezen společnou konstantou: definujme F_1=F_2=1,
F_(k+1)=F_k+F_(k-1). Euclidův algoritmus na (F_(k+1),F_k) sestupuje
po těchto číslech, takže lze vynutit libovolně mnoho dělení. Geometrická
varianta na nesouměřitelných délkách nemůže skončit: zpětným dosazením
z posledního nulového zbytku by obě původní délky byly celočíselné
násobky jediné délky, tedy měly racionální poměr.

Formální metoda (Q,I,Omega,f) používá množinu stavů Q, vstupní stavy I,
koncové stavy Omega a přechod f:Q->Q. Koncové stavy jsou pevné body.
V příkladu (2) mají fáze 1 a 2 nezáporný pomocný zbytek; fáze 3 používá
kladný pomocný parametr. Všechny uvedené přechody jsou v těchto oborech
definované a přesně odpovídají E1,E2,E3. Počáteční a koncový pomocný
krok mění jen formalizaci, nikoli vypočtený gcd.

## 2. Cvičení 1–4

1. Pět přiřazení t<-a, a<-b, b<-c, c<-d, d<-t provede cyklický posun.
   Pro čtyři nezávislé původní hodnoty je pět minimum v uvedeném modelu
   jednotlivých přiřazení: každá ze čtyř cílových proměnných se musí
   změnit. Při pouhých čtyřech krocích by první z nich už dostala svou
   konečnou hodnotu a její vlastní původní hodnota by nebyla nikde
   uložena, přestože ji některá pozdější cílová proměnná ještě potřebuje.
2. Při každém návratu k E1 je nová dvojice (staré n,staré r), kde
   0<r<n. Proto po prvním dělení vždy platí m>n.
3. Algoritmus F střídá m<-m mod n a n<-n mod m, po každém kroku testuje
   nulový zbytek. Dvojice se vyměňují pouze významem názvů, nikoli
   kopírováním. Každé dělení odpovídá následujícímu dělení E; nulou se
   nedělí, protože test předchází příštímu dělení. Počet dělení je stejný.
4. Pro (2166,6099) jsou nenulové druhé složky
   6099,2166,1767,399,171,57, další zbytek je 0. Tedy gcd=57.

## 3. Čtenářská procedura (cvičení 5)

Krok 18 bezpodmínečně vrací ke kroku 3, takže neexistuje ukončení ani
po přečtení všech kapitol. Rozhodování podle zajímavosti, únavy či
spokojenosti s řešením není přesně určeno. Pokyny řešit a kontrolovat
obecné matematické úlohy nedávají konečný mechanický postup pro každý
jednotlivý krok. Chybí tedy konečnost, určitost a efektivnost v knižním
smyslu; případný požadovaný výstup není specifikován jako funkce vstupu.
V typografii chybí písmenná označení kroků, stručné popisky v hranatých
závorkách a koncová značka. Odpověď souhlasí se skutečnou procedurou.

Errata z 25. prosince 2010 správně zpřesňují „v předmluvě“ na „za
předmluvou“ a „ve třech“ na „alespoň ve třech“ požadavcích. Nejde
o nový nález. Úlohou se neuděluje souhlas k odesílání zpráv autorovi;
čtenářská procedura je zde pouze předmětem kontroly.

## 4. Průměry T_n a U_m (cvičení 6–7)

Nechť L(m,n) je počet dělení v E. Pro pevné n závisí L(m,n) jen na
zbytku m modulo n: po prvním dělení pokračuje tentýž výpočet, nebo
v obou případech skončí. Proto má posloupnost L(1,n),L(2,n),...
periodu n. Její Cesàroův průměr, tedy limita aritmetických průměrů
prvních M členů pro M->infinity, existuje a je
T_n=(1/n) sum_(m=1)^n L(m,n).

Pro n=5 jsou počty 2,3,4,3,1, tedy T_5=13/5=2,6. Pro pevné m
a každé n>m platí L(m,n)=1+L(n,m), protože první nulový podíl pouze
obrátí dvojici. Změna konečně mnoha členů nemění Cesàroův průměr,
a periodičnost L(n,m) tak dává U_m=1+T_m; zvlášť U_5=18/5.
Není potřeba neexistující rovnoměrné pravděpodobnostní rozdělení na
všech kladných celých číslech.

Dodatky `all1-pre` z 10. srpna 2014 a 28. prosince 2017 tuto
periodičnost ilustrují; číselné odpovědi se nemění.

## 5. Doslovná přepisovací tabulka (cvičení 8)

Stav tvoří konečné slovo nad {a,b,c} a číslo instrukce 0,...,5.
Instrukce hledá nejlevější výskyt vzoru; nalezený výskyt přepíše a skočí
na b_j, jinak skočí na a_j. Prázdný vzor se nalézá na začátku slova.
Tabulka na s. 467 má sloupce b_j,a_j právě v tomto pořadí.

Pro vstup a^m b^n s m,n>0 instrukce 0 a 1 opakovaně mění
c^t a^(m-t)b^(n-t) na c^(t+1)a^(m-t-1)b^(n-t-1). Po min(m,n)
opakování už podslovo ab není přítomné. Instrukce 2 změní zbylá a na b,
instrukce 3 změní všechna c na a. Výsledkem je

```text
a^min(m,n) b^|m-n|.
```

Pokud druhý exponent vymizel, instrukce 4 přejde do koncového stavu 5.
Jinak se vrátí na 0 s novou kladnou dvojicí (min(m,n),|m-n|).
Gcd se zachovává, součet exponentů striktně klesne na max(m,n), takže
nakonec zůstane přesně a^gcd(m,n). Jednotlivé vnitřní smyčky také
skončí, neboť zkracují slovo nebo počet přepisovaných písmen.
Předpoklad m,n>0 patří k zadání; libovolná chybná vstupní slova se
tímto důkazem necertifikují. Dodatek o lexikografickém poklesu m,n
z 29. dubna 2013 je správný.

## 6. Výpočty, errata a dosud otevřený rozsah

`check_algorithms.py` ověřil všech 4096 dvojic 1<=m,n<=64 porovnáním
E, F a doslovné přepisovací tabulky s nezávislým hledáním největšího
společného dělitele mezi všemi kandidáty. Kontrola přepisu nepoužívá
odvozený makrokrok z oddílu 5. Nejdelší ověřený přepis měl 697 kroků.
Perioda počtu dělení a konkrétní číselné odpovědi rovněž souhlasí.
Výsledky a další kontroly simulace jsou v `results/algorithms.json`.

Prohledány všechny vrstvy errat pro s. 1–9,466–467 i témata Euclid,
Markov, representation, equivalence. Vedle výše uvedených oprav jde
o drobná zpřesnění společných dělitelů, zápisu funkce na dvojici,
prázdného slova, množiny vstupů a bibliografie. Dvě podstatné úpravy
simulace jsou vedeny odděleně v `simulation.md`.

Hlubší asymptotika T_n~(12 ln(2)/pi^2) ln(n), odkazovaná na §4.5.3
svazku 2, potřebuje samostatné ověření zdroje; není prokázána malým
výčtem. Historická tvrzení o názvu algoritmus, raných slovnících a
Markovově modelu také nejsou uzavřena pouhým přečtením této sekce.
Konečnost obecného šachového algoritmu se zkontroluje u §2.2.3-28.
