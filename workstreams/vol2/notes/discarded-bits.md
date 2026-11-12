# §3.6-14: vynechávání a adaptivní test

Původní zadání193 a odpověď603–604 byly přečteny vizuálně. Posloupnost
X splňuje X_j=X_(j−100)+X_(j−37) modulo2. Výstup Y ponechává prvních
100 bitů každého bloku délky d; v hlavním příkladu d=200. Index bitu
Y_i v původní posloupnosti je

```
f_d(i)=d floor(i/100)+(i mod100).
```

V jednom pokusu se přečte100 bitů; je-li mezi nimi nejvýše40 jedniček,
přečte a vypíše se ještě jeden bit. Poloha p začátku pokusu modulo100
se proto nezmění při neúspěšném pokusu a zvětší o1 při výpisu.
Fáze vypsaných bitů se cyklicky střídají, fáze začátků pokusů však
nejsou tímto pozorováním dokázány jako rovnoměrné.

## 1. Přesné lineární vztahy

Dvojím použitím rekurence je

```
X_(n+200)=X_n+X_(n+126)
          =X_n+X_(n+26)+X_(n+89) modulo2.
```

Pro p>=74 jsou oba členy prvního vztahu v předchozím100bitovém okně
Y, takže Y_(i+100)=Y_i+Y_(i+26). Pro p<=10 platí obdobně trojčlenný
vztah Y_(i+100)=Y_i+Y_(i+26)+Y_(i+89). Počty26 a11 správné.

Obecná expanze začíná u_1=126 a má
u_(j+1)=u_j−37+100[u_j<100]. Zde hranatá závorka znamená1, pokud
podmínka platí, jinak0. Pro u_j>=100 se člen X_(n+u_j) rozloží na
X_(n+u_j−100)+X_(n+u_j−37); pro u_j<100 použijeme rekurenci obráceně
a dostaneme X_(n+u_j+100)+X_(n+u_j+63). V obou případech se jeden
člen odloží a druhý zůstane jako nový X_(n+u_(j+1)). Proto pro k>=2

```
X_(n+200)=X_n+sum_(j=1)^(k−2) X_(n+v_j)+X_(n+u_(k−1)),
v_j=u_j−100 pro u_j>=100, jinak u_j+100.
```

### C0074: chybějící posun v posledním indexu na604

V sazbě posledního členu obecné expanze chybí n. Již k=2,n=1 dává
nepravdivé X_201=X_1+X_126. Zvolíme-li počátečních100 bitů nulových
kromě X_27=1, dostaneme X_201=1,X_1=X_126=0 a X_127=1. Správný
poslední člen je X_(n+u_(k−1)).

Pro t=100−p jsou dostupné indexy

```
[n,n+t) sjednoceno s [n+100+t,n+200).
```

Zvětšený výřez originálu potvrdil, že sazba správně používá
„>=n+100+t“. OCR ztrácí dolní čárku; tento kraj není chyba knihy.
Například p=74,t=26 používá právě krajní člen X_(n+126).

## 2. Nezávislé ověření všech fází

Každý X_j je lineární funkce100 počátečních bitů. Verifier reprezentuje
tuto funkci100bitovou maskou a vytváří masky obyčejnou rekurencí.
Gaussova eliminace pak určí, zda je následující bit v lineárním obalu
předchozích100 a jak jej vyjádřit. Hodnost je počet nezávislých
lineárních funkcí; nemusí být100. Všechny vztahy mezi předchozími bity
se rovněž uchovávají. Nejkratší vyjádření následujícího bitu se získá
přidáním každého takového vztahu k jednomu nalezenému vyjádření.
Nejde tedy o výběr náhodného řídkého řešení.

Pro d=200 jsou počty délek vztahů přesně

```
k:       2  3  4  6  9 12 20 28 47 74 99
počet:  26 11 26 11 11  4  4  3  1  1  1.
```

Zbývající fáze p=37 má hodnost99 a další bit je nezávislý na okně,
pokud počáteční stav volíme rovnoměrně. Jediný vztah v okně je součet
všech100 bitů rovný0. Dostaneme jej také úplným cyklem u: u prochází
všech100 hodnot63..162, protože gcd(37,100)=1. Odložené členy mají
indexy0..62 a163..199; po návratu téhož zbývajícího členu se jejich
součet musí rovnat0. Pro p=36 vzniká99členný vztah z odpovědi.

Pro d=300,400,1009 souhlasí všechny vytištěné začátky soupisů:
26 vztahů délky5/22 délky6/19 délky10;15 délky3/37 délky6/15 délky9;
a17 délky7/10 délky11/2 délky12. Úplné soupisy jsou v JSON.
Při d=1009 jsou však některá předchozí okna až o9 rozměrů závislá.
Počet členů v jednom vztahu proto sám neurčuje jeho podmíněnou
pravděpodobnost podle binomického vzorce níže.

## 3. Pravděpodobnosti a rozsah modelu

Nejprve předpokládejme100 nezávislých spravedlivých bitů. Označme
S=sum_(i=0)^40 binom(100,i) a q=S/2^100. Pro paritu pevně určených
k bitů, podmíněnou celkovým počtem jedniček nejvýše40, je pravděpodobnost
liché parity přesně

```
p_k = sum_(i=0)^40 sum_(j odd) binom(k,j)binom(100−k,i−j) / S.
```

