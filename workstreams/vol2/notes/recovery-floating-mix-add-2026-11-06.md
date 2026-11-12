# Obnova §4.2.1: celý Program A, úloha6 a přesný rozsah19

7. listopadu2026, X0196. Originály218–219/file230–231,
227–228/file239–240,612–613/file624–625 a opravy2002 na
`all2-prepre` file14/37. Níže jsou posouzeny všechny instrukce
opraveného Programu A a jeho okolní tvrzení. **Obecnou správnost
programu vyvrací [C0251](C0251-fadd-overflow-sticky.md).**
To nebrání samostatnému uzavření ostatních větví a nákladů
nezměněného programu. Žádný starý test nebyl znovu spuštěn.

## Model, rozhraní a instrukční předpoklady

`b≥64`, `4|b`, `p=4`, `q=b/2`; `W=b^5`.
Zlomek uloženého slova je `σF/b^4`, kde nenulové normalizované
`b^3≤F<b^4`, a exponent je jeden nezáporný bajt. Nula má exponent0.
Souvislý zlomek v AX má velikost `(|A|W+|X|)/W²` a znaménko A;
znaménko X se při posunech do tohoto významu nezapojuje.

Instrukční sémantika je převzata přesně ze svazku1:129 (načítání
pole a znaménka),130 (pravé zarovnání ukládaného pole, STJ),131
(ADD a jeho nulové znaménko/přenos),133–135 (adresové operace,
porovnání stejného pole obou operandů, skoky a posuny),138 (ceny).
JXO je explicitně definováno ve svazku2,339 jako skok při lichém X.
Nejde o obecný assembler: místní interpret je pouze konečný doplněk,
nikoli důkaz sémantiky knihy.

Rozhraní přijímá u v ACC a v v A. STJ uloží návratovou adresu do
EXITF ještě před dalšími skoky, které přepisují rJ. Úspěšný výstup
se uloží do ACC, přičemž STA A nemění; proto jsou obě kopie shodné.
Ukázka(8) nejprve naplní ACC hodnotou A, pak zavolá s B a C postupně
FADD a FSUB a uloží výsledné A do D. Jde o odpovídající posloupnost
dvou plovoucích operací, nikoli tvrzení o přesné rovnosti s pevnou
aritmetikou(7). Po C0251 tato ukázka dědí chybu použitého FADD.

OFLO je výslovně externí služba pro neočekávaně zapnutý přenos.
Zdejší běžné větve a čas předpokládají přenos při vstupu vypnutý;
diagnostický výstup neimplementujeme ani nepovyšujeme na ověřený.
Předpoklad NORM je `A=0 ⇒ (X=0 a I2<b)`. Nerovnost `I2<b`
není bezpodmínečným předpokladem nenulového vstupu, neboť N6/N7
musí umět zjistit exponentový přetečení i u dalších podprogramů.

## Každá instrukce rozbalení, řazení a zarovnání

Čísla A jsou podle opravy2002, před A26 stejná jako v prvním tisku.
U každého řádku je uveden důvod, nikoli jen jeho anglický komentář.

