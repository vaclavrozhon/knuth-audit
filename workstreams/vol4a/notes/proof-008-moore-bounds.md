# Mooreovy meze: str.15 a §7–63 až66

6. listopadu 2026. Tento blok byl doplněn dopředu, protože na něj přímo
odkazuje str.15. Zadání40/file57, odpovědi522–523/file539–540, původní sazba
přečtena. Žádná enumerace ani matematický program. Pět4A/F0 vrstev errat
v relevantním rozsahu bez změny těchto argumentů.

## 63: obecná mez počtu vrcholů

Pro g=2t+1 vezmi kořen v. Vrstvy vzdáleností1..t mají alespoň
d,d(d−1),…,d(d−1)^(t−1) různých vrcholů: každá kolize rodičů nebo návrat
do dřívější vrstvy by vytvořil kružnici délky nejvýše2t<g. Sčítáním
dostáváme1+dΣ[k=0..t−1](d−1)^k, přesně první případ knihy.

Pro g=2t+2 vezmi hranu uv a rozvíjej strom do hloubky t z obou konců,
bez opětovného použití uv. Větvení je alespoň d−1 a obě strany jsou
disjunktní; kolize by vytvořila kružnici délky≤2t+1. Počet je alespoň
2Σ[k=0..t](d−1)^k. Algebraicky je to stejná hodnota jako vytištěné
1+(d−1)^t+dΣ[k=0..t−1](d−1)^k. Pro g5 zvlášť dostáváme d²+1.

## 64: rovnost při g4

Na2d vrcholech musí mít každý vrchol přesně d sousedů: pro hranu uv
jsou při zákazu trojúhelníků množiny N(u) a N(v) disjunktní, tedy
2d≥deg(u)+deg(v). Větší stupeň by překročil mez. Pro pevný v
je d jeho sousedů nezávislá množina (jinak trojúhelník). Každý z nich
musí sousedit se všemi zbývajícími d−1 vrcholy. Tyto vrcholy spolu s v
tvoří druhou část; uvnitř ní by hrana vytvořila trojúhelník přes společného
souseda. Výsledkem je přesně K_d,d. Pro d≥2 má skutečně girth4.

## 65(a,b): matice a vlastní čísla při g5

Při N=d²+1 dává BFS od libovolného v nejméně1+d·deg(v) vrcholů, proto
deg(v)=d všude. Celá množina je ve vzdálenosti≤2 od libovolného kořene.
Sousední vrcholy nemají společného souseda, nesousední mají přesně jednoho:
existence plyne z naplněné BFS koule, jednoznačnost ze zákazu4-cyklu.
Proto A²+A=(d−1)I+J, včetně diagonály d.

Jednotkový vektor všech1 je vlastní s číslem d. Graf je souvislý; pokud
Ax=dx, největší souřadnice reálného x vynutí stejnou hodnotu na všech
sousedech a pak všude. Vlastní prostor pro d je tedy jednorozměrný.
Použijeme standardní spektrální větu pro reálné symetrické matice jako
explicitní lineárně-algebraický vstup. Zbytek ortogonální báze má Jx=0,
takže λ²+λ=d−1 a λ=(-1±sqrt(4d−3))/2.

## 65(c,d): povolené stupně

Označ multiplicity obou kořenů m+,m−; jejich součet je d². Ze stopy0:
0=d−d²/2+(m+−m−)sqrt(4d−3)/2.
Je-li odmocnina iracionální, musí m+=m− a d−d²/2=0. Pro graf obvodu5
zbývá d2 (případ d0 nemá obvod5).

Je-li s=sqrt(4d−3) racionální, je celočíselné a liché. Máme
d=(s²+3)/4 a s(m+−m−)=d(d−2), takže s dělí d(d−2). Přitom
16d(d−2)=(s²+3)(s²−5)≡−15 mod s. Proto s|15:
s=1,3,5,15, tedy d=1,3,7,57. Stupeň1 na N2 nemá obvod5, zbývá3,7,57.
To ověřuje závěr i zkrácenou algebraickou úvahu odpovědi65(d).
Případy d2 a3 realizují C5 a Petersen (doloženo v proof-007).
Existence d57 se zde netvrdí ani nehledá; související výzkumná úloha67 čeká.

## 66: knižní konstrukce stupně7

Zapiš U_(i,j)=[j,i] a V_(k,l)=(l,k), indexy v F5. Knižní hrany jsou
U_(i,j)–U_(i,j±1), V_(k,l)–V_(k,l±2) a U_(i,j)–V_(k,j−ki).
Máme50 vrcholů, každý dva sousedy stejného typu a pět opačného, tedy stupeň7.

Bez3-cyklů: cykly uvnitř stejného typu jsou pentagony. Dva sousední U
mají stejné i a různá j, proto nemají společného V; analogicky pro V.
Smíšený trojúhelník tudíž neexistuje.

Bez4-cyklů jsou všechny možnosti:
- Čtyři vrcholy téhož typu leží v pentagonu, kde4-cyklus není.
- Při poměru3:1 jsou dva konce dvoukrokové cesty ve stejném pentagonu
  různé, a nemají společného souseda opačného typu.
- Při střídání U,V,U,V mají dvě U nanejvýš jednoho společného V:
  pro různá i rovnice j−ki=j′−ki′ určuje právě jedno k, pro stejné i
  a různá j žádné.
- Při typu U,U,V,V vyžaduje U-hrana rozdíl j o±1 a V-hrana rozdíl l o±2,
  ale při stejných i,k platí l=j−ki, takže oba rozdíly musí být stejné.
  V F5 se množiny {±1} a{±2} neprotínají.

Girth je tedy alespoň5 a přítomné pentagony dávají rovnost. Počet50=7²+1
ověřuje i existenční tvrzení hlavního textu. Nezávislost tohoto důkazu je
symbolická; žádné malé ani velké grafy se neenumerovaly.

Po odstranění prvních dvou typů hran zůstávají body(i,j) a přímky
j=l+ki pro pět sklonů k. Jde o síť pěti rovnoběžných tříd získanou
z OA úlohy19 vynecháním třídy i=konst.; incidence má podle51 girth6.
Tím je vysvětlen i dovětek odpovědi, včetně počtu50 místo55 pro úplnou
šestitřídní afinní rovinu. Citace Brown a jedinečnost stupně7 podle
Hoffman–Singleton jsou externí bibliografické vstupy, nikoli zde znovu
dokázaná klasifikace.
