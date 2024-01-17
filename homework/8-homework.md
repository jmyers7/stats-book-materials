# Homework for [Chapter 8](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#)

**List of problems:**

1. [Expectation of a transformation of two variables](#problem-1-expectation-of-a-transformation-of-two-variables)
2. [Independence and expectations](#problem-2-independence-and-expectations)
3. [Expectation of a transformation of an IID random sample](#problem-3-expectation-of-a-transformation-of-an-iid-random-sample)
4. [Conditional expectations](#problem-4-conditional-expectations)
5. [Average scores on a standardized exam](#problem-5-average-scores-on-a-standardized-exam)
6. [A transformation of a uniform variable](#problem-6-a-transformation-of-a-uniform-variable)


**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted. You must show all relevant steps in any computations, and in problems that ask for explanations or proofs, you must write in complete sentences with correct grammar and correct notation. Sloppy and confusing solutions are inappropriate for students in a class at this level, and will be penalized accordingly.

## Problem 1: Expectation of a transformation of two variables

(_From [Section 8.1](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#expectations-and-joint-distributions)_.) Suppose that $X$ and $Y$ are jointly continuous with density

$$
f(x,y) = \begin{cases}
2x & : 0 \leq x \leq 1, \ 0 \leq y \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

Compute $E(XY)$.

## Problem 2: Independence and expectations

(_From [Section 8.1](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#expectations-and-joint-distributions)_.) Suppose that $X$ and $Y$ are two independent, continuous random variables. Prove that $E(XY) = E(X)E(Y)$. (This is [Theorem 8.2](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#ind-expect-thm) in the book.)

## Problem 3: Expectation of a transformation of an IID random sample

(_From [Section 8.1](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#expectations-and-joint-distributions)_.) Let three random variables $X$, $Y$, and $Z$ form an IID random sample from the continuous uniform distribution on $[0,1]$. Determine the value of the expectation

$$
E\left[ (X - 2Y + Z)^2\right].
$$

## Problem 4: Conditional expectations

(_From [Section 8.2](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#expectations-and-conditional-distributions)_.) Suppose that $X$ and $Y$ are jointly continuous with density

$$
f(x,y) = \begin{cases}
6(1-x) & : 0 \leq y \leq x \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

**(a)**: Compute $E(Y \mid X=x)$. Be sure to carefully identify the range of $x$-values for which this expectation is defined.

**(b)**: Using your answer to (a), compute the  expectation $E\left[ E(Y \mid X) \right]$ of the random variable $E(Y\mid X)$ via the LotUS.

**(c)**: Now, compute the maginal density $f(y)$ and use it to compute the expectation $E(Y)$ directly. Does this expectation agree with the one in part (b)?

## Problem 5: Average scores on a standardized exam

(_From [Section 8.2](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#expectations-and-conditional-distributions)_.) Suppose that 20% of students in a certain district attend School A, 30% attend School B, and the remaining 50% attend School C. The average score on a standardized exam of the students at School A is 80, the average score for those students at School B is 76, and the average score for students at School C is 84. If a student is selected at random from the entire school district, what is the expected value of their score on the exam?

## Problem 6: A transformation of a uniform variable

(_From [Section 8.3](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#density-transformations)_.) Let $X$ be the continuous random variable with density

$$
f(x) = \begin{cases}
1 & : 0 < x < 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

Thus, $X$ is uniformly distributed on $(0,1)$. Use the Density Transformation Theorem to compute the density of the random variable $Y  = 2 \sqrt{X}$. Is $Y$ uniform?