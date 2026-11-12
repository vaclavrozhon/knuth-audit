# §1.3.1: sémantika, příklady a úlohy 1–15

Originál s. 124–144 a odpovědi 507–510 zobrazeny 1.11.2026.
Níže b znamená počet možných hodnot jednoho MIX bajtu: 64 <= b <= 100.
Slovo má znaménko s z množiny {+1,−1} a pět číslic d1,...,d5 mezi
0 a b−1. Jeho velikost je D = d1 b^4 + ... + d5 a hodnota sD.
Znaménko zůstává součástí stavu i při D=0. Označme B=b^5.

## Hlavní popis

- Číselné části šestnácti názvů v (1) dávají součet 16150; dolní
  celá část průměru 16150/16 je 1009. Římské M+IX rovněž 1009.
  Nejde o doslovné sčítání alfanumerických názvů. Úvodní tvrzení o
  snadné simulaci není formální porovnání výkonu šestnácti strojů.
- Garantované kapacity jsou b^k−1 >= 64^k−1; čtyři vytištěné hodnoty
  pro k=2,...,5 jsou správné. Devět registrů znamená A,X, šest I a J.
  Adresy 0,...,3999 se vejdou do dvou bajtů i při b=64.
- Pole (L:R), 0<=L<=R<=5, má kód 8L+R <=45<64. Je jich 21.
  Při načtení se číslice pole zarovnají doprava a ostatní doplní nulami;
  znaménko se přenese právě pro L=0. Při uložení se naopak vezme
  odpovídající počet pravých číslic registru a přepíše určené pole.
  Porovnávání bere **totéž pole obou operandů**, ne celé rA proti
  zarovnanému paměťovému poli. Pole (0:0) proto vždy porovná dvě nuly.
- Adresová část je a; efektivní adresa M=a+rIi při I=i>0, jinak a.
  Pro paměťový operand musí 0<=M<=3999. Přeplnění dvoubajtové
  adresy nebo indexového registru je nedefinováno, nikoli běžné
  pětibajtové přetečení s příznakem.
- ADD/SUB zachovají znaménko původního registru, je-li výsledek nula;
  při přetečení zůstává velikost modulo B a příznak se zapne.
  Bez přetečení se již zapnutý příznak nemaže. INC/DEC mají stejné
  pravidlo. ENT při M=0 bere znaménko instrukce, ENN jeho opak.
  Proto ENT1 0,1 není identita na záporné nule a ENN3 0,3 ponechá −0.
- MUL vytváří přesný desetibajtový součin; obě znaménka jsou součin
  znamének operandů, i když horní nebo dolní část má nulovou velikost.
  Velikost součinu je <B^2, proto nejde o přetečení.
- U DIV nechť A,X označují **velikosti** původních registrů a d>0
  velikost dělitele. Dělenec je n=AB+X, nikoli samotné A.
  Kvocient se vejde právě když A<d: A>=d dává n>=dB, zatímco
  A<=d−1 dává n<dB. Nulový dělitel také splňuje A>=d a přeteče.
  V platném případě jsou nové velikosti floor(n/d) a n mod d;
  znaménka jsou sA*sV, respektive sA. Původní znaménko X se ignoruje.
  Chybějící X ve dvou vzorcích s.131 opravují errata z 28.9.1997.
- Skok ukládá do J adresu následující instrukce právě tehdy, když
  nastane; výjimka JSJ ponechá J. Úvodní zkratku na s.125 je nutno
  číst s touto následnou explicitní výjimkou. JOV i JNOV vždy skončí
  s vypnutým příznakem přetečení. Porovnávací příznak skoky nemění.
- Posuny mění číslice, nikoli znaménka. Kruhový posun závisí na M
  modulo 10; posun s vyhazováním pro M>=5 nebo 10 vymaže příslušná
  číslicová pole. Sekvence s.135 dává přesně vytištěné výsledky.
- MOVE kopíruje po jednom slově vzestupně; nejde o souběžnou kopii
  původního bloku. To dokazuje oba příklady překryvu na s.135–136:
  posun doleva kopíruje tři původní slova, posun doprava rozmnoží první.
  Přírůstek rI1 nastává až po kopii; pro F=0 je celá operace identita.
- Zařízení 0–7 jsou pásky, 8–15 disky/bubny, 16 čtečka, 17 děrovač,
  18 tiskárna, 19 terminál, 20 papírová páska. Fig.13 prvního dotisku
  nemá správný poslední úsek; opravený obrázek je z 15.7.1998.
  Velikosti bloků jsou 100,100,16,16,24,14,14 slov. Znaky neobsahují
  znaménka; při čtení se znaménka nastaví na +, při výstupu ignorují.
- IN/OUT/IOC čekají na dokončení předchozí operace **téhož** zařízení;
  jejich vlastní operace může dále běžet souběžně. Po IN se nesmí
  předčasně číst vstupní blok, po OUT se nesmí měnit výstupní blok.
  JBUS/JRED testují tento stav. Po OUT, IOC −1, IN na téže pásce se
  znovu přečte právě zapsaný blok; IOC +1 po OUT by překročilo poslední
  zapsaný blok a je zakázáno. Při poruše zůstane zařízení obsazeno,
  takže ukončení čekací smyčky předpokládá funkční dokončení I/O.
- NUM interpretuje deset zbytků číslic modulo 10 jako desetinné
  číslo; mění pouze velikost A a případně zapne přetečení. CHAR
  zapíše deset desetinných číslic kódy 30–39. Deset číslic stačí,
  protože B<=10^10. Obě znaménka zůstávají. Příklad s.138 dává
  −12977700, pak −12977699, pak přesně uvedené znaky.
