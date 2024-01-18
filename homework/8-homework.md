# Homework for [Chapter 8](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#)

**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. [Expectation of a transformation of two variables](#problem-1-expectation-of-a-transformation-of-two-variables)
2. [Independence and expectations](#problem-2-independence-and-expectations)
3. [An expectation of a function of an IID random sample](#problem-3-an-expectation-of-a-function-of-an-iid-random-sample)
4. [Conditional expectations](#problem-4-conditional-expectations)
5. [Average scores on a standardized exam](#problem-5-average-scores-on-a-standardized-exam)
6. [A transformation of a uniform variable](#problem-6-a-transformation-of-a-uniform-variable)
7. [Practice with covariance and correlation](#problem-7-practice-with-covariance-and-correlation)
8. [A special case of bilinearity](#problem-8-a-special-case-of-bilinearity)
9. [Diagonals of positive semidefinite matrices](#problem-9-diagonals-of-positive-semidefinite-matrices)
10. [Practice with correlation matrices](#problem-10-practice-with-correlation-matrices)

 **Tips (to maximize your grade)**:
 
1. Show all relevant steps in all computations. However, I do not need to see trivial things like, for example, the intermediate steps in computing an integral. But if there is a key step in a set of computations that you skip over, I'll have to remove a point or two. Use your best judgment.

2. Explain your work and reasoning using complete and grammatically correct sentences. (It is a myth that mathematicians, engineers, and scientists are all bad at writing. We do many goodly words!)
 
3. Use correct notation.

4. Your goal is to demonstrate your depth of understanding, not simply that you obtained the correct answer. Your goal is to _explain_, as if you're trying to teach me the material.

5. Figure out the answer before writing! More precisely: Carry through your initial computations on your own scratch paper before writing your solutions.  It is difficult to follow a solution that is written in a "stream-of-consciousness" style. If I can't follow along, I am likely to give up and take off points (even if your final answer is right).


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

## Problem 3: An expectation of a function of an IID random sample

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

**(c)**: Now, compute the marginal density $f(y)$ and use it to compute the expectation $E(Y)$ directly. Does this expectation agree with the one in part (b)?

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

## Problem 7: Practice with covariance and correlation

(_From [Section 8.5](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#covariance-and-correlation)_.) Suppose that $X$ and $Y$ are jointly continuous with density

$$
f(x,y) = \begin{cases}
24xy & : 0 \leq x \leq 1, \ 0 \leq y \leq 1, \ x+y \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

**(a)**: Compute the marginal densities $f(x)$ and $f(y)$.

**(b)**: Note that $X$ and $Y$ are identically distributed. They are examples of what type of random variable from [Chapter 5](https://mml.johnmyersmath.com/stats-book/chapters/05-examples-of-rvs.html)? What are the parameters?

**(c)**: Compute the covariance $\sigma_{XY}$.

**(d)**: Compute the correlation $\rho_{XY}$.

## Problem 8: A special case of bilinearity

(_From [Section 8.5](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#covariance-and-correlation)_.) Let $X_1,X_2,Y_1,Y_2$ be four random variables. Prove

$$
\sigma(X_1+X_2,Y_1+Y_2) = \sigma(X_1,Y_1) + \sigma(X_1,Y_2) + \sigma(X_2,Y_1) +  \sigma(X_2,Y_2)
$$

## Problem 9: Diagonals of positive semidefinite matrices

(_From [Section 8.5](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#covariance-and-correlation)._) Let $\mathbf{A}=[a_{ij}]$ be a positive semidefinite $d\times d$ matrix. Prove that the diagonal entries $a_{ii}$ ($i=1,\ldots,d$) are all nonnegative.

## Problem 10: Practice with correlation matrices

(_From [Section 8.5](https://mml.johnmyersmath.com/stats-book/chapters/08-more-prob.html#covariance-and-correlation)._) Let $\mathbf{X} = (X_1,X_2,X_3)$ be a continuous random vector with density

$$
f(x_1,x_2,x_3) = \begin{cases}
2x & : 0\leq x_1 \leq 1, \ 0\leq x_2 \leq 1, \ 0 \leq x_3 \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

**(a)**: Are $X_1$, $X_2$, and $X_3$ are independent? Be sure to entirely and completely justify your reasoning with the utmost care.

**(b)**: Compute the correlation matrix $\mathbf{P}_\mathbf{X}$.
