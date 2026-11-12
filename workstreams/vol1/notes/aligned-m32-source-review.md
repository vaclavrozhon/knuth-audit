# Pramenná kontrola nálezu C0091 dne2.11.2026

Předmětem je první odstavec odpovědi §2.5–40 na616 ve třetím
vydání, prvním dotisku svazku1. Přímo čtený sken má SHA-256
e2c5ee120bad91e33f617614b846849c4801115b2e7aa820f56fc5ffb9bbebb9.
Původní obrazy456 a616 jsou v `parallel/dynamic-storage/images/`.
Na456 byly znovu ověřeny definice živého rozpočtu, nemožnost přesunů
a navazující limitní otázky. Na616 je skutečně dolní mocnina pro
zarovnání a jen požadovaná délka bloku pro test volnosti.

Robsonův algoritmus a celý navazující důkaz horní meze byly znovu
čteny na původních418–419 v autorizovaném reprintu článku1971
uvnitř disertace1981. Obrazy jsou
`parallel/dynamic-storage-followup/images/robson1981-011.png`
a `robson1981-012.png`; totožnost a získání celého PDF dokládá
tamní `SOURCES-robson-reprints.md`. Netvrdí se přečtení celé disertace.
Původní číslování buněk začíná1; po přechodu na0 vyžaduje algoritmus
celý volný slot zaokrouhlený nahoru na mocninu dvou a zarovnání
na stejnou mocninu. Rezervuje pouze skutečnou délku žádosti.

Čerstvá kontrola oficiální stránky
https://www-cs-faculty.stanford.edu/~knuth/taocp.html
potvrdila odkazy na errata. Všechny čtyři původní soubory byly
staženy běžnými veřejnými odkazy z téhož adresáře přibližně14:43:41UTC:

| soubor | bajtů | Last-Modified | porovnání s archivem |
|---|---:|---|---|
| all1-prepre.ps.gz | 261910 | 16.8.2022 | shodný |
| all1-pre.ps.gz | 143181 | 16.8.2022 | shodný |
| all1.ps.gz | 112798 | 31.5.2026 | shodný |
| err1.ps.gz | 109261 | 31.5.2026 | shodný |

Všechny odpovědi byly HTTP200. Přesné URL, časy, hlavičky a SHA-256
jsou v `sources/aligned-m32-source-review-20261102/retrievals.json`;
nové komprimované soubory jsou vedle něj. Výsledek neodvozuji jen
z data Last-Modified: porovnány byly celé přijaté bajty.

Navigace plnými texty všech vrstev hledala456,616, Robsona, Krogdahla,
alokaci, first-fit, odpověď40 a1.1825. Rozdělení na položky bylo podle
`(?=Page\s+\d+)`, bez předřazené hranice slova, aby nezmizely položky
nalepené na předchozí OCR. Širší výskyt answer40 na474 patří jiné
kapitole a není opravou zdejší odpovědi.

Výsledek odpovídá přímo zkontrolovaným původním obrazům:
all1-prepre opravuje na456 proměnné v úlohách39 a40 (10.10.1997,
6.11.1997); all1-pre nemá opravu616. all1 a err1 mají na616
pouze opravu Krogdahlova rozsahu96–97 na96–99 z7.7.2023.
Poslední dvě položky jsem znovu četl na obrazech
`errata-all1-16.png` a `errata-err1-14.png`. Předchozí vrstvy
samostatně znovu obrazově prošel autor matematického paketu;
příslušné obrazy a hashe jsou v jeho SOURCES.md a manifestu.

Nebyla nalezena oprava dolní mocniny, délky testovaného volného
intervalu ani tvrzení, že vytištěná strategie zajišťuje faktor r+1.
Toto je omezený závěr o čtyřech oficiálních vrstvách k uvedenému dni,
nikoli tvrzení historického prvenství. Fyzický výtisk ani pozdější
dotisk nebyl při této revizi ověřen. Robsonovu optimální horní mez
nález nevyvrací a bibliografická oprava Krogdahla je samostatná.
