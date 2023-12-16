# Solutions for suggested problems for [Section 11.2](https://mml.johnmyersmath.com/stats-book/chapters/learning.html#maximum-likelihood-estimation-for-linear-regression-models)

## Problem 1 ([problem statement](./11-2-suggested-problems.md#problem-1-solution))

For simplicity, set $\mathbf{v} = \mathbf{v}(\mathbf{x})$. We first compute the $j$-th partial derivative:

$$
\frac{\partial}{\partial x_j} (\mathbf{v}^T \mathbf{v}) = \frac{\partial }{\partial x_j} \left( \sum_{k=1}^m v_k^2 \right) = 2 \sum_{k=1}^m v_k \frac{\partial v_k}{\partial x_j} = 2 \mathbf{v}^T J_{\ast, j},
$$

where $J_{\ast, j}$ denotes the $j$-th column of the Jacobian matrix. But then 

$$
\nabla\left(\mathbf{v}^T \mathbf{v} \right) = \begin{bmatrix}
\frac{\partial}{\partial x_1} (\mathbf{v}^T \mathbf{v}) & \cdots & \frac{\partial}{\partial x_n} (\mathbf{v}^T \mathbf{v}) 
\end{bmatrix} = 2 \begin{bmatrix} \mathbf{v}^TJ_{\ast,1} & \cdots & \mathbf{v}^T J_{\ast, n} \end{bmatrix} = 2 \mathbf{v}^T \text{Jac}(\mathbf{v}),
$$

as desired.

## Problem 2 ([problem statement](./11-2-suggested-problems.md#problem-2-solution))

(a): The assumption that

$$
\nabla f(\mathbf{x}) = c \mathbf{x}^T A + \mathbf{b}
$$

may be rewritten in vector notation as

$$
\nabla f(\mathbf{x}) = \left[ \sum_{k=1}^n cx_k a_{kj} + b_j \right]_j.
$$

Thus

$$
\frac{\partial f}{\partial x_j} = \sum_{k=1}^n cx_k a_{kj} + b_j,
$$

and so

$$
\frac{\partial^2 f}{\partial x_i\partial x_j} = ca_{ij}.
$$

This implies

$$
\text{Hess}(f(\mathbf{x})) = \left[ c a_{ij} \right]_{ij} = c A,
$$

as desired.


(b): From lecture, we have

$$
\nabla J (\boldsymbol\theta) = (\mathbf{y} - \mathcal{X} \boldsymbol\theta)^T \mathcal{X} = - \boldsymbol\theta^T \mathcal{X}^T \mathcal{X} + \mathbf{y}^T \mathcal{X}.
$$

But it then follows immediately from part (a) of this problem that

$$
\text{Hess}(J(\boldsymbol\theta)) = -\mathcal{X}^T \mathcal{X}
$$

for all $\boldsymbol\theta$. Then, given $\mathbf{z} \in \mathbb{R}^{1\times (n+1)}$, we have

$$
\mathbf{z}^T \text{Hess}(J(\boldsymbol\theta))\mathbf{z} = -\mathbf{z}^T \mathcal{X}^T \mathcal{X} \mathbf{z} = -(\mathcal{X}\mathbf{z})^T \mathcal{X}\mathcal{z} = - \left \lVert \mathcal{X}\mathbf{z} \right \rVert \leq 0,
$$

where the double vertical bars denote the standard Euclidean norm.