Stačí spočítat, kterých j jedniček leží ve vybraných k pozicích.
To dokazuje vytištěný vzorec. Malý k způsobí závislost příštího bitu
na převaze nul: zejména sudá parita dvou bitů je častější než lichá.
Jde o konkrétní mechanismus požadovaný v zadání, nikoli o předpoklad
že pseudonáhodný proud jsou nezávislé hody.

### C0075: chybějící pravděpodobnost výpisu

Průměr vytištěných p_k s uvedenými vahami a s1/2 za zbývající fázi je

```
bar_p=0.4936962823889473608895652705...
q=0.02844396682049039583518215156...
```

Na604 se uvádí10^6 bar_p≈14043, ale levá strana je493696.282388947...
Teprve10^6 q bar_p=14042.6806756707... odpovídá uvedenému číslu.
Doplnění q rovněž dává28443.9668204904 výpisů a14401.2861448197 nul,
což reprodukuje další dvě čísla z odpovědi. Je to oprava číselného
výrazu v použitém přibližném modelu; sama o sobě nedokazuje přesnou
střední hodnotu skutečného adaptivního experimentu.

Tuto kvalifikaci nelze vynechat. V rovnoměrném100bitovém počátečním
stavu má okno při p=37 nutně sudou paritu. Pravděpodobnost výpisu je
pak2 sum_(i even,i<=40) binom(100,i)/2^100, ne q. Pokud pro každou
fázi losujeme nový nezávislý stav a fáze rovnoměrně průměrujeme, dostaneme
pravděpodobnost výpisu0.0285090300207602... a společnou pravděpodobnost
výpisu jedničky0.0140752122758056.... To jsou přesné hodnoty jiného,
jasně vymezeného experimentu, nikoli opravené přesné průměry původního
milionu navazujících pokusů. Adaptivní spotřeba v původním experimentu
může změnit podmíněné rozdělení stavu při další návštěvě fáze.

Stejně při d=1009 má fáze83 sedmičlenné vyjádření příštího bitu, ale
hodnost předchozího okna je95. V rovnoměrném počátečním stavu vychází
podmíněná pravděpodobnost0.5000004471961484..., zatímco vzorec p_7
pro nezávislé předchozí bity dává0.5000004499182895.... Rozdíl je malý,
ale prokazuje, že vytištěná forma závisí na aproximaci, ne jen na
správné délce lineárního vztahu. Nevedeme tento rozdíl jako další
samostatný nález; explicitní chybějící normalizace je C0075.

Zadaný binomický ocas pro28482 nezávislých spravedlivých výstupů je
přesně sum_(i=0)^13955 binom(28482,i)/2^28482. Vyhodnocení dává
0.000357861717654307519..., tedy uvedených0.000358 správně. Při prahu75
nul je binomický model výpisů0.281814101710270... na milion pokusů,
takže0.28 rovněž souhlasí. Jde o nulový model nezávislých bitů.
Původní seed a přesný běh, který dal14527/13955, nejsou v zadání uvedeny;
jejich historická reprodukce se netvrdí.

## 4. Přesný výpočet pro závislé bity a validace

Nechť A je matice100 pozorovaných lineárních funkcí a C její obraz:
možné100bitové vektory okna. Při rovnoměrném počátečním stavu je
rozdělení na C rovnoměrné. Duální prostor D tvoří masky d, jejichž
skalární součin se všemi c v C je0 modulo2; to jsou právě nalezené
paritní vztahy. Součet znaků splňuje

```
1_C(y)= (1/|D|) sum_(d in D) (−1)^(d·y).
```

Pro masku s w jedničkami definujme

```
K_i(w)=sum_j (−1)^j binom(w,j)binom(100−w,i−j).
```

Je to součet znaku přes všechny vektory y s i jedničkami. Následně

```
Pr(weight(Y)<=h)=2^−100 sum_(d in D) sum_(i=0)^h K_i(weight(d)).
```

Po přidání řádku pro následující bit stejný vzorec s101 souřadnicemi
a pevným posledním bitem1 dává společnou pravděpodobnost s výpisem
jedničky. Toto je obecný důkaz metody verifieru, bez předpokladu plné
hodnosti. Včetně nulového počátečního stavu používáme rovnoměrné2^100
stavy; jeho případné vyloučení má výslovnou malou opravu: odečte se
jedna od počtu spouštějících stavů a od celkového počtu stavů, nikoli
od počtu vypsaných jedniček.

Nezávislý vyčerpávající model přímo vypočítal všechny bitové hodnoty
pro30848 malých stavů ve116 fázových případech. Souhlasí přesné
pravděpodobnosti vypočtené pomocí duálního prostoru. Poté bylo
zpracováno400 skutečných fází a binomický ocas bez normální aproximace.
První pokus verifieru nesprávně vyžadoval plnou hodnost všech oken1009;
po vyhodnocení tohoto neplatného testovacího předpokladu se kontrolují
minimální délky napříč všemi paritními vztahy. Již úspěšné malé modely
se neopakovaly. Všechny tři bloky nyní prošly.

Prohledány všechny čtyři vrstvy errat i uložený aktuální TeX podle604,
indexů a pravděpodobností; žádná oprava C0074/C0075 nenalezena.
Známé změny u úlohy15 jsou jiné. Fyzický novější tisk a prvenství
neověřeny; žádné hlášení nebylo odesláno.
