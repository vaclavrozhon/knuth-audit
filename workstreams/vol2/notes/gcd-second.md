# §4.5.2-30: druhá iterace a všechny čtyři rozvoje

Rozsah: úloha30 na355 a odpověď644–645. Obě původní strany
vizuálně přečteny; definice dvojitých součtů, body derivací a fáze
Fourierových členů také ve zvětšených výřezech. Čtyři vrstvy errat
prohledány2026-11-02; relevantní oprava30 nenalezena.

## Přesné součty

G_1 je první spojitá iterace modelu z `gcd-model.md`, G_2 druhá.
Označme L=ln2, lg x=ln(x)/L. Pomocné funkce jsou pro x>0

```text
Sigma1(x)=sum_{k,l>=1}1/(2^(k+l) (1+2^l(1+2^k x))),
Sigma2(x)=sum_{k,l>=1}1/(2^k (1+2^l+2^k x)).
```

První koeficient je skutečně 2^(-k-l), bez dodatečné poloviny;
malá sazba byla ověřena zvětšením. Všechny členy jsou kladné
a součty konvergují. Dosazení G_1=f(x)-f(1/x) do operátoru
G_2 dává S_2(x)=1-Sigma1(x)-Sigma2(x), tedy

```text
G_2(x)=Sigma1(x)-Sigma1(1/x)+Sigma2(x)-Sigma2(1/x).
```

Záměny kladných součtů jsou dovoleny; následné rozdíly jsou konečné.

## Mellinovy transformace a správné body derivací

Pro komplexní s definujme

```text
a(s)=sum_{l>=1}4^-l (1+2^-l)^(s-1)
    =sum_{j>=0}binom(s-1,j)/(2^(j+2)-1),
b(s)=sum_{l>=1}(1+2^l)^(s-1), Re(s)<1,
    =sum_{j>=0}binom(s-1,j)/(2^(j+1-s)-1).
```

Mocniny kladných základů užívají reálný logaritmus. Funkce a je
celá: její první součet konverguje stejnoměrně na kompaktních
množinách s. Druhý součet pro b poskytuje meromorfní pokračování;
má jednoduché póly s=j+1+2pi i m/L, j>=0,m celé. Binomické
koeficienty v těchto definicích mají obvyklé polynomické pokračování
v horním argumentu. Pro 0<Re(s)<1 platí

```text
Mellin(Sigma1)(s)=pi a(s)/((2^(s+1)-1)sin(pi s)),
Mellin(Sigma2)(s)=pi b(s)/((2^(s+1)-1)sin(pi s)).
```

Odvození lze provést termínově stejnou transformací1/(1+x) jako
v úloze29. Nezávislá kontrola je přímý přepis

```text
Sigma1(x)=sum_l 4^-l/(1+2^-l) f(x/(1+2^-l)),
Sigma2(x)=sum_l 1/(1+2^l) f(x/(1+2^l)).
```

Pro libovolnou funkci h analytickou u -1 má integrand
pi h(s)x^-s/((2^(s+1)-1)sin(pi s)) v s=-1 reziduum

```text
x [h(-1)(lg x+1/2)-h'(-1)/L].                              (1)
```

Stačí položit e=s+1 a násobit h(-1)+e h'(-1),
pi/sin(pi s)=-1/e+O(e),
1/(2^e-1)=1/(Le)-1/2+O(e), x^-s=x(1-e ln x+O(e²)).
Tištěná a'(1) a b'(1) na645 proto musejí být a'(-1) a b'(-1).
Navíc b má v s=1 pól, takže b'(1) ani není konečná hodnota.
U a je a'(1)>a'(-1)>0 termínovým srovnáním kladných součtů;
ani první vadný člen není neškodná ekvivalentní hodnota. To je C0126.

## Úplné opravené rozvoje

Pro h=a nebo b označme

```text
F_h(t)=(1/L) sum_{m>=1} Re[
       (2pi i/sinh(2m pi²/L)) h(-1+2pi i m/L) exp(-2pi i m t)].
```

V knize je F_a=A a F_b=B. Pro 0<x<1 pak

```text
Sigma1(x)=a(0)+a(-1)x(lg x+1/2)-a'(-1)x/L+x F_a(lg x)
          -sum_{k>=2}2^(k-1)a(-k)(-x)^k/(2^(k-1)-1),
Sigma2(x)=b(0)+b(-1)x(lg x+1/2)-b'(-1)x/L+x F_b(lg x)
          -sum_{k>=2}2^(k-1)b(-k)(-x)^k/(2^(k-1)-1),
Sigma1(1/x)=-sum_{k>=1}a(k)(-x)^k/(2^(k+1)-1).
```

První dvě rovnosti lze získat i dosazením již dokázaného rozvoje
f z29 do výše uvedených jednoduchých součtů. Tím se obejde
potřeba nekontrolovaného zavření Mellinovy kontury. Třetí rovnost
plyne přímo geometrickým rozvojem: příslušný poměr má velikost
nejvýše3x/4. Všechny tři řady konvergují i při x=1. U první
stačí pozorovat

```text
sum_{k>=2}a(-k)=sum_{l>=1}2^-l/(1+2^-l)² < infinity.
```

