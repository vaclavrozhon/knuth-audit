# §7.1.1–8 až 11: distributivita a koeficienty multilineárního tvaru

6. listopadu 2026, X0062. Zadání p80/file97, odpovědi p535/file552.
Originály images/file097.png a images/proof-file552.png; pruhy dlouhé
podmínky úlohy 8 navíc v proof-answer8-detail.png. Žádný matematický
program, tabulková enumerace 256 dvojic ani hledání formulí.

## P0568: distributivita je zachování pravé operace dvěma unárními mapami

Pro levou operaci o polož L_a(t)=a o t. Identita

    a o (b □ c) = (a o b) □ (a o c)

platí pro všechna a,b,c právě tehdy, když každá ze dvou map L₀,L₁
zachovává operaci □. Na B jsou přesně čtyři unární mapy. Jejich
nutné i postačující podmínky pro zachování jsou:

| unární mapa | podmínka na □ |
|---|---|
| id | žádná |
| konstanta 0 | 0 □ 0 = 0 |
| konstanta 1 | 1 □ 1 = 1 |
| negace | □(¬b,¬c)=¬□(b,c) pro všechna b,c |

Poslední podmínka říká, že tabulka □ má protilehlé bity opačné.
Při označení její tabulky wxyz je to w=¬z a x=¬y; možné tabulky
jsou 0011,0101,1010,1100, tedy obě projekce a jejich komplementy.
Definice množin S₀,S₁,S₂ v odpovědi je přesně tato klasifikace.

## P0569: všechny levé operace, bez vynechané kombinace

Řádky pravdivostní tabulky levé operace o jsou právě tabulky L₀,L₁.
Každý řádek 00,01,10,11 proto přiřadí podmínku S₀, žádnou,
S₂ nebo S₁. Průnik obou podmínek je přesně nutný i postačující.

| levá tabulka o | obě unární mapy | všechny dovolené pravé □ |
|---|---|---|
| 0000 | 0,0 | S₀ |
| 0001 | 0,id | S₀ |
| 0010 | 0,neg | S₀∩S₂ |
| 0011 | 0,1 | S₀∩S₁ |
| 0100 | id,0 | S₀ |
| 0101 | id,id | všechny |
| 0110 | id,neg | S₂ |
| 0111 | id,1 | S₁ |
| 1000 | neg,0 | S₀∩S₂ |
| 1001 | neg,id | S₂ |
| 1010 | neg,neg | S₂ |
| 1011 | neg,1 | S₁∩S₂ |
| 1100 | 1,0 | S₀∩S₁ |
| 1101 | 1,id | S₁ |
| 1110 | 1,neg | S₁∩S₂ |
| 1111 | 1,1 | S₁ |

Toto je přesně sedm skupin v odpovědi 8, rozepsaných tak, aby
každá levá operace měla jasnou doménu pravých operací.

## P0570: číslo 92

S₀ má první bit fixovaný na 0, tedy 8 členů; S₁ má poslední bit
fixovaný na 1, také 8. S₀∩S₁ má dva volné bity, tedy 4 členy.
S₂ má dva volné bity a oba jejich komplementy, tedy 4.
S₀∩S₂ a S₁∩S₂ mají po 2 členech. Počet párů je proto

    3·8 + 3·8 + 2·4 + 3·4 + 2·2 + 2·2 + 16 = 92.

Skupiny levých operací jsou disjunktní a pokrývají všech šestnáct.
Nikde se tedy nepřekrývají započítané uspořádané páry; počet není
empirickým výstupem programu.

## P0571: celá Schröderova algebraická podmínka v odpovědi

Nechť tabulky o a □ jsou pqrs a wxyz. Aby L₀ nebo L₁ byla
konstanta 1, musí pq∨rs=1. Selhání požadované podmínky z=1 je
tedy přesně (pq∨rs)∧¬z.
Konstanta 0 se objeví právě při ¬p¬q∨¬r¬s=1; její selhání je
(¬p¬q∨¬r¬s)∧w.
Negace se objeví právě při p¬q∨r¬s=1. Její zachování selže
právě při w=z nebo x=y, tedy při (w≡z)∨(x≡y).

Disjunkce těchto tří selhání se rovná nule právě tehdy, když
není žádné selhání:

    ((pq∨rs)∧¬z)
    ∨ ((¬p¬q∨¬r¬s)∧w)
    ∨ ((p¬q∨r¬s)∧((w≡z)∨(x≡y))) = 0.

