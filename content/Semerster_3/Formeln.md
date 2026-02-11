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

# GPC Fraktionierung und Maldi TOF
>[!important] Hydrodynamisches Volumen
>$$
>V_h \propto [\eta]\cdot M
>$$
>Mit 
>$$
>[\eta] = 2.5\cdot N_A \frac{V_h}{M}
>$$

>[!important] MALDI TOF
>$$
>\frac mz = 2e\frac U{v^2}
>$$
>z: Ladungszahl (meist 1)

# Glasübergang
>[!example] Latente Schmelzwärme
>Energiemenge um einen Körper ohne Temperaturerhöhung aus dem festen in den flüssigen Zustand zu überführen

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

# Lichtstreuung und Viskosität
>[!important] Rayleigh Streuung von Gasen
>$$
>\frac {I_\theta}{I_0} = \frac{8\cdot \pi^4\cdot \alpha^2\cdot (1+ \cos^2 \theta)}{\lambda^4\cdot r^2}
>$$
>I0 Intensität unpolarisierter einfallender Strahlung
> alpha: Polarisierbarkeit des Moleküls: Proportionalitätskonstante bezogen aufdie Größe des induzierten Dipols

>[!important] Rayleigh Verhältnis
>$$
>R_\vartheta = \frac{V_S\cdot i_\vartheta\cdot r^2}{I_0\cdot f\cdot V_s}
>$$
>![[Pasted image 20260130175101.png]]
>![[Pasted image 20260130175418.png]]

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

>[!important] Intrinsische Viskosität Polymerlösung
>$$
>[\eta] = A_0
>$$

>[!important] Viskosität nach nach Hagen und Poiseulle
>$$
>\eta =\frac{\pi r^4\Delta pt}{8LV}
>$$
>mit delta p: Druckunterschied bei der Kapillare

>[!important] Huggins-Gleichung
>$$
>\frac{\eta_{sp}}c = [\eta] + k_H[\eta]^2c
>$$

>[!important] SChulz-Blaschke Formel
>$$
>	\frac{\eta_{sp}}c = [\eta] + k_{SB}[\eta]\eta_{sp}
>$$

>[!important] Mark-Houwink-Gleichung (monodispers)
>$$
>[\eta] = K\cdot M^a
>$$
>$$
>\log [\eta] = \log K + a\log M
>$$
>Mark-Houwink Koeffizienten können bei bekanntem Molekulargewicht bestimmt werden.

>[!important] EInstein Gleichug für Viskosität
>$$
>[\eta]=\frac{2.5}\rho = \frac {2.5 V \cdot N_A}{M}
>$$

# Molmassenbestimmung
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

>[!important] Polydispersitätsindex
>$$
>PDI = \frac {\overline{M_w}}{\overline{M_n}}
>$$
>PDI=1 => Monodispers

>[!important] Endgruppenanalyse
>$$
>\overline {M_n} = \frac {qw}{n_end}
>$$

>[!important] Kolligative Eigenschaften
>$$
>Y = K\frac NV
>$$
>Y: Kolligative Eigenschaften

>[!warning] c steht in der Molekulargewichtsbestimmung für  die Massekonzentration
>$$
>[c] = \frac gL
>$$
>$$
>c(mol/L) = \frac 1M \cdot c(g/L)
>$$

>[!important] Dampdfdruckosmometrie
>$$
>\frac{\Delta T}{c} = \frac{K\cdot R\cdot T^2}{\rho_l\cdot \Delta H_\nu}\cdot \left( \frac{1}{M_n} + A_2\cdot c + \ldots \right)
>$$
>Für verschiedene Konzentrationen c-> 0

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

# VL-1
>[!example] Polymer
>Besteht aus mehren Makromolekülen

>[!example] Makromoleküle
>bestehen aus vielen molekularen Einheiten welche kovalent verknüpft sind
>![[Pasted image 20260124183423.png]]
>
>Nach IUPAC: Vielfache Wiederholung konstitutioneller Einheiten und so groß, dass sich die Eigenschaften beim Entfernen einiger Einheiten kaum ändern

>[!example] Monomere
>Monomere sind niedermolekulare Substanzen, die durch Polyreaktionen in Polymere überführt werden

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

# VL-3 Radikalische Polymerisation
>[!example] Käfig Effekt
>Nach der Radikalbildungsreaktion halten die Lösemittelmoleküle sie kurzzeitig in einem "Käfig" -> hohe Wahrscheilichkeit für Rekombination
>

