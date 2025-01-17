Gibt an einen Stoff konzentriert in Lösung, so verteilt sich dieser Stoff mit der Zeit.  Dieser Prozess wird als ==Diffusion== bezeichnet.    
# 1. Konzentrationsgradient
$$
\frac{dc}{dx}<0
$$
Das Gefälle vom Punkt mit der initial höchsten Konzentration wird als der Konzentrationsgradient bezeichnet

# 2. Der Fluss
Der Fluss bezeichnet die Durch eine Fläche Fließende Stoffmenge pro Zeiteinheit
$$
J = \frac{\textit{Stoffmenge}}{\textit{Fläche}\cdot\textit{Zeit}}
$$
Der Fluss ist immer Proportional zum Konzentrationsgradienten
$$
J \propto\frac{dc}{dx}
$$
# 3. Das Erste Ficksche Gesetz
$$
J = -D\frac{dc}{dx}
$$
Mit: D als Diffusionskonstante $[D] = \dfrac{m^2}{s}$ 
Das negative Vorzeichen kommt daher, dass der Fluss positiv ist
# 4.  Chemisches Potential
Allgemein gilt Für eine Kraft F und eine Energie / ein potenzial W"

$$
F = - \frac{dw}{dx}
$$
Die treibende Kraft der Diffusion ist das chemische Potential bei konstantem Druck und Temperatur (anngegeben durch den Index)
$$
F = - \left(\frac{\partial\mu}{\partial x}\right)_{p,T}
$$
# 5. Zeitabhängigkeit der Diffusion
## 5.1 Das 2. Fick'sche Gesetz
$$
\frac{\partial c}{\partial t} = D\frac{\partial^2c}{\partial x^2}
$$
# 5.1.1 Herleitung
![[Pasted image 20250117191545.png]]
Es strömen in das Volumen ein: $JAdt$
$$
\left(\frac{\partial c}{\partial t}\right)_{x=x} = \color{red}\frac{JAdt}{Al\color{white}dt}\color{white} = \frac{J}{l}
$$
Mit dem roten als $\partial c$

Es strömt aus $J^\prime Adt$
$$
\left(\frac{\partial c}{\partial t}\right)_{x=x+l=x^\prime} =- \frac{J^\prime A\,dt}{Al\,dt} = -\frac{J^\prime}{l}
$$
Für die Gesamtkonzentrationsänderung gilt
$$
\frac{\partial c}{\partial t} = \frac{J-J^\prime}{l}
$$
$$
J-J^\prime = -D\frac{dc}{dx} + D\frac{dc^\prime}{dx}= -D\frac{dc}{dx} + D \frac{\partial}{\partial x}\left(c + \frac{dc}{dx}l\right) = Dl\frac{\partial^2c}{\partial x^2}
$$
Q.E.D
#### Lösungen des 2. Fick'schen Gesetzes                                                
1. Bsp: Diffusion von x0 in beide Richtungen                                                
	 ![[Pasted image 20241126224245.png]]                                                
Es gilt:                                               
$$                                              
c(x,t) = \frac{n_0}{2 A \sqrt{\pi D t}}e^{-x^2/(4 D t)}                                              
$$                                              
2. Wand zwischen zwei Volumina wird entfernt                                          	                                        
$$                                        
c(x,t)=\frac{c_0}{2}\left(1- \frac{2}{\sqrt{\pi}}\int_0^{x/(2\sqrt{D t)}} e^{-\beta^2} d\beta \right)                                        
$$                                        
Hierbei taucht die sogenannte "Error Funktion auf"                                          	                                        
$$                                        
erf(z) = \frac{2}{\sqrt{\pi}}\int_0^{z} e^{-y^2} dy                                        
$$                                        
3. Bsp.: bei dreidimensionalem Konzentrationsgradienten und Kugelsymmetrie                                          	                                        
$$                                        
c(r,t) = \frac{n_0}{8(\pi D t)^{3/2}}e^{-r^2/(4 D t)}                                        
$$                                            
# 6. Der Random Walk
# 6.1 1D
Es seien
- N: Anzahl der Schritte
- V: Anzahl Vorwärtsschritte
- R: Anzahl Rückwärtsschritte
- p,q WKeit für V/R
Dann gilt nach der Binomialverteilung
$$
W(N,V) = \frac{N!}{V!R!}p^Vq^R
$$
Es gilt:
$$
N = V+R
$$
Für die Entfernung vom Ursprung
$$
V-R = m
$$
Es folgt:
$$
\begin{align}
V = \frac{N+m}2 && R = \frac{N-m}2
\end{align}
$$
eingesetzt folgt
$$
W(N,V) = \frac{N!}{\frac{N+m}2!\frac{N-m}2!}p^{\frac{N+m}2}q^\frac{N-m}2
$$
Für q und p
$$
\begin{align}
p+q = 1 && p=q=\frac12
\end{align}
$$
Mit der Stirling Näherung folgt:
$$
N! = \sqrt{2\pi N} N^Ne^{-N}
$$
(Do not ask Why und ich werde das nicht ausrechnen) 
$$
	W(N,x) = \left( \frac1{2\pi Nl^2} \right)^\frac12e^{-\dfrac{x^2}{2Nl^2}}
$$
Mit $x = m\times l$ (Anzahl Vorwärtsschritte * Schrittlänge)

