# Všech 16 Chowových parametrů a self-duální kofaktory, 107–108

7. listopadu 2026, X0120, P1138–P1143. Původní zadání p92/file109,
odpovědi p553/file570 a p554/file571 zobrazeny. Přesně přebíráme
celou Table 1 z proof-028/P0512 a Theorem T z proof-084; neopakujeme
jejich důkazy. Níže jsou nové jednotlivé argumenty požadovaných údajů.

## 1. Úplná tabulka 107

Pro čtyři výstupy (a,b,c,d) v pořadí 00,01,10,11 z definice platí

    N(f)=a+b+c+d,       Σ(f)=(c+d,b+d).

První složka tedy sčítá jen vstupy 10 a 11, druhá jen 01 a 11.
Každý řádek následující tabulky je přímým dosazením do těchto dvou
rovnic; symbolické názvy odpovídají přesně dříve doložené Table 1.
Poslední sloupec současně udává konkrétní prahovou reprezentaci
[w_1 x+w_2 y≥t] všude, kde existuje.

| Výstupy | Funkce | N | Σ | (w_1,w_2,t) |
|---|---|---:|---|---|
| 0000 | false | 0 | (0,0) | (0,0,1) |
| 0001 | x∧y | 1 | (1,1) | (1,1,2) |
| 0010 | x∧¬y | 1 | (1,0) | (1,−1,1) |
| 0011 | x | 2 | (2,1) | (1,0,1) |
| 0100 | ¬x∧y | 1 | (0,1) | (−1,1,1) |
| 0101 | y | 2 | (1,2) | (0,1,1) |
| 0110 | xor | 2 | (1,1) | neexistuje |
| 0111 | or | 3 | (2,2) | (1,1,1) |
| 1000 | nor | 1 | (0,0) | (−1,−1,0) |
| 1001 | equivalence | 2 | (1,1) | neexistuje |
| 1010 | ¬y | 2 | (1,0) | (0,−1,0) |
| 1011 | y⇒x | 3 | (2,1) | (1,−1,0) |
| 1100 | ¬x | 2 | (0,1) | (−1,0,0) |
| 1101 | x⇒y | 3 | (1,2) | (−1,1,0) |
| 1110 | nand | 3 | (1,1) | (−1,−1,−1) |
| 1111 | true | 4 | (2,2) | (0,0,0) |

Všechny hodnoty N a Σ souhlasí s každou položkou odpovědi 107.
Rozdílné funkce xor a equivalence mají stejné N i Σ; kdyby některá
byla prahová, již dokázaná Theorem T by vynutila jejich rovnost.
Proto ani jedna prahová není. Ostatních 14 má explicitní reprezentaci
v tabulce. Samotná odlišnost jejich parametrů by tento kladný závěr
nedokazovala; proto byly uvedeny i váhy a prahy.

## 2. Obě části 108 pro n>0

Nechť g(x_0,x_1,…,x_n) je self-duální a Σ(g)=(s_0,s_1,…,s_n).
Komplement vstupu je involuce bez pevného bodu a každá jeho dvojice
obsahuje právě jeden pravdivý vstup. Proto N(g)=2^n.

Označme f_0(x)=g(0,x), f_1(x)=g(1,x). Složka s_0 z definice
počítá právě jedničky s x_0=1, takže

    N(f_1)=s_0,             N(f_0)=2^n−s_0.

Rozdělení všech vstupů podle x_0 dává pro j=1,…,n

    Σ_j(f_0)+Σ_j(f_1)=s_j.

Self-dualita navíc znamená f_0(x)=1−f_1(1−x). Bijektivní záměna
y=1−x v konečném součtu dává

    Σ_j(f_0)
      = Σ_x x_j (1−f_1(1−x))
      = 2^(n−1) − Σ_y (1−y_j) f_1(y)
      = 2^(n−1) − s_0 + Σ_j(f_1).

Právě 2^(n−1) vektorů x má x_j=1, což vysvětluje první člen.
Vyřešením těchto dvou lineárních rovnic dostáváme jednotlivě

    (a) Σ_j(f_0)=(s_j−s_0+2^(n−1))/2,
    (b) Σ_j(f_1)=(s_j+s_0−2^(n−1))/2.

Jde o přesné vytištěné vzorce, včetně všech znamének a faktoru 1/2.
Celočíselnost a nezápornost vyplývají z odvozených konečných součtů;
netvrdíme přípustnost vzorců pro libovolný nezávisle zvolený vektor s.

## 3. Okraje, historický dodatek a rozsah

Konstantní kofaktory jsou přípustné: g=x_0 dává s_0=2^n,
s_j=2^(n−1), tudíž f_0=0 a f_1=1; pro g=¬x_0 je tomu naopak.
Odpověď výslovně omezuje souřadnicové vzorce na n>0. Při n=0
existuje jediný bit x_0, g je x_0 nebo ¬x_0, N(f_1)=s_0,
N(f_0)=1−s_0 a oba vektory Σ jsou prázdné. Není třeba přiřazovat
hodnotu neexistující souřadnici s členem 2^(−1).

Historická atribuce ekvivalentních výsledků Gotovým přednáškám na
MIT v roce 1963 nebyla nezávisle ověřena; jde o výslovný bibliografický
skip, nikoli o matematický předpoklad. Dříve získaný částečný článek
Goto–Takahasi z roku 1962 tuto odlišnou atribuci nedokládá.

Tentýž cílený průchod pěti erratovými vrstvami jako v proof-092
neukázal opravu tohoto obsahu. Číslo 108 v grafové odpovědi na p148
historického fasciklu patří jinému zadání. Celé 107 a obě části 108
včetně matematických dodatků jsou checked; okolní úlohy tím nejsou.
