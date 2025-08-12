>[!important] Rydbergformel für das Wasserstoffatom
>Einzelne Energieniveaus:
>$$
>E_n = -hcR_H\frac1{n^2}
>$$
>$$
>h\nu_{nm} = hcR_H\left(\frac1{n^2}-\frac 1{m^2}\right)
>$$
>Rydbergkonstante Wasserstoff: $R_H = 109677 \mathrm{cm}^{-1}$


>[!important] Schrödingergleichung Wasserstoffatom
>Modell: Kern im 3D Ursprung und $\vec r = (x,y,z)$
>Klassisch
>$$
>E_{kin} = \frac{\vec p^2}{2m} = \frac{p_x^2+p_y^2+p_z^2}{2m}
>$$
>$$
>E_{pot} = - \frac{e^2}{4\pi\epsilon_0} \frac{1}{r} \quad \text{mit}\quad r=\sqrt{x^2+y^2+z^2}
>$$
>Nichtklassich
>Hamilton:
>$$
>\begin{align}
>\hat H &= -\frac{\hbar^2}{2m}\left(\frac{\partial}{\partial x}+\frac{\partial}{\partial y}+\frac{\partial}{\partial z}\right) - \frac{e^2}{4\pi\epsilon_0 r}\\
>&= -\frac{\hbar^2}{2m}\nabla^2- \frac{e^2}{4\pi\epsilon_0 r}\\
>\end{align}
>$$
>Es folt nach umstellen auf Kugelkoordinaten
>$$
>\Psi_{n\ell m_\ell} = R_{n\ell}(r)\cdot Y_{\ell m_\ell}(\vartheta, \varphi)
>$$
>Mit Quantenzahl $n\in \mathbb N$, Nebenquantenzahl $\ell=0,1,\ldots,n-1$, Magnetquantenzahl $m_\ell= 0,\pm 1,\ldots, \pm \ell$
>$$
>E_n = -hcR_\infty\frac 1{n^2}
>$$
>mit $hcR_\infty=13.6 eV$ oder $R_\infty=109737 cm^{-1}$ 
>Entartung der Zustände mit gleicher Hauptquantenzahl

>[!important] Radialteil
>Bei Kernbewegung wird im Bohrschen Radius die reduzierte Masse eingesetzt
>![[Pasted image 20250811231607.png]]
>Wahrscheinlichkeitsbestimmung
>Bei dder Verwendung von Kugelkoordinaten folgt für das VOlumenelement
>$$
>r^2\sin(\vartheta)d\vartheta d\varphi
>$$
>Für die Radiale Verteilunggsfunktion abhängig von abstand folgt
>$$
>\begin{align}
>p(r) &= \int_0^{2\pi}\int_0^\pi |\Psi(r,\vartheta,\varphi)|^2 r^2\sin(\vartheta)d\vartheta d\varphi\\
>p(r) &= R(r)^2 r^2 \int_0^{2\pi}\int_0^\pi Y(\vartheta,\varphi)\sin(\vartheta)d\vartheta d\varphi\\
>&=R(r)^2r^2\cdot 1
>\end{align}
>$$
>Dementsprechend bedeutet eine Normierung $\int_0^\infty R(r)^2 r^2dr=1$


>[!important] Terme
>$$
>T_n = \frac{E_n}{hc}
>$$
>Wellenzahl bei Emission ($\color{red}\text{in cm} ^{-1}$)
>$$
>\tilde \nu = |T_2-T_1|
>$$

>[!important] Wasserstoffatom mit Kernbewegung
>Vereinfachung auf Kernladung (also Kationen)
>$$
>\hat H = -\frac{\hbar^2}{2m} \nabla^2_e  -\frac{\hbar^2}{2m}\nabla^2_K- \frac{Ze^2}{4\pi\epsilon_0r}
>$$
>Nach Separation von Kern und Elektronenkoordinaten folgt
>$$
>E_n = -hcR_K\frac{Z^2}{n^2}\quad \text{mit}\quad hcR_K = \frac12\frac{\mu_Ke^4}{(4\pi\epsilon_0)^2\hbar^2} 
>$$
>mit $\mu_K = \frac{m_Km_e}{m_K+m_e}$


