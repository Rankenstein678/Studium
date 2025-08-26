	# Wellen in der Materie
$$
v_{p, mat} \approx \frac{v_{vac}}{\sqrt{\mu\varepsilon}}

$$
Überall außer Ferromagneten
$$
v_{p, mat} \approx \frac{v_{vac}}{\sqrt\varepsilon}
$$
Die Dielektrizitätszahl ε hängt dabei zusätzlich von der Frequenz der elektromagnetischen Welle ab
$$
\varepsilon(\omega) = 1+\frac{n_e\cdot e^2/(\varepsilon_0\cdot m)}{\omega_0^2-\omega^2+i\gamma\omega}
$$
Dabei bezeichnet ne: Elektronendichte, m: Elektronenmasse, γ: Dämpfungskonstante der Elektronen und ω0: Eigenfrequenz der Elektronen
![[Pasted image 20250823165056.png]]![[Pasted image 20250823165124.png]]
![[Pasted image 20250823165317.png]]

![[Pasted image 20250823164429.png]]
# intensitätsabfall bei sichtbaren Licht
$$
	p= I_0\cdot 4\pi s^2
$$

# Optische INstrumente
## Linsen
- kleines $n_1\approx (1\ldots2)$ im relvanten $\omega$ Bereich -> Wenig Reflexion aber Brechung
- Materialien von Linsen für den sichtbaren Bereich sind zumeist Gläser
- Es gibt mehrere Bauformen von Linsen: Konvex (Wölbung nach außen), konkav (Wölbung nach innen), plan (eben) sowie Mischformen.
## Spiegel
- Spiegel haben ein großes n1 im interessanten ω-Bereich ⇒ fast vollständige Reflexion
- Materialien für Spiegel für den sichtbaren Bereich sind häufig Ag-Schichten
- Bei Spiegeln gibt es drei Bauformen: Plane Spiegel, konvexe Spiegel (nach außen gewölbt) und konkave Spiegel (nach innen gewölbt).
Sowohl bei Linsen als auch bei Spiegeln sollte n2 möglichst klein sein, um Absorptionsverluste des Lichts zu vermeiden

## Planare Elemente
### Ebene Spiegel
- Einfallswinkel = Ausfallswinkel
- Erzeugen umgekehrte gleich große Abbildung
 ![[Pasted image 20250823165730.png]]

### Ebenes Glasplättchen: Phasenschieber
- Phasenverschiebung im Vergleich zum Vakuum
![[Pasted image 20250823165843.png]]
### Interferenzfilter
Ein Interferenzfilter wird dazu verwendet, um Licht nur mit einer bestimmten Wellenlänge λ durchzulassen.
Beispiel: 2 parallele Halbdurchlässige Spiegel (90% Reflexion)
Das Interferenzfilter bildet damit einen Resonator für die Lichtwelle
$$
d=m\frac\lambda 2 \quad m\in\mathbb N
$$
Der Filter lässt Licht nur dann durch, wenn die entsprechende Lichtwellenlänge die Resonanzbedingung erfüllt.
![[Pasted image 20250823170118.png]]
## Gekrümmte Bauelemente
Jeder Objektpunkt Q wird auf einen Bildpunkt D mit Breite B abgebildet. An diesem ist die INtensität des Lichts am stärksten (Kugelwelleninterferenz oder gleichphasiges Licht, da alle Lichtstrahlen gleihc lange brauchen)
### Sammellinse
Form
$$
y^2 − y^2_0 = \pm2Rx
$$
$$
B\approx\frac\lambda{2\sin(\theta)}
$$
Theta: Halber Öffnungswinkel
### Brennpunkt
Punkt F, wo sich parrallel einfallende Lichtstrahlen treffen
![[Pasted image 20250823170727.png]]
Die optische Achse ist dabei die Symmetrieachse der Linse, um die die Linse drehbar ist, ohne sich zu verändern
#### Hohlspiegel
Für kleine Winkel
$$
f = \frac R2
$$
![[Pasted image 20250823170929.png]]
#### Konvex/Konkavlinse
![[Pasted image 20250823171105.png]]
$$
\frac {n_a}f = \frac{n_b-n_a}{n_a}\cdot \left( \frac1{r_1}+\frac1{r_2} \right)
$$

Bei der Beschreibung einer Konkavlinse werden negative Radien genutzt
![[Pasted image 20250823171412.png]]
###### chromatische Abberation (farblicher Linsenfehler):
Brennweite abhängig von Frequenz

### Kombinationen von Linsen
$$
\frac1{f_{ges}}=\simeq\frac1{f_2}-\frac1{D-f_1}
$$
![[Pasted image 20250823171712.png]]

## Abbildung mit Spiegeln und Linsen
Gilt sowohl für konvexlinsen, als auch für hohlspiegel
In den bisherigen Konfigurationen ist das Bild sowohl bei der Konvexlinse als auch beim Hohlspiegel relativ zum Objekt umgedreht.
![[Pasted image 20250823171820.png]]
![[Pasted image 20250823171835.png]]
$$
\frac GB=\frac{g-f}f=\frac f{b-f} = \frac gb
$$
$$
\frac 1f=\frac 1b+\frac 1g
$$

### Lupe
b < 0
Der Abstand des Bildpunktes von der Linse wird also negativ. Tatsächlich entsteht das durch die Lupe sichtbare, vergrößerte Bild auf der Gegenstandsseite
Vergrößerung
$$
V=\frac{|\u B|}G\frac sb
$$
Mit betrachtungsabstand s
Herkunft aus Virtuellem Bildpunkt (-b,-B)
![[Pasted image 20250823174019.png]]
### Mikroskop
![[Pasted image 20250823174200.png]]
Abstand Okkular Bild: b2
$$
V=s\cdot \left( \frac D{f_1f_2}-\frac{D-f_2}{b_2f_1} \right)\underbrace\approx_{\text{b2 groß}} \frac{s\cdot D}{f_1f_2}
$$
Die Berechnung von V in Abhängigkeit von den Parametern des Mikroskops f1 (Objektivbrennweite), f2 (Okularbrennweite) und D (Abstand Objektiv-Okular) ergib


##### Warum kann man keine beliebig hohe Vergrößerung erreichen
- Lichtintensität
- Beugungslimit: Nur Punkte mit $\Delta \gt \lambda/(2\sin\theta)$ Dabei ist θ derWinkel vom Objektpunkt zum Linsenrand. ∆ kann nie kleiner als λ/2 sein. Um ∆ klein zu machen, muss θ möglichst nahe bei 90◦ sein, was für große D nicht möglich ist. Außerdem wird das maximal erreichbare θ durch die Dicke der Linse d begrenzt
Vergrößerung einer Optik wird in der Regel auf den optimalen Sichtabstand s ≈ 25 cm bezogen

