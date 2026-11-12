# V2-C0029: chybějící N ve třetím momentu

**Confirmed**, 1.11.2026. §3.3.2-35(d), odpověď str.572,
řádek začínající „Thus E S_m^3“. Původní obraz572 vizuálně
potvrzuje `m³−6B(N+1)/N`; první člen má být m³/N.
Zadání na80 má tento jmenovatel správně.

Y_n je binární lineární rekurence s periodou N=2^k−1,
Z_n=2Y_n−1 a S_m součet m po sobě jdoucích znamének.
Průměrujeme přes všech N počátečních fází. B počítá trojice
různých pozic v okně, jejichž odpovídající lineární funkce
mají nulový součet nad tělesem dvou prvků. Rozvinutí součinu
dává přesně

```text
E S_m³ = [m³−6B(N+1)]/N.
```

Nejkratší netriviální příklad: k=2, rekurence
Y_n=Y_(n−1) XOR Y_(n−2), počáteční bity1,0. Perioda je1,0,1,
tedy N=3. Pro m=1 je B=0 a E S_1³=E Z_n=1/3;
tištěný výraz by dal1. Doklad nepotřebuje asymptotiku.

Obecný důkaz a nezávislé konečné modely jsou v `lfsr-walks.md`.
Všech6977 oken51 primitivních rekurencí stupňů2–8 potvrzuje
opravený vzorec. Pro55/24 a m79 dává B=24 a moment přibližně−144,
jak správně uvádí následující odstavec knihy.

Všechny čtyři vrstvy errat i aktuální TeX prohledány1.11.2026
podle572, answer35 a third moment. Oprava2024 mění jen slovní
popis m mnohem menšího než N, nikoli tento řádek. Oprava
jmenovatele nenalezena; fyzický dotisk/prvenství neověřeny.
Draft neodeslán.
