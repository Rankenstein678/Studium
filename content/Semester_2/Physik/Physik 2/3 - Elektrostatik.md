Ladung erzeugen durch reiben von isolatoren
# E-Feld
Kraft die auf einen Punkt wirkt, wenn man ihn im E-Feld der Ladung platzieren würde
$$
E(r) \quad mit\quad [|\u E|] = \frac NC
$$
$$
F=q\cdot E
$$
## Mehrere Diskrete Ladungen
$$
E(r) = \frac1{4\pi\epsilon_0}\sum_i\frac{q_i}{|\u r-\u r_i|^2}\cdot\frac{(\u r-\u r_i)}{|\u r -\u r_i|}
$$
$\u E_i$ zeigt immer entlang der Verbindungslinie Messpunkt-Ladung $q_i$
Die Ausrichtung von Ei wird zusätzlich durch das Vorzeichen von qi bestimmt


## Kontinuierliche Ladung
$$
E(r)=\frac 1{4\pi\epsilon_0}\iiint_V \frac{\rho(r^\prime)}{|\u r-\u r^\prime|^2}\cdot\frac{(\u r-\u r^\prime)}{|\u r -\u r^\prime|}d^3r^\prime
$$
Mit Ladungsdichte

# Feldlinine
Tangenten an das E Feld
![[Pasted image 20250822180447.png]]
![[Pasted image 20250822180834.png]]![[Pasted image 20250822180843.png]]
E-Feld Plattenkondesnator
$$
\u E(\u r)=\frac Q{\varepsilon_0A}\cdot \u e_z = \frac{\rho_A}{\varepsilon_0}\cdot\u e_z
$$
# Ungeladene Körper im elektrischen Feld
## Isolatoren
$$
D= p\times E
$$
Mit DIpolmoment p von minus nach plus
$$
\u p=\delta q\ddot d\cdot \u e_z  \quad mit \quad [|\u p|]=C\cdot m
$$

![[Pasted image 20250822181257.png]]
Bei Isolatoren ohne permanentes Dipolmoment werden im E-Feld Dipole induziert. 
Allgemein schwächen Dipole ein E-Feld

### Abschwächung durch Isolatoren
Dielektrizitätskonstante: $\varepsilon$
$$
\u E(\u r) = \frac q{4\pi\varepsilon_0}\frac{\hat{\u r}}{|\u r|^2}\cdot \frac 1\varepsilon
$$
Zum rechnen in symmetrischen Isolatoren nutzt man die dielektrische Verschiebung
$$
\u D(\u r) = \varepsilon(\u r)\cdot \varepsilon_0\cdot \u E(\u r)
$$
## Metalle
Im Metall sind einige Elektronen frei verschiebbar $\implies$ $\u E=0$ im Metall
1. Überschüssige Ladungen können nur auf der Oberfläche sitzen
2. E-Feldlinine immer Senkrecht zur Metalloberfläche
3. Die Ladungen auf der Metalloberfläche kompensieren die E-Felder der äußeren Ladungen im inneren des Metalls
$$
\u E(\u r) = \sum_\text{äußere Ladung}\u E_i(\u r) + \sum_\text{Ladung auf der Oberfläche}\u E_i(\u r)=0
$$
![[Pasted image 20250822182738.png]]
Der Prozess der Ladungsverschiebung im Metall durch äußere E-Felder heißt Influenz.

# Elektrisches Potenzial, Spannung, Kapazität
## Potenzial
Die Coulombkraft ist eine Zentralkraft. Man kann also für die Coulombkraft eine potenzielle Energie definieren
$$
E_{pot}=-\int^{\u x}_{\u \infty}q\cdot\u E(\u r)d\u r
$$

![[Pasted image 20250822183107.png]]
$$
E_{pot} = \frac{qQ}{4\pi\varepsilon_0|\u x|}
$$
Das Potenzial wird analog zum E-Feld für  die potenzielle Energie definiert.
$$
\Phi_{el}(\u x)=\frac{E_{pot}(\u x)}q
$$
![[Pasted image 20250822183428.png]]
## Spannung
Da der Nullpunkt des Potenzials beliebig festgelegt wurde zählen dur differenzen.
$$
U_{12} = \Phi_{el}(\u x_1)-\Phi_{el}(\u x_2)
$$
Mit einheit $V= \frac JC$
Es folgt
$$
E_{pot}=qU
$$
## Kapazität
$$
Q = C\cdot U
$$
Mit \[C] = F
$$
C = \frac{\varepsilon\varepsilon_0A}{d}
$$
