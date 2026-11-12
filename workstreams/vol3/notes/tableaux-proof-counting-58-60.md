# Počty tableaux58–60 a úloha17: rekurence, determinant a háčky

Kontrola vzorců(30)–(36), Fig.5 a Theorem H ze sazby69–71; úloha17
na66 a odpověď608. Všechny relevantní vrstvy již obsahuje
sources/tableaux-errata-review.json. Na60 se použije známá oprava
n_2+m−1→n_2+m−2, nikoli původní chybný faktor. Nejde o nález.
Historická prvenství a citace Robinson/Schensted/Schützenberger,
Frobenius/MacMahon a Frame–Robinson–Thrall jsou výslovně neověřená
bibliografie. Výrok o rozšíření korespondence na opakované štítky
je naopak matematická závislost a není schován mezi bibliografii;
má samostatné argumenty P0445–0447 v tableaux-proof-repeated-labels.md.
Souvislost se stromy na konci60 se
doplní v následujícím bloku s pokračováním61.

## P0432–433: přesná rekurence a příklad(33)

Velikost n je nezáporný počet označených buněk. Pro neplatný tvar
λ=(n_1,…,n_m) je f(λ)=0 podle definice; přidání nulového řádku
nic nemění a f(prázdný tvar)=1. V neprázdném tableau leží maximum n
v rohu, jinak by existoval větší soused vpravo/dole. Jeho odstranění
dává tableau jednoho z tvarů λ−e_i. Naopak každé tableau takového
platného tvaru lze jednoznačně doplnit n právě v tomto rohu. Možnosti
jsou disjunktní podle jeho pozice, takže platí(32); neplatné výsledky
mají nulu. Po ignorování koncových nul rekurence zmenšuje n, proto
spolu s prázdným základem určuje f jednoznačně.

Pro(6,4,4,1) lze maximum15 odstranit v(1,6),(3,4),(4,1). Odstranění
z(2,4) by dalo(6,3,4,1), tedy neplatný tvar a nulový člen. Poslední
možnost(6,4,4,0) se rovná(6,4,4). To ověřuje celý součet i všechny
tři schematické diagramy(33), ne pouze jejich počet.

## P0434: determinant(35) a jeho znaménko

D(x)=det(x_j^(m−i))_(i,j=1)^m je alternující homogenní polynom
stupně d=binom(m,2). Při x_i=x_j jsou dva sloupce shodné, takže
každý x_i−x_j pro i<j dělí D. Různé takové lineární faktory jsou
nesoudělné v polynomiálním okruhu nad Q, proto jejich součin Δ dělí D.
Oba mají stejný stupeň, takže D=cΔ. Koeficient monomu
x_1^(m−1)x_2^(m−2)…x_m^0 je v determinantu1 (identická permutace)
a v součinu rovněž1; volby potřebných členů jsou postupně vynuceny.
Tedy c=1, včetně správného znaménka při obráceném pořadí exponentů.
Pro m=0,1 dává prázdný determinant/součin1. Druhá mocnina Δ je
přesně součin čtverců rozdílů, tedy diskriminant v použitém významu.

## P0435–436: úloha17, včetně všech kroků odpovědi

Označme g(x;y)=Σ_i x_i Δ(x_1,…,x_i+y,…,x_m). Po permutaci x se
jen přeuspořádají sčítance a Δ přidá znaménko permutace. Proto je
g alternující a je dělitelný Δ stejným argumentem jako výše. Součet
má homogenní stupeň d+1 v x,y; podíl g/Δ je tudíž symetrický
homogenní polynom stupně1. Musí mít tvar aΣx_i+b y.

Položení y=0 dává a=1. Derivace podle y při0 dává
Σ_i x_i∂_iΔ=dΔ podle Eulerovy identity pro homogenní polynom,
ověřitelné po jednotlivých monomech. Tedy b=d=binom(m,2), což
dokazuje celé zadání, pro libovolné x a y včetně shodných x.

Rovněž explicitní výpočet odpovědi608 souhlasí. Pro navzájem různé
x je ∂_iΔ/Δ=Σ_(j≠i)1/(x_i−x_j). Dva členy každého neuspořádaného
páru dávají x_i/(x_i−x_j)+x_j/(x_j−x_i)=1. Párů je binom(m,2).
Racionální mezikrok slouží jen mimo diagonály; výsledná polynomiální
identita pak platí i na nich. Pro m=1 je g=x_1, pro prázdný součet0.

