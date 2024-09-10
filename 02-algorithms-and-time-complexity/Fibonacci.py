def iterative_fibonacci_OnSpace(n):
    if n <= 1: return n

    F = [1]*n
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]

def iterative_fibonacci_O1Space(n):
    if n <= 1: return n

    Fbefore, Fn = 0, 1
    for i in range(1,n):
        Fbefore, Fn = Fn, Fbefore + Fn
    return Fn

if __name__== '__main__':
    print("O(1) Space:", [iterative_fibonacci_O1Space(i) for i in range(0, 1001, 200)])
    print("O(n) Space:", [iterative_fibonacci_OnSpace(i) for i in range(0, 1001, 200)])