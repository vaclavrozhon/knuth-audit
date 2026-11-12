# SAT 442–444: odvozování, UC/PC a SLUR

Kontrola 31. 10. 2026. Nové nálezy F053 a F054, slovní kandidát C010.
Výpočty přesně rozlišují vytištěnou definici od zamýšleného algoritmu.

## F053: chybný odkaz v odpovědi 443(e), str. 637

Odpověď „False“ je správná, ale odkaz na příklady v (c) ji nedokazuje.
Všechny příklady v (c) patří do UC0, a tedy také do UC_(n−1) pro n≥1.
Stačí místo odkazu uvést F={(x),(¬x)}: n=1, F je nesplnitelná,
ale neobsahuje prázdnou klauzuli, takže není v UC0.

Obecně úplná soustava všech 2^n klauzulí délky n je nesplnitelná
a má tvrdost právě n. Každé omezení na jednu proměnnou dá úplnou
soustavu na n−1 proměnných. Pro k<n nelze začít žádný krok odvozování,
zatímco na úrovni n lze odvodit obě polarity libovolné proměnné.
Program ověřil n=1,…,5. PDF str. 637 i autorův PS str. 273 mají
stejný nesprávný odkaz. V načtených all4b a all4f6 oprava nenalezena.

## F054: definice neumožňuje vše, co vrací postup 442(f)

V zadání na str. 359 musí odvozovací posloupnost končit cílovým
literálem a její proměnné musejí být navzájem různé. To může zabránit
odvození negace literálu, který je nutným prvním krokem, i když už
byl odvozen spor. Odpověď na str. 637 naopak po sporu prohlašuje
všechny literály za členy L_k. Rozdíl zasahuje i popis v 442(b).

Jednoduchý příklad pro k=1 je

    F = (a) ∧ (¬a∨b) ∧ (¬a∨¬b).

Posloupnosti (a,b) a (a,¬b) odvodí b a ¬b. Pro cíl ¬a ale nelze
použít a; žádný jiný literál nemůže být prvním krokem, protože
žádné jeho opačné dosazení nevytvoří přímo prázdnou klauzuli.
Tedy L1={a,b,¬b}, nikoli všechny čtyři literály.

Protože odstavec o P_k výslovně začíná k≥2, pro vlastní hlášení
používáme silnější příklad na čtyřech proměnných:

    F = (a∨b) ∧ (a∨¬b)
        ∧ (¬a∨c∨d) ∧ (¬a∨c∨¬d)
        ∧ (¬a∨¬c∨d) ∧ (¬a∨¬c∨¬d).

Jediný možný první literál odvození druhého řádu je a:

- F|¬a obsahuje protikladné jednotky b a ¬b.
- F|a je úplná nesplnitelná soustava čtyř binárních klauzulí
  na c,d; jednotková propagace ještě spor nenajde.
- Po dosazení kterékoli polarity b propagace vynutí a a zbude
  tatáž binární soustava, opět bez jednotek.
- Po dosazení kterékoli polarity c nebo d má formule pouze
  binární klauzule a žádnou jednotku.

Posloupnosti (a,c) a (a,¬c) jsou platná odvození druhého řádu,
protože po a a opačném dosazení c vzniknou jednotky d,¬d.
Proto F⊢₂ε a P₂(F)={ε}. Literál ¬a však nelze odvodit:
posloupnost by musela začínat a a končit ¬a, což není strictly
distinct. Přesné L2 obsahuje zbývajících sedm literálů.

Možná oprava definice: vedle zakončení l_p=l povolit zakončení
platné odvozovací posloupnosti nižším sporem
`F|{l1,…,lp} ⊢_k ε`, nezávisle na cílovém l. Povolit i prázdnou
posloupnost. Tím se výslovně zahrne obvyklá konvence, že po sporu
lze vrátit všechny literály. Samotné zjišťování sporu a procedura
P_k zůstávají správné; nejde o chybný výsledek SAT/UNSAT.

Rozdíl není jen v seznamu: u čtyřproměnného příkladu je index PC
podle vytištěné definice 3, podle algoritmické konvence 2.
Vytištěnou definici potvrzuje PDF str. 359 a autorův PS str. 175;
algoritmický výrok PDF str. 637 a PS str. 273. Ve veřejných
erratech all4b a all4f6 odpovídající oprava nenalezena.

## Rozsah nezávislých výpočtů

`check_hardness.py` ověřuje postup P_k přímo přes zjednodušování
formulí, s úplnými pravdivostními tabulkami jako sémantickým
oraclem. Testováno všech 512 soustav na dvou proměnných včetně
prázdné klauzule a všech 17 902 soustav na třech proměnných
s nejvýše čtyřmi neprázdnými klauzulemi:

- 18 414 formulí, 479 208 částečných ohodnocení;
- 72 639 dvojic formule/úroveň pro všechny možné volby SLUR;
- 429 852 kontrol omezení z 442(c);
- 16 547 přejmenovatelných Hornových soustav;
- všech sedm vytištěných příkladů ostré hierarchie v 443(a);
- R′ z (7): UC index 2, PC index 3, L0=L1=L2=∅,
  L_k={¬1,2,4} pro k≥3;
