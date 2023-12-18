# Suggested problems for [Section 11.3]()

## Problem 1 ([solution](./11-3-suggested-problems-sol.md#problem-1-problem-statement))

Prove that the data log-likelihood function

$$
\ell(\beta_0,\boldsymbol\beta) = \sum_{i=1}^m \left[ y^{(i)} \log{\phi^{(i)}} + \big( 1-y^{(i)}\big) \log{ \big( 1- \phi^{(i)} \big)}  \right]
$$

for a logistic regression model is concave, where

$$
\phi^{(i)} = \sigma \big(\beta_0 + \mathbf{x}^{(i)T} \boldsymbol\beta\big)
$$

for each $i=1,\ldots,m$, and $\sigma(z) = 1 / (1+e^{-z})$ is the sigmoid function.