| Řádek | Argument |
|---|---|
| A00 BYTE EQU1(4:4) | Jednička ve čtvrtém z pěti bajtů má hodnotu b; BYTE tedy skutečně označuje bázi. |
| A01 EXP EQU1:1 | Pole obsahuje pouze exponentový bajt, nikoli znaménko. |
| A02 STA TEMP | Uloží celý druhý operand včetně znaménka pro FSUB. |
| A03 LDAN TEMP | Obrátí znaménko v včetně znaménkové nuly, potom propadne do FADD; tím realizuje u+(−v). |
| A04 STJ EXITF | Přepíše pouze návratové adresové pole, zachová podmíněný skok J2N. |
| A05 JOV OFLO | Při vypnutém vstupním přenosu pokračuje; jinak přejde na deklarovanou diagnostiku. |
| A06 STA TEMP | Zachová v pro pozdější načtení exponentu. |
| A07 LDX ACC | Načte celé původní u; A nadále obsahuje v. |
| A08 CMPA ACC(EXP) | Porovná exponent v v A s exponentem u v ACC; stejná pole obou slov vylučují znaménka. |
| A09 JGE SWAP | Pro e_v≥e_u včetně rovnosti vybere v jako větší pracovní operand. |
| A10 STX FU(0:4) | V druhé větvi uloží znaménko u a pravé čtyři cifry F_u do bajtů1–4 FU; bajt5 zůstane0. |
| A11 LD2 ACC(EXP) | I2=e_u je větší exponent v této větvi. |
| A12 STA FV(0:4) | Stejným polem uloží menší v jako σ_v F_v b. |
| A13 LD1N TEMP(EXP) | I1=−e_v, protože načtené pole bez znaménka je nezáporné. |
| A14 JMP ALIGN | Přeskočí druhou větev; původní návrat je již uložen v EXITF. |
| A15 STA FU(0:4) | Pro e_v≥e_u uloží větší v, včetně případu rovnosti exponentů. |
| A16 LD2 TEMP(EXP) | I2=e_v. |
| A17 STX FV(0:4) | Uloží menší pracovní operand u; při rovnosti je to původní u z ACC. |
| A18 LD1N ACC(EXP) | I1=−e_u. |
| A19 INC1 0,2 | V obou větvích I1=d=max(e_u,e_v)−min(e_u,e_v)≥0. |
| A20 LDA FV | A má znaménko menšího operandu a velikost F_small b. |
| A21 ENTX0 | Připraví kladnou nulovou dolní část, nezávisle na předchozím obsahu X. |
| A22 SRAX0,1 | Posune desetibajtovou velikost o d míst doprava, znaménka A/X zachová. |
| A23 ADD FU | Přičte podepsanou horní část většího operandu; X nemění. |
| A24 JOV N4 | Zachytí jediný celočíselný přenos při stejných znaménkách; zbytek A doplní N4. Ztráta X v N4 je přesně C0251. |
| A25 JXZ NORM | Je-li dolní velikost0, znaménko A již správně popisuje celý přesný pracovní součet. |

Značme po A22 horní a dolní nezáporné části menšího operandu H,L
a velikost připraveného většího B=`F_big b`. Při nenastaveném
přenosu A23 vytvoří podepsané `C=σ_big B+σ_small H` a pravý
pracovní součet je

```
C/W + σ_small L/W².
```

Čtyři cifry vstupu a šest doplněných nul v AX znamenají, že pro
`d≤6` je posun přesný. Pro `d≥6` má celý menší zlomek velikost
menší `b^−6`; původní i zkrácený leží uvnitř stejné zaokrouhlovací
buňky většího čísla. Nejmenší sousední mezera u normálního většího
operandu je nejméně `b^−5`; `b^−6 < b^−5/2`, protože b≥64.
Jestliže posun pro d≥7 zahodí nízké cifry, nezmění konečný nejbližší
výsledek. Přetečení zlomku zde nemůže nastat: odstup největšího
zlomku od1 je `b^−4`, větší než celý přičítaný menší člen.
Proto se C0251 na toto zdůvodnění vynechaného A4 nevztahuje.

Naopak příklad `f_big=1/b`, `F_small=b^3+1`, `d=5` má nenulovou
devátou cifru přesného součtu. Požadavek `2p+1=9` přesných míst
není záměna s počtem pěti bajtů A. Desetibajtový AX je uchová;
krátké zaokrouhlovací ekvivalenty mají jiný rozsah podle celé5.

## Opravená větev znamének: každá instrukce a meze

`L>0` vyžaduje `d≥2`, neboť d=0/1 přesouvá jen doplněné nuly.
Menší operand je tehdy nenulový a normalizovaný. Platí
`H≤b^3−1`, `B≥b^4`; tedy větší operand rozhodne znaménko C a
`|C|≥b^4−b^3+1>1`. Nula ani záporná nula proto nemohou zmást
JAP nebo J1N/J1P. Po případném odečtení1 zůstane horní část kladná.

