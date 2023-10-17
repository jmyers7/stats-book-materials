**Solutions for suggested problems for Sections [4.6](https://mml.johnmyersmath.com/stats-book/chapters/random-variables.html#the-algebra-of-random-variables) and [4.7](https://mml.johnmyersmath.com/stats-book/chapters/random-variables.html#functions-of-random-variables).** ([Problems](./13-suggested-problems.md))

---

**Problem 1**:

**(a)** We have

$$
\begin{array}{c|cc}
s & X(s) & Y(s) & (X+Y)(s) & (X-Y)(s) & (3XY)(s) & (4X-5Y)(s) \\\ \hline
1 & 0 & -1 & -1 & 1 & 0 & 5\\
2 & 0 & -2 & -2 & 2 & 0 & 10\\
3 & 2 & -2 & 0 & 4 & -12 & 18\\
4 & 2 & 0 & 2 & 2 & 0 & 8\\
5 & 3 & 0 & 3 & 3 & 0 & 12
\end{array}	
$$

**(b)** We have

$$
p_X(x) = \begin{cases}
0.4 & : x=0, \\
0.3 & : x=2, \\
0.3 & : x=3, \\
0 & : \text{otherwise},
\end{cases}
$$

and

$$
p_Y(y) = \begin{cases}
0.4 & : y=-2, \\
0.1 & : y=-1, \\
0.5 & : y=0, \\
0 & : \text{otherwise},
\end{cases}
$$

and

$$
p_{X-Y}(z) = \begin{cases}
0.1 & : z=1, \\
0.5 & : z=2, \\
0.3 & : z=3, \\
0.1 & : z=4, \\
0 & : \text{otherwise},
\end{cases}
$$

and

$$
p_{3XY}(z) = \begin{cases}
0.1 & : z = -12, \\
0.9 & : z=0, \\
0 & : \text{otherwise}.
\end{cases}
$$


---

**Problem 2**:

**(a)** Recall (by definition!) that

$$
P(X+Y\in [1,2]) \stackrel{\text{def}}{=} P_{X+Y}\big( [1,2] \big) \stackrel{\text{def}}{=} P\big( \\{s\in \mathbb{R} : (X+Y)(s) \in [1,2]\\} \big).
$$

But $(X+Y)(s) = X(s) + Y(s) = s^2 +1$, so we may rewrite the condition

$$
(X+Y)(s) \in [1,2]
$$

as

$$
s^2 + 1 \in [1,2].
$$

But if you inspect a graph of the function $s^2+1$ (or use some other means), you will see that $s^2 + 1\in [1,2]$ precisely when $s\in [-1,1]$. Therefore, we have

$$
P(X+Y\in [1,2]) = P\big([-1,1] \big) = \int_{-1}^1 f(s) \ \text{d} s = \frac{1}{2} \int_0^1\text{d}s = \frac{1}{2}.
$$

**(b)** Since

$$
s^2 + 1 \notin [0,1]
$$

for all $s\in \mathbb{R}$, we have

$$
P(X+Y\in [0,1])=P_{X+Y}\big([0,1] \big) = P_{X+Y} (\emptyset) = 0.
$$

**(c)** Since

$$
s^2 +1 \in [2,5]
$$

when $s \in [-2,-1]\cup[1,2]$, we have

$$
P(2\leq X+Y \leq 5) = P\big([-2,-1] \big) + P\big([1,2]\big) = \int_{-2}^{-1}f(s) \ \text{d}s + \int_1^2 f(s) \ \text{d}s = \frac{1}{2} \int_1^2\text{d}s = \frac{1}{2}.
$$

---

**Problem 3**:

**(a)** Just like the previous problem, we have

$$
P\big(0\leq g(Z) \leq 1 \big) = P_{g(Z)}\big([0,1] \big) = P \big( \\{ s\in \mathbb{R} : g(Z) \in [0,1] \\} \big).
$$

But $\big(g(Z)\big)(s) = (s-1)^3$, so we may rewrite the condition

$$
g(Z) \in [0,1]
$$

as

$$
(s-1)^3 \in [0,1].
$$

But again, if you inspect a graph of $(s-1)^3$, you will see that $(s-1)^3 \in [0,1]$ exactly when $s\in [1,2]$. Thus, we have

$$
P\big(0\leq g(Z) \leq 1 \big) = P\big([1,2] \big) = \frac{1}{2}.
$$

**(b)** By definition, we have

$$
F_{g(Z)}(0) = P_{g(Z)} \big( (-\infty,0] \big).
$$

But

$$
P_{g(Z)} \big( (-\infty,0] \big) = P\big(\\{s\in \mathbb{R} : g(Z) \in (-\infty,0]\\} \big).
$$

Using the same methods as above, we determine

$$
\\{s\in \mathbb{R} : g(Z) \in (-\infty,0]\\} = (-\infty,1],
$$

and so

$$
F_{g(Z)}(0) = P\big((-\infty,1] \big) = \frac{1}{2}.
$$
