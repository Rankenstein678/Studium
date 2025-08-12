# Klassischer Harmonischer Oszillator
Modell zweier mit Feder verbundener Atome
>[!important] klasischer Harmonischer Oszillator I
>$$
>E = E_{kin} + E_{pot} = \frac 12 mv^2 + \frac 12 k_fx^2 = const.
>$$
>Mit $k_f$ Federkonstante. $x$ Auslenkung
>
>Für die Rückstellkraft gilt nach Hookschem Gesetz
>$$
>F_{r\ddot uck} = -k_fx 
>$$

Für den Zusammenhang von Energie und Kraft gilt:
$$
E = \int_a^b F
$$
$$
F = -\frac d{dx}E
$$


>[!important] Klassischer Oszillator II
>Bei 2 Atomigen Molekülen:
>reduzierte Masse
>Kreisfrequenz $\omega=\sqrt{\frac{k_f}m}$ 
>Schwingungsperiode $T=\frac{2\pi}\omega$
>Schwingungsfrequenz $\nu = \frac 1T = \frac 1{2\pi} \sqrt{\frac{k_f}m}$
>Es folgt für $x(0)=x_0$ und $v_0 = 0$
>$$
>x(t) = x_0\cos\omega t
>$$
>Für die Geschwindigkeit folgt:
>$$
>v = \sqrt{\frac{2E}{m}-\frac{k_f}mx^2}
>$$

>[!important] Quantenmechanischer Harmonischer Oszillator
>Hamiltonoperator
>$$
\hat H = -\frac{\hbar^2}{2m}\frac{\mathrm d^2}{\mathrm dx^2} + \frac 12k_fx^2
>$$
>Energieniveaus (äquidistant)
>$$
>E_v = (v+\frac 12 )\omega \hbar
>$$
>Mit Schwingungsquantenzahl $v \in \mathbb N_0$
>
>Die Wellenfunktion ist
>$$
>\Psi_v = N_v\cdot H_v(y)\cdot e^{-y^2/2}
>$$
>$y=x/\alpha$
>$\alpha = \sqrt[4]\frac{\hbar^2}{mk_f}$, 
>Normierungskonstante $N_y=(\sqrt\pi2^vv!)^{-\frac12}$
>Hermite Polynome $H_0(y)=1$, $H_1(y)=2y$, $H_2(y)=4y^2-2$
>![[Pasted image 20250810185436.png]]

>[!important] Harmonischer Oszillator - Nichtklassische Aufenthaltswahrscheinlichkeit
>Klassicher Mech. hat maximalauslenkung für Feder
>$$
>P_{nichtklassisch}(v) = 2\int_{y_{max}}^\infty \Psi_v(y)^2dy
>$$
>Nimmt mit v ab



