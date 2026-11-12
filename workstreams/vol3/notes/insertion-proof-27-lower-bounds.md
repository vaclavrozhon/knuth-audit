# §5.2.1-27 — dolní meze a přesný rozsah vnějších vět

Stav 2026-11-07. Zadání104/file115 a odpověď623/file634 znovu zobrazeny.
Základní27(a),(b) jsou doloženy níže, s výslovnou hlubokou vnější závislostí
na Poonenově lemmatu17. Poznámka o **libovolném c<1/2** zůstává partial
v uniformním režimu rostoucího m; není označena jako chyba výsledku.
Žádný matematický výpočet/program se nespouštěl. Starý K a náklady D se přebírají.

## Model a elementární redukce — P0855–P0856

Předpoklad je pevná posloupnost přírůstků zvolená před čtením klíčů; může
záviset na N. Jde o porovnávací třídění všech permutací. V každém průchodu
D proběhne h-vkládání. Zasunutí prvku lze rozložit na přesně stejné výměny
s jeho předchůdci ve vzdálenosti h. Jeden přesun odpovídá jedné takové
výměně; počet porovnání a čas D tuto práci zespodu omezují konstantou.
Na již h-uspořádaném souboru stále proběhne N−h prvních porovnání.
Proto každý z m průchodů s h<N/2 stojí >N/2 porovnání, nezávisle na datech.
Pro N>2 je m≥1, protože poslední přírůstek je1.

K z P0774–P0777 říká, že h-třídění zachová každé předchozí k-uspořádání.
Je-li vstup uspořádaný pro všechny skutečné přírůstky h≥β, tyto průchody
nevymění nic, i kdyby byly vloženy mezi menší průchody. Toto používá
uspořádání celého průchodu, nikoli nesprávné tvrzení o každé jednotlivé výměně.

Výměna inverzní dvojice ve vzdálenosti h odstraní nejvýše2h−1 inversí.
Pár koncových prvků přispívá1, každý z h−1 vnitřních prvků nejvýše2;
pro prvek vně intervalu se součet jeho vztahů k oběma koncům nezmění.
Pro různé klíče přesně mizí1+2r, kde r vnitřních hodnot leží mezi koncovými.
Proto vstup s I inversemi, na němž mění data jen přírůstky h<β,
vyžaduje alespoň I/(2β) výměn. To je dolní mez, nikoli tvrzení, že
každá výměna odstraní právě2h inversí.

Samostatná informační větev počítá **porovnání**, nikoli úspěšné výměny:
binární rozhodovací strom musí mít N! listů, tedy výšku≥log₂(N!).
Už posledních floor(N/2) faktorů dává log₂(N!)≥floor(N/2)log₂(N/2),
což pro dost velké N převyšuje N sqrt(ln N).

## Převzaté lemma, padding a různé klíče — P0857

Vnější závislost: Bjorn Poonen, autorský rukopis *The worst case in Shellsort
and related algorithms*, datum1992-10-11, vydán J. Algorithms15(1993),101–124.
Lokální `sources/poonen-1993-shellsort.pdf`, lemma17 na13:
pro celá r≥1,2≤a₁≤…≤aᵣ, a₁≥r^(9r) a2≤ℓ≤a₁^(1+1/r)/2 existuje
0–1 seznam délkyℓ, který je aᵢ-uspořádaný pro všechna i a má alespoň
2^(−16)ℓ²/r² inversí. Geometrický/Frobeniův důkaz lemmat6–16 se zde
**neprohlašuje za nově nezávisle ověřený**. Toto je pojmenovaná převzatá
věta se všemi podmínkami; nejde o pouhý odkaz na požadovaný výsledek27.

Následující rozšíření (lemma18) odvozujeme: vezměme takový seznam X a
pro0≤j<N definujme Y[j]=10 floor(j/ℓ)+X[j mod ℓ]. Uvnitř jednoho bloku
platí potřebná aᵢ-uspořádání podle X; při přechodu do pozdějšího bloku
naroste základ nejméně o10, kdežto X∈{0,1}. Totéž dokazuje všechna
h-uspořádání s h≥ℓ. V úplných blocích je alespoň
floor(N/ℓ)·2^(−16)ℓ²/r²≥2^(−17)Nℓ/r² inversí, protože N≥ℓ.
Neúplný poslední blok další inverse nepotřebuje.

