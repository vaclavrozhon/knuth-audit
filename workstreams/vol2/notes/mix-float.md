# §4.2.1: programy MIX a úlohy 6, 14, 15, 19

**Oprava při obnově7.11.2026:** obecné tvrzení níže o správném N4
neplatí. [C0251](C0251-fadd-overflow-sticky.md) dokládá ztrátu
nenulového X instrukcí ENTX1 při přenosu a nesprávně zaokrouhlený
součet i po opravě2002. X0035 je znovu partial. Archivní konečné
testy zůstávají platné pro své vstupy, nikoli pro celý program.
Následující starý rozbor se přebírá jen po jednotlivých doložených
argumentech; nový úplný instrukční průchod pokračuje samostatně.

Kontrola 2. listopadu 2026. Vizuálně přečteny originály 218–221,
227–228, 612–613 a oprava 10. listopadu 2002 v all2-prepre,
strany souboru 14 a 37. Následující důkaz se vztahuje k **opravenému**
Programu A. Původní odlišný program a jeho čas 73 jednotek se neberou
jako platná aktuální tvrzení. Matematický model je definován v
[single-precision.md](single-precision.md), §§1–2.

## 1. Strojový model a sčítání

Báze jednoho bajtu je b, p=4 a exces q=b/2. MIX předpokládá b>=64
a dělitelnost čtyřmi. Slovo má pět bajtů a samostatné znaménko;
W=b^5 označuje počet nezáporných velikostí slov. Registr A obsahuje
horní a X dolní část desetibajtového pracovního zlomku. Jejich
znaménka se posuny **nemění**, jak požaduje definice MIX.

[Instrukční přepis](../sources/single-precision.mix) zachovává každou
instrukci; místní číselná návěští mají jedinečné názvy. Číslování A
je po opravě 2002. [Interpret](../mix_float_machine.py) provádí
instrukce, pole, přenosy, znaménkové nuly a změny adres/znamének
instrukcí samostatně od matematického modelu. Nejde o obecný assembler.
Zvlášť zachovává porovnání stejného pole obou operandů, pravé zarovnání
při ukládání pole a skutečnost, že nulový ADD zachová původní znaménko A.
Instrukční sémantika a ceny odpovídají §1.3.1 svazku 1, str.129–138.

Před sčítáním se vyberou větší a menší exponent. Uložením pole (0:4)
se ze čtyř cifer zlomku stane pětibajtové číslo s koncovou nulou;
tento bajt FU/FV zůstává nulový i mezi opakovanými voláními. Posun
menšího zlomku v AX vytvoří horní celé H a nezápornou dolní velikost L.
ADD přičte horní část k FU; má-li její výsledek stejné znaménko jako
původní menší operand, AX již udává správnou velikost součtu.

Při opačných znaménkách a L!=0 je správná velikost
`|A| − L/W = (|A|−1) + (W−L)/W`. Opravené řádky A26–A30
rozhodují právě podle znamének A a FV. A31–A39 sníží horní velikost
o jedna a nahradí dolní L číslem W−L. Dvě přičtení HALF uskuteční
odečet od W bez reprezentace W v jediném slově; znaménko A zůstává
zachováno. Potom se znovu testuje normalizace, jak vyžaduje oprava.
Nulová horní část s nenulovým ocasem při této korekci nenastane:
nenulový ocas vyžaduje rozdíl exponentů nejméně dva, takže větší
normalizovaný operand převažuje nad menším.

Při rozdílu exponentů nejvýše p+1=5 zachová desetibajtový registr
všechny potřebné cifry přesně. Při větším rozdílu je celý menší operand
pod prahem, který podle důkazu A4 nemůže změnit zaokrouhlený výsledek;
případné odříznutí jeho konce tedy nevadí. Přetečení zlomku zachytí
přenosový příznak; N4 vloží vedoucí jedničku a zvýší exponent.
N5 použije poslední bajt A a test nenulovosti X k rozhodnutí zaokrouhlení.
Při přesné polovině zvolí lichou poslední uloženou cifru, protože b/2
je sudé. Kontrola exponentu následuje až po normalizaci a zaokrouhlení.

