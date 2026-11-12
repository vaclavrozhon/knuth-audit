# V2-C0185: chybějící etapa nula v součtu BBS

**Stav: confirmed.** §4.5.4-43, odpověď 668–669, etapy a celková pravděpodobnost.

Smyčka začíná t=0, ale geometrický součet chyb na 669 od t=1. V nulté etapě je třeba zjistit parity a/2,b/2. Pro r=8 dávají uvedené meze celkem19/18, ne <=8/9. Skutečná chyba >9/10 se netvrdí; vlastní důkaz s upravenými konstantami dává úspěch >1/2.

Úplný důkaz a oprava: [BBS](bbs.md). Přesná data: `results/bbs.json`;
nezávislé modely: `verify_bbs.py`. Původní sazba 416–417/668–669
a relevantní stránka errat byly vizuálně přečteny. Všechny čtyři
časové vrstvy errat a aktuální TeX prohledány bez této opravy.
Známé opravy z 2000/2001 jsou zahrnuty. Tištěný exemplář ani prvenství
nejsou ověřeny; návrh hlášení nebyl odeslán.
