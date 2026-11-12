# V2-C0088: výklad počtu úvodních nul při přenosu v dělení

**Candidate: vnitřní nesoulad při doslovném požadavku na výsledek.**
§4.2.2, str.239, pravidlo před(48) a rovnice(50). Strana239 znovu
vizuálně přečtena; relevantní oprava mezi čtyřmi vrstvami errat ani
v aktuálnímTeXu nenalezena2.11.2026.

Pravidlo říká, že odpověď má být škálována tak, aby měla právě
max(l_u,l_v) úvodních nul. Uvažujme b10,p2,q0,
u=(0,.99),v=(0,.01). Počty úvodních nul jsou0 a1; přesný podíl99.
K zachování jedné úvodní nuly je výsledek počítán na jednu významnou
cifru, tedy100, s reprezentací(4,.01). Rovnice(50) však dovoluje
pouze exponent

```text
0−0−0+1+max(0,1)+(0 or1) = 2 or3.
```

Rozdíl vzniká přenosem při zaokrouhlení: před zaokrouhlením vychází
(3,.099), které se zaokrouhlí na(3,.10). Tento zápis má nulový počet
úvodních nul; dodatečný posun na(4,.01) obnoví požadovaný počet,
ale zvýší přírůstek v(50) z1 na2.

Pokud měl být počet nul zajištěn pouze **před** zaokrouhlením,
pak(3,.10) a formule(50) jsou konzistentní, zatímco slovo„answer“
a„precisely“ potřebují výklad. Proto se zde dosud netvrdí jednoznačná
chyba samotné aritmetické hodnoty; oba výklady dávají100. Model
`unnormalized_model.py` oba způsoby výslovně odděluje a konečné
kontroly testují i možné důsledky pro následné operace.

Nulové výsledky mají navíc samostatnou neurčenost exponentu:
počet p úvodních nul sám neurčuje jejich měřítko. Model pro ně
výslovně volí nulovou větev(49), nikoli domnělý jednoznačný důsledek
pouhého pokynu„scale until“. Tato otázka je evidována jako omezení
interpretace, zatím ne jako další samostatná chyba.

Žádná zpráva nebyla odeslána. Fyzický tisk a prvenství neověřeny.
