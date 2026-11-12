# Souvislá revize §3.4.1 G a logistické úlohy 24

6. listopadu 2026, X0123. Původní 138 a 140 znovu přečteny v obrazu;
odpověď 24 na 588 není, jde o výzkumné zadání. Nový nález nepřibyl.
C0053 má nadále stav confirmed; závažnost je nyní **medium**, protože
chybná konstanta porušuje normalizaci hustoty, ale nemění samotnou
rekurenci ani zamýšlený arcsinový zákon. Matematika a výpočetní modely
jsou níže výslovně odděleny od přijatých starších výsledků.

## Další čtení na 138

Znovu přečten celý dvoustránkový von Neumannův dopis ve facsimile
na původní 135 Eckhardtova článku a navazující výklad na 136.
Datum 21. května 1947, adresát Stan Ulam i popis inverzní a odmítací
metody souhlasí. Citace 135–136 je správným odkazem, přestože název
souboru LANL naznačuje delší článek. Existence dopisu nedokazuje
neexistenci dřívějšího objevu; absolutní historická priorita je
výslovnou bibliografickou výjimkou.

Přečten celý pětistránkový preprint Hörmanna–Derflingera, jeho strana 2
také v obrazu. Potvrzuje, že odmítání může zhoršit výstup kongruenčního
generátoru s násobitelem blízkým odmocnině modulu. Netvrdí selhání
každého malého násobitele pro každou transformaci. Pro beta(2,3) je
hustota 12u(1−u)², obálka 16/9 a odmítací test pro dvojici (x,y)
na mřížce m přesně

```
4 y m² < 27 x (m−x)².
```

Přečten celý `verify_distribution_context.py`, protokol a JSON.
Archivovaný příklad m=1024, a=33, c=1 obsahuje všech 1024 sousedních
dvojic a 579 přijetí. Cílová CDF je 6u²−8u³+3u⁴. Největší prázdná
mezera (75/1024,94/1024) má cílovou hmotnost
16993023901/1099511627776; intervalová odchylka je přesně
144653575173/6631429505024. Jednostranné odchylky se sčítají, protože
intervalovou chybu vyjadřuje rozdíl dvou hodnot rozdílu CDF.
To je kontrola všech sousedních dvojic, nikoli tvrzení o jednom
proudu, který spotřebovává nepřekrývající se dvojice. Velká tabulka
modulu 2³¹−1 a milionové statistické vzorky článku se neopakovaly.

U Devroyeovy knihy znovu přečten model na původních 1–3 a bitová
Bernoulliho konstrukce na 769. Reálná aritmetika, ideální nezávislé
uniformní vstupy a jednotkové ceny operací jsou předpoklady analýzy,
nikoli naměřená rychlost na dnešním stroji. Odkaz na knihu je obsahově
přiměřený. Knuthův–Yaův článek 1976 má starší ověření bibliografických
metadat 357–428; plný text nebyl přečten a jeho obecná teorie se tímto
blokem neprohlašuje za auditovanou. Leva je uzavřen v předchozím bloku.

## Přesná logistická dynamika a C0053

Pro f(x)=4x(1−x) a x=sin² θ platí f(x)=sin²(2θ). Posun binárních
cifer u při θ=πu dává pro téměř každý počátek správné dlouhodobé
četnosti. Nulová výjimečná množina u má nulový obraz x, protože
sin²(πu) je Lipschitzovské zobrazení. Jde o četnosti jedné trajektorie,
nikoli o tvrzení, že každé V_n má při uniformním V_0 již stacionární
hustotu. Zdvojení úhlu je dvoulistá semikonjugace; monotónní souřadnice
F(x) převádí f na stanové zobrazení.

Transformace uniformního u má CDF a hustotu

```
F(x) = (2/π) arcsin √x,
h(x) = 1 / (π √(x(1−x))).
```

Tištěný jmenovatel √(2πx(1−x)) dává integrál přes [0,1] rovný
√(π/2), tedy větší než jedna. Substituce x=sin² θ ověřuje obě
normalizace přesně. Přímo znovu porovnána sazba na 140. Všechny čtyři
vrstvy errat a aktuální TeX byly prohledány podle 140/588, logistické
mapy, Ulama a von Neumanna; žádná odpovídající oprava nebyla nalezena.
Změny úlohy 25 z let 2005/2024 jsou odlišné. Nejnovější fyzický dotisk
ani prvenství nálezu ověřeny nejsou.

Přečteny důkazy ve `logistic-finite.md`, včetně odlišení nulové
kovariance od nezávislosti a globální meze zaokrouhlovací chyby
δ(4ⁿ−1)/3. Tato mez není tvrzením skutečného tempa růstu chyby.
Tvrzení o typickém infinitesimálním exponentu log 2 lze doplnit
bez simulace: pro x=sin² θ dává řetězové pravidlo

