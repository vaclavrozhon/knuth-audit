# §4.5.1: slash formáty, zaokrouhlení a úlohy 12–14

Audit 2. listopadu 2026. Původní strany 331–333 a 639–640 přečteny
v sazbě. Zde uvedené algoritmy jsou vlastní přesné referenční modely;
nepředstírají hardwarovou implementaci. Experimenty úloh 15/16 navazují.

## Formáty a pravidlo zaokrouhlení

Zlomek zapisujeme jako redukovanou dvojici (u,a), kde a>0. Znaménko
je v čitateli u. Nula je (0,1), nekonečna jsou (1,0) a (-1,0).
Délka kladného celého čísla v základu b je počet číslic jeho zápisu
bez úvodních nul; délku nuly definujeme jako 0. Znaménko se počítá
samostatně. Binární floating slash formát připouští součet délek
|u| a a nejvýše q. Pro fixed slash používáme přesně konvenci příkladu
na str. 332: |u|<2^(p-1), a<2^p, takže znaménko spotřebuje jeden
bit pole čitatele. Zejména při p=8 jsou meze 127 a 255.

Medián dvou zlomků u/a a v/b zde znamená zlomek (u+v)/(a+b),
anglicky *mediant*; není to aritmetický průměr jejich hodnot.
Mezi sousedními reprezentovatelnými čísly se zaokrouhluje podle
toho, na které straně tohoto mediánu vstup leží. V rovnosti se
vybere menší jmenovatel, při shodě menší čitatel. V referenčním
modelu jde doslovně o podepsaný čitatel, jak je definován v textu.
Reprezentovatelné vstupy zůstávají beze změny.

### Obecný algoritmus hledání sousedů

Pro nezáporný přesný vstup x začneme intervalem [0/1,1/0].
Jeho koncové dvojice (u,a),(v,b) splňují

```text
av - ub = 1.                                             (1)
```

Nahrazení jednoho konce mediánem zachová (1). Je-li medián menší
než x, posune se levý konec, jinak pravý. Shoda vrací x přesně.
Kladné složky přípustných dvojic tvoří množinu uzavřenou směrem
k menším složkám: zvětšení čitatele nebo jmenovatele nemůže
napravit překročenou mez fixed ani floating slash formátu.

Je-li (c,d) celočíselná dvojice uvnitř intervalu s invariantem (1),
pak ji lze jednoznačně zapsat

```text
(c,d) = s*(u,a) + t*(v,b),
s = vd-bc > 0,   t = ac-ud > 0.
```

Obě čísla jsou kladná celá, tedy s,t>=1. Každý vnitřní zlomek
má proto obě složky alespoň tak velké jako medián. Jakmile medián
není přípustný, žádný přípustný vnitřní zlomek neexistuje a konce
jsou hledaní sousedé. To je obecný důkaz úplnosti výstupu, nejen
ověření několika testovacích vstupů.

`sources/slash_arithmetic.py` spojuje stejnosměrné kroky: pro posun
levého konce o k pravých konců vypočte z přesného x=A/B mez
k<=floor((Aa-Bu)/(Bv-Ab)), obdobně na druhé straně. Binárním hledáním
omezí k také podmínkou formátu. Každý krok posune konec směrem k x;
přípustných dvojic je konečně mnoho, takže algoritmus skončí.
Pro záporné x se nejprve najdou sousedé |x|, potom se obrátí znaménka
a pořadí. Samotné tie pravidlo se následně vyhodnocuje na skutečných
podepsaných koncích. Tím se nepředpokládá lichost zaokrouhlovací funkce.

### Příklad knihy

Pro p=8 byly sousední hodnoty i zaokrouhlení ověřeny nezávislým
úplným výčtem redukovaných dvojic. Přesné rozhodovací nerovnosti jsou:

```text
77/39 < 314/159 < 79/40,     314*79 = 24806 > 156*159 = 24804;
7/6 < 1300/1113 < 125/107,  1300*113 = 146900 < 132*1113 = 146916;
113/36 < 377/120 < 22/7,    377*43 = 16211 > 135*120 = 16200.
```