| Řádek | Argument |
|---|---|
| A26 LD1 FV(0:1) | Znaménko a první cifra nenulového normalizovaného menšího operandu dají nenulový index se znaménkem σ_small. |
| A27 JAP POSITIVE | Rozliší C>0 od C<0, protože C=0 je zde vyloučeno. |
| A28 J1N N2 | Při C<0 a σ_small<0 je AX už správná společná velikost; přeskočí doplněk. |
| A29 JMP COMPLEMENT | Při C<0 a σ_small>0 je nízká část opačná a potřebuje doplněk. |
| A30 J1P N2 | Při C>0 a σ_small>0 přeskočí doplněk; jinak do něj propadne. |
| A31 SRC5 | Prohodí velikosti A a X, znaménka ponechá: A=σ_C L, X=+\|C\|. |
| A32 DECX1 | X=\|C\|−1>0; odečtení nevyvolá podtečení ani změnu zamýšleného znaménka. |
| A33 STA TEMP | Uloží σ_C L. |
| A34 STA HALF(0:0) | Přenese do HALF pouze σ_C, jeho velikost W/2 zůstává. |
| A35 LDAN TEMP | A=−σ_C L. |
| A36 ADD HALF | A=σ_C(W/2−L); může mít dočasně opačné znaménko, velikost je ale menší W/2. |
| A37 ADD HALF | A=σ_C(W−L), jehož velikost leží v(0,W); nenastane přenos. |
| A38 SRC5 | Obnoví A=σ_C(\|C\|−1) a kladné X=W−L; oprava5 místo původního4 je podstatná. |
| A39 JMP N2 | Znovu otestuje vedoucí cifru. Skok do původního N3A by přeskočil správný test. |
| A40 HALF CON1//2 | MIXAL zlomkové dělení vytvoří W/2 přesně, protože b je sudé; mění se pouze znaménko. |
| A41 FU CON0 | Inicializuje také poslední bajt0, který pozdější zápisy(0:4) nepřepisují. |
| A42 FV CON0 | Totéž pro menší operand, i mezi opakovanými voláními. |

Výsledná reprezentace po A38 je přesně
`σ_C((|C|−1)/W+(W−L)/W²) = C/W+σ_small L/W²`.
To dokazuje opravenou větev i při dočasné změně znaménka po A36.
Původní chyby2002 jsou známé erratum; nepočítají se jako nový nález.
Všechny načítané indexové hodnoty, d≤b−1 a exponenty posunuté
nejvýše o čtyři místa se vejdou do dvou bajtů pro b≥64.

## NORM, zaokrouhlení, zabalení a opakovaná volání

