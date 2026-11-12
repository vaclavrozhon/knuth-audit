# Samostatné argumenty: tištěné p. 2–8 (file 10–16)

Nový průchod podle pokynu 6. listopadu 2026. Nejde o opakování celého prvního čtení: níže jsou konkrétní argumenty ke každému matematickému odvození nebo příkladu tohoto bloku. Samotné definice imaginární architektury se berou jako definice, ne jako empirická tvrzení o nezávislém simulátoru. Historické/bibliografické údaje, obecné hodnocení rozšíření architektur a jazyků nejsou dokázány těmito argumenty.

Zdroj: sources/file-010.txt až file-016.txt, kontrola sazby zejména images/file-010-p002.png, images/depth-011.png až depth-015.png a již dříve prohlédnuté images/file-016-p008.png. Existující nález C0001 se přebírá bez přepočtu. Na p. 4 je v sazbě **2^5**, nikoli 25; nativní extrakce ztrácí exponent.

## Předmluva p. iii

Hexadecimální dolar je konvenčně 0x100 běžných centů: 16² = 256 centů = $2.56. Nejde o obecné tvrzení, že stejné reálné číslo 1 zapsané v jiné soustavě mění hodnotu. Další matematický argument v předmluvě není; historické údaje zůstávají bibliografickou výjimkou.

## P. 2 — V0001–V0003

V0001, rovnice (1): číselné části jmen dávají postupně součet 1+801+2+300+29+88+601+960+21164+2+4000+4+110+64 = 28126. Součet lze seskupit jako 21164+4000+960+801+601+300+110+88+64+29+4+2+2+1. 2009×14 = 28126. K a jiné části modelových jmen nejsou násobitele; zde jde o pojmenovací hru definovanou autorem. Samotná historická dostupnost/podobnost všech modelů není tímto součtem ověřena.

V0002: římské MMIX = M+M+(X−I) = 1000+1000+9 = 2009.

V0003, (2) a (4): rozdělení na čtveřice dává
`1001 1110 0011 0111 0111 1001 1011 1001 0111 1111 0100 1010 0111 1100 0001 0110`, tedy šestnáct číslic `9e3779b97f4a7c16` a 16×4 = 64 bitů. Výrok o zlatém řezu zde není nově dokazován; viz V0037/C0001.

## P. 3 — V0004–V0009

V0004, (3): hodnota každé čtveřice b3b2b1b0 je 8b3+4b2+2b1+b0. Postupný výčet 0000,0001,…,1111 proto dává 0,1,…,15 a tabulka správně používá a,b,c,d,e,f pro 10,…,15. Záměna velikosti písmene hodnotu nemění.

V0005: osm bitů = dvě hex číslice. Šestnáct hex číslic má 16^16 = 2^64 možných slov, od nuly do 16^16−1, jehož zápis je šestnáct f. To dokazuje uvedený rozsah adres, při definované byte-addressable paměti.

V0006: ASCII M=0x4d, I=0x49, X=0x58, takže MMIX = 4d4d4958. Znaky 00–1f představují 32 pozic, 20–7e dalších 95 a 7f poslední pozici; 32+95+1=128=2^7. Konkrétní kódování nezávisle porovnáno s místním ASCII codec v results/character-examples-p003.json; klasifikace control/printing odpovídá tabulce ASCII na zadním listu, už přečtené v prvním průchodu. Originální články CACM nebyly znovu dohledány.

V0007: Latin-1 kódy p,â,t,é jsou 70,e2,74,e9. Cílená kontrola codec je uložena v character-examples-p003.json. Časový údaj o vzniku Latin-1 v osmdesátých letech zůstává bibliograficky neověřený.

V0008: jednotlivé uvedené Unicode znaky mají kódy 03a3,03c3,0429,0449,0547,0577,05e9,0634,0936,09b6,0b36,0bb7,7b97 a římské M,I,X mají 216f,2160,2169. Všechny jsou samostatně vypsány se jménem znaku v uvedeném výsledku (místní UnicodeData 15.0.0); jejich tvar byl srovnán se sazbou. Nejde o census podporovaných jazyků ani o důkaz širokého tvrzení „nearly every modern language“; to zůstává neurčité historické tvrzení, nikoli nově nalezená chyba.

V0009: Latin-1 bajty mají stejné Unicode číselné kódy 0..255, tedy při 16bitovém big-endian zápisu dostanou vysoký nulový byte. Pâté proto dává 0070 00e2 0074 00e9, nezávisle zkontrolováno codec. Poznámka o překročení původní 16bitové sady opravňuje nevykládat předchozí odstavec jako tvrzení, že celý dnešní Unicode má jen 2^16 kódových bodů. Obecné kvantifikátory o počtech běžných znaků nejsou samostatně ověřeny.

## P. 4 — V0010–V0014

V0010: 1 byte=8 bitů, wyde=2 bytes=16 bitů, tetra=2 wydes=4 bytes=32 bitů, octa=2 tetras=4 wydes=8 bytes=64 bitů. Všechny jednotkové rovnosti v prvním odstavci z těchto násobení vyplývají.

