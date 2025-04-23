>[!error] Im folgenden sei $I:=(a,b)$ stets ein offenes Intervall mit $-\infty \le a< b \le \infty$

# 1. Differenzierbarkeit
Eine Funktion $f : I  \mapsto \mathbb R$ heißt in $x_0 \in I$ differenzierbar wenn der Grenzwert der ==Differenzenquotienten== $\Delta_hf(x_0)$ für $h\mapsto 0$ an der Stelle $x_0$ existiert und endlich ist: $\Leftrightarrow$ 
$$
f^\prime (x_0) := \lim_{h\mapsto 0} \Delta_hf(x_0) := \lim_{h\mapsto 0}\frac 1h \{f(x_0+h)-f(x_0)\} < \infty
$$

## 1.2 Ableitung
$f:I \mapsto \mathbb R$ heißt auf $I$ differenzierbar $:\Leftrightarrow f^\prime(x)$ existiert und für alle $x\in I$ endlich ist. Die Funktion $x\mapsto f^\prime(x)$ heißt ==Ableitung== von $f$ und man schreibt:
$$
f^\prime \quad\left(=\frac{\mathrm df}{\mathrm dx}=\frac {\mathrm d}{\mathrm dx}f\right) : I\mapsto \mathbb R
$$
Der Wert der Ableitung einer Funktion ist identisch mit der Steigung der Tangenten an den Graphen in diesem Punkt. Die zugehörige Tangentengleichung ist
$$
y = f^\prime(x_0)(x_0-x)+f(x_0)
$$

Mithilfe der Ableitung erhält man die bestmögliche ==lineare Approximation== $g(x):=m(x_0-x)+f(x_0)$ an den Graphen von $f$ durch den Punkt $(x_0,f(x_0))$. Der relative Fehler:
$$
\frac{f(x)-g(x)}{x-x_0}
$$
konvergiert bei Verwendung der Ableitung für $m$ gegen 0, falls $x\mapsto x_0$ 
## 1.3
Falls $f,f^\prime \in C^0(I)$ dann schreiben wir $f \in C^1(I)$ 
$C^1$ = "Menge aller differentierbaren Funktionen auf I"

# Landausche Symbole
Für $f : I\mapsto \mathbb R$ und $g:I\mapsto \mathbb R$ schreiben wir
### 1. "Groß O"
$$
f(x) = O(g(x))\quad \text{für $x\mapsto x_0$}:\Leftrightarrow
$$
$$
\exists\: C \ge 0, \delta > 0 : |f(x)| \le C|g(x)| \quad \forall |x-x_0| \le \delta 
$$
"Im Intervall $[-\delta,\delta]$ liegen f und g höchstens um den Faktor $C$ auseinander"
![[Pasted image 20250421210738.png]]

Dies bedeutet, dass
$$
\Longrightarrow \lim_{x\mapsto x_0}\left|\frac{f(x)}{g(x}\right| \ne \infty
$$
Es folgen drei Möglichkeiten:
$$
\begin{align}
&\lim_{x\mapsto x_0}\left|\frac{f(x)}{g(x}\right| = 0: \quad &\text{$|f(x)|$ geht schneller nach $0$ als $|g(x)|$ für $x\mapsto x_0$}\\
&\lim_{x\mapsto x_0}\left|\frac{f(x)}{g(x}\right| = C \: \text{mit } 0<C<\infty: \quad &\text{$|f(x)|$ und $|g(x)|$ gehen vergleichbar schnell ...  für $x\mapsto x_0$}\\
&\lim_{x\mapsto x_0}\left|\frac{f(x)}{g(x}\right| \quad &\text{existiert nicht, aber Quotient ist begrenzt $\mapsto$ Vergleichbar}
\end{align}
$$
=="f geht mindestens so schnell wie g nach 0"==
### Klein O
$$
f(x) = o(g(x))\quad \text{für $x\mapsto x_0$}:\Leftrightarrow
$$
$$
\forall \epsilon\: \exists \: \delta(\epsilon) > 0 : |f(x)| \le |g(x)| \quad \forall |x-x_0| \le \delta
$$
"Wie O nur keine Auswahl mehr, dafür hängt $\delta$ von $\epsilon$ ab.

Anders gesagt
$$
\lim_{x\mapsto x_0} \left|\frac{f(x)}{g(x)}\right| = 0
$$
Der Betrag von f geht schneller gegen 0 als der von g

Für differenzierbare Funktionen gilt demnach:

$$
f(x_0 +h) = f(x_0) + f^\prime (x_0)h + o(h) \text{ für } h\mapsto 0
$$
"o geht schneller nach 0 als h"
=="f geht schneller als g nach 0"==

# Lemma 7.5
Falls $f^\prime(x_0)$ für $x_0\in I$ existiert, dann ist $f : I\mapsto \mathbb R$ stetig in $x_0$

>[!error] Nur weil eine Funktion stetig ist, heißt dies nich dass sie dfferenzierbar ist (einseitge Implikation)