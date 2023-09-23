**Solutions for suggested problems for Section [2.11](./05-suggested-problems.md).**

---

**Problem 1**:

**(a)** Since $f(s,t) \geq 0$ for all $(s,t)$ (assuming $c\geq 0$) we must only choose $c$ such that

$$
\iint_{\mathbb{R}^2} f(s,t) \ \text{d}s\text{d}t= 1.
$$

But

$$
\iint_{\mathbb{R}^2} f(s,t) \ \text{d}s\text{d}t = c \int_0^1 \int_0^2 t^2 \ \text{d}s \text{d}t = \frac{2}{3} c,
$$

and hence we must have $c = 3/2$.

**(b)** For the first event, we have

$$
P(C_1) = \iint_{C_1} f(s,t) \ \text{d}t\text{d}s = \frac{3}{2}\int_1^2\int_{2-s}^1 t^2 \ \text{d}t \text{d}s = \frac{3}{8}.
$$

For the second event, we have

$$
P(C_2) = \iint_{C_2} f(s,t) \ \text{d}s\text{d}t = \frac{3}{2}\int_0^{1/2} \int_0^2 t^2 \ \text{d} s \text{d} t = \frac{1}{8}.
$$

For the third event, we have

$$
P(C_3) = \iint_{C_3} f(s,t) \ \text{d}s \text{d} t = \frac{3}{2} \int_0^1 \int_0^1 t^2 \ \text{d} s \text{d} t = \frac{1}{2}.
$$

For the fourth event, we note that $C_4$ is a line in the $(s,t)$-plane. We then have $P(C_4)=0$, since the volume underneath a surface and above a line must always be zero.

---

**Problem 2**:

**(a)** Since $f(s,t)\geq 0$ for all $(s,t)$ (assuming $c\geq 0$), we must only choose $c$ such that

$$
\iint_{\mathbb{R}^2} f(s,t) \ \text{d}t \text{d}s = 1.
$$

But

$$
\iint_{\mathbb{R}^2} f(s,t) \ \text{d}t \text{d}s = c \int_{-1}^1 \int_0^{1-s^2} (s^2 + t) \ \text{d}t \text{d} s = \frac{4}{5}c,
$$

and hence we must have $c = 5/4$.

**(b)** For the first event, we have

$$
P(C_1) = \iint_{C_1} f(s,t) \ \text{d}t \text{d}s = \frac{5}{4} \int_0^{1/2} \int_0^{1-s^2} (s^2 + t) \ \text{d}t \text{d} s = \frac{79}{256}.
$$

For the second event,

$$
P(C_2) = \iint_{C_1} f(s,t) \ \text{d}t \text{d}s = \frac{5}{4} \int_0^1 \int_{t-1}^{\sqrt{1-t}} (s^2 + t) \ \text{d}s \text{d}t = \frac{13}{16}.
$$

For the third event, we note that $C_3$ is a parabola in the $(s,t)$-plane. We then have $P(C_3)=0$, since the volume underneath a surface and above a curve must always be zero.

---

**Problem 3**: 

**(a)** Since $p(s,t) \geq 0$ for all $(s,t)$ (assuming $c\geq 0$), we must only choose $c$ such that

$$
\sum_{(s,t)\in \mathbb{R}^2} p(s,t) = 1.
$$

But

$$
\sum_{(s,t)\in \mathbb{R}^2} p(s,t) = c \sum_{s=-2}^2 \sum_{t=-2}^2 p(s,t) = 2c\big(1 \cdot 4 + 2\cdot 3 + 3 \cdot 2 + 4\cdot 1 \big) = 40c,
$$

so that we must have $c = 1/40$. (It helps to draw a picture of the support of $p(s,t)$ in the $(s,t)$-plane. Then find lines of slope $-1$ along which $p(s,t)$ is constant and count the points along these lines.)

**(b)** For the first event, we have

$$
P(C_1) = \sum_{(s,t) \in C_1} p(s,t) = p(0, -2) = \frac{1}{40} |0 - 2| = \frac{1}{20}.
$$

For the second event, we have

$$
P(C_2) = \sum_{(s,t) \in C_2}p(s,t) = \sum_{t=-2}^2 p(1,t)= \frac{1}{40}(1 + 0 + 1 + 2 + 3 ) = \frac{7}{40}.
$$

For the third event, we first note that the inequality $|s-t|\leq 1$ is equivalent to the pair of simultaneous inequalities

$$
s-1 \leq t \leq s+1.
$$

If we imagine $t=s-1$ and $t=s+1$ as lines in the $(s,t)$-plane, then $C_3$ consists of all points that lie between (or on) these parallel lines. There are exactly 13 of these points; if we sum the mass function over them, we get

$$
P(C_3) = \sum_{(s,t)\in C_3} = \frac{2}{40}\big( 2\cdot 1 + 2 + 2\cdot 3 + 4) = 0.7.
$$

---

**Problem 4**: First, if $(s,t)$ is in the interior of the square, we must have

$$
f(s,t) = \frac{1}{5}.
$$

This is because there is already probability mass of size

$$
0.1 + 0.2 + 0.4 + 0.1 = 0.8
$$

placed at the corners of the square, and so the rest of the probability (equal to $0.2 = 1/5$) must be spread continuously and uniformly over the interior of the square.

**(a)** We have

$$
P(C_1) = \frac{1}{5} \int_0^1 \int_0^{1/4}  \text{d}s \text{d}t + 0.1 + 0.4 = 0.55,
$$

where $0.1$ and $0.4$ are the probability masses at the corners $(0,0)$ and $(0,1)$.

**(b)** We have

$$
P(C_2) = \frac{1}{5} \int_0^1 \int_0^{1-s} \text{d}t\text{d}s + 0.1 + 0.4 + 0.2 = 0.8,
$$

where, as in the previous part, $0.1$, $0.4$, and $0.2$ are the probability masses at the corners $(0,0)$, $(0,1)$, and $(1,0)$.

---

**Problem 5**: We are asked to compute $P(C)$, where

$$
C = \\{ (s,t) : 0 \leq s, t\leq 1/4\\}.
$$

Then, we have

$$
P(C) = \iint_C f(s,t) \ \text{d}s\text{d}t = \frac{6}{5} \int_0^{1/4} \int_0^{1/4} (s+t^2) \ \text{d}s \text{d}t = \frac{7}{640} \approx 0.011.
$$
