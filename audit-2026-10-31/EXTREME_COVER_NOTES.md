# Extrémní exact cover a Gouldovy konstanty

Kontrola 31. 10. 2026: 7.2.2.1–182,184–192, vzorce (82)–(86).
Otevřená výzkumná úloha 183 není vyřešena. Značení: B_n jsou Bellova čísla,
G_n počty rozkladů s posledním blokem velikosti jedna; g je Eulerova–Gompertzova
konstanta. Bloky jsou uspořádány podle nejmenšího prvku.

## F018: nadbytečný i_2 v odpovědi 180

Str. 468 nejprve správně určuje výskyty i_2 jako o_2,o_3,o_4,o_5, ale
o dva řádky níže uvede další možnost o_6 obsahující i_2. Tento symbol
má být vypuštěn: o_6 obsahuje i_3, nikoli i_2.

Konkrétní strict příklad má řádky
`1000,1100,1110,1111,0111,0011,0001`.
Každý sloupec má délku čtyři, první čtyři větvící řádky protínají
postupně 4,5,6,7 možností. Splňuje tedy t=u=4. Šestý řádek je 0011,
a druhý sloupec v něm není. Obecný strukturální důkaz je v
[EXACT_COVER_NOTES.md](EXACT_COVER_NOTES.md).

Publikovaná oprava z 15. 2. 2026 se týká **zadání** na str. 147;
tento symbol v odpovědi neopravuje. Znění je také v autorově PS str. 172.

## 182,184,185: počty řešení

Čtyři singletony a čtyři hrany čtyřcyklu dávají sedm řešení a 16 uzlů.
Při k disjunktních kopiích MRV dokončí rozpracovanou kopii, protože její
zbývající sloupce mají délku nejvýše dvě proti třem v nedotčené kopii.
Tedy S_k=7^k a T_k=9+7T_(k−1), T_0=1; výsledkem je
T_k=(5·7^k−3)/2. DLX ověřil k=0,...,5, až 16 807 řešení a 42 016 uzlů.

V konstrukci 184 obsahují možnosti všechny neprázdné podmnožiny prvních
n−1 prvků a vybrané možnosti obsahující n. Možnost velikosti n−j s n
ponechá j prvků s úplnou soustavou možností, tedy B_j dokončení.
Kapacita takových možností je C(n−1,j). Proto je počet řešení součet
a_j B_j, 0≤a_j≤C(n−1,j). Indukce z odpovědi funguje: po zaplnění
vyšších kapacit a odečtení násobku B_j je zbytek menší než B_j;
indukční kapacity C(j−1,k) se vejdou do C(n−1,k). Případ t=B_n
zaplní všechny kapacity a případ t=0 má nepokrytý poslední prvek.
Zákaz stejných sloupců platí i pro t=0; pro n=1 je jen jeden sloupec.

Nezávislý množinový solver ověřil **všech 1162 požadovaných počtů**
0≤t≤B_n, 1≤n≤7, i příklad n=9,t=10 000. Vypočtený rozklad do
Bellových čísel nemusí být stejný jako v knize; reprezentace není jedinečná.

Pro 185 zvolme rozklad N_1 primárních prvků do m bloků. Každý sekundární
prvek může být nepoužit nebo připojen k jednomu z m bloků, nezávisle.
Počet je tedy Σ_m S(N_1,m)(m+1)^N_2. Nezávislý algoritmus s volitelnými
sekundárními prvky ověřil všech 30 dvojic 0≤N_1≤5, 0≤N_2≤4.

## (82)–(85),186–188: aktualizace a vytvářející funkce

Při výběru možnosti velikosti k obsahující zvolený prvek zbývá úplná
úloha na n−k prvcích. To přímo dává (82). Počet odstraněných uzlů při
cover je `u_n=1+Σ_k C(n−1,k−1)(k−1)=1+(n−1)2^(n−2)` pro n≥1.
Další pokryté sloupce mají postupně velikosti úloh n−1,...,n−k+1;
jejich příspěvek je součet u těchto indexů. Součet přes k dává (84),
včetně zvlášť ošetřeného n=0.

