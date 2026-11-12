# Přetečení: přesný kontrakt MMIX před cílenou reprodukcí

6. listopadu 2026. Tento záznam rozlišuje MMIX architekturu, chování
zmrazeného programu a vlastní pravidla IEEE. Samotný odkaz na IEEE
nenahrazuje kontrolu výslovných odchylek MMIX. Žádný test nebyl pro tento
záznam potřeba.

## Normativní řetězec a jeho meze

Primární `sources/mmix-doc-20131017.w` má následující souvislé části.
Soubor `mmix-doc.w` v autorově distribuci z roku 2025 je **bytově totožný**,
SHA-256 `97034eec4d10a9f7ee7b55e80d0ca1d850fecbc7818a569ea0fef08dfb9d3a9b`.

1. Ř. 1120–1178 stanoví IEEE/ANSI 754 aritmetiku a čtyři režimy; OFF
   znamená směr k nule, UP k +∞, DOWN k −∞, NEAR nejbližší se sudou půlkou.
2. Ř. 1217–1238 ukládá pro sedm aritmetických operací přesnou operaci
   následovanou aktuálním zaokrouhlením. Výjimka O se detekuje, když
   přesně zaokrouhlená konečná hodnota vyžaduje exponent přes 2046.
   Tato formulace neurčuje jinou implicitní hodnotu O než převzatý IEEE
   kontrakt; neříká, že se všechny režimy mají přepnout na NEAR.
3. Ř. 1517–1527 výslovně přenáší stejné zaokrouhlovací konvence na STSF,
   s kratší přesností a rozsahem. Je to nejužší přímý MMIX kontrakt
   pro níže uvedený případ; nevychází jen z obecného sloganu o IEEE.
4. Ř. 1988–1995: při vypnutém enable se pouze nastaví event; při zapnutém
   enable se zavolá handler. Ř. 2005–2015 výslovně odchyluje **příznaky**:
   MMIX má vždy O i X, i když je O-trip zapnut. Není zde odchylka výsledné
   číselné hodnoty při vypnutých tripech.
5. Ř. 2023–2027 mapuje rA[17:16]=01 na OFF. Ostatních 46 horních bitů
   musí být nula. Stav rA=#0000000000010000 má platný OFF a všechny
   enable/event bity nulové.
6. Ř. 2195–2202 dovoluje handleru změnit již vypočtený implicitní výsledek
   přes rZ/RESUME; u stores je změna obtížnější. To neplatí pro případ
   se všemi enable bity vypnutými, kdy se žádný handler nevolá.

V celém dokumentu byla zkontrolována každá zmínka o overflow, rounding
a inexact, nejen vyhledaná jedna věta. Nebyla nalezena výslovná výjimka,
která by pro vypnuté O/X přikazovala nekonečno při OFF, UP záporného
výsledku nebo DOWN kladného výsledku. Popsané výjimky FEQL, NaN payloadů,
tininess a O/X při **zapnutém** tripu se této hodnoty netýkají.

Přesný default při vypnutém O je převzat z IEEE/ANSI 754-1985 §7.3,
tištěná p. 11 / file 17: OFF saturuje na největší konečnou absolutní
hodnotu; UP/DOWN saturují na konečnou mez na příslušné straně, jinak
dávají správně znaménkové nekonečno. NEAR dává nekonečno. Jde o
**výslovnou externí závislost** MMIX konvencí, nikoli samostatnou
MMIX větu obsahující všechny hexadecimální výsledky.
Primární normativní sazba byla prohlédnuta, uložena jako
`sources/ieee754-1985.pdf` a `images/ieee754-1985-file017.png`;
[zdroj](https://www.ime.unicamp.br/~biloti/download/ieee_754-1985.pdf#page=17).
Nepřenáší se sem pozdější změna standardu ani požadavky na přenos
exponentu do zapnutého handleru.

## Platný architektonický případ

V uživatelském programu je rA=#10000, všechny tři dotčené registry jsou
globální (např. rG=32, X=253, Y=254), efektivní adresa A=#1000 je
zarovnaná, zapisovatelná a bez paměťových výjimek. V registru X je
`#47f0000000000000`, přesné kladné 2^128. STSF $253,$254,0 má uložit
největší konečný binary32 výsledek:

```text
(2 − 2^−23) 2^127 = 2^128 − 2^104,  bits #7f7fffff.
```

Mez exponentu binary32 je 127; 2^128 je konečný binary64 vstup a neleží
v cílovém konečném rozsahu. Znaménko je kladné, proto OFF musí zmenšit
velikost, nikoli vyrobit +∞. Výsledné event bity mají být O|X=#09;
celé rA tedy #10009. Žádný trip nemůže dodatečně výsledek upravit.

Toto je rozpor programu s uvedeným MMIX→IEEE kontraktem, pokud program
uloží #7f800000. **Není** to nové tvrzení o vadě správné souhrnné definice
STSF v sazbě fasciklu. Osobitá autorova politika zmrazení MMIXware 1.0
se zaznamenává: nevytváří jiné pravidlo pro OFF v původní dokumentaci
a opravená distribuce 2025 obsahuje stejný packer. Původní soubory se
nemění.

## Vypnuté versus zapnuté výjimky

Reprodukce a případná oprava se omezí na **vypnuté všechny arithmetic
trips**. Pak je následný stav plně určen: výsledek v paměti/registru,
O|X v rA, běžný následující programový čítač. Při zapnutém O přechází
řízení na #50 a handler může výsledek změnit; při zapnutém pouze X
na #80. Tento blok nedokazuje plnou IEEE semantiku předávaného
exponentu ani libovolných handlerů a nepoužije je jako svědky chyby.

V simulátoru rA=#10000 nastaví `cur_round=ROUND_OFF` přes ř. 2235.
STSF na ř. 2160–2162 přímo ukládá výsledek `store_sf` a přebírá jeho
exceptions. Ř. 2586–2592 při našem rA nevolá handler, pouze ORuje
`exceptions>>8`; výsledné slovo se znovu nezaokrouhluje. Tak je vyloučeno,
že by šlo jen o nehotový interní výsledek pomocné rutiny, který dispatcher
později správně saturuje.
