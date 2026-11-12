# Souvislý průchod §1.3–1.3.1 dne 5. listopadu 2026

Přímo přečteny původní strany 124–144 a odpovědi 507–510, tedy
souborové strany 139–159 a 522–525. Na 144 byl přečten i úvodní odstavec
§1.3.2; další MIXAL začíná na 145. Předchozí asymptotická část strany
507 má samostatný záznam X0947. Cílem této recenze je správnost textu,
tabulek, příkladů a odpovědí, nikoli pouhé znovuspuštění emulátoru.

## Sémantika a matematika

Přečteny celé `mix-semantics.md`, `mix-programs.md`, `mix-loader.md`
a `mix-scope.md`. Původní tabulky byly porovnány přímo s obrazy,
včetně obou stran tabulky 1. Přijímám následující obecné argumenty:

- Radix b je 64 až 100; pětibajtová velikost má rozsah 0 až b^5−1.
  Součet čísel šestnácti modelů je 16150, jeho podíl šestnácti má
  dolní celou část 1009. M+IX má stejnou hodnotu. Kapacity 2–5 bajtů,
  21 sousedních polí a kód 8L+R jsou správné. Adresy 0–3999 se vejdou.
- LOAD zarovnává vybrané bajty doprava; STORE používá pravé bajty
  registru a nevybrané části nemění. CMP porovnává stejné pole obou
  operandů, nikoli celý registr proti zarovnanému poli. Znaménko nuly
  je součástí stavu, ač obě nuly jsou při číselném porovnání stejné.
- U dělení je dělenec |A|b^5+|X| a podíl se vejde právě pro
  |A|<|V|. Původní dvě formule na 131 chybně postrádají X, známá
  oprava 1997. Znaménko X na vstupu se ignoruje; výstupní zbytek
  přebírá původní znaménko A. Všechny vytištěné příklady sedí
  s tímto pravidlem, včetně neznámých bajtů závislých na radixu.
- ADD/SUB a adresové přírůstky ponechají při nulovém výsledku
  staré znaménko. ENT při nulové efektivní adrese přebírá znaménko
  instrukce. JOV/JNOV vypínají overflow; JSJ je výslovná výjimka
  z ukládání návratové adresy do J. Přeplněný index není platný
  způsob zapnutí pětibajtového overflow.
- Posuny zachovávají oba znaménkové bity. MOVE kopíruje postupně,
  proto pravostranný překryv může rozmnožit první slovo. Prázdný
  MOVE je identita; nové rI1 vznikne po dokončení přesunu.
- I/O čeká na předchozí operaci téhož zařízení; přístup do ještě
  načítaného bloku a změna právě vypisovaného bloku jsou nepřípustné.
  U pásky OUT; IOC −1; IN čte právě zapsaný blok. Zařízení jsou
  volitelná, což je podstatné pro přenositelné dolní meze.
- NUM používá deset zbytků modulo 10; CHAR má dost číslic, protože
  b^5≤10^10. Přesné příklady, kódy, normální pole, znaky a počty
  144 celočíselných + 5 plovoucích názvů souhlasí. C0020 je samostatná
  neuzavřená výhrada k časové hlavičce HLT.

Úlohy 1–15 mají přesné odpovědi v `mix-semantics.md`; zvlášť přijato
vyloučení ENT jako univerzální identity a doplněné no-op STORE.
U 16–26 byly znovu sledovány všechny programové invarianty:
nulování překryvem, dělení N na dávky, konečný stav programu „number
one“, zaplnění celé paměti HLT včetně právě vykonávaného kódu,
dočasný skok pro nastavení J a následná obnova paměti, zabalené
násobení X^13, oba algoritmy obrácení bajtů a permutace A/X.
Žádná z těchto kontrol nezaměňuje běžné celé číslo s jeho znaménkovou
reprezentací. Zvláště úloha 22 žádá číselný výsledek, úloha 23 výslovně
plusový znaménkový bit.

