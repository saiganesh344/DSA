class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[write -1]:
                nums[write] = nums[j]
                write = write + 1
        return write
        