# D152 — celá MPR50(a–e), doplnění P050

7. listopadu 2026. Zadání p16/file36, odpovědi
p377–378/file397–398 a autorův PS p16/file22,
p34/file40 byly přímo zobrazeny. P050 byl skutečně
znovuotevřen jako partial: starý důkaz obsahoval
normalizované indikátory a oba Jensenovy kroky,
ale ne každé podmínění s indexem J v(c,d), obecný
dovětek(a) a všechny nulové události. Jeho původní
poznámka je archivována v ledger history.

Přebíráme přesně argumenty z
`GENERAL_PROBABILITY_NOTES.md`, oddíl50, a úplné
momentové/nulové doplnění D096 v
`notes/sequential-mpr-004-005.md`. Všech6642 nenulových
tabulek,6 nulových případů a258 vynechaných nulových
marginál z `results/ross.json` zůstává beze změny
a bez opakování. Níže je souvislý důkaz každé části.

V celé zadané úloze je m≥1, Xⱼ∈{0,1}, X=∑ⱼXⱼ,
pⱼ=EXⱼ=P(Xⱼ=1), μ=EX=∑ⱼpⱼ. Index J je rovnoměrný
na {1,…,m} a nezávislý na celém vektoru(X₁,…,Xₘ).
Vzájemná nezávislost samotných Xⱼ se nepředpokládá.
Všechny proměnné potřebné pro(b–e) jsou omezené m.

## 50(a): každý bod a každá podmíněná váha

Definujme Uⱼ=Xⱼ/X tam, kde Xⱼ>0, jinak Uⱼ=0.
Je-li Xⱼ>0, je i X≥Xⱼ>0, takže skutečně použitý
podíl má kladný jmenovatel. Když X=0, jsou všechny
Xⱼ=0 a všechny Uⱼ=0. Když X>0, nulové Xⱼ nepřispívají,
a součet podílů je ∑ⱼXⱼ/X=1. Bodově proto

    ∑ⱼUⱼ=[X>0],
    P(X>0)=∑ⱼEUⱼ.

Uⱼ je0 mimo Aⱼ={Xⱼ>0} a 0≤Uⱼ≤1. Pro qⱼ=P(Aⱼ)>0
tedy podmíněný součet přesně dává

    EUⱼ=qⱼ E(Uⱼ|Aⱼ)
        =P(Xⱼ>0) E(Xⱼ/X|Xⱼ>0).

Pokud qⱼ=0, Uⱼ=0 skoro jistě a oba příspěvky jsou0;
zápis podmíněného poměru se chápe přes výše definované
Uⱼ. Autorova nulová konvence dává E(Uⱼ|Aⱼ)=EUⱼ=0.
Sečtením získáme celou zadanou identitu.

Tento důkaz, jak tvrdí tištěný dovětek, potřebuje jen
konečně mnoho nezáporných, konečných Xⱼ. Ani jejich
první momenty nemusejí být konečné, protože Uⱼ∈[0,1]
je vždy integrabilní. Binárnost v(a) nebyla použita.
Obě krajní větve X=0 a Xⱼ=0 jsou plně definovány.

## 50(b): každá rovnost a první Jensen

Pro binární Xⱼ máme Aⱼ={Xⱼ=1} a qⱼ=pⱼ. Při pⱼ>0
je na Aⱼ současně Xⱼ=1 a 1≤X≤m. Proto

    E(Xⱼ/X|Xⱼ>0)
       =E(Xⱼ/X|Xⱼ=1)
       =E(1/X|Xⱼ=1)
       ≥1/E(X|Xⱼ=1).

Poslední krok je Jensen pro h(t)=1/t na [1,m],
h″(t)=2/t³>0; oba podmíněné momenty jsou konečné.
Označme sⱼ=E(X|Xⱼ=1). Pro kladné pⱼ máme
1≤sⱼ≤m, takže násobení pⱼ a součet(a) dávají(24):

    P(X>0)≥∑ⱼ:pⱼ>0 pⱼ/sⱼ.                 (A)

Pokud pⱼ=0 a μ>0, autorova nulová konvence určuje
sⱼ=EX=μ>0, takže i nevynechaný tištěný člen je0.
Při μ=0 jsou všechna Xⱼ skoro jistě0 a pravděpodobnost
vlevo je0; v této samostatné větvi se žádné0/0 nepočítá.
To je přesně převzaté úplné doplnění D096.

## 50(c): náhodný index a všechny Bayesovy faktory

Události {J=j,Xⱼ=1} pro j=1,…,m jsou disjunktní
a jejich sjednocení je přesně {X_J=1}. Nezávislost J na vektoru dává

    P(J=j,Xⱼ=1)=P(J=j)P(Xⱼ=1)=pⱼ/m,
    P(X_J=1)=∑ⱼpⱼ/m=μ/m.

