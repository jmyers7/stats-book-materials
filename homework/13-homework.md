# Homework for [Chapter 13: Learning](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html)

**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. [Section 13.1: Negative logarithms and optimization](#problem-1-negative-logarithms-and-optimization)
2. [Section 13.1: MLEs for the univariate Bernoulli model](#problem-2-mles-for-the-univariate-bernoulli-model)

 **Tips (to maximize your grade)**:
 
1. Show all relevant steps in all computations. However, I do not need to see trivial things like, for example, the intermediate steps in computing an integral. But if there is a key step in a set of computations that you skip over, I'll have to remove a point or two. Use your best judgment.

2. Explain your work and reasoning using complete and grammatically correct sentences. (It is a myth that mathematicians, engineers, and scientists are all bad at writing. We do many goodly words!)
 
3. Use correct notation.

4. Your goal is to demonstrate your depth of understanding, not simply that you obtained the correct answer. Your goal is to _explain_, as if you're trying to teach me the material.

5. Figure out the answer before writing! More precisely: Carry through your initial computations on your own scratch paper before writing your solutions.  It is difficult to follow a solution that is written in a "stream-of-consciousness" style. If I can't follow along, I am likely to give up and take off points (even if your final answer is right).


## Problem 1: Negative logarithms and optimization

(_From [Section 13.1](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html#a-first-look-at-likelihood-based-learning-objectives)_.) It was mentioned in class that the maximizers of a (nonnegatively-valued) function are the same as the minimizers of the negative logarithm of the function. In this problem, you will prove this statement.

Precisely, let $J:\mathbb{R}^n \to (0,\infty)$ be an objective function taking values in the interval $(0,\infty)$.

**(a)**: Prove that $\boldsymbol{\theta}^\star \in \mathbb{R}^n$ is a global maximizer of $J(\boldsymbol{\theta})$ if it is a global minimizer of $-\log{J(\boldsymbol{\theta})}$. (_Hint_: The negative logarithm function is a _strictly decreasing function_. What's the definition of a _strictly decreasing function_? Look it up! Also, do **not** assume any form of differentiability!)

**(b)**: Conversely, prove that $\boldsymbol{\theta}^\star \in \mathbb{R}^n$ is a global minimizer of $-\log{J(\boldsymbol{\theta})}$ if it is a global maximizer of $J(\boldsymbol{\theta})$.

## Problem 2: MLEs for the univariate Bernoulli model

(_From [Section 13.1](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html#a-first-look-at-likelihood-based-learning-objectives)_.) Suppose we choose to model an observed dataset

$$
1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0
$$

with our simple Bernoulli PGM with parameter $\theta$. In all parts below that require computations, round your final answer to three decimal places.

**(a)**: Plot the data surprisal function $\mathcal{I}(\theta;x_1,\ldots,x_{11})$.

**(b)**: Compute the maximum likelihood estimate $\theta^\star_\text{MLE}$ for $\theta$.

**(c)**: Compute the data surprisal $\mathcal{I}(\theta^\star_\text{MLE};x_1,\ldots,x_{11})$ corresponding to the MLE.

**(d)**: Compute the data likelihood $\mathcal{L}(\theta^\star_\text{MLE};x_1,\ldots,x_{11})$ corresponding to the MLE.

**(e)**: If $P_\theta$ is the model distribution of the Bernoulli model and $\hat{P}$ is the empirical distribution of the dataset, compute the cross entropy $H_{\hat{P}}(P_{\theta^\star_\text{MLE}})$.

**(f)**: Compute the KL divergence $D(\hat{P} \parallel P_{\theta^\star_\text{MLE}})$.
