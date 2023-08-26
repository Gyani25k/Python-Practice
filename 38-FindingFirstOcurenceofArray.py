
'''
Given a sorted array of integers of size N and a number X. 
Find the leftmost index of X in the array arr[].

'''

# METHOD 1 USING ITERATIVE METHOD

def leftIndex( N, arr, X):
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < X:
            low = mid + 1
        elif arr[mid] > X:
            high = mid - 1 
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1
    
    return -1

l = [0, 0, 0, 1, 1, 1, 1]
res1 = leftIndex(7,l,1)
print(res1)

# METHOD 2 NAIVE METHOD

def firstoccurence(arr,n,x):
    for i in range (0,n):
        if i in arr:
            return i
        
    return -1 

