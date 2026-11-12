# D160–D161 — celé MPR58–59 včetně silnějšího dodatku

7. listopadu 2026. Původní zadání p17/file37 a odpovědi
p378–379/file398–399 byly přímo zobrazeny; také autorův
PS p17/file23 a p35/file41. Všech šest vrstev errat a tři
TeX soubory byly posouzeny; žádná relevantní oprava.
Obdobné číslování58 v pozdějších sekcích není tato úloha.

P059 a GENERAL_PROBABILITY_NOTES.md obsahují platné
základní argumenty59(a–c), ale výslovně vylučují silnější
graduovaný dodatek. Nepřebírají se jako důkaz celé59.
Níže jsou doplněny všechny tištěné mezikroky, příklady
a kraje; zvlášť je uzavřen původně nepokrytý dodatek.
Starý výsledek17788 základních případů se zachovává
bez běhu. Kontroly FKG z P059 tím nejsou automaticky
povýšeny na novou úplnou kontrolu61.

## 58: všechny k-klikové členy

Zadání „generalizing54“ přebírá nezávislost hran z54.
Nechť 0≤k≤n jsou celá, p∈[0,1], q=binom(k,2) a
m=binom(n,k). Pro každou k-prvkovou množinu A vrcholů
je W_A součin indikátorů všech jejích q hran; jde
o indikátor k-kliky. Nezávislost hran dává E W_A=p^q,
tedy pro X=∑_A W_A máme E X=mp^q a

    {X>0}={graf obsahuje k-kliku},
    P(X>0)≤mp^q.                                      (A)

Používáme přirozenou konvenci prázdného součinu1,
tedy p^0=1 i při p=0.

Je-li P(W_A=1)>0, podmínění určí všechny hrany uvnitř A,
ostatní hranové bity zůstávají nezávislé s parametrem p.
Pro další k-prvkovou množinu B s t=|A∩B| je přesně
binom(t,2) jejích hran už určeno. Proto

    E(W_B|W_A=1)=p^{binom(k,2)−binom(t,2)}.

Je přesně binom(k,t)binom(n−k,k−t) takových B:
zvolíme průnik s A a doplněk mimo A, jednoznačně.
Součet přes všechna t=0,…,k tedy dává

    D=∑_{t=0}^k binom(k,t)binom(n−k,k−t)
                         p^{k(k−1)/2−t(t−1)/2}.         (B)

Je stejný pro každé A. Nerovnost(24), v plném rozsahu
převzatá z D152, proto dává přesně tištěnou dolní mez

    P(X>0)≥mp^q/D.                                    (C)

Člen t=k v(B) je1; všechny ostatní jsou nezáporné.
D je tedy vždy≥1 a žádný zlomek(C) nemá nulový
jmenovatel. Žádné jiné typy překryvu chybět nemohou:
společné hrany obou úplných podgrafů jsou právě všechny
dvojice společných vrcholů.

Tento výsledek je také přímo druhou momentovou mezí,
kterou žádá návaznost na54. Pro každé A platí
∑_B E(W_AW_B)=p^q D, takže E X²=mp^qD. Je-li mp^q>0,
podíl(EX)²/EX² je právě(C). Nevyžaduje se nezávislost
různých W_A.

### Kraje

- Pro k>n neexistuje žádná taková množina, takže
  pravděpodobnost0 určíme přímo;(B) není potřeba
  vyhodnocovat se záporním horním binomickým parametrem.
- Pro k=0 je jedinou klikou prázdná množina. m=D=1
  a obě meze jsou1, i pro n=0,p=0.
- Pro k=1 a n≥1 jsou všechny jednotlivé vrcholy klikami.
  D=(n−1)+1=n=m, takže dolní mez je přesně1.
- Pro k≥2,p=0 je událost nemožná a(C) dává0/1=0.
  Rovnost podmíněného průměru s(B) na nulové události
  se zde netvrdí; mez platí přímo.
- Pro p=1 součet multiplicity v(B) počítá každou
  k-prvkovou množinu B právě jednou, tedy D=m a(C)=1.
- Pro k=n zbývá pouze t=k a(C) je přesná hodnota p^q.
- Pro k=2 redukuje(B) na1+(m−1)p: každá odlišná
  hrana má při podmínění stále pravděpodobnost p.
  Dostáváme správnou mez mp/(1+(m−1)p).

Tím jsou doloženy všechny členy i všechny přirozené
okrajové případy; žádný číselný výčet není potřebný.

## 59(a): každý krok základní nerovnosti

Všechny jednotlivé hodnoty aᵢ,bᵢ,cᵢ,dᵢ jsou konečná
nezáporná reálná čísla. Předpoklady jsou

    a₀b₀≤c₀d₀,       a₀b₁≤c₁d₀,
    a₁b₀≤c₁d₀,       a₁b₁≤c₁d₁.                      (H)

