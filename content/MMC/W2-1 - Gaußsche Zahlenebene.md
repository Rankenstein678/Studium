# Polardarstellung
Komplexe Zahlen haben ==keine== Ordnung. Deshalb Zahlenebene nach Gauß
![[Pasted image 20241229175604.png]]

>[!important] Def: Betrag einer komplexen Zahl
> Wenn $z = x + yi$, dann
> $$
> |z| = \sqrt{x^2+y^2}
> $$
> oder 
> $$
> |z|^2 = z \cdot \overline z
> $$


> [!important] Def: Polardarstellung
> Eine komplexe Zahl $z = x +yi$ kann mithilfe ihres Betrags und des Winkels $\varphi$ dargestellt werden:
> $$
> z = r \left(\cos(\varphi) + i \sin(\varphi)\right)
> $$
> oder 
> $$
> z = r e^{i\varphi}
> $$
> Mit $r := |z|$ und $\varphi := \angle \left(\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}x\\y\end{pmatrix}\right)$


> [!important] Def: Konjugiert komplexe Zahlen
> $$
> \overline z = x - iy = |z|(\cos(\varphi)-i\sin(\varphi)) = re^{-i\varphi}
> $$

Eine Addition entspricht einer Vekoraddition in der Zahlenebene
Eine Multiplikation einer Drehstreckung
>[!warning] Unwandlung polardarstellung in x,y Koordinaten
>Im 1. Quadranten: $\frac {|y|}{|x|} = \tan(\varphi)$ 
>Im 2. Quadranten: $\frac {|y|}{|x|}= 90°+\tan(\varphi)$ 
>Im 3. Quadranten: $\frac {|y|}{|x|}= 180°+\tan(\varphi)$ 
>Im 4. Quadranten: $\frac {|y|}{|x|}= 270°+\tan(\varphi)$ 