U druhé b(-k)<=1/(2^(k+1)-1); u třetí
a(k)<=(1/3)(3/2)^(k-1). V nule se berou spojité limity.

Pro poslední rozvoj definujme pro celé k>=1

```text
bhat(k)=sum_{j=0}^{k-2}binom(k-1,j)/(2^(j+1-k)-1),
H_(k-1)=sum_{r=1}^{k-1}1/r,
P_k(t)=(1/L)sum_{m>=1}Re[
       (2pi i/sinh(2m pi²/L))
       binom(k-1-2pi i m/L,k-1) exp(-2pi i m t)].
```

Prázdné součty pro k=1 jsou nula. Fáze posledního exponenciálního
členu je v původní sazbě **záporná** a je správně; zvětšení
vyvrátilo podezření na opačnou fázi. Nyní pro 0<x<1 platí

```text
Sigma2(1/x)=sum_{k>=1}(-x)^k/(2^(k+1)-1) [
  lg x-bhat(k)-1/2-1/(2^(k+1)-1)+H_(k-1)/L+P_k(lg x)].      (2)
```

Kontrola reziduí: u s=k je
b(s)=-1/(L(s-k))+bhat(k)-1/2-H_(k-1)/L+O(s-k).
Záporné reziduum při posunu doprava pak dává právě neperiodickou
závorku v (2). U s=k-2pi i m/L je reziduum b rovno
-binom(k-1-2pi i m/L,k-1)/L; konjugované dvojice dávají P_k.

Konvergenci pro 0<x<1 lze ospravedlnit také bez kontury. Položme
Phi(y)=sum_{l>=1}1/(2^l+y) a P=P_1 z úlohy29. Její přesný vztah
odvozený z Phi(y)=1-f(1/y) je

```text
Phi(y)=(lg y-1/2+P(lg y))/y+1/(y(y+1))+Phi(1/y)/y².
Sigma2(1/x)=sum_{k>=1}2^-k Phi(1+2^k/x).
```

Rozvinutí logaritmu, racionálních členů a periodických komplexních
mocnin v x/2^k je absolutně konvergentní na kompaktních podintervalech
0<x<1. Zbývající geometrický součet má poměr nejvýše
x/(2-x)<1. Koeficienty jsou přesně stejné jako vypočtená rezidua.
Tím je (2) skutečná rovnost ve svém otevřeném oboru, nikoli pouze
formální nebo asymptotický rozvoj.

## Krajní bod x=1 a C0127

Současný obor všech čtyř rozvojů na645 je vytištěn jako 0<=x<=1.
Poslední řada (2) však při x=1 nesplňuje ani nutnou podmínku,
aby její jednotlivé členy šly k nule. Přeznačení r=k-1-j dává

```text
-bhat(k)=sum_{r=1}^{k-1}binom(k-1,r)/(1-2^-r)
        =2^(k-1)-1+E_k,
0<=E_k=sum_{r=1}^{k-1}binom(k-1,r)/(2^r-1)
      <=2((3/2)^(k-1)-1).
```

Proto `-bhat(k)/(2^(k+1)-1)->1/4`. Všechny ostatní členy
závorky v (2), dělené 2^(k+1)-1, jdou k nule. Pro P_k je třeba
uniformní, nikoli jen bodová mez. Při w=2pi m/L platí

```text
|binom(k-1-iw,k-1)|=prod_{r=1}^{k-1}sqrt(1+w²/r²)<=exp(pi w/2).
```

Logaritmus součinu je shora omezen integrálem klesající funkce
(1/2)ln(1+w²/t²) přes t>0; jeho hodnota je pi w/2. Odtud
|P_k(t)|<=(2pi/L)sum_{m>=1}exp(pi w_m/2)/sinh(pi w_m),
konečná konstanta nezávislá na k,t. Harmonické číslo H_(k-1)
roste pouze logaritmicky. Člen (2) při x=1 tedy je

```text
(-1)^k(1/4+o(1)).
```

Řada diverguje v běžném smyslu. Platí Abelův limit, tj. limita
součtu při x->1 zleva; původní dvojitý součet je konečný. Oprava
společného oboru na 0<x<1 (s uvedením spojitých limit) je dostatečná.
To je samostatný problém C0127; oprava bodů derivací jej neodstraní.

## Kontroly a rozsah

`verify_gcd_second.py` přesně kontroluje lokální reziduum a
binomické meze. Numerická část při75 desetinných místech počítá
všechny čtyři součty dvěma způsoby pro x=1/7,1/3,1/2: přímo
z definic a ze všech opravených členů rozvojů. Navíc aplikuje
původní operátor na G_1 v samostatném uspořádání. Používá240
dyadických členů,180 mocninných členů a14 Fourierových dvojic.
Výstup uvádí chyby jednotlivě; nejde o intervalový certifikát.
Hraniční členy pro k=10,20,40,80,160 doplňují obecný důkaz.

K potvrzení C0126/C0127 žádná numerika potřeba není. Oba checkpointy prošly, běh46419
(PID1146768) skončil exit0. Celá úloha30 je uzavřena jako confirmed; stav dalších
výzkumných úloh31–34 tím není předjímán.
