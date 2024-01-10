"""
Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.

Example 1:

Input:
N = 5
Output: 1 1 2 3 5

"""

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        l= []
        a, b = 1, 1
        
        for _ in range(n):
            l.append(a)
            a, b = b, a + b
        
        return l