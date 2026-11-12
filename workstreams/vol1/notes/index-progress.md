# Hlavní rejstřík a slovník: průběžná evidence

1. listopadu 2026. Přímo přečteno všech23 původních stran628–650,
včetně úvodní poznámky, Swiftova a Hobbesova citátu a tiráže650.
Výsledkem zatím není uzavřená kontrola všech cílů ani historických
tvrzení. X0596 zůstává partial. Obrázky jsou `images/index-p*.png`.

`index_navigation.py` zachovává všechny OCR řádky s jejich souřadnicemi
a seskupuje je podle odsazení. Výstup má provizorně2089 hesel a podhesel,
6265 jednotlivých možných stránkových odkazů po rozvinutí rozmezí.
Tyto počty nejsou tvrzením o bezchybné transkripci: OCR nezachovává
spolehlivě řecké, arabské či jiné znaky a někdy ztrácí číslici.
Některé odkazy uvnitř slovníkových vět nejsou zachyceny automaticky.
Samotné strojové nalezení slova na cílové straně není obsahový důkaz.

## Rozsah prvního přímého průchodu

Byly přečteny všechny řádky, matematické symboly a definice.
Definice odpovídají zkrácenému slovníku knihy: například kofaktor
je determinant po nahrazení vybraného prvku1 a ostatních prvků jeho
řádku nebo sloupce0; rozvoj determinantu skutečně dává správné
znaménko. „Proper divisor“ výslovně požaduje1<x<y, takže nejde
o neurčitou záměnu s jinými učebnicovými konvencemi. Velikost slova
MIX se výslovně týká pěti bajtů; samostatné znaménko do této definice
nevstupuje. Krátké heslo „Ordering“ neprohlašujeme za plnou náhradu
formální definice uspořádání v §2.2.3.

Zjevné starší nesrovnalosti mají známé opravy: dvě různé osoby
Conway, nesprávné691 u desetinné soustavy,110 u kořene stromu,
rozsah tabulky harmonických čísel i doplnění některých odkazů.
Celé textové seznamy změn all1-prepre48–50 a all1-pre19–20 byly
přečteny; jejich vizuální a položková integrace ještě pokračuje.
Novější seznam all1-16/err1-14–15 se přebírá zvlášť.

Na644 se v malém zobrazení a OCR zdálo být „resting“ místo
„restoring“. Přímý300dpi obraz `images/index-p644-detail.png`
jednoznačně obsahuje správné „restoring“. Nejde o chybu knihy,
nevznikl kandidát. To je konkrétní důvod ponechat OCR jen navigací.

Úvodní poznámka628 výslovně omezuje indexování odpovědí: odkaz na
zadání zároveň odkazuje na jeho odpověď; odpověď se zvlášť indexuje,
jen když přináší nové téma. Chybějící samostatný odkaz na každou
odpověď proto není automaticky opomenutí.

## Otevřená práce

- Přesně porovnat všechny cíle a odkazy „see“, započítat nové a
  nahrazené položky čtyř vrstev. Posun rejstříku2011 o2 strany
  nemění čísla stran hlavního textu; cíle do rejstříku se mění.
- Ověřit dvě původní citace. Některé přímé požadavky na primární
  skeny selhaly403/404; nejsou vydávány za přečtené prameny.
- Prověřit údaj o vydavateli AMM. Oficiální historie MAA potvrzuje
  vznik časopisu1894 a pozdější vznik MAA v prosinci1915, zatímco
  heslo628 spojuje vydávání MAA s1894. Zatím jde o otázku k vyjasnění
  přesného znění, nikoli zaregistrovaný potvrzený nález.
- Samostatně zachovat dosud chybějící úvodní stranyxv–xvii,
  na které rejstřík odkazuje. Čtení rejstříku tuto zdrojovou mezeru
  neuzavírá.

Pramenné pokusy jsou v `sources/index-historical-retrievals-*.json`.
[Oficiální historie MAA](https://maa.org/history-of-the-american-mathematical-monthly/)
byla přečtena webovým nástrojem; přímé lokální stažení HTML dostalo403.
Historické předávání vydávání se proto nesmí vydávat za místně
uložený a vizuálně přečtený původní ročník časopisu.

## Doplnění po získání dobových skenů

Všechny obrazové seznamy změn jsou nyní přímo přečtené: navíc
all1-prepre48–50, all1-pre19–20 a err1-15. X0649 eviduje známé
změny; obsahová kontrola všech nových cílů zůstává součástí
pokračujícího indexového průchodu, nikoli automatickým důsledkem čtení.

Následně byly získány původní AMM1894/1916 a Swift1704.
Jejich konkrétní čtecí rozsahy, limity a závěry jsou v
`index-historical-root-review.md`. C0075 potvrzuje nesprávné
spojení vydavatele MAA s1894; C0076 pouze kandidátsky eviduje
adaptovaný úvod Swiftova epigrafu. X0650 dokládá nalezení citátu
v přesně identifikovaném třetím vydání1704. Hobbes ještě zbývá.

X0653 následně uzavírá Hobbesův citát: původní titul1656 a tištěná4
jsou přímo přečteny. Výpustka a modernizace pravopisu jsou v pořádku;
kratší název je doložen také před vznikem TAOCP. Podrobnosti a přesné
meze čtení jsou ve výše uvedené historické poznámce.
