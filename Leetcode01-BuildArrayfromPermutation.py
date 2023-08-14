
def Buildarray(nums):
    n=len(nums)
    ans=[]
    for i in range(0,n+1):
        ans.append(nums[nums[i]])

    return ans

nums=[1,2,3,4,5,6]
res=Buildarray(nums)
print(res)