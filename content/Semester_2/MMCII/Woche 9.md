# Integration von exponentialfunktionen
Gegeben sei 
$$
\int f(e^{ax})
$$
mit der Substitution $z = e^{ax}$ lässt sich folgern
$$
\int f(z)\frac1{az}dz
$$
## Integral spezieller Wurzelfunktionen
$$
\int R\left(x, \sqrt[k]{\frac{ax+b}{cx+f}}=\right)dx
$$
Lässt sich mit
$$
z:= \sqrt[k]{\frac{ax+b}{cx+f}}
$$
$$
\implies x = \frac{fz^k-b}{a-cz^k}
$$
$$
\int R\left(\frac{fz^k-b}{a-cz^k},z\right)
$$
integrieren

# Integral spezieller trig
![[Pasted image 20250728160503.png]]

# Hyperbolische Funktionen
$$
\begin{align}
    \sinh x &= \frac{e^x-e^{-x}}{2}\\
    \cosh x &= \frac{e^x+e^{-x}}{2}\\
    \tanh x &= \frac{\sinh x}{\cosh x}\\
    \coth x &= \frac{\cosh x}{\sinh x}\\
\end{align}
$$
## Eigenschaften
$$
\begin{align}
    \sinh^\prime x = \cosh x \ \wedge \ \cosh^\prime x = \sinh x\\
    \cosh^2 x - \sinh^2 x = 1
\end{align}
$$
## Additionstheorem
$$
\begin{align}
    \sinh(x+y) = \sinh x \cosh y + \cosh x \sinh y\\
    \sinh(x-y) = \sinh x \cosh y - \cosh x \sinh y\\
    \cosh(x+y) = \cosh x \cosh y + \sinh x \sinh y\\
    \cosh(x-y) = \cosh x \cosh y - \sinh x \sinh y\\
\end{align}
$$
# $\color{red}\text{ HIER FEHLT WAS}$


# Taylor  Formel
Für alle in n stetigen Funktionen gilt
$$
f(x) = f(a) + \frac{f^\prime(a)}{1!}(x-a)+\frac{f^{\prime\prime}(a)}{2!}(x-a)^2+\frac{f^{(n)}(a)}{n!}(x-a)^n+R_{n+1}(x,a)
$$
$$
f(x) = \sum_{i=0}^{n} \frac{f^(i)}{i!}(x-a)^i + R_{n+1}(x,a)
$$
Näherungsgrad + Fehler

mit 

$$
\begin{align}
R_{n+1} &= \color{teal} \frac 1{n!}\int_a^x(x-t)^nf^{(n+1)}(t)dt & \ \text{Cauchy Restglied}\\
	&= \color{yellow} \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1} &\quad \text{Langrange Restglied}
\end{align}
$$

Die Taylor Formel ist exakt für Polynome ($R_n=0$ bei Grad n)
