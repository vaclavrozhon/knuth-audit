# §1.3.1′ — samostatné argumenty k úlohám1–24

Zadání p.24–25/file32–33, odpovědi p.94–95/file102–103. Každá úloha má níže vlastní argument; shoda s odpovědí se kontrolovala až proti tomuto argumentu. B=2^64. Pomocné registry v programech je nutné volit tak, aby nepřepsaly ještě potřebný operand; kde výstup může aliasovat vstup, je to výslovně rozlišeno.

**1.** 2009=7·256+13·16+9, tedy7d9. Uvedený binární vzor po doplnění úvodní nuly je0111 1101 1001, totéž. Odpověď souhlasí.

**2.** Hex písmena A..F mají hodnoty10..15; liché jsouB,D,F a jejich malá varianta. ASCII A..F=41..46hex, malá a..f=61..66hex; přičtení20hex je sudé, takže liché majíA,C,E,a,c,e. Odpověď souhlasí; nejde o vlastnost tvaru písma.

**3.** Názvosloví je návrh, ne jednoznačné matematické tvrzení. S „nyp“=2 bity funguje2 nyps=4 bity=nybble a2 nybbles=8 bitů=byte; zbytek řady V0010. Připsání Gregoru Purdymu a historický vznik slova byte v IBM1956 zde nejsou samostatně doloženy; citovaný BYTE článek nebyl dohledán.

