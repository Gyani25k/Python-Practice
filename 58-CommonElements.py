
"""
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.

"""

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        set_a=set(A)
        set_b=set(B)
        set_c=set(C)
        combination_a_b=set_a.intersection(set_b)
        combinatio_a_b_c=combination_a_b.intersection(set_c)
        ans=list(combinatio_a_b_c)
        ans.sort()
        if len(ans)==0:
            ans.append(-1)
        return ans