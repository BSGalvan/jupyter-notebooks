# Root-Finding

### Bisection

- Linear convergence since successive figures are won linearly.
- How do you handle oscillations, multiple roots, singularities? (One solution is plot and see!)

### Newton-Raphson

- Better than linear (actually quadratic convergence $\Rightarrow$ will get double the amount of digits with one step)
 \[x_{n+1} = x_n - \dfrac{f(x_n)}{f^{\prime}(x_n)}\]
- Works if function and first derivative are continuous near the root. Get from Taylor series expansion of the function around root. Also, works iff near root.

### *Regula Falsi* (False Position) Method

- Better than bisection if linear approximation of $f(x)$ is *good enough*.
- Basically, assume the function is a line near the root, and iteratively solve for the 'root' with this idea.
