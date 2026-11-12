# V2-C0149: který Nikomachův postup se analyzuje?

Stav: **candidate**, historická interpretace. §4.5.4-8,
str.659, tvrzení o N ln ln N+O(N) operacích původního
algoritmu popsaného Nikomachem.

Přímý překlad *Introduction to Arithmetic*,1926, I.13.2–8,
str.204–205, postupuje přes všechny liché členy3,5,7,...
a jejich liché násobky od trojnásobku. Poznámka vydavatelů
na205 výslovně upozorňuje na rozdíl: běžný výklad používá
jen lichá prvočísla, zatímco doslovné znění zdá se zahrnuje
všechna lichá čísla. Současně připouští, že tak přísný
výklad nemusí být zamýšlen. Proto zde **není potvrzená chyba**.

Matematický rozdíl je podstatný. Pokud se skutečně zpracovávají
všechny liché základy d>=3, počet záznamů d*3,d*5,...<=N je

```
sum_(3<=d<=N/3, d odd) (N/(2d)+O(1))
 = (N/4)ln N+O(N).
```

Je tedy řádu N ln N, nikoli N ln ln N. Pokud se složené
základy přeskakují, Mertensův součet dává řád N ln ln N,
což je správná složitost knižního sítaS. Konkrétní vedoucí
faktor záleží na počítaných operacích; zde napadáme jen rozdíl řádů.

Doložen je původní historický algoritmus prostřednictvím
přímého překladu a výslovná redakční nejistota. Řecké
rukopisy ani zamýšlený výklad Knuthovy věty nejsou rozhodnuty.
Možné upřesnění: uvést složitost standardního síta s vynecháváním
složených základů a od historické atribuce ji oddělit.

[Překlad vydaný University of Michigan](https://www.fulcrum.org/concern/monographs/zs25xc31c);
místní výňatek203–206, příslušné obrázky, metadata
v `sources/factoring-basic.json`. Všechny4 vrstvy errat
i současný TeX prohledány, upřesnění nenalezeno.
Kontrola3.11.2026; neodesláno.
