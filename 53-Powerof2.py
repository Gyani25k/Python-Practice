"""
Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some integer x.

Example 1:

Input: 
N = 8
Output: 
YES
Explanation:
8 is equal to 2 raised to 3 (23 = 8).

"""

class Solution:
    def isPowerofTwo(self,n):
        P=0
        while(P>=0):
            x=2**P
            if x == n:
                return "YES"
            elif x>n:
                break
            P=P+1