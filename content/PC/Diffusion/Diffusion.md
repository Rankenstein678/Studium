Gibt an einen Stoff konzentriert in Lösung, so verteilt sich dieser Stoff mit der Zeit.  Dieser Prozess wird als ==Diffusion== bezeichnet.
                                                  
### Konzentrationsgradient                                                  
Das Gefälle zwischen dem Punkt mit der initial höchsten Konzentration und einem Punkt im Abstand $x$ heißt ==Konzentrationsgradient==                                                  
Für den Konzentrationsgradienten gilt:                                                  
$$                                                
\dfrac{dc}{dx} < 0                                                
$$                                                
                                                  
### Der Fluss $J$                                                  
Der Fluss bezeichnet die Stoffmenge die eine gewisse Fläche in einer gewissen Zeit durchfließt:                                                  
$$                                                  
\textit{Fluss} = \dfrac{\textit{Stoffmenge}}{\textit{Fläche} \cdot \textit{Zeit}}                                                  
$$                                                  
Der Fluss ist proportional zur Konzentrationsgradienten:                                                  
$$                                                  
J \propto \dfrac{dc}{dx}                                                  
$$                                                  
Da der Fluss in x-Richtung positiv ist gilt das erste Fick'sche Gesetz                                                  
                                                  
### Das 1. Fick'sche Gesetz                                                  
> [!important]  1\. Fick'sches Gesetz                                                 
>$$                                              
>J = - D \dfrac{\partial c}{\partial x}                                              
>$$                                              
                                                  
D ist hier der ==Diffusionskoeffizient== mit der Einheit $[D] = \dfrac{m^2}{s}$                                                   
                                                  
### Das 2. Fick'sche Gesetz                                                  
#### Herleitung                                                  
Gegeben sei folgende Situation                                                  
                                                  
![[Pasted image 20241126215142.png]]                                                  
Es wird betrachtet wie sich die Konzentration mit der Zeit ändert.                                                  
$$                                          
\frac{\partial c}{\partial x} = \, ?                                           
$$                                          
Für den Zustrom bei x gilt:                                                
$$                                                  
\partial c_{x=x} = \frac{J\cdot A \cdot dt}{A\cdot l}                                                  
                                                    
$$                                                  
Daraus folgt:                                                
$$                                              
\frac{\partial c}{\partial t}_{x=x} = \frac{J\cdot A \cdot dt}{A\cdot l \cdot dt} = \frac{J}{l}                                              
$$                                              
Bei x+l strömt aus:                                                
$$                                              
\frac{\partial c}{\partial t}_{x=x+l}  = - \frac{J^\prime}{l}                                              
$$                                              
Für die Gesamtkonzentrationsänderung gilt:                                                
$$                                              
\frac{\partial c}{\partial t}  = \frac{J- J ^\prime}{l}                                              
$$                                              
Mithilfe des 1. Fick'schen Gesetzes lässt sich der Zähler umstellen                                                
$$                                              
J - J^\prime =  - D \dfrac{\partial c}{\partial x} + D \dfrac{\partial c^\prime}{\partial x} = -D \dfrac{\partial c}{\partial x} + D \dfrac{\partial }{\partial x}\left(c + \dfrac{\partial c}{\partial x} \cdot l \right)                                               
$$                                              
                                                
$$                                              
= D l \frac{\partial^2c}{\partial x^2}                                              
$$                                              
Daraus folgt das 2.Fick'sche Gesetz                                                
> [!important]  2\. Fick'sches Gesetz                                                
>$$                                        
>\frac{\partial d}{\partial t} = Dl\frac{\partial^2c}{\partial x^2}                                              
>$$                                         
                                                
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
### Der Irrflug / Random Walk                                          
Eine statistische Betrachtungsweise für den Prozess der Diffusion ist der so genannte Random-Walk. Ein Teilchen legt in einem Zeitschritt $\tau$ eine feste Strecke $\lambda$ zurück. Betrachtet man den Random Walk in einer Dimension so lässt sich der Prozess als Bernouli-Kette und somit mit einer Binomialverteilung beschreiben.                                          
$$                                          
\begin{aligned}                                          
W = \textit{Wahrschheinlichkeit einer gewissen Anzahl Vorwärtschritte}\\                                          
N = \textit{Anzahl Schritte}\\                                          
V = \textit{Anzahl Vorwärtsschritte}\\                                          
R = \textit{Anzahl Rückwärtsschritte}\\                                          
p,q = \textit{Wahrscheinlichkeit fürw Vorwärts- und Rückwärtsschritte}                                          
\end{aligned}                                          
$$                                          
$$                                          
W(N,V) = \frac{N!}{V!R!}p^Vq^R                                          
$$                                          
Es gilt $V + R = N$ und $V-R=m$                                           
$m$ ist dabei die Anzahl vom Schritten, die sich vom Ursprung entfernt wurde.                                          
Setzt man dies in die Binomialverteilung ein:                                          
$$                                          
W(N,V) = \frac{N!}{\frac{N+m}{2}!\frac{N-m}{2}!}p^{\frac{N+m}{2}}q^{\frac{N-m}{2}}                                          
$$                                          
Durch die Stirling Näherung für Fakultäten erreicht man folgende Formel:                                          
> [!important] Wahrscheinlichkeit für eine Entfernung von x im 1D Random Walk                                          
>$$                                        
> W(N,x)=  \left( \frac{1}{2\pi N l^2}\right)^{1/2} e^{-\dfrac{ x^2}{2 N l^2}}                                         
>$$                              
>mit $x= m \times l$                              
                              
> [!error] Großer Sprung                                          
> Der Sprung hier ist ziemlich heftig. Aus den Vorlesungen, Folien und Atkins lässt sich nicht genau erahnen wie er das gemacht hat :(                                          
                              
#### 3D Random Walk                              
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
>$$                              
                              
#### Mittlerer quadratischer Abstand $\langle R^2 \rangle$                              
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
Kann mit folgenden Paramtern durch die [[Diffusion#Der Irrflug / Random Walk|Irrflugsstatistik]] beschrieben werden:                              
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
Die Teilchenbewegung lässt sich durch den [[Diffusion#Der Irrflug / Random Walk|Random Walk]] beschreiben. Es gilt:                              
> [!important] Einstein'sches Verschiebungsquadrat                              
> $$                              
> \langle x^2 \rangle = \left\{\begin{matrix}   2Dt & (1D)\\   4Dt&(2D) \\ 6Dt & (3D)   \end{matrix}\right.                              
                              
