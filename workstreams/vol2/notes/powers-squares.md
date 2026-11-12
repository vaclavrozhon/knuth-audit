# §4.6.3-38: společný řetězec všech čtverců

Stav 2026-11-04: úloha auditována, nikoli vyřešena její otevřená otázka
o přesné asymptotice. Obě uvedené meze dokazujeme níže s výslovně
uvedenými standardními prvočíselnými vstupy. **C0230 je potvrzená chyba
ve volbě parametru r v odpovědi 38 na straně 697.** Celková horní mez
zůstává správná po opravě r. Jde o matematickou chybu konstrukce,
ne o pouhý rozdíl v zaokrouhlování nebo OCR.

## 1. Značení a otázka

Sčítací řetězec začíná 1 a každý další člen je součtem dvou dřívějších.
Jeho délka je počet sčítání. Píšeme S(m)=l(1²,2²,...,m²) pro nejmenší
délku řetězce obsahujícího všechny uvedené cíle. Po odstranění duplicit
a členů větších než m² má takový řetězec m čtverců a nějaký počet h
ostatních členů; jeho délka je m+h-1. Úloha se ptá na růst S(m)-m.

Symboly ln a lg znamenají přirozený, respektive dvojkový logaritmus.
O(g) označuje výraz omezený konstantním násobkem g, o(g) výraz, jehož
podíl s g jde k nule. Konstanty smějí záviset na pevném epsilon>0.
Dále p_r je r-té prvočíslo, K_r=p_1*...*p_r jejich součin, zvaný
primoriál. Zbytek a mod k bereme v {0,...,k-1}.

Používáme standardní analytické výsledky o prvočíslech:

```text
p_r = r*(ln r+ln ln r-1+O(ln ln r/ln r)),
ln K_r = p_r + o(p_r/(ln p_r)^2),
sum_(p<=x) 1/p = ln ln x+O(1),
#{p<=x : p prime, p=3 mod4} ~ x/(2 ln x).                   (S1)
```

