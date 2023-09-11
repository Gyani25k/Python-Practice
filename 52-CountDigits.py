"""
Given a number N. Count the number of digits in N which evenly divides N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 

Example 1:

Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly

"""

class Solution:
    def evenlyDivides (self, N):
        sumX = 0
        for i in str(N):
            if int(i) == 0 or N % int(i) != 0:
                pass
            else:
                sumX += 1
        return sumX