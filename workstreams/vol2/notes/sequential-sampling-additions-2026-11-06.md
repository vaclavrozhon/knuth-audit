# Souvislá revize §3.4.2: doplněné úlohy 18 a 19

6. listopadu 2026, X0129. Zadání v all2-prepre na souborových stranách
8–9, odpověď 18 na 33 a odpověď 19 na 34 byly znovu vizuálně přečteny.
Tyto doplňky patří k původním stranám 148, 592 a 593; v našem prvním dotisku nejsou vysázeny.
Všechny části obou úloh jsou přezkoumané bez nového nálezu. Z celé sekce
§3.4.2 zbývá konkrétní konstanta 5n/2 v úloze 16 (X0128).

## Úloha 18: třídy grafů a pravděpodobnosti

Celé poznámky `exchange-shuffle.md`, oba verifiery v Pythonu a C++,
všechny řádky census JSONL, výsledný validační JSON a log byly přečteny.
Pozicová permutace je inverzí výsledného pole; v naší a Goldsteinově
konvenci se funkce skládají zprava doleva. Robbins–Bolker používají
opačný zápis skládání, který je při čtení důkazů nutné respektovat.

Obecné důkazy tří tříd souhlasí:

- Komponenta funkčního grafu s jednou smyčkou dává jeden permutační
  cyklus. Komponenta s kruhem délky alespoň dva dává dva cykly.
  Odstranění hrany, indukce pro strom a následné rozštěpení cyklu
  transpozicí dokazují tvrzení i pro dvojici protisměrných hran.
- Posun doprava má stromové reprezentace popsané rekurzivním sléváním
  rostoucí a klesající řady. Hvězda s největším kořenem a odstranění
  poslední transpozice dávají F_m=1+Σ_{j<m}F_j=2^(m−1).
- Identitu dávají právě smyčky a dvojice protisměrných hran: involuce.
  Q_0=Q_1=1 a Q_n=Q_{n−1}+(n−1)Q_{n−2}. Pro n≥2 indukce dává
  √n<Q_n/Q_{n−1}<√n+1, a tedy Q_n≥√(n!). Dolní indukční krok používá
  x+1/(x+1)>√(x²+1) pro x=√(n−1)>0.
- Posun doleva dávají binární vyhledávací stromy. Vlastní indukce
  se vnějším rodičem dokazuje postačitelnost konstrukce; úplnost
  vyplývá z obecného počtu C_n=C(2n,n)/(n+1). Robbins–Bolker tento
  počet odvozují z rozkladu reziduálních cyklů a Catalanovy rekurence.

Práh n≥18 pro maximum se neopírá jen o porovnání tří uvedených výsledků.
Pro minimum byl znovu přečten úplný zdvojovací důkaz Robbins–Bolker:
odstranění jednoho ze dvou vrcholů sestupu vytvoří dvě disjunktní rodiny
reprezentací. Identitu pokrývá Q_n≥2^(n−1), přímo z její rekurence.
Pro maximum Goldstein–Moews redukují libovolnou permutaci na její
cyklový typ a klesající cykly na oddělených intervalech. Celková násobnost
je součet přes rozdělení cyklů na jednotlivce a dvojice; samotné G_mp
počítá jednu unicyklickou komponentu. Pro dva cykly je proto celkový
počet C_m C_p+G_mp, což je ve verifieru zahrnuto.

Původní přesný soupis 17 650 828 historií pro n≤8 ani nezávislé
dynamické rozdělení nebyly znovu spuštěny. Také 18 459 rozkladů
n≤28 se neopakovalo. Znovu byla přečtena všechna jejich uložená maxima
a vítězné cyklové typy: pro 4≤n≤17 dvě téměř stejně dlouhé klesající
cykly, pro 18≤n≤28 identita. Pro n≥29 platí obecný odhad
N(π)≤Q_q 4^(n−q), kde q je počet cyklů. Konečný počáteční úsek
nerovností je archivovaný; další růst plyne z poměrů Q_n a Catalanovy
řady. Výpočet není vydáván za samostatný důkaz strukturálních lemmat.

### Konkrétní obrázek odpovědi

Nově byl přepsán celý nakreslený strom s 26 vrcholy a kořenem 15.
Jeho slévaná posloupnost je

    1,2,26,25,3,24,23,4,22,21,20,19,5,6,7,8,9,10,18,11,12,17,13,16,14,15.

