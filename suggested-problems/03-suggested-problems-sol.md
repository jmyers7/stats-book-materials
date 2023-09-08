**Solutions for suggested problems for Section [2.8](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#continuous-probability-measures).**

---

**Problem 1**: 

**(a)** In order for $f(s)$ to be a valid density, we must have

$$
\int_{\mathbb{R}} f(s) \ \text{d} s = 1.
$$

Integrating the left-hand side gives:

$$
\int_{\mathbb{R}} f(s) \ \text{d} s = c\int_0^4 s \ \text{d} s = 8c.
$$

So, we must have $8c = 1$, which means $c=1/8$.

Then:

**(a)** We compute

$$
P\big([1,2]\big) = \frac{1}{8}\int_1^2 s \ \text{d} s = \frac{3}{16}.
$$

**(b)** We compute

$$
P\big((2,\infty)\big) = \frac{1}{8} \int_2^4 s \ \text{d} s = \frac{3}{4}.
$$

**(c)** We compute

$$
P\big((-\infty,1) \cup [2,5] \big) = \frac{1}{8}\int_0^1 s \ \text{d} s + \frac{1}{8} \int_2^4 s \ \text{d} s = \frac{13}{16}.
$$

---

**Problem 2**: 

**(a)** We compute:

$$
\int_{\mathbb{R}} f(s) \ \text{d}s = \int_{0}^{\infty} \frac{1}{(1+s)^2} \ \text{d}s = 1 - \lim_{s\to \infty} \frac{1}{1+s} = 1.
$$

**(b)** We compute:

$$
P\big( (1000,\infty) \big) = \int_{1000}^\infty \frac{1}{(1+s)^2} \ \text{d} s = \frac{1}{1001} -\lim_{s\to \infty} \frac{1}{1+s} = \frac{1}{1001}.
$$

---

**Problem 3**: I'll let you draw the graph of $f(s)$ on your own.

**(a)** We have

$$
P\big( [-10, 1/2) \big) = \frac{4}{3}\int_{0}^{1/2}(1-s^3) \ \text{d}s = \frac{31}{48}.
$$

**(b)** We have

$$
P\big( (1/4, 3/4) \big) = \frac{4}{3} \int_{1/4}^{3/4} (1-s^3) \ \text{d}s = \frac{9}{16}.
$$

**(c)** We have

$$
P\big( [1/3, 1000] \big) = \frac{4}{3} \int_{1/3}^1 (1-s^3) \ \text{d} s = \frac{136}{243}.
$$

---

**Problem 4**: We will show that

$$
\int_{\mathbb{R}} f(s) \ \text{d} s = \infty
$$

no matter what we might choose for $c$. So, notice:

$$
\int_{\mathbb{R}} f(s) \ \text{d} s = c \int_0^\infty \frac{1}{1+s} \ \text{d} s= \lim_{s\to \infty} c \ln{(1+s)} = \infty.
$$

---

**Problem 5**: We must have

$$
\int_{\mathbb{R}} f(s) \ \text{d}s = 0.9.
$$

Do you see why? Why doesn't it matter that we integrate "over" the point $s=20$, which already has probability $0.1$ assigned to it?

Once you convince yourself that this equation is correct, we carry out the integration on the left-hand side to get

$$
\int_{\mathbb{R}} f(s) \ \text{d}s = c\int_0^{20} s^2 \ \text{d}s = \frac{8000c}{3}.
$$

Thus, we must have $8000c/3=0.9$, which implies $c=27/80000$.