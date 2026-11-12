# D131 — celá MPR29, Samuelsova dolní mez

6. listopadu 2026. Zadání p15/file35 a celá odpověď p375/file395
jsou přímo zobrazeny; shodná autorova sazba je v Pre-Fascicle5A,
p15/file21 a p31–32/file37–38. Níže jsou doloženy všechny tištěné
mezivýsledky, včetně indukčního konce a počtu změn znaménka.
Starých 5950 přesných nerovností a 28 symbolických derivací z P028
se přebírá bez opakování. Tento obecný důkaz na konečných testech nestojí.

## Vymezení a všechny přímé konce

Pro celé n≥1, 0≤m≤n, p∈[0,1] a np≤m+1 dokazujeme

    B_{m,n}(p) ≥ R_{m,n}(p),
    R_{m,n}(p) = ((1−p)(m+1)/(1+(1−p)m))^{n−m}.

B je binomická distribuční funkce z D125. Jmenovatel je vždy
alespoň1. Nultá mocnina znamená konstantu1, jako v konečných
pravděpodobnostních polynomech; při m=n tak nevzniká výjimka p=1.
Při m=0 jsou obě strany (1−p)^n; při m=n jsou obě1.
Pro případ prázdného součtu n=m=0 jsou rovněž obě1, aniž by se
použila některá z následujících formulí s dělením n.

Pro m=n−1 je B=1−p^n a R=n(1−p)/(n(1−p)+p). Kladný
jmenovatel je n−(n−1)p≥1. Rozdíl po jeho vynásobení je přesně

    (1−p^n)(n−(n−1)p)−n(1−p)
      = p−np^n+(n−1)p^{n+1}
      = p(1−p)(∑_{j=0}^{n−1}p^j−np^{n−1}) ≥ 0.

Poslední součet je nezáporný, neboť každý p^j≥p^{n−1};
oba vnější faktory jsou nezáporné. Faktorizační rovnost plyne
z (1−p)∑p^j=1−p^n, takže platí také pro p=1 bez dělení 1−p.
Pokrývá i překryv n=1,m=0. Pro p=0 jsou obecně obě strany1.
Pro p=1 a m<n jsou obě0; podmínka np≤m+1 zde navíc dovoluje
jen m=n−1. Pro m=n platí již předchozí konstantní větev.

Zbývá 1≤m<n−1, tedy d=n−m≥2, a 0<p≤p*=(m+1)/n<1.

## Pravý konec a přesná indukce

Použijeme indukci podle n, se všemi m současně. Základ n=1
byl vyřešen výše. Při daném n má indukční předpoklad rozsah
všech přípustných indexů pro n−1. Pro p*=(m+1)/n dostáváme

    1−p*=(d−1)/n,
    1+m(1−p*)=(n+m(d−1))/n=d(m+1)/n,
    R_{m,n}(p*)=((d−1)/d)^d.

Položme p̂=m/(n−1), což je v netriviální větvi v(0,1).
Vezmeme n−1 nezávislých bitů s parametrem p̂ a poslední bit
rovný1. Součet jejich parametrů je (n−1)p̂+1=m+1=np*.
Úplně dokázaná MPR28(c), D130, tedy dává

    B_{m,n}(p*) ≥ Pr(1+Bin(n−1,p̂)≤m)
                 = B_{m−1,n−1}(p̂).

Je to přesně tištěný součet: člen k=0 je0, ostatní členy
jsou binom(n−1,k−1)p̂^{k−1}(1−p̂)^{n−k}, k=1,…,m.
Nulový člen se chápe z distribuce, nikoli jako formální součin
nedefinované mocniny s nulovým binomickým koeficientem.
Index j=k−1 dává celou distribuční funkci vpravo.

Indukční podmínka je splněna na rovnosti:
(n−1)p̂=m=(m−1)+1. Její pravá strana má exponent d a základ

    ((1−p̂)m)/(1+(1−p̂)(m−1))
      = m(d−1)/((n−1)+(m−1)(d−1))
      = m(d−1)/(md)=(d−1)/d.

Zde m>0 opravňuje krácení. Proto
B_{m,n}(p*)≥((d−1)/d)^d=R_{m,n}(p*).
Nejde o kruhové použití právě dokazované nerovnosti se stejným n.

## Každý faktor derivace

Položme q=1−p, h=1+mq=m+1−mp a C=binom(n,m).
Pro Q=B−R již víme Q(0)=Q(1)=0 a Q(p*)≥0. D126 dokázal
obecnou derivaci B′=−d C p^m q^{d−1}, včetně zrušení obou
konečných součtů. Zde se přebírá právě tento rozsah.

Derivace R=(m+1)^d q^d h^{−d} je

    R′=(m+1)^d(−d q^{d−1}h^{−d}
                  +dm q^d h^{−d−1})
       =−d(m+1)^d q^{d−1}h^{−d−1},