Každý vrchol míří na první pozdější vrchol z opačné řady, nebo na kořen.
Přímé provedení 26 vytištěných výměn dává (26,1,2,…,25), jak má.
Rodiče všech vrcholů, posloupnost i výsledek jsou v `exchange-appendix.json`.
Jde o kontrolu jednoho konkrétního obrázku, nikoli další velký soupis.

### Doplnění obecného důkazu uzavřeného vzorce pro G_mp

Goldstein–Moews v lemmatu 14 uvádějí

    G_mp = [C(2m,m) C(2p,p)(m+p+4mp)
            −(m+p)C(2m+2p,m+p)] / [2(m+p)(m+p+1)],

ale algebraické odvození ponechávají čtenáři. Zde je doplněno; tato
identita již nemusí zůstat pouze převzatým vzorcem testovaným do n=8.

Nechť C(z)=Σ C_j z^j, tedy C=1+zC². Pro klesající cyklus délky m
označme H_{m,k} a J_{m,k} autorovy počty N̄_k a N̄'_k z oddílu 6.
Jejich bijektivní rozklady (20) a (21) dávají pro pevné k≥1

    J_k(z) = k C(z)(C(z)−1)^(k−1) zC(z) = k(C(z)−1)^k,
    H_k(z)−J_k(z) = H_k(z) zC(z).

Ve druhém vztahu je poslední podstrom zakořeněn v nejmenším prvku,
proto jeho počet na v vrcholech je C_{v−1}, nikoli C_v.
Protože 1−zC=1/C, dostáváme

    H_k(z)=k C(z)(C(z)−1)^k = k z^k C(z)^(2k+1).

Lagrangeova inverze pro C=1+zC² (nebo Catalanova konvoluce) dává

    H_{m,k}=k [C(2m,m−k)−C(2m,m−k−1)] = k Δ_{m,k},

kde binomický koeficient s dolním indexem mimo 0,…,2m je nula.
Důsledek 9 článku proto převádí hledanou násobnost na

    G_mp = Σ_{k≥1} H_{m,k} H_{p,k}/k
         = Σ_{k≥1} k Δ_{m,k} Δ_{p,k}.                        (G)

Položme s=m+p, t=mp a A_k=C(2m,m−k) C(2p,p−k). Pro
1≤k≤min(m,p) platí

    A_{k+1}/A_k = (m−k)(p−k)/[(m+k+1)(p+k+1)],
    Δ_{m,k}Δ_{p,k}/A_k = (2k+1)²/[(m+k+1)(p+k+1)].

Definujme

    R(k)=[2(s+1)k²−sk+s+2t]/[s(s+1)].

Po vynásobení společným jmenovatelem a porovnání koeficientů vznikne
přesná teleskopická identita

    R(k)A_k−R(k+1)A_{k+1}
      = k Δ_{m,k}Δ_{p,k}+A_k/(s+1).

Na horním konci A_{min(m,p)+1}=0; na dolním
R(1)A_1=2t A_0/[s(s+1)]. Vandermondova identita a symetrie dávají

    A_0+2Σ_{k≥1}A_k=C(2s,s).

Sečtením teleskopické identity tedy

    G_mp = 2t A_0/[s(s+1)] − [C(2s,s)−A_0]/[2(s+1)],

což je přesně uvedený vzorec. Tento obecný důkaz používá rozklady
primárního článku, jejichž bijekce byly přečteny; netvrdí nezávislou
novou klasifikaci všech unicyklických reprezentací.

Nový `verify_exchange_appendix.py` porovnává pro 1≤m,p≤28 konvoluční
rekurence H/J s binomickým tvarem, součet (G) s uzavřeným vzorcem
a přesnou teleskopickou identitu. Zároveň ověřuje uvedený obrázek.
Běh s nice 15 skončil za přibližně 0.2 sekundy s kódem 0; počty
malých kontrol jsou v přiloženém JSON a logu.

## Úloha 19: vážené vzorkování

Celý vlastní důkaz v `priority-sampling.md` byl znovu přezkoumán.
Pro pevné kladné váhy a nezávislé spojité U_i jsou priority U_i/w_i
kladné a různé skoro jistě. Vybereme n−1 nejmenších a práh r je n-tá
priorita. Události rovnosti a přesné nuly mají pravděpodobnost nula;
tím se netvrdí stejný výsledek pro libovolný konečný pseudonáhodný zdroj.

