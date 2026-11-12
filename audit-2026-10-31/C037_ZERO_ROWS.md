# C037: mají úlohy 175–176 výslovně ošetřit nulové řádky?

Stav: **candidate**, nízká závažnost. 4B 7.2.2.1–175–176, zadání
str. 146, odpovědi str. 467. Stejné znění v autorově draftu.
Nejde o novou potvrzenou chybu ani o námitku proti nenulovým příkladům.

Zadání mluví o obecné matici 0/1, respektive 0/1/2. Nezakazuje nulové
řádky. Definice MCC na str. 93 přitom výslovně vyžaduje, aby každá
možnost obsahovala alespoň jednu primární položku. Doslovné převedení
nulového řádku vytvoří prázdnou možnost, kterou takto nelze vybrat.

Pro 175 vezměme dva řádky A=(0,1)^T, horní meze r=(1,1) a sloupcový
součet jedna. Existují dva vektory x=(0,1),(1,1). Doslovný MCC vstup
má jen jednu použitelnou možnost a jedno řešení. S mezí r1=2 jsou
tři vektory; řetězcový gadget obsahuje sekundární možnost bez primární
položky a DLX3 vrátí jen dvě řešení.

Pro 176(a) vezměme řádky A=(2,0)^T a požadujme součet dva.
Podmnožiny {první řádek} a {první, druhý řádek} jsou různé.
Doslovný MCC převod zachová jen jednu z nich.

Oprava je snadná: vyjmout nulové řádky a na závěr doplnit všechny
jejich nezávislé volby (v 176 faktor 2^z, v 175 součin (r_i+1)),
nebo každému přidat novou primární značku Z s intervalem [0,1],
respektive [0,r_i]. Následný převod pak funguje beze změny.
Šest uložených minivstupů dává dvojice počtů 1/2, 2/3 a 1/2.

Proč pouze kandidát: parentetické „generalizes the MCC problem“ v 175
může přenášet předpoklad neprázdných možností a oddělení nulových řádků
lze chápat jako samozřejmé předzpracování. Potřebujeme rozhodnout, zda
má smysl požadovat explicitní větu; nedokazujeme chybný obecný princip.
Úlohy 177–178 používají výslovně nenulové blokové vektory, takže
jejich správnost tato otázka neovlivňuje.

Podklady: [úplné poznámky](MCC175_179_SOURCE_NOTES.md),
`results/mcc175_179/source-checked.json`, šest `.mcc/.log/.out` souborů,
zobrazená definice MCC (`images/mcc175-179-original-113.png` a draft35),
zadání `images/vol4b-p146.png`, odpověď `images/chess173-174-original-487.png`.
V šesti vrstvách errat není nalezena odpovídající poznámka. Původní
X175 zůstává platnou kontrolou své výslovně nenulové domény.
