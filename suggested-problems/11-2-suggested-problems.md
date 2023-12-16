# Suggested problems for [Section 11.2](https://mml.johnmyersmath.com/stats-book/chapters/learning.html#maximum-likelihood-estimation-for-linear-regression-models)


## Problem 1 ([solution](./11-2-suggested-problems-sol.md#problem-1-problem-statement))

Let

$$
\mathbf{v}:\mathbb{R}^n \to \mathbb{R}^m, \quad \mathbf{v}(\mathbf{x}) = (v_1(\mathbf{x}),\ldots,v_m(\mathbf{x}))
$$

be a differentiable vector-valued function. Define the _Jacobian matrix_ of $\mathbf{v}$ to be the $m\times n$ matrix of first-order partial derivatives:

$$
\text{Jac}(\mathbf{v}(\mathbf{x})) \stackrel{\text{def}}{=} \left[\frac{\partial v_i}{\partial x_j} \right].
$$

From $\mathbf{v}$, we define the real-valued function

$$
\mathbb{R}^n \to \mathbb{R}, \quad \mathbf{x} \mapsto \mathbf{v}(\mathbf{x})^T \mathbf{v}(\mathbf{x}).
$$

Prove that the gradient of this latter function is given by the following vector-matrix product:

$$
\nabla \left(\mathbf{v}(\mathbf{x})^T \mathbf{v}(\mathbf{x}) \right) = 2 \mathbf{v}(\mathbf{x})^T \text{Jac}(\mathbf{v}(\mathbf{x})).
$$

## Problem 2 ([solution](./11-2-suggested-problems-sol.md#problem-2-problem-statement))

Let

$$
f: \mathbb{R}^n \to \mathbb{R}
$$

be a function. While [concavity](https://en.wikipedia.org/wiki/Concave_function) of $f$ is defined without reference to calculus, the concavity of $f$ may be measured using the _Hessian matrix_ of $f$ consisting of all second-order partial derivatives:

$$
\text{Hess}(f(\mathbf{x})) \stackrel{\text{def}}{=} \left[ \frac{\partial^2 f}{\partial x_i \partial x_j} \right].
$$

Indeed:

> **Theorem**. Provided that the second-order partial derivatives of $f$ are all continuous (so that the Hessian matrix is symmetric), $f$ is concave if and only if the Hessian matrix is _negative semidefinite_, which means that $\mathbf{z}^T \text{Hess}(f(\mathbf{x})) \mathbf{z} \leq 0$ for all column vectors $\mathbf{x},\mathbf{z}\in \mathbb{R}^{1\times n}$.

This criterion is the natural generalization to multiple variables of the familiar fact from single-variable calculus that a function is concave if and only if its second derivative is negative.

Using this theorem, prove that the objective function

$$
J(\boldsymbol\theta) = - \frac{1}{2}\left( \mathbf{y} - \mathcal{X}\boldsymbol\theta\right)^T \left( \mathbf{y} - \mathcal{X}\boldsymbol\theta\right)
$$

associated with a linear regression model is concave.

## Problem 3

In the book and during lecture, we assumed that the variance $\sigma^2$ in our linear regression model was known. However, in this problem, you will assume that $\sigma^2$ is unknown and must be learned from data. By taking the partial derivative of the data log-likelihood function with respect to $\sigma^2$ and setting it to $0$, prove that the MLE for the variance is given by the formula

$$
\sigma^2 = \frac{1}{m} \sum_{i=1}^m \left( y^{(i)} - \mu^{(i)}\right)^2
$$

where, as always, we have $\mu^{(i)} = \mathbf{x}^{(i)} \boldsymbol\beta + \beta_0$ for each $i=1,\ldots,m$.
