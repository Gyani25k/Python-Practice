# Solution 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
      
        return len(nums)

# Solution 2

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
          nums.remove(val)
          
        return len(nums)
