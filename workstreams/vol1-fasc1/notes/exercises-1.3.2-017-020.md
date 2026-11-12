# §1.3.2′ — úlohy17–20

Zadání p.46/file54, odpovědi p.101–104/file109–112. Nový nález žádný. Statická validita/privilegované podmínky a rozsáhlé průměrné časy se nepovyšují na dokázané výsledky.

**17 — statický tabulkový test ověřen, úplná platnost partial.** Z neprivilegované nezáporné vstupní adresy LDTU získá32bitovouinstrukci. `SR tetra,22` dává8bitOPposunutýo2 a dva nízkébityzX; následnýLDTzarovná na4 a přesně vybereTETRA[OP]. LDT použije sign extension: tabulky a,b,d,e,f,g,h začínajíff, proto jsouzáporné;PUTtabulkac=001f00ffjekladná aLDVTSpoložky0jsounula. BDIFpo jednotlivýchbytech dávánenulovývýsledekprávěkdyž některýinstrukčníbytepřekročísvémaximum. Vysoké64bitovépaddingbytes dávají0, protože instructionmáhorní0.

PBNPmaxXYZukončí všechny non-PUTcases. ULDVTSproti0zůstane vBDIFnenulovýOP98/99, takže jevždyodmítnut. UPUT seANDNML#ff00vymažejenOPbytevevýsledku; zbývátestX≤31,Y=0,Zlibovolné. MORimmediate4vybereXbyte ztetra;CMPs18 aCSPvynulujeX,je-li>18. ODIFs7potomvrátí0právěproX≤7nebo19..31. To je přesnýPUpovolenýstatickýrozsah. OstatnítabulkydokládajíY≤4uFProundmode, všechnyoperandynulauRESUME, YZ0uSAVE,XY0uUNSAVE,XY0aZ≤3uSYNC,Y0aZ≤31uGET. Generickýmaxa dovolí všeostatní.

Tento důkaz ověřuje zapsanou statickoutabulkovoumetodu. **Odpověďsama výslovněpřipouští,žeSAVE $0,0 neodmítne,ačkoli$0nemůžebýtglobal, a nekontroluje skokdonegativníadresy.** Požadavek „všechnyrestrikce“ má tedy širší možnéčtenínežtestovanátabulka; úplnouvalidaci tohotozadáníponechávám **partial**. Tato otevřeněuvedenáomezeníneoznačuji zanovýneohlášenýnález. Globálníoptimálnosttabulkyproti všemprogramům rovněžnenídokázána.

**18 — řešení1.** Vstupje9×8signedbytearraynaA+8i+j;počátečníij72a a10=A+8načtoua98. Přirow-scanuodcol8dolůjekandidátxminimumzatímpřečtenýchhodnot a seznamA+1..A+kusuchovávávšechnycolumnindices,kdeje totominimum. Menšíyresetujeseznam,rovnéypřidáindex,většíypřeskočí. SUBx−yleží−255..255,tedynepřeteče. Poukončenířádkujeij=8(i−1), a listobsahuje všechnyrow minima,nikolijenprvní.

ColMaxprokaždýlistedcolumnc procházírow9..1naadresáchA+8r+c aodmítne,pokudněkteráhodnota>x. Přiúspěchuxje rowminimumi columnmaximuma výslednáadresaA+8+8(i−1)+c=A+8i+cjesprávnýsaddle. Kdyžvšechnycolumnsodmítneme,jde senadalšírowi−1;pořádku1jeij0avrátíse0. Tiesjsou zachoványseznamem, a pomocných8bytůA+1..8nepřekrývávstupzačínajícíA+9. Programmá tedy správnoufinal$0 hodnotu;POP1seberejako standardnínávratovýkontraktprojedinhodnotu.

**18 — minimax theorem.** Pro R_i=min_j aij aC_j=max_i aij vždyR_i≤aij≤C_j;proto maxR≤minC. Je-li(i0,j0)saddlehodnotys, pakR_i≤a_i,j0≤sprokaždéi, as≤a_i0,j≤C_jprokaždéj, takžeR_i0=maxR=s=minC=C_j0. OpačněR_i0=C_j0svírá a_i0,j0mezi stejnýmičíslýa dárovnost. Nesaddle jeekvivalentníostrémeze maxR<minC,tedy všechnaRjsoumenšínežvšechnaC.

**18 — řešení2.** Phase1procolumnjnejprvenačterow9přesa20aij=j+56, pakcykluspřesa10row8..1;maxxjezčásti−128..127. Poukončeníij=j−8, takžeSTBnaA+8+ij=A+j uložíC_jmimoarray. Po8sloupcíchjez=minC;initial1000jepřísněvětšínežvšechna data. Phase2odrow9krow1odmítneřádekhned,kdyžnajde aij<z. Pokudřádekprojdecelý, R_i≥z;minimaxnerovnostdáváR_i≤z,tedysaddleexistuje. ProkaždýsloupecsC_j=zpotomz≤aij≤C_j=z, takžeprogramnejménějednouzapíšeanssprávnýmindexem, ačkolijejnapočátku neinicializoval. Kontrola hlavičkovéhoC_jje proto podstatná. Failedrowmůže zanechatstaréans, alepassingrowjej nutněpřepíše;pokudneprojdežádnýřádek,explicitníSETans0vynulujevýsledek. Takje uzavřen i tento snadnopřehlédnutelnýstavovýpřípad.

