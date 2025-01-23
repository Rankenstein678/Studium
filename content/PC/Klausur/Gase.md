# 1. Grunddefinitionen
## 1.1 Avogadrozahl
$$
N_A = 6.022\cdot10^{23}\ \mathrm{mol}^{-1}
$$
## 1.2 Einheiten des Drucks

$$
1\ Pa = 1*10^5\ bar = 1.023 * 10^5
$$
$$
1\ bar = 1.013\ bar
$$
## 1.3 Boltzmann Konstante
$$
k_B = R/N_A
$$
# 2. Thermodynamik
##  2.1 Systeme
- offen
- geschlossen
- abgeschlossen
## 2.2 Hauptsätze
### 2.2.1 0. Haupsatz
Wenn Objekt A und B im thermo. GGW und B & C im GGW, dann sind auch A&C im GGW
### 2.2.2 1. Hauptsatz
Die innere Energie eines abgeschlossenen Systems ist konstant

# 3. Ideales Gas
Das Ideale Gas ist die einfachste Form der Materie
- Teilchen in zufälliger Bewegung
- keine interpartikulären Wechselwirkungen

Der Zustand des Gases wird definiert durch
- Volumen (V) _\[V]_ = m³ 
- Druck (p) \[p] = Pa = N/m² = kg/m*s² 
- Temperatur (T) \[T] = K
- Stoffmenge (n) \[mol]

Alle Zustandsgrößen lassen sich durch die ==Zustandsgleichung== (equation of state) des idealen Gases verknüpfen:

$$
 p\cdot V = n\cdot R\cdot T
$$
mit
$$
\textit{Ideale Gaskonstante } R:=8.314\ \frac{kg\cdot m^2}{mol\cdot K \cdot s^2}/ \frac{J}{mol\cdot K}
$$

Alternativ mit dem molaren Volumen
$$
p\cdot V_m = RT
$$
Das System ideales Gas befindet sich in einem zeit- und vorgeschichtsunabhängigen ==Gleichgewichtszustand==. 

##  2.2 Iso...
Trägt man eine Zustandsvariable der idealen Gasgleichung gegen andere auf so werden sie wie folgt bennant
- konst. Druck: _isobar_
- konst. Volumen: _isochor_
- konst. Temp: _isotemp_

## 2.3 Partialdrücke
Betrachtet man ein (auch reales) Gasgemisch so gilt für den Anteil jedes Bestandteils am Druck
$$
p_J  = x_J\, p
$$
Mit 
$$
Molenbruch\ x_J = \frac{n_J}{n}
$$

# 3. Reale Gase
Bei hohem Druck / Tiefer Temperatur weichen reale Gase vom idealen Verhalten ab oder ändern sogar ihren Aggregatszustand / erleben Phasenübergänge
Dies kommt durch in der Praxis existierende ==intermolekulare Wechselwirkungen==

Beispiel Phasenübergänge

![[Pasted image 20250112215445.png]]
##### Abstoßende WW:
Teilchen kommen in Kontakt
kurzreichweitig
wichtig bei hohem Druck und hoher Dichte

##### Anziehende WW
etwas langreichweitiger

![[Pasted image 20250112211607.png]]
## 3. 1 Der Kompressionsfaktor $Z$
Der Kompressionsfaktor $Z$ ist definiert als 
$$
Z = \frac{p\,V_m}{R\,T}
$$
Für ein ideales Gas ist $Z = 1$

Für reale Gase gilt:

- Wenn $p\rightarrow 0$, dann $Z\approx 1$
- Bei mittleren Drücken: $Z < 1$
	- Anziehung der moleküle Überwiegt
- Bei hohen Drück: $Z > 1$
	- Abstoßung überwiegt
## 3.2 Die Virialgleichung
$$
Z = \frac{pV_m}{RT} = 1 + \frac B{V_m} + \frac C{V_m} + \ldots 
$$
mit
$B:=\textit{Zweiter Virialkoeffizient}$
$C:= \textit{Dritter Virialkoeffizient}$

Die Virialkoeffizienten sind ==temperaturabhängig==
alternativ
$$
Z = 1 + B^\prime p + C^\prime p^2 + \ldots
$$

## 3.3 Boyle-Temperatur
Es kann für reale Gase eine Temperatur geben bei der gilt
$$
Z \rightarrow 1 \text{ und } Z\ne f(p)
$$
Bei dieser ==Boyle Temperatur== $T_B$ gilt:
$$
pV_m \approx RT_B
$$
Wenn $p\rightarrow 0$ und $B=0$ (die weiteren Virialkoeffizienten können ignoriert werden)