Loader má po j-tém průchodu rI1=2j, správnou cílovou adresu a počet
zbývajících slov. Dvojice IN bezpečně zavede druhou kartu před
vykonáváním jejího kódu; JBUS chrání datový buffer. Znaménko se zapisuje
zvlášť před velikostí, takže se zachová i −0. Každý znak obou opravených
karet je povolený při každém radixu a všechny konstanty pro sestavení
mají stejné hodnoty. Důkaz pokrývá libovolnou konečnou prodlevu čtečky,
ne pouze tři prodlevy dříve vyzkoušené emulátorem.

Uložený výsledek 4323 kontrol byl přečten, nikoli opakován. Jeho stará
omezení výslovně doplňují pozdější obecné důkazy. Emulátor stále není
formálně certifikovaný a neimplementuje všechny periférie ani floating.

## Optimalita: co je a není uzavřeno

Přečteny `mix-optimality-root-review.md`, `mix-crossrefs-and-space.md`,
`power-fast-space-root-review.md`, `power-multiply-num-root-review.md`,
`reload-shift-root-review.md` a `mix-block-zeroing-relaxed.md`.
Jejich přijaté závěry byly porovnány s původním zadáním a odpověďmi.
Staré vyčerpávající výpočty se neopakují.

- 16(b): 200u je dolní mez, protože každá ze sta libovolných buněk
  potřebuje zápis a přenos stojí nejméně 2u na buňku. Nepředpokládá
  se zdarma připravené externí médium.
- 17(a): minimum tří slov je přijato v přenositelném modelu, který
  počítá všechny použité kódové a pomocné buňky. 17(b) má lepší
  doloženou horní mez 2N+3 floor(N/994)+7; knižní dlouhé řešení
  samo výslovně netvrdí důkaz své optimality. Varianta s maximem
  6013u navíc přepisuje buňky za N a není bodovým zlepšením.
- 22: globální nejhorší čas 4u před HLT a 13 dodatečných slov mezi
  takto rychlými programy jsou přijaty. Sedm slov při neomezeném
  čase tím dokázáno není. Pět násobení v addition chain je jiný model
  než násobení zabalených bajtových polynomů.
- 24: prostor dvě slova a nejhorší čas 6u jsou přijaty. Jednoslovné
  DIV nedokáže číst potřebnou konstantu b^4 ze svého vlastního kódu;
  úplný časový rozbor zahrnuje samomodifikaci, LOAD i floating.
- **Otevřené zůstávají** globální prostor 16(a), 22, 23 a čas 17(b).
  Mnoho již vyloučených rodin tříbuněčných programů netvoří úplný
  důkaz. V tomto průchodu nejsou znovu recenzovány všechny jednotlivé
  větve X0783–X0929 a žádná jejich mezera se neuzavírá souhrnem.

Čtyři příslušné úlohy zůstávají `partial`. Povolení přeskočit dlouhý
brute force není důkazem jejich matematické optimality.

## Nálezy a přesná mapa stránek

**C0020 zůstává candidate, low.** Na 138 je pro HLT 1u plus čekání;
hlavička společné buňky NUM/CHAR/HLT na 141 má 10. Tabulka současně
neuvádí zvláštní časy floating variant, takže nelze bez dalšího
rozhodnout, zda jde o chybu, nebo zkratku pro hlavní operace.
V mapě mají 138 a 141 neuzavřenou kontrolu, nikoli potvrzenou chybu HLT.

**C0083 zůstává confirmed, ale pouze pro erratum z 28. 2. 2018.**
Jeho obraz `parallel/errata-additions/images/all1-pre-16.png` byl
přímo zobrazen. Podmínka A≥0 připouští −0; pro A=−0 a vstup +0
všech pět SLA/ADD zachová minus. Požadováno je +0. Oprava podmínky
na kladné znaménko A stačí. Původní Dixonův program má správný
výsledek i pro tento případ. V UI nastavena konkrétní erratová lokace,
závažnost medium (okrajový případ znaménka nuly), nikoli high.
Nezakládá se žádná nová korespondence.

