# V3-C0002 — v tabulkovém kroku je nesprávný modul

Lokace: odpověď §5-25, tištěná 591 / souborová 602, věta začínající
„In general if f is any divisor…“. Původní sazba je images/intro-file-602.png.
Kniha tvrdí, že z b^((p−1)/f) lze tabulkou délky f/d určit (n/d) mod f,
kde b=a^n, a je primitivní kořen a d dělí gcd(f,n).

Pišme n=dk. Prvek g=a^((p−1)/f) má řád f, tedy g^d má řád f/d.
Hodnota b^((p−1)/f)=(g^d)^k proto určuje pouze k mod (f/d).
Správná náhrada v této větě je **(n/d) mod (f/d)**.

Protipříklad: p=17, a=3, f=4, d=2. Oba exponenty n=2 a n=6 splňují
předpoklady. Dávají b=9, resp. 15, ale 9^4≡15^4≡16 (mod 17).
Požadované (n/d) mod 4 je přitom 1, resp. 3. Jediný klíč tabulky nemůže
určit oba různé výsledky. Primitivnost a=3 plyne také z 3^8≡−1 (mod 17).

6. 11. 2026 prohledány all3-prepre, all3-pre, all3 a err3 podle strany i
pojmů. Žádná příslušná oprava nalezena. Důležitá souvislost: err3-1e,
PDF strana 62, doplněk k tehdejší s. 576 z 5. 5. 1981, obsahuje stejné
chybné „mod f“. Není to známá oprava nynější vady, ale starší výskyt
téže formulace. Zachována sazba images/intro-err3-1e-file-062.png.

Stav confirmed znamená krátce doložený rozpor v našich zdrojích v rámci
prvního průchodu. Nezaručuje prvenství, úplnost auditu ani ověření fyzické knihy.
