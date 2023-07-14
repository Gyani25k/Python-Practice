# You are given an array arr(0-based indexing). The size of the array is given by n. 
# You need to get the element at index i and return it. 
# If no element exists at i then return -1.

def getByIndex(arr,n,idx):
    if idx < n:
        return arr[idx]
    else:
        return -1

# Input:
# n = =6
# arr[] = {1 2 3 4 5 6}
# index = 0
# Output: 1