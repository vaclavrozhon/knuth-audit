# V2-C0011: maska z bitů pi nemá požadovanou periodu

**Stav: confirmed, 1. listopadu 2026.** Doplněná odpověď §3.2.2-20
na str.555, erratum z 5.9.2013, doporučuje pro 64bitovou metodu (10)
masku A=(243F6A8885A308D3)_16. Její charakteristický polynom není
primitivní a pro povolený nenulový počáteční stav dává periodu 1.

Původní PS byl vykreslen a vizuálně zkontrolován:
[celá str.13 errat](../images/all2-pre-p13-direct.png),
[detail čísla ve vyšším rozlišení](../images/all2-pre-2013-pi-mask-detail.png).
Není to odhad z OCR. Text na [str.31](../images/vol2-p031.png)
výslovně vyžaduje primitivní polynom a dovoluje libovolný nenulový stav.
[Zadání na str.39](../images/vol2-p039.png) žádá vhodné masky pro tuto metodu.

## Nejkratší přímý doklad

Zápis 0x označuje šestnáctková celá čísla. XOR je součet jednotlivých
bitů modulo 2. Metoda (10) zdvojnásobí k-bitový stav X, zahodí horní
přetečený bit a právě při jeho přetečení použije XOR s maskou A.
Pro k=64 zvolme

```
A = 0x243F6A8885A308D3
X = 0xE3EAD987836107B1       (povolený nenulový 64bitový stav)

2X modulo 2^64 = 0xC7D5B30F06C20F62
0xC7D5B30F06C20F62 XOR A = 0xE3EAD987836107B1 = X.
```

Horní bit X je 1, takže větev s XOR se opravdu provede. Stav se nemění,
nejnižší bit je vždy 1 a perioda je 1, nikoli 2^64-1. Nezáleží na
žádném statistickém testu ani na dlouhém numerickém experimentu.

## Příčina a oprava jednoho bitu

Bit i masky A je koeficientem x^i v polynomu
f(x)=x^64+sum_i A_i x^i nad F_2, tělesem dvou prvků. Maska má 27
jedniček, tedy f(1)=1+27=0 modulo 2. Polynom má faktor x+1 a nemůže
být primitivní. Pevný stav výše je právě podíl f(x)/(x+1) zapsaný jako
bitové slovo: z rovnosti (x+1)X=f plyne xX=X modulo f.

Jedna možná oprava je změnit D3 na C3:

```
A' = 0x243F6A8885A308C3 = A XOR 0x10.
```

Tato maska má 26 jedniček a je primitivní. Už netvrdíme, že jde o
přesných prvních 64 binárních míst pi. Pro vhodnou vyváženou masku
je to konkrétní oprava jediného bitu, nikoli jediná možná oprava.

Přesný doklad: pro M=2^64-1 ověřeno x^M=1 modulo f' a
x^(M/q)!=1 pro q=3,5,17,257,641,65537,6700417. Tato prvočísla
mají rekurzivní Lucasovy certifikáty a jejich součin je M.
Řád x je tudíž M, což v kvocientním okruhu s 2^64 prvky vynucuje
těleso i primitivitu. Všechny zbytky se nezávisle shodují ve dvou
modelech: bitové umocňování a explicitní konvoluce koeficientů s dělením.

## Reprodukce a rozsah

[Program](../verify_binary_polynomials.py),
[výsledky](../results/binary-polynomials.json),
[prvočíselné certifikáty](../results/binary-period-factors.json).
První běh skutečně selhal na předpokladu, že publikovaná maska je
primitivní: [původní log](../results/binary-polynomials-initial.log).
Po kontrole sazby pokračování ověřilo místo tohoto předpokladu
protipříklad a opravenou masku. Již úspěšně zkontrolovanou tabulku
12 trojčlenů a 63 vlastních masek znovu nepočítalo.

Prohledány all2-prepre, all2-pre, all2, err2 a err2.textxt stažené
1.11.2026 podle str.31,39,555, úlohy20 a hexadecimální konstanty.
All2-pre uvádí uvedené doplnění 2013; pozdější oprava nenalezena.
Náhled digitálního vydání z července 2026 neobsahuje str.555,
takže u tohoto nálezu netvrdíme ověření v tomto vydání. Novější fyzický
dotisk a prvenství neověřeny. [ASCII draft](../reports/C0011-pi-feedback-mask-draft.txt)
nebyl odeslán.
