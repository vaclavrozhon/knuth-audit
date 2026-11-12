# §1.2.11 a §1.2.11.1: rozsah, pramen a známé opravy

Audit 1. listopadu 2026. Krátký úvod §1.2.11 je na s.107
a nemá vlastní cvičení. §1.2.11.1 má hlavní text na s.107–110,
všech 13 úloh na s.111 a odpovědi na s.502–503. Všechny tyto
strany byly skutečně zobrazeny; jejich čísla v DjVu jsou o 15 vyšší.
Za úlohou 13 na s.111 už začíná §1.2.11.2, který tento blok
neoznačuje za hotový.

## Dokončená matematika

- [asymptotic-notation.md](asymptotic-notation.md): definice,
  množinová interpretace, jednostranné rovnosti, lokální komplexní
  odhady, O/Omega/Theta a úlohy 1–11,13.
- [asymptotic-factorial-powers.md](asymptotic-factorial-powers.md):
  konečné rozvoje rostoucích a padajících mocnin pro všechna reálná r;
  konvergence v celočíselných případech; obecný důkaz zadané identity
  a divergence v úloze 12. Padající rozvoj navazuje na již uložený
  důkaz §1.2.6; staré kontroly se neopakovaly.

Zvlášť rozlišujeme nezávislé O-symboly, jednotnost konstant v součtu
s rostoucím počtem členů, nenulovost v rovnici (10), volbu větve
logaritmu a m=0 v úloze 9. Stručný důkaz odpovědi 9 byl doplněn
odhadem |exp(w)−1|; nejsou tím prohlášeny její opravené nerovnosti
za nepravdivé. Nový nález nevznikl.

Hodnocení podle skenu v pořadí 1–13:
`HM01,M10,M15,M15,M20,M20,HM15,HM20,HM20,HM22,M11,HM25,M10`.
V prověřených erratech nebyla nalezena přidaná úloha tohoto oddílu.
Vnitřní odkazy na generující funkce, Stirlingovu dualitu a předchozí
rozvoje jsou obsahově správné. Úvod §1.2.11 odkazuje na Stirlingovo
přiblížení a H_n; samostatný odvozený důkaz Stirlingova vzorce
následuje v §1.2.11.2.

## Bachmann 1894: skutečně přečtený originál

Získán celý veřejný sken *Die analytische Zahlentheorie*, Paul
Bachmann, Leipzig: B. G. Teubner, 1894, přes
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Die_analytische_Zahlentheorie._Dargestellt_von_Paul_Bachmann_(IA_dieanalytischeza00bachuoft).pdf).
PDF, extrahovaný text a metadata jsou v `sources/bachmann1894-*`.
Skutečně zobrazeny a přečteny titulní strana (soubor 7) a tištěné
s.401–402 (soubor 423–424), nikoli celá kniha.

Na s.401 Bachmann zavádí O(n) u součtu počtů dělitelů a výslovně
vysvětluje, že řád nepřekračuje řád n, ale nemusí být přesně n.
Na s.402 používá O(n log n) u součtu součtů dělitelů. To přímo
dokládá obsah a rok knižního odkazu. Netvrdíme vyčerpávající hledání
všech starších použití tohoto písmene v dějinách matematiky.

## Errata všech časových vrstev

Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1` a zdrojový
`err1.textxt`, podle stran i výrazů a čísel úloh. Shoda aktuálních
souborů s uloženými zdroji je doložena v
`sources/errata-refresh-2026-11-01.json`; poslední datum řady je
31. května 2026. Výřezy textu v `asymptotic-notation-errata-extract.json`
obsahují také sousední oddíly; následující tabulka je přesně třídí.

| Místo | Datum | Ověřený obsah opravy |
|---|---|---|
| s.107 za (1) | 2001-09-07 | Euler's constant, s výslovností Oiler |
| s.108 polynom | 1997-07-31 | a1 musí být a1 n |
| s.108 (10) | 2022-01-20 | f(n) nesmí být nikde nulové |
| s.109 ř.7 | 1998-05-22 | all values |
| s.110 konec | 2005-11-08 | Big Theta |
| s.110 (18) a vysvětlení | 2014-07-01 | obecný základ log v O a vysvětlení |
| s.110 za (18) | 2024-05-06 | potlačují se konstantní faktory |
| odpověď 8, s.503 | 1998-05-26 | metoda předchozí úlohy |
| odpověď 9, s.503 | 2003-05-05 | f(z), nikoli f(x) |
| odpověď 9, s.503 | 2008-02-26 | absolutní hodnota exp(f(z)) |
| odpověď 12, s.503 | 1999-07-30 | (k−1)!, nikoli (n−1)! |

Změny s.107 úloh 22–23 a s.502 odpovědí 21–23 patří §1.2.10.
Změna obrázku 12 na s.111, úloh 1–4 na s.503 a dalších Bernoulliho
konvencí patří §1.2.11.2 a bude řešena tam. Obsah errata (10)
byl znovu přímo ověřen v obrazu `errata-all1-pre-file008.png`.

## Pomocný Markdown vyžaduje opravu koordinátorem

Soubor `md/vol1/14-1.2.11.1-o-notation.md` není věrným přepisem:

- Jeho (7), `O(f)+O(g)=O(max(f,g))`, není původní rovnice (7)
  a bez absolutních hodnot je obecně nepravdivá: f=−n²,g=−n
  dává vpravo O(n), zatímco vlevo může být n². Správný obecný
  odhad používá max(|f|,|g|); originál zde má O(f)+O(f)=O(f).
- Chybí původní (8), O(O(f))=O(f), a podmínka nenulovosti
  původní (10) z errata 2022. Následující rovnice jsou přečíslované.
- Chybí harmonický příklad (15) a oba faktoriálové rozvoje (16)–(17).
- V úloze 3 je gamma zaměněna za číslici 7.
- V úloze 9 je m>0 místo původního m>=0.
- Úloha 12 je nahrazena obecným popisem; chybí konkrétní Stirlingův
  koeficient, jeho faktoriálová identita i požadované nejití členů k nule.

Sdílený Markdown nebyl měněn. Tyto chyby navigačního přepisu se
nepočítají mezi chyby Knuthovy knihy.
