# O(n) Time
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

# O(1) Time
a = (1 + (5**(0.5)) )/2
b = (1 - (5**(0.5)) )/2
AB = [ a**n - b**n for n in range(1001)]

def fibonacci_O1Time(n):
    global AB
    Fn = AB[n] // ( 5**(0.5) )
    return int(Fn)

# Version 2
b_n = [ b**n for n in range(1001)]
Beta_n = [0]*1001
for i in range(1,1001):
    Beta_n[i] = (a*Beta_n[i-1]) + (b_n[i-1]*(5**(0.5)))

def fibonacci_O1Time_v2(n):
    global Beta_n, b_n
    Fn = Beta_n[n] // (5**(0.5))
    return int(Fn)

def fibonacci(n, type=None):
    match type:
        case 'nT1S':
            return iterative_fibonacci_O1Space(n)
        case 'nTnS':
            return iterative_fibonacci_OnSpace(n)
        case '1T':
            return fibonacci_O1Time(n)
        case '1T2':
            return fibonacci_O1Time_v2(n)
        case _:
            return iterative_fibonacci_O1Space(n)

if __name__== '__main__':
    TestNValues = range(0, 1001, 250)
    TestLists = {
        'O(n) with O(1) Space': [fibonacci(n, 'nT1S') for n in TestNValues],
        'O(n) with O(n) Space': [fibonacci(n, 'nTnS') for n in TestNValues],
        'O(1) with O(1) Space': [fibonacci(n, '1T') for n in TestNValues],
        'O(1) with O(1) Space 2': [fibonacci(n, '1T2') for n in TestNValues]
    }
    for (key, val) in TestLists.items():
        print(f'{key}: {val}')

     # Calculate the differences for both V1 and V2
    diffs_v1 = [TestLists['O(1) with O(1) Space'][i] - TestLists['O(n) with O(1) Space'][i] for i in range(len(TestNValues))]
    diffs_v2 = [TestLists['O(1) with O(1) Space 2'][i] - TestLists['O(n) with O(1) Space'][i] for i in range(len(TestNValues))]

    # Print the differences (optional)
    print(f'V1 - Error: {diffs_v1}')
    print(f'V2 - Error: {diffs_v2}')