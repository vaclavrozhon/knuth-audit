# MMIX-C0023 — ropcode 2 nesmí odmítnout původní opcode RESUME

Confirmed, medium, book; nezávislá kořenová revize přijata v X0076 dne12.11.2026.
Místo: §1.4.3′–14, odpověď p.122/file130, poslední blok od `2H`.
Digitální vydání3, květen2023; fyzický výtisk nebyl kontrolován.

## Přesný kontrakt a přípustný stav

Zadání p.92/file100 výslovně definuje ropcode2: nastaví `$X←rZ`
a `exc←Q`; X je třetí byte zprava, Q třetí zleva. Vyžaduje pouze,
aby X nebyl marginal. Nepřikazuje vykonat opcode ze spodní poloviny rX.
Normativní MMIX-doc2342–2444 navíc omezuje zákaz vloženého RESUME
výslovně na ropcodes0 a3. Ropcode2 vkládá nastavení registru.
Tentýž kontrakt je na
[primární stránce RESUME](https://mmix.cs.hm.edu/doc/instructions/gitraptrip.html).

Vezměme běžný přípustný uživatelský stav:

* G240, L1; cíl X240 je globální;
* rW=#118, tedy řádná následující textová adresa;
* rX=#02000000f9f0f7f8, rZ=444 a rA=0;
* právě vykonávaná instrukce je platná `RESUME 0`.

Ropcode je2, Q0, X240. Kontrakt požaduje `$240=444` a následné
pokračování v rW. Byty f9,f7,f8 zde nejsou vykonávanou instrukcí
ani jejími operandy. Nejde tedy o pokus rekurzivně vložit RESUME.

## Celá chybová větev

Vytištěná rutina ověří XYZ0. rX je nezáporné, `xx=2`, `t=xx−2=0`.
BNN skočí na1H, BP neodmítne nulu. Výběr `(rX>>13)&(8*255)`
dá8X=1920. X není local, ale porovnání s gg=1920 správně
uzná global. Program tedy dospěje k2H.

`MOR t,x,#8` vybere opcode byte f9. Následující CMPU vytvoří0
a BZ nevyhnutelně skočí Error. Žádné načtení rZ, zápis `$240`
ani pokračování v rW nenastane. To odporuje jak zadání této
úlohy, tak výslovnému primárnímu kontraktu. Argument nevyžaduje
běh původního programu.

Obecně totéž nastane pro každé nezáporné rX s ropcode2,
opcode byte f9 a jakýmkoli nemarginal X, nezávisle na rY,rZ,Q.
Pro ostatních255 opcode bytes tento konkrétní zákaz nezasáhne.
Ani úplná oprava staršího C0015 pro ropcode1 tuto větev nezmění;
jde o nezávislou vadu.

## Autorovy implementace a úplná oprava této vady

MMIX-PIPE5774–5803 nejprve pro RESUME_SET nahradí spodní instrukci
za SETH se zachovaným X. Teprve potom provede společné kontroly.
Jeho zákaz RESUME tedy kontroluje skutečně vložený SETH, nikoli
zahazovaný původní opcode. Tento zdroj souhlasí s dokumentací.
Výřez je `sources/mmix-pipe-20250620-resume-excerpts.txt`.

C MMIX-SIM2013 i2025 naopak obsahují stejný příliš široký
fall-through zákaz jako knižní odpověď. Tento nesoulad dvou
implementací není důvodem přepsat výslovnou specifikaci.
Zde evidujeme **jeden knižní nález**; automaticky nepřidáváme
další software kartu či druhý počet.

Je nutné opravit dvě místa. V kontrole od2H se při `xx=2`
přeskočí test f9. V instalaci ropcode2 se zároveň nastaví
`op=#C1`, protože skutečně prováděnou instrukcí je ORI x,z,0.
Jinak by pozdější AllDone při původním `op=#F9` ponechalo
resuming=−2 a opakovalo vložení. `inst` se zachová pro záznam
původního slova při případném Q tripu. Celý konkrétní patch
je v `sources/sim-resume-audit.patch`; současně obsahuje
samostatně doloženou obecnou opravu C0015.

Pro libovolné původní OP,Y,Z tak nová větev provede právě jeden
set, zapíše příslušný nemarginal cíl, předá Q standardnímu
zpracování výjimek a v AllDone zruší resuming. Zákaz ropcode0
vkládajícího skutečné RESUME se zachovává. Ropcode1 f9 stejně
nepovoluje již jeho maska normálních instrukcí.

## Omezená nová reprodukce a prameny

Jeden nový případ `rop2-resume-marker` v
`results/resume-recovery-native.json` poprvé spustil opravený
program na nezávisle vytvořeném validním binárním obrazu.
První výstupní octabyte je444, rA0, nezměněné rR77 a rH33.
Nejde o opakování starého C0015 případu. Celých27 nových
případů opravy proběhlo jednou; první build a běhy2.273246s,
nice15, všechny napoprvé úspěšné. Původní chybný program se
znovu nespouštěl. Obecný důkaz výše není indukován z testu.

Originál130 byl zobrazen jako
`images/resume-answer-file130-p122.png`; sazba obsahuje právě
nepodmíněné MOR/CMPU/BZ. Originál zadání100 byl rovněž nově zobrazen jako
`images/resume-statement-file100-p092.png`; navazující131 má
dřívější uloženou obrazovou evidenci. Definice p.19 o zákazu
RESUME se vztahuje k ropcode0, nikoli k2.

`results/errata-C0023.json` ukládá SHA256 a sémanticky přečtené
kontexty všech13 relevantních historických/současných vrstev.
Známá oprava komentáře AllDone na p.90 z29.3.2023 ani změna
trip-handler návratu na p.114 se této větve netýkají. Aktuální
[MMIXware errata](https://cs.stanford.edu/~knuth/mmixware-errata.html)
a [seznam upstream chyb](https://mmix.cs.hm.edu/bugs/index.html)
byly znovu otevřeny7.11.2026; odpovídající oprava není uvedena.
Potvrzení znamená rozpor v našich zdrojích, nikoli tvrzení o prvenství.
