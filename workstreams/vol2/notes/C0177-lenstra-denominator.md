# V2-C0177: chybný jmenovatel v Lenstrově algoritmu

Stav **confirmed**, §4.5.4-42, odpověď667, krokL2.
Jmenovatel vzorce pro mu je vytištěn jako2*v3*s; správně
má být2*v1*s. Ověřeno v původní sazbě včetně zvětšeného výřezu.

Přesný protipříklad: N=14,r=1,s=3. Inicializace dává
rbar=1,r'=2,u=2,w=1,theta=2. Dvojice (v1,v3) postupně jsou

```
(0,3), (1,2), (-1,1), (2,1), (-3,0).
```

Předposlední dvojice vznikne pomocí výslovné úpravy podíluL4.
Pro ni k=0 dává z=w*v1+k*s=2, který splňuje0<z<=2theta.
Diskriminant je(6+1+4)^2−4*2*1*14=9. Pro sigma=−1
vypočte vytištěný vzorec

```
lambda=(6-1+4-3)/6=1,
mu=(6+1-4+3)/6=1.
```

Obě hodnoty jsou kladná celá čísla, takže L2 vypíše
lambda*s+r=4. Číslo4 nedělí14. Úplný tištěný algoritmus
vrátí{1,4,7}, správný výsledek je{1,7}.
Opravený jmenovatel dává mu=6/12=1/2 a tento výstup odmítne.
Je to chyba algoritmického výsledku, ne pouze pomocného odůvodnění.

Obecné odvození i úplný důkaz opravené varianty jsou v
[lenstra-residues.md](lenstra-residues.md), zvláště(L6).
První vážený faktor se dělí v3, druhý v1; záměna nemá
algebraické opodstatnění. Lenstrův původní článek na333
má správnou rovnici obou vážených faktorů.

Prohledány all2-prepre,all2-pre,all2,err2 a aktuální TeX,
bez nalezené opravy. Historická errata druhého vydání mají
stejný jmenovatel pod novou odpovědí42/616 z11.10.1995.
Testy a zdrojová metadata jsou společné s hlavní poznámkou.
Poslední fyzický dotisk a prvenství neověřeny; návrh neodeslán.