## P0437–438: vzorec(34), jeho doména a skutečná indukce

Položme L_i=n_i+m−i. Pro platný tvar jsou L_i přísně klesající
nezáporná celá čísla. Navržená pravá strana je

    F(λ)= n! Δ(L_1,…,L_m) ∏_i 1/L_i!.

Je třeba rozlišit podmínku na59, která požaduje jen L_1≥…≥L_m,
od podmínky platného tvaru. Pokud některé n_i<n_(i+1), celočíselnost
a uvedená slabá nerovnost nutí L_i=L_(i+1), takže Δ=0. Pokud n_m<0,
je1/L_m!=0. Zde nejde o nově vymyšlenou konvenci: svazek1,
§1.2.5, tištěná49, u Eulerova rozšíření výslovně bere faktoriál
záporného celého čísla jako nekonečno. Čteme tedy součin převrácených
faktoriálů; n samotné je stále nezáporná velikost. Tím F splní(30)
v celé uvedené mírně rozšířené doméně. Není tvrzena hodnota n! pro
záporný počet buněk. Mimo podmínku na L není(34) přislíbena.

Přidání koncového nuly mění L na(L_1+1,…,L_m+1,0). Nový
Vandermondův součin je Δ(L)∏(L_i+1), nový faktoriálový jmenovatel
je ∏(L_i+1)L_i!, takže se přidané faktory přesně zruší. To dokládá
(31) pro platné tvary; neplatné mají na obou stranách0. Z prázdného
tvaru se tak odvodí i F(0,…,0)=1, potřebný základ indukce.

Zbývá netriviální rekurence. Když n_m≥1, všechna L_i≥1 a

    Σ_i F(λ−e_i)
     = (n−1)!/(∏L_j!) · Σ_i L_i Δ(L_1,…,L_i−1,…,L_m).

Jestliže λ−e_i poruší tvar, sousední posunuté L se shodnou a jeho
člen skutečně zmizí; nemusíme takové i tiše vynechávat. Úloha17 při
y=−1 mění poslední součet na

    (ΣL_i−binom(m,2))Δ(L)=nΔ(L).

Celý výraz je tedy F(λ), přesně(32). Jednoznačnost rekurence s
prázdným základem dokazuje F=f, včetně nulových řádků a singletonu.

## P0439–440: všechny faktory v součtu(36)

Theorem A říká, že n! permutací je v bijekci s dvojicemi tableaux
stejného tvaru. Pro pevný tvar λ je párů f(λ)^2, proto
n!=Σ_(λ⊢n) f(λ)^2. Každý tvar doplňme nulami na přesně n řádků
a položme q_i=n_i+n−i. Pak q_1>…>q_n≥0 a
Σq_i=n+n(n−1)/2=n(n+1)/2.

Naopak každá přísně klesající nezáporná n-tice s tímto součtem dává
n_i=q_i−(n−i)≥0 (protože q_i≥n−i) a n_i≥n_(i+1). Jde tedy
o skutečnou bijekci indexových množin, ne jen formální substituci.
Vzorec(34) dává

    n!=n!² Σ_(q_1>…>q_n≥0, Σq_i=n(n+1)/2) Δ(q)^2/∏q_i!².

Přísně uspořádaný součet je tedy1/n!. Sčítanec je symetrický a
při shodě dvou q nulový. Uvolnění jejich pořadí proto každý nenulový
člen započte přesně n! krát, nikoli(2n)! ani jiný faktor. Výsledný
neuspořádaný součet je1, jak v(36). Pro n=0 má prázdná n-tice
jediný člen1 a rovnost zůstává správná.

## P0441: všechny délky Fig.5

Pro tvar λ a délky sloupců λ'_j má buňka(i,j) háček

    h_ij=λ_i−j+λ'_j−i+1.