>[!important] Radikalausbeute
>$R_{diff}$: Geschwindigkeit der Diffusion aus dem Käfig
>$R_{i}$: Geschwindigkeit inaktivierender Reaktionen
>$R_{Re}$: Geschwindigkeit der Rekombination im Käfig
>$k_{Re}$: Geschwindigkeitskonstante der Radikalrekombination im Käfig
>$[I^* + N_2 + I^*]$: Konzentration der Käfige mit zwei Startradikalen
>$$
>f = \frac{R_{diff}}{R_{diff}+\sum R_i}
>$$
>$$
>R_{Re} = k_{Re} [I^* + N_2 + I^*]
>$$
>Rekombination und andere Reaktionen zwischen den Zerfallsprodukten im Käfig als Reaktionen erster Ordnung anzusehen sind, weil die reaktionspartner nicht erst durch Diffusion Herangeführt werden müssen
>$$
>f =  \frac{R_{diff}}{R_{diff}+\sum R_i} =  \frac{k_{Diff}[I^* + N_2 + I^*]}{k_{diff}[I^* + N_2 + I^*]+\sum k_i[I^* + N_2 + I^*]}= \frac{1}{1 +\frac{\sum k_i}{k_{diff}}}
>$$
>![[Pasted image 20260125173248.png]]

>[!folge] Geringste sterissche Hinderung (Kopf Schwanz)

>[!important] Mayo Gleichung
>Mit Übertragungskonstante $C_T$
>Der letzte Term wird auch Verdünnungsverhältnis genannt
>Die Mayo-Gleichung ist nur anwendbar wenn der Lösungsmittel oder andere Stoff nicht in die Startreaktion eingreift
>$$
>\frac1{X_n}	= \frac{1}{\overline X_{n,0}} + C_T \frac{[XY]}{[M]}\\
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

# VL-4 - Emulsionspolymmersiation
>[!important] HLB
>Nach Griffith
>$$
>HLB = 20\cdot \left( 1- \frac{M_L}{M} \right)
>$$
>ML: Molmasse lipophiler Anteil
>M: Molmasser gesamtes mol
>Nach Davies
>$$
>HLB = 7 + mH_h - nH_l
>$$
>m: Anzahl hydrophile  Gruppen
>Hh: Wert der hydrophilen Gruppen
>ml: Anzahl lipophiler Gruppen im Molekül
>![[Pasted image 20260129113525.png]]

>[!important] Polymerisationsgeschwindigkeit Emulsion
>$$
>v = -\frac{\mathrm d [M]}{\mathrm d t} = k_p [M]_{Latex}[R*]_{Latex}= k_p [M]_{Latex} L \frac{N_{R, Latex}}{N_A}
>$$
>L: Konzentration an Latexpartikeln in der kontinuierliche Phase (Zahl Teilchen pro Volumen der wässrigen
>N_R, Latex = mittlere Zahl der Radikale pro Latexpartikel (wird über die Verteilung der Latexteilchen gemittelt)

>[!important] Radikalkonzentration
>$$
>\frac{N_{R,e}}{V_E} = k \left( \frac{v_{R,e}}{d V_{Lp}/dt} \right)^{\frac 25} (a_sc_s)^{\frac 35}
>$$
>![[Pasted image 20260129120716.png]]

>[!important] Partikelzahl 
>$$
>L = k  [I]^{\frac 25} [S]^{\frac 35}
>$$
>S: Tensidkonzentratiion

# VL-4
>[!important] Chemische Verschiebung
>$$
>\delta = \frac{\nu_{substanz}-\nu_{ref}}{\nu_{ref}}
>$$

# VL-5 Kontrollierte radikalische Polymerisationen
>[!folge] Verringerung der Radikalkonzentration hat einen wesentlich größeren Effekt auf die Geschwindigkeit der Abbruchreaktionen

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

# VL-6 Ionische Polymerisation
>[!important] Mittler Polymerisationsgrad Ionisch
>$$
>\overline X_n =  f_0 \frac{[\Delta M]}{[I]}
>$$
>

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

# VL-8 Polykondensationsreaktionen
>[!important] Carothers Gleichung
>$$
>p = \frac{N_0-N}{N_0}
>$$
>CArothers gleichung :
>$$
>\overline X_n = \frac{N_0}N = \frac 1{1-p}
>$$
>$N_0$ Anzahl reaktiver Gruppen bei Beginn

>[!important] Molmassenverteilung
>$$
>\frac{M_w}{M_n} = 1+p
>$$

>[!important] Xn der idealen AB polykondensation
>$$
>X_n = 1+[M]_0kt
>$$

