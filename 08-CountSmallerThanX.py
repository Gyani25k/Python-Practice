# Given an unsorted array arr[] of size N containing non-negative integers. 
# You will also be given an integer X, the task is to count the number of elements which are strictly smaller than X. 
# The given integer may or not be present in the array given.

def smallerThanX(self,arr,n,x):
    sum=0
    for i in arr:
        if i<x:
            sum+=1
    return sum 

# Time Complexity is O(N)