Počítáme ji jednou, buňky napravo a buňky dole; oba poslední úseky
jsou disjunktní. Fig.5 má řádky(7,6,6,4,2,2) a sloupce
(6,6,4,4,3,3,1). Dosazení po řádcích dává

    12 11 8 7 5 4 1
    10  9 6 5 3 2
     9  8 5 4 2 1
     6  5 2 1
     3  2
     2  1.

To jsou všechny vytištěné hodnoty. Stínovaný háček(2,3) má čtyři
buňky v řádku včetně rohu a dvě pod ním, tedy6. Největší háček
je h_11=λ_1+m−1: v řádku i je největší h_i1=L_i≤L_1.

## P0442–443: chybějící délky, součin a Theorem H

Pro skutečné kladné řádky jsou L_i=λ_i+m−i přísně klesající kladná
čísla. V řádku i je λ_i různých háčků, všechny v{1,…,L_i}; délky
se při posunu doprava striktně zmenšují. Pro každý k>i ukážeme,
že číslo L_i−L_k=λ_i−λ_k+k−i nemůže být délkou v tomto řádku.

Jestliže j≤λ_k, potom λ'_j≥k a
h_ij≥λ_i−λ_k+k−i+1=(L_i−L_k)+1. Jestliže j>λ_k, potom
λ'_j≤k−1 a h_ij≤λ_i−λ_k+k−i−1=(L_i−L_k)−1. To pokrývá
všechny buňky řádku i, včetně stejných délek sousedních řádků.

Těchto m−i chybějících čísel je různých, kladných a menších než L_i.
Spolu s λ_i=L_i−(m−i) různými skutečnými háčky tak vyčerpávají
celé{1,…,L_i}. To dokazuje výslovnou množinovou identitu v textu.
V prvním řádku Fig.5 jsou výjimky12−2,12−3,12−6,12−9,12−10,
tedy10,9,6,3,2. První chybějící buňky příslušných nižších řádků
jsou(6,3),(5,3),(4,5),(3,7),(2,7), souhlasně s tečkami v obrázku.

Součin délek v řádku i je tedy L_i!/∏_(k>i)(L_i−L_k). Součin
přes všechny řádky je ∏L_i!/Δ(L). Dosazením do již dokázaného(34)
dostaneme přesně Theorem H, n! dělené součinem háčků. Prázdný tvar
má prázdný součin1; nulové koncové řádky se před touto interpretací
odstraní podle(31). Známá chyba ve výjimce prvního řádku60 je
vyřešena použitím správného L_2=n_2+m−2 z errat.

## P0444: proč pravděpodobnostní „důkaz“ není platný

Pro rovnoměrné náhodné vyplnění je každá z h buněk daného háčku
stejně pravděpodobně jeho minimem, takže uvedená jednotlivá
pravděpodobnost1/h je správná. Splnění minima ve všech háčcích
je ekvivalentní tableau podmínce: zahrnuje všechny sousední
nerovnosti a ty naopak postačí pro celé háčky.

Události však nejsou nezávislé. Už v tvaru(2,2) označme buňky
a b / c d. A=[a je minimum{a,b,c}] má pravděpodobnost1/3,
B=[b<d] má1/2. Jejich průnik požaduje a<b<d a a<c. a musí být
nejmenší ze čtyř; mezi zbylými třemi musí b předcházet d, tedy
jsou právě3 přípustná pořadí z24. Proto Pr(A∩B)=1/8≠1/6.
Součin všech okrajových pravděpodobností sice díky Theorem H
dá správný celkový výsledek, ale nezávislost, kterou by tento
argument potřeboval, je již tímto párem vyvrácena. Správnost věty
tak není zaměněna za správnost zde výslovně odmítnutého důkazu.

## Opakované štítky na58

První odstavec58 zmiňuje možnost rozšířit korespondenci na opakované
p a nakonec i opakované q. Důkazy I/D pro různé klíče samy nestačily.
Proto je v tableaux-proof-repeated-labels.md zvlášť doplněno
porovnání vkládacích cest, standardizace a oba směry semistandardní
bijekce pro lexikograficky seřazené multisety dvojic. Tento skutečný
argument uzavírá matematickou část zmínky; historické citace nikoli.

Žádný výpočtový běh ani nový nález. Následuje spojení s ballot cestami,
binárními stromy a dvojicemi dvouřádkových tableaux na60–61.
