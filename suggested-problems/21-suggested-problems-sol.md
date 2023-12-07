**Solutions for suggested problems for Sections [7.7](https://mml.johnmyersmath.com/stats-book/chapters/random-vectors.html#the-law-of-total-probability-and-bayes-theorem-for-random-variables).** ([Problems](./21-suggested-problems.md))

---

**Problem 1**: From the Law of Total Probability, we get

$$
p(x) = \sum_{n=0}^m p(x|n)p(n)
$$

since the support of $p(n)$ is $\{0,1,\ldots,m\}$. However, we have $p(x|n) = 0$ if $x>n$, so we may assume that $x\leq n$. Since $n\leq m$ as well, we actually have

$$
p(x) = \sum_{n=x}^m p(x|n)p(n).
$$

Then, using the definitions of the binomial mass functions, we get:

$$
p(x) = \sum_{n=x}^m \binom{n}{x} \theta^x (1-\theta)^{n-x} \binom{m}{n} \phi^n (1-\phi)^{m-n}
$$

and so

$$
p(x) = \binom{m}{x} (\theta\phi)^x \sum_{n=x}^m \binom{m-x}{n-x} \big( (1-\theta)\phi\big)^{n-x}(1-\phi)^{m-n}.
$$

But an application of the [binomial theorem](https://en.wikipedia.org/wiki/Binomial_theorem#Statement) gives

$$
(1 - \theta\phi)^{m-x} = \sum_{n=x}^m \binom{m-x}{n-x} \big( (1-\theta)\phi\big)^{n-x}(1-\phi)^{m-n}.
$$

To see this, re-index the sum on the right-hand side with $k=n-x$. Putting everything together, we get

$$
p(x) = \binom{m}{x} (\theta\phi)^x (1 - \theta\phi)^{m-x},
$$

which is exactly the mass function of a $\mathcal{B}in(m,\theta\phi)$ distribution.

---

**Problem 2**:

**(a)** $p(x|\theta) = \theta(1-\theta)^{x-1}$, with support $x\in \{1,2,\ldots\}$.

**(b)** Note that the posterior density $f(\theta|x)$ is only defined for those $x$ for which the marginal mass $p(x)\neq 0$. We will need this marginal mass, so let's compute it using the Law of Total Probability:

$$
p(x) = \int_{\mathbb{R}} p(x|\theta)f(\theta) \ \text{d}\theta.
$$

We have $f(\theta) = 1$ with support $\theta \in [0,1]$. For these $\theta$-values, we get

$$
\int_{\mathbb{R}} p(x|\theta)f(\theta) \ \text{d}\theta = \int_0^1 \theta ( 1- \theta)^{x-1} \ \text{d} \theta = \frac{1}{x(x+1)},
$$

where the second equality holds if and only if $x\in \{1,2,\ldots,\}$ and where we used the substitution $u=1-\theta$ to compute the integral. Thus, we have

$$
p(x) = \frac{1}{x(x+1)}
$$

with support $x\in \{1,2,\ldots\}$.

Now, for $x\in \{1,2,\ldots\}$, from Bayes' Theorem we get

$$
f(\theta|x) = \frac{p(x|\theta)f(\theta)}{p(x)} = x(x+1) \theta (1-\theta)^{x-1} f(\theta) = x(x+1) \theta (1-\theta)^{x-1}
$$

where the third equality holds if and only if $\theta \in [0,1]$. Thus, $f(\theta|x)$ is only defined for $x\in \{1,2,\ldots\}$, and for these $x$-values we have

$$
f(\theta|x) = x(x+1)\theta(1-\theta)^{x-1}
$$

with support $\theta \in [0,1]$.