**4.** Násobení každého sousedního členu1000 vede k giga10^9,tera10^12,peta10^15,exa10^18,zetta10^21,yotta10^24,ronna10^27,quetta10^30, se symbolyG,T,P,E,Z,Y,R,Q. Aktuální primární tabulka [BIPM](https://www.bipm.org/en/measurement-units/si-prefixes) byla přečtena6.11.2026; doplnění R/Q je [rozhodnutí27.CGPM2022](https://www.bipm.org/en/-/resolution-cgpm-27-3). Tisk zastavující uYB má **známé erratum29.3.2023**, errata/originals/err1f1.textxt620–624. Není to náš nález. Poznámka KKB/MMB je autorovo doporučení, nikoli současné oficiální binární názvosloví; sám to v erratech výslovně rozlišuje. Bibliografické datování19.CGPM v původním textu je nahrazeno stejnou známou opravou.

**5.** Pro n≥1 leží s(α) v intervalu I=[−2^(n−1),2^(n−1)) a je kongruentní u(α) modulo2^n (V0012). Má-li také x∈I stejný zbytek, x−s(α) je násobek2^n ležící ostře mezi−2^n a2^n, tedy0. Opačný směr je dosazení. To dokazuje obě implikace a jedinečnost, nikoli jen binární příklad.

**6.** Komplement n bitů má u(¬α)=2^n−1−u(α), tedy po přičtení1 dává−u(α) modulo2^n. Signed rovnost před případným overflow je s(¬α)=−s(α)−1. Negovaná hodnota je reprezentovatelná kromě s(α)=−2^(n−1), kdy+2^(n−1) leží mimo rozsah. Pravidlo proto správně dává modular negation vždy; jako přesné signed negování má právě tuto jednu výjimku. Pro nulu vrací nulu a nevzniká signed overflow. Odpověď souhlasí.

**7.** Pro32bitový t se s(t)·2^32 liší od u(t)·2^32 buď0, nebo−2^64; uložených64 bitů je shodných a signed výsledek leží v signed64 rozsahu. Naopak pro64bitové x je floor(s(x)/2^32)=floor(u(x)/2^32)−2^32, je-li x záporné, jinak stejná hodnota. To je přesně signed interpretace horního tetra a leží v signed32 intervalu. Proto lze obě definice použít a nevznikne nový overflow. Důležitá je floor, nikoli truncation směrem k nule.

**8.** Je-li Y škálováno faktorem2^−64 a Z celočíselné, reálný součin je u(Y)u(Z)/2^64. Výsledek MULU je128bitový integer H·2^64+L, takže po škálování jeH+L/2^64: radix point je mezi rH aX. Obecně se škálovací exponenty sčítají, takže poloha je m+n bitů zprava. Odpověď souhlasí.

**9.** Bez aliasu a signed overflow se zachová y=qz+r z V0033, včetně z=0 fallbacku q=0,r=y. Pokud X=Y, staré y=7,z=3 dá po DIV Y=X=2,r=1, ale uvedená rovnost by tvrdila2=2·3+1; neplatí. Pokud X=Z se stejným vstupem, tvrdila by7=2·2+1; neplatí. Overflow y=−B/2,z=−1 dá bitový quotient−B/2,r=0 a pravou stranu+B/2≠−B/2. To jsou přesně uvedené kategorie výjimek; alias může náhodou rovnost zachovat, odpověď pouze vylučuje univerzální platnost.

**10.** Pro signed y,z s z≠0 může |floor(y/z)| překročit B/2−1 pouze při |z|=1 a největší absolutní hodnotě|y|=B/2. z=1 dává y=−B/2, která je dovolená; z=−1 dává+B/2, která není. Pro |z|≥2 je quotient v signed64 intervalu, při z=0 je fallback0. Jediný overflow je tedy Y=8000000000000000,Z=ffffffffffffffff, jak uvádí odpověď.

**11(a).** s(Y)≡u(Y),s(Z)≡u(Z) moduloB, proto součiny mají stejné spodní64 bity. MUL a MULU se mohou lišit overflow/rH, otázka se ale týká pouzeX. **11(b).** Pro oba nezáporné operandy odpovídá obojí stejnému celočíselnému quotientu. Z=0,Y=0,Z=1 aZ=Y rovněž dávají stejné bitové výsledky přímo definicí. Mimo tyto případy: při y≥0,z<0 je signed quotient záporný a unsigned0; při y<0,z≥2 je signed záporný a unsigned<B/2 nezáporný. Při obou záporných nestejných hodnotách má jedna varianta quotient0 a druhá≥1, protože uspořádání velikostí jejich absolutních hodnot je opačné k unsigned pořadí. Tím je úplná klasifikace v odpovědi zdůvodněna.

**12.** Po ADDU je x=y+z−cB,c∈{0,1}. Pokud c=0, x≥y; pokud c=1, x=y+z−B<y, protože z<B. Je-li Y zachováno, CMPU carry,X,Y aZSN carry,carry,1 tedy vrátí přesněc. Při X=Y≠Z lze symetricky porovnat zachovanéZ. Při X=Y=Z je c1 právě pro u(Y)≥B/2, tedy původní negative sign; ZSN carry,X,1 před zdvojením jej uloží. Scratch carry musí být jiný než ještě potřebný operand. Odpověď zahrnuje stejnou výjimku aliasu.

**13.** Různá znaménka sčítanců vždy vedou do signed intervalu. Pro stejná znaménka nastane overflow právě když výsledné modular x má opačné znaménko. Horní bit (x XOR y) AND NOT(y XOR z) je tedy přesněoverflow flag. První XOR musí zachytit staré operandy, druhý potřebuje staréY (proto uvedená podmínka X≠Y). ANDN aZSN převedou horní bit na0/1. To ověřuje odpověď; scratch registry volíme odlišné od živých hodnot.

**14.** Při x=y−z je overflow právě pokud sign(y)≠sign(z) a sign(x)≠sign(y); při shodných znaménkách je rozdíl v rozsahu. Proto lze použít XOR t0,Y,Z; SUBU X,Y,Z; XOR t1,X,Y; AND t1,t1,t0; ZSN flag,t1,1, se zachovanýmY a vlastními scratch. Ekvivalentní podmínka pro inverzní modular y=x+z je sign(x)=sign(z)≠sign(y), jak míní odpověď „interchange X and Y“. Nejde o slepé prohození instrukcí, které by četly dosud nevypočtenéX.

**15.** S η,ζ∈{0,1} jako sign bity platí s(y)s(z)=u(y)u(z)−B(ηu(z)+ζu(y))+B²ηζ. ModuloB² poslední člen mizí. MULU dáP=HB+L; požadovaný high half je(H−ηu(z)−ζu(y)) modB, low zůstáváL. ZSN vybírá jednotlivé korekce a dva SUBU je odečtou přesně podle vzorce odpovědi. Operandy musí přežít do obou ZSN; pomocné registry lze volit čerstvé. Součin má absolutní hodnotu nejvýšeB²/4=2^126, tedy se vždy vejde do signed128. Již opravené u(y),u(z) z errata2.7.2016 jsou v digitálním textu zahrnuty.

**16.** Signed128 hodnota se vejde do signed64 právě když jejích horních64 bitů je sign extension spodních64: buď horní0 a spodní sign0, nebo horníB−1 a spodní sign1. SR L,63 vyrobí odpovídající0/−1; CMP s korektním high z15 aZSNZ dává overflow iff nerovnost. Tento důkaz používá přesný128bitový součin, nikoli jen kontrolu unsigned rH bez signed korekce.

**17.** Konstanta a=(2^65+1)/3=(2B+1)/3 má hex aaaaaaaa aaaaaaab (též16ciferněaaaaaaaaaaaaaaab): geometrická řada všech a dává2(B−1)/3 a poslední+1 výsledek. Pro0≤y<2^65 je ay/2^65=y/3+y/(3·2^65), chyba je v[0,1/3). Zlomková část y/3 je0,1/3 nebo2/3, takže floor se nikdy nezvýší. GET high aSRU o1 realizují floor(floor(ay/B)/2)=floor(ay/(2B)); shoda floor identity plyne rozdělením ay na násobek2B a zbytek. Pro úlohový rozsah y<B tedy program funguje, i když matematická odpověď dokazuje širší rozsah.

**18.** a=(2^66+1)/5=(4B+1)/5 má hexcccccccccccccccd, protože řada c je4(B−1)/5. Pro0≤y<2^66 je chyba ay/2^66−y/5=y/(5·2^66)<1/5. Možné zbytky y/5 jsou0,1/5,…,4/5, tedy floor nezměněn. High aSRU o2 realizují dělení4B; konstanta a<B se vejde do registru. Odpověď souhlasí.

**19.** Tvrzení je nepravdivé. Stačí z=7,e=2,y=B−3. Protože B mod7=2, je y mod7=6 a a=ceil(4B/7)=(4B+6)/7. Přídavná chyba ay/(4B)−y/7=6y/(28B) je≥1/7, neboť3(B−3)≥2B proB≥9, a<2/7. Výsledný floor je tedy o1 větší než floor(y/7). To je obecný symbolický64bitový protipříklad bez census.

Dále pro libovolné z z úlohy a r=2^(64+e) modz je δ=(z−r)y/(2^(64+e)z)∈[0,2/z), neboť z<2^(e+1) a y<B. K překročení proto může dojít jen při y≡−1 modz. V této třídě δ roste s y, takže stačí největší y*=B−1−(B modz); tím je dokázána odpovědní jednoprvková podmínka. Pro y<B/2 je δ<1/z, a žádné překročení nenastane. VylepšeníA=ceil(2^(65+e)/z),a'=A−B má0≤a'<B a δ'<1/z pro celý y<B; high(a'y)+y =floor(Ay/B). Následný posun e+1 tedy funguje, **pokud se při součtu zachová případný65.bit**; není to tvrzení o jednom přetékajícím64bitovém ADDU.

