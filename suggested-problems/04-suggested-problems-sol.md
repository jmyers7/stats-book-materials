**Solutions for suggested problems for Section [2.10](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#distribution-and-quantile-functions).**

---

**Problem 1**: Using the Fundamental Theorem of Calculus (Probability Version), we get that

$$
f(s) = F'(s) = \begin{cases}
\frac{2}{9}s & : 0 < s <3, \\
0 & : s<0 \text{ or } s>3.
\end{cases}
$$

Note that $f(s)$ is undefined at the points $s=0,3$ where $F(s)$ is not differentiable. I will let you produce the sketch of the graph on your own.

---

**Problem 2**: Using the Fundamental Theorem of Calculus (Probability Version), we get that

$$
f(s) = F'(s) = \begin{cases}
e^{s-3} & : s<3, \\
0 & : s>3.
\end{cases}
$$

Note that $f(s)$ is undefined at the point $s=3$ where $F(s)$ is not differentiable. I will let you produce the sketch of the graph on your own.

---

**Problem 3**: For all $s\in \mathbb{R}$, we have

$$
F(s) = P\big( (-\infty,s] \big) = \int_{-\infty}^s f(s) \ \text{d}s.
$$

If $s\leq -2$, then we must have $F(s)=0$. But if $-2 \leq s \leq 8$, then we have

$$
F(s) = \int_{-2}^s \frac{1}{10} \ \text{d}t = \frac{1}{10} (s+2).
$$

Finally, if $s\geq 8$, then $F(s)=1$. So, altogether, we have

$$
F(s) = \begin{cases}
0 & : s \leq -2, \\
\frac{1}{10}(s+2) & : -2 \leq s \leq 8, \\
1 & : s\geq 8.
\end{cases}
$$

I will let you produce the sketch of the graph on your own.

---

**Problem 4**: We have

$$
F(s) = \begin{cases}
0 & : s<1, \\
0.4 & : 1 \leq s < 2, \\
0.7 & : 2\leq s <3, \\
0.9 & : 3\leq s < 4, \\
1 & : s\geq 4.
\end{cases}
$$

I will let you produce the sketch of the graph on your own.

---

**Problem 5**:

**(a)** The mass function is given by

$$
p(s) = \begin{cases}
0.2 & : s\in \\{1,2,3,4,5\\}, \\
0 & : \text{otherwise}.
\end{cases}
$$

**(b)** The CDF is

$$
F(s) = \begin{cases}
0 & : s < 1, \\
0.2 &: 1\leq s < 2, \\
0.4 & : 2\leq s <3, \\
0.6 & : 3\leq s < 4, \\
0.8 & : 4\leq s < 5, \\
1 & : s\geq 5.
\end{cases}
$$

**(c)** $P\big((-\infty,3)\big) = 0.4$

**(d)** $F(3) = 0.6$

**(e)** $P\big(\\{3\\}\big) = 0.2$

---

**Problem 6**: 

**(a)** $P(\\{-1\\}) = 0.1$

**(b)** $P\big( (-\infty,0) \big) = 0.1$

**(c)** $P \big( (-\infty,0] \big) = F(0) = 0.2$

**(d)** $P(\\{1\\}) = 0$

**(e)** $P \big( (0,3] \big) = F(3) - F(0) = 0.6$

**(f)** $P \big( (0,3) \big) = P\big( (-\infty,3) \big) - F(0)=0.6 - 0.2 = 0.4$

**(g)** $P \big( [0,3] \big) = P\big( (-\infty,3] \big) - P\big((-\infty,0) \big) = 0.8 - 0.1 = 0.7$

**(h)** $P \big( (1,2] \big) = F(2) - F(1) = 0.3-0.3 = 0$

**(i)** $P \big( [1,2] \big) = F(2) - P\big( (-\infty, 1) \big) = 0.3 - 0.3 = 0$

**(j)** $P \big( (5,\infty) \big) = 1 - F(5) = 1-1 = 0$

**(k)** $P \big( [5, \infty) \big) = 1 - P\big( (-\infty,5)  \big) = 1 - 1 = 0$

**(l)** $P\big([3,4] \big) = F(4) - P \big( (-\infty,3) \big) = 0.8-0.6 = 0.2$

---

**Problem 7**: Restricted to $s\in (0, 3]$, the quantile function $s=Q(p)$ is the inverse of the distribution function $p = F(s)$. So, we solve:

$$
p = \frac{1}{9}s^2 \quad \Rightarrow \quad s = 3 \sqrt{p},
$$

which shows $Q(p) = 3 \sqrt{p}$ for $0 < p \leq 1$.

---

**Problem 8**: Restricted to $s\in (-\infty, 3]$, the quantile function $s=Q(p)$ is the inverse of the distribution function $p=F(s)$. So, we solve:

$$
p = e^{s-3} \quad \Rightarrow \quad s = \ln(p) + 3,
$$

which shows $Q(p) = \ln(p) + 3$ for $0 < p \leq 1$.

---

**Problem 9**:

**(a)** The probability measure $P$ is discrete, since its CDF is a step function. (Draw the graph!)

**(b)** The mass function of $P$ is give by

$$
p(s) = \begin{cases}
1/8 & : s=2, \\
1/16 & : s=2.5, \\
3/16 & : s=4, \\
1/4 & : s=5.5, \\
1/16 & : s=6, \\
5/16 & : s=7.
\end{cases}
$$

**(c)** The median is

$$
Q(0.5) = \min\\{ s\in \mathbb{R} : 0.5 \leq F(s)\\} = 5.5.
$$