| Řádek | Argument |
|---|---|
| A43 JAZ ZRO | Při A=0 předpoklad zaručuje X=0 a I2<b; cesta ZRO uloží celé nulové A včetně znaménka. |
| A44 CMPA=0=(1:1) | Testuje pouze vedoucí cifru velikosti; rovnost právě znamená \|f\|<1/b. |
| A45 JNE N5 | Nenulová vedoucí cifra již zaručuje normalizaci, protože celé AX má velikost<1. |
| A46 SLAX1 | Při nulové vedoucí cifře nezahodí významný bajt a přesně násobí velikost b. |
| A47 DEC2 1 | Sníží exponent a zachová hodnotu `f*b^(e−q)`. |
| A48 JMP N2 | Opakuje test; A bylo nenulové, proto nejvýše čtyři posuny přivedou jeho první nenulový bajt dopředu. |
| A49 ENTX1 | Při přenosu zahodí starý ocas; samostatný protipříklad a oprava jsou C0251. |
| A50 SRC1 | Vloží přenosovou1 a posune A; po A49 je reprezentovaný guard správný, obecná informace pod ním však není. |
| A51 INC2 1 | Zvýší exponent po posunu doprava; samotné škálování je správné. |
| A52 CMPA=BYTE/2=(5:5) | Srovná jediný guard se sudou hodnotou b/2, bez znaménka. |
| A53 JL N6 | Guard<b/2 znamená zaokrouhlení dolů; další cifry nemohou dosáhnout půlky. |
| A54 JG ROUNDUP | Guard>b/2 znamená zaokrouhlení nahoru bez ohledu na zbytek. |
| A55 JXNZ ROUNDUP | Při guard=b/2 odliší nenulový další ocas; platí, pokud jeho invariant nebyl porušen A49. |
| A56 STA TEMP | Při přesné strojové půlce zachová A pro izolaci poslední ponechané cifry. |
| A57 LDX TEMP(4:4) | Načte nezápornou čtvrtou cifru do X. |
| A58 JXO N6 | Protože b je sudé, parita celého ponechaného F je parita této cifry; 4\|b vyžaduje tie-to-odd. |
| A59 STA*+1(0:0) | Nastaví pouze znaménko následující INCA podle A, vždy znovu. |
| A60 INCA BYTE | Přičte σ_A b, tedy jednu jednotku čtvrté ponechané cifry k velikosti; funguje i pro záporné A. |
| A61 JOV N4 | Zachytí zaokrouhlovací přenos. Zbytek A je menší b, takže po N4 je guard0 a další zaokrouhlení je nečinné. |
| A62 J2N EXPUN | Nenulový výsledek s e<0 ohlásí před balením jako podtečení. |
| A63 ENTX0,2 | Načte nezáporný exponent e do X. |
| A64 SRC1 | Pro 0≤e<b přesune jeho jediný bajt před čtyři ponechané cifry A; guard se zahodí do X. |
| A65 DEC2 BYTE | I2=e−b; v nulové větvi je záporné díky předpokladu, přičemž A samo již obsahuje exponent0. |
| A66 STA ACC | Uloží výsledné slovo, A nezmění. |
| A67 EXITF J2N saved-return | Pro e<b se normálně vrátí; pro e≥b propadne do EXPOV. |
| A68 HLT2 | Signalizuje exponentové přetečení. Pole A/ACC bylo již zabaleno modulo bajt; není vydáváno za platný výsledek. |
| A69 HLT1 | Signalizuje exponentové podtečení před zabalením; ani tato cesta netvrdí platný normální výsledek. |
| A70 ACC CON0 | Počáteční nulový akumulátor má nulový exponent i zlomek. |

Po druhém průchodu N4 vyvolaném zaokrouhlením je výsledek přesná
mocnina báze; C0251 zde nedává nový případ ztráty půlky. N5 je
samostatně správné s pravdivým invariantem nízkého ocasu, a po N3
jej zachovávají přesné posuny. Test exponentu skutečně přichází
až po konečném zaokrouhlení, takže dočasné e<0 může být následným
zaokrouhlovacím přenosem opraveno.

Mezi voláními přetrvávají jen zamýšlené změny: poslední bajty FU/FV
zůstávají0; HALF má stálou velikost a nové znaménko se nastaví před
každým použitím; znaménko INCA se nastaví před každým zaokrouhlením;
EXITF dostane novou návratovou adresu. TEMP se vždy uloží před
příslušným čtením. Program není prezentován jako reentrantní;
to kniha nepožaduje. Stav po externí chybové službě není součástí
úspěšného rozhraní.

## Celá úloha6: přesná nula a její znaménko

Nenulové normalizované hodnoty se mohou přesně zrušit jen při
stejných exponentech a opačných stejně velkých zlomcích: pásma
`[b^(e−q−1),b^(e−q))` pro různé e se nepřekrývají. Pro rozdílné
exponenty je velikost většího operandu přísně větší než menšího.
N5 nenulový normalizovaný zlomek na nulu nezaokrouhluje. Výjimka
podtečení není normálním návratem nulového výsledku.

Při rovnosti exponentů A09 vybere větev SWAP; do FV uloží původní
u z ACC. Tedy A20 před ADD nese znaménko původního u. D=0 zanechá
X=0 a ADD při přesném zrušení zachová předchozí znaménko A podle
definice ADD ve svazku1,131. NORM/ZRO je nemění. Stejná argumentace
platí pro oba nulové operandy: oba mají exponent0 a stejnou větev.