VylepšenípomocíminimálníchCsloupců smí vyřadit každýrowi,kterývněkterémtakovémcolumnunedosahujeC_j=z. Podlenutnépodmínkyteorému to nemůževyřaditsaddle. Při distinctentriesjedefinujícícolumnmaximumjednoznačné,tedyzůstane nejvýšejedenrow; pro tiesjejichpočetnemusíbýt1.

**18 — pevný all-zero profil ověřen.** Řešení1čte8rowvalues,zapíše8listpositions, načte1columnindex a9columnvalues:26μ. Inicializace/arithmetic/branchprofileprvnífázečiní116υ, výběrcolumnu2υ, jeho9řádků65υa finálníADD/LDA/POP5υ,celkem188υ. Řešení2vPhase1čte9a zapisuje1bytepercolumn,tedy80μ;passingrowPhase2čte8values+8Cheaders,dalších16μ. Phase1má396υvčetněinitialSETs, Phase2initialization3υ,8rowpositions114υafinalLDA/POP4υ,celkem517υ. Tím jsouoba uvedenéall-zerocosts26μ+188υa96μ+517υdoloženy ručnímprofilem, bezběhů.

Trialaverages147μ+863υ a95μ+510υpro náhodnádata−2..2, a bibliografické tvrzeníO(m+n)matrixprobes/O(m logn)auxiliarywork zcitovanéhoAMM1991 **zůstávajíneověřenévedlejšítvrzení**, nikolipřevzatýdůkaz našichdvouprogramů.

**19(a).** Dva saddlesmajístejnouhodnotu:minrowi≤intersection(i,l)≤maxcolumnl aobrácenědají oběnerovnosti mezi jejichhodnotami. Při72distinctentriesje tedynejvýšejedensaddle. Prokonkrétníbuňkuje vjejímrow∪column m+n−1elementů;vybranábuňkamusíbýt většínežm−1columnentries a menšínežn−1rowentries. Vuniformnímrelativnímpořadíjsou příznivé(m−1)!(n−1)!permutací z(m+n−1)!, tedy pravděpodobnostmnkráttato, m!n!/(m+n−1)!. Pro m9,n8je9/binom(16,8)=9/12870=1/1430; algebraickyje totéž(m+n)/binom(m+n,m)jako vodpovědi.

**19(b).** Binarysaddle0existujeprávěkdyžexistujecelánulovácolumn; saddle1právěkdyžexistujecelájedničkovárow. Tytojevysenavzájemvylučují, protožejejichintersectionby muselabýtzároveň0a1. Rowsjsounezávisléa columnsseparátnětaké, takžeP=2−(1−2^−n)^m−(1−2^−m)^n. Prom9,n8dávákrátkáexactfractionkontrola `nice15` výsledku924744796234036231/18446744073709551616;reciprocal≈19.94792958souhlasís„about1in19.9“. Vizresults/saddle19-probability.json;neproběhla enumerace2^72matic. Aproximacen2^−m+m2^−njsou prvníunionterms;možnédvojitépočítáníuvnitřrodinyjeboundedbinom(n,2)2^−2m+binom(m,2)2^−2n. Tímje jejísmysljako approximationdoložen,neexactformula.

**20 — partial.** Výšejsouuzavřenyalgoritmy,pevnéprofilynulovématicea pravděpodobnostisaddle;nejsouuzavřeny očekávané počtyscanů a instrukcí podoběmarandommodely. AsymptotickévýrazyodpovědisodkazemHofri/Jacquet,Algorithmica22(1998),516–528 jsemneodvozoval ani tentočláneknezískal. Ze samotných tvrzenýchkoeficientů5mnvs6mn by propevnéμ/υasymptotickyvycházelvýhodnějšíSolution2,ale tento podmíněnýpostřehnenídůkazvzorců ani odpověďpronáhodné9×8binarymatice. **Úloha20zůstávápartialbezbruteforce.**

Stav:17a20partial;18a19majíindividuálníargumenty,vedlejšíneověřenébenchmarky/bibliografieodděleně. Dalšíkurzor21,p47/file55 (Farey).


Aktualizace recovery6.11.: celý nový maskový důkaz je v exercises-1.3.2-017-recovery.md; stránky54/110–112 a obě rutiny v recovery-pages-054-110-112.md. Autorský Hofri–Jacquet report byl mezitím získán a přečten. Druhá vytištěná průměrná formule je vyvrácena přesným profilem a obecnou dolní mezí v MMIX-C0018-saddlepoint-average-cost.md. Staré tvrzení, že se průměrné vzorce pouze nezkoušely, už nepopisuje tento nový stav; úloha20 nadále zůstávápartial ve zbývajícím rozsahu.


Následné doplnění20: oba distinct očekávané časy jsou nyní plně odvozeny v exercises-1.3.2-020-distinct-recovery.md, oba binární časy v exercises-1.3.2-020-binary-recovery.md. Obě vytištěné formule jsou chybné; C0018 byl rozšířen o první konstantu2υ. Výše uvedené starší otevřené očekávání obou programů je tím vyřešeno; zbývá konkrétní třetí varianta a její srovnatelné náklady.


Konečné doplnění20: exercises-1.3.2-020-third-recovery.md nyní dává úplný obecný MMIX kandidátní program, všechny větve a náklady, exact binary očekávání a rigorózní distinct9×8 srovnání. Třetí metoda je tím konkrétně realizována; v obou modelech má menší oba očekávané koeficienty než Solution2, a ta než Solution1. Úloha20 je argument_recorded; dřívější third-variant partial je vyřešeno. Globální optimum ani historické trial běhy se netvrdí.
