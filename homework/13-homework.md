# Homework for [Chapter 13: Learning](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html)

**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. 

 **Tips (to maximize your grade)**:
 
1. Show all relevant steps in all computations. However, I do not need to see trivial things like, for example, the intermediate steps in computing an integral. But if there is a key step in a set of computations that you skip over, I'll have to remove a point or two. Use your best judgment.

2. Explain your work and reasoning using complete and grammatically correct sentences. (It is a myth that mathematicians, engineers, and scientists are all bad at writing. We do many goodly words!)
 
3. Use correct notation.

4. Your goal is to demonstrate your depth of understanding, not simply that you obtained the correct answer. Your goal is to _explain_, as if you're trying to teach me the material.

5. Figure out the answer before writing! More precisely: Carry through your initial computations on your own scratch paper before writing your solutions.  It is difficult to follow a solution that is written in a "stream-of-consciousness" style. If I can't follow along, I am likely to give up and take off points (even if your final answer is right).

## Problem 1:

(_From [Section 13.1](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html#a-first-look-at-likelihood-based-learning-objectives)_.) It was mentioned in class that global minimizers of a function are the same as global maximizers of the negative of the function. In this problem, you will **rigorously** prove this statement from first principles.

Precisely, let $J:\mathbb{R}^n \to \mathbb{R}$ be a function.

**(a)**: Prove that $\boldsymbol\theta^\star \in \mathbb{R}^n$ is a global minimizer of $J(\boldsymbol\theta)$ if it is a global minimizer of $-J(\boldsymbol\theta)$.

**(b)**: Conversely, prove that $\boldsymbol\theta^\star \in \mathbb{R}^n$ is a global maximizer of $-J(\boldsymbol\theta)$ if it is a global minimizer of $J(\boldsymbol\theta)$.


## Problem 2:

(_From [Section 13.1](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html#a-first-look-at-likelihood-based-learning-objectives)_.) It was mentioned in class that the maximizers of a (nonnegatively-valued) function are the same as the minimizers of the logarithm of the function. In this problem, you will prove this statement.

Precisely, let $J:\mathbb{R}^n \to (0,\infty)$ be a function taking values in the interval $(0,\infty)$.

**(a)**: Prove that $\boldsymbol{\theta}^\star \in \mathbb{R}^n$ is a global minimizer of $J(\boldsymbol{\theta})$ if it is a global minimizer of $\log{J(\boldsymbol{\theta})}$. (_Hint_: The logarithm function is a strictly increasing function.)

**(b)**: Conversely, prove that $\boldsymbol{\theta}^\star \in \mathbb{R}^n$ is a global minimizer of $\log{J(\boldsymbol{\theta})}$ if it is a global minimizer of $J(\boldsymbol{\theta})$. (_Hint_: The exponential function is a strictly increasing function.)