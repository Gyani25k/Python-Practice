'''
FACTORIAL AND FIBONACII SERIES

'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))


def fibonacii(n):
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)
    
print(fibonacii(6))