V0011: n nezávislých bitů má 2^n vzorů, jejich nesignovaná poziční hodnota je 0..2^n−1. Pro n=8,16,32,64 jsou pravé meze 255,65535,4294967295,18446744073709551615, shodné se sazbou.

V0012: dvoukomplementové zobrazení je s(u)=u pro u<2^(n−1), jinak u−2^n. Dolní půlka dává 0..2^(n−1)−1, horní −2^(n−1)..−1; celé rozmezí je tudíž −2^(n−1)..2^(n−1)−1. Pro 8,16,32,64 bitů vycházejí přesně meze −128/127, −32768/32767, −2147483648/2147483647 a −9223372036854775808/9223372036854775807. Vzor všech jedniček má u=2^n−1 a s=−1 pro všechny čtyři velikosti.

V0013: 2^8=256 obecných registrů je indexováno celým bytem 0..255. 2^5=32 speciálních registrů souhlasí s p. 5. Počty a velikosti registrů a virtuální paměti jsou definice MMIX; nevydáváme je za nezávisle otestovaný implementační fakt.

V0014: disjunktní zarovnané bloky po t=2,4,8 bytech mají počty 2^64/t = 2^63,2^62,2^61. Blok obsahující x začíná na t floor(x/t), takže má stejnou hodnotu pro všech t zbytků x mod t. Vymazání posledních log2(t) bitů je přesně toto zaokrouhlení adresy dolů. Dvojice bytů má big-endian hodnotu 256·M[2k]+M[2k+1]; stejná poziční expanze vysvětluje concatenation tetra/octa.

## P. 5 — V0015–V0017

V0015: pro libovolné celé x existuje jediný zbytek modulo 2^64 v 0..2^64−1; rozšířená definice M[x] proto adresu vždy převádí do platné paměti a zachovává obvyklou adresu, je-li už v rozsahu. Zarovnání a modulo jsou kompatibilní, protože t dělí 2^64.

V0016: seznam rA..rZ obsahuje 26 jmen, navíc rBB,rTT,rWW,rXX,rYY,rZZ šest, dohromady 32. Fig. 13 uvádí shodně 256 obecných,32 speciálních registrů po64 bitech a2^64 bytů paměti; grafické vynechání prostředních řádků je výslovné.

V0017: rozdělení 20010203 na čtyři bajty dává OP=20,X=01,Y=02,Z=03. Při definici opcodu20=ADD jde o ADD $1,$2,$3. Osmibitový OP má 2^8=256 hodnot; operandové formáty X/Y/Z, X/YZ a XYZ odpovídají rozdělení tří zbývajících bytů. Zde jsou pravidla instrukcí definována, nikoli odvozována z implementace.

## P. 6 — V0018–V0021

V0018: posun o 1000000 bytů odpovídá 1000000/4=250000 tetrabytům. 0x03d090 = 3·65536+13·4096+9·16 =196608+53248+144=250000. S definovaným OP=f0 vznikne f003d090. Meze 24bitového pole jsou splněny.

V0019: pro přiřazení signed n-bit výsledku N je jediný reprezentovatelný vzor zbytek N mod2^n. Bez overflow právě N leží v −2^(n−1)..2^(n−1)−1 (V0012); ostré podmínky N<−2^(n−1) nebo N≥2^(n−1) jsou přesně doplněk tohoto intervalu. Pro ADD s64bitovými operandy to dává uvedené meze −2^63 a2^63−1. Úloha5 bude řešena samostatně při průchodu úlohami.

V0020, (5): součet unsigned operandů může mít nejvýše65 bitů; odstranění přenosu vlevo je zbytek modulo2^64. V0015 zaručuje platnou adresu. Pro1000+2 je A=1002 a floor(1002/8)·8=1000, tedy M8[1002]=M8[1000].

V0021, čtyři příklady: pro A=1002 jsou zarovnané počátky byte1002,wyde1002,tetra1000,octa1000. Při bytové posloupnosti01,23,45,67,89,ab,cd,ef se načítají45,4567,01234567,0123456789abcdef. Všechny mají nejvyšší znaménkový bit0, takže délkové rozšíření je nulové. To dává přesně všechny čtyři výsledky na p.6.

## P. 7 — V0022–V0028

V0022, čtyři příklady: A=1005 má počátky1005,1004,1004,1000. Načtené vzory jsouab,89ab,89abcdef,0123456789abcdef. První tři mají horní bit1; jejich signed hodnoty se při prodloužení zachovají doplněním jedniček: ffffffffffffffab,ffffffffffff89ab,ffffffff89abcdef. Octa už délku64 má, zůstává0123456789abcdef.

V0023: jestliže krátký n-bit vzor x představuje záporné N=x−2^n, jeho64bitová reprezentace je N+2^64=x+(2^64−2^n), tedy stejné spodní n bity a jedničky nad nimi. Kladné hodnoty už mají x=N a dostanou nuly. Tím je obecně dokázána sign extension popsaná v textu.

