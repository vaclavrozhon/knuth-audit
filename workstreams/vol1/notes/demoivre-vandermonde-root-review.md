# §1.2.3–40: de Moivrovo druhé vydání1738

V1-X0743, 2. listopadu 2026. Celá původní úloha40 je checked.
Zbývající citace197–199 v druhém vydání The Doctrine of Chances
byla získána a přímo přečtena. Stávající matematický důkaz
v notes/matrices.md,oddíl2, ani úspěšné testy se neopakovaly.

Root ověřil10souborů zmrazeného MANIFEST-demoivre40.json,
SHA-256 `40cf5bd97c0e1b1b4d1273d3c2f505d1a7412ca69c0cbdf9e255d682e2d460c9`.
Přečetl celé předání a poznámku. Přímo obrazově porovnal
knižní zadání38,odpověď474,erratum all1-prepre31 a původní
titul i všechny tři citované stránky197–199. Čtyři obrazy
veřejného mikrofilmu jsou zachovány s přenosovými metadaty.
Nejde o náhradu jiným vydáním1718 nebo1756; titul přímo
potvrzuje druhé vydání,London1738. Poškozené číslo197
je určeno i sousedními198–199 a uloženou mapou mikrofilmu.

De Moivre197 vyjadřuje člen posloupnosti jako kombinaci
mocnin různých reálných kořenů. General Rule na198–199
určuje koeficient každé mocniny střídavým součtem počátečních
členů a symetrických součinů ostatních kořenů, děleným
součinem rozdílů. Symetrický součin stupně d zde znamená
součet součinů všech d-prvkových podmnožin zadaných kořenů.

Pro různé kořeny x_i a počáteční členy s_l,0<=l<n,
je koeficient c_i v s_l=sum_i c_i*x_i^l právě

```text
sum_(l=0)^(n-1) (-1)^(n-1-l) e_(n-1-l)(x_hat_i) s_l
-------------------------------------------------.
               product_(k!=i)(x_i-x_k)
```

Zde e_d(x_hat_i) je uvedený symetrický součin všech kořenů
kromě x_i a e_0=1. Je to inverze systému s exponenty0..n−1.
Knižní matice A má exponenty1..n: od předchozí matice V
se liší násobením i-tého sloupce hodnotou x_i. Tedy
A=V*diag(x_i) a A^(-1)=diag(1/x_i)*V^(-1). Odtud

```text
b_ij = (-1)^(n-j) e_(n-j)(x_hat_i)
       / (x_i product_(k!=i)(x_i-x_k))
     = (-1)^(j-1) e_(n-j)(x_hat_i)
       / (x_i product_(k!=i)(x_k-x_i)).
```

Souhlasí tedy faktor1/x_i i pořadí rozdílů v knize.
Inverze vyžaduje navzájem různé nenulové uzly. Rozšíření
na komplexní uzly plyne z již přijatého algebraického
důkazu; původnímu autorovi se nepřipisuje nevyřčená
komplexní ani pozdější maticová formulace.

Citaci přidalo známé erratum8.ledna2005. Čtyři vrstvy
errat jsou zachyceny ve sdíleném errata-extract.json;
starší opravy vysvětlení koeficientu zůstávají oddělené.
Nový nález není a jiné historické prameny1.2.3 zůstávají
otevřené podle ledgeru.
