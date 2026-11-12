# V1-X0778–X0780: původní pravděpodobnostní nerovnosti

Bienaymého citovaný výsledek z roku 1853 je doložen původním tiskem.
Kolmogorovův obecný princip a Bernsteinova exponenciální metoda jsou
obsahově doloženy přesně identifikovanými přetisky. Hlavní text
§1.2.10 zůstává partial: chybí hlavní článek Foster–Stuart, Roesova
citovaná strana, Haldova studie a některá přesná historická porovnání.
Všech 23 cvičení je již checked; zde nepřibývá další dokončené cvičení.

Root ověřil 87 souborů a 13 vstupů paketu
`parallel/analysis-primary-followup/remaining-history/MANIFEST.json`,
SHA-256 `0763342d059986c28bbbff57ce7101b225c1a065436c0362b034dcd843107122`.
Přečetl HANDOFF, UNIT_STATUS, poznámku a read-log. Zároveň přebírá
celý zmrazený archiv analýzy, 308 souborů, jeho závěrečný inventář
a všechny vstupní seznamy. Archivní převzetí nerozšiřuje již zapsané
rozsahy četby v X0759, X0766–X0767 a X0770–X0771.

## Bienaymé a relativní chronologie

Root přímo četl titul článku na 309 a celý citovaný argument na
320–321 původního Comptes rendus 37 (1853), PDF 319, 330–331.
Záhlaví dokládá zasedání 29. srpna 1853. Agent četl celý článek
309–324; jeho širší četbu nepřipisujeme rootovi. Zdroj je digitalizát
Natural History Museum Library přes BHL/Internet Archive:
https://archive.org/download/comptesrendusheb37acad/comptesrendusheb37acad.pdf.

Označme sigma² rozptyl jedné pozorovací chyby a v=(k/n)sigma²
rozptyl uvažované lineární kombinace. Práh je a=t sqrt(2sigma²).
Je-li p pravděpodobnost vnější oblasti a S její příspěvek ke druhému
momentu, původní argument píše S=fv=p a²/theta, kde 0<=f,theta<=1.
Případy nulového příspěvku se uzavírají přímo. Jinak tedy

```text
p = theta f k/(2t²n) <= v/a².
```

Jde o právě citovaný rozptylový odhad. Konečnost druhého momentu
je na 321 výslovná. Nezávisle jsme nekontrolovali numerické tabulky
článku ani všechna jeho tvrzení o nejmenších čtvercích.

Root dále četl první stranu Liouvilleova přetisku 1867, s. 158,
která potvrzuje původní zasedání a odstup čtrnácti let, a Čebyševův
článek 1874, s. 157 a úvod 158 včetně bibliografické poznámky.
Čebyšev sám přičítá metodu Bienaymému. Nesprávné 1833 a II
v tomto pozdějším zdroji nejsou nález v TAOCP; rok 1853 dokládá
původní tisk. Agent zvlášť četl formulaci a začátek důkazu
francouzského překladu Čebyševa 1867 na 177–179; root tuto četbu
neopakoval a ruský originál porovnán nebyl. X0778 uzavírá obsah
citace a tuto relativní chronologii, nikoli vyčerpávající světovou prioritu.

## Kolmogorov a Bernstein

Root přímo četl titul přetisku Springer 1973 a celý §3 na tištěné
37 (PDF 43) Kolmogorovových Grundbegriffe. Název staženého souboru
s rokem 1933 není důkaz fyzického prvního tisku. Agent navíc přečetl
reprodukovaný titul 1933, vydavatelské údaje a začátek 38 před §4.

Pro globálně nezápornou funkci f s f(x)>=b>0 při x>=a dostává
zdroj P(X>=a)<=E f(X)/b, pokud očekávání existuje. Jeho rovnice (2)
volí f(x)=exp(epsilon x), epsilon>0. To přesně podporuje obsah
TAOCP 104 a známou opravu globální nezápornosti z 30. října 2007.
Kolace se skutečným tiskem 1933 a absolutní slovo „first“ zůstávají
otevřené. Starší exponenciální speciální případ sám nevyvrací
prioritu této obecné formulace pro libovolné nezáporné f.

U Bernsteina root přímo četl titul Nauka 1964, autorovu a redakční
předmluvu a tištěné 71–73. Jde o svazek IV sebraných spisů připravený
autorem; redakční předmluva rozlišuje původní a nově připojené poznámky.
První strana článku uvádí přesnou bibliografii původních 38–48 z roku
1924. Pro nezávislé centrované veličiny, tedy veličiny se střední
hodnotou nula, strany 71–72 rozkládají očekávání exponenciály součtu
na součin a odhadují pravděpodobnost pomocí tohoto očekávání. Na 73
je aplikace na Bernoulliho veličiny s různými pravděpodobnostmi.
Agent navíc četl závěr 79; 74–78 byly pouze vykresleny. To dokládá
klíčovou myšlenku známého dodatku z 19. července 2012, nikoli audit
všech jeho numerických konstant. Přesný časopisecký tisk 1924 nebyl
získán ani kolacionován. X0779 uzavírá tyto obsahové atribuce.

## Přesné zbývající mezery

U Foster–Stuarta 1954 root četl obálku institucionálního otisku CWI
SP29 a jeho poslední stranu, tištěnou 22. Agent četl všech pět stran
souboru, obsahujících diskusi na 19–22. Je to příspěvek van Dantziga
a Hemelrijka s koncem odpovědi autorů, nikoli hlavní článek na 1–13.
Dokládá celý stránkový rozsah citace, ale ne původní rekordní formule.
Indexovaný text hlavního článku byl pouze navigace.

Roes1966, CACM9, 340–342, DOI10.1145/355592.365627 je bibliograficky
identifikován; konkrétní citovaná strana 342 o vyšších momentech
počtu rekordů chybí. Správný archivní sešit má omezené PDF i OCR.
Hald2000 zůstává ve stavu popsaném X0771. Neúspěšný přístup neznamená
neexistenci zdroje. Tyto mezery a výše uvedené meze priorit a edic
shrnuje X0780; hlavní text se proto neoznačuje za dokončený.

Root přímo četl původní TAOCP 98, 100, 104 a relevantní errata
all1-pre 8 a all1-prepre 11. Všechna čtyři úplná errata byla
prohledána podle obsahu i stran; výstup je v paketu. Zachovány
známé změny Paris2002, Roes2020, nezápornost2007 a Bernstein2012.
Nový nález nevznikl; C0013–C0015 a přijaté důkazy zůstávají beze změny.
Přijaté matematické testy se neopakovaly. Fyzický výtisk TAOCP
nebyl tímto ověřen.
