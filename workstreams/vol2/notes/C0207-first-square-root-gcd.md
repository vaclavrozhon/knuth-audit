# V2-C0207: první gcd může být celý polynom

Stav: **confirmed**. §4.6.2–15, strana 681, odstavec pro p mod4=1.
Původní sazba byla zobrazena. Uvádí, že gcd bude 1; pro p=5,u=1
je však gcd(x²−1,x²−1)=x²−1 nad F_5.

Obecně x^((p−1)/2) mod(x²−u)=u^((p−1)/4). Pro nenulový čtverec u
je poslední hodnota ±1. Gcd po odečtení 1 je tedy celé x²−u při +1
a je 1 při −1. Stačí nahradit tvrzení formulací, že gcd je triviální.
Doporučení první gcd vynechat zůstává správné; samotné hledání kořene
tento doprovodný omyl nepoškozuje.

Důkaz a přesné kontroly: [sqrt-mod-prime.md](sqrt-mod-prime.md), §2,
`results/sqrt-mod-prime.json`. Všech šest vrstev errat prohledáno
4. listopadu 2026, odpovídající oprava nenalezena; známá oprava 2001
se týká jiného odstavce. Nejnovější fyzický dotisk a prvenství
neověřeny. Nic neodesláno.
