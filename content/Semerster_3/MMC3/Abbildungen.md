Allg:
$$
\vec y = A\vec x
$$
$$
A \in \mathbb R^{m\times n}, \quad a_{ij}\in\mathbb R
$$

# Lineare Abbildungen
![[Pasted image 20260220211020.png]]
y: Bildvektor
"Skalarprodukt: Zeile mal Spalte"
A: Abbildungsmatrix

Beispiel: Rotation 90
$$
A = \begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$
![[Pasted image 20260220211238.png]]

## Abbildungsmatrix berechnen
![[Pasted image 20260220211810.png]]
![[Pasted image 20260220211816.png]]
![[Pasted image 20260220211829.png]]
![[Pasted image 20260220211835.png]]

![[Pasted image 20260220211902.png]]
# Orthogonale Matrizen
- Spaltenvektoren sind normmiert und orthogonal (paarweise)
- daraus ffolgt gleiches für zeilenvektoren
- spiegelungen und rotatiionen sind orthogonal
- streckungen nicht
- Abstände und winkel bleiben erhalten

![[Pasted image 20260220212118.png]]

### Symmetrische Matrizen 
$$
A=A^T
$$
### Multiplikation
Matrixmultiplikation nicht kommutativ, da nur bei gleicher Spalttenzahl von A zur Zeilenzahl von B

# Inverse Matrix
Eine matrix heißt invertierbar / ==Regulär== wenn
$$
\exists A^{-1} : A\cdot A^{-1} = I_n
$$
In: Einheitsmatrix
Nicht invertierbar: ==Singulär==

![[Pasted image 20260221163333.png]]
# ORthogonale Matrix
$$
A^T=A^{-1}
$$
![[Pasted image 20260221163645.png]]
# Determinanten
3x3:
![[Pasted image 20260221164156.png]]
nxn:
Von Links oben nach rechts abwechseln +/- dran schreiben.
Zeile mit den Meisten nullen wählen.
Element von Zeile * determinante von Matrix ohne Zeile und spalte

- Ist eine Zeile vertauscht dann $det(A) = -det(B)$
- $det(A\cdot B) = det(A)\cdot det(B)$
