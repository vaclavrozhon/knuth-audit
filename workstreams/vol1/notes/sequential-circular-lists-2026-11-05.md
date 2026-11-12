# Souvislý průchod §2.2.4 — 5. listopadu 2026

Přímo přečteny celé originály 273–280 a 551–553, všechny obecné
důkazy v `parallel/circular-lists/NOTES.md` a přijaté výsledky.
Přezkoušeny invarianty a algebra; dřívější úspěšné MIX běhy ani
kombinatorické kontroly se neopakovaly. Všechny čtyři aktuální vrstvy
errat mají nový výpis s hashi v `sources/sequential-2026-11-05/`.

## Seznamy a reprezentace

Vložení rozděluje jednu hranu cyklu, odebrání ji obnovuje. Prázdný
seznam a odebrání singletonu jsou správně ošetřeny na 274; záměrně
neúplné operace na 273 nejsou novým nálezem. Výměna AVAIL s jedním
odkazem rozstřihne cyklus na přesně všechny uvolněné uzly následované
původním volným seznamem. Zřetězení dvou disjunktních cyklů zachovává
pořadí; výměna dvou hran téhož cyklu jej naopak rozdělí. Shodné
ukazatele jsou samostatný správný případ.

Pevná hlava řeší prázdný zásobník. Pohyblivá hlava z náhrady 2021
zachovává i pravé vložení: stará hlava dostane hodnotu, nová prázdná
hlava se vloží za ni. Původní úloha 4 a její odpověď jsou správné;
náhrada není nová úloha ani chyba původního zásobníku. Omezení věty
o ztrátě pravého vložení na pevnou hlavu je obsahová oprava na 275.

Obrácení odpovědi 5 nejprve přeruší hranu startu a po n průchodech
se do startu vrátí. Ještě jeden průchod zpracuje jeho dočasný null
a uzavře obrácený cyklus. Platí pro singleton i prázdný seznam.
XOR a modulární součet/rozdíl v odpovědi 18 mají algebraické inverze
ze známého souseda; u rozdílu se uchovává směr. Dvě hlavy poskytnou
počáteční sousední dvojici i u prázdného seznamu. Kniha nepřisuzuje
konkrétní historické prvenství; její přiznaná neznalost původu není
naše nezávislé tvrzení, že původ nelze zjistit.

## Polynomy a programy

Konvoluce na 275 ruší vnitřní koeficienty podle
(i+1)−2i+(i−1)=0 a nechává právě x^6−6xy^5+5y^6. Obraz na 276
i oba obrazy odpovědi 6 odpovídají znaménku, koeficientu, exponentům
a odkazům. Zabalení e=A b²+B b+C zachovává pořadí; sentinel −1
je jediný záporný exponent. Jednorozměrná substituce v odpovědi 10
je správná při uvedených hranicích všech mezivýsledků.

Slučovací invariant A rozděluje Q na hotový prefix a nedotčený
suffix. Každá větev spotřebuje alespoň jeden term; sentinel ukončí
oba průchody na původních hlavách. Nulový součet se vrací do AVAIL.
M přičítá postupně posunuté násobky P, se zachovaným sentinelem;
indukce po termech M dává Q_initial+P_initial*M_initial.
Tato základní analýza používá oddělený výstup; aliasy řeší úloha 9.

Fig. 10 souhlasí se všemi větvemi A. Její přesun v erratu 2024
nemění obsah a nepředstavuje vadu obrázku. Přesné počty instrukcí
Programu A dávají 27m′+18m″+27p′+8q′+13. Maximum živých uzlů
je 2+p+q plus maximum prefixového rozdílu vložení−zrušení, mezi
0 a p′. Tím jsou doloženy obě paměťové meze bez měření.

COPY kopíruje p+1 uzlů včetně hlavy, čas 21p+31. ZERO má 18u,
ERASE 11u a přijímá i nulový polynom s vlastní hlavou. Známá oprava
odpovědi 12 dává ZERO+ADD=27p+31 a limitní poměr 7/9, přibližně
78 %. Pro malé p nejde o pevný poměr. MULT obnovuje tři switche
i požadované ukazatele; není deklarován jako reentrantní.
OVERFLOW musí zachovat živé registry a vrátit se na rJ−2.
Vlastní alternativní programy mají jiné, odděleně evidované konstanty.

## Dva potvrzené nálezy

**C0037, pouze odpověď 9 na 552:** P=Q=1, oddělené M=−1,
AVAIL=null. Jediný term se v A3 vynuluje, A4 jej vrátí do AVAIL
a přepíše LINK na null. Následující posun P přečte tento nový
odkaz místo původní hlavy. Žádná alokace ani timeout nejsou potřeba
k doložení porušení invariantu. Oprava pořadí Q/LINK(Q1) z 2022
se posunu P netýká. Odpověď musí vyloučit konstantní term M=−1,
analogicky k již uvedené výjimce pro M=Q. Případ nulového P
je neškodný. Ostatní jednotlivé aliasy mají uvedené obecné důkazy;
nezaměňujeme je za tvrzení o souběžném P=M=Q.

**C0038, pouze druhý časový vzorec na 553:** první přesný vzorec
21pr+38r+29+27Σm′+18Σm″+27Σp′+8Σq′ je správný. Při tištěných
předpokladech se jeho suma rovná
4αpr²+39pr+5αpr+8q′₀r+38r+29, nikoli výrazu s 40pr+4αpr.
Rozdíl je (1−α)pr. Pro P=x+1, Q=x, M=1 je p=2, r=1, α=1/2,
q′₀=0: přesně 154u proti tištěným 155u. Jde o algebraickou chybu,
nikoli o spor o heuristiku α. Doporučení menšího násobitele je
podmíněným vodítkem této analýzy, ne větou o každém vstupu.

Oba nálezy byly znovu porovnány s originálem a čtyřmi vrstvami
errat. Jejich potvrzení není tvrzením prvenství ani kontrolou
fyzického výtisku. Nový neznámý nález tento blok nepřidal.

## Prameny a stránkové uzavření

Přímo přečtené originály IPL-V P-1918, strany 46–47, dokládají
oba triky bez známého předchůdce včetně potíže s posledním uzlem.
Ověřují použití v IPL-V, nikoli prvenství v celé řadě IPL.
Xieho atribuce je přímo v autorově erratu. Odkaz 5.2.3-29 skutečně
vede na Brownovu úlohu na straně 157 svazku 3. Slučování r proudů
pomocí haldy dává O(pr log(r+1)+q), takže odkaz má technický obsah;
tím není proveden celý audit oné úlohy ve svazku 3.

Všech 18 úloh a hlavní text zůstávají uzavřené v zaznamenaném
rozsahu. Celé 273–280 a 551–552 mají stránkové pokrytí, včetně
již zkontrolovaného konce §2.2.3 na sdílených stranách. Na 280
jsou ověřeny i úvodní diagramy dvojitých seznamů a identita (3).
Na 553 je zatím uzavřena část §2.2.4; následující odpověď §2.2.5-1
se sloučí s dalším blokem. Pokračuje §2.2.5 na 281.
