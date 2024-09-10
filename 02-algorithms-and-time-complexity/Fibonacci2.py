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

if __name__== '__main__':
    print("O(1) Time:", [fibonacci(i) for i in range(0, 1001, 200)])
