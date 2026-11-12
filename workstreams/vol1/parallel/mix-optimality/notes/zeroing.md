# §1.3.1-16(a),17(a,b): kratší mezera a rychlejší horní mez

Zde b označuje počet hodnot bajtu, 64 <= b <= 100, a u jednotku
instrukčního času MIXu. N je číselná hodnota počátečního rI2.
Nulování zapisuje kladnou nulu. Není předepsáno HLT: konec úseku
je předání řízení na určenou následující adresu. Ostatní počáteční
registry a paměť jsou libovolné, kromě zavedeného kódu. Vnější zařízení
neposkytují předem připravené nuly ani další program zdarma.

Přímo znovu přečteny originály 142 a 508; stránka souboru je o15 vyšší.
Zadání16 žádá nejkratší a nejrychlejší program. Zadání17 výslovně
stanoví 0 <= N <= 2999 a počátek v3000. Odpověď17 popisuje dlouhou
variantu pouze jako „slightly faster“, nikoli jako doložené minimum.

## Nová rychlejší varianta17(b)

```
3000 DEC2 994
3001 J2NN 3004
3002 ENN1 0,2
3003 JMP 3003,1
3004 STZ 1,2
3005 STZ 2,2
     ...
3997 STZ 994,2
3998 J2NN 3000
3999 [pokračování]
```

Je zde999 instrukcí, všechny v3000,...,3998. Nepotřebuje konstantu,
pomocnou paměť ani předpoklad o libovolném počátečním registru.
Všechny adresy, včetně indexovaných, jsou platné pro každý radix.

Položme q=floor(N/994), r=N−994q, tedy0 <= r < 994.
Prvních q průchodů začíná po DEC2 nezáporným rI2=N−994k,
k=1,...,q. Blok994 zápisů vynuluje interval

```
[N−994k+1, N−994(k−1)].
```

J2NN na3998 se vrací do3000. Další DEC2 nastaví rI2=r−994<0;
J2NN na3001 tentokrát nepřeskočí. ENN1 nastaví rI1=994−r a
indexovaný skok vstoupí na instrukci STZ j,2 s j=994−r.
Posledních r+1 instrukcí proto zapíše přesně adresy0,...,r.
J2NN na3998 již neskáče a předá řízení na3999.

Úplný průchod stojí2*994+3 jednotek; závěrečný průchod
2(r+1)+5. Přesný čas je tedy

```
T(N) = 2N + 3 floor(N/994) + 7.
```

Knižní dlouhá varianta má doložený čas

```
T_book(N) = 2N + 3 floor(N/993) + 8.
```

Protože floor(N/994) <= floor(N/993), nový program je pro každý
povolený N alespoň o1u rychlejší. Například N=0 dává7u proti8u,
N=993 dává1993u proti1997u a N=2999 dává6014u proti6015u.
První DEC2 převádí +0 i −0 na −994, takže důkaz zahrnuje obě
počáteční znaménka nuly. Žádná jiná než výstupní paměť se nemění.

Samostatná nová kontrola je v check_zeroing.py a results/zeroing.json.
Neopakuje4323 již úspěšných kontrol původního checkeru. Test nenahrazuje
výše uvedený důkaz a není důkazem globální optimality.

## Co se tím neuzavírá

- Pro16(a) zůstává platná horní mez čtyř slov. Zatím není doloženo,
  že tři slova nemohou využít samomodifikaci nebo nově vytvořený kód.
- Pro17(a) zůstává horní mez tří slov a čas4(N+1)u. Chybí úplné
  vyloučení dvouslovných samomodifikujících programů.
- Pro17(b) nová horní mez neřeší minimum. Je nutno výslovně rozlišit
  bodovou optimalitu pro každé N a minimum nejhoršího času. Rychlejší
  speciální větev pro malé N může zhoršit velká N. V tomto zápisu se
  ani jedna z těchto optimalit nepředstírá.

Pouhý seznam druhů původních instrukcí není důkazem dolní meze:
zápis může změnit druh pozdější instrukce. Ani požadavek libovolných
počátečních registrů automaticky neznamená zvláštní inicializační
instrukci; například DEC1 0,1 vynuluje číselnou hodnotu rI1 jediným
odečtením registru od sebe. K záporné nule je přitom nutno stále
přihlížet. Tyto možnosti musí případná úplná redukce pokrýt.

## Errata

Všechny čtyři vrstvy byly přímo přečteny v předchozím zmrazeném
bloku errata-additions, celkem101 stran. Cílená mapa je také v
../../../sources/mix-description-errata-extract.json. U stran142
a508 jsou opravy13,14,18,21; žádná nemění zadání ani odpovědi16/17.
Bylo ověřeno také věcné hledání STZ, MOVE, 993, 994 a čísla úloh,
nikoli pouze čísla stránek. Nové rychlejší řešení je zde označeno
jako lepší horní mez; není tím automaticky založen nález proti
nevyřčenému tvrzení, že uvedená odpověď je globálně optimální.