Je-li μ>0, je podmínění v další otázce kladné. Na
události J=j je X_J=Xⱼ, takže

    P(J=j|X_J=1)
      =P(J=j,Xⱼ=1)/P(X_J=1)
      =(pⱼ/m)/(μ/m)=pⱼ/μ.

Váhy jsou nezáporné a jejich součet je1. Při pⱼ=0
je konkrétní váha0 bez dalšího nulového dělení.
Při μ=0 je podmínění X_J=1 nulové. Podle autorovy
konvence(4) z D093 pak podmíněné rozdělení J zůstává
nepodmíněné, tedy každá hodnota má váhu1/m; poměr
pⱼ/μ se v této větvi nepoužije. Všechny obě vyžádané
pravděpodobnosti tak mají určený správný rozsah.

## 50(d): přesné podmínění s J a druhý moment

V zadání je tⱼ=E(X|J=j a X_J=1). Pro pⱼ>0 a libovolnou
hodnotu x proměnné X je

    P(X=x|J=j,X_J=1)
      =P(J=j,X=x,Xⱼ=1)/(pⱼ/m)
      =P(X=x,Xⱼ=1)/pⱼ
      =P(X=x|Xⱼ=1).

První rovnost využívá X_J=Xⱼ na J=j, druhá nezávislost
J na celém vektoru. Proto tⱼ=sⱼ, jak tvrdí tištěná
odpověď. Pro pⱼ=0 jsou obě události nulové a obě
očekávání jsou podle konvence EX=μ, takže rovnost
zůstává platná i tehdy.

Protože Xⱼ je indikátorem Aⱼ, dostáváme pro pⱼ>0

    pⱼtⱼ=E(X[Xⱼ=1])=E(XXⱼ).

Pro pⱼ=0 jsou opět obě strany0. Sečtení konečného
počtu členů dává každý krok požadované identity

    ∑ⱼpⱼtⱼ=E(X∑ⱼXⱼ)=E(X·X)=E X².

Takto je doplněn i mezikrok, který krátká tištěná
odpověď(d) výslovně nerozepisuje. Pro μ=0 je to
rovnost0=0, nikoli podíl.

## 50(e): všechny váhy druhého Jensena

Je-li μ>0, položme wⱼ=pⱼ/μ a ponechme kladné váhy.
Jejich součet je1; k nim příslušející tⱼ leží v [1,m].
Druhý Jensen pro1/t dává přesně tištěný krok

    ∑ⱼpⱼ/tⱼ = μ∑ⱼwⱼ/tⱼ
               ≥ μ/(∑ⱼwⱼtⱼ)
               = μ/(E X²/μ)=μ²/E X².

Poslední rovnost je právě(d). Jmenovatel E X² je
kladný, protože X≥0 a μ>0. Nulové váhy se buď
vynechají, nebo při autorově tⱼ=μ>0 přispějí0.
Při μ=0 je X=0 skoro jistě a P(X>0)=0 přímo;
žádná z mezí se nevyhodnocuje jako0/0.

Pro m=1 a p₁>0 je t₁=1, všechny tři hodnoty
P(X>0), podmíněná mez a druhá momentová mez jsou
p₁, zatímco J=1 jistě. To potvrzuje nejmenší povolený
rozměr. m=0 není součástí zadané uniformní volby J.
Případy pⱼ=1 nepůsobí výjimku: podmínění je jisté,
tⱼ=μ≥1 a všechny předchozí identity platí.

## Uzavření a bibliografie

Celé50(a–e) je nyní doložené v obnovené hloubce.
P050 může být znovu checked s přidaným D152 a se
zachováním původních důkazů, testů i historie otevření.
Žádný numerický nebo starý verifikační běh neproběhl.

PDF+PS a6errat+3TeX neobsahují použitelnou opravu50.
Vyhledaná oprava „plus na OR“ patří následující51,
nikoli tomuto důkazu; bude převzata jako známá oprava
při samostatné kontrole51. Nevytváří se z ní nový nález.

Bibliografická výjimka: přesná citace D. Aldous,
Discrete Math.76(1989),168, a historická věta o dlouhé
neznámosti identity(a) nebyly rychle ověřeny z původního
článku. Cílené hledání primárního vydavatele/autorského
webu neposkytlo tento obsah. Obecná matematická identita
je výše úplně dokázána; bibliografická výjimka ji neotevírá.

File397 je tímto celý reviewed s dřívějšími i nynější
výslovnými bibliografickými výjimkami. File398 má
doloženo pouze pokračování50(b–e);51–59 zůstávají
otevřené. Původní file36 zůstává partial pro51–57.