Mediány jsou postupně 156/79, 132/113 a 135/43. Výsledky jsou
79/40, 7/6 a 22/7, přesně jak uvádí text. Také
314/159+1300/1113=22/7 a 79/40+7/6=377/120.
Nula má sousedy +/-1/255, mediány +/-1/256; oba mezní body
zaokrouhlí na nulu díky jejímu menšímu jmenovateli. V sazbě je
správné **<=**, přestože OCR ukazuje ostrou nerovnost.

Tvrzení o obvyklé jednoduchosti vstupů a o častém rušení chyb je
empirická motivace závislá na souboru úloh. Tento příklad nedokazuje
univerzální převahu nad zaokrouhlením na nejbližší hodnotu.

## 12: rozsah a okolí nuly

Pro celé q>=1 spotřebuje kladný jmenovatel alespoň jeden bit.
Největší konečná hodnota je proto (2^(q-1)-1)/1, včetně nulové
hodnoty při q=1. Pro q>=2 je nejmenší kladná hodnota
1/(2^(q-1)-1). Její medián s nulou je 2^(1-q).
Pro q>=3 má nenulový soused větší jmenovatel než nula, a proto

```text
round(x)=0 právě pro |x| <= 2^(1-q),   q>=3.              (2)
```

U kladného nekonečna je medián s největší konečnou hodnotou
2^(q-1). Nekonečno má menší jmenovatel 0, takže v rovnosti vítězí.
Tištěná podmínka round(x)=+inf právě pro x>=2^(q-1) je správná
pro všechna q>=1.

Pro q=1 však (2) neplatí: jediná konečná hodnota je nula a sousedé
jsou nekonečna. V bodech +/-1 vítězí nekonečna, takže nulová oblast
je otevřený interval (-1,1). Pro q=2 jsou konečné hodnoty -1,0,1.
Doslovná volba menšího podepsaného čitatele v bodě -1/2 vrátí -1,
zatímco v bodě 1/2 vrátí 0. Nulová oblast je tedy (-1/2,1/2].
**C0115** je drobná chybějící kvalifikace nejmenších formátů;
praktické formáty q=27 a q=58 zůstávají správné. Základní protipříklad
q=1,x=1 se neopírá o interpretaci znaménka v pomocném tie pravidle.

## 14: počet nesoudělných dvojic

Möbiova funkce mu(n) je 0, obsahuje-li kladné n čtverec prvočísla;
jinak je (-1)^r, kde r je počet jeho různých prvočísel. Z rozvoje
součinu (1-1)^r plyne

```text
sum_{d|g} mu(d) = 1, je-li g=1; jinak 0, pro g>0.        (3)
```

V celém intervalu (M1,M2] je floor(M2/d)-floor(M1/d) násobků d.
Pro **0<=M1<=M2 a 0<=N1<=N2** jsou obě souřadnice kladné,
takže jejich gcd je kladné a nejvýše min(M2,N2). Sečtení (3)
přes všechny dvojice dává přesně tištěný vzorec i verzi s inkluzí
a exkluzí. To také vysvětluje jeho použití k počítání kladných
čitatelů v úloze 13.

Zadání však uvádí celé dvojice bez těchto omezení. Například
M1=-1,M2=1,N1=0,N2=2 připouští právě tři nesoudělné dvojice:
(0,1),(1,1),(1,2). Tištěná suma končí na 1 a vrátí 4, protože
neodečte (0,2). To je **C0116**, chybějící obor platnosti.
Jde o problém již s kanonickou nulou a kladnými jmenovateli,
nikoli pouze o umělé záporné jmenovatele.

Jedna obecná oprava pro neprázdné celé intervaly je použít
K=max(|M1+1|,|M2|,|N1+1|,|N2|). Nechť I=1, pokud obdélník
obsahuje (0,0), jinak I=0. Správný počet je

```text
sum_{d=1}^K mu(d) *
  ((floor(M2/d)-floor(M1/d))*(floor(N2/d)-floor(N1/d)) - I). (4)
```

