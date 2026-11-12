# §1.3.2-19: Farey, Haros a Cauchy — rozsah pramenů

Kontrola 1. listopadu 2026. Matematické důkazy a strojová reprodukce jsou
v `mixal-farey.md`. Následující záznam rozlišuje přečtený historický text
od neověřených bibliografických detailů. Nejde o úplný audit citovaných knih.

## Haros a Farey v přetisku

Scott B. Guthery, *A Motif of Mathematics* (Docent Press, 2010), obsahuje
francouzský přetisk Harosova článku a Fareyův dopis v původní angličtině.
[PDF](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/farey.pdf) je uloženo
jako `sources/guthery2010-farey.pdf`; rok a název potvrzuje též
[stránka vydavatele](https://www.docentpress.com/books/a-motif-of-mathematics/).
Přečten text s.44–49,98–105 a příslušné bibliografické položky na s.230–231;
zobrazeny dvoustrany souboru34,59,61,62.

Harosův francouzský článek na s.45–49 skutečně popisuje konstrukci
zlomků se jmenovateli nejvýše99 vkládáním mediant. Medianta dvojice
zlomků je součet jejich čitatelů dělený součtem jmenovatelů. Jeho
výchozí seznam má sousední determinant1; vkládání tento invariant
zachovává. Odvození rovnic pro vložený zlomek je správné. Tvrzení,
že jde vždy o nejjednodušší další zlomek a že nic nezbývá, když součet
jmenovatelů přesahuje99, potřebuje ještě obecný argument o minimálním
jmenovateli. Ten výslovně dodává naše lemma o mezeře. Knuthovo hodnocení
nedostatečného důkazu má tedy konkrétní oporu; algoritmus je správný.

Fareyův celý dopis na s.98–99 uvádí mediantovou vlastnost, příklad
řádu5 a příklad z tabulek se jmenovateli do99. Autor výslovně neví,
zda byla vlastnost již známa, a žádá obecný důkaz. To dokládá obsah
konjektury i jeho vlastní prohlášení o neznalosti předchozího výsledku.
Samo o sobě to není nezávislý důkaz všech okolností objevu.

Gutheryho úvod na s.45 uvádí svazekIV, sešit11, Messidor rokuX
(1802), což souhlasí s Knuthem. Jeho vlastní bibliografie ale uvádí
svazek6. Tento rozpor není důvodem opravit Knutha: původní časopisecký
obal a stránkování364–368 jsme zatím nezobrazili. Nalezen veřejný
[svazek Gallica](https://gallica.bnf.fr/ark:/12148/bpt6k4336689), přístup
k obrazům zde vrátil403. `sources/haros1802.metadata.json` eviduje
neúspěšný pokus, nikoli přečtený dokument.

## Francouzský Cauchyho důkaz

Celý třístránkový důkaz je přečten v *Oeuvres complètes*, sérieII,
tomeVI (1887), s.146–148, přetisku *Exercices de mathématiques*1826.
[Veřejný sken](https://archive.org/details/oeuvresdaugusti206caucrich)
byl získán přímo z Internet Archive. Uložen čtyřstránkový výřez s
úplným titulem1887 a článkem; obrazy všech tří stran skutečně zobrazeny.
Čísla stran souboru156–158 odpovídají tištěným146–148. Počáteční
pomocné mapování z metadat archivu bylo posunuto o jednu a před
uložením konečného výřezu opraveno podle tištěných čísel.

Důkaz volí pro dané a/b největší přípustný jmenovatel b' řešení
ba'−ab'=1. Potom b+b'>n. Pro libovolný větší zlomek f/g definujme
kladné celé m=bf−ag. Jmenovatele všech takových řešení jsou
mb'+kb, kde k je celé; další hodnota mb'+b je větší než n.
Proto g<=mb' a f/g−a/b=m/(bg)>=1/(bb'). Kandidát a'/b' je tedy
skutečný bezprostřední následník. Mediantová vlastnost plyne ze dvou
sousedních determinantů1. Jde o obecný důkaz, nikoli o konečný test.

Originál výslovně připisuje pozorování vlastnosti J. Fareymu. Gutheryho
anglický překlad na s.102–105 není spolehlivý ve všech detailech:
na s.104 mění horní mez g<=mb' na rovnost a na konci porovnává
zlomek s nesprávnou veličinou. Francouzská s.148 má správnou horní
mez i rozdíl od a/b. Tyto vady překladu nejsou nálezy v TAOCP.
Původní vydání1816 jsme nečetli přímo; tento rozsah nenahrazujeme
pouhým bibliografickým odkazem.

J. W. L. Glaisher, *On a property of vulgar fractions*, Philosophical
Magazine, série5, sv.7 (1879),321–336, je uložen z
[Zenodo](https://zenodo.org/records/1725066/files/article.pdf).
Přečteny a zobrazeny s.329–330 (strany souboru10–11), nikoli celý článek.
Cituje Fareyův dopis47(1816),385–386 a první tři odstavce Cauchyho
článku; potvrzuje Bulletin1816,133–135 a přetisk1826,114–116.
Cauchyho výslovný odkaz na Fareyho souhlasí s naším francouzským skenem.

## Hardy a Wright

Přečten titul, tiráž a relevantní části čtvrtého vydání (1960,
dotisk1975), zejména §3.1–3.4 na s.23–26 a historické poznámky na
s.36–37. Uložen jen osmistránkový výřez `hardy-wright-farey.pdf`;
metadata uvádějí zdrojový plný PDF a mapu stran. Zobrazeny tiráž,
s.23,25,26. [Zdrojová kopie na CNRS](https://gaetan.chenevier.perso.math.cnrs.fr/GT/hardy-wright-theory_of_numbers.pdf).
Oficiální [obsah OUP](https://academic.oup.com/book/54489) potvrzuje
stejné téma kapitolyIII i v šestém vydání; to jsme celé nestahovali.

Věty28–30 jsou přesně determinant, medianta a součet jmenovatelů
větší než řád. Důkaz §3.4 používá maximální přípustné řešení
kx−hy=1 a porovnání rozdílů obdobné Knuthovu. Odkaz na kapitolu3
je tedy věcně správný. Nejde o ověření všech vět této kapitoly ani
historických soudů Hardyho a Wrighta o Fareyově ostatní práci.

## Errata a zbývající meze

Prohledány všechny čtyři vrstvy `all1-prepre`, `all1-pre`, `all1`,
`err1`, podle stran i jmen/tématu. Oprava25.listopadu1997 doplňuje
akcent v Société; oprava29.března2023 mění Philomathique na
philomatique. Nová chyba matematického důkazu či programu nalezena nebyla.

Úloha18 je uzavřená. Matematika úlohy19 je rovněž uzavřená;
celkový stav19 zůstává `partial` pro původní Harosovo časopisecké
číslování a přesný rozsah tvrzení, že Cauchy zavedl jméno pro celou
posloupnost. Přečtený článek dokládá připsání pozorování Fareymu,
ne samostatně dějiny rozšíření názvu. Tyto meze nejsou nové kandidáty
na chybu a nemění platnost rekurence.
