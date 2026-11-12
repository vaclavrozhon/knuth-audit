# Schwartz 1963: vedlejší minima a kanonický prefixový kód

Datum: 2026-11-02. Dotčené jednotky: hlavní text §2.3.4.5 na 404
a úloha 4 s odpovědí na 595. **Nový přímý autorský doklad** pochází
z technické zprávy z roku 1963. Konkrétní časopisecké verze
Information and Control 7 (1964), 37–44, a CACM 7 (1964), 166–169,
nebyly získány ani přečteny; jejich přesná verzová shoda zůstává
`source-partial`. Zpráva přesto podstatně zužuje původní mezeru:
technický obsah i Kallickův podíl nyní mají dobový primární doklad.

## Pramen a skutečně přečtený rozsah

Eugene S. Schwartz, *An Adaptive Information Transmission System
Employing Minimum Redundancy Word Codes*, ASD-TDR-62-265, Part II,
1 June 1963, Armour Research Foundation of Illinois Institute of
Technology, DTIC AD0404463. Název, autor, datum a číslo zprávy jsou
na přímo prohlédnutém titulním listu, PDF 3.

[Veřejný původní sken](https://archive.org/download/DTIC_AD0404463/DTIC_AD0404463.pdf)
je uložen jako `sources/schwartz1963-dtic.pdf`, 7664622 bytů,
257 PDF stran, SHA-256
`128fdaa2c225de11950b1f4247a3f0a281995a1e17ea13d07f5311aca073f3ad`.
Metadata i přesná síťová provenience jsou v
`sources/schwartz1963-dtic-metadata.json` a `sources/retrievals-72.json`.
Soubor je veřejný, bez omezení výpůjčkou; u jiných nalezených
archivních položek níže tomu tak není.

Přímo přečteny obrazy: titul PDF 3; předmluva PDF 5; abstract
iii/PDF 6; obsah iv–v/PDF 7–8; **všechny 39–55** (PDF 53–69),
**všechny 170–176** (PDF 184–190), diagramy **213–216**
(PDF 227–230), bibliografie 240–241 (PDF 254–255).
Obrazy mají názvy `images/schwartz1963-file-NNN.png`; kopie
diagramů s příponou `-reading.png` jsou pouze otočeny pro čtení.
Zbytek zprávy nebyl přímo přečten a není zde certifikován.
Knižní originály 404, 594 a 595 byly při tomto doplňku znovu
zobrazeny z frozen `../tree-path-length/images/`.

Předmluva rozlišuje tuto zprávu od prvního výstupu projektu
z 1 April 1962, který má stejné základní číslo ASD-TDR-62-265,
ale označení Part I na něm nebylo. Rok 1963 proto nelze nahradit
rokem 1962 jen podle čísla zprávy. Předmluva výslovně připisuje
Bruceovi Kallickovi základní vývojové diagramy kódovacího postupu,
Antanasi V. Dundsilovi jeho naprogramování a Leonu Westerovi
příspěvek k analýze bottom merging. To je dobové svědectví
o těchto konkrétních příspěvcích; nepřidáváme tvrzení o výlučné
prioritě jednotlivých autorů.

## Přesné pravidlo rovností a minima

Prefixový kód je soubor konečných binárních slov, v němž žádné
slovo není vlastním začátkem jiného. Jeho strom má kódová slova
v listech. Zpráva používá pravděpodobnosti `p_i` nebo úměrné
frekvence `f_i`, délky slov `L_i` a největší délku `Lmax`.
Primární optimum minimalizuje `sum p_i*L_i`; sekundární minima
jsou `sum L_i` a `Lmax` mezi primárními optimy. Jde o
pravděpodobnostní/frekvenční doménu, nikoli o výslovnou větu pro
záporné váhy.

Na 48 je bottom merging definováno přesně: nově spojenou váhu
vložíme **za všechny již přítomné stejné váhy** v rostoucím
seznamu. To zachovává přednost původních listů a pořadí dříve
vytvořených vnitřních uzlů při rovnosti. Na 47–50 následuje
argument přes zaplnění úrovní a přesun chybějících pozic; závěr
na 50 je současná minimalita obou sekundárních veličin.
Abstract iii totéž výslovně shrnuje. Na 52 se pravidlo opakuje
pro dávkové spojování a diagram 2 na 213 při vkládání nové váhy
přeskočí i rovné starší váhy.

Obrázek 9 na 51 ukazuje frekvence `(1,1,2,2,4,4,4,4)`.
Všechny tři zobrazené stromy mají primární součet 64; pro
top merging vycházejí `(sum L_i,Lmax)=(27,5)`, pro prostřední
volbu `(26,4)` a pro bottom merging `(25,4)`. Přímé sečtení
hloubek z obrázků souhlasí. Tato ilustrace sama není důkazem
obecného minima; vlastní obecný důkaz již tvoří první oddíl
frozen `../tree-path-length/notes/generalizations.md`.

Zprávu používáme jako primární doklad formulace, pravidla
rovností a atribuce. Její stručný argument o deficitech úrovní
nezaměňujeme za nový úplný audit všech jeho implicitních kroků;
již předaný vlastní důkaz ani úspěšné výpočetní kontroly se
neopakují. Obecnější knižní doména a Markowského konvexní
kritérium nejsou tímto pramenem doloženy.

## Kanonická konstrukce a vztah ke knižní úloze 4

Na 54–55 je kanonický kód definován i zkonstruován: slova se
vypisují od nejkratších, v rámci jedné délky v rostoucím binárním
pořadí, s nejmenšími hodnotami slučitelnými s prefixovou podmínkou.
Počty slov každé délky získá předchozí průchod stromem. Diagram 4
na 215 a jeho popis na 173 upřesňují stručný text na 55.

Položme `b_l` počet slov délky `l` a `s_l` hodnotu prvního
disponibilního slova této délky, chápanou jako celé číslo
zapsané přesně `l` bity. Pro více než jeden list dává konstrukce

```text
s_1 = 0;
slova délky l: s_l, s_l+1, ..., s_l+b_l-1;
s_(l+1) = 2*(s_l+b_l).
```

Prázdná skupina `b_l=0` pouze posune hodnotu doleva. Po neprázdné
skupině diagram nejprve přičte jedničku k poslednímu slovu a pak
posune výsledek doleva; slovní formulace na 55 tedy není pokyn
k prostému přičtení dvojky bez posunu. Přední jednička uložená
v programu je pomocná značka délky, není součástí vysílaného
slova. Případ jediného listu s prázdným slovem řeší vlastní
knižní argument zvlášť; diagram začíná délkou 1.

Pro kontrolu vztahu ke knize stačí následující obecný argument.
Kódové slovo s hodnotou `a` a délkou `l` odpovídá intervalku
`[a/2^l,(a+1)/2^l)` v `[0,1)`. Rekurence skládá intervalky
těsně vedle sebe; celková délka je Kraftův součet
`sum b_l/2^l=1`. Žádné dvě vnitřní části se nepřekrývají,
takže žádné slovo není začátkem jiného. Získaný strom je úplný.
Přiřazení nejkratších slov největším frekvencím zachovává
Huffmanovy délky a tím primární optimum. Obrácení všech levých
a pravých hran pak dá rostoucí pořadí vah zleva doprava přesně
požadované úlohou 4. Při stejných vahách lze jejich pořadí zvolit
libovolně. Tento převod přesně odlišuje orientaci kanonického
kódu zprávy od zrcadlové orientace knižního obrázku na 595.

Konkrétní obrázek 10 na 53 při frekvencích
`(2,2,2,3,3,4,6,9,12,30)` dává slova
`0,100,101,1100,11010,11011,11100,11101,11110,11111`;
v tabulce rostoucích frekvencí jsou vypsána v opačném pořadí.
Jejich délky mají součet 41. Nejde o jinou optimalizační úlohu
se závazným původním pořadím libovolných nesetříděných vah.

## Co zůstává otevřeno

Přímý autorský obsah obou konstrukcí a Kallickův výslovně
uvedený podíl jsou tímto doplňkem `checked`. Přesné znění
časopiseckých článků z roku 1964 a jejich případné změny vůči
zprávě zůstávají `source-partial`. Původní CACM březen 1964 byl
identifikován až na položku
`sim_association-for-computing-machinery-communications_1964-03_7_3_0`,
ale její PDF i OCR jsou výslovně soukromé; nebyly staženy.
Přístupové podklady jsou v `sources/retrievals-62.json` a `-63.json`.
Markowsky 1981 je nadále oddělená mezera. Žádný nový nález
v TAOCP se tímto doplňkem nepotvrdil.
