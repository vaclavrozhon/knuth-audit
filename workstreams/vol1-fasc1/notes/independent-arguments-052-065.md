# MMIX — samostatné argumenty p. 52–65

Čtení originálu bylo již dokončeno. Zde jsou individuální argumenty,
nikoli nové označení pouhého čtení za důkaz. U deklarovaných instrukčních
pravidel se ověřují jejich důsledky; implementační sémantika fyzického
zásobníku se nepovažuje za automaticky uzavřenou.

- **V0108, p. 52 — Max100.** Převzatý invariant V0078 platí při pevném
  n=100: prochází se 100,…,1, m je maximum již navštíveného suffixu a j
  největší index s tímto maximem. Při shodě se j nemění. 800 je přesná
  byteová pozice X[100]. Návrat j/m je doložen níže ve V0124.
- **V0109, p. 53 — GO varianta.** GO uloží adresu následující instrukce
  do $0 a přejde na cíl. Koncové GO použije starou hodnotu $0 jako cíl
  dřív, než zapíše link do kk. Globální m/j tudíž zůstanou výsledky.
  GREG @ u vstupu poskytuje adresu v jednom dostupném bázi; bez takové
  dostupné báze stačí GETA a GO. Nejde o tvrzení, že dvoukrokový zápis
  je nutný za každého jiného možného rozmístění registrů.
- **V0110, p. 53 — délka kódu.** Původní mk proti novému m+k+1 dává
  `mk−m−k−1=(m−1)(k−1)−2`. Pro k=1 či m=1 je úspora záporná;
  pro k=2 je m−3>0 právě při m>3. Předpoklady jednooperační vazby
  jsou v textu výslovné.
- **V0111, p. 54 — čas vazby.** Tabulka 1 dává PUSHJ 1υ, POP 3υ,
  GO 3υ. T volání přidá 4Tυ, respektive 6Tυ. Toto není odhad cache
  missů nebo libovolného skutečného hardware; text sám omezení uvádí.
- **V0112, p. 54 — argument v instrukčním proudu.** GO ukládá adresu
  následující TETRA n. LDT načte signed n, SL násobí osmi a GO s offsetem
  4 přeskočí právě jedno datové tetrabyte. Podmínkou je platné kladné n
  a adresovatelná tabulka; vložené data se neprovedou jako instrukce.
- **V0113, p. 54 — argument v registru.** SET $1,n přenese hodnotu,
  další SL již nepotřebuje LDT. GO s offsetem 0 se vrací hned za call.
  Překlad stejného Max invariantu je přímý; dynamické n nemění instrukce.
- **V0114, p. 55 — c instrukcí volání.** Pro tělo k a pevnou návratovou
  režii r je úspora `mk−(mc+k+r)=(m−1)(k−c)−(c+r)`. „constant“
  v (8) je tedy nezávislá na počtu míst m, při pevném c a r.
- **V0115, p. 55 — uložení kk/xk.** STO uloží dvě původní octabytes
  a dvě LDO je přesně obnoví; finální GO $0,$0,0 potřebuje hodnotu $0
  před zápisem linku. Rutina potřebuje dvě odlišná dočasná místa mimo
  tabulku. Bez rekurze je nepřepisuje jiný aktivní rámec; rekurze je
  správně řešena až následným zásobníkem.
- **V0116, p. 56 — více vstupů.** Max100 nastaví n=100 a propadne do
  obecného vstupu; Max50 nastaví 50 a skočí na tentýž vstup. Zbytek
  invariantu není na zvoleném vstupu závislý.
- **V0117, p. 56 — dva výstupy.** BNP m pokryje m≤0. Jinak CMP m,b
  s BN pokryje m<b; zbývají právě kladná m≥b. GO s offsetem 0 či 4
  proto rozliší přesně uvedené množiny, i když b≤0 (pak je druhá prázdná).
- **V0118, p. 57 — opakovaný GO link.** V explicitním schématu (13)
  opětovné GO $0,A přepíše původní návrat do Main. Bez jiného uložení
  tohoto linku ho kód neobnoví. Nejde o obecnou nemožnost rekurze pomocí GO;
  hned další schéma přidává právě potřebnou paměť.
- **V0119, p. 57 — zásobník návratů.** STO na sp a sp+=8 vytvoří
  rámec s linkem. Indukčně každé vnořené volání použije další octabyte
  a při návratu obnoví původní sp. SUB/LDO tedy vrátí právě link tohoto
  rámce. List bez dalšího volání může nechat link v $0, pokud ho sám
  nepoužije jako pracovní registr. Paměť musí být dostatečná a disjunktní.
- **V0120, p. 58 — rámec 22 octabytes.** Offset 0 je starý fp, 8 návrat,
  offsety 16,24,…,168 jsou přesně 20 míst `8k+8`. Posun sp o 176
  rezervuje celý rámec bez přesahu. Epilog nejdřív získá link přes současný
  fp, obnoví sp=fp a teprve z něho načte starý fp; po návratu jsou oba
  ukazatele jako při vstupu. Totéž platí induktivně při rekurzi.
- **V0121, p. 58 — třídy registrů.** Intervaly [0,L),[L,G),[G,256)
  jsou disjunktní a úplné při 0≤L≤G≤255. Zápis do marginal X<G rozšíří
  lokální prefix přes X a mezilehlé nové pozice vynuluje. Při L=8 a
  G>20 čte ADD $10,$20,5 nulové $20; výsledek $10=5, nové $8=$9=0,
  L=11. Tvrzení, že $20 zůstane marginal, předpokládá právě G>20;
  v této architektuře G≥32 tento předpoklad zaručuje.
