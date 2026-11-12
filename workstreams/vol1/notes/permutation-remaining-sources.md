# §1.3.3-28–38: primární prameny a známé změny

Kontrola1.11.2026. Matematické důkazy jsou v
`permutation-remaining-working.md`; název souboru je zachován kvůli
starším odkazům, jeho matematická část už není pracovní mezera.
MIX36 a doplněný test nerovnosti33 mají samostatné poznámky.
Kniha je třetí vydání, první dotisk1997; fyzický exemplář neověřen.

## Originály a errata

Přečteny původní obrazy tištěných184–185,526–527 a dodatky v původních
PDF errat: all1-prepre16,38,39 a all1 8,14. Všechny čtyři textové
vrstvy all1-prepre,all1-pre,all1,err1 prohledány podle stran i témat.
Aktuální kopie byly koordinátorem ověřeny1.11.2026.

| Místo | Známá změna | Posouzení |
|---|---|---|
| 184,29 | perfect shuffle,14.10.2008 | Stejná permutace, přesnější názvosloví. |
| 184,30 | posun obou exponentů,1.1.2006 | Opravená charakterizace pevných bodů dokázána. |
| 184,31 | HM38,m>1 a mocnina(m−1)^k,14.10.2008 | Podmínka i opravený průměr ověřeny, včetně uniformního ocasu. |
| 185,34 | směr přiřazení x_k←x_p(k),6.8.2001 | Rozlišeno přesouvání hodnot a čtení následníka. |
| 185/527,37 | nové cvičení a odpověď,29.1.2010 | Úplná indukce a původní pramen přečten. |
| 185/527,38 | nové cvičení a odpověď,24.3.2023 | Všech šest částí,36 konjugátorů i odkaz ověřeny. |
| 526,28 | Herstein–Kaplansky,14.10.2008 | Konkrétní původní stránky ještě chybí. |
| 526,29 | Shamsův vzorec,7.4.2003 | Vzorec nezávisle dokázán; původní článek nepřístupný. |
| 526,31 | rozšířený důkaz reziduálních tříd,14.10.2008 | Doplněna integrálnost i odhad dovolující sečíst hustoty. |
| 527,34 | Fletcher–Silver,26.10.1997 | Algoritmus přečten v primárním souboru ACM. |
| 527,35 | γ'' s βγ' → γ''β s γ',1.1.2006 | Oprava hranice operandů, nikoli jen pořadí; prověřeno přímo. |

Při konečné revizi byl v naší pracovní poznámce35 nalezen přepis
původního chybného pokynu namísto opravy2006. Poznámka jej nyní
správně odlišuje. Cyklický algoritmus ani již provedené MIX testy
tím nebyly dotčeny; nejde o nový nález v knize.

## Skutečně přečtené primární prameny

**Concrete Mathematics, §3.3, s.80–81.** Přečten text i obrazy obou
stran (PDF93–94) a titul autorů Graham,Knuth,Patashnik. Postup
přečíslování a obrácená iterace obsahově souhlasí s úlohou31;
transformace na vzdálenost od mn+1 vysvětluje nezávislost nové iterace
na n. Vlastní důkaz limitního průměru nepředpokládá, že jej tyto dvě
strany uvádějí. Stažená kopie neobsahuje čitelnou tiráž s dotiskem,
takže jí takový dotisk nepřisuzuji.
[Použitá kopie knihy](https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/Misc/Concrete%20Mathematics%20-%20A%20Foundation%20for%20Computer%20Science.pdf).