Nahraďme Y jeho stabilními hodnostmi: seřaďme dvojice (Y[j],j) a dejme
jim hodnosti1,…,N. Přísné inverse zůstanou a žádná nová nevznikne;
je-li Y[j]≤Y[j+h], pořadí dvojic je díky j<j+h přísně rostoucí.
Tak získáme skutečnou permutaci různých klíčů se všemi požadovanými
uspořádáními. Binární pomocný seznam tedy nemění doménu úlohy.

## Uniformní volba řídkého intervalu — P0858

Položme c=1/432, L=ln N. Když N^(c/sqrt(m))<sqrt(L), informační větev
již dává požadovanou mez. Jinak

    N^(c/sqrt(m))≥sqrt(L),  m≤(2cL/ln L)²≤(L/ln L)².                 (A)

Pro k=0,…,ceil(18sqrt(m)) položme βₖ=N^(1/2+k/(72sqrt(m))). Protože
m≥1 a k≤18sqrt(m)+1≤24sqrt(m), βₖ≤N^(5/6)≤N/2 pro všechna dost
velká N, s prahem nezávislým na m. Máme nejméně18sqrt(m) disjunktních
polouzavřených intervalů [βᵢ,βᵢ₊₁), které obsahují dohromady nejvýše m
přírůstků. Některý obsahuje r≤sqrt(m)/18 přírůstků a₁,…,aᵣ.
Dále r≤L/(18ln L) a r≤L. Případ r=0 je vyřešen zvlášť níže;
nesmí se dosadit do1/r.

Je-li r≥1, a₁≥βᵢ≥sqrt(N), takže
ln a₁≥L/2≥9r ln r, tedy a₁≥r^(9r). Volíme ℓ=ceil(βᵢ₊₁).
Pak2≤ℓ≤N a pro dost velké N

    ℓ ≤2βᵢ₊₁
      ≤(1/2)sqrt(L) N^(1/(72sqrt(m))) βᵢ
      ≤(1/2)N^((c+1/72)/sqrt(m)) βᵢ
      ≤(1/2)N^(9/sqrt(m)) βᵢ
      ≤(1/2)a₁^(1+18/sqrt(m))
      ≤(1/2)a₁^(1+1/r).

První oslabení používá sqrt(L)≥4, další(A), pak c+1/72≤9,
a₁≥sqrt(N), βᵢ≤a₁ a1/r≥18/sqrt(m). Všechny podmínky lemmatu jsou
splněny uniformně, nikoli jen pro pevné m.

## Celá27(a), včetně prázdného intervalu — P0859–P0860

Pro r≥1 má permutace z P0857 alespoň2^(−17)Nℓ/r² inversí a je
uspořádána pro všechny skutečné přírůstky≥βᵢ: ty uvnitř intervalu jsou
aᵢ a každý celočíselný přírůstek≥βᵢ₊₁ je≥ceil(βᵢ₊₁)=ℓ.
Podle P0856 a r≤L tedy počet výměn je alespoň

    Nβᵢ₊₁/(2^18 βᵢ L²)
     = N^(1+c/sqrt(m)) · N^(5c/sqrt(m))/(2^18 L²)
     ≥ N^(1+c/sqrt(m)) · sqrt(L)/2^18
     ≥ N^(1+c/sqrt(m)).

Zde1/72=6c a(A) poskytuje N^(5c/sqrt(m))≥L^(5/2).

Pro **r=0** je důkaz jednodušší a nepoužívá lemma: rozdělme1,…,N do
po sobě jdoucích bloků délkyℓ=ceil(βᵢ₊₁), poslední může být kratší,
a každý blok obraťme. Každý pozdější blok má všechny hodnoty větší;
proto je permutace h-uspořádaná pro h≥ℓ. Prázdnota intervalu znamená,
že to jsou všechny skutečné přírůstky h≥βᵢ. Úplné bloky dávají alespoň
floor(N/ℓ)ℓ(ℓ−1)/2≥Nℓ/8 inversí. Potřebný počet výměn je alespoň

    Nℓ/(16βᵢ) ≥ N^(1+c/sqrt(m))·N^(5c/sqrt(m))/16,

opět dost velký podle(A). Tento případ zahrnuje i malé m, kde r≥1
vůbec nemusí nastat. Nejde o chybu knihy: její odpověď na úplný vnější
důkaz pouze odkazuje. Hotový argument má uniformní kladnou konstantu
a práh N; konečně mnoho menších N není asymptotickým protipříkladem.

## Celá27(b) — P0861

