Mehrdimensionale Schrödingergleichung können Teilweise durch Separation gelöst werden. Dazu wird der Hamilton Operator gespalten und ein Separationseinsatz genutzt.

## Beispiel: Teilchen im 2D kasten

$$
\begin{align}
    E_{kin} &= \frac{p^2}{2m}\\
    p^2 &= |p|^2 = \left(\sqrt{p_x^2+p_y^2}\right)^2\\
    &=p_x^2+p_y^2\\
    E_{kin} &= \frac{p_x^2+p_y^2}{2m}\\
    \hat H &= -\frac{\hbar^2}{2m}\frac{\partial}{\partial x} - \frac{\hbar^2}{2m}\frac{\partial}{\partial y}\\
    &= \hat H_x + \hat H_y
\end{align}
$$
Mit dem Ansatz $\Psi(x,y) = \Psi_x(x)\cdot \Psi_y(y)$ folgt
$$
\begin{align}
\frac{\hat H_x\Psi_x}{\Psi_x} = \epsilon_x\\
\frac{\hat H_y\Psi_y}{\Psi_y} = \epsilon_y\\
\epsilon = \epsilon_x+\epsilon_y
\end{align}
$$
>[!important] Zeitabhängige Schrödingergleichung
>$$
>i\hbar \frac{\partial}{\partial t}\Psi(x,t) = \hat H\Psi(x,t)
>$$
>Ist der Hamiltonoperator zeitunabhängig ist die Gelichung mit $\Psi(x,t) = \Psi(x)\cdot f(t)$ separierbar
>Es folgt:
>$$
>\Psi(x,t) = C_0\Psi(x)e^{-{iEt}/\hbar}
>$$
>Mit $C_0=exp(-i\varphi)$ folgt alternativ
>$$
>\Psi(x,t) = \Psi(x)\cdot e^{-i({Et}/\hbar + \varphi)} 
>$$ 

# Interpretation
Ein Zeitabhängiger Quantenmechanischer Oszillator schwingt ==nicht==
Durch Linearkombination von Eigenzuständen kann sich ein Quantensystem in einem schwingenden Superpositionszustand aufhalten ??????? (tf)