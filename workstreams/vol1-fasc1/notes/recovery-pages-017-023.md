# Rekonsiliace file 17–23 / p. 9–15

6. listopadu 2026. Celý text těchto sedmi stran je znovu porovnán se
samostatnými V0038–V0064 v `independent-arguments-009-015.md`, ne jen
se seznamem startovních ID. Matice se porovnala se starším přímým
čtením sazby file 19; všechny zdejší příklady a definice mají přesné
níže uvedené umístění. Výklad FP zůstává částečný.

| File / p. | Celý rozsah tvrzení a definic | Argument / zbývající část |
|---|---|---|
| 17 / 9 | DIVU fallback a zero divisor; rD; LDA; 2/4/8/16ADDU a násobení 3; NEG/NEGU; SL/SLU/SR/SRU včetně z≥64 a časových/vedlejších rozdílů; CMP/CMPU | V0038–V0043, zpřesnění NEG níže |
| 18 / 10 | Všech osm CS a osm ZS, znaménkový a paritní bit; všech osm bitových operací a každá ze čtyř dvojic tabulky (8) | V0044–V0045 |
| 19 / 11 | MUX; SADD; BDIF/WDIF/TDIF/ODIF a rozsahy dílů; oba 8×8 obrazy (10); obecný produkt (11), indexy a associativita | V0046–V0050; přesný Iversonův bibliografický originál přeskočen |
| 20 / 12 | OR/XOR matrix produkty, obě jednostranné podmínky shody s AB, transpozice MOR/MXOR, byte reverse i poslední byte OR/XOR; obě FP pole a všechny třídy; plná IEEE deklarace; FADD/FSUB/FMUL/FDIV/FREM | V0051–V0054; FP položky rozděleny v fp-verification-items.json, aritmetika a plná IEEE shoda stále partial |
| 21 / 13 | FSQRT/FINT; tři obyčejná a tři epsilon porovnání; šest konverzí plus LDSF/STSF; čtyři režimy a override Y; ROUND_UP příklad; dvě fáze SFLOT; remainder, signed zero/NaN/∞ upozornění; začátek immediate pravidla | V0055–V0056, fp-comparisons-recovery.md, fp-conversions-recovery.md; každá zbývající operace/příznak má samostatnou partial položku |
| 22 / 14 | Všechny immediate příklady a opcode+1 pravidlo; všech 16 wyde instrukcí včetně carry; sestavení libovolného octa ve čtyřech instrukcích a přesný příklad; oba významy SET | V0057–V0060 |
| 23 / 15 | Následník @+4, relativní JMP vpřed/vzad a oba hex příklady, celý dosah; GO včetně aliasu X=Y a návratu; všech osm branch podmínek/dosah; prvních pět probable variant | V0061–V0064; zbytek probable variant na file 24 bude mapován tam |

NEG pro obecné Y∈[0,255] lze zpřesnit bez výčtu vstupů. Pro
z∈[−2^63,2^63−1] je Y−z≥−2^63+1, takže dolní overflow nenastane.
Horní nastane právě pro z≤Y−2^63. Pro Y=0 je to pouze z=−2^63;
pro obecné Y jde o Y+1 dolních signed hodnot. Ostatní výsledky se
vejdou, všechny spodní bity dává obecné signed přiřazení. Starší
poznámka V0040 odkazovala na C0003 ještě jako na otevřený; nyní je
přesný saved-immediate kontrakt převzat z přijatého důkazu C0003,
bez nového běhu či nového nálezu.

Časové výroky o násobení/posunech jsou výslovně v tabulkovém modelu
1υ versus 10υ/60υ. Pozdější p. 21–23 jejich hardwarovou platnost
samo kvalifikuje. Nezávislost částí monus a maticový row selection
jsou dokázány obecně, nikoli jen pro uvedenou matici. Citace Iversona
není vydávána za ověřený historický původ definice.

**Výsledek:** file 17,18,22,23 má úplné argumentové pokrytí. File 19
má všechny matematické části uzavřené a explicitní bibliografickou
výjimku. File 20–21 je partial; dvě samostatné programové vady S0001
a S0002 neobarvují správné souhrnné definice v knize. Obecné rozbalení,
porovnání, celočíselné→FP a short-load konverze mají vlastní důkazy;
FINT/FIX hodnoty jsou odděleny od příznaků, STSF od overflow vady.
Žádná samostatná FP dílčí položka nezastupuje důkaz celé stránky.
Další sekvenční mapa začíná file 24 / p. 16.
