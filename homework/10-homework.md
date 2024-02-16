# Homework for [Chapter 10: Information theory](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html)

**Due date**: Monday, February 19

**Guidelines:** You are free to work and collaborate with your classmates, but you must turn in your own written solutions. Do not consult any outside resources for your solutions, including anything on the web. Late submissions will not be accepted.

**List of problems:**

1. [Section 10.1: Practice with surprisal and entropy](#problem-1-practice-with-surprisals-and-entropies)
2. [Section 10.1: Entropy in different bases](#problem-2-entropy-in-different-bases)
3. [Section 10.1: Independence and entropy](#problem-3-independence-and-entropy)
4. [Section 10.1: Uncertain draws](#problem-4-uncertain-draws)
5. [Section 10.1: Differential entropy](#problem-5-differential-entropy)
6. [Section 10.2: Practice with KL divergence](#problem-6-practice-with-kl-divergence)
7. [Section 10.2: Differential KL divergence](#problem-7-differential-kl-divergence)
8. [Section 10.3: Practice with "flows" of information](#problem-8-practice-with-flows-of-information)
9. [Section 10.3: The data processing inequality](#problem-9-the-data-processing-inequality)

 **Tips (to maximize your grade)**:
 
1. Show all relevant steps in all computations. However, I do not need to see trivial things like, for example, the intermediate steps in computing an integral. But if there is a key step in a set of computations that you skip over, I'll have to remove a point or two. Use your best judgment.

2. Explain your work and reasoning using complete and grammatically correct sentences. (It is a myth that mathematicians, engineers, and scientists are all bad at writing. We do many goodly words!)
 
3. Use correct notation.

4. Your goal is to demonstrate your depth of understanding, not simply that you obtained the correct answer. Your goal is to _explain_, as if you're trying to teach me the material.

5. Figure out the answer before writing! More precisely: Carry through your initial computations on your own scratch paper before writing your solutions.  It is difficult to follow a solution that is written in a "stream-of-consciousness" style. If I can't follow along, I am likely to give up and take off points (even if your final answer is right).

## Problem 1: Practice with surprisals and entropies

(_From [Section 10.1](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#shannon-information-and-entropy)_.) Let $P$ be a probability measure defined on $S = \\{1,2,3,4\\}$ with mass function

$$
\begin{array}{c|c}
s & p(s) \\\ \hline
1 & 0.4 \\\
2 & 0.05 \\\
3 & 0.15 \\\
4 & 0.4
\end{array}
$$

Compute the surprisal $I(s)$ of each sample point and the entropy $H(P)$.

## Problem 2: Entropy in different bases

(_From [Section 10.1](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#shannon-information-and-entropy)_.) Let $P$ be a probability measure on a finite sample space with mass function $p(s)$. The entropy $H(P)$ was defined in class using the base $e$ logarithm:

$$
H(P) = - \sum_{s\in S} p(s) \log(p(s)).
$$

However, suppose that we defined a new entropy, denoted $H_2(P)$, using the base $2$ logarithm:

$$
H_2(P) = - \sum_{s\in S} p(s) \log_2(p(s)).
$$

Then these two entropies are proportional, which means there is a constant $k$ (not depending on $P$) such that

$$
H_2(P) = k\cdot H(P).
$$

Find the constant $k$.

## Problem 3: Independence and entropy

(_From [Section 10.1](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#shannon-information-and-entropy)_.) Let $X$ and $Y$ be **independent** random variables with finite ranges and mass functions $p(x)$ and $p(y)$. Prove that

$$
H(X,Y) = H(X) + H(Y).
$$

## Problem 4: Uncertain draws

(_From [Section 10.1](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#shannon-information-and-entropy)_.) I have two urns, both containing 100 balls.

* Urn #1 contains: 20 red balls, 62 white balls, and 18 blue balls.
* Urn #2 contains: 35 red balls, 28 white balls, and 37 blue balls.

Suppose I draw a ball at random from both urns and record the color of each ball. Let $P_1$ be the probability distribution over the colors for Urn #1, and $P_2$ the probability distribution over the colors for Urn #2.

**(a)**: For which urn is the color of the randomly drawn ball _more_ uncertain? (Your intuition certainly suggests the answer, but you must carefully and rigorously justify your answer for full credit.)

**(b)**: Compute the cross entropy $H_{P_1}(P_2)$.

## Problem 5: Differential entropy

(_From [Section 10.1](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#shannon-information-and-entropy)_.) We only defined entropy for random variables with finite ranges. However, by replacing sums with integrals and mass functions with density functions in the usual way, we may define entropy for continuous random variables as follows:

$$
H(X) \stackrel{\text{def}}{=} -\int_\mathbb{R} f(x) \log(f(x)) \ \text{d}x,
$$

where $f(x)$ is the density of $X$. This is called the _differential entropy_ of $X$.

Suppose that $X$ is a continuous random variable with density function

$$
f(x) = \begin{cases}
2x & : 0 \leq x \leq 1, \\
0 & : \text{otherwise}.
\end{cases}
$$

Compute the differential entropy of $X$. (You might be surprised by the answer.)

## Problem 6: Practice with KL divergence

(_From [Section 10.2](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#kullback-leibler-divergence)_.) Let $P$ and $Q$ be two probability measures defined on $S = \\{1,2,3,4\\}$ with mass functions

$$
\begin{array}{c|cc}
s & p(s) & q(s) \\\ \hline
1 & 0.4 & 0.5 \\\
2 & 0.05 & 0.35 \\\
3 & 0.15 & 0.05 \\\
4 & 0.4 & 0.55
\end{array}
$$

Compute the KL divergences $D(P \parallel Q)$ and $D(Q \parallel P)$.

## Problem 7: Differential KL divergence

(_From [Section 10.2](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#kullback-leibler-divergence)_.) We only defined KL divergence for random variables with finite ranges. However, by replacing sums with integrals and mass functions with density functions in the usual way, we may define KL divergence for continuous random variables as follows:

$$
D(Y \parallel X) = \int_\mathbb{R} f(y) \log \left( \frac{f(y)}{f(x)} \right) \ \text{d}x,
$$

where $f(x)$ and $f(y)$ are the densities of $X$ and $Y$, respectively. This is called the _differential KL divergence_ from $Y$ to $X$.

**(a)**: Consider the family of all exponential distributions with densities

$$
f(x;\lambda) = \begin{cases}
\lambda e^{-\lambda x} & : x>0, \\
0 &: \text{otherwise},
\end{cases}
$$

parametrized by real numbers $\lambda>0$. Let $X_\lambda \sim \mathcal{E}xp(\lambda)$ and $X_\theta \sim \mathcal{E}xp(\theta)$. Show that the KL divergence is given by the formula

$$
D(X_\lambda \parallel X_\theta) = \frac{\theta}{\lambda} - \log(\theta) + \log{\lambda} - 1.
$$

**(b)**: Using the expression from part (a), plot the KL divergence $D(X_\lambda \parallel X_\theta)$ as a function of $\theta$ (with $\lambda$ held fixed). Label the global minimum of the divergence. (The value and location of the minimum should _not_ be surprising.)

**(c)**: Compute the curvature of the graph in part (b) at the global minimum. (_Hint_: For us, the curvature of the graph of a twice-differentiable function $y=f(x)$ at a point $x=x_0$ is the second derivative $f''(x_0)$.)

**(d)**: Unsurprisingly, the _surprisal_ of an outcome $x$ drawn from $X_\theta \sim \mathcal{E}xp(\theta)$ is given by the formula

$$
I(x;\theta) \stackrel{\text{def}}{=} -\log(f(x;\theta)).
$$

Compute the second-order partial derivative

$$
\frac{\partial^2}{\partial \theta^2}\left( I(x;\theta) \right)
$$

and evaluate it at $\theta = \lambda$. Do you notice a similarity to your answer in (c)?

(This question will take on more significance when we learn about _Fisher information_ in [Chapter 14](https://mml.johnmyersmath.com/stats-book/chapters/14-stats-estimators.html).)

## Problem 8: Practice with "flows" of information

(_From [Section 10.3](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#flow-of-information)_.) Suppose that $X$ and $Y$ are Bernoulli random variables with $X\sim Ber(0.5)$, and that the communication channel from $X$ to $Y$ has transition matrix

$$
\begin{array}{c|cc}
p(y|x) & y=0 & y=1 \\\ \hline
x = 0 & 0.75 & 0.25 \\\
x = 1 & 0.6 & 0.4
\end{array}
$$

**(a)**: Compute the mutual information $I(X,Y)$.

**(b)**: Use Bayes' theorem to "reverse the flow" of the communication channel, i.e., compute the transition matrix

$$
\begin{array}{c|cc}
p(x|y) & x=0 & x=1 \\\ \hline
y = 0 & ? & ? \\\
y = 1 & ? & ?
\end{array}
$$

of the Markov kernel in the opposite direction.

## Problem 9: The data processing inequality

(_From [Section 10.3](https://mml.johnmyersmath.com/stats-book/chapters/10-info-theory.html#flow-of-information)_.) Consider the disease/test/vacation probabilistic model described in class of the form:

&nbsp;
<p align="center">
  <img src="../img/markov.svg" width="30%">
</p>
&nbsp;

Suppose that the transition matrices between the variables are given by

$$
\begin{array}{c|cc}
p(y|x) & y=0 & y=1 \\\ \hline
x=0 & 0.8 & 0.2 \\\
x=1 & 0.1 & 0.9
\end{array} \quad\quad \text{and} \quad\quad
\begin{array}{c|cc}
p(z|y) & z=0 & z=1 \\\ \hline
y=0 & 0.25 & 0.75 \\\
y=1 & 0.95 & 0.05
\end{array}
$$

and that the marginal distribution for $X$ is given by

$$
\begin{array}{c|c}
x & p(x) \\\ \hline
0 & 0.99 \\\
1 & 0.01
\end{array}
$$

Before beginning, think about what the probabilities in these tables mean! For example, the conditional probability $p(y=1\mid x=1) = 0.9$ says that if the subject has the disease, then the probability is $0.9$ that the test is positive.

Except in parts (c) and (f), all your answers in this problem will be tables of probabilities like those above. You do _not_ need to show me any intermediate computations. I strongly recommend that you use appropriate methods from Python for each part (except (c)) to cut down on the number of tedious computations that you need to do. (In fact, it's possible to complete this entire problem having done _no_ computations by hand!)

**(a)**: Compute the joint mass function $p(x,y)$.

**(b)**: Compute the marginal mass function $p(y)$.

**(c)**: Show that $p(x,y,z) = p(y|x)p(z|y)p(x)$. (_Hint_: Remember, $X$ and $Z$ are conditionally independent given $Y$.)

**(d)**: Using your answer to (c), compute the joint mass function $p(x,z)$. (_Hint_: You can do this in one line of code in Python by leveraging the [`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html) method in NumPy. Can you discover how?)

**(e)**: Using your answer to (d), compute the marginal mass function $p(z)$.

**(f)**: Compute the mutual information $I(X,Y)$ and $I(X,Z)$ and confirm that the data processing inequality holds.
