# §1.3.1′ — samostatné argumenty k úlohám25–40

Zadání p.26/file34, odpovědi p.95–97/file103–105. Pomocné konstanty jsou v registrech tam, kde je tak používá odpověď; nepočítáme jejich načtení jako bezplatné, pokud bychom hodnotili celý program od libovolného počátečního stavu. Živé vstupy nesmějí být přepsány scratch registrem. Žádný nový nález.

**25.** XOR vytvoří1 právě na odlišných bitových pozicích. SADD X,X,0 počítá jedničky v tomto výsledku, tedy přesně Hammingovu vzdálenost0..64. Zdrojové operandy XOR jsou přečteny před zápisem, takže X může aliasovatY neboZ, pokud není jiný živý údaj vyžadován.

**26.** Pro jednotlivé bity je max(0,y−z)=1 jen pro y=1,z=0 a jinak0. To je přesně y AND NOT z; ANDN tedy řeší všech64 pozic současně.

**27.** Nechť v každém bytu d=max(0,y−z). Pak max(y,z)=z+d a min(y,z)=y−d. První součet je≤255 a druhý rozdíl≥0, takže při celém64bitovém ADDU/SUBU nevzniká přenos ani zápůjčka mezi byty. BDIF W,Y,Z; ADDU X,Z,W; SUBU W,Y,W proto dává osm maxim a minim, s X odlišným od ještě potřebnéhoY a se scratch W. Odpověď souhlasí v tomto běžném scratch režimu.

**28.** d=max(0,y−z) a e=max(0,z−y) nemohou být současně nenulové. Proto bytewise d OR e=d+e=|y−z|. Dva BDIF aOR provádějí přesně toto nezávisle ve všech bytech.

**29.** Komplement bytu je255−y. BDIF dává max(0,255−y−z) a další komplement255−max(0,255−y−z)=min(255,y+z). Tři instrukce tak přesně saturují součet bez mezibytových přenosů. Známé erratum29.3.2023 pouze převede scratch$0 na výstup$X, aritmetický argument nezmění; není náš nález.

**30.** XOR s2020202020202020 udělá v každém bytu a=0 právě pro ASCIIspace20, jinak a≥1. BDIF s0101010101010101 spočítá max(0,1−a), tedy právě1 pro shodu a0 jinak. V každém shodném bytu je tak jeden nastavený bit; SADD s0 vrátí počet mezer. Tříinstrukční řešení funguje dokonce pro libovolné8bitové byty, nejen ASCII.

**31.** Matice konstanta0101010101010101 má každý řádek00000001. Výsledek MXOR X,const,chars má proto v bytu i paritu osmi bitů chars_i v posledním bitu, ostatní bity0. SADD s0 přesně sečte počet bytů s lichou paritou. Důvod je xorová redukce řádku matice, ne celočíselný součet s přenosy.

**32.** Obecné tvrzení je false bez komutativity•. Pro1×1 matice A=[1],B=[2] a a•b=a−b je C=[−1], ale B^T•A^T=[1]. Pokud• komutuje, (A○•B)^T_ji je redukce členů A_ik•B_kj a(B^T○•A^T)_ji redukce stejných členů v témže pořadí k, jen s prohozenými dvěma činiteli. Stačí tedy komutativita•;○ nemusí být komutativní, pouze asociativní podle definice. Pro univerzální platnost je komutativita• i nutná, jak ukáže obecný1×1 případ. Odpověď uvádí správnou podmínku.

**33.** Mask01,80,40,20,10,08,04,02 vybere postupně byty8,1,2,3,4,5,6,7. Jediný MOR/MXOR tak dává cyclic rotate right8. Je-li tato maska již v registru, jedna instrukce je minimální: nulová posloupnost je identita, ale požadovaná permutace některé vstupy mění. **Partial je bezpodmínečná optimalita bez určených počátečních konstant**; odpověď masku předpokládá dostupnou. Při účtování jejího načtení nelze jednoduše tvrdit, že celý program má jednu instrukci. Nejde o potvrzenou chybu textu.

**34.** První dvě masky vyberou řádky (0,1,0,2,0,3,0,4) a(0,5,0,6,0,7,0,8), kde0 znamená nulový byte. Dostaneme tedy přesně osm wydes00ci. Pro opačný směr napišme X=(h1,l1,…,h4,l4),Y=(h5,l5,…,h8,l8). První MOR na X s4020100804020180 dá t=(l1,h2,l2,h3,l3,h4,l4,h1). Maska rM=00ff00ff00ff00ff dává prvním MUX (h5,h2,h6,h3,h7,h4,h8,h1), takže BNZ správně odmítne kterýkoli nenulový high byte. Druhý MUX dává(l1,l5,l2,l6,l3,l7,l4,l8). Poslední MOR s8020080240100401 řadí1,3,5,7,2,4,6,8, a vrátí(l1,…,l8). Při původním ASCII vstupu jsou li<128. Dodatečný BadCase test ověřuje8bitovou reprezentovatelnost, jak výslovně říká odpověď, nikoli nezávisle7bitovou platnost libovolného vstupu.

**35.** OznačmeR antidiagonální permutační matici z(14). První MOR X,Y,Z dá m(X)=R·m(Y), tj. obrátí pořadí bytů. Druhý MOR X,Z,X dá(R·m(Y))·R, tedy obrátí také pořadí bitů v každém bytu. Pozice(i,j) přejde na(9−i,9−j), přesně obrácení všech64 bitů. R musí zůstat dostupná pro obě instrukce.

