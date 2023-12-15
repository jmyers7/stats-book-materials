**Solutions for suggested problems for Section [11.2](https://mml.johnmyersmath.com/stats-book/chapters/learning.html#maximum-likelihood-estimation-for-linear-regression-models).** ([Problems](./11-2-suggested-problems.md))

---

**Problem 1**: For simplicity, set $\mathbf{v} = \mathbf{v}(\mathbf{x})$. We first compute the $j$-th partial derivative:

$$
\frac{\partial}{\partial x_j} (\mathbf{v}^T \mathbf{v}) = \frac{\partial }{\partial x_j} \left( \sum_{k=1}^m v_k^2 \right) = 2 \sum_{k=1}^m v_k \frac{\partial v_k}{\partial x_j} = 2 \mathbf{v}^T J_{\ast, j},
$$

where $J_{\ast, j}$ denotes the $j$-th column of the Jacobian matrix. But then 

$$
\nabla\left(\mathbf{v}^T \mathbf{v} \right) = \begin{bmatrix}
\frac{\partial}{\partial x_1} (\mathbf{v}^T \mathbf{v}) & \cdots & \frac{\partial}{\partial x_n} (\mathbf{v}^T \mathbf{v}) 
\end{bmatrix} = 2 \begin{bmatrix} \mathbf{v}^TJ_{\ast,1} & \cdots & \mathbf{v}^T J_{\ast, n} \end{bmatrix} = 2 \mathbf{v}^T J(\mathbf{v}),
$$

as desired.

---

**Problem 2**: Since partial derivatives are additive, so too is the Hessian matrix, in the sense that

$$
H\left( \sum_{i=1}^m f^{(i)}(\mathbf{x}) \right) = \sum_{i=1}^m H\left(f^{(i)}(\mathbf{x})\right)
$$

for functions $f^{(1)},\ldots,f^{(m)}$. Thus, we have

$$
H(\text{NRSS}(\beta_0,\beta_1)) = \sum_{i=1}^m H\left( \text{NRSS}^{(i)}(\beta_0,\beta_1)\right),
$$

where

$$
\text{NRSS}^{(i)}(\beta_0,\beta_1) = - \left( y^{(i)} - \beta_0 - \beta_1 x^{(i)} \right)^2
$$

for each $i=1,\ldots,m$. But since a sum of negative semidefinite matrices is negative semidefinite (proof?), all of this means that we can prove our desired result by reducing to the case that $m=1$, so that our objective function looks like

$$
\text{NRSS}(\beta_0, \beta_1) = - \left( y - \beta_0 - \beta_1 x \right)^2
$$

where we've set $y = y^{(1)}$ and $x = x^{(1)}$ for simplicity. Then, it is easy to compute

$$
H\left( \text{NRSS}(\beta_0,\beta_1)\right) = \begin{bmatrix} -2 & -2x \\\ -2x & -2x^2 \end{bmatrix}.
$$

The eignevalues $\lambda$ of the Hessian matrix are the solutions to the characteristic equation

$$
(-2 - \lambda)(-2x^2 - \lambda ) - 4x^2 = 0.
$$

But the solutions are easily computed to be $\lambda =0$ and $\lambda = -2(1+x^2)$, both of which are nonpositive.
