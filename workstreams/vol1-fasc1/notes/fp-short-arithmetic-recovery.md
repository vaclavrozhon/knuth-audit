# Převzetí single aritmetiky: přesný důkaz absence dvojího zaokrouhlení

6. listopadu 2026. Konkrétní věta v MMIX-doc:1528–1535 tvrdí, že načtení
short operandů, jedna ze sedmi aritmetických operací a následné STSF
dají výsledek single aritmetiky. Jde o přesný zděděný závazek obecného
IEEE tvrzení na fascikl file20/p12, ne o kontrolu libovolného programu.
Pouhé tvrzení „53 bitů je dost“ by nebylo důkazem. Zde jsou všechny
operace odvozeny zvlášť; žádný nový běh není potřeba.

## Přípustný stav a převzatá lemmata

Vstupy jsou libovolné binary32 vzory. Paměťové přístupy jsou povolené,
LDSF zachová oba operandy až do aritmetiky a STSF uloží její výsledek.
Režim je během sekvence stejný; u FSQRT/FINT je Y=0 nebo stejný režim
jako v rA. Arithmetic trips jsou vypnuty, původní event bity mohou být
libovolné a k novým se připojí OR. Není přidán předpoklad chování
libovolného handleru ani úspěchu zakázaného paměťového přístupu.

`fp-conversions-recovery.md` §1–4 a §7 již dokazují přesnost LDSF,
jediné správné STSF zaokrouhlení a všechny packovací větve. Úplné
výsledky sedmi operací v binary64 jsou zvlášť dokázány v
`fp-binary-arithmetic-recovery.md`, `fp-square-root-recovery.md`,
`fp-remainder-recovery.md` a konverzní poznámce §5. Zde se používají
jejich **matematické kontrakty**, nikoli předpoklad správnosti originálů.
Pro implementační složení je nutné zohlednit programové vady S0002,
S0003 a S0004 a jejich již dokázané auditní opravy. Kód 2013 navíc
obsahuje známou fplus/sfpack opravu, již zahrnutou v současném 2025 kódu.
Tato poznámka neprohlašuje původní program za opravený.

Označme p=24, P=53. Každé nenulové konečné short číslo lze přesně
napsat ±A·2^a s celým 2^(p−1)≤A<2^p; případné koncové nuly v A
nevadí. Všechny skutečné short hodnoty jsou zároveň násobky 2^−149.

Při konečných vstupech nehrozí v mezilehlé binary64 operaci O/U:
nenulový součet/rozdíl má velikost nejméně 2^−149 a menší než 2^129;
součin je v [2^−298,2^256), podíl v (2^−277,2^277), kladná odmocnina
v [2^−74.5,2^64). Remainder je přesná binary32 hodnota (důkaz níže),
integerizace je nula nebo celé číslo v původním rozsahu. Tyto meze
včetně nejbližších binary64 výsledků leží v normálním binary64 rozsahu.
Přesná nula se ošetřuje zvlášť a její znaménko se nemění konverzí.

## Společné lemma pro rounding

Pro stejný directed režim je převod přes binary64 přesný z hlediska
konečného binary32 zaokrouhlení: každý short bod je binary64 bod.
Například největší short s≤r je zároveň ≤floor_binary64(r), protože s
patří do jemnější mřížky. Obrácená implikace plyne z
floor_binary64(r)≤r. Proto floor_short(floor_binary64(r))=floor_short(r).
Pro ceil je důkaz obrácený; ROUND_OFF používá jeden z nich podle znaménka.
Argument zahrnuje subnormály, nulu a konečnou overflow mez; znaménko
nuly se řídí převzatým aritmetickým kontraktem, nikoli uspořádáním bitů.

Pro nearest může nastat odlišnost pouze tehdy, pokud nepřesný binary64
výsledek dopadne **přesně na midpoint** mezi dvěma short výsledky.
Midpoint je sám binary64; monotonicita nearest zakazuje jeho přeskočení
ze špatné strany. Je-li přesný výsledek již midpoint, binary64 jej
reprezentuje přesně a pozdější short tie-to-even je správné.
Zbývá tedy pro každou operaci vyloučit falešný dopad na midpoint.
Zahrnujeme midpoint u nejmenšího subnormálu a overflow midpoint mezi
největším short a ideální hodnotou 2^128.

