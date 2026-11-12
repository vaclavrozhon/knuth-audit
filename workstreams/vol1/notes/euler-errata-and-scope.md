# §1.2.11.2: rozsah, errata a prameny

Audit 1. listopadu 2026. Ověřeny obrazy s.111–116 a odpovědí
503–504 v prvním dotisku třetího vydání; souborová strana je o 15
vyšší. Všech devět původních úloh je skutečně přítomno. Hodnocení
jsou 1:M18, 2:HM20, 3:HM20, 4:HM20, 5:HM30, 6:HM30,
7:HM32, **8:M23**, 9:M25. OCR i Markdown chybně čtou u 8 M25.
Žádná další úloha v prohlédnutých erratech nalezena nebyla.

## Matematické pokrytí

| Rozsah | Doklad a výsledek |
|---|---|
| (1)–(13), úlohy 1–3 | [euler-summation.md](euler-summation.md): oba způsoby sčítání krajních členů, obě konvence Bernoulliho čísel, obecný integrální zbytek, jeho velikost i znaménko |
| Úloha 4 | Tamtéž: součet mocnin pro všechna celá m,n>=0 včetně 0^0=1 |
| (14)–(19), úlohy 5–6 | [euler-applications.md](euler-applications.md): harmonická čísla, logaritmus faktoriálu, Wallisova konstanta, jednotný odhad pro kladný reálný argument |
| Úlohy 7–9 | [euler-products.md](euler-products.md): hyperfaktoriál, konstanta A, kvadratický argument faktoriálu, poměr binomických koeficientů a dyadické koeficienty |
| Přepis a numerické hodnoty | [check_euler_summation.py](../check_euler_summation.py), [výsledek](../results/euler-summation.json): 1915 úspěšných přesných kontrol |

Kontrola koeficientů středního binomického koeficientu používá dvě
různé konstrukce: logaritmický Stirlingův rozvoj a interpolaci
diagonál celočíselné tabulky počtů cyklů. Konstanta A je uzavřena
racionálním intervalem mezi 1.2824271291005600 a 1.2824271291006229;
odhad vychází z konečného součtu logaritmů a dokázaného zbytku,
nikoli z numerického vyhodnocování funkce zeta. Konečné testy
doplňují obecné důkazy; nedokazují samy asymptotické věty.

Nový potvrzený problém ani nový kandidát v tomto bloku nevznikl.
Matematika všech úloh je ověřena; úlohy 3,7,9 zůstávají ve společné
mapě `partial` kvůli níže uvedeným konkrétním citačním mezerám.
Hlavní text je `partial` z téhož důvodu. Ostatních šest úloh je `checked`.