Hardwarová instrukce FADD má původní první operand v A, který se
podle definice přenese do ACC; software naproti tomu přijímá v A
druhý operand. Odpověď612 proto správně říká, že **hardwarové A
zachová své původní znaménko**. Nejde o znaménko softwarového A
při vstupu. Přesná nula nemůže projít vadnou větví přenosu C0251.
Definice224 případné nenormalizované vstupy nejprve normalizuje.
Tyto přesné levé posuny zachovají hodnotu i znaménko; disjunktnost
pásem platí i pro přechodně záporný exponent. Při shodných nulových
vstupech se normalizuje exponent na0 a znaménko zůstává. Výslovně
potlačené přechodné podtečení proto závěr o konečné přesné nule
nemění; nejde o nahrazení nenulového výsledku nulou.
FSUB obrací druhý operand a tentýž důkaz platí, pokud je potřeba
závěr přenést i na odčítání; zadání6 se ptá pouze na FADD.

## Úloha19: odvození nákladů z každé větve

Používáme známou náhradu odpovědi z10.11.2002. Původní vzorec a
maximum73 se nevydávají za současné tvrzení. Svazek1,138 přiděluje
2u všem LOAD/STORE/ADD/posunům/porovnáním a1u adresovým operacím
a skokům; JXO je rozšíření stejného druhu jako ostatní skoky.

Indikátory: `D=[e_v<e_u]`, F=přenos zlomku, Z=přesná nula,
R=přenos při zaokrouhlení, H=první guard=b/2, T=strojový ocas
b/2 následovaný nulami, U=zvětšení velikosti programem. N je počet
levých posunů, X znamená nenulový zarovnaný ocas a žádný přenos
zlomku, O=opačná vstupní znaménka, S=záporný výsledek. H/T jsou
odečteny při prvním vstupu do N5; po C0251 je nesmíme automaticky
ztotožnit s přesným matematickým ocasem. U je indikátor, nikoli
první vstupní operand.

| Blok | Přesná cena a důvod |
|---|---|
| A04–A09 | 2+1+2+2+2+1=10. |
| A10–A14 nebo A15–A18 | První cesta9, druhá8; dohromady8+D. |
| A19–A24 | 1+2+1+2+2+1=9. Celkem k rozhodnutí přenosu27+D. |
| F=1 | N4 má1+2+1=4, tedy před N5 celkem31+D. |
| F=0,X=0,nenula | A25 a A43 po1, test A44–45 má3: před N5 celkem32+D. |
| Jeden levý posun | A46–48 a nový test A44–45 stojí2+1+1+2+1=7. |
| F=0,X=1,O=0 | A25 stojí1, opravený znaménkový test4, přímý vstup do N2 stojí3:35+D. |
| F=0,X=1,O=1,S=0 | Znaménkový test4, doplněk A31–39 stojí16; s A25 a testem N2 je51+D. |
| F=0,X=1,O=1,S=1 | Přibude skok A29, tedy52+D. |
| Přesná nula | K27+D přibude A25,A43 po1 a ZRO/STA/EXITF za4:33+D. |

Pro nenulu je tedy před prvním N5
`32+D−F+7N+(3+(16+S)O)X`.

| První N5 | Cena |
|---|---:|
| guard<b/2 | CMPA+JL =3 |
| guard>b/2 | CMPA+JL+JG+STA+INCA+JOV =8 |
| guard=b/2, X≠0 | Navíc JXNZ:9 |
| přesná strojová půlka, ponechaná cifra lichá | Porovnání/skoky5, STA+LDX+JXO5:10 |
| přesná strojová půlka, ponechaná cifra sudá | K10 přibudou STA+INCA+JOV4:14 |

Tato tabulka je přesně `3+5U+6T−TU+H`. Zaokrouhlovací přenos
přidá N4 za4 a druhý N5 s guard0 za3, tedy7R. N6 až návrat stojí
`1+1+2+1+2+1=8`. Nulový případ odpovídá odečtu10Z, při němž
F,H,T,U,R,N,X jsou0. Dostáváme přesně známý vzorec

```
time/u = 73 − (5−T)(6−U) + D + H − F − 10Z + 7R + 7N
         + (3+(16+S)O)X.
```

