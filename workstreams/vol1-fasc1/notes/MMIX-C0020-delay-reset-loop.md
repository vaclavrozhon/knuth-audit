# MMIX-C0020 — časovač může v Delay způsobit nekonečné čekání

**Confirmed, medium, book.** §1.3.2′–34, tištěné111–112 / file119–120,
vstupní testy a poslední čekací smyčka Delay. Nejde o doprovodný C program
ani o známý překlep delay/delta na113. Originální119/120/121 byly zobrazeny;
evidence zahrnuje `images/file-119-p111.png`, `recovery-delay-120.png`
a `recovery-delay-121.png`. Kořenová revize přijata v X0073 dne12.11.2026.

## 1. Přesný knižní závazek a přípustný OS

Kniha tvrdí, že program sleduje semaforový protokol s odchylkou nejvýše
několika setυ. Výslovně předpokládá přerušení při rI=0 a OS, který se
brzy vrátí, přitom rI nastaví na nepříliš malou hodnotu. Nevyžaduje,
aby uživatelský GET někdy pozoroval nulu nebo záporný rI, ani konkrétní
fázi timeru při volání Delay.

Povolme intervalové přerušení v rK. Při dosažení0 handler před dalším
uživatelským GET zachová živé registry, potvrdí obsloužený request,
nastaví timer a rychle se vrátí. Při návratu je rI=R, kde0<R<2^63
a R může být libovolně velké oproti krátké režii handleru. Žádný user
GET proto nečte0 ani zápornou hodnotu; mezi resety čte kladné rI.
To je přípustné splnění knižních předpokladů, nikoli jejich porušení
dlouhým handlerem, zakázanými přerušeními nebo nezachovaným registrem.
Počítadlo během handleru může i projít zápornými hodnotami; uživatelský
kód je v té době přerušen. Hodnota při návratu se realizuje nastavením
R plus počet zbývajících epilogových taktů před RESUME.

V primárním `sources/mmix-doc-20131017.w`,2489–2503, rI klesá každým
clock pulsem a nula vyvolá intervalový request v rQ. Oddíl dynamických
trapů,2307–2343, dovoluje přesné přerušení po právě dokončené instrukci
a návrat handleru; žádná povinnost provést ještě jeden user GET tam není.
Jednotaktová zdejší ALU/GET větev s kontrolou requestu na hranici
instrukcí je s tím slučitelná. Stejné rI pravidlo má současný primární
MMIX-DOC a známá MMIXware změna z6.6.2011, nikoli jiná starší definice rC.

## 2. Obecný protipříklad s ref_time=0

Označme H=2^63. Vezměme libovolné0<δ<H a přípustný vstup do Delay,
v němž první GET čte rI=δ. Caller má platný delay_go a delta=δ.
Čtyři vstupní instrukce provedou

    t=δ; ref_time=t−delta=0;
    BN t,1F není vzat; BN ref_time,2B není vzat.

Program proto vstoupí do normální čekací smyčky

    GET t,rI
    SUBU t,t,ref_time
    PBP t,1B

Její invariant je ref_time=0 a delta=δ; ani jedna se uvnitř nemění.
Každý GET podle§1 čte0<rI<H. SUBU tedy ponechá **kladné signed t**
a PBP se vždy vrátí na GET. Ani jeden z resetů nezmění ref_time.
Return GO se nikdy neprovede. Časovač dál pravidelně přerušuje a OS
se pokaždé rychle vrátí, takže to není zablokovaný stroj či hladovění
procesu: samotná uživatelská smyčka vykonává nekonečně mnoho instrukcí.

Tento přípustný vstup je dosažitelný i v celém tištěném řídicím programu:
po známé opravě na `MUL delta,rho,18` je prvníδ=18ρ. Pro vytištěné
ρ=250000000 jde o4500000000<H. Fáze počátečního rI může být zvolena
tak, aby první GET v Delay četl právě tuto hodnotu. Pravidelné další
resety mohou vracet např.10^9 taktů, tedy čtyři sekundy, s několikátaktovým
handlerem. Obsluha požadavku na Berkeley se pak nikdy nedostane do Wait,
i když byl sensor aktivován. Nejde pouze o malý časový posun světla.

## 3. Krátký přesný cyklus a kladný ref_time

V `sources/delay34-reset.mms` je tělo Delay přesným přepisem tisku.
Malý harness pouze nastaví delta a skutečný návrat. Dvě počáteční
instrukce stojí2υ; před nimi nastavíme rI20. První GET v Delay tedy
čte18. Pro delta18 dostaneme ref0, pro delta17 ref1.

Po čtyřech vstupních instrukcích čte normální smyčka rI14,11,8,5,2.
Při posledním SUBU dosáhne timer0 a simulátor pozastaví před PBP
na adrese#134. Živé stavy jsou:

| delta | ref_time | t po SUBU | příští PC | delay_go | rI |
|---:|---:|---:|---|---|---:|
| 18 | 0 | 2 | #134 | #13c | 0 |
| 17 | 1 | 1 | #134 | #13c | 0 |

