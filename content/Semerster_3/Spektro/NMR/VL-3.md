Ein ==radiofrequenzpuls== wird uasgesendet um die Magnetisierung prözedieren zu lassen.
Ist er on resonance so gilt:

>[!important] Winkel nach RF
>$$
>\beta =\omega_1\cdot t_P = -\gamma B_1 t_P
>$$

Es gilt die rechte Hand Regel (Jorking it Variante) zur Bestimmung der Kippung des Vektors.

In der Spule wird durch wechselndes Magnetfeld Strom induziert;
==Freier Induktionszerfall== FID
$$
U(t) = \cos(\omega_{local,0}t) \cdot\exp(-t/T_2)
$$
![[Pasted image 20260115165125.png]]

## Das einfachste NMR-Experiment: Einpulsexperiment
![[Pasted image 20260115165239.png]]
- D1: Wiederholungszeit
- P1: Pulslänge
- PLW1: Pulsleistung (in W)
- TD: Anzahl Aquisitionspunkte
- DW: Dwell Time
- NS: Anzahl Scans
Die Pulslänge definiert das Anregungsprofil. Harte Pulse (kleines Δt, großes ω1 ) haben ein breites Anregungsprofil, weiche Pulse (großes Δt, kleines ω1 ) ein schmales Anregungsprofil.

>[!important] SNR
>$$
>SNR \propto I(I+1)\gamma_I^{\frac52} N \sqrt Q B_0^{\frac 32}T^{-\frac 32}\sqrt{NS}
>$$
>Q: Q Faktor
>N: ANzahl spins
>NS Anzahl scan

## Experimente zur Bestimmung von Relaxationszeiten

### T1 -Relaxation: Das “Inversion Recovery” Experiment
![[Pasted image 20260115165720.png]]
### T1 -Relaxation: Das “Saturation Recovery” Experiment
![[Pasted image 20260115170006.png]]

>[!important] Optimales SNR
>Eine Repetitionszeit von 1.3 Mal T 1 ist die beste Wahl für 90º-Pulse für ein optimales SNR/Zeit. Das Spektrum ist dann NICHT mehr quantitativ

### T2 Relaxation: Das Hahn Echo Experiment
![[Pasted image 20260115170325.png]]

## Linienbreite
>[!important] Lininenbreite
>$$
>\Delta_{\frac12} = \frac{1}{\pi T^*_2}
>$$

