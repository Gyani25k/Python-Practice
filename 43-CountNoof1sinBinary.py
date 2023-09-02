
'''
METHOD 1
'''
class Solution:
    ##Complete this code
    def firstoccurrence(self,arr,N):
        low=0
        high=N-1
        x=1
        while (low<=high):
            mid=(low+high)//2
            if arr[mid]<x:
                low=mid+1
            elif arr[mid]>1:
                high=mid-1
            else:
                if mid==0 or arr[mid]!=arr[mid+1]:
                    return mid
                else:
                    high=mid+1
        return -1
                
    def countOnes(self,arr, N):
        #Your code here
        first=self.firstoccurrence(arr,N)
        if first==-1:
            return 0
        else:
            return N-first
        
# METHOD 2

def count(l,N):
    count=0
    for i in l:
        if i==1:
            count+=1
    return count

l=[0,0,0,1,1,1]
N=len(l)
res=count(l,N)
print(res)

