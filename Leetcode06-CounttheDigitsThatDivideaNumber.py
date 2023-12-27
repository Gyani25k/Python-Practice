'''
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

 

Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

'''

class Solution:
    def countDigits(self, num: int) -> int:
        nums=str(num)
        digits=0
        for i in nums:
            i=int(i)
            if num%i==0:
                digits+=1
        return digits