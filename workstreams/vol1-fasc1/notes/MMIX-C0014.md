# MMIX-C0014 — PUT rL ztrácí horní bity před porovnáním

**Confirmed, medium;** §1.4.3′, odpověď 9, tištěná p. 118 / file 126,
blok `PutL`. Digitální vydání 3 (květen 2023), fyzický výtisk neověřen.

Platný stav: rL=1, rG=32, $255=2^61. Instrukce `PUT rL,$255`
se pokouší rL zvýšit a musí je ponechat rovno 1. Pravidlo je výslovně
uvedeno na p. 19. Stejně rozhoduje autorův MMIXware 1.0:
`mmix-sim-20131017.w`, řádky 2213–2217, nejprve testují celý octabyte
(`if (z.l>L || z.h)`), teprve potom nastavují minimum.

V knižním interpretu je ll=8*rL=8 a z=2^61. `SLU z,z,3`
spočte (8*2^61) mod 2^64=0. `CMPU t,z,ll` proto vrátí −1 a
`CSN ll,t,z` nastaví ll=0, tedy simulované rL=0. Další
`GET $254,rL` vrátí 0 namísto 1; $254 i $255 jsou globální,
takže protipříklad nemá vedlejší růst lokálních registrů.

Vstup lze připravit pomocí `SETL $0,1; SETH $255,#2000`
při rG=32. Není potřeba spouštět simulátor: čtyři vypsané instrukce
PutL dávají přesný úplný protipříklad.

Oprava může nejprve porovnat nescalované z s ll/8 a ignorovat každé
z≥ll/8; teprve menší hodnotu násobit osmi. Alternativně před posunem
odmítnout jakoukoli hodnotu s nenulovými horními třemi bity.

Původní sazba file126 zobrazena, instrukce souhlasí s textovou vrstvou.
Relevantní historická a aktuální errata neobsahují tuto opravu;
opravují pouze odstranění STOU cc v odpovědi 8 (2011) a opačný
komentář nerovnosti v PutG na p. 119 (2024). Viz results/errata-C0014.json.

Primární zdroj sémantiky: [autorův MMIXware](https://www-cs-faculty.stanford.edu/~knuth/mmixware.html),
archiv 17. října 2013; lokální metadata sources/mmix-20131017-metadata.json.
Nejde o kontrolu celého MMIXware, jen uvedeného pravidla PUT rL.
