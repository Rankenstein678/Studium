# 1. Experimentelle Techniken
## 1.1 - Fortschritt einer Reaktion
Der Fortschritt einer Reaktion lässt sich experimentell beispielsweise über folgende Parameter bestimmen
- Leitfähigkeit
- pH-Wert
- Absorbanz
- Druck
> [!example]
> Gegeben ist die Reaktion $\ce{2NOBr -> 2 NO + Br2}$
> Wie verändert sich der Druck?
> ==Methode==:
>  Druck durch Teilchenzahl $n$ in Abhängigkeit vom Reaktionsumsatz $\alpha$ bestimmen
>  
>| NOBr | NO | Br2 | | Gesamt |
>| --- | --- | --- | --- |
>| $n(1-\alpha)$ | $n\alpha$ | $\frac 12 n\alpha$ | $n(1 + \frac 12\alpha)$ |
> Der Druck ist somit ausgehend vom Ausgangsdruck $p_0$:
> $n(1 + \frac 12\alpha)p_0$

## 1.2 - Flow und Stopped Flow verfahren
![[Pasted image 20250104230814.png]]
Beispiele für das zeitabhängige messen der Konzentration durch Spetroskopie

# 2. Reaktionsgeschwindigkeit
Man beginnt mit den Bildungsgeschwidigkeiten aller Reaktanden. Diese können jedoch verschieden seien.
Dies wird durch die Reaktionslaufzahl $\xi$ vermieden
>[!important] Def: Reaktionslaufzahl $\xi$
>Stoffmenge zur Beschreibung des Reaktionsfortgangs
>$$
>\xi = \frac{n_J-n_{J_0}}{\nu_J} 
>$$

$$
d\xi = \frac 1{\nu_J} \frac{dn_J}{dt}
$$

$$
v = \frac 1V \frac {d\xi}{dt} = \frac 1\nu \frac{d[J]}{dt}
$$
(Bei konst. Volumen)
> [!important] Def: Reaktionsgeschwindigkeit $v$
> $$
> v =\frac 1\nu \frac{d[J]}{dt}
> $$
> $[v]=mol.L^-1.s^-1$
> Unabhängig von der Spezies
> Abhängig von der Stöchiometrie

# 3. Geschwindigkeitsgesetz
Das Geschwindkeitsgesetz ist eine Funktion die die Reaktionsgeschwindigkeit mit den Konzentrationen der beteiligten Stoffe verbindet.
Viele Reaktionen besitzen ein folgendes Geschwindkeitsgesetz
$$
v = k[A]^\alpha[B]^\beta
$$
Mit der $k$ als ==ReaktionsGeschwindikeitskonstante==. Die Einheit für k ist immer so gewahlt, dass aus dem Geschwindigkeitsgg eine passende Einheit folgt.

$\alpha$ = partielle Ordnung für A
$\beta$ = partielle Ordnung für B
$\alpha + \beta$ = Gesamtordnung der Reakktion

Das Geschwindigkeitsgesetz ==muss== experimentell ermittelt werden und ist nicht ableitbar.

## 3.1 Elementarreaktionen
Eine Elementarreaktion ist ein kleiner Teilschritt der Gesamtreaktion. Es wird kein Aggregaszustand angegeben da die Reaktionsgleichung eine reine Beschreibung des Mechanismus  ist.
Die Molekularität besagt, wie wie viele ==Edukte== an dieser Reaktion teilnehmen. Ist eine Elementarreaktion unimolekular, dann ist die Kinetik erster Ordnung usw. Hat eine Reaktion eine gewisse Ordnung so kann sie dennoch wesentlich komplexer sein.
## 3.2 Bestimmen eines Geschwindigkeitsgesetzes
### 3.2.a Isolierungsmethode
Ein Stoff wird deraßen im Übermaß zugegeben, dass seine Konzentration als konstant angenommen wird.
Dann erhält man ein Geschwindigkeitsgesetz "Pseudeoerster Ordnung"
$$
\begin{align}
v = k^\prime [A]_0^a && k^\prime = k[B]_0
\end{align}
$$

