- Monomere: Nahezu alle Acrylate und Vinylmonomere
- Initiatoren: Radikalbildner (Azo/Peroxid)
- Lösungsmittel: Nahezu alle aber manche wirken als Überträgerr CCl4
- Temp: 0-130C
- Verfahren: Substanz, Lösung, Emulsion, Dispersion
# Polymerisation in Masse
![[Pasted image 20260125170540.png]]
## Nachteile
- Wärmestau / temperaturgradienten
- mmehrmodale Molmassenverteilung
- Polymerisationsaabruch bei 40-60%
Graph mit Umsatzen
![[Pasted image 20260125170642.png]]
# Polymerisation in Suspension
Hydrophobe Monomertropfen in Wasser
Tropfen werden mit Radikalstarter Polymmerisiert
![[Pasted image 20260125170931.png]]
## Vorteile
- gute Temperaturkontrolle
- geringe Viskosität
- Umhüllungsprozesse möglich
# Lösungspolymerisation
Mono und Polymer sind in LM löslich
![[Pasted image 20260125171039.png]]
## Vorteile
- gute Temperaturkontrolle
- geringe Viskosität
- enge Molmassenverteilung
## Nachteile
- LM muss entfernt werden
- LM beeinflusst Polymerisationsprozess
# Fällungspolymerisation
Monomere sind in LM löslich Polymer aber nicht
![[Pasted image 20260125171203.png]]
# Gasphasen Polymerisation
Reaktionsgeschwindigkeit sinkt mit T
v steigt mit höherem Druck
![[Pasted image 20260125171331.png]]

# Monomere
![[Pasted image 20260125171403.png]]

# Reaktion
## Idealisierte Elementarreaktion
![[Pasted image 20260125171502.png]]

## Initiierung
### Selbstinduzierte 
Bsp Styrol
![[Pasted image 20260125171840.png]]
-> Thermische Polymerisation
- Reines Monomer wird erhitzt -> Radikalbildung![[Pasted image 20260125171623.png]]
	![[Pasted image 20260125171905.png]]
## Radikalbildungsreaktionen
### Homolytische Spaltung
- Thermischer Zerfall von peroxiden
- Thermischer Zerfall von Azoverbindungen
- Zefall durch Licht
- zerfall durch energeitcshe Strahlung (Radiolyse)
![[Pasted image 20260125172039.png]]
![[Pasted image 20260125172109.png]]
### Elektronenübertragung
- Redoxreaktionen

### Problem bei vielen Initiatoren: induzierte Zerfall
![[Pasted image 20260125172156.png]]
## Radikalausbeute
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

## Redox Initiatoren
Redox-Initiatoren erzeugen polymerisationsauslösende Radikale durch Reaktion eines Reduktionsmittels mit einem Oxidationsmittel
## Peroxid + Amin
$$
\ce{(CH3)2NC6H5 + (CH5COO)2 -> [(CH3)2N^*C6H5]+ C6H5COO- + C6H5^*}
$$

## Hydroperoxid + Metallion
$$
\ce{ROOH + Me^{n+}-> RO^* +  Me^{(n+1)+}}
$$
z.B. H2O2 + Fe2+
## Übergangsmetall + organisches Halogenid
$$
\ce{Me^0 + RHal -> MeHal + R^*}
$$

##  Zusammenfassung
![[Pasted image 20260125173621.png]]


# Kettenwachstum und Kettenübertragungen
## Startreaktionen
![[Pasted image 20260125173651.png]]
## Wachstumreaktion
Die Wachstumsgeschwindigkeit ist von der Stabilität des Produkts definiert
![[Pasted image 20260125173809.png]]
Sterische Effekte bestimmen in starkem Maß die Geschwindigkeit und die Orientierung
der Radikaladdition an die Doppelbildung. 
>[!folge] Geringste sterissche Hinderung (Kopf Schwanz)
## Kettenabbruch
![[Pasted image 20260125173930.png]]
## Kettenübertragung
Ohne Übertragung
$$
\overline X_{n,0} = \frac{v_{w}}{v_{ab}}
$$
Mit Übertragung
$$
\overline X_n = \frac{v_w}{v_{ab}+v_{üb}}
$$
#### Mayo Gleichung
$$
\begin{align}
\overline X_n &= \frac{k_w [P*][M]}{k_{ab}[P*]^2 + k_{üb}[P*][XY]}\\
\frac1 {\overline X_n}&=\frac{k_{ab}[P*]^2 + k_{üb}[P*][XY]}{k_w [P*][M]}\\
&=\frac{k_{ab}[P*]^2 }{k_w [P*][M]}+ \frac{ k_{üb}[P*][XY]}{k_w [P*][M]}\\
	&= \frac{1}{\overline X_{n,0}} + \frac{k_{üb}}{k_{w}} \frac{[XY]}{[M]}\\
	&= \frac{1}{\overline X_{n,0}} + C_T \frac{[XY]}{[M]}\\
	
\end{align}
$$
>[!important] Mayo Gleichung
>Mit Übertragungskonstante $C_T$
>Der letzte Term wird auch Verdünnungsverhältnis genannt
>Die Mayo-Gleichung ist nur anwendbar wenn der Lösungsmittel oder andere Stoff nicht in die Startreaktion eingreift
>$$
>\frac1{X_n}	= \frac{1}{\overline X_{n,0}} + C_T \frac{[XY]}{[M]}\\
>$$

![[Pasted image 20260125174939.png]]
![[Pasted image 20260125174954.png]]

Wenn küb = k_bü -> Überträger
k_üb > r_bü -> Retarder
k>üb >> Inhibtor

# Inhibitor
Radikalfänger, die selbst inaktive Radikale bilden
Stabilisatoren zur Monomerstabilisierung
![[Pasted image 20260125175645.png]]
# Kinetik
![[Pasted image 20260125175759.png]]
Mit Bodenstein Gilt
$$
[P*] = const. \quad R_d=R_a
$$
$$
\begin{align}
2\,f\,k_d\,[I_2] &= 2\,k_a\,[P^*]^2\\
[P*] &= \sqrt{f\frac{k_d}{k_a}[I_2]}\\
R_w &= k_w \sqrt{f\frac{k_d}{k_a}[I_2]} [M]\\
&= k_w \sqrt{f\frac{k_d}{k_a}} \sqrt{[I_2]} [M]
\end{align}
$$
![[Pasted image 20260125180337.png]]

![[Pasted image 20260125180344.png]]
![[Pasted image 20260125180404.png]]
![[Pasted image 20260125180417.png]]
![[Pasted image 20260125180424.png]]
