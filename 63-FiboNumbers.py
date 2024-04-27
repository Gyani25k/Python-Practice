from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def fibonacciSeries(n):
    sum_result = 0 
    if n == 1:
        return 1 
    elif n == 2:
        return 1 
    else:
        sum_result += (fibonacciSeries(n-1)+fibonacciSeries(n-2))
        return sum_result


n = int(input())
result  = fibonacciSeries(n)
print(result)


def fibonacciSeries(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacciSeries(n-1, memo) + fibonacciSeries(n-2, memo)
        memo[n] = result
        return result

n = int(input())
result = fibonacciSeries(n)
print(result)
