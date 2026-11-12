# Obnova §3.5, úlohy 26–30 — V2-X0153

6. listopadu 2026. Úplně přečten `white-parity.md`, původní zadání
182/file194 a odpovědi596–597/file608–609 včetně obr. A-5. Všechny
tři obrazy znovu zobrazeny; pro identitu29 také plné rozlišení596.
Úloha28 již má přesný uzavřený důkaz v X0150; ten přebíráme ve stejném
rozsahu a nepočítáme podruhé. Čtyři nově přidaná zadání jsou26,27,29,30;
**27 zůstává partial**. Žádný archivní výpočet se neopakuje.

## 26(a,b) a celá Watermanova odpověď

Známé erratum z23.9.2024 v aktuálním TeX i textu mění dvojice
na (2n,2n+1); tím jsou definovány i V_0,V_1. Je to zapracovaná známá
oprava, nikoli náš nález ani důvod k obarvení stránky.

Původní G používá přesně `x−1/2<y≤x` nebo `x+1/2≤y`.
Starší důkaz v §1 píše otevřené varianty těchto hranic: rozdíl leží
na konečně mnoha úsečkách a má četnost nula. Mimo ně prohodí
transformace právě jednu z dvojic (x,y),(y,x) do G, takže výsledná
hustota je 2 na G. Věta C dává společné zákony libovolného pevného
počtu nepřekrývajících se vstupních párů; nemusíme předpokládat
pravděpodobnostní nezávislost konkrétní deterministické posloupnosti.

Každý svislý i vodorovný řez G má délku1/2. Obě parity výsledku proto
mají rovnoměrné marginály, tedy výsledek26(a) je ekvidistribuovaný.
Součin xy je invariantní při prohození, takže společný moment členů
uvnitř páru je1/4. Moment členů z různých párů je rovněž1/4 podle
součinového zákona odpovídajících vstupních bloků. Pro k=1 je nutné
sloučit oba typy, pro k≥2 jsou to vždy různé páry. Tím jsou ověřeny
všechny kladné posuny v tvrzení o bělosti.

Část26(b) rozlišuje sestup uvnitř páru (plocha3/8 násobená hustotou2,
tedy3/4) a přes hranici párů (1/2); obě parity začátku mají hustotu1/2.
Výsledek je přesně5/8. Diagonála a všechny okraje mají nulovou četnost.
Franklinův původní článek zůstává nedostupnou bibliografickou výjimkou;
tento přímý důkaz na jeho přečtení nezávisí.

Pro **Watermanovu alternativu** přebíráme celý §2, zejména argument,
který nevyžaduje nezávislost U a X. Jeho jednotlivé mezikroky:

1. Pro Y_n=(−1)^X_n a z_n=Y_n či Y_nY_(n+k), k>0, má klouzavý
   H-průměr limitní druhý moment1/H. Různé dvojice {h,h+k} nemohou
   při k>0 úplně splývat; v každém smíšeném součinu zbude bit v liché
   mocnině, a jeho průměr je nula i při částečném překrytí.
2. Posun o h naruší blokově konstantní váhy jen na O(h√N) indexech.
   Nahrazení z_n H-průměrem má chybu O_B(H/√N); Cauchy dá horní
   limitu B/√H. Limita N se bere první, H až potom. Platí to i pro
   váhy závislé na všech bitech X.
3. Indikátor intervalu je součtem symetrické části v U_j,1−U_j a
   váženého Y_n. Druhá část mizí. Abelova sumace převádí obvyklou
   ekvidistribuci U na váhy2j+1; poslední čtvercový blok má o(N)
   členů. Výsledná V je ekvidistribuovaná.
4. Pro každý pevný posun k výjimky přes hranice bloků tvoří O(k√N)
   pozic. Jinde je centrovaný součin `(U_j−1/2)²Y_nY_(n+k)`;
   bod2 tedy dokazuje všechny nulové korelace.
5. Na hustotě1 mimo blokové hranice se rovnost vyskytne při stejných
   bitech, pokud U_j≠1/2. Výjimečné bloky mají nulovou váženou četnost.
   Vážené čtyřpárové zákony dávají rovnosti1/2, vzestupy1/4 a sestupy1/4.
6. Při přísně klesajícím ε_n→0 se rovnosti mění na vzestupy. Nenulové
   rozdíly mimo libovolně malé okolí U_j=1/2 si od jistého místa zachovají
   znaménko; obal přes0 má nulovou horní hustotu po zmenšení okolí.
   Malá změna hodnot mimo nulovou hustotu zachová rozdělení i korelace.
   Proto W má vzestupy3/4, jak uvádí odpověď.

Zachováváme dvě přesná omezení z původní poznámky. Při U_j=0 může
tištěná V_n dosáhnout1; tento okraj má nulovou hustotu a pro doslovný
obor[0,1) se opravuje na0. Doslovný vzorec se nevydává za vždy uvnitř
[0,1). „Decreases monotonically“ se zde vykládá jako přísný pokles:
pouhé nerostoucí hodnoty konstantní na čtvercových blocích by ponechaly
rovnosti hustoty1/2. Volba ε_n=1/(n+2) splňuje požadovaný silnější
výklad. Nezavádíme z těchto již zaznamenaných okrajů další nové nálezy.

## 27: hranice skutečně dosaženého výsledku

