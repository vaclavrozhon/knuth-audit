# §1.3.2′ — úlohy 27–35, individuální argumenty a otevřené části

Zadání p. 47–51 / file 55–59; odpovědi p. 109–113 / file 117–121.
Převzaté uzavřené výsledky svazku 1 se nepřepočítávaly. Dvě krátké
cílené kontroly proběhly s nice 15, nikoli jako plošný census.

## 27 — Fibonacciovy aproximace

`verify_fibonacci27.py` zaokrouhluje kladné normální binary64 hodnoty
přesnými racionálními čísly: po určení exponentu zaokrouhlí 53bitovou
signifikandu k nejbližšímu sudému celému. FSQRT(5) vybere sousední
hodnotu porovnáním čtverce jejich středu s 5. Nejde o závislost na
hostitelském floating point ani o MMIX simulátor. Výsledky jsou v
`results/fibonacci27-exact.json`.

(a) `sqrt(5)` má bity 4001e3779b97f4a8, vypočtené φ pak
3ff9e3779b97f4a8. INCH #fff0 sníží exponent o jednu, tedy přesně
vydělí kladné `1+sqrt(5)` dvěma. φ je mírně větší než přesná hodnota:
například jde přímo ověřit znaménko `φ²−φ−1>0`; kladný kořen je φ.
Počáteční old=0 plyne z nevyplněného GREG. Indukčně new a old tvoří
sousední Fibonacciova čísla; acc se každý krok zaokrouhleně násobí φ.
Případy n=0,1 se zaokrouhlí správně. Všechna porovnání do n=70
souhlasí; pro n=69,70 jsou chyby přesně 1/4 a 13/32. V n=71 je
acc = 308061521170129 + 11/16, takže FIXU vrátí 308061521170130.
To dokládá i knižní přibližné „F71+.7“ a nejmenší index 71.

(b) Konstantu phii přebírám z C0001: je správně zaokrouhlená aproximace
φ−1, navzdory chybné slovní formulaci o prvních bitech. MULU dá přesný
součin ve dvou slovech. GET/ADDU vytvoří `old+floor(old*phii/2^64)`;
CSN přičte 1 právě když spodní slovo je nejméně `2^63`. Tento konkrétní
postup tedy zaokrouhluje poloviny nahoru. Krátký celočíselný průchod
všemi požadovanými indexy 3–93 souhlasí s přesnými F_n. V n=94 dojde
dříve k unsigned přetečení: `F93=12200160415121876738 < 2^64`,
`F94=19740274219868223167 > 2^64`; zabalená hodnota
1293530146158671551 je menší než předchozí new. CMPU proto vrátí −1
a program končí před testem aproximace, přesně jak uvádí odpověď.

## 28 — magický čtverec

Přebírám obecný důkaz `workstreams/vol1/notes/mixal-magic-square.md`:
pro `n=2h+1`, číslo `nq+s+1` leží v souřadnicích
`(h+1+q+s,h−q+s) mod n`. Inverze 2 modulo n dokazuje bijektivitu;
řádky, sloupce a obě diagonály mají součet `n(n²+1)/2`. Vzorec také
dokazuje právě každou n-tou kolizi a opravu posunem o dvě pole dolů.
Pro n=19 je součet `19*362/2=3439`; hodnoty 1–361 potřebují tři cifry.
Obrázek řádu 7 je totožný s již ověřeným obrázkem svazku 1.

Historie a omezený rozsah pramenů jsou převzaty z `mixal-magic-sources.md`:
Ibn al-Haythamův postup je tentýž až na rotaci, životopisný údaj je
podložen, celá kapitola Ball–Coxeter 1939 nebyla auditována.
**Partial:** požadovaný úplný MMIX program včetně formátování 19×19
není v knize dodán ani zde nově implementován. Hotový MIX program
svazku 1 se nepovažuje automaticky za MMIX program.

## 29 — Josephus

