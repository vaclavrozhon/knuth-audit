# D183 — celá MPR82, Ace Now a zobecněná urna

7. listopadu 2026. Původní zadání p19/file39, rovnice(28)
p6/file26, pravidla hry p8/file28 a odpověď p382/file402
přímo zobrazeny. Autorův PS z11.9.2019: zadání p19/file25,
odpověď p39/file45. Všechny šest vrstev errat a tři TeX
zdroje v manifestu80–82 posouzeny; použitelná oprava82
nenalezena. D099 již dokázal konečnou hru a její zisk.
Tento přesný důkaz se přebírá bez běhu; zde je doplněn
celý rozsah zadání, zobecněná urna a bibliografická výjimka.

## 82(a): model, každá podmíněná větev a konec indexů

Prostor je konečný: rovnoměrné promíchání52 různých karet,
z nichž4 jsou esa. X₀=0, X_j je indikátor esa v pozici j.
Po n odkrytých kartách položme A_n=4−Σ_{j=1}^n X_j
a C_n=52−n. Zbývající pořadí je podmíněně rovnoměrné,
neboť každý pevný prefix má právě(52−n)! pokračování.
Proto pravděpodobnost dalšího esa je A_n/C_n. Platí to
jak pro historii indikátorů X, tak pro jemnější historii
všech skutečně odkrytých identit karet: součty přes
prefixy se stejnými indikátory zachovávají týž poměr.

Podíl Z_n=A_n/C_n je definován pro0≤n≤51, je známý
z historie a leží v[0,1]. Integrabilita je tedy přímá.
Pro0≤n≤50 máme C_n≥2 a při označení A=A_n,C=C_n:

    E(Z_{n+1} | celá historie do n)
      =(A/C)(A−1)/(C−1)+(1−A/C)A/(C−1)
      =(A(A−1)+(C−A)A)/(C(C−1))
      =A(C−1)/(C(C−1))=A/C=Z_n.

Je-li A=0 nebo A=C, nemožná větev se nepoužije;
jediný skutečný nový podíl je0 nebo1. Algebra s nulovým
koeficientem dává stejný výsledek, protože C−1 je kladné.
Odpověď píše na levé straně pouze E Z_{n+1}. V odstavci
fixujícím současné A_n,C_n jde o očekávání z aktuálního
stavu. Výše je jeho podmínění rozepsáno; neztotožňujeme
nepodmíněnou konstantu E Z_{n+1} s náhodným A_n/C_n
a nevytváříme samostatnou kartu pro tuto zkratku.

**F167, místní indexová chyba zadání:** požadovaný rozsah
„satisfies(28) for0≤n<52“ zahrnuje n=51. Rovnice(28)
však obsahuje Z_{n+1}; v tomto kroku je třeba Z₅₂,
zatímco tiskový podíl je(4−4)/(52−52)=0/0 na každém
promíchání. Správný rozsah přechodů je0≤n<51.
Rozsah samotných definovaných Z_n je0≤n<52.
Alternativně lze výslovně definovat Z_n=Z₅₁ pro n≥51;
to je konstantní pokračování, nikoli hodnota tiskového0/0.
Pak je i přechod n=51 (a každý pozdější) martingalový.

Z₅₁ je indikátor, že poslední zbývající karta je eso.
Na události pravděpodobnosti4/52=1/13 je tedy1.
Plošná konvence0/0=0 by ani sama neopravila přechod:
podmíněné Z₅₂ by bylo0, kdežto Z₅₁=1 na této události.
Pravidla skutečné hry poslední podíl nepotřebují.
Jde o lokální chybu horního indexu, nikoli o nepravdivý
výsledek(b,c). Anglický přesný doklad je v samostatné
poznámce F167; mapuje se pouze zadánífile39.

## Celý dovětek zobecněné urny

