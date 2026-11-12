# Binární porovnání a přesná délka většiny, celá úloha 106

7. listopadu 2026, X0120, P1132–P1137. Zadání p92/file109 a odpověď
p553/file570 zobrazeny v původní sazbě. Pruhy jsou nad y i z; podmínka
je ≥, nikoli >. Žádný matematický program ani enumerace vstupů.

## 1. Identita a všechny její okraje

Položme N=2^n, q_i=2^(n−i), X=Σq_i x_i, Y=Σq_i y_i. Polarizované
vstupy jsou x_i, b_i=¬y_i a c=¬z. Většina v odpovědi má násobnosti
q_i u x_i i b_i a jednu u c. Její délka a práh jsou

    L=2Σq_i+1=2N−1,       T=N.

Její skutečný počet jedniček je

    S=X+(N−1−Y)+(1−z)=N+X−Y−z.

Proto S≥N právě když X≥Y+z. Toto pokrývá i přenos Y=N−1,z=1:
pravá strana je N a žádné X nevyhoví. Pro X=Y je výsledek ¬z.
Při n=1 máme přesně úvodní identitu ⟨x ¬y ¬z⟩=[x≥y+z].
Při n=0 zůstává ⟨¬z⟩=[0≥z], délka 1; nic se nedělí nulou.

## 2. Vnořená verze a její cena

Začněme C_(n+1)=¬z a pro i=n,…,1 počítejme

    C_i=⟨x_i ¬y_i C_(i+1)⟩.

Jsou-li x_i=y_i, první dva vstupy jsou opačné a výsledek je C_(i+1).
Je-li x_i>y_i, jsou oba 1 a výsledek je 1; je-li x_i<y_i, jsou oba 0.
Invariant tedy říká, že C_i testuje příslušné binární suffixy s původním
z. První rozdílný bit rozhodne správně; shodné suffixy předají ¬z.
Výpočet končí po n mediánech tří, s hloubkou n a jedním stavovým bitem
při průchodu od nejnižšího bitu. Případné vstupní negace mají lineární
celkovou cenu. Výpis ploché většiny má oproti tomu 2N−1 výskytů.

To také přesně souhlasí s již dokázanou identitou 99 (proof-085): při
rozbalování další úrovně dostanou dva nové vstupy násobnost 2^k, kde
k nižších bitů bylo již zpracováno. Dolní mez níže je pro jednu plochou
většinu vstupních literálů, nikoli pro počet hradel tohoto obvodu.

## 3. Obecná rodina nutných nerovností

Vezměme všechny hraniční pravdivé vstupy X=Y+z. Tvoří je dvě
disjunktní rodiny:

* z=0 a X=Y=0,…,N−1: N vstupů;
* z=1, Y=0,…,N−2 a X=Y+1: N−1 vstupů.

Je jich přesně 2N−1. Jejich polarizované podpory mají váhu S=N,
takže jsou prime: odebrání kteréhokoli jedničkového vstupu sníží
váhu alespoň o 1. Pro libovolné nové násobnosti u_i,v_i,w v čisté
většině proto každá taková podpora B vyžaduje

    2Σ_(j∈B) a_j − Σ_all a_j ≥ 1,

kde a=(u_1,…,u_n,v_1,…,v_n,w). Stačí tyto nutné nerovnosti;
netvrdíme, že jsme tím vypsali všechny prime podpory.

V první rodině je každé x_i a b_i jedničkou N/2 krát a c vždy.
Ve druhé je každé x_i jedničkou N/2 krát, protože z úplného rozsahu
X zmizela jen nula; stejně každé b_i je jedničkou N/2 krát, protože
z rozsahu Y zmizel jen vektor samých jedniček. Hodnota c je zde 0.
Každý z 2n+1 vstupů tedy má ve všech řádcích dohromady incidenci N.
Součet nerovností má u každé násobnosti koeficient

    2N−(2N−1)=1.

Dostáváme Σu_i+Σv_i+w≥2N−1, což konstrukce v §1 dosahuje.
Pro n=0 tatáž úvaha obsahuje jediný vstup c=1 a dává w≥1;
počítání N/2 se v tomto nulárním případě nepoužije.

## 4. Každá ze sedmi vytištěných nerovností pro n=2

Při pořadí koeficientů (u_1,u_2,v_1,v_2,w) odpovídají vytištěné
řádky přesně následujícím hraničním vstupům. Znaménko + znamená
jedničku příslušného polarizovaného vstupu.

| Řádek odpovědi | X | Y | z | Znaménka |
|---|---:|---:|---:|---|
| 1 | 3 | 2 | 1 | ++−+− |
| 2 | 3 | 3 | 0 | ++−−+ |
| 3 | 2 | 1 | 1 | +−+−− |
| 4 | 2 | 2 | 0 | +−−++ |
| 5 | 1 | 0 | 1 | −+++− |
| 6 | 1 | 1 | 0 | −++−+ |
| 7 | 0 | 0 | 0 | −−+++ |

Každý sloupec má čtyři plusy a tři minusy. Nejde jen o kontrolu
tohoto příkladu: §3 dává chybějící obecný argument pro každé n.

## 5. Konstanty ani opačné literály mez neobcházejí

Polarizovaná funkce je monotónní a self-duální: komplement všech
vstupů změní D=X−Y−z na −D−1, čímž se výsledek obrátí.
Každá proměnná je podstatná, protože se vyskytuje v některé hraniční
prime podpoře a její odstranění změní výsledek.

Libovolná plochá většina literálů a konstant se po sečtení opačných
výskytů píše [a·r≥t] s celočíselným t. Monotónnost a podstatnost
vynucují a_j>0: nulový koeficient by proměnnou odstranil, záporný
by nedovolil žádný přechod 0→1 zvýšením tohoto bitu. Součet A=Σa_j
je nejvýše původní počet výskytů, i kdyby obsahoval konstanty.

Pro pravdivou podporu B je s=Σ_B a_j≥t a její komplement je
nepravdivý, takže A−s≤t−1. Tedy

    2s−A ≥ max(2t−A, A−2t+2) ≥ 1.

Platí přesně všechny nutné nerovnosti z §3, bez předpokladu předem
vycentrovaného prahu. Proto i celková délka původního výrazu je
nejméně A≥2N−1. Tím je dolní mez doložena i pro tuto širší konvenci.

## Errata a rozsah

Prohlédnuty relevantní zásahy a hledání podle stránek, čísel úloh
i témat v all4a-pre, all4a, err4a, all4f0 a err4f0. Opravy odpovědi
108 ve fasciklu na p148 patří grafům, nikoli tomuto bloku. Vrstvy
neobsahují opravu 106; žádný nový rozpor zde nevznikl. Úloha 106
včetně úvodní identity, obou částí a vnořeného dodatku je checked.
