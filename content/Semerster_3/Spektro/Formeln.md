# Fluoreszenz
>[!important] Fluoreszenzquantenausbeute
>$$
>\phi_f = \frac{N_{emit}}{N_{abs}}=\frac{k_f}{\sum k_{alle}} = \frac{k_F}{k_F+k_{IC}+k_{ISC}} = k_F \cdot \tau_F
>$$
>Fluoreszenzlebensdauer $\tau_F$: Wie lange lebt S1

>[!warning] Aber:
>Nicht sehr genau $(\pm 5 \%)$

>[!important] Parker-Rees:
>$$
>\frac{\phi_P}{\phi_R} = \frac{F_P}{F_R}\cdot \frac{I_{0,R}}{I_{0,P}}\cdot \frac{1-10^{-A_R}}{1-10^{-A_P}}\cdot \frac{n^2_P}{n^2_R}
>$$
>$I_0$ Anregungsintensität
>zweiter Term: Anteil der Lichtenergie, der in der Probe absorbiert wird (idealerweise gleich mit A <0.1)
>n: Brechungsindizes

>[!important] FRET Rate
>$$
>k_{FRET} = \frac 1{\tau_{f,0}(Donor)}\left(\frac{R_0}{R_{Donor\_Akzeptor}}\right)^6
>$$

>[!important] FRET Effizienz
>Wie viel der angeregten Zustände geben Ihre Energie an den FRET-Akzeptor ab?
>$$
>\eta_{FRET} = \frac{k_{FRET}}{k_{FRET}+k_{sonst}}=\frac{1}{1+ \frac{k_{sonst}}{k_{FRET}}} = \frac1{1+ \left(\frac{R_{Donor\_Akzeptor}}{R_0}\right)^6}
>$$

# Formeln
>[!important] Winkel nach RF
>$$
>\beta =\omega_1\cdot t_P = -\gamma B_1 t_P
>$$

>[!important] SNR
>$$
>SNR \propto I(I+1)\gamma_I^{\frac52} N \sqrt Q B_0^{\frac 32}T^{-\frac 32}\sqrt{NS}
>$$
>Q: Q Faktor
>N: ANzahl spins
>NS Anzahl scan

>[!important] Optimales SNR
>Eine Repetitionszeit von 1.3 Mal T 1 ist die beste Wahl für 90º-Pulse für ein optimales SNR/Zeit. Das Spektrum ist dann NICHT mehr quantitativ

>[!important] Lininenbreite
>$$
>\Delta_{\frac12} = \frac{1}{\pi T^*_2}
>$$

>[!important] Spektren höherer Ordnung
>Ab:
>$$
>k = \left | \frac{\nu_A -\nu_X}{J(A,X)}\right| < 10
>$$

>[!important] Koaleszenz
>$$
>\frac{\sqrt 2 k_{ex}}\pi =  \nu_1-\nu_2
>$$

>[!important] Doppelbindungsäquivalente
>$$
>DB\ddot A = \frac{2\cdot n_C - n_H + n_N + 2}{2}
>$$
>𝑛𝐶 : Anzahl Kohlenstoffatome
>𝑛𝐻: Anzahl Wasserstoffatome (auch Halogene)
>𝑛𝑁: Anzahl Stickstoffatome
>Auch ein Ring zählt als 1 DBÄ

>[!important] Multiplizität
>$$
>M=2\cdot n \cdot I +1
>$$
>I: Kernspinquantenzahl
>n: Anzahl benachbarter chemisch nicht-äquivalenter Kerne

>[!important] Chemische Verschiebung
>$$
>\delta = \frac{\nu_{substanz}-\nu_{ref}}{\nu_{ref}}
>$$

>[!important] Die gyromagnetische Beziehung
>Ein Kernspin erzeugt ein magnetisches Moment:
>$$
>\vec {\mu_N} =  \gamma_N \vec I
>$$
>$\gamma_𝑁$ : gyromagnetisches Verhältnis

>[!important] Zeeman WW
>$$
>\hat{\mathcal {H}_Z} = -\gamma B_0\hat I_Z
>$$

>[!important] Larmor Frequenz
>$$
>\omega_0 =2\pi\nu_0= -\gamma B_0
>$$

