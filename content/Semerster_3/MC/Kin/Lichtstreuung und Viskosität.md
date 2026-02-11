# Lichtstreuung
## EM Strahlung
Streuung wird erzeugt indem Moleküle mit dem Oszillierenden E Feld wechselwirken
- Elektronen bewegen sich von Kernen weg -> Dipol
- Oszillierender Dipol ist quelle von Strahlung (Streulicht)
### Raman Streuung
- Inelastische Streuung -> Impuls (Richtung)und Richtung ändern sich
### Rayleigh Streuung
- Elastische Streuung -> andere Richtung aber gleiche Energie
- nimmt mit lambda/4 ab
- Mie Streuung: vorwärts bei schweren Partikeln
#### Quantitative Beschreibung der Rayleigh Streuung bei gasen
![[Pasted image 20260130173927.png]]
>[!important] Rayleigh Streuung von Gasen
>$$
>\frac {I_\theta}{I_0} = \frac{8\cdot \pi^4\cdot \alpha^2\cdot (1+ \cos^2 \theta)}{\lambda^4\cdot r^2}
>$$
>I0 Intensität unpolarisierter einfallender Strahlung
> alpha: Polarisierbarkeit des Moleküls: Proportionalitätskonstante bezogen aufdie Größe des induzierten Dipols

itetha Intensität gestreute Strahlung pro Volumeneinheit
$$
\frac {i_\theta}{I_0} = \frac NV\frac{8\cdot \pi^4\cdot \alpha^2\cdot (1+ \cos^2 \theta)}{\lambda^4\cdot r^2}
$$
![[Pasted image 20260130174752.png]]
![[Pasted image 20260130174813.png]]
### Rayleigh Verhältnis
>[!important] Rayleigh Verhältnis
>$$
>R_\vartheta = \frac{V_S\cdot i_\vartheta\cdot r^2}{I_0\cdot f\cdot V_s}
>$$
>![[Pasted image 20260130175101.png]]
>![[Pasted image 20260130175418.png]]
### In Verdünnter Lösng
![[Pasted image 20260130175522.png]]
![[Pasted image 20260130175535.png]]
![[Pasted image 20260130175546.png]]
![[Pasted image 20260130175635.png]]
### Große Moleküle
- Streuintensität hängt vom Winkel ab
- Es entstehen unterschiedliche Weglängen (außer bei 𝜃 = 0)
- ![[Pasted image 20260130175805.png]]

## Statische vs Dynamische Lichtstreuung
- Statische Lichtstreuung: Durchschnittliche Streuintensität durch messen einer Population von Partikeln und subsequentes integrieren. -> Partikelgröße und bei Kalibration MW
- dynamische: Messung in kurzen ABständen -> Brownsche Molekularbewegun -> Teilchengröße
- ![[Pasted image 20260130180250.png]]
- ![[Pasted image 20260130180300.png]]
- ![[Pasted image 20260130180310.png]]

# Viskosität
## Übersicht
>[!important] Viskosität
>Relative Viskosität (Viskositätsverhältnis)
>$$
>\eta_r = \frac{\eta}{\eta_0}
>$$
>Spezifisch Viskosität
>$$
>\eta_{sp}=\eta_r-1
>$$
>Reduzierte Viskosität (Viskositätszahl)
>$$
>[\eta_{red}]=\frac{\eta_{sp}}c
>$$
>Intrinsische Viskosität (Limitierende Viskositätszahl) \[L/g]
>$$
>	[\eta]=\lim_{c\rightarrow 0} [\eta_{red}]
>$$

## Polymerlösungen
In Polymerlösungen gilt
$$
\frac{\eta}{\eta_0} = 1 + A_0c + A_1c^2+\ldots
$$
Somit gilt
>[!important] Intrinsische Viskosität Polymerlösung
>$$
>[\eta] = A_0
>$$
## Viskosimetrie
![[Pasted image 20260130163219.png]]
- Ein bekannte Flüssigkeitsvolumen wird durch Rohr A in Kolben D pipetiert
- mit Druck p in E pumpen
- bei geschlossenem C: Druck auf A
- bei offenem C: fluss durch Kapillare mit L und r. 
- Messung der Zeit von x nach y
>[!important] Viskosität nach nach Hagen und Poiseulle
>$$
>\eta =\frac{\pi r^4\Delta pt}{8LV}
>$$
>mit delta p: Druckunterschied bei der Kapillare

### Extrapolation zur Nullkonzentration
- Zur Bestimmung von \[𝜼\] wird eine Konzentrationsreihe gemessen, danach kann das Molekulargewicht über die Mark-Houwink-Gleichung berechnet werden
- Bei hohen Konzentrationen verfangen sich die random coils, sodass es zu einer höheren Viskosität kommt
- Eine Extrapolationsformel zum Erhalten von \[𝜂] ist die Huggins-Gleichung, mit der tabellierten Huggins-Konstante 𝒌𝐇
>[!important] Huggins-Gleichung
>$$
>\frac{\eta_{sp}}c = [\eta] + k_H[\eta]^2c
>$$

Alternativ für breiteren Parameterbereich
>[!important] SChulz-Blaschke Formel
>$$
>	\frac{\eta_{sp}}c = [\eta] + k_{SB}[\eta]\eta_{sp}
>$$

##  Mark-HouwinkGleichung
Für Monodisperse Fraktionen
>[!important] Mark-Houwink-Gleichung (monodispers)
>$$
>[\eta] = K\cdot M^a
>$$
>$$
>\log [\eta] = \log K + a\log M
>$$
>Mark-Houwink Koeffizienten können bei bekanntem Molekulargewicht bestimmt werden.
## Einstein Gleichung für die Viskosität von Lösungen

>[!important] EInstein Gleichug für Viskosität
>$$
>[\eta]=\frac{2.5}\rho = \frac {2.5 V \cdot N_A}{M}
>$$
## Kuhn Random Coil
![[Pasted image 20260130180417.png]]