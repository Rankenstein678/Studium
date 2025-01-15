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
