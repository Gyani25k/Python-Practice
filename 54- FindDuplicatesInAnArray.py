"""
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: 
-1
Explanation: 
There is no repeating element in the array. Therefore output is -1.

"""

class Solution:
    def duplicates(self, arr, n): 
        unique_set = set()
        duplicates = set() 
    
        for num in arr:
            if num in unique_set:
                duplicates.add(num)  
            else:
                unique_set.add(num)
    
        duplicates = sorted(duplicates) 
        return duplicates if duplicates else [-1]