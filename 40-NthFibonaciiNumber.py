'''

The nthFibonacci function takes an integer n as input.

It checks if n is less than or equal to 0. If n is 0 or negative, the function returns 0 because there's no Fibonacci number for non-positive indices.

It then checks if n is 1. If n is 1, the function returns 1 because the first Fibonacci number is 1.

A list named fib is created with a length of n + 1. This list will store the Fibonacci numbers modulo 1000000007.

The first element of the fib list, fib[0], is initialized to 0, and the second element, fib[1], is initialized to 1.

A loop runs from index 2 to n, inclusive. In this loop, the Fibonacci numbers are calculated iteratively using the formula: fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007.

The calculated Fibonacci number is stored in the fib list at the current index, and the modulo operation with 1000000007 is performed to keep the number within the required range.

Finally, the function returns the nth Fibonacci number, which is stored in fib[n].

'''

def Nthfibonacii(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    
    fib = [0]*(n+1)
    fib[1]=1

    for i in range(2,n+1):
        fib[i]=(fib[i-1]+fib[i-2])%1000000007

        return fib[n]
    
n=10
res=Nthfibonacii(n)
print(res)

