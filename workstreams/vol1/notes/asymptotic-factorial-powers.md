# §1.2.11.1-(16)–(17), úloha 12: faktoriálové rozvoje

Audit 1. listopadu 2026; původní strany 109–111 a 503 byly zobrazeny.
Rostoucí mocnina je `n^[r]=Gamma(n+r)/Gamma(n)` a padající
mocnina `n_[r]=Gamma(n+1)/Gamma(n−r+1)`. Zde r je pevné
reálné číslo a n jde po kladných celých číslech do nekonečna.
Gamma je funkce definovaná Eulerovým integrálem a pokračováním
v [gamma-functions.md](gamma-functions.md).

Označme `P_k(r)=c(r,r−k)`: polynom stupně 2k pokračující
diagonálu Stirlingových čísel prvního druhu. Přesná konstrukce
je v [stirling-identities.md](stirling-identities.md), (S3).
P_k splňují `P_k(r+1)=P_k(r)+r P_(k−1)(r)`, P_0=1.
Níže jsou chyby O(...) ve smyslu odhadu pro n→infinity,
s konstantou závislou na pevných r a m.

## Konečné rozvoje pro každé reálné r

Padající rozvoj (17) je již dokázán v
[stirling-analytic.md](stirling-analytic.md), (A2), včetně
zbytku do libovolného řádu. Pro rostoucí rozvoj (16) nelze
prostě nahradit n záporným n v tamním odhadu; použijeme beta integrál.

Nejprve r=−p<0. Pro n>p dává beta integrál a změna proměnné
u=exp(−t) přesně

```text
n^[−p] = 1/Gamma(p) integral_0^infinity exp(−nt) t^(p−1) H_p(t) dt,
H_p(t) = exp(t) ((exp(t)−1)/t)^(p−1).                    (F1)
```

Funkce H_p je analytická v okolí 0, s větví určenou hodnotou 1
uvnitř mocniny. Položíme-li Q_p(t)=((exp(t)−1)/t)^p, platí
H_p=Q_p+(t/p)Q'_p. Pro kladné celé p dává známá exponenciální
generující funkce Stirlingových čísel druhého druhu S(j,p)

```text
[t^k]Q_p(t) = p! S(p+k,p)/(p+k)!,
(p)^[k] [t^k]H_p(t) = S(p+k,p) = P_k(−p).               (F2)
```

Symbol [t^k] znamená koeficient t^k. Poslední rovnost je dualita
Stirlingových polynomů (58). Obě strany druhé rovnosti (F2)
jsou polynomy v p, proto souhlas pro všechna kladná celá p
dokazuje rovnost pro všechna p; zejména pro každé reálné p>0.

Taylorův zbytek H_p po stupni m je O(t^(m+1)) na malém
intervalu [0,epsilon]. Jeho příspěvek k (F1) je nejvýše konstanta
krát `integral_0^infinity exp(−nt)t^(p+m)dt`, tedy
O(n^(−p−m−1)). Na [epsilon,infinity) roste H_p(t)t^(p−1)
nejvýše jako konstanta krát exp(pt); faktor exp(−nt) tam
poskytuje exponenciálně malý zbytek. Totéž dovoluje prodloužit
integrály každého Taylorova členu do nekonečna. Integrace a (F2) dávají

```text
n^[r] = sum_{k=0}^m P_k(r) n^(r−k) + O(n^(r−m−1)).       (F3)
```

Pro libovolné pevné reálné r začneme u r−N<0 a N-krát
použijeme `n^[r+1]=(n+r)n^[r]`. Rekurence P_k výše
zachovává koeficienty (F3); násobení n+r zvedá řád zbytku
přesně o jednu mocninu n. Tím je (16) dokázána pro všechna r.

Pro nezáporné celé r jsou obě mocniny polynomy a rozvoje
skončí. Pro r=−p, p kladné celé, je rostoucí mocnina
`1/((n−1)...(n−p))`. Součin konečně mnoha geometrických
řad konverguje absolutně pro |n|>p. Jeho koeficienty jsou
úplné symetrické polynomy v 1,...,p, tedy S(p+k,p), jak
plyne z generující funkce `product_{j=1}^p(1−jz)^−1`.
Dualita dává přesně knižní alternativní zápis s c(−p,−p−k).

## Úloha 12: ověření zadané koeficientové identity

Definujme F(z) analyticky u nuly rovnicí

```text
F(z) = (z exp(z)/(exp(z)−1))^(1/2),   F(0)=1.             (F4)
```

Odmocnina má jednoznačnou místní větev díky nenulové hodnotě 1.
Beta integrál nyní poskytuje druhé vyjádření stejné rostoucí mocniny:

```text
n^[1/2] = n/Gamma(1/2) integral_0^infinity
                       exp(−nt) t^(−1/2) F(−t) dt.      (F5)
```

Integrál je B(n+1/2,1/2) po substituci u=exp(−t).
Stejný Taylorův odhad jako u (F1) ukazuje, že koeficient
n^(1/2−k) v jeho konečném asymptotickém rozvoji je

```text
(−1)^k Gamma(k+1/2)/Gamma(1/2) [z^k]F(z)
 = (−1/2)_[k] [z^k]F(z).                                (F6)
```

Asymptotické koeficienty jsou jednoznačné: odečteme dva rozvoje,
vezmeme první rozdílný koeficient a po vydělení příslušnou
mocninou n přejdeme k limitě. Porovnání (F3) a (F6) proto
dokazuje zadanou identitu
`P_k(1/2)=(−1/2)_[k] [z^k]F(z)` pro každé k>=0.
**Činitel (−1/2)_[k] je padající faktoriálová mocnina,
nikoli obyčejná k-tá mocnina.** Podtržení je vidět v originálu.

## Divergence a opravený odhad odpovědi 12

Fixujme n!=0 (v kontextu knihy je n kladné celé). Kdyby
`P_k(1/2)n^(−k)` šlo k nule, bylo by P_k(1/2)=O(|n|^k)
jako posloupnost v k. Pro k>=1 máme

```text
|(−1/2)_[k]| = (1/2)(3/2)...(k−1/2) >= (k−1)!/2.
```

Identita (F6) by tedy dávala
`[z^k]F(z)=O(|n|^k/(k−1)!)`. To je právě odhad po známé
opravě z 30. července 1999; první dotisk má chybně (n−1)!.
Takové koeficienty by definovaly funkci G analytickou na celé
komplexní rovině, která se shoduje s F u nuly. Z (F4) by pak
v okolí nuly platila identita

```text
(exp(z)−1) G(z)^2 = z exp(z).                            (F7)
```

Obě strany (F7) jsou analytické na celé rovině, takže rovnost
musí platit všude. Dosazením z=2pi i dostaneme vlevo 0 a
vpravo 2pi i, spor. Členy řady tedy nejdou k nule pro žádné
pevné n!=0 a nekonečný rozvoj nemůže konvergovat. Tento
důkaz nepotřebuje neformální přiřazení F(2pi i)=infinity
v bodě, kde F není definována. Konečné rozvoje (16)–(17)
přitom mají rigorózně dokázané chyby výše.
