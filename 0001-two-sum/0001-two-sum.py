class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap={}
        for i , n in enumerate(nums):
            differ = target - n 
            if differ in premap:
                return [premap[differ],i]
            premap [ n] =i
        return