```
(fⁿ)'(x) = 2ⁿ sin(2ⁿ⁺¹ θ) / sin(2θ).
```

Pro každé ε>0 má množina θ s |sin(2ⁿ⁺¹ θ)|<exp(−εn) míru
nejvýše C exp(−εn). Součet těchto měr je konečný, takže podle první
Borelovy–Cantelliho věty nastává nerovnost téměř jistě jen konečněkrát.
Současně |sin|≤1. Pro spočetnou posloupnost ε→0 tedy
log|(fⁿ)'(x)|/n→log 2 skoro všude. To je důkaz typického lokálního
exponentu, ne model statistické nezávislosti zaokrouhlovacích chyb.

## Přijaté výpočty a jejich přesný rozsah

Přečten celý `verify_logistic.py`, všech 38 záznamů PASS a struktura
uložených výsledků. Dvě pravidla na mřížce k/2ᵇ pro b=2,…,20 dávají
38 úplných funkčních grafů a 4 194 334 stavů/hran. Zaokrouhlení je
jediné po přesném vyhodnocení, buď dolů, nebo k nejbližšímu sudému;
nejde o model plovoucích mezivýsledků. Druhý vzorec
N−(2k−N)²/N kontroluje každou hranu, invarianty vzdálenosti a povodí
kontrolují rozklad všech stavů. Rozsahy použitých celočíselných typů
pro b≤20 postačují. Pole označení všech stavů nejsou samostatně
uloženým certifikátem; přijímáme jejich archivovanou validaci uvnitř
programu, ne nově přehrané certifikáty. Všech osm řádků tabulky
největších povodí bylo porovnáno s JSON. Největší povodí nemusí mít
nejdelší cyklus. Desetinné odchylky CDF jsou popisná numerika.

Přečten celý `experiment_logistic.cpp` a `validate_logistic_float.py`,
všech 40 řádků PASS a všech 40 validačních záznamů. Model A postupně
počítá round(round(4x)·round(1−x)); model B počítá
round(4·round(x−round(x²))). Zakázané přeuspořádání a FMA, explicitní
mezivýsledky, režim zaokrouhlení i skutečné vstupní bity jsou doloženy.
Deset počátků, dva výrazy a dva formáty dávají 40 případů. Archiv
obsahuje 9185 přesných racionálních kontrol hran, všech 20 úplných
binary32 trajektorií s 27 491 stavy a opakování nalezených binary64
cyklů v Pythonu přes 30 086 200 kroků. Dlouhé binary64 opakování
nepočítá každý krok racionálně; přesný racionální model mají sondy.
Uzavření, minimálnost periody a začátku a kontrolní součty souhlasily.

Osm binary64 případů vyčerpalo limit detektoru. Z toho neplyne perioda
ani její dolní mez 50 milionů. U binary64/A s počátkem zapsaným
0.3141592653589793 je odchylka prvních 65 536 hodnot asi 0.00295,
ale po 5 509 878 krocích trajektorie vstoupí do nuly. Krátký histogram
tedy sám nedokazuje dlouhodobou kvalitu. Obecná konečnost stavového
prostoru dokazuje pozdější periodicitu bez ohledu na tyto pokusy.
Žádný výpočet se v tomto bloku nespouštěl znovu.

## Primární doklady a zbývající práce

Všechny tři strany 768–770 von Neumannova textu znovu vizuálně přečteny.
Ulamova atribuce, úhlový vztah, upozornění na zaokrouhlování i omezení
nezávislosti jsou doloženy. Historický zdroj má jinou chybnou konstantu
1/(2π); nejde o nový nález v TAOCP. Strana 770 podporuje také původ
konstrukce v úloze 23.

Přečten celý Galiasův článek 2021 a znovu vizuálně jeho tabulky II/III.
Pro přesný výraz A autor uvádí 10 binary32 a 20 binary64 cyklů při
parametru 4. Naše pozorované periody 4344 a 836 s tabulkou souhlasí.
Jeho úplný rozsáhlý soupis samostatně nepotvrzujeme; uvádí přibližně
500 dní výpočtu jednoho jádra a podle výpočetního omezení
uživatele se neopakuje. U binary64 je většina podílů povodí
statistické odhady ze 100 000 počátků, nikoli přesné počty. Rovnoměrné
reprezentovatelné plovoucí stavy také nejsou rovnoměrná reálná mřížka.

Úloha 24 je uzavřena jako výzkum uvedených modelů, ne jako klasifikace
všech aritmetik. Strana 138 je nyní celá prošlá s uvedenými
bibliografickými výjimkami. Strany 140/588 zůstávají částečné kvůli
globálnímu maximu E v úloze 21. Dále následuje Wallaceova úloha 31
a návrat k faktickým tvrzením na 119 a 132. Žádná korespondence nevznikla.
