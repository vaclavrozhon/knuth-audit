# Tag hlavy po přidání smyčky v odpovědi 25

Pracovní označení: `header-loop-tag`. Stav: kandidát k nezávislé revizi.
Jde o přesnost doplňkové poznámky na s. 585, nikoli o pravidla obecné
reprezentace na s. 584 ani o splnění požadavků úlohy bez přidané smyčky.

## Doslovná pravidla a minimální příklad

Uvažujme původní orientovaný strom tvořený jediným kořenem R. Přidáme
oblouk r:R->H a poté smyčku h:H->H. Zde I_H={h} je množina výstupů z H
a F_H={r,h} množina vstupů do H. Zvolme přesně druhý případ poznámky 585:
nová smyčka h je v pořadí F_H poslední, tedy F_H=(r,h).

Pravidlo na 584 říká: ALINK vede na další výstup z téhož vrcholu s ATAG=0;
poslední výstup vede na první vstup s ATAG=1. BLINK a BTAG se definují
záměnou rolí vstupů a výstupů. Proto přesně:

| Uzel | ALINK | ATAG | BLINK | BTAG |
|---|---|---:|---|---:|
| r | NULL | 1 | h | 0 |
| h | r | 1 | h | 1 |

Hlavou reprezentace je uzel h, kořenovým uzlem stromu uzel r. Úloha 25
výslovně identifikuje ALINK, BLINK, BTAG s LLINK, RLINK, RTAG; netvrdí
identifikaci ATAG s LTAG, proto ji zde nepoužívám.

Poznámka na 585 tvrdí, že v tomto druhém případě dostaneme standardní
konvence, s výjimkou RTAG=0 u uzlu kořene. Výjimka u r je skutečně v tabulce.
Navíc však platí **RTAG(h)=BTAG(h)=1**, zatímco standardní konvence
2.3.1-(8), s. 324, výslovně vyžaduje **RTAG(HEAD)=0**. Chybí tedy druhá
výjimka týkající se hlavy. Tento rozpor nepotřebuje žádnou interpretaci
levého tagu.

Stejný výpočet platí pro libovolný ne-prázdný původní orientovaný strom:
oblouky incidentní s H jsou vždy pouze r a h a výše uvedené tři hodnoty
ALINK(h), BLINK(h), BTAG(h) na zbytku stromu nezávisí. V prvním pořadí
F_H=(h,r) lze přímo spočítat h=(h,1,r,0) a r má BLINK=h, BTAG=1;
zde ale převod levého tagu není součástí zadání a hlavní kandidát na něm
nestojí.

## Dopad a návrh opravy

Jde o chybné tvrzení o přesné shodě tagů. Pro druhé pořadí stačí doplnit,
že kromě RTAG kořene se liší i RTAG hlavy: je 1. Pokud by měl vzniknout
standardní sentinel, je třeba jej dodatečně nastavit na 0. Neměním vlastní
reprezentaci digrafu: v ní je BTAG(h)=1 správně podle obecných pravidel.

## Originály a errata

Přímo prohlédnuty originály:

- `images/vol1-file339-p324.png`, rovnice (8);
- `images/vol1-file395-p380.png`, úloha 25 a přesná trojice identifikovaných polí;
- `images/vol1-file599-p584.png`, úplná pravidla a obě tabulky;
- `images/vol1-file600-p585.png`, úplná doplňková poznámka.

Prohledány všechny čtyři vrstvy errat podle 324, 584, 585, list head,
ATAG, BTAG, RTAG a Lynch. Příslušné originální stránky errat již byly
prohlédnuty v tomto bloku: all1-prepre 25–26, 43–44; all1-pre 13;
all1 10; err1 8–9. Oprava obrázku vlevo na 584 z 31. 12. 1997 mění šipky,
nikoli pravidla ani tag hlavy. Na 585 jsou jen známé opravy odpovědí 27 a 28.
Na 324 se relevantní oprava nenachází.

Potvrzení zde znamená evidenci proti dostupnému skenu, nikoli fyzickou
kontrolu výtisku nebo tvrzení o prvenství nálezu.

## English ASCII draft

Page 585, note following answer 2.3.4.2-25: When the added loop h at H is
last in F_H=(r,h), the construction gives ALINK(h)=r, BLINK(h)=h, and
BTAG(h)=1. Thus the representation also differs from convention 2.3.1-(8)
at the list head: RTAG(HEAD)=1, whereas (8) requires 0. The stated exception
RTAG=0 at the root is not the only exception. Please mention the head tag
as well, or explicitly reset it to 0 when adopting the standard sentinel
conventions.
