**Suggested problems for Section [2.6](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#discrete-and-uniform-probability-measures):**

---

**Problem 1**: Let $P$ be the discrete probability measure on the sample space $S=\mathbb{R}$ with mass function

$$
p(s) = \begin{cases}
1/12 & : s=0, \\
1/2 & : s=1/2, \\
1/3 & : s=1, \\
1/12 & : s=4, \\
0 & : \text{otherwise}.
\end{cases}
$$

Compute the probabilities $P(A)$ of the following events.

**(a)** $A = (-\infty,1)$

**(b)** $A = \\{0\\} \cup [1,4)$

**(c)** $A = [-10, 1] \cap [1, 4)$

---

**Problem 2**: Let $P$ be the discrete probability measure on the sample space $S = \mathbb{R}$ with mass function

$$
p(s) = \begin{cases}
\displaystyle\frac{(0.5)^s}{s!}e^{-0.5} & : s=0,1,2,\ldots, \\
0 & : \text{otherwise}.
\end{cases}
$$

Compute the probabilities $P(A)$ of the following events.

**(a)** $A = [-5, 2]$

**(b)** $A = \\{\text{all nonnegative even integers}\\}$ (_Hint_: The formula for hyperbolic cosine [here](https://en.wikipedia.org/wiki/Hyperbolic_functions#Taylor_series_expressions) might be helpful.)

---

**Problem 3**: Describe in complete detail a probability space that models each of the following scenarios. Be sure to check that the two requirements in the Discrete Probability Construction Lemma are both satisfied.

**(a)** Flipping an **unfair** coin three times, with probability $0.15$ of obtaining heads, and probability $0.85$ of obtaining tails. What is the probability that you flip _exactly_ two heads?

**(b)** The sum of the results of rolling two **fair** six-sided dice. What is the probability that you obtain a sum less than or equal to $10$?

---

**Problem 4**: Suppose that $A$ and $B$ are two events in a sample space $S$ with $P(A) = 1/3$ and $P(B) = 1/2$. Compute the probability $P(B\cap A^c)$ in each of the following scenarios:

**(a)** $A\cap B = \emptyset$

**(b)** $A\subset B$

**(c)** $P(A \cap B) = 1/8$.