Nyní handlerův účinek obnoví rI60. Čekající PBP je vzat a dalších
dvacet GET čte59,56,…,2. Všechna tato čísla jsou větší než ref0 i ref1.
Po přesně60υ je timer znovu0 **před touž instrukcí PBP se stejnými
všemi živými registry**. V tomto cyklu není žádný jiný zápis paměti,
změna delta/ref_time ani cesta na návrat. Obnovením stejného rI60
se proto celý cyklus induktivně opakuje libovolně dlouho.

Počítadla profilu a rU se mění, ale tento program je nečte a nemají
vliv na přerušení. To není tvrzení, že se zastavil veškerý vnější stav;
opakují se přesně všechny části, na kterých závisí jeho další řízení.
Na větší hodiny lze použít i obecný ref0 důkaz§2, bez přehrávání
miliard taktů. Kladný ref1 navíc ukazuje, že pouhá změna vstupního
`BN ref_time` na `BNP ref_time` neopraví celou chybu.

## 4. Co skutečně ověřilo provedení

`verify_delay34_reset.py` byl spuštěn pod nice15. Jde o nové malé
programy, nikoli opakování dřívějšího auditu. MMIX-SIM neimplementuje
tento konkrétní kernel handler: jeho dokumentovaný rI breakpoint
pozastaví po vypršení intervalu a debuggerový příkaz `rI=60` modeluje
pouze povolený účinek handleru při návratu. To je záměrné a výslovné
omezení reprodukce; architekturní přípustnost i nekonečnost dokazuje§1–3.

Oba nové programy vykonaly každý jednou pouze200 instrukcí/200υ,
s pozorováním po20,80,140,200υ. Všechna čtyři pozorování přesně
souhlasí s tabulkou, žádný programový Halt ani Return se neprovedl.
Po třech resetových cyklech běh úmyslně ukončil debugger `q`;
nejde o timeout a z pouhých200 kroků se neodvozuje nekonečnost.
Tu poskytuje výše popsaný uzavřený přechod téhož živého stavu.

Primární MMIX-SIM dokumentuje `rI=250` jako přerušení simulace po250υ
a v `Update the clocks`,2650–2664, přesně odečítá cenu provedené
instrukce. Končí návratovou hodnotou g[255].l, řádek2916. Proto první
`q` vrátil procesu2 a druhý1: to jsou právě živé t, ne chyba assembleru
ani vyvolaný Halt. Vlastní obecný wrapper první2 chybně považoval za
chybu příkazu **až po celém dokončeném replayi**; trace byl zachován,
wrapper opraven a první případ se neopakoval. Krátká následná syntaktická
oprava wrapperu byla odmítnuta Pythonem před dalším spuštěním; poté se
provedl pouze dosud nespouštěný druhý případ. Oba native replaye měly
0.001603 a0.001216s. Všechny logy jsou zachované, žádný dlouhý běh nebyl.

Evidence: `results/delay34-reset.json`, oba `delay34-delta*-trace.txt`,
oba listingy, `results/delay34-reset-build-and-run.json` a přesné
debuggerové příkazy v `sources/delay34-reset-debugger.txt`.

## 5. Originál, všechny relevantní errata a rozsah opravy

Originál119 obsahuje oba BN a výslovný OS předpoklad;120 obsahuje
GET/SUBU/PBP a návrat. Aktuální i kumulativní errata a původní TEX
znovu tisknou stejnou smyčku v náhradě z4.6.2011. Jediná následující
oprava34 z15.3.2024 mění delay na delta v posledním MUL. Je zde
aplikovaná a s tímto protipříkladem nesouvisí. Knownerrata nejsou nález.

`results/errata-C0020.json` zachycuje13 prohledaných textových vrstev,
hashes a všechny zásahy: tři MMIX erratové podoby, MMIXware errata
a aktuální stránku, upstream bug/rounding/change-file zdroje a pět
historických vrstev svazku1. Sémanticky relevantní změny rI z2011 jsou
už součást použité architektury. Ostatní `delay` v MMIXware patří cache
copy_block; staré stránky111–113 svazku1 jsou Bernoulliho formulace,
ne semafory. Žádná oprava resetové smyčky nebyla nalezena.

Je třeba rozpoznat reset také v normálním čekání nebo použít jiný
monotónní zdroj uplynulého času. Změna jediného BN na BNP nestačí
podle druhého cyklu. Zde se nevydává neprokázaný jednořádkový patch
za úplnou opravu všech OS časových podmínek. Kniha potřebuje opravit
rutinu nebo podstatně zesílit podmínky, aby reset nemohl skrýt cílový
interval; dosavadní „soon“ a „not-too-small“ tuto vlastnost nezajišťují.

Starší tvrzení v `exercises-1.3.2-027-035.md`, že Delay je správný už
jen z0≤delta<2^63, je tímto výslovně odvoláno. Platí pouze při dalších
podmínkách na pozorování timeru bez skrytého resetu, ne obecně v knize.
Zbytek34 a nezávislé OS/I/O časové předpoklady zůstávají odděleně partial.

Binomický vzor je použit na přesný obor rI/δ a dosažitelný mezní stav;
Algorithm R na celý opakující se přechod místo timeoutu; kografový vzor
na kladný ref1, který vylučuje nejbližší zdánlivou jednobitovou opravu.
Závažnost medium odpovídá skutečnému zacyklení knižního algoritmu.
