# V2-C0021: zaokrouhlení překročí sentinel v kolizním algoritmu

**Confirmed**, 1.11.2026, s níže vymezeným numerickým rozsahem.
§3.3.2 I, algoritmus S, str.71 (DjVu str.83), třetí vydání,
první dotisk1997. Původní sazba `images/vol2-p071.png` vizuálně
zkontrolována. Algoritmus výslovně pracuje s plovoucí čárkou.

## Přesný příklad

Nechť n=2 a m=10. Použijme IEEE754 binary64, zaokrouhlování
k nejbližšímu číslu, při shodě k sudé mantise, po každé operaci.
Po jediném průchodu S2 jsou nenulové položky pole

```text
A[1] = round(1/10) = 3602879701896397 / 36028797018963968,
A[2] = round(round(1 + round(1/10)) − round(2/10))
     = 4053239664633447 / 4503599627370496.
round(A[1]+A[2]) = 1 + 2^(-52).
```

S3 nejprve zpracuje A[1]; index t se zastaví na prahu T_4=.50.
Po přičtení A[2] vytiskne počet kolizí −1 a zápornou
pravděpodobnost −2^(-52). Vnitřní smyčka má opakovaně zvětšovat t,
dokud p<=T_t. Ani poslední práh T_8=1 tuto podmínku nesplní,
a běžný doslovný překlad vnitřní smyčky čte neexistující T_9.

Nejde jen o model, kde je m blízké n: tentýž výsledek nastane
pro m=10018,n=2, tedy m/n=5009. Racionální hodnoty všech
zaokrouhlení jsou v `results/collision-test.json`, blok
`sparse_sentinel`. V obou případech žádnou nenulovou položku
neodstraní mez10^(-20).

## Rozsah a oprava

V přesné aritmetice tento protipříklad neexistuje. Vnější formulace
„until t=tmax“ může být zamýšlena jako okamžité ukončení i uvnitř
vnitřní smyčky. Při této interpretaci se přístup k T_9 neprovede;
záporný výstup ale vznikne ještě před ním. Nález tedy není tvrzení,
že všechny rozumné implementace nutně havarují. Je to chybějící
numerická ochrana výslovně uvedeného algoritmu s plovoucí čárkou.

Stačí ve vnitřní smyčce výslovně skončit při t=tmax a pro výstup
omezit vypočtenou distribuční funkci na interval[0,1]. Tím se
opraví tento problém; úplnou mez zaokrouhlovací chyby všech
pravděpodobností tato změna sama neposkytuje.

## Ověření a errata

`verify_collision_test.py` obsahuje doslovný model S a oddělený
racionální model zaokrouhlení. Ten určuje binární exponent,
kvantizační krok2^(e−52) a přesně rozhoduje o zaokrouhlení;
nejde o dvě opakování téhož výpočtu s float.

Vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX
prohledány1.11.2026 podle str.70–71, názvu testu, algoritmu a
podmínek ukončení. Odpovídající oprava nenalezena. Náhled vydavatele
končí před touto stranou; nejnovější fyzický tisk ani prvenství
nejsou ověřeny. ASCII draft neodeslán.
