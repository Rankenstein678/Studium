Parallel in die gleiche Richtung bewegte gleichnamige Ladungen ziehen sihc an
$$
|\u F_{\u B}| = \frac{\mu_0}{4\pi}\cdot\frac{q_1v_1\cdot q_2v_2}{r_{12}^2}
$$
Mit Vakuumpermeabilität $\mu_0$
$$
\mu_0 = 4\pi\cdot10^{-7}\frac{Ns^2}{C^2}
$$
Die magnetische und die elektrische Kraft sind exakt gleich stark, wenn sich beide Ladungenparallel mit der Lichtgeschwindigkeit bewegen. Dies deutet an, dass beide Kräf-te Erscheinungsformen derselben Wechselwirkung sind, der so genannten elektromagnetischenWechselwirkung. Die Lichtgeschwindigkeit lässt sich außerdem durch die elektrische und die magnetische Konstante ausdrücken 
$$
v=\frac1{\sqrt{\varepsilon_0\mu_0}}
$$
# B-Feld
$$
|\u B| = \frac{\u F_{\u B}}{q_2v_2}= \frac{\mu_0}{4\pi}\cdot\frac{q_1v_1}{r_{12}^2}
$$
\[B\] = T (Tesla) = $\frac{Ns}{Cm}$
$$
\u B(r) =  \frac{\mu_0}{4\pi \cdot |\u r_{12}|^2}\cdot \left( q\cdot \u v\times\frac{\u r}{|\u r|} \right)
$$
Linke Hand Regel:
Dauem: Ladung, Zeige: Richtung zum Messpunkt; Mitte: B-Feld
Entweder nach Superpositionsprinzip oder dreifachintegral
$$
B_ges = \iiint   \frac{\mu_0}{4\pi \cdot |\u r-\u x|^2}\cdot \left( \rho(\u x)\cdot \u v\times\frac{\u r-x}{|\u r-x|} \right)d^3\u x

$$

## Unendlich langer Stromdurchflossener Leiter
$$
B_{ges}(\u r^\prime)=\frac{\mu_0I}{2\pi y}
$$
y: Kürzester Abstand zur Drahtachse
$$
\u B_{ges}=\frac{\mu_0}{2\pi |\u r_\perp|}\cdot \left( \u I\times \hat r_\perp \right)
$$
$r_{perp}$ Vektor zur Drahtachse
Rechte hand (daumen + kreis regel)

# Leiterschleife
- Außerhalb der Leiterschleife ist B(r) identisch zum E(r)-Feld eines elektrischen Dipols
- Innerhalb der Leiterschleife zeigt das B(r)-Feld in die umgekehrte Richtung wie das E(r)-Feld eines elektrischen Dipols
Dennoch spricht man bei B(r)-Feldern, die durch Kreisströme erzeugt werden, von magnetischen Dipolfeldern mit dem magnetischen Dipolmoment
$$
|p_m|=I\cdot A_{eingeschlossen} \quad [p_m]= Am^2
$$
![[Pasted image 20250822203857.png]]

# unendliche Spule
n: Windungsdichte
$$
|B| = \mu_0\cdot n\cdot I
$$
![[Pasted image 20250822204147.png]]
Bei unendlicher Spule exakt mit Außenraum 0T
# B-Feld einer Toroidspule
![[Pasted image 20250822204259.png]]
$$
|\u B| = \frac{\mu_0\cdot N\cdot I}{2\pi\cdot r}
$$
# Permanentmagnete
Bei parallen Spins aller Teilche:
ferromagnetismus -> B-Feld
antiparrallel
antiferromagnetiscmus -> kein B Feld

Formal mikroskopische Kreisstöme
Im Stabmagnet
$$
|\u B| \propto \frac 1{|r|^3}
$$
![[Pasted image 20250822204653.png]]
# Magnetische Ladungen
Keine Monopole
Es gibt keine Start-und Endpunkte der B-Feldlinien


