**Suggested problems for Chapter [11](https://mml.johnmyersmath.com/stats-book/chapters/models.html).** ([Solutions](./x-suggested-problems-sol.md))

---

**Problem 1**: Use the following code to import some data into a Colab notebook.

```python
import pandas as pd

url = 'https://raw.githubusercontent.com/jmyers7/stats-book-materials/main/data/ch11-suggested-problems-data-01.csv'
df = pd.read_csv(url)
```

Using the implementation of linear regression in Scikit-Learn, fit a cubic polynomial to this data. (_Hint_: Fit the model with the original column of $x$-values, along with columns for $x^2$ and $x^3$.) Can you determine the cubic polynomial that I used to generate the data?

---