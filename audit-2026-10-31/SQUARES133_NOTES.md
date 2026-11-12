# DLX133–134: MacMahonovy čtverce a výskyty pentomin

Zadání na str. 139 i odpovědi na str. 450 byly zobrazeny. Matematický
počet skládání je potvrzen; úloha 134 přinesla [F133](F133_PENTOMINO_COUNTS.md).
Obě celé úlohy zůstávají `partial`, protože některé historické prameny
a konvence nákladů dosud nejsou doložené.

## Úloha 133

Burnsideův počet cyklických čtveřic nad třemi barvami je
`(3^4 + 3^2 + 2·3)/4 = 24`. Jejich 81 orientovaných podob a 24 pozic
dává před omezeními právě 1 944 možností. Barvy jsou po směru
obvodu buňky; reflexe dílků se do jedné cyklické třídy automaticky
neslučují. Odraz celé desky přesto zachovává úplný inventář.

Oprava z 16. ledna 2023 výslovně doplňuje odstranění možností
s nebílou stranou na obvodu. V našem dotisku tato věta chybí;
vedeme ji jako **E066**, nikoli jako nový nález. Opravený model
má 1 008 možností před geometrickou kotvou a 988 po ní.

Nezávislý konečný důkaz kotvy zapomene rozdíl mezi b a c. V inventáři
je 32 bílých stran, z toho 20 na obvodu, takže uvnitř musí být šest
bílých hran. Program `white_patterns133.cpp` prověřil všech
`C(38,6)=2 760 681` množin. Přesný bílý inventář splňuje 80 vzorů,
rozdělených do **20** čtyřprvkových geometrických orbit. Ve všech
je aaaa na obvodu. Čtyři zástupce jeho polohy volíme jako
`(0,0),(1,0),(2,0),(0,1)`. Žádná neidentická symetrie obdélníku
nefixuje obvodovou buňku. Následná společná záměna b/c je také volná.

Nativní výčet Algorithm C dává **13 328** modelů; nezávislý model
z geometrických koncových bodů hran a řešič s neměnnými konfliktními
bitovými množinami dávají **106 624** modelů bez normalizace. Celé
množiny se přesně shodují po rozšíření osmi symetriemi. Každý model
byl ověřen; všech 80 bílých vzorů skutečně připouští obarvení.
[Akceptovaný výsledek](results/squares133/accepted.json).

Ze 96 původních barevných výsečí obrázku byl získán úplný vektor
58 hran. Má všech 24 typů, 38 vnitřních shod a 20 bílých obvodových
hran a je obsažen v nezávislém úplném výčtu.
[Strukturální certifikát](results/squares133/structure-checked.json).

Nativní náklad je 14 983 652 077 hrubých memů, po odečtení
2 439 202 456 pomocných memů zbývá **12 544 449 621**. Hrubá hodnota
se zaokrouhlí na knižních 15 Gμ, čistá na 13 Gμ. Bez přesného
historického pořadí/konvence to neprohlašujeme ani za úplnou reprodukci
nákladu, ani za chybu. Změny pro omezení barev jsou uložené v samostatném
CWEB zdroji a patchi; zdroje ostatních běžících úloh se neměnily.

Převod jednotlivých ilustračních možností h/v na sudé/liché souřadnice
ještě vyžaduje přesně sjednotit konvenci názvů chirálních dílků.
Samotná jiná orientace názvů není protipříkladem k úplnému modelu;
z této poznámky nevytváříme nález.

## Úloha 134

Úplný cenzus maximálních monochromatických komponent dává pro
O až Z:

`0,1685,22,729,402,61,36,48,174,259,243,0`.

Dvě čísla se liší od knihy. [F133](F133_PENTOMINO_COUNTS.md) obsahuje
nezávislý krátký verifier a certifikát dolní meze bez jakéhokoliv
nového hledání. Zbývající deset čísel souhlasí. Rozdělení řešení podle
počtu pentomin je `0:10232,1:2572,2:486,3:37,4:1`.
Původní obrázek má světlé S a tmavé P,V, přesně podle zadání.
Čtyři pentomina v jediném řešení jsou P,P,W,Y.

## Primární prameny a další práce

MacMahonův [originál z roku 1921](https://archive.org/download/newmathematicalp00macmuoft/newmathematicalp00macmuoft.pdf),
tištěné str. 23–24, oddíl 17, výslovně zavádí 24 čtverců, počty
32 stran každé barvy a obdélník s jednobarevným obvodem. Obě strany
jsou archivované a byly zobrazené.

Stanfordský [institucionální katalog](https://i.stanford.edu/pub/cstr/reports/cs/tr/74/409/CS-TR-74-409.pdf)
byl získán jako [archivní kopie](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/1974/CS-TR-74-409.pdf).
Na tištěné str. 69 potvrzuje Feldmana, název, AIM12 a leden 1964,
ale uvádí čtyři strany proti osmi v knize. Bez originálního memoranda
není rozhodnuto, zda jde o jiné počítání příloh/obalu; není to nový nález.

Zbývají originály New Scientist 9 (1961), 288–289; Feldmanova memoranda
s údaji 12 261/40 hodin; doklad května 1977 u Fernándeze Longa; návod
Multimatch I 1991. Výroční webové přehledy výrobce poslední údaj samy
nedokládají. [Evidence a omezení](results/squares133/source-status.json).
Šest vrstev errat bylo prohledáno včetně historických posunů stran.

Žádný úspěšný výčet se neopakoval. V akceptačním skriptu bylo opraveno
použití zkráceného návratu kontrolní funkce místo úplného metadata.
První očekávání, že cenzus134 musí souhlasit s knihou, neprošlo;
následné nezávislé postupy potvrdily, že rozdíl je ve zdrojovém tvrzení.
