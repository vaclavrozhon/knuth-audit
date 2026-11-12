# §4.3.2: historický a aplikační kontext

Kontrola2.11.2026 uzavírá text287/291–292 v níže vymezeném rozsahu.
Matematické důkazy a úlohy jsou v `modular-basic.md` a
`modular-convolution.md`. Původní stránky knihy byly vizuálně přečteny;
vyhledané bibliografické záznamy nejsou vydávány za přečtené články.

## Čínská věta a historické názvy

Erratum10.4.2021 přesouvá označení tai-yen od Sun Tsu k Ch’in
Chiu-Shaovi a zachovává nejistotu datování staršího díla. Oprava2004
mění název Needhamovy knihy na *Science and Civilisation in China*.
Všechny čtyři vrstvy errat byly porovnány.

Citovaný [Shenův článek1988](https://people.math.harvard.edu/~knill/crt/lib/Kangsheng.pdf)
byl čten v dostupné webové textové vrstvě na285–287 a290–292.
Popisuje Sunziho příklad se zbytky2,3,2 modulo3,5,7 a výsledek23;
obecné pravidlo Dayan qiuyi řadí k Qin Jiushaovu dílu z1247. Rozebírá
i moduly se společnými děliteli a jejich převod. To podporuje opravený
historický odstavec. Přímé stažení Harvard PDF vrátilo403, takže
jeho původní sazba zde nebyla vizuálně přečtena. Absolutní prvenství,
slovo „proved“ ve smyslu moderního důkazu ani přesné krajní roky
Sunziho datování nebyly samostatně doloženy z původních čínských tisků.
Needham, Li–Du a Dickson nebyli v tomto bloku čteni celé.

Vlastní aritmetická kontrola příkladu je okamžitá:
`2*70+3*21+2*15=233=2*105+23`, a23 má právě zbytky2,3,2.
Shenova historická interpretace není potřeba pro obecný důkaz CRT,
který je v `modular-basic.md` včetně společných dělitelů.

## Československá práce a další bibliografie

Dobová [zpráva Františka Svobody1955](https://dml.cz/bitstream/handle/10338.dmlcz/108165/CasPestMat_080-1955-2_14.pdf)
v *Časopise pro pěstování matematiky* byla lokálně získána; tištěné
255,257–258 byly vizuálně přečteny. Popisuje konferenci1.–3.12.1954
v Poděbradech, Valachovu reprezentaci zbytky a Svobodovu práci
s operátory a odhadem velikosti. Na258 oznamuje sborníkIII na podzim1955.
Podporuje tedy obsah a dobové zasazení knihy; dřívější přednáška není
rozporem s rokem tištěné publikace1955. Samotný článek247–295 nebyl
získán a absolutní prvenství není z této zprávy dokázáno.

Garnerova práce má dvě různé bibliografické podoby: sborník1959,
146–153, a časopis *IRE Transactions on Electronic Computers* EC-8,
140–147. Knuth cituje časopis; odlišné stránkování sborníku není chyba.
Sborník přes Bitsavers nebyl přístupný (403); neprohlašujeme jeho úplné
přečtení ani nezávislost objevu za ověřenou. Samotný Garnerův převod
byl zkontrolován obecným důkazem a přesnými výpočty.

[Fraenkelův vlastní seznam prací](https://www.wisdom.weizmann.ac.il/~fraenkel/)
uvádí článek o Mersennových prvočíslech a návrhu násobičky, JACM8
(1961),87–96; zároveň potvrzuje Borosh–Fraenkel1966,107–112.
[Schönhageův autorský seznam](https://pages.iai.uni-bonn.de/schoenhage_arnold/publis.html)
potvrzuje *Multiplikation großer Zahlen*, Computing1(1966),182–196.
Jde zde o bibliografické kontroly, nikoli audit celých těchto článků.

[Archiv Parametronu](https://www.iijlab.net/~ew/archivesindex.pdf), položka
na PDF straně2, rozlišuje japonskou práci Takahasi–Ishibashi1960,
78–86, od anglické1961,28–42. Knuthova citace anglické verze souhlasí;
samotný článek zde nebyl získán. Oprava2003 názvu Szabo–Tanaka
(*Its Applications*) je již známá. Ruská kniha1968, její recenze1970,
Barnardův literární citát a přesný historický rok objevu věty S nebyly
z původních publikací samostatně ověřeny. Rok časopisového zveřejnění
Szabovy práce1962 sám nevyvrací možné datování objevu1961.

## Přesné řešení lineárních rovnic

Dostupný text [Fraenkel–Loewenthal1971](https://nvlpubs.nist.gov/nistpubs/jres/75B/jresv75Bn1-2p67_A1b.pdf),
strany67–68, výslovně uvádí9 nezávislých řešení111 homogenních rovnic
ve120 neznámých, hodnost111, koeficienty v[-2180,2568] a čas19 minut
na CDC1604-A. To odpovídá knižnímu „less than20 minutes“. Číslo19 je
převzatý historický výsledek, nikoli naše měření. Článek popisuje konečnou
zkoušku dosazením; pouhé dva shodné mezivýsledky nejsou osvědčením.
Přímé stažení NIST PDF vrátilo403; použita byla webová textová vrstva,
neprovedena vizuální kontrola sazby ani spuštění historického Fortranu.

Vlastní matematické odůvodnění tvrzení knihy: racionální soustavu lze
vynásobením jmenovateli převést na celočíselnou. Pro čtvercovou regulární
matici A označme nenulový determinant Δ. Pro každé prvočíslo p, které
nedělí Δ, je A invertibilní nad polem zbytků modulo p. Cramerovo pravidlo
dává složky řešení jako podíly celočíselných determinantů. Zbytky těchto
podílů se tedy dají kombinovat čínskou větou.

Je-li známá mez B na absolutní hodnoty čitatelů a kladné jmenovatele
v základním tvaru, součin modulů M>2B^2 určuje každý podíl jednoznačně:
pro dva přípustné podíly a/b,c/d se stejnými zbytky dělí M číslo ad−bc,
ale |ad−bc|<=2B^2<M. Tedy ad=bc. Jmenovatele jsou nesoudělné s M,
protože jsme vynechali prvočísla dělící Δ. Taková B existuje například
z konečných determinantových mezí; tento argument netvrdí optimální
rychlost rekonstrukce. U obecné hodnosti se zvolí nenulový maximální
minor a volné proměnné; jen konečně mnoho prvočísel dělí tento minor.
Kontrola výsledné báze a pravých stran dosazením ověří získaná řešení.

Konečné číslo v pohyblivé řádové čárce je racionální, takže metoda se
na jeho **přesnou uloženou hodnotu** vztahuje. Neodstraňuje chybu
předchozího zaokrouhlení vstupů; u špatně podmíněné soustavy může být
rozdíl mezi uloženým a zamýšleným problémem velký. Tvrzení o rychlosti
na292 čteme jako dobovou motivaci a příklady, ne univerzální nerovnost
pro každou matici, počítač a požadovanou přesnost.

[Vydavatelský abstrakt Bareisse1972](https://academic.oup.com/imamat/article-abstract/10/1/68/724253)
potvrzuje srovnání eliminačních a modulárních metod a stránky68–104;
plný článek zde nebyl čten. McClellanova bibliografie1973,563–588 byla
nalezena, ale stránka ACM vrátila403; žádné konkrétní meze jeho článku
se zde nepřebírají. Nedostupnost pramenů nezaměňujeme za nesprávnost
algoritmu ani za ověřenou výkonnostní převahu.

## Uzavření a limity

Text sekce je matematicky zkontrolován a historické citace kriticky
porovnány v popsaném rozsahu. Bibliografické limity jsou trvalou součástí
evidence; „checked“ neznamená, že byl přečten každý citovaný článek či
ověřeno každé tvrzení o prvenství. Žádný nový potvrzený historický nález.
C0102 zůstává candidate pro formulaci modulárního půlení v úloze14.
Zdrojové adresy, hashe lokálních PDF a selhání jsou v
`sources/modular-fetch-2026-11-02.json` a doprovodném manifestu.
