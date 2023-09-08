# METHOD 1

class Solution:
    def getPairsCount(self, arr, n, k):
        freq_map = {}  
        ans = 0
        
        for num in arr:
            complement = k - num  
            
            if complement in freq_map:
                ans += freq_map[complement] 
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        return ans

# METHOD 2

def getpairs(arr,k):
    ans=0
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if (arr[i]+arr[j]==k):
                ans+=1
    return ans