Das Geschwindigkeitsgesetz kann durch aufeinanderfolgendes austauschen aller Reaktionsteilnehmer erhalten werden.

### 3.2.b Anfangsgeschwindigkeits-methode
Die Anfangsgeschwindigkeit wird gemessen und es wird wie folgt gerechnet
$$
v_0 = k[A]_0^a
$$
$$
\log v_0 = \log k +  a\log [A]_0
$$
Die Ordnung sowie k sich dann aus einer Auftragung von log v0 gegen log \[A] errechnen

Sie wird häufig in Kombination mit der Isolationsmethode verwendet um Gesetze erster Ordnung zu erhalten.
Das Geschwindigkeitsgesetz ist aber  ==nicht== unbedingt richtig, da die Produkte interferieren könnten.

## 3.3 Integrierte Geschwindigkeitsgesetze
Da Geschwindigkeitsgesetze Differentialgleichungen sind müssen sie integriert werden, um eine Funktion der Konzentration nach der Zeit zu erhalten.
==Beim aufstellen der Reaktionsgeset ansatzes ist auf die Stöchiometrischen Konstanten zu achten.==
### 3.3.a Erste Ordnung
$$
\begin{align}
\frac {d[A]}{dt} = -k[A]\\
\frac{d[A]}{[A]} = -kdt\\
\int_{[A]_0}^{[A]}\frac 1{[A]} d[A] = -k \int_{t_0}^t 1 dt\\
\ln([A])-ln([A]_0) = -kt - (-k*t_0)\\
\color {red} \ln\left(\frac{[A]}{[A]_0}\right) = -kt\\
\ln\left(\frac{[A]}{[A]_0}\right) = -\nu_Akt\\

\end{align}
$$
Die Geschwindigkeitskonstante kann durch ein plotten vom ln gegen die Zeit erhalten werden.
Das Gesetz lässt sich auflösen zu
$$
\color{red}[A] = [A]_0\ e^{-kt}
$$
oder mit $\tau = 1/k$
$$
[A] = [A]_0\ e^{-\frac t\tau}
$$
Die Halbwertszeit berechnet sich wie folgt
$$
\begin {align}
-\ln\left(\frac{\frac12[A]_0}{[A]_0}\right) = kt_{1/2}\\
-\ln(\frac 12) + \ln (1) = kt_{1/2}\\
\color{red} t_{1/2} = \frac{\ln(2)}{k}
\color{red} t_{1/2} = \frac{\ln(2)}{\nu_Ak}\\
\end{align}
$$

### 3.3.b Zweite Ordnung
$$
\begin{align}
-\frac {d[A]}{dt} = k[A]^2\\
- \int_{[A]_0}^{[A]} \frac 1{[A]^2} d[A] = kt\\
- \left(-\frac{1}{[A]}+\frac 1{[A]_0}\right) = kt\\
\color{Red} \frac{1}{[A]} - \frac 1{[A]_0} = kt\\
\color{red} [A] = \frac {[A]_0}{1+kt[A]_0}\\
\frac{1}{[A]} - \frac 1{[A]_0} = |\nu|kt
\end{align}
$$
Für die Halbwerszeit gilt
$$
\color{red} t_{1/2} = \frac  1{|\nu_A|\,k[A]_0}
$$
Um auf die Zweite Ordnung zu testen plottet man $1/[A]$ gegen t.

#### 3.3.b.b Zweite Ordnung der Art A+B
![[Pasted image 20250105155305.png]]

### 3.3.c Nullte Ordnung
$$
\frac{d[A]}{dt} = -k
$$
$$
t_{1/2} = \frac{[A]_0}{2k}
$$
# 4. Temperaturabhängigkeit - Die Arrheiusgleichung
In der Regel nimmt die Geschwindigkeit einer Reaktion mit steigender Temperatur zu.
Aus Experimenten folgt
$$
\ln k = m*\frac 1T +c
$$
mann  stellt die Arrheniusgleichung auf

