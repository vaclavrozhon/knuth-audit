# D179–D180 — celé MPR78–79

7. listopadu 2026. Původní zadání p19/file39 a odpovědi
p382/file402 přímo zobrazeny; totéž PS p19/file25 a p38/file44.
Šest vrstev errat a tři TeX zdroje posouzeny. Žádný numerický
běh. Přesné přechody mezi pomocnou a vlastní historií se
přebírají z D098, nikoli z jeho chybných vedlejších příkladů.

## 78: násobení a všechny nulové případy

Už p2 vyžaduje absolutní konvergenci součtů definujících
očekávání a p6 u martingalů výslovně předpokládá existenci
E Z_n. P7 tutéž podmínku opakuje pro předvídatelné násobení.
Tuto konvenci používáme i zde: všechny součiny a podíly,
jejichž očekávání se v argumentu bere, jsou integrabilní.
Integrabilita jednotlivých faktorů se sama o sobě nezaměňuje
s integrabilitou jejich součinu nebo podílu. Na konečném
pravděpodobnostním prostoru s konečnými hodnotami je tato
podmínka automatická. Bez ní by formule s nedefinovaným
očekáváním nebyla tvrzením v režimu knihy.

Nechť H_n=(V₀,…,V_n) a E(V_{n+1}|H_n)=1. Konečný
součin Z_n=V₀···V_n je známý z H_n a

    Z_{n+1}=Z_n V_{n+1},
    E(Z_{n+1}|H_n)=Z_n E(V_{n+1}|H_n)=Z_n.          (1)

Na každém kladně hmotném vlákně H_n je Z_n konstantní,
proto jej lze vytknout; integrabilita ospravedlňuje součty.
Vlastní historie Z₀,…,Z_n je funkcí H_n. Její další
podmínění v(1) dává martingalovou rovnost(26), přesně
jako v D098. Definice nevyžaduje E V₀=1; počáteční
člen Z₀=V₀ může mít libovolnou konečnou střední hodnotu.

Obráceně každý konečný součin nutně splňuje
Z_n=0 ⇒ Z_{n+1}=0. Proto odpověď na otázku „every“ je
obecně záporná. Přesný protipříklad je Z₀=0 a Z_n=ξ
pro n≥1, kde ξ=±1 férově. Jde o celý omezený martingale,
ale první nenulová hodnota nemůže být0 krát konečný faktor.
Tento již doložený obecný svědek se pouze aplikuje,
žádný výpočet se neopakuje.

Pro martingale, který na nule zůstane, položme V₀=Z₀
a pro n≥1

    V_n=Z_n/Z_{n−1}, je-li Z_{n−1}≠0;
    V_n=1,          je-li Z_{n−1}=0.                (2)

Ve druhé větvi je také Z_n=0. Indukce tedy dokazuje
Z_n=V₀···V_n v každé větvi, nejen před první nulou.
V_j je funkcí historie Z do j; naopak všechny Z_j
rekonstruujeme ze součinů historie V. Obě celé historie
do n tak poskytují stejnou informaci.

Na vlákně, kde Z_n≠0, lze v podmíněném očekávání
poměru vytknout1/Z_n a martingalová vlastnost dává

    E(V_{n+1}|Z₀,…,Z_n)
      =E(Z_{n+1}|Z₀,…,Z_n)/Z_n=1.

Na vlákně Z_n=0 je V_{n+1}=1 přímo. Stejnost historií
pak dává multiplikativní férovost vzhledem k V.
To dokazuje celou tištěnou obrácenou konstrukci včetně
větve nuly. Podmínka integrability poměrů v(2) se zde
explicitně dědí z obecné konvence o existenci očekávání;
samotná absorpce nuly ji u obecných neomezených znaménkových
proměnných nedokazuje. Není tvrzeno širší zobecnění.

## 79: každý faktor De Moivreova martingalu

Výraz s oběma poměry q/p,p/q má přirozený obor0<p<1,
q=1−p. Na tomto oboru jsou všechny základy kladné
a konečné. Degenerované p=0,1 do zapsaného poměrového
modelu nepatří; vzorec se tam nerozšiřuje pomocí0/0
ani negativních mocnin nuly.

Označme S_n=X₁+…+X_n, S₀=0, a V₀=1. Položme

    V_j=(q/p)^{2X_j−1},    j≥1.

Pro X_j=1 je to q/p, pro X_j=0 je to p/q.
Nezávislost bitů zaručuje nezávislost těchto funkcí bitů.
Jejich přesné očekávání je

    E V_j=p(q/p)+q(p/q)=q+p=1.

Součin má exponent Σ(2X_j−1)=2S_n−n, a je tedy přesně
Z_n=(q/p)^{2S_n−n} ze zadání. Pro každé konečné n má
jen n+1 možných hodnot a je omezen konečnou konstantou
max(q/p,p/q)^n; integrabilita tedy není přidaný předpoklad.
Nezávislost nového bitu od celé dosavadní historie a výše
vypočtená střední hodnota dávají(1), takže Z je martingale
vzhledem k bitům, faktorům i vlastní historii.

Základ n=0 je prázdný součin1. Při p=q=1/2 je každý
faktor i každý Z_n roven1. Jako přesnou kontrolu všech
mocnin lze také sečíst celý konečný binomický zákon:

    E Z_n=Σ_{k=0}^n binom(n,k) p^k q^{n−k}
                             (q/p)^{2k−n}
         =Σ_{k=0}^n binom(n,k) q^k p^{n−k}=1.

Každý součin se zjednoduší na q^k p^{n−k}; poslední
rovnost je binomická věta při p+q=1. Samotná shoda
nepodmíněných průměrů nenahrazuje martingalový důkaz,
který je výše úplný.

## Bibliografie a rozsah

[Katalog ETH/e-rara](https://www.e-rara.ch/zut/doi/10.3931/e-rara-10420)
přímo potvrzuje De Moivreovu The Doctrine of Chances,
londýnské vydání1718. Přesný
historický obsah celého citovaného rozsahu pp102–154
nebyl v tomto krátkém bibliografickém kroku prohlédnut;
výslovně se vynechává. Zvláště se netvrdí, že autor1718
používal současný pojem martingale. Matematický důkaz
zde na historickém prameni nezávisí.

V erratech odpovídají shody sousední72,83 nebo jiným
fasciklovým oddílům; žádná použitelná změna78–79 nebyla
nalezena. Obě úlohy jsou uzavřeny ve výše přesně vyložené
obecné konvenci integrability a v oboru definice poměrů.
Žádný nový nález ani kandidát, žádný běh nebo restart.

