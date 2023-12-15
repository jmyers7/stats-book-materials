**Suggested problems for Section [11.2](https://mml.johnmyersmath.com/stats-book/chapters/learning.html#maximum-likelihood-estimation-for-linear-regression-models).** ([Solutions](./11-2-suggested-problems-sol.md))

---

**Problem 1**: Let

$$
\mathbf{v}:\mathbb{R}^n \to \mathbb{R}^m, \quad \mathbf{v}(\mathbf{x}) = (v_1(\mathbf{x}),\ldots,v_m(\mathbf{x}))
$$

be a differentiable vector-valued function. Define the _Jacobian matrix_ of $\mathbf{v}$ to be the $m\times n$ matrix of first-order partial derivatives:

$$
J(\mathbf{v}(\mathbf{x})) \stackrel{\text{def}}{=} \left[\frac{\partial v_i}{\partial x_j} \right].
$$

From $\mathbf{v}$, we define the real-valued function

$$
\mathbb{R}^n \to \mathbb{R}, \quad \mathbf{x} \mapsto \mathbf{v}(\mathbf{x})^T \mathbf{v}(\mathbf{x}).
$$

Prove that the gradient of this latter function is given by the following vector-matrix product:

$$
\nabla \left(\mathbf{v}(\mathbf{x})^T \mathbf{v}(\mathbf{x}) \right) = 2 \mathbf{v}(\mathbf{x})^T J(\mathbf{v}(\mathbf{x})).
$$

---

**Problem 2**: Let

$$
f: \mathbb{R}^n \to \mathbb{R}
$$

be a function. While [concavity](https://en.wikipedia.org/wiki/Concave_function) of $f$ is defined without reference to calculus, the concavity of $f$ may be measured using the _Hessian matrix_ of $f$ consisting of all second-order partial derivatives:

$$
H(f(\mathbf{x})) \stackrel{\text{def}}{=} \left[ \frac{\partial^2 f}{\partial x_i \partial x_j} \right].
$$

Indeed:

> **Theorem 1**. Provided that the second-order partial derivatives of $f$ are all continuous (so that the Hessian matrix is symmetric), $f$ is concave if and only if the Hessian matrix is _negative semidefinite_, which means that $\mathbf{z}^T H(f(\mathbf{x})) \mathbf{z} \leq 0$ for all column vectors $\mathbf{z}\in \mathbb{R}^{1\times n}$.

This criterion is the natural generalization to multiple variables of the familiar fact from single-variable calculus that a function is concave if and only if its second derivative is negative.

However, since the Hessian is symmetric, the [spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem) applies, and can be used to show the following:

> **Theorem 2**. Provided that the second-order partial derivatives of $f$ are all continuous, $f$ is concave if and only if all eigenvalues of the Hessian matrix are non-positive.

Using Theorem 2, prove that the negative residual sum of squares function 

$$
\text{NRSS}: \mathbb{R}^2 \to \mathbb{R}, \quad \text{NRSS}(\beta_0,\beta_1) = - \sum_{i=1}^m \left( y^{(i)} - \beta_0 - \beta_1 x^{(i)}  \right)^2
$$

associated with a simple linear regression model is concave.
