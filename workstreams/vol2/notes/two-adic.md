# §4.1-31: 2-adická aritmetika a chybějící nulový případ

Kontrola 2. listopadu 2026. Původní strany 213 a 610 (DjVu 225 a 622)
byly znovu vizuálně přečteny. Části (a–c), algoritmus H i všech osm
vytištěných koncových bitových řetězců souhlasí. Část (d) potřebuje
výjimku `n = 0`, evidovanou jako **V2-C0080**. Jde o formulaci kritéria,
nikoli o chybu algoritmu H pro liché vstupy.

## 1. Význam nekonečného zápisu a dělení

2-adické celé číslo je konzistentní volba zbytků modulo `2,4,8,...`.
Ekvivalentně jde o bity `u_0,u_1,...`, z nichž prvních `h` udává
zbytek modulo `2^h`. Nekonečná řada se zde neposuzuje podle reálné
konvergence: konverguje právě tehdy, když se pro každý pevný počet
nejnižších bitů jejich hodnoty od jisté chvíle nemění. Obecné 2-adické
číslo navíc připouští konečně mnoho pozic se zápornými indexy.

Pro nenulové číslo `u` označme `v_2(u)` jeho nejnižší nenulovou pozici.
Pak `u = 2^a U`, kde `a = v_2(u)` je celé číslo a `U` je liché 2-adické
celé číslo. Nejnižší nenulová cifra součinu dvou nenulových čísel je
součin jejich nejnižších nenulových cifer modulo 2. Proto
`v_2(uv) = v_2(u)+v_2(v)` a součin není nula.

Pro dělení stačí rozdělit čitatele a jmenovatele na mocninu dvojky
a celou část: podíl `2^a U / (2^b V)` je `2^(a-b)` krát podíl `U/V`,
kde `V` je liché. Ten získáme po bitech. Je-li již
`U = V W (mod 2^h)`, potom pro `epsilon` v `{0,1}`

```
V(W + epsilon*2^h) = VW + epsilon*2^h  (mod 2^(h+1)).
```

Právě jedna volba opraví následující bit. Začínáme `W = U mod 2`.
Každý bit je vynucený; kompatibilní limity dávají existenci i jednoznačnost.
To přesně odpovídá postupu na straně 610. Základní zákony operací platí
na každé konečné úrovni modulo `2^h`, a tedy i pro celé zápisy. Tím je
odůvodněna zmínka o tělese, tj. aritmetickém systému, kde lze dělit
každým nenulovým prvkem.

## 2. Racionální čísla a periody

Pro liché `d = 2n+1 > 1` existuje kladné `k` s `2^k = 1 (mod d)`:
násobení dvěma permutuje konečně mnoho zbytků nesoudělných s `d`.
Položme `m = (2^k-1)/d` a zapišme `m` přesně `k` bity jako slovo `alpha`.
V obvyklé reálné aritmetice opakování tohoto slova za bodem dává
`m/(2^k-1) = 1/d`. Opakování téhož slova doleva má 2-adickou hodnotu

```
m * (1 + 2^k + 2^(2k) + ...) = m/(1-2^k) = -1/d.
```

Směr bitů uvnitř slova se neobrací. Tím je dokázána část (b).

Pro část (c) lze periodicitu racionálních čísel dokázat bez odvolání
na neprokázanou uzavřenost periodických zápisů. Pro celé `m` a liché
kladné `d` volíme postupně

```
r_0 = m;
epsilon_j = r_j mod 2;
r_(j+1) = (r_j - d epsilon_j)/2.
```

Invariant zní `m/d = sum_{i<j} epsilon_i 2^i + 2^j r_j/d`.
Zbytky jsou celá čísla a `abs(r_(j+1)) <= abs(r_j)/2 + d/2`.
Od jisté chvíle zůstanou v konečném intervalu. Proto se deterministická
posloupnost zbytků a jejích výstupních bitů začne opakovat. Obecný
racionální podíl dostaneme posunem bodu o konečně mnoho míst.

Naopak zápis s periodou délky `lambda` od pozice `M` je součtem
konečného dyadického racionálního prefixu `A` (jmenovatel je mocnina 2)
a ocasu `2^M B/(1-2^lambda)`, kde `B` je celočíselná hodnota jednoho
bloku. Je tedy racionální. Tato argumentace také vysvětluje známou
opravu z 26. ledna 2007: k odstranění zlomkového prefixu musí být
mocnina dvojky dostatečně velká, ne bezpodmínečně `2^(-mu)` z původního
textu. Náš závěr tuto zveřejněnou opravu nezapočítává jako nový nález.

## 3. Odmocniny a invariant algoritmu H

Pro **nenulové** celé `n` je existence 2-adického `v` s `v^2=n`
ekvivalentní těmto dvěma podmínkám: `v_2(n)=2k` je sudé a lichá část
`n/2^(2k)` je `1 modulo 8`. Dohromady to je přesně tištěná kongruence

