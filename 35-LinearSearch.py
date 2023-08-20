'''
Program to implement Linear search

'''

def linearsearch(arr,n):
    if n in arr:
        idx=arr.index(n)
        temp=f"Element {n} present at index {idx}"
        return temp
    else:
        temp = "Element Not Found"
        return temp
    
arr=[2,1,3,7,4,9,10]
n=10
print(linearsearch(arr,n))
