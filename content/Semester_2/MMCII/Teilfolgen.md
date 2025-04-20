Gegeben seien $\{x_n\}_{n\in \mathbb N} \subset \mathbb R$ und $\{n_k\}_{k\in \mathbb N} \subset \mathbb N$ . Beide Folgen seien Streng monoton wachsend. Dann heißt:
$$
\{x_{n_k}\}_{k \in\mathbb N}
$$
==Teilfolge== von $\{x_n\}_{n\in \mathbb N} \subset \mathbb R$
"Sprich wenn Teile einer Folge in Reihe nur gewählt werden dann Teilfolge (Teilmenge der Indizes)"
x1,  x3, x5, x7, etc

# Häufungspunkte
Ein Punkt $x_0 \in \mathbb R$ heißt ==Häufungspunkt== einer Folge $\{x_n\}_{n\in \mathbb N} \subset \mathbb R :\, \Leftrightarrow$  
in jeder Umgebung $B_\epsilon(x_0) := (x_0-\epsilon, x_0 + \epsilon), \: \epsilon > 0$ unendlich viele Glieder der Folge liegen.

$$
(\Leftrightarrow | B_\epsilon(x_0)\wedge\{x_n\}_{n\in \mathbb N} |= \infty
)$$
Ist eine Folge konvergent gibt es nur 1 Häufungspunkt
>[!example] Beispiel
>$$
>x_n = \sin \frac 12 n \pi:\qquad 1,0,-1,0,1,...
>$$
### Bestimmung
Eine Folge hat einen Häufungspunkt $x_0$, wenn es eine Teilfolge der Folge gibt, die gegen $x_0$ konvergiert.

>[!example] Beispiel:
>Die Folge::
>$$
>\left\{(-1)^n+\frac 1n\right\}^\infty_{n=1}
>$$
>hat 2 Häufungspunkte. Die Teilfolge der ungeraden Indizes geht gegen 1, die der ungeraden gegen -1
# Intervallschachtelungen 
Eine Folge abgeschlossener intervalle 
$$
\left\{[a_n,b_n\right\}^\infty_{n=1}
$$
heißt ==Intervallschachtelung== wenn:
1. $[a_{n+1},b_{n+1}] \subset [a_n,b_n]$
2. $b_n -a_n \rightarrow 0$ fr $n \rightarrow \infty$
![[Pasted image 20250420215932.png]]

Zu einer Intervallschachtelung gibt es genau ein $x_0$ gegen das a und b konvergieren.

## Bolzano-Weierstraß-Satz
Jede beschränkte Folge ($-u \leq a_n \geq u \,\forall n$) besitzt (mindestens) einen Häufungspunkt.
>[!warning] Beweis:
>Halbiere Intervall und wähle Hälfte mit mehr Elementen ad infinitum
> -> Intervallschachtelung
> (basically Binary-Search)


# Zwischenwertsatz
Sei $f \in C^0([a,b])$ (begrenzte Stetige Funktion auf einem geschlossenem Intervall). Dann gilt:
1. Falls $f(a)\cdot f(b) < 0$ dann gibt es mindestens ein $x_0 \in (a,b) mit f(x_0) = 0 (eine Nullstelle)
2. $W(f)  = [\mathrm{inf}_{[a,b]},\mathrm{sup}_{[a,b]}]$ (Stetige Funktionen nehmen alle Werte zwischen Minimum und Maximum an)

### Collar 6.26 (Polynome)  aus dem Zwischenwertsatz
Jedes Polynom mit ungeradem Grad hat mindestens eine reelle Nullstelle

# Fixpunkte
Für eine Funktion $f : M \rightarrow \mathbb R$ heißt $x_0$ ==Fixpunkt== von $f :\Leftrightarrow$
$$
f(x_0) = x_0
$$
Die Funktion hat genau dann einen Punkt wenn:
$$
g(x) = f(x) - x
$$
eine Nullstelle hat
# Fixpunktsatz
Für $f \in C^0([a,b])$ mit $W(f) \subset [a,b]$ gibt es mindestens einen Fixpunkt

$$
\begin{align}
g(a) = f(a)-a >0\\
g(b) = f(b)-b< 0
\end{align}
$$
Es folgt es gibt eine Nullstelle für g