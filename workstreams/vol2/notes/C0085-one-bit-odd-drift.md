# V2-C0085: drift při jediném binárním místě a lichých polovinách

**Confirmed pro rozšířeníTheoremD na zaokrouhlování na liché.**
§4.2.2, str.237, první věta odstavce za důkazovým odkazemTheoremD.
Nezpochybňuje se zde hlavní varianta s doporučeným binárním
zaokrouhlováním na sudé. Původní sazba217,236–237 a úloha29 na245
vizuálně přečteny. Novější fyzický tisk/prvenství neověřeny, neodesláno.

Vezměme základ b=2, počet cifer p=1 a dostatečně široký konečný rozsah
exponentů, např.−10..10. Nenulové hodnoty jsou ±2^e. Funkce R_o
zaokrouhluje na nejbližší hodnotu a přesnou polovinu podle liché cifry
v krokuN5, před případným následným posunem při přenosu. Právě takto
se rozumí změna pravidla v AlgoritmuN; nejde o odříznutí všech vstupů.
Na půlce3/4=(.11)_2 se volí(.1)_2=1/2, protože její zachovaná cifra
je lichá, zatímco alternativa(1.0)_2 má před přenosem sudou cifru.

Položme u=1,v=1/4. Všechny operandy i mezivýsledky jsou v rozsahu:

```text
u⊕v        = R_o(5/4) = 1         (jednoznačně nejbližší),
(u⊕v)⊖v    = R_o(3/4) = 1/2       (lichá polovina),
((u⊕v)⊖v)⊕v = R_o(3/4) = 1/2,
(((u⊕v)⊖v)⊕v)⊖v = R_o(1/4) = 1/4 (přesně).
```

Pravá stranaTheoremD je tedy1/2 a levá1/4. Věta zaTheoremD tvrdící
platnost i pro liché poloviny potřebuje přinejmenším vyloučit b=2,p=1.
Pokud by se volba sudé/liché vykládala až na finálním normalizovaném
slově, v tomto formátu mají všechny nenulové hodnoty cifru1 a pravidlo
by vůbec neurčovalo obě varianty. Proto je ve zprávě výslovná vazba
na krokN5. Kniha jednobitový formát výslovně používá v úloze29;
obecný předpoklad p>=2 zde uveden není.

Čtyři vrstvy all2-prepre,all2-pre,all2,err2 a aktuální TeX prohledány
2.11.2026 podle237,TheoremD,drift,rounding; relevantní oprava nenalezena.
Reprodukce: results/accuracy-exact.json, D_b2_p1_odd. Konečná kontrola
obsahuje150640 dvojic pro variantyD; našla uvedenou výjimku a žádnou
další ve vymezených formátech. **Absence dalšího selhání není obecný důkaz**
opravenéD. Kompletní obecný důkaz byl následně dokončen v
`accuracy-drift.md`; výjimka je právě b2,p1, liché poloviny, u≠0 a v=u/4.
