>[!important] Definition: Stetigkeit
> Eine Funktion $f : (a,b) \rightarrow \mathbb R$ heißt stetig in  $x_0 \in (a,b) : \, \Leftrightarrow$
> $$
> f(x_0) = \lim_{x\rightarrow x_0} f(x)
> $$
> Praktisch wenn man "eine linie durchziehen kann"
> Auch bei mehrdimensionalen Funtkionen der Art $M \rightarrow \mathbb R^m$
>
>Für jede im Intervall $[a,b]$ stetige Funktion gibt es eine Konstante $K$ sodass
>$$
>|f(x)| \leq K \quad \forall x\in [a,b]
>$$
>Jede ==begrenzte== stetige Funktion auf einem ==geschlossenem== Intervall nimmt ihr Infimum und Supremum an => $\exists$ Minimum und Maximum






## Beispiel:
Gegeben sei folgende Funktion:
$$
f(x) = \left\{ \begin{matrix}\frac{2x-2}{\sqrt x -1}\quad &x\ne 1 \\ 4\quad &x=1\end{matrix} \right.
$$
Es wird der Grenzwert bei x = 1 bestimmt:
$$
\lim_{x\rightarrow 1} \frac{2x-2}{\sqrt x-1} = \lim_{x\rightarrow 1} \frac{2(\sqrt x-1)(\sqrt x+1)}{\sqrt x -1} = \lim_{x\rightarrow 1} 2(\sqrt x +1) = 4
$$
Es gilt somit 
$$
f(x) = \lim_{x\rightarrow x_0}= f(x)
$$
Die Funktion ist  ==stetig== in $x_0 = 1$



>[!important] Definition: Links- & und Rechtsseitige Stetigkeit
>Eine Funktion $f(x)$ ist linksseitig stetig wenn gilt:
>$$
>f(x_0) = \lim_{x\nearrow x_0} f(x) 
>$$
>Sie ist rechtsseitig stetig wenn gilt:
>$$
>f(x_0) = \lim_{x\searrow x_0} f(x) 
>$$

# Stetige Intervalle
Ist eine Funktion $f(x) : (a,b) \rightarrow \mathbb R$ in allen $x\in (a,b)$ stetig, dann heißt f(x) ==stetig auf $(a,b)$==
Die Menge aller auf $(a,b)$ stetigen Funktionen bezeichnet man als 
$$
C^0((a,b))
$$
(Continous)
Man schreibt auch
$$
f \in C^0((a,b)) \quad \mbox{oder} \quad  f\in C^0(\mathbb R)
$$

# Stetig Fortsetzbare Funktionen
Gegeben ist eine auf $x_0$ ==nicht== stetige Funktion $f$
$$
f(x) \in C^0(B_\epsilon \setminus \{x_0\})
$$
Existiert der Grenzwert an Punkt $x_0$ 
$$
\exists \lim_{\xi\rightarrow x_0}(\xi)
$$
dann heißt $f$ ==stetig fortsetzbar==. Mit folgender Funktion als ==stetige Fortsetzung== von $f$ auf $B_\epsilon(x_0)$ :
$$
\tilde f(x) = \left\{ \begin{matrix}f(x) &\forall x \in B_\epsilon(x_0)\setminus \{x_0\}\\ \lim_{\xi\rightarrow x_0}(\xi) &\text{für }x=x_0\end{matrix} \right.
$$

## Hebbare Singularitäten und Unstetigkeiten
Der Punkt $x_0$ heißt eine hebbare Singularität, wenn $x_0 \notin D(f)$

Falls $x_0$ nicht als der Grenzwert definiert wurde spricht man von einer hebbaren Unstetigkeit.

# Operationen

1. Rechenregeln für Stetige Funktionen
	Falls $f$ und $g$ stetig sind, gilt:
	- $f+g$, $f\cdot g$ sind stetig
	- falls $g(x_0)\ne 0$ dann ist $f/g$ stetig
2. Ist $f(x) : (a,b) \rightarrow \mathbb R$ mit $W(f) = (c,d)$ und und $g(x) : (c,d) \rightarrow \mathbb R$ so gilt:
		Wenn $g(y_0)$ stetig und $y_0 = f(x_0)$, dann ist auch $g \circ f$ in $x_0$ stetig
3.  Ist f streng monoton und stetig, so ist diee Umkehrfunktion von f auch stetig und streng monoton
# Konvergenzkriterium von Folgen
Gegeben sei ein Intervall B(a) um den Punkt $a$ mit Spannweite $2\epsilon$

---|<---a--->|---
      $\epsilon$         $\epsilon$ 
Sei $\epsilon > 0$, $a\in\mathbb R$ und $f : B(a) \rightarrow \mathbb R$ stetig in $a$. Dann gilt für jede Folge $\{a_n\} \subset B(a)$  mit $a_n \rightarrow a$ für $n\rightarrow \infty$ :
$$
\lim_{n\rightarrow\infty} f(a_n) = f(a)
$$
# Potenzreihen
$$
P \in C^0((-R,R))
$$

# Sinus und Cosinus
1. Sinus und Cosinus sind stetig.