**Barrington.** Přečtena definice permutačních větvicích programů na
s.1 a celá hlavní věta1 s lemmaty1–3 a indukcí na s.2 originální
konferenční verze1986. Konstrukce konjunkce pomocí komutátoru
pěti-cyklů přímo podporuje připsání kroku v úloze33 i obecný výrok
o booleovských funkcích. Čtena také navazující diskuse na s.2–3,
bez auditu celé teorie uniformity. Kniha cituje rozšířený časopisecký
článek JCSS38(1989),150–164, DOI10.1016/0022-0000(89)90037-8;
konkrétní PDF této verze nezískáno. Obsahový závěr zde stojí na
primární dřívější verzi stejného autora, ne na sekundárním výkladu.
[Konferenční originál](https://cctbio.ece.umn.edu/wiki/images/3/3f/Barrington_Bounded-Width_Polynomial-Size_Branching_Programs_Recognize_Exactly_Those_Languages_in_NC1.pdf).

**Fletcher a Silver, Algorithm284.** Přečten celý algoritmus a jeho
skupinové vysvětlení v původním souboru *Collected Algorithms from
ACM*, svazekII, list284-P1-R1 (PDF111). Počet cyklů je gcd(m,n),
uvnitř se prochází posunem n. Veřejný přetisk zachovává autory,
data přijetí a celý kód; navazující primární poznámka Ita uvádí
přesnou citaci CACM9(5),květen1966,326. Jde o přetisk kódu, nikoli
předstíraný obraz samotné časopisecké326. Zvlášť přečtena Itova
poznámka na PDF111–112; její výklad reverzí není zdrojem nové chyby
TAOCP. Vlastní důkaz cyklů34 nevyžaduje správnost všech tvrzení
navazujícího článku.
[Primární soubor ACM](https://bitsavers.trailing-edge.com/pdf/acm/collected_algorithms_from_acm/Collected_Algorithms_from_ACM_Volume_2_Algorithms_221-492_1980.pdf).

**Jacques,Lenormand,Lentin,Perrot1968.** Celý třístránkový originál
s.A446–A448 byl přečten a vizuálně prohlédnut (PDF2–4). Věta1(ii)
dává sudou permutaci jako součin dvou permutací s jediným cyklem;
věta2 uvádí silnější komutátor n-cyklu s involucí. Přečteny definice,
propozice1–3 i induktivní důkaz na448. Přesná knižní citace souhlasí
s hlavičkami originálu. Webový nástroj na HAL vrátil zákaz přístupu,
ale obyčejné stažení stejné veřejné adresy úspěšně poskytlo skutečné
PDF s titulním listem HAL a skeny; stav je zaznamenán v metadatech.
[HAL, primární originál](https://hal.science/hal-01573916/document).

**Netto1892, §46.** Přečten celý §46 na s.49–50 v originálním překladu
F.N.Colea, včetně definice konjugace a důkazu přejmenováním cyklů;
obrazyPDF69–70 porovnány. Okolní §45 a koroláry§47 sloužily ke
kontrole konvence součinu. TitulPDF9 označuje autora,překladatele a
Register Publishing Company; rok1892 byl také vizuálně
potvrzen, ačkoli OCR jej chybně četlo1802. Uložený OCR soubor je úmyslně
omezen na prvních72 PDF stran, není označen za úplný přepis knihy.
[Archivní originál](https://archive.org/download/theoryofsubstitu00nett/theoryofsubstitu00nett.pdf).

## Konkrétní otevřené zdrojové body

- Herstein–Kaplansky, *Matters Mathematical*1974, §3.5: archivní
  záznam získán, ale PDF a OCR jsou ve výpůjčním archivu označeny
  private. Bez původních stránek se nová odpověď28 vede zdrojově
  partial; vlastní důkaz součinu je hotov. PDF odkaz „3.5 An
  Application“ z Wikipedie patří jiné knize *Concrete Abstractions*,
  proto nebyl použit jako zaměnitelný pramen.
- Shams2002: přesný vzorec je dokázán nezávisle. Hledání titulu
  *Formulating the Extended Josephus Problem* přivedlo k bývalé
  autorské adrese Manchesteru, která vrátila404. Samotné pozdější
  citace ani údaj v oficiálním erratu nejsou vydávány za čtení
  původních stran29–33 sborníku.
- Alpern1978,*Superhamiltonian graphs*: vydavatelský abstrakt a
  bibliografie potvrzují příslušné téma, svazek25 a strany62–73.
  Celý text i otevřený PDF odkaz vracely403. Přesný výskyt konstrukce
  pro cestu nebyl ověřen primárním plným textem; úloha32 zdrojově
  partial, vlastní obecný důkaz hotov.
- Mohammed–Subi1987,*An Improved Block-Interchange Algorithm*:
  bibliografická metadata souhlasí, ale původní článek113–121 nebyl
  získán. Sekundární shrnutí nenahrazuje ověření jeho varianty
  algoritmu. Proto úloha35 zdrojově partial, všechny uvedené
  knižní postupy včetně opravy2006 jsou matematicky ověřeny.

Získané soubory a metadata jsou v `../sources/permutation-remaining/`.
`downloads.json`, `access-extra.json` a `access-final.json` obsahují
URL, skutečné HTTP stavy, časy a SHA-256, včetně jasného rozlišení
PDF od chybových stránek. Žádný pramen nebyl publikován ani odeslán.