Z `workstreams/vol1/notes/mixal-josephus.md` přebírám důkaz kruhového
seznamu, význam vytištěného pořadí i nezávisle doložený výsledek:

    15 12 22 08 16 11 23 21 03 05 01 17 10 07 24 19 20 18 09 14 04 02 13 06

Jsou to pořadí odstranění na původních pozicích; poslední člověk je
na pozici 15. Pro n=8,m=4 stejná konvence dává 54613872, tedy souhlasí
obrázek i zadání. Převzatá rekurence pořadí mezi dosud živými je
`b1=(m−1) mod n`, `b(j+1)=(bj+m−1) mod(n−j)`. Skládání map volných
pozic je asociativní a vyvážené slučování dává O(n log n) slovních
operací; stejné zrychlení poskytne strom s počty živých listů.
Bibliografie Ahrens 1918, kapitola 15, je převzata v původním vymezeném
rozsahu. **Partial:** knižní MMIX odpověď je výzva k doplnění programu
s prázdným časem, nikoli úplná implementace; MMIX převod a jeho přesný
čas zde zatím nejsou vytvořeny.

## 30 — harmonické součty se zaokrouhlením k sudému

Zde nelze bez úpravy převzít MIX součty: MIX úloha zaokrouhluje poloviny
nahoru, MMIX k sudému. Označme M=10^n. Rovnost `M/j=q+1/2` znamená
`j(2q+1)=2M`. Lichý faktor `2q+1` musí být `5^h`, h=0,…,n; pak
`q=(5^h−1)/2` je vždy sudé. Všech přesně n+1 takových půlek se proto
zaokrouhlí dolů. Pro ostatní členy se pravidla neliší. Platí tedy přesně

    scaled_sum_even = scaled_sum_up − (n+1).

To současně dokazuje platnost knižního `ceil(M/j−1/2)` pro převrácená
celá čísla, nikoli jako obecný předpis pro libovolné x. Skupina se
škálovanou hodnotou r je `2M/(2r+1) ≤ j < 2M/(2r−1)`. Poslední index
je `floor((2M−1)/(2r−1))`. Po již započteném indexu m dá krok 2H
`floor((2M+m)/(2m+2)) = ceil(M/(m+1)−1/2)`. Kladné r určí novou
skupinu, příspěvek `(mm−m)r` přidá právě dosud nezapočtené členy.
R=0 zastaví smyčku dřív, než by se dělilo záporným 2R−1.
Pro n=5,r=1 je interval 66667–199999 včetně, tedy 133333 členů.

`verify_harmonic30_transfer.py` převezme uložené součty a počty skupin
z `workstreams/vol1/results/rounded-harmonic.json`; neprovádí nové
sčítání milionů členů. Kontroluje jen 65 půlek pro n=1,…,10 a změnu
dvou sousedních hranic skupin u každé z nich. Počet neprázdných skupin
se tím pro žádné z deseti n nezmění. Výstupy v
`results/harmonic30-transfer.json` přesně souhlasí se všemi deseti
knižními hodnotami; poslední je 24.5665766342.

Tisk začíná newline na pozici n+1 vpravo od dec a vypisuje cifry zprava.
`BZ a,@-4` při nule zopakuje SUB a přeskočí desetinnou tečku na dec.
V původní sazbě BYTE obsahuje **tři** mezery a tečku; dec=@+3 je
správně. OCR může vložit mezeru navíc. Zbytky po DIV 10 jsou 0–9,
přidání '0' je ASCII cifra. Další n přepíše předchozí newline a poslední
nulový bajt z původně nulové paměti stále ukončuje řetězec.

Přesný profil: je 292472 skupin po první, 72 tištěných číslic a deset
newline. Jeden úplný průchod skupiny stojí 139υ: bloky 3H,4H,2H mají
63,13,63. Počáteční/neúspěšné testy, tisk a vnější smyčka dávají
`139*292472 + 66*72 + 99*10 + 9 = 40659359υ`.
Koeficient 66 na cifru zahrnuje DIV 60, GET/INCL a čtyři instrukce
ukládací větve; zvlášť je započteno přeskočení tečky a poslední špatně
predikovaný skok. Paměťové instrukce jsou jen 72+10 STB, tedy 82μ.
Knižní přesný čas je správný v modelu tabulky 1, bez hostitelských I/O časů.

