# V2-C0124 — chybné dosazení zlatého řezu v odpovědi 26

Stav: **confirmed**. §4.5.2-26, str.643, poslední věta odpovědi.
Originál celé strany i zvětšený výřez byly vizuálně přečteny.
Obecná identita v zadání na355 a její důkaz jsou správné.

Označme phi=(1+sqrt(5))/2, zlatý řez. Tištěný příklad tvrdí

```text
2G(4phi)-5G(2phi)+G(phi²/2)-G(phi³)=2G(2phi²).
```

Protože phi²=phi+1, v obecné identitě pro x=phi platí
1+2phi=phi³, 1+1/phi=phi, 1+1/(2phi)=phi²/2. Po zrušení
2G(phi) a přenesení zbývajících členů tedy dostáváme přesně

```text
2G(4phi)-5G(2phi)+G(phi²/2)-G(phi³)=-2G(1+4phi).
```

Chyba není jen alternativní zápis stejné hodnoty: pro Brentovu
funkci je G(x)<0 při x>1, neboť G(x)=-G(1/x) a její ocasová
pravděpodobnost je kladná na (0,1). Kladnost též plyne z
Morrisovy kladné hustoty xi=-G', jejíž věta2 byla přečtena.
Tištěná pravá strana je záporná, opravená pravá strana kladná.

Podrobnější souvislosti a obecný důkaz v `gcd-model.md`;
symbolické dosazení v `results/gcd-model.json`, checkpoint algebra.
K potvrzení nepotřebujeme numerickou aproximaci G.

Čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` prohledány
2026-11-02 podle stran355/643/644, čísla úlohy a výrazů pro phi;
žádná oprava tohoto příkladu nenalezena. Aktuální fyzický dotisk
a prvenství neověřeny. Návrh hlášení neodeslán.
