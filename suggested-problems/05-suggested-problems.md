**Suggested problems for Section [2.11](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#bivariate-continuous-probability-measures).** ([Solutions](05-suggested-problems-sol.md))

---

**Problem 1**: Suppose that $P$ is a continuous probability measure on $S=\mathbb{R}^2$ with density function

$$
f(s,t) = \begin{cases}
ct^2 & : 0 \leq s \leq 2, \ 0 \leq t \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

**(a)** Determine the value of the constant $c$ that makes $f$ a valid PDF.

**(b)** Determine the probabilities $P(C_k)$ ($k=1,2,3,4$) for the following events:

* $C_1 = \\{(s,t) : s+t > 2\\}$

* $C_2 = \\{(s,t) : t < 1/2\\}$

* $C_3 = \\{(s,t) : s\leq 1 \\}$

* $C_4 = \\{(s,t) : s=3t\\}$

---

**Problem 2**: Suppose that $P$ is a continuous probability measure on $S=\mathbb{R}^2$ with density function

$$
f(s,t) = \begin{cases}
c(s^2 + t) & : 0 \leq t \leq 1-s^2,\\
0 & : \text{otherwise}.
\end{cases}
$$

**(a)** Determine the value of the constant $c$ that makes $f$ a valid PDF.

**(b)** Determine the probabilities $P(C_k)$ ($k=1,2,3$) for the following events:

* $C_1 = \\{ (s,t) : 0 \leq s \leq 1/2\\}$

* $C_2 = \\{ (s,t) : t \leq s + 1\\}$

* $C_3 = \\{ (s,t) : t=s^2\\}$

---

**Problem 3**: (This problem introduces you to bivariate discrete probability measures. Even though we didn't discuss these in class, I bet you'll have no problem imagining their definition.)

Suppose that $P$ is a bivariate discrete probability measure on $S= \mathbb{R}^2$ with mass function

$$
p(s,t) = \begin{cases}
c|s+t|  & : s,t \in \\{ -2, -1, 0, 1, 2\\}, \\
0 & : \text{otherwise}.
\end{cases}
$$

**(a)** Determine the value of the constant $c$ that makes $p$ a valid PMF.

**(b)** Determine the probabilities $P(C_k)$ ($k=1,2,3$) for the following events:

* $C_1 = \\{ (0,-2)\\}$

* $C_2 = \\{ (s,t) : s=1 \\}$

* $C_3 = \\{ (s,t) : |s-t| \leq 1 \\}$

---

**Problem 4**: (How about a probability measure with a mixed density/mass function?)

Suppose that a point $(s,t)$ is to be chosen in the square

$$
S = [0,1] \times [0,1].
$$

Suppose that:

* The probability of choosing the corner $(0,0)$ is $0.1$.
* The probability of choosing the corner $(1,0)$ is $0.2$.
* The probability of choosing the corner $(0,1)$ is $0.4$.
* The probability of choosing the corner $(1,1)$ is $0.1$.

Suppose also that if the chosen point is not one of the four corners of the square, then it will be an interior point in the square and it will chosen according to a constant density function over the interior of the square.

**(a)** Compute $P(C_1)$, where $C_1 = \\{ (s,t) : s\leq 1/4\\}$.

**(b)** Compute $P(C_2)$, where $C_2 = \\{(s,t) : s+t \leq 1\\}$.

---

**Problem 5**: A bank operates both a drive-up facility and a walk-up window. On a randomly selected day, let $s$ be the proportion of time that the drive-up facility is in use (at least one customer is being served or waiting to be served) and let $t$ the proportion of time that the walk-up window is in use. Suppose that $s$ and $t$ follow a continuous probability distribution $P$ on $S=\mathbb{R}^2$ with density function

$$
f(s,t) = \begin{cases}
\frac{6}{5}(s+t^2) & : 0\leq s, t \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

Compute the probability that neither facility is busy more than one quarter of the time.
