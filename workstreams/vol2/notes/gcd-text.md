# §4.5.2: předpoklady a odvození v textu349–353

Navazuje na `gcd-model.md` a `gcd-research.md`. Původní stránky349–353
byly zobrazeny; zde doplňujeme kontrolu přechodů mezi již prověřenými
úlohami. Uzavření tohoto rozsahu neuzavírá úlohu32 o všech spojitých
řešeních a nepotvrzuje neprokázané předpoklady rozvojů jako věty.

## Funkce a rozsah předpokladů

G(x) je limitní pravděpodobnost, že poměr menšího a většího lichého
operandu je větší než x, pro0<=x<=1. Pro x>1 ji rozšiřujeme vztahem
G(1/x)=-G(x). Dále

```text
S(x)=sum_{k>=1} 2^-k G(1/(1+2^k x)),
rho(x)=G(1+x)=sum_{j>=1} rho_j x^j,
lambda=-rho_1=-G'(1)>0.
```

Morrisův výsledek dává existenci limitu a analytické pokračování G
na pravou polorovinu; převod je doložen v `gcd-research.md`.
Z toho plyne konvergence Taylorovy řady rho pro |x|<1.
Pozitivita hustoty dává monotonicitu G a S na kladné ose.
Dominovaná konvergence v definici S dává S(0+)=0,S(+infinity)=1;
pak G(0+)=1,G(1)=0,G(+infinity)=-1. Tyto vlastnosti odpovídají
obr.10; přesné souřadnice každého bodu tištěné křivky neměříme.

V(41)/(42) kniha **předpokládá** rozklad G a S na logaritmický člen,
obyčejnou mocninnou řadu a periodické členy cos(2pi m lg x),
sin(2pi m lg x), jejichž amplitudy jsou opět mocninné řady.
Z existence takových rozkladů pro konečné iterace sama o sobě
neplyne stejný rozklad limitu. Níže kontrolujeme odvozené identity
pod tímto výslovným předpokladem a při konvergenci dovolující
porovnat jednotlivé koeficienty a Fourierovy složky. Pouhá
konvergence každé jednotlivé amplitudy by ještě neospravedlnila
libovolné přeskupení nekonečného součtu přes m. Netvrdíme, že
Morrisova věta samostatně dokazuje všechny rozklady(41)/(42).

## Přechody(44)–(51)

Oddělení prvního členu a posun indexu v S dávají přesně

```text
2S(x)=G(1/(1+2x))+S(2x)=S(2x)-rho(2x).                 (A)
```

Logaritmickou amplitudu v S označme Lambda(x), aby se nepletla
s konstantou lambda. Protože lg(2x)=1+lg x a všechny periodické
faktory se po zdvojení x vrátí, dostáváme(45)–(47):

```text
2Lambda(x)=Lambda(2x),
2mu(x)=mu(2x)+Lambda(2x)-rho(2x),
2sigma_m(x)=sigma_m(2x), 2tau_m(x)=tau_m(2x).
```

Je-li analytická f(x)=sum f_j x^j a 2f(x)=f(2x), pak
(2-2^j)f_j=0: jediný možný člen je lineární. Koeficient x
ve druhé rovnici tedy určí Lambda(x)=rho_1 x=-lambda x.
Konstantní člen dává mu_0=0. Pro j>=2 dostáváme

```text
mu_j=rho_j/(1-2^(1-j)).
```

Koeficient mu_1 zůstává volný, přesně jak uvádí text.
Amplitudy sigma_m,tau_m jsou lineární. Koeficienty(49)/(60)
byly nezávisle numericky prověřeny jen v přesnosti popsané
v `gcd-model.md`, nikoli jako certifikát všech40 číslic.

## Přechody(52)–(57)

Dosadíme x<-1/(2x) do(A) a použijeme G(x)=S(1/x)-S(x):

```text
2S(1/(2x))=S(1/x)+G(x/(1+x)),
2G(2x)+2S(2x)=G(x)+S(x)+G(x/(1+x)).                  (B)
```

Logaritmickou amplitudu G označme alpha. V posledním členu je
lg(x/(1+x))=lg x-lg(1+x); druhý člen je analytický v nule.
Posunutí fáze periodických členů mění jejich analytické amplitudy,
ale nevytváří nový explicitní násobek lg x. Porovnání těchto
koeficientů v(B) dává přesně(54):

```text
2alpha(2x)-4lambda x=alpha(x)-lambda x+alpha(x/(1+x)). (C)
```