**Úloha 6.** Nenulové normalizované operandy se mohou zrušit přesně
jen při stejných exponentech a opačných zlomcích. V této větvi je
před ADD v A původní ACC, tedy operand u hardwarové instrukce FADD.
Nulový součet jeho znaménko zachová. Totéž platí pro oba nulové
operandy. Softwarový podprogram přijímá druhý operand v A; jeho
vstupní znaménko se nesmí zaměnit s původním A hardwarové instrukce.
FSUB jen obrátí znaménko druhého operandu a použije FADD.

## 2. Násobení, dělení a převody

FMUL násobí dvě pětibajtová čísla F_u b a F_v b přesně do AX.
Výsledný zlomek je buď nula, nebo má velikost nejméně b^(-2), takže
normalizace potřebuje nejvýše jeden posun vlevo. Při nenulovém
součinu tedy A není nula a vstupní test NORM je bezpečný.

FDIV nejprve porovná velikosti F_u a F_v. Jsou-li v rostoucím pořadí,
vydělí bez předchozího posunu; jinak vydělí po posunu o bajt a zvýší
exponent. Nenulový podíl je v obou větvích již normalizovaný. Celočíselné
DIV dává pět cifer a zbytek, jehož nenulovost stačí N5 k rozhodnutí
poloviny. Nulový jmenovatel vyvolá přenos a větev DVZRO. Znaménko
součinu i podílu je správným součinem vstupních znamének.

FLOT nastaví exponent q+5, vloží X=0 a normalizuje. Jeho pracovní
hodnota je přesně původní celé číslo n, protože `(n/b^5)b^5=n`.

**Úloha 14 (FIX).** Po odstranění exponentového bajtu označme L počet
dodatečných posunů vlevo potřebných k nenulovému prvnímu bajtu A.
Jeho velikost je `F b^(L+1)` a indexový registr má e−L−1.
Příkaz ENN1 vytvoří posun `n=q+5+L−e`. Je-li n<0, velikost vstupu
je nejméně b^5 a převod nelze uložit. Jinak SRAX oddělí celočíselnou
část od zlomkového zbytku. Porovnání X s W/2 určuje zaokrouhlení;
při rovnosti se volí liché celé číslo. Případné cifry odříznuté daleko
vpravo nemohou zaměnit polovinu s hodnotou nad polovinou: vstup má
nejvýše čtyři významné bajty a nenulový celočíselný či poloviční díl
musí být před jejich koncem. Při extrémně malém vstupu je výsledek
bezpečně nula.

Zaokrouhlovací INCA nemůže přetéct. Největší vstup pod b^5 se čtyřmi
významnými bajty je b^5−b, nikoli hodnota těsně pod b^5. Nulové
vstupy i nulové zaokrouhlené výsledky zachovají vstupní znaménko.
Argument zahrnuje nenormalizované vstupy požadované zadáním.

**Úloha 15 (FP).** Je-li e−q kladné, SLA zahodí celočíselné cifry
modulo velikost slova. Pro nezáporné u je zbylá část připravena k NORM.
Pro záporné u se musí vytvořit `1−(|u| mod 1)`, pokud zbytek není nula.
Je-li zbytek přesně uložen jako H/W, INCA a ADD WM1 vytvoří W−H.
Při nenulovém dolním ocasu se místo toho vytvoří W−1−H a ponechá
se informace, že ocas je nenulový. Jeho přesná doplněná hodnota není
potřeba: tato větev vzniká pro |u|<1/b a výsledný kladný zlomek je
již normalizovaný, takže N5 potřebuje jen test nulovosti ocasu.

