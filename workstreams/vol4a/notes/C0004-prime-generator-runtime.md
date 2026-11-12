# V4A-C0004 — opakované hledání bitu v kroku P2

6. listopadu 2026. **Candidate, medium.** Odpověď §7.1.1–30,
p539/file556, krok P2 a následující časová věta. Správnost výstupů
není zpochybněna. Důkaz celé okolní konstrukce a opravy je v
proof-040-prime-cube-generator.md, P0654–P0661.

Po známé opravě z13.10.2013 má být čas nejvýše O(mn+nC), kde C
je počet všech podkrychlí vstupní množiny. Pro n≥2 vezmi
V={0,2^(n−1)}. Máme m=2,C=3: dva body a jedinou hranu.

P1 ponechá dva nenulově tagované body. Všechny postupně vytvořené
seznamy s maskou A=2^h jsou prázdné: pro h<n−1 nemají buddy pár,
pro h=n−1 vznikne maximální hrana, která se ihned vypíše a neuloží.
P2 proto při každém takovém A nastaví j=0 a h krát jej zvýší,
než najde první jedničku. Celkový počet těchto zvýšení je přesně
n(n−1)/2, tedy Ω(n²), zatímco mn+nC=5n. Jde o obecnou analytickou
stopu pro libovolně velké n, bez programu a bez okrajového prázdného
nebo nulárního vstupu.

Otevřený je pouze modelový výklad: časový rozpor platí pro doslovnou
smyčku postupných zvýšení j. Pokud by celá fráze „increase j … until“
označovala skrytou konstantní bit-scan operaci, nelze její cenu měřit
počtem rozvinutých zvýšení. Taková operace není v uvedeném P2 popsána.
Proto tento záznam zatím není confirmed.

Přímá oprava nevyžaduje ani zvláštní instrukci: při prázdném seznamu
a A≠0 stačí zachovat j z předchozího P3, protože je nejnižším bitem A.
Pro prázdný seznam a A=0 algoritmus skončí; při neprázdném seznamu
se j nastaví na0 jako dosud. P0661 dokazuje zachování všech kroků
i horní mez O(mn+nC) po této změně.

Sazba zadání p82/file99 a odpovědí p538–539/file555–556 zkontrolována.
Známá časová oprava z all4a-pre.pdf p21 pouze přidává faktor n,
nemění P2. Relevantní vrstvy all4a-pre/all4a/err4a/all4f0/err4f0
neobsahují další opravu; doplňkové all4f1/err4f1 také ne.
Fyzický první dotisk nebyl porovnán a není tvrzena priorita nálezu.
UI lokace patří pouze p539/file556, ne zadání nebo hlavnímu textu54.
