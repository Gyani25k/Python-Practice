# Given an unsorted array arr[] of size N containing non-negative integers. 
# You will also be given an integer X, the task is to count the number of elements which are strictly greater than X. 
# The given integer may or not be present in the array given.

class Solution:
    def greaterThanX(self,arr,n,x):
        count=0
        for num in arr:
            if num>x:
                count += 1
        return count
