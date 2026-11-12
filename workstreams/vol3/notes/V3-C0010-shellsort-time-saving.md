# V3-C0010 — číselná úspora pro Table4

Potvrzená drobná číselná chyba v odpovědi §5.2.1-10, s.620 / file631.
Tisk uvádí přibližné úspory87 a88 jednotek pro Tables3 a4. Správně jsou
87 a75; první údaj i obecný vzorec3(C−T) jsou v pořádku.

C počítá vložení, při nichž už na začátku Kj≥Kj−h a není nutný posun.
Pro Table4 na85, inkrementy7,5,3,1, je počtů vložení9,11,13,15.
Nenulový posun nastane na původních indexech j jednotlivých průchodů:
- h=7: 8,10,12,14; tedy C7=5.
- h=5: 6,11; tedy C5=9.
- h=3: 4,6,8,10,11,13,15; tedy C3=6.
- h=1: 4,8,10,11,13,16; tedy C1=9.
Celkem C=29, T=4, úspora3(29−4)=75u. Malý cílený průchod oběma
vytištěnými16prvkovými vstupy je uložen v results/insertion-targeted-checks.json,
včetně mezistavů. Nejde o hledání/enumeraci. Ruční kontrola úspory:
v každém z C případů odpadá ENT2 za1u a STA za2u; každému z T průchodů
přibudou INC1 za1u a ST1 za2u. Ostatní počty instrukcí se nezmění.

Původní sazba631 a Table4/file96 prohlédnuta, číslo88 též ve zvětšeném
výřezu631-saving-detail. Pět vrstev errat prošlo kontrolou. Opravy620
z8.3.2001 mění lokální značky programu, oprava29.4.2013 upravuje slovní
spojení „time savings“ a pozdější poznámku; žádná nemění88. Historická
err3-1e nepřináší odpovídající opravu. Prvenství/fyzický výtisk neověřeny.