Součet obou diagonálních členů je již odhadnut.
Zbývá a₀b₁+a₁b₀≤c₀d₁+c₁d₀. Položme
h=c₁d₀, x=a₀b₁, y=a₁b₀. Přímé roznásobení dává

    h(c₀d₁+h−x−y)
      =(h−x)(h−y)+(c₀c₁d₀d₁−a₀a₁b₀b₁).            (1)

První součin je nezáporný podle obou smíšených
předpokladů(H). Druhá závorka je nezáporná, neboť
vynásobením obou diagonálních nerovností(H) dostáváme
a₀a₁b₀b₁≤c₀c₁d₀d₁; násobíme jen nezáporná čísla.

Pro h>0 lze(1) vydělit h. Pro h=0 vynutí(H) x=y=0
a požadovaná smíšená nerovnost platí přímo.
Přičtením diagonálních nerovností dostáváme
(a₀+a₁)(b₀+b₁)≤(c₀+c₁)(d₀+d₁) ve všech případech.

### Oba požadované příklady rovnosti

První tištěný vektor je

    (a₀,a₁,b₀,b₁,c₀,c₁,d₀,d₁)=(0,1,0,1,1,1,0,1).

Všechny čtyři předpoklady jsou rovnosti0=0,0=0,0=0,1=1,
ale závěr je1<2.

Druhý je

    (a₀,a₁,b₀,b₁,c₀,c₁,d₀,d₁)=(1,1,1,2,1,2,1,1).

Předpoklady jsou1=1,2=2,1<2,2=2, ale závěr je
(1+1)(1+2)=(1+2)(1+1)=6. Obě otázky v zadání
tedy mají kladnou odpověď; jsou ověřeny všechny
předpoklady, nikoli jen poslední součty.

## 59(b): všechny čtyři indukční aplikace

Symboly j|k a j&k znamenají bitové OR a AND.
Pro n bitů rozdělme indexy jako2j+l, kde l∈{0,1}
a 0≤j<2^{n−1}. Pro l,m∈{0,1} platí přesně

    (2j+l)|(2k+m)=2(j|k)+(l|m),
    (2j+l)&(2k+m)=2(j&k)+(l&m).                         (2)

Nízký bit a ostatní bity se zde nemísí, nevzniká přenos.
Původní hypotéza tedy pro čtyři zvolené podposloupnosti
a_{2j+l},b_{2k+m},c_{2r+(l|m)},d_{2s+(l&m)}
splňuje tentýž předpoklad na n−1 bitech.

Označme součty sudé a liché podposloupnosti A_l,B_l,C_l,D_l.
Indukce dává postupně

    A₀B₀≤C₀D₀,       A₀B₁≤C₁D₀,
    A₁B₀≤C₁D₀,       A₁B₁≤C₁D₁.

Všechny čtyři součty jsou konečné a nezáporné, takže
na ně lze použít celou část(a), včetně nulových případů.
Výsledek je(A₀+A₁)(B₀+B₁)≤(C₀+C₁)(D₀+D₁).
Sudé a liché třídy tvoří přesně rozklad původních
indexů; to je požadovaná nerovnost.

Základ n=1 je(a); lze také začít n=0, kdy jde pouze
o původní hypotézu a₀b₀≤c₀d₀. Tím je indukce konečná
a všechny mezikroky odpovědi(b) jsou zdůvodněny.

## 59(c): nekonečné součty bez nevymezeného0·∞

Použijme přesně dvojné součty ze zadání. Pro každý r
nechť A_r,B_r,C_r,D_r jsou součty přes0≤j<2^r.
Všechny jsou konečné a z(b) máme

    S_r=A_rB_r=∑_{j,k<2^r}a_jb_k
      ≤T_r=C_rD_r=∑_{j,k<2^r}c_jd_k.

Čtverce indexů rostou a vyčerpají všechny dvojice
nezáporných celých čísel. Každá konečná množina dvojic
je obsažena v některém takovém čtverci. Proto definice
součtu nezáporné řady jako supremu konečných podsoučtů
dává S_r↑S a T_r↑T, kde S,T jsou právě dva dvojné
součty ze zadání, případně+∞. Z toho S≤T.

Tištěný důkaz sporem je rovněž platný v této přesné
interpretaci: kdyby S>T, muselo by být T konečné a
některé S_r>T; přitom S_r≤T_r≤T. V případě nulové celé
a-posloupnosti či b-posloupnosti je S=0 přímo, i když
druhá jednoduchá řada diverguje. Není potřeba přiřazovat
nevymezený reálný součin0·∞; dvojné součty jej obejdou.

## Silnější graduovaný dodatek: úplný konečný argument

