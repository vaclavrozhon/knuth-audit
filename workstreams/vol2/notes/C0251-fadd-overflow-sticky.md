# C0251 — Program A ztratí nenulový ocas při přetečení zlomku

7. listopadu 2026. **Confirmed, medium.** §4.2.1, tištěná219,
file231, N4: původní řádky46–48, po opravě2002 řádky49–51.
Oba normalizované vstupy jsou přípustné, nenastane výjimka exponentu,
ale FADD vrátí vzdálenější ze dvou sousedních reprezentovatelných čísel.
Nejde o známou opravu větve opačných znamének z10. listopadu2002.

## Přesný vstup a správný výsledek

Použijme dovolené `b=100, p=4, q=50` a slova

```
u = +50 |99 99 99 50
v = +48 |50 00 00 01
```

Jejich zlomky jsou `99999950/100^4` a `50000001/100^4`.
Oba leží v `[1/100,1)` a oba exponenty v `[0,99]`.
Hodnota druhého operandu má navíc faktor `100^(48−50)`.
Proto přesný součet je

```
x = 99999950/100^4 + 50000001/100^6
  = 1000049500001/10^12
  = 1.000049500001.
```

Po posunu zlomku doprava je jeho base100 zápis
`e=51, f=.01 00 00 49 50 00 01`. Dva sousedé jsou

```
L = +51 |01 00 00 49 = 1.000049
U = +51 |01 00 00 50 = 1.000050.
```

Mají stejný exponent a po sobě jdoucí celočíselné zlomky1000049
a1000050. V tomto normálním pásmu jsou tedy sousední; žádný
vzdálenější reprezentovatelný výsledek nemůže být bližší než oba.
Přesná vzdálenost od L je `500001/10^12`, od U `499999/10^12`.
Součet je o `1/10^12` nad jejich polovinou. Správně zaokrouhlený
výsledek je jednoznačně U, nezávisle na pravidle pro přesnou půlku.

## Ruční průchod instrukcemi

Čísla A/X níže jsou nezáporné velikosti pětibajtových registrů;
znaménka jsou v celém tomto průchodu kladná. `W=100^5=10^10`.
Čísla řádků jsou po opravě2002.

| Stav / instrukce | A | X | I2 | Odůvodnění |
|---|---:|---:|---:|---|
| Před A22 `SRAX 0,1` | 5000000100 | 0 | 50 | FU=9999995000; rozdíl exponentů2. |
| Po `SRAX 2` | 500000 | 100000000 | 50 | Desetibajtový zlomek se posune přesně o dva bajty; ocas je `01 00 00 00 00`. |
| Po A23 `ADD FU` | 495000 | 100000000 | 50 | Součet horních částí10000495000 překročí W, v A zůstane zbytek495000 a nastaví se overflow. |
| Po A24 `JOV N4` | 495000 | 100000000 | 50 | Skok do N4; overflow se zruší. |
| Po A49 `ENTX 1` | 495000 | 1 | 50 | Celý starý X se přepíše; informace o nenulovém ocasu zmizí. |
| Po A50 `SRC 1` | 100004950 | 0 | 50 | Poslední1 z X přejde před A; poslední bajt A byl00 a nový X je nulový. |
| Po A51 `INC2 1` | 100004950 | 0 | 51 | Exponent se správně zvýší. |
| A52–A55, N5 | 100004950 | 0 | 51 | Poslední bajt A je50=b/2, X je0: program rozpozná domnělou přesnou půlku. |
| A56–A58 | 100004950 | 49 | 51 | Poslední ukládaná cifra49 je lichá, JXO přejde do N6 bez zaokrouhlení nahoru. |
| A62–A67 | 5101000049 | 5000000000 | −49 | Exponent51 se zabalí do slova a program normálně vrátí L. |

Tento průchod neprochází chybnou původní větví26–28 ani její
náhradou2002. Proto se stejná chyba vyskytuje v původním i opraveném
programu. Nejde o náhodu interpreta: výsledek plyne přímo z významu
ENTX a SRC ve svazku1,133/file148 a135/file150. ENTX nahrazuje celý
registr; SRC cyklicky posouvá všech deset bajtů a nemění znaménka.
Původní oba obrazy jsou uložené jako `fadd-vol1-p133.png` a135.

## Obecná příčina a místní oprava

Před N4 po sčítacím přenosu nechť A obsahuje zbytek H a X ocas L.
Přenos je1, protože oba normalizované zlomky mají velikost menší1.
Po posunu doprava musí A začínat1 a pokračovat prvními čtyřmi
bajty H. Nový guard je čtvrtý bajt H; za ním zůstávají poslední
bajt H a všech pět původních bajtů X. Pro správný test půlky tedy
musí nový X být nenulový právě tehdy, když