Nezávislý DLX pro n=0,...,8 souhlasí s kořenovými i celkovými počty
aktualizací. Například n=8: 4140 řešení, 38 941 aktualizací u kořene,
87 056 celkem. Rekurence a explicitní (85) souhlasí přesně až do n=80.
Koeficienty a_nk pro k>0 počítají rozklady s posledním blokem velikosti k;
ověřeno úplným výčtem **5296 rozkladů** pro n≤8. Sloupec k=0 je B_n.

Pro EGF B(z)=exp(exp(z)−1) a T(z)=T_(0,0)(z) máme
`B'=exp(z)B`, `T'=exp(z)T+1`. Explicitní výraz 187(d) proto stačí
dosadit do `X'−exp(z)X=V'` a zkontrolovat X(0)=0. Symbolický výpočet
ověřil obojí; stejně ověřil pomocný výraz pro T_(1,3).

Obecně `T_(r,s)'−exp(z)T_(r,s)=z^r exp(sz)` a T_(r,s)(0)=0.
Integrace derivace `t^(r+1)exp(−exp(t))` dává první identitu 187(c).
Pro s>0 vezmeme primitivní funkci

`P(t)=exp(st) Σ_(k=0)^r (−1)^k r! t^(r−k)/((r−k)! s^(k+1))`.

Má P'=t^r exp(st). Integrace per partes s exp(−exp(t)) dává
přesně druhou identitu (c), včetně krajního členu
`−(−1)^r r! B(z)/s^(r+1)`. Tím je obecný vztah ověřen bez
spoléhání na konečný výčet r,s.

Trojúhelník 188 má **úmyslně zvláštní první řádek 0**. Jeho levý okraj
se shoduje s G_n až pro n≥2. Odpověď výslovně předpokládá n>1;
počáteční řádek tedy není chyba knihy. Původní test zde chybně požadoval
shodu i při n=1 a byl opraven. Zbytek trojúhelníku souhlasí do n=80.

### F019: chybějící exp(sz) v odpovědi 187(b)

Na str. 468 je obecný index s, ale pravá strana diferenciální rovnice
má pouze z^r. Musí obsahovat z^r exp(sz), nebo se musí všechny indexy
omezit na s=0, což pro část (b) stačí. Například r=0,s=1,z=1 dává
`T'−exp(z)T=e`, zatímco tisk dává 1. Znění potvrzuje PS str. 172.
Ostatní zkontrolované identity 187 jsou správné.

## 189–192: šest míst v sazbě a návaznost

### F020: opačné znaménko R(z)

Str. 148 definuje ρ_n=G_n−g B_n. Protože G_0=0 a B_0=1,
musí být R(0)=−g. Vytištěný kladný integrál dává +g.
Správně je

`R(z)=−exp(exp(z)) ∫_z^∞ exp(−exp(t)) dt`.

Stejný rozpor je i v koeficientu z: skutečně ρ_1=1−g, zatímco
kladný integrál má derivaci g−1. Odhady absolutní hodnoty tato oprava
nemění. Znění potvrzuje PS str. 84.

### C006: nesprávný výraz uvnitř již publikovaného errata

Erratum Fascicle 5 z 19. 12. 2019 nahrazuje odpověď 189(a), ale jeho
druhá rovnost a kniha na str. 469 mají `exp(exp(−x) cos y)` místo
`exp(−exp(x) cos y)`. Pro z=0 dávají e místo 1/e. Ve starém PS je
ještě starší verze odpovědi; nezaměňovat ji za znění nové opravy.
Tohle vedeme jako **doplnění známého errata**, mimo počet nových
nezávislých nálezů. Matematický rozpor je jednoznačný; nejistá je
nezávislost vůči již hlášené opravě.

### F021: dvě místa v odstavci 189(c)