Samotná(C) neurčuje konstantní člen alpha_0. Omezenost G u nuly,
při uvedeném kontrolovaném rozkladu, však nutí alpha_0=0:
nenulové alpha_0 lg x by divergovalo, zatímco ostatní členy
jsou omezené. Koeficient x v(C) pak dává alpha_1=3lambda/2.
Pro každý další stupeň j má neznámý alpha_j nenulový
koeficient2^(j+1)-2; nižší koeficienty jej určují jednoznačně.

Funkce psi je definována rovnicí

```text
psi(z)=(z+psi(z/2)+psi(z/(2+z)))/2, psi(0)=0,psi'(0)=1.
```

Po dosazení z=2x jde právě o(C) pro alpha=(3lambda/2)psi.
Iterací této rovnice vznikají na hloubce k všechny argumenty
z/(2^k+jz),0<=j<2^k, každý s vahou2^-k. Příspěvky členů
z/2 ze všech hloubek jsou proto

```text
psi(z)=(z/2) sum_{k>=0} 2^-k sum_{j=0}^{2^k-1}1/(2^k+jz).
```

Pro |z|<=r<1 je |2^k+jz|>=2^k(1-r), takže celá řada
konverguje absolutně a stejnoměrně. Zbytek iterace je O(2^-k):
každý koncový argument je O(2^-k), psi(w)=O(w) u nuly,
a součet2^k vah2^-k je1. To dokazuje(57) a jednoznačnost
analytického řešení s danými počátečními údaji. Bernoulliho
koeficienty(58), jejich známá změna znamének2021 i odhad
Theta(j^-2) jsou již prověřeny v `gcd-model.md`.

## Pokles velikosti a empirické odhady(59)–(66)

Pro u>v>0 položíme X=v/u a Y=uv. Po odečtení a k posunech
je Y'=(u-v)v/2^k, tedy lg(Y/Y')=k-lg(1-X).
V modelu P(k=j)=2^-j pro j>=1, takže E[k]=2. Pro rostoucí
h(x)=-lg(1-x), h(0)=0, platí ocasová integrace
E[h(X)]=integral_0^1 h'(x)G(x)dx. Odtud

```text
b=E[lg(Y/Y')]=2+(1/ln2)integral_0^1 G(x)/(1-x)dx.
```

Integrál je konečný: u1 je G(x)=lambda(1-x)+O((1-x)^2),
u0 stačí G<=1. Při konečné rovnosti lichých operandů je
lg(uv)=2lg(gcd(u,v)); limit jeho střední hodnoty0.9779...
byl odvozen v `gcd-probability.md`. To ale samo o sobě není
důkaz, že lze počet kroků v původním algoritmu nahradit
počáteční velikostí dělenou b. Rigorózní vedoucí koeficienty
2/b a4/b plynou až z citované Morrisovy věty.

(62) je fit z milionů vstupů v uvedených konečných rozsazích;
tento původní experiment bez dat/seedu neopakujeme jako údajně
identickou reprodukci. Koeficienty m/2 a m pro pevný druhý
operand mají vlastní důkaz v úloze21. Při dosazení koeficientu2/b do tohoto empirického tvaru na
diagonále vyjde pro druhý rozměr2/b-1/2=0.205971...;
to vysvětluje náhradu0.203 za0.206 na353. Pro posuny je
analogická hodnota4/b-1=0.411942.... Nejde o samostatný
důkaz asymptotiky pro všechny podmíněné binární intervaly.

(64)/(65) jsou v kontextu přibližné empirické vztahy. Rigorózní
výsledky o vedoucím členu nepovažujeme za důkaz zbytku O(1)
ani konstant-0.5,-2.7. Navíc přesná váhová identita odpovědi22
vyžaduje počáteční posuny z C0123; jejich limit4/3 nemění
vedoucí koeficient, ale ovlivňuje konstantní člen.

Maximální počet odečtení(66) je dokázán v `gcd-basic.md`
a `gcd-extremal.md`. Pro rozměr n=0 lze použít dvojici
(2^(m+1)-1,1), pro m=n=0 dvojici(1,1); oba krajní případy
dávají max(m,n)+1. Tento výrok nelze zaměňovat s výrokem
o přesném nejhorším času MIX, jehož jednobitovou výjimku
eviduje C0117. V tomto doplňujícím algebraickém bloku nebyl
zjištěn další nový nález.