Je-li m>(c²/4)(L/ln L)², samotná režie m průchodů stojí
>mN/2=Ω(N(L/ln L)²). Jinak sqrt(m)≤cL/(2ln L), a tudíž
N^(c/sqrt(m))≥exp(2ln L)=L². Část(a) pak dává Ω(NL²), což je silnější.
Právě zde musí platit uniformita(a) pro rostoucí m. Místo celkového
počtu průchodů se správně používá pouze počet h<N/2, jinak by režijní
krok nemusel platit pro přírůstky těsně pod N.

## Plaxton–Suel: doložený režim a ponechaná mezera — P0862 partial

Oba primární autorské soubory, NYU `shell2.pdf` a UT `pubs/1997/j_algorithms.ps`,
obsahují na12 větu4.1 ve tvaru

    T(N,M)=Ω(N^(1+d/sqrt(M))/(lg N)^5),  d=1/(2+ε), ε>0,

kde M je **celkový** počet přírůstků. Sazba UT kopie byla zobrazena;
nejde o OCR záměnu. Diskuse na16 tento dělitel výslovně zachovává.
Autorské kopie nejsou vydavatelský tisk; přístup k němu nebyl získán.

Převod na počet m malých přírůstků je legitimní: vložme obtížnou
permutaci délky n=floor(N/2) na začátek pole a za ni rostoucí největší
hodnoty. V každé kongruenční třídě je příslušný prefix menší než celý
suffix, takže se přes hranici nic nevymění a podproblém se třídí přesně
svými přírůstky h<n. Všechny ostatní průchody data nemění. Efektivních
přírůstků M≤m a n≥N/3; faktor3^(1+d/sqrt(M)) je omezený konstantou.
Tím dostaneme stejnou dolní mez s N,m a logaritmickým dělitelem.

Pro každé pevné0<c<1/2 vyberme c<d<1/2. Pokud

    m=o((ln N/ln ln N)²),

pak (d−c)ln N/sqrt(m)−5ln ln N→+∞. Dělitel se pohltí a vyjde
Ω(N^(1+c/sqrt(m))). To zahrnuje každé pevné m i běžné m=O(log N).

**Neuzavřeno:** stejný závěr uniformně pro všechna m(N). Samotná citovaná
věta jej bez dalšího argumentu nedává. Například při
m≈(ln N/(6ln ln N))² a c=.49 je cílem N(ln N)^2.94, kdežto uvedená
věta s libovolným d<.5 dává mocninu logaritmu6d−5<−2 a režie dává
jen řád N(ln N)²/(ln ln N)². Toto je mezera v odvození z dostupných
vět, **nikoli protipříklad k tvrzení knihy**. Výrok může mít zamýšlený
omezený režim nebo silnější důkaz; bez něj se neuzavírá. Základní(a),(b)
s c=1/432 na tomto dodatku nezávisí. Nová karta chyby nevzniká.

## Síťový a historický dovětek — P0863

Cypherova věta se přebírá jako další pojmenovaný vnější výsledek:
monotónně klesající přírůstky a pevná Shellsortová síť vyžadují
Ω(N(log N)²/loglog N) **komparátorů**. Primární vydavatelský abstrakt
potvrzuje síťový a monotónní rozsah; Poonenův úvod na2 výslovně uvádí
správně seskupenou mez a odlišuje ji od adaptivních porovnání. Úplný
Cypherův důkaz nebyl získán ani nově auditován. Odkaz5.3.4-2 skutečně
znamená síť: zadání235/file246, odpověď666/file677 převádí každý
Prattův h-průchod na1 nebo2 pevné hladiny komparátorů. Z toho nelze
bez dalšího vyvodit silnější dolní mez na skutečně provedená adaptivní
porovnání D; kniha takový závěr netvrdí.

Poslední věta o neznámé obecné průměrné mezi je historická k vydání1998,
nikoli tvrzení o stavu2026. Dobový Plaxtonův–Suelův závěr na16 popisuje
právě tuto otevřenou otázku. Úplné negativní bibliografické tvrzení
„nikdo před1998 neměl výsledek“ se výslovně nepřezkoumává; pozdější
pokrok by nebyl chybou původního tvrzení. Zde není další matematická
úloha ani důvod spouštět cens literatury.

## Errata a výstup

Pět vrstev je zohledněno v `sources/insertion-lower-bound-sources.json`.
První vydání obsahuje na602 náhradní odpověď27 z1995, která už tvrdí
c<1/2; druhé vydání přidává správné omezení Cypherova tvrzení na sítě.
V ostatních vrstvách není změna27. P0862 zůstává matematická partial,
nepublikuje se jako nový nález. Pokračování:42 na105/627 a její
konstanty25/P0785; potom list insertion95–96.
