# V2-C0182: chybějící plus v hlasu BBS

**Stav: confirmed.** §4.5.4-43, odpověď na 669, definice G_j.

V definici G_j chybí plus mezi alpha_t a j*beta_t. Následující samostatný vzorec je správný. Přesný příklad m=209, y=1, t=0, epsilon=1/2, a=1, b=2, j=−6, alpha_0=1/128, beta_0=5/512 dává správnou podlahu −1, vytištěný součin 0, mimo krajní chybové pásy.

Úplný důkaz a oprava: [BBS](bbs.md). Přesná data: `results/bbs.json`;
nezávislé modely: `verify_bbs.py`. Původní sazba 416–417/668–669
a relevantní stránka errat byly vizuálně přečteny. Všechny čtyři
časové vrstvy errat a aktuální TeX prohledány bez této opravy.
Známé opravy z 2000/2001 jsou zahrnuty. Tištěný exemplář ani prvenství
nejsou ověřeny; návrh hlášení nebyl odeslán.
