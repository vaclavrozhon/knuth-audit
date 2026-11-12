# §4.5.4: Fermatovy algoritmy C/D, úlohy5 a7

Kontrola3.11.2026. Matematický text387–390, tabulky a úlohy5/7
jsou uzavřeny v níže vymezeném rozsahu. Historické odstavce
Fermat/Narayana/Jevons/sítové stroje a externí Lehmanova věta
zůstávají pro samostatný kontextový blok. Nejde o uzavření
celých stran ani celého oddílu.

## Rozdíl čtverců a algoritmus C

Pro kladné liché N je rozklad N=u*v,1<=u<=v, ekvivalentní
celočíselnému řešení N=X^2-Y^2 s X=(u+v)/2,Y=(v-u)/2.
Funkce X=(u+N/u)/2 na 1<=u<=sqrt(N) klesá; hledání
nejmenšího X>=sqrt(N) tedy najde největší faktor u<=sqrt(N).
Triviální rozklad1*N zaručuje konec nejpozději při X=(N+1)/2.

Proměnné algoritmu označme a=2X+1,b=2Y+1,
r=X^2-Y^2-N. Toto odlišení odpovídá známé změně jmen2004.
Inicializace X=floor(sqrt(N)),Y=0 dává -a<r<=0.
Je-li r=0, jde o čtverec a okamžitě končíme.

Jinak C3 zvyšuje X o1 pomocí r+=a,a+=2.
Krok C4 zvyšuje Y o1 pomocí r-=b,b+=2.
Známá oprava1997 vrací z C5 při r>0 do C4, nikoli C3.
Pro pevné X se tak najde nejmenší Y s X^2-Y^2<=N.
Pokud nenastala rovnost, vzroste X a pokračuje se.
Monotonicita potřebného Y umožňuje ponechat dosavadní hodnotu.

Důležitá drobnost: bezpodmínečný první C4 po C3 nepřeskočí
řešení s původním Y. Při první C3 je nový X=ceil(sqrt(N))
a nečtvercové N dává r>0. Při každé další C3 byl původní Y
nejmenší s r<0; tedy r>-(2Y-1). Nová hodnota r+(2X+1)
je kladná, protože X>Y. Žádná rovnost v tomto mezikroku
se proto neztrácí.

Dokud nenastane řešení, X<=(N+1)/2. Pro takové X existuje
vhodné Y<X, takže b<a. Po C3 je 0<r<a; po posledním
odečtení v C4 je r>-(b-2)>-a. Invariant |r|<a proto platí
při všech kontrolovaných přechodech.
Výstupní formule dává u=(a-b)/2,v=(a+b-2)/2.

Počet zvýšení X je X_final-floor(sqrt(N)), počet zvýšení Y
je Y_final. Součet je přesně v-floor(sqrt(N)), jak uvádí
text pro dominantní práci. Příklad377 dává13*29, dvě
zvýšení X a osm zvýšení Y. Tvrzení o absenci násobení/dělení
se týká těchto jednoduchých přechodů; inicializační odmocninu
lze také získat sčítáním postupných lichých čísel.

## Síta a algoritmus D

Pro modul m definujme S_m(j)=1 právě tehdy, je-li j^2-N
čtvercem modulo m. Platí S_m(-j)=S_m(j).
Proto knižní index k=(-X) mod m správně testuje kandidáta X.
Krok X+=1,k=(k-1) mod m zachovává tento invariant.
Každé skutečné řešení projde všemi síty; konečný celočíselný
test odmocniny v D4 vyloučí všechny falešné kandidáty.
X začíná na ceil(sqrt(N)) a roste, takže dokázaná
charakterizace nejmenšího X zaručuje hledaný největší faktor.
Platí to i pro N=1 a pro úplné čtverce.

Čínská věta o zbytcích ukazuje, že pro nesoudělné moduly
m_i se podmínky přesně spojují nezávisle na úplné periodě
jejich součinu. Hustota přeživších je součin jednotlivých
hustot. Přibližný komentář2^(-30) používá faktor asi1/2
z úlohy6; není to přesná pravděpodobnost pro libovolnou
sadu malých prvočísel nebo krátký interval.

Párování modulů na389 má chybný index r-k; nový
[C0150](C0150-sieve-pair-index.md). Správné dvojice jsou
m_k*m_(r+1-k) pro k<=floor(r/2); lichý prostřední modul
zůstane samostatný. Jejich čtvercový test je ekvivalentní
konjunkci původních dvou testů: kořeny lze spojit čínskou
větou, redukce složeného kořene dává opačný směr.
Snížení počtu tabulek přibližně na polovinu vysvětluje
uváděné zrychlení v modelu času úměrného počtu tabulek,
za cenu větší paměti.

## Moduly a číselné příklady

Množina čtverců modulo100 souhlasí s uvedenými zakončeními
00,e1,e4,25,o6,e9, kde e je sudá číslice a o lichá.
Ověřena celá tabulka a povolené třídy pro moduly3,5,7,8,11
při N=8616460799 i sedm tříd modulo25.
Nejmenší přípustné X je92880 a X^2-N=3199^2,
tedy N=89681*96079.

V úloze5 je11111 shodné s tímto N modulo3*7*8*11.
Modulo5 jsou přípustné X=0,1,4.
První prosátý kandidát X>=106 je144; rozdíl9625 není čtverec.
Další je156 a156^2-11111=13225=115^2,
tedy11111=41*271. Všechny mezilehlé kandidáty síta odmítnou.

