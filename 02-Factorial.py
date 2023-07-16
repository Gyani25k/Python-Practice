# Given a positive integer N. The task is to find factorial of N.


class Solution:
    def factorial(self, N):
        if N == 0 or N == 1: 
            return 1
        else:
            return N * self.factorial(N - 1) 
    
solution = Solution()

# Calculate the factorial of 5
result = solution.factorial(5)
print(result)  

# Output: 120