protože h−mq=1. Odečtením dostáváme přesně tištěnou formuli

    Q′=d C q^{d−1}(A−F(p))/h^{d+1},
    A=(m+1)^d/C,
    F(p)=p^m h^{d+1}.

Vnitřní prefaktor je kladný na[0,1); v1 je0, protože d≥2.
Doslovná hodnota Q′(1) je tedy0. Tištěné „positive again at p=1“
vyjadřuje znaménko na konci intervalu, tedy v levém okolí1;
toto běžné kontextové čtení je přesně to, co další argument
používá. Není zapotřebí přisuzovat důkazu neplatný kladný
derivační údaj v samotném koncovém bodě ani zakládat nález.

## Striktní A>1 a celý průběh F

Počet binom(m+d,d)=C je počet slabých kompozic d do m+1 částí:
slovo s d nerozlišenými značkami a m přepážkami jednoznačně určí
kompozici, i s prázdnými částmi. Kompozice se rovněž jednoznačně
zobrazuje na neklesající slovo délky d nad abecedou0,…,m,
v němž se symbol i opakuje tolikrát, kolik je i-tá část.
Těchto slov je méně než všech (m+1)^d slov: při m≥1,d≥2
existuje například slovo začínající1,0, které neklesající není.
Tím je dokázáno C<(m+1)^d, a tedy A>1 bez odhadu faktoriálů.

Máme F(0)=0 a F(1)=1. Přímá derivace pro 0<p<1 dává

    F′=m p^{m−1}h^{d+1}−m(d+1)p^m h^d
       =m p^{m−1}h^d((m+1)−(n+1)p).

Všechny faktory mimo závorku jsou kladné. F tedy striktně roste
do c=(m+1)/(n+1) a striktně klesá od c do1.
Zbývá prokázat, že její vrchol překročí A; samotné slovo
„dramatically“ by tento fakt nedokládalo.

Kdyby F≤A všude, byla by Q′≥0 všude a Q′>0 v okolí0,
protože F(0)=0<A. Pak základní věta integrálního počtu dává
Q(1)−Q(0)=∫₀¹Q′(p)dp>0, spor s oběma nulovými konci.
Proto F(c)>A. Spojitost, striktní monotónnost, F(0)<A
a F(1)<A zaručují právě dva průsečíky

    0<u<c<v<1,       F(u)=F(v)=A.

Derivace Q je kladná na(0,u), záporná na(u,v) a kladná
na(v,1). Její nuly uvnitř(0,1) jsou právě u,v.
Existence záporné větve a jedinečnost obou změn jsou tím
úplně doloženy bez obrázku či numerického pokusu.

## Proč v požadovaném intervalu zbývá právě jedna změna

Pro v≤p<1 platí Q(p)=−∫_p^1Q′(t)dt<0, protože celý
integrand na(v,1) je kladný. Naproti tomu Q(p*)≥0 a p*<1,
proto nutně p*<v. Zároveň p*=(m+1)/n>c>u. Dostáváme

    0<u<c<p*<v<1.

Na[0,p*] tedy Q nejprve roste z Q(0)=0 do maxima v u
a potom klesá k nezápornému Q(p*). Na první části je nejmenší
hodnota Q(0), na druhé Q(p*); všude je tak Q≥0.
Tím je dokončena indukce a celá zadaná nerovnost pro np≤m+1.
Tištěné tvrzení o jediné změně znaménka na[0,p*] není
převzato bez důkazu ani odvozeno jen z hodnot na koncích.

## Bibliografie, errata a rozsah uzavření

Primární obsah čísla časopisu potvrzuje S. M. Samuels,
„On the Number of Successes in Independent Trials“,
Annals of Mathematical Statistics36(4), srpen1965,1272–1278:
[JSTOR, obsah čísla](https://www.jstor.org/stable/i312824).
Ověřeny jsou tyto bibliografické údaje, nikoli celý externí článek;
výše uvedený vlastní důkaz na jeho nepřečteném textu nezávisí.
Přesný rozsah je v sources/mpr029-bibliography.json.

Šest vrstev errat a tři TeX zdroje byly prohledány podle současné
i historické stránky, čísla29 a jména Samuels. Žádná oprava
tohoto tvrzení nebo důkazu nenalezena. Položka F5p229/answer29
se týká jiné sekce; nejde o MPR. Konkrétní hashe a kontexty
obsahuje results/sequential/mpr-029-samuels-errata.json.

D131 a MPR29 jsou checked/reviewed. P028 lze znovu uzavřít:
celý jeho původní rozsah28–29 nyní pokrývají D130 a D131,
včetně převzaté F016. Historie znovuotevření i staré úspěšné
výsledky zůstávají zachovány. Žádný nový nález, žádný výpočet
ani restart. File35 zůstává partial pro30–40; file395 pro30.