> [!important] Arrheniusgleichung
> $$
> \begin{align}
> k = Ae^{-\frac{E_A}{RT}} &&\text{oder}&&\ln k = \ln A - \frac{E_A}{RT}
> \end{align}
> $$
> Mit:
> $A$ = Vorfaktor, Präexponentieller Faktor, Frequenzfaktor (Maß für die Zahl der Stöße)
> $E_A$ = Aktivierungsenergie: Minimale Energie, die die Reaktanten haben müssen, damit die Reaktion ablaufen kann
> $Ae^{-\frac{E_A}{RT}}$ = Maß für die Zahl der Stöße die zur Reaktiiion führen
 


# 5. Abfolgen von Elemenarreaktionen
gegeben sei folgende Reaktion
$$
\ce{A ->[k1] I ->[k2] P}
$$Unter der Annahme dass $[I]_0=[P]_0 = 0$ fährt man wie folgt fort.

Für $[I]$ gilt:
$$
\frac {d[I]}{dt} = k_1[A] - k_2[I]
$$
Da A unimolekular ist kann man für die Konz von A einsetzen:
$$
\frac{d[I]}{dt} = k_1[A]_0\,e^{-k_1t} - k_2 [I] 
$$
Diese Differetallgleichung löst sich zu
$$
	[I] = [A]_0 \frac{k_1}{k_2-k_1}\left(e^{-k_1t}-e^{-k_2t}\right)
$$