## FADD a FSUB

Nulový operand dává přesný druhý operand; obecné speciální třídy jsou
níže. Pro dva nenulové konečné operandy uspořádejme exponenty a pišme
u=A·2^a, v=B·2^(a−d), d≥0; znaménko pouze určí ±.

Je-li d≤23, celé A·2^d±B má nejvýše 24+d+1≤48 bitů. Je-li
24≤d≤29, pak B<2^24≤2^d a A≤2^24−1, takže součet je menší než
2^(24+d) a má nejvýše 53 bitů. Rozdíl jich nemá více. Výsledek je
proto přesný binary64, včetně případného zrušení na nulu.

Je-li d≥30, označme 2^h≤u<2^(h+1). Pak v<2^(h+1−d)≤2^(h−29).
Vzdálenost u od nejbližšího short midpointu je alespoň 2^(h−25);
u mocniny dvou se zde počítá i menší krok směrem dolů. U subnormálů
je pevný krok ještě větší než tato dolní mez. Přesný u±v i jeho nearest
binary64 approximation leží od u blíže než
2^(h−29)+2^(h−52)<2^(h−28)<2^(h−25).
Obě short nearest volby jsou tedy právě u. Toto platí i pro největší
short před overflow midpointem. FSUB používá stejné případy s opačným
znaménkem druhého konečného operandu.

## FMUL

Součin A·B má nejvýše 48 významných bitů a jeho výše uvedený rozsah
nemůže v binary64 podtéct ani přetéct. Mezilehlý výsledek je proto
vždy přesný. Pozdější STSF je jediné zaokrouhlení, pro každý režim.

## FDIV: oddělení od každého short midpointu i hodnoty

Nechť r=(A/B)·2^q>0. Pro pomocný bod m>0 použijme buď short midpoint,
nebo nenulovou konečnou short hodnotu. Položme 2^h≤m<2^(h+1) a
k=max(h−24,−150). Pak m=M·2^k s celým M; vždy h≥−150 a k≤h.

Předpokládejme, že nějaké binary64 zaokrouhlení r dopadne na m, a přitom
r≠m. Vzdálenost |r−m| je nejvýše jeden sousední binary64 krok,
tedy 2^(h−52). Z toho r≥2^(h−1). Protože A/B<2, musí q≥h−1≥k−1.
Nyní

    r−m = 2^(k−1) · (A·2^(q−k+1) − 2BM) / B.

Výraz v závorkách je nenulový integer. Jelikož B<2^24,

    |r−m| ≥ 2^(k−1)/B > 2^(k−25) ≥ 2^(h−49) > 2^(h−52),

což je spor. Podíl tedy nemůže chybně dopadnout ani na midpoint,
ani na přesnou short hodnotu. Tento důkaz zahrnuje všechny subnormální
midpointy, všechny normální exponenty a overflow midpoint. Pro záporný
podíl použijeme absolutní hodnotu a odpovídající directed směr.
Přesné r=m není problém: binary64 je pak přesné a short tie se zachová.

## FSQRT

Pro konečné kladné short z je r=sqrt(z) v normálním short rozsahu,
takže možné midpointy mají m=M·2^(h−24), 2^h≤m<2^(h+1).
Předpokládejme falešný dopad binary64 rounding r na m. Pak
|r−m|≤2^(h−52), tedy 2^(h−1)≤r<2^(h+2). Proto má short z=r²
exponent nejméně 2h−2 a je násobkem 2^(2h−25), případně hrubšího
subnormálního kroku. m² je násobkem 2^(2h−48). Obě hodnoty jsou
proto násobky posledního kroku; jsou-li rozdílné,
|z−m²|≥2^(2h−48). Avšak r+m<6·2^h<2^(h+3), takže

    |r−m| = |z−m²|/(r+m) > 2^(h−51) > 2^(h−52),

opět spor. Pokud z=m², mezilehlý výsledek je přesný a není co opravit.
Zde je výslovně použito P=53, nikoli obecné neurčité „vyšší přesnosti“.

