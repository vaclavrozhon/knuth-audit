# V2-C0026: oprava2004 nesprávně zahrnuje kubický člen

**Confirmed**, 1.11.2026. Veřejné erratum ze7.1.2004 pro
§3.3.2-30, str.569 řádek12, nahrazuje mez j>=8 mezí j>=3
v tvrzení c_j=O(n^(-3)). Původní strana569 i příslušná
strana31 historických errat vizuálně přečteny; doklad je
`images/errata-partition-1999-2004.png`.

Kniha píše exponenciálu lokálního rozvoje jako
exp(−t²/2+f(exp(−rho))) exp(i c_1 t−c_2 t²−i c_3 t³+...),
kde rho=n/m a delta=sqrt(n)/m. Koeficient kubického členu je

```text
c_3 = delta³ theta³ f(exp(−rho))/6,
theta=z d/dz,
f(z)=−m log(z)−sum_(k=1)^n log(1−z^k).
```

Při m=n³/alpha a pevném alpha>0 má správná třetí derivace
(nezávisle na chybně vytištěné identitě C0025) rozvoj

```text
theta³ f(exp(−rho)) = 2n/rho³ + O(rho sum_(k=1)^n k^4).
```

Odhad je rovnoměrný, protože k rho<=alpha/n. Jeho důkaz:
singulární část−n log(rho) dává2n/rho³; lineární a kvadratická
část pravidelného rozvoje po třech derivacích zmizí, první
zbývající člen je řádu rho sum k^4. Vyšší členy jsou rovnoměrně
menší v pevném okolí0. Jelikož rho=alpha/n² a delta=alpha/n^(5/2),
dostáváme

```text
c_3 = 1/(3sqrt(n)) + O(n^(-9/2)).
```

c_3 tedy není O(n^(-3)). Původní mez j>=8 odpovídá velikosti
1/[j n^(j/2−1)] vedoucího členu pro pevné j>=3; přechod na3
je nesprávný. Oprava horního indexu c^3 na dolní index c_3 z12.4.1999
tento problém nemění. Hlavní asymptotické vzorce úlohy jsou
správné a mají nezávislý důkaz v `partition-certificate.md`.

Všechny pozdější vrstvy errat i aktuální TeX prohledány1.11.2026.
Zrušení nebo oprava této změny nenalezeny. Aktuální PDF historických
errat bylo staženo1.11.2026 a shoduje se s archivem31.10.
Nejnovější fyzický tisk a prvenství neověřeny; draft neodeslán.