>[!important] Resonanzbedingung
>$$
>\Delta E = -\hbar\omega_0
>$$

>[!important] Makroskopische Magnetisierung
>$$
>\vec M  = \frac 1V \vec m =  \left[ \frac Am \right]
>$$

>[!important] $T_1$ Relaxation
>$$
>M_z(t) = M_0\left(1-\exp\left(-\frac t{T_1}\right)\right)
>$$

>[!important] $T_2$ Relaxation
>$$
>\frac 1{T_2^*} = \frac 1{T_2} + \frac 1{T_2^\prime}
>$$

>[!important] Fluoreszenzquantenausbeute
>$$
>\phi_f = \frac{N_{emit}}{N_{abs}}=\frac{k_f}{\sum k_{alle}} = \frac{k_F}{k_F+k_{IC}+k_{ISC}} = k_F \cdot \tau_F
>$$
>Fluoreszenzlebensdauer $\tau_F$: Wie lange lebt S1

>[!warning] Aber:
>Nicht sehr genau $(\pm 5 \%)$

>[!important] Parker-Rees:
>$$
>\frac{\phi_P}{\phi_R} = \frac{F_P}{F_R}\cdot \frac{I_{0,R}}{I_{0,P}}\cdot \frac{1-10^{-A_R}}{1-10^{-A_P}}\cdot \frac{n^2_P}{n^2_R}
>$$
>$I_0$ Anregungsintensität
>zweiter Term: Anteil der Lichtenergie, der in der Probe absorbiert wird (idealerweise gleich mit A <0.1)
>n: Brechungsindizes

>[!important] FRET Rate
>$$
>k_{FRET} = \frac 1{\tau_{f,0}(Donor)}\left(\frac{R_0}{R_{Donor\_Akzeptor}}\right)^6
>$$

>[!important] FRET Effizienz
>Wie viel der angeregten Zustände geben Ihre Energie an den FRET-Akzeptor ab?
>$$
>\eta_{FRET} = \frac{k_{FRET}}{k_{FRET}+k_{sonst}}=\frac{1}{1+ \frac{k_{sonst}}{k_{FRET}}} = \frac1{1+ \left(\frac{R_{Donor\_Akzeptor}}{R_0}\right)^6}
>$$

>[!important] Leistungsabfall in Probe
>$$
>P = P_0 \cdot e^{-\sigma_A\frac NV d} \color{purple} \cdot X
>$$
>Mit X: Transmissionseffizienz“ (Streuung und Reflexion)

>[!important] Transmittanz
>$$
>T_{int} = \frac{\text{Leistung Probe}}{\text{Leistung Referenz}}= \frac{P_P}{P_0\cdot X} = \frac{T_{total}}X = \frac{P_P}{P_R2}= e^{-\sigma_A\frac NV d}
>$$ 
>$$
>= 10^{-\frac 1{\ln 10}\sigma_A\frac NV d} =10^{-\epsilon cd} = 10^{-A}
>$$
>Absobanz A, molarer dekadischer Absorptionskoeffizient $\epsilon$
>$$
>A = -\log_{10} \frac{P_P}{P_R} = -\log_{10} T_{intern} = \epsilon cd
>$$

>[!important] Wichtiger praktischer Hinweis: 
>Bei Absorptionsmessungen sollte der Konzentrationsbereich so eingestellt werden, dass die Transmission zwischen 1% und 99% liegt

>[!important] Energie einer (IR) Schwingung
>$$
>\nu = \frac 1{2\pi}\sqrt{\frac{D}\mu}
>$$
>Mit 
>$$
>\frac 1\mu = \frac 1{m_1} + \frac 1{m_2}
>$$

>[!important] N Schwinugnen
>Linear
>$$
>3N -5
>$$
>n-Linear
>$$
>3N-6
>$$

# IR
>[!important] Energie einer (IR) Schwingung
>$$
>\nu = \frac 1·{2\pi}\sqrt{\frac{D}\mu}
>$$
>Mit 
>$$
>\frac 1\mu = \frac 1{m_1} + \frac 1{m_2}
>$$

>[!important] N Schwinugnen
>Linear
>$$
>3N -5
>$$
>n-Linear
>$$
>3N-6
>$$

