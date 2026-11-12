# V2-C0152: rychlost síta a čas 256 iterací si odporují

Stav: **confirmed**. §4.5.4, str. 390, poslední odstavec, věta
začínající „By 1995“. Kontrola 3. listopadu 2026.

Kniha udává 6144 milionů prosetých čísel za sekundu a zároveň
256 iterací D2/D3 za přibližně 5.2 nanosekundy. Jedna iterace
testuje jednu hodnotu x. Nanosekunda je 10^(-9) sekundy, takže

```
256 / (6144 * 10^6) sekund = (125/3) nanosekund
                           = 41.666666... nanosekund.
```

Oprava: **5.2 -> 42**, případně změnit počet iterací **256 -> 32**
při zachování 5.2 ns. Jde o faktor 8, nikoli o zaokrouhlovací odchylku.

Primární popis v disertaci Richarda F. Lukese *A Very Fast Electronic
Number Sieve* (University of Manitoba, 1995) potvrzuje na str. 30 a 38
32 čipů SSU a na str. 41 frekvenci 24 MHz, osm testů za takt,
tedy 192 milionů testů za sekundu na čip. Celkem:

```
32 * 8 * 24 * 10^6 = 6144 * 10^6 testů za sekundu.
```

Fyzický takt všech 256 paralelních testů proto trvá 1/(24 MHz),
tedy 41.666... ns. Čas 5.20833... ns odpovídá efektivnímu průměru
jednoho testu na jednom čipu, nikoli 256 testům celé sestavy.
Tato interpretace vylučuje pouhé zaměnění počtu fyzických a logických kroků.

Stejné parametry 24 MHz, 8 výstupů a 32 čipů uvádějí Lukes,
Patterson a Williams v *Some Results on Pseudosquares*, Math. Comp.
65 (1996), str. 366. Jejich následující slovní údaj „in excess of
6.4 billion“ má vlastní numerickou nepřesnost; nález o něj neopíráme.
Vizuálně byly přečteny uvedené stránky disertace i článku.
Disertace je dostupná z
[univerzitního repozitáře](https://mspace.lib.umanitoba.ca/bitstream/1993/12210/1/Lukes_A_very.pdf).

Původní strana knihy 390 byla vizuálně ověřena. Prohledány všechny
čtyři vrstvy all2-prepre/all2-pre/all2/err2 i současný err2 TeX;
oprava se nenachází. Změna z 19. května 2005 na téže stránce řeší
jen symbol AND. Stejný rozpor obsahuje už historický dodatek k druhému
vydání, str. 58 err2-2e: změna ke str. 374 z 27. února 1996.
To je doklad původu textu, nikoli oprava rozporu.

Fyzický nejnovější dotisk a prvenství nejsou ověřeny. Draft neodeslán.
