# Inverze: jednotlivé argumenty úloh26–29

S.22, odpovědi596–597. Sazba obou odpovědních stran prohlédnuta;
známá oprava odpovědi27 převzata. Úloha25 je již uzavřena v
notes/inversions-proof-main.md a její argumenty se neopakovaly.
Bez výpočetního běhu, bez nového nálezu. Historické citace přeskočeny.

## 26: korelace

Označme I počet inverzí, M index a D_l indikátor sestupu na l.
Prohození sousedních pozic l,l+1 je bijekce mezi D_l=0 a D_l=1;
zvyšuje I právě o1. Všechny páry s třetím prvkem mají v součtu
nezměněný příspěvek, změní se jen vzájemný pár. Proto
E(I|D_l=1)−E(I|D_l=0)=1 a P(D_l=1)=1/2, tedy cov(I,D_l)=1/4.
Z linearity cov(I,M)=Σ_(l=1)^(n−1)l/4=n(n−1)/8.

Převzaté shodné střední hodnoty I,M jsou n(n−1)/4; dostáváme
E(IM)=n(n−1)/8+n²(n−1)²/16, skutečně polynom stupně4.
Dosazení n=1,…,5 dává0,1/2,6/2,21/2,55/2, jak uvádí odpověď.
Převzatý rozptyl n(n−1)(2n+5)/72 dává korelaci9/(2n+5), pro n≥2.
U n=0/1 je rozptyl nulový a korelace nedefinovaná; kniha tyto případy
správně vylučuje. Drobný násobitel l v sazbě očekávání je přítomen.

## 27: vazba na q a q-multinomiální faktor

MacMahonova bijekce řadí indexy stabilně podle klesajících q_i.
Pro u<v je tedy v před u v permutaci a právě když q_v>q_u.
To je právě inverze těchto dvou pozic v obráceném slově q_n…q_1.
Proto inv(a)=inv(q_n…q_1), včetně případů shodných q.

Použitý dopředný výsledek úlohy5.1.2-16 lze dokázat samostatně
bez čekání na další sekci. Nechť M(k_1,…,k_r) je inverzní GF slov
s danými násobnostmi, n=Σk_i. Připojení posledního písmene i dává
rekurenci M(k)=Σ_(i:k_i>0) w^(Σ_(j>i)k_j)M(k−e_i).
Výraz n!_w/∏k_i!_w ji splňuje, neboť po vytknutí společného
faktoru zbývá rovnost
Σ_i w^(Σ_(j>i)k_j)(1+…+w^(k_i−1))=1+…+w^(n−1).
Intervaly exponentů se rozdělují bez překryvů. Základ M(0,…,0)=1
dokazuje q-multinomiální vzorec. Tento důkaz se v úloze5.1.2-16 převezme.

Ze součtové identity MacMahona plyne, po známé opravě odstraněného
součtu přes n na levé straně prvního řádku odpovědi27,
H_n(w,z)/(z;z)_n=Σ_(q_1,…,q_n≥0) w^inv(q_n…q_1) z^(Σq_i).
Seskupení podle násobností k_j hodnot j dá q-multinomiální faktor
n!_w/∏k_j!_w a váhu z^(Σj k_j). Vytknutí n!_w a extrakce
koeficientu u^n jsou proto přesně n!_w[u^n]∏_(j≥0)exp_w(z^j u).
Produkt exp_w již doložen v16. Přeznačení u→u/(1−w) dává

F(u)=∏_(j,k≥0)(1−w^j z^k u)^−1
    =Σ_(n≥0) H_n(w,z)u^n/((w;w)_n(z;z)_n).

Všechny kroky jsou koeficientové formální identity. Produkt také
dokazuje symetrii H_n(w,z)=H_n(z,w), v souladu s hotovou úlohou25.
Jiná statistika zmíněná na597 má stejný GF: bijekce
a→(f(a^−1))^−1 z hotové úlohy25 zachová ind(a) a změní
inv(a) na ind(inverse). Nejde tedy o pouhou záměnu názvů statistik.

