Magnetische Induktion $\vec B =[T] = [Vsm^{-2}]$
Vauumpermeabilität $\mu_0 = 4\pi\cdot 10^{-7}$

>[!important] Die gyromagnetische Beziehung
>Ein Kernspin erzeugt ein magnetisches Moment:
>$$
>\vec {\mu_N} =  \gamma_N \vec I
>$$
>$\gamma_𝑁$ : gyromagnetisches Verhältnis

1 H hat das größte gyromagnetische Verhältnis aller natürlich vorkommender Kernspin

### Zeeman Wechselwirkung
Laut klassischer Physik
$$
E = -\mu_0 B
$$
umwandelbar in Zeeman WW:
>[!important] Zeeman WW
>$$
>\hat{\mathcal {H}_Z} = -\gamma B_0\hat I_Z
>$$

Es folgt mit $E_{I,m_I}$ 
$\alpha$ : $E_{\frac 12,\frac 12} = -\frac 12 B_0\gamma\hbar$ 
$\beta$ : $E_{\frac 12,-\frac 12} = +\frac 12 B_0\gamma\hbar$ 
==Im Magnetfeld ist die Entartung der Ausrichtung des Kernspins aufgehoben==


>[!important] Larmor Frequenz
>$$
>\omega_0 =2\pi\nu_0= -\gamma B_0
>$$


>[!important] Resonanzbedingung
>$$
>\Delta E = -\hbar\omega_0
>$$

![[Pasted image 20251124093800.png]]
![[Pasted image 20251124093827.png]]

## Auswahlregel der Spetroskopie
$$
\Delta m_l =\pm 1
$$
# Makroskopische Magnetisierung
Das Magnetische Moment ist definiert:
$$
\mu_N = \gamma_N \vec I
$$


Das makroskopische Moment entspricht der Gesamtsumme eines Ensembles von Spins
$$
\vec m = \sum \vec \mu
$$
Relativ zum Volumen definiert man die Makroskopische Magnetisierung 
>[!important] Makroskopische Magnetisierung
>$$
>\vec M  = \frac 1V \vec m =  \left[ \frac Am \right]
>$$

![[Pasted image 20251124094253.png]]
## Gleichgewichtsmagnetisierung $M_0$
(Mit Hochtemperaturnäherung)
$$
M_z = \frac{\color{red}N_V\gamma^2\color{white}\hbar^2I(I+1)\color{red}B_0}{3k_B\color{red}T} = M_0
$$
![[Pasted image 20251124094552.png]]
![[Pasted image 20251124094720.png]]

# Larmor Präzession
Die Makroskopische magnetisierung präzediert (im UZ: $\gamma >0$ )
![[Pasted image 20251124094831.png]]



# T1 Relaxation: Spin-Gitter-Relaxation
Beschreibt Widerherstellung der Gleichgewichtsmagnetisierung (Entlang $B_0$)
-> longitudinale Komponente Mz
Eine Änderung in Mz hat einen Energieaustausch mit der Umgebung zur Folge (longitudinale Relaxation)
>[!important] $T_1$ Relaxation
>$$
>M_z(t) = M_0\left(1-\exp\left(-\frac t{T_1}\right)\right)
>$$

# T2 Relaxation: Spin-Spin-Relaxation
Dephasierung der Magnetisierung in der xy-Ebene (transversale Relaxation)
Lokale magnetische Felder induzieren die Relaxation
Die Abnahme der Magnetisierung ist nicht nur durch T2-Relaxation begründet, sondern z.B. auch durch Inhomogenitäten im Magnetfeld. Hierfür wird die Zeit T2‘ gewählt
>[!important] $T_2$ Relaxation
>$$
>\frac 1{T_2^*} = \frac 1{T_2} + \frac 1{T_2^\prime}
>$$

