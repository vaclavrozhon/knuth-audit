# V3-C0006 — zobecnění S′ potřebuje změnit i návrat ze S4

Potvrzená chyba algoritmu v úloze §5.1.4-39, s.70 / file81.
S′ je podle textu stejné jako S (s.55), kromě nových S1′ a S2′.
Zděděný S4 však vrací řízení do S3, čímž přeskočí nový test S2′.
Pro S′ musí S4 po vodorovném posunu vracet řízení do S2′.

Platný vstup je jediný řádek P=(2,1), tvar(2), n=2. Algorithm P
prochází buňky zprava doleva. Na(1,2) K=1 ihned splní S2′. Na(1,1)
K=2 nesplní S2′, protože pravý soused je1. S3 zvolí S4: P11←1,s←2.
S4 jde přímo do S3. Oba sousedé nyní mají∞, takže S5 zapíše P12←∞
a zvýší r na2. S2′ nyní zapíše K=2 do P22 a skončí. Výsledkem je
(1,∞) v původním řádku a2 mimo tvar, nikoli tabulka stejného tvaru.
Rovněž Q12=−1 překračuje zamýšlenou dolní mez0 v této koncové buňce.
Se změnou S4→S2′ se2 správně uloží do P12.

Sazba images/tableaux-file-066.png a081.png prohlédnuta. Všech pět
vrstev errat zkontrolováno: sources/tableaux-errata-review.json. Žádná
odpovídající oprava nalezena; stará první edice ještě tento nový
Algorithm P/S′ nemá. Prvenství ani fyzický výtisk neověřeny.
