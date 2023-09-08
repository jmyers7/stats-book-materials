**Suggested problems for Section [2.8](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#continuous-probability-measures).** ([Solutions](./03-suggested-problems-sol.md))

---

**Problem 1**: Let $P$ be a continuous probability measure on the sample space $S = \mathbb{R}$ with density function

$$
f(s) = \begin{cases}
cs & : 0 < s < 4, \\
0 & : \text{otherwise,}
\end{cases}
$$

for some constant $c$. Find $c$ so that $f(s)$ is a valid PDF. Then, compute the probabilities $P(A)$ of the following events.

**(a)** $A = [1,2]$

**(b)** $A = (2,\infty)$

**(c)** $A = (-\infty,1) \cup [2,5]$

---

**Problem 2**: Let $P$ be a continuous probability measure on the sample space $S = \mathbb{R}$ with density function

$$
f(s) = \begin{cases}
\displaystyle\frac{1}{(1+s)^2} & : s>0, \\
0 & : s\leq 0.
\end{cases}
$$

**(a)** Verify that $f(s)$ is indeed a valid density function by proving $\int_{\mathbb{R}} f(s) \ \text{d}s=1$.

**(b)** Compute the probability $P\big( (1000,\infty) \big)$.

---

**Problem 3**: Let $P$ be a continuous probability measure on the sample space $S = \mathbb{R}$ with density function

$$
f(s) = \begin{cases}
\frac{4}{3}(1-s^3) & : 0 < s <1, \\
0 & : \text{otherwise}.
\end{cases}
$$

Sketch a graph of $f(s)$, and then compute the following probabilities.

**(a)** $P\big( [-10, 1/2) \big)$

**(b)** $P\big( (1/4, 3/4) \big)$

**(c)** $P\big( [1/3, 1000] \big)$

---

**Problem 4**: Show that there does not exist any constant $c$ such that the function

$$
f(s) = \begin{cases}
\frac{c}{1+s} & : s >0, \\
0 & : s \leq 0
\end{cases}
$$

is a density function of a continuous probability measure on $S = \mathbb{R}$.

---

**Problem 5**: (This problem briefly introduces *mixed probability measures*, which are probability measures that have both a continuous and discrete part.)

An ice cream seller takes 20 gallons of ice cream in her truck each day. Let $s\in \mathbb{R}$ stand for the number of gallons that she sells. The probability is $0.1$ that $s=20$. Otherwise, the probability measure $P$ has the density function

$$
f(s) = \begin{cases}
cs^2 & : 0 < s < 20, \\
0 & : \text{otherwise}
\end{cases}
$$

for some constant $c$. Find the constant $c$.