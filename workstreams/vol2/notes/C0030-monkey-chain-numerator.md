# V2-C0030: nadbytečný čitatel u zakázaných dvojic ab,bc

**Confirmed**, 1.11.2026. §3.3.2-34, str.571, tabulka případ5.
Původní sazba vizuálně potvrzuje generující funkci
`(1+z)/(1−mz+2z²−z³)` pro řetězce bez dvojic ab a bc,
kde a,b,c jsou různé znaky abecedy velikosti m.

Správný čitatel je1. Již koeficient z je v tištěném vzorci m+1,
ačkoli každé z m jednopísmenných slov je přípustné. Obecný
důkaz: nechť F je generující funkce všech přípustných slov
včetně prázdného a A,B,C funkce slov končících znakem a,b,c.
Přidání posledního znaku dává

```text
A=zF,  B=z(F−A),  C=z(F−B),
F=1+(m−3)zF+A+B+C.
```

Dosazení tedy dává `(1−mz+2z²−z³)F=1`.

Asymptotické sloupce c,tau téhož řádku odpovídají správnému
čitateli1. Všechny vzorce pro momenty i kalibrace141909.33,
290.46 na75 jsou správné. Doklad v `monkey-test.md` zahrnuje
šest symbolických automatů,21 přesných slovních modelů
a rigorózní160bitové intervalové násobení matic.

Všechny čtyři vrstvy errat a aktuální TeX prohledány1.11.2026
podle571, answer34, monkey a excluded; oprava nenalezena.
Fyzický dotisk a prvenství neověřeny; draft neodeslán.