![[Pasted image 20250112215220.png]]
## 3.4 Kritischer Punkt
Der kritische Punkt ist genau der Punkt im  Phasendiagramm (siehe [[Gase#3. Ideales Gas]]) an dem die Obere Spitze des Verflüssigungsbergs berührt wird.
In diesem Zustand lassen sich Flüssigkeit und Gas nicht mehr unterscheiden;

Beschrieben wird der Punkt durch
$p_{cr}$ und $V_{cr}$ und $T_{cr}$


Überkritische Fluide sind besondere Lösemittel

# 4. Mikroskopisches Modell und Van-der-Waals Gleichung
## 4.1 Korrektur der Abstoßenden WW
Teilchen in Realen Gasen haben ein Volumen, dass anderen Teilchen nicht mehr zur Verfügung steht
$$
V_{real} = V - nb 
$$
Eine Kugel des Durchmessers $d$ hat ein Volmen von
$$
V_K = \frac {4\pi}3 \left(\frac d2\right)^3
$$
Der kleinste Abstand zwischen zwei Kugeln ist $d$
Das von Zwei Kugeln ausgeschlossene Volumen ist also
$$
\frac 43\pi d^3
$$
 Eine Kugel schließt demnach ein Volumen von
$$
\color{red}b =4V_K = \frac 12 \frac{4\pi}3 d^3
$$
aus
## 4.2 Korrektur der Anziehenden WW
Die anzeihenden WW sind von der Konzentration abhhängig und verringern den Druck:

$$
- a\left(\frac{n}{V}\right)^2
$$
## 4.3 Die Van-der-Waals Gleichung
$$
p = \frac{nRT}{V-nb} - a \frac nV^2
$$
Van der Waals Schleifen werden durch horizontale Lininen so ersetzt das oben und unte Gleich viel ist.

Für kritische Isotherme gilt $T = T_{krit}$
![[Pasted image 20250112222057.png]]
## 4.4 Der Kritische Punkt und die vdW - Gleichung
Am (und nur am) kritischen Punkt gilt

$$
\frac{\mathrm d\,p}{\mathrm d\,V_m}  = 0 \textit{ und } \frac{\mathrm d\,p^2}{\mathrm d\,V_m^2} = 0
$$
für die vdw gilt dann
$\displaystyle p_{cr} = \frac {a}{27b^2}$ , $\displaystyle T_{cr} = \frac{8a}{27Rb}$, $\displaystyle V_{m,cr}= 3b$
es folgt
$$
Z_{cr} = \frac 38
$$
## 4.5 Prinzip der übereinstimmenden Zustände
Verwendet man reduzierte Variablen
$$
x_r = \frac x{x_{cr}}
$$
erhält man ähnliches Verhalten für verschiedene Gase
$$
p_r = \frac{8T_r}{3V_r-1}- \frac{3}{V_r^2}
$$
![[Pasted image 20250112224221.png]]

# 5  Wechselwirkungspotentiale
Das Wechselwirkungspotential beschreibt die Kräfte zwischen Teilchen nach dem Abstand

$$
F = - \frac{dU(r)}{dt}
$$
## 5.1 Das harte Kugel Modell
![[Pasted image 20250112224940.png]]
"Unbewegbares Objekt ohne andere WW""
## 5.2 Kastenpotential
![[Pasted image 20250112225130.png]]
## 5.3 Sutherland Potential
![[Pasted image 20250112225152.png]]
## 5.4 Lennard-Jones-Potential (12-6)
![[Pasted image 20250112225224.png]]
$$
U(r) = 4\epsilon\left[\left(\frac{\sigma}r\right)^{12} - \left(\frac\sigma r \right)^6\right]
$$

# $\color{red}\text{ Langmuir und Oberflächen fehlen}$

# 7. Das mikroskopische Modell
## 7.1 Annahmen
- Gase bestehen aus Teilchen der Masse m
- Teilchen haben zufällige Bewegung
- Teilchen haben nur kinetische Energie (pot. ist vernachlässigbar)
- Es gibt nur perfekt elastische Stöße zwischen den Teilchen
## 7.2 Herleitung
Jedes Teilchen hat den Impuls in x-Richtung $mv_x$
Und nach einem Stoß $-mv_x$

Teilchen innerhalb des Volumens $v_x\Delta tA$ können die Wand erreichen
![[Pasted image 20250113155419.png]]

Teilchenzahldichte: 
$$
\frac {nN_A}{V}
$$
Zahl der Stöße auf die Wand im Intervall $\Delta t$
$$
\frac 12 \frac{nN_A}{V}Av_x\Delta t 
$$
Die 1/2 kommt daher, dass sich sich immer die Hälfte der Teilchen in x-Richtung und die anderen in -x Richtung  bewegen

Für die Impulsänderung gilt:
$$
	\frac 12 \frac{nN_A}{V}Av_x\Delta t \cdot 2mv_x =  \frac{n m N_A Av_x^2\Delta t}{V} = \frac{nMAv_x^2\Delta t}{V}
$$
Die Änderungsrate ist demnach
$$
\frac{nMAv_x^2}{V}
$$
Nach Newton gilt
$$
F = m\times a = m \frac{dv}{dt}
$$
Also ist die Änderungsrate = F

Für den Druck gilt
$$
p = \frac FA
$$
Also gilt
$$
 Druck = \frac{nMv_x^2}{V}
$$
==Aber== nicht alle Teilchen haben die gleiche Geschwindigkeit. Man wählt daher den Durchschnitt.
$$
\color{red} p = \frac{nM}{V}\langle v_x^2\rangle
$$

Für die  Gesamtgeschwindigkeit gilt dann
$$
c^2 = \langle v^2_x\rangle + \langle v^2_y\rangle + \langle v^2_z\rangle = 3\langle v_x^2\rangle
$$
da die Geschwindigkeit in alle Richtungen gleich groß ist

Es folgt

$$
pV = \frac 13 nMc^2
$$
$$
c = \sqrt{\frac{3RT}M}
$$
## 7.3 Arten der Geschwindigkeit
### 7.3.1 Mittlere Quadratische Geschwindigkeit $\langle v_x^2 \rangle$
(in x Richtung)

### 7.3.2 Wurzel der Mittleren Quadratischen Geschwindigkeit c
$$
c = \langle v^2\rangle^{1/2}
$$
###  7.3.3 Durchschnittliche Geschwindigkeit (in Maxwell)
$$
\overline  c =  \sqrt{\frac{8RT}{\pi M}}
$$
### 7.3.4 wahrscheinlichste Geschwindigketi (Maxwell)
$$
c^*=\sqrt{\frac{2RT}{M}}
$$
# 8. Maxwell Geschwindigkeitsverteilung
Für den Anteil der Teilchen im Intervall $v$ bis $v+\mathrm dv$ gilt
$$
f(v)\mathrm d v
$$
Mit 
$$
f(v)  = 4\pi\left(\frac{M}{2\pi RT}\right)^{3/2}v^2exp\left(\frac{-Mv^2}{2RT}\right)
$$
Ist das Interval zu groß um als Infinitessimal berschrieben zu werden gilt:
$$
\int_{v_1}^{v_2} f(v)\mathrm dv
$$
(Wird außer  in Sonderfällen nur numerisch gelöst)

Spielt die Richtung eine Rolle so gilt:

$$
 \left(\frac{M}{2\pi RT}\right)^\frac32 exp\left(\frac{-Mv^2}{2RT}\right)dv_xdv_ydv_z
$$
Dies wird durch zur Gleichung 1 umgeformt, indem das Volumen einer Kugelschalge $4\pi v^2dv$ genutzt wird. Dann gilt sie für den Betrag der geschwindigkeit.


## 8.1 kin Energie eines Teilchens
$$
\langle\epsilon_{kin}r\rangle = \frac12 m \langle v^2\rangle=\frac{3}{2}k_BT
$$
$$
\overline E_{kin} = \frac 32 RT
$$
$$
\langle v_x^2\rangle = \frac 13 \langle v^2\rangle
$$

# 9. Boltzmann Verteilung
Der Term der Maxwell Verteilung
$$
	\exp\left(-\frac{Mv^2}{2RT}\right)
$$
kann geschrieben werden als
$$
	\exp\left(-\frac{E_{kin}}{RT}\right)
$$
Dieser Term wird auch Boltzmann Faktor gnannt
$$
\frac{N(E)}{N} \propto e^{-\dfrac{E}{RT}}
$$
# 10. Relative Geschwindigkeit
![[Pasted image 20250115133608.png]]
Gleiche Masse
$$
\overline c_{rel} = \sqrt 2 \ \overline c
$$
Verschiedene Masse
$$
\overline c_{rel} = \sqrt{\overline c^2_1 + \overline c_2^2} = \sqrt{\frac{8k_BT}{\pi m_1} +\frac{8k_BT}{\pi m_2}} = \sqrt{\frac{8k_BT}{\pi\mu}}
$$
Mit reduzierter Masse
$$
\mu = \frac{m_1m_2}{m_1+m_2}
$$
# 10. Stoßfrequenz
$$
Z = \sigma \overline c_{rel} \frac{p}{k_BT}
$$
## 10.1 Der Stoßquerschnitt
Ein sich bewegendes teilchen bewegt sich gewisssermaßen durch eine Röhre mit

Grundfläche
$$
\sigma = \pi d^2
$$
und Länge
$$
\lambda = \overline c_{rel}\Delta t
$$
Demzufolge hat die Röhre ein Volumen von 
$$
V = \sigma \overline c_{rel} \Delta t
$$
![[Pasted image 20250115134734.png]]
## 10.2 Die Stoßfrequenz
In der Röhre befinden sich teilchen. Die Zahl kann als konstant angenommen werden, da sich die Teilchen perfekt zufällig bewegen.
$$
\textit{Zahl der Stöße} = \frac NV\ \sigma\ \overline c_{rel}\ \Delta t 
$$
Stoßfrequenz 
$$
Z_1 = \frac{\frac NV\ \sigma\ \overline c_{rel}\ \Delta t }{\Delta t} = \frac{N}{V} \ \sigma\ \overline c_{rel}
$$
Mit dem idealen Gassgesetz folgt:
$$
\frac NV = \frac{p\ nN_A}{RT} = \frac{p\,n}{k_BT}
$$
## 10.3 Die mittlere freie Weglänge
$$
\lambda = \frac{\overline c}{Z_1} = \frac{\overline c k_B}{\sigma \overline c_{rel} p}
$$
Für nur eine Teilchensorte folgt:
$$
\lambda = \frac{\overline c k_B}{\sigma \sqrt 2\overline c p} =  \frac{k_B}{\sqrt 2 \sigma p }
$$
