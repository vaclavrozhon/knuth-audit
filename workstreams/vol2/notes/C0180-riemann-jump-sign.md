# V2-C0180: opačné znaménko půlskoku

Stav **confirmed**, odpověď§4.5.4-25,str663, druhý řádek.
Po zahrnutí známé opravy n→x z10.12.2011 zůstává
„minus1/(2k) if x is the kth power of a prime“ nesprávné:
má být **plus1/(2k)**.

Kniha381 definuje pi(x) počtem p<=x a výslovně má pi(2)=1.
Proto levá strana úlohy J(x)=sum_(k>=1)pi(x^(1/k))/k
obsahuje celý skok1/k v bodě x=p^k. Rigorózní párovaná
explicitní formule dává střední hodnotu J_0, takže

```
J(x)=J_0(x)+1/(2k)  při x=p^k.
```

Při x=2 je J=1 a J_0=1/2. Tištěné odečtení vrátí0,
správné přičtení1. Při x=4 jsou hodnoty J=5/2,J_0=9/4,
a rozdíl mezi oběma znaménky je1/2. Obecně je rozdíl1/k.

Jde o chybu přesného popisu O(1) v odpovědi, nikoli
samotné asymptotické meze O(1), která půlskok pohltí.
Tento závěr je oddělen od chybějící reálné části C0179:
platí i poté, co se zadání správně spáruje.

Obecný převod, konstanta i nezávislé přesné testy19999hodnot
jsou v [riemann-explicit.md](riemann-explicit.md).
Mangoldt295 definuje střední hodnotu při prvočíselných
mocninách a299 uvádí příslušnou explicitní formuli.
Pramen tedy Knuthovu minus korekci pro pravostrannou konvenci
nepodporuje. Riemannův originál rovněž pracuje se střední hodnotou.

Sazba381/414/663 a erratum2011 vizuálně. Prohledány
all2-prepre,all2-pre,all2,err2 a aktuální TeX bez opravy
znaménka. Historická řada druhého vydání tuto minus korekci
přidává24.10.1995 na staré614. Fyzický poslední dotisk
a prvenství neověřeny; návrh neodeslán.
