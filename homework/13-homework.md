# Homework for [Chapter 13: Learning](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html)

**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. [Section 13.1: Negative logarithms and optimization](#problem-1-negative-logarithms-and-optimization)
2. [Section 13.1: MLEs for the univariate Bernoulli model](#problem-2-mles-for-the-univariate-bernoulli-model)
3. [Section 13.2: Training objectives for Naive Bayes models](#problem-3-training-objectives-for-naive-bayes-models)

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
x_1,x_2,\ldots,x_{11} = 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0
$$

with our simple Bernoulli PGM with parameter $\theta$. In all parts below that require computations, round your final answer to three decimal places.

**(a)**: Plot the data surprisal function $\mathcal{I}(\theta;x_1,\ldots,x_{11})$.

**(b)**: Compute the maximum likelihood estimate $\theta^\star_\text{MLE}$ for $\theta$.

**(c)**: Compute the data surprisal $\mathcal{I}(\theta^\star_\text{MLE};x_1,\ldots,x_{11})$ corresponding to the MLE.

**(d)**: Compute the data likelihood $\mathcal{L}(\theta^\star_\text{MLE};x_1,\ldots,x_{11})$ corresponding to the MLE.

**(e)**: If $P_\theta$ is the model distribution of the Bernoulli model and $\hat{P}$ is the empirical distribution of the dataset, compute the cross entropy $H_{\hat{P}}(P_{\theta^\star_\text{MLE}})$.

**(f)**: Compute the KL divergence $D(\hat{P} \parallel P_{\theta^\star_\text{MLE}})$.

## Problem 3: Training objectives for Naive Bayes models

(_From [Section 13.2](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html#general-mle)_.) Consider a Naive Bayes model as described in the [programming assignment](https://github.com/jmyers7/stats-book-materials/blob/main/programming-assignments/assignment_12.ipynb) for [Chapter 12](https://mml.johnmyersmath.com/stats-book/chapters/12-models.html). The underlying graph is of the form

<br>
<center>
<img src="https://raw.githubusercontent.com/jmyers7/stats-book-materials/main/img/nb.svg" width="200" align="center">
</center>
<br>

where $\mathbf{X}\in \mathbb{R}^n$. The parameters are described as follows:

1. The parameter $\psi$ is a real number in $[0,1]$ such that $Y\sim Ber(\psi)$.

2. The parameters $\boldsymbol{\theta}_0$ and $\boldsymbol{\theta}_1$ are vectors in $[0,1]^n$.

The link function at $\mathbf{X}$ is given by

$$
p(\mathbf{x} \mid y; \boldsymbol{\theta}_0,\boldsymbol{\theta}_1) = \prod_{j=1}^n \phi_j^{x_j}(1-\phi_j)^{1-x_j} \quad \text{where} \quad \boldsymbol{\phi} = (1-y)\boldsymbol{\theta}_0 + y \boldsymbol{\theta}_1
$$

and $\boldsymbol{\phi}^\intercal = (\phi_1,\ldots,\phi_n)$.

**(a)**: Assuming that Naive Bayes models are trained as **generative** models, write down an explicit formula for the model likelihood function $\mathcal{L}_\text{model}(\psi,\boldsymbol{\theta}_0,\boldsymbol{\theta}_1)$. Your formula will involve $\psi$, $y$, all the $x_j$'s, and all the $\theta_{ij}$'s, where

$$
\boldsymbol{\theta}_0^\intercal = (\theta_{01},\ldots,\theta_{0n}) \quad \text{and} \quad \boldsymbol{\theta}_1^\intercal = (\theta_{11},\ldots,\theta_{1n}).
$$

**(b)**: Using your answer from part (a), write down a formula for the model surprisal function $\mathcal{I}_\text{model}(\psi,\boldsymbol{\theta}_0,\boldsymbol{\theta}_1)$.