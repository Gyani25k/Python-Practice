
'''

Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).

Example 1:

Input:
N = 7, x = 0 
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less 
than 0 is found. So output 
is "-1".

'''


def floorsorted(l,x):
    start=0
    end=len(l)-x
    while(start<=end):
        mid=(start+end)//2
        if l[mid]>x:
            end=mid-1
        elif l[mid]<x:
            start=mid+1
        else:
            return mid
    return end

