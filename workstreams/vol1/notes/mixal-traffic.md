# §1.3.2-20: řízení semaforu

Originály s.161–162 a520–521 zobrazeny1.listopadu2026. Časová jednotka
u je10 mikrosekund, takže sekunda je100000u. Registr X má v bajtech2,3
barvy Del Mar a Berkeley (1 zelená,2 oranžová,3 červená); v bajtech4,5
pokyny chodcům (0 zhasnuto,1 WALK,2 DON'T WALK). Vnější požadavek
nastavuje přepínač přetečení. JOV a JNOV jej testují a vynulují.

## Známá oprava a podprogram DELAY

První dotisk má na s.521 instrukci `LDA *=`, která není platný výraz
MIXAL. Erratum20.ledna2008 ji nahrazuje `LDA *` s komentářem o ztrátě2u.
Náš přepis `mixal_traffic.py` obsahuje tuto zveřejněnou opravu. Byly
prohledány všechny čtyři vrstvy errat podle stran i názvů podprogramů;
Další stylistická oprava zadání z21.května1999 mění jednotné číslo
„this traffic light“ na „these lights“. Výpočty ani hardwarovou
konvenci nemění.

Vstup DELAY je nezáporné celé n v registru A. STJ uloží návratovou
adresu za2u, DECA6 stojí1u, dvojice DECA2/JAP se opakuje k-krát,
k=max(1,ceil((n−6)/2)). Po ní A=n−6−2k. JAN a návratový JMP stojí
po1u; NOP se vykoná právě při A=0. Čas je tedy

```
5+2k+[n−6−2k=0] = max(n,7).
```

Hranaté závorky zde znamenají1, pokud podmínka platí, jinak0.
Cena volajícího JMP není zahrnuta. Pro n<=7 je k=1 a A<0;
pro větší n rozhoduje parita. Všechna odčítání zůstanou mezi−8 a
největším strojovým číslem, takže přepínač přetečení nezměníme.
Počet instrukcí je max(n,7)−1; jedinou instrukcí ceny2u je STJ.
Ostatní registry ani porovnávací indikátor se nemění. Návratový
registr J po posledním JMP obsahuje adresu za tímto JMP.

## Přesné fáze a blikání

Označme t okamžik přepnutí chodce z WALK na DON'T WALK těsně před
voláním FLASH. ENT1 a JMP volajícího plus první instrukce FLASH
a DELAY způsobí první zhasnutí přesně v t+50000. Každé další
rozsvícení či zhasnutí následuje po50000u. Pro opakovanou půlsekundu
je podstatná právě opravená instrukce LDA * ceny2u:

```
DEC2 1 + J2Z 1 + LDA * 2 + JMP 1 + LDA 2 + JMP 1
+ DELAY 49991 + DECX 1 = 50000.
```

Po osmém rozsvícení v t+800000 následují DEC2,J2Z,LDA,JMP,DELAY,
návrat z FLASH a LDX oranžové. Jejich ceny jsou
1+1+2+1+399992+1+2=400000. Celá varovná fáze tak trvá přesně12s.

Následující tabulka používá čas0 při prvním rozsvícení zelené Del Mar;
požadavek již čeká při prvním testu. Každá změna registru X se počítá
na konci instrukce, jak zadání výslovně požaduje.

| Čas od první zelené | Změna |
|---:|---|
| 0s | Del Mar zelená, WALK; Berkeley červená |
| 18s | Začátek dvanáctisekundového varování Del Mar |
| 30s | Del Mar oranžová |
| 38s | Berkeley zelená, WALK |
| 46s | Začátek dvanáctisekundového varování Berkeley |
| 58s | Berkeley oranžová |
| 63s | Del Mar zelená, WALK |

Přímé součty mezi barevnými přepnutími jsou
2+1+799995+2=800000u (Del Mar oranžová),
2+1+799996+1=800000u (prvních8s Berkeley zelené),
1+2+1+499994+2=500000u (Berkeley oranžová).
Po návratu k Del Mar trvá nejméně18s do dalšího varování, tedy
nejméně30s zelené celkem. Není-li požadavek, JNOV se opakuje a
žádné světlo se už nezmění. Vnější požadavek zpožděný za minimální
čekání prodlouží pouze zelenou Del Mar.

ALF konstanty a operace na X nikdy nepřenášejí do sousedního bajtu:
počáteční WALK1 se zvýší na2; blikání střídá2 a0 odečtením/přičtením2.
Pro Del Mar jde o přírůstky násobené velikostí bajtu. Barvy zůstávají
vždy (1,3),(2,3),(3,1),(3,2); WALK se nevyskytuje s červenou či oranžovou.

## Reprodukce a hranice asynchronního vstupu

Checker prošel15125 kontrolami. DELAY byl771krát spuštěn po jednotlivých
instrukcích (n=0..256,b=64,65,100) a porovnán s odvozeným zkráceným
modelem ve všech registrech, celé paměti, indikátorech, čase i počtu
instrukcí. Model celého programu zkracuje jen takto dokázané čekání
a prázdné dotazování. Úplný seznam změn světel pro jeden cyklus
souhlasí s nezávislou časovou specifikací pro všech37 radixů.
Dále prošlo165 časových scénářů požadavků. Úspěšný checker neopakovat.

Pro tyto scénáře je model čtení přepínače výslovný: JOV/JNOV jej čte
na začátku instrukce; vnější událost na hranici je dostupná následující
instrukci. Přepnutí Berkeley na oranžovou nastane při prvním cyklu
v čase5800002u od spuštění (první LDX skončil v2u). Bezprostřední
JOV začíná ve stejném čase. Požadavek přesně na této hranici se v našem
modelu vymaže; pozdější požadavek vyvolá nový cyklus. Při jiném modelu,
kdy JOV testuje až na konci instrukce, by se mazací okno prodloužilo
ještě o1u do oranžové fáze. Žádný počet simulací nemůže určit
nepopsané pořadí souběžné vnější události a čtení hardwaru.

**Uzavřeno:** obecné časování, délky všech fází, barvy a blikání,
obsluha požadavků mimo uvedenou hranici při popsaném modelu.
**Otevřeno:** zda zamýšlená hardwarová konvence na hranici dovoluje
ztrátu požadavku během přechodu do oranžové, nebo vyžaduje úpravu
programu. Zadání určuje okamžik změny X, nikoli okamžik testu
přepínače. Zatím to není potvrzená chyba. Celkový stav úlohy20 je
proto `partial`; nelze jej nahradit tvrzením, že simulace prověřily
libovolně načasovaný analogový vstup.
