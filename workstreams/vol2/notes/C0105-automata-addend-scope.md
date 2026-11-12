# V2-C0105: zahrnuje úloha 11 také přídavné q?

**candidate**, 2.11.2026. §4.3.3-11, zadání str.317, odpověď633–634.
Původní stránky317/633/634 a definice315 byly vizuálně přečteny.
Jde o vyjasnění rozsahu operace, nikoli prokázané selhání automatů.

Zadání se ptá na počet modulů pro součin dvou n-bitových čísel.
Odpověď uvádí ostrou mez floor(n/2)+1 a výslovně odkazuje na potřebu
modulu M_2 u dvoubitových čísel. Samotné pole však v textu počítá
obecnější UV+q se třetím n-bitovým vstupem q.

Pro čisté násobení, tedy q=0,n=2, stačí jeden modul pro všech16
párů0<=U,V<4. U největšího páru U=V=3 nabývá tříbitový akumulátor
S_1=4z2+2z1+z0 v časech0,1,... hodnot

```
0,1,2,2,1,0,0,... .
```

Výstup je1,0,0,1, tedy9. Bit z2 prvního modulu nikdy není1;
do M_2 nepřijdou nenulové bity operandů ani přenos, a M_2 zůstává0.
Obecně jsou první čtyři nenulové akumulace pro dva bity omezeny
postupně1,2,2,1, takže tentýž argument platí pro všechny dvojice.

Pokud je q proměnné, mez je správná i pro n=2. Například U=V=q=3
dává UV+q=12 se dvěma moduly, kdežto zkrácené pole s jedním modulem
vrací4. Rovněž příklad v tabulce2 má nenulové q, takže sám o sobě
nedokládá nutnost druhého modulu pro čistý součin dvou bitů.

Možné vyjasnění: v zadání výslovně požadovat UV+q, nebo u čistého
násobení uvést výjimku n=2. Podrobný důkaz obou variant a přesné
simulace jsou v [fast-automata.md](fast-automata.md) a
`results/fast-automata.json`. Ve všech čtyřech vrstvách errat nebyla
taková oprava nalezena.

Ponecháno jako candidate, protože slovo „multiplication“ může v
kontextu předchozího textu zahrnovat i jeho přídavný vstup q.
Poslední fyzický dotisk a priorita neověřeny; neodesláno.