**36.** XOR vytvoří byte d_i=0 iff y_i=z_i. Matice m(−1) má všechny prvky1; MOR s ní vrací v bytu i hodnotu ff iff některý bit d_i je1, jinak00. S BDIF místoXOR je d_i nenulové iff y_i>z_i, takže dodatečná poznámka odpovědi je také správná. AND s8040201008040201 nechá jeden diagonální bit v každém označeném bytu; MOR sff v operandovém poliZ zredukuje tyto řádky ORem do posledního bytu a vytvoří požadované8bitové kódování pozic.

**37 — GF(256).** Obecné kritérium primitivity a reciproké zachování přebírám z `workstreams/vol2/notes/primitive-polynomials.md`, oddíly „Kritérium na str.30“ a „Tabulka1“. Staré censy nebyly opakovány. Pro konkrétní p=x^8+x^6+x^5+x^4+1 (bitová maska171hex) byl jednou spuštěn krátký přesný certifikát `nice -n 15 python3 workstreams/vol1-fasc1/verify_field_examples.py`: modulo p vyšlo x^255=1,x^85=db,x^51=4d,x^15=c1. Proto má x plný řád255=3·5·17 a podle převzatého kritéria je podílový okruh tělesem, bez potřeby druhého testu ireducibility.

Zobrazená maticeT je companion matrix: e1T^j=e_(j+1) pro0≤j<8, a e1T^8=e1+e5+e6+e7. Tedy p(T)=0 a žádný polynom stupně<8 T neanuluje (jeho první řádek je vektor koeficientů). Algebra polynomů vT je proto izomorfní F2[x]/(p), má256 prvků, XOR je součet a MXOR součin; opačné pořadí matic v instrukci nevadí, protože polynomy v jednéT komutují. T² má prvních sedm řádků následující řádkyT a poslední40 XOR04 XOR02 XOR01=47, tedy2010080402018e47, přesně odpověď.

Stejný cílený certifikát ověřil **jen šest dalších výslovně uvedených companion polynomů**, bez hledání: stupně2..7 mají masky7,d,19,29,61,c1 a plné řády3,7,15,31,63,127. Všechny mocniny a prvočinitelé jsou v results/field37-power-certificates.json. Pro menší k se pracuje s k×k blokem; při vložení do8×8 má jednotka podobu identity tohoto bloku, nikoli celé8×8 identity. S tímto přirozeným embeddingem vzniknou přesně tělesa2^k prvků, jak uvádí odpověď.

Pro16×16 blokové matice potřebuje každý ze4 výstupních bloků dva8×8 součiny a jeden XOR, celkem8MXOR+4XOR. Pro kvadratické tělesové rozšíření zvolímeθ²=θ+c nadK=GF(256), kde trace(c)=1. Takové c existuje: trace je nenulový polynom stupně128<256, hodnoty má veF2, tedy je surjektivní; obraz t²+t je přesně její128prvkové jádro. Proto u²+u+c nemá kořen a je ireducibilní. Produkt(a+bθ)(d+eθ) má koeficienty ad+cbe a ae+bd+be. Vyžaduje5 násobení vK (ad,be,cbe,ae,bd) a3 součty, tedy5MXOR+3XOR při reprezentaci koeficientů maticemi. Tím je i rozšířený počet instrukcí v odpovědi odvozen, ne pouze převzat.

**38.** SR o56 vybere první byte aktuálního slova se znaménkem. ADD jej přidá do součtu, SLU o8 odstraní tento byte a zbytek posune. Invariant po j průchodech: sum je součet prvních j původních signed bytů a$0 obsahuje zbývající byty následované nulami. Nejpozději po8 průchodech je$0=0; časné zastavení vynechá jen samé zbývající nulové byty. Součet je v−1024..1016, nepřeteče. $2 je poslední zpracovaný, tj. pravý nenulový původní byte; pro původní0 proběhne jeden nulový průchod a$2=0. NahrazeníSR zaSRU změní interpretaci na unsigned aSL místoSLU může při posunu přetéct. Všechny závěry odpovědi souhlasí.

**39.** Nechť p=P($0<0); dvojice časů jsou pro negative/nonnegative. Přímým součtem nákladů větví z tabulky1 vzniká(a)(3,2) proti2, (b)(4,3) proti2, (c)(4,3) proti3, (d)(1,4) proti2, (e)(2,5) proti2, (f)(2,5) proti3, vše vυ. Pro(d) je průměr4−3p<2 iff p>2/3; pro(f)5−3p<3 iff p>2/3. V(b,e) conditional nikdy není horší (v e,p=1 je shoda, nikoli striktní zlepšení). Ve(a,c) conditional rovněž dominuje. PoužitíADD místoADDU může v nevybraném spekulativně spočítaném výrazu vyvolatoverflow, což ruší sémantickou ekvivalenci, jak odpověď uvádí. Pomocné registry jsou zde považovány za scratch, stejně jako v zadání.

**40.** GO uloží do@ cílovou byte adresuA, ale následující instrukce se načte jako M4[A], tedy z4floor(A/4); samotné nízké bity@ se tím nemění. ProA=101hex se načte tetra100hex, zatímco@+4=105hex a PUSHJ uloží rJ=105hex. GETA s nulovým relativním offsetem vrátí@=101hex. Relativní násobky4 zachovávají low2 bity, takže je lze použít jako skrytý tag, ačkoli assembler obvykle počítá se zarovnanou adresou. Odpověď souhlasí s definicí paměti a relativních skoků.

## Stav

Úlohy25–32 a34–40 mají konkrétní argument. U33 je ověřena jednooperační konstrukce a její minimum s předem dostupnou maskou; neurčené náklady na získání konstanty zůstávají partial optimalitou. Bibliografické připsání externím autorům nebylo plošně ověřováno. Další úloha41/p27/file35.
