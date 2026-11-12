# V2-C0101: historický dodatek připisuje Eulerovi přesně BBP řadu

**candidate**,2.11.2026. Doplněk30.9.2024 k odpovědi§4.3.1-39,str.628,
ve vrstvách all2/err2 i uloženém aktuálním TeXu. Originál dodatku vizuálně
přečten v [all2,str.10](../images/normal-errata-all2-p10.png).

Dodatek tvrdí, že uvedenou identitu odvodil Euler1779. Citovaný Ojanguren,
Elemente der Mathematik77(2022),94–100, ale rozlišuje dvě různé řady:

```
Euler, (2) na95:
pi = sum_{k>=0} (-1)^k 4^(-k) (2/(4k+1)+2/(4k+2)+1/(4k+3)).

BBP, (3) na96, také zadání a odpověď knihy:
pi = sum_{k>=0} 16^(-k) (4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6)).
```

Ojanguren se na96 výslovně ptá, zda by Euler mohl druhou řadu objevit;
poté sám uvádí dodatečnou nulovou logaritmickou relaci, která ji odvodí
z první. Tedy citovaný pramen podporuje Eulerovo prvenství u příbuzné řady
pro binární extrakci číslic, ale nepřipisuje mu odvození právě tištěné BBP
formule. Navrhované zpřesnění: Euler1779 odvodil blízce příbuznou identitu,
která rovněž umožňuje tento druh výpočtu bitů.

[Původní PDF](../sources/ojanguren-2022.pdf), vizuálně přečtené strany95–97:
[95](../images/ojanguren-2022-2.png),[96](../images/ojanguren-2022-3.png),
[97](../images/ojanguren-2022-4.png).
Primární URL: https://ems.press/content/serial-article-files/45728
Důkaz matematické ekvivalence s přidáním nulové relace je samostatně
ověřen v [classical-bbp.md](classical-bbp.md). Ekvivalence sama není
historický důkaz, že Euler provedl tento konkrétní převod.

Kandidát zatím není confirmed: originál Eulerova E706 jsme nezískali
(veřejný download Pacific403, starý MAA odkaz404; žádný pokus obejít
omezení). Neprohlašujeme tedy nezávisle ověřenou absenci dané formule
v celém Eulerově textu. Otázkou také zůstává, zda autor dodatku nepoužil
slova „stated identity“ volně pro tuto rodinu příbuzných formulí.
Rozdíl dvou řad je nicméně v citovaném prameni jednoznačný.

Všechny čtyři vrstvy errat prohledány podle628,39,Euler,Ojanguren a
polylog; jiné zpřesnění této atribuce nenalezeno. Poslední fyzický dotisk
ani priorita neověřeny. Nic neodesláno.