## 6.2 3D
3D Random Walk                              
Um die Wahrscheinlichkeit in einem 3D Raumvolumen zu berechnen ersetzen wir zunächst x durch den Vektor $\vec R$. Außerdem teilen wir jeder Raumrichtung $N_{x,y,z} = \frac{N}{3}$ Schritte zu.                              
$$                              
W(N,\vec R) = \left(\left(\frac{1}{2\pi \frac{N}{3}l^2}\right)^\frac{1}{2}\right)^3 e^{\dfrac{-3x^2}{2Nl^2}}e^{\dfrac{-3y^2}{2Nl^2}}e^{\dfrac{-3z^2}{2Nl^2}}                              
$$                              
Die Quadratwurzel und die "e"s lässt sich vereinfachen zu:                              
$$                              
W(N,\vec R) = \frac{3}{2\pi Nl^2}^\frac{3}{2} e^{\dfrac{- 3(x^2+y^2+z^2)}{2Nl^2}}                              
$$                              
Der Exponent der eulerschen Zahl entspricht dem quadratischem Betrag des Vektors                              
$$                            
W(N,\vec R) = \frac{3}{2\pi Nl^2}^\frac{3}{2} e^{\dfrac{-3 |\vec R|^2}{2Nl^2}}                            
$$                            
Mit dem infinitessimalen Volumenelement $d\vec R$ gelangt man zu folgender Formel: 

>[!important] Random Walk: Wahrscheinlichkeit sich in einem gewissen Volumenelement auzuhalten                              
>$$                              
>W(N,\vec R)d\vec R = \frac{3}{2\pi Nl^2}^\frac{3}{2} e^{\frac{-3 |\vec R|^2}{2Nl^2}} d\vec R                              
>$$                              

### 3D Random Walk nach Abstand                              
Will man hingegen die Wahrscheinlichkeit für ein Aufhalten im Abstand R berechnen so benutzt man die Oberfäche einer 1D Kugelschale $O=4\pi R^2$ und die Dicke $dR$                              
>[!important] Random Walk: Wahrscheinlichkeit sich in einem gewissen Abstand R auzuhalten                              
>$$                              
>W(N,R)dR = \frac{3}{2\pi Nl^2}^\frac{3}{2} e^{\frac{-3 |\vec R|^2}{2Nl^2}} 4\pi R^2  dR                              
>$$                              Mittlerer quadratischer Abstand $\langle R^2 \rangle$                              
Als Ansatz gilt                               
$$                              
\langle R^2\rangle=\int^\infty_0 R^2 W(N,R) dR                              
$$                              
Durch einsetzen und Ausrechnen folgt:                              
> [!important] Random Walk: Mittlerer Quadratischer Abstand                              
> $$                              
>\langle R^2\rangle = Nl^2                              
>$$                              
                          ### Die Selbstdiffusion                              
Beschreibt die Bewegung eines Teilchens in der Umgebung identischer Teilchen. Bsp:                              
- Wassermolekül im Wasser                              
- Fehlstelle im Kristall                              
Kann mit folgenden Paramtern durch die Irrflugsstatistik beschrieben werden:                              
- $\lambda$: Die Schrittlänge                              
- $\tau$: Die Schrittdauer                              
- $N = t/\tau$: Die Schrittzahl                              
Es folgt:                              
$$                            
\langle r^2\rangle = \frac{t\lambda^2}{\tau}                            
$$                            
Mit $D=\dfrac{\lambda^2}{6\tau}$ folgt:                              
> [!important] Selbstdiffusion: Mittlerer Quadratischer Abstand                              
> $$                              
> \langle r^2\rangle = \frac{t\lambda^2}{\tau}                              
> $$                              
> $$                              
> \sqrt{\langle r^2\rangle} = \sqrt{6Dt}                              
>$$                              
                              
Es gilt da ==Wurzel T Gesetzt==                              
=> Für Weglängen gilt:                              
>[!important] Wurzel T Gesetz                              
>$$                              
>\langle R \rangle \propto \sqrt{t}                              
>$$                              
                              
## Brown'sche Teilchenbewegung                              
Befindet sich ein Teilchen in einem anderen Stoff so erfährt es durch Kollisionen mit anderen Teilchen eine zeitliche variierende Kraft. Es wird von folgenden Bedingungen ausgegangen:                              
- rundes Teilchen in Flüssigkeit eingebettet                              
- bei unendlicher Verdünnung (Konzentration c = 0)                              
Es gilt die                              
> [!important] Brown'sche Teilchenbewegung: Stokes-Einstein-Gleichung                              
> $$                              
> D = \dfrac{k_BT}{f} = \dfrac{k_BT}{6\pi\eta r}                              
> $$                              
> - $r : \textit{Kugelradius}$                              
>- $\eta : \text{\it Viskosität der Flüssigkeit}$                              
>- $F(t) : \textit{Kraft}$                              
>- $f : \text{\it Reibungskoeffizient}$                              
>- $k_B : \text{\it Boltzmann Konstante}$                              
                              
Fluktuations-Dissipations-Theorem                              
                              
## Einstein'sches Verschiebungsquadrat                              
Die Teilchenbewegung lässt sich durch den Random Walk beschreiben. Es gilt:                              
> [!important] Einstein'sches Verschiebungsquadrat                              
> $$                              
> \langle x^2 \rangle = \left\{\begin{matrix}   2Dt & (1D)\\   4Dt&(2D) \\ 6Dt & (3D)   \end{matrix}\right.                              
                              
