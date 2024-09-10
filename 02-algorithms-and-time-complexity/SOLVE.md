<!-- @format -->

# FazendaTech - Programming Challenge

## 02 - Algorithms and Time Complexity - Solving the problems from [README.md](README.md)

### Problem 01 - Fibonacci Sequence + Time Complexity

1. Come up with an `O(n)` time complexity implementation of the Fibonacci Sequence. Bonus points for a solution that has `O(1)` space complexity, and another that has `O(n)` space complexity.

To solve this in O(n) time complexity I did a iteration over the sequence and returned the N solution. To solve this in O(n) space complexity I did a list with all values of fibonacci values from 1 to N.

```python
def iterative_fibonacci_OnSpace(n):
    if n <= 1: return n

    F = [1]*n
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]
```

The O(1) space complexity uses just 2 variables F(n) and F(n-1) that I call F(before).

```python
def iterative_fibonacci_O1Space(n):
    if n <= 1: return n

    Fbefore, Fn = 0, 1
    for i in range(1,n):
        Fbefore, Fn = Fn, Fbefore + Fn
    return Fn
```

2. Come up with an `O(1)` time complexity implementation of the Fibonacci Sequence for `n <= 1000`. Bonus points for including both an approximate\* solution, and an exact solution.

Starting of $F(n) = F(n-1) + F(n-2)$, $F(0) = 0$ and $F(1) = 1$ respectively, I will asume that $F(n)$ is equivalent to $\alpha^n$, so

$
\alpha^n = \alpha^{n-1} + \alpha^{n-2}\\
\alpha^n - \alpha^{n-1} - \alpha^{n-2} = 0\\
\dfrac{\alpha^n}{\alpha^{n-2}} - \dfrac{\alpha^{n-1}}{\alpha^{n-2}} - \dfrac{\alpha^{n-2}}{\alpha^{n-2}} = 0\\
\alpha^{n-n+2} - \alpha^{n-1-n+2} - 1 = 0\\
\alpha^2 - \alpha^1 -1 =0
$

This is a Bhaskara situation, so:

$
\Delta = (-1)^2 - 4 \cdot 1 \cdot (-1)\\
\Delta = 1 + 4 = 5\\
\longrightarrow \alpha = \dfrac{-(-1) \pm \sqrt{5}}{2}
\therefore \alpha = \frac{1\pm\sqrt{5}}{2}
$

Now, I can assume that

$
F(n) = F(n-1) + F(n-2)\\
\therefore
F(n) = C_1\alpha_1^n + C_2\alpha_2^n\\
F(n) = C_1\left[\frac{1+\sqrt{5}}{2}\right]^n + C_2\left[\frac{1-\sqrt{5}}{2}\right]^n
$

As we know $F(0) = 0$, so

$F(0) = 0 = C_1\alpha_1^0+C_2\alpha_2^0 = C_1 + C_2\\
\therefore C_1 = -C_2\\
\therefore F(n) = C_1\left( \left[\frac{1+\sqrt{5}}{2}\right]^n - \left[\frac{1-\sqrt{5}}{2}\right]^n\right)\\
F(n) = C_1\left( \dfrac{[1+\sqrt{5}]^n - [1-\sqrt{5}]^n}{2^n}\right)
$

And we know $F(1) = 1$, so

$
F(1) = 1 = C_1\left[\frac{1+\sqrt{5}}{2}\right] + C_2\left[\frac{1-\sqrt{5}}{2}\right]\\
1 = C_1\left[\frac{1+\sqrt{5}}{2}\right] - C_1\left[\frac{1-\sqrt{5}}{2}\right]\\
\dfrac{1}{C_1} = \left[\frac{1+\sqrt{5}}{2}\right] - \left[\frac{1-\sqrt{5}}{2}\right]\\
\dfrac{1}{C_1} = \left[\dfrac{1+\sqrt{5}-1+\sqrt{5}}{2}\right] = \dfrac{2\sqrt{5}}{2} = \sqrt{5}\\
\therefore
C_1 = \dfrac{1}{\sqrt{5}} \nonumber
$

$
F(n) = C_1\left( \dfrac{[1+\sqrt{5}]^n - [1-\sqrt{5}]^n}{2^n}\right)\\
F(n) = \left(\dfrac{1}{\sqrt{5}}\right)\cdot\left( \dfrac{[1+\sqrt{5}]^n - [1-\sqrt{5}]^n}{2^n}\right)\\
\therefore\left\{
\begin{align}
a &= \frac{1 + \sqrt{5}}{2} \nonumber\\
b &= \frac{1 - \sqrt{5}}{2}\nonumber\\
F(n) &= \dfrac{1}{\sqrt{5}} \cdot \left[a^n - b^n\right]\nonumber\\
\end{align}
\right.
$

For computing, this will be hard, so lets simplify:

$
\beta_n =  a^n - b^n \\
\beta_n = a\cdot a^{n-1} - b\cdot b^{n-1}\\
\beta_n = a\cdot(a^{n-1} - b^{n-1}) + b^{n-1}\cdot(a-b)\\
\beta_n = a\cdot\beta_{n-1} + b^{n-1}\cdot (a-b)\\
$

$
\therefore \left\{ \begin{align}
a =& \frac{1 + \sqrt{5}}{2} \nonumber\\ b =& \frac{1 - \sqrt{5}}{2} \nonumber\\
\beta_n =& a\cdot\beta_{n-1} + b^{n-1}\cdot \sqrt5 &&\nonumber\\
F(n) =& \dfrac{1}{\sqrt{5}} \cdot \beta_n && \nonumber \end{align} \right.
$

In this form, I can make a list for $\beta_n$ and $b^n$, because the square root of the function is hard to give exact values for bit positions, but the function can be used.

```python
sqrt5 = 5**(0.5)
a = (1+sqrt5)/2
b = (1-sqrt5)/2
bN = [1]*1001
BetaN = [0] + [a-b]*1000
for i in range(1, 1001):
    bN[i] = bN[i-1] * b
    BetaN[i] = (a * BetaN[i-1]) + (bN[i-1]*sqrt5)

def fibonacci(n):
    global BetaN
    return int(BetaN[n] // sqrt5)
```

### Problem 02 - Data Storage/Retrieval
