Übergang von Grundzustand S1 auf irgendeinen Zustand S0
![[Pasted image 20260123124506.png]]
![[Pasted image 20260123124521.png]]
![[Pasted image 20260123124612.png]]
# Stokes Shift
![[Pasted image 20260123124643.png]]
Energie geht auf Strahlungslosen wegen verloren.
# Aufbau
Lichtquelle -> Monochromator -> Probe -> Emissionsmonochromator im 90° Winkel (filtert Eingestrahltes Licht) -> Detektor

## Probenvorbereitung
Standardbedingungen für pH & Temperatur müssen gegeben sein + verdüünnen und filtern
## Vergleich
Vergleich zwischen Geräten mithilfe eines Fluoreszenzstandards
## Konzentrationsmessungen
sinnd möglich

# Innerer Filter-Effekt
Ist die Konzentration zu stark wird das Licht nur in einer dünnen Lamelle außen absorbiert und das Emittierte Licht trifft nicht auf den Detektor / Wird von der Probe absorrbiert -> deshalb verdünnt arbeiten (bis zu 10^-9 M messbar)
## Fehler generell
![[Pasted image 20260123112334.png]]

# Todo:: Hier fehlt wegen dem Basstard was

# Fluoreszenz-Quantenausbeute und -Lebenszeit

>[!important] Fluoreszenzquantenausbeute
>$$
>\phi_f = \frac{N_{emit}}{N_{abs}}=\frac{k_f}{\sum k_{alle}} = \frac{k_F}{k_F+k_{IC}+k_{ISC}} = k_F \cdot \tau_F
>$$
>Fluoreszenzlebensdauer $\tau_F$: Wie lange lebt S1

### Bestimmung mittels der Relativmethode von Parker und Rees
Das Verhältnis der Fluoreszenz-Quantenausbeuten
zwischen Probe (P) und Referenz (R) entspricht dem Verhältnis der entsprechenden (korrigierten) Fluoreszenzintensitäten. Die Fluoreszenz-Quantenausbeute der Probe kann mit dem bekannten Wert der Referenz bestimmt werden.
 $$
\frac{\phi_P}{\phi_R} = \frac{F_P}{F_R}
$$
- Probe und Referenz sollten optisch dünn sein (A < 0.05).
- Probe und Referenz sollten die gleiche Menge an Anregungsenergie absorbieren
- Die Fluoreszenz-Quantenausbeute der Referenz sollte nicht von der Wellenlänge abhängen
- Referenz und Probe sollten Fluoreszenz im gleichen Wellenlängenbereich zeigen
>[!warning] Aber:
>Nicht sehr genau $(\pm 5 \%)$

>[!important] Parker-Rees:
>$$
>\frac{\phi_P}{\phi_R} = \frac{F_P}{F_R}\cdot \frac{I_{0,R}}{I_{0,P}}\cdot \frac{1-10^{-A_R}}{1-10^{-A_P}}\cdot \frac{n^2_P}{n^2_R}
>$$
>$I_0$ Anregungsintensität
>zweiter Term: Anteil der Lichtenergie, der in der Probe absorbiert wird (idealerweise gleich mit A <0.1)
>n: Brechungsindizes

### Absolutmethode mit der ULBRICHT-Kugel

![[Pasted image 20260123124348.png]]

# Fluoreszenzlöschung
Fluoreszenzlöschung = fluorescence quenching (engl.)
Jeder Prozess, der die Fluoreszenzintensität / -lebensdauer verkleinert wird als Fluoreszenzlöschung bezeichnet.
Zusätzlicher Weg zur Desaktivierung des angeregten Zustands.

## Wege
Es gilt mit Quenchmittel Q
$$
\phi_F = k_F \cdot \tau_F = \frac{k_F}{\sum_j k_{j,monomolek}+ \sum_i k_{i,q}[Q_i]}= \frac{k_F}{k_F+k_{IC}+k_{ISC}+k_{sonst, mono} +\sum_i k_{i,q}[Q_i]}
$$
Als Maß für die Löschung
$$
\frac{F_0}{F} = \frac{\phi_{f,0}}{\phi_f} = 1+\frac{k_q}{k_F+k_{IC}+k_{ISC}}\cdot [Q] = 1+ \tau_F \cdot k_q \cdot [Q] = 1+ K_{SV} \cdot [Q]
$$

# Statisches vs dynamisches Quenchen
## Dynamisches Quenchen
höhere Temperatur oder niedrigere Viskosität
⇒ schnellere Diffusion
⇒ stärkere Fluoreszenzlöschung
![[Pasted image 20260123125317.png]]
## Statisches Quenchen
Gleichgewicht im Grundzustand
$$
\ce{F^*+Q <=>[K] (F\cdot Q)^*}
$$
höhere Temperatur
⇒ verstärkte Dissoziation (Entropie)
⇒ schwächere Fluoreszenzlöschung
![[Pasted image 20260123125458.png]]
# Energieübertragung
# Förster und Dexter
## Förster
Wechselwirkung über elektrisches Feld
$$
k_{Foerster}\propto r^{-6}
$$
![[Pasted image 20260123125617.png]]
## Dexter
Austausch von Elektronen bei Überlappung der Elektronenwolken
$$
k_{Dexter}\propto  e^{-r}
$$
![[Pasted image 20260123125659.png]]

# Energetische Betrachtung für die  Energieübertragung
![[Pasted image 20260123125809.png]]
![[Pasted image 20260123125818.png]]
# FRET-Rate (Förster-Resonanz-Energietransfer (FRET))
![[Pasted image 20260123125911.png]]
Mit dem Förster Radius ($R_0$) (==Abstand== (nicht radius) wo Intensität ist halb) gilt
>[!important] FRET Rate
>$$
>k_{FRET} = \frac 1{\tau_{f,0}(Donor)}\left(\frac{R_0}{R_{Donor\_Akzeptor}}\right)^6
>$$

>[!important] FRET Effizienz
>Wie viel der angeregten Zustände geben Ihre Energie an den FRET-Akzeptor ab?
>$$
>\eta_{FRET} = \frac{k_{FRET}}{k_{FRET}+k_{sonst}}=\frac{1}{1+ \frac{k_{sonst}}{k_{FRET}}} = \frac1{1+ \left(\frac{R_{Donor\_Akzeptor}}{R_0}\right)^6}
>$$

# Fluoreszenzlöschung durch Schweratome
Löschung da schwere Atome den ISC beschleunigen


