Einfachstes Modell für Pontentialkurve gebundenener Teilchen: ==Parabel==
![[Pasted image 20250507142023.png]]
# Harmonischer Osillator
Modelll zur Beschreibung der Schwingung eines Teilchens, dass eine rückstellende Kraft verspürt, die Proportianal zur Auslenkung ist.

>[!important] Harrmonischer Ozillator
>$$
> E_{pot} = \frac 12 k_fx^2
>$$
>Mit:
>$k_f$ : Kraftkonstante (Stärke der Feder / Rückstellkraft) \[$Nm^{-1}$\]
>$x$ : Auslenkung \[m]
>
>Kreisfrequenz $\omega = \sqrt\frac{k_f}m$  
>Periodendauer $T = \frac{2\pi}{\omega}$
>Schwingungsfrequenz $\nu = \frac1{2\pi} \sqrt\frac{k_f}m$

Gesamtenergie des Systems ist konstant
$$
E = E_{kin} + E_{pot} = \frac 12mv^2 + \frac 12 k_fx^2 = const.
$$

>[!important] Rückstellkraft (Hooksches Gesetz)
>$$
>F = -k_fx
>$$

>[!important] Zusammenhang Energie und Kraft
>$$
>F = - \frac{\mathrm dE}{\mathrm dx}
>$$
>$$
>E = \int_a^bF(x)\mathrm dx
>$$
>oder wenn F const:
>$$
>E=F(b-a)
>$$

Aus dem 2. Newtonschen Axiom $F=m\frac{d^2x}{dt^2}= m\ddot x$ und dem Hookschen Gesetz folgt:
$$
 m\frac{d^2x}{dt^2}=- \frac{k_fx}{m}
$$
Dies ist sehr ähnlich zu schrödingergleichung des TiK.

Für Anfangsbedingungen $x (0) = x 0 und v (0) =0$ folgt
$$
x(t) = x_0\cos\omega t \qquad \omega =\sqrt\frac{k_f}{m}
$$
## Aufenhaltswarscheinloichkeit
- Je schneller Bewegung, desto kürzer Aufenthalt in Streckenstück
- Zeit für (kleine) Strecke $\Delta x : \Delta t \approx \frac 1v \Delta x$ (circa weil $\Delta$ und nicht $d$ also nur sekante und keine Tangente)
Es folgt
$$
P(x) \propto \frac1{v(x)}
$$
v folgt aus der Gesamtenergie des Systems
>[!important] Geschwindikeit harmonischer Oszillator
>$$
>v(x) = \sqrt{\frac{2E}{m}-\frac{k_f}{m}x^2}
>$$

# quantenmechanischer harmonischer Oszillator
Aus der klassischen Energie folgt der Hamilton Operator
$$
\hat H = -\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2} + \frac 12k_fx^2
$$
Für die Quantenzahl v folgt dann:
$$
\hat H \psi_v = E\psi_v
$$
![[Pasted image 20250507145228.png]]

Durch Substituion folgt:
$$
\left(-\frac{\hbar\omega}2\frac{d^2}{dy^2}+ \frac{\hbar\omega}{2}y^2 \right)\psi = E\psi
$$
Mit 
$$
y = \sqrt\frac{m\omega}{\hbar}x = \frac{x}{\sqrt[4]{\frac{\hbar^2}{mk_f}}}
$$
Es folgt die ==Transformierte Schrödingergleichung==
$$
\left(\frac{d^2}{dy^2} + y^2\right)\psi = \frac {2}{\hbar\omega}E\psi = \lambda<ßpsi
$$
Setzt man den Ansatz $\psi =e^{-ay^2}$ ein so ist diese Eine Lösung mit:
$$
\lambda = 2*a=1
$$
und 
$$
E_0 = \frac12\hbar\omega
$$