Před tahem nechť jsou počty r,b nezáporná celá čísla,
t=r+b>0, a po vybrání a navrácení koule se přidá k
koulí téže barvy. Hodnota k je zvolena před tahem
(tištěná posloupnost k_n), případně může být známou
funkcí dosavadní historie. Není dovolena dodatečná
závislost k na právě vylosované barvě, která by měnila
obě větve různě. Každá možná větev musí mít nezáporné
počty a t+k>0, aby následující podíl byl definován.

Pro r,b>0 potřebujeme při k<0 zároveň r+k≥0,b+k≥0.
Podmíněný průměr nového červeného podílu je přesně

    (r/t)(r+k)/(t+k)+(b/t)r/(t+k)
      =r(r+k+b)/(t(t+k))=r/t.

Při r=0 je jediná možná barva černá a červený podíl
zůstává0; při b=0 je jediná možná barva červená
a podíl zůstává1. Nevyžadujeme platnost fyzicky nemožné
větve. Záporné k tedy nijak nevadí, jsou-li tyto podmínky
splněny. Proces zastavíme před prázdnou urnou nebo jeho
poslední podíl výslovně zmrazíme. Všechny podíly jsou
omezené, přizpůsobené celé urnové historii a jejich
podmíněné průměry rovny předchozí hodnotě; to dokazuje
celý obecný dovětek i pro proměnné předvídatelné k.
Přechod k vlastní historii je již doložen věží v D098.

Karty jsou přímo případ k=−1, počáteční r=4,b=48.
Výpočet proto přesně zahrnuje model úlohy. Poslední
vyprázdnění urny se nesmí vydávat za definovaný poměr,
což je právě indexová hranice posouzená výše.

## 82(b,c): libovolná přípustná strategie

N označuje počet již odkrytých karet v okamžiku volby
Stop. Pravidla nutí0≤N≤51; rozhodnutí závisí jen na
dosavadních kartách. Použijme úplnou historii karet,
aby byly zahrnuty i strategie využívající barvy či
hodnoty jiných karet, nikoli jen indikátory es.
První důkaz platí také vůči této historii.

D099 již dokazuje omezené zastavení. Konkrétní použití
lze rozepsat bez limitu: s Δ_j=Z_j−Z_{j−1},

    Z_N=Z₀+Σ_{j=1}^{51}[N≥j]Δ_j.

Událost[N≥j] je známa před j-tým odkrytím, takže
E([N≥j]Δ_j)=E([N≥j]E(Δ_j|historie do j−1))=0.
Všechny součty jsou konečné, všechny veličiny omezené.
Proto E Z_N=Z₀=4/52=1/13, přesně(b), bez předpokladu
neomezené verze optional stopping a bez Z₅₂.

Podmíněná pravděpodobnost, že zvolená následující karta
je eso, je Z_N. Formálně rozložíme podle konečně mnoha
událostí[N=n]; na každé z nich použijeme výše dokázaný
poměr A_n/C_n. Tedy P(X_{N+1}=1)=E Z_N=1/13.
Čistý zisk G je12 při esu a−1 jinak, takže

    E G=12/13−12/13=0,

nebo podmíněně E(G|historie při zastavení)=13Z_N−1.
Tím jsou celé(b,c), všechny strategie i jejich stejná
pravděpodobnost výhry doloženy. Nejde o rovnost každého
realizovaného zisku. Konstantní pokračování po51 nemění
žádnou z herních veličin.

## Bibliografie a přesný rozsah

Původní citace R. Connelly, „Say Red“, Pallbearers Review
9(1974),702 nebyla při krátké bibliografické kontrole
dostupná v primárním časopisu. Přesný historický obsah
a vztah varianty Ace Now se proto výslovně vynechávají.
Sekundární odkazy se nevydávají za kontrolu originálu.
Matematický důkaz je na nich nezávislý.

Celá82(a–c), všechny kroky odpovědi a zobecněná urna
jsou posouzeny; F167 je lokální oprava v zadání(a).
Žádný běh ani restart. C047 a staré otevřené mezery
zůstávají zachovány; nepředstírá se root revize F167.

