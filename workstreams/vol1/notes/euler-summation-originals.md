# Eulerovy originály: sumační vzorec a sudé hodnoty zeta

Root kontrola 2. listopadu 2026, X0682. Eneströmova čísla E25,
E41 a E47 označují jednotlivé Eulerovy práce v katalogu jeho díla.
Nově získané veřejné skeny časopisů uzavírají konkrétní mezeru
v původní sazbě E25/E47 z X0135. E41 navíc přímo dokládá čtyři
hodnoty funkce zeta připsané Eulerovi na knižní s. 76.
Historická četba není náhradou moderních důkazů ani audit všech
matematických tvrzení v původních článcích.

## Identita pramenů a rozsah přímé četby

Internet Archive poskytl svazky ze sbírky AMNH/Biodiversity
Heritage Library. PDF byly porovnány s MD5 uvedenými v jejich
archivních metadatech; souhlasí. SHA256, velikosti, URL a časy
stažení jsou v `sources/euler-summation-followup/retrievals-originals.json`.
Archivní datum řady 1726 neoznačuje datum vydání jednotlivého svazku.

| Pramen | Originální strany přímo čtené rootem | Meze |
|---|---|---|
| E25, *Methodus generalis summandi progressiones*, Commentarii 6 | titul svazku; 68–70, zejména celé §§1–2 | Strany 71–97 nebyly čteny. Na 70 začíná další postup; pokračování §4 není tímto blokem uzavřeno. |
| E47, *Inventio summae cuiusque seriei ex dato termino generali*, Commentarii 8 | titul svazku; celý článek 9–22, §§1–34 | Čteno pro obsah citace, koeficienty sumačního vzorce a způsob použití; neproběhla kontrola všech desetinných tabulek a všech historických limitních kroků. |
| E41, *De summis serierum reciprocarum*, Commentarii 7 | celý text 123–134, §§1–19 | Oddělená obrazová tabule VII nebyla otevřena; pro čtyři citované identity není potřebná. |

Přesná vazba tištěných a PDF stran je v obou souborech
`page-map-initial.json` a `page-map-e25.json`. Všech jejich 31
obrazů root skutečně zobrazil. Svazek 7 byl získán již v X0679
a jeho původní manifest zůstává beze změny.

