Ladungsfluss -> Strom
Nicht im GGw, daher E-Feld im metallenen leiter
# Widerstand
In idealem Leiter:
Elektronen ungebremst:
Gesamte potenzielle energie wird in kinetische umgewandelt
## Realer leiter
Mit freier Weglänge lambda folgt
$$
v_{max} = \sqrt{\frac{2|\u E|e\lambda}m}
$$
Mittlere Geschwindigkeit ist nachb lambda/2 erreicht
$$
v_{D} \simeq \sqrt{\frac{|\u E|e\lambda}m}=\frac{e\tau}m\cdot|\u E|
$$
mit Stoßzeit Tau
$$
\lambda = v_D\cdot \tau
$$

Driftgeschwindigkeit $v_D$
Es wird die Materialabhängige Beweglichkeit definiert
$$
\mu=\frac{e\tau}m\implies v_D=\mu|\u E|
$$
### Stromstärke
$$
I = \ddt{Q}t=\dot Q
$$
Mit Leitergeometrieunabhängiger Stromdichte
$$
\u j =\frac IA=\frac{ne^2\tau}m\cdot \u E = \sigma\cdot\u E
$$
Mit spezifischer Leiftähigkeit $\sigma$
Mit spezifischem Widerstand
$$
\rho =\sigma^{-1}
$$
Einheit $\Omega m$
### Widerstand
$$
I = \frac{\sigma\cdot A}LU=S\cdot U
$$
Mit Leitfähigkeit S in  Siemens ($\frac AV$)
(Steigung im I/U Diagram)
Mir $R=S^{-1}$
$$
U=R\cdot I
$$
$$
R=\rho\cdot \frac LA
$$
# Verlustenergie
- Verlustenergie=potenzielle Energie
$$
\Delta E_{pot}= U\cdot I\cdot \Delta t
$$
- Verlustleistung
$$
P_W=U\cdot I =R\cdot I^2
$$
# Kondensator
Ladung

$$
I(t)=I(0)\cdot e^{-\dfrac1{RC}\cdot t}
$$
$$
Q(t) =U(0)\cdot C\cdot(1-\exp\left(-\frac1{RC} \cdot t\right))
$$
![[Pasted image 20250823005828.png]]
Mit Zeitkonstante $\tau=R C$
Die SPannung steigt mit der Zeitkonstante exponentiell an
Entladung
$$
Q(t)=Q(0)\cdot\exp(-\frac1{RC}t)
$$
# Verallgemeinert
## Ionische Flüssigkeiten
$$
\rho =\frac{m_{Ion}}{n_{ion}\cdot(Ze)^2\cdot\tau}
$$
n: Ionen pro m³
## Isolatoren
Ladungsträger = energiereiche Elektronen, n exponentiell abhängig von T , τ abhäng von T
## Halbleiter
Wie Isolatoren, aber höheres n (kleineres $\Delta E$),
## Dotierte Halbleiter
Wie Metalle, aber kleineres n, schaltbar durch äußeres n
# Batterien
- Batterien/Akkus sind aufgeladene Kondensatoren, in denen die Ladung als Ionen in Lösung gespeichert ist
- Gespeicherte Ladungsmenge (“Kapazität”) hängt von der Ionenlöslichkeit im Elektrolyt ab
- Entladung der Batterie kann reversibel (Akku) oder irreversibel (Batterie) sein
- Spannungsquellen haben einen Innenwiderstand, der die nutzbare Spannung reduziert
$$
U_N =U_0\frac{R_N}{R_i+R_N}
$$