Odečtení I odstraňuje (0,0) z každého členu. Každá zbývající
dvojice má kladné gcd nejvýše K, a proto se použije (3).
Jestliže K=0, jde nejvýše o (0,0) a prázdná suma správně vrací 0.
Pro kladné intervaly zůstává efektivnější původní kratší suma.
Asymptotická hustota 6/pi² se posuzuje s podmínkami limitního
modelu v §4.5.2; není rovnoměrnou relativní aproximací každého
tenkého obdélníku. Například řádek se jmenovatelem 1 má hustotu 1.

## 13: přesné počty a bitové kódování

Pro základ b a celkovou mez q číslic rozdělíme kladné čitatele
podle délky a=1,...,q-1. V příslušné třídě leží čitatel v
[b^(a-1),b^a-1], jmenovatel v [1,b^(q-a)-1]. Kladné hodnoty
spočítáme vzorcem úlohy 14; záporné přidají stejný počet a nula
jednu hodnotu. Každý redukovaný zlomek se započte právě jednou.
Nejde o počet bitových kódů včetně redundantních zápisů.

Přesný výpočet dává:

| Formát | Konečné reprezentovatelné hodnoty |
|---|---:|
| Součet nejvýše 27 binárních číslic | 2140040119 |
| Součet nejvýše 7 hexadecimálních číslic | 1830986459 |

Obě hodnoty v knize jsou správné. Nejdelší potřebné Möbiovo síto
má mez 8191, respektive 4095; miliardy zlomků se nevypisují.
Menší formáty byly nezávisle spočítány přímým výčtem gcd.

Konkrétní binární kód má jeden znaménkový bit, tag určující délku
jmenovatele a q-1 datových bitů. Pro nenulový jmenovatel se jeho
úvodní bit 1 neukládá; zbylé bity se spojí s velikostí čitatele.
Tag 0 a datové pole 1 kódují nekonečno. Tag 1 s nulovým datovým
polem kóduje nulu. Nepřípustné tagy, nekrácené zlomky a záporná
nula se odmítají. Tag potřebuje 5 bitů pro q=27 a 6 pro q=58,
takže celkové délky jsou 32 a 64 bitů.

Hexadecimální kód má znaménko, 3bitový tag délky jmenovatele
a 28 datových bitů. Úvodní hexadecimální číslice se ukládá;
tag a datové pole musí souhlasit o minimální délce jmenovatele.
Také zde jsou povoleny jen kanonické dvojice. Dekódování je
inverzí uvedených bitových posunů; kontrola kanoničnosti zajišťuje
jediný kód na hodnotu. Úplný výčet malých kódových prostorů
potvrdil přesně počet konečných hodnot plus dvě nekonečna.

## Reprodukovatelnost a rozsah

`verify_rational_slash.py`, `results/rational-slash.json` a `.log`:
relace 29872, PID 1091775, exit 0. Čtyři checkpointy:

- 53985 přesných kontrol úplných mřížek: floating q=1,...,10,
  fixed p=2,...,6; zvlášť úplná mřížka p=8 pro příklad knihy.
  Dále 2000 certifikátů sousednosti pro q=27 a q=58.
- Mezní body q=1,...,58, včetně všech nejmenších výjimek.
- 2025 kladných a 3025 obecných celočíselných obdélníků,
  13 malých formátů a dva vytištěné velké počty.
- Úplné kódové prostory 9 malých binárních a 3 hexadecimálních
  formátů; 6000 velkých roundtrip kontrol a zvláštní hodnoty.

Čtyři vrstvy errat all2-prepre/all2-pre/all2/err2 prohledány podle
sekce, stran 331–333/639–640, formátů, vzorců a mezí. Opravy C0115
ani C0116 nebyly nalezeny. Doplněk chybějících dvou řádků úlohy
4.5.3-43 z 1. ledna 2020 nepozmeňuje zdejší pravidlo; algoritmus
této poznámky má vlastní důkaz. Poslední fyzický dotisk a priorita
nálezů neověřeny; návrhy hlášení neodeslány.
