# V2-C0022: vynechaná možnost žádné malé mezery

**Confirmed**, 1.11.2026. §3.3.2-26(c), odpověď str.566,
třetí vydání, první dotisk1997. `images/vol2-p566.png` přečten
v původní sazbě i ve zvětšeném výřezu.

F_k(s) je distribuční funkce k-té nejmenší mezery S_(k).
G_j(s) je pravděpodobnost, že právě j mezer je menších než s.
Tištěná identita začíná G_1(s), ale musí začínat G_0(s):

```text
1−F_k(s) = G_0(s)+G_1(s)+...+G_(k−1)(s).
```

Pro n=2,k=2,s=1/4 je levá strana1, protože větší ze dvou mezer
o součtu1 je vždy alespoň1/2. Pravá strana v knize je G_1(1/4)=1/2.
Zbývající pravděpodobnost G_0(1/4)=1/2 právě chybí. Tento příklad
funguje jak pro původní kruhové mezery, tak po opravě C0018.
Pro k=1 je chyba ještě zřetelnější: správnou odpovědí je G_0(s).

Následující vzorec pro G_j, jeho znaménko(−1)^(j−l), výsledný
součet pro1−F_k a uvedené momenty jsou správné. Oprava tedy mění
jen počáteční index této mezilehlé identity. Vlastní důkazy
a464 přesných porovnání dvojic momentů jsou v `spacings.md`
a `results/spacings.json`.

Všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální
TeX prohledány1.11.2026 podle str.566, odpovědi26 a mezer.
Známá oprava18.9.2002 mění pouze Whitworthovu bibliografickou
atribuci; oprava tohoto indexu nenalezena. Novější fyzický tisk
ani prvenství neověřeny; draft neodeslán.
