# MMIX — §1.4.3′–12: přesný obor UNSAVE a konec bootstrapu

## Obor a již uzavřená inverse

P.16 popisuje UNSAVE jako obnovení kontextu předchozího SAVE.
Úloha12 p.92 a binární vstupní formát20 tuto sémantiku používají;
bootstrap obraz smí být vytvořen přímo, má-li stejný platný layout.
Není zde požadavek implementovat nezdokumentovanou nápravu všech
poškozených či záměrně neplatných obrazů. Proto odvoláváme starý
partial požadavek dokazovat clamping G<32 v této knižní úloze.
Je to jiný obor než přípustný SAVE image. Poznámka k sanitizaci
markeru ve zdroji nerozšiřuje veřejný kontrakt na každý64bit obraz.

Celá inverse platného obrazu se **přesně přebírá** ze
`exercises-1.4.3-001-014.md`§11–12: obecné32≤G≤255,
0≤L≤G, ρ≥256, původní pushed stack, marker, globals a12specials,
packed(G,A) a všechny přechody ringu. C0007 opravuje samostatnou
SAVE větev, nikoli UNSAVE. Není třeba znovu dokazovat ani spouštět
SAVE/UNSAVE. Nízké3bity pointeru se normativně ignorují. Podmínky
X=Y=0, adresní konečnost a paměťové chyby mají vlastní vstupní testy.

Zbývající skutečná povinnost je výslovný požadavek úlohy12:
vynechat Update **jen při prvním umělém UNSAVE**.

## Vytištěný diskriminátor má omezený rozsah

Na p.121/file129 závěr používá `PBNZ uu,Update`,
`BZ resuming,Update`, `JMP AllDone`. Při prvním načtení jsou
uu0,resuming1; správně nepočítá bootstrap. Ordinary UNSAVE
s resuming0 správně projde Update i tehdy, je-li uu0.
Při uu≠0 se aktualizace provede bez ohledu na resuming.

Ale uu je celý64bit hostitelský registr zvyšovaný ADDU na543.
Po2^64 aktualizacích se opět rovná0. Vložené ropcode0 UNSAVE
pak má uu0,resuming1 a je mylně považováno za bootstrap.
To je chyba i na platných obrazech; žádný malformed header
není zapotřebí. Není dovoleno pouze mlčky předpokládat, že
64bit čítač nikdy nepřeteče.

Přesná konečná dosažitelná rodina nepotřebuje2^64 kroků spustit.
V platném počátečním obrazu s G240,L1 nechť global registry
předem obsahují validní SAVE pointer S, word`#00000000fb0000ff`,
adresu After a N=(2^64−4)/3=#5555555555555554. Obraz samotný
může být tím původním, nezměněným bootstrap obrazem; S je
jeho packed-header adresa. Proveďme pouze:

```
        SET     $255,saved_pointer_register
        PUT     rX,unsave_word_register
        PUT     rW,after_address_register
Loop    SWYM
        SUBU    counter,counter,1
        PBNZ    counter,Loop
        RESUME  0
After   GET     result_register,rU
```

Všechna jmenovaná vstupní i výsledková místa jsou existující
globals. N je kladné a menší než2^63. Smyčka má invariant
counter=N−j po j průchodech, přesněN průchodů a3N instrukcí.
Tři přípravné instrukce plus smyčka plus RESUME dávají
3+3N+1=2^64, tedy při vstupu do vloženého UNSAVE uu0.
Žádný předchozí příkaz nemění paměť obrazu, ring, rG ani L.
Vložené UNSAVE je legální a jeho obnova proběhne podle přijaté
inverse. Obnoví i g[rX]/g[rW], avšak pracovní inst_ptr už má
After a resuming je samostatný hostitelský registr.

Tři závěrečné větve neprávem vynechají aktualizaci tohoto
pozdějšího UNSAVE. Následující GET vrátí0 namísto1; navíc
schází20μ+1υ v nominálním clocku a jedno snížení ii. Paměť
zůstává konečná: smyčka je v jediném textovém chunku, rámec
se nezvětšuje, žádné datum ani globální hodnota nepřeteče
nepřípustně. Přetáčí se jen deklarované modulo čítače.
Příklad nesouvisí s C0015 nebo C0023 a nepoužívá chybný SAVE.

## Konkrétní oprava s úplným invariantem

`sources/sim-unsave-bootstrap.patch` přidává soukromý nulový
GREG `initial_unsave`. Main jej nastaví1. Závěr UNSAVE je:

```
        PBZ     initial_unsave,Update
        SET     initial_unsave,0
        JMP     AllDone
```

Invariant je jednoduchý a nezávislý na délce běhu: před
prvním umělým UNSAVE je flag1; právě jeho úspěšný konec jej
jednou změní na0; žádný jiný příkaz flag nemění. Při chybném
vstupním souboru před bootstrapem se program ukončí a další
příkaz neexistuje. Po bootstrapu tedy každé úspěšné UNSAVE,
ordinary i vložené, projde Update, i při libovolném přetočení
uu či cc. Guest paměť a registry nemohou měnit tento hostitelský
soukromý registr. Nový GREG je nulový, tedy se neslučuje
s jinou měnitelnou proměnnou.

Typická pozdější cesta PBZ stojí1υ, stejně jako původní
vzatý PBNZ. Bootstrap cesta stojí3+1+1=5υ, stejně jako původní
nevzatý PBNZ, nevzatýBZ aJMP. Jediné nové SET v Main stojí1υ
hostitelské inicializace mimo virtuální clock. Oprava je
acyklická a nemění prověřenou inverse ani žádnou guest hodnotu.
Patch je konkrétní a zkontrolovaný proti jedinečným zdrojovým
kontextům; **nebyl sestaven ani spuštěn**, neboť žádná nová
instrukce či aritmetický předpoklad to zde nevyžaduje.

## Prameny, příbuzná známá oprava a priorita

Originál129 byl zobrazen v
`images/unsave-answer-file129-p121.png`. Celých13 errata vrstev
má cílené kontexty v `results/errata-unsave-bootstrap-boundary.json`.
Změna slov „clocks and counters“ z29.6.2020 nemění větvení.
Související veřejná oprava C MMIX-SIM z2012 změnila bootstrap
test z rU na sclock při zavádění filtrů rU; oprava2015 řeší
precedenci operátoru v jeho čítači. Oba původní reporty byly
přečteny a uloženy, odkazy v
`results/unsave-related-counter-reports.json`.

Jejich již zveřejněné změny nejsou náš nález. Pro výše uvedený
konkrétní svědek je cc=(3+3N+2+5)mod2^64=6, takže veřejná
náhrada testu uu za cc by právě tento svědek také odvrátila. Neprohlašujeme
je za obecný důkaz, že libovolný modulární clock spolehlivě
identifikuje bootstrap. Proto je zde uveden samostatný flag.
Tento velmi vzdálený čítačový okraj zapisujeme jako drobnou
věcnou korekci v důkazu, **bez nové karty a bez zvýšení počtu
confirmed nálezů**. Dlouhý běh by nic matematického nedodal
a v souladu s pokynem uživatele nebyl zahájen.

E12 má nyní argument_recorded: přesný původní obor, celá
převzatá inverse a úplná oprava skutečné zbývající bootstrap
povinnosti jsou doloženy. Vzory1/4B jsou použity na dosažitelné
mezní stavy a explicitní celočíselný invariant; nereálná délka
příkladu není zaměňována za nepřípustnost stavu.
