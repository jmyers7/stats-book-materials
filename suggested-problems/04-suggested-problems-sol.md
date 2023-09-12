**Solutions for suggested problems for Section [2.10](https://mml.johnmyersmath.com/stats-book/chapters/prob-spaces.html#distribution-and-quantile-functions).**

---

**Problem 1**: 

**(a)** $P(\{-1\}) = 0.1$

**(b)** $P\big( (-\infty,0) \big) = 0.1$

**(c)** $P \big( (-\infty,0] \big) = F(0) = 0.2$

**(d)** $P(\{1\}) = 0$

**(e)** $P \big( (0,3] \big) = F(3) - F(0) = 0.6$

**(f)** $P \big( (0,3) \big) = P\big( (-\infty,3) \big) - F(0)=0.6 - 0.2 = 0.4$

**(g)** $P \big( [0,3] \big) = P\big( (-\infty,3] \big) - P\big((-\infty,0) \big) = 0.8 - 0.1 = 0.7$

**(h)** $P \big( (1,2] \big) = F(2) - F(1) = 0.3-0.3 = 0$

**(i)** $P \big( [1,2] \big) = F(2) - P\big( (-\infty, 1) \big) = 0.3 - 0.3 = 0$

**(j)** $P \big( (5,\infty) \big) = 1 - F(5) = 1-1 = 0$

**(k)** $P \big( [5, \infty) \big) = 1 - P\big( (-\infty,5)  \big) = 1 - 1 = 0$

**(l)** $P\big([3,4] \big) = F(4) - P \big( (-\infty,3) \big) = 0.8-0.6 = 0.2$

---

**Problem 2** Using the Fundamental Theorem of Calculus, we get that

$$
f(s) = F'(s) = \begin{cases}
\frac{2}{9}s & : 0 < s <3, \\
0 & : s<0 \text{ or } s>3.
\end{cases}
$$

Note that $f(s)$ is undefined at the points $s=0,3$ where $F(s)$ is not differentiable.