Na str. 469 je `g/3`, má být `g/e`. Substituce x=exp(t)−1 dává

`∫_0^∞ exp(−exp(t)) dt = (1/e) ∫_0^∞ exp(−x)/(1+x) dx = g/e`.

Obě hodnoty jsou přibližně 0.2193839344 a chybně 0.1987824541.
Hned další věta maximalizuje modul exp(exp(uz)), ale používá
vzorec pro modul **exp(−exp(uz))**. V levém výrazu chybí minus.
Už z=0 rozliší e a 1/e. Obě místa jsou i v původním PS str. 173;
vedeme je společně jako opravu tohoto odstavce.

### F022: faktor k v konstantách za odpovědí 189(d)

První z dvojice integrálů pro g_k musí mít jmenovatel **(k−1)!**,
nikoli k!. Druhý integrál s log^k(1+x)/k! je správný. Substituce
x=exp(t)−1 a integrace per partes přímo dávají

`∫_0^∞ exp(−x)log^k(1+x) dx = k ∫_0^∞ t^(k−1)exp(1−exp(t)) dt`.

Pro k=2 je druhý integrál po vydělení 2! přibližně 0.2659653850,
první vytištěný jen poloviční. Integrály jsou kladné, takže rozdíl
pro k>1 není otázka numerické přesnosti. Obě opravené formy souhlasí
na 55 desetinných míst pro k=1,...,12. Znění potvrzuje PS str. 173.