## FREM a FINT

Pro remainder r=y−nz s nejbližším sudým quotientem platí
|r|≤|z|/2 a zároveň |r|≤|y|: je-li |y|<|z|/2, quotient je nula;
jinak první mez již implikuje druhou. Pišme |y|=A·2^a, |z|=B·2^b.
r je násobkem 2^min(a,b). Pro a≤b jeho koeficient podle |r|≤|y|
má nejvýše 24 bitů; pro b<a má podle |r|≤|z|/2 dokonce nejvýše
23 bitů. Navíc je r násobkem skutečné short mřížky 2^−149. Nemůže
tedy vypadnout pod subnormální rozsah ani vyžadovat více než 24 bitů.
Je přesné binary32 i binary64, se znaménkem nuly určeným y.

Pro FINT je každý short s |z|≥2^23 již celý. Je-li |z|<2^23,
zaokrouhlený integer má |n|≤2^23 a vejde se přesně do 24 bitů.
V obou případech je výsledek sám short hodnota, bez druhého rounding.
Ztráta původní neceločíselné části však vyžaduje X; původní programová
vada a auditní oprava tohoto příznaku jsou samostatné S0004.

## NaN, infinity, nuly a výsledné eventy

LDSF přesně rozšíří payload i signaling bit bez arithmetic eventu.
Každá aritmetická operace pak podle svého již dokázaného type switch
buď vrátí správně quietovaný payload s potřebným I, vytvoří canonical
NaN pro neplatnou numerickou dvojici, nebo určí infinity/zero a sign.
STSF quiet NaN zúží bez dalšího I; původní short payload má všechny
bity v zachované části. Infinity i zero se přenesou se znaménkem.
Neplatné třídy, divide-by-zero a sign pravidla tedy mají přesně stejný
výsledek a I/Z události jako odpovídající short operace. Zvlášť je
potřeba S0003 pro záporné NaN FSQRT; tato vada se neskrývá pod lemma.

U konečných hodnot nemá mezilehlá binary64 operace O/U, jak bylo
ohraničeno výše. X vznikne právě tehdy, pokud je alespoň jedno z obou
zaokrouhlení neexaktní. Je-li přesný výsledek short, je přesný i
binary64, takže žádné falešné X nevznikne. Není-li short, nemohou být
oba převody přesné. O se rozhodne při STSF a vyžaduje správnou S0002
saturaci podle režimu. FINT X se vztahuje k necelému vstupu, přestože
je výsledný integer přesný; jeho STSF je exact a předchozí rA.X zůstane.

**U vyžaduje zvláštní kontrolu:** event z předchozí instrukce sám
nezpůsobí, aby STSF přijal svůj raw U jako neexaktní. Potenciální problém
by nastal, kdyby neexaktní binary64 mezivýsledek byl již přesným short
subnormálem. U FMUL je mezivýsledek exact; u součtu/rozdílu v subnormálním
oboru je výsledek kvůli mřížce 2^−149 přesný short. U FREM je rovněž
exact a FSQRT má jen normální kladné výsledky. FDIV nemůže falešně
dopadnout na **žádnou short hodnotu**, jak dokazuje samostatná širší
formulace výše. Jeho nenulový binary64 výsledek také nemůže být nula.
Proto STSF přidá X vždy, kdy je konečný tiny short výsledek neexaktní;
v přesném případě je správně raw U potlačeno. FINT může vrátit jen nulu
nebo integer a U u něj nenastává. To uzavírá U/X, nikoli pouze bity.

Výsledek a nové arithmetic eventy při vypnutých tripech jsou tedy
správné pro všech sedm operací a všechny čtyři režimy. Náklady tří
paměťových konverzí jsou podle tabulky 3μ+3υ, plus 4υ pro běžnou
aritmetiku nebo 40υ pro FDIV/FSQRT. U unary stačí jeden LDSF a náklady
jsou 2μ+2υ plus cena operace. Jde o deklarovaný model, ne C benchmark.
Tato věta neřeší desítkový vstup/výstup, obecné IEEE trap prostředí
ani jiné části MMIXware.
