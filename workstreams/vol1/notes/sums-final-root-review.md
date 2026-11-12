# Sumační konvence a poslední prameny §1.2.3

Root převzal závěrečný zmrazený paket `parallel/sums-remaining-sources/`:
23 souborů a 16 zaznamenaných vstupů/dokladů ověřeno podle velikosti
a SHA-256. `MANIFEST-final.json` má SHA-256
`9ab777d736e0889ad3e445b79b0366bce34173c63c0b6da1ee495fdfbf064e8c`.
Sedm dílčích manifestů uvnitř paketu již bylo přijato samostatně;
jejich závěry se nyní nepřepočítávají. X0762 uzavírá celé úlohy 1 a 19,
X0763 obsahovou atribuci Fourier/Iverson, X0764 zachovává přesnou
pramennou mezeru u Apostola. C0004 je nově dismissed.

## Proč C0004 není doložený rozpor

Root přímo zobrazil knižní 27, 34–35, all1-prepre 5–6 a 31 a all1
4 a 11. Původní úloha 1 je prostě součet a1+a2+a3 pro mez 3,14.
V roce 2010 se přesunula na číslo 2; nová 1 se ptá na a2+...+a0.
Odpověď 2010 definuje tři tečky pravidlem spojování orientovaných
úseků a dává −a1. Oprava 2007 k úloze 19 dává obvyklé teleskopování
násobené indikátorem m<=n; indikátor má hodnotu 1, když podmínka platí,
a 0 jinak. Doplněk 2022 nabízí alternativní použití sigmy slovy
„We might also say“ a výslovně odlišuje součet s podmínkou na indexu.
Současně se v hlavním textu mění „equivalent“ na „essentially equivalent“.

Obě konvence mají přesný a konzistentní model. Pro posloupnost c_j
na celých číslech označme T_c(p,q) součet přes množinu celých j
s p<=j<=q. Pro p>q je nulový. Zvolme funkci F na celých číslech
s F(k)−F(k−1)=c_k a definujme orientovaný součet

    U_c(p,q) = F(q) − F(p−1).

Taková F existuje rekurzivně oběma směry od F(0); její aditivní
konstanta výsledek nemění. Přímým odečtením se pro všechna celá p,q,r
dokáže U_c(p,q)+U_c(q+1,r)=U_c(p,r). Pro p<=q souhlasí s T_c,
pro p=q+1 je nula a pro p>q+1 je záporným součtem od q+1 do p−1.

V úloze 19 vezměme c_j=a_j−a_(j−1). Dostaneme

    T_c(m,n) = (a_n−a_(m−1))[m<=n],
    U_c(m,n) = a_n−a_(m−1).

Starý příklad a_j=j,m=2,n=0 skutečně dává 0 versus −1. Dokazuje
rozdíl definic; rozpor by vznikl teprve dodatečným požadavkem,
že se alternativa z odpovědi 1 musí globálně použít i na odpověď 19.
Doložený text tento silnější požadavek nevynucuje. Proto root
zamítá C0004 jako kandidáta matematické chyby. Možnost výslovněji
vymezit lokální konvenci je redakční podnět, nikoli potvrzený nález.
Staré testy ani archivní poznámky se nemění; tento závěr je nahrazuje
jen v otázce konečného posouzení kandidáta. Známé erratum X0045 trvá.

## Fourier a Iverson

Root přímo zobrazil BnF identifikaci výřezu Fourierových Oeuvres II
a s. 271, 279–280 (PDF 1–3, 11–12). Záhlaví přetisku odkazuje na
Bulletin des Sciences, s. 58–70, duben 1820. Rovnice (9) na 279
má sigma s i=1 dole a i=infinity nahoře; text na 280 výslovně
vysvětluje dosazování celých i=1,2,3,... a sčítání členů.
Knižní atribuce na 27 je tím obsahově doložena. Původní časopisecký
exemplář 1820, samostatný historický titul přetisku ani absolutní
prvenství vůči veškeré starší literatuře se nevydávají za prověřené.

Root přímo zobrazil Iversonův titul, copyright a s. 11 (PDF 8, 9, 38).
Jde o A Programming Language, copyright 1962, čtvrtý tisk květen 1967.
Relační výrok v kulatých závorkách má hodnotu 1 při platnosti relace,
jinak 0; příkladem je (x>0)−(x<0). V již přijatém autorském zdroji
Knuth, Two Notes on Notation, root znovu četl pasáž ř. 124–128:
rozšíření na libovolné logické výroky v hranatých závorkách se od
Iversonovy původní relační formy výslovně odlišuje. Knižní s. 33
říká „notations such as (16)“, nikoli že Iverson použil doslova
celou pozdější konvenci. Obsahová atribuce je checked; první fyzický
tisk 1962 nebyl kolacionován. C0088 ke Kroneckerovu datu se nemění.

## Apostol zůstává pramenně otevřený

Root přímo zobrazil knižní s. 28: citováno první vydání Mathematical
Analysis (1957), kapitola 12. Matematika přeuspořádání a absolutní
konvergence je již přijata v X0036. Konkrétní kapitola, zejména §12-13,
však dosud nebyla přečtena. Nová institucionální stopa University of
Macedonia vrátila Access Denied; metadata a indexovaný přepis nejsou
kontrolou pramene. Druhé vydání 1974 nelze bez kolace zaměnit za první.

Agent prohledal všechny čtyři erratové vrstvy podle stran i témat;
výsledek a vstupní hashe jsou v results/errata-extract.json. Žádné další
erratum nemění zdejší atribuce ani odkaz na Apostola. Celý hlavní text
§1.2.3 tedy zůstává partial; všech 47 původních úloh je nyní checked
včetně odpovídajících pozdějších oprav. Žádné dříve úspěšné matematické
testy nebyly opakovány. Úplné podklady fixuje root manifest.
