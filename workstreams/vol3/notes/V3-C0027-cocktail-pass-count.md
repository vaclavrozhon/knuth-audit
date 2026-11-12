# V3-C0027 — započtení posledního cocktail průchodu

**Candidate / low**, 2026-11-07. Originál tištěná696/file707,
odpověď§5.4.8-9; souvislost s úlohou§5.2.2-9 a obrázkem16
na110/file121. Jde o nejasnou počítací konvenci, nikoli
potvrzenou chybu redukce u nebo třídicího algoritmu.

Na353 je u_k=#{i≤k:a_i>k}. Odpověď696 uvádí počet průchodů
2max(u_1,…,u_n)−(0 nebo1). Úplný binární prahový důkaz
v `notes/exchanging-proof-cocktail-109-110-9.md`, P0962–0963,
prokazuje, že dvojice průchodů sníží každé kladné u_k právě
o1. Proto tento vzorec skutečně platí pro **první okamžik,
kdy už je pole uspořádané**, při U=max u_k>0; pro identitu
je tento čas0.

Varianta z obrázku16 může potřebovat další ověřovací průchod.
Na permutaci2341, u=(1,1,1,0), jsou řady

    2341 → 2314 → 1234 → 1234.

Po prvním průchodu je R=3, po druhém L=2. Třetí tedy
provede porovnání pozic2 a3 a teprve zjistí nulový počet
výměn. Vykonány jsou3 průchody, nikoli1 nebo2. Již původní
obrázek16 má U=3 a sedm zobrazených průchodů; poslední je
bez výměny, ale se třemi porovnáními. Všech osm sloupců,
hranice i výměny jsou samostatně doloženy v P0959.

Znění696 nemusí zamýšlet započtení poslední kontroly. Při
této interpretaci je vzorec správný; proto se položka
**nepovyšuje na confirmed**. Přesné doplnění by řeklo
„until the array first becomes sorted, excluding a possible
final verification pass“. Při počítání všech vykonaných
průchodů do zjištění nulového počtu výměn je obvykle nutno
přidat tento další průchod; konkrétní politika prázdných
intervalů a okamžitého ukončení musí být určena zvlášť.

Original353/356/696 je uložen beze změny v
`sources/cocktail-cross-reference.pdf` a zobrazen v
`images/cocktail-cross-reference-1.png` až`-3.png`.
Pět vrstev je v `sources/cocktail-pass-count-errata-review.json`.
Nalezená oprava696 se týká jiného vzorce v§5.4.9-2, nikoli
tohoto počtu průchodů. Známé poznámky k popisku16 a modernímu
hardwaru se nedotýkají této počítací konvence. Žádný brute force
ani výpočetní experiment; fyzický výtisk nebyl kontrolován.
