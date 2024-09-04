# Homework for [Chapter 12: Learning](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html)

**Due date**: TBD

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. [Section 12.1: Negative logarithms and optimization](#problem-1-negative-logarithms-and-optimization)
2. [Section 12.1: MLEs for the univariate Bernoulli model](#problem-2-mles-for-the-univariate-bernoulli-model)
3. [Section 12.2: Gaussian mixture models](#problem-3-gaussian-mixture-models)
4. [Section 12.3: MLEs for linear regression models](#problem-4-mles-for-linear-regression-models)
5. [Section 12.5: Counting neural network stuff](#problem-5-counting-neural-network-stuff)
6. [Section 12.5: Assessing goodness-of-fit of a neural network](#problem-6-assessing-goodness-of-fit-of-a-neural-network)

 **Tips (to maximize your grade)**:
 
1. Show all relevant steps in all computations. However, I do not need to see trivial things like, for example, the intermediate steps in computing an integral. But if there is a key step in a set of computations that you skip over, I'll have to remove a point or two. Use your best judgment.

2. Explain your work and reasoning using complete and grammatically correct sentences. (It is a myth that mathematicians, engineers, and scientists are all bad at writing. We do many goodly words!)
 
3. Use correct notation.

4. Your goal is to demonstrate your depth of understanding, not simply that you obtained the correct answer. Your goal is to _explain_, as if you're trying to teach me the material.

5. Figure out the answer before writing! More precisely: Carry through your initial computations on your own scratch paper before writing your solutions.  It is difficult to follow a solution that is written in a "stream-of-consciousness" style. If I can't follow along, I am likely to give up and take off points (even if your final answer is right).


## Problem 1: Negative logarithms and optimization

(_From [Section 12.1](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#a-first-look-at-likelihood-based-learning-objectives)_.) It was mentioned in class that the maximizers of a (nonnegatively-valued) function are the same as the minimizers of the negative logarithm of the function. In this problem, you will prove this statement.

Precisely, let $J:\mathbb{R}^n \to (0,\infty)$ be an objective function taking values in the interval $(0,\infty)$.

**(a)**: Prove that $\boldsymbol{\theta}^\star \in \mathbb{R}^n$ is a global maximizer of $J(\boldsymbol{\theta})$ if it is a global minimizer of $-\log{J(\boldsymbol{\theta})}$. (_Hint_: The negative logarithm function is a _strictly decreasing function_. What's the definition of a _strictly decreasing function_? Look it up! Also, do **not** assume any form of differentiability!)

**(b)**: Conversely, prove that $\boldsymbol{\theta}^\star \in \mathbb{R}^n$ is a global minimizer of $-\log{J(\boldsymbol{\theta})}$ if it is a global maximizer of $J(\boldsymbol{\theta})$.

## Problem 2: MLEs for the univariate Bernoulli model

(_From [Section 12.1](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#a-first-look-at-likelihood-based-learning-objectives)_.) Suppose we choose to model an observed dataset

$$
x_1,x_2,\ldots,x_{11} = 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0
$$

with our simple Bernoulli PGM with parameter $\theta$. In all parts below that require computations, round your final answer to four decimal places.

**(a)**: Plot the data surprisal function $\mathcal{I}(\theta;x_1,\ldots,x_{11})$.

**(b)**: Compute the maximum likelihood estimate $\theta^\star_\text{MLE}$ for $\theta$.

**(c)**: Compute the data surprisal $\mathcal{I}(\theta^\star_\text{MLE};x_1,\ldots,x_{11})$ corresponding to the MLE.

**(d)**: Compute the data likelihood $\mathcal{L}(\theta^\star_\text{MLE};x_1,\ldots,x_{11})$ corresponding to the MLE.

**(e)**: If $P_\theta$ is the model distribution of the Bernoulli model and $\hat{P}$ is the empirical distribution of the dataset, compute the cross entropy $H_{\hat{P}}(P_{\theta^\star_\text{MLE}})$.

**(f)**: Compute the KL divergence $D(\hat{P} \parallel P_{\theta^\star_\text{MLE}})$.

## Problem 3: Gaussian mixture models

(_From [Section 12.2](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#general-mle)_.) A _Gaussian mixture model_ (or _GMM_) is a probabilistic graphical model with underlying graph of the form

&nbsp;
<p align="center">
<img src="https://raw.githubusercontent.com/jmyers7/stats-book-materials/main/img/gmm.svg" width="300" align="center">
</p>
&nbsp;

The parameters are given by a number $\theta\in [0,1]$ that parametrizes $Z \sim Ber(\theta)$, as well as real parameters $\mu_0$ and $\mu_1$, and positive real parameters $\sigma_0^2$ and $\sigma_1^2$. The link function at $X$ is given by

$$
X \mid Z \sim N(\mu,\sigma^2),
$$

where

$$
\mu = (1-z)\mu_0 + z \mu_1 \quad \text{and} \quad \sigma^2 = (1-z)\sigma_0^2 + z \sigma_1^2.
$$

**(a)**: Assuming that GMMs are trained as **generative** models, write down a formula for the model likelihood function $\mathcal{L}_\text{model}(\theta,\mu_0,\mu_1,\sigma_0^2,\sigma_1^2)$. For simplicity, your formula should contain $\mu$ and $\sigma^2$ rather than the parameters $\mu_0$, $\mu_1$, $\sigma_0^2$, and $\sigma_1^2$ themselves.

**(b)**: Using your answer from part (a), write down a formula for the model surprisal function $\mathcal{I}_\text{model}(\theta,\mu_0,\mu_1,\sigma_0^2,\sigma_1^2)$. For simplicity, your formula should contain $\mu$ and $\sigma^2$ rather than the parameters $\mu_0$, $\mu_1$, $\sigma_0^2$, and $\sigma_1^2$ themselves.

**(c)**: Discuss the difficulties that would be encountered in maximum likelihood estimation for the parameters in a GMM.

## Problem 4: MLEs for linear regression models

(_From [Section 12.3](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#mle-for-linear-regression)_.) Consider the dataset

$$
\begin{array}{r|r|r}
x_1 & x_2 & y \\\ \hline
2 & 3 & 0 \\\
0 & 4 & 1 \\\
2 & 6 & -3 \\\
-1 & -2 & 5
\end{array}
$$

in $\mathbb{R}^3$, with predictor vectors $\mathbf{x}^\intercal= (x_1,x_2) \in \mathbb{R}^2$ and response variables $y\in \mathbb{R}$. In both parts below, round your answers to four decimal places. And please do not carry out the computations with something silly like a handheld calculator. A few lines of basic NumPy code is enough to get this problem done in a jiffy.

**(a)**: Using the formula in [this](https://mml.johnmyersmath.com/stats-book/chapters/13-learning.html#mle-lin-reg-thm) theorem, compute the MLEs for the parameters $\beta_0$ and $\boldsymbol{\beta} = (\beta_1,\beta_2)$ of a linear regression model with known variance.

**(c)**: Just to make sure you aren't cheating by using a Python library that computes MLEs for you, give me your matrix $(\mathcal{X}^\intercal \mathcal{X})^{-1}$ used in the formula in part (a). Round all nine entries in this matrix to four decimal places.

**(b)**: With respect to the parameters you found in part (a), compute the mean squared error of the model on the given dataset.

## Problem 5: Counting neural network stuff

(_From [Section 12.5](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#mle-for-neural-networks)_.) Suppose that we have a neural network with _four_ hidden layers of widths $16$, $32$, $8$, and $4$, and an input layer of width $4$. We run SGD on this network over $N=20$ epochs over a dataset of size $m=3{,}000$ with a mini-batch size of $k=320$.

**(a)**: What is the number of mini-batches per epoch? What are the sizes of the mini-batches?

**(b)**: What is the number of gradient steps per epoch?

**(c)**: How many total gradient steps are taken over the whole training run?

**(d)**: How many trainable parameters does the network contain?

## Problem 6: Assessing goodness-of-fit of a neural network

(_From [Section 12.5](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#mle-for-neural-networks)_.) The confusion matrix for the neural network classifier trained in [the book](https://mml.johnmyersmath.com/stats-book/chapters/12-learning.html#mle-for-neural-networks) is given by

$$
\begin{array}{c|cc}
& \hat{y}=0 & \hat{y}=1 \\\ \hline
y = 0 & 1529 & 7  \\\
y = 1 & 6 & 1530
\end{array}
$$

For all parts below, round your answers to four decimal places.

**(a)**: Compute the _accuracy_ of the classifier.

**(b)**: Compute the _precision_ of the classifier.

**(c)**: Compute the _recall_ of the classifier.