```
(H mod b != 0) or (L != 0).
```

Tištěné `ENTX 1; SRC 1` zajistí pouze první podmínku. Pokud je nový
guard `b/2`, poslední bajt H je0, L je nenulové a poslední ponechaná
cifra je lichá, program chybně použije pravidlo přesné půlky a
nezaokrouhlí nahoru. Zvolený vstup splňuje všechny čtyři podmínky.

Místně stačí před SRC nastavit `X = 1 + b*[starý X != 0]` místo
bezpodmínečného1. Pak má A po SRC zcela stejné bajty jako předtím,
ale velikost nového X je `(H mod b)*b^4 + [L != 0]`. To zachová
přesně potřebnou nenulovost, a tedy všechna rozhodnutí N5. Velikost
ocasu již není přesná, což nevadí: po přenosu je nový zlomek
normalizovaný a následuje zaokrouhlení, nikoli další posun vlevo.

Je-li N4 vyvolán až zaokrouhlovacím přenosem, zbytek H po přičtení
b má velikost menší b. Nový A je proto `1 0 0 0 0`, guard0 a další
zaokrouhlení již nemění výsledek. Případné zachování nenulového
starého X v této větvi nemá vliv. Toto je důkaz místní opravy N4,
nikoli tvrzení, že už byl znovu uzavřen celý zbývající Program A.
Změna vyžaduje další instrukce; časový vzorec a maximum84u pro
tištěný program se nesmějí bez nové analýzy přenést na opravený kód.
Původní přepis jsme neměnili.

## Originál, errata, archiv a omezení

Inventář: třetí vydání, první tisk, září1997; offset+12.
Zobrazen originál219/file231, zejména N4 a následující N5.
Přečtena i původní grafická oprava `all2-prepre`, file14;
mění opačná znaménka, posun SRC5 a návrat do N2, nikoli N4.
Příslušná časová oprava odpovědi19 je na file37.

Vyhledány stránky219/220 i `N4`, `ENTX`, `FADD`, přenos zlomku
a zaokrouhlovací cifry ve všech relevantních vrstvách:

| Místní soubor | Výsledek pro tento problém |
|---|---|
| `errata/text/all2-prepre.txt` | Známá oprava10.11.2002 a její časový důsledek; N4 nezměněno. |
| `errata/text/all2-pre.txt` | Žádná oprava N4 ani ztráty ocasu. |
| `errata/text/all2.txt` | Žádná oprava N4 ani ztráty ocasu. |
| `errata/text/err2.txt` | Žádná oprava N4 ani ztráty ocasu. |
| `errata/originals/err2.textxt` | Žádná taková oprava; výskyt219 v položce rejstříku JXO není oprava programu. |

Vrstvy pocházejí z oficiálního webu podle `errata/manifest.json`,
stažení31.10.2026. Historické dlouhé vrstvy mají Last-Modified
16.8.2022; aktuální all2/err2/TeX10.6.2026. Pozdější fyzický
dotisk a prvenství nebyly ověřeny. Původní sken a všechny dostupné
vrstvy však doložený rozpor ponechávají.

Jediný nový cílený běh `nice -n 15 python3
workstreams/vol2/repro_C0251_sticky_overflow.py` dne7.11.2026
00:09:14UTC skončil0. Výsledek `results/C0251-sticky-overflow.json`
obsahuje jednu instrukční exekuci, snímky registrů, přesné racionální
vzdálenosti a SHA256 přepisu/interpreta. Nezávislá správná odpověď
vzniká porovnáním racionálních vzdáleností sousedů, nikoli stejným
zaokrouhlovacím algoritmem. Skript odmítá opakování uloženého běhu.
Staré censy ani jejich výsledky nebyly opakovány nebo přepisovány.

Staré X0035 je znovu `partial`; tvrzení o obecném správném N4
v `mix-float.md` je tímto výslovně opraveno. Úspěšná konečná sada
`results/mix-float.json` je zachována pouze jako konečná sada kontrol,
ne jako důkaz všech vstupů. X0134 zůstává již dříve otevřenépartial.
Samostatné matematické algoritmy A a N na216–217 tuto vadu nemají.

Při následné kontrole nákladů X0196 byla cena tohoto průchodu ručně
sečtena jako32+10+8=50u. Ve vzorci známého errata19 je nutné T
vykládat jako **strojově pozorovaný** ocas: zde T=1, protože po N4
vidí N5 přesnou půlku. Přesný matematický ocas má T=0; jeho dosazení
by dalo44u. Jde o další důsledek téže ztráty, nikoli nový nález.
Viz [instrukční důkaz a náklady](recovery-floating-mix-add-2026-11-06.md).