Původně otevřený seznam a census „189 odd divisors<1000“ jsou nyní úplně uzavřeny v `notes/recovery-pages-024-033.md`, oddíl „Answer 19: complete finite census“. Dokázaná nutná a postačující podmínka byla vyhodnocena pro všech 499 lichých z=3,…,999; divisor1 je přesný. Certifikát `results/reciprocal-divisor-census.json` obsahuje každý řádek včetně celočíselné nerovnosti a svědka, nikoli vzorek dividendů. Všech šestnáct vypsaných divisorů i počet189 souhlasí. Článek Granlund/Montgomery1994 zůstává bibliografickou výjimkou. Známá oprava26.10.2006 naδ≥0 je už v tomto tisku.

**20.** 4ADDU X,Y,Y dává5y modB, druhé4ADDU X,X,X dává25y modB. Za předpokladu bez signed overflow jde o požadovaný výsledek;2υ místo10υ podle tabulky1. Mezikrok5y se vejde, pokud se vejde25y. Odpověď souhlasí.

**21.** Přebírá se V0041–V0042: pro z≥64 je nízkých64 bitů y·2^z nula; signed nenulový součin přeteče. SRU je0, SR je0/−1 podle signu. Záporně vypadající shift count je jako unsigned obrovský kladný, nikoli posun druhým směrem.

**22.** Konkrétně y=0,z=−B/2 má kladný matematický rozdílB/2, ale jeho64bitový signed vzor je−B/2, takže BN zvolí chybný případ. Obecně všechna y≥0 proti−B/2 a y=B/2−1 proti všem z<0 mají popsaný overflow. Při stejných znaménkách se rozdíl vejde; při |y|,|z|<B/4 má |y−z|<B/2. CMP vrátí správný sign porovnání bez odečítacího overflow (V0043), následnýBN je tedy správná náhrada.

**23.** CMP dá−1,0,+1; „≤“ odpovídá právě nekladným výsledkům. BNP proto zahrne menší i rovné a vynechá větší, jak uvádí odpověď.

**24.** Pro každý i je indikátor i∈S\T roven[i∈S] AND NOT[i∈T]. Operace ANDN tak nezávisle vytvoří všech64 správných bitů. Odpověď souhlasí.

## Stav

Vlastní úlohy1–24 mají konkrétní argumenty (u3 návrh a jednotkovou konzistenci, u4 primární ověření současných názvů a zohlednění známého errata). Úplná obnova file32–33 znovu porovnala každou podčást s tímto rozsahem; census odpovědi19 je nově uzavřen samostatným certifikátem. Přeskočená bibliografie a historické připsání z3 zůstávají výslovnými výjimkami. Žádný nový nález. Další úloha25/p26/file34; následující odpovědi p95–96 se budou hodnotit v jejím rozsahu.
