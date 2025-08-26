# Harmonische
$$
\ddot x = -ax
$$
Allgemeine Lösung
$$
x(t) = A\cdot \cos(\omega_0 t + \phi)
$$
![[Pasted image 20250821171951.png]]
mit
$$
\omega_0 = \sqrt{\frac{D}m}
$$
$$
T= \frac{2\pi}{\omega_0}
$$

$$
E_{Ges}\propto A^2
$$
## Beispiele
### Pendel
$$
\alpha(t) = \alpha_0\cos(\sqrt{\frac gl}t)
$$
$$
v=\alpha_0\cdot\omega\cdot L
$$
### Längsschwingungen
$$
x(t) =A\cos(\sqrt{\frac{E\cdot A}{m\cdot l}t+\varphi})
$$
### Balkenschwingung
D: dicke
rho: dichte
$$
\omega_0 = \sqrt{\frac{ED^2}{2L^4\rho}}
$$
# Gedämpfte
$\alpha$ Dämpfunkoeffizinet
$\gamma= \frac\alpha{2m}$ Dämpfungskonstante
Allgemein
$$
x(t)=A\cdot e^{-\gamma t}\cdot\cos(\sqrt{\omega-\gamma^2}\cdot t+\varphi)
$$
Eponentielle Dämpfung der Amplitude
Die Frequenz ist gegenüber dem ungedämpften Pendel verringert $\omega=\sqrt{\omega^2-\gamma^2}$
# Erzwungene
$$
x(t)=A\cdot e^{-\gamma t}\cdot\cos(\sqrt{\omega-\gamma^2}\cdot t+\varphi) + |B|\cdot\cos(\omega_At+\beta)
$$
Mit 
Amplitude
$$
|B| = \frac{F_A}{m\cdot\sqrt{(\omega_0^2-\omega_A^2)^2+(2\gamma\omega_A)^2}}
$$
Phasenverschiebung
$$
\beta=\arctan \left(\frac{2\gamma\omega_A}{\omega_A^2-\omega_0^2}  \right)
$$
Vorderer Teil: homogener Teil
HInterer: inhomogener Teil
Nach Einschwingzeit bleibt lediglich inhomogener Teil

# Gekoppelte SChwingungen
- Energieaustausch: Schwinger 1 überträgt Schwingungsenergie an Schwinger 2
- Eigenschwingungen: Schwinger schwingen, ohne Energie auszutauschen
- Schwebungsfrequenz: Frequenz, mit der die Energie zwischen den Schwingern ausgetauscht wird


Generell bei mehreren gekoppelten Pendeln:
- 2 gekoppelte Schwinger haben 2 Eigenschwingungen, bei denen keine Energie zwischen den Schwingern ausgetauscht wird
- Eine Eigenschwingung mit Eigenfrequenz ω+ ist langsam und die Schwinger schwingen im Gleichtakt, die andere Eigenschwingung mit Eigenfrequenz $\omega_−$ ist schnell und die Schwinger schwingen im Gegentakt
- Jede allgemeine Schwingung der beiden Schwinger lässt sich durch Addition/Subtraktion der Eigenschwingungen mit spezifischen Amplituden und Phasen A+, A−, ϕ+, ϕ− darstellen
- Die allgemeine Schwingung hat für beide Pendel einen Anteil, bei dem die Amplitude beider Schwingungen oszilliert und zwar im Gegentakt (Energieaustausch), und einen Anteil mit konstanter Amplitude (kein Energieaustausch) im Gleichtakt
![[Pasted image 20250821192748.png]]
![[Pasted image 20250821192849.png]]

Bei angeregter Kopplung ![[Pasted image 20250821193041.png]]
Resonanz bei jeder Eigenfrequenz