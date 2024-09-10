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

### Problem 02 - Data Storage/Retrieval