Pro libovolnou pevnou množinu I velikosti k<n podmíníme prioritami
mimo I a vezmeme jejich (n−k)-tou pořadovou statistiku s. Součin odhadů
při skutečném prahu r je skoro jistě stejný jako součin při s+:
buď jsou všechny priority I pod s, nebo jsou oba součiny nulové.
Podmíněná nezávislost a rovnost

    min(w_i s,1) max(w_i,1/s)=w_i

dokazují oba součinové výroky (a,b) i nestrannost. Tonelliho věta
umožňuje integraci nezáporných součinů bez předchozího předpokladu
konečných vyšších momentů.

Pro druhý moment stačí s_i, (n−1)-tá priorita ostatních záznamů:
E[W_i² | ostatní]=w_i max(w_i,1/s_i). Sjednocovací mez dává
Pr(s_i≤t)≤C t^(n−1) pro malé t, takže E(1/s_i)<∞ při n>2.
Součinový výrok s k=2 potom skutečně implikuje nulové kovariance
a sčítání konečných rozptylů. Při N=n=2 a jednotkových vahách je druhý
moment nekonečný, takže podmínka n>2 má podstatný význam.

Maximová halda uchovává n nejmenších priorit dosud přečtených položek;
kořen je po konci vstupu r, ostatní uzly vzorek. Paměť je O(n), změna
haldy O(log n), jeden průchod stačí. Netvrdíme očekávané O(1) na krok
pro tuto prostou implementaci. Výroky o součtech se týkají pevné skupiny
položek, případně skupiny vybrané nezávisle na náhodných prioritách;
nejsou garancí pro libovolný výběr podle samotného výsledku vzorkování.

Primární Duffield–Lund–Thorup byl znovu přečten v definici 1.1 a celém
oddílu 2 (strany 5–8); strana 7 také vizuálně. Autoři používají opačné
priority w_i/α_i a k=n−1 největších prvků, práh τ=1/r. Jde o arXiv
cs/0509026v1, nikoli ověřenou sazbu JACM 2007. Na PDF je současně
datum sazby 2018; nelze je zaměňovat s datem původního preprintu 2005.
Doplněná odpověď 19 na původní 593 obsahuje pouze odkaz na JACM 54
(2007), článek 32, strany 32:1–32:37; byla přečtena v all2-prepre 34.
Některé indexy v důkazu preprintu jsou nekonzistentní; správnost výroku
zde stojí na samostatném stručném podmíněném důkazu, ne na jejich převzetí.

## Prameny, errata a další krok

Robbins–Bolker: v této revizi vizuálně přečteny strany 270–278 včetně
celých důkazů vět 1–4 a 6–9 a důsledku 5. Nové obrazy 270, 273–275
odpovídají souborovým stranám 4, 7–9; mapování potvrzeno v záhlaví.
Tabulka jiných extrakčních míchání ani následující věty se tím nově
neuzavírají. Goldstein–Moews: oddíly 2–4 (strany 2–11) a 6 (14–18),
strany 4 a 18 vizuálně. Jde o arXiv math/0010066v1 z roku 2000,
s pozdějším datem sazby na titulní straně, nikoli časopiseckou sazbu 2003.
Oddíl 5 o symetriích a oddíl 7 o limitních zákonech nejsou součástí
tohoto důkazu a nebyly celé znovu auditovány.

Všechny čtyři již obnovené vrstvy errat a aktuální TeX prohledány
pro 148/592, priority sampling a příslušné autory. Žádná další oprava
těchto tvrzení nenalezena. Přesný Cervantesův citát doplněný za úlohy
zůstává bibliografickou výjimkou; stejně tak samostatná časopisecká
sazba Goldstein–Moews 2003 a Duffield–Lund–Thorup 2007. Odkazy
na rovnici 5.1.4–(40) a sekci 6.2.2 nebyly v tomto bloku nově prověřovány ve svazku 3;
potřebná nerovnost a vlastnosti stromů mají zde vlastní důkaz.

Sekce má nyní souvisle přezkoumaný celý text i všech 19 úloh včetně
dodatků; 18 úloh je uzavřených, jedna partial. To není dokončený celý
svazek. Strany 148/592 zůstávají partial kvůli úloze 16; na 592 navíc
čekají první odpovědi §3.5. Pokračování je §3.5 od původní strany 149.
