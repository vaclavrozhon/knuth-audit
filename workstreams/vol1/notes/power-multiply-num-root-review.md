# §1.3.1-22: dvě násobení a NUM v šesti slovech

Kořenová revize 2. listopadu 2026, V1-X0709. Přijata je úplná
neexistence programu v přesně vymezené rodině
`LOAD vstupu; integer MUL; T; integer MUL; NUM; HLT`, kde T je jeden
z šesti celočíselných posunů nebo integer DIV. Povoleny jsou platné
výběry polí a konstanty čtené z vlastních instrukcí. Nepovolujeme
další připravená slova. Nejde o dolní mez pro všechna pořadí instrukcí,
cykly, samomodifikaci ani floating operace. Celá úloha zůstává partial.

Root přečetl celý zmrazený důkaz
`parallel/mix-optimality/notes/power-multiply-num-obstruction.md`
a ověřil jeho hash a délku. Argument je algebraický; nevyžaduje
omezení velikosti hledaných konstant ani nový konečný test.

## Rozhodující rozpor

Stačí radix b = 100, tedy základ jednoho bajtu 100; celé slovo má
B = b^5 = 10^10 možných velikostí. Nepředepsané indexové registry
volíme nulové, takže adresy operandů jsou pevné. NUM vezme z každého
z deseti bajtů A/X jeho zbytek modulo 10 a složí desetinné číslo.
Tuto funkci desetibajtové velikosti P označme phi(P).

Výsledek pro vstup 5 je 5^13 = 1220703125 > 10^9. Poslední
násobitel K2 proto musí mít všech pět bajtů, tedy K2 >= 100^4.
Nemůže být malým vstupním slovem ani kratším polem. Pro vstup 1
musí phi(P1) = 1. Poslední bajt K2 je tedy nesoudělný s 10.
Mezi operačními bajty šesti dovolených instrukcí tuto podmínku
splňuje pouze MUL s kódem 3. Odtud K2 = 3 modulo 10 a velikost
A1 před posledním násobením je 7 modulo 10.

První násobení vstupním slovem nedá takové A1 po jediném posunu
ani dělení; dělení vstupním slovem navíc selže na nule. Zbývá pevný
první násobitel K a pevné kladné d s

```text
A_n = floor(n*K/d) modulo B.
K = q*d + t,  0 <= t < d.
A_1 = q,  A_2 = 2*q + e modulo B,  e in {0,1}.
```

Pro posun je d mocninou 100 odpovídající poloze posledního bajtu
okna; pro DIV jde o velikost dělitele. Požadovaná jednotková číslice
výsledku pro 2 nutí e = 0. Posledních pět bajtů produktu proto
splňuje P2 = 2*P1 modulo B. Jelikož phi(P1) = 1, poslední dva
bajty P1 jsou 10*a+1 a 10*c pro celá a,c. Po zdvojení mohou poslední
dvě desetinné číslice NUM být pouze 02 nebo 12. Požadované
2^13 = 8192 končí 92: spor.

## Dvě výslovná doplnění modelu

První LDA/LDAN musí zahrnout poslední bajt vstupu. Jinak má při
malých kladných vstupech vždy nulovou velikost a následný výpočet
je nerozliší. S tímto bajtem má načtená velikost právě n; případné
znaménko nemění argument o velikostech.

Při přetečení DIV kniha neurčuje obsah A/X. Takový případ nemůže
zaručit správnost pro kladný vstup: přípustná nulová hodnota A po
dělení vede přes poslední MUL a NUM k nule. Proto lze u správného
programu v této rodině použít obvyklý podíl bez přetečení. U kruhového
posunu musí poslední bajt A pro vstup 1 pocházet z původních pěti
bajtů X; jinak je nulový. Zvolené pětibajtové okno pak neprochází
kruhovým přechodem, takže také má uvedený podílový tvar.

Sémantika MUL/DIV, posunů a NUM na původních s. 131, 135 a 138,
včetně dříve zachycené opravy DIV z roku 1997, je převzata z již
přijatého čtení. Nový argument nehlásí chybu knihy.

## Souhrnné předání MIX

Závěrečný agentův REPORT, UNIT_STATUS a SOURCE_STATUS jsou nyní
zmrazeny spolu s celým adresářem `parallel/mix-optimality/`.
Root přečetl všechny tři souhrny a ověřil 48 souborů, 1149367 bajtů
v novém MANIFEST.json. Staré úspěšné matematické běhy neopakoval.
Čtyři obecné mezery zůstávají: prostor 16(a), čas 17(b), neomezený
prostor 22 a neomezený prostor 23. Případné starší „review pending“
u této jediné rodiny v neměnném UNIT_STATUS nahrazuje X0709;
neznamená uzavření globálního minima. Nový souhrn nemění dříve
přijaté jednotlivé výsledky ani jejich archivní manifesty.