## 27: rekurence

Z právě dokázaného produktu
F(u)=F(zu)∏_(j≥0)(1−w^j u)^−1
    =F(zu)Σ_(k≥0)u^k/(w;w)_k.
Pro a_n=H_n/((w;w)_n(z;z)_n) dostáváme
(1−z^n)a_n=Σ_(k=1)^n z^(n−k)a_(n−k)/(w;w)_k.
Vynásobení faktoriálovými produkty dává přesně

H_n=Σ_(k=1)^n [n choose k]_w z^(n−k)
                  ∏_(j=1)^(k−1)(1−z^(n−j)) H_(n−k).

Tím je rekurence ověřena přímo, bez nedoloženého spoléhání na
odkazovanou úlohu4.7-27. H_0=1 určuje počáteční případ.

## 28: celkové posunutí

Sousední prohození mění každý ze dvou příspěvků |a_j−j| o±1,
tedy celkově o0 nebo±2. Již dokázaná cesta od identity o délce
inv(a) dává td(a)≤2inv(a).

Pro druhou mez nechť j je nejmenší nesprávně umístěná hodnota,
a_k=j, tedy k>j a pozice před j jsou pevné. Mezi j,…,k−1 existuje
hodnota alespoň k: jinak by k−j pozic obsahovalo jen k−j−1 možných
hodnot j+1,…,k−1. Zvolme její nejpravější pozici l. Potom
j≤l<k, a_l≥k a pro l<i<k platí j<a_i<k≤a_l.
Prohození a_l s a_k odstraní jejich jednu inverzi a po dvou inverzích
s každým z k−l−1 prostředních prvků. Pokles je2(k−l)−1.
Z nerovností j≤l<k≤a_l plyne přímým rozpisem absolutních hodnot,
že td současně klesne o2(k−l).

Počet inverzí ostře klesá, takže proces skončí identitou. Pro m
provedených prohození proto td(a)=inv(a)+m, a zvláště td(a)≥inv(a).
U netriviální permutace je tato nerovnost ostrá, což tvrzení knihy
nevadí. Průměr při uniformní permutaci je
(1/n)Σ_(i,j)|i−j|=(2/n)Σ_(d=1)^(n−1)d(n−d)=(n²−1)/3.
Neformální hodnocení jednoduchosti generující funkce není nový teorém.

## 29: součin a inkluze inverzí

Použije se přesná konvence knihy (ππ′)_i=π′_(π_i): levé násobení
τ_j prohodí sousední pozice j,j+1. Permutaci π lze vytvořit
inv(π) takovými prohozeními, takže stejná prohození převedou π′
na ππ′. Každé mění počet inverzí o±1, tedy
inv(ππ′)≤inv(π)+inv(π′). Při rovnosti každé přidá jeden pár
a E(ππ′) obsahuje E(π′).

Obráceně nechť E(ππ′)⊇E(π′). Pokud jsou pořadí různá, některá
sousední dvojice v π′ má v cíli opačné pořadí; kdyby žádná neměla,
tranzitivita by zachovala celé pořadí. Již sestupnou dvojici cíl
obrátit nesmí, kvůli inkluzi E. Existuje tedy sousední vzestupná
dvojice, jejíž obrácení přidá právě jeden požadovaný pár. Po něm
inkluze trvá a mezera velikostí E klesne o1. Indukce tak převádí π′
na cíl přesně inv(ππ′)−inv(π′) kroky; jejich součin musí být π.
Minimalita inv(π) a předchozí nerovnost pak vynutí rovnost.

Tištěné příklady souhlasí: τ_1τ_3τ_2 dává3142. U314592687 jsou
vzestupné sousední páry(1,4),(4,5),(5,9),(2,6),(6,8), tedy
možné přidávané inverze přesně(4,1),(5,4),(9,5),(6,2),(8,6).
Prohození τ_4 dává314952687, jak uvádí odpověď.
