# C0018 — přidaná úloha29(a), singletonová konvence

Candidate/low, nikoli confirmed. Přidaná úloha§5.1.3-29(a) je v
all3-prepre PDF6, `images/runs-errata-new28-29.png`; v první sazbě
knihy tento výrok není. Odkazuje na počty střídavých běhů z úlohy16.
Její odpověď na604/file615 výslovně zavádí Aalt(1,k)=δ_(k,0), G_1=1
(`images/multisets-file-615.png`).

Pro n1,k0 existuje jediná permutace a nemá vrchol: s_(1,0)=1.
Pravá strana29(a) je ale
`(1/2)Aalt(1,0)+Aalt(1,1)+(1/2)Aalt(1,2)=1/2`.
Pro n≥2 je(a) samostatně dokázána;29(b,c) platí i pro n1.

Možné řešení je dodat podmínku n≥2 k(a), případně výslovně použít
jinou singletonovou konvenci než formální základ rekurence16.
Právě rozdíl mezi formální a kombinatorickou konvencí brání označení
confirmed. Nespekuluje se o dopadu na běžné algoritmy nebo asymptotiky.

Převzata plná kontrola all3-prepre,all3-pre,all3,err3 a historické
err3-1e v `sources/runs-errata-review.json`. První vrstva obsahuje
zadání i odpověď29, ale žádná zahrnutá oprava nevymezuje n≥2 ani
nemění singletonovou konvenci16. Nejde o převzatou známou opravu.
V UI není nález připsán neexistujícímu místu v první sazbě knihy:
přesná lokace je přidaný text v erratech, logicky umístěný na47.
