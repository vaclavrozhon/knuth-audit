# Kořenová revize úplnosti erratových dodatků

X0671 přijímá zmrazené předání `parallel/errata-additions/`.
Manifest obsahuje 129 souborů o celkové velikosti 17954844 bytů;
root nezávisle porovnal všechny délky a SHA-256. Vstupní scope,
ledger a mapa odpovědí odpovídají přesně commitu `56c6d2f`.
Pozdější změny evidence se tedy nepovažují za chybu tohoto snímku.
Výsledek strukturální kontroly je
`results/errata-additions-root-validation.json`.

Podagent přímo přečetl všech 101 stran čtyř PDF, včetně úvodů
a rejstříkových seznamů. Root přečetl celý report, skript stavějící
inventář, soupis všech 145 obsahových skupin a jejich vymezených
mezer. Ověřil jednoznačnost identifikátorů, existenci obrazů,
vazby všech skupin a shodu šesti přidaných čísel s globálním
soupisem. Znovu přímo zobrazil čtyři úvodní strany a tři strany
nového Eulerova překladu. Netvrdí vlastní druhé přečtení všech
101 stran ani opakované matematické testy.

Inventář obsahuje 976 nezávislých skutečných záhlaví, 160 jejich
protějšků v krátkém aktuálním seznamu a 15 fiktivních příkladů
Page 666 z úvodních vysvětlivek. Dvě záhlaví spojená chybou OCR
byla oddělena. Číslo 1136 je počet skutečných záhlaví včetně
duplikátů, nikoli počet nezávislých oprav nebo nových chyb.

Přesně šest nových čísel je §1.2.2-30, §1.2.4-50, §1.2.7-25,
§1.3.3-37, §1.3.3-38 a §1.4.3.1-9. Sedm skupin úplných přepisů
zasahuje deset starých čísel. Z 21 záhlaví „new answer“ se 15
týká 16 starých čísel; zbývající patří k přidaným úlohám nebo
pozdější opravě jejich odpovědi. Šest nových čísel proto nemůže
sloužit jako zástupný počet všech obsahových změn.

Celkem 145 obsahových skupin propojuje 232 záhlaví s dosavadní
evidencí. Zbývající drobné opravy a změny zadání jsou zachovány
zvlášť. Ve všech přidaných úlohách existuje vlastní matematický
nebo programový důkaz. Historické zdroje i otevření kandidáti
si ponechávají svůj stav; 88 skupin napojených na otevřený záznam
neznamená 88 nově objevených mezer.

**Oprava slovního popisu předání:** skupina
`mix-digit-sum-solutions` (pořadí 100) nesprávně píše o součtu
číslic. §1.3.1-23 je obrácení pořadí pěti bajtů a k němu patří
Dixonův i Wahidův program. Cíl, zdroj i připojený audit jsou
správné; jde o chybu názvu a shrnutí v našem inventáři, nikoli
o nález v TAOCP. Zmrazené soubory zůstávají beze změny a tato
kořenová poznámka je autoritativní kvalifikací.

Globální položka dodatků má nyní uzavřený inventář, ale zůstává
`partial` pro konkrétní zděděné obsahové a pramenné mezery.
Není důvod převést všechny připojené položky na `checked` pouze
proto, že byl jejich seznam úplně sestaven.

## X0672: Euler E477, §§1–2 v překladu

Root přímo přečetl titul, úvod a §§1–2 na stranách 1–3 překladu
Alexandra Aycocka, stejně jako podagent. Překlad rozděluje součin
dvou řad na dva trojúhelníky a navíc přičítá diagonálu. Je-li
zeta(s)=sum_(k>=1) k^(-s), pak pro reálná m,n>1 dostáváme

```
sum_(k>=1) k^(-m) sum_(j=1)^k j^(-n)
+ sum_(k>=1) k^(-n) sum_(j=1)^k j^(-m)
= zeta(m) zeta(n) + zeta(m+n).
```

Absolutní konvergence v tomto oboru dovoluje přeskupení. Konečná
verze s horní mezí N je algebraické rozdělení všech dvojic indexů
a byla již dokázána v `harmonic-finite.md`, bez omezení exponentů
potřebných pro nekonečnou konvergenci. Přeložený §2 proto opravdu
obsahuje relevantní historický protějšek úlohy §1.2.7-25.

Původní latinská sazba konkrétní pasáže nebyla získána. X0672
označuje přečtený překlad, ne celý 56stránkový dokument ani
ověření první latinské publikace. X0091 a přidaná úloha 25 si
z tohoto důvodu ponechávají pramenný stav `partial`.

## V1-C0077: číslo dotisku v úvodech errat

Na prvních stranách `all1` a `err1` je uveden 27. dotisk a rok
prvního tisku 2022; `all1-pre` uvádí pro 27. dotisk rok 2011
a pro 49. dotisk rok 2022. Root tento rozdíl přečetl přímo ze
všech čtyř PDF. Jde o jeden společný redakční kandidát, nikoli
dvě matematické chyby. Pracovní zpráva je
`parallel/errata-additions/printing-introduction-mismatch.txt`.

Záměna 27th za 49th je pravděpodobná oprava, ale bez příslušných
tiráží ji nepovyšujeme na nezávisle doložené přesné opravné znění.
Předání zachovává kontrolní součty PDF i absenci dalšího vysvětlení
ve všech čtyřech vrstvách. Nic nebylo odesláno.
