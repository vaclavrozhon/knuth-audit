# §1.3.2′ — první sada úloh1–16

Zadání p.43–45/file51–53; odpovědi p.99–101/file107–109. Úloha3 má přesnouPUSHJ/POPvazbu uzavřenou veV0124 a úplný obnovený důkaz v recovery-pages-049-051.md;14 má nyní úplný důkaz v exercises-1.3.2-009-014-recovery.md;16 je rozsáhlýotevřenýprojekt. Dalšíbibliografické/číslenépoznámky odpovědí jsou výslovněodděleny.

**1.** (a)4Bnařádku29 volí nejbližšípředchozí4H, tedyřádek24. (b)Přejmenování24na2H nestačí opravitjen29: forward2Fna23 bypakpřešlo na24 místo38, takžeukončenígenerování seporuší; backward2Bna31 bymířilo24 místo21, takže byse právězjištěnéprime neuložilo. Odpověďsprávněuvádíobaodkazy.

**2.** Předprvním9H je9B=0 podlepravidla. Po m-tém`9H IS 9B+1` má novádefinicehodnotu m indukcí z předchozí m−1. Každénásledné9Btedy nese počet jižprovedenýchdefiničníchřádků; nepočítá běhovéprůchodyprogramu.

**3 — sorting invariant, callinterface resolved.** VArgjeX0+1<<3 podleprecedence X0+(1<<3)=X0+8, aN<<3=800. PřiúspěšnémFread se tedy načte100octabytesX[1..100]. Caller$0 drží8n, SRvytvoříparametrn; poMaximum má podleuvedeného rozhraní$1=max a$2=j. LDO$3zachovástaréX[n]; dvěSTOprohodíX[n] aX[j]. To zachovápermutaci aumístínejvětšíprefixovýprvek najehopravé místo. Invariantvnějšíhosmyčky: jižhotovýsuffix jevzestupný akaždýjehoprvek≥všechzbývajících. Po100průchodech je tedycelývstup vzestupněsorted aFwritevrátístejných800bytů. **PřesnýPUSHJ/POPpřenosm,j aobnovenícaller$0 je uzavřen veV0124**; recovery-pages-049-051.md rozepisuje všechny větve swapu, meze i adresy. Krátké/selhanéI/O neníimplicitněpovažováno zaúspěšný100prvkovývstup.

**4.** Konstanty se redukujímod2^64, tj.ponecháse16nejnižšíchhexčíslic. Z112233445566778899takzůstane2233445566778899. Odstraněnýhorníbyte11je násobek2^64.

**5.** Stringexpansion dáseznam3+'p','i','l','l','s'+6. ASCIIp112+3=115=s, i,l,l zůstanou a s115+6=121=y. VýslednéBYTE je „silly“, nikolineplatnésčítáníceléhořetězce.

**6.** Pro@=100hex vyhodnotíjednaEXPRlist`TETRA @,@` oběhodnotypři stejnémcurrentlocation, tedydvě00000100. Dvěinstrukcevyhodnotídruhé@až poposunuprvnío4 a uloží00000104. Tímje univerzálnítvrzení vyvráceno. Alignmentna4 sepředoběmivariantamishoduje; rozdílemjen okamžikvyhodnoceníEXPR.

**7.** RelativníoperandGETA se kódujevtetrabytech, nízkédvabitycílejsouignorovány. Rozdíl@+1−@má po dělení4stejnýceločíselnýoffset0 jako@−@, protooběinstrukcevrátí@. NenítoinstrukceADDaddress1.

**8.** Pišp=16q+r,0≤r<16. (p+15)&−16dá16qpror=0a16(q+1)jinak,tedyzvýšení0nebo16−r. Alternativa−p/16·(−16),sunsignedmodulárnínegací, dávástejně: pro r>0 je floor((2^64−p)/16)=2^60−q−1, po násobení−16a redukcidostaneme16(q+1); pro r=0vyjdep. Posunovávarianta−(−p>>4<<4) jetážaritmetika. Při přetečeníadresovéhoprostoru se výsledek chápe modulo2^64; tvrzeníobyčejnémzvýšenípředpokládáexistencinásledujícíadresyvprostoru.

**9.** ZměnitL500→600 a titleFive→Six. InvariantV0089zůstává sjj=2(j−600), ptop=D+1200,j0=−1198; výstupníinkrement je120a50řádkůsenahradí60, stále10sloupců. Poslednítestje118a vejdese doimmediatebyte. V0086binomickédůkazydávajíπ(8192)≥630, takžei600.prime<8192a čtyřicifryiwydepostačí. Přesnéodpovědníúdaje1230/6542 jsou nyní uzavřeny v exercises-1.3.2-009-014-recovery.md a novém malém incremental certifikátu; staré síto se neopakovalo.

**10 — ručnísestavení.** Programzačínána100. Prořádky19–33jsouadresy100..138 po4a numericcodes vpořadí:
`e3fe0003 c1fbf700 a6fef8fb e7fb0002 42fb0013 e7fe0002 c1faf700 86f9f8fa 1cfd fef9 fefc0006 43fcfffb 30fffdf9 4dfffff6 e7fa0002 f1fffff9`.
Mezera u `1cfd fef9` jejenhexseskupení, jednaTETRA. ForwardBZna110máoffset(15c−110)/4=19=13hex. BackwardBZna128cíl114má−5;BNPna130cíl108má−10;JMPna138cíl11cmá−7. Ostatnífieldyjsouregistry254..249,ptop248,j0247 adříveověřenéopcodes.