Také [Corollary 4 původního článku autorů](https://math.sun.ac.za/swagner/gould.pdf)
uvádí správný jmenovatel (k−1)!; to je další doklad vedle přímého odvození.

### F023: konstantní člen řady v odpovědi 191

G(0)=0 z definice na str. 148, ale gamma-řada na str. 469 dává e.
Chybí člen −e. Pro z>0 integrací per partes získáme

`G(z)=e z ∫_1^∞ exp(−t)t^(z−1)dt`.

Rozdělení úplného gamma integrálu v bodě 1 a rozvoj exp(−t) na [0,1]
dají

`G(z)=e Γ(1+z) − e − Σ_(k=1)^∞ (−1)^k e z/((k+z)k!)`.

Výraz pokračuje spojitě i do z=0. Oprava souhlasí s přímým integrálem
pro z=0,1/4,1/2,1,2,3 na 55 míst. Střední hodnota 1+g i rozptyl
`2g_2+g−g²≈0.7726479558` jsou v knize správně; člen −e nemění derivace.
Znění potvrzuje PS str. 173.

## Odhad 189 po opravách

Znaménko R pro absolutní hodnoty nehraje roli. Na kružnici z=ξ exp(iθ),
ξ exp ξ=n, stačí pro symetrii 0≤θ≤π. Označme x=Re z, y=Im z.

Při y≤3/2, θ≤π/2 je x≥ξ−(9/4)/ξ a cos y≥cos(3/2)>0.
Obloukový a reálný díl integrálu dávají mez v (b), protože pro každé
c_1<cos(3/2) absorbuje exponenciální rezerva polynomiální faktor ξ.

Při y≥3/2 máme x≤ξ−9/(8ξ). Vyberme u_0 maximalizující
exp(−exp(ux)cos(uy)). Pokud cos(u_0 y)≥0, integrál po úsečce je O(ξ).
Pokud cos y−cos(u_0 y)≤1, součin s |exp(exp(z))| je nejvýše
ξ exp(exp(x)). V posledním případě trigonometrická identita vynutí
u_0≤1−π/(3y), a tedy

`u_0 x ≤ ξ cos θ − (π/3)cot θ ≤ ξ−c ξ^(1/3)+O(1)`,

kde c³=3π²/8. Minimum ztráty plyne z vyvážení ξθ²/2 a π/(3θ);
pro θ oddělené od nuly je ztráta ještě větší. Proto je exp(u_0 x)
zanedbatelné proti exp(ξ)/ξ a všechny tři případy dávají (c) pro
libovolné c_2<9/8. Pro θ≥π/2 máme x≤0 a integrand po vynásobení
|exp(exp(z))| omezený konstantou, takže R=O(ξ).

Cauchyho odhad a Bellova sedlová asymptotika pak dávají
`|ρ_(n−1)/B_(n−1)|=O(sqrt(ξ n) exp(−c_2 n/ξ²))`.
Volba **1<c_2<9/8** absorbuje odmocninu a díky ξ<ln n dostaneme
požadovaný O(exp(−n/ln²n)). Hlavní výsledek tedy po opravách platí.
Bellova asymptotika z dílu 4A zde byla použita jako vstup, ne znovu dokázána.

## Původně neuzavřená kontrola 190 a 192

V 192 je stacionární bod x=exp(ξ)−1, ξ exp ξ=n, druhá derivace
logaritmu integrandu je −(1+ξ)/n. To souhlasí s uvedeným Gaussovým
hlavním členem. Numerická integrace normalizovaná v sedle dává poměr
skutečnost/asymptotika 1.02531 při n=10, 1.00403 při n=100 a 1.000562
při n=1000. Obecný argument chvostů je doplněn níže. Znaménkový vzor 190 byl následně
přepočítán přesnými celými Bellovými a Gouldovými čísly a konstantou g
na 1000 a 1200 desetinných míst. Všech 101 znamének pro 4000≤n≤4100
a délky jejich běhů přesně souhlasí s knihou. Relativní odchylky jsou
řádu 10^−557 až 10^−569; běžná strojová přesnost by nestačila.
Jde o stabilní numerické znaménko, nikoli certifikovanou intervalovou
aritmetiku. Obecná otevřená otázka znamének v 190 tím není vyřešena.

Doklady: `check_extreme_cover.py`, `results/extreme_cover.json`,
`check_gould_constants.py`, `results/gould_constants.json`, vykreslené
strany 148,468,469 a PS 84,172,173. F018–F023 nebyly nalezeny v načtených
úplných erratech 4B a Fascicle 5; výjimka C006 je výslovně popsána výše.
Fyzický výtisk dosud neověřen.

## Doplnění: úplný Laplaceův argument pro 192

Položme f(x)=−x+n ln ln(1+x), ξ exp ξ=n, x₀=exp ξ−1,
σ²=n/(1+ξ), A=exp(f(x₀)). Funkce f je přísně konkávní na x>0:

`f''(x)=−n(ln(1+x)+1)/((1+x)² ln²(1+x))`.

Třetí derivace je

`f'''(x)=n(2l²+3l+2)/((1+x)³ l³)`, kde l=ln(1+x).

V sedle je f'=0, f''=−1/σ² a f''' σ³=O(sqrt(ξ/n)). Vezměme
h=(n/ξ)^(1/12). Na |x−x₀|≤hσ je relativní odchylka (x−x₀)/(1+x₀)
řádu O((ξ/n)^(5/12)), tedy mizí. Třetí derivace je tam stejného řádu
jako v sedle a Taylorova chyba je uniformně O((ξ/n)^(1/4))=o(1).
Proto f(x₀+σy)−f(x₀)=−y²/2+o(1) pro |y|≤h.

Současně na tomto intervalu pro velká n platí f''≤−1/(2σ²).
Na jeho pravém kraji je tedy f≤f(x₀)−h²/4 a f'≤−h/(2σ);
na levém kraji obdobně f'≥h/(2σ). Globální konkávnost omezuje
oba zbývající chvosty tečnou. Jejich integrály jsou dohromady
nejvýše `4Aσ exp(−h²/4)/h=o(Aσ)`. Střední část má integrál
`Aσ(sqrt(2π)+o(1))`. Po vydělení n! dostáváme přesně hlavní člen
z odpovědi 192. Zanedbatelnost chvostů je tím doplněna obecně,
nikoli jen numericky.
