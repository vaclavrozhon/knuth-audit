# Souvislý průchod §1.2.7 — 5. listopadu 2026

Přímo přečten původní text na tištěných stranách 75–79 a odpovědi
492–493 (soubor 90–94 a 507–508). Na 79 a 493 začíná také Fibonacciho
sekce; její obsah není tímto blokem uzavřen. Převzaty úplné důkazy
`harmonic-finite.md`, `harmonic-valuations.md`, `harmonic-analytic.md`
a `harmonic-transform.md`, přesné výsledky `results/harmonic.json`
a vymezené pramenné recenze X0679, X0682, X0689, X0696, X0704,
X0776–77. Úspěšný výpočet se znovu nespouštěl.

## Matematický rozsah

Pokrývá definice H_n a H_n^(r), geometrické bloky, divergenci H_n,
konvergenci pro r>1, asymptotiku s ostrým zbytkem, sudé zeta hodnoty,
všechny konečné součty, větu A, původních 24 úloh a přidanou úlohu25.
Obory a hraniční případy byly porovnány se sazbou:

- Asymptotický zbytek je kladný a menší než 1/(252n^6) pro n>=1.
  Z integrálu s jádrem 1/t−1/(exp(t)−1) a částečných zlomků plyne
  střídavá jednostranná mez. Oprava výslovného n>0 z2025 je zahrnuta.
- T(m,n)=H_m+H_n−H_(mn) je nerostoucí v každém kladném indexu.
  Maximum1 nastává právě při m=1 nebo n=1; infimum je gamma
  a není dosaženo. Odpověď7 tuto odlišnost od minima správně vysvětluje.
- S_n(x)=sum C(n,k)x^k H_k má polynomiální tvar
  (1+x)^n H_n−sum_(j=1)^n (1+x)^(n−j)/j. Ten platí také pro x=−1
  a n=0; podílový mezikrok (10) se v x=−1 nepoužívá.
- Věta A zahrnuje n=0; kladný ocas má mez 1/(x(n+1)) pro x>0.
  S_1=x není nepravdivé tvrzení; změna na S_0=0 zpřehledňuje základ.
- Dělitelnost čitatele H_(p−1) číslem p, a pro p>3 číslem p²,
  je doložena obecně. Valuace v_2(H_n)=−floor(lg n) platí pro n>=1;
  u součtu prvních n lichých reciprokých čísel je v_2=2v_2(n).
- Oba tvary odpovědi16 jsou pro n>=1 totožné; novější H_(2n)−H_n/2
  zahrnuje také prázdný součet. Odpověď9 musí při n=0 vrátit0.
- Číslice H_10000, prefix gamma a konstanta .158 v odpovědi8
  jsou podloženy uloženými racionálními intervaly. Odhad zeta(1000)
  se vztahuje k absolutní chybě, nikoli k tvrzení o zaokrouhlení na301 míst.
- Inverzní gama součin konverguje lokálně stejnoměrně v celé rovině;
  H_z=gamma+psi(z+1) je meromorfní se zápornými celočíselnými póly.
  Vyšší komplexní mocniny vyžadují volbu větve. Pouhé interpolování
  celočíselných hodnot by samo neurčovalo jediné pokračování.
- Přidané H_n^(u,v) dělí konečný čtverec indexů na dva trojúhelníky
  s jednou společnou diagonálou. Obě nulové specializace odpovědi2022
  a součtová identita platí i pro komplexní exponenty.

## Nález a známé změny

C0010 zůstává potvrzený v původním zadání20 na79. Pro
N_k=2^(2^k), a_(N_k)=2^(−k), a_(N_k+1)=−2^(−k), ostatní a_n=0,
je sum |a_n|=2. Funkce g(x)=sum 2^(−k)x^N_k je spojitá na[0,1],
f(x)=(1−x)g(x), f(1)=0. Pravý integrand je tedy −g(y), spojitě
rozšířený i v1, a jeho integrál je konečný. Naproti tomu
a_(N_k) H_(N_k)>1/2, takže členy levé řady nejdou k nule.
Párování členů není důkazem obyčejné konvergence této řady.
Stačí vážená absolutní konvergence; zvláště bod uvnitř kruhu konvergence.

Změna2026 odstraňuje pouze Gouldovu citaci. Původní Klamkinovo
zadání4946 se týká konkrétně koeficientů1/n!, pro které je vážená
řada absolutně konvergentní. C0010 se mu nepřipisuje; nepřečtenému
Kantorovu řešení se rovněž nepřipisuje žádná chyba.

Pět erratových zdrojů bylo dnes staženo a hashově porovnáno;
manifest je `sources/sequential-2026-11-05/errata-refresh.json`.
X0090 mapujeme jako původní opravy jen na75 a492. Doplněný odkaz
na logaritmickou řadu na77 není opravou nesprávného původního odkazu:
původní text žádné číslo odkazu nemá. Změny S_1 na S_0 a explicitní
obor věty A jsou upřesnění. Přidaná úloha25 a chybná odpověď2013
nejsou součástí původní strany493. Žádná z těchto změn proto sama
nebarví původní77 či493 červeně. Nový dosud neevidovaný nález nevznikl.

## Bibliografie a dokončení bloku

Úlohy7 a20 se nyní uzavírají v matematickém rozsahu s výslovnými
výjimkami: Nanjundiah5022, AMM70(1963),575–577; původní řešení4946,
AMM69(1962),239–240, zejména KantorI. Pozdější Guyův přetisk obsahuje
jen II/III a tuto mezeru neuzavírá. Neúspěšná hledání bez nové stopy
se neopakují. Pramenné záznamy X0091/X0704/X0777 zůstávají partial.
Ostatní přijaté prameny mají přesné meze v jejich vlastních recenzích;
přijetí konkrétní pasáže neznamená úplný audit celého článku.

Strany75–78 a492 jsou obsahově zkontrolované, nálezy mají v mapě
přednost před zelenou barvou. Strany79 a493 mají zatím částečné pokrytí
kvůli navazujícímu Fibonacciho textu. Celkem je uzavřeno856/932
původních úloh,76 zůstává partial; to není procento celé knihy.