Je-li záporný vstup tak malý, že posun zahodí celý jeho zlomek,
program ponechá horní velikost W−1, která se správně zaokrouhlí na 1.
Nulový zbytek po odstranění celočíselných cifer se naopak přes JANN
vrátí jako nula; záporná nula není záporné číslo pro podmíněný skok.

## 3. Přesný čas opraveného sčítání (19)

Časy jsou počty standardních časových jednotek MIX. Zaveďme indikátory
s hodnotou 0 nebo 1: d=[e_v<e_u], f=přetečení zlomku, z=nulový výsledek,
r=přetečení při zaokrouhlení, h=první zaokrouhlovací cifra b/2,
t=celý zaokrouhlovací ocas přesně b/2 následovaný nulami,
u=zvětšení zaokrouhlované velikosti. Dále N je počet posunů vlevo,
X značí nenulový ocas po zarovnání **bez přetečení zlomku**, o značí
opačná vstupní znaménka a s záporný výsledek. Použití u jako indikátoru
platí jen v tomto časovém vzorci, nikoli pro vstupní operand výše.

Přímým sečtením instrukcí před prvním N5 dostáváme pro nenulový výsledek
`32+d−f+7N+(3+(16+s)o)X`. Samotná první fáze zaokrouhlení má ceny:

| Ocas | Rozhodnutí | Čas |
|---|---|---:|
| první cifra < b/2 | dolů | 3 |
| první cifra > b/2 | nahoru | 8 |
| první cifra = b/2, další ocas nenulový | nahoru | 9 |
| přesná polovina, uložená cifra lichá | dolů | 10 |
| přesná polovina, uložená cifra sudá | nahoru | 14 |

To je `3+5u+6t−tu+h`. Přetečení při zaokrouhlení přidá 7;
kontrola exponentu, zabalení a návrat přidají 8. Nulová větev má
přímo cenu 33+d. Spojením dostáváme přesně erratum 2002:

```text
T = 73 − (5−t)(6−u) + d + h − f − 10z + 7r + 7N
    + (3+(16+s)o)X.
```

Je-li X=0 a N>0, všechny zaokrouhlovací cifry po posunu jsou nulové,
tedy u=h=t=r=0. Platí N<=4 a T<=72. Při X=N=0 dává i nezávislé
nahrazení indikátorů jejich největšími hodnotami T<=62.

Je-li X=1, počáteční rozdíl exponentů je nejméně dva. Větší operand
má velikost nejméně 1/b a menší po zarovnání méně než 1/b^2, takže
N<=1. Pro t=0 je základ `73−5(6−u)` nejvýše 48; ostatní kladné
příspěvky jsou nejvýše 1+1+7+7+20, a tedy T<=84. Pro t=1 nemůže
nastat zaokrouhlovací přetečení: poslední možná cifra b−1 je lichá,
a přesná polovina by ji ponechala. Proto r=0 a T<=53+1+1+7+20=82.

Mez **84 je dosažena** příkladem errata b=100,
`u=−50|01 00 00 00`, `v=+45|49 99 99 99`.
Zde X=o=s=d=h=u=r=N=1, t=f=z=0. Stejný vzor funguje i pro b=64.
Průměrný čas z poznámky patří až k distribuční analýze §4.2.4.

## 4. Výpočetní doplnění a rozsah

[Kontrola](../verify_mix_float.py) porovnává vykonané instrukce
s přesnou racionální aritmetikou a dříve nezávisle ověřeným modelem
A/N/M. Úspěšné bloky uchovává a znovu automaticky nespouští.
[Výsledky](../results/mix-float.json) obsahují:

- 20 442 sčítání; 20 418 bez exponentové výjimky má přesně čas podle
  vzorce, maximum 84;
- 21 384 násobení/dělení a dalších 40 nulových dělitelů;
- po 10 920 vstupech FIX a FP, včetně nenormalizovaných hodnot,
  a 4 040 celočíselných převodů FLOT;
