# F152: počet memů v odpovědi260 má opačné znaménko konstanty

3. listopadu 2026; §7.2.2.1–260, odpověď str.481, draft str.185.
Pro kruhové přesazování z úlohy201 je počet uložených signatur
**6n−9**, nikoli vytištěných **6n+9**, při přirozeném pořadí
X1,Y1,…,Xn,Yn a MRV s prvním minimem. Platí pro n≥3, včetně
předem uložené nulové signatury. Rozdíl18 nemůže vysvětlit konvence
o jednom terminálním stavu.

Například n4 dává15 memů,23 uzlů ZDD a78 updatů. Tisk udává33 memů.
Nový nezávislý množinový model a nezměněný autorův DLX6 souhlasí pro
n3,…,24. Všechny tyto běhy jsou krátké; celý nový blok35 případů trval
2,867s s nice15. Starý výčet Algorithm X pro201 se neopakoval.

## Obecný důkaz počtu stavů

Stav tvoří dvojice zbývajících množin X,Y. `[a,b]` znamená celý
celočíselný interval. Po kořeni jsou přesně následující rodiny:

- Dva stavy B: X=[2,n], Y={1}∪[3,n], resp. Y=[1,n−1].
- P(a,b): X=Y=[a,b], pro b∈{n,n−1} a2≤a≤b.
- Q(a,b): X=[a+1,b], Y={a}∪[a+2,b], pro stejná b a2≤a<b.
- A+(a): X=[a,n−1], Y=[a+1,n]; A−(a) má obě množiny obráceně,
  pro2≤a<n.
- Prázdný terminál.

Kořen zvolí X1. Jeho diagonální větev vede do P(2,n), ostatní do B.
V B se zvolí Y1; větve vedou do P(3,n), P(2,n−1) nebo do A+(2),A−(2).
P(a,b) volí Xa; diagonála vede do P(a+1,b), sousední volba do Q(a,b).
Q vynutí dvojici Ya,X(a+1) a přejde do P(a+2,b).
A postupně posouvá a o1. Jednoprvkové konce přejdou do terminálu.
To dokazuje uzavřenost i dosažitelnost všech uvedených stavů.

Jediný dvojí popis je `Q(n−1,n)=A−(n−1)`. Sečtením tedy dostaneme

    1+2+(2n−3)+(2n−5)+(2n−4)−1+1 = 6n−9.

První1 je kořen, poslední1 prázdný stav. Ve všech neprázdných stavech
existuje řešení, takže žádná větev se při tvorbě ZDD nezahodí.
Kořen má3 větve, oba B po2; P má2 kromě jednoprvkových konců,
Q a A mají jednu. Celkem8n−11 rozhodovacích uzlů a dva terminály:
vytištěných **8n−9 uzlů je správně**.

## Updaty a malá výjimka

Lokální cena bipartitního stavu s pivotem v je
`1+d(v)+sum_(w soused v)d(w)`. Pro P délky m jsou ceny3,7,8 pro
m1,2,≥3. Pro Q jsou3 a4; pro A jsou3,4,5 pro délky1,2,≥3.
Kořen stojí13, oba B po8 pro n≥4. Součty rodin jsou

    13+16+(16n−36)+(8n−22)+(10n−26)−3 = 34n−58.

Tento vytištěný vzorec je správně pro **n≥4**. Pro n3 stojí každý B
jen7, ale krátká rodina P nemá délku2 v obou větvích. Přímá báze
má **46 updatů**, nikoli44. Uvádíme to jako související omezení domény
téže odpovědi, nikoli jako další samostatně počítaný nález.

Obecné rodiny byly porovnány se všemi uloženými22 stopami bez opakování
vyhledávání. Doklady: [cases-checked.json](results/zdd251_260/cases-checked.json),
[source-checked.json](results/zdd251_260/source-checked.json),
[kniha](images/zdd251-260-original-501.png),
[draft](images/zdd251-260-draft-191.png). Šest vrstev errat bez nalezené
opravy. Fyzický výtisk neověřen; prvenství netvrdíme.
