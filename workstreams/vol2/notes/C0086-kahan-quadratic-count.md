# V2-C0086: počet členů druhého řádu v Kahanově rozvoji

**Confirmed, drobná algebraická nepřesnost.** Odpověď§4.2.2-19,
str.615, řádek s „4n terms of 2nd order“. Hlavní mez po známé opravě
s_n−c_n je správná; tento nález nemění funkčnost metody.

Proměnné η_k,σ_k,γ_k,δ_k jsou relativní chyby čtyř operací zadání.
Odpověď definuje f_k jako koeficient x1 v s_k−c_k a g_k jako
koeficient x1 v c_k. Přesná rekurze v odpovědi je správná;
přímým rozepsáním z původních tří rovnic byla ověřena nezávisle.

Pro n2 je homogenní část f2 stupně2 rovna

```text
−η1γ1−γ1δ1−γ1σ1−δ1σ1
−γ2σ2−δ2σ2
+γ2γ1+γ2σ1−η2γ1−η2σ1.
```

Jde o deset různých nenulových monomů místo tištěných4n=8.
Obecně pro n>=2 je členů4n+2; pro n1 jsou čtyři. Dva dodatečné
členy souvisejí s g1=γ1+σ1+O(ε²), zatímco pro k>=2 je
g_k=σ_k+O(ε²). Oprava „O(n) terms of 2nd order“ by zachovala
zamýšlený argument bez nutnosti rozlišovat n1.

Původní strana615 vizuálně přečtena. Všechny čtyři vrstvy errat
a aktuální TeX prohledány2.11.2026 podle615,4n a formulace rozvoje;
opravy2003/2007/2021 mění cílový součet a doplňují ostřejší mez,
ale neupravují tento počet. Novější fyzický tisk a prvenství
neověřeny; zpráva nebyla odeslána.

Reprodukce: `verify_accuracy_compensation.py`, výsledek
`results/accuracy-compensation.json`. Přímá symbolická expanze pro
n1..8 dává4,10,14,18,22,26,30,34. Obecná rekurze a explicitní
platná mez zbytku jsou v `notes/accuracy-compensation.md`.
