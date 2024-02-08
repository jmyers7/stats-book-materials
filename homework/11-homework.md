# Homework for [Chapter 11: Optimization](https://mml.johnmyersmath.com/stats-book/chapters/11-optim.html)

**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. [Section 11.1: Finding saddle points](#problem-1-finding-saddle-points)
2. [Section 11.2: Derivatives of quadratic functions](#problem-2-derivatives-of-quadratic-functions)
3. [Section 11.2: Practice with multi-variable calculus](#problem-3-practice-with-multi-variable-calculus)
4. [Section 11.3: Rate of convergence of gradient descent](#problem-4-rate-of-convergence-of-gradient-descent)
5. [Section 11.4: Convergence of batch gradient descent](#problem-5-convergence-of-batch-gradient-descent)

 **Tips (to maximize your grade)**:
 
1. Show all relevant steps in all computations. However, I do not need to see trivial things like, for example, the intermediate steps in computing an integral. But if there is a key step in a set of computations that you skip over, I'll have to remove a point or two. Use your best judgment.

2. Explain your work and reasoning using complete and grammatically correct sentences. (It is a myth that mathematicians, engineers, and scientists are all bad at writing. We do many goodly words!)
 
3. Use correct notation.

4. Your goal is to demonstrate your depth of understanding, not simply that you obtained the correct answer. Your goal is to _explain_, as if you're trying to teach me the material.

5. Figure out the answer before writing! More precisely: Carry through your initial computations on your own scratch paper before writing your solutions.  It is difficult to follow a solution that is written in a "stream-of-consciousness" style. If I can't follow along, I am likely to give up and take off points (even if your final answer is right).

## Problem 1: Finding saddle points

(_From [Section 11.1](https://mml.johnmyersmath.com/stats-book/chapters/11-optim.html#gradient-descent-in-one-variable)_.) Consider the objective function

$$
J:\mathbb{R} \to \mathbb{R}, \quad J(\theta) = \theta^3.
$$

**(a)**: Write the update rule (in the form of a recurrence relation) for the gradient descent algorithm with learning rate $\alpha$ and decay rate $\beta$.

**(b)**: Beginning from $\theta_0=1$ and with decay rate $\beta=0$, there is one (and only one) value of the learning rate $\alpha$ such that the algorithm finds the saddle point $\theta^\star = 0$ in _two_ gradient steps. Find this $\alpha$.


## Problem 2: Derivatives of quadratic functions

(_From [Section 11.2](https://mml.johnmyersmath.com/stats-book/chapters/11-optim.html#curvature-and-derivatives-in-higher-dimensions)_.) Consider the following matrix, vector, and scalar:

$$
\mathbf{A} = \begin{bmatrix}
\alpha & \beta \\\ \beta & \gamma \end{bmatrix}\in \mathbb{R}^{2\times 2}, \quad \mathbf{b} = \begin{bmatrix} \delta \\\ \epsilon \end{bmatrix} \in \mathbb{R}^2, \quad c\in \mathbb{R}.
$$

Using these, define the function

$$
J:\mathbb{R}^2 \to \mathbb{R}, \quad J(\boldsymbol{\theta}) = \boldsymbol{\theta}^\intercal \mathbf{A} \boldsymbol{\theta} + \mathbf{b}^\intercal \boldsymbol{\theta} + c.
$$

**(a)**: Compute the gradient vector $\nabla J(\boldsymbol{\theta})$ in terms of $\mathbf{A}$, $\boldsymbol{\theta}$, and $\mathbf{b}$. (Suppose that $\boldsymbol{\theta}^\intercal = (\theta_1,\theta_2)$.)

**(b)**: Compute the Hessian matrix $\nabla^2 J(\boldsymbol{\theta})$ in terms of $\mathbf{A}$. (Again suppose that $\boldsymbol{\theta}^\intercal = (\theta_1,\theta_2)$.)

**(c)**: How do you expect your formulas in (a) and (b) to generalize to $\mathbf{A}\in \mathbb{R}^{d\times d}$ and $\mathbf{b} \in \mathbb{R}^d$ for arbitrary $d$?

(_Hint_: Notice that $J$ is the $2$-dimensional analog of the single-variable polynomial $J(\theta) = a\theta^2 + b\theta + c$. The formulas you will derive in (a) and (b) are the natural extensions of the equations $J'(\theta) =2a\theta + b$ and $J''(\theta) = 2a$.)


## Problem 3: Practice with multi-variable calculus

(_From [Section 11.2](https://mml.johnmyersmath.com/stats-book/chapters/11-optim.html#curvature-and-derivatives-in-higher-dimensions)_.) Consider the objective function

$$
J:\mathbb{R}^2 \to \mathbb{R}, \quad J(\boldsymbol{\theta}) = 2\theta_1^2 +2\theta_1\theta_2 + 3 \theta_2^2 -12\theta_1 -16\theta_2 +28.
$$

**(a)**: Find a matrix $\mathbf{A} \in \mathbb{R}^{2\times 2}$, a vector $\mathbf{b} \in \mathbb{R}^2$, and a scalar $c\in \mathbb{R}$ such that

$$
J(\boldsymbol{\theta}) = \boldsymbol{\theta}^\intercal \mathbf{A} \boldsymbol{\theta} + \mathbf{b}^\intercal \boldsymbol{\theta} + c.
$$

**(b)**: Compute the gradient vector $\nabla J(\boldsymbol{\theta})$ and the Hessian matrix $\nabla^2 J(\boldsymbol{\theta})$. (_Hint_: Use part (a) and the previous problem.)

**(c)**: Compute the directional derivatives $J^\prime_{\mathbf{v}}(2,2)$ and $J''_{\mathbf{v}}(2,2)$, where $\mathbf{v}^\intercal = (1,1)$.

**(d)**: Find the direction of minimum rate of change at the point $\boldsymbol{\theta} = (3,4)$. What is the rate of change in this direction?

**(e)**: Find and classify all extremizers of $J$ using the Second Derivative Test.

**(f)**: Find the directions of extreme curvature at the point $\boldsymbol{\theta}^\intercal =(3,4)$. What are the curvatures in these directions?

**(g)**: Compute the spectral radius $\rho\left(\nabla^2 J(3,4)\right)$ and the condition number $\kappa\left(\nabla^2 J(3,4)\right)$.

## Problem 4: Rate of convergence of gradient descent

(_From [Section 11.3](https://mml.johnmyersmath.com/stats-book/chapters/11-optim.html#gradient-descent-in-multiple-variables)_.) Consider again the polynomial objective function $J$ from Problem 3:

$$
J:\mathbb{R}^2 \to \mathbb{R}, \quad J(\boldsymbol{\theta}) = 2\theta_1^2 +2\theta_1\theta_2 + 3 \theta_2^2 -12\theta_1 -16\theta_2 +28.
$$

Beginning from _any_ initial guess $\boldsymbol{\theta}_0$, find the largest value of the learning rate $\alpha$ that will guarantee exponentially fast convergence to the global minimizer $\boldsymbol{\theta}^\star$ identified in part (e) of Problem 3. (Assume the decay rate is $\beta=0$.)

## Problem 5: Convergence of batch gradient descent

(_From [Section 11.4](https://mml.johnmyersmath.com/stats-book/chapters/11-optim.html#stochastic-gradient-descent)_.) Consider the stochastic objective function

$$
J: \mathbb{R}^2 \to \mathbb{R}, \quad J(\boldsymbol{\theta}) = \frac{1}{m} \sum_{i=1}^m \left[\frac{3}{2}(x_{i1}-\theta_1)^2 + \frac{3}{2}(x_{i2} - \theta_2)^2 \right],
$$

where $\mathbf{x}_1,\mathbf{x}_2,\ldots,\mathbf{x}_m\in \mathbb{R}^2$ is an observed dataset. Identify values of the learning rate $\alpha$ that guarantee convergence of the batch gradient descent algorithm applied to $J$. Of course, this will require that you identify _what_ the algorithm converges _to_. (Assume the decay rate is $\beta=0$.)
