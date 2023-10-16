"""
Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

 

Example 1:

Input:
n = 5
nums[] = {10, 3, 5, 6, 2}
Output:
180 600 360 300 900
Explanation: 
For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.


"""


class Solution:
    def productExceptSelf(self, nums, n):
        
        prod_arr = [1 for i in range(n)]
        
        temp = 1
        
        for i in range(n):
            prod_arr[i] *= temp
            temp *= arr[i]
            
        temp = 1
        
        for i in range(n-1, -1, -1):
            prod_arr[i] *= temp
            temp *= arr[i]
            
        return prod_arr