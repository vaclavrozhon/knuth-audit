# D184 — celá MPR83, Waldova rovnost

7. listopadu 2026. Původní zadání p20/file40, definice(31)
p7/file27 a celá odpověď p382/file402 přímo zobrazeny.
PS11.9.2019: zadání p20/file26, odpověď p39/file45.
Šest vrstev errat a tři TeX zdroje posouzeny v samostatném
manifestu83. Žádný výpočet ani restart.

## Zastavovací pravidlo, každá hodnota N a každá nezávislost

Označme I_n=N_n(X₀,…,X_{n−1}) pro n≥1.
Definice pravidla vyžaduje I_n∈{0,1} a po prvním0
již samé0. Tedy na každém výsledku je posloupnost I
řetězec jedniček a pak nul, případně nekonečně mnoho
jedniček. Proto pro N=Σ_{n≥1}I_n platí přesně

    I_n=[N≥n].

Zahrnuty jsou N=0, každé konečné N i N=∞.
I_n je funkcí celé historie X₀,…,X_{n−1}, a tudíž
je nezávislé na X_n díky vzájemné nezávislosti
celé zadané posloupnosti. Nezaměňujeme vzájemnou
nezávislost za pouhou párovou nezávislost.

Pro nezáporné X_n definujeme S₀=0 a při N=∞
S_N jako nezáporný součet celé řady. Bodově platí

    S_N=Σ_{n≥1}X_n I_n.

Nekonečná hodnota je dovolena; neprovádí se rozdíl
dvou nekonečen. Pišme μ_n=E X_n. V obvyklé konvenci
integrabilních jednotlivých veličin jsou μ_n konečné.
Nezávislost přímo dává

    E(X_n I_n)=μ_n P(N≥n)=E(μ_n I_n).             (1)

Kdyby se zadání rozšířilo i na nekonečná μ_n,
stejná rovnost plyne nejprve pro min(X_n,M),
pak monotónním limitem M→∞. Nulový indikátor
na nemožné události přispívá0; právě to stanoví
obvyklou konvenci0·∞=0 v nezáporných integrálech.
Tato širší varianta není potřebná pro níže uvedený
martingalový důkaz s centrováním.

## Každý tištěný součtový krok

Všechny členy X_n I_n i μ_n I_n jsou nezáporné.
Monotónní konvergence pro jejich částečné součty
a(1) proto dovolují každou rovnost v odpovědi:

    E S_N
      =Σ_{n≥1} E(X_n I_n)
      =Σ_{n≥1} μ_n E I_n
      =Σ_{n≥1} E(μ_n I_n)
      =E Σ_{n≥1} μ_n I_n
      =E Σ_{n=1}^N μ_n.

Poslední identita je bodová podle již doloženého
tvaru I_n. Není potřeba E N<∞ ani předem konečné
E S_N. Obě strany mohou být+∞, přesně jak uvádí
tištěný dovětek. Není zde použit optional stopping
pro neomezený čas.

Je-li μ_n=μ pro všechny n>0 a0<μ<∞, náhodný
součet je μN a dostáváme E S_N=μ E N.
Pro μ=0 jsou všechna nezáporná X_n=0 skoro jistě;
sjednocení spočetně mnoha výjimek má míru0,
takže i S_N=0 skoro jistě, včetně N=∞.
Tento kraj lze buď uvést samostatně, nebo použít
uvedenou nezápornou konvenci0·∞=0.
Při N=0 skoro jistě jsou obě náhodné sumy0.
To pokrývá přesně obecný i konstantně-průměrový
výrok zadání a jejich degenerované případy.

## Úvodní martingale a F168

První věta odpovědi tiskne

    Z_n=Σ_{k=1}^n(X_n−E X_n).

Summand neobsahuje index k, proto tato posloupnost
je n(X_n−μ_n), nikoli centrovaný částečný součet.
Není obecně martingale. Na dvou stejně pravděpodobných
atomech nechť X₁=0 nebo1 a X₀=X₂=X₃=…=0.
Všechny členy jsou nezávislé, nezáporné a omezené;
konstantní členy nekladou žádnou překážku nezávislosti.
Tiskový Z₁=X₁−1/2 nabývá±1/2, ale Z₂=0.
Tedy E(Z₂|Z₀,Z₁)=0≠Z₁ na obou atomech.

**F168 low:** v obou výskytech uvnitř summandu
nahradit n indexem k. Pro opravené

    M_n=Σ_{k=1}^n(X_k−μ_k), M₀=0,

je M_n známé z X₀,…,X_n a konečně integrabilní,
protože E|X_k−μ_k|≤2μ_k. Nezávislost dává

    E(M_{n+1}|X₀,…,X_n)
      =M_n+E(X_{n+1}−μ_{n+1}|X₀,…,X_n)=M_n.

Vlastní martingalová historie pak plyne věží
(přesný obecný argument již v D098).
Dvouatomový svědek vyvrací i vlastní historii,
takže nejde o jiný výklad pomocného podmiňování.
Hlavní Waldova rovnost i přímý důkaz výše zůstávají
zcela správné; chyba je v pomocné první větě.
Anglický doklad F168 a lokace pouzefile402 jsou oddělené.

## Celá historická oprava a dokončení naznačené druhé cesty

Errata16.8.2020, historická p194, mění dvě místa83:
„min(m,N)“ na přesnou funkci

    N'_n(x₀,…,x_{n−1})=[n<m]N_n(x₀,…,x_{n−1})

a následné S_n na S_N. Obě opravy jsou již ve4B;
PS2019 ještě ukazuje původní znění. Originál errat
all4f5p10 i TeX blok4f5.194 přímo posouzeny.
**E127 pouze známé erratum**, žádná nová karta.

Pro každé celé m≥1 má N'_n hodnoty0,1,
závisí jen na minulosti a po prvním0 zůstává0.
Je tedy platným omezeným pravidlem. Jeho počet kroků
je přesně N^{(m)}=min(N,m−1), protože členy s n≥m
jsou0. Pro m=1 je počet0. Tím je přesný koncový
index objasněn; při limitě m→∞ pokryje každé N.

Na opravený M_n lze použít již dokázané konečné
zastavení D099: E M_{N^{(m)}}=0. Přesná důsledná
rovnost je

    E S_{N^{(m)}}=E Σ_{k=1}^{N^{(m)}} μ_k.

Obě strany jsou očekávání konečných integrabilních
součtů. Při m→∞ jejich náhodné nezáporné součty
monotónně rostou k oběma stranám hlavní identity.
Použitím monotónní konvergence jednotlivě na obě
strany dostaneme tentýž výsledek. Netvrdíme
monotónnost centrovaných M_{N^{(m)}} ani jejich
automatickou uniformní integrabilitu.
Tím je dokončena i celá první naznačená metoda.

## Bibliografie a rozsah

Primární archiv JSTOR identifikuje názvy obou
citovaných Waldových článků. Archiv čísla16(3)
potvrzuje1945 a pp287–293. Přímý plný text
Project Euclid nebyl při krátkém přístupu dostupný;
samotné titulní stránky vJSTOR nevystavily obsah.
Přesné původní předpoklady, srovnání „somewhat
different problem“ a „proved more“ i zbývající
neověřená metadata1944 se výslovně bibliograficky
vynechávají. Žádný historický výsledek se nepřebírá
jako matematická opora našeho důkazu.

Celá83, oba důkazy, každý nekonečný součet,
všechny okraje a známé opravy jsou posouzeny.
F168 je samostatná místní chyba prvního summandu.
Není tvrzena nezávislá revize koordinátora.

