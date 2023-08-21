'''
IMPLEMENT A BINARY SEARCH

'''
# METHOD 1

def binarysearch(arr,start,end,x):
    mid=(start+end)//2
    if arr[mid]==x:
        temp = f"Element Present at index {mid}"
        return temp
    elif arr[mid]>x:
        return binarysearch(arr,start,mid-1,x)
    else:
        return binarysearch(arr,mid+1,end,x)
        
arr=[1,2,3,4,5,6]
start=0
end=5
x=4

res=binarysearch(arr,start,end,x)
print(res)

# METHOD 2

def binarysearch1(arr,start,end,k):
    mid=(start+end)//2
    if arr[mid]==k:
        return mid
    elif arr[mid]>k:
        end=mid-1
        return mid
    elif arr[mid]<k:
        start=mid+1
        return mid
    else:
        return -1
    
arr=[1,2,3,4,5,6]
start=0
end=5
k=4

res1=binarysearch1(arr,start,end,k)
print(res1)