X0152 zůstává sadou známých oprav. Pro červenou mapu jsou vybrány
jen původní vady: obrázek periférií 126; chybějící slovo a interpunkce
130; rA a obě chybějící X na 131; typografické i na 133; rA na 134;
„registers“ na 138; uvozovka na 142; „ability“ na 143; chybějící
no-op možnosti na 508; kvalifikace času HLT a nepřípustné krajní
tabulkové hodnoty na 509; dva skutečně chybné kódy štítků na 510.
Samotné nové formulace, rozšíření specifikace GO, povolení adresy
0100, upřesnění počtu skoků a původně správné užší podmínky nejsou
automaticky chybami původního textu. Nová instrukční pole ani
dobové srovnání procesorů se nepřenášejí zpětně jako chyby sazby.

Všechny čtyři erratové vrstvy mají aktuální identické otisky v
`sources/sequential-2026-11-05/errata-refresh.json`; výtah 40 záznamů
byl přečten. Nejde o 40 různých chyb. C0083 neopraveno v těchto
vrstvách, bez tvrzení prvenství či fyzického ověření tiskového exempláře.

## Historie a dostupné prameny

Knuthův uložený MMIX text potvrzuje 64bitový návrh a jeho vlastní plán;
časově neurčitý budoucí záměr z roku 1997 není slibem dnešního stavu.
Wordsworthovy dva řádky odpovídají uloženému přepisu sbírky 1807.
Knight 1896 uvádí vznik 1804 a první vydání 1807; pasáž i báseň byly
přečteny. Rukopisnou chronologii verzí znovu nezkoumáme. Všechny
konkrétní mezisvazkové odkazy odpovědi 25 byly přijaty z X0669 s přesně
vymezenými cíli; kontrola odkazu neznamená audit cílové kapitoly.

Nově stažen a přímo zobrazen Buchholzův vlastní dopis v BYTE 2(2),
únor 1977, s. 144 (soubor 146). Dokládá původně proměnlivý význam
byte a pozdější obecný osmibitový význam spojený se System/360.
Není to důkaz přesného roku celosvětové standardizace: knižní
„1975 or so“ ponecháváme jako přibližné dobové vymezení, nikoli
datum prvního osmibitového byte. Přesná historie standardů je
bibliografická výjimka, nikoli nalezená chyba.

Dobový Computer Directory, Computers and Automation, červen 1965,
s. 58–66, byl stažen z funkčního zrcadla a obrazy byly přímo přečteny
pro identifikaci modelů. Zobrazuje IBM 360, 650, 709, 7070; Univac III,
SS 80/90 a 1107; CDC 1604 a G-20; Burroughs 220; Philco 2000;
SDS 920; RCA 601; Honeywell H-800 a PDP-4. Jde o patnáct skutečných
modelových rodin odpovídajících číselným částem knihy; dnešní názvy
vlastníků se nepodsouvají do původního vzorce. Existenci RECOMP II
doplňuje vlastní manuál Autonetics 508-T-8 (1959), titul a předmluva.
Tyto zdroje nenahrazují šestnáct úplných manuálů ani nezávislou
implementaci všech šestnácti simulátorů. „Easily simulated“ je zde
kvalitativní autorské vysvětlení volby obecného modelu, ne měřený
výkonový či prostorový limit.

Neúspěšné přístupy: bitsavers.org/…/196106.pdf vrátil 403,
bitsavers.computerhistory.org/…/196506.pdf timeout; zrcadlo your.org
poskytlo celé PDF. Webový čteč odmítl velké BYTE PDF; běžné stažení
a lokální render fungovaly. Všechny rendery měly nízkou prioritu.
Rozsahy čtení a kontrolní součty jsou v metadatech nových zdrojů.

Nový neznámý nález: **0**. Celá §1.3.1 zůstává částečná kvůli
C0020 a čtyřem globálním minimům. Pokračování: §1.3.2, strana 145.
