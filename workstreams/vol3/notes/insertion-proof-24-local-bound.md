# Úloha24: obecný lokální odhad a uzavření ostrosti

7. listopadu 2026. Doplňuje právě P0804 z
`notes/insertion-proof-p-and-24-construction.md`; jeho konstrukce,
přípustnost, příklad i obousměrný vzorec inversí se přebírají.
Neprovádíme nový výpočet. Původní Prattův zdroj se krátkým
dohledáním nepodařilo získat; níže je vlastní úplný důkaz,
který na tomto zdroji nezávisí. Pokus a přesný neověřený širší
odkaz jsou v `sources/insertion-pratt-source-attempt.json`.

Piš Q=2^h, A=Q−1=2a+1, a=Q/2−1, h≥2. Funkce b(v)
je počet jedniček v binárním zápisu v; d(v)=v−b(v).
G je semigroup generovaný Q2^j−1, j≥0.

## P0805: přesný test členství a pořadí minimálních zástupců

Pro n≥0 napiš n=Av+r,0≤r<A. V intervalovém důkazu P0792
mají všechny možné intervaly index≤v a jejich pravé konce
rostou. Proto

    n∈G ⇔ n≤Qv−b(v) ⇔ r≤d(v).                  (1)

Pro nenulový zbytek r je tedy minimální reprezentant

    w_r=A v_r+r,  v_r=min{v≥0:d(v)≥r}.

Monotonicita d znamená, že v_r neklesá s r; w_r proto přísně
roste s r. Pro r≥1 platí r+1≤v_r≤Q: první nerovnost plyne
z b(v)≥1 pro v>0, druhá z d(Q)=Q−1=A. Nejmenší kladný
zástupce nulového zbytku je A a je menší než všechny w_r,r≥1.

Zástupce w_k v sestupném pořadí W⁺ z P0804 má proto přesně
zbytek r=A−1−k=2a−k, pokud k<A−1. Pro k, na nichž záleží
kladná knižní mez, totiž0≤k≤(a−1)/2, je r≥1 a můžeme psát

    w_k=Av+r,  2a−k+1≤v≤2a+2.                   (2)

Tím je vazba mezi pořadím nově přidělovaných položek a zbytky
dokázána; není to domněnka podle tabulky s=4.

## P0806: pomocná inverze jedné monotónní funkce

Polož e(x)=2x−b(x) pro x≥1. Při přičtení1 má e přírůstek
1+t≥1, kde t je počet koncových jedniček, takže e přísně roste.
Pro z≥1 definuj L(z)=min{x≥1:e(x)≥z}. Existuje, protože e(x)≥x.

Potřebujeme pouze obecnou horní mez

    L(z)≤⌈2z/3⌉.                               (3)

Pro z=1,2,3,4 ji dokazují e(1)=1,e(2)=3,e(3)=4.
Pro x≥4 máme b(x)≤⌊x/2⌋: při x=2u je b(x)=b(u)≤u,
při x=2u+1,u≥2 je b(x)=b(u)+1≤u, protože b(u)≤u−1.
Tedy e(x)≥3x/2. Při z≥5 je x=⌈2z/3⌉≥4 a e(x)≥z,
což dokazuje(3) ve všech případech bez asymptotického odhadu bitů.

## P0807: tři disjunktní rodiny skutečných inversí

Podle P0804 přesně

    c(w_k)=#{ℓ≥1:w_k−A−ℓa ∈ G\{0}}.

Pro k v kladném rozsahu z(2) polož

    B=v−k−1,  C=B−a,  D=B+a.

Máme C≥a−2k≥1 a B≤2a+1. Zkonstruujeme tři rodiny různých
ℓ; jejich počet bude dolní mezí c(w_k), není třeba tvrdit,
že vyčerpávají i případné zbývající krajní hodnoty.

1. Pro každé1≤x≤B vezmi ℓ=2(v−x). Pak

       w_k−A−ℓa=Ax+(B−x).

   Posun je kladný, protože v−x≥k+1≥1. Zbytek B−x leží
   v0,…,A−1 a číslo je kladné. Test(1) říká, že patří do G
   právě když e(x)≥B. Tato rodina dává B−L(B)+1 inversí.

