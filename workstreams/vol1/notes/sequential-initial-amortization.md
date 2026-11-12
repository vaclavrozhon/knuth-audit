# Kandidát V1-C0035: počáteční interval v §2.2.2-18

Tištěné zadání na254 udává O(m+n sum alpha_k/(1−alpha_k)), kde alpha_k=0
před prvním přebalením, a předpokládá M=L∞−L0≥n². Odpověď544 prokazuje
odhad pro interval následující po přebalení; každému zásobníku pak přidělila
alespoň floor(S/(10n)) volných buněk.

Při inicializaci(11), BASE[j]=TOP[j]=L0, je ale celá kapacita u zásobníku n.
Zvolme n≥2, M=n², OLDTOP=TOP a jedinou operaci I1, tedy m=1. Tato operace
okamžitě přeteče a G2 musí projít všech n zásobníků; G5 a R také procházejí
lineárně mnoho indexů. Cena je Ω(n), ale alpha_1=0 a tištěný odhad jeO(1).
Nejde o čas vytvoření tabulek: jde o smyčky uvnitř první už počítané operace.

Kandidát zůstává otevřený kvůli významu věty na248, že počáteční tabulky
jsou nastaveny „as before“. Předchází jak(11), tak volitelná rovnoměrná
inicializace(13). Pokud má G implicitně začínat výhradně podle(13), tento
protipříklad se neuplatní: první přeplnění vyžaduje nejméněfloor(M/n)+1
vkladů a počátečníO(n) cena se do nich amortizuje. Tato výhradnost ale není
výslovná. Možná oprava je přidat předpoklad rovnoměrného počátečního
přídělu nebo členO(n) do obecné celkové meze.

Originály248/249/254/544 byly zobrazeny; kontrola všech čtyř řad errat
nenalezla opravu této počáteční otázky. Nezávislá revize podagentem je
v `parallel/linked-allocation/notes/review-sequential-overflow.md`, oddíl
kúloze18. Potvrzen je pouze výše uvedený rozpor při výkladu dovolujícím11,
nikoli že autor tento výklad zamýšlel. Nález proto není mezi confirmed.
