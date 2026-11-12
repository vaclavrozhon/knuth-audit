# MMIX-C0017 — opakovaná stejná definice globálního symbolu není chyba

**Stav:** confirmed v doložené digitální sazbě; kořenová revize přijata
v X0072 dne12.11.2026. **Závažnost:** low. **Rozsah:** knižní tvrzení o diagnostice
assembleru, nikoli chybný assembler nebo výpočet programu.

Na tištěné straně 35 / souborové 43, bod 4, kniha tvrdí, že opakovaný
výskyt globálního symbolu v LABEL více než jednoho řádku vyvolá chybu
assembleru. Je třeba doplnit, že nový výskyt musí změnit jeho ekvivalent
nebo typ. Dvě totožné definice stejného ekvivalentu a typu jsou
ve skutečném MMIXAL povoleny a nejsou diagnostikovány.

## Přímý protipříklad a úplná rozhodovací větev

Následující zdroj má globální symbol X dvakrát ve sloupci LABEL:

```
X       IS      1
X       IS      1
        LOC     #100
Main    TRAP    0,Halt,0
```

Není použita lokální značka, PREFIX, předdefinovaný X ani future reference.
X je při prvním výskytu čisté číslo 1; druhý výskyt je tentýž globální
symbol se stejným typem a hodnotou. Main je platně definováno, instrukce
je zarovnaná a Halt předdefinováno. Žádný GREG ani doplňková báze nejsou
potřeba. Předpokládá se běžné úspěšné čtení/zápis souboru a dostatek
hostitelské paměti; tvrzení se týká sémantické diagnostiky LABEL.

V autorově verzi 2013 `sources/mmixal-20131017.w`, řádky 2713–2747,
i verzi 2025 `sources/mmixal-20250620.w`, řádky 2716–2750, úvod oddílu
výslovně dovoluje opakovanou definici, zachová-li ekvivalent. Následující
skutečná větev kontroluje také typ:

```
if (pp->link==DEFINED || pp->link==REGISTER) {
  if (pp->equiv.l!=cur_loc.l || pp->equiv.h!=cur_loc.h ||
      pp->link!=new_link) {
    ... diagnostic ...
  }
}
```

Pro IS nastaví předchozí kód `cur_loc` na vyhodnocený operand a
`new_link=DEFINED` pro čisté číslo, `REGISTER` pro číslo registru.
Po první definici zde tedy je `(equiv.h,equiv.l,link)=(0,1,DEFINED)`.
Při druhé definici jsou porovnávané tři složky přesně `(0,1,DEFINED)`.
Vnitřní podmínka je nepravdivá, neprovede se žádné `derr`; po větvi se
stejný ekvivalent i typ znovu uloží. Vnější alternativy PREDEFINED a
future-reference se nepoužijí, protože X už je DEFINED. Běžný location
counter se po IS obnoví, takže opakování nevytváří data ani neposouvá
program. To je úplný zdrojový důkaz tohoto případu bez assembler run.

Obecný invariant je tentýž pro každou již definovanou dvojici
(unsigned octabyte ekvivalent, pure/register typ): druhá definice se
stejnou dvojicí projde, rozdílná vyvolá diagnostiku. Například
`X IS 2` místo druhého řádku změní hodnotu a vyvolá chybu; `X IS $1`
změní typ a vyvolá chybu i při stejných numerických bitech. Kniha
správně říká, že globální symbol má jediný význam; chybné je pouze
zesílení na počet jeho výskytů v LABEL. Pravidla místních symbolů
2B/2F a všechny příklady Programu P tím nejsou zasaženy.

Úvodní definice MMIXAL jinde doporučuje definovat symbol jen jednou.
Tento stylistický požadavek se nezaměňuje s doloženým chováním
assembleru: zkoumaná knižní věta výslovně předpovídá hlášení chyby,
zatímco implementace i její lokální dokumentace výslovně dovolují
právě uvedený opakovaný případ. Nejde o požadavek zpřísnit assembler.

## Vydání, originál a errata

`images/file-043-p035.png` byl zobrazen; je na něm jasně výslovné
tvrzení o hlášení chyby při opakovaném globálním LABEL. Knižní PDF je
digital release 3, květen 2023, se SHA256
`16f86d86839647a0c99be829a537a7516577704393ad8f95492ab42119905666`.
Fyzický dotisk nebyl prohlédnut.

Původní 2013 assembler pochází přímo z autorova archivu
`https://www-cs-faculty.stanford.edu/~knuth/programs/mmix-20131017.tgz`.
SHA256 archivu souhlasí s dříve uloženým
`aa64c4b9dc3cf51f07b330791f8ce542b0ae8a1132e098fa95a19b31350050b4`;
vytažen byl pouze dříve neuložený mmixal.w. SHA256 zdroje je
`31b1c78cffe20cbc2b7d5d17f614f6a5a46180fd1ea8b1ea2328f0e1a741c7b8`.
Novější originál má SHA256
`1335621eb854fc6d34689b5812cbdf2fc4aaead59e30d4f2bd7acf32d7cd5071`.
Relevantní větev má v obou stejný kontrakt a stejné tři porovnávané
složky. Nedošlo k buildu ani běhu assembleru; nejde o nově dodané
chování, které by se mylně přeneslo do staré knihy.

`results/errata-C0017.json` zaznamenává stejných deset veřejných vrstev
jako C0016: fasciklový zdroj/short/long, MMIXware errata/current,
upstream bugs/rounding/warnings a source/long errata původního svazku 1.
Všechny výskyty čísla 35 nebo 150 v nich jsou index, matematická úloha,
I/O, odkaz na hlášení chyb, typografická nebo header-name oprava.
Žádný se netýká této diagnostiky. Hledání redefinition, already defined,
same equivalent/value a global symbol nenalezlo příslušnou opravu.
Na veřejném primárním MMIX webu je dostupný i vytištěný mmixal.pdf;
obecné doporučení definovat symbol jednou nemění výše dokázanou větev.

Přesná oprava textu: chybové hlášení vázat na opakovanou **odlišnou**
definici globálního symbolu. Žádná oprava programu ani globální
novost nálezu se netvrdí.