§3 dokazuje po odrazu Watermanovy konstrukce dolní mez3/4 a jednoduchou
horní mez11/12. Pro d_n=V_n−V_(n+1) jsou první moment0 a druhý1/6;
z `d_n²≤|d_n|` a teleskopické rovnosti pro součet d_n plyne dolní
hustota vzestupů nejméně1/12, a tedy horní hustota sestupů nejvýše11/12.
Hranice, rovnosti a případ neexistující hustoty jsou pokryty liminf/limsup.

To **neřeší optimum** ani knižní hodnotu7/8. Primární Knuthovo oznámení
1973 potvrzuje pouze historické připsání Coppersmithovi; neobsahuje
konstrukci. Přesný důkaz7/8 a aktuální úplný stav výzkumu nejsou zde
doloženy. Žádné tvrzení, že problém je dosud otevřený, ani nový LP běh.

## 29: všechny členy odhadu a nová místní chyba

Převzat §4: přepočet nul na každé pozici okna má krajní chybu nejvýše2k;
součet2k takových rovností dává O(k²). Po dělení n je O(1/n) při
**pevném k**, jak je pro limitu potřeba. Následuje rozklad podle r,s,
omezení `0≤ν_x^E≤ν_x`, 2k-distribuce a přesná teleskopická identita

```
d binom(2k,k+d)
 = k[binom(2k−1,k+d−1)−binom(2k−1,k+d)].
```

Tím vyjde uvedená horní hustota i obě dodatečné identity pro max(r,s)
a min(r,s). Normalizace sudých pozic potřebuje n/2+O(1), a proto
vede faktor2 přesně na konstantu ze zadání. Nejmenší případ k=1
je zahrnut: horní mez3/4.

Starší tvrzení, že „všechna znaménka“ v odpovědi byla správná, bylo
nepodložené. V původním obrazu596 mezi dvěma členy hlavní identity
**chybí plus**. Nový **C0250** má přesný protipříklad k=1, perioda0011,
s korektní2-distribucí; levá strana je1/2 a tištěný součin je0.
Detail v `C0250-parity-missing-plus.md` obsahuje originál, všechny vrstvy
errat a obecnou opravu. Vlastní dřívější důkaz i konečná mez zůstávají
správné, ale nepřenášíme je na chybnou tištěnou identitu.

## 30: přesný graf, existence tahu, indexy a obrázek

Převzat celý §5. Pro každý z2^(2k) formálních vrcholů se vstupní a
výstupní stupeň rovnají, protože posun stejného bitu přes liché slovo
obrací znaménko alternujícího součtu. Stupně jsou v{0,1,2,3,4}.
Vyřazené izolované vrcholy jsou přesně ty ze sazby. Z neizolovaného O
vede připojení1 do E; z E lze vždy připojit01. Po k takových dvojicích
je dosažen E101…1. Konečnost a vyrovnanost stupňů vyloučí zdrojovou
komponentu s výstupní hranou, takže tato vlastnost dokazuje silnou
souvislost, včetně cest ze středu ven, jak požaduje odpověď.

Použití Eulerovy věty lze zde uzavřít bez další externí mezery: od
zvoleného vrcholu sledujeme nepoužité hrany. Při uvíznutí se díky
vyrovnanosti stupňů musíme vrátit do výchozího vrcholu. Zbývající hrany
se ve stejné komponentě připojí dalšími takovými uzavřenými tahy a
vloží do dosavadního tahu. V každém kroku ubude alespoň jedna hrana;
konečný proces pokryje všech2^(2k+1) hran. To je i deklarovaná délka
periody; menší nejkratší perioda se v textu netvrdí.

Start v E00…0 a **X_1**, nikoli X_0, je podstatný: E odpovídá lichému
začátku okna, O sudému. Každé slovo délky2k se v obou fázích vyskytne
celkem dvakrát. Pro r>s leží oba výskyty na skutečně sudém začátku,
pro r<s na lichém. Tím se dosahuje každá maximalizace v opravené29.
Volbu počátečního X_0 lze doplnit bez posunu ostatních indexů. Případ
k=1 funguje stejným důkazem a nemá izolované vrcholy.

ObrázekA-5 se skládá ze14 neizolovaných vrcholů a32 číslovaných hran.
Převzata dříve jednotlivě ověřená tabulka všech32 hran v
`results/white-parity.json`, klíč `figure_A5`; při nynějším zobrazení
597 souhlasí popisky i orientace, včetně čtyř paralelních přechodů
O010↔E101, označených12–15. Posloupnost hran1–32 se vrací do E000.
Tištěná perioda začínající X_1 je
`00001000110010101001101110111110`; přesný archivní výpočet četností
ji porovnal se všemi2k-okny a doložil11/16 nul na sudých indexech.
Tuto uzavřenou konečnou kontrolu přebíráme, nespouštíme nový výčet.

## Další rozsah

Mapa má nyní38 jednotlivých úloh, z nichž výzkumné17 a27 partial.
Je to kontrola příslušných úloh a odpovědí, nikoli celých stran182,
596 nebo597. Nový nález jenC0250; známé erratum26 zůstává v auditní
evidenci mimo nálezy. Obnova hlavního textu pokračuje **E168/file180**,
zbylé úlohy38,40–44 čekají. Dopředný **418/file430 držen**.