```
n mod 2^(2k+3) = 2^(2k),     k >= 0.
```

Nutnost: nejnižší pozice čtverce je dvojnásobkem nejnižší pozice
odmocniny. Lichý čtverec je `1 modulo 8`, neboť pro `v=1+2t`
platí `v^2=1+4t(t+1)` a jedno z `t,t+1` je sudé.

Postačitelnost stačí dokázat pro `n = 1 modulo 8`, potom odmocninu
vynásobíme `2^k`. Algoritmus H začíná `k=2`, `v=1`, `m=(n-1)/8`
a udržuje

```
v = sum_{j<k} v_j 2^j,       v^2 = n - 2^(k+1) m.
```

Při sudém `m` se nový bit rovná nule a `m` se vydělí dvěma.
Při lichém `m` se položí `v_new=v+2^k` a
`m_new=(m-v-2^(k-1))/2`, s původní hodnotou `v` na pravé straně.
Rozvinutí `(v+2^k)^2` dokazuje invariant s `k_new=k+1`.
Limit `v` existuje po bitech a má čtverec `n`, protože chyba má stále
vyšší dělitelnost dvojkou. Algoritmus vybírá větev `v=1 modulo 4`;
opačná odmocnina je `-v`, tedy `3 modulo 4`.

Každé nenulové `n`, které má odmocninu, má právě dvě: z rovnosti
`u^2=v^2` plyne `(u-v)(u+v)=0`, a součin nenulových 2-adických čísel
není nula podle části 1. Naproti tomu nula má jedinou odmocninu nula.
Čtyři kořeny modulo konečného `2^h` tomu neodporují: při zvyšování
přesnosti ne všechny konečné volby pokračují stejným způsobem.

## 4. V2-C0080: vynechané n = 0

Zadání na straně 213 říká celé `n`, bez vyloučení nuly. Pro `n=0`
je levá strana tvrzené ekvivalence pravdivá (`sqrt(0)=0`), pravá je
nepravdivá pro každé `k >= 0`: zbytek nuly je nula, zatímco `2^(2k)>0`.
Nejmenší oprava je vložit slovo „nonzero“ před „integer“; případně
přidat alternativu `n=0` do kritéria.

Původní stránka byla 2. listopadu 2026 znovu vizuálně zkontrolována.
Ve všech čtyřech vrstvách `all2-prepre`, `all2-pre`, `all2`, `err2`
a v uloženém aktuálním `err2.textxt` byly hledány strany 213/610,
číslo úlohy, Hensel, 2-adická aritmetika a odmocniny. Relevantní jsou
pouze oprava části (c) z roku 2007 a změna Henselovy citace z roku 2023;
nulový případ (d) neopravují. Fyzický nejnovější dotisk, prvenství ani
nárok na odměnu nejsou ověřeny. [ASCII návrh](../reports/C0080-two-adic-zero-draft.txt)
zůstává neodeslaný.

## 5. Přesné kontroly a jejich meze

[Program](../verify_two_adic.py) porovnává bitové dělení s Eukleidovým
modulárním inverzem v 17885 případech. Úplná množina čtverců modulo
32768 nezávisle ověřila kritérium pro všech 8193 celých vstupů od −4096
do 4096; na tomto intervalu postačuje přesnost i pro nejvyšší možnou
valuaci 12. Algoritmus H ověřen pro 1025 kladných i záporných lichých
vstupů do 64 bitů s přesnou kontrolou invariantu. Dalších 128 úplných
množin kořenů modulo 1024 souhlasí s nezávislým výčtem čtverců.

Pro 100 lichých jmenovatelů 3–201 ověřeny přesné periodické identity.
Všech šest vytištěných racionálních a oba 15bitové odmocninové konce
souhlasí; úplnost period plyne z geometrických řad výše, nikoli jen
z konečného testu. Zejména `-1/7 = sum_{j>=0} 8^j` a
`1/5 = 1 + 12 sum_{j>=0} 16^j` vysvětlují periodické příklady.
Odmocninové konce jsou `100000010110101` a `011111101001011`.

První běh skončil až při porovnání vlastního chybného přepisu `1/10`
jako `7/10`. Zvětšený výřez originálu jednoznačně ukázal `1/10`.
Hotové bloky byly zachovány a obnoven pouze závěrečný blok, s exit 0.
[JSON](../results/two-adic.json) uvádí rekonstrukci počtů po této chybě;
[log](../results/two-adic.log) obsahuje první selhání i úspěšné dokončení.
Úspěšné kontroly nebyly opakovány.

Henselova historická citace je v erratech z 18. prosince 2023 posunuta
z článku roku 1904 na Jahresbericht der Deutschen Mathematiker-Vereinigung
6 (1897), 83–88. Její primární historické ověření patří do kontextového
bloku; důkazy výše jsou nezávislé na této atribuci.