V0024: unsigned rozšíření zachovává x∈[0,2^n), tudíž horní64−n bity jsou0. Pro ab je výsledek00000000000000ab. Pokud n=64, nezbývá žádný bit k doplnění; LDO i LDOU kopírují přesně tentýž vzor (bez možnosti konverzního overflow), tedy jejich chování na uvedeném paměťovém přenosu je shodné.

V0025: LDHT násobí32bitový vzor2^32, tj. připojí32 nulových bitů, což se vejde do64 bitů. Pro A=1005 je tetra89abcdef a výsledek89abcdef00000000.

V0026: LDA vrací (u($Y)+u($Z)) mod2^64, což je přímo definice ADDU z p.8. Jde o shodu daného výsledku a overflow konvence.

V0027: signed STB/STW/STT/STO jsou zkrácená přiřazení z V0019, takže spodní8/16/32/64 bity určí paměť a případné overflow závisí pouze na cílovém signed rozsahu. Při N=−65536 je64bitový vzor2^64−2^16 =ffffffffffff0000.

V0028, čtyři příklady: A=1002. STB změní jen byte1002 na00; N<−128 =>overflow a výsledné octa0123006789abcdef. STW zapíše0000 do1002–1003; N<−32768 =>overflow a0123000089abcdef. STT začíná1000, spodních32 bitů jeffff0000, N patří do signed32 rozsahu =>ffff000089abcdef bezoverflow. STO začíná1000 a uloží všech64 bitů =>ffffffffffff0000 bezoverflow. Každý příklad se vyhodnocuje proti původnímu (6), jak stojí v zadání.

## P. 8 — V0029–V0037

V0029: pro t=8,16,32,64 platí s(x)≡u(x) modulo2^t, protože jejich rozdíl je buď0, nebo2^64. Proto signed a unsigned store ukládají stejné nízké bity; unsigned definice nepředepisuje kontrolu signed intervalu, tedy nesignalizuje overflow. STO a STOU se shodují i bez zkrácení.

V0030: pro u<2^64 je floor(u/2^32) právě horních32 bitů, spodních32 se zahodí. STHT tím uloží přesně horní tetra; jeho hodnota je nejvýše2^32−1 a vejde se.

V0031: poleX je unsigned byte0..255, tedy STCO může vložit tuto konstantu do64bitového paměťového octa bez ztráty nebo overflow. Pojem instruction field se nesmí zaměnit s obsahem registru$X.

V0032: ADD/SUB/MUL jsou definované celočíselné operace následované mapou z V0019. Konzistence signed zápisu se znaménkem je tím dána; nejde o tvrzení, že součin dvou64bitových signed hodnot vždy vejde do64 bitů.

V0033: pro divisor z≠0 je q=floor(y/z), r=y−qz. Pro z>0 z nerovnosti q≤y/z<q+1 plyne0≤r<z; pro z<0 vyjde z<r≤0. Identita y=qz+r platí v obou případech, takže definice DIV odpovídá matematickému floor/mod. Quotient může přesáhnout signed64 jen při y=−2^63,z=−1; obecná kontrola z V0019 tento případ zachytí. Pro z=0 je fallback q=0,r=y definicí; i tehdy zachovává identitu y=qz+r, nikoli dělení nenulovým z.

V0034: ADDU a SUBU produkují zbytek v0..2^64−1, proto má výsledek vždy64bitovou reprezentaci. Ignorování přenosu/zápůjčky je součást unsigned definice, ne aritmetický přetečený signed výsledek.

V0035: s B=2^64 jsou oba unsigned činitele menší než B, takže jejich součin je ≤(B−1)^2<B². Dvojice rH,$X má128 bitů a unese celý výsledek; horní polovina je floor(product/B), dolní product modB.

V0036: pro DIVU je N=DB+Y,0≤D,Y<B. Jestliže z>D, pak N<(D+1)B≤zB, tedy floor(N/z)<B a quotient i remainder mají platné64bitové unsigned reprezentace. Jestliže z≤D a z>0, N≥zB, quotient by byl≥B; fallback je proto odlišná záměrná definice, nikoli tvrzení o vejití quotientu. Při z=0 se rovněž použije fallback. Tento argument uzavírá implicitní důvod podmínky z>D.

V0037: konkrétní součin (7), high=B−a a vztah ke zlatému řezu se **přebírají** z notes/MMIX-C0001.md a results/golden-ratio-exact.json. Produkt a numerická konstanta jsou správné. Text „první64 bity“ je již potvrzená nízkozávažná chyba: prefix končí7c15, zatímco7c16 je správné zaokrouhlení. Zde nebyl výpočet opakován.

## Stav a mezery

V0001–V0037 mají výše konkrétní argument nebo přesný odkaz na již uzavřený důkaz. Úlohy tohoto oddílu začínají později a nejsou tímto blokem prohlášeny za vyřešené. Definiční architektonická pravidla nejsou otestována simulátorem; externí bibliografie/historické komentáře a široké nekvantifikované kulturní výroky mají zvláštní otevřenou výjimku. Další matematický kurzor je p.9/file17.
