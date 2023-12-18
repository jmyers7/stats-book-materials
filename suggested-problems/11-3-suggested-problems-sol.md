# Solutions for suggested problems for [Section 11.3]()

## Problem 1 ([problem statement](./11-3-suggested-problems.md#problem-1-solution))

Since the Hessian matrix is additive, we may assume that $m=1$, so that

$$
\ell(\boldsymbol\theta) = y\log{\phi} + (1-y) \log{(1-\phi)},
$$

where $y\in \{0,1\}$ and $\phi = \sigma(\mathbf{x}^T \boldsymbol\theta)$ for

$$
\mathbf{x}^T = \begin{bmatrix} 1 & x_1 & \cdots & x_n\end{bmatrix} \quad \text{and} \quad \boldsymbol\theta^T = \begin{bmatrix} \beta_0 & \beta_1 & \cdots & \beta_n \end{bmatrix}.
$$

In particular, note that $x_0=1$.

It is easy to prove that

$$
\frac{\text{d}\sigma}{\text{d}z}(z) = (1- \sigma(z))\sigma(z).
$$

Using this identity, we compute

$$
\frac{\partial \ell}{\partial \beta_i} = yx_i - \phi x_i
$$

for each $i=0,1,\ldots,n$, and then

$$
\frac{\partial^2 \ell}{\partial x_i \partial x_j} = - (1-\phi)\phi x_i x_j
$$

for $0 \leq i , j \leq n$. Thus,

$$
\text{Hess}(\ell(\boldsymbol\theta)) = -(1-\phi)\phi \left[ x_i x_j \right]_{ij}.
$$

But it is easy to see that

$$
\mathbf{z}^T [x_ix_j]_{ij} \mathbf{z} = \sum_{i=0}^n \sum_{j=0}^n x_ix_j z_iz_j = (\mathbf{x}^T \mathbf{z})^2
$$

for all vectors

$$
\mathbf{z}^T = \begin{bmatrix} z_0 & z_1 & \cdots & z_n \end{bmatrix},
$$

and so

$$
\mathbf{z}^T \text{Hess}(\ell(\boldsymbol\theta)) \mathbf{z} = -(1-\phi)\phi (\mathbf{x}^T \mathbf{z}) \leq 0
$$

since $0 \leq \phi \leq 1$. Thus, the Hessian matrix of $\ell(\boldsymbol\theta)$ is negative semidefinite, which proves $\ell(\boldsymbol\theta)$ is concave.