Pro FSUB se navíc vykonají A02–03 za4u; zadání19 výslovně požaduje
FADD. Vstupní zapnutý overflow a chybové HLT nejsou v deklarovaném
maximu pro úspěšné návraty. Čas vytištěného programu je tímto
odvozen i pro chybně zaokrouhlenou úspěšnou cestu C0251.

## Maximum84, dosažení a přesný rozsah dodatku

1. Je-li X=0 a N>0, F=0 a nízká část před posunem byla nulová.
   První levý posun doplní nulový guard; všechny nižší cifry jsou
   rovněž nulové. Proto U=H=T=R=0, N≤4 a čas≤43+1+28=72.
2. Je-li X=N=0, prosté omezení zbývajících indikátorů dává≤62.
   Nulová cesta má nejvýše34, tedy ani ona nemůže být maximem.
3. Je-li X=1, d≥2 a větší normalizovaný zlomek má velikost≥1/b,
   menší<1/b². Po doplnění je součet velikostí přísně větší
   `1/b−1/b²≥1/b²`; proto N≤1. Pro T=0 je základ≤48,
   další kladné členy≤1+1+7+7+20, tedy celkem≤84.
4. Pro X=T=1 není možný zaokrouhlovací přenos. Ten vyžaduje všechny
   ponechané cifry b−1, tedy lichou poslední cifru, kterou přesná
   strojová půlka ponechá. Proto R=0 a čas≤53+1+1+7+20=82.

Vzor errata `b=100, u=−50|01 00 00 00, v=+45|49 99 99 99`
dává před normalizací přesně `−.009999999950000001` s exponentem50.
Po jediném posunu vlevo je zlomek `−.9999999950000001` a exponent49.
Guard50 má nenulový další ocas; velikost se zaokrouhlí na1,
přenos vrátí exponent50 a zlomek−.01. Tedy
`D=H=U=R=N=X=O=S=1`, `T=F=Z=0`; všechny exponenty i vstupy
jsou přípustné. Cena je `60+9+7+8=84u`. Tento ruční průchod
dokládá dosažení horní meze, bez další exekuce starého svědka.

C0251 má naproti tomu cenu `32+10+8=50u`; strojové T=1,
matematické T=0. Jejich záměna by ve vzorci dala44u. To je
důsledek stejné ztráty ocasu, ne samostatný nový nález. Hodnotu84u
nelze převzít pro navrženou opravu N4, která mění počet instrukcí.

**Dodatek o průměrném času menším47u není uzavřen tímto důkazem.**
Vyžaduje distribuční předpoklady a výpočty §4.2.4; ponechán partial
pro navazující obnovu tohoto rozsahu. Samotné zadání19 (vzorec a
maximum) je matematicky uzavřeno ve strojovém významu indikátorů.
Celá evidovaná odpověď19 má proto zatím status partial.

## Archiv, okolní text a další krok

Staré `results/mix-float.json` bylo pouze přečteno:20442 sčítání,
20418 časovaných úspěšných případů, maximum84; tyto konečné údaje
nejsou obecný důkaz správnosti. Ostatní uložené bloky násobení,
dělení a převodů se teprve přiřadí k vlastním instrukčním důkazům.
Veškeré známé opravy2002 zůstávají oddělené od C0251.

Tvrzení219 o možnosti zkrátit program přibližně na polovinu při
obětování přesnosti nemá zde konkrétní alternativní kód ani přesnou
metodu měření; je evidováno jako kvalitativní tvrzení, nikoli
nezávisle dokázaná poloviční délka. Význam přesnosti odkazuje na
následující oddíl; tento odkaz nepřebírá jeho dosud nedoplněné důkazy.
Poznámka220 o závislosti času na datech plyne z jednotlivých větví;
její distribuční analýza teprve následuje v §4.2.4.

Celá6 je uzavřena;19 má uzavřený požadovaný vzorec/maximum a přesně
vymezený otevřený průměr. Všechny instrukce Programu A jsou nyní
individuálně posouzeny, včetně potvrzené vady. Neznamená to zelené
uzavření celé stránky. Další jsou všechny kroky M a jeho program220–221
a související části úloh; dopředný418 stále čeká na celou obnovu.
