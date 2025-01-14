>[!important] Def: Polynome
>Ein Polynom n-ter Ordnung (ganzrationale Funktion) ist wie folgt definiert          
>$$          
>\begin{align}          
>&P_n(x) = a_nx^n + a_{n-1}x^{n-1}+\ldots + a_0x^0\\          
>\textit{reell: }& x \in \mathbb{R},\ a_i \in \mathbb{R},\ n \in \mathbb{N}\\          
>\textit{komplex: }& z \in \mathbb{C},\ a_i \in \mathbb{C},\ n \in \mathbb{N}\\          
>\end{align}          
$$          
          
> [!example] Satz: Identitätssatz für Polynome          
> "Wenn die Koeffizienten zweier Polynome gleich sind so sind sie gleich"          
> Mathematisch:          
> Gegeben seien          
> $$          
> P_n(z) = \sum_{i=0}^n a_iz^i          
> $$          
> und           
> $$          
> Q_n(z) = \sum_{i=0}^n b_nz^n          
> $$          
> P und Q sind gleich wenn:          
> $$          
> a_i=b_i\ \forall\ 0\ldots n          
> $$          
> daher "Koeffizientenvergleich"          
          
> [!warning] Technik: Polynomdivision          
> Es soll für die beiden Polynome $P(x)$ und $Q(x)$ der Ausdruck $\frac{P(x)}{Q(x)}$ berechnet werden. Das ganze läuft wie eine schriftliche Division ab:          
> Bsp:          
>           
> 1. Teile den Faktor höchsten Grades von P durch den Faktor höchsten Grades von Q und nenne das Ergebnis R          
> 2. Addiere R zum Ergebnis          
> 3. Multipliziere Q mit R und ziehe von P ab.          
> 4. Ziehe einen weiteren Faktor von P nach unten und wiederhole bis der Grad von P kleiner als der von Q ist          
> Bsp:          
> Hierbei in der oberen Zeile steht eigentlich          
> $$          
> x^3-x^2-4x+4=(x-1)\times (x^2-4)          
> $$          
> ![[Pasted image 20241206211040.png]]          
>           
          
> [!important] Definition: Nullstellen          
> Für ein Polynom $P_n$ ist eine Zahl $z_0$ eine Nullstelle die sich mit $(z - z_0)^m * Q_{n-m} = 0$ ausklammern lässt. Die Anzahl an möglichen Ausklammerungen definiert die n-fachheit der Nullstelle.          
          
> [!warning] Technik: Linearfaktorzerlegung          
> 1. Errate eine Nullstelle          
> 2. Klammere die Nullstelle mithilfe der Polynomdivision aus          
> $$          
> P(x) = (z-z_0) \cdot \frac{P}{z-z_0} = (z-z_0) \cdot Q          
> $$          
> 3. Wiederhole dass bis $Q(z_0) \neq 0$          
> 4. Errate eine neue Nullstelle und fahre fort bis die Linearfaktorzerlegung erreicht ist          
          
> [!important] Definition: Rationale Funktion          
> TLDR: Quotient zweier Polynome          
> Mathematisch:          
> Gegeben seien die Polynome $P_n(x)$ und $Q_m(x)$          
> $$          
> R := \frac{P_n(x)}{Q_m(x)}          
> $$          
> $$          
> {x \in \mathbb{C} : Q_m(x) \neq 0}          
> $$          
          
> [!example] Satz: Normalform von Rationalen Funktionen          
> TLDR: Fall $n \geq m$  dann führt solange wie  $n \geq m$  Polynomdivision zur Normalform          
> Mathematisch:          
> Falls $n \geq m$, dann          
> $$          
> S_{n-m}, T_k,\ \textit{so dass  } R = S_{n-m} + \frac{T_k}{Q_m}          
> $$          
> mit Rest $T_k$          
> Beispiel:          
>![[Pasted image 20241206220827.png]]          
>Die Vereinfachung unten Rechts ist nur kosmetisch und nicht nötig          
          
          
          
          
