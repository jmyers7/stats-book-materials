# Homework for [Section 9.2]()


## Problem 1

Let

$$
f: \mathbb{R}^n \to \mathbb{R}, \quad \mathbf{x} \mapsto f(\mathbf{x}),
$$

be a function whose second-order partial derivatives exist. Define the _Hessian matrix_ of $f$ to be the $n\times n$ square matrix

$$
\text{Hess}(f(\mathbf{x})) \stackrel{\text{def}}{=} \left[ \frac{\partial^2 f}{\partial x_i \partial x_j} (\mathbf{x}) \right].
$$

Provided that the second-order partial derivatives are all continuous, notice that the Hessian matrix is symmetric.

Suppose that $f$ is a polynomial of degree $2$, which means there is symmetric matrix $A\in \mathbb{R}^{n\times n}$, a vector $\mathbf{b}\in \mathbb{R}^n$, and a scalar $c\in \mathbb{R}$ such that

$$
f(\mathbf{x}) = \mathbf{x}^\intercal A \mathbf{x} + \mathbf{b}^\intercal \mathbf{x} + c
$$

for all $\mathbf{x} \in \mathbb{R}^n$.

(a): Prove that $\nabla f(\mathbf{x}) = 2A \mathbf{x} + \mathbf{b}$.

(b): Prove that $\text{Hess}(f(\mathbf{x})) = 2A$.

(c): Prove that

$$
f(\mathbf{x})  = f(\mathbf{x}_0) + (\mathbf{x}-\mathbf{x}_0)^\intercal \nabla f(\mathbf{x}_0) + \frac{1}{2} (\mathbf{x}-\mathbf{x}_0)^\intercal H (\mathbf{x}-\mathbf{x}_0)
$$

where $H = \text{Hess}(f(\mathbf{x}_0))$.

Notice that the right-hand side of this last equation is the degree-$2$ multivariable Taylor polynomial of $f$ centered at $\mathbf{x}_0$. Since $f$ is _assumed_ in this problem to be a degree-$2$ polynomial, this Taylor polynomial is _exactly_ equal to $f$. In the general case, however, we may only assume that $f$ is locally approximated by the Taylor polynomial:

$$
f(\mathbf{x}) \approx f(\mathbf{x}_0) + (\mathbf{x}-\mathbf{x}_0)^\intercal \nabla f(\mathbf{x}_0) + \frac{1}{2} (\mathbf{x}-\mathbf{x}_0)^\intercal H (\mathbf{x}-\mathbf{x}_0)
$$

for all $\mathbf{x}$ sufficiently near $\mathbf{x}_0$. In any case, if $\mathbf{x}_0$ is a *stationary point of $f$* so that $\nabla f(\mathbf{x}_0)=0$, then we have

$$
f(\mathbf{x}) \approx f(\mathbf{x}_0) + \frac{1}{2} (\mathbf{x}-\mathbf{x}_0)^\intercal H (\mathbf{x}-\mathbf{x}_0).
$$

Thus, the character of the stationary point may be investigated through properties of the Hessian matrix $H$ which, in turn, encodes the curvature of the graph of $f(\mathbf{x})$ near $\mathbf{x}_0$.

## Problem 2

To keep things simple, let's suppose that we have a real-valued function

$$
f: \mathbb{R}^2 \to \mathbb{R}, \quad (x,y) \mapsto f(x,y),
$$

defined on the plane. Suppose, as in Problem 1, that $f$ is a polynomial of degree $2$, so that

$$
f(\mathbf{v}) = \mathbf{v}^\intercal A \mathbf{v} + \mathbf{b}^\intercal \mathbf{v} + c
$$

where $\mathbf{v}^\intercal = (x,y)$, $A\in \mathbb{R}^{2\times 2}$ is a symmetric matrix, $\mathbf{b} \in \mathbb{R}^2$ and $c\in \mathbb{R}$. The goal in this problem is to prove that the _directional second derivatives_ of $f$ are determined by the Hessian matrix. Since second derivatives encode curvature (convexity and concavity), this will show that the Hessian is connected to curvature.

To do so, consider the unit vector in the plane with its tail at the origin making an angle of $\theta$ with the positive $x$-axis:

$$
\mathbf{u}_\theta = \begin{bmatrix} \cos{\theta} \\ \sin{\theta} \end{bmatrix}.
$$

With $\theta$ fixed, define the function

$$
g_\theta: \mathbb{R} \to \mathbb{R}, \quad g_\theta(r) = f(r\mathbf{u}_\theta) = f(r\cos{\theta},r\sin{\theta}).
$$

Notice that the graph of $g_\theta(r)$ is precisely the intersection of the graph of $f(x,y)$ (in $xyz$-space) with the vertical plane containing the $z$-axis and the line in the $xy$-plane determined by the vector $\mathbf{u}_\theta$. Thus, the second derivative $g_\theta''(0)$ may be naturally identified with the *directional second derivative of $f$ at $(0,0)$ in the direction of $\mathbf{u}_\theta$*.

(a): Prove that

$$
g''_\theta(0) = \mathbf{u}_\theta^\intercal H \mathbf{u}_\theta
$$

where $H = \text{Hess}(f(0,0))$.

(b): Since $H$ is symmetric, by the [Spectral Theorem](https://en.wikipedia.org/wiki/Spectral_theorem) the plane $\mathbb{R}^2$ has an orthonormal basis $\mathbf{e}_1,\mathbf{e}_2$ of eigenvectors of $H$ and the corresponding eigenvalues $\lambda_1,\lambda_2$ are real. Prove that a vector

$$
\mathbf{u} = \alpha \mathbf{e}_1 + \beta \mathbf{e}_2
$$

is a unit vector if and only if $\alpha^2 + \beta^2 = 1$.

(c): If $\mathbf{u} = \alpha \mathbf{e}_1 + \beta \mathbf{e}_2$ is a unit vector as in part (b), prove that the directional second derivative of $f$ at $(0,0)$ in the direction of $\mathbf{u}$ is given by

$$
D = \alpha^2 \lambda_1 + \beta^2 \lambda_2.
$$

Conclude that if both eigenvalues are positive, then the graph of $f$ at $(0,0)$ is convex (i.e., concave upward), while if both eigenvalues are negative, then the graph of $f$ at $(0,0)$ is concave (i.e., concave downward).

(d): Suppose that $|\lambda_2| \geq |\lambda_1|$. Prove that the magnitude of the directional second derivative $D$ in part (c) is maximized when $\mathbf{u} = \mathbf{e}_2$, and it is minimized when $\mathbf{u} = \mathbf{e}_1$.

Now, supposing $|\lambda_2| \geq |\lambda_1|$, the _condition number_ of $H$ is defined to be the ratio

$$
\kappa(H) \stackrel{\text{def}}{=} \frac{|\lambda_2|}{|\lambda_1|} \geq 1.
$$

Our arguments show that if the condition number $\kappa(H)$ is much bigger than $1$, say $\kappa(H) \approx 10^m$ for some $m\geq 1$, then the graph of $f(x,y)$ has $m$ times as much curvature in the direction of the eigenvector $\mathbf{e}_2$ compared to the curvature in the direction of $\mathbf{e}_1$.