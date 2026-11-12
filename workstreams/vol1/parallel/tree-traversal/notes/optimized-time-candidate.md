# Kandidát: čas optimalizace v odpovědi §2.3.1-20

Kořenový stav při předání: **V1-C0048, confirmed**. Globální ID přidělil koordinátor; lokální dočasné označení a níže zachovaná historie revize slouží návaznosti evidence.
Dočasné označení `optimized-stack-time`; kořenově potvrzeno jako V1-C0048. Originály 325–326 a 567 přečteny. Nejde o chybu vypočteného pořadí uzlů.

Odpověď 20 vkládá před zásobníkový krok T3 dvě instrukce `LD3 0,5(LLINK); J3Z T5`, mění řádky 10 a 11 a uvádí časy `(27a+6n-22)u` pro spojový zásobník a `(12a+6n-7)u` pro souvislý zásobník. Stejně jako hlavní rozbor značí n počet uzlů a a počet nulových pravých odkazů.

Pro jediný uzel je n=a=1 a obě formule dávají 11u. Skutečný průběh je však stejný pro obě verze:

```text
LD5 HEAD(LLINK)   2
J5Z DONE         1   (neskáče)
ENT6 0           1
LD3 0,5(LLINK)   2
J3Z T5           1   (skáče)
JMP VISIT        1
LD5 1,5(RLINK)   2
J5NZ T3          1   (neskáče)
J6NZ T4          1   (neskáče)
------------------
celkem          12
```

Do samotného VISIT a návratu není započítán čas; jeho volací JMP je součást původního rozboru. Skokem z J3Z se řádky 10 a 11 obejdou, takže žádná jejich „appropriate“ změna tento nejkratší rozpor neopraví. Vstup je první instrukce T1, konec je dosažení DONE; nepočítá se případný HLT v DONE. Zásobník se nepoužije, takže jeho reprezentace ani kapacita výsledek neovlivňuje.

## Obecný rozbor konkrétních úplných variant

V přiloženém `check_mix.py` jsou řádky 10 a 11 po úspěšném vložení do zásobníku nahrazeny `ENT5 0,3; J5NZ T3`. Druhý skok se vždy bere, protože test nenulového levého dítěte již proběhl. Z ekvivalence může být nahrazen JMP za stejnou cenu. Počet nenulových levých odkazů je a−1, nulových levých odkazů n−a+1. Tedy:

| Blok | Četnost | Cena souvislý | Cena spojový |
| --- | ---: | ---: | ---: |
| Inicializace | 1 | 4 | 4 |
| Nový test levého dítěte | n | 3 | 3 |
| Vložení do zásobníku | a−1 | 5 | 12 |
| ENT5 a skok k T3 | a−1 | 2 | 2 |
| Vyjmutí ze zásobníku | a−1 | 3 | 11 |
| Volání VISIT a pravý odkaz s testem | n | 4 | 4 |
| Test prázdného zásobníku | a | 1 | 1 |

Součty jsou `(7n+11a-6)u` a `(7n+26a-21)u`. Od tištěných hodnot se liší o `(n-a+1)u`, tedy o jeden časový krok za každý nulový levý odkaz. Tyto formule platí pro n>0; prázdný vstup skončí po LD5 a J5Z za 3u.

## Errata a ověření

Všechny čtyři vrstvy prohledány podle 325–326/567 i témat 27a, 12a, T3, running time, linked allocation a two more lines. Záznam `results/optimization-errata-search.txt`; žádná příslušná oprava nenalezena. Skutečné MIX varianty prošly všechny tvary s n≤7 při radixu 64 a všechny tvary s n≤4 při každém radixu 65–100, včetně zachování původních uzlů. Četnosti a obecný součet jsou důkazem pro všechny konečné neprázdné stromy; konečné běhy pouze kontrolují realizaci.
