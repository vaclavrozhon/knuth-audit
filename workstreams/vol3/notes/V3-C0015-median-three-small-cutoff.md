# V3-C0015 — záporný počet výměn při povoleném M=2

Confirmed, low. Odpověď §5.2.2-56, s. 639 / file 650, dává pro
první fázi průměr (N−4)/5 výměn B a celkově B_N=(C_N−3A_N)/5.
Při povoleném prahu M=2 a N=3 dostaneme B_3=−1/5, což je nemožné.

Kontext: úloha 56 používá program úlohy 55. Erratum s. 138 z 5. 8. 1999
výslovně požaduje M>1, takže M=2 je platné. Při N=3 nejprve mediánová
úprava z odpovědi 55 uspořádá všechny tři klíče: minimum, medián, maximum.
Vlastní partition pak nemá co vyměnit v Q6. Proběhne jedna fáze a dvě
porovnání, tedy A_3=1, C_3=2, B_3=0 pro každý vstup s různými klíči.
Obě výsledné části mají délku 1≤M a další fáze není.

Stejný závěr plyne přímo z vytištěného b_stN na s. 639: při N=3 je
s=2 a t=0 s pravděpodobností 1. Průměr t je 0, nikoli −1/5.
Toll (N−4)/5 potřebuje výjimku N=3; pak je nutné upravit i řešení
rekurence pro M=2. Pro M≥3 se takto krátká část již nepartitionuje.
Tato lokální hranice nevyvrací uváděné doporučení M=9 ani jeho asymptotiku.

Sazba files 149, 649, 650 prohlédnuta. Pět vrstev errat v
sources/exchanging-errata-review.json. Historické opravy odpovědi 56
(err3-1e s. 614, 30. 10. 1997) mění znaménko/koeficienty obecných
řešení; hranici M=2 ani řádek B_N neopravují. Pozdější příslušná
oprava nenalezena. Prvenství/fyzický výtisk neověřeny.
