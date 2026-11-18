# Úplný zdrojový průchod 7.2.2.1–189–192

3. 11. 2026. Přečtena celá zadání na str. 148 / PDF 168 a odpovědi na
str. 469 / PDF 489, včetně historického odstavce a obrázku. Autorův draft:
str. 84 / PDF 90 a str. 173 / PDF 179. Přijaté starší výpočty se neopakovaly.
Nová kontrola trvala 1,30 sekundy, nice 15, bez solveru.

## 189: obecný odhad a nové omezení parametrů

Dřívější obecný důkaz v [EXTREME_COVER_NOTES.md](EXTREME_COVER_NOTES.md)
zůstává platný po opravách F020–F022 a C006. Křížový odkaz 4A
7.2.1.5–(24),(26), str. 422, byl nyní přímo zobrazen. Jeho Bellova
asymptotika má právě potřebný index n−1 a faktor `sqrt(n(ξ+1))`.
Jako vstup se přebírá, celý cizí svazek tím neoznačujeme za prověřený.
V závěru je nutné vybrat `1<c2<9/8`, aby rezerva v exponenciále absorbovala
prefaktor `sqrt(ξn)`; knižní cíl potom plyne pro `ξ<ln n`.

Autorův článek Asakly et al. byl uložen z webu spoluautora; Theorem 1
na PDF 2 podporuje obecnou konvergenci a Corollary 4 na PDF 8 má správný
faktoriál `(k−1)!`. Tím je F022 znovu zdrojově doložena, bez nové kvadratury.
Primární metadata vydavatele pro DOI 10.1016/j.jmaa.2014.02.061 potvrzují
šest autorů, časopis, svazek 416(2), rok 2014 a strany 672–682.
Stažení mělo nejprve chybu certifikátu; veřejné PDF bylo následně získáno
bez ověření TLS certifikátu. Přesný postup a hash jsou v retrieval.json.

Nová **F142** je chybné `a,b>0` v historické definici Gompertzovy CDF.
Přesný protipříklad dává −1, správná doména je `a>1,b>1`.
[Samostatný krátký důkaz](F142_GOMPERTZ_DOMAIN.md). Nejde o další výskyt F022.

F020–F023 nadále nejsou opraveny v prohledaných šesti vrstvách.
Znění publikovaného errata 189(a) z roku 2019 je již v knižním PDF;
starý PS má starší, jinak chybné znění. C006 zůstává kandidátem jako
doplnění známého errata, nikoli nově připočtenou chybou. Matematická
oprava `exp(−exp(x)cos y)` je jednoznačná. Její klasifikace nezanechává
otevřenou část matematického důkazu 189.

## 190: celý obrázek s přesným znaménkem

Černá odpovídá kladnému rozdílu, bílá zápornému. Z původních vektorových
cest byly nezávisle dekódovány oba obrázky: knižní PDF slučuje buňky do
132 obdélníků, draft obsahuje 2522 jednotlivých černých čtverců.
Mřížka má krok 0,6 bodu; její rozměr a polohu určuje obvodová cesta.
Veškeré hranice jsou na mřížce, žádné překryvy ani buňky mimo trojúhelník.

Oba trojúhelníky čísel vznikají pouze sčítáním, s počátečními řádky
Bell `[1]` a Gould `[0]`, druhým Gouldovým řádkem `[1,1]`.
Pro všech `1≤k≤n≤100` byly porovnány přesné podíly s intervalem pro g.
**Všech 5050 znamének na verzi souhlasí**, 2522 kladných a 2528 záporných.

Interval používá pouze zlomky:

- `ln 2=2 Σ 1/((2j+1)3^(2j+1))`, 100 členů a geometrická mez zbytku;
- Eulerovu konstantu z `H64−ln64−1/128` a 32 Bernoulliho korekcí;
  další člen omezuje zbytek podle [DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii);
