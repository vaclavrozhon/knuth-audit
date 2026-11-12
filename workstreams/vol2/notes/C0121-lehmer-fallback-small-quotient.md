# V2-C0121 — plné dělení v L4 nemusí mít velký podíl

Stav: **confirmed**. §4.5.2, str.347, závorka v kroku L4.
Originál zobrazen 2026-11-02. Vysvětlení říká, že B=0 implikuje,
že Eukleidův algoritmus vyžaduje velmi velký podíl.

Vezměme základ b=10, p=4 cifry ve slově, u=10001,v=10000. Obě čísla
vyžadují více než jedno slovo, takže L1 neukončí výpočet. Nejmenší
k s floor(u/10^k)<10000 je k=1. Vedoucí části jsou obě1000 a
A=D=1,B=C=0. Test L2 porovná

```text
floor((1000+1)/(1000+0)) = 1,
floor((1000+0)/(1000+1)) = 0.
```

Podíly se liší. Algoritmus přejde do L4 s B=0, kde vykoná plné dělení
10001 div10000. Jeho podíl je1, nejmenší možný pro u>=v>0.
Výsledná dvojice10000,1 a konečný gcd1 jsou správné.

Pro libovolně velké slovo W=b^p funguje stejná rodina u=W+1,v=W:
obě vedoucí části jsou h=b^(p-1). Dolní odhad podílu je0, horní je
1 pro h>=2, respektive2 pro h=1. Rozhodnutí L4 není způsobeno velikostí
pravého podílu, ale tím, že interval odhadů překračuje celočíselnou hranici.

Oprava může vypustit danou implikaci nebo dodat, že neshoda vzniká také
u malých podílů poblíž hranice; samotné kroky L1–L4 se nemění. Z příkladu
neplyne žádné tvrzení o četnosti při náhodných vstupech.

Čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` prohledány podle
strany i výrazů Lehmer/quotient/simulate/precision 2026-11-02. Oprava
nenalezena. Důkaz algoritmu v `gcd-extensions.md`; reprodukce protipříkladu
v `verify_gcd_extensions.py` a jeho výsledcích.
Aktuální fyzický dotisk a prvenství neověřeny, návrh hlášení neodeslán.
