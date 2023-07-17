# Given an integer N. Find the number of digits that appear in its factorial. 
# Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1

# Method 1 
# This method not good for numbers like 8000,8468

def factorial(N):     
        if N == 0 or N == 1: 
            res=1
            return res
        else:
            res=N * factorial(N - 1) 
            return res
x=factorial(12)
print(f"The Factorial of Above Number is {x}")
result=0
while x !=0:
    result=result+1
    x=x//10
print(f"The Number of digits in the given Number is {result}")

# Method 2 Using Log
import math
class Solution:
    def digitsInFactorial(self, N):
        if N < 0:
            return 0
        if N == 0 or N == 1:
            return 1
        log_factorial = 0
        for num in range(2, N + 1):
            log_factorial += math.log10(num)
            print(log_factorial)
        num_digits = int(log_factorial) + 1
        return num_digits
    
solution_obj = Solution()
N = 10
num_digits = solution_obj.digitsInFactorial(N)
    

