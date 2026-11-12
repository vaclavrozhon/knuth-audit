# §1.3.2: rozsah a inventář

> Oprava auditu 5. listopadu 2026: C0022 je zamítnuto. Originál na s.512
> správně obsahuje ≥64; starší čtení níže přehlédlo spodní čárku.
> Platný závěr a obrazový detail jsou v [souvislé recenzi](sequential-mixal-basics-2026-11-05.md).

Zobrazeny hlavní stránky144–163 a potvrzeno23 původních úloh.
Hodnocení z originálu:

```
1:00 2:10 3:23 4:25 5:11 6:HM20 7:10 8:24 9:25
10:31 11:M29 12:M47 13:28 14:31 15:M30 16:31 17:HM30
18:25 19:M30 20:33 21:28 22:31 23:37
```

Oprava24.4.1997 mění12 naHM42 a doplňuje publikovanou analýzu.
Nejde o novou úlohu. OCR měnilo16 naSI a19 naM50; originál ukazuje31,M30.

## Uzavřený první blok

- Syntaxe a význam uvedených příkladů, Programy M/P a úlohy1–9:
  [důkazy a přesný rozsah](mixal-basics.md).
- Odpovědi511–512 zobrazeny. Checker52324 kontrol prošel jednou;
  nejsou tím prověřeny odpovědi10–23 na dalších stránkách.
- [C0021](../reports/V1-C0021.txt): nepromítnuté důsledky změny
  PRIME=−1 na99 do obrázku15, slovního popisu a odpovědi4.
- [C0022](../reports/V1-C0022.txt): pouze chybná ostrá nerovnost
  v komentáři testu C>=64; kód rozhoduje správně.
- Úlohy10–23 zůstávají todo; originály jejich odpovědí513–522 jsou
  připraveny, ale v tomto checkpointu ještě nebyly zobrazeny/ověřeny.

## Errata

Všechny čtyři řady a současný TeX byly prohledány podle stran i pojmů.
Výpis je v `sources/mixal-errata-extract.json`; obsahuje též okrajové
záznamy sousedních sekcí a duplicity. OCR slučuje nadpis opravy157
s předchozím záznamem156; obsah byl ověřen ze skutečné stránky14.

Pro uzavřený rozsah byly zkontrolovány známé změny:145 formulace
registrů a odkaz96;147 program/algorithm;149 odkaz naIOC řádek09;
150 libovolné pořadí literálů;151 ALF, kladná nula a ORIG řádek50;
154–156 typografie, zrušený příslibPL/MIX a zadání1;157 d>1;
512 paměťový test plovoucích instrukcí a zkrácení porovnání.
Změny PRIME2022 a návazná hodnota599 z2026 jsou hlavní částí C0021.
Zobrazeny errata `all1-prepre`13,14,37, `all1-pre`11 a `all1`7
(včetně zobrazení v předchozím bloku, které se zbytečně neopakovalo).
Zbývající opravy10–23 z výpisu budou uplatněny při jejich kontrole.

## Prameny a historický rozsah

[Knuthův manuál CASE SOAP III](https://archive.computerhistory.org/resources/access/text/2018/07/102784981-05-01-acc.pdf)
obsahuje datované poděkování Conwayeovi31.1.1958 za program points;
současně zmiňuje kompatibilitu s připravovaným UNISAP pro Univac.
Přečteny a zobrazeny s.1,5,9 (PDF3,7,11): lokální dopředné/zpětné
symboly mají právě vysvětlený význam a nereferují na vlastní řádek.
Je to soudobý doklad autorství a použití, nikoli průzkum všech možných
předchůdců. Samotný manuál UNISAP nebyl získán. Autorova vzpomínka
na jugoslávský prací prostředek1971 nemá v tomto bloku nezávislý doklad;
není zaměněna s matematickým tvrzením. Hlavní text má proto výslovně
vymezený historický zbytek.

Křížový odkaz odpovědi3 byl ověřen přímo: svazek3, druhé vydání/první
dotisk1998, s.139 (soubor150), Algorithm5.2.3S. Vybere nejpravější maximum
prefixu a vymění s jeho koncem; odpovídá přesně této úloze, jen vynechá
poslední triviální průchod délky1. Doklad je ve vlastní složce images;
svazek3 ani jeho pracovní evidence nebyly měněny.

Pro následující úlohu12 se hledá Hofri–Jacquet. CiteSeer vrátil403
přes prohlížeč a429 při přímém stažení; není to přečtený článek.
Plný14stránkový preprint následně získán přes veřejné API archivu Rice;
uložen jako `hofri-jacquet-saddle-rice.pdf`, zatím nepřečten. Přesný
URL a hash jsou v metadatech s příponou `-rice-api`.

## Pomocný Markdown

`md/vol1/19-1.3.2-mix-assembly-language.md` je pouze navigace.
Originál v P7 i P11 obsahuje <=, částečná pole mají neostré meze;
OCR tyto rovnosti ztrácí. Graficky vysázená slova a dvojice sloupců
instrukcí vyžadují skutečný sken. Ratingy16,19 opraveny v našem inventáři.
Sdílený Markdown nebyl měněn.
