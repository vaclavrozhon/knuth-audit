# §1.3.2-21: připsání konstrukce a odkaz na Ballovu knihu

Kontrola 1. listopadu 2026; původní s.162 byla zobrazena. Všechny
čtyři vrstvy errat byly prohledány podle stránky i jmen. `all1-prepre`
obsahuje opravu překlepu jumt→just z12.7.1997 a náhradu připsání
Moschopoulovi připsáním Ibn al-Haythamovi z28.3.2000. Nejde o nový nález.

## Dva historické postupy

[Tanneryho francouzský překlad Moschopoulova textu z1886](https://remacle.org/bloodwolf/erudits/moschopoulos/carremagique.htm)
byl přečten v rozsahu úvodu a celé liché konstrukce „po dvou a po třech“.
Začíná pod středem, postupuje dolů a doprava, přechází přes okraje a po
n číslech klesá o dva řádky. To odpovídá algoritmu úlohy. Původní
řecký rukopis ani všechny ostatní metody jsme neprověřovali. Webový
obrázek7×7 má v řádku3,sloupci6 hodnotu38 místo36; TAOCP má správně36.
Přímé stažení stránky vrátilo403, obsah zpřístupnil webový nástroj.

V Berggrenově kapitole v Katzově *The Mathematics of Egypt, Mesopotamia,
China, India, and Islam: A Sourcebook* (2007), s.658–659, jsme přečetli
 a zobrazili celý přeložený Ibn al-Haythamův postup pro lichý čtverec.
Zdrojová položka37 na s.674 odkazuje na Sesianovo vydání z1980.
Postup začne řádkově uspořádaným čtvercem, vymezí otočený vnitřní
čtverec a přesune vyčnívající čísla do protilehlých děr. Zobrazený
příklad řádu5 je redakční rekonstrukce; původní obrázek chyběl.
[PDF zdroje](https://edukacja.3bird.pl/download/filozofia/historia_filozofii/filozofia-the-mathematics-of-egypt-mesopotamia-china-india-and-islam.pdf).

Následující výpočet dokazuje, že jde až na otočení o stejnou konstrukci
pro každý lichý řád, nikoli pouze o podobnost jednoho obrázku. Použijme
n=2h+1 a rozklad čísla k=nq+s+1 z matematické poznámky, 0<=q,s<n.
Souřadnice čísla v otočené vnitřní síti před přesuny jsou

```
u=q−s+h,     v=q+s−h.
```

Leží mezi −h a3h. Mimo interval0..2h může být nejvýše jedna
souřadnice: například u<0 a v<0 by dávalo s>q+h a s<h−q, což
není možné; ostatní tři kombinace se vyloučí obdobně pomocí mezí
q,s. Přesun do protilehlé díry tedy právě přičte nebo odečte n
od jedné souřadnice. Konečné souřadnice jsou u,v modulo n.
Pro souřadnice r,c z `mixal-magic-square.md` platí

```
u = n−1−c (mod n),     v = r (mod n).
```

To je otočení čtverce o90 stupňů. Bijektivita již dokázaná v matematické
poznámce také zaručuje, že jde skutečně o dosud prázdné díry a že jsou
všechny zaplněny. Připsání staršímu Ibn al-Haythamovu postupu je tedy
věcně podpořeno. Netvrdíme zde nezávislé ověření rukopisu ani prvenství.

Životopisný úvod na s.587 téhož zdroje uvádí Basru a roky965–1040.
Úvod odborného hesla A.I.Sabry v *Dictionary of Scientific Biography*,
dostupný jako [přetisk PDF](https://mathshistory.st-andrews.ac.uk/DSB/Al-Haytham.pdf),
potvrzuje Káhiru a přibližné datum úmrtí. Přečten byl životopisný
úvod, nikoli celý dlouhý článek. Dvě nedostupné cesty k Langermannovu
heslu nepovažujeme za přečtený další zdroj.

## Ball a Coxeter

Bibliografii vydání Macmillan1939 potvrzuje [knihovní záznam](https://library.marshallfoundation.org/portal/Default/en-US/RecordView/Index/35251).
Přímo dobové recenze Harolda Thayera Davise (1940,357–358) a W.D.R.
(1940,46), [přetištěné v oddílu8 této sbírky](https://mathshistory.st-andrews.ac.uk/Extras/Ball_books/),
shodně identifikují kapitolu7 jako magické čtverce a popisují její
rozšíření. Odkaz v TAOCP proto míří na správnou kapitolu správného
vydání. Pozdější vydavatelský obsah1974 to rovněž potvrzuje, ale
nenahrazuje důkaz o vydání1939. Celá kapitola1939 nám zpřístupněna
nebyla a její jednotlivé konstrukce nejsou tímto záznamem auditovány.

Rozsah úlohy21 je uzavřen: obecná konstrukce, požadovaný program,
obrázek a konkrétní historické a bibliografické výroky. Neznamená to
 audit celých citovaných knih. Metadata rozlišují stažené a přečtené části.