Pro n≤17 je `2M<2^58`; dyadická mez `H_(2M)≤59` a zaokrouhlovací
chyba nejvýše 1 dávají `M*S_n≤60M≤6*10^18<2^63`. Ostatní mezivýsledky
jsou nejvýše 4M, případně konečné c*10≤2*10^18, takže ani ty
nepřetečou. Počet skupin je Θ(sqrt M): pod √M je nejvýše √M indexů,
nad ním nejvýše √M různých hodnot; prvních řádově √M podílů je naopak
navzájem různých. To dokazuje řád `10^(n/2)`.

Známé erratum z 2023 mění poslední vzorec odpovědi na
`Rn(1/m_(k+1))=Rn(1/m_k)−1`. Pro velké m se sousední přesné hodnoty
liší o méně než 1, takže mezi nenulovými skupinami nemůže být přeskočena
celá škálovaná hodnota. Přímé sečtení malých indexů odstraní jedno
z dvojice drahých dělení. Odhad „asi polovina“ není tvrzení globálního
optima pro všechny pipeline.

## 31 — limita

Přebírám obecný důkaz ze svazku 1, `mixal-rounded-harmonic.md`, oddíl
„Úloha17“. Výsledkem pro poloviny nahoru je
`S_n=n ln10+2γ−1+2 ln2+O(10^(−n/2))`. Právě dokázaná úprava
`−(n+1)/10^n` je menšího řádu, takže tentýž hlavní člen i chyba platí
zde. Odečtením dvou sousedních n plyne požadovaná limita ln10.
Převzatý hlavní člen pro n=10 je 24.56657662086342, tedy zaokrouhlený
údaj 24.5665766209 na p. 111 je správný.

## 32 a 33 — Velikonoce

Celý kalendářní důkaz, minimální rok chybného záporného zbytku, přesná
perioda i uložené četnosti jsou převzaty z `workstreams/vol1/notes/mixal-easter.md`
a `results/mixal-easter.json`; žádná enumerace 5 700 000 let se neopakovala.
Jde o stejný algoritmus E a stejná pravidla zaokrouhlení/modulo.

Konkrétně `D=Y+floor(Y/4)−floor(Y/100)+floor(Y/400)+2`, takže
`(D+N) mod 7` opravdu určuje březnový den týdne. E7 přidá nejmenší
kladný počet dní k neděli. Algebraická shoda s nezávislým kalendářním
pramenem zahrnuje epaktové výjimky E=24 a E=25,G>11. První špatný rok
je 10317; předchozích jedenáct hraničních roků `10108+19k` nezmění
následující neděli. Příklad 14250 dává chybně 42 APRIL. Důkaz periody
5 700 000 i její minimality a četnosti 27550,220400,42000 jsou převzaty
s již uzavřeným rozsahem, stejně jako obecná dělitelnost četností 25.

MMIX umožňuje podlahové DIV přímo; ve zadaném rozsahu Y<100000 jsou
všechny mezivýsledky malé signed integers. Pro navržené dělení 100
pomocí násobení konstantou `floor(2^64/100)+1` platí přesné kritérium
`100Y<2^64`, takže jde o správný nápad. FREM vrací remainder k
nejbližšímu podílu; pro běžné nezáporné modulo je nutné případný záporný
výsledek přičtením modulu opravit. Odpověď dává nápady, ne hotový kód
bez této úpravy ani důkaz celosvětové nejrychlejší implementace.

**Partial pro 32 i 33:** chybí vlastní úplný MMIX program a formátování
požadované tabulky/vyhledání; původní MIX provedení se za ně nevydává.
Historické meze, včetně opakovaných výskytů již evidovaných nálezů
V1-C0025 a V1-C0026 na MMIX p. 111, jsou zvlášť v
`notes/repeated-vol1-findings-p111.md`. Nová finding ID se nezakládají.

