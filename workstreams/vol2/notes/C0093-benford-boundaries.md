# C0093: krajní body při počítání vedoucích číslic

**Confirmed**, 2.11.2026. TAOCP2,3.vydání,1.dotisk1997, §4.2.4,
str.257–259 a odpověď8 na str.620. Originály vizuálně přečteny.
Základní limitní Lemma Q a Theorem F jsou správné; chyba je v přesné
rovnosti(8) a souvisejících okrajových výrocích.

## Přesný protipříklad k(8)

Podle(6) se počítá *ostrá* nerovnost `10f<r`. Položme r=s=2,n=1.
Mezi celými1,...,20 mají vedoucí číslici1 právě1 a10,...,19: celkem11.
Proto P1(20)=11/20. První řádek(8), který je uveden pro s<=r, dává

```
(ceil(2)-1 + floor(20)+1-10)/20 = 12/20.
```

Zahrnuje totiž i20. Obecně je chyba přesně1/(10^n r), pokud 1<=r<10, s=r a
10^n r je celé. Pro 1<r<10 a 1<=s<10 je oprava: první větev používat
pro s<r; druhou pro r<=s<10, s horním počtem `ceil(10^n r)`.
Bod s=10 musí být vyhodnocen samostatně jako s=1 v následující dekádě.
Jinak druhá větev vynechá právě nové číslo10^(n+1): pro r=2,s=10,n=1
dává11/100 místo správných12/100. Krajní hodnoty r=1/10 mají přímé
konstantní indikátory. Obecný přesný vzorec platný i na hranicích je
uveden v [matematické poznámce](benford-math.md).
Asymptotické O(n)/10^n tento rozdíl pohlcuje, takže limitní formule
se nemění. [Přesný ověřovač](../verify_benford_math.py) porovnal opravený
počet nezávisle se100000 přímými prefixovými počty.

## Koncové hodnoty r a úloha8

Str.257 výslovně připouští 1<=r<=10. Pro r=1 je Pm(k)=0 a pro r=10
Pm(k)=1 pro všechna celá k,m. Výroky, že pro žádné pevné m neexistuje
limita Pm(k), proto potřebují omezení1<r<10. Nejde o chybu Theorem F.

Otázka8 se ptá na platnost(10) i pro m=0 s Q0=1,R0=−1.
Pro r=10 je P0(10^n s)=Q0+R0[s>r]=1, takže odpověď je kladná.
Pro r<10 zůstává záporná, a důkaz je bodový: pro1<r<10 vezměme s=10,
kde P0(10^(n+1))=1 a pravá strana0. Pro r=1 vezměme s=1.
Pro r=2,s=2 je navíc P0(2*10^n)=0 a pravá strana1 pro každé n.

Tištěná odpověď8 tedy potřebuje krajní výjimku r=10. Její závěrečný
argument o spojitosti stejnoměrné limity nelze používat bez spojitosti
aproximujících funkcí; takový předpoklad zde splněn není. Přímý důkaz
výše tuto formulaci opravuje bez konvence pro P0 v neceločíselných bodech.

V `all2-prepre`, `all2-pre`, `all2`, `err2` byly prohledány uvedené
strany a výrazy/rovnice; relevantní oprava nenalezena. Erratum str.620
z25.2.2010 se týká pouze odpovědi7. Neověřen poslední fyzický dotisk
ani priorita; [návrh hlášení](../reports/C0093-benford-boundaries-draft.txt)
nebyl odeslán.