Použijeme cestu z [Christofides, §2, str.3–4](https://arxiv.org/pdf/0909.5137).
Předpoklad na konečné množině E označme
α(A)β(B)≤γ(A∪B)δ(A∩B); doplňky jsou relativní k E.

Nejprve pomocná nerovnost: jestliže u(A)v(B)≤s(B\A)t(A\B),
pak

    u(A)v(Bᶜ)≤s((A∪B)ᶜ)t(A∩B).

Použití59(b) na u,v∘complement,s∘complement,t dává
(∑u)(∑v)≤(∑s)(∑t), protože doplněk permutuje podmnožiny.

Položme f(A)=α(A)β(Aᶜ), g(A)=γ(Aᶜ)δ(A). Přesné identity:

    f(A)f(B)=α(A)β(Bᶜ)α(B)β(Aᶜ)
      ≤γ(A∪Bᶜ)δ(A∩Bᶜ)γ(B∪Aᶜ)δ(B∩Aᶜ)
      =g(A\B)g(B\A).

Pomocná nerovnost nyní dává(∑f)²≤(∑g)², tedy∑f≤∑g,
neboť oba součty jsou nezáporné. Po přejmenování doplňku:

    ∑_A α(A)β(Aᶜ)≤∑_A γ(A)δ(Aᶜ).                     (3)

Pro pevné I⊆U použijme(3) na E=U\I a funkce
α′(R)=α(I∪R), analogicky β′,γ′,δ′. Předpoklad se zachová:

    α′(R)β′(S)≤γ((R∪S)∪I)δ((R∩S)∪I)
              =γ′(R∪S)δ′(R∩S).

Dvojice(I∪R,U\R) mají právě průnik I a sjednocení U.
Jejich velikosti se sčítají na|I|+|U|. Sečtení(3) přes
I⊆U s|I|+|U|=h započte každou dvojici velikostí se součtem h
právě jednou. Dostáváme koeficientovou nerovnost.

### Přesný přenos na knižní nekonečné indexy

Každé j<2^r kóduje podmnožinu r pozic, ν_j je počet
jejích prvků. Výše dokázaný konečný výsledek tedy dává

    ∑_{j,k<2^r; ν_j+ν_k=h} a_jb_k
      ≤∑_{j,k<2^r; ν_j+ν_k=h} c_jd_k.                  (4)

Pro pevné h≥0 obě strany monotónně rostou při r→∞.
Každá jednotlivá dvojice s ν_j+ν_k=h má konečnou
bitovou délku, a proto se nakonec objeví. Definice
nezáporného součtu ze59(c) dovoluje přejít k limitě
a dává přesně celý tištěný dodatek i při nekonečných
hodnotách. Pro h=0 jde o původní a₀b₀≤c₀d₀.
Konečný primární výsledek se nepoužívá bez zdůvodnění
na nekonečný svaz.

Výše uvedené formule byly znovu odvozeny přímo;
žádný pomocný tištěný řádek externího článku se nepřebírá
jen podle autority. Například ve smíšeném součinu se
musí objevit α(B)β(Aᶜ), což zaručuje první rovnost
pro obecné funkce bez jakékoli symetrie.

## Bibliografie a hranice převzetí

[Původní Ahlswede–Daykinův článek](https://www.math.uni-bielefeld.de/ahlswede/homepage/public/30.pdf)
byl uložen. První a poslední strana přímo potvrzují
časopis, ročník43, rok1978, stránky183–185 i formulaci
přes rodiny množin, na kterou odkazuje kniha. Celý
obecný nekonečný distributivní svaz z článku zde
nepřebíráme; potřebný binární případ je dokázán výše.

[Záznam vydavatele Björnerova článku](https://link.springer.com/article/10.1007/s00493-011-2644-1)
potvrzuje Combinatorica31(2011),151–164 a téma
koeficientové FKG nerovnosti. Obsah tohoto celého
článku není náhradou důkazu našeho obecnějšího dodatku.
Ten je doložen předchozím argumentem.

Christofidesova původní sazba má šest stran a identifikaci
arXiv0909.5137v1,28.9.2009. Přímo byly posouzeny
strany1,3–4 včetně potřebných vět2.1/2.2 a lemmatu2.3.
Netvrdíme audit celé lattice reprezentace z dodatku
článku, kterou zde vůbec nepotřebujeme.

## Rozsah

Celé58 a59(a–c) i celý silnější dodatek jsou reviewed.
P059 zůstává zachovaný se svým původním rozsahem a testy;
nový D161 doplňuje právě chybějící rozsah. Žádný nový
nález, kandidát, bibliografická výjimka ani numerický běh.
File398 je nyní celý posouzen s již uloženými výpočetními
výjimkami55. File37 a399 zůstávají partial pro60 a další.

