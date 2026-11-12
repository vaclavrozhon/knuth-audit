# Kandidát: chybějící inicializace LLINK(Q), §2.3.1-32

Kořenový stav při předání: **V1-C0046, candidate**. Globální ID přidělil koordinátor; lokální dočasné označení a níže zachovaná historie revize slouží návaznosti evidence.
Dočasné označení `explicit-successor-left-link`; stav candidate V1-C0046.

Původní obrazy přečteny: zadání 333, odpověď 570, kontrakt a krok I1 algoritmu I na327. Úloha 32 stanoví obyčejné LLINK a RLINK (ukazatel na podstrom nebo null) a zvláštní pole SUC/PRED pro inorder sousedy. Má se navrhnout algoritmus jako I. Tištěná odpověď přepíše RLINK, SUC, PRED nového Q, ale LLINK(Q) vůbec nezapisuje. AlgoritmusI přitom výslovně inicializuje obě strany Q.

## Nejkratší příklad

Nechť H je hlavička a původní strom má jediný uzel P:

```text
LLINK(H)=P; RLINK(H)=H;
LLINK(P)=null; RLINK(P)=null; SUC(P)=H; PRED(P)=H;
SUC(H)=P; PRED(H)=P.
```

Q je odlišný čerstvě přidělený uzel. Jeho INFO je již nastaveno; starý obsah linků není přidělením nulován. Zvolme `LLINK(Q)=P`. Tištěná posloupnost provede:

```text
RLINK(Q)=null; SUC(Q)=H;
SUC(P)=Q; RLINK(P)=Q;
PRED(Q)=P; PRED(H)=Q.
```

`LLINK(Q)=P` zůstane. V grafu obyčejných potomků vznikne cyklus `P --right--> Q --left--> P`; výsledná struktura tedy není binární strom. Správný výsledek musí mít `LLINK(Q)=null` a inorderP, Q. Stačí doplnit toto jediné přiřazení; zbývajících pět operací pak je správných i při neprázdném původním pravém podstromuP.

## Přesná mez kontraktu

Pokud by volající předem inicializoval Q jako izolovaný list s LLINK(Q)=null, odpověď funguje. Zadání 333 ani odpověď 570 takový předpoklad neuvádějí a předloha I na327 výslovně nastavuje odpovídající pole. Kandidát je proto chybějící inicializace, nikoli chyba při silnějším dodatečném předpokladu nulového levého odkazu. Ověření obecné konvence přidělených uzlů je nutnou součástí kořenové revize.

Všechny čtyři erratové vrstvy byly prohledány podle 333/570 i témat insertion, LLINK, PRED, successor, exercise 32; v již inventarizovaných původních PDF/TeX není oprava tohoto přiřazení. Přilehlá známá oprava odpovědi 23 se týká jiného algoritmu a pole RLINKT.
