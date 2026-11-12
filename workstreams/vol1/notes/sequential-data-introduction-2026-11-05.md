# Souvislý průchod §2.1 — 5. listopadu 2026

Přímo přečteny všechny originály 232–237 a příslušné odpovědi
534–536. Porovnány úplné `parallel/linear-lists/notes/intro-proofs.md`,
pramenný rozbor a uložených 1260 kontrol v `results/intro-programs.json`.
Výpočty nebyly znovu spuštěny. Současné čtyři vrstvy errat jsou
vypsány s otisky v `sources/sequential-2026-11-05/data-introduction-errata-extract.json`.

## Definice, obrázky a algoritmy

Rozlišení uzlu, pole, adresy uzlu a konkrétní proměnné F(L) je
konzistentní. NEXT zabírá poslední dva byty prvního slova, TITLE
celé druhé slovo. Lambda je hodnota, která není adresou uzlu;
zvolená 0 tedy předpokládá, že tam žádný uzel neleží. Řetěz karet
je 242→386→100→Λ. Všechny hodnoty v(4), směry šipek, TAG a SUIT
souhlasí, s jedinou známou vadou: TITLE poslední karty v(3) má D
místo C, ačkoli SUIT=1 i původní obrázek(2) určují kříže.

Algoritmus A vloží novou, dosud nezařazenou kartu před původní
řetěz a nastaví TAG=0; správně zahrnuje prázdnou hromádku. U B
platí, že N počítá již navštívený prefix a X je následující uzel.
Každá iterace prefix prodlouží; konečnost řetězu dává ukončení.
Nikdy se nečte NEXT(Λ). Volné, nepřekrývající se kartové uzly
jsou významem reprezentace, ne dodatečným omezením kvůli opravě.
Překlad A do MIX zapisuje právě NEXT, TOP a TAG, zachovává ostatní
pole. Ani krajní platná adresa dvouslovného uzlu 3998 nepřetéká.

CONTENTS(LOC(V)) je V pro celočíselné slovo. Obrácený výraz vyžaduje
platný nenulový odkaz; úloha mluví o proměnné V, nevylučuje tak
konstantní adresy jako CONTENTS(1000) v hlavním textu. Kopie celého
uzlu v(7) má správně 0≤j<c. Adresa symbolu TOP v MIXAL a hodnota
proměnné TOP v algoritmu jsou výslovně rozlišeny.

## Devět odpovědí

1–3: hodnoty 4 a Λ, typová podmínka LOC/CONTENTS a odebrání prvního
uzlu přímo souhlasí. „Essentially undoes“ nepožaduje znovuvytvořit
původní TAG nové karty; úloha žádá její odebrání.

4–5: pomocná hlava S=LOC(TOP), NEXT(S)=TOP je v odpovědi výslovně
zavedena. Vložení na konec proto funguje i pro prázdný řetěz.
Při odebírání platí Y=NEXT(X); X je předchůdce nebo pomocná hlava.
Pro jedinou kartu se tedy správně vynuluje TOP. Neformální komentář
„next-to-last card“ nepřepisuje tento uvedený invariant ani správný
jednoprvkový případ.

6–8: CARD je uzlová hodnota, proto SUIT(LOC(CARD)) a SUIT(TOP),
nikoli SUIT(CARD). LDA TOP(NEXT) dává 242; až indexované načtení
na této adrese dává požadovaných 386. Program B správně skočí
přes všechny tři smyčkové instrukce při prázdném řetězu, jinak
počítá a posouvá ukazatel, bez změny paměti.

9: tiskárna se testuje před prvním zápisem do obsazeného PBUF.
Konstanty PAREN/BLANKS se úmyslně překrývají; přebytečná závorka
v prostředním slově se celá přepíše TITLE karty. Zbylých 21 slov
řádku zůstává podle obecné konvence MIXAL nulových, tj. mezerových.
Prázdná hromádka tiskne PILE EMPTY. Poslední výstup smí doběhnout
po HLT. Dřívější testy zahrnují 48 úplných tiskových případů,
báze 64/100 a latence 0/1/97, kontrolují i zachování uzlů a TOP.
Obecnou správnost dokládají invarianty, ne počet konečných případů.

## Prameny a stránkové pokrytí

Oba epigrafy na232 mají přijaté konkrétní primární/ediční doklady:
Poetry, srpen1913, s.160 a edice Hamlet I.5.98. Další vzdálené
části básní ani Shakespeare se neauditují. Úvahy o vhodnosti vlastních
List struktur jsou metodické soudy, nikoli univerzální benchmark.
Budoucí kapitoly9/10 se čtou v rámci tehdejšího plánu díla.

X0961 odděleně registruje dvě již známé opravy z1997, dříve přítomné
jen v pramenné poznámce: JAVA→Java a chybné TITLE. Červeně se mapuje
skutečný rozpor obsahu obrázku na234; samotná kapitalizace názvu
jazyka není zde počítána jako matematická/faktická vada celé233.
Nejde o nový neznámý nález.

Všech devět úloh i celý hlavní text zůstává checked. Strany232–237
a535 mají úplné pokrytí. Doplnění tří odpovědí na534 uzavírá i celou
tuto stranu společně s předchozí kontrolou I/O. Na536 je zatím
zkontrolován jen konec tiskového programu; zbytek patří §2.2.1.
Pokračování je na238, lineární seznamy.