- identitu `E1(1)=−γ−Σ (−1)^k/(k k!)` a střídavou mez po 100 členech,
  viz [DLMF 6.6.2](https://dlmf.nist.gov/6.6.E2);
- 101 členů řady pro e a geometrickou mez kladného zbytku; `g=e E1(1)`.

Šířka intervalu je asi `5,81·10^−81`; nejmenší doložená vzdálenost
zkoumaného podílu od intervalu je asi `2,88·10^−35`. Úplné racionální
meze i dekódované řádky jsou v
[source-checked.json](results/gould189_192/source-checked.json).
Zdroj programu a jeho závislosti mají uložené hashe.

Starých 101 znamének pro n=4000…4100 bylo pouze převzato z
`results/gould_signs.json`: stabilita při 1000/1200 cifrách, nikoli
intervalový důkaz. Vytištěných 24 běhů znamének je shodných v obou
verzích. **Obecný výzkumný problém znamének jsme nevyřešili**;
kontrola formulace a publikovaných příkladů je dokončena.

## 191–192: pravděpodobnosti, momenty a chvosty

Všech devět vytištěných pravděpodobností v obou verzích odpovídá
zaokrouhlení již přijatých hodnot. Kladnost koeficientů je z integrálu;
`G(1)=∫e^(−x)(1+x)dx−1=1` zajišťuje normalizaci. První a druhá
derivace dávají střední hodnotu `1+g` a rozptyl `2g2+g−g²`.
F023 se týká pouze chybějící konstanty −e v alternativní gamma řadě.

Celé zadání i odpověď 192 souhlasí s dříve uloženým obecným Laplaceovým
důkazem: sedlo `x0=e^ξ−1`, šířka `σ²=n/(1+ξ)`, lokální Taylorův odhad
a oba chvosty omezené tečnami ke konkávnímu logaritmu integrandu.
Sedm numerických poměrů n=10…1000 zůstává podpůrnou evidencí, nikoli
náhradou tohoto důkazu; nic se znovu neintegrovalo.

## Historické zdroje a bibliografické rozdíly

Eulerův původní latinský sken E247 byl získán z Dartmouthu. Obsahuje
strany 205–237; na str. 230 / PDF 26, §25, je přímo uvedena přibližná
hodnota 0,59634736… . Překlad Alexandera Aycocka sloužil k navigaci,
rozhodující místo bylo zobrazeno v originále. [Archivní záznam](https://scholarlycommons.pacific.edu/euler-works/247/)
a basilejský index odlišují nominální ročník 1754/5 od vydání 1760.
Proto knižní rok 1754 neoznačujeme za nový omyl.

Gompertzův článek je nyní uložen celý z veřejné kolekce JSTOR přes
Internet Archive. Str. 513 obsahuje název a rok, str. 518 dvojitou
exponenciálu počtu přeživších; odpovídá transformaci do knižního tvaru
po normalizaci. Samotný článek končí na str. 583. Následující str. 584–585
obsahují jeho errata k článku z roku 1820, jsou archivována zvlášť a byla
také zobrazena. Knižní rozsah 513–585 zahrnuje tento navazující dodatek;
rozdíl proti katalogovému 513–583 zaznamenáváme bez dalšího F/C nálezu.
Není třeba z běžné bibliografické varianty dělat druhou matematickou chybu.

Rozsah historické kontroly jsou citované texty a jejich relevantní místa,
nikoli nezávislý audit celých historických článků nebo absolutního prvenství.

## Uložení a další krok

Všechna čtyři cvičení mají dokončený zdrojový průchod; 190 zůstává
nevyřešeným výzkumným zadáním, což není totéž jako neprovedená kontrola.
Jedna nová karta F142, anglicky, s krátkým ručním ověřením.
Staré karty, nálezy, programy a osobní anotace se zachovávají.
Vlastních 26 procesů pod 10 sledovanými kořeny má nice 15; žádný nový
dlouhý běh ani restart. Následuje 193–198. Svazek 4B není dokončený.

## Změna klasifikace C006 — 17. listopadu 2026

C006 je nově potvrzený nález. Dřívější vyloučení pouze kvůli tomu, že jde o doplnění publikovaného errata, bylo příliš opatrné: samotná náhrada z roku 2019 obsahuje chybný vzorec, neopravuje jej. Přímý rozpor 1/e versus e zůstává. Původní historii zachováváme; podrobnosti v [nové poznámce](notes/C006-exponential-modulus.md).
