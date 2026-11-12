# V2-C0166: součin pravděpodobnostních mezí pro RSA

**Stav: confirmed.** §4.5.4, strana 405, druhý odstavec,
věta začínající podmínkou o velkých prvočinitelích p1 a q1.
[Původní sazba](../images/vol2-p405.png) byla přečtena vizuálně.
Kniha tvrdí: buď p1*q1 dělí m, nebo je pravděpodobnost
x^m=1 (mod N) menší než 1/(p1*q1).

Vezměme p=23, q=47, N=1081, p1=11, q1=23 a m=22.
Obě prvočísla p,q jsou 2 modulo 3; p1|p-1 a q1|q-1.
Přitom 253 nedělí 22. Modulo 23 vyhovuje všech 22 nenulových
zbytků, modulo 47 právě dva, protože gcd(22,46)=2.
Čínská věta o zbytcích tedy dává přesně 44 řešení modulo 1081.
Pravděpodobnost 44/1081 je větší než 1/253.

Obecný přesný vzorec je

    Pr[x^m=1 (mod pq)] = gcd(m,p-1)*gcd(m,q-1)/(pq).

Každý chybějící prvočinitel dává jeden malý činitel; podmínka,
že chybí alespoň jeden, neopravňuje vynásobit obě meze.
Podrobný vlastní důkaz je v [RSA §3](rsa-basic.md#3-úloha-34-a-chybný-součin-na-straně-405).
Přívlastek „velký“ nemění tuto algebraickou záměnu podmínek;
malý příklad pouze zpřehledňuje přesný výpočet.

Možná obecná oprava: pokud alespoň jedno z p1,q1 nedělí m,
pravděpodobnost je menší než 1/min(p1,q1). Když nedělí ani
jedno, platí silnější mez 1/(p1*q1). Při p1=q1 je třeba
větev společné dělitelnosti psát pomocí lcm, nikoli součinu.
Nález se týká číselné meze, nikoli prolomení RSA.

Dne 3. listopadu 2026 prohledány celé all2-prepre, all2-pre,
all2, err2 a TeX err2 podle stran 405/664, probability,
RSA, p1/q1 a úlohy 34. Odpovídající oprava nenalezena.
Známé změny na okolních stranách jsou vypsány v RSA §6.

[Program](../verify_rsa_basic.py), [výsledek](../results/rsa-basic.json)
a [metadata](../sources/rsa-basic.json) obsahují přesný protipříklad
a kontrolu vzorce na 4992 instancích a 2226816 zbytcích.
Pozdější fyzický dotisk a prvenství nebyly ověřeny.
[Návrh hlášení](../reports/C0166-rsa-root-density-draft.txt) nebyl odeslán.
