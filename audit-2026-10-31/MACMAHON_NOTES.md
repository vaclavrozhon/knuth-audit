# MacMahonovy trojúhelníky — 7.2.2.1, 125 a 129

## F063: souřadnice při zvětšení

Na p.447 má být druhá souřadnice ky+q, resp. ky+q′, místo kx+q, resp. kx+q′.
Už k=1,(x,y)=(0,1) vyvrací tisk. Nezávislý geometrický test všech vrcholů
podtrojúhelníků potvrzuje opravu pro 400 případů. Vizuálně PDF i fasc5c p.151.
Podrobnosti v `knuth-report-f063-draft.txt` a `results/macmahon/scaling.json`.

## F065: počet slabých levopravých symetrií

Na p.449 je uvedeno 281 618 slabě, ale ne silně symetrických vzorů. Úplný
přepočet dává **294 457**. Větev se dvěma pevnými jednobarevnými trojúhelníky
souhlasí: 107 611. Větev bez pevných jednobarevných trojúhelníků má **186 846**
namísto součtu vytištěných šesti čísel 174 007. Rozdíl je **12 839**.

Každý model byl generován nezávislým souřadnicovým popisem trojúhelníkové mřížky.
Všech 24 různých dílků se musí použít jednou, barvy na sdílených hranách se
musí shodovat. Slabá symetrie je přesně shoda trojice booleovských testů
nerovnosti barev uvnitř zrcadlených trojúhelníků, s přehozením šikmých hran.
Na ose se navíc vyžaduje invariantnost tohoto vzoru. Toto vystihuje hranice
barevných ploch, nikoli konkrétní pojmenování barev.

### Úplnost a nezávislé kontroly

Čtyři jednobarevné dílky musejí tvořit množinu invariantní vůči zrcadlení.
Mohou být nula nebo dva pevné; čtyři pevné by obsahovaly sousední různé barvy.
Všech 67 invariantních nesousedících čtveřic bylo vyčísleno: 35 bez pevného
bodu a 32 se dvěma. U každé byly barvy normalizovány podle lexikografického
pořadí čtyř pozic. Tím se přesně odstraní 24 globálních přejmenování barev.

Větev bez pevných bodů má 747 906 normalizovaných barevných rozmístění.
Každý z 35 případů spočítal vlastní bitsetový algoritmus i původní, nezměněný
Knuthův DLX2, se shodnými výsledky. Vlastní počítadlo bylo navíc ověřeno na
1000 náhodných malých XCC proti úplnému výčtu všech podmnožin řádků.

Všech 747 906 rozmístění je uloženo v komprimovaných souborech. Samostatný
validátor znovu zkontroloval přesně 24 různých dílků, shodu všech hran,
požadovanou slabou symetrii a polohy jednobarevných dílků. Poté přímo
kanonizoval všechna rozmístění čtyřmi prostorovými transformacemi zachovávajícími
levopravou osu a následným přejmenováním barev. Výsledek: 186 846 orbit velikosti
4 a 261 orbit velikosti 2. Menší orbity mají navíc silnou půlobratovou symetrii.

To je úplné ztotožnění i vzhledem ke všem dvanácti symetriím hexagonu: jiná
osa stejného typu by spolu s první dávala slabou rotaci o 120 stupňů, která
nemůže permutovat čtyři jednobarevné trojúhelníky bez pevných bodů. Osa tohoto
typu je proto jedinečná a při porovnání dvou již normalizovaných vzorů ji musí
prostorová transformace zachovat. Silné zrcadlení je nemožné podle argumentu
knihy (rovněž zkontrolovaného).

Větev se dvěma pevnými jednobarevnými dílky má 430 444 rozmístění, tedy
430444/4 = 107611 orbit. Celkem 107611+186846 = **294457** slabých nesilných.

### Rodina odpovídající rozdílu

Umístěme aaa,bbb,ccc,ddd postupně do **02′,11′,21′,22′**. Existuje 25 678
rozmístění. Zrcadlení spolu s a↔d,b↔c je páruje, bez pevných bodů. Podmínka
barvy vodorovné hrany −13 v {a,c} vybírá jednoho z každé dvojice a oba
počítací programy dávají **12 839**. Tato hodnota přesně odpovídá rozdílu.
Je pravděpodobné, že právě tato geometrie v původním rozdělení chyběla;
protože šest typů pro tuto větev není v knize explicitně popsáno, původ chyby
neprohlašujeme za prokázaný. Celkový opravený počet však plyne z úplného výčtu.

Svědek: `results/macmahon/lr-missing-witness.json`, `.svg`, `.png`.
Vektor barev všech 42 hran dovoluje příklad zcela nezávisle rekonstruovat.
Znění p.449 a autorova fasc5c p.153 bylo vizuálně ověřeno. Historická stránka
v publikovaném Fascicle 5 je 257. Odpovídající oprava v all4b/all4f5 nenalezena.
Fyzický výtisk nebyl kontrolován.

## Ověřené správné počty

- Silné rotace před redukcí: 68 024 064. Všech šest kanonických počtů
  80768,164964,77660,819832,88772,185172 souhlasí; součet 1 417 168.
- Z nich rovinu bez rotace dláždí 40 208. Neredukovaný počet 1 929 984
  souhlasí i s autorovým původním generátorem MACMAHON-TRIANGLES-SYM-TILE.
- Slabé nesilné rotace: všech šest čísel 24516,45818,22202,341301,44690,130676
  i součet 609 203 souhlasí, ve dvou nezávislých solverech.
- Slabá hornodolní symetrie: všech šest surových počtů i zvláštních silných
  počtů 88,0,0,98,0,75 souhlasí. Silných je 261, ostatních 41 608.
- Obě osové slabé symetrie: 1298 rozmístění po normalizaci barev, tedy
  (1298−2×261)/4 = **194** nesilných orbit, jak uvádí kniha.

V tomto původním bloku neopakujeme historické memové benchmarky. Úlohy 126–128 a 130 nejsou tímto
blokem pokryty, kromě potřebných souřadnic a generátorů.

Doplnění 2. listopadu 2026: [nový průchod celé 129](SYMMETRIES129_NOTES.md)
ověřil všech pět původních obrázků, obecné důkazy symetrií a úplnost
kanonických typů. Doslovné kódování nově reprodukuje 68 024 064 i 0,5 Tμ.
Všech 32 případů s pevnými jednobarevnými dílky má nyní také nezávislé
nativní počty, součet 430 444 a tři knižní dílčí počty souhlasí.
Nová evidence výslovně rozlišuje skutečně dvojí výčet od starších
tabulek doložených jen bitsetovým programem. Historická příručka 1991
zatím chybí, takže staré `checked` o počtech neuzavírá celou úlohu.

## Soubory a reprodukce

- `check_macmahon.py`: souřadnice, geometrický test 125, generátory XCC.
- `xcc_bitset.cpp`: vlastní nezávislý počítač, konfliktní bitové množiny.
- `check_macmahon_models.py`: kontrola každého modelu a explicitní kanonizace.
- `results/macmahon/`: všechny vstupy, protokoly obou solverů, modely a výsledky.
- `sources/knuth-programs/`: archiv původních zdrojů s URL, datem a SHA256.
  Zdroj DLX2 je https://www-cs-faculty.stanford.edu/~knuth/programs/dlx2.w;
  původní generátor periodických sestav je na stejné cestě pod názvem
  macmahon-triangles-sym-tile.w. Jejich zdroje nebyly upravovány.
