# Úloha 225 a číselné příklady předzpracování

3. listopadu 2026. Celé zadání 225 na straně 152 a odpověď 475,
autorův draft 88/179, i související hlavní text 109–111 byly přímo
přečteny z obrazů. Obrazy již zobrazené v bloku 218–224 se znovu
nevyráběly. Nově zobrazena úplná errata Fascicle 5, PDF strana 8.

Nová [F146](F146_Y_FORCING_CELL.md) má obecný geometrický důkaz.
E101 je známá oprava z 8. prosince 2021: v zadání 225 má být u 6×15
uvedeno „one-sided“. Kniha ji již obsahuje, draft 2019 ještě ne.

Původní autorův `dlx-pre.w` byl sestaven izolovaně. Každý vstup měl
limit 30 sekund a nice 15; nejdelší předzpracování trvalo 2,26 s.
Neběželo hledání úplných řešení. Zdroj, hlavička, vygenerované C,
binárka, příkazy a hashe jsou v `results/preprocess225/build.json`.

| Vstup | Možnosti před → po | Primární položky před → po | Kola | Čisté mems předzpracování |
|---|---:|---:|---:|---:|
| 6×10 pentomina | 2032 → 1797 | 72 → 72 | 3 | 191892997 |
| 6×15 jednostranná pentomina | 3308 → 3157 | 108 → 108 | 2 | 259170792 |
| 3×20 pentomina | 1236 → 1086 | 72 → 72 | 3 | 62453178 |
| MacMahon 126 | 1537 → 961 | 49 → 49 | 2 | 19773399 |
| Symetrické sudoku 114 | 5410 → 2426 | 585 → 506 | 3 | 404190607 |
| Y pentomina 15×15 | 1344 → 992 | 225 → 205 | 5 | 21063594 |

MacMahon zachovává všech 42 sekundárních položek, sudoku všech 90.
Inicializační náklady jsou ve výstupech oddělené. Knižní hodnoty
20M, 0,19G a 260M odpovídají zaokrouhlení uvedených měření.

[Nezávislý checker](check_preprocess225.py) přehrál všechna blokování
a vynucování pomocí bitových množin a barevných masek. Ověřil jmenované
blokované primární položky, průniky pro vynucování, přesné původní
identity i obsahy přeživších řádků a aktivní hlavičky. Celý průchod
trval 4,334 s s nice 15. U tří čistých pentominových vstupů navíc
nezávislý současný pevný bod odstraní v jednotlivých kolech
[195,40,0], [151,0] a [142,8,0] řádků a dá přesně stejné množiny
jako postupné nativní předzpracování. Žádné vynucování u nich nenastalo.

Zadání 225 a odpověď souhlasí:

- Vstup 6×10 má ze všech 2056 umístění ponechaných 8 z 32 poloh X,
  tedy 2032 možností. X má střed v řádcích 1,2 a sloupcích 1–4.
  U jednostranného 6×15 je 18 dílků a ze 3346 možností zůstává 14
  z 52 poloh X, celkem 3308; středy X mají sloupce 1–7.
- `P 02 12 13 22 23` blokuje X v prvním kole 6×10.
  `O 22 23 24 25 26` jej blokuje v druhém. Jedinou původní podporou
  druhé možnosti je `X 01 10 11 12 21`; ta v prvním kole odpadne,
  protože izoluje roh 00. V 6×15 žádná mazaná možnost neblokuje X.
- Na každé desce přesně osm O možností blokuje některý roh.
  Počty možností vytvářejících komponentu menší než pět jsou
  P8,Q8,R24,S16,T8,U24,V4,W8,X1,Y16,Z8 pro 6×10. U 6×15 se po
  součtu chirálních partnerů liší pouze U: 34. To přesně dokládá
  vysvětlení rozdílu počtů v odpovědi.
- Nemožné V z (38), `V 09 0a 0b 19 29`, přežije pevný bod 3×20.
  Jeho zbylé komponenty mají 27 a 28 políček, přesto lokální test P
  tuto nemožnost neodhalí. Úplné hledání není potřeba.
- MacMahonovo jediné kořenové rozhodnutí `*` smaže přesně stejných
  576 řádků jako preprocessing. Následující strom Algorithm C je
  proto stejný; starý výčet 11 milionů řešení se neopakuje.
- Sudoku ztrácí 2984 možností a 79 položek. Správný počet řešení
  30258432 je již přijat v X114; staré dva výčty se neopakují.
- Y odstraní 352 možností a 20 položek. První a čtvrtý jmenovaný
  krok knihy sedí; druhý má F146. Jediný doplňkový běh s pořadím
  orientací S0–S7 dal totéž a byl rovněž nezávisle přehrán.

Výslovně vynechané náročné reprodukce podle pokynu uživatele:

- Úplný počet 2339 pokrytí 6×10 zde nebyl nezávisle přepočítán.
  Dokázaná ekvivalence redukce zachovává počet, ale neurčuje jeho hodnotu.
- Historické úplné hledání 6×10: 4,11G → 3,52G; součet s 0,19G
  předzpracování je 3,71G, zlepšení asi 10 %. Aritmetika souhlasí,
  samotné dva velké náklady nejsou znovu změřené.
- Historické 6×15: 15,5T → 13,1T; sudoku: 2162G → 287G.
  U sudoku poměr přibližně 7,5 sedí aritmeticky, ne jako nové měření.
- Kvalitativní tvrzení o malém vlivu Y předzpracování na celkový
  čas nebylo měřeno. Celé hledání by bylo drahé a nepomohlo F146.

Tyto přesné výjimky mají `verified:false` v `full-review.json`.
Úloha 225 je zrevidovaná; hlavní strana 110 je dokončená s těmito
výjimkami. Strana 109 zůstává částečná kvůli příkladu Soma před (46),
který patří k dosud neuzavřenému hlavnímu textu 82–86. Strana 111
zůstává částečná pro následující část o minimální ceně, úlohy 226–229.
Jiné staré mezery se tím neuzavírají.

[Výsledky](results/preprocess225/verified.json),
[zdrojová pozorování](sources/preprocess225/source-observations.json),
[šest vrstev errat](results/preprocess225/errata-check.json).