Tvrzení o zvýšení informace z p na p^2 používáme pro
liché prvočíslo p nesoudělné s N, stejně jako moduly v D.
Je-li N nenulový čtverec modulo p, existují dvě třídy X
s X^2-N=0 mod p. Mezi p pokračováními každé této třídy
modulo p^2 je jen jedno, kde rozdíl dělí p^2; ostatní
mají přesně jednu mocninu p a nejsou čtverce.
U nenulového čtvercového rozdílu se každý kořen zvedne:
v (y+pt)^2 je lineární koeficient2y invertibilní modulo p.
Zbylé přípustné třídy proto neztrácejí žádné pokračování.

Počet přípustných tříd modulo p^2 je
(p^2-3p+4)/2, je-li N čtverec modulo p,
a p(p-1)/2 jinak. To dává skutečné zpřesnění právě
v prvním případě. Bez nesoudělnosti není věta v této podobě
platná: N=9,p=3 dovoluje všechny třídy modulo3 i9.
Bereme to jako potřebnou kvalifikaci v kontextu D,
nikoli nový samostatný nález.

Rychlá omezení na389 také sedí: při N mod3=2 musí X mod3=0;
při N mod9=1,4,7 jsou třídy X mod9 postupně ±1,±2,±4.
Pro N mod4=1 je X liché. Pro N mod4=3 je X sudé a
N mod8=3 nebo7 určuje X mod4=2 nebo0.
Uváděné faktory3,9/2,4,2 vyjadřují úsporu procházených tříd.

## Slovní AND a úloha7

Šířku slova označme w (v knize30).
Periodické síto modulo m lze uložit do L=lcm(m,w) bitů,
tedy W=L/w celých slov. Pro začátek bloku X_0 zvolme fázi
a=-X_0 a do bitu b slova q uložme

```
S'_m[q]_b = S_m((a+w*q-b) mod m),  0<=b<w, 0<=q<W.
```

V bloku X=X_0+w*t čteme q=-t mod W. Jelikož wW
je násobek m, tento bit znamená S_m(-X-b)=S_m(X+b).
AND několika slov tedy přesně reprezentuje průchod všech
kandidátů X,...,X+w-1 příslušnými síty.
Další blok vyžaduje q-=1 s návratem q+=W při záporné hodnotě.
Komentáře programu přičítají L místo W:
nový [C0151](C0151-sieve-word-wrap.md).

Po načtení slov a posunu X o w je třeba nenulové bity
vyhodnotit od nejmenšího b, vzhledem k původnímu X.
Kniha ukazuje jen vnitřní smyčku; přesný test D4 zůstává
součástí celého algoritmu.

Pro MIX v uvedeném modelu stojí LD1/LDA/AND/ST1 po dvou
cyklech, DEC1 a podmíněný skok po jednom; obvyklá cesta
tedy8 cyklů na modul. INCX a JAZ přidávají2.
Návrat přes konec tabulky přidává jeden cyklus navíc.
Proto2+8r je správná přibližná cena bloku bez těchto
občasných oprav, inicializace a konečných čtvercových testů.
Pro r=11 je90/30=3. Srovnání s C počítá navíc Y=(v-u)/2
odečítacích kroků; nejde o univerzální hardwarový benchmark.

Úloha7 lze realizovat i bez prodloužení na L:
uložíme periodickou bitovou posloupnost délky m a za ni
ještě w-1 ochranných bitů, které opakují její začátek
(při m<w podle potřeby několikrát).
Každé kruhové okno délky w pak tvoří souvislý úsek.
Nechť j je počáteční bitový index, q=floor(j/w),s=j mod w.
Dvě sousední slova A,B dávají okno

```
((A >> s) | (B << (w-s))) & (2^w-1).
```

Pro s=0 lze druhé čtení vynechat; v modelu je vyhrazen
neškodný koncový nulový sentinel. Dva udržované indexy
jsou právě q a s. Ochranné bity ošetřují neúplné poslední
slovo a opakování periody; bez nich by pouhé připojení
zaokrouhleného posledního slova k prvnímu mohlo vložit
neplatné výplňové bity. Režie posunů a přechodů záleží
na instrukční sadě. Odhad vhodnosti v/u z textu je pouze
orientační, nikoli matematický práh.

## Ověření a rozsah

`verify_factoring_fermat.py` porovnává C/D s nezávislým
hledáním největšího dělitele směrem dolů od isqrt(N).
Používá přesná celá čísla:

- C:4096 lichých vstupů, 2 340 338 kroků X a2 506 340 kroků Y,
  všechny invarianty a přesná nákladová identita.
- D:2048 lichých vstupů a oba knižní velké příklady.
- 948 modelů p^2, úplné koncové číslice a tabulkové třídy.
- 11 610 ekvivalencí opravených dvojic sít.
- 161 577 kompaktních slovních bloků s9315 návraty;
  34 170 nevyplněných oken ověřených přímým bitovým orákulem.

Všech pět checkpointů prošlo: PID1259264, session10688,
limit120s, skutečně8.71s, exit0. Úspěšný běh neopakován.
Všechny čtyři vrstvy errat a aktuální TeX prohledány:
C5 opraven1997, jména2004, AND2005; nové dva indexové
problémy neopraveny v dostupných vrstvách.
Obrázky387–390 a658 jsou původní vizuální doklady.