Katalog Euler Archive rozlišuje sepsání a vydání:
[E25](https://scholarlycommons.pacific.edu/euler-works/25/)
1732 / 1738,
[E47](https://scholarlycommons.pacific.edu/euler-works/47/)
1735 / 1741 a
[E41](https://scholarlycommons.pacific.edu/euler-works/41/)
1735 / 1740. Údaj ročníku na titulní straně je ještě třetí údaj,
viz kandidát níže. Katalogový matematický souhrn nebyl použit místo
četby originálu.

## Co je přímo doloženo pro sumační vzorec

V E25 §2, s. 69, značí t obecný člen posloupnosti s indexem n
a s součet od prvního členu po t včetně. Euler uvádí formální
rozvoj rozdílu s(n)−s(n−1) a jeho obrácení:

```text
t = s' − s''/2! + s'''/3! − ...,
s = integral(t dn) + t/2 + t'/12 − t'''/720 + t^(5)/30240 + ... .
```

Čárky zde označují derivace podle n, t^(5) pátou derivaci;
integrační konstanta se určuje z počátečního součtu. Koeficienty
a kladné znaménko polovičního členu souhlasí s již přečteným
překladem a s konvencí opravy knihy z roku 2021. Po opraveném
zúžení bibliografického rozsahu na 68–69 je příslušná původní
pasáž přečtena celá. Původní širší citace 68–97 neznamená tvrzení,
že každá strana článku je zapotřebí pro uvedený vzorec.

E47 nejprve odvozuje Taylorův rozvoj (§§4–6), pak přechází od
S(x)−S(x−1)=X(x) k rekurenci koeficientů (§§12–18, s. 13–15).
X označuje obecný člen, S odpovídající částečný součet.
§19 na s. 16 píše tentýž sumační vzorec. §§20–23 vysvětlují
ukončení rozvoje pro polynomy, normalizaci S(0)=0 a příklady
součtů mocnin. §§24–34 používají vzorec pro aproximace, včetně
harmonických součtů a převrácených mocnin; §28 výslovně upozorňuje
na nekonvergenci jednoho vzniklého rozvoje. Tato historická
formální řada sama nedodává moderní integrální zbytek. Ten byl
nezávisle dokázán v `euler-summation.md` a nyní se neopakoval.

Předchozí hlavní poznámka správně mluvila obecně o překladech.
Pro přesnost: uložený Aycockův E25 je anglický, uložený E47
(`47.pdf`) je německý. Rok 1738 v poznámce tohoto překladu E47
není rok původního svazku ani chyba Knuthova textu.

## E41 a knižní hodnoty zeta

Pro reálné r>1 je zde zeta(r)=sum(k^(-r), k>=1). E41 §2,
s. 124, výslovně oznamuje vztah součtu převrácených čtverců
a čtvrtých mocnin k obvodu kruhu. §§11–13, s. 128–130,
odvozují hodnoty pro r=2,4,6,8 a §18 na s. 133 je vypisuje
společně:

```text
zeta(2) = pi^2/6,       zeta(4) = pi^4/90,
zeta(6) = pi^6/945,     zeta(8) = pi^8/9450.
```

Eulerovo p v tomto místě znamená obvod kruhu o průměru 1,
tedy dnešní pi. Tyto čtyři formule jsou právě knižní (7), s. 76,
kterou root znovu přímo porovnal. Atribuce těchto konkrétních
hodnot je tedy ověřena z originálu. Článek obsahuje rekurzi
pro další sudé mocniny, ale neuvádí obecný vzorec přes Bernoulliho
číslo v přesné podobě knižní (6). Četba E41 proto sama neuzavírá
celou historickou atribuci (6) ani odkaz na CMath §6.5.
Eulerovo zacházení s nekonečným součinem se zde nepovažuje
za automatický moderní důkaz jeho analytické konvergence.

## C0082: rok ročníku ve veřejné opravě

Obraz `errata-all1-pre-file008.png` obsahuje na konci změnu
s. 111 z 21. března 2021: `6 (1732), 68–69; 8 (1735), 9–22`.
Titul skutečně získaného osmého svazku má `TOMUS VIII`,
`AD ANNUM MDCCXXXVI` (1736) a tiskový rok 1741. Rok 1735
odpovídá sepsání E47 podle Euler Archive, nikoli vytištěnému
ročníku 8. U svazku 6 se údaj 1732 shoduje s prvním ze dvou
roků na titulu (1732–1733); u dříve čteného svazku 7 odpovídá
1734 prvnímu roku 1734–1735.

Jde o kandidáta na bibliografické upřesnění: nahradit u svazku 8
rok 1735 rokem 1736, nebo výslovně odlišit sepsání od ročníku.
Není to domnělá záměna 1735 a tiskového 1741 ani chyba původního
tisku 1997, který E47 vůbec necituje. Záměr této datační konvence
a úplné pozdější vydání knihy nebyly ověřeny, proto stav zůstává
`candidate`. Všechny čtyři veřejné vrstvy errat byly znovu
prohledány podle s. 111 i souvislostí Euler/Petrop/1735;
`errata-date-review.json` obsahuje nalezený blok a otisky vstupů.
Odpovídající pozdější oprava roku nebyla nalezena.

## Co nadále zůstává otevřeno

X0135 je nadále `partial`: konkrétní Seki 1974, Steffensen §14,
Kinkelin/Glaisher/de Bruijn, Knuth–Vardi a CMath §9.5 nejsou
tímto čtením vyřešeny. X0091 je nadále `partial`: obecná atribuce
zeta přes Bernoulliho čísla, CMath §6.5, Cullen 2007 a konkrétní
prameny úloh 7,17,18,20. Počet uzavřených cvičení se tímto
pramenným blokem nemění. Nové matematické testy nebyly potřebné.