2. Pro C≤x≤v−1 vezmi ℓ=2(v−1−x)+1. Potom

       w_k−A−ℓa=Ax+(D−x).

   Zbytek je mezi a−k a2a=A−1, tedy platný. Opět jde o
   kladné číslo a test je e(x)≥D. Přitom L(D)>C, protože
   e(C)≤2C−1=2B−2a−1<D (už B≤2a+1≤3a).
   Dále L(D)≤v, protože d(v)≥2a−k a
   e(v)=v+d(v)>v+a−k−1=D. Rodina má přesně v−L(D) členů,
   včetně možnosti nula. Její liché posuny odpovídají
   0≤(ℓ−1)/2≤a+k.

3. Pro1≤x≤C vezmi ℓ=2(v−x)+1. Zde

       w_k−A−ℓa=Ax+(C−x).

   Opět jde o kladné číslo s platným zbytkem. Členství je
   e(x)≥C, takže dostáváme C−L(C)+1 členů. Jejich liché
   posuny mají (ℓ−1)/2≥a+k+1.

První rodina je sudá; obě liché mají disjunktní rozsahy.
Uvnitř každé rodiny různé x dávají různé posuny, tedy různé
skutečné inverse. Všechny koncové pozice existují podle už
ověřené kladné podmínky P0804. Žádný počet ze stejného kroku
přidělování ani z jiné třídy modulo a se sem nepřimíchává.

## P0808: součet a knižní lokální nerovnost

Předchozí konstrukce dává

    c(w_k)≥B−L(B)+1+v−L(D)+C−L(C)+1
           =2B+v−a+2−L(B)−L(B+a)−L(B−a).

Použij(3). Součet argumentů B,B+a,B−a je3B; jejich
dvojnásobky dělené3 mají celočíselný součet2B. Součet tří
zaokrouhlení nahoru proto nepřesahuje2B+2: součet jejich chyb
je celé nezáporné číslo menší než3. Vyjde dokonce

    c(w_k)≥v−a≥a−k+1≥a+1−2k=Q/2−2k.

Tím je obecně dokázána právě chybějící nerovnost P0804.
Pro zbývající k je pravá strana nekladná a tvrzení plyne
z c(w_k)≥0. Zahrnut je i h=2, kdy a=1 a kladný rozsah
obsahuje jen k=0; všechny pomocné rozsahy a odhad(3) stále platí.

## P0809: nepodmíněná ostrost a všechny velikosti vstupu

Teď už se podmíněná algebra z předchozí poznámky stává důkazem.
Pro N=2QA existuje Q vnitřních kroků, v každém je součet
kladných mezí přes k=0,…,Q/4−1 roven

    (Q/4)(Q/4+1)>Q²/16.

Každá počítaná inverse má jedinečný levý větší prvek, takže
se mezi kroky ani položkami nepočítá dvakrát. Všechny leží
v třídách přírůstku a a předchozí větší průchody vstup nemění.
Počet přesunů tohoto jediného a-průchodu je proto

    B>Q³/16=2^(3h−4)>N^(3/2)/64.

Poslední nerovnost používá N<2Q² a2√2<4. Jediný průchod
již dokazuje, že exponent horní meze P nemůže být menší než3/2.

Lze získat i uniformní Ω(N^(3/2)) pro všechna velká N.
Rodinné velikosti N_h=2·2^h(2^h−1) mají pro h≥2 poměr
N_(h+1)/N_h=4+2/(2^h−1)<5. Vezmi největší N_h≤N a doplň
konstruovaný prefix N−N_h vzestupnými největšími hodnotami.
Ty nikdy nevytvoří inversi s prefixem; případné přidané větší
přírůstky≥N_h také nic nezmění. Ve všech menších průchodech
se operace na prefixu chovají stejně jako dříve a připojené
hodnoty zůstanou vpravo. Původní dolní cena se zachová a
N_h>N/5. S úplnou horní větou P tak jde o Θ(N^(3/2)).

## P0810 — partial: širší historická generalizace

Celá úloha24 a všechny konkrétní kroky její konstrukce jsou nyní
uzavřené. První věta623 navíc tvrdí Prattovo rozšíření na širší
rodinu včetně posloupnosti(12). Původní práci se nepodařilo
získat a obecné hypotézy tohoto širšího výsledku zde dosud nejsou
doloženy. Tato samostatná položka zůstává partial; není potřebná
pro právě dokončenou dolní mez Mersenneových přírůstků a nesmí
ji zpětně zneplatnit ani být zaměněna za její hotový důkaz.

Další souvislý kurzor je Prattova posloupnost2^p3^q na91,
úlohy30/31 a poté následující konstrukce Incerpi/Sedgewick.
