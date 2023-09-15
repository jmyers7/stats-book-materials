**Suggested problems for Section [2.10](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#distribution-and-quantile-functions).** ([Solutions](04-suggested-problems-sol.md))

---

**Problem 1**: Suppose that the CDF of a continuous probability measure $P$ on $S=\mathbb{R}$ is given by

$$
F(s) = \begin{cases}
0 & : s \leq 0, \\
\frac{1}{9}s^2 & : 0 < s \leq 3, \\
1 & : s>3.
\end{cases}
$$

Find and sketch a PDF of the measure $P$.

---

**Problem 2**: Suppose that the CDF of a continuous probability measure $P$ on $S=\mathbb{R}$ is given by

$$
F(s) = \begin{cases}
e^{s-3} & : s \leq 3, \\
1 & : s>3.
\end{cases}
$$

Find and sketch a PDF of the measure $P$.

---

**Problem 3**: Let $P$ be the continuous uniform distribution supported on the interval $[-2,8]$, so that its PDF is

$$
f(s) = \begin{cases}
1/10 & : -2 \leq s \leq 8, \\
0 & : \text{otherwise}.
\end{cases}
$$

Find and sketch the CDF of the measure $P$.

---

**Problem 4**: Let $P$ be the discrete probability measure on $S=\mathbb{R}$ with mass function

$$
p(s) = \begin{cases}
0.4 & : s=1, \\
0.3 & : s=2, \\
0.2 & : s=3, \\
0.1 & : s=4.
\end{cases}
$$

Find and sketch the CDF of the measure $P$.

---

**Problem 5**: A box contains five keys, only one of which will open a lock. Keys are randomly selected and tried, one at a time, until the lock is opened (keys that do not work are discarded before another is tried). Let $s\in \mathbb{R}$ be the number of the trial on which the lock is opened.

**(a)** Assuming the probability measure $P$ on $S$ is uniform, find the mass function of $P$. (*Hint*: It has support $\\{1,2,3,4,5\\}$.)

**(b)** Give the corresponding distribution function.

**(c)** What is $P\big((-\infty,3)\big)$?

**(d)** What is $F(3)$?

**(e)** What is $P\big(\\{3\\}\big)$?

---

**Problem 6**: Suppose that a probability measure $P$ on $S = \mathbb{R}$ has a CDF $F(s)$ whose graph is shown [here](../img/cdf.png). (Replace the $x$ with an $s$.) Compute the following probabilities:

**(a)** $P(\\{-1\\})$

**(b)** $P\big( (-\infty,0) \big)$

**(c)** $P \big( (-\infty,0] \big)$

**(d)** $P(\\{1\\})$

**(e)** $P \big( (0,3] \big)$

**(f)** $P \big( (0,3) \big)$

**(g)** $P \big( [0,3] \big)$

**(h)** $P \big( (1,2] \big)$

**(i)** $P \big( [1,2] \big)$

**(j)** $P \big( (5,\infty) \big)$

**(k)** $P \big( [5, \infty) \big)$

**(l)** $P\big([3,4] \big)$

---

**Problem 7**: For the CDF from Problem 1 above, find a formula for the quantile function.

---

**Problem 8**: For the CDF from Problem 2 above, find a formula for the quantile function.

---

**Problem 9**: Suppose that a probability measure $P$ on $S = \mathbb{R}$ has CDF given by

$$
F(s) = \begin{cases}
0 & : s <2, \\
1/8 & : 2\leq s < 2.5, \\
3/16 & : 2.5 \leq s < 4, \\
3/8 & : 4 \leq s < 5.5, \\
5/8 & : 5.5 \leq s < 6, \\
11/16 & : 6 \leq s <7 , \\
1 & : s\geq 7.
\end{cases}
$$

**(a)** Is the measure $P$ discrete or continuous? Explain.

**(b)** Compute a formula for either a mass function or density function of $P$, depending on whether you determine $P$ is discrete or continuous.

**(c)** Compute the median of the probability distribution $P$.