- **V0122, p. 59 — PUSHJ/PUSHGO.** Logický základ aktuálního rámce
  označme O a počet lokálních registrů L. Pro X<G se případný marginal
  X nejdřív alokuje; pak je do S[O+X] vložen odkaz X a nový základ je
  O+X+1. Nové lokály jsou staré X+1,…,L−1. Pro X≥G se přidá odkaz L
  na konec a nový rámec má L'=0. Přesný odkaz X/L je výslovně vidět
  v kódu p. 86, řádky 263–276; tvrzení „stack unchanged“ v úvodu p. 59
  se týká zachovaných hodnot a přeznačení, nikoli ponechání hodnoty
  rezervované výsledkové buňky. PUSHJ nastaví rJ=@+4; PUSHGO má stejný
  rámec a jiný výpočet cílové adresy. Tím je uzavřena logická část V0066.
- **V0123, p. 59 — POP a permutace výsledků.** Je-li v uloženém odkazu
  p, pak `L_new=min(G,p+min(X,L+1))`. Pro 0<X≤L je hlavní výsledek
  staré $(X−1), pro X>L je 0. Je vložen na místo odkazu, pokud toto
  místo zůstává lokální; ostatní pomocné výsledky se v zásobníku fyzicky
  neposunou. X=0 odkaz i celý aktuální rámec zahodí. Tento předpis je
  přímo rozepsán v odpovědi §1.4.3′–10, p. 119–120; zde jsou převzaty
  jen logické indexy, ne znovu prokázaný cache/ring mechanismus.
  Pro p=5 dávají X=0,1,2,10 přesně L=5,6,7,15 a umístění uvedená
  v textu. X=4 ponechá tři původní argumenty v $6,$7,$8. Při překročení
  G se přebytek zahodí; v knižních příkladech G≥32 oříznutí nenastává.
- **V0124, p. 60 — adresy a návrat Max.** POP vrací na rJ+4YZ, tedy
  pro YZ=0,1 na dvě sousední tetrabytes za call. PUSHJ $R chrání $0…$(R−1),
  argument z $(R+1) se stane $0 a POP 2 vrátí původní callee $1=m do $R,
  callee $0=j do $(R+1). Tím je uzavřena konkrétní závislost V0082
  i §1.3.2′–3: tam m/j mají přesně požadované caller pozice. Program (16)
  má stejné tělo i počet instrukcí jako (12), pouze 3υ GO nahrazuje
  1υ PUSHJ a návrat zůstává 3υ. Známá oprava BNZ→BN z 2005 je v této
  sazbě již zapracována.
- **V0125, p. 61 — uložení rJ.** GET do lokálního retadd zachová návrat
  přes další PUSHJ, pokud caller tento lokál zahrne mezi chráněné
  registry. PUT před POP obnoví správný link. Je-li retadd≥X, nebude
  tento pracovní lokál součástí vrácených X výsledků. Nejde o automatické
  zachování všech speciálních registrů libovolným volaným kódem.
- **V0126, p. 61 — hranice registrů a paměť.** Registry nemají obecné
  nepřímé čtení podle vypočteného čísla; běžné lokální pole proto vyžaduje
  adresovatelnou paměť. Smíšený rámec s fp/sp a scalars v lokálních
  registrech oba invarianty zachovává. **Partial:** přesné spilling,
  ring kapacity a SAVE/UNSAVE inverse patří k dosud otevřené implementaci
  v §1.4.3′; tato stránka je sama nedokazuje.
- **V0127, p. 62 — PREFIX.** Prefix se připojí pouze jménům bez úvodní
  dvojtečky. Proto posloupnost prefixů je :, :Foo:, :Foo:Bar:, : a všech
  pět ADD má přesně vypsané absolutní názvy. `x0 IS :x0` uvnitř Max:
  sváže :Max:x0 s vnějším :x0; :Max a :Max100 zůstanou veřejné vstupy,
  ostatní jména oddělená. Nejde o runtime alokaci ani změnu adres kódu.
- **V0128, p. 62 — LOCAL.** Podmínka neguje globalitu zadaného čísla:
  LOCAL $40 vyžaduje G>40. Protože G≥32, LOCAL $31 je vždy splněna.
  Jde o kontrolu při sestavení a nikoli o okamžitou změnu rL.
- **V0129, p. 62 — BSPEC/ESPEC.** Text popisuje metadata objektového
  souboru a odkazuje na MMIXware. **Partial:** formát/debugger kontrakt
  externího dokumentu nebyl získán; žádný implementační důkaz se netvrdí.
- **V0130, p. 63–65 — návrh programů a historické výroky.** Kroky 0–4
  jsou doporučení s výslovně osobním komentářem, nikoli algoritmus se
  slibem optimálního výsledku. **Partial bibliografie:** Dijkstra 1972,
  kapitola 1; Wirth CACM 14 (1971), 221–227; Literate Programming 1992,
  kapitola 11, a Turingova citace 1945 nebyly nově získány. Výroky o
  četnosti postupů a podílu debugging kódu nejsou povýšeny na ověřenou
  kvantitativní statistiku.

Nové samostatné nálezy: žádné. Dřívější kandidáti nejsou touto poznámkou
uzavřeni. SAVE, RESUME, system/IEEE a fyzický ring zůstávají v backlogu.
