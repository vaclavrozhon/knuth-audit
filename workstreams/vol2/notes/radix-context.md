# §4.4 F: historické poznámky a bibliografie, strany 326–327

Vymezený audit 2. listopadu 2026. Původní stránky 326–327 byly
přečteny v sazbě; čtyři vrstvy errat podle stran i jmen.
Nový nález není. Dokončení tohoto bloku znamená kontrolu všech
odstavců a níže uvedených dostupných dokladů; neznamená ověření
všech historických prvenství ani všech algoritmů citovaných článků.

## Starší převody

Smíšené jednotky skutečně vedou na matematiku úloh 1/2, která má
obecné důkazy v `radix-basic.md`. Konkrétní starověké tabulky zde
nebyly určeny a datovány; úvodní kulturní shrnutí není nový nález.

**Oughtred.** [Katalog Folgerovy knihovny](https://catalog.folger.edu/record/452265)
potvrzuje čtvrté vydání *Clavis Mathematicae*, Oxford 1667,151 stran,
s reprodukcí exempláře Bodleian Library. Získán byl pouze katalog;
odkazovaný text VI.18 a jeho absence ve vydání 1631 nejsou tímto
auditem samostatně doloženy. Stránka MAA s odkazem na úplný sken
Linda Hall vrátila chybu 521; původní oba tisky nebyly porovnány.

**Al-Káší.** V textové vrstvě [citovaného ruského překladu1954](https://djvu.online/file/7jl0TnbbTm5H2)
byla přečtena kapitola na stranách126–135: převod celých čísel
postupným násobením a přičítáním, opačný převod dělením se zbytkem
a zlomky postupným násobením cílovým základem. To odpovídá 1b,1a,2a.
Příklady `(2,46,40)_60=10000` a `.376=(.22,33,36)_60` jsou přesné.
Úvod překladatele uvádí dokončení1427. Přímé stažení serveru vrátilo
ověřovací stránku, nebylo obcházeno; sazba překladu ani arabské
rukopisy nejsou v tomto bloku přečteny. Výrok o neznalosti díla
v Evropě není nezávisle prokázán. [Katalog rukopisu British Library](https://qdl.qa/en/archive/81055/vdc_100040164536.0x000001)
podporuje identifikaci díla, nikoli všechny uvedené algoritmy.

**Hugh Jones.** [British Library Add MS21893](https://searcharchives.bl.uk/catalog/040-002034360)
eviduje jeho rukopis o oktávovém počítání. Samotné výrazy
„octavation/decimation“ a hodnocení obratnosti metod nebyly ověřeny
v rukopisu. Novodobé opakování Knuthovy věty není nezávislý doklad.

**Legendre.** Přečten originál1798, strana229, poznámka pod čarou
([obrázek](../images/radix-legendre-p229.png),
[jednostránkový výňatek](../sources/legendre-1798-p229.pdf)).
Opravdu opakovaně dělí64 a seskupuje šest binárních míst:

```text
11183445 = 64*174741 + 21,
  174741 = 64*2730   + 21,
    2730 = 64*42     + 42,
11183445 = (101010 101010 010101 010101)_2.
```

Všechna čísla souhlasí. Tisk je *Essai sur la théorie des nombres*,
Paris,Duprat1798; zkrácený titul v TAOCP nehodnotíme jako chybu.
Zdrojový [sken Internet Archive](https://archive.org/details/essaisurlathor00lege)
má562stran; tištěná229 je PDF257 a leaf257 v jeho scandata
(úvodní vynechaný list způsobuje rozdíl proti naivnímu leaf+1).

## První elektronické počítače a pozdější bibliografie

**Goldstine–von Neumann.** Rok1946 je **known_erratum**: all2 i err2,
10. ledna2026, opravují na1947. Předmluva [originálu IAS](https://www.ias.edu/sites/default/files/library/pdfs/ecp/planningcodingof0103inst.pdf)
je datována1. dubna1947. Webovou textovou vrstvou byly přečteny
předmluva a §9.1–9.3, strany47–48, kde autoři zdůvodňují převody
mezi binárním strojem a desítkovým lidským vstupem/výstupem.
Obsah uvádí vlastní postupy9.6/9.7. Celé jejich instrukční programy
zde nezávisle nesimulujeme; nové datum netvoří nový nález.

**Koons–Lubkin.** [Primární článek AMS](https://www.ams.org/journals/mcom/1949-03-026/S0025-5718-49-99511-3/S0025-5718-49-99511-3.pdf)
byl přečten webovou textovou vrstvou na427–429. Převádí BCD zlomek
pro EDVAC. Místo samostatného vyříznutí číslice ponechává i nižší
číslice a upravuje násobicí konstanty. Pro číslice d_i definujme
t_i=sum_(j>=i) d_j*16^(-(j-i+1)), y_(m+1)=0 a
y_i=a_i*(t_i+y_(i+1)). Volí a_1=8/5,a_2=3/80,a_i=1/10 pro i>=3.
Pro h=1/16,c=1/10 je koeficient d_j v y_1 pro j>=2

```text
(c/h)*[h^j + (c-h)*sum_(k=2)^j c^(k-2)*h^(j-k+1)] = c^j.
```

Teleskopický součet dokazuje přesný racionální převod; pro j=1
je koeficient c. Ověřeno také55 jednotkových vstupů. Nejde o audit
zaokrouhlování, rozmístění instrukcí či časování skutečného EDVAC.

**Bauer–Samelson1953.** Bibliografii312–316 podporuje poznámka11
v [Bauerově vlastním rozhovoru](https://archive.computerhistory.org/resources/access/text/2013/12/102746781-05-01-acc.pdf).
Celý článek nebyl získán; prvenství floating point převodu není
z pouhé bibliografie ověřitelné. Důkaz priority zde netvrdíme.

**Lake1962.** Název a rozsah468–469 se podařilo dohledat jen
v sekundárních bibliografiích. Původní text nebyl přečten; tvrzení
o konkrétních hardwarových příkladech zůstává nedoložené primárním čtením.

**Stroud–Secrest1963.** [Vydavatelský abstrakt](https://academic.oup.com/comjnl/article-abstract/6/1/62/400443)
potvrzuje ročník6,strany62–66 a vstupní/výstupní převod při
vícenásobné přesnosti pro CDC1604. Plný článek nebyl přečten.

**Kanner1965, Metropolis–Ashenhurst1965, Sikdar1968.**
[Archiv JACM](https://projects.csail.mit.edu/jacm/jacm65.html)
potvrzuje Kannerův titul a242–246. [Obsah čísla Math.Comp.](https://www.jstor.org/stable/i334514)
potvrzuje druhý titul a435–441. Sikdarův název a315–334 jsou
citovány v [pozdějším primárním článku o záporných základech](https://repository.ias.ac.in/28204/1/342.pdf),
jeho původní text však získán nebyl. Jde o ověřenou bibliografickou
relevanci, nikoli o kontrolu všech algoritmů a záruk významnosti.
Neztotožňujeme neznormalizovanou významnost s přesností roundtrip věty18.

**Plauger1992.** [Textová vrstva původní knihy](https://djvu.online/file/CUaYh63U3oOY8)
obsahuje tiráž1992 a index mapující printf/sprintf a pomocné
formátovací funkce na301–331. Rozsah odpovídá citaci; celé C podprogramy
nebyly v tomto bloku načteny ani testovány. Citace není záruka
správného zaokrouhlení ve smyslu úlohy17 pro každé vstupní číslo.

## Doplněk errata2021: převod bez hardwarového dělení

All2-pre,2. května2021, přidává Granlund–Montgomery1994,61–72.
Přečteno PDF z [veřejného reprintu](https://blol.org/wp-content/uploads/2008/01/divcnst-pldi94.pdf),
strany souboru3,10,11: věta4.2 a výpis pro čtyři architektury.
Tvrzení, že násobení a posuny mohou odstranit instrukci dělení
při binárně-desítkovém převodu, je doloženo. Nejde o tvrzení,
že roku1994 skončil vývoj nejrychlejších převodů.

Pro úplnost, jádro postačující podmínky lze ověřit přímo. N je
počet bitů vstupu, d>0 pevný dělitel a m,ell nezáporná celá čísla.
Pokud 2^(N+ell)<=md<=2^(N+ell)+2^ell, zapišme
n=qd+r,0<=r<d,0<=n<2^N a k=md-2^(N+ell). Pak

```text
mn/2^(N+ell) - q = r/d + k*n/(d*2^(N+ell)),
0 <= pravá strana < (d-1)/d + 1/d = 1.
```

Podlaha tedy vrací přesný q. Pro32bitové dělení10 stačí
m=3435973837,ell=3, protože10m=2^35+2. Zbytek je n-10q.
Kontrola141072 hraničních a náhodných vstupů souhlasila; úplný
důkaz je výše. Soubor `verify_radix_context.py` zachovává přesný
jednorázově spuštěný kód; výsledky v `results/radix-context.json`.
Samostatný opakovaný běh nebyl proveden, protože nebyla změněna matematika.

## Uzavření a omezení

Zdrojová metadata a rozsah čtení jsou v `sources/radix-context-manifest.json`.
Původní errata v obrázcích `radix-all2-pre-9.png` a `radix-all2-7.png`
zůstávají dokladem známé změny2021 a2026. Historický audit je
uzavřen v popsaném rozsahu, s výslovnými nedostupnými primárními
doklady. Nevyplývá z něj nové tvrzení o prvenství ani nová odměna.
Matematika textu A–E a všech19 úloh má samostatné důkazy či
u výzkumné15 výslovně vymezené závěry. §4.4 lze uzavřít.
