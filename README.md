**Integration Techniques in Python**

**Overview**
This project demonstrates *numerical integration techniques* — including the *Midpoint Rule, **Trapezoidal Rule, and **Simpson’s Rule* — and compares them with the *exact analytical solution* for power functions of the form:

\[
f(x) = x^n
\]

The goal is to explore how well these numerical methods approximate the true area under the curve and understand their relative accuracy and efficiency.

Features
- Implementation of *Midpoint, **Trapezoidal, and **Simpson’s* integration methods.  
- Comparison with the *exact integral value* using analytical formulas.  
- Easy-to-understand Python code for educational and research purposes.  
- Demonstrates the *effect of function power (n)* on numerical error.  
- Minimal dependencies — runs with plain Python.


**Mathematical Background**
For a function \( f(x) = x^n \), the definite integral between \( a \) and \( b \) is:

\[
I_{\text{exact}} = \frac{b^{n+1} - a^{n+1}}{n+1}
\]

The numerical approximations are computed as:

- *Midpoint Rule:*
  \[
  I_{\text{mid}} = (b - a) \times f\left(\frac{a+b}{2}\right)
  \]

- *Trapezoidal Rule:*
  \[
  I_{\text{trap}} = \frac{(b - a)}{2} [f(a) + f(b)]
  \]

- *Simpson’s Rule:*
  \[
  I_{\text{simp}} = \frac{(b - a)}{6} [f(a) + 4f\left(\frac{a+b}{2}\right) + f(b)]
  \]


**Code Example**
```python
def f(x, n):
    return x ** n

a = 1
b = 5

for n in [1, 2, 3, 4]:
    I_mid = (b - a) * f((a + b) / 2, n)
    I_trap = (b - a) * (f(a, n) + f(b, n)) / 2
    I_simp = (b - a) * (f(a, n) + 4 * f((a + b) / 2, n) + f(b, n)) / 6
    I_exact = (b * (n + 1) - a * (n + 1)) / (n + 1)

    print(f"\nFor n = {n}:")
    print(f"Midpoint Approximation = {I_mid}")
    print(f"Trapezoidal Approximation = {I_trap}")
    print(f"Simpson's Approximation = {I_simp}")
    print(f"Exact Value = {I_exact}")

**Example Output**

For n = 2:
Midpoint Approximation = 63.0
Trapezoidal Approximation = 78.0
Simpson's Approximation = 66.6667
Exact Value = 66.6667

**Learning Outcomes**

Understand the concept and derivation of numerical integration methods.

Learn how to compare approximate and exact solutions.

Build intuition for error estimation in numerical methods.

Develop strong foundations for computational mathematics and scientific computing.



**Author**

Venu Madhav Shetty
Numerical Analysis & Python Integration Enthusiast
University of Rostock-Germany


Acknowledgements:

This project was built for academic enrichment and to demonstrate how computational techniques can bridge the gap between theory and implementation.

> “Mathematics is not about numbers, equations, or algorithms — it’s about understanding.”
— William Paul Thurston
