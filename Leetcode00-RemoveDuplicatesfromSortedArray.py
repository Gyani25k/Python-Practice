'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

'''



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set()
        i = 0
        while i < len(nums):
            if nums[i] in unique_set:
                nums.pop(i)
            else:
                unique_set.add(nums[i])
                i += 1
        return len(nums)
    