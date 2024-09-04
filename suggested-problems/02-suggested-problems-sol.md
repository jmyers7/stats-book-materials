**Solutions for suggested problems for Section [1.6](./02-suggested-problems.md).**

---

**Problem 1**:

(a) $P(A) = p(0) + p(1/2) = 1/12 + 1/2 \approx 0.583$.

(b) $P(A) = p(0) + p(1) = 1/12 + 1/3 \approx 0.417$.

(c) $P(A)= p(1) = 1/3 \approx 0.333$.

---

**Problem 2**:

**(a)** We have

$$
P(A) = \sum_{s=0}^2 \frac{(0.5)^s}{s!}e^{-0.5} = e^{-0.5} + (0.5)e^{-0.5} + \frac{1}{2}(0.5)^2 e^{-0.5} \approx 0.987.
$$

**(b)** We have

$$
P(A) = \sum_{s=0}^\infty \frac{(0.5)^{2s}}{(2s)!}e^{-0.5} = e^{-0.5} \cosh{(0.5)} \approx 0.684.
$$

---

**Problem 3**: 

**(a)** The sample space is

$$
S = \\{TTT,TTH,THT,THH,HTT,HTH,HHT,HHH \\}.
$$

The probability measure is discrete with mass function given by

$$
p(TTT) = (0.85)^3, \quad p(\text{two tails}) = 3(0.15)(0.85)^2, \quad p(\text{one tail}) = 3(0.15)^2(0.85), \quad p(HHH) = (0.15)^3.
$$

Since

$$
(0.85)^3 + 3(0.15)(0.85)^2 + 3(0.15)^2(0.85) + (0.15)^3 = \sum_{k=0}^3 \binom{3}{k}(0.85)^k(0.15)^{3-k} = (0.85+0.15)^3 = 1
$$

according to the [Binomial Theorem](https://en.wikipedia.org/wiki/Binomial_theorem#Statement) (or just add them up by hand), we have a valid probability measure.

**(b)** The sample space is

$$
S = \\{2,3,\ldots,12\\}.
$$

For the probability measure, observe that:

* We may obtain a sum of $2$ in only **one** way, by rolling two $1$'s. 
* We may obtain a sum of $3$ in **two** ways, by rolling a $2$ on the first roll and a $1$ on the second, or by rolling a $1$ on the first roll and a $2$ on the second. 
* _Etc._

Do you see the pattern? The ascending pattern continues till we reach $7\in S$, which may be obtained in six ways. Then, the pattern begins to descend till we reach $12\in S$, which may be obtained in only one way (by rolling two $6$'s).

Since the probability of rolling a particular pair of numbers is the same as any other, we have a chance of $1/36$ of rolling any particular pair of numbers. Therefore, combined with what we observed above, we see that:


$$p(2) = 1/36,$$

$$p(3) = 2/36,$$

$$p(4) = 3/36,$$

$$p(5) = 4/36,$$

$$p(6) = 5/36,$$

$$p(7) = 6/36,$$

$$p(8) = 5/36,$$

$$p(9) = 4/36,$$

$$p(10) = 3/36,$$

$$p(11) = 2/36,$$

$$p(12) = 1/36.$$

We note that this is a valid probability mass function, since

$$
\sum_{s=2}^{12} p(s) = 2\left( \frac{1}{36} + \frac{2}{36} + \frac{3}{36} + \frac{4}{36} + \frac{5}{36} \right) + \frac{6}{36} = 1.
$$

The probability that we obtain a sum $\leq 10$ is the same as

$$
1 - P(\text{sum} \geq 11) = 1 - \left( \frac{2}{36} + \frac{1}{36} \right) = \frac{11}{12}.
$$

---

**Problem 4**:

**(a)** Observe that since $A$ and $B$ are disjoint, we must have $B\subset A^c$. But then $B\cap A^c = B$, and so

$$
P(B\cap A^c) = P(B) = 1/2.
$$

**(b)** Since $A\subset B$, we have

$$
B = (B\cap A^c) \cup A.
$$

Since both of the sets on the right-hand side of this equation are disjoint, we have

$$
P(B\cap A^c) = P(B) - P(A) =  1/2 - 1/3 = 1/6.
$$

**(c)** Note that

$$
B = (B\cap A) \cup (B\cap A^c).
$$

Since both of the sets on the right-hand side of this equation are disjoint, we have

$$
P(B\cap A^c) = P(B) - P(A\cap B) = 1/2 - 1/8 = 3/8.
$$