To je celý vytištěný vzorec včetně všech negací a obou ekvivalencí.
Není zaměněn s dřívějšími symboly proměnných v samotné distributivitě.

## P0572–P0574: všechny části úlohy 9 a dodatky odpovědi

**P0572, (a):** tvrzení je nepravdivé. Pro x=y=0,z=1 je
(x⊕y)∨z=1, ale (x∨z)⊕(y∨z)=1⊕1=0.
Opravená identita v odpovědi přidává XOR z. Při z=0 jsou obě
strany x⊕y; při z=1 je pravá strana 1⊕1⊕1=1, stejně jako levá.
Je tedy dokázána jak neplatnost zadané, tak platnost opravené identity.

**P0573, (b):** pro z=0 se obě strany rovnají w⊕x⊕y. Pro z=1
je levá 1 a pravá XOR tří jedniček, také 1. Zadaná identita platí.

**P0574, (c):** kterýkoli z výrazů
(x⊕y)∨(y⊕z), (x⊕z)∨(y⊕z), (x⊕y)∨(x⊕z)
je 0 právě tehdy, když příslušné dvě rovnosti vynutí x=y=z.
Proto jsou všechny tři rovny 1−[x=y=z]. To dokazuje zadanou
rovnost i obě doplněná tvrzení odpovědi.

## P0575: úloha 10, celý konkrétní multilineární polynom

Vstup je tabulka (22), 1100100100001111 v pořadí wxyz.
Při z=0 vybereme sudé pozice a dostaneme g(w,x,y)=10100011.
Při z=1 dostaneme 10010011, tedy
h(w,x,y)=10100011 XOR 10010011 = 00110000.
Oba mezivýsledky v odpovědi jsou správné.

Při w=0 je g=¬y, při w=1 je g=x. Proto nad F₂

    g = 1+y+w(1+y+x) = 1+y+w+wy+wx.

h je pravdivé právě při w=0,x=1, nezávisle na y, tudíž
h=(1+w)x=x+wx. Rozklad f=g+hz dává

    f(w,x,y,z) = 1+y+xz+w+wy+wx+wxz  (mod 2),

přesně jako odpověď. Jedinečnost takto získaného multilineárního
polynomu už dokazuje P0532; není nutné ji odvozovat znovu.
Jako kontrola použitých vstupů: při w=0 je f=1+y+xz s tabulkou
11001001, při w=1 je f=x s tabulkou 00001111, dohromady původní
šestnáctibitový vstup. Nejde o hledání mezi polynomy.

## P0576: úloha 11, obecný koeficient a celý tříproměnný dodatek

Piš f(x)=Σ_S a_S ∏_(j∈S)x_j nad F₂. Pro charakteristický
vektor 1_T platí f(1_T)=Σ_(S⊆T)a_S. Sečti přes všechna T⊆U:

    Σ_(T⊆U) f(1_T)
      = Σ_(S⊆U) a_S · 2^{|U∖S|}
      = a_U  (mod 2).

Poslední rovnost platí, protože všechny mocniny dvojky s kladným
exponentem jsou sudé; jediný lichý příspěvek má S=U. Koeficient
monomu na U je tedy parita počtu jedniček funkce při vynulování
všech proměnných mimo U. Zůstává právě 2^{|U|} vstupů.
Pro monom x₂x₃x₆x₈ se opravdu nulují indexy 1,4,5,7,9,10,…
a mění se pouze uvedené čtyři proměnné.

Pro n=3 a pořadí x,y,z dávají koeficienty členů
1,z,y,yz,x,xz,xy,xyz přesně
f₀₀₀,f₀₀*,f₀*₀,f₀**,f*₀₀,f*₀*,f**₀,f***,
kde hvězdička označuje součet obou možností modulo 2.
Zvláště f**₀=f(1,1,0)⊕f(1,0,0)⊕f(0,1,0)⊕f(0,0,0),
jak je vytištěno. Pro U=∅ není žádná hvězdička, jediné
vyhodnocení je f(0); argument pokrývá i nulární funkci.

## Meze a pokračování

Všechna zadání 8–11 a matematické dodatky jejich odpovědí jsou
doloženy. Schröderovu historickou prioritu a citaci knihy z roku
1905 nepovyšuji na nezávisle ověřenou. V této části nevzniklo
podezření ani nový nález; relevantní errata zůstávají zohledněna.
Další úloha 12: celočíselná multilineární reprezentace, mez velikosti
koeficientů, hodnoty uvnitř krychle a monotónnost; zbylá část p535
ani celá p80 tím dosud nejsou uzavřeny.