První dva jsou slabší verze vstupů citovaných přímo v odpovědi38 a
v odpovědi4.5.4-36; jejich význam je rozebrán v
[factoring-refinement.md, §1](factoring-refinement.md#1-co-přesně-se-minimalizuje).
Třetí byl použit i v [factoring-basic.md](factoring-basic.md). Poslední
je věta o prvočíslech v pevné aritmetické posloupnosti. V tomto bloku
netvrdíme nový důkaz těchto analytických vět; z nich však všechny
níže uvedené odhady pro řetězce odvozujeme samostatně.

## 2. Přesná Newmanova konstrukce

Pro k=K_r vytvoříme k a všechny nenulové zbytky čtverců modulo k.
Potom vytvoříme k,2k,...,qk, kde q=floor(m²/k). Pro každý i<=m je

```text
i² = k*floor(i²/k) + (i² mod k),
```

takže stačí nejvýše jedno další sčítání. Nulový sčítanec se vynechá.
Celková cena je nejvýše

```text
m + P(r) + max(0,floor(m²/K_r)-1),                         (S2)
```

kde P(r) označuje cenu první společné tabulky.

Je nutné zpřesnit neformální počet zbytků v knize. Označme jejich
počet včetně nuly R_r. Čínská zbytková věta, tedy bijekce mezi zbytky
modulo k a seznamy zbytků modulo jeho různá prvočísla, dává přesně

```text
R_r = 2*product_(2<p<=p_r) (p+1)/2
    = (4/3)*2^(-r)*K_r*product_(p<=p_r)(1+1/p).             (S3)
```

Modulo liché p je (p-1)/2 nenulových čtverců a nula; modulo2 oba
zbytky. Proto R_r není asymptoticky ekvivalentní prostému 2^(-r)K_r.
Ze (S1) a ln(1+x)<=x plyne R_r=O(2^(-r)K_r ln p_r).

Přesto je uvedená cena P(r)=O(2^(-r)K_r ln K_r) správná. Použijeme
již dokázanou konečnou mez úlohy37, viz
[powers-vector.md, (V1)](powers-vector.md#31-konečná-horní-mez).
Při d=floor(lg K_r) a blokové délce b=floor((lg d)/2) stojí společná
tabulka mocnin d kroků a každý ze R_r cílů dalších O(d/lg d) kroků.
Protože ln p_r je řádu ln ln K_r, dostáváme

```text
P(r) = O(ln K_r + R_r*ln K_r/ln ln K_r)
     = O(2^(-r)*K_r*ln K_r).                              (S4)
```

Zvláštní malé r lze pohltit konstantou. Užití společného výpočtu
je podstatné: samostatné binární řetězce pro všechny zbytky by měly
navíc faktor řádu ln ln K_r. Slovo „approximately“ v knize proto
nebereme jako samostatné přesné tvrzení o poměru počtů; (S3) a (S4)
vyplňují potřebné podrobnosti důkazu.

## 3. C0230: vytištěná volba r nefunguje

Na straně697 je vytištěno

```text
r = floor((1+(ln2)/(2*lg lg m))*ln m/ln ln m).               (S5)
```

Původní stránka byla zobrazena a oba dvojkové logaritmy i koeficient
ověřeny přímo v sazbě. Položme t=ln m, u=ln t a a=(ln2)^2/2<1.
Protože lg lg m=(u-ln ln2)/ln2, dostáváme

```text
r = (t/u)*(1+a/u+O(1/u²)) + O(1).
```

Obecně pro libovolnou pevnou konstantu A a
r=(t/u)*(1+A/u+O(1/u²))+O(1) platí

```text
ln r = u-ln u+A/u+O(1/u²),
ln ln r = ln u-(ln u)/u+O((ln u)²/u²),
p_r = t+(A-1)*t/u+O(t*ln u/u²),
ln K_r = t+(A-1)*t/u+O(t*ln u/u²).                         (S6)
```

Poslední dva řádky vyplývají ze (S1). Změna r o O(1) má v tomto
rozvoji zanedbatelný vliv O(u). Dosazení A=a dává

```text
floor(m²/K_r) = m*exp((1-a+o(1))*ln m/ln ln m).             (S7)
```

Protože 1-a>0, poměr této hodnoty k m jde do nekonečna. Už seznam
násobků v předepsané konstrukci tedy obsahuje mnohem více než m
různých čísel. Nemůže vést k řetězci délky m+o(m), natož k uvedené
ostřejší horní mezi. Jde o asymptotický rozpor, nezávislý na konečné
konstantě skryté v O.

Pouhá výměna lg lg m za ln ln m nestačí: potom by A=ln2/2<1 a
problém (S7) by zůstal. Je třeba zároveň změnit koeficient.
Jedna korektní explicitní volba je

```text
r = floor((1+(1+(ln2)/2)/ln ln m)*ln m/ln ln m).            (S8)
```

Pro c=ln2/2 je nyní A=1+c, takže (S6) dává

```text
ln K_r = t+c*t/u+O(t*ln u/u²),
ln(m²/K_r) = t-c*t/u+O(t*ln u/u²),
ln(2^(-r)*K_r*ln K_r) = t-c*t/u+O(t*ln u/u²).
```

V posledním řádku jsme použili r*ln2=2c*t/u+O(t/u²); člen
ln ln K_r=O(u) je zanedbatelný. Pro každé epsilon>0 jsou obě
přípravné ceny O(m*exp(-(c-epsilon)*t/u)). Dosazení do (S2) dokazuje
přesně horní mez uvedenou v knize. Oprava se týká parametru, nikoli
platnosti výsledné nerovnosti.

Konečný ilustrativní případ: m=2^1024 dává podle (S5) r=111,
p_r=607. Přesný součin prvních111 prvočísel má831 bitů, kdežto
floor(m²/K_r) má1218 bitů. Samotná příprava násobků už tedy
přesahuje m o nejméně193 bitů v exponentu poměru. Tento příklad
ilustruje (S7); důkaz chyby asymptotického tvrzení je (S6)–(S7).

## 4. Vlastní důkaz dolní meze

### 4.1 Dva jednoduché číselné odhady

Pro prvočíslo q=3 mod4 nemůže být q² součtem dvou kladných čtverců.
Kdyby q²=x²+y² a q nedělilo y, pak (x/y)²=-1 modulo q, ve sporu
s malou Fermatovou větou po umocnění na (q-1)/2. Když q dělí y,
dělí i x a oba kladné sčítance jsou alespoň q², opět spor.
Ze (S1) je takových cílových čtverců asymptoticky m/(2 ln m).

Nechť tau(d) je počet kladných dělitelů d a
T(m)=max_{1<=d<=m²} tau(d). Pro každé eta>0 platí
T(m)=O_eta(m^eta). Zde je elementární důkaz: pro dostatečně velká
prvočísla p a každé e>=1 je e+1<=2^e<=p^(eta*e/2). Pro konečně
mnoho menších p je maximum (e+1)/p^(eta*e/2) přes e>=0 konečné.
Vynásobením přes prvočíselný rozklad d dostaneme tau(d)<=C_eta*d^(eta/2).

### 4.2 Kolik čtverců mohou vytvořit pomocné členy

Vezměme libovolný rostoucí řetězec obsahující všechny čtverce do m²,
a A jeho h nečtvercových členů. Pro každé prvočíslo q=3 mod4 zvolme
operaci, která vytvořila q². Podle §4.1 musí obsahovat pomocný člen.

Je-li druhým operandem čtverec b², pak pro pevný a v A platí
(q-b)(q+b)=a. Každá dvojice určuje rozklad a na dva kladné dělitele,
a proto vznikne nejvýše T(m) takových čtverců pro jedno a, nejvýše
h*T(m) celkem. Operace a+a vytvoří nejvýše h dalších čtverců.

Zbývají dvojice různých prvků A. Vytvořme jednoduchý neorientovaný
graf na A: spojíme a a b, právě když a+b je čtverec. Je-li z společný
soused dvou různých vrcholů a,b, pak a+z=x², b+z=y², a tudíž

```text
(x-y)(x+y)=a-b.
```

Při prohození a,b můžeme předpokládat a>b. Každý kladný rozklad
rozdílu a-b určuje x,y a pak z nejvýše jedním způsobem. Dvojice
vrcholů tedy má nejvýše T(m) společných sousedů.

Označme E počet hran a d_v stupeň vrcholu v. Dvojím spočtením cest
délky dva a Cauchyho nerovností dostaneme

```text
sum_v binom(d_v,2) <= T(m)*binom(h,2),
(2E)^2 <= h*sum_v d_v²
        <= h*(T(m)*h*(h-1)+2E).
```

Pro h>=1 řešení kvadratické nerovnosti dává

```text
E <= (h/4)*(1+sqrt(1+4*T(m)*(h-1)))
  <= h/2 + sqrt(T(m))*h^(3/2)/2.                           (S9)
```

To je celý potřebný kombinatorický argument; nepřebíráme bez důkazu
obecnou extrémní větu o grafech. Pro h=0 je tvrzení triviální.
Počet vybraných čtverců je tedy nejvýše

```text
h*T(m)+h+E <= (5/2)*h*T(m)+(1/2)*sqrt(T(m))*h^(3/2).        (S10)
```

### 4.3 Závěr

Pro pevné 0<epsilon<1/3 předpokládejme h<=m^(2/3-epsilon).
V odhadu T(m) zvolme eta=epsilon. Pravá strana (S10) je pak
O(m^(2/3)+m^(1-epsilon))=O(m^(1-epsilon)). Levá strana je však
asymptoticky m/(2 ln m), což je větší řád. To je spor pro velká m.

Máme tedy h>m^(2/3-epsilon) pro každé pevné epsilon>0 a dostatečně
velké m. Použitím výsledku s epsilon/2 a rovnosti délka=m+h-1
získáme i přesnou ostrou formulaci knihy

```text
S(m) > m + m^(2/3-epsilon)                                (S11)
```

pro dostatečně velká m. Hodnoty epsilon>=1/3 plynou ze silnější
malé kladné volby. Mezi (S11) a opravenou horní mezí zůstává mezera;
žádný z těchto důkazů neurčuje asymptotickou ekvivalenci S(m)-m.

## 5. Prameny, aktuálnost a známé opravy

Plný originál Dobkina–Liptona (1980), strany121–125, nebyl získán:
PDF i běžná stránka SIAM při lokálním přístupu vracejí403, webové
rozhraní poskytuje metadata a abstrakt. Autorský Yaleův seznam zpráv
neobsahoval použitelný odpovídající odkaz. Přečtení pěti stran článku
netvrdíme. Vlastní důkaz §4 tuto mezeru v matematické kontrole nahrazuje.

[Enge, Hart, Johansson (2018)](https://cs.uwaterloo.ca/journals/JIS/VOL21/Enge/enge1.pdf)
byl přečten v relevantních částech na stranách5,7–8,17,21–22, včetně
původní sazby. Text17 stále uvádí Newmanův výsledek jako nepublikovanou
mez komunikovanou Pippengerovi a rozlišuje asymptoticky slabší praktické
metody. Dolní mez na5 odpovídá (S11). Algoritmus pro vyčíslení celého
součtu na5 a21 nemusí vytvářet každý monom, a proto není vyřešením
úlohy38. Obecné vzorce pro prvočíselné mocniny na21 nejsou předmětem
samostatného úplného auditu; pro náš čtvercuprostý modul stačí (S3).

[Autorský přehled Sergeeva](https://igorssergeev.github.io/#p42) zmiňuje
výsledek2024 s vyššími dolními mezemi pro jiné explicitně konstruované
množiny a zlepšení Pippengerova maticového odhadu. Nevydává jej za řešení
posloupnosti všech čtverců. Získali jsme autorovu stránku; plný článek
přes MathNet dostupný nebyl. V dostupných novějších pramenech jsme
nenalezli odstranění mezery v úloze38. Nejde o důkaz absence další
literatury ani o tvrzení, že byly přezkoušeny všechny výsledky do2026.
Johanssonovy slidy2015 byly staženy jen jako navigační podklad;
matematické závěry neopíráme o jejich plnou kontrolu.

Pro C0230 byly přečteny všechny relevantní bloky šesti vrstev errat.
Ve druhém vydání existuje související změna z1997-06-28, strana638,
odpověď33, řádek8: (1+ln2/2) se mění na ln2/2. Příslušná stránka127
errat byla zobrazena. **Tuto změnu nezamlčujeme**, ale nedává opravu
(S5) na správné (S8) v našem třetím vydání. Bez originální stránky
638 druhého vydání neurčujeme, kterou instanci koeficientu přesně
měnila ani zda právě ona způsobila chybu. Ostatní opravy na697 se
týkají37 a39. Odpovídající oprava r ve třetím vydání nebyla nalezena.

## 6. Reprodukovatelné konečné kontroly

`verify_powers_squares.py` provedl tři úspěšné bloky:

- `constructor`: všech šest tabulek zbytků pro r=1,...,6 porovnáno
  přímým výčtem a vzorcem (S3). Počty jsou2,4,12,48,288,2016.
  Dále249 celých konstrukcí pro vymezené m do4096; validováno196150
  sčítání a všechny cíle. Malé případy mají navíc samostatný validátor
  vzestupného řetězce. Netvrdíme, že zvolené konečné parametry jsou
  optimální, ani že asymptotická úspora už platí v malém rozsahu.
- `graph`: všech65536 podmnožin16 nečtverců mezi1 a20, dvojité počítání
  cest a celočíselná Cauchyho nerovnost. Všech120 dvojic vrcholů navíc
  porovnáno s přímými rozklady rozdílu; ověřeno87 prvočíselných překážek
  q=3 mod4 do1000.
- `parameters`: m=2^(2^j), j=4,...,20, tři verze volby r. Podlaha
  určena intervaly s80 desetinnými místy, oba konce každého intervalu
  mají stejnou podlahu. Primoriály a počty násobků jsou přesná celá
  čísla, až do59225 prvočísel. Vytištěná volba má K_r<m ve všech17
  případech. Symbolická kontrola ověřuje pouze lineární koeficient
  A-1 v (S6). Formální O(x²) vrácené CAS není použito jako analytický
  zbytek při přítomnosti ln x; správný zbytek O(x²*(1+|ln x|)) je
  odvozen v §3. Tento limit je výslovně zaznamenán i u raw výsledku.

Časy0.336906865,0.292389100 a4.632881871s; obal7.034409454s,
session19292, PID1578856/1578866/1578870, vše exit0, limit300s/blok.
Žádný matematický blok nebyl opakován. Dodatečně se pouze upřesnil
popis rozsahu CAS výstupu; program a výpočty zůstaly stejné.
Pokus o vykreslení přes nepřítomný modul fitz selhal před vykreslením;
stránky byly následně získány pdftoppm. To nesouvisí s matematickými testy.

Nález C0230 je doložen naším skenem a obecnou analýzou. Tištěný
exemplář, novější dotisk a prvenství nejsou ověřeny. Anglický ASCII
návrh v `reports/C0230-square-parameter.txt` nebyl odeslán. Integritu
souborů a přesný rozsah zdrojů uvádí `sources/powers-squares.json`.
