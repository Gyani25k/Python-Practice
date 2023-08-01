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


# NEW METHOD WITH FOR LOOP

def factorial1(N):
    if N==0 and N==1:
        return 1
    result=1
    for i in range(2,N+1):
        result=result*i
    return result


result1 = factorial1(6)
print(result1) 