# Solutions for suggested problems for [Section 10.2]()

## Problem 1 ([problem statement](./10-2-suggested-problems.md#problem-1-solution))

For legibility, we will omit all parameters from the probability functions. By definition, we have

$$
p(y^{(1)},\ldots,y^{(m)} \mid \mathbf{x}^{(1)},\ldots,\mathbf{x}^{(m)}) = \frac{p(\mathbf{x}^{(1)},y^{(1)},\ldots,\mathbf{x}^{(m)},y^{(m)})}{p(\mathbf{x}^{(1)},\ldots,\mathbf{x}^{(m)})}.
$$

By the Mass/Density Criteria for Independence (see [Section 7.9](https://mml.johnmyersmath.com/stats-book/chapters/07-random-vectors.html#independence) in the book), we have

$$
p(\mathbf{x}^{(1)},y^{(1)},\ldots,\mathbf{x}^{(m)},y^{(m)}) = \prod_{i=1}^m p( \mathbf{x}^{(i)},y^{(i)}).
$$

But the random vectors $\mathbf{X}^{(i)}$ are independent as well (see [this](https://mml.johnmyersmath.com/stats-book/chapters/07-random-vectors.html#invar-independent-thm) theorem and its corollary), and hence

$$
p(\mathbf{x}^{(1)},\ldots,\mathbf{x}^{(m)}) = \prod_{i=1}^m p(\mathbf{x}^{(i)}).
$$

Then

$$
p(y^{(1)},\ldots,y^{(m)} \mid \mathbf{x}^{(1)},\ldots,\mathbf{x}^{(m)}) = \frac{\prod_{i=1}^m p( \mathbf{x}^{(i)},y^{(i)})}{\prod_{i=1}^m p(\mathbf{x}^{(i)})} = \prod_{i=1}^m \frac{p( \mathbf{x}^{(i)},y^{(i)})}{p(\mathbf{x}^{(i)})} = \prod_{i=1}^m p(y^{(i)} \mid \mathbf{x}^{(i)}),
$$

as desired.