# UV-VIS
>[!important] Leistungsabfall in Probe
>$$
>P = P_0 \cdot e^{-\sigma_A\frac NV d} \color{purple} \cdot X
>$$
>Mit X: Transmissionseffizienz“ (Streuung und Reflexion)

>[!important] Transmittanz
>$$
>T_{int} = \frac{\text{Leistung Probe}}{\text{Leistung Referenz}}= \frac{P_P}{P_0\cdot X} = \frac{T_{total}}X = \frac{P_P}{P_R2}= e^{-\sigma_A\frac NV d}
>$$ 
>$$
>= 10^{-\frac 1{\ln 10}\sigma_A\frac NV d} =10^{-\epsilon cd} = 10^{-A}
>$$
>Absobanz A, molarer dekadischer Absorptionskoeffizient $\epsilon$
>$$
>A = -\log_{10} \frac{P_P}{P_R} = -\log_{10} T_{intern} = \epsilon cd
>$$

>[!important] Wichtiger praktischer Hinweis: 
>Bei Absorptionsmessungen sollte der Konzentrationsbereich so eingestellt werden, dass die Transmission zwischen 1% und 99% liegt

# VL-2
>[!important] Die gyromagnetische Beziehung
>Ein Kernspin erzeugt ein magnetisches Moment:
>$$
>\vec {\mu_N} =  \gamma_N \vec I
>$$
>$\gamma_𝑁$ : gyromagnetisches Verhältnis

>[!important] Zeeman WW
>$$
>\hat{\mathcal {H}_Z} = -\gamma B_0\hat I_Z
>$$

>[!important] Larmor Frequenz
>$$
>\omega_0 =2\pi\nu_0= -\gamma B_0
>$$

>[!important] Resonanzbedingung
>$$
>\Delta E = -\hbar\omega_0
>$$

>[!important] Makroskopische Magnetisierung
>$$
>\vec M  = \frac 1V \vec m =  \left[ \frac Am \right]
>$$

>[!important] $T_1$ Relaxation
>$$
>M_z(t) = M_0\left(1-\exp\left(-\frac t{T_1}\right)\right)
>$$

>[!important] $T_2$ Relaxation
>$$
>\frac 1{T_2^*} = \frac 1{T_2} + \frac 1{T_2^\prime}
>$$

# VL-3
>[!important] Winkel nach RF
>$$
>\beta =\omega_1\cdot t_P = -\gamma B_1 t_P
>$$

>[!important] SNR
>$$
>SNR \propto I(I+1)\gamma_I^{\frac52} N \sqrt Q B_0^{\frac 32}T^{-\frac 32}\sqrt{NS}
>$$
>Q: Q Faktor
>N: ANzahl spins
>NS Anzahl scan

>[!important] Optimales SNR
>Eine Repetitionszeit von 1.3 Mal T 1 ist die beste Wahl für 90º-Pulse für ein optimales SNR/Zeit. Das Spektrum ist dann NICHT mehr quantitativ

>[!important] Lininenbreite
>$$
>\Delta_{\frac12} = \frac{1}{\pi T^*_2}
>$$

# VL-4
>[!important] Chemische Verschiebung
>$$
>\delta = \frac{\nu_{substanz}-\nu_{ref}}{\nu_{ref}}
>$$

# VL-5
>[!important] Doppelbindungsäquivalente
>$$
>DB\ddot A = \frac{2\cdot n_C - n_H + n_N + 2}{2}
>$$
>𝑛𝐶 : Anzahl Kohlenstoffatome
>𝑛𝐻: Anzahl Wasserstoffatome (auch Halogene)
>𝑛𝑁: Anzahl Stickstoffatome
>Auch ein Ring zählt als 1 DBÄ

>[!important] Multiplizität
>$$
>M=2\cdot n \cdot I +1
>$$
>I: Kernspinquantenzahl
>n: Anzahl benachbarter chemisch nicht-äquivalenter Kerne

# VL-6
>[!important] Spektren höherer Ordnung
>Ab:
>$$
>k = \left | \frac{\nu_A -\nu_X}{J(A,X)}\right| < 10
>$$

>[!important] Koaleszenz
>$$
>\frac{\sqrt 2 k_{ex}}\pi =  \nu_1-\nu_2
>$$