## Všechny časové vrstvy oprav

Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1`, včetně názvů,
čísel rovnic a odpovědí. Záznamy jsou v
[euler-errata-extract.json](../sources/euler-errata-extract.json).
Obsahují i sousední §1.2.11.1 na s.503; tyto záznamy byly odděleny.
Aktuálnost souborů dokládá dřívější obnovení všech pěti pramenů
[1. listopadu 2026](../sources/errata-refresh-2026-11-01.json).
Samotná krátká řada err1 řadu níže uvedených změn neobsahuje.

- 1997–2008: chybějící závorka v odpovědi 1 (1.8.1997), odkaz
  na (9′) (4.11.2001), argument f^(m)(x) a znaménko minus před
  integrálem (10. a 28.11.2002), zbytečný faktor (−1)^m pro sudé m
  v úloze 3 (1.1.2006), závorky okolo faktoriálů (1.1.2006), tečka
  za definicí relativní chyby (3.5.1998), jméno James Bernoulli
  a upřesnění evropských matematiků (20.3.2006), Kinkelin–Glaisher
  místo Glaisher (20.5.2005), člen **(ln a)/2** v odpovědi 8
  (1.1.2006), uzavření O-závorky v odpovědi 9 (24.3.1998).
- 2012–2013: závorky jmenovatele poměru v úloze a odpovědi 8
  (18.2.2012), absolutní hodnota odhadu zbytku (26.2.2013), rok
  Steffensenovy knihy 1927 místo 1937 (5.3.2013).
- 21.3.2021: konzistentní přechod B_1=−1/2 na B_1=+1/2.
  Nový obrázek 12, rovnice (3)–(8),(10),(14),(15),(17), inkluzivní
  součty a odpovědi 1,4,6,7 jsou ověřeny ve správné konvenci.
  Bernoulliho polynomy samy zůstávají stejné. Současný součet
  mocnin obsahuje n i 0; člen 0^m v odpovědi 4 je nutný pro m=0.
  Zahrnuta nová poznámka o Luschnym a přesnější odkazy na Eulera
  a definici konečné aproximace gama funkce.
- 2023: m! bez závorek (29.3.), Kinkelinovy strany **122–138**,
  nikoli 122–158 (29.3.).
- 4.9.2024: Bernoulliho čísla nejsou přímo koeficienty bez j!,
  vysvětlení sudosti, první **nenulový** vynechaný člen, upřesnění
  dolní meze v úloze 4, x→infinity v úloze 6 a nezbytný počáteční
  polynom B_1(x)=x−1/2 v odpovědi 2.
- 29.1.2026: název hyperfaktoriál v úloze 7.

Sazba podstatných změn ověřena na obrazech řad pre/prepre i all1,
zejména `errata-all1-pre-file009.png` až `file011.png` a
`errata-all1-prepre-file012.png`, `file036.png`. Oprava fráze v úloze 4
je v seznamu lokalizována na s.114, ačkoli úloha je ve skenu na s.115;
nebyla proto opomenuta při hledání pouze podle stránky.

## Primární prameny a přesné meze čtení

- Bernoulli, *Ars conjectandi* (1713): získán veřejný úplný sken
  Smithsonian/Internet Archive. Přečtena titulní strana a s.97–99
  (PDF strany 7,147–149; čísla listů v scandata nelze slepě posunout
  o jedna). Na s.97 je tabulka součtů mocnin a obecný vzorec s kladným
  polovičním členem; s.98 identifikuje další koeficienty. To dokládá
  obsah citace i konvenci. Nejde o ověření historického prvenství.
- Euler E025 a E047: relevantní odvození skutečně přečtena
  v překladech Alexandra Aycocka uložených univerzitou Mainz.
  E025: strany 1–3, zejména §2; E047: strany 1–2 a 8–12,
  zejména §§15–22. Obsahují integral+f/2+f′/12−f‴/720+…,
  rekurenci koeficientů i příklady součtů mocnin. Skeny přímo
  citovaných latinských stran nebyly získány (Euler Archive 403).
  Archiv rozlišuje roky sepsání 1732/1735 a vydání 1738/1741.
  Překlad E047 má v poznámce rok 1738; tento nesoulad není chybou
  Knuthovy knihy a překlad nepovažujeme za kontrolu původní sazby.
- Peter Luschny, [The Bernoulli Manifesto](https://luschny.de/math/zeta/The-Bernoulli-Manifesto.html):
  uložen a přečten úvod, oba generující vzorce a zdůvodnění volby
  B_1=+1/2. Text je výslovně věnován výročí 1713–2013. Nedokládáme
  každý historický či polemický výrok této webové eseje.
- NIST [DLMF 25.4.2](https://dlmf.nist.gov/25.4#E2): přečtena
  funkcionální rovnice a uložena její oficiální TeX reprezentace.
  Je použita jako standardní analytická věta při odvození druhého
  vyjádření A, nikoli jako náhrada výpočtu jeho číslic.
- Seki: katalogy Národní parlamentní knihovny Japonska a Kjótské
  univerzity dokládají posmrtné vydání *Katsuyo sanpo* roku 1712
  a vazbu druhého svazku na součty mocnin. Konkrétní citovaný
  soubor *Collected Works* (Osaka 1974), s.39–42, ani matematická
  sazba původního japonského textu zatím nejsou přímo prověřeny.
- Steffensen, *Interpolation* (1927), §14: katalog a obsah potvrzují
  rok a začátek oddílu na s.129. Samotné citované odvození zatím
  nepřečteno; naše odhady (E8)–(E11) mají nezávislý úplný důkaz.
- Kinkelin 1860, Glaisher 1877 a de Bruijn §3.7: matematické
  identity konstanty jsou dokázány, ale konkrétní citované pasáže
  zatím ne. Kinkelin: GDZ 404, EuDML 403, odkaz vydavatele
  nedostupný. Seznam opravených stran není vydáván za přečtený článek.
- Knuth–Vardi, AMM 97 (1990), 629–630: autorská bibliografie
  potvrzuje řešení úlohy 6581; text na JSTOR nebyl přístupný.
  Obecné tvrzení o mocninách 2 ve jmenovatelích je dokázáno
  nezávisle celočíselnými Newtonovými koeficienty.
- Doporučené alternativní odvození v *Concrete Mathematics* §9.5
  zatím nebylo přečteno. Základní Eulerův vzorec i celý zbytek
  jsou zde odvozeny přímo.

Lokální metadata zaznamenávají adresy, otisky a skutečný rozsah
čtení. Nedostupnost jednoho pramene neznamená neplatnost citace.
Tyto konkrétní bibliografické zbytky zůstávají v X0135 pro další průchod.

## Chyby pomocného Markdownu pro koordinátora

Soubor `md/vol1/15-1.2.11.2-eulers-summation.md` nebyl měněn.
Samotná stará konvence B_1=−1/2 není chyba, je-li použita konzistentně.
V přepisu jsou však další věcné odchylky:

- V Eulerově součtu užívá indexy 2j do 2m, ale následný zbytek
  má řád m; tyto dva vzorce nelze společně použít.
- U harmonických čísel mizí faktor (−1)^(k−1). Definice konstanty
  faktoriálového rozvoje se mění na nekonečný divergentní součet;
  originál pracuje s pevným konečným m a integrálním zbytkem.
- Úloha 3 mění m-tou derivaci na (m+1)-ní a <= na <.
  Například nulová funkce ostrou nerovnost vyvrací; sken je správný.
- Úloha 5 má nepůvodní nedefinovaný symbol e_n místo zadaného
  asymptotického vzorce. V úloze 7 mizí exponenty součinu.
- Úloha 8 nahrazuje zadaný poměr binomických koeficientů jiným
  faktoriálovým poměrem a mění hodnocení M23 na M25.

Tyto vady nejsou započítány jako nové chyby TAOCP.

## Doplnění 2. listopadu 2026: původní Eulerova sazba

X0682 překonává výše uvedenou nedostupnost latinských originálů:
root přímo přečetl E25 s. 68–70 a E47 s. 9–22 včetně titulů
svazků. Citovaný sumační vzorec je potvrzen z původní sazby.
Přesné meze, otisky a kandidát C0082 k roku ročníku v opravě
2021 jsou v `euler-summation-originals.md`. Ostatní pramenné
mezery X0135 zůstávají otevřené; počty cvičení se nemění.

## Doplnění X0688: Kinkelin a Glaisher

Obě výše uvedené nedostupnosti byly překonány novými původními
skeny. Kinkelin122–138 a Glaisher43–47 jsou obsahově ověřeny,
včetně převodu konstant a rozdílu roku článku/svazku. Přesný
rozsah root a agentovy četby uvádí kinkelin-glaisher-root-review.md.
Úloha7 má nyní jedinou konkrétní pramennou mezeru de Bruijn§3.7;
ostatní nezávislé mezery X0135 se tím nemění.

## Doplnění X0689: konkrétní citace CMath

Celá §9.5 s integrálním zbytkem a jeho odhady je nyní přímo
přečtena; přesně rozlišena starší a současná konvence. Ostatní
nezávislé citace v X0135 zůstávají otevřené.
Rozsah četby a důkazové porovnání uvádí
`concrete-citations-root-review.md`. Počty úloh se nemění.
