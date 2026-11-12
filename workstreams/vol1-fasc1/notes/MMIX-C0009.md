# MMIX-C0009 — záměna indikátorů v časové analýze MemFind

**Confirmed, low**, po krátkém rozpisu jednotlivých cest dne 6. 11. 2026.
Původní candidate z prvního průchodu se tím uzavírá. Místo: odpověď
§1.4.3′–2, p. 117 / file 125, odstavec pod tabulkou; definice na
p. 116 / file 124 a kód MemFind na p. 78 / file 86.

P. 116 správně definuje U=[key≠curkey], A=[new node needed] a cenu

    9υ + (2μ+8υ)C + (3μ+6υ)U + (2μ+11υ)A.

P. 117 však pro dvě nutná přepnutí mezi kódovým a datovým chunkem
použije C=A=2 a výsledných 13μ+158υ. Pokud jsou oba chunky již přítomné,
jsou správné hodnoty C=U=2,A=0. U nemůže být nula při A>0 ani při
výslovně popsaných misses. Jde tedy o chybnou záměnu rolí indikátorů,
nikoli o zvolenou konvenci počítání hranice instrukce.

## Přímý profil

Fast hit: řádky 029–031 stojí 3υ; 048–051 mají 6υ, tedy 9υ.
Při ne-head hitu s C porovnáními mají search iterace 2C paměťových
operací a 8C−2υ (poslední BNZ není taken). Mimo ně přibudou
2υ za chybně predikované PBZ, BN 1υ, SET 1υ a čtyři instrukce
044–047 s 3μ+4υ. Penalta je tedy `(2μ+8υ)C+3μ+6υ`.

Při alokaci je všech C kandidátů neúspěšných, tedy jejich větve stojí
o 2υ více než v předchozím vzorci; závěrečná nulová LINK iterace a
alokace přidají 2μ+9υ. To přesně dává další 2μ+11υ. Vzorec na
p. 116 je tak nezávisle doložen v obou případech.

Pro konkrétní dvě již existující položky seznamu a střídání jejich
adres jsou obě volání C=1,U=1,A=0. Dohromady přidají 10μ+28υ,
nikoli vytištěných 8μ+38υ. S uvedeným základním řádkem 5μ+120υ
by výsledkem bylo **15μ+148υ**. I samotný počet μ je přímo rozhodný:
základ má fetch, info, načtení globálních X/Y a STHT, tedy 5 přístupů;
každý ze dvou ne-head hitů přidá pět, celkem 15, nikoli 13.
Ostatní řádky celé tabulky se tím ještě nepovažují za kompletně ověřené.

Empirické hodnoty U≈.00001 a A≈.16 na konci odstavce mají rovněž
zjevně opačné role oproti definicím (musí platit A≤U na každém volání).
Skutečné historické průměry se nereprodukovaly a jejich správnost
nelze odvodit jen přehozením jmen.

Sazba všech tří stran znovu zobrazena: images/file-086-p078.png,
file-124-p116.png a file-125-p117.png. Relevantní původní i textové
vrstvy errat neobsahují opravu indikátorů či času; viz
results/errata-C0009-C0012.json. Nová chyba neovlivňuje funkční
výsledek MemFind, pouze jeho analytické a odvozené časové údaje.