- 96 dalších volání na opakovaně používaném stroji a 8 konkrétních
  případů podtečení při sčítání/odčítání.

Poslední malý blok byl přidán kvůli dříve nepokryté vstupní větvi FSUB,
zachování měněné paměti mezi voláními a přímému zásahu podtečení ADD.
Předchozí úspěšné kontroly se neopakovaly. Vše proběhlo pro b=64 i 100;
konečné počty nejsou náhradou obecných argumentů výše.

Model původního programu navíc vrací chybně u při
`b=100, u=+50|01 00 00 00, v=−45|50 00 00 00`; opravený výsledek
je `+49|99 99 99 99`. To je reprodukce **známého errata**, nikoli nový
nález. Totéž je doloženo v bázi 64. Nová potvrzená chyba v tomto bloku
nebyla nalezena. Ošetření dříve nastaveného přenosu OFLO je externí
služba volajícího programu; reproduktor je pouze označuje pomocným HLT.

## 5. Hardwarové zkratky a varovné příklady (222–225)

Hardwarové FADD/FSUB/FMUL/FDIV jsou v knize definovány pomocí uvedených
podprogramů s předběžnou normalizací vstupů; jejich samostatné pevné
časy jsou definice modelu, nikoli naměřený čas softwaru. Přechodné
podtečení předběžné normalizace se nemá hlásit, pokud konečný výsledek
je v rozsahu. FCMP je odkaz na přesný program v §4.2.2-17 a bude
prověřen tam. Obecné výroky o kvalitě hardwaru jsou historické komentáře.

Ve zkratce (12) má celé n velikost menší než b^4, tedy nulový první
bajt. SLA 1, ENTX q+4, SRC 1 z něj vytvoří plovoucí kód s exponentem
q+4 a zlomkovým polem |n|; jeho hodnota je přesně n. FADD s nulou
jej normalizuje. Pro pětibajtové n by první posun nenulový bajt zahodil,
což vysvětluje výslovné omezení. Plný FLOT skutečně může zaokrouhlit
přes hranici exponentu: n=b^5−1 se zaokrouhlí na b^5.

Ve zkratce (13) má FUDGE hodnotu b^3. Pro nezáporné u, jehož
**zaokrouhlený celočíselný výsledek se vejde do tří bajtů**, leží
b^3+u v pásmu s exponentem q+4 a s jednotkovou vzdáleností sousedů.
FADD proto uloží b^3+round(u). Jelikož b^3 je sudé, přičtení této
konstanty zachová také pravidlo liché cifry při přesné polovině.
Výsledné pole je tudíž `q+4 | 1 | round(u)` podle obrázku. Pokud
by round(u)=b^3, už tříbajtový předpoklad nesplňuje; vedoucí bajt by
byl 2. Zkratka sama ještě neodstraňuje exponent a vedoucí bajt,
což text také netvrdí.

Příklad nevhodného dvojího zaokrouhlení v desítkové soustavě:
.1234567851 nejprve na devět cifer dá .123456785 a pak na osm cifer
.12345678, kdežto přímé zaokrouhlení na osm cifer dává .12345679.
Výjimka po zaokrouhlovacím přetečení je bezpečná, protože výsledek
je přesně mocnina základu. Oba intervaly na str.223 mají deklarovanou
inkluzi; jde o argument s mezemi relativní chyby, nikoli o dvě
skutečné Voroného buňky zaokrouhlování na nejbližší hodnotu.

Také prostý násobicí příklad str.222 existuje: v desítkové aritmetice
s excesem nula a exponenty od −50 do 50 vezměme u=v=10^(−40),
w=10^40. Při nahrazení podtečení nulou je (u*v)*w=0, ale
u*(v*w)=10^(−40). Všechny vstupy a druhá cesta jsou v rozsahu.
Přesnější pozitivní příklad (11) a postupné podtečení již dokládá
[single-precision.md](single-precision.md), §3.
