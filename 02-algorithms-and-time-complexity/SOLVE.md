<!-- @format -->

# FazendaTech - Programming Challenge

## 02 - Algorithms and Time Complexity - Solving the problems from [README.md](README.md)

### Problem 01 - Fibonacci Sequence + Time Complexity

1. Come up with an `O(n)` time complexity implementation of the Fibonacci Sequence. Bonus points for a solution that has `O(1)` space complexity, and another that has `O(n)` space complexity.

To solve this in O(n) time complexity I did a iteration over the sequence and returned the N solution. To solve this in O(n) space complexity I did a list with all values of fibonacci values from 1 to N.

```python
def fibonacci(n):
    if n <= 1: return n

    F = [1]*n
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]
```

The O(1) space complexity uses just 2 variables F(n) and F(n-1) that I call F(before).

```python
def fibonacci(n):
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

With this, I can make the following code:

```python
a = (1 + (5**(0.5)) )/2
b = (1 - (5**(0.5)) )/2
AB = [ a**n - b**n for n in range(1001)]

def fibonacci(n):
    global AB
    Fn = AB[n] // ( 5**(0.5) )
    return int(Fn)
```

For computing, the float numbers make it hard, the values will not be exact, so i tried to make another function:

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

In this form, I can make a list for $\beta_n$ and $b^n$ using the last position.

```python
a = (1 + (5**(0.5)) )/2
b = (1 - (5**(0.5)) )/2

b_n = [ b**n for n in range(1001)]
Beta_n = [0]*1001
for i in range(1,1001):
    Beta_n[i] = (a*Beta_n[i-1]) + (b_n[i-1]*(5**(0.5)))

def fibonacci(n):
	global Beta_n, b_n
    Fn = Beta_n[n] // (5**(0.5))
    return int(Fn)
```

This second version is equivalent, but the results are more accurate. The pyhon file [Fibonacci.py](Fibonacci.py) can be used to test and see the results.

### Problem 02 - Data Storage/Retrieval

1. Implement a function that receives a string and returns the output as described above.

```ts
function CountCharacters(str: string): string {
	const charMap = new Map<string, { firstChar: string; count: number }>();

	for (const char of str) {
		const lowerChar = char.toLowerCase();
		if (charMap.has(lowerChar)) {
			charMap.get(lowerChar)!.count++;
		} else {
			charMap.set(lowerChar, { firstChar: char, count: 1 });
		}
	}

	let result = "Key | FirstChar | Count\n";
	result += "------------------------\n";
	for (const [key, value] of charMap.entries()) {
		result += `${key}  |     ${value.firstChar}     | ${value.count}\n`;
	}

	return result;
}
```

2. What is the time complexity of your implementation?

The time complexity depends on the loop used and the complexity of the operations performed with the Map structure. Since it is necessary to iterate through all the characters, the loop's complexity is O(n), so the algorithm is at least O(n). However, the operations with the Map need to be analyzed. Typically, Maps are structures that use a hash table, and after some research, I found that in JavaScript, they work similarly, allowing get and set operations to be approximately O(1). Regarding the has operation, I couldn't find specific information about its complexity, but considering that get and set operations require identifying where the key is, checking whether a key exists can also be approximated to O(1). Since the operations inside the loop are O(1), I can assert that the loop itself is O(n). To build the output string, it's necessary to go through all the objects in the map, which in the worst case is O(n) if the input string contains all unique characters. Therefore, the overall complexity of the implemented function is O(n) because it only depends on the size of the input.

3. Is this complexity optimal? If yes, why? If not, how would you improve it?

Yes, it is optimal because it would be impossible to do this without passing through the input at least once. So, O(n) is the best complexity for this function.
