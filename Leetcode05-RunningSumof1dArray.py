
def runningSum(nums):
    n=len(nums)
    sum=0
    ans=[]
    for i in range(len(nums)):
        sum+=nums[i]
        ans.append(sum)
    return ans

nums=[1,1,1,1,1]
res=runningSum(nums)
print(res)