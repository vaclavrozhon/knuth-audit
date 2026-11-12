# Kandidát: rozpor čísla dotisku v úvodech errat

Stav `candidate`, místní označení `printing-introduction-mismatch`.
Nejde o matematickou chybu knihy ani o kontrolu fyzického výtisku.

Přímo zobrazeny první strany všech čtyř archivovaných PDF:
`all1-prepre`, `all1-pre`, `all1`, `err1`. Samostatné obrazy
`images/*-01.png` zachovávají celý první odstavec i titul dokumentu.
Konkrétní PDF a jejich SHA-256 uvádí `results/evidence-snapshot.json`.
Zdroje byly kořenově obnoveny1.11.2026; tento podklad je z2.11.2026.

`all1-pre` je označeno **ERRATA TO VOLUME1 (after2010)**. První odstavec
identifikuje třetí vydání,27.dotisk, poprvé vytištěný2011, a uzavírá
interval49.dotiskem z2022. To souhlasí s `all1-prepre`, PDF47:
dodatekC vznikl od27.dotisku, záznam je datován6.1.2011.

`all1` i `err1` nesou titul **ERRATA TO VOLUME1 (after2021)**, ale první
odstavec opět uvádí27.dotisk a připojuje datum prvního tisku2022.
Doslovné relevantní fragmenty jsou:

```text
all1-pre: (third edition, 27th printing) ... first printed in 2011
          until the 49th printing came out in 2022
all1/err1: (third edition, 27th printing), since it was first printed in 2022
```

Obě časová určení téhož dotisku si odporují. Nejpravděpodobnější
redakční oprava současného úvodu je27th→49th, ale bez prohlédnutí
tiráží příslušných dotisků neměníme tuto pravděpodobnou rekonstrukci
na nezávisle ověřený bibliografický fakt. Otevřeno zůstává, zda opravit
samotnou číslovku, nebo větu jako celek. Návrh hlášení tento rozdíl
zachovává.

Úplná četba všech101 stran a hledání27th/49th/2011/2022 ve všech
čtyřech textových vrstvách další vysvětlení tohoto rozporu nenalezly.
Fiktivní příklady Page666 v úvodech nejsou skutečná knižní errata.
Vlastní auditovaný exemplář je třetí vydání,první dotisk1997; jeho
tiráž tento spor o27./49.dotisk sama nerozhoduje.

Nic nebylo odesláno; globální ID přiděluje kořenová revize.