# Wirkung von B-Feldern
## Wirkung auf bewegte Ladungen
Lorentzkraft
$$
\u F_L = q\cdot \u v\times\u B
$$
Um ein Bfeld kreisende Ladung
$$
-\u\omega=\frac qm\cdot\u B
$$
### Lorentzkraft auf stromdurchflossenen Leiter
$$
\u F_B=L\cdot(\u I\times\u B)
$$
### Lorentzkraft nicht senkrecht
Nur senkrechte Komponente > spiralbahn:
Für den radius gilt
$$
r=\frac{m|\u v_\perp|}{q|\u B|}
$$
### Wirkung des B-Feldes auf magnetische Dipole
$$
\u D=\u p_m\times \u B
$$
# Materialien im B-Feld
- Es gibt keine Magnetischen Ladungen, also auch keine Magnetischen Metalle
- In Richtung $\u B$ ausgerichtete Dipole verstärken das B-Feld anstatt es wie beim E-Feld zu abzuschwächen
Folgende Materialien werden unterschieden
- Diamagneten: Materialien ohne atomare Dipole. In diesen Materialien werden durch das äußere B-Feld Kreisströme erzeugt, die das äußere Feld abschwächen
- Paramagneten: Materialien mit atomaren Dipolen. In diesen werden die Dipole durch das äußere B-Feld ausgerichtet. Sie verstärken das äußere B-Feld.
- Ferromagneten: Materialien, in denen die Dipole durch die Austauschwechselwirkung bereits parallel zueinander ausgerichtet sind (auch ohne ein äußeres B-Feld).
## Paramagneten
$$
\u B_{Dipol}\propto\u B_{Materie}
$$
$$
B_{mat}= (1+\chi_m)\cdot \u B_{ext}
$$
$$
\mu = 1+ \chi_m
$$
$\chi_m$ heißt magnetische Suszeptibilität, μ heißt magnetische Permeabilität
![[Pasted image 20250823012627.png]]
Die Stärke des DIpolfeldes ist Temperaturabhänigg (je kleiner T desto größer die Suszeptibilität)
![[Pasted image 20250823012038.png]]
$$
\u B_{Sättigung}=\frac{\mu_0\cdot n\cdot p^2_{m,Atom}}3
$$
n: Dichte der Dipole
## Einführung des H-Feldes
Für unabhänigkeit von $\mu$
$$
\u H(\u x)=\frac{\u B(\u x)}{\mu(\u x)\mu_0}
$$
$[H]=\frac Am$

## Diamagneten
Diamagneten sind Materialien ohne permanente Dipole pm. Beim Diamagnetismus wird ein magnetischer Dipol erst beim Anlegen von $B_{ext}$ induziert
- Diamagnetismus hängt nicht von der Temperatur ab
- Diamagnetismus gibt es bei allen Materialien. Er wird aber bei pm,Atom 6 = 0 zumeist vom stärkeren Paramagnetismus überdeckt
## Ferromagneten
Bei Anlegen eines äußeren Magnetfeldes Bext gilt für das B-Feld in der Materie wiederum
$$
\u B_{Mat}=\u B_{ext}+\u B_{Dipole} = \u B_{ext} + \mu_0\cdot \u M
$$
Mit Magnetisierung M $[M]=\frac Am$ als Maß für die dichte N der Ausgerichteten Dipole
$$
\u M = n_{Dipole}\cdot \u p_{m,Atom}
$$
Einzelne ausgerichtete Bereichen: magnetische Domänen
![[Pasted image 20250823153621.png]]
Bei äußerem B-Feld hängt Magnetisierung auch vom Anfangszustand ab
-> Hysterese
![[Pasted image 20250823153736.png]]

Bei kleinem B-Feld
$$
\u M = \frac{\chi_m}{\mu_0}\cdot \u B_{ext}
$$
Oberhalb der ==Curie Temperatur== verliert ein Magnet durch die Entropie seine Remanz. Oberhalb von Tc : Paramagnet