Es gilt immer $[A]_0=[A]+[I]+[P]$
Für $[P]$ folgt:
$$
[P] = [A]_0 \left[1+\frac{k_1e^{-k_2t}-k_2e^{-k_1t}}{k_2-k_1}\right]
$$
## 5.1 Der geschwindigkeitsbestimmende Schritt
Wenn $k_2 \gg k_1$, dann ist der erste schritt der geschwindigkeitsbestimmende Schritt (rate determining step).
Alles gebildete I reagiert sofort weiter
$$
[P] \approx (1-e^{-kt_1})[A]_0
$$
## 5.1 Das Bodenstein'sche Stationaritätsprinzip
Wenn $k2\gg k1$ dann kann angenommen werden, dass alles neu gebildete $I$ sofort weiterreagiert. Man nimmt an:
$$
\frac{d[I]}{dt} = 0
$$
Dies vereinfacht viele Rechnungen. So wird aus der Gleichung aus [[Kinetik#5. Abfolgen von Elemenarreaktionen]]:
$$
	[P] = [A]_0\left(1-e^{-k_1t}\right)
$$
# 6. Parallel Reaktionen
Gegeben sei folgende Reaktion
$$
\begin{align}
\ce{A->[k_1] B}\\
\ce{A->[k_2] C}
\end{align}
$$
Es wird angenommen dass $[B]_0 = [C]_0 = 0$ 
Für A gilt
$$
v= -\frac{d[A]}{dt} = k_1[A] + k_2[A] = [A](k_1+k_2)
$$
Das Zeitgesetz lässt sich differenzieren
$$
\ln \frac {[A]}{[A]_0} = -(k_1+k_2)t
$$
Für B gilt
$$
\frac{d[B]}{dt} = k_1[A] = [A]_0\,e^{-(k_1+k_2)t}\color{red}k_1
$$
Differenziert:
$$
[B] = \frac{[A]_0\color{red}k_1}{k_1+k2}\left[1-e^{-(k_1+k_2)t}\right]
$$
Analog das gleiche für C mit dem Roten Wert verändert
# 7. Rückreaktionen
mit
$$
\begin{align}
\ce{A->[k]B}\\
\ce{B->[k^\prime]A}
\end{align}
$$
Die Rückreaktion kann meist vernachlässigt werden. In der Nähe der Gleichgewichtskonzentrationen wird sie jedoch relevant und muss mit einbezogen werden.
Es gilt:
$$
\begin{align}
v_{hin}=v_{rück}\\
k[A]_{eq}=k^\prime[B]_{eq}\\
K = \frac k {k^\prime} = \frac{[B]_{eq}}{[A]_{eq}}
\end{align}
$$

Aus Kinetikbetrachtungen folgt:
$$
\frac{d[A]}{dt}  = -k[A]+k^\prime[B]
$$
Es wird $[B]=[A]_0-[A]$ eingestzt

$$
\frac{d[A]}{dt}  = -(k+k^\prime)[A] + k^\prime [A]_0
$$
Aus dem GGW folgt:
$$
\frac{[B]_{eq}}{[A]_{eq}} = \frac {[A]_0-[A]}{[A]_{eq}} = \frac{k}{k^\prime}
$$
$$
[A]_{eq} = \frac{k^\prime}{k+k^\prime}[A]_0
$$

Daher kann man die Gleichung umformen

$$
\frac{d[A]}{dt} = -(k+k^\prime)\left([A]-[A]_{eq}\right)
$$
Es folgen
$$
\color{red} \ln \frac{[A]_0-[A]_{eq}}{[A]-[A]_{eq}} = (k+k^\prime)t
$$
$$
\color{red}[A] = \frac{k^\prime[A]_0}{k+k^\prime}\left(1+\frac k{k^\prime}e^{-(k+k^\prime)t}\right)
$$
Aus der ersten Gleichung lässt sich durch Plotten $(k+k^\prime)$
# 8. Lindemann Mechanismus
Modell für Unimolekulare Gasreaktionen, da jede Unimolekullare Reaktion eine Vorgeschichte haben muss.
$$
\begin{align}
\ce{A + M &->[k_1] A^* + M \qquad\textit{(A bekommt Energie aus Stoß)}}\\
\ce{A^* + M&->[k_2] A + M\qquad\textit{(A verliert Energie durch Stoß)}}\\
\ce{A^* &->[k_3] B (+C)}
\end{align}
$$
Für $[A^*]$ lässt sich aufgrund der geringen Konzentration die Bodensteinsche ... treffen
Es folgt:
$$
0 = k_1[A][M]-(k_2[M] + k_3)[A^*]
$$
Für das Produkt gilt:
$$
\frac{d[B]}{dt} = k_3[A*] = k_3 \frac{k_1[A][M]}{k_2[M]+k_3} = k_{uni} [A]
$$
## 8.1 Sonderfälle
Bei hohem Druck $k_2[M] \gg k_3$
$$
-\frac{d[A]}{dt} = \frac{k_1k_3}{k2}[A]
$$
==> Erste Ordnung

Bei niedrigem Druck $k_2[M] \ll k_3$
$$
-\frac{d[A]}{dt} = k_1[A][M]
$$
==> Pseudo erste Orrdnung bei konstantem $[M]$
# 9. Enzymkinetik
Enzyme sind extrem effiziente Biokatalysatoren. Sie haben 1 oder mehrere Aktive Zentren, in denen das Substrat gebunden wird.
## 9.1 Exp.  Beob
1. Geschw. d. Substratumsatzes ist proportional zur Enzymkonz.
2. Plateau der Geschwindigkeit bei hoher Substratkonz
## 9.2 Der Michaelis-Menten-Mechanismus
Ein Modell für Enzymreaktionen ist:
$$
\ce{E + S <=>[k_1][k_{-1}]  ES ->[k_2] E + P}
$$
Für die Geschwindigkeit gilt
$$
v = \frac{k_2[E]_0}{1+K_M/[S]}
$$

### 9.2.1 Herleitung
Die Bodensteinsche Quasistationaritätsannnahme wird getroffen:

$$
\frac{d[ES]}{dt}=0 = k_1[E][S] - k_{-1}[ES] - k_2[ES]
$$
Es folgt
$$
[ES] = \frac{k_1}{k_{-1}+k_2}[E][S]
$$
Es wird die Michaelis konstante definiert als
$$
K_M = \frac{k_{-1}+k_2}{k_1} = \frac{[ES]}{[E][S]}
$$
Nun gilt
$$
[E] = [E]_0 - [ES]  
$$
Eingesetzt folgt
$$
\frac{[S]([E]_0-[ES])}{K_M} = [ES]
$$
Durch umformen folgt
$$
[ES] = \frac{[E]_0}{1+ \frac{K_M}{[S]}}
$$
Alternativ kann $[S]_0 = [S]$ angenommen werden, wenn das Substrat im Verglecichh zum Enzym im großen Überschuss vorhanden ist.

## 9.3 Einfluss der Substratkonzentration
### 9.3.1 $[S] \gg K_M$ 
Es ist soviel Substrat vorhanden, dass die Konzentration als Konstant angesehen werden kann. Die ordnung bezüglich des Substrats ist 0.
$$
\frac{d[P]}{dt} =v= v_{max}= k_2 [ES] = S] = \frac{k_2[E]_0}{1+ \frac{K_M}{[S]}}
 = k_2[E_0]
$$
Die Maximale Geschwindigkeit ist erreicht

Die maximale turn over Zahl ist die Maximale Zahl an Umgesetzten Substrat Teilchen pro sekunde pro aktives Zentrum
$$
k_2 = \frac {v_{max}}{[E]_0} = k_{cat}
$$
### 9.3.2 $[S] = K_M$ 
$$
v =\frac 12 v_{max}
$$
### 9.3.3 $[S] \ll K_M$
Siehe Herleitung
$$
v = \left(\frac{k_2}{K_M} [E]\right)[S] 
$$
linerare Anstieg

## 9.4 Enzymhemmung

### 9.4.1 kompetetive Hemmung
$$
\ce{E + I <=> EI -> \textit{Reagiert nciht zum Produkt}}
$$
Für die Dissoziation gilt:
$$
K_I = \frac{[EI]}{[E][I]} => \frac{[I]}{K_I} = \frac{[EI]}{[E]}
$$
Ist $\frac{[I]}{K_I}=1$ so ist die Enzymkonzenntration halbiert. Folglich gilt
$$
\frac{k_2[E]_0}{1+ \frac{K_M}{[S]}\left(1 + \frac {[I]}{K_I}\right)}
$$
![[Pasted image 20250117134941.png]]
### 9.4.2 unkompetetive Hemmung
![[Pasted image 20250117132754.png]]
Für die GGW konst. gilt
$$
K_I^\prime = \frac{[ES][I]}{[ESI]}
$$
![[Pasted image 20250117134951.png]]
### 9.4.3 nicht kompetetive Hemmung
![[Pasted image 20250117133227.png]]
Der Inhibitor bindet das Enzym an anderer Stelle, also nicht am aktiven Zentrum. Die Enzym Substrat-Bindung wird daher durch die Enzym-Inhibitor-Bindung nicht beinflusst. Das Produkt kann nur durch Freisetzung aus dem Enzym-Substratkomplex erfolgen und nicht aus dem Enzym-Inhibitor-Substratkomplex ESI.

Für das GGW gilt
$$
K_I = \frac{[E][I]}{[EI]}
$$
$$
K_I^\prime = \frac{[ES][I]}{[ESI]}
$$
![[Pasted image 20250117135220.png]]
## 9.5 Linweaver-Burk-Auftragung
Folgende Umformung ist möglich
$$
v = \frac{k_2[E]_0}{1+\frac{K_M}{[S]}} = \frac{v_max}{1+\frac{K_M}{[S]}}  
$$
=>
---
$$
\frac 1v = \frac 1{v_{max}} + \frac{K_M}{v_{max}}\frac{1}{[S]} 
$$
=> Lineare Auftragung von $\dfrac 1v$ gegen  $\dfrac 1{[S]}$ 
# 10 Ionenstärke
Mehrfach geladenen Ionen haben einen stärkeren Einfluss auf die Aktivität als ungeladene.
# 11. kinetischer Salzeffekt
???? brauchen wir das ???

# 12. Der Temperatursprung und die Relaxation
Bei $t_0$ ist $T = T^\prime$
Bei $t_1$ ist $T = T$

Im GGW zu beginn gilt
$$
k_1^\prime [A]_{eq} = k^\prime_{-1} [B]_{eq} 
$$
Bei t1:
$$
\frac{d[A]}{dt} = -k_1 ([A]_{eq}+x)+ k_{-1}([B]_{eq}-x) = (k_{-1}-k_1)x
$$ $\uparrow$ Da im GGW 

Es gilt:
$$
\frac{d[A]}{dt} = \frac{dx}{dt} => x = e^{-\dfrac t\tau}
$$
mit 
$$
\tau = (k_1+k_{-1})^{-1}
$$
Mit einer Zeitmessung und der Gleichgewichtskonstante können beide Geschwindigkeitskonstanten bestimmt werden.

> [!example] Bem.
> da der Temperatursprung i. Allg. nur zu geringen Abweichungen vom Glgw. führt, können quadratische Terme vernachlässigt werden und man kann – wie oben getan – schreiben

# 13. Diffusionskontrollierte Reaktionen
$$
\ce{A + B <=> (AB) -> C}
$$
(AB) ist ein Molekülpaar im Lösemittelkäfig, dass entweder auseinander diffundieren oder reagieren kann.

Wenn $k_2\gg k_{-1}$ und die Aktivierungsenergie klein ist dann ist die Reaktion Diffusionskontrolliert.

==> Die Moleküle treffen aufeinander und reagieren sofort weiter.
$$
\ce{A + B ->[k_a] C}
$$
Nach Smoluchowski
$$
k_a =4\pi N_L(D_A+D_B)(R_A+R_B) 
$$
Mit 
- D: Diffusionskoeffizient
- R: Molekülradius
- Annahme A&B sind Kugelförmig
# 14. Komplexe Zeitgesetze 
Manche komplexen Zeitgesetze können nicht mehr analytisch sondern nur noch numerisch bestimmt werden.
Dazu wird dann $\Delta$ statt $d$ genutzt
$$
\Delta [A] = -\Delta t\, k[A]
$$

Für Zeitintervalle wird die Konzentrationsänderung berechnet

# 15. Ideales Knäuel - Fadenendenabstand
Durchschnittlicher Fadenendenabstand:
$$
\langle R \rangle = 0
$$
Daher nutzt man den Quadratischen
$$
\langle R^2\rangle = N l^2
$$
Mit 
- N = Anzahl Teilstücke
- l = Länge eines Teilstücks
## 15.1 Herleitung
$$
\vec R = \sum_{n=0}^N \vec l_n
$$
$$
R^2= \vec R \cdot \vec R = (l_1+l_2+l_3+\ldots)(l_1+l_2+\ldots)
$$
Es kommt N mal zu $l_i*l_i$ 
$$
R^2 = Nl^2 + \ldots
$$
Der Rest wird wie folgt addiert
$$
R^2 = Nl^2 + 2 \sum_{i>j}\sum \vec l_i\cdot\vec  l_j
$$
Für den Mittelwert gilt
$$
\langle R^2\rangle = Nl^2+2\sum_{i>j} \sum \langle \vec l_i \cdot \vec l_j\rangle
$$
Das Skalarprodukt zweier Vektoren wird eingesetzt
$$
\langle R^2\rangle = Nl^2+2\sum_{i>j} \sum l^2\langle \cos \gamma_{ij}\rangle
$$
Geht man von einer idealen Kette aus ist der Durchschnittswinkel 90°
$$
<R^2> = Nl^2
$$