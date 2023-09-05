'''
arr=[2,1,3,4]
In bubble sort we check and compare first two elements 2 and 1 and if they are sorted we will pass if not we will swap these elements.
We will repeat till we get all the element in sorted

'''



def bubblesort(arr):
    n=len(arr)-1
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[2,1,3,4,5,6]
result=bubblesort(arr)
print(result)