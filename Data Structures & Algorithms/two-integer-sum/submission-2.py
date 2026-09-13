class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            value = target - n 
            for l in range(i+1,len(nums)):
                if nums[l] == value: 
                    return [i,l]
        
        
        