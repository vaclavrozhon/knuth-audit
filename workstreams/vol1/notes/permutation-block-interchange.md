# §1.3.3-36: dvě úplné rutiny MIX a přesné časy

Zadání185 bylo přečteno z originálu. Kniha nedává hotový kód odpovědi36;
proto jde o dvě naše řešení, ne o přepis programu vydávaný za tištěný.
Obecný důkaz cyklického postupu34–35 je v `permutation-remaining-working.md`;
tato poznámka doplňuje úplnou strojovou realizaci a srovnání.

## Kontrakt a správnost

Vstupní registry I1,I2,I3 obsahují nezáporné délky l,m,n tří bloků
α,β,γ. Nechť M=l+m+n<=3000. Pole začíná na adrese DATA=1000 a má
skončit v pořadí γβα, při zachování pořadí i bitů všech slov v blocích.
Nulové délky jsou povolené. Volání je `JMP EXCHANGE`; registr J obsahuje
běžnou návratovou adresu. Volatilní jsou A,X,I1,I2,I3,J a porovnávací
indikátor; I4–I6 a přepínač přetečení zůstávají nezměněné. Mění se
pouze datové pole, vlastní pracovní slova a návratové instrukce rutin.

`mixal_block_interchange.py` obsahuje obě celé rutiny i krátký obal
pro předání parametrů a zastavení. Vlastní kód je pod adresou1000,
takže se při nejvyšší délce3000 nepřekrývá s polem.

Cyklická metoda používá virtuální délku N=l+2m+n a posun s=l+m.
Tyto veličiny jsou v plných slovech; N může být6000, což se do
nejmenšího dvoubajtového indexového registru nevejde. Právě proto
se virtuální následník vypočítává v A. Jen výsledný skutečný index
menší než M přejde do I3. Tak je celá fyzická paměťová mez přípustná
pro každý radix64–100, bez implicitního omezení N<=4095.

Euclidův algoritmus na dvojici(l+m,m+n) spočte d=gcd(l+m,m+n).
Každá třída modulo d má v poli právě jeden zástupce j<d. Vnější
smyčka začne těmito j; X uchovává původní DATA[j], I2 aktuální index.
Při výpočtu dalšího indexu se k němu přičte s a případně odečte N.
Pokud index patří vypuštěné kopii β (je≥M), provede se ještě jeden
stejný krok. Vypuštěná kopie vždy v jediném kroku přejde do původní
β, takže druhý výsledek už je fyzický. Indukce podél cyklu zaručuje,
že se do hotového prefixu ukládají správné dosud nepřepsané hodnoty.
Při návratu na START se poslední hodnota doplní z X. Každý datový
index se navštíví právě jednou. M=0 se vyřídí samostatným návratem.

Druhá metoda obrátí celé pole a pak jeho tři bloky nových délek n,m,l.
Identita `(αβγ)^R=γ^Rβ^Rα^R` dokazuje výsledek. Pomocná rutina REV
používá levou mez I1 a pravou exkluzivní mez I2, dokud mezi nimi
zbývají alespoň dvě slova. Vymění krajní slova, zmenší interval a
opakuje. Obě varianty přesouvají celá slova LDA/LDX/STA/STX, tedy
zachovávají také zápornou nulu.

## Přesné časy

Jednotka u je standardní jednotka MIX; oba následující časy zahrnují
vstupní uložení návratu i skutečný návrat z EXCHANGE. Nezahrnují tři
instrukce obalu pro délky, samotný volající JMP a konečný HLT, dohromady5u.

Pro cyklickou variantu označme g počet dělení Euclidova algoritmu
začínajícího U=l+m,V=m+n. Počítá se i první nulový podíl, pokud U<V.
Pro M>0 stojí inicializace33u, testy a dělení Euclida25g+3u,
nastavení j jeden u a návrat jeden u. Na každý z d cyklů připadá5u
otevření a6u uzavření. Následník se počítá Mkrát; základ stojí9M,
porovnání se START3M a pokračování uvnitř cyklu10(M−d).

Ještě je třeba spočítat dvě proměnné ceny bez odhadu. Z M skutečných
pozic se přesně m následníků dostane do vypuštěné kopie β, tedy
přibude5m. Dohromady se tak projde každá hrana posunu na N virtuálních
pozicích právě jednou. Posun o s na0..N−1 přeteče přes N přesně s-krát,
takže odečtení modulu přidají2s=2(l+m). Celkem

```
T_cycles/u = 38+25g+24l+29m+22n+d,       M>0;
T_cycles/u = 20,                        M=0.
```

Pro reverzní variantu označme
`P=floor(M/2)+floor(l/2)+floor(m/2)+floor(n/2)`, počet výměn ve všech
čtyřech reverzích. REV stojí14u za výměnu a6u za uložení návratu,
poslední test a návrat. Pevná část EXCHANGE s předáním čtyř intervalů
stojí41u, takže

```
T_reversals/u = 65+14P.
```

Příklad l=3,m=4,n=5 má g=4,d=1,P=11:437u proti219u. Cyklická rutina
čte a zapisuje každé datové slovo jednou, ale její výpočty následníků
a odkazy na pracovní parametry zde převažují. Tato konkrétní realizace
proto není tvrzením o výhodě cyklické metody ani o globálně nejrychlejším
MIX programu. Rovnice dovolují přímé srovnání pro libovolné délky.
Obě metody jsou lineární v M, navíc g dělení u cyklické varianty.

## Reprodukce

`check_block_interchange.py` prošel9312 kontrolami v1552 úplných MIX
bězích. Pokrývá všech729 trojic délek0–8 pro obě metody,37 radixů
na stejném netriviálním příkladu a pět3000slovných hranic v radixech64
a100, včetně N=6000. Kontroluje všechna výstupní slova se znaménky,
paměť mimo povolené oblasti, zachované registry a overflow i přesné
uzavřené časové vzorce. Výsledek je `results/block-interchange.json`.

Při přípravě checkeru byly opraveny dva naše překlepy (`else20` a
nesprávné jméno parametru konstrukce záporné nuly). Nešlo o chyby knihy
ani o selhání matematických vzorců. Hotová sada prošla a neopakuje se.
