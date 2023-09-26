"""
Given two arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the kth position of the final sorted array.
 

Example 1:

Input:
arr1[] = {2, 3, 6, 7, 9}
arr2[] = {1, 4, 8, 10}
k = 5
Output:
6
Explanation:
The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.

"""

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        res = []
        start = 0
        end = 0
        while start < n and end < m:
            if arr1[start] < arr2[end]:
                res.append(arr1[start])
                start = start + 1
            else:
                res.append(arr2[end])
                end = end + 1
    
        while start < n:
            res.append(arr1[start])
            start = start + 1
    
        while end < m:
            res.append(arr2[end])
            end = end + 1
        
        ans=res[k-1]
    
        return ans