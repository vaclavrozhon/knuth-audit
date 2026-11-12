# DLX157–158: dokončení obrázků a malých případů

Kontrola 3. listopadu 2026. Zadání str. 144, odpovědi str. 461;
v autorském draftu str. 80 a 165. Osm obrázků v každé verzi má
dohromady 128 číselných popisků. Přímo dekódovány vektorové hrany,
rozměry a každý popisek; ověřeno nepřekrývání, násobnosti a mezery.
PDF a draft mají totožné sestavy. Vykreslené stránky byly přečteny.

## 157: obě maxima jsou správná

Vytištěné desky 21×21 a 28×28 mají právě po osmi prázdných buňkách.
Obsahují jeden jednotkový čtverec, žádný 2×2 a k čtverců k×k pro
k=3,…,n. Pokrytá plocha je tedy 433 a 776.

Starší důkaz horní meze zůstává přijatý a jeho výčet se neopakoval.
Kdyby některá sestava měla méně než osm prázdných buněk, nemohl
by v ní chybět žádný čtverec velikosti alespoň 3 ani oba čtverce 2×2.
Pokud má oba 2×2, jeden nahradíme čtyřmi jednotkami; pokud jen jeden,
doplníme mezery jednotkami. Případně chybějící skutečnou jednotku
také doplníme. Dostaneme přesné pokrytí inventářem (5,1,3,4,…,n).
Oba tyto inventáře již byly úplně vyvráceny, což dokazuje optimum.
Nově ověřené vytištěné obrázky toto optimum dosahují.

Tvrzení o praktické rychlosti Algorithm M oproti specializovanému
backtrackingu znovu neměřím. Nemá zde konkrétní číselný benchmark;
vynechání výkonnostní reprodukce je výslovně evidováno. Nejde o
vynechání matematické horní meze, která doložená je.

## 158: malé případy a F068

| n | Rozměry vytištěného obdélníku | Plocha | Prázdné buňky | Skutečné minimum |
|---:|---:|---:|---:|---:|
| 2 | 5×2 | 10 | 1 | 10 |
| 3 | 13×3 | 39 | 3 | 39 |
| 4 | 27×4 | 108 | 8 | 108 |
| 5 | 26×9 | 234 | 9 | 234 |
| 6 | 30×15 | 450 | 9 | **448** |
| 7 | 44×18 | 792 | 8 | 792 |

Pro n=2,3,4 dosud chyběla kontrola všech menších obdélníků ze zadání.
Nově provedeno 12 malých negativních případů dvěma různými metodami:
původním DLX3 a naším dříve validovaným geometrickým backtrackingem.
Obě metody všech 12 dokončily bez řešení. Nejdelší z 24 běhů trval
0,0371 s; všechny měly nice 15 a limit 10 s. Nic nebylo prodlužováno.

Pro n=4 jsou mezi nimi i všechny čtyři rozměry uvedené v zadání:
6×17, 8×13, 5×21 a 7×15. Zahrnuty jsou i zbylé malé možnosti,
takže minimum 108 neplyne jen z neúplného seznamu případů.

Pro n=5,6,7 se žádný výčet neopakoval. Již přijaté terminální výsledky
vylučují všech 10, 7 a 7 rozměrů pod plochami 234, 448 a 792.
Nově byla jen zkontrolována úplnost seznamu rozměrů a připojeny
vytištěné obrázky. Staré pole `claimed_optimum:450` v souboru pro n=6
je původní vstupní cíl, nikoli dnešní závěr; zůstává beze změny.

Enumerace rozměrů je úplná pro osově rovnoběžné skládání v kontextu
MCC (61): rozměr musí být alespoň n a plocha alespoň součet ploch.
Stačí celočíselné souřadnice. V libovolné případné reálné sestavě
vybereme pro každou dvojici dílků jednu vodorovnou nebo svislou
oddělující nerovnost. V každé souřadnici jsou to acyklická omezení
s celočíselnými délkami. Nejdelší cesty od okraje dávají celočíselné
umístění v nejvýše stejně velkém obdélníku a zachovají oddělení všech
dvojic. Sestava v neceločíselně velkém obdélníku tedy neobejde meze.

**F068 zůstává potvrzený, nejde o nový nález.** Uložený svědek
28×16 obsahuje všech 21 požadovaných čtverců, pokrývá 441 buněk
a nechává sedm volných. Samotná nerovnost 448<450 vyvrací optimálnost
prostředního obrázku, bez použití kteréhokoli negativního hledání.

Pro vlastní rychlou kontrolu je nově samostatný příkaz:

```bash
cd audit-2026-10-31
python3 verify_f068.py
```

Používá jen standardní Python, ověří hranice, počty dílků a průniky
všech buněk. Žádný solver ani hledání nespouští. Pokyn je i na
[anglické kartě F068](http://localhost:4318/#F068); osobní anotace zůstaly.

## Errata a uzavření rozsahu

Šest relevantních vrstev errat bylo prohledáno podle původních
i posunutých stran a čísel úloh. Oprava k 157 či 158, včetně F068,
nenalezena. To nedokládá prvenství. Fyzický výtisk stále neověřen.

Celé úlohy **157 i 158 jsou reviewed**, druhá se známým naším nálezem
F068. Reviewed zde neznamená bezchybnou knihu. Starší důkazy,
programy, výsledky a historický emailový návrh zůstaly zachované;
žádný nový návrh ani zpráva nevznikly. Další úloha: 159.

## Evidence

- [Přímé dekódování všech obrázků](results/partridge157_158/figures-checked.json)
- [Dvě metody pro 12 malých obdélníků](results/partridge157_158/small/accepted.json)
- [Úplnost starých seznamů rozměrů](results/partridge157_158/prior-range-check.json)
- [Krátký validátor F068](verify_f068.py)
- [Výsledek přímé kontroly F068](results/partridge157_158/f068-direct-checked.json)
- [Starší úplné důkazy](PARTRIDGE_NOTES.md)
- [Kontrola errat](results/partridge157_158/errata-check.json)
