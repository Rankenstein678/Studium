# Definitionen
>[!example] Polymerisationsgrad $P_n$
>Anzahl der Wiederholungseinheiten

>[!example] Molekulargewicht MW
>Gewicht des Polymers
>$$
>n\cdot M
>$$

>[!example] Zahlengemitteltes Molekulargewicht
>$$
>\overline {M_n} = \frac{\sum^N_{i=1} N_iM_i}{\sum^N_{i=1} N_i} = \frac{\sum^N_{i=1} W_i}{\sum^N_{i=1} (W_i/M_i)}
>$$

>[!example] Gewichtsgemitteltes Molekulargewicht
>$$
>\overline {M_w}  = \frac{\sum^N_{i=1} N_iM_i^2}{\sum^N_{i=1} N_iM_i} = \frac{\sum^N_{i=1} W_iM_i}{\sum^N_{i=1} W_i}
>$$

>[!example] Zentrifugenmittel
>$$
>\overline {M_z}  = \frac{\sum^N_{i=1} N_iM_i^3}{\sum^N_{i=1} N_iM_i^2} 
>$$

>[!example] Viskositätsmittel
>$$
> \overline {M_v}  = \left[   \frac{\sum^N_{i=1} N_iM_i^{1+a}}{\sum^N_{i=1} N_iM_i} \right]^{\frac 1a}
>$$
# Statistiche Betrachtung
![[Pasted image 20260130153823.png]]
## Momente
Ein zentraler Moment ist ein Moment der Wahrscheinlichkeitsverteilung einer zufälligen Variablen um den Mittelwert der zufälligen Variablen
DIe Momente bilden einen satz von Werten mit denen sihc eine Wahrschienlichkeitsverteikung beschreiben lässt.
Die Molekulargewichtsverteilung kann somit als ihre Momente beschrieben werden
$$
\mu_n  = \sum^N_{i=1} x_i M_i^n
$$
Die durchschnittlichen Molekulargewichte können als Fuktionen der Momente dargestellt werden
$$
\begin{align}
\overline M_n &= \frac {\mu_1}{\mu_0}\\
\overline M_w &= \frac {\mu_2}{\mu_1}\\
\overline M_z &= \frac {\mu_3}{\mu_2}\\
\end{align}
$$

# Polydispersitätsindex
Maß für die Breite der Molekulargewichtsverteilung
>[!important] Polydispersitätsindex
>$$
>PDI = \frac {\overline{M_w}}{\overline{M_n}}
>$$
>PDI=1 => Monodispers

# Bestimmung des Molekulargewichts
## Äquivalentmethoden
Vorkenntnisse über chemische Struktur notwendig
### Endgruppenanalyse
- Endgruppen müssen bekannt sein
- Gesamtgewicht dees Polymermaterials muss bekannt sein.
-> Äquivalent

Bestimmung der Endgruppe durch:
- Titration
- NMR
- UV/Vis
- Radiolabeling
Für aussagekräftige Ergebnisse ist eine große Anzahl von Endgruppen notwendig
gut für mittlere Molekulargewichte (5000 – 10000 g/mol)

#### Titration
- Makromoleküle müssen gut löslich sein
- Endgruppen müssen geeignet sein
>[!important] Endgruppenanalyse
>$$
>\overline {M_n} = \frac {qw}{n_end}
>$$


## Relativmethoden
Mit Kalibrierung
## Absolutmethoden
Direkte Bestimmung

# Ausnutzung kolligativer Eigenschaften
physikalische Methoden nutzen oft kolligative Eigenschaften
- hängen nur von der ANzahl Moleküle pro Volumeneinheit ab, nicht von chemischen Eigenschaften
>[!important] Kolligative Eigenschaften
>$$
>Y = K\frac NV
>$$
>Y: Kolligative Eigenschaften

Beispiele für Kolligative eigenschaften
- Absenken des Dampfdrucks
- Osmotischer Druck
- Erhöhung des Siedpunkts
- Erniedrigung des Gefrierpunkts

>[!warning] c steht in der Molekulargewichtsbestimmung für  die Massekonzentration
>$$
>[c] = \frac gL
>$$
>$$
>c(mol/L) = \frac 1M \cdot c(g/L)
>$$

## Dampfdruckosmometrie
- Mit steigender Konzentration sinkt der Dampfdruck der Lösung
- im thermodyn GGW hercgt der GGW Dampfdruck
- Erhöhte Konzentration führt zu Abweichung vom Gleichgewichtsdampfdruck
- mehr Lösemittel Kondensiert
- höhere Temperatur nptwendig
![[Pasted image 20260130155352.png]]
- Die notwendige Temperaturerhöhung ist charakteristisch 
- Der $\Delta T$ wird als spannung gemssen
>[!important] Dampdfdruckosmometrie
>$$
>\frac{\Delta T}{c} = \frac{K\cdot R\cdot T^2}{\rho_l\cdot \Delta H_\nu}\cdot \left( \frac{1}{M_n} + A_2\cdot c + \ldots \right)
>$$
>Für verschiedene Konzentrationen c-> 0

## Membranosmometrie
- Zwei kammern reines LM und Probe mit semipermeabler Membran getrennt (M< 10.000 g/mol)
- diffusion des LM am Konzentrationsgefälle
- osmotischeer Druck pi notwendig um  fluss zu stoppen
>[!important] Membranosmometrie
>$$
>\pi = \Delta h \rho g = \frac{1}{M_{solute}} \cdot cRT
>$$
>Für die Polymerlösung gilt
>$$
>\frac \pi{RTc} = \frac 1 {M_n} + A_2c+ A_3c^2
>$$ 
>Mit EExtrapolation folgt
>$$
>\lim_{c\rightarrow 0}\frac \pi c = \frac{RT}{M_n}
>$$

### Zsgh. Löslichkeit
Bei $\theta$ Lösemitteln verhält sihc das Polymer wie eine ideale Kette
$A_2=0$ Für tetha
$A_2>0$ gute LM
$A_2< 0$ für schlechte Lm
$A_3 = \frac {A_2}{4}$
![[Pasted image 20260130161243.png]]
