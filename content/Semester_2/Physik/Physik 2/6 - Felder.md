# Mawell
##  integraldarstellung 1. und 3. Maxwellgelichugn
1.
$$
\iint\u E_{ge}(\u r)d\u A = \frac{Q_{eingeschlossen}}{\varepsilon\varepsilon_0}
$$
3.
$$
\oint \u B_{ges}(\u r)ds = \mu\mu_0\cdot I_{eingeschlossen,\perp} 
$$
## Differenzielle Darstellung
Mit Ladungsdichte $\rho(\u r)$
$$
\nabla\cdot \u E(\u r)=\frac{\rho_{\u r}}{\varepsilon\varepsilon_0}
$$
![[Pasted image 20250823155007.png]]
3.
Mit Stromdichte j
$$
j(r) = \rho(r) · v(r) 
$$
$$
\u\nabla\times\u B(\u r)=\mu\mu_0\cdot\u j(\u r)
$$
![[Pasted image 20250823155159.png]]
## 2. und 4. Mawellgleichung
$$
\u \nabla\cdot\u B(\u r)=0 \iff \o \iint\u B(\u r)d\u A=0
$$
![[Pasted image 20250823155629.png]]
4.
![[Pasted image 20250823155704.png]]
![[Pasted image 20250823155718.png]]
![[Pasted image 20250823155728.png]]
Richtung des erzeugten Feldes
$$
	\dot{\u E}(t) = \lim_{\Delta t\rightarrow0}\frac{\u E(t+\Delta t/2)-\u E(t-\Delta t/2)}{\Delta t}
$$
![[Pasted image 20250823155939.png]]
## Alle 4
![[Pasted image 20250823155958.png]]
# Induktion
$$
U = |\u E| \cdot 2\pi r=-\pi r^2\cdot\ddt{|\u B|}t
$$
- UInd besteht nur so lange, wie sich B in der Schleife zeitlich ändert, d.h. der Magnet bewegt wird
- kann auch die Leiterschleife bewegen und den Magnet festhalten
- Dreht man die Leiterschleife im konstante B-Feld so erhält man
$$
U_{Ind}(t)=-\dot\Phi_m(t)\quad [\Phi_m] = Tm^2=Vs
$$
$\Phi_m$ heißt magnetischer Fluß durch eine Fläche und misst die Magnetfeldkomponente senkrecht zur Fläche über die Fläche aufintegriert
$$
\Phi_m =\iint \u B(\u x)d\u A
$$
- Lenzsche Regel: Induktion wirkt bremsend auf die B-Feld änderung
### Induktionsspannung in der Schleife
$$
U=|\u B| A\omega\cdot\sin(\omega t)
$$
# Selbstinduktion
Insbesondere beim Aus- und Einschalten des Stroms in einem Leiter entsteht eine Stromänderung die ein sich änderndes B-Feld zur Folge hat, das seinerseits eine Spannung im Leiter induziert.
Abhängig von ==Induktivität L==

## In der Spule
$$
U = - N\pi r^2|\dot{\u B}|= -N\pi r^2\mu_0\cdot n\cdot \dot I(t)
$$
mit  Windungsdichte n; WIndungszahl N

$$
U_{ind} = −L \cdot \dot I \quad [L] = 1 H(Henry) = 1 \frac{Vs}A
$$
$$
L_{Spule} = \mu_0\cdot n\cdot N\cdot \pi r^2
$$

### Stom nach ABschalten des Stroms
$$
I(t) = I_0\cdot \exp(-\frac RL t)
$$
# EM-Wellen
Wellengleichung
![[Pasted image 20250823161741.png]]
![[Pasted image 20250823161758.png]]
- Vektor $\u k$ heißt Wellenvektor und zeigt in die Ausbreitungsrichtung der Welle
- Die Vektoren E, B und k stehen senkrecht aufeinander, die Welle ist also transversal
![[Pasted image 20250823161916.png]]
![[Pasted image 20250823161939.png]]