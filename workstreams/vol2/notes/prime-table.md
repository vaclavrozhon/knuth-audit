# §4.5.4, tabulka 2 na straně 408: všech 460 prvočísel

Audit 3. listopadu 2026. Celá původní stránka 408 byla vizuálně
přečtena a všech 46 řádků přepsáno do
[programu](../verify_prime_table.py). Každý řádek má hranici N a
rostoucí kladné rozdíly `a_1,...,a_10`; tvrdí, že deset největších
prvočísel menších než N je právě `N-a_1,...,N-a_10`.

První sloupec už byl přesně ověřen v
[primitive-polynomials.md](primitive-polynomials.md), včetně vyloučení
všech celých čísel mezi `N-a_1` a N. Tyto úspěšné testy ani jejich
268 prvočíselných certifikátů se neopakovaly. Nový výpočet potvrzuje
zbývajících **414 položek**, s **1173 novými články Lucasových certifikátů**,
a dokazuje složenost všech **10202 zbývajících mezilehlých čísel**.
Celá tabulka je správná; žádná položka ani mezera nevyžaduje opravu.

## Důkaz a nezávislost kontroly

Lucasův certifikát čísla p obsahuje úplný rozklad p−1 na již prokázaná
prvočísla q a základ a splňující

```
a^(p-1) = 1 (mod p),
gcd(a^((p-1)/q)-1,p) = 1  pro každý prvočinitel q čísla p-1.
```

Pro každého prvočinitele d čísla p pak řád a modulo d obsahuje každou
prvočíselnou mocninu z p−1, takže `p-1 | d-1` a `d>=p`. Proto p je
prvočíslo. Rekurze končí v 2 nebo v dříve validovaném certifikátu.

SymPy pouze navrhuje faktorizace. Samostatný validátor zkontroluje
jejich úplný součin, již dokázané prvočinitele a všechny kongruence
explicitním binárním umocňováním, odlišným od použitého vestavěného
`pow`. Pravděpodobný prvočíselný verdikt se jako důkaz nepřijímá.

Každé neuvedené celé číslo mezi prvním a desátým prvočíslem dostane
buď vlastní dělitel, nebo svědka odmítnutí silným prvočíselným testem.
Dělitel se nezávisle zkontroluje po desetinných cifrách; silný svědek
samostatným explicitním umocňováním pro všechny potřebné exponenty.
Tím je vyloučeno i vynechané prvočíslo, nikoli pouze překlep v uvedené
položce. Certifikáty mohou používat dřívějších 268 prokázaných prvočísel;
jejich přesný zdrojový soubor je připojen otiskem SHA-256.

[Výsledek](../results/prime-table.json), [log](../results/prime-table.log):
čas **0.642645712 s**, wrapper PID 1316943, dítě 1316944,
session 27105, limit 180 s, exit 0. Program znovu nespouštíme.

Všechny čtyři vrstvy errat i současný TeX byly prohledány pro stranu,
název tabulky a jednotlivé oblasti čísel; oprava této tabulky nenalezena.
Závěr se týká sazby našeho prvního dotisku, ne fyzicky ověřeného
nejnovějšího exempláře.
