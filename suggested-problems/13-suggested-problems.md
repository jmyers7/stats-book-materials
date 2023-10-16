**Suggested problems for Sections [4.6](https://mml.johnmyersmath.com/stats-book/chapters/random-variables.html#the-algebra-of-random-variables) and [4.7](https://mml.johnmyersmath.com/stats-book/chapters/random-variables.html#functions-of-random-variables).** ([Solutions](./13-suggested-problems-sol.md))

---

**Problem 1**: Suppose that we have random variables $X$ and $Y$ defined on the probability space

$$
S = \\{1, 2, 3, 4, 5\\}
$$

as in the table

$$
\begin{array}{c|cc}
s & X(s) & Y(s) \\\ \hline
1 & 0 & -1\\
2 & 0 & -2\\
3 & 2 & -2\\
4 & 2 & 0\\
5 & 3 & 0
\end{array}	
$$

Suppose also that the probability measure on $S$ has mass function given by

$$
\begin{array}{c|c}
s & p(s) \\\ \hline
1 & 0.1\\
2 & 0.3\\
3 & 0.1\\
4 & 0.2\\
5 & 0.3
\end{array}
$$

**(a)** List the outputs of the random variables $X+Y$, $X-Y$, $3XY$, and $4X-5Y$.

**(b)** Compute the probability mass functions of the random variables $X$, $Y$, $X-Y$, and $3XY$.

---

**Problem 2**: Let $P$ be the (continuous) uniform probability measure on $\mathbb{R}$ with support $[0,2]$. Thus, $P$ has density function

$$
f(s) = \begin{cases}
1/2 & : 0 \leq s \leq 2, \\
0 & : \text{otherwise}.
\end{cases}
$$

Define two random variables by the formulas

$$
X: \mathbb{R} \to \mathbb{R}, \quad X(s) = s^2,
$$

and

$$
Y: \mathbb{R} \to \mathbb{R}, \quad Y(s) = 1.
$$

If the copies of $\mathbb{R}$ in the domains of $X$ and $Y$ are equipped with the measure $P$, and if $P_{X+Y}$ is the probability measure induced by the random variable $X+Y$ on the copy of $\mathbb{R}$ in its codomain, compute the following probabilities:

**(a)** $P\big(X+Y\in [1,2] \big)$

**(b)** $P\big( X+Y \in [0,1] \big)$

**(a)** $P\big( 2\leq X+Y \leq 5 \big)$

---

**Problem 3**: Let $P$ be the same probability measure on $\mathbb{R}$ as defined in the previous problem. Define a new random variable

$$
Z: \mathbb{R}\to \mathbb{R}, \quad Z(s) = s-1,
$$

and define the function

$$
g: \mathbb{R} \to \mathbb{R}, \quad g(z) = z^3.
$$

Similar to the previous problem, compute the following probabilities:

**(a)** $P\big(0\leq g(Z) \leq 1 \big)$

**(b)** $F_{g(Z)}(0)$
