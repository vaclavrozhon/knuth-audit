# §2.2.2: prameny a známé opravy

> Aktualizace5.11.2026: souvislá revize a aktuální pramenné výjimky jsou v [novém zápisu](sequential-allocation-2026-11-05.md). Starší stav otevřených kroků níže je historický; úloha13 je nyní uzavřena, C0035 zůstává otevřený.


Všechny čtyři vrstvy all1-prepre, all1-pre, all1, err1 byly prohledány.
Použitý poslední krátký seznam je aktualizován31.5.2026; nové stažení
1.11.2026 nezměnilo soubor. Originály244–254 a540–545 byly prohlédnuty,
včetně matematických mezí, znamének, exponentů a obrázků. Známé opravy
byly porovnány i s původními obrazy PDF, nikoli jen OCR.

## Známé opravy

| Místo | Datum | Změna |
|---|---|---|
|245|17.6.1998|Mezera mezi (6) a and.|
|245|2.5.2024|Výslovný předpoklad M>1.|
|247|29.10.2006|to be manipulated → to be treated.|
|247|6.1.2011|Při levém přesunu L<TOP[i], nikoli ≤.|
|248|20.2.2009|NODE(TOP[i]) → CONTENTS(TOP[i]).|
|249|6.3.1998|V R4 porovnání NEWBASE[j]>BASE[j].|
|252|13.8.1997|Odkaz na cvičení4(c).|
|253|18.12.1999|Typografická úprava max(k1,k2).|
|540-3|18.6.1998|LDA X2,7:1 místo LDA 2,7:1.|
|540-4|13.8.1997|Přeznačení částí(a)–(e).|
|541|5.10.1999|Mezera kolem přiřazení N←0.|
|542-10|10.9.2008|Přísná mez j<k v součtu.|
|542-11|4.10.2005|Opraveny oba konečné součty i generující funkce.|
|542/543-12|20.9.2024|Jednotné teleskopické odvození obou parit m.|
|543-14|18.11.1999|m/n+sqrt(m)x_j a Jacobian I1=I2/n².|
|543-14|11.9.2008|Faktor(sqrt(m))^(1−n).|
|544-14|18.11.1999|Mez3≤j≤n místo m.|
|544-17|20.2.2009|less → more; tato oprava neodstraňuje C0034.|

Doklady: images/sequential-errata-all1-prepre-p18,p19,p40,p41.png
 a images/sequential-errata-all1-p9,p14.png. Žádné nové cvičení tohoto
bloku v prohledaných vrstvách nebylo nalezeno. Nové C0034 a kandidát
C0035 jsou oddělené od známých oprav.

## Přečtené původní prameny

**Yao1979.** Autorův reportSTAN-CS-79-708, technický text1–17 přečten
včetně hlavních pomocných tvrzení a důkazu. Uložené PDF má20 souborových
stran, text začíná na souborové3. Primární verze je dostupná z veřejného
archivu Stanfordských zpráv přes zrcadlo Bitsavers. Její silnější
chybový člen log(m)/sqrt(m) se neztotožňuje s časopiseckým výsledkem1981.
Nakladatelský abstrakt DOI10.1137/0210029 potvrzuje log²(m)/sqrt(m)
v citované časopisecké verzi; její plný text zatím získán nebyl.
Vlastní důkaz meze knihy je v sequential-probability.md.

**Flajolet1986.** Autorův původní článek z algo.inria.fr, přečten úvod,
redukce na procházky, spektrální výpočet a relevantní věty2/3 na336–337,
včetně obrazu obou těchto stran. Při převodu parametrů je pravděpodobnost
jednoho vkladu v článku rovna(1−p_knihy)/2. Věta3 skutečně uvádí
rovnoměrnou limitu pro pevné p_knihy>1/2; vlastní úplný důkaz tohoto
kroku je dosud otevřený. Tištěná číselná aproximace kritické konstanty
v článku se liší od přesného součtu; kniha má správných0.675314… .
Nejde o nový nález v TAOCP.

## Dosud neuzavřené citace

**Wise–Watson1976, BIT16,442–450.** Nakladatelská stránka
DOI10.1007/BF01932727 potvrzuje titul, oba autory, rozsah i abstrakt
navazující na Garwickův algoritmus. PDF přesměrovalo na předplatitelskou
HTML stránku; plný článek nebyl přečten. Abstrakt není náhradou kontroly
technického obsahu.

**Fraenkel1979, IPL8,9–10.** DOI10.1016/0020-0190(79)90081-4 a přesná
Crossref metadata potvrzují bibliografii. Nakladatelská stránka vrátila
403; plný text ani původní návrh spárovaných zásobníků nebyl přečten.
Odkaz na pozdější společný článek1994 není vydáván za původní doklad.

**Kozelka1956, Ann.Math.Stat.27,507–512.** Primární obsah čísla naJSTOR
potvrzuje článek Approximate Upper Percentage Points for Extreme Values
in Multinomial Sampling, identifikátor2237008. Plný text chybí; atribuce
speciální konstanty pro n=3 není přímo zkontrolovaná. Vlastní obecný
výpočet konstant pro n=2,3,4,5 a chybový členO(1) jsou ověřené zvlášť.

URL, návratové kódy a kontrolní součty jsou ve zdrojové složce
sources/sequential-allocation/. Neúspěšné HTML odpovědi jsou zřetelně
odděleny od skutečných PDF; žádná placená či uzavřená kopie nebyla
považována za přečtený pramen.
