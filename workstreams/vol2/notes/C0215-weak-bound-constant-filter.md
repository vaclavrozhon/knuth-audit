# V2-C0215: konstantní filtr se slabou mezí vyřadí pravý faktor

Stav: **confirmed**. §4.6.2, strana452, odstavec o testu trailing coefficient,
v kombinaci s předchozím odstavcem o mezi pro alespoň jeden faktor.

Vezměme u=(x+1)(x^2+x+100), B=20 a p^e=41>2B. Malý pravý faktor
x+1 má koeficienty omezené B. Úplný rozklad modulo41 seřaďme jako
v_1=x^2+x+18, v_2=x+1; kvadratický faktor je ireducibilní,
protože jeho diskriminant11 není čtverec modulo41.

Při r=2,d=1 pravidlo i_1=1 testuje jen v_1. Souměrný zbytek jeho
konstanty je18 a 18 nedělí u(0)=100. Filtr odmítne kombinaci dříve,
než se vyzkouší její doplněk v_2, a nenajde žádný faktor.
Bez filtru slabá varianta úspěšně nalezne x+1.

Oprava: u slabé meze testovat konstanty obou stran a pokračovat,
pokud alespoň jedna projde, nebo udržovat zvláštní dostatečně velký
modul pro konstanty. Základní F s plnou mezí pro všechny faktory
je správný. Viz [integer-factorization.md](integer-factorization.md), §5.

Sazba452 a všech šest vrstev errat ověřeny 4.11.2026; oprava nenalezena.
Fyzický dotisk/prvenství neověřeny. Nic neodesláno.
