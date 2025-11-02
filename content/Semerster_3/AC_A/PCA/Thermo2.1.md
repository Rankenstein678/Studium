## Adiabatische Volumenarbeit
$$
dq=0
$$
- Adiabatische Volumenarbeit: Veränderung des Volumens ohne dass Wärmeaustausch stattfinden darf
-> somit ändert sich (im Normalfall) die Temperatur des Gases (↔ isotherme
Volumenarbeit

$$
dU =dw = -pdV = C_VdT
$$
ideal:
$$
\begin{align}
-\frac{nRT}VdV &= C_VdT\\
&\ldots\\
\frac{V_A}{V_E} &= \left( \frac{T_E}{TA} \right)^{\frac{C_V}{nR}}\\
V_ET_E^{\frac{C_V}{nR}}&=V_AT_A^{\frac{C_V}{nR}}
\end{align}
$$
![[Pasted image 20251031115011.png]]

Für einatomige ideale Gase
Mit der Adiabatenexponenten $\gamma = \frac{C_p}{C_V}$ 
$$
nR = C_p -C_V
$$
$$
T\propto V^{1-\gamma} \qquad \propto V^{-\gamma}
$$

# Carnotscher Kreisprozess
![[Pasted image 20251031120326.png]]

1. isotherme Expansion T = const
$$
\begin{align}
dU &=0\\
dw &= -dq\\
dw &= -pdV\\
w_1 &= - \int_{V_A}^{V_B}\frac{nrT_{hoch}}VdV\\
&= -nRT_{hoch}\ln \left( \frac{V_A}{V_B} \right)\\
q_1 &= \color{red}\mathbb+\ \color{white} nRT_{hoch}\ln \left( \frac{V_A}{V_B} \right)
\end{align}
$$

2. adiabatische Expansion q=0
$$
\begin{align}
dw &= dU = C_VdT\\
w_2 &=C_V(T_{tief}-T_{hoch}) 
\end{align}
$$
3. isotherme Kompression
$$
\begin{align}
w_3 &= -nRT_{tief}\ln \left( \frac{V_D}{V_C} \right)\\
q_3 &= \color{red}\mathbb+\ \color{white} nRT_{hoch}\ln \left( \frac{V_D}{V_C} \right)
\end{align}
$$
4. adiabatische Kompression
$$
\begin{align}
dw &= dU = C_VdT\\
w_4 &=C_V(T_{hoch}-T_{tief}) 
\end{align}
$$
![[Pasted image 20251031121237.png]]

Aus Adiabatengleihchung gesamt:
$$
\begin{align}
w&=w_1 + w_3 + w_2 - w_2\\
&\ldots\\
w &= nR(T_{h}-T_t)\ln \frac{V_A}{V_B}\\
q_{aufgenommen}&=nRT_{hoch}\ln\frac{V_A}{V_B}
\end{align}
$$
$$
\begin{align}
\text{𝑊𝑖𝑟𝑘𝑢𝑛𝑔𝑠𝑔𝑟𝑎𝑑} &= \frac{\text{𝑣𝑒𝑟𝑟𝑖𝑐ℎ𝑡𝑒𝑡𝑒 𝑚𝑒𝑐ℎ𝑎𝑛𝑖𝑠𝑐ℎ𝑒 𝐴𝑟𝑏𝑒𝑖𝑡}}{\text{
𝑎𝑢𝑓𝑔𝑒𝑛𝑜𝑚𝑚𝑒𝑛𝑒 𝑊ä𝑟𝑚𝑒𝑚𝑒𝑛𝑔𝑒}}\\
\eta= \frac{w}q = \frac{T_h-T_t}{T_h}
\end{align}
$$
Je größer Temp diff desto grrößer  wirkungsgrad
 