- Tabulka 1 souhlasí v kódech, polích, názvech a znacích. Je 144
  celočíselných názvů operací a pět plovoucích: celkem 149, tedy
  oprávněně „nearly 150“. Plovoucí operace jsou odkázány do §4.2.1;
  nejsou v tomto celočíselném modelu implementovány.
  Časové hodnoty jsou konzistentní s pravidly s.138 s výhradou
  zkráceného údaje u HLT, viz [mix-scope.md](mix-scope.md).

Všechny tabulkové příklady byly přečteny z obrázků. Příklady s.129,
130,132–133,135,138 byly navíc přesně spuštěny pro každé b=64,...,100.
Otazník ve spodním bajtu odečítání s.132 znamená b−9.
V posledním příkladu dělení s.133 je kvocient
617 b^2 + floor((b^2+3)/2) a zbytek 1 pro liché b, b+1 pro sudé b;
oba označené otazníky jsou proto oprávněné.

„Sideways addition“ na s.131 postupně sčítá pět nezáporných
jednobajtových hodnot. Součet je nejvýše 5(b−1)<B, takže se nový
overflow nezapne. Dřívější příznak přesto zůstane beze změny.

## Úlohy 1–15

1. Jediná mocnina 3 v intervalu [64,100] je 3^4=81: čtyři trity.
2. 64^4−1<99999999<=64^5−1: nutno rezervovat pět bajtů.
3. Adresa (0:2), index (3:3), pole (4:4), operace (5:5).
4. −2000+rI4 může být platná adresa: například rI4=2000 dává 0.
   Přesná podmínka je 2000<=rI4<=5999, navíc kapacita registru.
5. C=4,F=5,I=3,a=−80: DIV −80,3.
6. Původní číslice jsou (+,5,1,floor(200/b),200 mod b,15).
   LDAN obrátí znaménko; LD2N(3:4) dá −200; LDX(1:3) dá
   (+,0,0,5,1,floor(200/b)); LD6 celého slova je nedefinováno,
   neboť první bajt 5 není nula; LDXN(0:0) dá −0.
7. Přesný vzorec DIV je výše. Při stejných znaménkách lze použít
   floor(rAX/V), rAX mod V; při opačných ceil(rAX/V), rAX mod(−V).
   Záporná nula se musí obnovit podle pravidla znamének, protože
   běžná celočíselná notace její bit neobsahuje.
8. |rAX|=1234 b^3+3b+1 = (2b)(617 b^2+1)+(b+1).
   Proto rA=(+,0,617 ve dvou bajtech,0,1), rX=(−,0,0,0,1,1).
   Změna znaménka vstupního X nemá vliv.
9. Přetečení mohou změnit ADD,SUB,DIV,NUM,JOV,JNOV,INCA,DECA,INCX,DECX.
   To plyne projitím všech skupin instrukcí; MUL nepřetéká a indexové
   přeplnění není definováno jako nastavení příznaku. GO není operátor.
10. CMPA,CMP1,...,CMP6,CMPX, případně FCMP; jiná skupina příznak nemění.
11. MOVE,LD1,LD1N,INC1,DEC1,ENT1,ENN1; indexace sama registr nemění.
12. INC3 0,3 sčítá rI3 se sebou. Výsledek je definován jen tehdy,
    když dvojnásobek stále vejde do rI3; to je běžná kapacitní podmínka,
    nikoli slíbená aritmetika mimo rozsah registru.
13. JOV 1001 nastaví J=1001 právě pro původní overflow=on.
    JNOV 1001 právě pro off, proto mohou mít různá J.
    JOV 1000 s on jednou skočí s J=1001, pak projde dál; s off
    projde hned. Konečný stav je stejný, čas se liší nanejvýš o 1u.
    JNOV 1000 s on projde; s off skáče navždy a příznak zůstává off.
14. Kladné STJ *(0:0), STZ *(0:0) a STZ *(3:3) jsou no-op díky
    známému vlastnímu znaménku a nulovému indexu; to jsou doplňky
    errat 25.3.2003. ADD/SUB (0:0) přičítají nulu a zachovávají
    i −0 a overflow. ADD/SUB *(3:3) s I=0 čtou vlastní nulu.
    Posuny o nulu, kruhové posuny o násobek 10, MOVE(F=0),
    JSJ *+1 a INC/DEC 0 s I=0 jsou identity. HLT je identita
    pouze při konvenci, která dovoluje následné ruční spuštění;
    zastavení samo je pozorovatelný stav.
    Ostatní skupiny buď mohou přepsat libovolný registr/paměť,
    změnit příznak, nebo uskutečnit skok a změnit J. Zvlášť ENT
    nelze považovat za identitu pouhým přičtením indexu kvůli −0;
    ENN obrací nenulové hodnoty. MUL/DIV nemohou zachovat libovolné
    A i X, NUM/CHAR libovolné číslice a I/O libovolný stav zařízení.
15. Počet znaků je pětkrát počet slov: 70,80,120.

## Meze modelu

`mix_machine.py` je malý vlastní interpret pro reprodukci, nikoli
nezávisle formálně certifikovaný MIX. Zachovává znaménka nul,
samomodifikaci kódu, časování a zakazuje přístup do nedočteného bloku.
Implementuje pouze celočíselné instrukce a čtečku karet; ostatní I/O
a plovoucí operace odmítá. `check_mix_description.py` prošel 4323
kontrolami jednou. Dvě předchozí selhání byla chyby **našeho checkeru**:
kontrola slova 3000 po zavedení programu a přepis O jako 0 na řádku00.
Nejsou připsána knize. Kód bez nové změny znovu nespouštět.