- příklad 444(b) není přejmenovatelný na Hornův a každá volba
  SLUR přesto skončí SAT.

Hierarchie a počty PC v tomto prvním programu používají
algoritmickou konvenci po sporu. Nelze je bez výhrady vydávat
za kontrolu doslovné definice; odchylky jsou výslovně uloženy.

`check_hardness_definition.py` nezávisle vypočítá odvoditelné
literály výčtem všech povolených posloupností. Na 17 902
tříproměnných formulích porovná 71 608 úrovní: 456 odchylek
je na úrovni 1. U všech souhlasí detekce sporu. Samostatný
šestiklauzulový příklad výše dokládá odchylku i na úrovni 2.
Opravená definice souhlasila ve všech těchto případech s P_k.
Výsledky a celé protipříklady jsou v `results/hardness*.json`.

## Obecné argumenty pro zamýšlenou hierarchii

Omezení zachovává spor zjištěný r_k. Indukcí podle k lze proto
zaměňovat pořadí vynucených dosazení: když jsou oba opačné
literály odmítnuty na nižší úrovni, je spor; jinak vynucení
jednoho nezneplatní vynucení druhého. To zdůvodňuje pevný bod.
Jednotková propagace stojí O(nm). Každá vyšší úroveň zkouší
nejvýše 2n dosazení mezi nejvýše n vynuceními, takže dostáváme
O(n^(2k−1)m), jak uvádí kniha.

PC_k⊆UC_k plyne aplikací na obě polarity při nesplnitelném
omezení. UC_k⊆PC_(k+1) plyne z odmítnutí opačného literálu.
PC0 tvoří právě prázdná soustava a soustavy obsahující ε.
UC0 právě soustavy obsahující všechny své prvoimplikáty:
nesplnitelné omezení je negací implikátu, který obsahuje
prvoimplikát; ten po omezení vytvoří ε. Opačný směr vezme
omezení negující libovolný prvoimplikát.

Pro striktnost lze pokračovat v příkladech knihy. Soustava
všech klauzulí na k proměnných s přidaným společným literálem
z má UC index k a PC index k+1: po ¬z zbude úplná soustava,
ale před dosazením mají všechny klauzule délku k+1 a žádný
krok úrovně k nezačne. Soustava úplných klauzulí na k
proměnných, v níž jen k poslední klauzuli přidáme z, má oba
indexy k. Omezení buď vytvoří menší úplnou soustavu, nebo
menší soustavu téhož typu. To zároveň dává induktivní důkaz
horní meze; dosazení ¬z dává dolní mez. PC_n obsahuje každou
soustavu na n proměnných indukcí přes odmítnutí opačného
literálu. UC_(n−1) nikoli, viz F053.

## SLUR a C010: obě polarity jsou podstatné

U standardní definice vybírá E2 kteroukoli polaritu kterékoli
zbývající proměnné. Citovaný článek Gwynne–Kullmann to výslovně
zajišťuje definicí lit(F)=var(F)∪¬var(F) na str. 9 a definicí 3.1.
Lokální archiv: `sources/gwynne-kullmann-slur-2013.pdf`;
[primární zdroj](https://arxiv.org/abs/1204.6529).

Je-li F v UC_k, každé omezení, které r_k neodmítne, je
splnitelné a stále v UC_k. Algoritmus proto nemůže vrátit MAYBE.
Není-li F v UC_k, existuje nesplnitelné omezení L, které r_k
neodmítne. Algoritmus může volit literály z L: opačné vynucení
by už odhalilo spor v F|L. Po těchto volbách dosáhne nesplnitelné
soustavy bez zjištěného sporu; další volby nakonec skončí MAYBE.
Tím je dokázána ekvivalence i obecná verze v odpovědi.

Slova „any literal within F“ lze ale číst jako pouze skutečně
se vyskytující literály. Pak tvrzení 444(c) selže pro

    (a∨b∨c) ∧ (a∨b∨¬c) ∧ (a∨¬b∨c) ∧ (a∨¬b∨¬c).

Formule je ekvivalentní a a není v UC1. Volba ¬a vede k MAYBE,
ale ¬a se v zápisu nevyskytuje. Při omezení voleb na výskyty
skončí každá cesta SAT. Vzhledem k jasné konvenci primárního
článku vedeme bod jen jako možné slovní zpřesnění C010,
nikoli jako potvrzenou matematickou chybu.

Lineární implementace 444(d) může prokládat obě propagace.
První dokončenou nekonfliktní větev přijme; skončí-li první
větev sporem, dokončí druhou. Práce zahozené větve nepřesáhne
konstantní násobek práce přijaté. S vratnými seznamy výskytů
se každá operace přijaté větve účtuje odstraněné buňce formule;
návrat druhé větve i sladění dat mají stejný řád. Každá buňka
je nakonec odstraněna nejvýše jednou. Tento amortizovaný
argument podporuje text; plná implementace těchto seznamů
v auditu vytvořena nebyla.
