# V3-C0011 — maximální zásobník quicksortu

Confirmed, low. Odpověď §5.2.2-20, s. 631 / file 642, má v čitateli
N+2 místo N+1. Pro M=1, N=4 je vytištěné maximum 1; skutečné je 0.

Q7 na s. 116 vloží položku jen tehdy, když obě části mají více než M
prvků. Jejich délky mají součet N−1. Pro N=2M+2 tedy nemohou být obě
alespoň M+1, a ani pozdější menší podúloha nic nevloží. Tištěný vzorec
však dává floor(lg((2M+4)/(M+2)))=1.

Obecně minimální velikost pro k současných položek splňuje
N_0=M+1, N_k=2N_(k−1)+1: pokračuje se menší částí a odložená část
je nejméně stejně velká. Proto N_k=2^k(M+2)−1. Vyvážené rozklady
mez dosahují, takže výsledek je max(0,floor(lg((N+1)/(M+2)))).
Věta v závorce v samotné odpovědi už uvádí toto správné N_k.

Sazba files 127 a 642 prohlédnuta. Pět vrstev errat je zachyceno v
sources/exchanging-errata-review.json. Historická err3-1e, s. 608,
10. 1. 1984 přidává max(0,…) a chybný N+2 opakuje; nejde o opravu
zde popsaného čitatele. Novější vrstvy jej neopravují. Nejde o chybu
řazení: údaj pouze někdy nadhodnocuje potřebnou kapacitu o jednu položku.
Prvenství ani fyzický výtisk neověřeny.