Na13czačínáTitle. Jeho25znakůplusLF0a aNUL00 a třimezery+NUL dávají tetras `46697273 74204669 76652048 756e6472 65642050 72696d65 730a0020 20200000` na13c..158; poslednínulovýpaddingdoplníalignmentna15c. Prořádky38–62 od15c pakvychází:
`23fff600 00000701 35fa0002 20fafaf7 23fff61b 00000701 86f9f8fa aff5f800 23fff804 1df9f90a fefc0006 e7fc0030 a3fcff00 25ffff01 5bf9fffb 23fff800 00000701 e7fa0064 51fafff4 23fff619 00000701 31fffa62 5bffffed 00000000`.
ZdeGREGna45nepřidávácode;PTRpatternjereg245. OffsetyTitle0,Blanks27,NewLn25bylyodvozenyV0092;PBNZna194míří180(−5),PBNna1a4míří174(−12),PBNZna1b4míří168(−19). Výpisodpovědi99mátytéžkódy, poslednínulovýHaltneuvádímezinonzerodata. VdatovémsegmentujejenPRIME1=0002 nenulovépředběhem. rG=245=f5, $248=D+1000=20000000000003e8,$247=−998=fffffffffffffc1a,$246=13c,$245=2030303030000000. Všechnytytohodnotysouhlasí; neproběhlo spuštěníassembleru.

**11.** (a) Je-li n=ab složené,a,b>1, nemohou býtoba>sqrt(n),jinakab>n. Menšíje tedy v(1,sqrt(n)]; jeho prvočíselnýděliteljestejněmalý. (b) V0086jižsamostatnědokazujeP7z n<p(p+1)<(p+1)^2aexistenciuloženéhodivisora provšech500primes bezcensus. OdpověďpoužíváBertrandůvpostulát: nextprime<2p≤p²+p, cožje správná dostatečnámez. Jejímatematickároleje oddělena odnašeho konečnéhodůkazu pro500; opakováníobouproofůnenípotřeba.

**12.** PřesunTitle/NewLn/BlankszatextovýBUFdoDataSegmentučiníjejichoffsetyodptoprovny8,33,35, vše<256. VšechnyLDAmohoustálepoužítjedinouADDUimmediateaextraGREGodpadne. Alternativně adresykrátkéhoprogramu<65536umožníSETLsesame1υcost. UGETAjepotřeba4alignment;protoseseparátníTitlevčetněLF0ukončí,pakLOC(@+3)&−4zarovnáNewLn,aznovuBlanks. TytoposunynepřidávajíběhovéinstrukceaponechajíjednotlivéFputsřetězcesprávněukončené.

**13.** BYTE→WYDEměníelementna2byty;Fputs→Fputwsvyjádřístejnou změnujednotky. Decimalremainder0..9sepřičteke0660auložíSTWU,tedykód0660..0669. JednotkovýpointerzačínáBUF+8aklesápo2. Inicializačníocta0020066006600660obsahujespaceatřivyššízerodigits;unitswyde naBUF+8sepřepíšepřikaždémprvním průchodu, takže nemusíbýtpřednastavený. TerminátornaBUF+10zůstávánulovýzpočátečnípaměti; žádnájinádata zatímBUFv tomto programu nejsou. Tímvzniknespace+4wyde digits+0, přesněpožadovanáconversion. Samotný překladarabskéhotitulku, historicképojmenování„authentic“nebylynezávisleověřeny. Unicode pořadí konkrétních znaků je nyní přesně doloženo podle UAX9 a všech40 numerických skupin originálu v recovery-pages-052-053-107-109.md.

**14 — fully resolved.** Úplný funkční, rounding a profilový důkaz každé vytištěné varianty je v exercises-1.3.2-009-014-recovery.md. Uložený malý nový výpočet potvrzuje9597/9357 testů,426192υ−59μ a dodatečných38169υ, s konkrétní short-float implementací a přesnými μ/υ prahy. Žádný MMIX ani starý profiler se nespouštěl.

**15.** NEG1,1,75nastaví−74. Outerloopmá$1 postupně−74..−1;v něm$3=$1+75=1..74. Innerloopzapíšetoliko spaces a pakjedno'*'. $2rostepo1a sousednívýstupníznakyse tedynepřekrývají. Všechnyjsounenulové; prvnínenapsanýbytezůstane0zpočátečníDataSegmentpaměti aFputsvypíšeprávětentoprefix. Celkovádélka∑_(k=1)^74(k+1)=74·75/2+74=2849=binom(76,2)−1. Žádnýnewline seexplicitněnetiskne; vizuální„OPart“závisí nazobrazení/wrappingu. Programnebylspuštěn, v souladu sezadáním.

**16 — open research/project.** Návrh aimplementacePL/MMIXvliterateprogrammingstylujevelkýotevřenýprojekt rating46; žádnárealizacezde nevznikla. PůvodníWirthůvPL/360článek aniLiterateProgramming1992nebylyv rámci tohotoúkoludohledány.

Aktuální stav této sady:15úloh samostatnědoloženo,16openproject; přesné lingvistické výjimky úlohy13 jsou uvedeny samostatně. Vedlejšínumerické/bibliograficképoznámkyu9a13jsouoddělené. Dalšíkurzorúloha17,p46/file54.
