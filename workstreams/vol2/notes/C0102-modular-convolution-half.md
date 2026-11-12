# V2-C0102 — interpretace půlení v opravené odpovědi4.3.2-14

Stav: **candidate**, 2.11.2026. Nezapočítávat jako potvrzenou novou chybu.

## Lokalizace a důvod

Tištěná294 definuje w jako kanonický celočíselný zbytek součinu U*V
modulo M=2^q−1. Odpověď632 původního třetího vydání, prvního dotisku,
a erratum31.7.2020 (`all2-pre.pdf`, strana14) byly vizuálně přečteny.
Oprava nahrazuje t_k≈z_k/a_k hodnotou t_k≈2z_k/a_k a posune exponent
výstupu o−1. Dodává sečtení překrývajících se bitových úseků před
redukcí modulo2^q−1. Čtyři vrstvy errat včetně aktuálního TeXu nenabízejí
další vysvětlení půlení či bitu na pozici−1.

## Přesný svědek

Zvolme q3,n2,U=V6. Obě čísla mají plné tři bity. Rozdělení dané úlohou
je u_0=v_0=0,u_1=v_1=3. Váhy jsou a_0=1,a_1=1/sqrt(2). Cyklická
konvoluce je z_0=9/2,z_1=0, takže opravené zaokrouhlování dává přesně
t_0=9,t_1=0. Výstupní součet po opravě je **9/2**. Jeho běžný reálný
zbytek modulo7 je také9/2; správné w je však36 mod7=1.

Jde o přesnou algebraickou situaci, nikoli chybu konečné přesnosti.
Samotné přičtení překrývajících se bitových úseků půlbit neodstraní.

## Jak tomu rozumět správně

Obecně je `S=sum t_k 2^floor(kq/n)` celé a platí S≡2UV modulo M.
Správný výsledek je `(2^(q−1)*S) mod M`, tj. dělení dvěma v kruhu
zbytků. Kruh zbytků modulo M zde znamená celočíselné zbytky s operacemi
redukovanými modulo M. Konkrétně, pro R=S mod M, použijeme
`w=(R+M*(R mod2))/2`. Alternativně přesuneme případný bit na pozici−1
na pozici q−1 před běžnou celočíselnou redukcí.

## Proč pouze candidate

Doslovná interpretace jako reálného součtu následovaného běžným
operátorem mod selhává. Celá sekce je ovšem o modulární aritmetice,
bezprostřední úloha11 vysvětluje modulární dělení a autor mohl ve
stručné odpovědi pokládat cyklické zacházení s bity za implicitní.
Pod tímto výkladem je algoritmus správný. Chybějící explicitní instrukce
je tedy dobře doložena, ale její status jako nové chyby závisí na
výkladu textu. Priorita ani nejnovější fyzický dotisk nejsou ověřeny.

Obecný důkaz a nezávislé přesné kontroly viz `modular-convolution.md`.
Anglický návrh žádosti o vyjasnění je uložen v `reports/`; nic neodesláno.
