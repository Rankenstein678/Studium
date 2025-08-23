$$
s(x,t) = A\cos(\omega t \pm kx+\varphi)
$$
A: Amplitude
$\omega$: Kreifrequenz der Schwingung an jedem Ort
$\frac\omega{2\pi}=f$: Anzahl SChwingungen pro Zeiteinheit
$\varphi$ : Phasenverschiebung
$\frac\varphi\omega$ Zeitverschiebung der Maxima
k : Wellenzahl
$\frac k{2\pi}$ : Anzahl SChwingungen pro Längeneinheit
$\frac \omega k$ : Phasengeschwindigkeit/Ausbreitungsgeschwindigkeit der Welle
$\lambda=\frac{2\pi\cdot v_p}\omega$ 
Alternativ aus den Materialkonstante
$$
c= \left( \frac{\omega}k \right)^2
$$
Für die Schallgeschwindigkeit gilt:
$$
v_p=\sqrt \frac1{\kappa\rho_0}
$$
Wasserwellen:
$$
v_p=\frac\lambda T=\sqrt{\frac{g\lambda}{2\pi}\cdot\tanh \left( \frac{2\pi x}\lambda \right)}
$$
g: Erdbeschleunigung, z: Wassertiefe

# Fourieranalyse
Komplexe schwingungen werden in summen harmonischer Umgewandelt ==Superpositionen==
$$
x(t)=\sum_{n=0}^\infty|A_n|\cdot e^{i(n\cdot\omega_0\cdot t + \varphi_n)}
$$
mit $\omega_0= \frac{2\pi}T$
Für die Amplitude gilt (Fourier-Transformation)
$$
A_n = |A_n|\cdot e^{i\varphi_n}=\frac 1T\int_0^Tx(t)\cdot e^{-in\omega_0}dt
$$
# Dispersion
Hängt die Phasengeschwindigkeit von der Frequenz ab, so nennt man die Dispersion

# 2/3D Wellen
Longitudinal schneller als transversal
Bei gleichzeitg beiden gilt
$$
d = \Delta T\cdot v_l\cdot v_t/(v_l-v_t)
$$
$$
A\cos(\omega t-k|x|+\varphi)
$$
mit $E\propto A^2$
Kreiswelle $A(\u x)=\frac\alpha{\sqrt{|\u x|}}$ $[\alpha]=m^{\frac32}$
Kugelwelle $A(\u x) = \frac\alpha{|\u x|}$ $[\alpha]=m^2$

# Stehende Welle
Überlagerung von rechts- und linkslaufender Welle in 1D mit gleicher Frequenz und Amplitude
-> stehende WElle
#### Bei Reflexion
- festes Ende: Amplitude immer null
- loses Ende: Wellenbauch
2 feste/lose Enden $L=n\cdot \lambda/2$ n>0
1festes & 1 loses $L = n\cdot \lambda/2 + \lambda/4$ n>=0


# Interferenz
Zwei Wellen aus der gleichen Richtung interferieren
$\varphi = 2\pi$ Konstruktiv
$\varphi = \pi$ Destruktiv
Gangunterschied in 3d

# Reflexion
Grenzfläche medien mit vreschiedenen Phasengeschwindigkeiten
![[Pasted image 20250822173511.png]]

# Beugung & Brechung
Prinzip von Hyugens
Jeder Punkt auf einer ausgedehnten Wellenfront in 2D/3D bildet eine Quelle einer neuen kreis bzw. kugelförmigen Welle (Elementarwelle)
Die resultierende neue Wellenfront ist die Überlagerung der erzeugten Elementarwellen
$$
\sin\alpha=\frac\lambda d
$$
![[Pasted image 20250822173848.png]]
Gesetz von Snellius
$$
\frac{\sin\alpha}{\sin\beta}=\frac{v_{p1}}{v_{p2}}
$$