## 34 — semafory

Nejdřív aplikovat známou opravu 15. 3. 2024: závěrečné
`MUL delay,rho,18` musí být `MUL delta,rho,18`. Je v původních erratech
i obou textových vrstvách; nejde o nový nález. Bitová pole D/B a pěších
jsou disjunktní, takže OR vytvoří právě předepsané kódy. Všechny řetězce
mají jeden nenulový řídicí bajt a terminátor; Fputs tedy odešle jeden bajt.

Po opravě dává řídicí tok pro stálý požadavek přechody v časech
0,18,30,38,46,58,63 sekund: Del Mar nejprve 18 WALK a 12 blikání,
8 amber, Berkeley 8 WALK a 12 blikání, 5 amber. Bez požadavku se
Wait prodlouží libovolně a Del Mar zůstane zelená. Flash je osm dvojic
půlsekund a pak čtyři sekundy DON’T WALK; pro liché ρ je odchylka
zaokrouhlení osm taktů, v uvedené toleranci. Čtení sensoru po Berkeley
zelené zahodí již obsloužené požadavky, novější amber/red požadavky
zůstanou do následujícího Wait. Okamžitá mez mezi přepnutím amber a
čtením patří do autorovy výslovně přiznané malé časové odchylky.

**Aktualizace recovery 7.11.2026:** následující starý závěr je příliš
silný a je odvolán. `MMIX-C0020-delay-reset-loop.md` dokazuje nekonečný
resetový cyklus při ref_time0 i1 za přípustného rychlého OS. Samotné
`0≤delta<2^63` tedy nestačí. Následující odstavec je archiv původního
neúplného argumentu, nikoli aktuální potvrzení obecné správnosti:

Delay je správně modulární při `0≤delta<2^63`: pokud se do zbývajícího
rI vejde, uloží ref=rI−delta a signed SUBU testuje zbývající vzdálenost.
Při kladném rI<delta odečte dostupný čas, čeká na zvýšení rI resetem a
pokračuje se zbytkem. Při rI≥2^63 se malé delta vejde vždy. Pouhé CMPU
by při přechodu čítače přes nulu nebylo totožné s modulární vzdáleností.
**Partial:** obecné záruky závisí na době přerušení, konkrétním resetu
rI a latenci I/O; předpoklad „soon“ nebyl převeden na číselnou horní mez.
Není doloženo jednotné „few hundred υ“ pro všechny takto popsané OS.

## 35 — křížovka

Přebírám důkaz odstranění vnější černé komponenty a číslování z
`workstreams/vol1/notes/mixal-crossword.md`: změna 1 na −1 prodlužuje
cestu k obvodu, všechny takové cesty se postupně vyplní a konečnost
plyne z poklesu počtu jedniček. Sousednost znamená společnou stranu.
Začátky jsou právě bílé buňky s bílým následníkem a nebílým předchůdcem;
sjednocení vodorovných a svislých začátků čísluje dvojí začátek jen jednou.
V obrázku je stejných 14 začátků jako v přijaté tabulce svazku 1.

MMIX verze obrázku používá METAPOST. Vnější vodorovné úsečky nahoře
a dole mají souřadnice j=2…6, prostřední j=1…7; odpovídají odstraněným
rohům. Svislé úsečky jsou jejich analogie. Čtyři black(2,3),(3,5),(4,2),
(5,4) jsou právě zbývající vnitřní černá pole. Seznam 14 popisků souhlasí
s podmínkou číslování. Transformace otočením −90° posílá `(i,j)` na
`(j,−i)`, takže j roste vpravo a i dolů; měřítko 17pt zachová čtverce.
Doplnění příkladu na 25×25 jedničkami přidá pouze vnější černou oblast,
proto obrazec nezmění. První řádek je 100001 a dalších 19 jedniček.
**Partial:** nový úplný MMIX převod 25 vstupních řádků na METAPOST není
implementován a nebyl spuštěn METAPOST/fontový renderer. Matematická
správnost masky a popisků není tvrzení o provedeném end-to-end testu.
