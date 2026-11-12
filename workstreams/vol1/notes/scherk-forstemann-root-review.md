# §1.2.6-60: původní Scherk a Förstemann

Kořenová revize 2. listopadu 2026, V1-X0722. Celá úloha 60 je
nově checked. Již přijatá matematika X0078 se netestovala znovu;
nově jsou doloženy oba konkrétní prameny i přeložená citace.

Root ověřil všech 22 souborů, 4327198 bajtů, a sedm vstupů paketu
`parallel/binomial-summation-sources/exercise60/`. SHA-256 jeho
MANIFEST.json je
`42734cb814f6a945c9a16af882ec4c68e0264fe7d09bbce4bd8f1d456f29d537`.
Přečetl poznámku, předání, erratový výpis a starší vlastní důkaz.
Obrazově četl původní tituly obou ročníků, Scherkovy celé 96–97,
Förstemannovy celé 237–239 a knižní odpověď na 490.

Pro výběr k prvků s opakováním z n možností označme jejich
neklesající pořadí a_1,...,a_k. Knižní převod b_i=a_i+i−1 dává
ostře rostoucí k-tici v {1,...,n+k−1}; odečtení i−1 je inverze.
To je bijekce, tedy párové přiřazení obou množin výběrů, a dává
počet binom(n+k−1,k). Nulové případy již ošetřuje starší důkaz.

Scherkovo třetí tvrzení na 97 dává přesně opačný převod: odečíst
0,1,...,h−1 od h vybraných prvků. Jeho (h,k) odpovídá knižnímu
(k,n). Bezprostřední příklad pro h=k=3 vypisuje deset trojic
z pěti prvků a jejich deset obrazů s opakováním ze tří prvků.
První řádek má chybný konec množiny k−h+1 místo k+h−1; zamýšlené
správné znění určují příklad i samotný posun. Tato chyba původního
článku není chyba TAOCP. Celá rubrika výslovně předkládá tvrzení
k důkazu a závěr žádá kombinatorický důkaz: doloženo je zveřejnění
pravidla, nikoli hotový psaný důkaz v této rubrice. Titul ročníku
3 přímo potvrzuje Berlin 1828.

Förstemann na 237 redukuje vzorec na stejnou bijekci; na 238
výslovně přičítá 0,1,...,n−1 a ověřuje hranice i inverzi.
Jeho (m,n) odpovídá knižnímu (n,k). Příklad 2233+0123=2356
i zachování lexikografického pořadí souhlasí. Překládaná věta
o jednoduchém důkazu, který autor nenalezl v prohlédnutých dílech,
je na závěrečné 239. Knižní 237 je začátkem článku, nikoli chybným
umístěním samotné věty. Titul ročníku 13 uvádí 1835; podpis
13. října 1834 je datum rukopisu, nikoli rok tisku.

Čtyři hashované vrstvy errat neobsahují opravu těchto citací,
převodu ani překladu. Sousední změny odpovědí 58/62/64–68 jsou
odděleny. Závěr potvrzuje obsah a časové pořadí konkrétních dvou
publikací, nikoli vyčerpávající průzkum všech dřívějších textů.
Žádný nový nález nevznikl.
